> Generated reading edition · [exact source](../../../docs/reports/target_c_zr_central_attachment_quadratic_core_2026-09-09.md) · source SHA-256 `8bf631ac03e0394aa39f2e5296aa2083dd93c53158563eca7f8241c7d31c1a9b`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 8 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-FB2A34334606","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — ZCQ: central trunk attachments force a quadratic force-visible core

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-deep-harmonic-capture`  
**Run type:** geometric population transfer from ZSP + ZHA  
**Target:** Target C bridge-dominant near-zero, ZEG Branch A  
**Depends on:** ZHT, ZHA, corrected ZSP  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

Corrected ZSP proves that in ZEG Branch A the captured harmonic cell contains an actual unit-contact path `P_D` from one diameter endpoint `z` to another `y` with

```math
|P_D|=D+o(D),
```

and that every path vertex in a fixed central axial portion has a uniform positive subdiameter margin from the entire source.

ZHA independently assigns one distinct loaded diameter terminal to every internal block of the `Omega(D)` ZHT bridge route. A loaded terminal cannot lie close to a central ZSP path vertex. Therefore every central route block must pay a contact path of length `Omega(D)` from the main near-geodesic route to its assigned loaded attachment. ZHA's assignment makes those branch/block regions pairwise disjoint.

There are `Omega(D)` central route blocks. Hence the force-visible contact core contains `Omega(D^2)` distinct vertices.

This removes the `v=o(D^2)` mechanical-core escape from the ZEG-A bridge branch.

---

## 1. Linear bridge trunk inside a D+o(D) diameter path

Let

```math
c_H:=\frac{\eta^2}{16\pi}>0.
\tag{1.1}
```

ZHT gives a consecutive bridge trunk of length

```math
H\ge c_HD.
\tag{1.2}
```

Every global bridge separating the chosen ZSP endpoints `z,y` occurs exactly once in every simple `z--y` contact path. Hence all `H` trunk bridge edges occur, in bridge-tree order, on the corrected ZSP path `P_D`.

Write

```math
N:=|P_D|=D+o(D).
\tag{1.3}
```

Choose

```math
\kappa:=\frac{c_H}{16}.
\tag{1.4}
```

At most `kappa D+O(1)` trunk bridges can occur among the first `kappa D` path edges, and at most that many among the last `kappa D` path edges. Therefore at least

```math
H-2\kappa D-o(D)
\ge
\left(c_H-\frac{c_H}{8}-o(1)\right)D
```

trunk bridges occur at central path indices.

After converting bridge positions to the intervening internal route blocks and discarding endpoints, there is a family `mathcal C_D` of internal route blocks with

```math
\boxed{
|\mathcal C_D|
\ge
\left(\frac34c_H-o(1)\right)D.
}
\tag{ZCQ1}
```

The constant `3/4` is deliberately weaker than the preceding `7/8` margin and absorbs all endpoint/index rounding.

For every `X_i in mathcal C_D`, choose a path vertex

```math
p_i\in P_D\cap X_i
\tag{1.5}
```

between its parent and child trunk bridges. Distinct route blocks give distinct `p_i`.

---

## 2. Central path vertices have a fixed subdiameter margin

Put coordinates

```math
z=(0,0),
\qquad
y=(D,0).
```

Corrected ZSP gives

```math
\max_{p\in P_D}\operatorname{dist}(p,[z,y])=o(D)
\tag{2.1}
```

and

```math
N-D=o(D).
```

It also gives the exact directional identity

```math
\sum_{e\in P_D}(1-u\cdot v_e)=o(D),
\qquad u=(1,0).
\tag{2.2}
```

Consequently a path vertex whose index is between `kappa D` and `N-kappa D` has axial coordinate

```math
\kappa D-o(D)
\le t\le
D-\kappa D+o(D).
\tag{2.3}
```

After reducing `kappa` by a factor two for large `D`, every chosen `p_i` has

```math
\frac\kappa2D\le t_i\le\left(1-\frac\kappa2\right)D
\tag{2.4}
```

and transverse coordinate `h_i=o(D)`.

Use the exact estimate from Theorem P: for every source point `w`,

```math
|p_i-w|^2
\le
D^2-t_i(D-t_i)+\sqrt3D|h_i|+h_i^2.
\tag{2.5}
```

The central axial condition gives

```math
t_i(D-t_i)
\ge
\frac\kappa2\left(1-\frac\kappa2\right)D^2.
```

The final two terms in (2.5) are `o(D^2)`. Thus there is a constant

```math
\sigma_\eta>0
\tag{2.6}
```

depending only on `eta` such that for all sufficiently large members,

```math
\boxed{
\max_{w\in A}|p_i-w|
\le(1-2\sigma_\eta)D
\qquad(X_i\in\mathcal C_D).
}
\tag{ZCQ2}
```

For example, any fixed `sigma_eta` smaller than

```math
\frac12\left[
1-\sqrt{1-rac14\kappa(1-\kappa/2)}
\right]
```

works eventually; no optimization is needed.

---

## 3. Every loaded terminal is far from a central route vertex

Every loaded terminal `b in B` is an endpoint of an actual diameter pair, so some source point `w_b` satisfies

```math
|b-w_b|=D.
\tag{3.1}
```

If

```math
|b-p_i|<\sigma_\eta D,
```

then ZCQ2 and triangle inequality would give

```math
|b-w|
\le|b-p_i|+|p_i-w|
<\sigma_\eta D+(1-2\sigma_\eta)D
<D
```

for every source point `w`, contradicting (3.1).

Therefore

```math
\boxed{
|b-p_i|\ge\sigma_\eta D
\qquad
\text{for every loaded }b\in B
\text{ and every }X_i\in\mathcal C_D.
}
\tag{ZCQ3}
```

Since every contact edge has Euclidean length one, every contact path from `p_i` to any loaded terminal has at least

```math
\boxed{\sigma_\eta D}
\tag{3.2}
```

edges.

---

## 4. Apply the exact ZHA attachment injection

For each internal route block `X_i`, ZHA constructs a distinct attachment terminal `t_i in A_*` as follows.

- If `X_i` is loaded, `t_i` is the first loaded terminal reached by a contact path inside `X_i` from the cell route.
- If `X_i` is reaction-free, an off-route bridge-tree component is chosen and `t_i` is the first loaded terminal reached in that component.

In both cases there is a contact path `R_i` from a nonloaded route vertex in `X_i` to `t_i` whose internal vertices are nonloaded and hence lie in the same harmonic component `I_*`.

Choose the ZHA starting route vertex to be connected inside `X_i` to `p_i`; absorbing the bounded/actual internal prefix only makes the complete route to `t_i` longer. By ZCQ3, every such route has length at least

```math
\sigma_\eta D.
\tag{4.1}
```

The crucial ZHA distinctness proof is stronger than terminal distinctness: for different internal route nodes, the assigned regions are disjoint.

- Loaded case paths lie in different bridge blocks.
- Reaction-free case paths lie in pairwise disjoint off-route bridge-tree components.
- An off-route component is disjoint from every other route block and every off-route component attached elsewhere.

Thus, after deleting at most the distinct starting route vertices, the internal vertices of the chosen `R_i` are pairwise disjoint over `i in mathcal C_D`.

Each path of length at least `sigma_eta D` contains at least `sigma_eta D-O(1)` distinct nonloaded vertices in its assigned region.

---

## 5. Quadratic core theorem

Summing the disjoint branch/block populations over ZCQ1 gives

```math
 v
