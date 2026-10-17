> Generated reading edition · [exact source](../../../../docs/targets/target-c/91-explicit-ordered-grid-audit.md) · source SHA-256 `d3587149cab057f427a6d33d5a8c2fcfe9f791338d7c428d3c9de63ab11a74fc`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 5 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

# Target C — explicit ordered grid from the dense inverse-phase core

**Date:** 2026-09-12
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

Canonical Section 90 removes the unknown Fox--Pach constant at the dense-graph stage: in one canonical Type-II harmonic carrier it produces a simple bipartite train-crossing graph with `Omega(D^2)` actual crossings on `O(D)` local train segments, fixed distinct phase labels, and all reduced phases in one interval of width `O(1/D)`.

A dense graph alone is not enough for the Section-76 diameter theorem, which needs a complete train grid. This module closes that remaining extraction gap by using geometry that an arbitrary dense bipartite graph does not have:

1. every crossing edge is directed from the lower reduced phase to the higher reduced phase;
2. after a dense phase-threshold cut, all trains on one shore have lower reduced phase than all trains on the other shore;
3. the Section-76 cone argument then makes every retained train strictly monotone in one common linear coordinate, with one crossing sign;
4. after partitioning that coordinate into finitely many endpoint-balanced slabs, a positive fraction of crossings have one train spanning the whole slab;
5. neighbors of a curve among a pairwise-disjoint spanning family form an interval; and
6. a dense consecutive-ones bipartite graph contains an explicit linear-by-linear biclique.

The result is an internally proved complete ordered train grid with an explicit positive coefficient depending only on the internal Section-90 constants. No pseudosegment density theorem is used.

---

# 91. Dense inverse-phase cores contain explicit linear complete grids

Work along the Type-II sequence and inside the same Section-88 harmonic carrier used in canonical Section 90. Use the Section-90 dense inverse-phase core before or after its minimum-degree pruning. Thus there are fixed constants

```math
C_0>0,\qquad \eta_0>0,\qquad K_0>0
\tag{91.1}
```

and two families `A,B` of local train segments such that, for all sufficiently large `D`,

```math
N:=|A|+|B|\le C_0D,
\qquad
E:=e(A,B)\ge\eta_0D^2,
\tag{91.2}
```

all trains in `A` have one phase label, all trains in `B` have a distinct phase label, every edge is an actual strict-rhombus crossing, and all reduced phases `x_tau` lie in one interval of width

```math
W_D\le {K_0\over D}.
\tag{91.3}
```

For each actual crossing, orient the labels so that `ell_B-ell_A=1 mod 3`. The canonical phase law then gives

```math
\boxed{x_b-x_a=\delta_{ab}>0}
\qquad(ab\in E).
\tag{91.4}
```

The graph is simple because two local train segments cross at most once.

Canonical Section 89 permits `C_0=6\pi` after increasing the large-`D` threshold: the whole carrier has fewer than `6\pi D` local train segments. The proof below keeps `C_0` symbolic.

## 91.1 A dense forward graph has a quadratic phase cut

We first use only the total order supplied by the reduced phases.

### Lemma 91.1 — ordered-cutwidth lower bound

Let a simple graph on `N` ordered vertices have `E` edges, each directed forward in the order. If `E>=4N`, some order cut is crossed by at least

```math
\boxed{{E^2\over8N^2}}
\tag{91.5}
```

edges.

### Proof

Let

```math
r:=\left\lfloor{E\over2N}\right\rfloor.
```

Then `r>=E/(4N)>=1`. An edge has **short order span** if it crosses fewer than `r` order cuts. For each left endpoint there are fewer than `r` possible right endpoints, so there are at most

```math
Nr\le {E\over2}
```

short edges. At least `E/2` edges therefore have order span at least `r`.

Let `M` be the largest number of edges crossing one order cut. Summing the crossing count over all `N-1` cuts counts each edge exactly its order span, so

```math
MN
\ge
\sum_e \operatorname{span}(e)
\ge
r{E\over2}
\ge {E^2\over8N}.
```

Hence `M>=E^2/(8N^2)`. `square`

The phase order can have ties. Break ties arbitrarily to obtain a total order. No edge has equal-phase endpoints by (91.4). If a maximizing order cut lies inside one equal-phase class, every edge crossing that artificial cut crosses at least one of the two genuine cuts immediately before or immediately after the whole tie class. Therefore one genuine cut between two distinct phase values carries at least half the edges of the artificial cut.

