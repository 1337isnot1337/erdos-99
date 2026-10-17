# Target C — Robinson-kernel localization frontier

**LEVEL I STATUS: STILL OPEN.**

Full proof: [target_c_robinson_kernel_localization_2026-08-31.md](../../reports/target_c_robinson_kernel_localization_2026-08-31.md).

## C55 — equality modes are piecewise affine in diameter direction

For a two-dimensional selected KKT stress, order positive diameter edges by projective direction and use the C53 scaled edge defect `M` with

`M>=0`, `M1=0`, `Mt=0`,

where `t_0<...<t_(m-1)` are the edge slopes.

Pass to consecutive differences with first-difference matrix `D` and cumulative inverse `T`. Put

`C=D Gamma^(-1) D^T`,

`G=T^T M T`,

`H=D Gamma^(-1) M T = C G`.

Then `C>0`, `G>=0`, and `H` is a singular Z-matrix. The positive vector `Dt` is a right nullvector; `C^(-1)Dt` is a positive left nullvector. Scaling columns by `Dt` gives a finite directed Laplacian with positive stationary mass on every state, so its condensation graph has no edges. The irreducible components of `H` are therefore independent blocks.

The Robinson formulas make those blocks contiguous intervals of consecutive direction gaps.

For a scalar edge-space kernel vector `x`,

`Mx=0`

is equivalent to

`x_(i+1)-x_i = c_a (t_(i+1)-t_i)`

on each block `I_a`. Thus every scalar kernel function is piecewise affine in projective diameter slope.

## C55.2 — nonconstant angular rate needs a singleton block

For a tangential diameter velocity in the full stress kernel,

`v_a-v_b = omega_i J u_i`

on edge `i`. With Euclidean axes chosen so `u_i=a_i(1,t_i)`, the two scalar normalized edge-difference sequences are

`omega_i`

and

`t_i omega_i`

up to sign. Both lie in `ker M`.

On a Robinson block containing at least two consecutive gaps, `omega` is affine in `t` and `t omega` is also affine in `t` at at least three distinct slope samples. Hence the quadratic coefficient vanishes and `omega` is constant on that whole block.

Therefore any genuine diameter shear requires an irreducible component consisting of a single direction gap `{i}`.

## C55.3 — isolated gaps are two-edge electrical hinges

At a singleton gap all off-diagonal entries of row `i` in the difference-space Z-matrix vanish. Since each Kalmanson interval split contributes a nonpositive amount to those entries, equality is termwise.

Consequently, for every positive circular interval split vector `z` with

`z_i != z_(i+1)`,

all other edge coordinates vanish:

`supp z subset {i,i+1}`.

So the response can distinguish the two adjacent diameter directions only through splits that see no other positive diameter edge.

## Exact next target

Exclude or finitely integrate this two-edge electrical hinge in the actual connected triangle-free positive unit-contact network. A successful theorem can proceed by either:

- converting the isolated split pattern into a forbidden one- or two-vertex terminal separator; or
- showing the corresponding sector is an actual hinge motion, so its differential angular shear integrates to a same-diameter weak-contact release.

No quantitative conductance lower bound is needed. This is an exact zero-pattern problem.
