"""Sets up mesh."""

import numpy as np

import imc_global_mesh_data as mesh
import imc_global_mat_data as mat


def make():
    """
    @brief   Sets up mesh.

    @details Sets up fixed spatial mesh.
    @param   None
    @return  None

    Mesh creation
    =============

    The overall problem size and number of mesh cells are specified as user
    input, and the cell size ($dx$) is calculated from these.

    Arrays of both the cell-centre and the cell-edge (node) positions are
    created.

    Cell-centred arrays for temperature, initial temperature, opacity, beta
    factor, Fleck factor, and total energy deposited, are initialised.
    """
    # Create cell data as a 2D array (with first dimension = 1)
    # to facilitate use of matplotlib.pyplot.pcolor
    # mesh.cells = np.zeros((1, mesh.ncells + 1))
    # mesh.cells[0, 0:mesh.ncells + 1] = np.linspace(0., mesh.xsize, mesh.ncells + 1)

    mesh.dx = mesh.xsize / float(mesh.ncells)

    mesh.cellpos = np.arange(0.5 * mesh.dx, mesh.xsize, mesh.dx)
    mesh.nodepos = np.linspace(0.0, mesh.xsize, mesh.ncells + 1)

    # Create empty arrays for the mesh-based physical quantities

    mesh.temp = np.zeros(mesh.ncells) - 1.0  # Temperature (keV)
    mesh.temp0 = np.zeros(mesh.ncells) - 1.0  # Initial temperature (keV)
    mesh.sigma_p = np.zeros(mesh.ncells) - 1.0  # Opacity
    mesh.beta = np.zeros(mesh.ncells) - 1.0  # Beta factor
    mesh.fleck = np.zeros(mesh.ncells) - 1.0  # Fleck factor
    mesh.nrgdep = np.zeros(mesh.ncells) - 1.0  # Total energy deposited in timestep

    mesh.temp0[:] = mat.tmp0


def echo():
    """
    @brief   Prints mesh.

    @details Prints out spatial mesh for debugging.
    @param   None
    @return  None
    """
    print("Mesh:")
    print(mesh.ncells, mesh.xsize, dx)
    print(mesh.cellpos)
    print(mesh.nodepos)
