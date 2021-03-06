fcimc
=====

A Python implementation of Fleck and Cummings's implicit Monte Carlo (IMC) scheme,
published in Journal of Computational Physics (JCP) in 1971.

<img src="https://img.shields.io/github/v/release/msleigh/fcimc?include_prereleases"> <img src="https://img.shields.io/github/license/msleigh/fcimc"> <img src="https://img.shields.io/tokei/lines/github/msleigh/fcimc"> <img src="https://img.shields.io/github/last-commit/msleigh/fcimc"> <img src="https://img.shields.io/badge/code%20style-black-lightgrey">

![Build status (`main`)](https://github.com/msleigh/fcimc/actions/workflows/build.yml/badge.svg?branch=main)

Both a Python and a Fortran implementation are included; in each, the results from the
published paper (Fleck and Cummings 1971) are reproduced via a set of predefined runs
included in the repository.

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
- LaTeX

### Installation

To create a Conda env with the necessary Python dependencies:

    conda env create -f environment.yml
    conda activate fcimc

To install the non-Python dependencies on macOS:

    brew install gfortran
    brew install doxygen
    brew install graphviz

### Notes

1. The requirement for Python < 3.8 is due to a bug in Doxypypy; see
   https://github.com/Feneric/doxypypy/issues/70. If documentation is not required
   then this limit can be ignored.

## Usage

### Execution

To build and run everything from scratch, run the top-level script:

    ./runall

To see the aggregated output:

    jupyter notebook verification.ipynb

To open the documentation:

    open docs/html/index.html

### Cleaning

To clean up intermediate build files etc.:

    ./runall clean

and to clean out everything (output files, executables, etc.) for a clean start:

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

## Verification of FCIMC

Verification against the original Fleck and Cummings (1971) results (shown on the left)
of both a Fortran (middle) and a Python (right) implementation of the IMC scheme
described therein.

<table>
<tr><td><img src="fig2.png" width="700"></td><td><img src="fortran/calcs/fig2.png"></td><td><img src="python/calcs/fig2.png"></td></tr>
<tr><td><img src="fig3.png" width="700"></td><td><img src="fortran/calcs/fig3.png"></td><td><img src="python/calcs/fig3.png"></td></tr>
<tr><td><img src="fig4.png" width="700"></td><td><img src="fortran/calcs/fig4.png"></td><td><img src="python/calcs/fig4.png"></td></tr>
<tr><td><img src="fig5.png" width="700"></td><td><img src="fortran/calcs/fig5.png"></td><td><img src="python/calcs/fig5.png"></td></tr>
<tr><td><img src="fig6.png" width="700"></td><td><img src="fortran/calcs/fig6.png"></td><td><img src="python/calcs/fig6.png"></td></tr>
</table>

