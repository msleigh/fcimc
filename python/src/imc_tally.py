"""Tally end-of-timestep quantities."""

import numpy as np

import imc_global_mat_data as mat
import imc_global_mesh_data as mesh
import imc_global_phys_data as phys
import imc_global_time_data as time


def run():
    """Tally end-of-timestep quantities."""
    print("\n" + "-" * 79)
    print("Tally step ({:4d})".format(time.step))
    print("-" * 79)

    # Start-of-step radiation energy density
    radnrgdens = np.zeros(mesh.ncells)
    radnrgdens[:] = phys.a * mesh.temp[:] ** 4

    # Temperature increase
    nrg_inc = np.zeros(mesh.ncells)
    nrg_inc[:] = (
        mesh.nrgdep[:] / mesh.dx
        - mesh.fleck[:] * phys.c * time.dt * mesh.sigma_p[:] * radnrgdens[:]
    )

    mesh.temp[:] = mesh.temp[:] + nrg_inc[:] / mat.bee

    print("\nMesh temperature:")
    print(mesh.temp)
