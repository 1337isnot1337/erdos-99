> Generated reading edition · [exact source](../../../docs/reports/target_c_post_zf_boundary_only_first_layer_2026-09-09.md) · source SHA-256 `fee90211a6cf7a58585378fbf4a64e25ddd706b4753959571076ba761085b398`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 1 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-3D7E451EE05A","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — boundary-only primitive defect: exact first layer

**Date:** 2026-09-09  
**Repository base:** PR #118 after PN/ME/CY/CG  
**Run type:** exact finite branch classification  
**Target:** Target C, C-II after ZF  
**Depends on:** PN primitive normal form and ME missing-hull-side incidence theorem  
**External web search:** not used  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

This note classifies the first primitive-defect layer above the cyclic endpoint when the entire nonisolated contact core lies on the loaded force hull.

Let

```math
p:=m+k=m+d_H+s_Z,
```

with PN notation:

- `m`: number of nonunit loaded force-hull sides;
- `k=d_H+s_Z`;
- `c_B`: number of loaded-loaded unit contacts beyond the unit hull sides;
- `r_m`: number of cyclic runs of the `m` nonunit hull sides.

Assume

```math
\boxed{c_I=0,}
\tag{BO.0}
```

so there are no unpinned vertices in the positive contact core.

Then necessarily

```math
\boxed{s_C=0}
\tag{BO.1}
```

and the PN/ME identities reduce to

```math
\boxed{c_B=m+k-2=p-2,}
\tag{BO.2}
```

and, whenever `m>0`,

```math
\boxed{2c_B\ge m+r_m.}
\tag{BO.3}
```

At the first layer `p=3`, these constraints have one and only one realization:

```math
\boxed{
 m=0,
 \qquad k=3,
 \qquad c_B=1.}
\tag{BO.4}
```

Thus a boundary-only post-ZF source with primitive defect three has every force-hull side as a unit contact and exactly one additional loaded-loaded unit chord.

---

## 1. Boundary-only simplification

If `c_I=0`, then every nonisolated positive-contact vertex lies in `B_+`. Hence

```math
v=q,
\qquad e=e_{BB}.
```

By definition

```math
s_C=(e-e_{BB})-2(v-q)-c_I,
```

so `s_C=0`, proving BO.1.

PN gives

```math
c_I+s_C+c_B=m+k-2.
```

With `c_I=s_C=0`, this becomes BO.2.

ME gives

```math
e_{BI}+2c_B\ge m+r_m.
```

Here `e_{BI}=0`, so BO.3 follows. `square`

---

## 2. General boundary-only run inequality

Combining BO.2 and BO.3 gives, for `m>0`,

```math
2(m+k-2)\ge m+r_m.
```

Therefore

```math
\boxed{
 m+2k\ge r_m+4.}
\tag{BO.5}
```

This is an exact finite restriction on how missing unit hull sides can occur in a boundary-only core.

Equivalently,

```math
\boxed{
 k\ge 2+\frac{r_m-m}{2}.}
\tag{BO.6}
```

The bound is useful when the missing sides occur in many separated runs: separation consumes primitive diameter/mixed defect.

---

## 3. Classify `p=3`

Assume

```math
p=m+k=3.
\tag{3.1}
```

BO.2 gives

```math
\boxed{c_B=1.}
\tag{3.2}
```

We now exclude every case with `m>0`.

### Case `m=2`, `k=1`

Every nonempty set of two missing hull sides has

```math
r_m\ge1.
```

ME/BO.3 requires

```math
2c_B=2\ge m+r_m\ge3,
```

a contradiction.

### Case `m=1`, `k=2`

There is one missing hull side, so

```math
r_m=1.
```

ME/BO.3 reads

```math
2c_B=2\ge m+r_m=2,
```

so equality holds.

Let the missing side have consecutive loaded endpoints `a,b`. These are exactly the two loaded vertices incident to a missing hull side. ME.1 says each of `a,b` requires at least one non-hull contact incidence.

There are no loaded-interior contacts. Since `c_B=1`, there is exactly one extra loaded-loaded unit contact chord, contributing exactly two non-hull loaded incidences in total. Equality therefore forces this one chord to have endpoints exactly `a,b`.

But the straight segment `ab` is the missing force-hull side itself. By definition of `m`,

```math
|a-b|>1,
```

whereas an edge counted by `c_B` is a unit contact. Contradiction.

### Case `m=0`, `k=3`

