# fcimc

fcimc provides Python and Fortran implementations of the Fleck and Cummings
(1971) implicit Monte Carlo (IMC) method for 1D slab radiation transport.
This site is the entry point for the repository and covers build, usage, and
implementation notes for both versions.

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
- [Theory](theory.md)

## Fortran API reference

The detailed Fortran API reference is generated separately with Ford and is
written to `doc/` by default. See the Fortran page for build steps and a link.
