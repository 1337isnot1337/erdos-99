<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "ffff474847f63ca7e19052ba440d2b872b0f6b1d", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_low_response_typeii_localized_train_hull_gap_self_audit_2026-09-12.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "565f362b6f2a5be9f4c6eb42d9b367c5fab7bc090224b508226acb0bcdf3227e"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile self-audit — localized Type-II train/hull low-response gap

**Date:** 2026-09-12  
**Reviewed files:**

- `research/target_c_harmonic_internal_outer_face_2026-09-12.md`
- `research/target_c_low_response_typeii_localized_train_hull_gap_2026-09-12.md`

**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

## 1. Verdict

**PASS after two scope repairs.**

The candidate theorem

\[
\liminf\mu_D
\ge
M_*:={2\over5}\left(\pi+\sqrt{\pi/(2\sqrt3)}\right)
=1.6375621841\ldots
\]

under canonical Type II and `epsilon_D->0` survives the hostile audit.

Two overstatements were found and repaired before this audit was written:

1. C40 plus response selection gives only
   \[
   \liminf\delta_*/D\ge1,
   \]
   not `delta_*/D->1`. The proof uses only the lower bound through `gamma>=1`.
2. When loaded attachment edges are restored to `C[I_r]`, later edges need not remain
   in the *current* outer face after earlier inserted edges subdivide it. The correct
   statement is that every added loaded edge lies in the closure of the **original**
   outer-face region of `C[I_r]`. This is exactly enough to preserve all original
   bounded faces.

No numerical or theorem statement changes after those repairs.

## 2. Audit of the response-selected cell

C41 gives

\[
D^2=\sum c_{bk}|b-k|^2,
\qquad
\sum c_{bk}=1+\varepsilon_D.
\]

Let `d_*` be the largest Euclidean diameter of an attachment hull. Component response
pairs have distance at most `d_*`; direct loaded-loaded response pairs have distance
one. Therefore

\[
D^2\le\max\{1,d_*^2\}(1+\varepsilon_D).
\]

For large `D`, `d_*>1`, and `epsilon_D->0` gives `d_*/D->1` from below. C40 then gives

\[
\delta_*\ge d_*-2,
\qquad
\liminf\delta_*/D\ge1.
\]

There is no use of HSR stress localization or of a unique stress-dominant cell.

## 3. Audit of the HOF face-preservation lemma

Canonical Section 82 gives

\[
I_r\subset\operatorname{int}P_r.
\]

Because `I_r` is finite,

\[
K_r:=\operatorname{conv}(I_r)\subset\operatorname{int}P_r.
\]

Every attachment vertex is an extreme vertex of `P_r`, hence lies outside `K_r`.
For an attachment contact segment, or a loaded-loaded contact among attachment
vertices, its relative interior is disjoint from `C[I_r]` by straight-line planarity.
Starting from an endpoint outside `K_r`, the segment begins in the unbounded
complementary component. Entering any old bounded face would require crossing that
face boundary, a contradiction.

Thus every added loaded edge lies in the original outer-face region. Added loaded
edges may create new faces *inside that region*, but they cannot enter or subdivide an
old bounded face. Therefore the bounded four-faces of `C[I_r]` are exactly the
all-unloaded canonical four-faces, hence strict rhombi.

This is sufficient for the local train count. No 2-connectivity or disk topology is
assumed.

## 4. Audit of the local Euler/train ledger

For `G_*=C[I_*]`, let `k_*,Q_*` be its outer-face incidence and bounded face-defect
currencies. Euler and face incidence give exactly

\[
k_*+Q_*=2(\delta_*+r_*).
\]

Let `R_*` be its bounded four-faces and `B_*` their train-boundary occurrence count.
The finite train theorem gives

\[
B_*\ge4\sqrt{R_*}.
\]

Every boundary occurrence faces either the outer face or a bounded nonquadrilateral
face. Thus

\[
B_*\le k_*+4f_*+Q_*\le k_*+5Q_*.
\]

The last inequality uses only `f_*<=Q_*`, valid because every nonquadrilateral bounded
face has degree at least five. Eliminating `Q_*` gives

\[
B_*\le10(\delta_*+r_*)-4k_*.
\]

This is the same coefficient-five recipient loss as canonical Section 85. The audit
does **not** replace it by four; the documented thin-pentagon regression forbids that
shortcut.

