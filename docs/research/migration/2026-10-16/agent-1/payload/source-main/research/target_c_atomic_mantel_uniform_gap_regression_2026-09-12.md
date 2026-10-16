# Target C — regression: endpoint nonattainment does not automatically give a uniform atomic-mass gap

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Status:** hostile regression; the attempted all-regime compactness corollary was deleted in commit `4d0729b9`.

The robust near-complete-grid theorem on this branch proves that a single Type-II train-measure limit cannot satisfy

\[
x\sigma=2\sqrt{\Delta_2},
\]

because equality forces one Mantel-saturated `pi/3` orbit and hence a forbidden near-complete train grid.

It is tempting to infer a universal constant `eta>0` with

\[
x\sigma\ge2\sqrt{\Delta_2}+\eta
\]

for every Type-II limit by compactness. That inference is not justified by weak compactness alone.

The obstruction is that total atomic mass is not upper-semicontinuous under weak convergence. Diffuse measures can concentrate into an atom; for example, normalized Lebesgue measure on an interval of width `1/j` has atomic mass zero for every `j` but converges weakly to a Dirac mass of atomic mass one. Conversely, atomic mass can also disappear when many small atoms spread out.

Therefore a sequence of Type-II limiting measures with `x_j sigma_j downarrow 2sqrt(Delta_2)` need not admit a diagonal weak limit whose atomic mass is at most the limiting `sigma_j`. The compactness step in the retracted corollary was invalid.

A genuine all-regime positive gap would require a finite quantitative version of the robust-grid theorem, phrased directly in terms of train counts in fixed/shrinking phase windows and crossing deficits. Endpoint nonattainment itself remains valid because its equality hypotheses already identify a specific limiting measure and do not pass atomic mass through a second weak limit.

**Disposition:** route correction. The zero-detour endpoint exclusion remains live; the attempted universal `eta_grid` corollary is rejected.