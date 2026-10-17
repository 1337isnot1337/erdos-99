> Generated reading edition · [exact source](../../../docs/reports/target_c_zr_trunk_forces_linear_surplus_2026-09-09.md) · source SHA-256 `e395285fc72b9337ea53791f09d6c82309598a6d08e02d33841f8d1d7dc9f5a0`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 2 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-0324B25076B2","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — ZHL: a macroscopic bridge trunk forces linear post-ZF component surplus

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-deep-harmonic-capture`  
**Run type:** closing-proof continuation / post-ZF ledger synthesis  
**Target:** Target C, Gate C-II / Level I  
**Depends on:** ZHT/ZHH and current-main component slack cancellation  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

Current `main` adds the exact post-ZF component ledger

```math
\sum_r\delta_r+R_I+s_B+3(d_H+s_Z)
=6+e_{BB}+2s_C.
\tag{1}
```

ZHT, in the bridge-dominant near-zero phase, produces one unloaded harmonic component `I_*` containing a consecutive macroscopic bridge trunk of length

```math
H\ge\frac{\eta^2}{16\pi}D.
\tag{2}
```

This report joins the two statements. The response-visible `z--y` path through `I_*` must cross every trunk bridge. Since the internal vertices of that path lie in `I_*`, only the first and last trunk bridge can possibly be attachment contacts; every other trunk bridge lies inside `C[I_*]`. Therefore the internal contact graph of `I_*` has graph diameter at least `H-2`.

Substitution into (1) forces a linear amount of the exact post-ZF surplus `e_BB+2s_C`. Thus the bridge-dominant small-defect branch is disjoint from the sublinear-surplus phase analyzed by the current-main force-area/gap reports.

---

## 1. Post-ZF component notation

For each unloaded contact component `I_r` of `C[V\setminus B]`, current `main` writes

- `delta_r` for the graph diameter of `C[I_r]`, zero for a singleton;
- `e_r` for internal contacts;
- `t_r` for attachment contacts to `B`;
- `s_r=e_r+t_r-2|I_r|-1>=0` for extra pinned-stress dimension;
- `r_r=2|I_r|-delta_r-2-e_r>=0` for Eppstein slack.

The global sums are

```math
s_C=\sum_rs_r,
\qquad
R_I=\sum_rr_r.
\tag{1.1}
```

Also

```math
s_B=3q-e_{BI}-2e_{BB}\ge0,
\qquad
k:=d_H+s_Z\ge0.
\tag{1.2}
```

The exact component-slack cancellation theorem on current `main` gives

```math
\boxed{
\sum_r\delta_r+R_I+s_B+3k
=6+e_{BB}+2s_C.
}
\tag{1.3}
```

---

## 2. The ZHT trunk is internal to one unloaded component except at its two ends

Assume

```math
S_{br}\ge\eta D^2,
\qquad
D\varepsilon\to0.
\tag{2.1}
```

ZHT supplies an unloaded component `I_*`, attachment set `A_*`, and an actual diameter pair

```math
z,y\in A_*
\tag{2.2}
```

such that a contact path `P` from `z` to `y` has all internal vertices in `I_*` and crosses a complete bridge-tree trunk

```math
f_1,\ldots,f_H,
\qquad
H\ge\frac{\eta^2}{16\pi}D.
\tag{2.3}
```

Every `f_j` is a physical bridge of the complete contact graph and belongs to the closure `E_*` of `I_*`.

The path `P` has the form

```math
z\ --\ I_*\ --\ y,
\tag{2.4}
```

with exactly one attachment edge incident to `z` at its beginning and one attachment edge incident to `y` at its end; every other edge of `P` has both endpoints in `I_*`.

Because every trunk bridge separates `z` from `y`, every `f_j` occurs on `P`. Therefore at most two trunk bridges can fail to be internal edges of `C[I_*]`: one may be the initial attachment contact at `z`, and one may be the final attachment contact at `y`.

Thus at least

```math
H-2
\tag{2.5}
```

physical trunk bridges are internal edges of `C[I_*]` and separate successive portions of any internal path joining the corresponding interior endpoint regions.

Consequently:

### Theorem ZHL.1 — component diameter from the trunk

```math
\boxed{
\delta_*:=\operatorname{diam}_{C[I_*]}(I_*)
\ge H-2.
}
\tag{ZHL1}
```

In particular,

```math
\boxed{
\delta_*
\ge
\frac{\eta^2}{16\pi}D-2.
}
\tag{ZHL2}
```

### Proof detail

Remove the possible first and last attachment edges from `P`. The remaining internal `I_*` subpath crosses every internal trunk bridge. A contact bridge separates its two sides, so a path crossing `H-2` distinct internal bridges contains at least `H-2` internal contact edges. Hence the distance in `C[I_*]` between the first and last interior vertices of `P` is at least `H-2`, proving ZHL1.

---

## 3. Exact linear-surplus lower bound

Apply the global component ledger (1.3). Since every term except `sum delta_r` on the left is nonnegative,

```math
6+e_{BB}+2s_C
\ge
\sum_r\delta_r+3k
\ge
\delta_*+3k.
\tag{3.1}
```

Using ZHL1,

```math
\boxed{
 e_{BB}+2s_C
\ge
H-8+3(d_H+s_Z).
}
\tag{ZHL3}
```

In particular,

```math
\boxed{
 e_{BB}+2s_C
\ge
\frac{\eta^2}{16\pi}D-8.
}
\tag{ZHL4}
```

Thus along every bridge-dominant near-zero sequence,

```math
\boxed{
\liminf\frac{e_{BB}+2s_C}{D}
\ge
\frac{\eta^2}{16\pi}>0.
}
\tag{ZHL5}
```

The post-ZF component surplus is necessarily linear.

---

## 4. Consequence for the current-main force-area split

Current `main` defines

```math
\lambda_2:=\limsup\frac{e_{BB}+2s_C}{D}
\tag{4.1}
```

and proves the upgraded force-hull gap bound

```math
\liminf\frac G{D^2}
\ge
\frac12\sin1-rac\pi4\lambda_2^2.
\tag{4.2}
```

ZHL shows that the bridge-dominant near-zero branch cannot lie in the sublinear-surplus regime `lambda_2=0`. More precisely, for fixed bridge-stress fraction `eta`,

```math
\lambda_2\ge\frac{\eta^2}{16\pi}.
\tag{4.3}
```

This does **not** by itself contradict the gap theorem: increasing `lambda_2` weakens the right side of (4.2). The value of ZHL is a clean phase separation:

```text
bridge-dominant + D epsilon -> 0
    => one long internal harmonic component
    => e_BB+2s_C = Omega_eta(D).

