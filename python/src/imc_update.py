"""Update at start of time-step."""

import math

import imc_global_phys_data as phys
import imc_global_mat_data as mat
import imc_global_mesh_data as mesh
import imc_global_time_data as time
import imc_global_bcon_data as bcon


# Update  of a time-step


def run():
    """Update temperature-dependent quantities at start of time-step."""
    print("\n" + "-" * 79)
    print("Update step ({:4d})".format(time.step))
    print("-" * 79)

    # Calculate Planck mean opacity for the mesh
    # ------------------------------------------

    # In general do this every time-step because sigma can be temperature-dependent
    # There is a factor gamma missing that is problem-dependent (assumed = 1 here)

    mesh.sigma_p[:] = phys.x15pi4 * mat.gamma * mesh.temp[:] ** -3

    print("\nPlanck mean opacity (Fleck & Cummings 1971 Eqn 4.7)")
    print(
        8.0
        * phys.pi
        * mat.gamma
        / (phys.c ** 3 * phys.h ** 3 * phys.a * mesh.temp[:] ** 3)
    )
    print("Planck mean opacity (Wollaber 2008 Eqn 2.21)")
    print(mesh.sigma_p[:])
    print("...These should match...")
    print("...These should decrease as T^3...")

    # Calculate beta for the mesh
    # ---------------------------

    mesh.beta[:] = 4.0 * phys.a * (mesh.temp[:] ** 3.0) / mat.bee

    print("\nBeta (non-linearity factor) (Fleck & Cummings 1971 Eqn 1.6)")
    print(mesh.beta)
    print("...This should increase as T^3...")

    # Fleck
    # -----

    mesh.fleck[:] = 1.0 / (1.0 + mesh.beta[:] * phys.c * time.dt * mesh.sigma_p[:])

    print("\nFleck factor (Fleck & Cummings 1971 Eqn 4.1d)")
    print(mesh.fleck)
    print("...This should be constant (for a given timestep length)...")
    print(
        "...This should equal {:10.8f}...".format(
            1.0
            / (
                1.0
                + (32.0 * phys.pi * mat.gamma / (phys.c ** 3 * phys.h ** 3 * mat.bee))
                * phys.c
                * time.dt
            )
        )
    )
    print("\nSlab thickness       = {:6.3f} cm".format(mesh.xsize))
    print("Boundary source temp = {:6.3f} keV".format(bcon.T0))
    print("Material gamma/D     = {:6.3f}".format(mat.gamma))
    print(
        "Sigma at nu = 3 keV  = {:6.3f} cm^-1".format(
            mat.gamma * (1.0 - math.exp(-3.0 / 0.001)) / (3.0 ** 3)
        )
    )
    print("Spatial step         = {:6.3f}".format(mesh.dx))
    print("Time step            = {:6.3f} sh".format(time.dt / 1.0e-08))
    print("\nInitial temperature (keV):")
    print(mesh.temp0)
    print("\nScattering fraction (%):")
    print(100.0 * (1 - mesh.fleck[:]))
