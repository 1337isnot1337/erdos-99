<!-- theorem-state: {"artifact_id":"ART-7719BC1E31F3","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — Section-96 endpoint outer-walk geodesic collapse at `mu_4`

**Date:** 2026-09-12  
**Repository commit at start:** `d020b88c2b5b399be2c51412a799390fe7c39994`  
**State version at start:** `2026-09-11.audit.37`  
**Target:** C-II  
**Classification:** proved candidate; unpromoted handoff

## Candidate implication

```text
lambda -> mu_4 in the canonical wrapping-cell threshold
  -> equality in the Section-96 outer-walk budget
  -> three distinct forbidden-gap contact routes have o(D) geodesic excess
  -> all but o(D) ordinary attachment intervals are exact two-edge routes
  -> couple these corridors to the ordered grid, or obtain a strict source-preserving deformation.
```

The exact canonical quantity sharpened here is the sidewise outer-walk excess. No
KKT coefficient floor, contact-isolated deletion, or “near-geodesic is impossible”
inference is used.

## 1. Endpoint parameters and the exact budget

Work along a Type-II sequence and let `P_D=conv(A_D)` be a wrapping harmonic cell,
with `a_D=|A_D|`, diameter `d_D`, and normalized diameter

\[
 d_D/D\to\mu_4,
 \qquad \theta_4:=2\arcsin\mu_4.
\]

The canonical Section-96 threshold is characterized by

\[
 {3\over2}\sin\theta_4=3\theta_4-2\pi.
\tag{97.1}
\]

Put

\[
 \alpha_4:=3\theta_4-2\pi={3\over2}\sin\theta_4.
\tag{97.2}
\]

For the induced contact graph on the unloaded component and `A_D`, retain the
canonical notation `L_D` (outer-face walk length), `Q_D` (bounded-face degree
excess), `s_D` (pinned surplus), and `c_D` (loaded-loaded attachment contacts).
Section 96 gives

\[
 L_D+Q_D=4a_D-6-2s_D-2c_D.
\tag{97.3}
\]

The three-forbidden-gap packing ceiling gives

\[
 \limsup {a_D\over D}\le3\theta_4-2\pi=\alpha_4.
\tag{97.4}
\]

The Section-96 outer-walk estimate, with the three distinguished forbidden gaps,
gives

\[
 L_D\ge
 3D\sin\theta_4
2(a_D-3)-c_D^{\partial}-o(D),
\tag{97.5}
\]

where `c_D^{partial}` counts direct loaded-loaded sides of the attachment polygon.
Since `c_D^{partial}\le c_D`, (97.3)--(97.5) imply

\[
 2a_D\ge3D\sin\theta_4+2s_D+c_D+Q_D-o(D).
\tag{97.6}
\]

Using (97.1), the lower and upper bounds squeeze

\[
\boxed{a_D/D\to\alpha_4.}
\tag{97.7}
\]

The retained nonnegative terms in (97.6) therefore vanish at linear scale:

\[
\boxed{s_D/D\to0,\qquad c_D/D\to0,\qquad Q_D/D\to0.}
\tag{97.8}
\]

Substituting (97.7)--(97.8) into (97.3) gives

\[
\boxed{L_D/D\to4\alpha_4.}
\tag{97.9}
\]

This is an outer-walk statement, not an attachment-polygon perimeter statement.
The latter can remain smaller by a linear amount; that distinction is essential.

## 2. Sidewise decomposition of the outer walk

List the attachment vertices in cyclic order on `partial P_D` as
`p_1,...,p_{a_D}`. The outer-face walk can be partitioned, with edge occurrences and
bridge repetitions retained, into cyclic subwalks

\[
 W_{i,D}:p_i\leadsto p_{i+1}.
\]

Let `ell_{i,D}` be the unit-edge length of `W_{i,D}` and
`d_{i,D}=|p_i-p_{i+1}|`. The regular-neighborhood boundary of a connected embedded
plane graph proves that the subwalks can be chosen in the same cyclic order as the
extreme attachment vertices. Consequently

\[
 \ell_{i,D}\ge d_{i,D},
 \qquad
 \sum_i\ell_{i,D}=L_D.
\tag{97.10}
\]

For the three Section-96 forbidden gaps, the endpoints are separated by

\[
 d_{i,D}\ge(sin\theta_4-o(1))D.
\tag{97.11}
\]

They cannot be direct unit contacts for large `D`. For every other interval, the
canonical attachment-route rule says the route has length one only when the two
endpoints form a direct loaded-loaded contact; otherwise it has length at least two.
There are at most `c_D^{partial}=o(D)` such direct sides by (97.8).

Subtract the lower bound

\[
3D\sin\theta_4+2(a_D-3)-c_D^{partial}-o(D)
\]

from the exact total `L_D`. Equations (97.7)--(97.9) and
`2\alpha_4=3\sin\theta_4` show that the resulting slack is `o(D)`. It is a sum of
nonnegative terms:

* the excess `ell_{i,D}-d_{i,D}` on each of the three distinguished routes; and
* for every other non-direct route, the excess `ell_{i,D}-2`.

Therefore

\[
\boxed{
 \sum_{i\in I_{special}}(\ell_{i,D}-d_{i,D})=o(D),
}
\tag{97.12}
\]

and

\[
\boxed{
 \sum_{i\notin I_{special},\ W_{i,D}\text{ non-direct}}
 (\ell_{i,D}-2)=o(D).
}
\tag{97.13}
\]

In particular, all but `o(D)` of the ordinary attachment intervals are two-edge
routes, after counting the `o(D)` direct sides.

## 3. Metric collapse of the three special routes

For a unit-edge path from `u` to `v`, write `m` for its length, `d=|u-v|`, and
`e=m-d`. If `z_k` are its unit edge vectors and `q=(v-u)/d`, then

\[
 \sum_k(1-q\cdot z_k)=m-d=e.
\tag{97.14}
\]

If `psi_k` is the signed angle from `q` to `z_k`, the elementary inequality
`1-cos x\ge2x^2/pi^2` on `[-pi,pi]` yields

\[
 \sum_k\psi_k^2\le {\pi^2\over2}e.
\tag{97.15}
\]

Every path point lies in the ellipse with foci `u,v` and major-axis length `m`.
Consequently its Hausdorff distance from the chord segment is at most

\[
 \sqrt{de/2+e^2/4}+e/2.
\tag{97.16}
\]

By (97.11)--(97.12), each of the three distinguished routes has `d=Theta(D)` and
`e=o(D)`. Hence, for `j=1,2,3`,

\[
\boxed{
 d_H(W_{j,D},[u_{j,D},v_{j,D}])=o(D),
 \qquad
 \sum_{e\in W_{j,D}}\psi_e^2=o(D).
}
\tag{97.17}
\]

Thus the endpoint carrier has three distinct macroscopic unit-contact boundary
corridors that are geodesic at the global scale. This is a metric conclusion; it
does not say their transverse width is `O(1)`.

## 4. Handoff to the remaining C-II bridge

The endpoint normal form is now

```text
diam(P_D)/D -> mu_4
  -> a_D/D -> alpha_4
  -> Q_D+s_D+c_D=o(D)
  -> L_D/D -> 4 alpha_4
  -> three forbidden-gap routes have o(D) excess over their chords
  -> all ordinary attachment routes are 2-edge up to o(D) total excess.
```

The canonical ordered-grid theorem supplies a complete linear-by-linear phase-pure
train grid in the same carrier. A genuine closure would require a new interaction
lemma, for example:

\[
\text{three geodesic outer corridors}
+\text{near-quadrangulated carrier}
+\text{ordered grid}
\Longrightarrow
\text{unit triangle or strict source-preserving diameter decrease}.
\]

The near-geodesic regression remains binding: a long doubled corridor can have
`o(D)` normalized width while carrying linear contact length. No contradiction is
claimed from (97.17) alone.

## Dependency and scope audit

- **Canonical Section 96 / `C-WRAP-OUTER-WALK-GAP`:** the threshold equation,
  three-gap route lower bound, and the six-cluster attachment ceiling.
- **Canonical Section 82 / `C-HARMONIC-CARRIER-QUAD`:** the exact outer-face identity
  and attachment-route rule.
- **Canonical Section 80 / `C-FULLCORE-NEAR-DISK`:** annular force-hull geometry
  used for the chord lower bound.
- **Canonical Sections 90–91:** handoff only; they are not used in the endpoint
  collapse proof.
- **Contact-isolated source points:** retained; none are assigned to the carrier.

**Status:** proved candidate; unpromoted research artifact. C-II remains open.

