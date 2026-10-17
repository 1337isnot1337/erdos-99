> Generated reading edition · [exact source](../../research/target_c_high_t_tb1_thin_phase_cone_uniqueness_t18687_2026-09-17.md) · source SHA-256 `c47318980678e807887b4f1e3e9fadd9367725da0ee4f97ff88f68cd4bf76532`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 16 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "cd6e235ded668c751c0f296ef154698cabd7e349", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_high_t_tb1_thin_phase_cone_uniqueness_t18687_2026-09-17.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "793496faa032df75b43dcdeca6a6a437730e6d9dfdf150c009c999f898c7a99c"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II - inverse-D directional packing and a THIN row/guard uniqueness fork

**Date:** 2026-09-17  
**Status:** proof-only geometric strengthening of the macroscopic four-guard THIN normal form; no canonical promotion claimed  
**Scope:** THIN side of the 15-spaced one-sign strong-TB1 Horn upper family through `t=(q-k)/D<=1.8687`  
**Dependencies:** macroscopic four-guard theorem; finite stopped-train monotonicity theorem DT; THIN superdiameter window  
**Certificate:** `research/verify_target_c_high_t_tb1_thin_phase_cone_uniqueness_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The current THIN bottleneck includes a genuine multiplicity issue: a straight inactive almost-diameter is known to meet every selected row, but the repository has not proved that it meets a stopped-train midpoint curve only once. The same issue occurs when one asks whether a THIN chord meets one of the fixed train guards.

Two elementary facts resolve that ambiguity on a logarithmic sub-braid.

First, inverse-`D` concentration of near-diameter chord directions has bounded capacity. The earlier repeated-witness argument proved a stronger-slack special case. The correct general scale is already

```math
D-{A\over D}\le |xy|\le D.
```

Second, Theorem DT puts every oriented midpoint step of a train with transverse direction `u` inside the open `pi/3` cone centered on `Ju`. A straight line whose projective direction lies outside that cone meets the complete train at most once.

The row phase and the two possible column phases divide the projective direction circle into exactly three such `pi/3` sectors. After deleting the bounded number of THIN chords lying in inverse-`D` neighborhoods of the three sector boundaries, a constant fraction of the logarithmic braid lies in one open sector. This gives an exact fork:

> **THIN phase-cone uniqueness theorem.** In the macroscopic four-guard normal form there is a pairwise-crossing sub-braid
> ```math
> F_D^{uniq}
> ```
> of size `Theta(log D)` such that one of the following holds uniformly for every chord in the sub-braid:
>
> 1. **ROW-UNIQUE:** the chord meets every retained selected row exactly once; or
> 2. **GUARD-UNIQUE:** the chord meets each of the four fixed complete train guards at most once.
>
> The sub-braid may simultaneously be chosen to have one common four-bit meet/avoid word against the guards.

At the half-exponent choice of the macroscopic-guard theorem this leaves

```math
\boxed{
\left({1\over96\log5}-o(1)\right)\log D
}
\tag{PU.1}
```

pairwise-crossing THIN chords on

```math
\boxed{D^{1/2-o(1)}}
\tag{PU.2}
```

common near-equilateral rows, together with the same two macroscopically separated train guards on each flank.

In the GUARD-UNIQUE case the common four-bit word now means exact intersection counts `0` or `1`, not merely binary nonempty/disjoint incidence. In the ROW-UNIQUE case the polynomial row stack acquires a well-defined single intersection point with every selected braid chord, removing the row-intersection multiplicity ambiguity that blocked order arguments in the previous frontier.

---

## 1. An inverse-D direction cone contains only boundedly many near-diameters

### Lemma PU.1 - inverse-D directional capacity

Fix constants `A,L>0`. Let `S` be a unit-separated planar set with

```math
\operatorname{diam}(S)\le D.
```

Fix a projective direction `[u_*]`. Let `E_D(A,L)` be the unordered source pairs `xy` satisfying

```math
D-{A\over D}\le |x-y|\le D
\tag{PU.3}
```

and

```math
d_{\mathbb{RP}^1}([xy],[u_*])\le {L\over D}.
\tag{PU.4}
```

Then

```math
\boxed{|E_D(A,L)|=O_{A,L}(1).}
\tag{PU.5}
```

The constant is independent of `D` and of the source.

### Proof

Orient every edge in the common projective cone, writing

```math
r_e=y_e-x_e=\ell_e d_e,
\qquad
\angle(d_e,u_*)\le {L\over D},
```

and let

```math
m_e={x_e+y_e\over2}.
```

For two edges `e,f`, both cross-endpoint distances are source distances and hence at most `D`:

```math
\left|m_f-m_e+{r_e+r_f\over2}\right|\le D,
\qquad
\left|m_f-m_e-{r_e+r_f\over2}\right|\le D.
\tag{PU.6}
```

Adding the squared inequalities gives

```math
|m_f-m_e|^2
\le
D^2-{1\over4}|r_e+r_f|^2.
\tag{PU.7}
```

The angle between `r_e,r_f` is at most `2L/D`, while both lengths are at least `D-A/D`. Therefore

```math
{1\over2}|r_e+r_f|
\ge
\left(D-{A\over D}\right)\cos{L\over D}.
```

Consequently

```math
\boxed{
|m_f-m_e|^2
\le
D^2-\left(D-{A\over D}\right)^2\cos^2{L\over D}
=2A+L^2+o(1).
}
\tag{PU.8}
```

Thus all midpoints lie in one fixed-radius disk.

Also

```math
|r_e-r_f|
\le |\ell_e-\ell_f|+\ell_f|d_e-d_f|
\le {A\over D}+2D\sin{L\over D}
\le 2L+1
\tag{PU.9}
```

for sufficiently large `D`. Fixing one reference edge, the identities

```math
x_e=m_e-{r_e\over2},
\qquad
y_e=m_e+{r_e\over2}
```
place all oriented left endpoints in one fixed-radius disk and all oriented right endpoints in another fixed-radius disk.

The source is unit-separated, so each fixed-radius disk contains only `O_{A,L}(1)` source points. Hence there are only `O_{A,L}(1)` possible ordered endpoint pairs. This proves (PU.5). `square`

For THIN blockers we may take `A=1/4` after the existing fixed-threshold reduction, because

```math
D-|e|<{1\over4D}.
\tag{PU.10}
```

Thus any fixed `O(D^-1)` direction cone contains only `O(1)` THIN chords.

---

## 2. A line outside a train's step cone meets that train at most once

### Lemma PU.2 - line/train uniqueness

Let `b` be a complete stopped train with fixed projective transverse contact-edge direction `[u_b]`. Orient its midpoint path as in Theorem DT. Every oriented path step `v` obeys

```math
\angle(v,Ju_b)<{\pi\over6}.
\tag{PU.11}
```

Equivalently, on the projective direction circle the train's step directions lie in one open interval

```math
\mathcal C(u_b)
:=
\left(
[u_b]+{\pi\over3},
[u_b]+{2\pi\over3}
\right)
\pmod\pi.
\tag{PU.12}
```

Let `ell` be any straight line whose projective direction `[d]` lies outside the closure of `C(u_b)`. Then

```math
\boxed{
ell\text{ meets the complete midpoint curve of }b\text{ in at most one point}.}
\tag{PU.13}
```

### Proof

Orient `d` so that

```math
\det(d,v)
```
has one strict sign for every allowed train step direction `v`; this is possible precisely because `[d]` is outside the closed projective step interval.

For a fixed point `p_0` on `ell`, the signed line-normal coordinate

```math
H(p):=\det(d,p-p_0)
```
therefore changes strictly monotonically along every segment of the oriented train and hence along the entire train path. The line `ell` is exactly `H=0`, so the train can meet it at most once. `square`

This uses the full-train monotonicity already proved in DT and does not assume that the train is straight.

---

## 3. The row and column phases give three complementary step sectors

Use the macroscopic four-guard theorem. There is a reference projective row transverse phase `[u_*]` such that every retained selected row has transverse direction

```math
[u_a]=[u_*]+O(D^{-1}).
\tag{PU.14}
```

Each fixed guard train crosses every retained row at angle

```math
{\pi\over3}+O(D^{-1}),
```
so every guard transverse direction lies in one of the two column phase cones

```math
[u_*]+{\pi\over3}+O(D^{-1}),
\qquad
[u_*]-{\pi\over3}+O(D^{-1}).
\tag{PU.15}
```

The corresponding ideal train-step sectors on `RP^1` are

```math
\mathcal S_-=
\left([u_*],[u_*]+{\pi\over3}\right),
\tag{PU.16}
```

```math
\mathcal S_0=
\left([u_*]+{\pi\over3},[u_*]+{2\pi\over3}\right),
\tag{PU.17}
```

```math
\mathcal S_+=
\left([u_*]+{2\pi\over3},[u_*]+\pi\right),
\tag{PU.18}
```

with endpoints interpreted modulo `pi`.

Here `S_0` is the row-train step sector. The two possible guard phases have step sectors `S_-` and `S_+`. Thus the three ideal sectors partition the projective direction circle.

All phase errors are bounded by `C_0/D` for one source-independent constant `C_0`, inherited from the inverse-`D` phase purification. Fix any constant

```math
L_0>10C_0+10.
\tag{PU.19}
```

Delete from the THIN braid every chord whose projective direction lies within `L_0/D` of one of the three ideal boundary directions

```math
[u_*],
\quad [u_*]+{\pi\over3},
\quad [u_*]+{2\pi\over3}.
\tag{PU.20}
```

By Lemma PU.1 with `A=1/4`, each deleted boundary tube contains only `O(1)` THIN chords. Hence only `O(1)` braid chords are deleted in total.

Every remaining chord belongs unambiguously to one of the three open sectors, with enough inverse-`D` clearance that the conclusion remains true for all perturbed row and guard step cones.

---

## 4. A logarithmic sub-braid has one uniform uniqueness mode

Start with the `k_D=Theta(log D)` braid from the macroscopic four-guard theorem and delete the `O(1)` boundary-near chords from Section 3. One of the three ideal sectors contains at least

```math
{k_D-O(1)\over3}
\tag{PU.21}
```

remaining chords. Retain that sector class.

There are two cases.

### Case A: the selected direction sector is not `S_0`

Then every retained chord direction lies outside the closed step cone of every selected row. Lemma PU.2 gives at most one intersection with each row.

But every THIN braid chord belongs to the exact selected-cut support of every retained row, so its endpoints are separated by that row and the straight segment meets the row at least once. Therefore

```math
\boxed{
\text{every retained chord meets every retained selected row exactly once.}
}
\tag{PU.22}
```

This is the ROW-UNIQUE alternative.

### Case B: the selected direction sector is `S_0`

Every fixed guard has one of the two column transverse phases from (PU.15), so its train-step cone is a perturbation of `S_-` or `S_+`. A chord direction in the cleared core of `S_0` therefore lies outside every guard step cone. Lemma PU.2 gives

```math
\boxed{
\text{every retained chord meets each fixed train guard at most once.}
}
\tag{PU.23}
```

This is the GUARD-UNIQUE alternative.

Notice that this conclusion does not depend on whether the left and right guard pairs use the same column phase or opposite column phases.

---

## 5. Add the four-bit guard-incidence purification

The four fixed guard trains give at most `16` binary meet/avoid words. Split the sector-homogeneous braid once more by this four-bit word and retain the largest class.

The resulting braid `F_D^uniq` has

```math
\boxed{
|F_D^{uniq}|
\ge
{k_D-O(1)\over48}.
}
\tag{PU.24}
```

It is still vertex-disjoint and pairwise properly crossing, all its chords cross every retained selected row, and it retains the same common four-guard incidence word.

In the GUARD-UNIQUE alternative, (PU.23) upgrades each bit of that word to an exact count:

```text
0 = no intersection with that fixed guard;
1 = exactly one intersection with that fixed guard.
```

In the ROW-UNIQUE alternative, (PU.22) gives one well-defined chord/row intersection point for every pair

```math
(e,a)\in F_D^{uniq}\times A_D.
```

This is the first current THIN reduction that removes row-intersection multiplicity on a logarithmic pairwise-crossing braid while retaining a polynomial-height common row scaffold.

---

## 6. Concrete half-exponent form

Take the macroscopic-guard half-exponent choice

```math
c={1\over2\log5}.
```

Then

```math
k_D=
\left({1\over2\log5}+o(1)\right)\log D
```

and the common row family has size

```math
D^{1/2-o(1)}.
```

Equation (PU.24) becomes

```math
\boxed{
|F_D^{uniq}|
\ge
\left({1\over96\log5}-o(1)\right)\log D.
}
\tag{PU.25}
```

Thus the surviving THIN geometry has one of two exact forms:

```text
ROW-UNIQUE:
    Theta(log D) pairwise-crossing almost-diameter hull chords;
    each chord crosses each of D^(1/2-o(1)) common rows exactly once;
    four fixed macroscopically separated train guards;
    one common four-bit guard-incidence word.

GUARD-UNIQUE:
    Theta(log D) pairwise-crossing almost-diameter hull chords;
    D^(1/2-o(1)) common rows;
    four fixed macroscopically separated train guards;
    every chord/guard pair has exact intersection count 0 or 1;
    the same four-bit count word for every chord.
```

The next ROW-UNIQUE target is now an actual order problem: the unique intersection points permit the braid order to be compared across the common row stack, rather than working with arbitrary multiple crossings. The GUARD-UNIQUE target is a finite four-crosscut problem with exact `0/1` incidence and macroscopic guard-pair spacing.

**Disposition:** generalized the directional packing lemma to the natural `D-A/D` shell, then used the three train phase sectors to force a logarithmic THIN sub-braid with either unique row intersections or unique fixed-guard intersections. C-II and Level I remain open.
