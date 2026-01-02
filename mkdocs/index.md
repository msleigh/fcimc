# fcimc

fcimc provides Python and Fortran implementations of the Fleck and Cummings
(1971) implicit Monte Carlo (IMC) method for 1D slab radiation transport.
This site is the entry point for the repository and covers build, usage, and
implementation notes for both versions.

## Repository layout

- `python/src` - Python implementation.
- `fortran/src` - Fortran implementation.
- `python/calcs` and `fortran/calcs` - reproduction runs and figure scripts.
- `ford.md` and `docs/` - Ford configuration and pages for the Fortran API docs.

## Where to start

- [Getting started](getting-started.md)
- [Python implementation](python.md)
- [Fortran implementation](fortran.md)
- [Verification workflow](verification.md)

## Fortran API reference

The detailed Fortran API reference is generated separately with Ford and is
written to `doc/` by default. See the Fortran page for build steps and a link.
