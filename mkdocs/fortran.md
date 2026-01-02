# Fortran implementation

## Overview

The Fortran version is the reference implementation and relies on global data
modules for shared state. The top level program is `fortran/src/imc.f90`.

## Build and run

```bash
make -C fortran/src
./fortran/src/imc.exe -i fortran/calcs/calc1.in -o calc1_output.dat
```

## Timestep flow

`imc_opcon` orchestrates the timestep loop and calls, in order:
`imc_update`, `imc_source`, `imc_track`, and `imc_tally`.

## Fortran API reference (Ford)

Generate the API reference with either command:

```bash
make -C docs html
# or
ford ford.md
```

The output is written to `doc/index.html` by default. When you build the
documentation via `make -C docs html`, it is copied into the MkDocs site so the
link below works from the rendered pages:

[Fortran API reference](../doc/index.html)

If you are using `mkdocs serve`, open `doc/index.html` from disk instead.
