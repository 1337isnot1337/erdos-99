> Generated reading edition · [exact source](../../research/target_c_three_cut_kernel_cusp_1086_hostile_audit_2026-09-15.md) · source SHA-256 `f13962f04ff537f66cca6d348b30d9d0ef535d511f1015ce65d0f3563e174663`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "36c8fd1ca85e3ed7f8fb31d19f6acbc866247568", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_three_cut_kernel_cusp_1086_hostile_audit_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "f38b93a1ba4d34eba9a670d093c5fd997849a80bc01af5dae8b445c224bb634e"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — `1085`-row optimized three-cut kernel

**Date:** 2026-09-15  
**Reviewed:**
- `research/target_c_three_cut_kernel_cusp_1086_2026-09-15.md`
- `research/verify_target_c_three_cut_kernel_cusp_1086.py`
- parent exact three-cut kernel theorem and C65 scope correction
- current `t<=1.844` switch-density ledger

**Disposition:** **PASS at proof-only full-core `t<=1.844` scope.**  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The candidate does not alter the exact three-cut shear argument.  It only replaces the
parent theorem's coarse triple selection by a count-focused high-center extraction and
then reapplies the already-audited two-boundary Pareto method.  The count improves from
`<42400+o(1)` to an eventual integer bound `<=1085`.

The main risks are the near-boundary center split `d_low=10^-4`, the conversion of
weighted good-leaf mass to distinct train count, double counting in the two-boundary
budgets, and the passage from the selected triple to the exceptional-set KKT mass.
All four are sound.

---

## 1. The sharper global switch budget is already proved on main

The candidate uses the current exact `t<=1.844` ledger

```math
\kappa<0.007259926+o(1)
```

and

```math
{h_H\over D}<1.851259926+o(1).
```

These follow from the matched `g=0.007707` residual envelope together with the already
proved retained-mass floor `z>2.2069-o(1)`.  No unmerged `z>2.217` strengthening is
used.

Each actual diameter interval on a laminar backbone has at most one start and one stop,
so

```math
\sum_iN_i\le2h_H
<3.702519852D+o(D).
```

This is exactly the later adjacent-switch-count input already present on main.

**Verdict:** PASS.

---

## 2. The count-optimized path does not recreate the rejected weighted-fan error

The candidate sets

```math
\lambda=0.6404.
```

The audited fan theorem gives a weighted average center degree above `0.7404D` and
retained pair weight above `0.0848D`.  Weighted thresholding first yields retained
weight on good leaves

```math
gD-o(D),
\qquad
g=0.0200662565\ldots .
```

Only after that inequality is established does the proof use `w_tau<=1` to infer at
least `gD-o(D)` **distinct** good leaf trains.  It never treats a weighted average as
an unweighted density floor.

Choose

```math
d_{low}=10^{-4},
\qquad
r={\lambda-d_{low}\over1.063}.
```

Then

```math
\lambda-r(1.063)=d_{low}>0
```

and

```math
\lambda-(1-r)(1.063)=0.2177>0.
```

Thus every good leaf has a fixed positive linear number of center neighbors on both
sides of the high-center cut.  Double counting incidences with the top `r` center
fraction gives one center train crossing more than

```math
pD-o(D),
\qquad
p=0.0068224645348\ldots
```

distinct good leaves.  Since the good leaves are pairwise noncrossing, their crossings
with one center train form one simple dual-tree path, as in the audited parent
construction.

**Verdict:** PASS.

---

## 3. Tiny `d_low` enlarges a constant; it does not change the asymptotic order

For each path leaf put

```math
q_j=\beta_j-\alpha_\gamma-\pi/3>0.
```

The leaf has at least

```math
d_{low}D-o(D)=10^{-4}D-o(D)
```

center neighbors of phase at most `alpha_gamma`.  Every such strict rhombus pays
angular defect at least `q_j`.  Since different leaf/center pairs are different strict
rhombi,

```math
\sum_jq_j\le {C_{phase}\over d_{low}}+o(1).
```

The constant `C_phase/d_low` is large, approximately `5.3e4`, but it is independent of
`D`.  Therefore the total two-boundary phase cost is still `O(D)`, and imposing a fixed
threshold `L=10^14` still yields an adjacent phase-variation bound `L/D+o(D^-1)`.

There is no hidden interchange in which `d_low` tends to zero with `D`; it is the fixed
rational `1/10000` throughout the theorem.

**Verdict:** PASS.

---