This case is not contradicted. BO.2 gives `c_B=1`.

Every one of the `q` force-hull sides is a unit contact and there is exactly one extra loaded-loaded unit chord.

Therefore BO.4 is the unique boundary-only primitive-defect-three state. `square`

---

## 4. Exact graph form

In BO.4 the positive contact graph is

```math
\boxed{C=C_q+e_*}
\tag{BO.7}
```

where `e_*` is one unit chord between nonconsecutive vertices of the convex loaded cycle.

Triangle-freeness imposes the immediate local restriction that `e_*` cannot connect vertices at cyclic distance two, because the two intervening unit hull edges would form a unit triangle with `e_*`.

Thus the cyclic distance of the chord endpoints is at least three on both sides when `q` is sufficiently large.

The mixed defect satisfies

```math
\boxed{d_H+s_Z=3.}
\tag{BO.8}
```

This is the exact first boundary-only branch after the `p=2` cycle classified in CY/CG.

---

## 5. Boundary-only primitive hierarchy

The boundary-only normal form now begins:

### `p=2`

ME/CY leave only

```math
C=C_q,
\qquad m=0,
\qquad k=2.
```

### `p=3`

BO leaves only

```math
C=C_q+e_*,
\qquad m=0,
\qquad k=3,
\qquad c_B=1.
```

Hence the first two primitive levels have **no nonunit force-hull sides at all**. The first deviation from the pure unit hull cycle is an interior loaded-loaded contact chord, not a boundary gap.

Any boundary-only stability theorem near the cyclic endpoint should therefore count extra loaded chords before missing hull sides.

---

## 6. Rattler consequence

Since `c_I=0`, the nonisolated core has exactly the `q` loaded vertices for every boundary-only branch, not only the cyclic endpoint.

Thus all `n-q` remaining source points are contact-isolated. The universal perimeter bound `q<=pi D` gives

```math
\boxed{
 n-q>\Delta D^2-\pi D,
 \qquad
 \Delta=\frac\pi{2\sqrt3}.}
\tag{BO.9}
```

So the entire boundary-only primitive hierarchy coexists with the same quadratic force-invisible population identified in CY.

This remains a structural reduction, not a contradiction.

---

## 7. Regression audit

### Regular odd shell

It lies at `p=2`, not `p=3`, and is unaffected.

### Unit square

Also lies at `p=2`.

### One missing hull side plus one extra loaded chord

BO excludes it exactly at `p=3`: the sole chord would have to coincide with the nonunit hull side.

### Two consecutive missing hull sides

Even with one run, `m+r_m=3`, exceeding the two incidences supplied by the single extra chord. Excluded.

### One extra long loaded chord

Allowed at the combinatorial level provided it does not create a unit triangle. BO does not assert that the resulting geometry realizes a global minimizer or the necessary diameter stress.

---

## 8. Next theorem

The natural next finite target is BO.4:

> exclude or classify a convex loaded unit cycle with exactly one extra unit chord and `d_H+s_Z=3`.

Because the extra chord splits the cycle into two contact cycles, its geometry may be attacked using the reciprocal-force polygon, selected-stress support, or the diameter-thrackle edge-cover constraints.

A parallel asymptotic target is to prove that a boundary-only survivor cannot have primitive defect `p=o(D)`. The exact `p=2,3` classifications provide the first two base cases for such a stability induction.

---

## 9. Promotion recommendation

**Hold as report pending independent audit.**

The proof is exact downstream of report-level PN/ME.

---

## 10. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Boundary-only means c_I=0. Then v=q, e=e_BB, hence s_C=0.
PN gives exactly
  c_B=m+k-2,
where k=d_H+s_Z.
ME gives, for m>0,
  2c_B>=m+r_m.
Therefore
  m+2k>=r_m+4.

At primitive defect p=m+k=3:
  c_B=1.
- m=2,k=1: impossible because 2< m+r_m.
- m=1,k=2: equality in ME forces the sole extra loaded chord to join the two
  endpoints of the unique nonunit hull side, but that side has length >1 and
  cannot be a unit contact.
- m=0,k=3: survives.

Hence the unique boundary-only p=3 state is
  m=0,
  k=3,
  c_B=1,
  C=C_q plus one extra unit chord.

The p=2 and p=3 boundary-only levels therefore both have a complete unit force-hull
cycle; the first defect is one interior loaded contact chord, not a missing hull side.
All boundary-only branches still have n-q > Delta D^2-pi D contact-isolated points.
```
