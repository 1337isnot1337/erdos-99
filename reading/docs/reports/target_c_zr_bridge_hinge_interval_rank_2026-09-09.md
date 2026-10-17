> Generated reading edition · [exact source](../../../docs/reports/target_c_zr_bridge_hinge_interval_rank_2026-09-09.md) · source SHA-256 `6dcc4137f0d11fb5887d7adfec707aa56c9bdef7ee48bf95189c841f89923289`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-334DC3FDC35C","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — ZHI: bridge-hinge interval rank and two-sided diameter blockers

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-bridge-hinge-interval`  
**Base:** stacked on PR #111 at `28ed905220197286268ce7c0a01fb29c4995d1cd`  
**Run type:** exact kinematic reduction / bridge-trunk diameter rank  
**Target:** Target C, post-ZF bridge branch  
**Depends on:** ZF mixed infinitesimal rigidity; physical contact bridges; C65 full diameter visibility for the positive-`beta` statements; ZHT only for the final quantitative corollary  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

The ZHT branch contains a consecutive chain of `H=Omega(D)` physical contact bridges.  Each contact bridge is an exact first-order rotational hinge: one may rotate the entire descendant contact component about the bridge endpoint while preserving every unit-contact length to first order.

For a consecutive bridge trunk these hinge motions form an `H`-dimensional contact-preserving space.  An active diameter row sees such a hinge only when its two endpoints lie on opposite sides of that bridge.  Along a nested trunk the bridges separating two fixed endpoints form one consecutive interval.  Hence the restriction of the full diameter rigidity matrix to the hinge space is an **interval-support matrix**.

ZF then forces this matrix to have rank at least `H-1` (and rank `H` when the root side contains two vertices).  Relative-interior KKT equilibrium supplies a strictly positive left dependence among its nonzero rows.  Consequently:

- at least `H` active diameter rows have nonzero action on the trunk (at least `H+1` in the anchored case);
- every non-Euclidean individual trunk hinge is blocked by diameter rows of **both first-order signs**;
- rows from diameter edges incident to a terminal in the root block have prefix support.

This gives a finite ordered-matrix model for the entire macroscopic bridge trunk.  It is independent of the later rhombic-bulk reduction and may be combined with C66 star concentration, C18 diameter geometry, or the ZSP diameter path.

---

## 1. Consecutive physical bridge trunk

Let `C` be the connected positive contact graph of the fully force-visible core.  Fix a consecutive path of physical contact bridges in its bridge-block tree,

```math
f_1,f_2,\ldots,f_H.
\tag{1.1}
```

Root the bridge-block tree on the side before `f_1`.  Write

```math
f_j=a_jb_j,
\tag{1.2}
```

where `a_j` is on the root side and `b_j` is on the descendant side.  Removing `f_j` from `C` gives a descendant vertex set `S_j` containing `b_j`.  Along the chosen trunk,

```math
S_1\supset S_2\supset\cdots\supset S_H.
\tag{1.3}
```

Let `R_0=V(C)\setminus S_1` be the root-side component of the first bridge.

No assumption on bridge stresses, response defect, or rhombic faces is needed in Sections 1--7.

---

## 2. One exact hinge velocity per bridge

Let `J` denote counterclockwise rotation by `pi/2`.  Define a velocity field `phi_j` on the contact-core vertices by

```math
\boxed{
\phi_j(v)=
\begin{cases}
J(p_v-p_{a_j}),&v\in S_j,\\
0,&v\notin S_j.
\end{cases}}
\tag{2.1}
```

Thus the whole descendant shore is infinitesimally rotated about the root-side bridge endpoint `a_j`, while the root shore is fixed.

### Lemma ZHI.1 — each `phi_j` preserves all contact lengths to first order

For every contact edge `xy in C`,

```math
(p_x-p_y)\cdot(\phi_j(x)-\phi_j(y))=0.
\tag{2.2}
```

#### Proof

If both endpoints lie outside `S_j`, both velocities are zero.  If both lie in `S_j`, then

```math
\phi_j(x)-\phi_j(y)=J(p_x-p_y),
```

which is perpendicular to the contact vector.

Because `f_j` is a bridge, it is the only contact edge with one endpoint on each shore.  On `f_j=a_jb_j`,

```math
\phi_j(a_j)=0,
\qquad
\phi_j(b_j)=J(p_{b_j}-p_{a_j}),
```

again perpendicular to the bridge vector.  This proves (2.2). `square`

Put

```math
W=\operatorname{span}\{\phi_1,\ldots,\phi_H\}.
\tag{2.3}
```

Then `W` lies in the kernel of the contact rigidity matrix.

---

## 3. The hinge motions are linearly independent

For a velocity field `u`, let

```math
\Delta_k(u):=u(b_k)-u(a_k)
\tag{3.1}
```

be its relative velocity across trunk bridge `f_k`.

Fix `j,k`.  If `j<k`, both endpoints of `f_k` lie in `S_j`, so

```math
\Delta_k(\phi_j)=J(p_{b_k}-p_{a_k}).
\tag{3.2}
```

The same identity holds for `j=k`.  If `j>k`, neither endpoint of `f_k` lies in `S_j`, so

```math
\Delta_k(\phi_j)=0.
\tag{3.3}
```

Therefore, for

```math
u=\sum_{j=1}^H\theta_j\phi_j,
```

we have the triangular identity

```math
\boxed{
\Delta_k(u)
=\left(\sum_{j=1}^k\theta_j\right)
J(p_{b_k}-p_{a_k}).}
\tag{ZHI1}
```

If `u=0`, every left side vanishes.  Since every bridge has unit length, the rotated bridge vector is nonzero.  Hence all prefix sums vanish:

```math
\sum_{j=1}^k\theta_j=0
\qquad(1\le k\le H).
```

Subtracting consecutive equations gives every `theta_j=0`.

### Theorem ZHI.2 — exact hinge dimension

```math
\boxed{\dim W=H.}
\tag{ZHI2}
```

This is an exact finite statement.  No genericity assumption is used.

---

## 4. Euclidean motions inside the hinge space

Every `phi_j` vanishes on `R_0`, hence every velocity in `W` vanishes on `R_0`.

A planar infinitesimal Euclidean motion has the form

```math
u(v)=t+\omega Jp_v.
\tag{4.1}
```

If such a motion vanishes at two distinct vertices, then subtracting the two zero equations gives `omega=0`, and then `t=0`.

Consequently:

### Lemma ZHI.3 — Euclidean intersection

```math
\boxed{
\dim(W\cap\mathcal E)\le1,
}
\tag{ZHI3}
```

where `mathcal E` is the three-dimensional space of planar Euclidean infinitesimal motions.

Moreover, if the root shore `R_0` contains at least two vertices, then

```math
\boxed{W\cap\mathcal E=\{0\}.}
\tag{ZHI4}
```

The only possible one-dimensional exception is the degenerate root-shore case `R_0={a_1}`, where a global infinitesimal rotation about `a_1` can lie in `W`.

---

## 5. Restrict the active diameter rows to the hinge space

Let `H_*` denote the full actual active diameter graph in the C65 normalization.  For a diameter edge

```math
h=xy\in H_*,
\qquad |p_x-p_y|=D,
```

define its first-order squared-length row on hinge coordinate `j` by

```math
G_{h j}
:=
2(p_x-p_y)\cdot\bigl(\phi_j(x)-\phi_j(y)\bigr).
\tag{5.1}
```

Let `G` be the resulting `|H_*| times H` matrix.

A vector `theta in R^H` represents the contact-preserving hinge velocity

```math
u_\theta=\sum_j\theta_j\phi_j.
```

Then

```math
G\theta=0
```

if and only if `u_theta` also preserves every active diameter length to first order.

ZF says the mixed contact/diameter framework is infinitesimally rigid.  Therefore every such velocity is Euclidean, and

```math
\ker G
\cong W\cap\mathcal E.
\tag{5.2}
```

Combining with ZHI3--ZHI4 gives:

### Theorem ZHI.4 — trunk hinge rank

```math
\boxed{
\operatorname{rank}G\ge H-1.}
\tag{ZHI5}
```

If `|R_0|>=2`, then

```math
\boxed{
\operatorname{rank}G=H.}
\tag{ZHI6}
```

Thus the active diameter system must kill essentially every independent physical-bridge hinge mode.

---

## 6. Every diameter row has consecutive-interval support

Fix one diameter edge `h=xy`.  If `x,y` lie on the same shore of bridge `f_j`, then `G_{hj}=0`.

- If both lie outside `S_j`, both hinge velocities vanish.
- If both lie inside `S_j`, their relative velocity is `J(p_x-p_y)`, perpendicular to the diameter vector.

Therefore

```math
G_{hj}\ne0
\quad\Longrightarrow\quad
|\{x,y\}\cap S_j|=1.
\tag{6.1}
```

For a fixed vertex `x`, membership in the nested sets `S_j` changes at most once as `j` increases.  Hence the symmetric difference of the two membership strings for `x` and `y` is one consecutive interval.

### Theorem ZHI.5 — interval-support normal form

For every active diameter edge `h`, there are indices

```math
0\le l_h<r_h\le H
```

such that

```math
\boxed{
G_{hj}=0
\qquad\text{whenever }j\notin\{l_h+1,\ldots,r_h\}.}
\tag{ZHI7}
```

Entries **inside** that interval may also vanish; no generic nonzero claim is made.

If one endpoint of `h` lies in the root block before `f_1`, then its separating set is a prefix.  In particular, for a diameter edge `zy` incident to a terminal `z` in the ZHT root block,

```math
\boxed{
\operatorname{supp}G_{zy,*}\subseteq\{1,\ldots,r_{zy}\}.}
\tag{ZHI8}
```

So the C66 stress-star rows form a weighted prefix family on the bridge-hinge coordinates.

This interval statement is purely topological: it uses only the nested bridge cuts.  It does not assume a rhombic disk or train coordinates.

---

## 7. Positive KKT dependence on the interval rows

Take the relative-interior normalized KKT stress, with

```math
\alpha_e>0\quad(e\in C),
\qquad
\beta_h>0\quad(h\in H_*).
\tag{7.1}
```

KKT equilibrium says the signed contact/diameter rigidity rows have a nonzero dependence.  Evaluate that dependence on any hinge velocity `phi_j`.  Every contact derivative is zero by ZHI.1, leaving

```math
\boxed{
\sum_{h\in H_*}\beta_h G_{hj}=0
\qquad(1\le j\le H).}
\tag{ZHI9}
```

Equivalently,

```math
\boxed{
\beta^{\mathsf T}G=0,
\qquad
\beta_h>0.}
\tag{ZHI10}
```

Delete the identically zero rows of `G` and let `m_{nz}` be the number remaining.  The same strictly positive coefficients give a nontrivial linear dependence among those rows.  Therefore

```math
m_{nz}\ge\operatorname{rank}G+1.
```

Using ZHI5--ZHI6:

### Corollary ZHI.6 — linearly many diameter rows act on the trunk

```math
\boxed{
m_{nz}\ge H.}
\tag{ZHI11}
```

If `|R_0|>=2`, then

```math
\boxed{m_{nz}\ge H+1.}
\tag{ZHI12}
```

Every counted diameter edge has a nonzero first-order moment on at least one physical bridge hinge, and therefore its bridge-tree path crosses the trunk on a nonempty interval.

This is stronger than merely saying that one diameter pair crosses the complete trunk: mixed rigidity requires a linear family of diameter constraints to act nontrivially on the hinge degrees of freedom.

---

## 8. Every non-Euclidean bridge hinge has blockers of both signs

Consider a single column `j`.  If `phi_j` is not Euclidean, mixed rigidity implies that some active diameter row has

```math
G_{hj}\ne0.
\tag{8.1}
```

Equation ZHI9 is a weighted sum with all `beta_h>0`.  A nonzero column cannot have all nonzero entries of the same sign.  Hence:

### Theorem ZHI.7 — two-sided rotational blockers

For every trunk bridge `f_j` whose descendant hinge `phi_j` is non-Euclidean, there exist active diameter edges `h_+,h_-` such that

```math
\boxed{
G_{h_+,j}>0,
\qquad
G_{h_-,j}<0.}
\tag{ZHI13}
```

Both diameter edges cross the physical bridge cut `f_j`.

For every `j>=2`, the root side of `f_j` contains the preceding bridge and hence at least two vertices, so `phi_j` is non-Euclidean.  Thus all trunk bridges except possibly the first singleton-root hinge have two-sided diameter blockers.

This sign statement is not contained in the body-bar rank count alone.  It says the actual positive KKT source must oppose each articulation rotation from both rotational directions.

---

## 9. ZHT quantitative corollary

In the PR #111 bridge-dominant near-zero branch, ZHT supplies one consecutive trunk with

```math
H\ge\frac{\eta^2}{16\pi}D.
\tag{9.1}
```

Therefore ZHI11 gives at least

```math
\boxed{
\frac{\eta^2}{16\pi}D
}
\tag{ZHI14}
```

active diameter rows with nonzero hinge action on that one trunk, up to integer rounding.

All but possibly the first trunk hinge have diameter blockers of both signs.  At the same time C66 places all but `o(1)` of the **beta mass**, but not necessarily all but `o(D)` of the support, on diameter rows incident to one star center `z`.  By ZHI8 those star rows are prefix-supported.

Thus the surviving near-zero bridge branch has the ordered finite normal form

```text
H = Omega_eta(D) physical hinge coordinates;
rank(G) >= H-1;
every row has consecutive-interval support;
C66-star rows have prefix support;
beta^T G = 0 with every beta_h>0;
all but possibly the first hinge column has both positive and negative blockers;
nonstar beta mass = o(1), but nonstar support may still be linear.
```

This is an exact interface between the bridge-trunk geometry and the earlier C83/C84 interval-matrix machinery developed for exact diameter chains, without assuming the trunk itself is a pure-rhombic chain.

---

## 10. What this does not prove

ZHI does **not** close the bridge branch by rank alone.

1. A diameter edge may cross several trunk cuts while some or all corresponding hinge coefficients vanish geometrically.
2. A linear number of nonstar diameter rows can have total `beta` mass `o(1)` and still supply rank.
3. Positive dependence plus interval support does not by itself force the C66 star-prefix rows to have full rank.
4. The first hinge may coincide with a global rotation when its root shore is a singleton.
5. No uniform lower bound on a nonzero hinge coefficient is claimed.

A finite interval matrix can therefore realize ZHI5--ZHI13 with arbitrarily small positive weights on the rows needed only for rank.  Any closing theorem must use the actual geometric coefficients, C18/C66 mass concentration, ZSP global-diameter geometry, or response/area information.

---

## 11. Next exact targets

The new finite problem has two concrete continuations.

### ZHI-A — star-prefix rank or quantitative nonstar necessity

Use the geometric formula for a star edge `h=zy`,

```math
G_{zy,j}
=2(p_y-p_z)\cdot J(p_y-p_{a_j})
=2(p_y-p_z)\cdot J(p_z-p_{a_j})
\tag{11.1}
```

whenever `f_j` separates `z,y`.  Combine the common C18 star cone and ZHT near-radial bridge pivots to bound the sign changes or effective rank of the star-prefix submatrix.  If its rank is deficient by `Omega(D)`, ZHI forces `Omega(D)` genuinely nonstar blocker rows.

### ZHI-B — interval positive-dependence rigidity

Exploit the fact that every non-Euclidean hinge column has both signs while every row has interval support.  A source-specific sign-order theorem could force a forbidden crossing pattern, a large nonstar beta mass, or a disconnected/zero-transfer interval structure already excluded by ZC.

These are smaller and more concrete than the full weak-transverse-rhombus exclusion.

---

## 12. Regression audit

### Long axial ladder with weak braces

Compatible with ZHI.  The weak brace rows can carry tiny positive `beta` while supplying the missing hinge rank.  This is the principal quantitative obstruction.

### Single bridge with singleton root

The unique hinge can be a global rotation and need no diameter blocker.  ZHI keeps the one-dimensional Euclidean exception explicitly.

### Multiple consecutive bridges

Every hinge after the first has a root side containing at least two vertices and is genuinely non-Euclidean, so the two-sided blocker theorem applies.

### Diameter row crossing a bridge but tangent to its hinge motion

Allowed.  ZHI states interval **support containment**, not that every separating bridge gives a nonzero coefficient.

### Rhombic exceptional faces

Irrelevant to ZHI.  The theorem applies before any train decomposition and incurs no `2f_exc` loss.

---

## 13. Classification

**Status:** proved report-level kinematic/rank theorem, conditional only on the stated ZF/C65 inputs.  
**Level I:** still open.  
**External literature:** none.  
**Computation:** none.

## 14. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

ZHI bridge-hinge interval theorem:
For a consecutive path f_1,...,f_H of physical contact bridges, orient each away from
a root.  Let S_j be its descendant shore and rotate S_j infinitesimally about the
root-side endpoint a_j:
    phi_j(v)=J(p_v-p_a_j) on S_j, 0 outside.
Each phi_j preserves every contact length.  Across trunk bridge f_k,
    Delta_k(sum theta_j phi_j)
      =(theta_1+...+theta_k) J f_k,
so the H hinge velocities are independent.

Restrict all active diameter rows to this H-dimensional hinge space, obtaining G.
ZF mixed rigidity gives
    rank G >= H-1,
and rank G=H if the first root shore has at least two vertices.
For one diameter edge h=xy, G_hj can be nonzero only when f_j separates x,y.
Along a nested trunk those separating bridges form one consecutive interval.  Thus
every row has interval support; a z-star row from the root block has prefix support.

Relative-interior KKT equilibrium gives the exact positive row dependence
    beta^T G=0, beta_h>0.
Hence at least H nonzero diameter rows act on the trunk (H+1 in the anchored case).
Every non-Euclidean hinge column contains both a positive and a negative diameter
coefficient; all trunk hinges j>=2 therefore have two-sided rotational blockers.

For ZHT, H>=eta^2 D/(16pi), so one macroscopic bridge trunk forces Omega_eta(D)
active diameter rows with nonzero hinge action, organized as an interval matrix.
The remaining issue is quantitative: rows of tiny total nonstar beta mass may still
supply rank.  Next target is to combine the explicit star coefficient formula with
C18/ZHT geometry to bound star-prefix rank/sign changes or force nonstar beta mass.
```
