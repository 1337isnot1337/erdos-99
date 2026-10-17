> Generated reading edition · [exact source](../../../docs/reports/target_c_strict_fullcore_interface_corollaries_2026-09-09.md) · source SHA-256 `8d6d99a31cf54c47ddd0ba7882dee1c72e6cf7b9b85ae4d0d2fee9388acbbf02`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-F3131F85B0A3","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — strict full-core interface gap propagates to stress and diameter support

**Date:** 2026-09-09  
**Repository branch:** `research/fullcore-interface-perimeter-2026-09-09`  
**Run type:** exact-ledger corollary  
**Target:** full-core near-circle endpoint after HA  
**Depends on:** HA sharp-interface exclusion, HBd exact near-circle identities  
**Computation:** displayed baseline decimal only

## LEVEL I STATUS

`STILL OPEN`

HA proves that the GP coefficient two is uniformly unattainable: there exists an absolute `eta_IF>0` such that every sufficiently large full-core near-circle survivor satisfies

```math
Q_B\ge(2+\eta_{IF})D-o(D).
\tag{SC.1}
```

Since `Q>=Q_B`, HBd's exact near-circle identity

```math
Q+2s_C=(\pi+o(1))D
\tag{SC.2}
```

gives

```math
\boxed{
s_C
\le
\frac{\pi-2-\eta_{IF}}2D+o(D).}
\tag{SC.3}
```

HBd also gives

```math
d_H+s_Z=s_C+o(D),
\tag{SC.4}
```

so

```math
\boxed{
d_H+s_Z
\le
\frac{\pi-2-\eta_{IF}}2D+o(D).}
\tag{SC.5}
```

In particular

```math
\boxed{d_H
\le
\frac{\pi-2-\eta_{IF}}2D+o(D).}
\tag{SC.6}
```

Since `d_H=q-h` and `q=(\pi+o(1))D`,

```math
\boxed{
h
\ge
\frac{\pi+2+\eta_{IF}}2D-o(D).}
\tag{SC.7}
```

Thus the full actual diameter graph has a strict linear separation above the baseline coefficient

```math
\frac{\pi+2}{2}
=2.57079632679\ldots .
```

The same `eta_IF/2` improves the baseline upper bound on the cycle-edge deletion count in the TC maximal-thrackle completion.

No numerical value of `eta_IF` is claimed. HA proves existence by excluding every sequence with `Q_B/D->2`; quantifying it requires explicit stability estimates not yet established.

---

## 1. Direct derivation

Equation SC.1 and nonnegativity of internal face defect give

```math
Q\ge Q_B\ge(2+\eta_{IF})D-o(D).
```

Insert in SC.2:

```math
2s_C
=(\pi+o(1))D-Q
\le(\pi-2-\eta_{IF})D+o(D),
```

which is SC.3.

Equation SC.4 and `s_Z>=0` give SC.5-SC.6. Finally

```math
h=q-d_H
```

and `q=(pi+o(1))D` give SC.7.

---

## 2. Why this corollary matters

Before HA, GP alone supplied only

```math
Q_B\ge2D-o(D),
```

which allowed the baseline limiting values

```math
s_C/D\to\frac{\pi-2}{2},
\qquad
h/D\to\frac{\pi+2}{2}.
```

HA eliminates that entire equality package. Therefore any future compactness argument at the baseline diameter-support coefficient may treat it as a forbidden limit, exactly as HKN treats the scalar Hemmi threshold on PR #130.

This is useful even before `eta_IF` is explicit: a proposed extremizing sequence whose other inequalities force `h/D` down to `(pi+2)/2` is automatically impossible by HA.

---

## 3. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| existence of `eta_IF>0` | proved by HA diagonal exclusion |
| SC.3--SC.7 | proved | direct HBd exact-ledger substitution |
| explicit value of `eta_IF` | not proved | stability moduli remain qualitative |
| Level I | still open | strict gap may still fit below the global `q~pi D` budget |

---

## 4. Next target

Quantify `eta_IF`, or combine SC.7 with an independent upper bound on `h/D` in the same full-core near-circle phase. A coefficient upper bound below `(pi+2)/2+eta_IF/2` would close that phase without needing to quantify every intermediate interface constant.
