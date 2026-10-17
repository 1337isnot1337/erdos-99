> Generated reading edition · [exact source](../../../docs/reports/target_c_post_zf_cyclic_endpoint_stress_polytope_2026-09-09.md) · source SHA-256 `9789e0b114104d3e4f057ba39915f48b5147b4b327390a964ce7c61801c97e70`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 16 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-E6CC222342F1","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic endpoint: selected-stress support and quadratic rattlers

**Date:** 2026-09-09  
**Repository base:** PR #118 after ME  
**Run type:** exact selected-stress classification / endpoint reduction  
**Target:** Target C, C-II after ZF  
**Depends on:** PN/ME primitive endpoint, canonical positive-support connectivity and force-hull theorem C4, ZF/ZR, DB area floor  
**External web search:** not used in the proof  
**Computation:** displayed decimals only

## LEVEL I STATUS

`STILL OPEN`

PN and ME reduce the exact primitive equality

```math
m+d_H+s_Z=2
```

to one survivor:

```math
\boxed{
 m=0,
 \qquad d_H+s_Z=2,
 \qquad C=C_q.}
\tag{CY.0}
```

Thus the complete nonisolated positive contact core is the convex loaded force-hull cycle, every one of its `q` hull sides is a unit contact, and there are no unpinned contact vertices.

This endpoint is more rigid at the KKT-polytope level than the full-support description suggests. The main new result is:

> **Every normalized KKT stress, including every boundary and extreme stress, keeps all `q` cycle contacts strictly positive.**

Consequently every selected positive diameter support must cover all `q` force-hull vertices.

The endpoint also forces a quadratic contact-isolated population in the full source.

---

## 1. Endpoint bookkeeping

From `C=C_q` on the `q` loaded convex vertices,

```math
 v=e=q.
\tag{1.1}
```

The outer contact-face walk is the convex unit cycle itself, so

```math
 b=q,
 \qquad x_B=0.
\tag{1.2}
```

There is one bounded contact face of degree `q`, hence

```math
\boxed{Q=q-4.}
\tag{1.3}
```

The primitive equality gives

```math
\boxed{d_H+s_Z=2.}
\tag{1.4}
```

Since `d_H=q-h`,

```math
\boxed{h=q-d_H,}
\qquad
(d_H,s_Z)\in\{(0,2),(1,1),(2,0)\}.
\tag{1.5}
```

Thus the full diameter graph has `q`, `q-1`, or `q-2` edges.

---

## 2. A selected stress cannot delete a cycle contact

Let

```math
s=(\alpha,\beta)
```

be an arbitrary normalized KKT stress of the same fixed source. Let `C_s` and `H_s` denote its positive contact and diameter supports.

Canonical positive-support connectivity says `C_s` has one nontrivial connected component containing every endpoint of `H_s`. The force-hull theorem gives

```math
\operatorname{conv}V(C_s)
=
\operatorname{conv}B_s,
\tag{2.1}
```

where `B_s=V(H_s)`, and every vertex of the selected force hull belongs to `B_s`.

Suppose `C_s` is a proper subset of the cycle `C_q`. Any nonempty connected proper edge subset of a cycle is a path. Let `b` be one endpoint of that positive-contact path and let `bc` be its unique positive contact.

The vertices of the original force hull are in strictly convex position. Therefore every member of `V(C_s)` is an extreme point of its own convex hull, in particular `b`. By (2.1),

```math
b\in B_s.
\tag{2.2}
```

The edge `bc` is one of the original force-hull sides. Choose its inward normal `n`, so every other selected force-hull vertex `x` satisfies

```math
n\cdot(x-b)>0.
\tag{2.3}
```

Selected KKT equilibrium at `b` is

```math
\alpha_{bc}(b-c)
=
\sum_{bk\in H_s}\beta_{bk}(b-k).
\tag{2.4}
```

The left side has zero `n`-component. Since `D>1`, `c` is not a diameter partner. Every positive diameter partner `k` is therefore a selected force-hull vertex distinct from `b,c`, so (2.3) gives

```math
n\cdot(b-k)<0.
```

All selected `beta` coefficients are positive, hence the right side of (2.4) has strictly negative `n`-component. Contradiction.

Therefore:

### Theorem CY.1 — universal positive cycle support

For every normalized KKT stress,

```math
\boxed{C_s=C_q.}
\tag{CY.1}
```

In particular every cycle contact coefficient is positive throughout the complete normalized KKT polytope.

This is stronger than maximal support: no cycle contact can even vanish on a KKT-polytope boundary face.

---

## 3. Every selected diameter support covers every terminal

Since CY.1 gives

```math
V(C_s)=B_+
```

for every normalized stress, the selected force hull is the complete original force hull `F`. The force-hull theorem then gives