Consequently there is a real threshold `t` not equal to any retained phase such that the subgraph

```math
G_t:=\{ab\in E:x_a<t<x_b\}
\tag{91.6}
```

has

```math
\boxed{
e(G_t)\ge\gamma D^2,
\qquad
\gamma:={\eta_0^2\over16C_0^2}>0.
}
\tag{91.7}
```

Indeed (91.5), the tie correction, (91.2), and `E/N -> infinity` give (91.7) for all sufficiently large `D`.

Let `A_t,B_t` be the vertices incident with `G_t`. Then

```math
\boxed{
\max_{a\in A_t}x_a<t<\min_{b\in B_t}x_b.
}
\tag{91.8}
```

Both shores are automatically linear because their opposite shore has at most `C_0D` vertices:

```math
|A_t|,|B_t|\ge {\gamma\over C_0}D.
\tag{91.9}
```

## 91.2 The phase-separated core has one common monotone coordinate

Put `L=pi/3`. Choose real representatives

```math
\alpha_a=x_a+L\ell_A,
\qquad
\beta_b=x_b+L(\ell_A+1).
```

By (91.8),

```math
\beta_b-\alpha_a>L
\qquad(a\in A_t,b\in B_t).
\tag{91.10}
```

By (91.3), for all sufficiently large `D`,

```math
\beta_b-\alpha_a<L+W_D<2L.
\tag{91.11}
```

These are exactly the strict angular inequalities used in canonical Section 76. Completeness was not used in its projection-cone calculation. Orient every `A_t` train canonically and every `B_t` train opposite to its canonical orientation. The Section-76 construction therefore gives one unit vector `e` such that

```math
X(p):=e\cdot p
\tag{91.12}
```

strictly increases along every retained train centerline.

Every retained train is an `X`-monotone graph over one interval. At every actual `A_t`--`B_t` crossing, the determinant sign is the Section-76 sign: as `X` increases, the `A_t` graph passes from below the `B_t` graph to above it.

Because all inequalities are strict and only finitely many train segments are present for each `D`, perturb `e` arbitrarily slightly if necessary so that all train-end `X` coordinates are distinct and no slab boundary chosen below passes through a crossing. Strict monotonicity and the crossing sign are unchanged.

## 91.3 Endpoint-balanced slabs leave a dense spanning-family subgraph

Fix once and for all an integer

```math
M_0\ge {8C_0^2\over\gamma}.
\tag{91.13}
```

Partition the real `X` axis into `M_0` consecutive open slabs using `M_0-1` cuts chosen between endpoint coordinates so that each slab contains at most

```math
{2N\over M_0}+2
\tag{91.14}
```

train endpoints. For sufficiently large `D`, this is at most

```math
{4C_0D\over M_0}.
\tag{91.15}
```

Assign each crossing edge of `G_t` to the unique slab containing its crossing.

Call an assigned edge **bad** if both of its train segments have at least one endpoint in its crossing slab. If slab `j` contains `p_j` train endpoints, the number of `A_t` trains and `B_t` trains with an endpoint there has sum at most `p_j`, so at most `p_j^2/4` assigned edges can be bad in that slab. Since

```math
\sum_jp_j\le2N,
```

(91.15) gives

```math
\sum_j\#\{\text{bad edges in slab }j\}
\le {1\over4}\left(\max_jp_j\right)\sum_jp_j
\le {2C_0^2\over M_0}D^2
\le {\gamma\over4}D^2.
\tag{91.16}
```

Thus at least `3gamma D^2/4` phase-cut edges are not bad. For each nonbad edge, at least one of its two train segments has no endpoint in the crossing slab. Since that train is `X`-monotone and contains the crossing, its two endpoints lie on opposite sides of the slab: it spans the whole slab.

Assign every nonbad edge to one of its spanning shores. One shore receives at least half the assignments, and one of the `M_0` slabs receives at least the average. Therefore some slab `S` and, after interchanging the shore names if necessary, a family `B_S` of pairwise-disjoint `B_t` trains spanning `S` support at least

```math
\boxed{
E_S\ge \varepsilon_0D^2,
\qquad
\varepsilon_0:={3\gamma\over8M_0}>0
}
\tag{91.17}
```

