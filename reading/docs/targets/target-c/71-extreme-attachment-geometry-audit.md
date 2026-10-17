> Generated reading edition · [exact source](../../../../docs/targets/target-c/71-extreme-attachment-geometry-audit.md) · source SHA-256 `435eb27b87645f4f5b594fb00a6aebde206c6d2e9d9c2d7fa776e05462740b1a`.
> [Current theorem state](../../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

# Target C — extreme-circuit attachment geometry audit

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This module independently certifies the valid mathematics from stale PR #217 against
canonical Sections 58, 62, 64, 68, and 69. It consolidates that branch's four old
modules under current numbering and keeps every selected-support deficiency explicit.

For an extreme normalized KKT stress let

```math
e_*+h_*=2v_*-2-\sigma_*,
\qquad
\kappa_*=2(v-v_*)+\sigma_*.
```

In the low-degeneracy regime `kappa_*=o(D)`:

1. the planar attachment-incidence graph has at most one component whose loaded set
   contains an internal selected diameter edge;
2. either at least `(rho-o(1))D` selected loaded-loaded mixed edges cross the
   attachment quotient, or one attachment block contains at least `(rho-o(1))D`
   internal selected diameter edges and a centered diameter-supported body of area at
   least `((rho+sin rho)/4-o(1))D^2` and inradius at least
   `(sin(rho/2)/2-o(1))D`;
3. if the cross-block family is `o(D)`, that block is almost spanning and inherits the
   full Section-59 area/inradius constants; and
4. selected pinned contact flexes have right-nullity `tau_*<=sigma_*` and cancel from
   the total selected harmonic-cell perimeter estimate.

No zero multiplier is treated as a geometric release and no KKT coefficient floor is
used.

---

## 71.1 One-dimensional extremes are high-degeneracy

The C53 one-dimensional selected support is the straight unit-contact chain between two
selected diameter endpoints. It has

```math
v_*=D+1,
\quad e_*=D,
\quad h_*=1,
\quad \sigma_*=D-1.
```

Hence `kappa_*>=D-1`; it never occurs under `kappa_*=o(D)`. Below assume the selected
force hull `F_*` is two-dimensional.

---

## 71.2 Attachment-incidence separation

Let `I_1,...,I_c` be the connected components of the selected contact graph induced by
unloaded selected vertices, with distinct loaded attachment sets `A_r subset B_*`.
Contract every `I_r` to one interior node and suppress parallel incidence edges. The
resulting bipartite graph is planar with all loaded nodes on the outer face.

Let its nontrivial connected components have loaded boundary sets `B_1,...,B_s`.
Distinct `B_i,B_j` cannot alternate around the strict convex boundary of `F_*`: a
simple arc in one connected incidence component between two alternating boundary
points separates the disk and must be crossed by the other component.

Two vertex-disjoint actual diameter segments cross. Therefore two incidence blocks
cannot both contain an internal selected diameter edge, because their four endpoints
would alternate. Thus at most one distinguished block `B^dagger` satisfies

```math
E(H_*[B^\dagger])\ne\varnothing.
\tag{71.1}
```

Write

```math
h_{int}:=|E(H_*[B^\dagger])|,
\qquad h_{cross}:=h_*-h_{int}.
```

---

## 71.3 Exact attachment quotient ledger

For one incidence block let `W_j` be its unloaded selected vertices together with
`B_j`. Outside the single-block/all-loaded exception, `W_j` is a proper vertex subset
of the selected rigidity-matroid circuit, so its induced mixed rows are independent.
Define

```math
\delta_j:=2|W_j|-3-|E((C_*\cup H_*)[W_j])|\ge0.
```

Let `u_0` count selected loaded vertices unused by every unloaded incidence component,
and let `m_cross` count selected loaded-loaded mixed edges not internal to one `B_j`.
Exact row counting gives

```math
\boxed{
m_{cross}=2u_0+3s-2-\sigma_*+\sum_j\delta_j.}
\tag{71.2}
```

The `-sigma_*` term is required. If one incidence block uses every selected loaded
vertex, the induced rows are the whole circuit and (71.2) is not applied; then
`m_cross=0` by definition.

Every selected diameter edge outside `B^dagger` is a cross edge, hence

```math
\boxed{h_*-h_{int}=h_{cross}\le m_{cross}.}
\tag{71.3}
```

Canonical Section 64 gives, when `kappa_*=o(D)`,

```math
h_*\ge(2\rho-o(1))D.
```

Therefore

```math
\boxed{
\max\{h_{int},m_{cross}\}\ge(\rho-o(1))D.}
\tag{71.4}
```

If `m_cross=o(D)`, then `h_int=h_*-o(D)` and every selected loaded vertex outside
`B^dagger` is incident to a cross selected diameter edge, so

```math
|B_*\setminus B^\dagger|\le2h_{cross}=o(D).
\tag{71.5}
```

Thus the distinguished block is almost spanning.

---

## 71.4 Geometry of the extreme support and distinguished block

Section 58's actual-diameter midpoint estimate is uniform over normalized KKT stresses.
Let `o` be the full-source circumcenter and `L_D=O(D^(3/4))=o(D)`. Then

```math
d_{Haus}(F_*-o,-(F_*-o))\le2L_D.
\tag{71.6}
```

Selected actual diameter directions are projectively separated by
`2a_D`, `a_D=asin(1/(2D))`, and their direction polygon lies in `F_*-F_*`. The
symmetry-corrected difference-body calculation gives, if `h_*/D->y`,

```math
\liminf {\operatorname{area}(F_*)\over D^2}
\ge {y+\sin y\over4},
\qquad
\liminf {r_o(F_*)\over D}\ge{1\over2}\sin(y/2).
\tag{71.7}
```

Because low degeneracy gives `y>=2rho`, every such extreme has

```math
\boxed{
\liminf {\operatorname{area}(F_*)\over D^2}
\ge {2\rho+\sin(2\rho)\over4},}
\tag{71.8}
```

```math
\boxed{
\liminf {r_o(F_*)\over D}\ge {1\over2}\sin\rho.}
\tag{71.9}
```

If the internal-block branch of (71.4) holds, let `F^dagger` be the convex hull of the
endpoints of the `h_int` internal selected diameter edges. The same midpoint and
direction argument applies to that endpoint set. Since `h_int/D>=rho-o(1)`,

```math
\boxed{
\liminf {\operatorname{area}(F^\dagger)\over D^2}
\ge {\rho+\sin\rho\over4}=0.3531742905\ldots,}
\tag{71.10}
```

```math
\boxed{
\liminf {r_o(F^\dagger)\over D}
\ge {1\over2}\sin(\rho/2)=0.1805944582\ldots.}
\tag{71.11}
```

If `m_cross=o(D)`, then `h_int=h_*-o(D)>=2rho D-o(D)` and the internal body upgrades
to the full constants (71.8)–(71.9).

---

## 71.5 Selected pinned right-nullity

Pin every selected loaded vertex. For one unloaded selected component `I_r`, let `M_r`
be its selected contact rigidity block on the `2n_r` unloaded coordinates and put

```math
\tau_r:=\dim\ker M_r,
\qquad
\dim\ker M_r^T=1+s_r.
```

Let

```math
\tau_*:=\sum_r\tau_r,
\qquad s_{C,*}:=\sum_rs_r.
```

Rank-nullity gives

```math
e_r+t_r=2n_r-\tau_r+1+s_r.
\tag{71.12}
```

The selected mixed support is a rigidity-matroid circuit, so its mixed rigidity matrix
has right-kernel dimension `3+sigma_*`. A pinned contact flex extended by zero on
`B_*` satisfies every selected mixed row. Since `F_*` is two-dimensional, no nonzero
Euclidean infinitesimal motion vanishes on all selected loaded vertices. Hence the
pinned-flex space injects into the non-Euclidean mixed-flex quotient and

```math
\boxed{0\le\tau_*\le\sigma_*.}
\tag{71.13}
```

---

## 71.6 Corrected pinned ledger and topology payment

Summing (71.12) and eliminating `e_*` through the circuit count gives

```math
\boxed{
c+e_{BB,*}+s_{C,*}
=q_*-2+d_*+\tau_*-\sigma_*,
\qquad d_*:=q_*-h_*.}
\tag{71.14}
```

For one unloaded component, the induced selected contact graph on the component plus
its loaded attachments is connected, planar, and triangle-free. If `a_r` is its
number of distinct loaded attachments, `c_r` its internal selected loaded-loaded
contacts, and `c_r^partial` those on the convex attachment hull, the outer walk has
length at least `2a_r-c_r^partial`. Euler yields

```math
s_r-\tau_r+c_r-{c_r^partial\over2}\le a_r-3,
```

so

```math
s_{C,*}-\tau_*\le a-3c.
\tag{71.15}
```

The simple bipartite planar incidence graph gives

```math
a\le q_*+2c-2
```

when `c>0`. Combining with (71.14)–(71.15) gives

```math
\boxed{e_{BB,*}\ge d_*-\sigma_*}
\tag{71.16}
```

in every two-dimensional extreme support; the `c=0` case follows directly from
(71.14).

---

## 71.7 Pinned flex cancels from harmonic-cell perimeter

Let `delta_r` be the graph diameter of the selected contact graph induced by `I_r` and
use the triangle-free penny-graph slack

```math
r_r:=2n_r-\delta_r-2-e_r\ge0.
```

Equation (71.12) gives

```math
t_r-\delta_r-3=s_r+r_r-\tau_r.
\tag{71.17}
```

Selected loaded contact degree is at most the canonical full loaded degree three, so

```math
s_{B,*}:=3q_*-e_{BI,*}-2e_{BB,*}\ge0.
```

Summing (71.17) and using (71.14) gives

```math
\sum_r\delta_r+\sum_rr_r+s_{B,*}
+3d_*+2\tau_*-3\sigma_*
=6+e_{BB,*}+2s_{C,*}.
\tag{71.18}
```

The convex hull `P_{r,*}` of one component's loaded attachments has diameter at most
`delta_r+2`, hence perimeter at most `pi(delta_r+2)`. Dropping the nonnegative
`r_r,s_{B,*}` in (71.18) and adding twice (71.14) eliminates `tau_*` and
`s_{C,*}` exactly:

```math
\boxed{
\sum_r\operatorname{per}(P_{r,*})
\le\pi(2+2q_*-e_{BB,*}-d_*+\sigma_*).}
\tag{71.19}
```

Thus `kappa_*=o(D)` implies only an `o(D)` correction to the full-support attachment
perimeter bound.

---

## 71.8 Canonical effect

A low-degeneracy extreme circuit has a geometric split:

```text
kappa_*=o(D)
  -> selected force hull already has the full area/inradius floors
  -> either >=(rho-o(1))D cross-block mixed loaded edges,
  -> or one attachment block contains >=(rho-o(1))D internal diameter edges
     and a centered body of area >=0.35317 D^2 and inradius >=0.18059 D.
  -> if cross-block edges are o(D), that block is almost spanning and inherits
     the full 0.61847... area / 0.33680... inradius constants.
  -> selected pinned flexes cannot open a linear harmonic-cell perimeter loophole.
```

Canonical Sections 68–69 now add global `E_4=O(D)`, an `O(D)` phase cut, and a forced
quadratic coherent physical grain whenever the full positive core is quadratic. The
next obligation is to connect that full-support grain/interface structure to the
selected extreme's cross-block family or thick distinguished attachment block.
