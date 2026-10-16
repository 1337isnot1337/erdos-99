# Hostile audit — minimal `K_5` reciprocal exclusion

**Date:** 2026-09-18  
**Audited source:** `research/target_c_minimal_k5_reciprocal_exclusion_2026-09-18.md`  
**Verdict:** `PASS at proof-only scope`  
**Theorem-state authority:** unchanged  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

This audit checks the new exclusion at the points where a false global conclusion could
enter: the two-turn trigonometric lemma, passage from force order to raw reciprocal-ray
order, use of the ground reciprocal vertex, finite sign-graph consistency, strictness of
the Euclidean negative-type inequality, and the transfer back to the one-anchor corank
bound.

## 1. The two-turn inequality is exact

For three consecutive unit force vectors,

\[
|u_i+u_{i+1}+u_{i+2}|^2
=3+2\{\cos\delta_i+\cos\delta_{i+1}
+\cos(\delta_i+\delta_{i+1})\}.
\]

Closure identifies this norm with `|u_{i+3}+u_{i+4}|`, and the already proved strict
source gap `delta_{i+3}<2pi/3` makes its square strictly larger than one.  The identity

\[
1+\cos a+\cos b+\cos(a+b)
=4\cos(a/2)\cos(b/2)\cos((a+b)/2)
\]

then forces `a+b<pi`, because the first two cosine factors are positive.  There is no
sign reversal or endpoint equality hidden in this step.

## 2. Force blocks really are contiguous

At a reciprocal hull vertex all five raw rays lie in one open cone of width strictly
less than `pi`.  Multiplying one sign color by `-1` places it in the antipodal cone.
Those two open cones are disjoint, so each sign color is a single contiguous block in
cyclic force-angle order.  The local `2+3` theorem therefore permits the notation used
in the exclusion note without assuming an extra rotation-system property.

Applying the two-turn inequality on both sides of each block boundary gives the raw
order

\[
N_1,P_1,N_2,P_2,N_3.
\]

Thus the size-two class occupies raw positions two and four.  Reversing the cyclic
orientation preserves those two positions, so the conclusion is orientation-safe.

## 3. The ground point is not assigned a source turn-gap

The `<120` source force-gap is used only at reciprocal vertices `1,...,5`, which
correspond to actual bounded contact pentagons.  The auxiliary ground reciprocal vertex
`0` is used only through facts already proved independently there: convex-hull
membership, the `2+3` local sign split, and the global signed length balance.

The seven-edge contradiction needs only the adjacent non-ground chain

\[
1-2-3-4-5.
\]

The six-edge case is determined from the five non-ground local rules; the resulting
edge set automatically gives ground degree two.  No unproved ground turn-gap is being
smuggled into the argument.

## 4. The finite sign step has been exhaustively regressed

`verify_target_c_minimal_k5_reciprocal_exclusion_2026_09_18.py` checks all `2^15`
undirected sign graphs on the six cyclically labelled vertices.  Imposing the local
alternation rule at vertices `1,...,5` and the already proved ground degree `2` or `3`
leaves exactly two graphs:

- the six-edge distance-two graph `C_3 sqcup C_3`;
- its nine-edge complement.

In particular no seven-edge graph survives.  The computation is a regression check;
the proof in the source note is the short undirected-edge consistency argument and does
not depend on enumeration.

## 5. The negative-type step is strict for the actual reciprocal points

The reciprocal construction already proves that all six points are distinct.  For a
projection direction not perpendicular to any pair difference, their six scalar
projections are all distinct.  In the one-dimensional identity

\[
\sum_{i,j}c_ic_j|t_i-t_j|
=-2\int\left(\sum_{t_i>s}c_i\right)^2ds,
\]

the integrand is nonzero on the interval immediately below the largest projected
coordinate, because exactly one coefficient `c_i in {+1,-1}` is present there.  Hence
the inequality is strict for every generic projection direction.  Only finitely many
directions are nongeneric, so the planar projection integral remains strict.

For `c=+1` on one alternating triple and `c=-1` on the other, the quadratic form is
exactly twice

\[
(\text{six within-triple lengths})-(\text{nine cross lengths}).
\]

It is therefore strictly negative, while reciprocal stress trace cancellation requires
those two length sums to be equal.  The contradiction is exact.

## 6. Scope of the corank consequence

The reciprocal `K_6` construction applies to the support-five equality case: five
one-anchor degree-five faces with relation graph `K_5`.  Excluding that object removes
support size five and nothing larger by itself.

The preceding one-anchor theorem already gives minimum relation degree four and a simple
relation graph for every nonzero component.  Hence the next possible support size is at
least six, giving

\[
\dim\ker(P|_{\ker C_{face}^T})\le n_1/6
\]

and

\[
\sigma_C\le2n_0+n_2+n_1/6.
\]

The audit does **not** claim that all one-anchor dual components are impossible, that
the weighted-seed frontier automatically improves, or that C-II closes.  Larger
support components remain a live obstruction.

**Audit disposition:** PASS.  The support-five one-anchor equality block is excluded;
the rigorous immediate global consequence is the coefficient improvement `n_1/5` to
`n_1/6`.  Larger one-anchor dual components and the positive diameter-locking problem
remain open.