actual `A_t`--`B_S` crossings inside `S`.

For the next step enlarge this assigned edge set to **all** actual crossings inside `S` between the incident `A_t` trains and the spanning family `B_S`. This can only increase the edge count. Every such crossing still has the fixed phase labels and, because both phases remain in the Section-90 bin, angular defect at most `W_D=O(1/D)`.

## 91.4 Spanning disjoint trains give interval neighborhoods

Order the curves in `B_S` from bottom to top at one vertical side of `S`. They are pairwise disjoint and each spans the slab, so that vertical order is the same throughout `S`.

### Lemma 91.2 — interval-neighborhood lemma

For any retained `A_t` train `a`, the `B_S` trains that cross `a` inside `S` form one interval in this vertical order.

### Proof

Suppose `a` crosses `b_i` and `b_k`, with `b_i` below `b_j` below `b_k`. The common crossing sign implies that `a` cannot cross `b_k` before `b_i`: immediately after a crossing of `b_k`, the curve `a` is above `b_k` and hence above `b_i`, so a later crossing of `b_i` with the required below-to-above sign is impossible.

Thus the `b_i` crossing occurs first. At that crossing,

```math
a=b_i<b_j.
```

At the later `b_k` crossing,

```math
a=b_k>b_j.
```

The `X` domain of `a` contains the whole interval between these two crossing coordinates, while `b_j` spans all of `S`. Continuity therefore forces a crossing of `a` with `b_j` between them. The pseudosegment theorem makes that crossing unique. `square`

Hence the crossing graph in `S`, with `B_S` in its vertical order, has the consecutive-ones property on the `A` neighborhoods.

## 91.5 A dense consecutive-ones graph contains an explicit linear biclique

We record the elementary extraction with constants.

### Lemma 91.3 — dense interval rows contain a linear rectangle

Let a bipartite graph have at most `CD` vertices on each shore, at least `epsilon D^2` edges, and suppose every neighborhood on the first shore is an interval in one fixed order of the second shore. Then, for all sufficiently large `D`, it contains a complete bipartite graph with shore sizes at least

```math
\boxed{
{\epsilon^2\over18C^3}D
}
\tag{91.18}
```

on each side.

### Proof

Call a row long if its degree is at least

```math
L_0:={\epsilon\over2C}D.
```

Rows shorter than `L_0` carry at most

```math
CD\,L_0={\epsilon\over2}D^2
```

edges, so the long rows carry at least `epsilon D^2/2` edges. Since the ordered shore has at most `CD` vertices, there are at least

```math
{\epsilon\over2C}D
\tag{91.19}
```

long rows.

Let

```math
b:=\left\lfloor{L_0\over2}\right\rfloor.
```

For sufficiently large `D`,

```math
b\ge {\epsilon\over8C}D.
\tag{91.20}
```

Partition the ordered shore into consecutive blocks of `b` vertices, with one possibly shorter final block. Every interval of length at least `L_0>=2b` contains a full block. The number of full blocks is at most

```math
{CD\over b}+1
\le {9C^2\over\epsilon},
\tag{91.21}
```

where `epsilon<=C^2` follows from the trivial edge upper bound.

Assign each long row one full block contained in its interval neighborhood. By (91.19)--(91.21), one block is contained in at least

```math
{\epsilon^2\over18C^3}D
```

long-row neighborhoods. That block itself has at least `epsilon D/(8C)` vertices, and

```math
{\epsilon^2\over18C^3}
\le {\epsilon\over8C}
```

because `epsilon<=C^2`. The chosen rows and block therefore contain the claimed complete bipartite graph. `square`

Apply Lemma 91.3 with `C=C_0` and `epsilon=epsilon_0` from (91.17). There are train families

```math
A_0\subset A_t,
\qquad
B_0\subset B_S
```

such that every member of `A_0` crosses every member of `B_0` in an actual strict rhombus inside the same harmonic carrier and

```math
\boxed{
|A_0|,|B_0|\ge c_{grid}D,
\qquad
c_{grid}:={\varepsilon_0^2\over18C_0^3}>0.
}
\tag{91.22}
```

The coefficient is explicit in the internal Section-90 constants:

