> Generated reading edition · [exact source](../../research/target_c_gapwise_local_slack_payment_hostile_audit_2026-09-12.md) · source SHA-256 `ac234ccd85a7be7ead5a4731b8d3eefe9ad5cb60a2c268a257cb73f20afff63d`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "f9b80aedb8db64eb6436b323d4399d5b6419d5eb", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_gapwise_local_slack_payment_hostile_audit_2026-09-12.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "5b82ea27d7a946053c75a628c33e8bdffbe13354f3a08d8c45493377d227fc38"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — gapwise local-slack payment

**Date:** 2026-09-12  
**Reviewed:** `target_c_gapwise_local_slack_payment_2026-09-12.md`  
**Disposition:** PASS after repairing one missing plus sign; proof-only scope retained.  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The report gives a valid groupwise refinement of the retained-remainder payment on
the stated Section-118 sharp wrapping window. It does not close C-II. The displayed
inequality (GLS.3) had a transcription error: the two lower bounds combine by a
maximum, which is `3 lambda + 2(C_loc sqrt(a)-lambda)_+`, not a subtraction. The
source and its verifier are repaired together below.

## 1. Groupwise local charge

For a group `j`, let `S_j=sum d_r`, `G_j=sum(r_r+eta_r)`, and let `A_j` be its
internal strict-rhombus area. The audited local area/slack argument gives

`S_j+G_j >= C_loc sqrt(a_j) D-o(D)`

when `A_j >= (a_j-o(1))D^2`. The group summation error is `o(D)` because the total
number of positive-contact components is `O(D^(2/3))`; no per-cell convergence rate
is needed. Also `S_j>=lambda_j D-o(D)` is an independently supplied group diameter
floor.

Therefore

`3S_j+2G_j = S_j+2(S_j+G_j)`

has the two valid lower bounds

`3lambda_j D-o(D)` and
`(lambda_j+2 C_loc sqrt(a_j))D-o(D)`.

Taking their maximum gives exactly

`3S_j+2G_j >= [3lambda_j + 2(C_loc sqrt(a_j)-lambda_j)_+]D-o(D)`.

The repaired plus sign is load-bearing; the arithmetic verifier already evaluated
the maximum form.

## 2. Endpoint inputs and disjointness

The four groups used in the endpoint specialization are the wrapping carrier and the
three principal gap groups from the audited Section-140/118 sharp-window geometry.
Their listed area floors and diameter floors are used as inputs, not optimized
independently. The groups are disjoint by the gap-cell convex-separation theorem, so
their `S_j` and `G_j` charges can be summed; all omitted groups contribute
nonnegative quantities.

The local coefficient

`C_loc=4 sqrt(pi)/5 + 2/(5 sqrt(sqrt(3)/2))`

is the audited internal-face coefficient. It is applied to unloaded-only strict
rhombi in the same harmonic components as the diameter floors. Contact-isolated
source points remain outside the core rigidity statements.

## 3. Section-161 composition

The audited retained-remainder inequality is

`5h-2d_H-7s_Z >= 3S_D+2G_D+c_*D-o(D)`.

Summing the four groupwise lower bounds and inserting `c_*` gives the displayed
`9.1819490263...` endpoint coefficient. Since `d_H,s_Z>=0`, this implies the
corresponding h-only lower bound shown in the source, but it does not produce an
upper bound or a strict-diameter competitor.

## 4. Arithmetic and limitations

The accompanying script recomputes the circular-segment values, all four positive
parts, the extra large-gap payment, and the final coefficient. Its floating-point
checks certify only the displayed arithmetic; they do not certify the geometric
sharp-window hypotheses or global optimality.

The result is a scoped proof-only tradeoff. It does not handle separated wrapping
parameters, the positive outer-detour branch, Type I, or the source-level descent
needed for C-II closure.

**Classification:** audited-working proof-only groupwise tradeoff; theorem state
unchanged; C-II remains open.
