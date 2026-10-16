# Hostile audit — generic H7b orbit-129 force-closure exclusion

**Date:** 2026-09-19  
**Object audited:** `target_c_support7_h7b_orbit129_force_closure_exclusion_2026-09-19.md` and `verify_target_c_support7_h7b_orbit129_force_closure_2026_09_19.py`  
**Scope:** generic interior-ground `H7b`, canonical affine cell 129 only  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

## Verdict

The orbit-129 exclusion survives the checks below. The proof is an outer-relaxation proof: every force-closed physical realization lies in the certified rational polyhedron, while an exact Farkas certificate separates that polyhedron from `z=0` by a positive rational amount. No numerical residual is promoted to a theorem.

The conclusion audited here is only

\[
\boxed{\text{generic H7b canonical orbit 129 is impossible}.}
\]

Together with the previously committed 22-cell endpoint, this leaves 21 generic `C7` cells. It does not address reciprocal-collinearity walls, `H7a`, `H6`, or `H8`.

## 1. The two-gap inequality really extends to the full physical range

The first possible failure point is the extension of the orbit-176 two-gap lemma from `T<pi/3` to

\[
0<T<2\pi/3.
\]

For a physical equilateral force pentagon, the previously established adjacent-turn bounds give

\[
T+A<\pi,
\qquad
T+E<\pi.
\]

Therefore every `z` between `A` and `E` satisfies

\[
0<z+T<\pi,
\qquad
0<z+T/2<\pi.
\]

So in the notation

\[
C=\cos(T/2),\qquad X=\cos(z+T/2),
\]

we have `C>1/2` and the derivative calculation is on one real monotonic branch. The arccos argument is monotone between its two actual endpoint values, both of which are cosines of physical gaps, hence it remains in `[-1,1]` throughout the interval.

The sign factor in the second derivative is

\[
-(4C^2-1)
\left(4CX^2+(4C^2+3)X+4C\right).
\]

On `0<T<2pi/3`,

\[
1/4<C^2<1,
\]

so `4C^2-1>0`. The quadratic has discriminant

\[
16C^4-40C^2+9
=16(C^2-1/4)(C^2-9/4)<0
\]

and positive leading coefficient. It is therefore positive for every real `X`. Thus `f_T''<0` on the whole interval required by the physical pentagon, not merely when `T<pi/3`.

The Jensen step then has the correct direction: `H_T` is increasing and concave, so `H_T^{-1}` is convex and

\[
A+E\ge2H_T^{-1}(\pi-T/2).
\]

Substitution of the symmetric equality case gives

\[
B+D\le
2\left[\pi-\arccos\left(\frac12-\cos(T/2)\right)\right].
\]

The convexity calculation for this upper envelope also remains valid on the full interval because

\[
2c^2-c+2>0
\]

for every real `c`. No orbit-specific hypothesis enters this lemma.

## 2. Secant direction is correct

Write the normalized sharp bound as

\[
M(t)=2\left[1-\frac1\pi\arccos\left(\frac12-\cos(\pi t/2)\right)\right].
\]

The proof establishes `M''(t)>0`. Therefore, on a certified interval `[l,u]`, the secant through exact endpoint values lies above `M`. The verifier uses rational endpoint values `U(l)>=M(l)` and `U(u)>=M(u)` instead. The line through those larger endpoint values is still above the exact secant, hence still a valid upper bound for `M`.

Thus every added row

\[
x_{i,k+2}+x_{i,k+3}
\le
L_{l,u}(x_{i,k})
\]

is a necessary condition for physical force closure whenever the separately certified affine bounds place `x_{i,k}` in `[l,u]`.

The proof uses closed intervals although the physical inequalities are strict. This only enlarges the feasible set and is therefore safe for an impossibility proof. The endpoint values `M(0)=2/3` and `M(2/3)=1` are the continuous limits of the strict physical formula.