## 5. Audit of the local perimeter comparison

Every attachment vertex is at distance one from an internal vertex, so

\[
K_*\subset P_*\subset K_*+B(0,1).
\]

The internal outer-face walk has `k_*` unit edge occurrences, giving

\[
\operatorname{per}(K_*)\le k_*.
\]

Cauchy's width formula then gives the finite estimate

\[
\operatorname{per}(P_*)\le k_*+2\pi.
\]

After division by `D`, the additive constant vanishes. No assumption that attachment
edges are convex-hull sides is made.

## 6. Audit of local Type-II rhombus saturation

Canonical Section 83 gives nonnegative local deficits

\[
\operatorname{area}(P_r)-A_{4,r}\ge0
\]

whose total is `o(D^2)`. Therefore the selected cell has deficit `o(D^2)`.

Every strict unit rhombus has area at least

\[
a_0=\sqrt3/2.
\]

The Type-II global limits imply

\[
A_4-a_0R_4=o(D^2),
\]

and each individual rhombus excess `area(R)-a_0` is nonnegative. Therefore the
selected subfamily also has only `o(D^2)` excess. Consequently

\[
R_*/D^2\to a/a_0,
\qquad
a=\lim\operatorname{area}(P_*)/D^2.
\]

No average-to-pointwise sign error occurs here; both discarded families are
nonnegative.

## 7. Audit of the remaining-cell area bound

Let

\[
tD+o(D)=\sum_{r\ne *}\delta_r.
\]

C40 and isodiametry give

\[
\sum_{r\ne *}\operatorname{area}(P_r)
\le {\pi\over4}\sum_{r\ne *}(\delta_r+2)^2.
\]

Since the canonical component ledgers give `c_I=O(D)`, while the finite `mu` subsequence
and ZK ledger give `sum delta_r=O(D)`,

\[
\sum_{r\ne *}(\delta_r+2)^2
\le t^2D^2+O(D).
\]

Thus the `+2` correction is not silently multiplied into a quadratic error.
Type-II area tiling yields

\[
a\ge {\pi\over4}(1-t^2)
\]

for `t<=1`. For `t>1`, the theorem is already trivial from `gamma>=1` and
`mu>=gamma+t`.

## 8. Audit of the scalar optimization

The exact ZK split gives

\[
\gamma+t\le\mu,
\qquad
\gamma\ge1.
\]

The local train/perimeter estimate gives

\[
\gamma\ge M_*\sqrt{1-t^2}.
\]

If `t>=M_*-1`, then `mu>=1+t>=M_*`. Otherwise

\[
\mu\ge M_*\sqrt{1-t^2}+t.
\]

The right side is concave, so its minimum on `[0,M_*-1]` is at an endpoint. At zero
it is exactly `M_*`. At the other endpoint it exceeds `M_*`, using only the exact
bounds

\[
3/2<M_*<5/3.
\]

Thus the minimum is exactly the `t=0` endpoint and the stated constant follows.

## 9. Novelty cross-check against current main

Current `main` has two nearby proof-only results.

- The hostile-audited HSR report localizes low-response stress to at most six
  near-diameter cells and gives only the scalar `mu_D>=1-o(1)`.
- The corrected TQ report proves
  \[
  \liminf(q-k)/D\ge M_*
  \]
  in Type II without a response assumption.

Neither proves LRTQ. The exact relation

\[
\mu_DD-(q-k)=s_C-c_I-k-2
\]

has no canonical nonnegative sign. Therefore the TQ floor cannot simply be substituted
for the LRTQ conclusion.

LRTQ is genuinely a lower bound on a different currency, obtained by response
selection plus the local component ledger.

## 10. Remaining obstruction

Near equality forces `t->0`, so one near-diameter harmonic cell carries essentially
all macroscopic cell area and all macroscopic component-diameter currency. It must
simultaneously approach:

- circular isoperimetry;
- the Mantel/train boundary equality `B_*=4sqrt(R_*)`; and
- the worst-case pentagonal recipient ratio.

The most plausible next route is to quantify incompatibility between near-Mantel train
intersection structure and the canonical ordered-grid diameter bounds in Sections
76/90/91. The existing complete-grid extraction coefficient is too crude to close this
by itself.

**Final self-audit disposition:** PASS after the two stated scope repairs. No theorem-
state promotion is requested by this audit.
