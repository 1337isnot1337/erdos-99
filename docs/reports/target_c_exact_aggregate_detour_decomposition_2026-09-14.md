<!-- theorem-state: {"artifact_id":"ART-7005D0860725","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — exact aggregate detour decomposition

**Date:** 2026-09-14  
**Repository commit:** `f174a9eb`  
**State version:** `2026-09-14.audit.51`  
**Run type:** closing proof / exact source-level reduction  
**Target:** Target C-II / Level I  
**Starting status:** canonical Sections 122–123 and the full-core train-coupled surplus floor  
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md`  
**External literature search:** not used  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

This report does not claim a Level I solution. It gives an exact finite
source-level decomposition of the aggregate outer-walk detour that remains in the
canonical full-core route.

## 1. Starting canonical endpoint

For a canonical full-core Type-II representative, Sections 122–123 give

\[
 \liminf_{D\to\infty}{1\over D}
 \sum_r(L_r+P_{{\rm exc},r}-2d_r)
 \ge {\pi\over2}(2-\sqrt3),
 \tag{AD.1}
\]

and

\[
 \sum_rP_{{\rm exc},r}\le10(e_{BB}-k),
 \qquad k=d_H+s_Z.
 \tag{AD.2}
\]

The residual was recorded as the aggregate outer detour

\[
 S_{\rm out}:=\sum_r(L_r-2d_r).
\]

The candidate chain for this run was

```text
local face identity + augmented-cell ledger
    -> exact formula for S_out
    -> upper bound or sign constraint in the loaded-hull currency
    -> contradiction with (AD.1), a strict source-preserving competitor, or a unit triangle
    -> C-II / Level I
```

The first arrow is proved below. The final bridge is not obtained.

## 2. Strongest genuinely new result

**Classification:** audited-working exact reduction; not canonical in this run.

### Theorem — exact finite aggregate-detour identity

Let `I_r` range over the unloaded positive-contact components in the canonical
post-ZF C-II representative. For each component use the canonical notation

- `A_r` for its distinct loaded attachment set and `a_r=|A_r|`;
- `P_r=conv(A_r)` and `d_r=diam(P_r)`;
- `s_r=e_r+t_r-2n_r-1` for its pinned surplus;
- `c_r` for loaded-loaded unit contacts with both endpoints in `A_r`;
- `Q_r` for the degree-above-four defect of bounded nonquadrilateral faces of the
  induced harmonic graph `H_r`; and
- `f_r` for the number of those nonquadrilateral faces.

Put

\[
 a:=\sum_ra_r,\quad C_{\rm loc}:=\sum_rc_r,
 \quad Q_{\rm loc}:=\sum_rQ_r,\quad F_{\rm loc}:=\sum_rf_r.
\]

Let `d_tile` be the exact polygon-dissection deficit from Section 123, and let
`e_BB`, `k`, `s_C`, and `q` have their canonical loaded-hull meanings. Then the
following are finite identities, with all outer walks occurrence-counted:

\[
\boxed{
 S_{\rm out}
 =2\sum_r(a_r-d_r)+2(e_{BB}-k)-2d_{\rm tile}
  -2C_{\rm loc}-Q_{\rm loc}.
}
\tag{AD.3}
\]

After adding the actual exceptional-face perimeters,

\[
\boxed{
 \sum_r(L_r+P_{{\rm exc},r}-2d_r)
 =2\sum_r(a_r-d_r)+2(e_{BB}-k)-2d_{\rm tile}
  -2C_{\rm loc}+4F_{\rm loc}.
}
\tag{AD.4}
\]

The degree defect `Q_loc` cancels exactly in (AD.4). Equivalently, with

\[
 \mu_DD:=e_{BB}+2s_C-3k,
\]

the detour itself is

\[
\boxed{
 S_{\rm out}
 =6q-12-2\mu_DD-4k-2\sum_rd_r
  -4d_{\rm tile}-2C_{\rm loc}-Q_{\rm loc}.
}
\tag{AD.5}
\]

In particular, the exact safe upper bound

\[
 S_{\rm out}
 \le 2\sum_r(a_r-d_r)+2(e_{BB}-k)
 \tag{AD.6}
\]

and the equivalent bound

\[
 S_{\rm out}
 \le 6q-12-2\mu_DD-4k-2\sum_rd_r
 \tag{AD.7}
\]

follow by discarding only nonnegative terms.

### Scope

This is a finite identity for the actual source-derived harmonic cells of the
canonical representative. It is not a statement about a scaffold, selected
carrier, or abstract train complex. The cells may have shared boundary vertices;
`C_loc` is counted with the same local multiplicity as the `c_r` in the induced
graphs. The source retains every contact-isolated point, although such points do
not enter these positive-contact ledgers. No affine-kernel statement is applied to
isolated coordinates. The identities do not assume that local outer walks are
globally injective or simple.

## 3. Proof

### 3.1 Local face algebra

Canonical Section 82 gives, for each induced harmonic graph,

\[
 L_r+Q_r=4a_r-6-2s_r-2c_r.
 \tag{AD.8}
\]

Define the nonnegative augmented-cell defect

\[
 \eta_r:=a_r-3-s_r\ge0.
 \tag{AD.9}
\]

Substituting `s_r=a_r-3-eta_r` into (AD.8) gives

\[
 L_r=2a_r+2\eta_r-2c_r-Q_r.
 \tag{AD.10}
\]

Subtracting `2d_r` and summing yields

\[
 S_{\rm out}
 =2\sum_r(a_r-d_r)+2\sum_r\eta_r
  -2C_{\rm loc}-Q_{\rm loc}.
 \tag{AD.11}
\]

No asymptotic estimate or boundary simplification is used here.

### 3.2 The augmented-cell ledger evaluates the total defect

Section 123 proves locally, after adding the attachment polygon sides,

\[
 \eta_r={a_r-T_r+Q_r^+\over2},
 \tag{AD.12}
\]

where `T_r` is the number of augmented triangular faces and `Q_r^+` is the
augmented degree-above-four defect. Its exact global dissection identity is

\[
 e_{BB}-k
 ={1\over2}\sum_r(a_r-T_r+Q_r^+)+d_{\rm tile}.
 \tag{AD.13}
\]

Therefore

\[
 \sum_r\eta_r=e_{BB}-k-d_{\rm tile}.
 \tag{AD.14}
\]

Insert (AD.14) into (AD.11). This proves (AD.3).

The proof only uses the same local occurrences on both sides. In particular, no
claim that a loaded-loaded edge belongs to at most one attachment cell is needed.

### 3.3 Exceptional-face cancellation

By definition of `Q_r` and `f_r`,

\[
 P_{{\rm exc},r}=4f_r+Q_r.
 \tag{AD.15}
\]

Adding (AD.15) to the componentwise version of (AD.10) gives

\[
 L_r+P_{{\rm exc},r}-2d_r
 =2(a_r-d_r)+2\eta_r-2c_r+4f_r.
 \tag{AD.16}
\]

Summation and (AD.14) prove (AD.4). This is why replacing `P_exc` by a coarse
bound such as `5Q_r` before summation loses an exact cancellation.

### 3.4 Elimination of attachment incidence

Section 123 defines

\[
 d_{\rm tile}=q-2-a+2c_I,
 \tag{AD.17}
\]

where `c_I` is the number of unloaded positive-contact components. Hence

\[
 a=q-2+2c_I-d_{\rm tile}.
 \tag{AD.18}
\]

The pinned ledger is

\[
 c_I+e_{BB}+s_C=q-2+k.
 \tag{AD.19}
\]

Eliminating `c_I` in (AD.18) gives

\[
 a=3q-6+2k-2e_{BB}-2s_C-d_{\rm tile}.
 \tag{AD.20}
\]

Use `sum_r(a_r-d_r)=a-sum_r d_r` in (AD.3) and substitute (AD.20). The result is

\[
 S_{\rm out}
 =6q-12+2k-2e_{BB}-4s_C-2\sum_rd_r
  -4d_{\rm tile}-2C_{\rm loc}-Q_{\rm loc}.
 \tag{AD.21}
\]

Since

\[
 -2\mu_DD-4k
 =-2(e_{BB}+2s_C-3k)-4k
 =2k-2e_{BB}-4s_C,
\]

(AD.21) is exactly (AD.5).

## 4. Exact frontier effect

The canonical endpoint can now be restated without treating the outer detour as an
independent route quantity:

\[
 \liminf {1\over D}
 \left(
 2\sum_r(a_r-d_r)+2(e_{BB}-k)-2d_{\rm tile}
  -2C_{\rm loc}-Q_{\rm loc}
  +4F_{\rm loc}
 \right)
 \ge {\pi\over2}(2-\sqrt3).
 \tag{AD.22}
\]

This is an exact source-level tradeoff between attachment geometry and the global
loaded-hull currency. It identifies three favorable deficits (`d_tile`, `C_loc`,
and `Q_loc` in (AD.3)) that any future upper-bound theorem can exploit. It also
shows that the exceptional-face degree does not need to be paid a second time in
(AD.4).

It does not yet provide a numerical contradiction. The canonical estimates do not
currently give a sharp enough upper bound on `q`, `sum d_r`, `sum(a_r-d_r)`, or the
combination of `mu_D` and `k` in (AD.5). It also does not convert the identity into
a finite same-cardinality strict competitor.

The macroscopic-container/exterior-cap branch is untouched.

## 5. Exact remaining lemma

One precise next target is:

> In the full-core near-disk branch, prove a uniform source-level upper bound for
> the right side of (AD.4), using the disjoint inscribed attachment cells and the
> actual loaded diameter geometry, that is strictly smaller than the Section-122
> lower bound for all sufficiently large representatives; or construct a strict
> same-cardinality sub-`D(n)` competitor from the positive deficits in (AD.3).

The required theorem must control the actual `d_tile`, `C_loc`, and repeated
occurrences, and must retain isolated source points in any competitor.

## 6. Claim audit table

| Claim | Status | Dependencies | Reason |
|---|---|---|---|
| (AD.8) local face identity | canonical input | `C-HARMONIC-CARRIER-QUAD`, Section 82 | occurrence-counted Euler identity |
| (AD.12) local augmented-cell defect | canonical input | `C-AUGMENTED-CELL-DEFECT-BUDGET`, Section 123 | exact augmented Euler ledger |
| (AD.13) global defect ledger | canonical input | `C-AUGMENTED-CELL-DEFECT-BUDGET`, Section 123 | exact cell dissection |
| (AD.3) exact detour identity | audited-working | preceding rows | direct substitution; no asymptotics |
| (AD.4) exceptional-face cancellation | audited-working | (AD.3), definition of `P_exc` | exact `4f+Q` cancellation |
| (AD.5) surplus form | audited-working | Sections 62, 123 | finite algebra |
| (AD.6)–(AD.7) upper bounds | audited-working | nonnegativity of `d_tile,C_loc,Q_loc,k` | no omitted sign assumption |
| C-II closure | open | unresolved source-level upper bound/deformation | no final quantifier discharged |

## 7. Regression checks

| Regression/correction | Result | Exact hypothesis or failure |
|---|---|---|
| Repeated outer walks and bridges | pass | `L_r` is used only through canonical occurrence-counted identities |
| Shared attachment vertices/cells | pass | `C_loc` retains local multiplicity; no global edge injectivity is assumed |
| Contact-isolated points | pass | they remain in the full source and are absent only from the positive-contact ledgers |
| Loaded-loaded contacts in multiple cells | pass | multiplicity appears in `C_loc` with the favorable negative sign |
| No unloaded components | pass | all sums vanish and (AD.3) reduces using `d_tile=q-2` and the pinned ledger |
| Near-equilateral oblique lattice | pass | no affine or angle-gap conclusion is inferred |
| Scalar near-floor compatibility witness | pass | it demonstrates that the identity alone is not a contradiction |
| Macroscopic inactive chamber | uncovered | this theorem uses only the full-core harmonic-cell branch |

## 8. Literature imports

None.

## 9. Computation

None was needed. The reduction is finite algebra over canonical identities. Any
future numerical optimization of (AD.4) must be run on `homelab` and cannot be used
as a proof without an exact certificate.

## 10. Promotion recommendation

**audited-working.** The identity has an independent hostile audit in
`docs/audits/target_c_exact_aggregate_detour_decomposition_independent_audit_2026-09-14.md`.
It should not be admitted as a canonical Level-I closure because it supplies no
upper bound strong enough to contradict (AD.1) and no source-preserving competitor.

## 11. Handoff

1. Strongest result: exact identities (AD.3)–(AD.5) for the actual full-core source.
2. Canonical chain: `C-HARMONIC-CARRIER-QUAD` → `C-AUGMENTED-CELL-DEFECT-BUDGET` → this reduction.
3. Exact remaining lemma: quantitatively upper-bound (AD.4), or turn its favorable deficits into a strict source-preserving descent.
4. Binding dead route: scalar optimization without a planar/source-level bridge.
5. Read next: `docs/targets/target-c/122-aggregate-two-arc-detour-audit.md`, `docs/targets/target-c/123-augmented-cell-defect-budget-audit.md`, and `docs/targets/target-c/84-typeII-interface-collapse-audit.md`.
