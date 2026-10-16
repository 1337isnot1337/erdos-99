<!-- theorem-state: {"artifact_id":"ART-DCAFC5CA7E9F","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — post-ZF branching currency and the zero-transfer forest

**Date:** 2026-09-11  
**Target:** Target C C-II  
**Status:** unpromoted research report; no route-map status change

## Level-I status

`STILL OPEN`.

Let (q) be the number of loaded diameter vertices, (h) the number of actual
diameter edges, and (r_H:=2h-q). In the post-ZF C-II representative,

\[
r_H=x_B+Q+2s_Z,
\tag{1}
\]

where (x_B=b-q) is outer-walk excess, (Q) is bounded-face degree defect, and
(s_Z=e+h-(2v-2)) is mixed-framework surplus. The stopped-train endpoint count
proves the finite inequality

\[
\boxed{3r_H\ge h-2.}
\tag{2}
\]

Thus every post-ZF survivor is quantitatively separated from a diameter matching:

\[
r_H\ge(\lceil D\rceil-2)/3.
\tag{3}
\]

In the additional exact (s_Z=0), C56-Z zero-transfer branch, the star-forest
classification gives (d_H:=q-h\ge h/5). The exact pinned ledger then gives the
new coupled currency estimate

\[
\boxed{c_I+e_{BB}+2s_C\ge {7h\over5}-2\ge {7\over5}\lceil D\rceil-2.}
\tag{4}
\]

This does not close the branch: there is no source-specific upper bound for (2) or
(4), and a large (c_I) is compatible with only (O(D)) attachment area.

## 1. Proof of the anti-matching inequality

Let (b) be the outer contact-face walk length, (f) the number of bounded
nonquadrilateral faces, and (g_F=Q-f), so that

\[
b+Q=2(h-s_Z),
\qquad
T={b+Q\over2}+2f=h-s_Z+2f.
\tag{5}
\]

Partition the outer walk into the (q) subwalks between consecutive loaded
force-hull vertices. Each has at least one edge. Since (b=q+x_B), bad (non-unit)
intervals have at most (x_B) members and contain at most (2x_B) edge
occurrences in total.

Every stopped train has two endpoint incidences. A train with two good unit
force-hull-side endpoints has two parallel hull-side directions. Any two such
tracks have alternating endpoint pairs on the convex boundary and therefore cross.
The train-intersection graph is triangle-free, so at most two trains have two good
endpoints. Every other train consumes a bad outer endpoint or an exceptional-face
endpoint. The latter capacity is exactly

\[
Q+4f=5f+g_F.
\tag{6}
\]

Therefore

\[
T-2\le2x_B+5f+g_F.
\tag{7}
\]

Substituting (5) gives

\[
h-2\le2x_B+3f+g_F+s_Z.
\tag{8}
\]

The exact terminal-defect partition is

\[
q=x_B+f+g_F+2d_H+2s_Z,
\tag{9}
\]

so

\[
r_H=2h-q=x_B+f+g_F+2s_Z.
\tag{10}
\]

Multiplying (10) by three and subtracting the right side of (8) gives

\[
3r_H-(2x_B+3f+g_F+s_Z)=x_B+2g_F+5s_Z\ge0.
\tag{11}
\]

Equations (8) and (11) prove (2). ZF gives (h\ge\lceil D\rceil), proving (3).
Repeated outer-walk edges and exceptional faces are counted with multiplicity; no
simple-polygon or pure-rhombic assumption is used.

There is a further phase-sensitive consequence when (s_Z=0). In that phase,

\[
r_H=x_B+Q,
\qquad h=r_H+d_H.
\tag{11a}
\]

Equations (2) and (11a) imply (d_H\le2r_H+2), hence

\[
h\le3r_H+2.
\tag{11b}
\]

Using the report-level DB density (h/D\ge2\rho-o(1)), with
\(\rho=\cos\rho=0.739085\ldots\), gives

\[
\boxed{\liminf {x_B+Q\over D}\ge {2\rho\over3}}
\quad(s_Z=0),
\tag{11c}
\]

and, in the cyclic subbranch (d_H=0),

\[
\boxed{\liminf {x_B+Q\over D}\ge2\rho.}
\tag{11d}
\]

These are lower bounds on the actual outer/face defect, not on an independently
chosen scaffold. They still have no opposing upper capacity bound: the current
full-source area estimates allow a linear defect of this size.

## 2. Proof of the zero-transfer coupling

Assume (s_Z=0) and C56-Z. C58 says that every component of (H) is a star of
degree at most five. Since (H) is a forest, its number of components is

\[
d_H=q-h,
\]

and (h) is the sum of the star degrees. Hence (h\le5d_H), so

\[
d_H\ge h/5.
\tag{12}
\]

The exact pinned ledger in the circuit phase is

\[
c_I+e_{BB}+s_C=q-2+d_H.
\tag{13}
\]

Using (q=h+d_H), this becomes

\[
c_I+e_{BB}+s_C=h+2d_H-2.
\tag{14}
\]

Adding (s_C\ge0) and using (12) proves (4). The final diameter-scale inequality
again follows from (h\ge\lceil D\rceil).

## 3. Exact surviving obstruction

The new inequality (2) forces linear diameter branching, while (4) couples the
zero-transfer star phase to the pinned/contact ledger. It nevertheless leaves the
following possibilities:

* in the cyclic (s_Z=0) branch, (d_H=0), so (4) is unavailable and the atomic
  lower bound still has no opposing upper tradeoff;
* in the general forest (s_Z=0) branch, Woodall gives only a caterpillar forest,
  and the (3d_H) surplus charge has no hub-block upper bound;
* in the (s_Z>0) branch, a zero coordinate of an extreme stress is not a weak
  geometric row, so (2) cannot be converted into a finite release.

The remaining obstruction is a bridgeless common contact block, arbitrarily small
positive stress on many active rows, and a macroscopic exceptional/outer source
population satisfying the known one-sided inequalities. A response-to-source upper
bound, simultaneous competitor, or support theorem is still required.

Regular odd shells, contact isolates, shared diameter endpoints, repeated outer
edges, and whole-circuit attachment exceptions are all retained by the hypotheses.
