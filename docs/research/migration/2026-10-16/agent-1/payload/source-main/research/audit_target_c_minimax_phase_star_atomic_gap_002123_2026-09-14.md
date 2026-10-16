# Independent hostile audit — minimax phase-star atomic gap `0.002123`

**Date:** 2026-09-14  
**Audited candidate:** `target_c_minimax_phase_star_atomic_gap_002123_2026-09-14.md` (`c897ad2d`)  
**Target:** C-II, canonical full-core Type-II branch  
**Disposition:** **PASS at proof-only scope**  
**Theorem-state authority:** unchanged

## LEVEL I STATUS

`STILL OPEN`

The candidate raises the hostile-audited minimax atomic excess from `g=0.0021` to

\[
\boxed{g=0.002123}
\]

without changing the proof architecture. This audit rechecks the only places where a
small numerical refinement could silently reverse an inequality: the dominant-orbit
outward bounds, the one-dimensional center-imbalance interval certificate, the
common-neighbor threshold, and the Section-171 propagation.

All four checks pass with strict rational margins.

## 1. Structural proof is inherited unchanged

The `0.002123` note changes no geometric lemma. It reuses the independently audited
`0.0021` minimax proof:

- dominant-orbit deficit
  \(\delta\le A^2/4-\Delta_2\);
- the three-partite phase-star inequality
  \(C e_{UV}\le Vx+Uy\);
- the weighted best-leaf lower bound;
- tie-safe phase ordering and missing-degree pruning;
- `K_{2,2}` consistency / triple-neighbor transitivity; and
- the opposite-corner diameter projection contradiction.

Thus the new burden is purely outward arithmetic plus domain coverage. Singleton trains
remain safe for the same reason as in the `0.0021` audit: they create missing crossing
pairs and never unpaid strict-rhombus edges.

## 2. Certified `sqrt(Delta_2)` bracket is self-contained

The verifier starts from rational decimal intervals for `pi` and `sqrt(3)` and checks

\[
\sqrt3_{lo}^2<3<\sqrt3_{hi}^2.
\]

It then forms outward rational bounds

\[
\Delta_{lo}={\pi_{lo}\over2\sqrt3_{hi}},
\qquad
\Delta_{hi}={\pi_{hi}\over2\sqrt3_{lo}}
\]

and obtains the bracket for

\[
s=\sqrt{\Delta_2}
\]

by integer square-root rounding. No floating-point value is used in a load-bearing
comparison.

With `g=0.002123`, the safe quantities are

\[
W_0={4s^2\over 2s+g},
\qquad
d_0=sg+{g^2\over4}.
\]

The verifier uses a lower bound for `W_0` and an upper bound for `d_0`, which are the
correct outward directions for the subsequent lower bound on the selected degree sum.

## 3. Interval minimization directions are correct

For negative center imbalance `z`, the audited scalar is

\[
\Phi_g(z)=
{3W_0\over4}+{z\over2}
-6\sqrt{(d_0-z^2){W_0+2z\over W_0+6z}}.
\]

For nonnegative `z`, the ratio is safely replaced by `1`.

The certificate covers `[-0.045,0.045]` in rational intervals of width `5e-6`, which
strictly contains the actual domain `|z|<=sqrt(d_0)`.

On one interval `[x,y]`:

1. the raw term `3W_0/4+z/2` is increasing in `z`, so the lower bound uses `x`;
2. `d_0-z^2` is maximized at the point of the interval nearest zero;
3. for `z<0`,

   \[
   R(W,z):={W+2z\over W+6z}
   \]

   satisfies

   \[
   {\partial R\over\partial z}={-4W\over(W+6z)^2}<0,
   \qquad
   {\partial R\over\partial W}={4z\over(W+6z)^2}<0.
   \]

   Therefore the loss ratio is maximized by the interval left endpoint and the lower
   bound on `W`, exactly as the verifier does.

Every square root in the loss is rounded upward. Hence every interval value is a true
outward lower bound for `Phi_g`.

The worst interval is the one reported by the certificate near
`z=-0.00584`, and the final lower margin over `2/sqrt(3)` remains greater than
`1e-5`.

## 4. The common-neighbor pruning still has fixed slack

The candidate must retain the Section-163 common-neighbor hypotheses after phase and
degree pruning. Its certificate computes a global upper missing-degree scale `p_max`
and a uniform lower selected-center mass `C_min`, then checks

\[
\boxed{C_{min}>5p_{max}.}
\]

This is stronger than the three-neighbor threshold actually needed after the two
`p_max` pruning losses. Thus the refinement has not crossed a hidden combinatorial
endpoint even though the final diameter margin is small.

The independent run of

`research/verify_target_c_phase_star_atomic_gap_002123.py`

passes this check together with the interval certificate.

## 5. Section-171 propagation is independently outward

For

\[
C_{146}={4\over9}(\pi+s),
\qquad
\epsilon_0=0.0017327,
\qquad
t_0=C_{146}+\epsilon_0,
\]

and `g=0.002123`, the feasible detour endpoint is

\[
\delta_0={{9\over2}\epsilon_0-g\over2}=0.002837075.
\]

The companion Fraction certificate bounds the cube-root term outward and proves the
Section-171 endpoint function is negative by more than `3e-5`. It also proves the
derivative with respect to detour is greater than `142` throughout the whole feasible
interval. The already-audited monotonicity in `t` therefore excludes every
`t<=t_0`.

The independent run of

`research/verify_target_c_orbit_detour_gap_002123.py`

passes with strict margins.

## 6. Downstream arithmetic is consistent

The propagation certificate verifies the exact substitutions

\[
\liminf {T-q/2\over D}\ge2s+0.002123,
\]

\[
\liminf {\sigma_R\over D}\ge0.004246,
\]

\[
\liminf {q-k\over D}
\ge C_{146}+0.0017327,
\]

and the corresponding low-`t` values

\[
{Q-f\over D}\le0.002837075+o(1),
\qquad
{p_5\over D}\ge0.495225672369096\ldots-o(1).
\]

It also checks the updated detour-free and bridge-subtracted constants. These are
algebraic consequences only; their parent geometric scopes remain unchanged.

## 7. Disposition

**PASS at proof-only scope.** The `0.002123` theorem is a safe numerical refinement of
the independently audited `0.0021` minimax mechanism. The current strongest certified
proof-only scalar chain is therefore

\[
\boxed{
A\ge2\sqrt{\Delta_2}+0.002123,
}
\]

\[
\boxed{
\liminf {\sigma_R\over D}\ge0.004246,
}
\]

\[
\boxed{
\liminf {q-k\over D}
\ge {4\over9}(\pi+\sqrt{\Delta_2})+0.0017327.
}
\]

This audit does not close C-II. The remaining obstruction is source-level diameter
locking / exchange, not uncertainty in this scalar endpoint.