```math
\gamma={\eta_0^2\over16C_0^2},
\qquad
M_0=\left\lceil{8C_0^2\over\gamma}\right\rceil,
\qquad
\varepsilon_0={3\gamma\over8M_0},
\qquad
c_{grid}={\varepsilon_0^2\over18C_0^3}.
\tag{91.23}
```

It is numerically crude; no claim of coefficient optimality is made.

## 91.6 The extracted grid is ordered and inverse-diameter phase-collapsed

The two shores have fixed distinct phase labels and satisfy the strict phase separation (91.8). Every cross-shore pair actually crosses. Therefore canonical Section 76 applies to `A_0 x B_0`:

- both shores are internally noncrossing;
- all crossings have the same sign;
- every shore sees the other shore in one common order; and
- the hole-stable complete-grid diameter argument applies.

Moreover all vertices are still drawn from the single Section-90 phase bin of width `K_0/D`. Thus every crossing defect satisfies

```math
0<\delta_{ab}\le {K_0\over D}.
\tag{91.24}
```

Let `d_*` be the diameter of the same harmonic cell. Repeating the already-canonical Section-78 localization of the Section-76 path argument gives

```math
\boxed{
 d_*
 \ge
 {\sqrt3\over2}(|A_0|+|B_0|)
 -{S_{A_0B_0}\over\min(|A_0|,|B_0|)}-2,
}
\tag{91.25}
```

where

```math
S_{A_0B_0}:=\sum_{a\in A_0,b\in B_0}\delta_{ab}.
```

Equation (91.24) gives

```math
{S_{A_0B_0}\over\min(|A_0|,|B_0|)}
\le
K_0{\max(|A_0|,|B_0|)\over D}
\le K_0C_0,
\tag{91.26}
```

so in particular

```math
\boxed{
 d_*
 \ge
 {\sqrt3\over2}(|A_0|+|B_0|)-O(1).
}
\tag{91.27}
```

This is now an explicit, internally derived complete ordered near-triangular grid inside the canonical `>=0.8896708101D-o(D)` harmonic carrier. The unknown Fox--Pach pseudosegment-density coefficient is absent.

## 91.7 What this closes and what remains

Section 91 strengthens the Type-II handoff from

```text
explicit dense inverse-phase crossing core
+ abstract/unknown-constant complete-grid extraction elsewhere
```

to

```text
one macroscopic harmonic carrier
+ explicit dense inverse-phase core
+ quadratic forward phase cut
+ endpoint-balanced spanning slab
+ consecutive-ones crossing graph
+ explicit c_grid D x c_grid D complete ordered grid
+ every crossing defect O(1/D).
```

The present coefficient `c_grid` is far too crude to force

```math
|A_0|+|B_0|>{2\over\sqrt3}D
```

and hence does not yet contradict `d_*<=D`. This is a real quantitative obstruction, not an unknown external-constant obstruction.

The next useful theorem should therefore aggregate **many** interval blocks or use the linear-minimum-degree core from Section 90 to prove that a much larger fraction of the carrier train mass participates in one ordered near-Cartesian structure. Merely extracting one biclique again will not close C-II.

## 91.8 Dependency audit

- **Canonical `C-HARMONIC-WRAPPING`:** supplies the macroscopic Type-II harmonic carrier.
- **Canonical `C-HARMONIC-CARRIER-QUAD` and `C-HARMONIC-TRAIN-BUDGET` / Sections 82 and 89:** supply `O(D)` local train count, with Section 89 allowing `C_0=6pi`.
- **Canonical Section 90:** supplies the dense inverse-diameter fixed-phase crossing core (91.1)--(91.4).
- **Canonical `C-HOLE-GRID-DIAMETER` / Section 76:** supplies the common projection/sign/order theorem and complete-grid diameter inequality once the phase-separated complete grid is obtained.
- **Canonical `C-HARMONIC-GRID-LOCAL` / Section 78:** supplies the localization of that diameter argument from global `D` to the diameter of the containing harmonic cell.
- **No Fox--Pach theorem:** not used anywhere in Section 91.
- **No KKT coefficient floor:** physical train crossings are not converted into multiplier lower bounds.
- **Contact-isolated source points:** untouched.

**Status:** canonical; promoted by the independent Sections-90–94 audit.
**Theorem state:** `2026-09-11.audit.36`.
