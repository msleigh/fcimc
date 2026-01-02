# Verification workflow

The repository includes predefined calculations that reproduce the results in
Fleck and Cummings (1971).

## Run the verification suite

```bash
./runall
```

This:

- runs the Python and Fortran input decks in `python/calcs` and
  `fortran/calcs`,
- generates the comparison figures, and
- diffs the outputs against the known good data.

## Plotting

Open the Jupyter notebook to view the combined results:

```bash
jupyter notebook verification.ipynb
```

## Output files

Each run writes an output file with three snapshots (times 6, 15, 90 in units
of `time * c`). For each snapshot the file contains:

1. `Time = <value>` line,
2. cell center positions, and
3. mesh temperatures.