```math
\boxed{B_s=B_+.}
\tag{CY.2}
```

Equivalently:

### Corollary CY.2 — selected diameter edge cover

For every normalized KKT stress, the positive diameter graph `H_s` has no isolated vertex on the `q` loaded terminals.

Thus every KKT extreme point is supported on

1. all `q` cycle contacts; and
2. a geometric-thrackle diameter edge cover of all `q` terminals.

No KKT face may shed a boundary terminal by turning off the adjacent cycle stresses.

---

## 4. Exact KKT-polytope dimension

The full mixed active framework has

```math
q+h=2q-d_H
```

rows. ZF gives rigidity rank

```math
2q-3.
```

Hence the vector space of signed equilibrium row dependences has dimension

```math
(2q-d_H)-(2q-3)=3-d_H=s_Z+1.
\tag{4.1}
```

A nonzero pure contact self-stress is impossible on the convex cycle: at any vertex its two noncollinear contact directions force both adjacent coefficients to vanish, and this propagates around the cycle. Therefore the diameter-total functional is nonzero on every nonzero nonnegative equilibrium stress and normalization

```math
\sum_h\beta_h=1
```

reduces affine dimension by one.

Because the full-support stress lies in the relative interior, the normalized KKT polytope has exact affine dimension

```math
\boxed{\dim\mathcal S=s_Z=2-d_H.}
\tag{CY.3}
```

Thus the three cyclic subcases are:

```math
\begin{array}{c|c|c|c}
d_H&s_Z&h&\dim\mathcal S\\ \hline
0&2&q&2\\
1&1&q-1&1\\
2&0&q-2&0.
\end{array}
\tag{4.2}
```

---

## 5. Extreme-stress diameter support size

Let `s` be an extreme normalized KKT stress and put

```math
h_s:=|H_s|.
```

C57.1 says there is no nonzero normalized signed tangent supported inside `supp(s)`. Equivalently, the signed equilibrium dependence space on the selected support is one-dimensional, generated by `s` itself.

The selected support has

```math
q+h_s
```

rows. Its rigidity-matrix row rank is therefore

```math
q+h_s-1.
```

Planar rigidity rank is at most `2q-3`, so

```math
\boxed{h_s\le q-2.}
\tag{CY.4}
```

On the other hand CY.2 says `H_s` is an edge cover of all `q` vertices, hence

```math
\boxed{h_s\ge\lceil q/2\rceil.}
\tag{CY.5}
```

Therefore every KKT extreme point has

```math
\boxed{
\lceil q/2\rceil
\le |H_s|
\le q-2.}
\tag{CY.6}
```

This is a selected-stress statement; it does not assert that every intermediate KKT stress has at most `q-2` positive diameter edges.

---

## 6. The `d_H=2` subcase is a rigidity circuit

If `d_H=2`, then `s_Z=0`, so the normalized KKT polytope is a singleton. The full support has

```math
q+h=q+(q-2)=2q-2
```

rows and one signed dependence. ZF gives rank `2q-3`, and the unique dependence has every row nonzero because the singleton stress is the relative-interior full-support stress.

Hence no proper row subset can be dependent.

### Corollary CY.3 — circuit endpoint

In the cyclic `d_H=2` phase,

```math
\boxed{C_q\cup H\text{ is a planar rigidity circuit}.}
\tag{CY.7}
```

The associated signed stress matrix is the ZR matrix

```math
\Omega\succeq0,
\qquad
\operatorname{rank}\Omega=q-3,
\qquad
\ker\Omega=\operatorname{span}\{1,P_x,P_y\}.
\tag{CY.8}
```

The circuit fact alone is not a contradiction: convex geometric-thrackle forests with two tree components can satisfy the abstract Laman-circuit inequalities. Any exclusion must use Euclidean diameter geometry or the PSD sign structure, not sparsity alone.

---

## 7. Quadratic rattler population

The cyclic nonisolated core has exactly `q` vertices. Every other source point is contact-isolated.

The force hull has perimeter

```math
\operatorname{per}(F)=q.
```

The convex perimeter-diameter inequality gives

```math
q\le\pi D.
\tag{7.1}
```

The canonical strict global diameter comparison gives

```math
D^2<\frac n\Delta,
\qquad
\Delta:=\frac\pi{2\sqrt3}.
```

Therefore the number `z=n-q` of contact-isolated source points satisfies the finite lower bound

```math
\boxed{
 z
 >
 \Delta D^2-\pi D.}
\tag{CY.9}
```

In particular, along any unbounded cyclic-endpoint sequence,

```math
\boxed{
\frac z{D^2}\to\Delta
=\frac\pi{2\sqrt3}
=0.9068996821\ldots .}
\tag{CY.10}
```

