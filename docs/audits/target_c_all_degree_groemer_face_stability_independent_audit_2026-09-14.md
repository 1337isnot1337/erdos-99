<!-- theorem-state: {"artifact_id":"ART-E5FA8DCD5D05","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Independent audit - all-degree Groemer face stability

**Date:** 2026-09-14
**Audited source:** `research/target_c_all_degree_groemer_face_stability_2026-09-14.md`
**Verdict:** PASS at proof-only scope, with an explicit activation-scope warning.
**LEVEL I STATUS:** STILL OPEN. C-II REMAINS OPEN.

## 1. External equality input

The normalization is correct. For centers of nonoverlapping unit disks, the
Thue-Groemer/Oler inequality is

\[
{A\over2\sqrt3}+{P\over4}+1\ge N.
\]

Scaling centers by `1/2` gives, for a unit-separated finite point set in its convex
hull,

\[
N\le {A\over a_0}+{P\over2}+1,
\qquad a_0={\sqrt3\over2}.
\]

The Groemer equality configurations are exactly the collinear segment case or a set
whose convex hull is triangulated by unit equilateral triangles using the points as
vertices. A modern restatement also records the equivalent disk version: a Groemer
packing has center hull either a segment of length `2(N-1)` or an equilateral-edge-2
triangulation. Thus the equality classification used in GS.1 has the correct scale and
content.

## 2. Local residual is exactly Oler equality slack

For a bounded exceptional face `P` of degree `d`, with `z` assigned contact-isolated
source points, the audited residual-conservation theorem gives

\[
r(P)={A(P)\over a_0}-{d\over2}+1-z.
\]

Because the face boundary is a convex unit-edge `d`-gon, its perimeter is exactly `d`.
For the `N=d+z` points consisting of boundary vertices plus assigned isolates,

\[
{A(P)\over a_0}+{d\over2}+1-N=r(P).
\]

Hence `r(P)->0` is precisely approach to equality in the finite Oler inequality; no
coarse chamber slack is substituted here.

The imported conservation law

\[
\sum_j r_j=R_F
\]

has already passed an independent algebra/sign audit. In particular every face
residual is nonnegative and their exceptional-face sum is at most `R_F`.

## 3. Compactness proof of GS.1

Fix `K` and `eta>0`. A counterexample sequence with degrees at most `K`, all hidden
pairs at distance at least `1+eta`, and residual tending to zero can be reduced to
fixed `d` and fixed assigned-isolate count `z`:

- the degree has finitely many values;
- isoperimetry bounds face area by `d^2/(4pi)`;
- Oler then bounds `z` in terms of `d`.

Normalize one unit boundary edge. All points lie in a common compact disk, so a
subsequence converges. Unit separation and the hidden-pair lower bound are closed;
area and convex perimeter are continuous. The limiting `N=d+z` point set therefore
attains Oler equality with hull perimeter `d`.

The segment equality case would have scaled convex-hull perimeter `2(N-1)`, which is
strictly larger than `d` for `N>=d>=5`. Thus the equality set is triangularly
triangulated. Such a triangulation has

\[
E=3N-h-3\ge2N-3>d.
\]

Only the `d` cyclic boundary pairs are non-hidden by definition. Hence at least one
unit triangulation edge is hidden, contradicting the limiting hidden-pair distance
`>=1+eta`. This proves the claimed uniform positive residual `sigma_K(eta)`.

No quantitative modulus is obtained; the source note correctly does not claim one.

## 4. Actual exceptional faces have no hidden unit pair

The strictness statement is valid.

- An assigned interior point is contact-isolated, so it has no unit pair at all.
- If two nonconsecutive boundary vertices of a convex contact face were at distance
  one, their unit segment would be an actual contact edge contained in that convex
  face. It would split the displayed face, contradicting the face definition.

Thus every hidden pair in an actual exceptional face is strictly longer than one.

## 5. Linear bounded-degree population

The arithmetic is correct. The AG42/Section-171 chain gives

\[
\liminf f/D\ge f_*=0.167124643466509\ldots .
\]

From `b+Q=2(q-k)`, `q<=P_F`, `b>=P_F`, and `k>=0`,

\[
Q\le P_F.
\]

A face of degree at least `K+1` contributes at least `K-3` to `Q`; hence

\[
f_{\le K}\ge f-{Q\over K-3}.
\]

Since `P_F/D->pi`, for `K=42`,

\[
\liminf f_{\le42}/D\ge
f_*-{\pi\over39}
=0.086570985682155\ldots .
\]

The regression correctly identifies `K=42` as maximizing the note's crude
matching coefficient over the tested integer range.

## 6. Face-disjoint near-contact matching

If `R_F=o(D)`, then for each fixed `eta>0`, only `o(D)` bounded-degree faces can have
all hidden pairs at least `1+eta`; otherwise their positive residuals would sum to a
linear amount. Thus linearly many degree-at-most-42 faces contain a hidden pair in
`(1,1+eta)`.

The conflict-degree estimate is safe. In a triangle-free unit-contact graph, contact
degree is at most five. At each boundary vertex of one face, at most four other bounded
face sectors occur. A degree-at-most-42 face therefore conflicts by shared boundary
vertex with at most `168` other bounded faces. Greedy coloring/independent-set
selection leaves at least a `1/169` fraction. Assigned isolates belong to one chamber,
so hidden pairs selected from these face-disjoint faces are pairwise vertex-disjoint.

The fixed-eta coefficient

\[
0.086570985682155\ldots/169
=0.000512254353148\ldots
\]

and the diagonal `eta_D->0` coefficient with the extra factor two are correct.

## 7. Binding activation-scope warning

The conclusion is a matching of hidden near-unit pairs, not a matching of isolated
points. A hidden pair may be

1. isolate-isolate;
2. isolate-boundary; or
3. boundary-boundary.

Existing protected simultaneous-contact creation theorems apply to contact-isolated
moving points safely inside a convex chamber. They do **not** justify moving arbitrary
positive-core boundary vertices while preserving their old unit contacts. Therefore
GS.20 cannot currently be fed wholesale into rattler first-contact absorption or PSC.

Likewise, near-unit distance alone does not create positive KKT force. Existing
activation regressions explicitly block that inference.

A valid next theorem must either isolate a linear submatching of type (1), or supply a
source-preserving deformation/rigidity argument for the boundary-involving pairs.

## 8. Verdict

PASS. The result supplies a genuine Type-II fork:

\[
R_F=\Omega(D)
\quad\text{or}\quad
\Omega(D)\text{ pairwise vertex-disjoint hidden pairs at }1+o(1).
\]

It does not close either branch. The main new research target is the type of the hidden
near-contact pairs, not their mere existence.

---

**Recovery provenance:** copied from `research/c2-closure-sol-20260914-r7` at exact tip `1541dac85e9ddf6450bb3cd7b14f5ce76e119420` during the 2026-10-04 Slot 2 branch audit. This recovered claim remains unreviewed and noncanonical.
