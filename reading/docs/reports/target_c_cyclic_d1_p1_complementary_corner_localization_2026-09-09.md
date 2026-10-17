> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_d1_p1_complementary_corner_localization_2026-09-09.md) · source SHA-256 `a8464270fc7b7b9322465c55d956eede6510656fd44101de54cf35a33d4f3382`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-4E04AD2A143A","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdos Problem #99 — P1 endpoint-zero diameters are complementary moving-corner chords

**Date:** 2026-09-09  
**Repository branch:** PR #118 after PR/AE/EU  
**Run type:** exact four-block corner localization  
**Target:** cyclic primitive phase `d_H=1`, P1  
**Depends on:** PR twin short completions, AE anchored component partition, EU opposite-corner theorem, MT addable-corner argument  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

AE proves that every P1 KKT endpoint-zero edge `e` cuts the diameter tree into components containing

```math
\{a,c\}\mid\{b,d\},
```

where `a,b,c,d` are the P1 rectangle vertices in cyclic order and `ab,cd` are the fixed parallel unit hull sides.

Thus the four contact transitions are

```math
ab,\ f,\ cd,\ h,
```

with `f` on the open shell chain `b -> c` and `h` on the open shell chain `d -> a`.

The two short rectangle chords `ad` and `bc` are separately addable to the diameter tree and hence to `H-e`. Applying the four-block corner theorem to all three cross-cut chords `ad,bc,e` leaves no freedom for `e`: the short chords occupy the two corner types based at the fixed transitions `ab,cd`, while the actual diameter edge must occupy one of the two complementary corner types based at `f,h`.

### Theorem CC — complementary-corner localization

Let the moving transition sides be

```math
f=pq,
\qquad
h=rs,
```

in the counterclockwise shell order

```math
a,\ b,\ldots,p,q,\ldots,c,\ d,\ldots,r,s,\ldots,a.
\tag{CC.1}
```

Color the `H-e` components so that

```math
a,c,p?\text{ after the transition}\in A,
\qquad
b,d\in B.
```

More precisely the four blocks are

```math
A_0\mid B_0\mid A_1\mid B_1
```
with

```math
A_0:\ s\leadsto a,
\qquad
B_0:\ b\leadsto p,
\qquad
A_1:\ q\leadsto c,
\qquad
B_1:\ d\leadsto r.
\tag{CC.2}
```

Then:

```math
\boxed{
\{ad,bc\}
\text{ are the two fixed-transition opposite-corner chords},
}
\tag{CC.3}
```

while

```math
\boxed{
e=sp\quad\text{or}\quad e=qr.}
\tag{CC.4}
```

In particular every endpoint-zero actual diameter edge has both endpoints incident to the two **moving** transition contacts `f,h`.

Equivalently the four moving corner vertices form the convex quadrilateral

```math
p,q,r,s
```
with

```math
|pq|=|rs|=1,
```

and one of its two complementary sides

```math
sp,\ qr
```
has length exactly `D` and is the zeroed full-tree diameter edge.

The other complementary side is necessarily strictly shorter than `D`, because `e` is the unique full diameter edge crossing the `H-e` cut.

---

## 1. Identify the four blocks from AE

AE gives component membership

```math
a,c\in A,
\qquad
b,d\in B.
```

Starting at `a` and traversing the shell counterclockwise:

1. `ab` changes from A to B;
2. there is exactly one transition `f=pq` on the `b -> c` chain, changing B to A;
3. `cd` changes A to B;
4. there is exactly one transition `h=rs` on the `d -> a` chain, changing B to A.

Therefore the component runs are exactly

```math
A_0=s,\ldots,a,
\quad
B_0=b,\ldots,p,
\quad
A_1=q,\ldots,c,
\quad
B_1=d,\ldots,r,
```

after choosing the tree bipartition labels consistently. This is CC.2.

---

## 2. The short chord `ad` occupies one fixed corner type

PR proves `H+ad` is a maximal convex thrackle. Hence after deleting `e`, the chord `ad` is addable to

```math
H-e=T_A\sqcup T_B.
```

It crosses the component cut because `a in A` and `d in B`.

The addable-cross-chord corner proof from MT/EU applies: an addable chord between two four-block tree components must join opposite endpoints of its two color blocks.

Here

```math
a\in A_0
```
is the A0 endpoint at the `A_0|B_0` transition `ab`, while

```math
d\in B_1
```
is the B1 endpoint at the `A_1|B_1` transition `cd`.

Thus `ad` is exactly the opposite-corner chord joining the A-side corner of `ab` to the B-side corner of `cd`.

---

## 3. The short chord `bc` occupies the other fixed corner type

Likewise PR proves `H+bc` is a maximal convex thrackle, so `bc` is addable to `H-e` and crosses the A/B component cut.

Its endpoints are

```math
b\in B_0
```
at the B-side corner of `ab`, and

```math
c\in A_1
```
at the A-side corner of `cd`.

Therefore `bc` is the other opposite-corner chord based at the same two fixed transitions.

The two short chords have exhausted the cross-block types

```math
A_0-B_1
\quad\text{and}\quad
B_0-A_1.
\tag{3.1}
```

---

## 4. The actual zeroed edge must use the complementary moving corners

EU says the actual zeroed edge `e` itself is an opposite-corner chord of the same four-block partition.

There are four possible component/color pair types:

```math
A_0-B_0,
\quad
A_0-B_1,
\quad
A_1-B_0,
\quad
A_1-B_1.
```

Sections 2-3 show that the unique opposite-corner chords of the middle two types are precisely the short rectangle chords

```math
ad,
\qquad
bc.
```

