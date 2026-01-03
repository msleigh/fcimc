# Theory

## Overview

Implicit Monte Carlo (IMC) is a Monte Carlo method for solving the thermal
radiation transport equation, published by
[Fleck and Cummings in 1971](https://www.sciencedirect.com/science/article/pii/0021999171900155)
, according to which:

> "The method is based upon the concept of effective scattering, wherein a
> fraction of the radiative energy absorbed is instantaneously and
> isotropically reradiated in a manner analogous to a scattering process."

The modelled particles in IMC are not photons, but represent 'packets' of
photons, whose total energy changes as they interact with the background
material in a way that captures the local energy absorption and radiation
rates.

One benefit of this 'effective scattering' is _variance reduction_. Because
particles are never absorbed, but simply scatter around until they leave the
system (losing energy gradually, to _represent_ absorption), each particle
contributes to the solution over a large area of the problem space. If
particles were absorbed directly in accordance with the material opacities,
they would contribute only locally to the solution, and many more particles
would have to be simulated to get a good, low-variance solution everywhere.

This, however, is possible to achieve in 'standard', as opposed to 'implicit'
Monte Carlo methods. The
defining aspect of IMC is the ability to better treat the non-linear
behaviour of thermal radiation transport, whereby the materials' opacities to
radiation and the emission rates are modified by their temperatures, which are
of course modified in turn by the radiation field. This non-linearity can be
dealt with explicitly, by computing a radiation time-step with constant
temperatures and material properties, and then updating the temperatures and
opacities at the end of the time-step according to the new radiation fluxes.
However, in optically-thick systems, where the radiation field is tightly
coupled with the material, and the material and radiation are in (or close to)
thermal equilibrium, a very short time-step is required that makes the whole
process very inefficient. IMC modifies this process by treating only a
fraction of the total radiation emission term as an explicit source term, fixed
throughout the time-step, and deals with the remainder of the energy emission
by way of the 'effective scattering' mechanism: an effective scattering term
is introduced which represents the absorption and re-emission (isotropically)
of radiation.

To understand this better, consider a computational cell which radiation is entering
from the left side (e.g. a plane Marshak wave advancing through a 1D slab). The
cell has a fixed temperature and therefore fixed opacities and absorption and
emission rates. In a standard Monte Carlo scheme, particles entering from the
left boundary are preferentially absorbed in the left part of the cell
(in optically thick problems the cells are by definition many mean-free-paths
wide). However the emission rate is constant throughout the whole
cell, so in effect the emission process is unphysically decoupled from the
absorption. In Implicit Monte Carlo, a fraction of both the absorption and
emission processes are taken care of through the mechanism of effective
scattering, so are very tightly coupled. Effectively, the IMC method allows,
to a certain extent, sub-grid-scale information about the absorption and
re-emission processes to be accounted for.

## Discretisation of the energy equation

Mathematically, IMC is simply the Monte Carlo solution of a time-dependent
transport equation which has been _implicitly discretised_ in time, which
yields unconditional stability with respect to time-step length, just as an
implicitly-discretised finite-difference scheme is unconditionally stable.
(The implicitly-discretised equations derived by Fleck and Cummings do not,
in fact, need to be solved by the Monte Carlo method to yield this key benefit.)

Consider the basic finite differencing of a simple differential equation

$$ \frac{\partial u}{\partial t} = f{\left(u\right)} $$

An explicit time discretisation is:

$$ u^{n+1} \approx u^n + \Delta t \; f{\left(u^n\right)} $$

and an implicit one is:

$$ u^{n+1} \approx u^n + \Delta t \; f{\left(u^{n+1}\right)} $$

In the implicit scheme, the right-hand-side is evaluated using the
end-of-time-step values (time level \\(n+1\\)), the explicit scheme using the
values from time level \\(n\\). A scheme can also be constructed that mixes the
two:

$$ u^{n+1} \approx u^n + \Delta t \left[
    \alpha            \:    f{\left(u^{n+1}\right)} +
    \left(1 - \alpha\right) f{\left(u^n\right)}
\right] $$

(with which \\(\alpha = 1/2\\) yields the well-known Crank-Nicholson scheme).
Similarly, in IMC, the radiation energy density equation:

$$ \frac{\partial u_r}{\partial t} = \beta \sigma \left( \phi - cu_r \right) $$

is discretised as:

$$ u_r^{n+1} \approx u_r^n + \Delta t
    \hat\beta \hat\sigma \left( \phi^\lambda - c\left[ \alpha u_r^{n+1} + \left(1-\alpha\right)u_r^n
 \right] \right)
$$

The value of \\(u_r\\), the radiation energy density, on the right-hand side
has been replaced with an implicit difference, \\(\alpha u_r^{n+1} +
\left(1-\alpha\right) u_r^n\\). The value of \\(\alpha\\) can be left as a free
parameter, chosen according to the specifics of the problem to be solved.

The other time-dependent quantities on  the RHS are:

- \\(\beta\\), which is a metric of the degree of non-linearity of the problem,
  defined as:
  $$ \beta = \frac{\partial u_r}{\partial u_m} $$
  where \\(u_m\\) is the material energy density;
- \\(\sigma\\), which is the total interaction cross-section (a property of the
  medium and a function of the local temperature); and
- \\(\phi\\), which is the scalar intensity of the radiation:
  $$ \phi{\left(x,t\right)} = \int_{-1}^1{I{\left(x,t,\mu\right)} d\mu } $$
  (We have assumed a 1D system where \\(x\\) is the spatial dimension and
  \\(\mu\\) the direction cosine of the radiation.)

In the discretised equation, \\(\beta\\) and \\(\sigma\\) have been substituted with
values averaged over the time-step, and \\(\phi\\) by a value \\(\phi^\lambda\\),
where the superscript \\(\lambda\\) denotes an as-yet unspecified time centering.

# Discretisation of the transport equation

Similarly, the transport equation:

$$ \frac{1}{c} \frac{\partial I}{\partial t} + \mu \frac{\partial I}{\partial x} + \sigma I = \frac{1}{2}c\sigma u_r $$

is discretised as:

$$ \frac{1}{c} \frac{\partial I}{\partial t} + \mu \frac{\partial I}{\partial x} + \sigma I = \frac{1}{2}c\sigma \left[\alpha u^{n+1}_r + \left(1-\alpha\right) u^n_r\right] $$

If the discretised energy equation is solved for \\(u^{n+1}_r\\), it is then
possible to write an equation for \\(\alpha u^{n+1}_r + \left(1-\alpha\right)u^n_r\\),
which can be substituted into the transport equation. That is:

$$ u_r^{n+1} \approx u_r^n + \Delta t
    \hat\beta \hat\sigma \left( \phi^\lambda - c\left[ \alpha u_r^{n+1} + \left(1-\alpha\right)u_r^n
 \right] \right)
$$

is rearranged to give:

$$ u_r^{n+1} \approx
\left[ \frac{1-\left(1-\alpha\right)\hat\beta c\Delta t\hat\sigma}{1+\alpha\hat\beta c\Delta t\hat\sigma} \right] u^n_r +
\left[ \frac{\hat\beta\hat\sigma\Delta t}{1+\alpha\hat\beta c\Delta t\hat\sigma} \right] \phi^\lambda
$$

which allows us to write:

$$ \alpha u^{n+1}_r + \left(1-\alpha\right) u^n_r =
\frac{\alpha\hat\beta\hat\sigma\Delta t}{1 + \alpha\hat\beta c\Delta t\hat\sigma} \phi^\lambda +
\frac{1}{1 + \alpha\hat\beta c\Delta t\hat\sigma} u^n_r
$$

Substituting this into the transport equation gives:

$$ \frac{1}{c} \frac{\partial I}{\partial t} + \mu \frac{\partial I}{\partial x} + \sigma I
= \frac{1}{2}\sigma
    \left[ \frac{\alpha\hat\beta c\hat\sigma\Delta t}{1 + \alpha\hat\beta c\Delta t\hat\sigma} \phi^\lambda +
\frac{c}{1 + \alpha\hat\beta c\Delta t\hat\sigma} u^n_r\right]
$$

which we can re-write as:

$$ \frac{1}{c} \frac{\partial I}{\partial t} + \mu \frac{\partial I}{\partial x} + \sigma I =
\frac{1}{2} \sigma_s \phi^\lambda +
\frac{1}{2} c\sigma_a u^n_r
$$

where the first term on the right is the equivalent of a scattering term with
cross-section \\(\sigma_s\\) given by:

$$ \sigma_s = \frac{\alpha\hat\beta c\hat\sigma\Delta t}{1 + \alpha\hat\beta c\Delta t\hat\sigma}\sigma $$

and the second term on the right is the 'remaining' source term, where
\\(\sigma_a\\) is the absorption cross-section:

$$ \sigma_a = \frac{1}{1 + \alpha\hat\beta c\Delta t\hat\sigma} \sigma  $$

derived from the fact that \\(\sigma = \sigma_s + \sigma_a\\).

Effectively, a fraction of the original emission term on the RHS as been re-cast
as a scattering term, leaving a modified direct emission term.
