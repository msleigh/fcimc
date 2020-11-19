fcimc
=====

A Python implementation of Fleck and Cummings's implicit Monte Carlo (IMC) scheme, as published in Journal of Computational Physics (JCP) in 1971.

<img src="https://img.shields.io/github/v/release/msleigh/fcimc?include_prereleases"> <img src="https://img.shields.io/github/license/msleigh/fcimc"> <img src="https://img.shields.io/tokei/lines/github/msleigh/fcimc"> <img src="https://img.shields.io/github/last-commit/msleigh/fcimc"> <img src="https://img.shields.io/badge/code%20style-black-lightgrey">

## Dependencies

### Python version

- Python 3 (<3.8, see note 1)
- Numpy

### Fortran version

- GFortran

### Bundled calculations

- Matplotlib (to plot the figures)
- Jupyter (to open the verification notebook)

### Documentation

- Doxygen
- Graphviz
- Doxypypy (requires Python<3.8, see note 1)

### Notes

1. The requirement for Python < 3.8 is due to a bug in Doxypypy; see
   [https://github.com/Feneric/doxypypy/issues/70]. If documentation is not required
   then this limit can be ignored.

## Installation

To create a Conda env with the necessary Python packages:

    conda env create -n <env-name> -f environment.yml
    conda activate <env-name>

To install the non-Python dependencies on macOS:

    brew install gfortran
    brew install doxygen
    brew install graphviz

## Usage

### Execution

To build and run everythina from scratch, run the top-level script:

    ./runall

To see the aggregated output:

    jupyter notebook verification.ipynb

To open the documentation:

    open docs/html/index.html

### Cleaning

To clean up intermediiate build files etc.:

    ./runall clean

and to clean out everything (output files, executables, etc.) for a fresh start:

    ./runall clobber

### Fine control

Each part of the project has its own `Makefile` which can be invoked directly:

    ./fortran/src/Makefile
    ./fortran/calcs/Makefile
    ./python/calcs/Makefile
    ./docs/Makefile

to either clean up one part, e.g.:

    make -C fortran/src clean
    make -C docs clobber

or build/execute, e.g.:

    make -C python/calcs -j 4 all
    make -C docs html


