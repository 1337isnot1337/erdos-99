# Target B — Section 120 boundary-backtracking hostile audit

**Date:** 2026-09-12  
**Status:** audited-working; not canonical theorem-state authority.  
**LEVEL I STATUS:** **STILL OPEN.**

This audit reviews `research/target_b_section120_boundary_backtracking.md` and its
nonpositive-train companion. The result repairs the exact gap identified in the old
proposed equation (37.7): the boundary arc and the non-overcounted train-to-boundary
charge are now explicit.

## Audited theorem

In a finite simply connected pure strict-unit-rhombus disk, let `z,a` be an active
diameter pair with `|p_a-p_z|=D`. Let `Gamma` be either outer-boundary arc from `z`
to `a`, directed from `z` to `a`, and let `L=|Gamma|`. For each separating train
`tau`, write

\[
a_\tau=d_\tau u_\tau,
\qquad
\lambda_\tau=(p_a-p_z)\cdot a_\tau.
\]

If `P_0` is the set of tangent separating trains, `P_-` the backward separating
trains, and

\[
S_-:=\sum_{\tau\in P_-}(-\lambda_\tau),
\]

then

\[
\boxed{
L-D\ge |P_0|+|P_-|+{S_-\over D}.
}
\tag{120.A1}
\]

Consequently

\[
\boxed{
S_-\le {D\over2}(L-D),
}
\tag{120.A2}
\]

which is the previously unproved boundary-backtracking estimate, and

\[
\boxed{|P_0|+|P_-|\le L-D.}
\tag{120.A3}
\]

## Crosscut/orientation audit

Canonical train geometry realizes every complete train as a proper simple crosscut of
the pure rhombic disk. If a train separates `z` from `a`, its two boundary terminal
edges separate `z` and `a` on the boundary circle. Therefore each of the two
`z`-to-`a` boundary arcs contains exactly one terminal occurrence of that train.

The train-coordinate vector `a_tau` is oriented from the `z`-side of the train to the
`a`-side. Traversing either boundary arc from `z` to `a` crosses the train in exactly
that direction, so the directed unit vector of the charged terminal edge is
`a_tau`, not `-a_tau`.

A physical contact edge belongs to exactly one train. Hence distinct separating trains
charge distinct boundary-edge occurrences. The charge is injective.

**Verdict:** PASS.

## Projection audit

Write the directed unit edges of `Gamma` as `v_1,...,v_L` and
`q=(p_a-p_z)/D`. Their sum is `Dq`, so exactly

\[
L-D=\sum_{j=1}^L(1-q\cdot v_j).
\]

Every summand is nonnegative. The terminal edge charged to `tau` contributes

\[
1-q\cdot a_\tau=1-\lambda_\tau/D.
\]

Thus a tangent train contributes exactly `1`, while a backward train with
`x_tau=-lambda_tau/D in (0,1]` contributes `1+x_tau`. Summing the injective charges
proves (120.A1). Since `1+x>=2x` on `[0,1]`, (120.A2) follows with the exact factor
`1/2`.

**Verdict:** PASS.

## Hessian and tangent-capacity consequences

For a first-order-neutral train-angle velocity `v`, the exact signed-variance formula
is

\[
\mathrm d^2f_{za}[v,v]
=-\sum_\tau\lambda_\tau(v_\tau-\bar v)^2.
\]

Only backward coefficients contribute positively, so

\[
\mathrm d^2f_{za}[v,v]
\le {D\over2}(L-D)\|v-\bar v\|_\infty^2.
\]

The same boundary charge gives `|P_0|<=L-D`. For the specific Section-43.1 paired
quartic regression, which uses two distinct tangent trains per paired variable, this
implies

\[
s\le\lfloor(L-D)/2\rfloor.
\]

This last inequality is **not** promoted as a universal rank theorem for arbitrary
quartic blockers.

## What remains open

The theorem is scoped to the simply connected pure strict-rhombic disk. It does not
handle exceptional faces, holes, multiple rhombic components, or exterior source
vertices automatically. More importantly, it is a per-active-bar capacity theorem.
Different active diameter bars may use overlapping but different nonpositive train
sets, so the component-quotiented blocker/coforest rank inequality is still unproved.

The audit therefore certifies the boundary-backtracking lemma and the nonpositive
support capacity, but not Target B or Level I closure.

**Final disposition:** PASS at audited-working pure-disk scope. Target B remains open.
