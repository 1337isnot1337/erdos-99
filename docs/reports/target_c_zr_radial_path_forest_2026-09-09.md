<!-- theorem-state: {"artifact_id":"ART-1D4D28B939FC","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — ZRP: near-zero response forces almost all contact stress onto a radial path forest

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-deep-harmonic-capture`  
**Run type:** exact radial geometry / C68 sharpening  
**Target:** Target C, Gate C-II / Level I  
**Depends on:** ZRF and C68  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

ZRF shows that contacts whose radial progress exceeds `sqrt(3)/2` form a forest. A slightly stronger fixed threshold forces maximum degree two away from the reference center. Consequently the mechanically dominant contact support in the near-zero response phase is asymptotically a **path forest**, not an arbitrary tree.

Choose

\[
\boxed{c_*:=\cos(\pi/12)=\cos15^\circ.}
\tag{1}
\]

Call a unit contact `uv` **strongly radial** about `z` if

\[
\boxed{
\bigl||u-z|-|v-z|\bigr|>c_*.
}
\tag{2}

Then every vertex other than `z` has strongly-radial degree at most two: at most one neighbor of smaller radius and at most one of larger radius. ZRF eliminates cycles. Hence every component avoiding `z` is a path, while the component containing `z` is a union of at most `deg_C(z)` outward paths meeting only at `z`.

In fully force-visible C-II, `deg_C(z)<=3`, so the centered component has at most three rays.

C68 gives that the complementary contacts carry only `o(D^2)` stress when `D epsilon->0`.

---

## 1. One smaller-radius strongly-radial neighbor at most

Fix a source vertex `v!=z` and put

\[
r=|v-z|.
\]

Unit separation gives

\[
r\ge1.
\tag{1.1}
\]

Let `u` be a unit-contact neighbor with smaller radius and write

\[
d=r-|u-z|>c_*.
\]

Let `n_in=(z-v)/r` be the inward radial unit vector. As in ZRF,

\[
n_{in}\cdot(u-v)
=d+\frac{1-d^2}{2r}
\ge d
>c_*
>\frac{\sqrt3}{2}.
\tag{1.2}
\]

Thus every strongly-radial edge from `v` to a smaller-radius neighbor lies within strictly less than `pi/6` of the same inward radial ray.

Two such unit edges would meet at angle less than `pi/3`, forcing their other endpoints to have mutual distance less than one. Therefore

\[
\boxed{
\text{at most one strongly-radial neighbor of }v\text{ has smaller radius.}
}
\tag{ZRP1}

---

## 2. One larger-radius strongly-radial neighbor at most

Now let `u` be a unit-contact neighbor with larger radius and put

\[
d=|u-z|-r>c_*.
\]

Let `n_out=(v-z)/r` be the outward radial unit vector. The outward projection is

\[
\begin{aligned}
n_{out}\cdot(u-v)
&=
\frac{|u-z|^2-r^2-1}{2r}\\
&=
 d-\frac{1-d^2}{2r}.
\end{aligned}
\tag{2.1}
\]

For `r>=1` and `d>c_*`, the right side is strictly larger than

\[
c_*-\frac{1-c_*^2}{2}.
\tag{2.2}
\]

Numerically this is

\[
0.93243\ldots
>
0.86602\ldots
=\frac{\sqrt3}{2}.
\tag{2.3}
\]

For an exact verification,

\[
c_*-\frac{1-c_*^2}{2}>\frac{\sqrt3}{2}
\]

follows directly after substituting `c_*=cos(pi/12)`.

Therefore every strongly-radial edge from `v` to a larger-radius neighbor lies within less than `pi/6` of the outward radial ray. Two such edges again violate unit separation of their other endpoints.

Hence

\[
\boxed{
\text{at most one strongly-radial neighbor of }v\text{ has larger radius.}
}
\tag{ZRP2}

Combining ZRP1 and ZRP2,

\[
\boxed{
\deg_{C_{rad}}(v)\le2
\qquad(v\ne z),
}
\tag{ZRP3}

where `C_rad` is the strongly-radial contact graph.

---

## 3. The strongly-radial graph is a path forest

Because

\[
c_*>\sqrt3/2,
\]

every strongly-radial edge is efficient in the sense of ZRF. ZRF.1 therefore says `C_rad` has no cycle.

Together with ZRP3:

### Theorem ZRP.1 — radial path-forest theorem

Every connected component of `C_rad` not containing `z` is a simple path or an isolated vertex.

The component containing `z` is a union of simple paths whose only common vertex is `z`. In fully force-visible C-II,

\[
\boxed{\deg_C(z)\le3,}
\]

so at most three strongly-radial rays meet at `z`.

No KKT hypothesis is needed for the graph-theoretic part except the final degree-three statement at `z`.

---

## 4. Almost all contact stress lies on this path forest

For every contact outside `C_rad`,

\[
|r_u-r_v|\le c_*.
\]

Its C68 radial defect is at least

\[
1-c_*^2
=\sin^2(\pi/12)
=:\sigma_* >0.
\tag{4.1}
\]

Therefore

\[
Q_z
\ge
\sigma_*
\sum_{e\notin C_{rad}}\alpha_e.
\]

Hence

\[
\boxed{
\sum_{e\notin C_{rad}}\alpha_e
\le
\frac{Q_z}{\sigma_*}.
}
\tag{ZRP4}

C68 gives `Q_z<=C_0D^3 epsilon`. Thus under

\[
D\varepsilon\to0,
\]

\[
\boxed{
\sum_{e\notin C_{rad}}\alpha_e=o(D^2).
}
\tag{ZRP5}

Since total contact stress is `D^2`,

\[
\boxed{
\sum_{e\in C_{rad}}\alpha_e=D^2-o(D^2).
}
\tag{ZRP6}

So asymptotically all contact stress is carried by a disjoint collection of radial paths, with at most three such paths meeting at the C66 center.

---

## 5. Counting consequence

Since `C_rad` is a forest,

\[
|C_rad|\le v-1.
\]

Exactly as in ZRF,

\[
|C\setminus C_{rad}|
\ge e-v+1
\ge v-h-1.
\tag{5.1}
\]

The stronger content of ZRP is geometric rather than cardinal: the high-stress support has no branching away from `z`.

If `v=Omega(D^2)`, the mixed framework is therefore rigidified by `Omega(D^2)` contacts outside the path forest whose total stress is `o(D^2)`.

---

## 6. Interaction with the ZWT trunk

Every ZWT trunk bridge has `alpha_e=Theta(D)` and, by C68/ZBL, all but `o(D)` trunk bridges have radial progress tending to one. Therefore all but `o(D)` trunk bridges lie in `C_rad`.

Because `C_rad` has degree at most two away from `z`, the strongly-radial trunk bridges cannot participate in a high-stress branching contact skeleton inside the captured harmonic cell. Any geometrically transverse branch or cycle closure must use contacts from the `o(D^2)`-stress complement.

This globalizes the ZHN local axial-degeneration picture.

---

## 7. Exact remaining obstruction

The near-zero response phase now has the source-wide mechanical normal form

```text
D^2-o(D^2) contact stress:
    carried by a path forest strongly radial about z;
    at most three high-stress rays can meet at z;
    no high-stress branching occurs elsewhere.

o(D^2) contact stress:
    carries every cycle closure and every transverse branch needed to make the
    complete mixed framework rigid and the force hull two-dimensional.
```

This is substantially narrower than an arbitrary anisotropic truss. The remaining question is whether a global diameter minimizer can have a two-dimensional, universally rigid active support whose mechanical measure degenerates to this radial path forest while the low-stress complement retains all transverse geometry.

A closing theorem may use:

- ZK universal/redundant rigidity;
- current-main force-hull area `>=0.5 sin(1) D^2`;
- ZRF/ZRP's path-forest stress degeneration;
- the external-rattler versus force-area split.

ZRP alone does not provide a positive stress floor on transverse contacts.

---

## 8. Regression audit

### High-force path with weak square braces

Still possible locally. The horizontal high-stress edges form paths; vertical/cycle-closing braces lie outside `C_rad` and may have small stress.

### Branching radial tree away from z

Excluded above the fixed `cos15` radial-progress threshold.

### Branching at z

Allowed, with at most three contact rays in C-II.

### Strong-support finite integration

Not used; low normalized stress does not make a finite contact row weak.

---

## 9. Dependencies

- ZRF cycle lemma;
- elementary unit-edge radial projection calculations;
- C35 for `deg_C(z)<=3`;
- C68 for the stress concentration.

No new external literature is imported.

---

## 10. Promotion recommendation

The path-forest geometry ZRP1--ZRP3 is unconditional and reusable. The stress concentration ZRP4--ZRP6 remains report-level downstream of the current ZR/ZF/C66/C68 chain.

---

## 11. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Let c_*=cos(15 degrees). Call a contact strongly radial if
    ||u-z|-|v-z|| > c_*.
For v!=z, r=|v-z|>=1.
- any strongly-radial edge to smaller radius has inward projection >sqrt(3)/2;
- any strongly-radial edge to larger radius has outward projection
      > c_*-(1-c_*^2)/2 > sqrt(3)/2.
Two neighbors on either side would make angle <60 degrees and violate unit separation.
Thus every v!=z has at most one inward and one outward strongly-radial neighbor.
ZRF already excludes cycles, so the strongly-radial support is a disjoint union of
paths; only z may branch, into at most three rays in C-II.

Every other contact has radial defect >=sin^2(15 degrees). C68 therefore gives
    sum_nonradial alpha <= Q_z/sin^2(15 degrees)=o(D^2)
when D epsilon->0.
Hence D^2-o(D^2) of all contact stress lies on a radial path forest.

The remaining rigidity/2D geometry is carried entirely by an o(D^2)-stress complement.
```
