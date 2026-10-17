> Generated reading edition · [exact source](../../../docs/reports/target_c_three_terminal_penny_circuit_tradeoff_2026-09-10.md) · source SHA-256 `b8f33b29000237d3e6a3fd887705fe773c15e63cad66e53d2c72f9b6560af0e7`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-BCBB90EAD18F","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — three-terminal penny deficit and extreme-circuit diameter/flex tradeoff

**Date:** 2026-09-10  
**Repository state:** PR #178 after EC/CT; uses current `main` FS and PI reports  
**Run type:** exact graph theorem + asymptotic geometric circuit sharpening  
**Target:** Target C, C-II after ZF  
**Depends on:** Eppstein degree-two lemma, EC extreme positive circuits, FS.4 common-center diameter geometry, PI.2 projective direction packing  
**External input:** no new external theorem; Eppstein's 2018 penny-graph lemma is already imported in the repository  
**Computation:** decimal root evaluation only

## LEVEL I STATUS

`STILL OPEN`.

Eppstein's standard edge/diameter theorem protects two endpoints of one graph-diameter
path during its induction.  The proof actually permits three protected terminals.
This gives a stronger edge deficit when the positive contact graph must connect three
geometrically separated diameter endpoints.

For a connected graph `G` and a terminal set `T`, let

```math
\tau_G(T)
```

be the minimum number of edges in a connected subgraph of `G` containing `T`.
For `|T|=2` this is ordinary graph distance.

### Theorem TP.1 — three-terminal Eppstein bound

If `G` is a connected triangle-free penny graph on `n` vertices and
`T subset V(G)` has `|T|<=3`, then

```math
\boxed{
|E(G)|\le2n-\tau_G(T)-2.
}
\tag{TP.1}
```

For an extreme selected KKT circuit, combine TP.1 with two separated positive diameter
chords.  If

```math
y:=\lim\frac{h_*}{D},
\qquad
s:=\lim\frac{\sigma_*}{D}
```

along a convergent subsequence, then

```math
\boxed{
y+s
\ge
\mathcal S(y):=
\sqrt{1+\frac{\sqrt3}{2}
\sin(\min\{y,\pi/2\})}.
}
\tag{TP.2}
```

In particular, if `sigma_*=o(D)`, then

```math
\boxed{
\liminf\frac{h_*}{D}\ge\gamma
=1.35891835330307\ldots,
}
\tag{TP.3}
```

where `gamma` is the unique root in `(1,pi/2)` of

```math
\boxed{
\gamma^2
=1+\frac{\sqrt3}{2}\sin\gamma.
}
\tag{TP.4}
```

Thus a near-maximal extreme rigidity circuit cannot concentrate its positive diameter
support on a small number of bars. Conversely, an extreme ray with small normalized
diameter support must pay a linear selected-support flex deficit.

---

## 1. Proof of the three-terminal penny theorem

Eppstein proves that every triangle-free penny graph containing a cycle has at least
four non-articulation vertices of degree at most two.  Fix `T` with `|T|<=3`.

We induct on `n`.

If `G` is a tree, then `|E|=n-1` and every connected subgraph spanning `T` uses at
most all `n-1` tree edges. Hence

```math
n-1\le2n-\tau_G(T)-2.
```

Now suppose `G` contains a cycle. Among Eppstein's at least four removable
non-articulation vertices of degree at most two, choose one

```math
v\notin T.
```

Set `G'=G-v`. Then `G'` is connected and triangle-free penny, with

```math
|E(G)|\le|E(G')|+2.
\tag{1.1}
```

Deleting a nonterminal vertex cannot create a smaller connected terminal-spanning
subgraph, so

```math
\tau_{G'}(T)\ge\tau_G(T).
\tag{1.2}
```

By induction,

```math
|E(G')|
\le2(n-1)-\tau_{G'}(T)-2
\le2n-\tau_G(T)-4.
```

Combine with (1.1) to obtain TP.1. `square`

The restriction `|T|<=3` is exactly what the four-removable-vertex lemma supports
without a stronger penny-graph theorem. For two terminals TP.1 recovers Eppstein's
`2n-distance-2` inequality.

---

## 2. Euclidean Steiner length lower-bounds contact Steiner size

Let three source points `a,b,c` be terminals of a unit-contact graph. Any connected
contact subgraph spanning them is a geometric network whose every edge has length one.
Its number of edges therefore equals its Euclidean total edge length. Allowing arbitrary
Steiner points can only lower the minimum possible network length. Hence

