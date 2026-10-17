> Generated reading edition · [exact source](../../research/target_c_minimal_k5_reciprocal_exclusion_2026-09-18.md) · source SHA-256 `5362f8aef5fd462f771af1e94ff31e9c427aa011aa4460c2181e9ce949ddc1c4`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "e193ecaad2c606d3d0254997836d3d8210439de4", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_minimal_k5_reciprocal_exclusion_2026-09-18.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "0f36f6d5329bc4eec70649c6c8fcb590a05ee4830b2171a4cc826e959f99830a"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — the degree-pure minimal one-anchor `K_5` dual block is impossible

**Date:** 2026-09-18  
**Status:** proved candidate; theorem-state authority unchanged  
**Scope:** the five-face equality case in the one-anchor closure-corank bound  
**Depends on:** `target_c_one_anchor_k5_reciprocal_unit_force_2026-09-18.md`; `target_c_one_anchor_k5_reciprocal_turn_gap_2026-09-18.md`; `target_c_reciprocal_source_gap_forces_convex_hexagon_2026-09-18.md`; signed reciprocal length balance  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The current reciprocal reduction turns a degree-pure five-face one-anchor `K_5` dual
component into six reciprocal points `y_0,...,y_5` with a signed unit-force equilibrium
on every edge of `K_6`.  The latest source-gap theorem further forces those six points
to be the vertices of a strictly convex hexagon, with a `2+3` sign split at every
vertex, and with every cyclic force-direction gap at the five non-ground vertices
strictly below `2pi/3`.

This note closes that finite endpoint.

The missing local fact is an exact two-turn inequality for a closed equilateral
pentagon.  It forces the two-edge sign class at every non-ground reciprocal vertex to
occupy the second and fourth raw rays of the convex hexagon.  Global undirected-edge
consistency then leaves only one minority sign graph: two disjoint triangles.  The
signed reciprocal length balance forbids that graph by strict negative type of the
Euclidean distance.

Consequently the five-face equality case in the one-anchor corank theorem does not
exist.  Every nonzero one-anchor relation component has at least six faces, and the
fiber term in the closure-corank estimate improves from `n_1/5` to `n_1/6`.

---

## 1. Two consecutive turns of a closed equilateral pentagon sum to less than `pi`

Let

```math
u_1,\ldots,u_5\in S^1,
\qquad
u_1+\cdots+u_5=0,
\tag{1.1}
```

be in cyclic angular order.  Write `delta_i in (0,pi)` for the positive cyclic angular
gap from `u_i` to `u_{i+1}`, with indices modulo five.  Assume, as holds for each
non-ground reciprocal force pentagon,

```math
\delta_i<{2\pi\over3}
\qquad(1\le i\le5).
\tag{1.2}
```

Fix `i`.  Closure gives

```math
u_i+u_{i+1}+u_{i+2}=-(u_{i+3}+u_{i+4}).
\tag{1.3}
```

The right side has magnitude

```math
|u_{i+3}+u_{i+4}|
=2\cos(\delta_{i+3}/2)>1
\tag{1.4}
```

by (1.2).  Squaring the left side therefore gives

```math
3+2\left(
\cos\delta_i+
\cos\delta_{i+1}+
\cos(\delta_i+\delta_{i+1})
\right)>1.
\tag{1.5}
```

Equivalently,

```math
1+\cos\delta_i+\cos\delta_{i+1}
+\cos(\delta_i+\delta_{i+1})>0.
\tag{1.6}
```

Use the exact factorization

```math
1+\cos a+\cos b+\cos(a+b)
=4\cos(a/2)\cos(b/2)\cos((a+b)/2).
\tag{1.7}
```

The first two factors on the right are positive because `a,b in (0,pi)`.  Hence (1.6)
forces

```math
\boxed{
\delta_i+\delta_{i+1}<\pi
\qquad\text{for every }i.
}
\tag{1.8}
```

This is strict.  No limiting or compactness argument is being used.

---

## 2. The local sign classes must alternate in raw reciprocal-ray order

Fix a non-ground reciprocal vertex `y_i`.  The five raw rays

```math
g_{ij}:={y_i-y_j\over|y_i-y_j|}
\qquad(j\ne i)
\tag{2.1}
```

lie in the open hull cone at `y_i`, whose width is strictly below `pi`.  The force rays
are

```math
f_{ij}=s_{ij}g_{ij}.
\tag{2.2}
```

The latest convex-hexagon theorem says the local signs split `2+3`.  Because the raw
cone and its antipodal copy are disjoint, the two sign classes occur as two contiguous
blocks in cyclic force-angle order.

