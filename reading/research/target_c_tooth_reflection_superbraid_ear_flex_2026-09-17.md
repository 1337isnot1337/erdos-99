> Generated reading edition · [exact source](../../research/target_c_tooth_reflection_superbraid_ear_flex_2026-09-17.md) · source SHA-256 `d6a6daca48710c4e1bc12dfb1a5381082b584d214a3f5a1193b9a37a97057e06`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 4 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "6c77b1dece6d079d5215deaa98c7ac6aa55f051f", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_tooth_reflection_superbraid_ear_flex_2026-09-17.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "0359802f24e053424a9d7b06fb41e461f982d585e226e77c0193729c4209e88e"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — shallow superbraid ears force a near-unit matching or a simultaneous inactive flex

**Date:** 2026-09-17  
**Status:** proved candidate awaiting promotion; proof-only corollary of the superbraid shallow-ear ledger  
**Scope:** BLOCK-SQRT-SUPER-BRAID with shallow endpoint set from SE.8  
**Dependencies:** superbraid shallow-ear ledger and its exact one-ear inward deformation  
**Certificate:** `research/verify_target_c_tooth_reflection_superbraid_ear_flex_2026_09_17.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The shallow-ear theorem gives many fully inactive hull endpoints `v` with ear depth
`d_v<=lambda`. Individually, each such endpoint is either guarded by an original pair
of length at most `1+lambda`, or can be moved all the way to its neighboring hull chord
without any unit collision.

This note makes that alternative collective. A large shallow endpoint family forces
either a vertex-disjoint near-unit matching in the **original source**, or a large
simultaneous motion of fully inactive coordinates which preserves the old contact graph,
the old diameter-pair graph, and the diameter `D` exactly.

---

## 1. Setup

Let `G` be any set of fully inactive full-hull vertices supplied by SE.8 such that

```math
\boxed{d_v\le\lambda\le1\qquad(v\in G).}
\tag{EF.1}
```

For each `v`, use its fixed original ear path

```math
\gamma_v(t)=(1-t)v+t p_v,
\qquad 0\le t\le1,
```

where `p_v` is the perpendicular foot in the relative interior of the chord between
the two original full-hull neighbors of `v`.

Call `v` **guarded** if its individual path reaches unit distance from some fixed
original source point. Otherwise call it **movable**. By the one-ear theorem:

- a guarded `v` has an original source point `u_v` with
  
  ```math
  1<|v-u_v|\le1+\lambda;
  \tag{EF.2}
  ```

- a movable `v` satisfies
  
  ```math
  |\gamma_v(t)-u|>1
  \quad\text{for every }u\in A\setminus\{v\},\ 0\le t\le1.
  \tag{EF.3}
  ```


---

## 2. Many guarded ears give a matching

Let `G_g` be the guarded endpoints. Choose one guard `u_v` for each `v in G_g` and
form the simple graph of the resulting original source pairs.

Every incoming guard center `v` for a fixed source point `u` lies in
`B(u,1+lambda)`. The source is unit-separated, so the open radius-`1/2` disks centered
at those `v` are disjoint and lie in `B(u,3/2+lambda)`. Therefore the number of
incoming guard edges at `u` is at most

```math
4(3/2+\lambda)^2=(3+2\lambda)^2\le25.
\tag{EF.4}
```

There is at most one chosen outgoing guard edge at a guarded endpoint. Hence the
simple guard graph has maximum degree at most `26`.

Two opposite choices can represent the same undirected source pair, but no edge has
more than two orientations. Thus the simple guard graph has at least `|G_g|/2` edges.
A greedy maximal matching in a graph of maximum degree `26` has size at least the edge
count divided by `2*26-1=51`. Consequently

```math
\boxed{
\nu_{\rm guard}\ge {|G_g|\over102}.
}
\tag{EF.5}
```

Every retained matching edge is an original source pair satisfying

```math
\boxed{1<|x-y|\le1+\lambda.}
\tag{EF.6}
```

---

## 3. Movable-ear tube conflicts

Let `G_m` be the movable endpoints. For `v,w in G_m`, put an edge `vw` in the
tube-conflict graph if

```math
\min_{0\le s,t\le1}|\gamma_v(s)-\gamma_w(t)|\le1.
\tag{EF.7}
```

If `vw` is a conflict edge, then for some `s,t`

```math
|\gamma_v(s)-\gamma_w(t)|\le1.
```

Both path lengths are at most `lambda`, so the original pair obeys

```math
\boxed{
1<|v-w|\le1+2\lambda.
}
\tag{EF.8}
```

The lower inequality is strict because the endpoints are fully contact-inactive.
Therefore every matching in the tube-conflict graph is already a vertex-disjoint
near-unit matching in the original source.

Let `r` be the size of a maximum tube-conflict matching.

If

```math
r\ge {|G_m|\over4},
```

then the original source contains a vertex-disjoint matching of that size with lengths
in `(1,1+2lambda]`.

Otherwise, take the vertices unmatched by a maximum matching. A maximum matching is
maximal, so its unmatched vertices form an independent set in the conflict graph. Its
size is

```math
|G_m|-2r>{|G_m|\over2}.
\tag{EF.9}
```

Call this set `M`.

---

## 4. Conflict-free movable ears move simultaneously

For every `v in M`, move `v` along `gamma_v(t)` with a common parameter `t` (indeed,
the stronger pairwise tube condition allows independent parameters).

### Lower constraints

Each individual movable path stays strictly more than unit distance from every fixed
original source point by (EF.3). Distinct vertices of `M` have no tube-conflict edge,
so

```math
|\gamma_v(s)-\gamma_w(t)|>1
```

for all independent parameters `s,t`. Thus all moved configurations remain strictly
unit-separated from every pair involving a moved endpoint. Old contacts involve only
fixed vertices and remain unchanged.

### Upper constraints and diameter-pair graph

Every point on every ear path lies in the original convex body `K`, so all mutual
distances are at most `D`. More is true: every pair involving a moved endpoint stays
strictly below `D`.

For moved-fixed pairs this is SE.17. For two moved endpoints `v,w`, the function

```math
(s,t)\mapsto |\gamma_v(s)-\gamma_w(t)|
```

is convex separately in each variable and is bounded by the convex combination of its
four corner values. All four corner values are strictly below `D`:

- `|v-w|<D` because both are diameter-inactive;
- `|p_v-w|<D` and `|v-p_w|<D` because an interior point of a nondegenerate hull chord
  cannot be a diameter endpoint of `K`;
- `|p_v-p_w|<D` for the same reason.

Hence

```math
\boxed{
|\gamma_v(s)-\gamma_w(t)|<D
\quad(v,w\in M).
}
\tag{EF.10}
```

All old actual diameter pairs use fixed loaded vertices, so the global diameter remains
exactly `D` and the diameter-pair graph is unchanged.

Therefore the terminal simultaneous motion gives a same-cardinality global minimizer
with exactly the old contact and diameter-pair graphs, while every `v in M` has been
moved to its original neighboring hull chord through distance at most `lambda`.

---

## 5. Uniform finite fork

Let

```math
g:=|G|.
```

If at least half the endpoints are guarded, (EF.5) gives a matching of size at least

```math
{g\over204}
```

with length at most `1+lambda`.

Otherwise `|G_m|>g/2`. The tube-conflict matching argument gives either

```math
{g\over8}
```

vertex-disjoint original pairs of length at most `1+2lambda`, or a simultaneous
conflict-free movable set of size greater than

```math
{g\over4}.
```

Using the weaker common constant, every shallow-ear family satisfies

```math
\boxed{
\begin{array}{ll}
\text{NEAR-UNIT:} &
\text{an original vertex-disjoint matching of size at least }g/204\\
&\text{with }1<|x-y|\le1+2\lambda;\\[2mm]
\text{SIMULTANEOUS-FLEX:} &
\text{more than }g/4\text{ fully inactive endpoints move to their ear chords}\\
&\text{while preserving unit separation, diameter }D,\text{ and both old graphs.}
\end{array}}
\tag{EF.11}
```

---

## 6. Consequences for the block superbraid

In the sublinear-terminal regime `t_D=o(D)`, the shallow-ear theorem permits

```math
\lambda_D=\sqrt{t_D/D}=o(1)
```

and

```math
g=(2c_{\rm blk}-o(1))\sqrt D.
```

Therefore BLOCK-SQRT-SUPER-BRAID forces one of:

```math
\boxed{
\left({c_{\rm blk}\over102}-o(1)\right)\sqrt D
=
(0.009073917398829\ldots-o(1))\sqrt D
}
\tag{EF.12}
```

vertex-disjoint original source pairs satisfying

```math
\boxed{
1<|x-y|\le1+2\sqrt{t_D/D}=1+o(1),
}
\tag{EF.13}
```

or a simultaneous same-diameter inactive flex involving

```math
\boxed{
\left({c_{\rm blk}\over2}-o(1)\right)\sqrt D
}
\tag{EF.14}
```

superbraid endpoints, each moving through only `o(1)` distance to its original ear
chord.

If `t_D<=C sqrt(D)` and `K` satisfies the positivity condition in SE.14, the same
statement holds with `lambda=K/sqrt(D)` and with the explicit shallow population from
SE.13. Thus the NEAR-UNIT branch reaches the `D^{-1/2}` excess scale, while the
SIMULTANEOUS-FLEX branch becomes a square-root-dimensional `D^{-1/2}`-amplitude flat
motion of fully inactive hull coordinates.

C-II remains open. The surviving superbraid escape is now specific: after the terminal
deficit is reduced below linear scale, either it generates a square-root near-unit
matching or the canonical minimizer stratum contains a square-root family of
simultaneously movable inactive hull ears. The next closing step should attack that
flat family directly, rather than treating the braid endpoints as rigid hull data.

**Disposition:** upgraded the shallow-ear endpoint theorem to a collective original-
source matching / simultaneous-deformation fork.
