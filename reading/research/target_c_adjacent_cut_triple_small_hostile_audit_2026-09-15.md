> Generated reading edition · [exact source](../../research/target_c_adjacent_cut_triple_small_hostile_audit_2026-09-15.md) · source SHA-256 `6e58fd6170ab6696924df14cadf73631ff82ccbe2f1eb3cade6197249334f4ef`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "a1e29c41841e926088ea76216b6e3a0fdbef3146", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_adjacent_cut_triple_small_hostile_audit_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "f495fe8db7197c51846dd3f960c7e2d9e285be5f8c19cac8d7de86c2f1e10da5"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — simultaneous phase/switch smallness on one adjacent O--O pair

**Date:** 2026-09-15  
**Reviewed:**
- `research/target_c_adjacent_cut_triple_small_2026-09-15.md`
- `research/verify_target_c_adjacent_cut_triple_small.py`

**Repository base:** `82ed6442ebf6313b364bde645076b2934aceeb57`  
**Disposition:** **PASS at proof-only `t<=1.844` full-core Type-II scope.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The candidate strengthens the current laminar-backbone normal form by forcing one consecutive pair of smallest-leaf outer-to-outer cuts to satisfy three properties simultaneously:

- only `O(1)` actual diameter rows change incidence;
- the total KKT multiplier on changing rows is `O(D^{-1})`; and
- the two leaf directions differ by `O(D^{-1})`.

The proof averages three independent nonnegative global budgets on one high-phase-center good-leaf path.  The two potentially delicate points are whether the phase quantile argument really pays every leaf offset through **distinct actual rhombi**, and whether a diameter edge whose selected incidence is only a truncated interval can create more than two internal switches.  Both checks pass.

---

## 1. The good-leaf thresholding is the already-audited weighted argument

The parent fan theorem gives retained pair weights `0<w_tau<=1`, total retained pair weight above `0.0848D`, weighted center-degree average above `0.7404D`, and total center count below `1.063D`.

For threshold

```math
\lambda=0.677,
```

the standard weighted threshold inequality gives good retained weight density

```math
g
={ (0.7404-0.677)(0.0848)\over1.063-0.677}
={16801\over1206250}
=0.01392829\ldots .
```

Because each retained pair weight is at most one, the distinct good-train count is at least the same linear density.  This is exactly the conversion already hostile-audited in the `0.7404D` rectangle profile; no weighted-average-to-unweighted-count shortcut is introduced.

**Verdict:** PASS.

---

## 2. The top-center quantile produces the claimed path length

Order the finite center family by one real phase representative inside the frozen center window.  Let `H` be the top `r=61/125` fraction, with integer rounding absorbed into `O(1)`.

Every good leaf has more than `lambda D` center neighbors.  Outside `H` there are at most

```math
(1-r)N_C+O(1)
\le(1-r)(1.063)D+o(D)
```

centers.  Hence every good leaf has at least

```math
d_{top}D-o(D),
\qquad
d_{top}=\lambda-(1-r)(1.063)
={16593\over125000}>0
```

neighbors in `H`.

Summing over at least `gD-o(D)` distinct good leaves and dividing by

```math
|H|\le r(1.063)D+o(D)
```

gives one `gamma in H` crossing at least

```math
pD-o(D),
\qquad
p={d_{top}g\over r(1.063)}
={278778993\over78216868750}
=0.0035641799\ldots
```

good leaves.

The parent complement-dual theorem says the good leaves crossed by one center train form one simple path in the good-leaf dual tree.  Thus the candidate gets a genuinely consecutive backbone, not an arbitrary subfamily.

**Verdict:** PASS.

---

## 3. Every path leaf has linearly many center neighbors below `gamma`

Because `gamma` belongs to the top `r` fraction, the number of centers with phase **strictly above** `alpha_gamma` is at most

```math
|H|\le rN_C+O(1)
\le r(1.063)D+o(D).
```

A good path leaf has more than `lambda D` center neighbors.  Therefore at least

```math
d_{low}D-o(D),
\qquad
d_{low}=\lambda-r(1.063)
={9891\over62500}
=0.158256
```

of its center neighbors have phase at most `alpha_gamma`.

This direction is correct even if `gamma` is the lowest-phase member of the top quantile; that is exactly the worst case used above.

**Verdict:** PASS.

---

## 4. The phase-offset payment uses distinct actual rhombi

For a path leaf `tau_j`, write

```math
q_j=\beta_j-\alpha_\gamma-\pi/3>0,
```

which is positive because `gamma` actually crosses `tau_j` in a strict rhombus and the frozen phase orientation is the center-to-leaf orientation.

