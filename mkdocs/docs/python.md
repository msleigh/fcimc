# Python implementation

## Overview

The Python version mirrors the Fortran layout. Each phase of the timestep is
implemented in its own module and shared state lives in `imc_global_*`
modules.

## Entry point

`python/src/imc.py` parses CLI arguments, seeds the RNG, reads input, builds the
mesh, and calls `imc_opcon.run`.

## Key modules

- `imc_mesh.py` - mesh construction and initialization.
- `imc_update.py` - update temperature dependent properties and Fleck factor.
- `imc_source.py` - source particle creation and sampling.
- `imc_track.py` - particle transport and energy deposition.
- `imc_tally.py` - update mesh temperatures.

## Calculations and figures

`python/calcs/Makefile` runs the input decks and generates figures that
reproduce the paper results.
