# Fortran API reference

This is the API reference for the Fortran implementation of the Fleck and
Cummings (1971) implicit Monte Carlo (IMC) scheme. It is intended to document
code structure and data flow rather than provide user-facing project guidance.
See `README.md` for the main project documentation.

## Build and run

Build the Fortran executable:

```bash
make -C fortran/src
```

Run with default input/output files:

```bash
./fortran/src/imc.exe
```

CLI options (from `fortran/src/imc.f90`):

- `-i, --input` input file (default `fcimc.in`)
- `-o, --output` output file (default `fcimc.out`)
- `-h, --help` usage message
- `-d, --debug` reserved flag, currently unused

## Program flow

The top-level program is in `fortran/src/imc.f90` and follows this sequence:

1. Parse CLI options and seed the random number generator.
2. Read user input and echo it.
3. Allocate particle state arrays and initialize them.
4. Build the mesh (`imc_mesh_make`).
5. Execute the timestep loop (`imc_opcon`).

Within each timestep, `imc_opcon` calls:

1. `imc_update` to update temperature-dependent material properties.
2. `imc_source` to create new source particles.
3. `imc_track` to transport particles and deposit energy.
4. `imc_tally` to update mesh temperatures.

## Input file format

The input reader in `fortran/src/imc_user_input.f90` accepts keyword/value
pairs. Keywords are case-insensitive and lines are tokenized on whitespace.
Recognized keys:

- `dt` time step size.
- `xsize` total slab width (cm).
- `dx` spatial cell width (cm). The code rounds `xsize / dx` up to compute
  `ncells` and then recomputes `dx` from `xsize / ncells`.
- `cycles` number of time steps (`ns`).
- `ns` number of source particles per timestep (`n_input`).
- `gamma` material opacity parameter (problem-dependent).
- `scatterfrac` requested scattering fraction, used to compute `bee`.
- `t_power` exponent used in the frequency-dependent opacity.
- `t_init` initial temperature (keV).

All other tokens are ignored.

## Output format

The output file written by `imc_opcon` contains snapshots at the three target
times used in the paper: 6, 15, and 90 (in units of `time * c`). For each
snapshot the file contains:

1. A line `Time = <value>` (cm).
2. A line of cell-center positions (`cellpos`).
3. A line of mesh temperatures (`temp`).

## Modules and global data

Global data is stored in modules under `fortran/src/imc_global_*.f90`:

- `imc_global_phys_data`: physical constants (`c`, `h`, `sb`, `a`, etc.).
- `imc_global_mesh_data`: mesh geometry and per-cell arrays (`dx`, `temp`,
  `sigma_p`, `fleck`, `nrgdep`, etc.).
- `imc_global_time_data`: time stepping (`dt`, `time`, `step`, `ns`).
- `imc_global_mat_data`: material parameters (`gamma`, `bee`, `tpower`, `tmp0`).
- `imc_global_bcon_data`: boundary condition data (`t0`).
- `imc_global_part_data`: particle census and state arrays (`xpos`, `mu`,
  `frq`, `nrg`, `t`, `dead`, `icell`, `origin`, etc.).

Particle arrays are sized by `n_max` and use `dead` plus the `inext` index as a
free-list mechanism for new particles.

## Core routines

- `imc_mesh_make` (`fortran/src/imc_mesh.f90`): allocate mesh arrays, compute
  cell and node positions, and initialize fields.
- `imc_update` (`fortran/src/imc_update.f90`): compute Planck mean opacity,
  non-linearity factor (`beta`), and the Fleck factor for the current timestep.
- `imc_source` (`fortran/src/imc_source.f90`): compute energy sources, emission
  probabilities, particle counts, and instantiate source particles.
- `imc_track` (`fortran/src/imc_track.f90`): transport particles, apply
  pseudo-scattering, deposit energy into `nrgdep`, and update census counts.
- `imc_tally` (`fortran/src/imc_tally.f90`): update mesh temperatures from
  deposited energy and print per-step diagnostics.
- `imc_opcon` (`fortran/src/imc_opcon.f90`): orchestrate the timestep loop and
  write plot snapshots to the output file.

## Utility routines

`fortran/src/imc_utils.f90` provides:

- `imc_get_free_lun` for finding a free Fortran I/O unit.
- `init_random_seed` to seed the RNG deterministically or from the clock.
- `samplePlanckspectrum` to draw from a Planck spectrum for emission frequency.

## Units and conventions

- Temperatures are in keV and energies are in keV.
- Distances are in cm and times are in seconds; plots use `time * c` (cm).
- `mu` is the cosine of the direction angle for 1D slab transport.

## Notes for extension

- The code relies on global modules rather than derived types; changes to data
  layout should be coordinated across all subroutines that `use` those modules.
- `imc_track` assumes 1D slab geometry and uses `nodepos` for boundary crossing.
- `imc_opcon` writes only three plot times; adjust `plottimes` to add outputs.
