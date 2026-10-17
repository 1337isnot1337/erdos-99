> Generated reading edition · [exact source](../../../docs/reports/target_c_finite_hull_side_train_capacity_2026-10-09.md) · source SHA-256 `2594b3bd61b48266a2f02f58ce6eadc494815f5bc8fffc24f9def5dd02b0df0e`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-603A2FAFC2A9","canonical":true,"claim_ids":["C-FINITE-HULL-SIDE-TRAIN-CAPACITY"],"claim_statuses":{"C-FINITE-HULL-SIDE-TRAIN-CAPACITY":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C: exact finite hull-side train-capacity bound

**Date:** 2026-10-09
**Repository base:** `08da5beefeb0cebeeabc532c83e814dba95b6241`
**State version:** `2026-10-09.audit.225`
**Run type:** independent audit and promotion
**Target:** C-II
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md`
**External literature search:** not used
**Computation:** exact finite verifier rerun; see the independent audit

## LEVEL I STATUS

`STILL OPEN`. C-I is closed and C-II remains open.

## 1. Exact theorem

Let **S** be a finite canonical contact-minimal, then diameter-pair-minimal triangle-free global minimizer in the post-ZF C-II normal form, with `C=C_*`, `H=H_*`, and every source point retained. Assume its actual loaded force hull `F=conv(B)` is a positive-area polygon. Write:

- `q=|B|` for the number of loaded force-hull vertices;
- `P_F` for the perimeter of `F`;
- `b` for the occurrence-counted outer contact-face walk length and `x_B=b-q`;
- `m_B` for the number of loaded-hull sides of length greater than one;
- `f` for the number of bounded nonquadrilateral contact faces;
- `Q=sum_G(deg(G)-4)` over those faces; and
- `k=d_H+s_Z`.

Let T_gg count complete trains whose two terminal incidences lie on direct unit loaded-hull sides. Then T_gg <= 2. The consecutive loaded-vertex outer-walk intervals W_i, of occurrence lengths ell_i, also satisfy

```math
\ell_i=1\quad\Longleftrightarrow\quad |b_i-b_{i+1}|=1,
\qquad
\sum_{\ell_i>1}\ell_i=x_B+m_B.
```

The exact finite train-capacity inequality is

```math
\boxed{5(q-k)+x_B+m_B\ge 3P_F-2.}
```

The theorem has no Type-II near-disk, small-matching, or asymptotic hypothesis. It is a count and perimeter inequality; it supplies no source motion, strict diameter decrease, C-II closure, or Level I consequence.

## 2. Proof

The canonical loaded-hull ledger gives `b+Q=2(q-k)` and partitions the occurrence-counted outer walk into intervals `W_i` joining consecutive loaded hull vertices. Each interval is a unit-contact walk, so `ell_i >= |b_i-b_{i+1}|`. If the hull side has length one, its endpoints are an actual contact. The positive-contact core lies in `F`; global unit separation rules out a third source point in the open unit side. The outer facial occurrence adjacent to the exterior of `F` is therefore that direct contact edge. Conversely, `ell_i=1` forces the hull-side length to be one. Thus the bad intervals are exactly the `m_B` nonunit hull sides, and

```math
\sum_{\ell_i>1}\ell_i
=\sum_i(\ell_i-1)+m_B
=b-q+m_B=x_B+m_B.
```

Let `T` be the number of complete stopped rhombus trains, including singleton contact-edge trains. The canonical face/train incidence identity is

```math
T=\frac{b+Q}{2}+2f=(q-k)+2f.
```

Let T_gg count trains with both terminal incidences on good unit hull sides. Each such train has opposite parallel terminal sides. A strictly convex polygon has at most one side in each oriented direction, and each contact edge belongs to one train, so distinct double-good trains have distinct projective directions. For directions 0 <= theta_i < theta_j < pi, the four directed hull sides occur in order theta_i, theta_j, theta_i+pi, theta_j+pi. Their endpoint pairs alternate, so the embedded train arcs must cross. The canonical triangle-free train-crossing graph therefore gives T_gg <= 2.

Every other train has at least one terminal occurrence either in a bad outer interval or on a bounded nonquadrilateral face. These terminal occurrences are counted by at most `x_B+m_B` bad outer occurrences and at most `4f+Q` exceptional-face incidences. Hence

```math
T-2\le x_B+m_B+4f+Q.
```

Substituting `T=(q-k)+2f` gives `q-k-2 <= x_B+m_B+2f+Q <= x_B+m_B+3Q`. Using `Q=2(q-k)-b` yields

```math
3b\le5(q-k)+x_B+m_B+2.
```

Finally, the polygonal routes `W_i` have total length `b` and join the consecutive vertices of `F`, so `P_F <= b`. This proves the claim.

## 3. Dependencies and exact scope

The proof uses canonical claims `C-LINEAR-NONMATCH` for stopped-train geometry and its simple triangle-free crossing graph, `C-LOADED-HULL` for the loaded-vertex outer-walk partition and exact face identity, and `C-ATTACH-CURRENCY` for harmonic trapping of every unloaded contact component in the convex hull of its loaded attachments. Since each loaded core vertex is in `B`, this gives the required `V subset F`. The separate `C-LOADED-HULL-CAP-BUDGET` assumes that containment and is not used to prove it. The source report `docs/reports/target_c_hull_side_exact_train_capacity_audit_2026-10-04.md` supplied the candidate accounting; its broader Type-II conclusions are not imported here.

The finite statement keeps contact-isolated source points in the global minimizer. They do not enter the positive-contact train graph, and no source point is deleted or moved.
