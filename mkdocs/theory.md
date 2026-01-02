# Theory overview

Implicit Monte Carlo (IMC) is a Monte Carlo method for thermal radiation
transport with an implicit time discretization of the material energy
equation. The implicit treatment introduces an effective scattering term that
improves stability and reduces variance in optically thick problems.

The implementation here follows Fleck and Cummings (1971) and reproduces their
Marshak wave results in a 1D slab. For full derivations and the original
problem setup, see:

- https://www.sciencedirect.com/science/article/pii/0021999171900155
