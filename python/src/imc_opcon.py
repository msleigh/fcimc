"""Control of main numerical calculation."""

import pickle
# import matplotlib.pyplot as plt

import imc_update
import imc_source
import imc_tally
import imc_track

import imc_global_io_data as io
import imc_global_mesh_data as mesh
import imc_global_phys_data as phys
import imc_global_time_data as time


def run():
    """
    Control calculation for fcimc.

    Timestep loop is within this function.
    """
    # Set plot times
    plottimes = [6.0, 15.0, 90.0]
    plottimenext = 0

    # Open output file
    fname = open(io.output_file, "wb")

    # Set an initial temperature field
    mesh.temp[:] = mesh.temp0[:]  # keV

    # Loop over timesteps

    time.time = 0.0

    for time.step in range(0, time.ns):

        print("\n" + "=" * 79)
        print("Timestep  {:4d}".format(time.step))
        print("Time (s)  {:24.16E}".format(time.time))
        print("Time (cm) {:24.16E}".format(time.time * phys.c))
        print("=" * 79)

        # Update temperature-dependent quantities
        imc_update.run()

        # Source new particles
        imc_source.run()

        # Track new particles through the mesh
        imc_track.run()
        imc_track.clean()

        # Tally
        imc_tally.run()

        # Energy check
        #

        # Update time
        time.time = time.time + time.dt

        # Plot
        if plottimenext <= 2:
            if (time.time * phys.c + 1.0e-06) >= plottimes[plottimenext]:
                print("Plotting {:6d}".format(plottimenext))
                print("at target time {:24.16f}".format(plottimes[plottimenext]))
                print("at actual time {:24.16f}".format(time.time * phys.c))
                # plt.plot(mesh.cellpos, mesh.temp, "b-o")
                fname.write("Time = {:24.16f}\n".format(time.time * phys.c).encode())
                pickle.dump(mesh.cellpos, fname, 0)
                pickle.dump(mesh.temp, fname, 0)
                plottimenext = plottimenext + 1

    # Close file
    fname.close()

    # Plot
    # plt.show()