If another center neighbor `c` satisfies `alpha_c<=alpha_gamma`, then its actual crossing rhombus with `tau_j` has angular excess

```math
\delta_{cj}
=\beta_j-\alpha_c-\pi/3
=q_j+(\alpha_\gamma-\alpha_c)
\ge q_j.
```

Different center/leaf train pairs cross in different strict rhombus faces: the complete-train crossing graph records one strict-rhombus crossing per crossing pair, and two complete trains do not meet twice.  Across different leaves the leaf train label changes, so no rhombus is reused.

Thus the selected payments are a sub-sum of the canonical global rhombus angular-defect budget.  Consequently

```math
d_{low}D\sum_jq_j
\le C_{phase}D+o(D),
```

and

```math
\sum_jq_j\le C_{phase}/d_{low}+o(1).
```

No assumption that the path itself lies in the phase-collapsed rectangle is needed.

**Verdict:** PASS.

---

## 5. Truncating a diameter interval to the selected path creates at most two internal changes

The exact laminar multishear theorem says one source pair is separated by a contiguous interval of the **selected** dual-path cuts.  This remains true when the pair's full complement-dual path enters the selected path before its first selected edge or leaves after its last selected edge: intersection of two tree paths is connected.

Therefore the restricted incidence sequence is

```math
0,\ldots,0,s,\ldots,s,0,\ldots,0
```

for one sign `s`.  Among the internal boundaries between selected cuts it changes zero, one, or two times, never more.

Hence

```math
\sum_iN_i\le2h
```

for actual diameter-edge switch counts, and with positive normalized multipliers

```math
\sum_iB_i\le2.
```

This does not count the two exterior boundaries of the selected path; omitting those only decreases both sums.

**Verdict:** PASS.

---

## 6. The diameter-edge count bound is legitimate at this scope

The full actual diameter graph is a planar straight-line thrackle, so Hopf--Pannwitz gives

```math
h\le q.
```

Every loaded force-hull side joins consecutive distinct source points and has length at least one.  Therefore

```math
q\le\operatorname{per}(F).
```

Cauchy's perimeter-diameter inequality gives

```math
\operatorname{per}(F)\le\pi D.
```

Thus

```math
\sum_iN_i\le2h\le2\pi D.
```

No near-disk equality or stale `q/D->pi` claim is used.

**Verdict:** PASS.

---

## 7. The KKT resultant difference is paid by switching multiplier only

With coherent nested shore orientation, §157 gives

```math
F_j=A_ju_j
=\sum_h\beta_h\varepsilon_{hj}r_h.
```

Subtract adjacent identities:

```math
F_{i+1}-F_i
=\sum_h\beta_h
(\varepsilon_{h,i+1}-\varepsilon_{hi})r_h.
```

Since every active diameter vector has length `D`,

```math
\|F_{i+1}-F_i\|
\le D\sum_h\beta_h
|\varepsilon_{h,i+1}-\varepsilon_{hi}|
=DB_i.
```

Rows spanning both cuts cancel **exactly** from the vector difference; no phase-closeness approximation is used here.

The reverse triangle inequality gives

```math
|A_{i+1}-A_i|\le\|F_{i+1}-F_i\|.
```

**Verdict:** PASS.

---

## 8. The combined averaging constant is certified outward

Define

```math
T_i=N_i+DB_i+D(q_i+q_{i+1}).
```

The previous sections give

```math
\sum_iT_i
\le
\left(2\pi+2+{2C_{phase}\over d_{low}}\right)D+o(D).
```

There are `m-1=pD-o(D)` internal boundaries.  The certificate uses only

```math
\pi<355/113,
\qquad
\sqrt3<17321/10000
```

to enclose

```math
C_{phase}<5.31673245699\ldots .
```

With the exact rational `p,d_low`, the resulting upper constant is

```math
21175.9033137\ldots<21200.
```

There is more than `24` units of slack.  Since `N_i`, `DB_i`, and `D(q_i+q_{i+1})` are nonnegative, the selected boundary satisfies each individual advertised bound.

**Verdict:** PASS.

---

## 9. Scope after the current `t<=1.84362` exclusion

The parent fan theorem and all finite interval/KKT identities are uniform through `t<=1.844`.  Current main excludes `t<=1.84362`; it does not invalidate these inputs.  The theorem therefore remains nonvacuous on the surviving band

```math
1.84362<t\le1.844.
```

The candidate correctly does not claim that `O(1)` switching rows are eliminable by a two-parameter shear.  The finite active set may still realize a max-function cusp.

**Final verdict:** PASS at proof-only `t<=1.844` full-core Type-II scope. C-II and Level I remain open.