Therefore the current-main low-surplus macroscopic-gap phase and the ZHT trunk phase
are disjoint.
```

A complete proof can now treat the bridge-dominant near-zero branch only inside the **linear-surplus** side of the post-ZF ledger.

---

## 5. Componentwise exact identity inside `I_*`

The same current-main report proves, for each component,

```math
\boxed{
 t_*-\delta_*-3=s_*+r_*.
}
\tag{5.1}
```

where `t_*` is its attachment-contact count.

Using ZHL1,

```math
\boxed{
 t_*
\ge
H+1+s_*+r_*.
}
\tag{ZHL6}
```

Thus the long trunk demands at least `H+1` attachment incidences even before any local pinned-stress or Eppstein slack is present. This independently matches the ZHA attachment injection at the incidence level; any extra component stress dimension or internal penny-graph deficit increases the required attachment count exactly one-for-one.

Since every loaded terminal has contact degree at most three, `t_*<=3|A_*|`, so

```math
|A_*|
\ge
\frac{H+1+s_*+r_*}{3}.
\tag{5.2}
```

The direct ZHA bridge-tree injection remains stronger in the zero-slack case (`|A_*|>=H+1`), while ZHL6 is stronger as an exact bookkeeping identity for additional component defects.

---

## 6. Exact target implication

The bridge-dominant near-zero phase now simultaneously has:

- a single harmonic component with `delta_*=Omega_eta(D)`;
- a consecutive `Omega_eta(D)` bridge trunk of `Omega_eta(D)` stress per bridge;
- `e_BB+2s_C=Omega_eta(D)` globally;
- `t_*-delta_*-3=s_*+r_*` exactly inside the captured cell;
- the ZHA linear attachment/short-response matching;
- the ZHN axial local-degeneration normal form for almost every trunk block.

Therefore no proof of this branch should continue using the post-ZF **sublinear-surplus** estimates. The remaining ledger target is explicitly a linear-surplus theorem.

A useful next dichotomy is:

1. `e_BB=Omega(D)`: exploit the geometry of linearly many unit contacts among loaded convex-hull terminals;
2. `s_C=Omega(D)`: exploit linearly many extra pinned-stress dimensions inside unloaded components, with `I_*` already consuming linear graph diameter.

Either route that yields one extra unit of exact face/boundary currency beyond the ZF identity closes Level I.

---

## 7. Regressions and limits

- ZHL does not upper-bound `lambda_2`; it only excludes `o(D)` surplus in the trunk phase.
- Linear loaded-loaded contact count is geometrically possible in convex polygonal shells.
- Linear pinned-stress surplus is possible in rhombic meshes.
- The force-area gap weakens as `lambda_2` grows, so no area contradiction follows from ZHL alone.
- Fully inactive rattlers remain outside the component ledger.

---

## 8. Dependencies

- ZHT/ZHH stacked in PR #111;
- current-main `target_c_component_slack_cancellation_2026-09-09.md`;
- C35 loaded degree bound only for the optional incidence-to-distinct-attachment estimate.

No new external literature is imported.

---

## 9. Promotion recommendation

**Hold as report.** It is downstream of report-level ZR/ZF and stacked PR #108/#111.

---

## 10. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Current main proves
    sum_r delta_r + R_I + s_B + 3(d_H+s_Z)
      = 6+e_BB+2s_C.

ZHT gives one harmonic cell I_* containing H>=eta^2 D/(16pi) consecutive bridge edges
on a z--y contact path through I_*. At most the first and last trunk bridge can be
attachment contacts; the other H-2 are internal bridges of C[I_*]. Hence
    delta_* >= H-2.

Substitution gives exactly
    e_BB+2s_C >= H-8+3(d_H+s_Z),
so in particular
    liminf (e_BB+2s_C)/D >= eta^2/(16pi).

Thus bridge-dominant + D epsilon->0 is necessarily a linear post-ZF surplus phase; it
cannot live in the sublinear-surplus macroscopic-gap branch.

Componentwise,
    t_*-delta_*-3=s_*+r_*,
so
    t_* >= H+1+s_*+r_*.

Next branch split:
- e_BB=Omega(D): use linearly many loaded-loaded unit contacts;
- s_C=Omega(D): use linearly many extra pinned stress dimensions.
```
