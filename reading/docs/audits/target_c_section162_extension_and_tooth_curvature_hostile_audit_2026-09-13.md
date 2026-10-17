> Generated reading edition · [exact source](../../../docs/audits/target_c_section162_extension_and_tooth_curvature_hostile_audit_2026-09-13.md) · source SHA-256 `3ceec82375e4a86c288f7903e509b2d86c8910d6435206b31892f807caf8a830`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-17AEC399420A","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Hostile audit — Section-162 extension and triangular-tooth curvature

**Date:** 2026-09-13  
**Base state:** `2026-09-12.audit.46`  
**Reviewed:**

- `research/target_c_section162_gap_extension_2026-09-12.md`;
- `research/target_c_triangular_tooth_curvature_2026-09-12.md`;
- the repaired ray-order argument in
  `research/target_c_consecutive_tooth_turn_order_repair_2026-09-12.md` and
  `docs/targets/target-c/post126-section141-coincident-apex-repair.md`.

**Disposition:** the Section-162 extension passes at audited-working proof-only scope.
The original triangular-tooth note is not standalone-safe; its conclusion is usable
only through the later repaired §141 scope. Canonical theorem state is unchanged.

## 1. Section-162 `eta=9/10000` extension

The reviewed extension does not change the inherited geometry. It assumes the same
Section-146 stability inequalities and the same audited Section-162 atom-versus-detour
lemma, then repeats the endpoint contradiction with `eta=9/10000`.

Under the endpoint assumption `t_D <= C_146+eta+o(1)`, the imported inequalities give
`k/D <= 9 eta+o(1)` and outer detour at most `(9/4)eta+o(1)`. The train ledger and
weighted Mantel step give the same bounds on atomic mass and off-orbit mass as in the
audited `eta=1/1250` theorem. The outer-terminal count is occurrence-counted, and the
atom-versus-detour lemma is applied to a limiting direction-measure atom, so no
probability-density normalization is lost.

The rational certificate was rerun:

```text
eta=0.0009000000
ell_lo=0.432298753842
ell_hi=0.432298768657
certified_lower_bound=0.004054430319
detour_upper_bound=0.004050000000
margin=0.000004430319
PASS: rational Section-162 eta extension
```

The monotonicity used in the certificate is correct. With `c=(9/2)eta` and
`A_0=2s+c`,

$$
A_0-\frac{4s^2}{A_0}=c\frac{4s+c}{2s+c},
$$

which is increasing in `s`; the displayed lower/upper rational evaluations therefore
enclose the atom mass in the correct directions. The denominator in the
atom-versus-detour bound is enlarged using the upper `pi` and atom bounds, so the
strict margin is conservative.

**Verdict:** PASS as a proof-only arithmetic extension under the named audited-working
Section-146/162 dependencies. It raises only the scoped endpoint floor to
`C_146+0.0009`; it does not address the remaining Type-II interval or Type I.

## 2. Original triangular-tooth curvature note

The finite turn inequality in the original note is geometrically plausible, but its
written proof is incomplete as a standalone theorem.

First, it applies source unit separation to the two tooth apices without excluding
the case that the two apexes coincide. A point is not unit-separated from itself, so
the displayed implication `|X_{i-1}-X_i|>=1` does not follow until distinctness is
proved.

Second, the original ray-order sentence treats membership in a common inward wedge as
if it fixed the order of the two rays. It does not: two rays in one wedge can occur in
either order.

The later repair supplies both missing inputs in the needed Type-II scope. Near-disk
loaded-hull convergence makes every exterior hull turn `o(1)`. Coincident adjacent
tooth apices would force a turn

$$
\alpha_i=\pi-\beta_i-\beta_{i+1}>\pi/3,
$$

so coincidence is impossible for sufficiently large Type-II sources. For distinct
apices, the repaired ray-order argument uses unit separation from the first apex to
the next loaded hull vertex; if the order were reversed, the cosine law would give a
source distance strictly below one. Only after that cross-distance argument is the
apex separation inequality valid.

Therefore the repaired §141 inequality may be used in its stated sufficiently-large
Type-II scope. The original unrestricted finite note must not be imported by itself.

**Verdict:** original note classified as conditional/repaired, not an independent
audited theorem. The repaired §141 result is the authoritative proof-only version and
still supplies only an `O(1)` total curvature payment, not C-II closure.

## Final disposition

One arithmetic endpoint strengthening passes. One older geometric finding required a
real proof repair; its original text is not promoted or treated as a premise. No
theorem-state mutation is justified, and C-II remains open.
