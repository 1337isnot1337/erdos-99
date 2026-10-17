> Generated reading edition · [exact source](../../../docs/reports/target_c_radial_winner_take_all_branching_2026-08-31.md) · source SHA-256 `9b53b848daba56d73280e7b340ed5f7b8a8f063d196ca5821db762df776a010a`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-D09FF90D8659","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C79: radial winner-take-all branching

**Date:** 2026-08-31  
**Repository base:** `4cea9f9b` (main after the C77/C78 cross-route audit / PR #83)  
**Run type:** exact local geometric/stress reduction  
**Target:** Target C Gate C-II, C66-C76 near-chain phase  
**Depends on:** C68 radial defect, C74 local radial identity, unit separation  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

The post-C76 audit correctly moves the mature rhombic train-track machinery back to Target B/shared theory. C79 contributes new information on the other side of that bridge: a small-response KKT certificate cannot repeatedly split its macroscopic outward stress.

Fix the C66 center `z`. Put

```math
r_x:=|p_x-z|.
```

For a unit contact `vw`, orient it outward when `r_w>r_v` and define

```math
d_{vw}:=r_w-r_v\in(0,1],
\qquad
q_{vw}:=1-d_{vw}^2.
```

For every vertex with `r_v>=10`:

### Theorem C79 — at most one highly radial outgoing contact

There is at most one outward contact `vw` with

```math
\boxed{q_{vw}<\frac15.}
\tag{C79.1}
```

Call that edge the **primary radial edge** when it exists. Every other outward contact from such a vertex has `q>=1/5`.

If `E_sec` is the set of all nonprimary outward contacts whose inner endpoint has radius at least ten, then

```math
\boxed{
\sum_{e\in E_{sec}}\alpha_e\le5Q_z,
\qquad
\sum_{e\in E_{sec}}\alpha_e d_e\le5Q_z,
}
\tag{C79.2}
```

where C68's radial defect is

```math
Q_z=
\sum_{ij\in C}\alpha_{ij}
\left[1-(r_i-r_j)^2\right].
```

At the C66 center,

```math
Q_z\le D^2(1-S_z)\le C_0D^3\varepsilon,
\qquad
C_0=\frac{2\pi}{\kappa_0}.
\tag{C79.3}
```

Hence `D epsilon->0` implies

```math
\boxed{
\sum_{e\in E_{sec}}\alpha_e=o(D^2).
}
\tag{C79.4}
```

More sharply, fix `lambda>0`. Let `N_split(lambda)` be the number of vertices `v` with `r_v>=10` that have at least two outward contacts of stress at least `lambda D`. Then

```math
\boxed{
N_{split}(\lambda)
\le
\frac{5Q_z}{\lambda D}
\le
\frac5\lambda D(1-S_z).
}
\tag{C79.5}
```

At the C66 center,

```math
\boxed{
N_{split}(\lambda)
\le
\frac{5C_0}{\lambda}D^2\varepsilon
=o(D)
}
\tag{C79.6}
```

whenever `D epsilon->0`.

Thus the near-chain KKT certificate has only sublinearly many macroscopic forward splitting events over diameter scale.

---

## 1. Exact radial projection of one contact

Fix `v!=z` and put

```math
n_v:=\frac{p_v-p_z}{r_v}.
```

For an outward unit contact, write

```math
e:=p_w-p_v,
\qquad |e|=1,
\qquad d:=r_w-r_v>0,
\qquad q:=1-d^2.
```

The exact C74 identity is

```math
\boxed{
n_v\cdot e
=d-\frac{q}{2r_v}.
}
\tag{C79.7}
```

If `q<1/5`, then

```math
d>\sqrt{4/5}.
```

If `r_v>=10`, C79.7 gives

```math
 n_v\cdot e
>
\sqrt{4/5}-\frac1{100}
=0.884427\ldots
>
\frac{\sqrt3}{2}.
\tag{C79.8}
```

Therefore any such contact makes angle strictly less than `pi/6` with the outward radial direction `n_v`.

---

## 2. Unit separation gives winner-take-all branching

Suppose two distinct outward contacts `vw_1,vw_2` both satisfied `q<1/5`. By C79.8, both unit direction vectors lie in the strict `pi/6` cone around `n_v`. Their mutual angle is therefore strictly less than `pi/3`.

Both endpoints are source points at unit distance from `v`, so

```math
|p_{w_1}-p_{w_2}|
=2\sin\frac{\angle w_1vw_2}{2}
<1,
```

contradicting unit separation. This proves C79.1.

The constants are deliberately coarse. More generally, for radius threshold `R`, any `eta` satisfying

```math
\sqrt{1-\eta}-\frac{\eta}{2R}>\frac{\sqrt3}{2}
```

gives at most one outward edge with defect below `eta` from radii at least `R`.

---

## 3. Secondary outward stress is paid directly by Q_z

Every edge in `E_sec` has

```math
q_e\ge\frac15.
```

Since every contact has a unique inner endpoint unless the two radii agree, and equal-radius edges are not outward, each secondary edge is charged once. Therefore

```math
Q_z
=\sum_{ij\in C}\alpha_{ij}q_{ij}
\ge
\frac15\sum_{e\in E_{sec}}\alpha_e.
```

This proves the first part of C79.2. The second follows from `0<d_e<=1`.

C68 and C66 then give C79.3-C79.4.

---

## 4. Macroscopic splits are sublinear

At a `lambda D` split vertex, at most one of the two heavy outward contacts can be primary. Hence at least one heavy contact is secondary and contributes at least

```math
\frac15\lambda D
```

to `Q_z`.

Choose one such secondary heavy edge for every split vertex. Distinct split vertices give distinct chosen oriented edges because an outward edge has a unique inner endpoint. Thus

```math
N_{split}(\lambda)\frac{\lambda D}{5}
\le Q_z,
```

which proves C79.5. C66 gives C79.6.

---

## 5. High-stress radial forestization

Fix `lambda>0` and retain the outward contacts with

```math
\alpha_e\ge\lambda D,
\qquad r_{\rm inner}(e)\ge10.
```

Delete the secondary ones. C79.5 says only `o(D)` heavy edges are deleted in the `D epsilon->0` phase. Every remaining vertex has outdegree at most one. Radius strictly increases along every directed edge, so directed cycles are impossible.

### Corollary C79.1

After deleting `o(D)` heavy outward contacts, the `alpha>=lambda D` outward carrier outside radius ten is a directed acyclic graph of outdegree at most one.

It may merge, and it may interact with arbitrarily light transverse contacts. What is excluded is repeated macroscopic forward branching.

---

## 6. Cross-route effect after the PR #83 audit

The train-track audit shows that Target B/shared theory already supplies the mature weight-free train-angle machinery. The genuinely new combination is now:

```text
Target C stress side:
    C66/C76 -> approach to a straight-chain KKT face
    C71-C74 -> one depth-D outward transport carrier
    C79     -> only o(D) macroscopic forward splits

Target B / shared geometry side:
    macroscopic train-angle neutral/equality spaces
    sixfold phase coherence and grain decomposition
    pure-rhombic exposed-hull constraints
    C75 short-diagonal slack as an extra Target C capacity currency
```

C79 does not close the gap because one fixed normalized stress may put arbitrarily small positive weight on almost all transverse contacts. But it removes one possible reconciliation: the two-dimensional shell cannot be supported by a repeatedly branching macroscopic stress tree in the small-response phase.

The next useful theorem should therefore connect a Target B train-angle blocker to a **macroscopic forward branch/turn** in the C79 carrier, or exploit the KKT polytope to select a second stress with nonnegligible transverse mass.

## Compact handoff

For `r_v>=10`, an outward contact with

`q_e=1-(Delta r)^2<1/5`

has radial projection greater than `sqrt(3)/2`. Two such contacts at one vertex would be separated by less than 60 degrees and violate unit separation. Therefore there is at most one.

All secondary outward contacts satisfy `q_e>=1/5`, hence have total stress at most `5Q_z`. At the C66 center, `Q_z<=C_0D^3 epsilon`.

For each fixed `lambda>0`, the number of vertices with two outward contacts of stress at least `lambda D` is at most `5Q_z/(lambda D)=o(D)` when `D epsilon->0`.

**Status:** open. The near-chain certificate is now winner-take-all in its macroscopic forward transport.