## 3. The iterative refinement does not assume its conclusion

Five first-stage secants are added only after exact base-system Farkas certificates establish their argument intervals. Those five valid necessary inequalities then imply, by another exact dual calculation,

\[
\frac{239920913653902889}{692699184098952240}
\le x_{1,4}
\le
\frac{5642257}{9678753}.
\]

The lower endpoint is strictly above `1/3`; the upper endpoint is strictly below `3/5`. Only after that implication is certified does the proof add the sharper `[1/3,3/5]` secant for `(i,k)=(1,4)`. The `[0,1/3]` secant for `(4,1)` already follows from a base-system bound.

So there is no circular use of the refined cuts to justify their own domains.

## 4. The transcendental endpoint checks are one-sided in the safe direction

For a rational proposed upper value `U`, put

\[
q=1-U/2.
\]

On the ranges used here, `0<q<2/3`, and

\[
M(t)\le U
\]

is equivalent to

\[
\cos(q\pi)+\cos(t\pi/2)\ge1/2.
\]

The verifier encloses `pi` using Machin's identity. The tangent calculation is exact:

\[
\tan(4\arctan(1/5)-\arctan(1/239))=1.
\]

The alternating arctangent bounds also place this angle strictly between `0` and `1`, so it lies on the principal tangent branch; hence it equals `pi/4`. This removes the only possible branch ambiguity in the identity.

For every cosine occurrence, the multiplier of `pi` lies in `[0,2/3]`. Replacing `pi` by the rational upper enclosure increases the angle while keeping it below `pi`; cosine therefore decreases. The finite cosine series is then lowered by a remainder larger than the first omitted magnitude. Consequently `cos_lower_multiple` is genuinely a lower bound. A strictly positive sum of those lower bounds proves the required endpoint inequality in the correct direction.

No binary floating-point value enters an accepted endpoint bound.

## 5. Farkas signs and the relaxation variable are correct

The affine system is represented as

\[
Ax\le b,
\qquad
Ex=d.
\]

For minimization, the verifier uses inequality multipliers `lambda<=0` and free equality multipliers `mu`, with

\[
c=A^T\lambda+E^T\mu.
\]

Then every feasible point satisfies

\[
c^Tx
=\lambda^TAx+\mu^TEx
\ge
\lambda^Tb+\mu^Td.
\]

This is the correct lower-bound sign convention. The verifier checks coefficient equality and the rational dual objective exactly.

In the final system each inequality is relaxed to

\[
a_jx-z\le b_j.
\]

A physical point would be feasible with `z=0`. The exact dual proves

\[
z\ge
\frac{30117197506100285749035263}
{444741384479402651773792227324}
>0.
\]

Therefore no `z=0` point exists even in the closed rational outer relaxation. This is stronger than needed to exclude the original strict physical cell.

## 6. Dependency and representative checks

The verifier does not silently inherit the known historical force-cycle dispatch defect. It requires the exact old call site to occur once, patches only that site in memory from `cyc` to `cyc[i]`, and refuses to proceed if the expected historical source shape has changed.

It also asserts the complete canonical orbit-129 representative before constructing the certificate: missing graph, ground slots, and all signed edges. The proof therefore cannot accidentally certify a neighboring orbit after a change in enumeration order without failing the representative assertion.

## 7. What is not proved

This audit does not turn the generic `H7b` branch into a theorem-level closure. Twenty-one generic `C7` cells remain after removing orbit 129. A numerical force-only residual for another cell is not an exclusion until it receives a comparable analytic or validated certificate.

The immediate reusable result is the full-range inequality

\[
\boxed{x_{k+2}+x_{k+3}\le M(x_k),\qquad 0<x_k<2/3,}
\]

which can be applied with adaptive rational secants to every remaining cell. If those outer polyhedra stop separating a cell, the next layer is the complete nonlinear force-closure plus radial sine-cycle system or a validated interval proof. C-II remains open.
