> Generated reading edition · [exact source](../../../docs/reports/target_c_zf_zero_transfer_forest_charge_2026-09-11.md) · source SHA-256 `9012238b40004b2a881ecb192d8223325ee814d65e3162ceecd15ffba95dbc00`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-A51075B4DDAD","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — ZF/zero-transfer forest charge

**Date:** 2026-09-11  
**Target:** Target C, C-II  
**Status:** report-level theorem; unpromoted  
**Dependencies:** ZF boundary-surplus collapse, Eppstein surplus coupling, C56-Z/C58 zero-transfer star-forest theorem, and the report-level forest surplus floor.

## Level-I status

`STILL OPEN`.

This report records one exact combination that was not present in the preceding
branch ledger. It separates the population-spanning escape from the zero-transfer
forest escape and gives a linear component charge in the latter. It does not supply
the missing upper tradeoff for the surplus currency.

## Theorem 1 — surplus-to-boundary-defect identity

Let (v,e,h,q,d_H,s_Z,x_B,Q) have the post-ZF meanings in the active Target C
ledger. Then

```math
h=x_B+Q+d_H+2s_Z,
\tag{1}
```

and Eppstein's triangle-free penny-graph bound gives

```math
\boxed{
x_B+Q+d_H+s_Z
\ge c_E\sqrt v-(C_E+2),
\qquad c_E=\tfrac12\sqrt{2\pi\sqrt3}.}
\tag{2}
```

### Proof

The exact post-ZF incidence identity is

```math
q=x_B+Q+2(d_H+s_Z),
\tag{3}
```

while the diameter topology gives (q=h+d_H). Subtracting gives (1).
Eppstein's bound is

```math
e\le2v-c_E\sqrt v+C_E.
```

Since (s_Z=e+h-(2v-2)), rearrangement gives

```math
h\ge s_Z+c_E\sqrt v-(C_E+2).
```

Insert (1) and cancel one (s_Z), obtaining (2). No source point is removed in
this calculation. (square)

If the contact-isolated population is (o(D^2)), then
(v/D^2	oDelta_2=pi/(2\sqrt3)), and (c_E\sqrt{\Delta_2}=pi/2). Hence

```math
\boxed{
\liminf_{D\to\infty}
\frac{x_B+Q+d_H+s_Z}{D}\ge\frac\pi2.}
\tag{4}
```

This is a full-source statement: the alternative to (4) is a quadratic
contact-isolated population, not a missing estimate on (h).

## Theorem 2 — zero-transfer forest charge

Assume in addition (s_Z=0), the diameter graph is in the forest branch, and the
selected full-support stress is in the exact zero-transfer phase

```math
Q^{\mathsf T}\Lambda^+Q=B_H^{-1}.
\tag{5}
```

Then, for all sufficiently large survivors:

1. (H) is a star forest, every star has at most five edges, and
   (d_H\ge D/5+O(1));
2. with (L=e_{BB}+2s_C), the report-level forest surplus floor gives

```math
\boxed{
\frac LD\ge 0.597+\varepsilon_{597}+\frac35-o(1).}
\tag{6}
```

### Proof

Equation (5) is the C56-Z hypothesis. The C58 zero-transfer theorem gives that
each connected component of (H) is a star and that its degree is at most five.
The Woodall forest classification gives (d_H) components and (q=h+d_H). Since
each component has at most five edges,

```math
h\le5d_H.
\tag{7}
```

The audited ZF edge/diameter comparison gives (h\ge\lceil D\rceil). Thus

```math
d_H\ge h/5\ge D/5+O(1).
\tag{8}
```

In the (s_Z=0) forest circuit phase the exact surplus variable is

```math
\nu_D=\frac{e_{BB}+2s_C-3d_H}{D},
```

and the explicit detour theorem gives
(liminf\nu_D\ge0.597+arepsilon_{597}). Therefore

```math
\frac LD=\nu_D+3\frac{d_H}{D}
\ge0.597+arepsilon_{597}+\frac35-o(1),
```

which is (6). (square)

## What this does not prove

The lower bound (6) is not a contradiction. (L=e_{BB}+2s_C) is a combinatorial
surplus currency, and the current theory proves no upper bound (L/D<1.197), or
any opposing hub-block inequality, in this branch. The common 2-connected contact
block cannot be treated as a bridge: the regular-hexagon response has a negative
off-diagonal transfer for opposite diameter pairs.

The branch ledger remains:

* cyclic (s_Z=0): high-surplus lower bound but no upper tradeoff;
* forest (s_Z=0): (6) in the exact zero-transfer subbranch, while generic
  transfer remains a caterpillar/hub problem;
* (s_Z>0): extreme stresses omit rows, but no zero-multiplier-to-release theorem
  exists; isolate-heavy and giant-face alternatives remain.

The exact missing implication is therefore still a global upper tradeoff or a
strict sub-(D) competitor, not another lower bound on (L).

## Regression audit

* The star-forest conclusion is conditional on exact C56-Z; it is not applied to
  arbitrary forest diameter graphs.
* The (h\ge D) input is the ZF/Eppstein comparison, not the weaker endpoint count
  (q\ge D/2).
* Contact-isolated points are retained in Theorem 1; Theorem 2 concerns only the
  actual contact/diameter core and does not declare isolates diametral.
* The regular odd-shell family is not excluded: it is not in the forest
  zero-transfer branch and lacks a large-(n) global-optimality certificate.
