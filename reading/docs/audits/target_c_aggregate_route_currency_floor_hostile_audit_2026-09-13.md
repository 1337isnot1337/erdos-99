> Generated reading edition · [exact source](../../../docs/audits/target_c_aggregate_route_currency_floor_hostile_audit_2026-09-13.md) · source SHA-256 `a81c66e09dfd8f6e95e1444c4d771c4c406809ab5c4f5fe6de2bae7988030d72`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-11808062A4AC","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Hostile audit — aggregate route-currency floor

**Date:** 2026-09-13
**Reviewed:** `research/target_c_aggregate_route_currency_floor_2026-09-13.md`
**Disposition:** PASS at proof-only endpoint/common-cap scope; no C-II closure.
**Theorem state:** unchanged at `2026-09-12.audit.46`.

## 1. Scope of the diameter-moment input

The lower bound

```math
 d_\Sigma/D\ge S_*-o(1),
 \qquad S_*=2.798596312209462\ldots,
```

is imported only on the Section-118 endpoint/common-cap profile. It is not an
all-Type-II theorem. The reviewed note states this restriction in its introduction,
derivation, and disposition; no universal Type-II conclusion is taken from `S_*`.

**Verdict:** pass.

## 2. Face-incidence and contact-reuse signs

Section 121's exact identity is

```math
E_\Sigma=4\Delta_R+4f+2(q-k-e_{BB}+C_{\rm att})-2d_\Sigma.
```

In Type II, `c_B=0` and disjoint attachment cells imply `C_att<=e_BB`. Thus

```math
E_\Sigma\le4\Delta_R+4f+2(q-k)-2d_\Sigma.
```

The inequality direction is correct: replacing `C_att` by `e_BB` enlarges the right
side. The proof does not identify local exceptional-face occurrences across cells.

**Verdict:** pass.

## 3. Outer-ledger substitution

From `b+Q=2(q-k)` and
`delta_D=(b-per(F))/D`,

```math
Q/D=2(q-k)/D-per(F)/D-\delta_D.
```

Since `P_exc=Q+4f`, the upper side becomes

```math
E_\Sigma/D
\le P_{\rm exc}/D+per(F)/D+\delta_D-2d_\Sigma/D+o(1).
```

Combining the Section-122 lower bound `E_\Sigma/D>=c_0-o(1)` with the scoped
`d_\Sigma/D>=S_*-o(1)` and `per(F)/D->pi` gives

```math
\liminf(P_{\rm exc}/D+\delta_D)\ge2S_*+c_0-\pi.
```

No division by a possibly vanishing diameter or reversal of a liminf inequality is
used.

**Verdict:** pass.

## 4. Numerical and closure boundary

The verifier uses the safe enclosures `S_*>2.7985`, `pi<3.14160`, `pi>3.14159`, and
`sqrt(3)<1.73206` to obtain a strict lower margin above `2.8762`. The displayed
`2.876493578...` is an evaluation, not the certified inequality used in the proof.

The result is a lower bound on route currency. It supplies no upper bound on outer
detour or exceptional perimeter, no strict-diameter competitor, and no exact unit
equilateral triangle. Other Type-II profiles and the Type-I branch remain untouched.

**Final verdict:** PASS as a proof-only endpoint/common-cap composition. C-II remains
open.