```math
\boxed{
\tau_C(\{a,b,c\})
\ge L_{ST}(a,b,c),
}
\tag{2.1}
```

where `L_ST` is the ordinary Euclidean Steiner-tree length of the three points.

For a triangle with side lengths `A,B,C`, area `Delta`, and all angles below
`120 degrees`, the classical elementary Steiner construction gives

```math
\boxed{
L_{ST}^2
=\frac{A^2+B^2+C^2+4\sqrt3\,\Delta}{2}.
}
\tag{2.2}
```

Only the right-triangle limit of this formula is needed below.

---

## 3. Two selected diameter directions produce a long three-terminal tree

Let an extreme normalized KKT stress have selected positive diameter graph `H_*`, with
`h_*` edges. Every selected diameter edge is an actual source diameter edge.

PI.2 applies to any subset of actual diameter directions. With

```math
\delta_D=2\arcsin\frac1{2D},
```

there are two selected diameter edges whose projective angle `theta_D in[0,pi/2]`
satisfies

```math
\boxed{
\theta_D
\ge
\min\left\{(h_*-1)\delta_D,\frac\pi2-\delta_D\right\}.
}
\tag{3.1}
```

Assume first that `h_*/D -> y>0`. Then the right side has a positive limiting lower
bound. FS.3 says two actual diameter edges sharing an endpoint have angle
`O(D^{-1/4})`. Therefore the two edges realizing a fixed positive asymptotic spread
are disjoint for all sufficiently large members of the subsequence.

Write them as

```math
aa',\qquad bb',
```

and orient their unit direction vectors `u,v` so the angle from `u` to `v` is
`theta_D`. Let `m_1,m_2` be the two chord midpoints. FS.4 gives one full-source
circumcenter `o` with

```math
|m_i-o|=O(D^{3/4})=o(D).
\tag{3.2}
```

Thus, after choosing `b` rather than `b'` if necessary,

```math
\begin{aligned}
|a-a'|&=D,\\
|a-b|&=D\sin(\theta_D/2)+o(D),\\
|a'-b|&=D\cos(\theta_D/2)+o(D).
\end{aligned}
\tag{3.3}
```

The limiting triangle is right, with normalized side lengths

```math
1,\quad\sin(\theta/2),\quad\cos(\theta/2).
```

Its normalized area is `sin(theta)/4`. Every limiting angle is below 120 degrees for
`theta>0`, so (2.2) and continuity give

```math
\boxed{
L_{ST}(a,a',b)
=
D\sqrt{1+\frac{\sqrt3}{2}\sin\theta_D}+o(D).
}
\tag{3.4}
```

All three terminals lie in the connected selected positive contact component.
Therefore TP.1 and (2.1) apply to that contact graph.

---

## 4. Insert the extreme-circuit edge count

EC gives

```math
e_*+h_*=2v_*-2-\sigma_*.
\tag{4.1}
```

TP.1 with the terminals from Section 3 gives

```math
e_*
\le2v_*-	au_*-2,
\tag{4.2}
```

where `tau_*` is their selected contact Steiner size. Subtract (4.2) from (4.1):

```math
\boxed{h_*+\sigma_*\ge\tau_*.}
\tag{4.3}
```

Combining with (3.4), dividing by `D`, and using

```math
D\delta_D\to1
```

proves for `y>0`

```math
y+s
\ge
\sqrt{1+\frac{\sqrt3}{2}
\sin(\min\{y,\pi/2\})}.
```

If `y=0`, the ordinary two-terminal Eppstein theorem applied to the endpoints of any
positive diameter edge gives

```math
h_*+\sigma_*\ge\lceil D\rceil,
```

so `s>=1=mathcal S(0)`. Hence TP.2 holds throughout the full nonnegative domain.

---

## 5. Consequences

### 5.1 Near-maximal circuits carry at least `1.3589 D` diameter edges

If `sigma_*=o(D)`, TP.2 reduces for any limit `y<pi/2` to

```math
y\ge\sqrt{1+\frac{\sqrt3}{2}\sin y}.
```

The right side minus `y` is positive at `y=1` and negative by `y=pi/2`; its unique
zero is `gamma` from TP.4. Therefore TP.3 follows.

The uniqueness follows by differentiating

```math
f(y)=y^2-1-\frac{\sqrt3}{2}\sin y:
\qquad
f'(y)=2y-\frac{\sqrt3}{2}\cos y>0
```

for `y>=1`.

### 5.2 Sparse positive diameter support forces linear flex deficit

For every subsequential limit with `0<=y<=gamma`,

