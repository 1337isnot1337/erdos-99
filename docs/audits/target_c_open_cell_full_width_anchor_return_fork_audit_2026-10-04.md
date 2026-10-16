<!-- theorem-state: {"artifact_id":"ART-E68CA406913E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Independent audit — strong open-cell full-width anchor / return fork

**Date:** 2026-10-04
**Audited artifact:** `docs/reports/target_c_open_cell_full_width_anchor_return_fork_2026-10-04.md`
**Source provenance:** `automation/target-c-open-cell-full-width-anchor-return-2026-10-04-v2`
**Audit base:** current main `596445ac32ffd45e2cbb8df9dbeba15be3465cf5`
**Verdict:** **PASS at proof-only conditional scope.**
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The report composes the proof-only strong open-cell host-cap / harmonic-localization
antecedent with canonical Sections 120 and 123. This audit checks the new
composition only. It does not promote or independently reprove the upstream
strong-SCC staircase, host-cap extraction, or harmonic-localization statements.

Write \(G_\cap\) for the quadratic strict-rhombus grain in one actual harmonic
attachment cell
\[
P_\cap=\operatorname{conv}A_\cap,
\qquad
A_G=\operatorname{area}(G_\cap),
\]
and let \(\eta\) be signed height from the host-cap chord. The current proof-only
attachment-depth theorem supplies a loaded attachment \(a_*\in A_\cap\) of maximal
height \(H_*\), with
\[
H_*\ge A_G/D.
\]

The audited new conclusions are:

1. there is a second loaded attachment \(b_*\in A_\cap\) with
   \[
   |a_*-b_*|\ge A_G/D;
   \]
2. canonical Section 120 applied to these two actual attachment vertices gives
   \[
   L_\cap+P_{{\rm exc},\cap}-2|a_*-b_*|
   \ge(4-2\sqrt3)\frac{A_G}{D};
   \]
3. hence, with \(\kappa=2-\sqrt3\), at least one of
   \[
   P_{{\rm exc},\cap}\ge\kappa\frac{A_G}{D}
   \tag{A.1}
   \]
   and
   \[
   L_\cap-2|a_*-b_*|
   \ge\kappa\frac{A_G}{D}
   \tag{A.2}
   \]
   holds;
4. in branch (A.1), canonical Section 123 gives
   \[
   e_{BB}-k\ge\frac{2-\sqrt3}{10}\frac{A_G}{D};
   \tag{A.3}
   \]
5. in branch (A.2), one of the two actual occurrence-counted outer routes between
   \(a_*,b_*\) has excess over its Euclidean chord at least
   \[
   \frac{2-\sqrt3}{2}\frac{A_G}{D}.
   \tag{A.4}
   \]

For \(A_G=\Omega(D^2)\), every displayed right-hand side is \(\Omega(D)\).

---

## 1. Full-width second attachment

Let
\[
h_-=\min_{y\in G_\cap}\eta(y),
\qquad
h_+=\max_{y\in G_\cap}\eta(y).
\]
Since \(G_\cap\subset P_\cap\) and \(\operatorname{diam}P_\cap\le D\), every
height slice of \(G_\cap\) has one-dimensional measure at most \(D\). Fubini gives
\[
A_G\le D(h_+-h_-).
\tag{A.5}
\]

Every point of \(P_\cap\) has height at most \(H_*\), because \(H_*\) is the
maximum attachment height and height is affine on
\(\operatorname{conv}A_\cap\). Thus \(h_+\le H_*\), so
\[
H_*-h_-\ge A_G/D.
\tag{A.6}
\]

Choose \(y_-\in G_\cap\) with height \(h_-\). Since
\(y_-\in P_\cap=\operatorname{conv}A_\cap\), affine averaging implies that some
\(b_*\in A_\cap\) satisfies
\[
\eta(b_*)\le h_-.
\]
Therefore
\[
\eta(a_*)-\eta(b_*)\ge A_G/D.
\]
Signed distance is 1-Lipschitz, so
\[
\boxed{|a_*-b_*|\ge A_G/D.}
\tag{A.7}
\]
The right side is positive, hence \(a_*\ne b_*\).

No convexity of the rhombus union is used; only containment in \(P_\cap\), its
diameter bound, Fubini, and affine height on the attachment hull are needed.

**Verdict:** pass.

---

## 2. Section-120 cut-pair applicability

Canonical Section 120 permits **any two distinct attachment vertices occurring on
the induced harmonic graph's occurrence-counted outer-face walk**.

Canonical Section 62 orders the attachment vertices on the boundary of
\(P_\cap=\operatorname{conv}A_\cap\) and decomposes that induced graph's outer walk
into routes between consecutive attachment vertices. Every attachment is a loaded
force-hull vertex; the loaded set is in strictly convex position, so each member of
\(A_\cap\) is an extreme vertex of \(P_\cap\). Thus both \(a_*\) and \(b_*\) are
legitimate Section-120 cut vertices. Repeated outer occurrences or bridges do not
invalidate the theorem because Section 120 is explicitly occurrence-counted.

Put
\[
r_*=|a_*-b_*|,
\qquad
d_\cap=\operatorname{diam}P_\cap\le D.
\]
Canonical Section 120 gives
\[
d_\cap\left(L_\cap+P_{{\rm exc},\cap}-2r_*\right)
\ge(4-2\sqrt3)A_{4,\cap}.
\tag{A.8}
\]
The selected grain is made of strict rhombi in this cell, so
\[
A_{4,\cap}\ge A_G.
\tag{A.9}
\]
Since the right side is positive, the route-excess factor is nonnegative. Divide
(A.8) by \(d_\cap\le D\):
\[
\boxed{
L_\cap+P_{{\rm exc},\cap}-2r_*
\ge(4-2\sqrt3)\frac{A_G}{D}.
}
\tag{A.10}
\]

This direction of comparison is correct: \(1/d_\cap\ge1/D\).

**Verdict:** pass.

---

## 3. The payment-versus-detour fork is exhaustive

Set \(\kappa=2-\sqrt3>0\). Equation (A.10) becomes
\[
(L_\cap-2r_*)+P_{{\rm exc},\cap}
\ge2\kappa\frac{A_G}{D}.
\tag{A.11}
\]

Both summands on the left are nonnegative. The exceptional perimeter is
nonnegative. Also the two complementary outer-walk arcs from \(a_*\) to \(b_*\)
each have length at least their common Euclidean chord \(r_*\), hence
\[
L_\cap\ge2r_*.
\]
Therefore if both (A.1) and (A.2) failed, their sum would be strictly less than
the right side of (A.11). At least one must hold.

**Verdict:** pass.

---

## 4. Section-123 payment is scope-correct

Canonical Section 123 applies to the actual induced harmonic cells and proves
\[
\sum_rP_{{\rm exc},r}\le10(e_{BB}-k).
\tag{A.12}
\]
The selected \(P_{{\rm exc},\cap}\) is one nonnegative term of this exact global
sum. Consequently (A.1) implies
\[
10(e_{BB}-k)
\ge P_{{\rm exc},\cap}
\ge\kappa\frac{A_G}{D},
\]
which is exactly (A.3).

No local exceptional-face occurrence is counted twice in this inference; the
injectivity/accounting issue is already part of the promoted Section-123 theorem.
No local outer-walk occurrence is identified with a global loaded-hull occurrence.

**Verdict:** pass.

---

## 5. The outer-route branch is an actual occurrence statement

Cut the occurrence-counted cell outer walk at \(a_*,b_*\). Let its two route
lengths be \(\ell_1,\ell_2\). Then
\[
\ell_1+\ell_2=L_\cap,
\qquad
\ell_i\ge r_*.
\]
If (A.2) holds,
\[
(\ell_1-r_*)+(\ell_2-r_*)
=L_\cap-2r_*
\ge\kappa\frac{A_G}{D}.
\]
Thus one route satisfies (A.4).

The conclusion is deliberately local and occurrence-counted. It does not assert that
the route is simple, bridge-free, globally injective across cells, a Section-122
selected route, or a finite source deformation.

**Verdict:** pass.

---

## 6. Scope limits

The proof does **not** establish any of the following.

- The host chord \(a_*b_*\) is an actual diameter edge. The endpoints are loaded
  actual-diameter endpoints, but their mutual pair need not be diametral.
- The linear route excess can already be summed injectively with other cells.
- The linear \(e_{BB}-k\) branch contradicts the current global surplus ledger.
- A same-cardinality strict-\(D\) competitor exists.
- The proof-only strong open-cell antecedent is canonical.
- Type I/macroscopic-container or the non-strong inverse-\(D\) inactive branch is
  affected.

The exact next strong-Type-II obligation is therefore source-level:

\[
\boxed{
\text{spend the linear }e_{BB}-k\text{ payment, or spend the anchored linear
outer-route excess against the cap-local grid / diameter topology.}
}
\]

**Disposition:** the new full-width attachment and canonical payment/detour
composition pass independent audit at their stated conditional proof-only scope.
Theorem-state authority remains unchanged.