Call the size-two class `P` and the size-three class `N`.  Choose lifted force arguments
so that

```math
P_1<P_2<N_1<N_2<N_3<P_1+2\pi.
\tag{2.3}
```

Let the five consecutive force gaps be

```math
\delta_1=P_2-P_1,
\quad
\delta_2=N_1-P_2,
\quad
\delta_3=N_2-N_1,
\quad
\delta_4=N_3-N_2,
\quad
\delta_5=P_1+2\pi-N_3.
\tag{2.4}
```

To recover raw directions, the `P` rays stay fixed while the `N` rays are shifted by
`-pi`.  The two-turn inequality (1.8) gives

```math
N_1-\pi<P_1
\tag{2.5}
```

from `delta_1+delta_2<pi`, while

```math
N_2-\pi>P_1
\tag{2.6}
```

because

```math
N_2-P_1
=2\pi-(\delta_4+\delta_5)>\pi.
```

Similarly,

```math
N_2-\pi<P_2
\tag{2.7}
```

from `delta_2+delta_3<pi`, and

```math
N_3-\pi>P_2
\tag{2.8}
```

because

```math
N_3-P_2
=2\pi-(\delta_5+\delta_1)>\pi.
```

Therefore the raw reciprocal rays occur in the exact order

```math
\boxed{
N_1,\ P_1,\ N_2,\ P_2,\ N_3.
}
\tag{2.9}
```

Thus the size-two sign class occupies exactly raw positions two and four; the
size-three sign class occupies positions one, three, and five.

This conclusion is local and sign-symmetric.  It does not designate one global sign as
positive or negative.

---

## 3. On a convex reciprocal hexagon, local alternation determines the incident edges

Label the reciprocal hexagon cyclically

```math
0,1,2,3,4,5,
\tag{3.1}
```

with `0` the ground reciprocal point.  At vertex `i`, the rays to the other five
vertices occur in hull-cone order

```math
i+1,\ i+2,\ i+3,\ i+4,\ i+5
\pmod6
\tag{3.2}
```

or in the reverse order.  In either orientation, raw positions two and four are exactly
`i-2` and `i+2`, while positions one, three, and five are exactly `i-1`, `i+3`, and
`i+1`.

Therefore, at every non-ground vertex `i=1,...,5`, for either chosen global sign color:

- if that color has local degree two, its neighbors are exactly
  
  ```math
  \boxed{\{i-2,i+2\}};
  \tag{3.3}
  ```

- if that color has local degree three, its neighbors are exactly
  
  ```math
  \boxed{\{i-1,i+1,i+3\}}.
  \tag{3.4}
  ```


All indices are modulo six.

---

## 4. Seven minority edges are impossible

Choose the global minority sign color.  The preceding reciprocal sign-count theorem and
convex-hexagon refinement leave only six or seven minority edges.

Assume there are seven.  The minority degree sequence is

```math
(3,3,2,2,2,2).
\tag{4.1}
```

Take two adjacent non-ground reciprocal vertices `i,i+1`, for any
`i=1,2,3,4`.  By (3.3), a minority-degree-two vertex excludes the edge `i(i+1)`.  By
(3.4), a minority-degree-three vertex requires that edge.  Since an undirected edge
cannot simultaneously be present and absent, adjacent non-ground vertices must have
the same local minority degree.

The chain

```math
1-2-3-4-5
\tag{4.2}
```

therefore forces all five non-ground vertices to have the same minority degree.
That is incompatible with (4.1), which has exactly two degree-three vertices in total.
Hence

```math
\boxed{
\text{the `7+8` sign-count case is impossible.}
}
\tag{4.3}
```

---

## 5. Six minority edges force exactly two disjoint triangles

It remains to consider six minority edges.  Every reciprocal vertex then has minority
degree two.

For each non-ground `i`, (3.3) forces the two minority edges

```math
i(i-2),\qquad i(i+2).
\tag{5.1}
```

Collecting these undirected edges gives exactly

```math
\{02,24,40\}
\quad\sqcup\quad
\{13,35,51\}.
\tag{5.2}
```

Thus the previously allowed `C_6` two-factor disappears, and the only remaining
minority graph is

```math
\boxed{
C_3\sqcup C_3,
}
\tag{5.3}
```

with the two color classes equal to the alternating vertex triples

```math
A=\{0,2,4\},
\qquad
B=\{1,3,5\}.
\tag{5.4}
```

The nine majority edges are exactly the complete bipartite cross edges `A--B`.

---

## 6. Euclidean strict negative type contradicts the signed length balance