```math
\boxed{
\liminf\frac{\sigma_*}{D}
\ge
\mathcal S(y)-y.
}
\tag{5.1}
```

Examples:

- `y->0` forces `sigma_*/D>=1-o(1)`;
- `y=1/2` forces a positive constant flex deficit;
- only once `y` reaches `gamma` can `sigma_*=o(D)` occur.

By CT,

```math
z_*-s_Z=2(v-v_*)+\sigma_*\ge\sigma_*.
```

Hence the same lower bound applies to the excess number of zero coordinates beyond
the unavoidable `s_Z` polytope dimension:

```math
\boxed{
\liminf\frac{z_*-s_Z}{D}
\ge\mathcal S(y)-y.
}
\tag{5.2}
```

Thus a diameter-sparse extreme ray is necessarily a strongly degenerate vertex of the
KKT polytope.

### 5.3 Selected outer/face topology also pays the three-terminal deficit

CT gives

```math
q_*+2\sigma_*=x_*+Q_*+2d_*,
\qquad
h_*=q_*-d_*.
```

Therefore

```math
h_*+\sigma_*
=x_*+Q_*+d_*-\sigma_*.
```

Using (4.3),

```math
\boxed{
x_*+Q_*+d_*
\ge\tau_*+\sigma_*.}
\tag{5.3}
```

In the positive-spread asymptotic regime this becomes

```math
\liminf\frac{x_*+Q_*+d_*}{D}
\ge
\mathcal S(y)+s.
\tag{5.4}
```

So selected underbracing costs twice: it directly removes mixed rows and also forces
additional outer/face/component topology.

---

## 6. Regression audit

- A one-diameter straight chain has `h_*=1`, `sigma_*=D-1`, and saturates the
  two-terminal endpoint `h_*+sigma_*=D`; it lies at `y=0,s=1` in TP.2.
- A regular odd-shell extreme circuit is not contradicted. Exact small-shell
  enumeration shows its positive circuits are full-vertex maximal circuits; their
  diameter support is already much larger than `gamma D`.
- TP.1 is not asserted for four protected terminals. Eppstein's four removable
  low-degree vertices only guarantee a removable vertex outside a protected set of
  size at most three.
- FS common-center geometry is used only after the selected direction spread has a
  fixed positive limit. The `y=0` endpoint is handled separately.
- The theorem concerns selected extreme circuits. It does not replace the stronger
  full-support DB bound `h/D>=2rho` for the relative-interior actual diameter graph.

---

## 7. Next theorem

TP leaves a sharp dichotomy for each extreme ray:

1. `sigma_*=o(D)` implies `h_*>= (gamma-o(1))D`, so the selected diameter support is a
   large Woodall caterpillar/odd-unicycle and should be attacked by circular-planar
   response plus near-antipodal geometry;
2. `h_*<(gamma-epsilon)D` forces `sigma_*=Omega(D)` and, by CT, at least the same
   linear excess degeneracy `z_*-s_Z`. The next target is to show that this much
   selected flex rank cannot be blocked by omitted strong rows without producing a
   second positive circuit with substantially larger diameter support.

A concrete matroid statement would be enough: prove that a full-support positive
stress on the C65 mixed rigidity matroid has an extreme positive circuit satisfying
`z_*-s_Z=o(D)`. TP would then immediately produce a selected support with at least
`(gamma-o(1))D` positive diameter bars.

---

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Three-terminal Eppstein theorem:
For connected triangle-free penny G and |T|<=3,
    |E(G)| <= 2|V(G)| - tau_G(T) - 2,
where tau_G(T) is minimum edge count of a connected subgraph spanning T.
Proof: Eppstein supplies >=4 removable non-articulation degree<=2 vertices, so one can
induct while protecting all three terminals.

For an extreme selected KKT circuit:
    e_*+h_*=2v_*-2-sigma_*.
Two selected diameter directions have spread
    theta >= min((h_*-1)delta_D, pi/2-delta_D).
FS.4 makes two fixed-spread diameter chords asymptotically centered at the same o.
Three suitable endpoints form a right-triangle limit with Steiner length
    D sqrt(1+(sqrt3/2)sin theta)+o(D).
Therefore, if h_*/D->y and sigma_*/D->s,
    y+s >= S(y):=sqrt(1+(sqrt3/2)sin(min(y,pi/2))).

If sigma_*=o(D), then
    h_*/D >= gamma-o(1),
    gamma=1.35891835330307...,
    gamma^2=1+(sqrt3/2)sin gamma.
If h_* is smaller, the exact deficit becomes linear in sigma_* and therefore in
z_*-s_Z via CT.
```
