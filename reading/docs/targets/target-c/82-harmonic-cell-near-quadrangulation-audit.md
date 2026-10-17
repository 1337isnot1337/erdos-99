> Generated reading edition · [exact source](../../../../docs/targets/target-c/82-harmonic-cell-near-quadrangulation-audit.md) · source SHA-256 `40a76b34aae32c02204266d45353afc0fbfa6af4da277321bfcb10783a626c29`.
> [Current theorem state](../../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 1 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

# Target C — harmonic carrier near-quadrangulation audit

**Date:** 2026-09-12
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

Canonical Section 78 localizes one quadratic coherent rhombic subgrain inside one
unloaded harmonic component `I_*` and its convex attachment cell
`P_*=conv(A_*)`. This module strengthens that localization from a selected subgrain to
the **entire induced positive-contact graph of the carrier component**.

The result is exact before asymptotics. For any unloaded harmonic component, the
bounded-face defect of the induced graph is controlled solely by its loaded attachment
set. Applied to the Section-78 carrier, this gives

```math
F_{4,*}=n_*+O(D)=\Theta(D^2),
```

where `n_*=|I_*|` and `F_{4,*}` is the number of bounded quadrilateral faces in the
induced contact graph on `I_* union A_*`. Moreover the outer boundary plus all
nonquadrilateral-face boundary has total length `O(D)`. Repeating the Section-68/69
phase cut inside this one cell therefore decomposes essentially the whole carrier into
`epsilon`-coherent strict-rhombus grains with total physical perimeter
`O_epsilon(D)`.

Thus the quadratic harmonic carrier is itself a boundary-order perturbation of a
rhombic quadrangulation; the Section-78 quadratic grain is not hiding inside an
otherwise topologically diffuse component.

No contact-isolated source point is deleted or assigned positive KKT stress. The
statement concerns only the nonisolated positive-contact carrier from Section 78.

---

# 82. The macroscopic harmonic carrier is near-quadrangulated

## 82.1 Local notation and canonical attachment identities

Fix one unloaded positive-contact component `I_r`. Use the canonical Section-62
notation

- `n=|I_r|`;
- `A=A_r subset B`, `a=|A|`, and `P=conv(A)`;
- `e` for contacts internal to `I_r`;
- `t` for contacts from `I_r` to `A`;
- `s=e+t-2n-1>=0`;
- `c` for loaded-loaded contacts whose endpoints both lie in `A`;
- `c_partial` for those `c` contacts that are sides of `P`;
- `delta` for the graph diameter of `C[I_r]`;
- `r_pen=2n-delta-2-e>=0` for the triangle-free penny-graph slack.

Let `H` be the induced straight-line contact graph on `I_r union A`, including the
`c` loaded-loaded contacts. Canonical Section 62 proves that `H` is connected, planar,
and triangle-free, that every point of `I_r` lies in `P`, and that every member of `A`
is a vertex of `P`.

It also gives

```math
\boxed{e+t=2n+1+s,}
\tag{82.1}
```

```math
\boxed{t-delta-3=s+r_{pen},}
\tag{82.2}
```

and, if `L` is the outer-face walk length of `H`,

```math
\boxed{L\ge2a-c_{partial}.}
\tag{82.3}
```

Finally its local attachment-stress inequality is

```math
\boxed{s+c-{c_{partial}\over2}\le a-3.}
\tag{82.4}
```

All identities below are finite consequences of these canonical facts.

## 82.2 The local bounded contact faces are convex

The face count will be useful only if a bounded four-face is an actual strict unit
rhombus. We therefore first record the local convexity statement.

### Lemma 82.1 — local hull augmentation

Add every missing side of the convex polygon `P` between consecutive vertices of `A`
to `H`, retaining the edge only once if it is already a contact. Call the augmented
plane graph `Hhat`. Then

1. every vertex of `I_r` lies in the interior of `P`;
2. `Hhat` is 2-connected; and
3. every bounded face of `Hhat`, hence every old bounded face of `H`, is a convex
   polygon.

### Proof

First let `x in I_r`. If `x` lay on `partial P`, choose a supporting line through
`x`. Positive equilibrium at an unloaded vertex makes `x` a strictly positive
weighted average of all its contact neighbors. Since every neighbor lies in the same
closed supporting half-plane, equality in the supporting coordinate forces every
neighbor onto the supporting line. Unit contacts then allow at most one neighbor in
each line direction, so `deg_C(x)<=2`, contradicting the canonical unloaded degree
lower bound three. Thus `I_r subset int(P)`.

Next fix any vertex `x` of `H`. We claim every component of `H-x` contains an
attachment vertex different from `x`. Otherwise one component `S` contains only
unloaded vertices. Every contact neighbor of a vertex of `S` lies either in `S` or is
`x`: a loaded neighbor would belong to `A`, and another unloaded neighbor would lie in
the same component `I_r`. The positive-coordinate maximum principle with sole
boundary value `p_x` therefore forces every vertex of `S` to coincide with `x`,
contradicting distinct source points.

The added polygon sides form the hull cycle on `A`. If `x` is unloaded that entire
cycle survives; if `x in A`, deleting `x` leaves a path through all remaining
attachments. The attachment representative in every component of `H-x` is therefore
connected to every other one in `Hhat-x`. Hence `Hhat-x` is connected for every
vertex `x`, so `Hhat` is 2-connected.

Every face boundary of a 2-connected plane graph is a simple cycle. At an attachment
vertex, every bounded-face sector lies in the convex tangent cone of `P` and has angle
at most `pi`. At an unloaded vertex, a bounded-face angle greater than `pi` would put
all incident contact directions in the complementary cone of width strictly less than
`pi`; a strictly positive combination of those contact vectors could not vanish,
contradicting equilibrium. Thus every interior angle of every bounded face is at most
`pi`. A simple polygon with all interior angles at most `pi` is convex.

The added sides lie on `partial P`, so they split only the old outer face and do not
alter any old bounded face of `H`. `square`

### Corollary 82.2 — four-faces are strict unit rhombi

Every bounded degree-four face of `H` is a convex equilateral quadrilateral with unit
sides, hence a unit rhombus. Its short diagonal is strictly larger than one: equality
would make a unit equilateral triangle with two face sides, contrary to the
triangle-free source. Thus every bounded four-face is a strict unit rhombus of the
canonical type.

Every other bounded face has degree at least five.

## 82.3 Exact local face-defect identity

Let `F_b` be the number of bounded faces of `H`, and define

```math
Q:=\sum_{f\text{ bounded}}(deg f-4)\ge0.
\tag{82.5}
```

The vertex and edge counts are

```math
N=n+a,
\qquad
M=e+t+c=2n+1+s+c.
\tag{82.6}
```

Euler gives

```math
\boxed{F_b=M-N+1=n+2+s+c-a.}
\tag{82.7}
```

Counting face-edge incidences, with multiplicity on the outer walk,

```math
2M=L+4F_b+Q.
```

Substitution of (82.6)--(82.7) gives the exact identity

```math
\boxed{
L+Q=4a-6-2s-2c.
}
\tag{82.8}
```

This is the local quadrangulation-defect ledger.

Using (82.3),

```math
Q
\le2a-6-2s-2c+c_{partial}
\le2a-6-2s-c,
\tag{82.9}
```

because `c_partial<=c`.

Let `f_exc` be the number of bounded nonquadrilateral faces. Corollary 82.2 gives

```math
f_{exc}\le Q.
\tag{82.10}
```

If `F_4` denotes the number of bounded quadrilateral faces, then

```math
F_4=F_b-f_{exc}
\ge F_b-Q.
```

Using (82.7) and (82.9),

```math
\boxed{
F_4
\ge n+8+3s+2c-3a
\ge n-3a+8.
}
\tag{82.11}
```

There is also a matching coarse upper bound. From (82.4) and
`c_partial<=c`,

```math
s+{c\over2}\le a-3,
```

so

```math
s+c\le2a-6.
\tag{82.12}
```

Equation (82.7) therefore gives

```math
F_4\le F_b\le n+a-4.
\tag{82.13}
```

Combining (82.11) and (82.13),

```math
\boxed{
 n-3a+8
\le F_4
\le n+a-4.
}
\tag{82.14}
```

Thus the number of strict-rhombus faces differs from the unloaded population by at
most a linear function of the attachment count.

The physical boundary of the full local strict-rhombus complex is boundary-order in
the same currency. Every boundary occurrence has on its other side either the outer
face of `H` or one bounded nonquadrilateral face. Since

```math
\sum_{f\text{ nonquad}}deg f
=4f_{exc}+Q
\le5Q,
```

its total physical boundary `P_R` satisfies

```math
\boxed{
P_R\le L+5Q\le5(L+Q)\le20a.
}
\tag{82.15}
```

(The harmless additive constant from (82.8) is suppressed in the final coarse bound.)

## 82.4 Apply the exact ledger to the Section-78 carrier

Now take the canonical Section-78 carrier component `I_*`, attachment set `A_*`, cell
`P_*`, and quadratic coherent subgrain `G_* subset P_*`. Write

```math
n_*=|I_*|,
\qquad
a_*=|A_*|,
\qquad
d_*=diam(P_*).
```

Section 78 gives

```math
R(G_*)=\Omega(D^2),
\qquad
d_*=\Omega(D).
\tag{82.16}
```

### Lemma 82.3 — the carrier population is quadratic

```math
\boxed{n_*=\Omega(D^2).}
\tag{82.17}
```

### Proof

Take the plane graph consisting of all vertices and sides of the edge-connected
rhombi in `G_*`. It is connected, simple, and triangle-free. Every retained rhombus
remains a distinct bounded face of this subgraph because its interior was an original
contact face and contains no source vertex or contact edge.

For a connected simple triangle-free plane graph with `V>=3`, the number of bounded
faces is at most `V-3`. Hence

```math
|V(G_*)|\ge R(G_*)+3.
```

All vertices of `G_*` lie in `I_*` by Section 78, so

```math
n_*\ge |V(G_*)|\ge R(G_*)+3=\Omega(D^2).
```
`\square`

### Lemma 82.4 — the attachment set is linear

```math
\boxed{
a_*=\Theta(D),
\qquad
a_*\ge {d_*+1\over3}.}
\tag{82.18}
```

### Proof

Canonical harmonic trapping gives

```math
d_*\le\delta_*+2.
```

Equation (82.2) gives

```math
t_*\ge\delta_*+3\ge d_*+1.
```

Every loaded attachment vertex has total positive-contact degree at most three, so
`t_*<=3a_*`. Therefore `a_*>=(d_*+1)/3=Omega(D)`. The global loaded-hull bound gives
`a_*<=q<=pi D`, proving `a_*=Theta(D)`. `square`

Substitute (82.17)--(82.18) in the exact local face bounds. We obtain

```math
\boxed{
F_{4,*}=n_*+O(D)=\Theta(D^2),
}
\tag{82.19}
```

```math
\boxed{
L_*+Q_*=O(D),
\qquad
P_{R,*}=O(D).
}
\tag{82.20}
```

So the entire induced positive-contact graph of the macroscopic harmonic carrier has
only boundary-order outer/nonquadrilateral defect and has one strict-rhombus face per
unloaded vertex up to `O(D)` error.

This is stronger than the mere existence of the selected Section-78 subgrain.

## 82.5 The whole carrier admits a boundary-order coherent-grain decomposition

Let `mathcal R_*` be the set of all `F_{4,*}` strict-rhombus faces from (82.19). Their
total angular defect is a sub-sum of the canonical Section-68 global defect, hence

```math
\Delta_*:=\sum_{R\in\mathcal R_*}\delta_R=O(D).
\tag{82.21}
```

Fix

```math
0<\epsilon<\pi/6.
```

Repeat the Section-68/69 phase-cut construction on the finite rhombic complex
`mathcal R_*`. The proof uses only train directions and the defect sum (82.21): first
cut the reduced direction circle, then perform the `epsilon`-bin coarea cut. Therefore
only

```math
\boxed{|F_{epsilon,*}|=O_\epsilon(D)}
\tag{82.22}
```

rhombi are deleted, and every surviving physical grain is `epsilon`-coherent in one
three-phase frame.

Before this phase deletion, (82.15) gives physical boundary `O(D)`. Each deleted
rhombus creates at most four new boundary-edge occurrences. Hence the surviving
physical grains `G_1,...,G_s` satisfy

```math
\boxed{
\sum_jP_j=O_\epsilon(D).
}
\tag{82.23}
```

Their retained rhombus count is

```math
\boxed{
\sum_jR_j=F_{4,*}-O_\epsilon(D)
=n_*+O_\epsilon(D).
}
\tag{82.24}
```

Each grain has area at least `a_0R_j`. Isoperimetry therefore yields

```math
\boxed{
\sum_j\sqrt{R_j}=O_\epsilon(D).
}
\tag{82.25}
```

Consequently, for any fixed `eta>0`, the grains with

```math
R_j<\eta D^2
```

carry at most

```math
\boxed{
O_\epsilon(\sqrt\eta\,D^2)
}
\tag{82.26}
```

rhombi. In particular, after fixing `epsilon` and then taking `eta` small, a bounded
number of macroscopic coherent grains carry all but an arbitrarily small fraction of
the carrier's rhombic mass.

All these grains lie inside the same harmonic attachment cell `P_*`.

## 82.6 What this changes and what remains

The canonical quadratic-side chain has now been strengthened to

```text
no macroscopic inactive chamber
  -> force-hull rhombic saturation (Section 79)
  -> one quadratic coherent subgrain in one harmonic cell P_* (Section 78)
  -> the entire induced carrier H_* has
       n_*=Theta(D^2), a_*=Theta(D),
       F_4=n_*+O(D),
       outer + nonquadrilateral defect O(D)
  -> after any fixed phase cut,
       essentially all carrier rhombi lie in epsilon-coherent grains
       with total physical perimeter O_epsilon(D).
```

This removes another possible regression: the harmonic carrier cannot consist of one
selected quadratic rhombic island plus a comparably complicated sparse positive-core
remainder. At the face-count level, the whole carrier is quadrangulated up to
boundary order.

It still does **not** settle C-II. The remaining rhombic-side theorem must use this
near-quadrangulated one-cell geometry to obtain either

1. a coverage/aggregation inequality stronger than the Fox--Pach complete-biclique
   constant, sufficient to violate the local Section-76 diameter budget; or
2. a source-preserving deformation of the harmonic cell that strictly decreases the
   global source diameter.

The inactive-chamber branch remains separate and requires its own boundary/minimality
coupling theorem.

## 82.7 Dependency audit

- **Canonical Section 62 / `C-ATTACH-CURRENCY`:** local induced graph, harmonic
  trapping, (82.1)--(82.4), and loaded degree cap consequences.
- **Canonical Section 78 / `C-HARMONIC-GRID-LOCAL`:** the quadratic carrier component,
  cell `P_*`, subgrain `G_*`, and `d_*=Omega(D)`.
- **Canonical Sections 68--69:** angular-defect phase cut and coherent physical-grain
  construction; Section 82 reapplies the same finite argument to the local rhombic
  complex.
- **Triangle-free source:** local plane graph has no triangular contact face; bounded
  four-faces are strict unit rhombi.
- **Contact isolates:** untouched and not included in `n_*`.

**Status:** canonical as `C-HARMONIC-CARRIER-QUAD`; see `docs/state/theorem-state.yaml` for lifecycle authority. C-II remains open.
