# Getting started

## Requirements

- [Python 3](https://www.python.org/).
- [uv](https://docs.astral.sh/uv/) (for installing Python dependencies from `pyproject.toml`).
- [Jupyter](https://jupyter.org/) (for verification plots).
- Fortran compiler ([gfortran](https://gcc.gnu.org/fortran/)), installed separately.
- [MkDocs](https://www.mkdocs.org/) and [mkdocs-material](https://squidfunk.github.io/mkdocs-material/) (for the documentation site).
- [Ford](https://forddocs.readthedocs.io/en/stable/) (optional, for the Fortran API reference).

## Environment setup

```bash
uv venv
source .venv/bin/activate
uv sync
```

## Install gfortran

macOS (Homebrew):

```bash
brew install gcc
```

Linux (Debian/Ubuntu):

```bash
sudo apt-get install gfortran
```

Linux (Fedora):

```bash
sudo dnf install gcc-gfortran
```

## Run everything

```bash
./runall
```

This builds the Fortran executable, runs the predefined calculations for both
implementations, generates plots, and builds the Ford API reference.

Clean outputs:

```bash
./runall clean
./runall clobber
```

## Run Python only

```bash
python3 python/src/imc.py -i python/calcs/calc1.in -o calc1_output.dat
```

## Run Fortran only

```bash
make -C fortran/src
./fortran/src/imc.exe -i fortran/calcs/calc1.in -o calc1_output.dat
```

## Input files

Inputs are keyword/value pairs, case-insensitive. Example:

```text
DT 2.e-11
XSIZE 4.0
DX 0.4
CYCLES 150
NS 1000
GAMMA 27.0
SCATTERFRAC 0.944
T_POWER 0
T_INIT 0.001
```

Example inputs live under `python/calcs` and `fortran/calcs`. The default
`fcimc.in` filename is supported but not provided in the repo.


## Documentation site

Preview the docs locally:

```bash
uv run mkdocs serve -f mkdocs/mkdocs.yml
```