The reciprocal unit-force theorem gives the exact signed length balance

```math
\sum_{s_{ij}=+1}|y_i-y_j|
=
\sum_{s_{ij}=-1}|y_i-y_j|.
\tag{6.1}
```

For the sign pattern (5.3), one side of (6.1) is the sum of the six within-triangle
lengths and the other is the sum of the nine cross lengths.  Denote

```math
W:=\sum_{\{i,j\}\subset A}|y_i-y_j|
  +\sum_{\{i,j\}\subset B}|y_i-y_j|,
\qquad
C:=\sum_{i\in A,\,j\in B}|y_i-y_j|.
\tag{6.2}
```

We prove directly that

```math
\boxed{W<C}
\tag{6.3}
```

for six distinct Euclidean points split into two triples.  This is the strict negative
type of the Euclidean distance in the special form needed here.

Put

```math
c_i=
\begin{cases}
+1,&i\in A,\\
-1,&i\in B.
\end{cases}
\qquad
\sum_i c_i=0.
\tag{6.4}
```

For a unit direction `u_theta=(cos theta,sin theta)`, write

```math
t_i(\theta)=u_\theta\cdot y_i.
```

In one dimension, the identity

```math
|x-y|=\int_{-\infty}^{\infty}
\left(\mathbf1_{x>s}-\mathbf1_{y>s}\right)^2\,ds
\tag{6.5}
```

gives, using `sum c_i=0`,

```math
\sum_{i,j}c_ic_j|t_i-t_j|
=-2\int_{-\infty}^{\infty}
\left(\sum_{i:t_i>s}c_i\right)^2 ds
\le0.
\tag{6.6}
```

For every projection direction not perpendicular to one of the fifteen pair
differences, all six projected coordinates are distinct.  Then the step function in
(6.6) cannot vanish identically: immediately after the largest projected coordinate it
has value `+1` or `-1`.  Hence (6.6) is strict for every such direction.  The excluded
directions form a finite set.

Finally use the planar projection formula

```math
|x|={1\over4}\int_0^{2\pi}|u_\theta\cdot x|\,d\theta.
\tag{6.7}
```

Integrating the strict one-dimensional inequality gives

```math
\sum_{i,j}c_ic_j|y_i-y_j|<0.
\tag{6.8}
```

But the left side is exactly

```math
2(W-C).
\tag{6.9}
```

Therefore `W<C`, proving (6.3).  This contradicts the exact equality (6.1).

Thus

```math
\boxed{
\text{the `6+9` sign-count case is also impossible.}
}
\tag{6.10}
```

Together with Section 4, no signed reciprocal `K_6` satisfying the inherited source
geometry exists.

---

## 7. Corollary: the five-face one-anchor equality block is removed

The reciprocal `K_6` was derived from precisely the degree-pure support-five equality
case in the one-anchor transpose-kernel theorem.  Sections 1--6 exclude that reciprocal
system.  Hence a nonzero one-anchor relation component cannot have five vertices.

The earlier theorem already proves that every such component has minimum relation
degree at least four and that the relation graph is simple.  Therefore every nonzero
component now has at least six one-anchor faces.

Since one connected relation component contributes at most one scalar dimension to the
one-anchor fiber,

```math
\boxed{
\dim\ker(P|_{\ker C_{face}^T})
\le {n_1\over6}.
}
\tag{7.1}
```

The closure-corank estimate improves from

```math
\sigma_C\le2n_0+n_2+{n_1\over5}
```

to

```math
\boxed{
\sigma_C\le2n_0+n_2+{n_1\over6}.
}
\tag{7.2}
```

With

```math
E_U:=a_F+{x_A\over2}+{n_0+n_2\over2},
\qquad
f=a_F+n_0+n_1+n_2,
\tag{7.3}
```

coefficient comparison gives the convenient aggregate form

```math
\boxed{
\sigma_C\le {f\over6}+{11\over3}E_U.
}
\tag{7.4}
```

Indeed the right side of (7.4) minus the right side of (7.2) is

```math
{23\over6}a_F+{11\over6}x_A+n_2\ge0.
\tag{7.5}
```

No theorem-state file is changed.

**Disposition:** proved a two-turn inequality for the five inherited source force
pentagons; used it to force exact sign alternation around every non-ground reciprocal
hull vertex; eliminated the `7+8` sign case by undirected-edge consistency; forced the
`6+9` case to `C_3 sqcup C_3`; excluded that final pattern by strict negative type of
Euclidean distance and the reciprocal signed-length balance; and improved the
one-anchor closure-corank fiber coefficient from `1/5` to `1/6`.  C-II remains open.