But

```math
|e|=D,
\qquad
|ad|=|bc|=\sqrt{D^2-1}<D,
```
so `e` cannot be either of those two chords.

Hence `e` has type `A_0-B_0` or `A_1-B_1`.

Apply EU's explicit endpoint rule.

### Type `A_0-B_0`

The A0 endpoint must be the one adjacent to `B_1`, namely

```math
s,
```
while the B0 endpoint must be the one adjacent to `A_1`, namely

```math
p.
```
Thus

```math
e=sp.
```

### Type `A_1-B_1`

Symmetrically the A1 endpoint adjacent to `B_0` is

```math
q,
```
and the B1 endpoint adjacent to `A_0` is

```math
r.
```
Thus

```math
e=qr.
```

This proves CC.4. `square`

---

## 5. The other moving-corner chord is subdiametral

Suppose, for example,

```math
e=sp.
```

The other complementary corner chord is

```math
qr.
```

If `|qr|=D`, then `qr` would be a second full-H diameter edge crossing the A/B component cut of `H-e`. But because `H` is a tree, the deleted edge `e` is the unique full-H edge crossing the cut between the two components of `H-e`.

Therefore

```math
\boxed{|qr|<D.}
\tag{5.1}
```

The case `e=qr` gives symmetrically

```math
|sp|<D.
```

Thus each endpoint cut selects a convex four-corner quadrilateral with two opposite unit sides `f,h`, one diameter side `e`, and one strictly subdiametral complementary side.

No quantitative lower bound on the latter is claimed yet.

---

## 6. Interaction with the anchored WM relation

CC gives a metric meaning to every line in AE's four-force wrench system.

If

```math
e=sp,
```
then the two moving contact lines are the unit sides

```math
pq,
\qquad rs
```
adjacent to the endpoints of the diameter side `sp` in the four-corner quadrilateral `p,q,r,s`.

The anchored endpoint force relation

```math
(\alpha_{ab}-\alpha_{cd})t
=\alpha_f t_f+\alpha_h t_h
```
is therefore not an arbitrary four-side identity: the moving forces act on the two unit sides adjacent to a common length-`D` supporting chord of the four-corner quadrilateral.

This supplies the metric input missing from a pure WM/WT calculation.

---

## 7. Regression audit

### Converse to EU

Not assumed. We know `ad` and `bc` are addable from PR, and `e` exists from the full diameter tree. The corner theorem is applied only to these known chords.

### Could `e=ad` or `bc` despite different labels?

No: those exact vertex pairs have length `sqrt(D^2-1)`, while every edge of `H`, including `e`, has length `D`.

### Could both `sp` and `qr` be diameters?

No. They both cross the same component cut, and a tree has exactly one edge crossing the cut created by deleting one of its edges.

### Extra zero beta coordinates

Irrelevant. CC is a theorem about the full tree `H` and one chosen zeroed edge `e`.

---

## 8. What this changes

Every P1 endpoint is now described by two nested quadrilaterals:

```text
fixed rectangle a,b,c,d:
  ab=cd=1,
  ac=bd=D,
  ad=bc=sqrt(D^2-1)

moving four-corner quadrilateral p,q,r,s:
  pq=rs=1,
  exactly one of sp,qr is the endpoint-zero diameter D,
  the other is <D.
```

The fixed rectangle supplies the two permanent transition contacts `ab,cd`; the moving quadrilateral supplies the other two transition contacts `pq,rs` and the zeroed diameter edge.

This is a finite metric normal form, not merely a block-order statement.

---

## 9. Next theorem

The immediate target is now geometric:

### CC-gap

For a convex quadrilateral `p,q,r,s` occurring in the P1 shell order, with

```math
|pq|=|rs|=1,
\qquad
|sp|=D,
\qquad
|qr|<D,
```
and with `sp` an actual source diameter, quantify the deficit

```math
D-|qr|
```
from the directions of the two unit sides `pq,rs`.

Those same directions occur in the anchored WM equation. A lower bound on the complementary-side deficit can therefore be converted into a lower bound on the line-intersection displacement, hence on

```math
|\alpha_{ab}/\alpha_{cd}-1|.
```

A second target is combinatorial: compare the two endpoint quadrilaterals along the common path `J`. If their diameter sides use opposite complementary types (`sp` versus `qr`), the resulting sign reversal in the anchored force equation may force an interior stress with `alpha_ab=alpha_cd`.

---

## 10. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

For a P1 endpoint cut, AE gives transitions ab,f,cd,h and component blocks
  A0=s..a | B0=b..p | A1=q..c | B1=d..r,
where f=pq and h=rs are the two moving unit transition sides.

PR says both short rectangle chords ad and bc are addable to H, hence to H-e.
The four-block addable-corner theorem puts
  ad in the A0-B1 fixed-corner type,
  bc in the B0-A1 fixed-corner type.
EU says the actual zeroed edge e is also an opposite-corner chord. It cannot equal
ad or bc because those have length sqrt(D^2-1)<D. Therefore e must be one of the two
complementary moving-corner types:
  e=sp or e=qr.
The other chord among {sp,qr} is strictly subdiametral; otherwise H would have two
edges crossing the cut of H-e.

Thus every P1 endpoint contains a moving convex quadrilateral p,q,r,s with
  pq=rs=1,
  one of sp,qr equal D,
  the other <D,
while the four-contact WM relation remains anchored on the fixed rectangle sides
ab,cd and moving unit sides pq,rs.

Next: quantify D-|other side| and feed that metric defect into WM/WT; also compare
which complementary type occurs at the two KKT endpoints.
```