\ge
|\mathcal C_D|\,[\sigma_\eta D-O(1)].
```

Hence:

### Theorem ZCQ.1 — quadratic force-visible core in ZEG-A

There is a constant `c_eta>0`, depending only on the fixed bridge-stress fraction `eta`, such that

```math
\boxed{
 v\ge(c_\eta-o(1))D^2.
}
\tag{ZCQ4}
```

One may take any constant strictly below

```math
\boxed{
 c_\eta^{raw}
:=
\frac34c_H\sigma_\eta
=
\frac{3\eta^2}{64\pi}\sigma_\eta>0.
}
\tag{5.1}
```

No attempt is made to optimize this small coefficient.

Thus the bridge-dominant near-zero branch with sublinear exceptional reset cannot have a subquadratic force-visible contact core.

---

## 6. Consequences for existing global reductions

### ZRF/ZRP low-stress brace population

ZRF proves

```math
|C_{bad}(z)|\ge v-\pi D-1.
```

Together with ZCQ4,

```math
\boxed{|C_{bad}(z)|=\Omega_\eta(D^2).}
\tag{ZCQ5}
```

while under `D epsilon->0` their total contact stress is `o(D^2)`. Therefore the ZEG-A branch necessarily contains quadratically many cycle-closing/radially inefficient contact rows with vanishing average stress.

### C42 strict-rhombic bulk

C42 gives an `v-O(D)` strict-rhombic bounded-face bulk in every C-II source. Hence ZCQ4 implies

```math
\boxed{F_4=\Omega_\eta(D^2).}
\tag{ZCQ6}
```

So the same branch simultaneously has a quadratic rhombic face population and a mechanical measure degenerating onto the radial path forest.

### Rattlers

ZCQ does not prove `n-v=o(D^2)`. A quadratic rattler population may coexist with the quadratic core. It does, however, eliminate the earlier alternative `v=o(D^2)` from the bridge-dominant ZEG-A phase.

---

## 7. Exact remaining obstruction

The sublinear-reset bridge branch is now forced to combine four strong structures:

```text
one D+o(D) contact path between diameter endpoints;
Omega(D) distinct loaded attachments, each forced far from central route positions;
a quadratic force-visible contact core v=Omega_eta(D^2);
a quadratic strict-rhombic face bulk,
while D^2-o(D^2) mechanical contact stress lies on the radial path forest and
Omega_eta(D^2) radially inefficient/cycle-closing rows carry only o(D^2) total stress.
```

The new closing target is a **rhombic-bulk / radial-force incompatibility theorem**: rule out a triangle-free globally diameter-minimal unit-contact core with quadratic strict-rhombic bulk whose normalized positive self-stress degenerates onto a radial path forest.

This is substantially more specific than the original C42 force-bulk gap.

---

## 8. Classification

**Status:** proved report-level consequence of ZSP/ZHA.  
**Level I:** still open.  
**External literature:** none.  
**Computation:** none.
