"""Read user input deck."""

from math import ceil

import imc_global_mesh_data as mesh
import imc_global_mat_data as mat
import imc_global_part_data as part
import imc_global_phys_data as phys
import imc_global_time_data as time


def read(input_file):
    """
    @brief   Reads input deck.

    @details Reads input deck with user-specified problem-specific
             information.
    @param   input_file  Name of input file
    @return  None
    """
    with open(input_file, "r") as input_file:
        for line in input_file:

            # Ignore blank lines
            if line == "":
                continue

            fields = line.split(None, 1)

            if len(fields) != 2:
                continue

            keyw = fields[0].lower()
            keyv = fields[1]

            if keyw == "dt":
                time.dt = float(keyv)

            elif keyw == "xsize":
                mesh.xsize = float(keyv)

            elif keyw == "dx":
                # Round up the number of cells if not an integer, then if
                # necessary adjust dx for the rounded up number of cells
                mesh.ncells = int(ceil(mesh.xsize / float(keyv)))
                mesh.dx = mesh.xsize / float(mesh.ncells)

            elif keyw == "cycles":
                time.ns = int(keyv)

            elif keyw == "ns":
                part.n_input = int(keyv)

            elif keyw == "gamma":
                mat.gamma = float(keyv)

            elif keyw == "scatterfrac":
                f_reqd = 1.0 - float(keyv)
                mat.bee = (
                    4.0
                    * phys.x15pi4
                    * phys.a
                    * phys.c
                    * f_reqd
                    * mat.gamma
                    * time.dt
                    / (1.0 - f_reqd)
                )

            elif keyw == "t_power":
                mat.tpower = float(keyv)

            elif keyw == "t_init":
                mat.tmp0 = float(keyv)

            else:
                continue


def echo():
    """Echoes user input."""
    print("\n" + "=" * 79)
    print("User input")
    print("=" * 79)

    print()
    print("mesh.ncells  {:5d}".format(mesh.ncells))
    print("mesh.xsize   {:5.1f}".format(mesh.xsize))

    print("mat.gamma    {:5.1f}".format(mat.gamma))
    print("mat.bee      {:24.16E}".format(mat.bee))
    print("mat.tpower   {:5.1f}".format(mat.tpower))
    print("mat.tmp0     {:5.1f}".format(mat.tmp0))

    print("time.dt      {:5.1f}".format(time.dt))
    print("time.ns      {:5d}".format(time.ns))

    print("part.n_input {:5d}".format(part.n_input))
    print("part.n_max   {:5d}".format(part.n_max))