Thus essentially the entire quadratic source population is KKT-invisible/contact-isolated; the mechanically active cycle contains only `O(D)` points.

This is stronger than a generic force-bulk warning but is not itself a contradiction. Strictly greater-than-one separations among isolated points can approach one with no uniform margin.

---

## 8. DB area forces a long cyclic force hull

DB gives, for every sufficiently large post-ZF survivor,

```math
\operatorname{area}(F)
\ge\frac{\sqrt3}{4}D^2.
\tag{8.1}
```

The isoperimetric inequality and `per(F)=q` give

```math
\operatorname{area}(F)
\le\frac{q^2}{4\pi}.
\tag{8.2}
```

Combining,

```math
\boxed{
 q
 \ge
 \sqrt{\pi\sqrt3}\,D
 =2.3326804523\ldots D.}
\tag{CY.11}
```

Since `h=q-d_H` and `d_H<=2`, the same leading constant holds for the full diameter-edge count:

```math
\boxed{
\liminf\frac hD
\ge\sqrt{\pi\sqrt3}
=2.3326804523\ldots .}
\tag{CY.12}
```

This is much stronger inside the cyclic endpoint than the generic DB bound `2rho=1.47817...`.

The upper perimeter bound remains

```math
q\le\pi D,
```

so CY.11 narrows but does not close the cyclic shell.

---

## 9. What the endpoint now is

The exact cyclic survivor simultaneously has:

1. a convex equilateral unit force-hull cycle on `q=Theta(D)` loaded vertices;
2. `h=q-d_H` actual diameter pairs with `d_H<=2`;
3. normalized KKT-polytope dimension at most two;
4. every KKT stress positive on every cycle edge;
5. every selected diameter graph an edge cover of all `q` vertices;
6. at least `Delta D^2-pi D` contact-isolated source points;
7. force-hull perimeter at least `2.33268...D` and at most `pi D`.

The remaining obstruction is therefore not an uncontrolled contact topology. It is coexistence of a one-dimensional mechanical shell with an asymptotically full-density two-dimensional cloud of KKT-invisible points.

---

## 10. Next theorem

There are two concrete routes.

### CY-A — selected-stress edge-cover rigidity

Use the fact that every KKT extreme has all cycle contacts positive and a diameter edge cover of size between `ceil(q/2)` and `q-2`. The `d_H=0,1` stress polytope has dimension only two or one, so all of its boundary is created solely by diameter coefficients reaching zero.

A theorem showing that such a low-dimensional positive-stress family cannot exist on a large convex equilateral diameter shell would exclude the cycle without touching the rattlers.

### CY-B — quadratic-rattler replacement

Use CY.9 together with the fact that no contact-isolated point is an actual diameter endpoint in the full-support C-II normalization. Prove that `n-O(D)` strict interior/rattler points can be retained while replacing the `O(D)` cyclic shell by a strictly smaller-diameter boundary, or can be augmented/repacked to contradict global minimality.

This is now a precise force-free replacement problem rather than a generic force-bulk theorem.

---

## 11. Promotion recommendation

**Hold as report pending independent audit.**

The selected-stress proof is exact but depends on the report-level PN/ME/ZF normalization. CY.9 and CY.11 are quantitative consequences, not a Level I closure.

---

## 12. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Primitive equality survivor:
  m=0,
  d_H+s_Z=2,
  C=C_q,
  v=e=b=q,
  Q=q-4,
  h=q-d_H.

New selected-stress theorem:
For any normalized KKT stress s, C_s cannot be a proper subset of C_q.
A connected proper subset is a path; its endpoint is an extreme vertex of the
selected force hull and therefore positively diameter-loaded. Its sole positive
hull-side contact has zero inward-normal component, while every positive diameter
reaction has strict opposite normal component. Contradiction.
Thus
  C_s=C_q
for every normalized stress, and consequently
  B_s=B_+;
every selected diameter support covers all q terminals.

Stress-polytope dimension:
  dim S = s_Z = 2-d_H.
Every extreme stress has
  ceil(q/2) <= |H_s| <= q-2.
If d_H=2, the full mixed graph C_q union H is a rigidity circuit with unique
full-support stress and ZR maximal-rank PSD matrix.

Rattlers:
  z=n-q > Delta D^2-pi D,
  Delta=pi/(2sqrt3),
so z/D^2 -> Delta=0.9068996821... .

DB + isoperimetry:
  q >= sqrt(pi sqrt3) D
    =2.3326804523... D
for sufficiently large cyclic survivors.

Next:
  low-dimensional selected-stress edge-cover exclusion,
or
  quantitative replacement of the O(D) mechanical shell around the n-O(D)
  contact-isolated cloud.
```