## 4. The two-boundary budgets have the stated factors of two

For triple starts `i`, define

```math
\mathcal N_i=N_i+N_{i+1}.
```

Each internal boundary count `N_j` appears in at most two consecutive triples.  Hence

```math
\sum_i\mathcal N_i
\le2\sum_jN_j.
```

The same combinatorics gives

```math
\sum_iD(B_i+B_{i+1})
\le2D\sum_jB_j
\le4D,
```

because the exact interval variation has `sum B_j<=2`.

For the phase cost, the boundary quantity is `D(q_j+q_{j+1})`.  Its total over all
boundaries is at most

```math
2D\sum_jq_j
\le {2C_{phase}\over d_{low}}D+o(D).
```

Each boundary phase quantity again occurs in at most two consecutive triples, giving

```math
{4C_{phase}\over d_{low}}D+o(D).
```

No factor is missing.

**Verdict:** PASS.

---

## 5. The Pareto union bound has genuine room at `N=1086`

The exact verifier recomputes the current `t<=1.844` defect ledger using Machin bounds,
radical enclosures, and the alternating sine series.  It obtains

```text
path density                         0.0068224645348...
two-boundary count-only average   1085.3907213145...
bad count density at N=1086          0.0068186369268...
bad beta density                     4.0e-14
bad phase density                    2.1266929828e-9
Pareto density margin                3.8254812077e-6
```

Thus the sum of bad triple-start densities is strictly below the available path/triple
density.  At least one triple simultaneously satisfies

```math
\mathcal N_i<1086+o(1),
\qquad
D(B_i+B_{i+1})<10^{14}+o(1),
```

and the analogous phase inequality.

Because `mathcal N_i` is an integer, the positive `1086-1085.390...` gap absorbs the
`o(1)` term for all sufficiently large members of the survivor sequence, giving

```math
\mathcal N_i\le1085.
```

**Verdict:** PASS.

---

## 6. Exceptional-set count and multiplier mass are inherited correctly

For three consecutive laminar cuts, every row whose support on the selected triple is
neither empty nor full switches at boundary `1|2` or `2|3`.  Therefore the parent exact
kernel theorem gives

```math
H_{exc}\subseteq H_{sw,1}\cup H_{sw,2}.
```

Hence

```math
|H_{exc}|\le N_i+N_{i+1}\le1085.
```

A row in that union contributes its positive multiplier at least once to
`B_i+B_{i+1}`; a middle-only row contributes twice, which only makes the upper bound
looser.  Thus

```math
\sum_{h\in H_{exc}}\beta_h
\le B_i+B_{i+1}
<{10^{14}\over D}+o(D^{-1}).
```

Likewise the adjacent projective gaps are bounded by the two selected phase costs.

**Verdict:** PASS.

---

## 7. The exact kernel and C65 conclusions need no new argument

The numerical optimization does not modify the parent algebra.  Three planar train
vectors still have a nonzero coefficient vector `c` with

```math
\sum_{j=1}^3c_ju_j=0.
```

Rows meeting none or all three selected cuts therefore have exactly zero first
relative-displacement coefficient.  Every possible nonzero first derivative lies in
`H_exc`.

Mixed infinitesimal rigidity makes that finite cusp nontrivial.  Canonical C65 supplies
`beta_h>0` on every actual diameter edge, so the exact weighted first-derivative balance
forces both derivative signs among force-visible rows of `H_exc`.  In the nonparallel
case, the parent implicit-function theorem still integrates the kernel to a genuine
finite multishear leaving all nonexceptional diameter rows unchanged exactly.

The later adjacent-strip sparse-force theorem is compatible but logically separate:
each of the two boundary layer reactions can be generated by at most two switching
bars when its reaction is nonzero.  That does not imply the entire three-cut cusp has
only four rows, because the max-function obstruction need not be supported only on the
chosen KKT conic generators.

**Verdict:** PASS.

---

## 8. Non-implications

The theorem does not establish:

- a lower bound on any exceptional KKT multiplier;
- a bound below `1085` on the actual max-function cusp from force sparsification alone;
- a feasible first-order kernel direction for all exceptional rows;
- a finite diameter-decreasing motion.

Small total exceptional `beta` mass cannot be used to discard an individual active
constraint.  The residual problem is a finite ordered full-support sign cusp, now on at
most `1085` actual diameter rows.

**Final verdict:** PASS at proof-only `t<=1.844` scope.  The quantitative strengthening
is valid; C-II and Level I remain open.
