fcimc
=====

Python and Fortran implementations of Fleck and Cummings's implicit Monte Carlo
(IMC) scheme, published in Journal of Computational Physics (JCP) in 1971.

![Release](https://img.shields.io/github/v/release/msleigh/fcimc?include_prereleases)
![License](https://img.shields.io/github/license/msleigh/fcimc)
![Last commit](https://img.shields.io/github/last-commit/msleigh/fcimc)
![Code style: black](https://img.shields.io/badge/code%20style-black-lightgrey)
![Build status (`main`)](https://github.com/msleigh/fcimc/actions/workflows/build.yml/badge.svg?branch=main)

For each implementation, the results from the published paper (Fleck and
Cummings 1971) are reproduced via a set of predefined runs included in the
repository.

<table>
  <tr>
    <th>Fleck and Cummings (1971)</th>
    <th>Fortran implementation</th>
    <th>Python implementation</th>
  <tr>
    <td><img src="images/figures/reference/fig2.png" style="width: 100%; max-width: 340px; height: auto;"></td>
    <td><img src="images/figures/fortran/fig2.png" style="width: 100%; max-width: 220px; height: auto;"></td>
    <td><img src="images/figures/python/fig2.png" style="width: 100%; max-width: 220px; height: auto;"></td>
  </tr>
  <tr>
    <td><img src="images/figures/reference/fig3.png" style="width: 100%; max-width: 340px; height: auto;"></td>
    <td><img src="images/figures/fortran/fig3.png" style="width: 100%; max-width: 220px; height: auto;"></td>
    <td><img src="images/figures/python/fig3.png" style="width: 100%; max-width: 220px; height: auto;"></td>
  </tr>
  <tr>
    <td><img src="images/figures/reference/fig4.png" style="width: 100%; max-width: 340px; height: auto;"></td>
    <td><img src="images/figures/fortran/fig4.png" style="width: 100%; max-width: 220px; height: auto;"></td>
    <td><img src="images/figures/python/fig4.png" style="width: 100%; max-width: 220px; height: auto;"></td>
  </tr>
  <tr>
    <td><img src="images/figures/reference/fig5.png" style="width: 100%; max-width: 340px; height: auto;"></td>
    <td><img src="images/figures/fortran/fig5.png" style="width: 100%; max-width: 220px; height: auto;"></td>
    <td><img src="images/figures/python/fig5.png" style="width: 100%; max-width: 220px; height: auto;"></td>
  </tr>
  <tr>
    <td><img src="images/figures/reference/fig6.png" style="width: 100%; max-width: 340px; height: auto;"></td>
    <td><img src="images/figures/fortran/fig6.png" style="width: 100%; max-width: 220px; height: auto;"></td>
    <td><img src="images/figures/python/fig6.png" style="width: 100%; max-width: 220px; height: auto;"></td>
  </tr>
</table>

## Dependencies

### Python implementation

- Python 3
- Numpy

### Fortran implementation

- GFortran (installed separately; see Installation)

### Bundled calculations

- Matplotlib
- Jupyter

### Documentation

## Installation

Install Python dependencies with uv (from `pyproject.toml`):

    uv venv
    source .venv/bin/activate
    uv sync

To install GFortran:

macOS (Homebrew):

    brew install gcc

Linux (Debian/Ubuntu):

    sudo apt-get install gfortran

Linux (Fedora):

    sudo dnf install gcc-gfortran

## Usage

### Execution

To build and run everything from scratch, run the top-level script:

    ./runall clobber  # Removes latest graphs
    ./runall

To see the aggregated output:

    jupyter notebook verification.ipynb

To open the documentation:

    open site/index.html

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

Building the documentation is a special case:

    make -C docs html

This builds the MkDocs site into `site/` and embeds the Ford API reference at
`site/doc/`.

To preview the documentation locally:

    uv run mkdocs serve

## Verification

Run the Jupyer notebook to plot the results:

    jupyter notebook verification.ipynb

Verification against the original Fleck and Cummings (1971) results (shown on the left)
of both a Fortran (middle) and a Python (right) implementation of the IMC scheme
described therein.
