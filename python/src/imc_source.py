"""Source IMC particles."""

import math
import random as ran

import numpy as np

import imc_global_part_data as part
import imc_global_mesh_data as mesh
import imc_global_phys_data as phys
import imc_global_bcon_data as bcon
import imc_global_time_data as time

from imc_utils import sample_planck_spectrum


def imc_get_energy_sources():
    """Get energy source terms for surface and mesh."""
    # Left-hand boundary is a black-body emitter at constant temperature T0
    # (Energy radiatied per unit area = sigma.T0**4 (sigma = S-B constant)
    e_surf = phys.sb * bcon.T0 ** 4 * time.dt

    # Emission source term
    e_body = np.zeros(mesh.ncells)  # Energy emitted per cell per time-step
    e_body[:] = (
        mesh.fleck[:]
        * mesh.sigma_p[:]
        * phys.a
        * phys.c
        * mesh.temp[:] ** 4
        * mesh.dx
        * time.dt
    )

    # Total energy emitted
    e_total = e_surf + sum(e_body[:])

    print("\nEnergy radiated in timestep:")
    print("\nIn total:")
    print("{:24.16E}".format(e_total))
    print("\nBy boundary condition:")
    print("{:24.16E}".format(e_surf))
    print("\nBy mesh:")
    print(e_body)

    return e_surf, e_body, e_total


def imc_get_emission_probabilities(e_surf, e_body, e_total):
    """Convert energy source terms to particle emission probabilities."""
    p_surf = e_surf / e_total
    # Probability of each cell _given that the particle is from the mesh not the
    # surface_
    p_body = np.zeros(mesh.ncells)
    p_body[:] = np.cumsum(e_body[:]) / sum(e_body[:])

    print("\nProbabilities:")
    print("\nIn total")
    print("{:16.8E}".format(p_surf + sum(p_body[:])))
    print("\nOf boundary particle")
    print("{:16.8E}".format(p_surf))
    print("\nOf mesh particle (cumulative)")
    print(p_body[:])

    return p_surf, p_body


def imc_get_source_particle_numbers(p_surf, p_body):
    """Calculate number of source particles to create at surface / throughout mesh."""
    n_census = part.n_census
    n_input = part.n_input
    n_max = part.n_max

    # Determine total number of particles to source this time-step
    n_source = n_input
    if (n_source + n_census) > n_max:
        n_source = n_max - n_census - mesh.ncells - 1

    print("\nSourcing {:8d} particles this timestep".format(n_source))
    print("(User requested {:8d} per timestep)".format(n_input))

    n_surf = 0
    n_body = np.zeros(mesh.ncells, dtype=np.uint64)

    # Calculate the number of particles emitted by the surface souce and each mesh cell
    for _ in range(n_source):
        if ran.random() <= p_surf:
            n_surf += 1
        else:
            eta = ran.random()
            for icell in range(mesh.ncells):
                if eta <= p_body[icell]:
                    n_body[icell] += 1
                    break

    print("\nBody source")
    print(n_body)

    return n_surf, n_body


def imc_source_particles(e_surf, n_surf, e_body, n_body):
    """For known energy distribution (surface and mesh), create source particles."""
    # Create the surface-source particles
    nrg = e_surf / float(n_surf)
    startnrg = nrg
    for _ in range(n_surf):
        origin = -1
        xpos = 0.0
        muu = math.sqrt(ran.random())  # Corresponds to f(mu) = 2mu
        ttt = time.time + ran.random() * time.dt
        frq = bcon.T0 * sample_planck_spectrum() / phys.h
        part.prop.append(
            [origin, ttt, 0, xpos, muu, frq, nrg, startnrg]
        )  # Add this ptcl to the global list

    # Create the body-source particles
    for icell in range(mesh.ncells):
        if n_body[icell] <= 0:
            continue
        nrg = e_body[icell] / float(n_body[icell])
        startnrg = nrg
        for _ in range(n_body[icell]):
            origin = icell
            xpos = mesh.nodepos[icell] + ran.random() * mesh.dx
            muu = 1.0 - 2.0 * ran.random()
            ttt = time.time + ran.random() * time.dt
            frq = mesh.temp[icell] * abs(math.log(ran.random())) / phys.h
            # Add this ptcl to the global list
            part.prop.append([origin, ttt, icell, xpos, muu, frq, nrg, startnrg])


def run():
    """
    Source new IMC particles.

    This routine calculates the energy sources for
    the (a) left-hand boundary (which is currently held at a constant
    temperature, T0), and (b) the computational cells, as well as the overall
    total for the time-step. These are then converted into particle emission
    probabilities. The number of particles to source in this time-step is
    determined (ensuring that the total number in the system does not exceed
    some pre-defined maximum), and then these are attributed either to the
    boundary or to one of the mesh cells, according to the probabilities
    calculated earlier. The particles are then created.
    """
    print("\n" + "-" * 79)
    print("Source step ({:4d})".format(time.step))
    print("-" * 79)

    # Determine probability of particles belonging to sources
    # -------------------------------------------------------

    # Get the energy source terms
    (e_surf, e_body, e_total) = imc_get_energy_sources()

    # Emission probabilities
    (p_surf, p_body) = imc_get_emission_probabilities(e_surf, e_body, e_total)

    # Number of source particles
    (n_surf, n_body) = imc_get_source_particle_numbers(p_surf, p_body)

    # Create the particles
    imc_source_particles(e_surf, n_surf, e_body, n_body)

    # Particle count
    print("Number of particles in the system = {:12d}".format(len(part.prop)))
