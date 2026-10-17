> Generated reading edition · [exact source](../../../docs/reports/target_c_disjoint_gap_followup_notes_2026-09-09.md) · source SHA-256 `1d1b82569c28df154fc1f340021036f65e55c3cae882e8ed804fab9856eb3cab`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-469DA84542AD","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# DG follow-up target notes

**Date:** 2026-09-09  
**Base theorem:** `target_c_disjoint_diameter_gap_outerwalk_collapse_2026-09-09.md`  
**Status:** research notes; no Level I claim

The new DG theorem leaves two quantitative post-ZF branches.

1. `x_B=Omega(D)`: the excess length of the outer contact walk is itself linear.
2. `x_B=o(D)`: `q/D->pi`, `per(F)/D->pi`, `min width(F)/D->1`, `area(F)>=D^2/2-o(D^2)`, `h/D>=3pi/5`, and `(Q+2s_Z)/D>=pi/5`.

The highest-value next steps are therefore:

- derive a finite packing/topology charge from `x_B`, preferably using the outer-pocket decomposition OP rather than raw perimeter;
- in the near-constant-width phase, exploit the incompatibility between an almost width-`D` hull and linear exceptional-face or mixed-row defect;
- keep `Q` and `s_Z` separate: `Q` is geometric face boundary, while `s_Z` is extra mixed-framework left-nullity.

A useful target inequality would be one of

```math
Q \le c\,x_B+o(D)
```

with a constant forcing `s_Z` linear, followed by a stress-rank contradiction, or

```math
Q+2s_Z\le \frac\pi5D-\epsilon D
```

under `min width(F)=D-o(D)`, which would directly contradict DG.7.

No such inequality is proved in this note.
