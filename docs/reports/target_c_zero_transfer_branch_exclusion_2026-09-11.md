<!-- theorem-state: {"artifact_id":"ART-E31E564A117E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — conditional exclusion of the zero-transfer branch

**Date:** 2026-09-11  
**Repository state:** `053e1e1b85643b738b4cde306838d150ea325783`  
**Run type:** exact branch closure / response and contact topology  
**Target:** Target C, C-II  
**Status:** STILL OPEN; hold as report

This report closes the zero-transfer branch conditional on the report-level bridge
collapse, mixed 3-connectivity, SEPq, and perfect-matching area-gap inputs. It is
not a Level I result because those dependencies have not been promoted as one
authoritative C-II stack.

## 1. Statement

Let (C) be the positive contact graph and (H) the full actual diameter graph
of a sufficiently large fully force-visible C-II source. Assume

\[
K=Q^{\mathsf T}\Lambda^+Q=\operatorname{diag}(\beta_e^{-1}).
\tag{1.1}
\]

Assume:

1. mixed-support 3-connectivity, so every contact bridge is crossed by at least
   two diameter edges;
2. the report-level zero-transfer bridge-collapse theorem, which says every
   contact bridge has a singleton side;
3. (deg_C(b)le3) for loaded vertices and (deg_C(v)le5) for unloaded
   vertices;
4. SEPq for additive response on at least four terminals; and
5. the report-level force-hull area gap excluding an unbounded perfect-matching
   diameter branch.

Then the zero-transfer branch has no unbounded C-II sequence.

## 2. A contact bridge is impossible

By bridge collapse, a contact bridge has a singleton side ({p}). The bridge
bypass count supplies two distinct diameter edges (pa,pb) crossing it. Since
(p) is a loaded strict force-hull vertex, the rays (a-p) and (b-p) lie in
an open wedge of width less than (pi). Choose a legal C53 projective cut whose
open half-plane contains both rays, and orient the two chords from (p) to
(a,b). For the unit-current potential (V) with source (p) and sink (b),
the bridge carries one unit and therefore

\[
V(p)-V(u)=1/\alpha_{pu}.
\]

On the far side of the bridge, (u) is the maximum-potential vertex, so
(V(u)ge V(a)). Hence

\[
K_{pa,pb}=V(p)-V(a)ge1/\alpha_{pu}>0.
\tag{2.1}
]

The diagonal identity (1.1) is invariant under changing legal chord orientations,
because (K) changes by (Kmapsto SKS) for a diagonal sign matrix (S). It
therefore requires the same off-diagonal entry to be zero. This contradiction
excludes all contact bridges:

\[
\boxed{C	ext{ is bridgeless}.}
\tag{2.2}
\]

## 3. Large diameter stars are impossible

The zero-transfer response theorem gives that (H) is a forest and every one of
its components is a star. Suppose a component is a (k)-edge star with (kge3).
Its (k+1ge4) terminals have additive effective-resistance metric, because
(K) is diagonal. SEPq supplies a contact vertex (z) such that each component
of (C-z) contains at most one of these terminals.

Since (C) is bridgeless, each component of (C-z) has at least two contact
edges to (z). If (z) is unloaded, this gives

\[
\deg_C(z)\ge2(k+1)\ge8>5.
\]

If (z) is loaded, the (k) other terminals give

\[
\deg_C(z)\ge2k\ge6>3.
\]

Thus no component has three or more edges.

## 4. Two-edge stars are impossible

It remains to exclude a two-edge star with center (p) and leaves (a,b). The
three terminal points are loaded. Choose a legal C53 cut so that both vectors
(a-p) and (b-p) have the same orientation from (p). Since (K) is diagonal,

\[
q_{pa}^{\mathsf T}\Lambda^+q_{pb}=0.
\tag{4.1}

Consider the unit-current potential (V) with source (p) and sink (b). With
(q_{pa}=\mathbf e_p-\mathbf e_a), (4.1) says

\[
V(p)=V(a).
\tag{4.2}

The source (p) is a maximum of the potential, while (a) has zero injection.
The discrete maximum principle propagates equality from (a) through the entire
component of (C-p) containing (a). That component cannot contain (b), whose
potential is strictly smaller. Therefore (p) separates (a) and (b) in (C).

Because (C) is bridgeless, every component of (C-p) has at least two contact
edges to (p). At least two components contain (a) and (b), so

\[
\deg_C(p)\ge4.
\]

But (p) is loaded and the fully force-visible degree bound is
(deg_C(p)le3). This contradiction excludes every two-edge star.

The maximum-principle step is the point that is missing from a purely response
separator argument: a three-terminal additive response need not have a high-degree
separator in general, but a zero cross-transfer at the shared diameter center
forces that center itself to be a contact cut vertex.

## 5. The only remaining zero-transfer graph is a matching

Every component of (H) is now a one-edge star. Since (H) is the full diameter
graph on its loaded vertices, this is a perfect matching. The report-level
force-hull area comparison for the perfect-matching branch gives

\[
\operatorname{area}F\le\frac{\pi^2}{16}D^2,
\qquad
\liminf\frac{\operatorname{area}F}{D^2}
\ge A_{FS},
\]

where

\[
A_{FS}=0.6184708847\ldots>
\frac{\pi^2}{16}=0.6168502750\ldots.
\]

This fixed gap excludes an unbounded perfect-matching sequence. Therefore the
zero-transfer branch has no unbounded C-II sequence, conditional on the listed
report-level inputs. \(\square\)

## 6. What this does not prove

The argument does not exclude the strict-negative alternative

\[
\min_{e\ne f}K_{ef}<0.
\]

The weighted four-cycle response regression shows that a bridgeless common block
can have negative cross-transfer, so bridge positivity cannot be extended to that
branch. Contact-isolated source points are not used in the branch argument and
remain part of the unresolved global C-II problem.

The unpromoted dependencies also matter. The promoted C53/C63 stack alone does
not establish the report-level ZF bridge-collapse and force-hull area statements.

## 7. Classification

| Claim | Status |
|---|---|
| zero-transfer contact bridges are impossible | proved conditional on bridge collapse, bypass, and C53 orientation |
| zero-transfer stars of size at least three are impossible | proved conditional on SEPq and degree caps |
| zero-transfer two-edge stars are impossible | proved conditional on the maximum-principle argument and degree caps |
| zero-transfer branch has no unbounded sequence | conditional on the perfect-matching area-gap theorem |
| strict-negative branch | unresolved |
| Level I settlement | not proved |

**Promotion recommendation:** hold as a report. An independent audit should check
the legal-orientation step in (2.1) and the use of the bridge-collapse theorem
before any route-map promotion.
