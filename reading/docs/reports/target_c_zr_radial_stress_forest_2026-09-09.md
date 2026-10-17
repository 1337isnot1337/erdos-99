> Generated reading edition · [exact source](../../../docs/reports/target_c_zr_radial_stress_forest_2026-09-09.md) · source SHA-256 `048e65395d69f558f3a5d14d9c42b83616b04e1e2f3bf812cef2baedad57b0d1`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-704B542316A1","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — ZRF: near-zero response forces almost all contact stress onto a radial forest

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-deep-harmonic-capture`  
**Run type:** closing-proof continuation / global radial geometry  
**Target:** Target C, Gate C-II / Level I  
**Depends on:** C68 and elementary unit-separation geometry  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

C68 proves that in the C66 near-star phase `D epsilon -> 0`, the weighted radial defect of the complete positive contact core about the star center `z` satisfies

$$
Q_z
:=
\sum_{ij\in C}\alpha_{ij}
\left[1-(r_i-r_j)^2\right]
=o(D^2),
\qquad
r_i=|p_i-z|.
$$

A priori this allows a high-stress contact edge to lie in a cycle whose remaining braces have tiny stress. The new observation is that all **radially efficient** contact edges, irrespective of their weights, form a forest. Every contact cycle therefore contains a quantitatively radially inefficient edge. C68 then shows that one can delete a set of total contact stress `o(D^2)` and destroy every contact cycle.

Hence `D^2-o(D^2)` of the normalized contact stress is carried by an actual forest.

This does not delete those low-stress cycle-closing contacts from the finite source; they remain strongly supported rows. It is a mechanical normal form, not a contact-minimality contradiction.

---

## 1. Radial progress along one unit contact

Fix any source point `z` and put

$$
r_x=|x-z|.
$$

For a unit contact `xy`, reverse triangle inequality gives

$$
|r_x-r_y|\le1.
\tag{1.1}
$$

Call the contact **radially efficient** when

$$
\boxed{|r_x-r_y|>\sqrt3/2.}
\tag{1.2}
$$

and **radially bad** otherwise.

For every bad edge,

$$
1-(r_x-r_y)^2
\ge1-3/4
=1/4.
\tag{1.3}
$$

---

## 2. Efficient contacts cannot contain a cycle

### Theorem ZRF.1 — radial-efficient forest theorem

For every unit-separated planar point set and every reference point `z` belonging to the set, the graph formed by unit contacts satisfying

$$
|r_x-r_y|>\sqrt3/2
$$

is a forest.

### Proof

Suppose there were a simple cycle consisting entirely of efficient contacts. Choose a cycle vertex `v` of maximal radius

$$
r=|v-z|.
$$

Let `u,w` be its two cycle neighbors. Then

$$
r_u,r_w\le r.
$$

Because both cycle edges are efficient,

$$
d_u:=r-r_u>\sqrt3/2,
\qquad
 d_w:=r-r_w>\sqrt3/2.
\tag{2.1}
$$

We have `r>0`; otherwise every cycle vertex would coincide with `z`.

Let `n` be the inward radial unit vector at `v`,

$$
n=\frac{z-v}{r}.
$$

For the unit edge `vu`, the inward radial projection is

$$
\begin{aligned}
n\cdot(u-v)
&=
\frac{r^2-v\cdot u}{r}\\
&=
\frac{r^2-r_u^2+1}{2r}\\
&=
 d_u+\frac{1-d_u^2}{2r}\\
&\ge d_u
>\sqrt3/2.
\end{aligned}
\tag{2.2}
$$

Thus the unit vector from `v` to `u` makes angle strictly less than `pi/6` with the inward radial direction. The same holds for `vw`.

Therefore

$$
\angle uvw? 
$$

more precisely, the angle between the two unit rays `vu` and `vw` is strictly less than

$$
\pi/6+\pi/6=\pi/3.
\tag{2.3}
$$

Since `|v-u|=|v-w|=1`, the chord between their endpoints satisfies

$$
|u-w|
=2\sin\frac{\angle uvw_v}{2}
<2\sin\frac\pi6
=1.
\tag{2.4}
$$

This contradicts unit separation of distinct source points `u,w`.

Hence no efficient contact cycle exists. QED.

The notation in (2.4) refers to the angle `angle uvw_v := angle(u-v,w-v)` at `v`.

---

## 3. Every contact cycle pays a fixed radial defect

Let

$$
C_{bad}(z)
:=
\{xy\in C:|r_x-r_y|\le\sqrt3/2\}.
\tag{3.1}
$$

ZRF.1 says

$$
\boxed{C\setminus C_{bad}(z)\text{ is a forest}.}
\tag{ZRF1}
$$

Equivalently, `C_bad(z)` is a feedback edge set: every cycle of the complete contact graph contains at least one bad edge.

This statement is unweighted and holds for any unit-separated point set.

---

## 4. C68 makes the cycle-hitting stress negligible

Now take `z` to be the C66 stress-star center in the lexicographically normalized C-II survivor. C68 gives

$$
Q_z
=
\sum_{xy\in C}\alpha_{xy}
[1-(r_x-r_y)^2].
\tag{4.1}
$$

Every bad edge contributes at least `alpha_e/4` by (1.3). Therefore

$$
\boxed{
\sum_{e\in C_{bad}(z)}\alpha_e
\le4Q_z.
}
\tag{ZRF2}
$$

C68 further gives

$$
Q_z\le C_0D^3\varepsilon.
\tag{4.2}
$$

Hence

$$
\boxed{
\sum_{e\in C_{bad}(z)}\alpha_e
\le4C_0D^3\varepsilon.
}
\tag{ZRF3}

If

\[
D\varepsilon\to0,
$$

then

$$
\boxed{
\sum_{e\in C_{bad}(z)}\alpha_e=o(D^2).
}
\tag{ZRF4}

Since the complete contact stress is normalized by

\[
\sum_{e\in C}\alpha_e=D^2,
$$

we obtain:

### Theorem ZRF.2 — asymptotic radial stress forest

Under `D epsilon->0`, there exists a contact forest

$$
F_z:=C\setminus C_{bad}(z)
$$

such that

$$
\boxed{
\sum_{e\in F_z}\alpha_e
=D^2-o(D^2).
}
\tag{ZRF5}

Thus asymptotically all mechanical contact stress is carried by a forest whose every edge changes distance from `z` by more than `sqrt(3)/2`.

---

## 5. Rigidity forces many low-stress cycle-closing contacts when the core is large

Let `v` be the number of nonisolated core vertices. Since `F_z` is a forest,

\[
|F_z|\le v-1.
\tag{5.1}
$$

Hence

$$
|C_{bad}(z)|
\ge e-v+1.
\tag{5.2}
$$

ZF gives

$$
e+h\ge2v-2,
$$

so

$$
\boxed{
|C_{bad}(z)|
\ge v-h-1
\ge v-q-1
\ge v-\pi D-1.
}
\tag{ZRF6}

Thus if the nonisolated core itself has quadratic cardinality `v=Omega(D^2)`, then it contains `Omega(D^2)` radially bad cycle-closing contacts, but by ZRF4 their **total** KKT stress is `o(D^2)`.

Their average stress is consequently `o(1)` whenever `v>=cD^2` for fixed `c>0`.

This is a source-wide version of the low-stress-brace phenomenon found locally in ZHN.

---

## 6. Interaction with the bridge trunk

Every ZWT trunk bridge has

\[
\alpha_e=\Theta(D)
$$

and ZBL/C68 makes all but `o(D)` trunk bridges satisfy radial progress arbitrarily close to one. Hence almost the entire macroscopic trunk belongs to the efficient forest `F_z`.

More generally, every macroscopic-stress corridor edge selected in ZHN belongs to `F_z` except for `o(D)` exceptions along the trunk population: a fixed radial defect on `Omega(D)` such edges would contribute `Omega(D^2)` to `Q_z`.

Thus the ZWT/ZHN force skeleton is a substructure of the global radial forest; the two reductions are consistent rather than independent.

---

## 7. Exact target implication and remaining obstruction

The near-zero response branch now has a global force decomposition:

```text
contact support C
    = radial-efficient forest F_z
      carrying D^2-o(D^2) stress
    + cycle-hitting set C_bad
      carrying o(D^2) stress.
