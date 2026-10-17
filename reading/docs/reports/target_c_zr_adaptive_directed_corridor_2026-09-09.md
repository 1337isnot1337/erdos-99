> Generated reading edition · [exact source](../../../docs/reports/target_c_zr_adaptive_directed_corridor_2026-09-09.md) · source SHA-256 `064c4ad72ef43fe264f78fd16f9c8bc093839f6c0141197ecd1f3b3a500bc676`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-379DE63D810B","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — ZDC: adaptive corridors are directed in one common star coordinate

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-deep-harmonic-capture`  
**Run type:** vector-flow sharpening of ZAC/ZHN  
**Target:** Target C bridge-dominant near-zero phase  
**Depends on:** ZHT, ZAC, ZHN cut equilibrium  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

ZAC gives, in all but `o(D)` blocks of the ZHT trunk, a port-to-port contact corridor whose selected edges have stress large relative to the near-zero defect and radial progress `1-o(1)`. The scalar max-flow construction does not control the sign of those geometric steps: an abstract selected path could oscillate in a transverse coordinate.

The mechanical cut equations contain a directed version of the same flow. Choose one fixed star direction `u_0` from the deepest ZHT cut. ZHT's force-coherence proof gives a uniform positive projection of every trunk force onto this direction. In an adaptive-regular block, side forces are `o(D)`. Therefore every port-separating cut carries `Omega(D)` **positive projected contact capacity** from the parent side to the child side.

Directed max-flow/min-cut then produces a port-to-port contact path all of whose geometric steps have positive `u_0` projection. Combining with ZAC/C68 gives, for all but `o(D)` trunk blocks, a path whose every selected edge is both `1-o(1)` radially efficient and strictly forward in one common global coordinate.

---

## 1. Common directed trunk axis

Use the ZHT notation. Let the complete consecutive trunk be

$$
f_1,\ldots,f_H,
\qquad H=\Omega_\eta(D),
\tag{1.1}
$$

oriented from the bridge block containing the C66 center `z` toward the deepest descendant cut.

ZHT chooses a star diameter edge `zy_0` crossing that deepest cut and puts

$$
u_0:=\frac{y_0-z}{D}.
\tag{1.2}
$$

C18 gives a common star-direction cone of width strictly below `pi/3`. The ZHT projection argument proves that for every trunk bridge, after orienting its geometric unit vector `t_j` from the root-side block to the descendant-side block,

$$
\boxed{
 u_0\cdot t_j\ge c_{dir}>0
}
\tag{1.3}

for all sufficiently large members, where `c_dir` depends only on fixed `eta` after absorbing the `o(1)` nonstar error. For definiteness one may take a smaller fixed constant than the eventual ZHT lower projection; its exact numerical optimization is irrelevant below.

Every trunk stress satisfies

\[
\alpha_{f_j}\ge c_BD,
\qquad c_B=\frac{\eta}{32\pi}.
\tag{1.4}

Thus the force exerted on an internal route block through its parent bridge has outward `u_0` projection at least

\[
 c_Bc_{dir}D.
\tag{1.5}

---

## 2. Adaptive-regular block and projected cut law

Take an internal trunk block `X` that is adaptive-regular in the sense of ZAC. Its side-force magnitude satisfies

\[
F_{side}(X)=o(D).
\tag{2.1}
$$

Let `p^-` be its parent trunk port and `p^+` its child trunk port.

For any vertex shore

$$
S\subset V(X),
\qquad p^-\in S,
\qquad p^+\notin S,
\tag{2.2}
$$

orient each internal contact edge crossing the cut from its endpoint `x in S` to its endpoint `y notin S`, and write

$$
d_{xy}:=y-x,
\qquad |d_{xy}|=1.
$$

Sum mechanical equilibrium over the vertices of `S`. Internal forces cancel except across the cut. With the contact-force sign convention, the parent trunk force is balanced by the outward contact transfers plus side forces. Project onto `u_0`. Using (1.5) and (2.1), for all sufficiently large members,

$$
\boxed{
\sum_{\substack{xy\in C(X)\\x\in S,y\notin S}}
\alpha_{xy}\,u_0\cdot d_{xy}
\ge
c_P D,
}
\tag{ZDC1}
$$

where one may take

$$
c_P:=\frac12c_Bc_{dir}>0.
\tag{2.3}
$$

The child trunk force does not occur because its port lies outside `S`; all other external forces are part of the side budget.

---

## 3. Directed projected-capacity network

Replace every undirected internal contact `xy` by the one directed arc pointing in the positive `u_0` direction. More explicitly, give the ordered arc `x->y` capacity

$$
\kappa(x,y)
:=
\alpha_{xy}\max\{u_0\cdot(y-x),0\}.
\tag{3.1}
$$

The reverse arc has the analogous capacity; exactly one direction is positive unless the contact is perpendicular to `u_0`, in which case both are zero.

For a cut `S` as in (2.2), the total directed capacity leaving `S` is

$$
\sum_{x\in S,y\notin S}
\alpha_{xy}\max\{u_0\cdot(y-x),0\}.
$$

This is at least the signed sum in ZDC1, because deleting negative terms can only increase the value. Therefore every directed `p^---p^+` cut has capacity at least

$$
c_PD.
\tag{3.2}
$$

Directed max-flow/min-cut gives a `p^---p^+` flow of value at least `c_PD`.

If the adaptive-regular block has at most `E_D` internal edges, delete directed flow cycles and decompose the remaining flow into simple directed paths. At most `E_D` path terms are required. Hence one directed simple path `P_X` carries at least

$$
\frac{c_P}{E_D}D.
\tag{3.3}
$$

Every edge `x->y` on that path obeys

$$
\boxed{
\alpha_{xy}\,u_0\cdot(y-x)
\ge
\widetilde\gamma_DD,
\qquad
\widetilde\gamma_D:=\frac{c_P}{E_D}>0.
}
\tag{ZDC2}

In particular

\[
\boxed{
u_0\cdot(y-x)>0}
\tag{ZDC3}
$$

and

$$
\boxed{
\alpha_{xy}\ge\widetilde\gamma_DD.
}
\tag{ZDC4}

The path is strictly monotone in the single global coordinate `u_0 dot p`.

Because `widetilde gamma_D` differs from ZAC's `gamma_D` only by a fixed `eta`-dependent factor,

\[
\boxed{
\frac{\delta_D}{\widetilde\gamma_D}\to0.
}
\tag{ZDC5}

---

## 4. C68 radializes the directed paths

Repeat the ZAC diagonal argument with `widetilde gamma_D`. Put

\[
\widetilde\zeta_D
:=
\sqrt{\frac{\delta_D}{\widetilde\gamma_D}}
\to0.
\tag{4.1}
$$

Every selected directed edge with radial defect

$$
1-(r_x-r_y)^2>\widetilde\zeta_D
$$

contributes at least

$$
\widetilde\gamma_DD\widetilde\zeta_D
$$

to C68's `Q_z`. Since

$$
Q_z\le C_0D^2\delta_D,
$$

the number of radially bad selected directed edges over the whole trunk population is

$$
O\!\left(
D\sqrt{\frac{\delta_D}{\widetilde\gamma_D}}
\right)
=o(D).
\tag{4.2}
$$

Consequently:

### Theorem ZDC.1 — directed adaptive corridor theorem

All but `o(D)` internal ZHT trunk blocks are either singleton blocks or have a port-to-port contact path

$$
p^-=x_0,x_1,\ldots,x_m=p^+
$$

such that for every selected step

\[
\boxed{
 u_0\cdot(x_{j+1}-x_j)>0,
}
\tag{ZDC6}

\[
\boxed{
\alpha_{x_jx_{j+1}}
\,u_0\cdot(x_{j+1}-x_j)
\ge
\widetilde\gamma_DD,
}
\tag{ZDC7}

and

\[
\boxed{
\bigl||x_{j+1}-z|-|x_j-z|\bigr|
=1-o(1)
}
\tag{ZDC8}

uniformly at the moving threshold supplied by (4.1).

Thus almost every route block admits a mechanically selected corridor that cannot backtrack in the common star coordinate.

---

## 5. Relation to the radial path forest

For large members, ZDC8 is stronger than ZRP's fixed `cos(15 degrees)` radial threshold. Hence every selected ZDC edge in all but `o(D)` blocks lies in the global strongly-radial path forest `C_rad`.

ZRP says every non-`z` vertex in `C_rad` has at most one inward and one outward neighbor. Therefore the ZDC path in a good block is a segment of one global radial path component.

The additional sign condition ZDC6 fixes its orientation in `u_0`: along the selected segment both radius (up to the ZRP inward/outward orientation) and the `u_0` coordinate cannot oscillate arbitrarily.

After also discarding the `o(D)` ZHT trunk bridges outside `C_rad`, consecutive ZDC-good blocks concatenate through their trunk bridges into simple strongly-radial path segments that are strictly forward in `u_0`.

---

## 6. New remaining obstruction

ZDC removes a loophole left by ZAC: the selected high-force radial corridors cannot zig-zag backward in the global star coordinate inside regular blocks.

The surviving obstruction is now entirely in `o(D)` exceptional blocks. Those blocks may still consume `Theta(D)` of the global C39 graph-diameter budget and thereby reset the route geometry between long directed radial segments.

A precise next target is:

> **Exceptional-block reset exclusion.** The `o(D)` exceptional ZHT trunk blocks cannot account for a macroscopic total loss of `u_0` displacement or a macroscopic angular reset while the complete source remains globally diameter-minimal and all trunk bridge forces are `Omega(D)`.

If their total reset is `o(D)`, the concatenated ZDC corridors form an almost-geodesic directed contact route of length `Theta(D)` between the ZHT diameter endpoint regions, bringing the sharp narrow-path theorem within reach.

---

## 7. Regression checks

- A bounded axial truss with weak braces is allowed; ZDC chooses its forward high-force corridor and ignores the weak braces.
- A selected path cannot contain a contact perpendicular or backward to `u_0`, because its directed projected capacity would be zero.
- `widetilde gamma_D` may tend to zero; only `delta_D/widetilde gamma_D->0` is needed.
- A small number of very large blocks can still carry all macroscopic detour; ZDC does not hide this.

---

## 8. Classification

**Status:** proved report-level refinement of ZAC/ZHN.  
**Level I:** still open.  
**External literature:** none.  
**Computation:** none.
