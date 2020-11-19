"""Advance IMC particles over a time-step."""

import math
import random

import imc_global_mat_data as mat
import imc_global_mesh_data as mesh
import imc_global_part_data as ptcl
import imc_global_phys_data as phys
import imc_global_time_data as time


def run():
    """Advance IMC particles over a time-step."""
    print("\n" + "-" * 79)
    print("Tracking step ({:4d})".format(time.step))
    print("-" * 79)

    # Create local storage for the energy deposited this timestep
    mesh.nrgdep[:] = 0.0

    ptcl.n_census = 0

    endsteptime = time.time + time.dt

    # Optimisations (avoid dot operator, saves 20% off cProfiled calc1
    exp = math.exp
    log = math.log
    ran = random.random
    nrgdep = [0.0] * mesh.ncells
    aaa = mat.gamma * phys.invh3 / mesh.temp[:] ** mat.tpower
    phys_h = -phys.h
    mesh_temp = mesh.temp
    mesh_fleck = -mesh.fleck
    mesh_nodepos = mesh.nodepos
    phys_c = phys.c
    top_cell = mesh.ncells - 1
    phys_invc = phys.invc
    bbb = phys.invh * mesh_temp

    print("\nParticle loop...")

    # Loop over all particles
    for iptcl in range(len(ptcl.prop)):

        # Get particle's initial properties at start of timestep
        (ttt, icell, xpos, muu, frq, nrg, startnrg) = ptcl.prop[iptcl][1:8]
        startnrg = 0.01 * startnrg

        # Loop over segments in the history (between boundary-crossings and collisions)
        while True:

            # Calculate the total macroscopic cross-section (cm^-1)
            sigma = (
                aaa[icell]
                * (1.0 - exp(phys_h * frq / mesh_temp[icell]))
                / (frq * frq * frq)
            )

            flecksig = mesh_fleck[icell] * sigma

            # Distance to boundary
            if muu > 0.0:
                dist_b = (mesh_nodepos[icell + 1] - xpos) / muu
            else:
                dist_b = (mesh_nodepos[icell] - xpos) / muu

            # Distance to collision
            dist_col = abs(log(ran())) / (sigma + flecksig)

            # Distance to census
            dist_cen = phys_c * (endsteptime - ttt)

            # Actual distance - whichever happens first
            dist = min(dist_b, dist_col, dist_cen)

            # Calculate the new energy and the energy deposited (temp storage)
            newnrg = nrg * exp(flecksig * dist)
            if newnrg <= startnrg:
                newnrg = 0.0

            # Deposit the particle's energy
            nrgdep[icell] += nrg - newnrg

            if newnrg == 0.0:
                # Flag particle for later destruction
                ptcl.prop[iptcl][6] = -1.0
                break

            # If the event was a boundary-crossing, and the boundary is the
            # domain boundary, then kill the particle
            if dist == dist_b:
                if muu > 0:
                    if icell == top_cell:
                        # Flag particle for later destruction
                        ptcl.prop[iptcl][6] = -1.0
                        break
                    icell += 1
                if muu < 0:
                    if icell == 0:
                        # Flag particle for later destruction
                        ptcl.prop[iptcl][6] = -1.0
                        break
                    icell -= 1

            # Otherwise, advance the position, time and energy
            xpos += muu * dist
            ttt += dist * phys_invc
            nrg = newnrg

            # If the event was census, finish this history
            if dist == dist_cen:
                # Finished with this particle
                # Update the particle's properties in the list
                # Starting energy comes in here but doesn't change
                ptcl.prop[iptcl][1:7] = (ttt, icell, xpos, muu, frq, nrg)
                ptcl.n_census += 1
                break

            # If event was collision, also update frequency and direction
            if dist == dist_col:
                # Collision (i.e. absorption, but treated as pseudo-scattering)
                frq = bbb[icell] * abs(log(ran()))
                muu = 1.0 - 2.0 * ran()

        # End loop over history segments

    # End loop over particles

    mesh.nrgdep[:] = nrgdep[:]


def clean():
    """Tidy up the particle list by removing leaked and absorbed particles."""
    # These had their energy set to -1 to flag them
    for iptcl in range(len(ptcl.prop) - 1, 0, -1):
        if ptcl.prop[iptcl][6] < 0.0:
            del ptcl.prop[iptcl]

    print("\nNumber of particles in the system = {:16d}".format(len(ptcl.prop)))