```

ZF rigidity requires the bad set to contain at least `v-h-1` contacts. Therefore a large core must use a large population of mechanically low-weight cycle-closing braces.

This gives a sharp remaining dichotomy:

1. `v=Omega(D^2)`: quadratically many low-total-stress radially inefficient braces are required to rigidify a force skeleton that is asymptotically a forest;
2. `v=o(D^2)`: the full-source packing density must be carried mainly by contact-isolated/rattler population, to be handled by the current-main force-hull/source-capacity branch.

A closing theorem can attack either side. ZRF itself does not provide a lower bound on individual brace stress and therefore does not close Level I.

---

## 8. Regression audit

### Square ladder / axial truss

Binding and correctly represented. A high-force radial path can be closed into cycles by low-stress transverse braces. ZRF says exactly that the braces must belong to `C_bad`; it does not claim they disappear.

### Pure contact tree

Then `C_bad` may be empty and ZRF is vacuous, as expected.

### Radial out-and-back cycle

At a farthest cycle vertex the two inward unit edges cannot both make radial progress greater than `sqrt(3)/2`; the unit-separation angle condition forces the quantitative bad edge.

### Strong-support finite integration

Not invoked. Small total or normalized stress does not make a finite contact row weak in the maximal KKT support.

### Contact-isolated points

Untouched by the forest theorem; they enter the second branch of Section 7.

---

## 9. Dependencies

- elementary reverse-triangle and unit-neighbor angle geometry;
- C68 radial defect and its `Q_z<=C_0D^3 epsilon` estimate;
- ZF only for the counting consequence ZRF6;
- Hopf--Pannwitz / perimeter bound only for `h<=q<=pi D`.

No new external literature is imported.

---

## 10. Promotion recommendation

**Report-level theorem.** ZRF.1 is unconditional and could eventually be promoted as a geometric lemma; ZRF.2 and later consequences remain downstream of report-level ZR/ZF/C66/C68.

---

## 11. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Fix z and call a unit contact xy efficient if
    ||x-z|-|y-z|| > sqrt(3)/2.
The efficient contact graph is a forest: on any hypothetical efficient cycle, take a
maximum-radius vertex v. Both incident cycle edges would point within 30 degrees of the
inward radial direction, so their angle at v would be <60 degrees and their other
endpoints would be less than unit distance apart.

Thus every contact cycle contains a bad edge with radial defect
    1-(Delta r)^2 >= 1/4.
At the C66 center, C68 gives
    sum_bad alpha <=4Q_z<=4C_0D^3 epsilon.
Hence D epsilon->0 implies
    sum_bad alpha=o(D^2),
while the complementary efficient forest carries D^2-o(D^2) contact stress.

ZF then forces
    |C_bad| >= e-v+1 >= v-h-1 >= v-pi D-1.
So a quadratic core requires quadratically many cycle-closing contacts carrying only
o(D^2) total stress. If the core is subquadratic, the remaining full-source population
must instead live in the rattler/source-capacity branch.
```
