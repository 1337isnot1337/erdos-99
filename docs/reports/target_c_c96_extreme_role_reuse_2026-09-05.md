<!-- theorem-state: {"artifact_id":"ART-0BD7401A94AC","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C96 extreme-role reuse at endpoint equality

**Date:** 2026-09-05  
**Repository state:** `eaf220a9` (`main`)  
**Run type:** exact finite equality-case sharpening  
**Target:** Target C C87–C96 common-cut endpoint floor  
**External web search:** not used  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

## 1. Starting point

The C96 endpoint-representative audit defines

`R_rep=sum_k[(l_k-1)+(u_k-1)]`

and, for the selected `2D` paired diameter edges plus the chain diameter `za`, proves

`c_sel = 3+R_rep-c_ext`,

where `c_ext=c_z+c_a` counts the number of extreme arc roles occupied by the actual chain endpoints `z,a`.

At the exact endpoint floor `q=2D+2`, the selected common-cut graph is one spanning tree, so

`c_sel=1`,

hence

`c_ext=R_rep+2`, `R_rep in {0,1,2}`.

The C88 staircase gives one additional exact fact not used in that equality classification:

`(0,D) in E(G_P)`.

C87 supplies two **non-chain** active diameter pairs over that simple interval, one in each physical orientation. This rules out the cases `R_rep=1,2`.

## 2. Extreme-role notation

For the simple interval `{0,D}`, choose the C87 paired physical diameters

`h_+ = L_0 U_D`,

`h_- = U_0 L_D`.

Here `L_0,U_0,L_D,U_D` denote the selected arc-role representatives used by these two non-chain diameter pairs; they are not assumed to be the chain endpoints.

By construction

`h_+ != za`, `h_- != za`,

because the paired family consists of non-chain diameters and C96 adjoins `za` separately.

## 3. Theorem — exact floor has no representative surplus

Assume

`q=2D+2`.

Then necessarily

`R_rep=0`, `c_ext=2`.

In particular every arc-level slot has exactly one selected representative:

`l_k=u_k=1` for all `0<=k<=D`.

### Proof

At equality the representative audit gives `c_ext=R_rep+2`.

If `R_rep=2`, then `c_ext=4`. Since each chain endpoint belongs to at most two arc-role sets, this forces

`c_z=2`, `c_a=2`.

Thus `z` occupies both `L_0,U_0` roles and `a` occupies both `L_D,U_D` roles. Then

`h_+=za=h_-`,

contradicting that `h_+,h_-` are two selected non-chain diameter pairs distinct from `za`.

If `R_rep=1`, then `c_ext=3`. Hence `(c_z,c_a)` is `(2,1)` or `(1,2)`.

Suppose `(c_z,c_a)=(2,1)`. Then `z` occupies both level-0 roles. If `a` occupies `L_D`, the edge

`h_-=U_0L_D`

is exactly `za`; if `a` occupies `U_D`, then

`h_+=L_0U_D`

is exactly `za`. Either case contradicts the non-chain status of the paired edges. The case `(1,2)` is symmetric.

Therefore `R_rep` is neither `1` nor `2`, so `R_rep=0`; then `c_ext=2`. By definition of `R_rep`, every `l_k=u_k=1`. `square`

## 4. Classification of the remaining extreme reuse patterns

Since `R_rep=0` and `c_ext=2`, exactly two of the four extreme role incidences are occupied by `z,a`, counted with multiplicity. The non-chain condition on `h_+,h_-` leaves only the following patterns:

1. `c_z=2,c_a=0`: `z` is the unique representative in both level-0 arc roles; `a` is in neither level-D role.
2. `c_z=0,c_a=2`: the symmetric case.
3. `c_z=c_a=1`, with the two chain endpoints occupying the **same arc sheet**: either `z=L_0,a=L_D` or `z=U_0,a=U_D`.

The crossed one-one patterns `z=L_0,a=U_D` and `z=U_0,a=L_D` are impossible because they make `h_+` or `h_-` equal to `za`.

Thus the exact C96 floor has a literal one-representative-per-arc-level paired lift, with only these three ways for the separately adjoined chain endpoints to overlap its four extreme roles.

## 5. Consequence

The existing near-equality handoff asked for a geometric stability theorem because `R_rep=o(D)`. At the **exact** floor the bookkeeping is stronger:

> There are no split arc-level representatives anywhere.

Therefore any contradiction at `q=2D+2` may work directly with a unique physical endpoint `L_k,U_k` for every prefix level, rather than carrying the `R_rep<=2` defect cases.

The remaining geometric equality models are:

- the two-copy C88 staircase lift with `z` gluing the two level-0 roles and `a` external to the level-D roles;
- its `z/a` reversal; or
- the lift with `z,a` lying on one common sheet and the other sheet having distinct extreme representatives.

These are graph-theoretically compatible with C90, so the next step still requires Euclidean diameter/unit-separation geometry.

## 6. Audit classification

| Statement | Classification | Reason |
| --- | --- | --- |
| `(0,D)` is a C88 staircase edge | canonical | row 1 is complete through `M_1=D` |
| its two C87 representatives are non-chain diameters distinct from `za` | canonical | C87 paired family; C96 adjoins `za` separately |
| `R_rep=2` impossible at `q=2D+2` | proved | would identify both paired edges with `za` |
| `R_rep=1` impossible at `q=2D+2` | proved | one paired orientation becomes `za` |
| exact floor has `R_rep=0,c_ext=2` | proved | exhaustive use of equality relation |
| exact floor itself is impossible | not proved | three Euclidean reuse patterns remain |

## 7. Handoff

```text
LEVEL I STATUS: STILL OPEN.

At q=2D+2 the representative audit gave R_rep<=2. Using the mandatory C88 edge (0,D) and the fact that its two C87 orientations are non-chain diameters distinct from za eliminates R_rep=1 and 2.

Therefore exact endpoint equality forces

  R_rep=0,
  c_ext=2,
  l_k=u_k=1 for every level k.

Only three extreme reuse patterns remain: z in both level-0 roles; a in both level-D roles; or z,a on the same arc sheet one role each.

Next target: rule out those three unique-representative Euclidean lift models using shared-endpoint diameter-angle geometry, train coordinates, or shell/perimeter constraints.
```