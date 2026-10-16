<!-- theorem-state: {"artifact_id":"ART-079BD266D9C7","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — ZWT: quadratic weak rhombus closures force linearly many weak-rich trains

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-weak-transverse-train`  
**Base:** stacked on PR #111  
**Run type:** train-scale propagation of ZRI  
**Target:** Target C, bridge-dominant near-zero / ZCQ-ZRI branch  
**Depends on:** ZRI, stopped-train theorem DT, post-ZF exact train count  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

ZRI proves that the ZCQ branch contains `Omega_eta(D^2)` strict unit-rhombus faces and that, after choosing a scale `a_D->0`, all but `o(D^2)` of those faces have at least two nonradial boundary contacts with KKT stress below `a_D`.

The local statement automatically lifts to a macroscopic train statement. In every such rhombus, at least one complete opposite side pair is nonradial and weak, hence belongs to one train that is weak at that crossing. A stopped train has only `O(D)` rhombi, and the total number of stopped trains is only `O(D)`. Consequently the quadratic weak-face population forces **linearly many distinct trains, each weak at linearly many rhombi**.

This is the first train-scale consequence of the ZRP/ZRI mechanical degeneration that does not assume a pure simply connected rhombic disk.

---

## 1. Setup

Fix the bridge-dominant ZEG-A/ZCQ sequence for a fixed `eta>0`. ZCQ and C42 give a constant

\[
c_\eta>0
\]

such that the number `R=F_4` of bounded strict-rhombus faces satisfies

\[
\boxed{
R\ge(c_\eta-o(1))D^2.
}
\tag{1.1}

ZRI supplies a sequence

\[
a_D\downarrow0
\tag{1.2}
\]

and a good-rhombus family `mathcal R_good` with

\[
\boxed{
|\mathcal R_{good}|\ge(c_\eta-o(1))D^2
}
\tag{1.3}

such that every `F in mathcal R_good` has at least two boundary contacts `e` satisfying

\[
e\notin C_{rad},
\qquad
\alpha_e<a_D.
\tag{1.4}

ZRI also proves that no two radial sides can be adjacent on a strict rhombus.

Use the stopped-train construction DT: opposite sides of every strict rhombus are linked; the link components are train paths stopped at the outer face or bounded nonquadrilateral faces. Every contact edge belongs to exactly one stopped train.

Let `T` be the number of stopped trains.

---

## 2. Every good rhombus contains a complete weak train pair

Take `F in mathcal R_good`.

If exactly two sides of `F` are nonradial, ZRI says the two radial sides, if present, must be opposite. Hence the two nonradial sides are also opposite.

If at least three sides are nonradial, among any three sides of a four-cycle there is an opposite pair.

All nonradial sides of a good rhombus have stress below `a_D` by the choice of the ZRI exceptional face family. Therefore every good rhombus contains an opposite side pair

\[
e_F,e_F'
\]

with

\[
\boxed{
 e_F,e_F'\notin C_{rad},
\qquad
\alpha_{e_F},\alpha_{e_F'}<a_D.
}
\tag{ZWT1}

The pair `e_F,e_F'` is one train link. Choose one such pair for each good rhombus and assign `F` to that stopped train.

For a train `tau`, let

\[
A_\tau
:=
\#\{F\in\mathcal R_{good}:F\text{ was assigned to }\tau\}.
\tag{2.1}
\]

Then

\[
\boxed{
\sum_{\tau=1}^T A_\tau
=|\mathcal R_{good}|
\ge(c_\eta-o(1))D^2.
}
\tag{ZWT2}

---

## 3. Uniform O(D) length bound for every stopped train

Fix a stopped train `tau` and orient its unit contact-edge direction by a unit vector `u`. DT orients traversal through each rhombus so that consecutive contact-edge midpoints move in a direction making angle strictly less than `pi/6` with the fixed normal `Ju`.

If the train crosses `m_tau` rhombi, write its successive contact-edge midpoints as

\[
m_0,m_1,\ldots,m_{m_\tau}.
\]

Each midpoint step has length one and

\[
(m_{j+1}-m_j)\cdot Ju
>
\cos(\pi/6)
=
\frac{\sqrt3}{2}.
\tag{3.1}
\]

All contact-edge midpoints lie in the convex hull of the source, whose diameter is `D`. Hence the total difference of their projections onto `Ju` is at most `D`. Summing (3.1),

\[
m_\tau\frac{\sqrt3}{2}<D.
\]

Therefore every stopped train satisfies the exact strict bound

\[
\boxed{
 m_\tau<\frac{2}{\sqrt3}D.
}
\tag{ZWT3}

In particular

\[
A_\tau\le m_\tau<\frac{2}{\sqrt3}D.
\tag{3.2}
\]

This bound is valid with exceptional-face and outer-face train endpoints; no pure-disk train coordinates are used.

---

## 4. The number of stopped trains is O(D)

DT gives

\[
T
=\frac{b+Q}{2}+2f,
\tag{4.1}
\]

where `f` is the number of bounded nonquadrilateral faces and

\[
Q=\sum_{F\text{ non4}}(\deg F-4).
\]

The exact post-ZF closing-defect identity is

\[
\frac{b+Q}{2}=h-s_Z.
\tag{4.2}
\]

Thus

\[
T=h-s_Z+2f
\le h+2f.
\tag{4.3}
\]

The diameter graph satisfies `h<=q`, and the exact terminal partition gives `f<=q`. Therefore

\[
\boxed{
T\le3q\le3\pi D.
}
\tag{ZWT4}

This is intentionally crude but topology-correct.

---

## 5. Linearly many trains have linearly many weak crossings

Put

\[
\theta_\eta:=\frac{c_\eta}{12\pi}>0.
\tag{5.1}
\]

Call a train **weak-rich** if

\[
A_\tau\ge\theta_\eta D.
\tag{5.2}
\]

The total contribution of trains that are not weak-rich is at most

\[
T\theta_\eta D
\le
3\pi D\cdot\frac{c_\eta}{12\pi}D
=
\frac{c_\eta}{4}D^2.
\tag{5.3}
\]

Together with ZWT2, the weak-rich trains carry at least

\[
\left(\frac{3c_\eta}{4}-o(1)\right)D^2
\tag{5.4}
\]

assigned good rhombi.

Each train carries fewer than `(2/sqrt3)D` assignments by ZWT3. Hence the number `N_wr` of weak-rich trains satisfies

\[
N_{wr}\frac{2}{\sqrt3}D
\ge
\left(\frac{3c_\eta}{4}-o(1)\right)D^2.
\]

Therefore:

### Theorem ZWT.1 — linear weak-rich train family

\[
\boxed{
N_{wr}
\ge
\left(\frac{3\sqrt3}{8}c_\eta-o(1)\right)D.
}
\tag{ZWT5}

Every one of these trains is weak at at least

\[
\boxed{
A_\tau\ge\frac{c_\eta}{12\pi}D
}
\tag{ZWT6}

strict-rhombus crossings.

Thus the weak transverse degeneration cannot be confined to `o(D)` exceptional train tracks.

---

## 6. Each weak-rich train contains linearly many distinct weak contact edges

The contact edges of a stopped train are the vertices of a path graph, and its rhombi are the links between consecutive train edges.

A set of `k` selected links in a path is incident with at least `k+1` path vertices if the selected links are contiguous, and with even more vertices if they are separated. Therefore the `A_tau` assigned weak links on a weak-rich train touch at least

\[
A_\tau+1
\]

distinct contact edges of that train.

Every endpoint of an assigned link is nonradial and has stress below `a_D`. Hence every weak-rich train contains at least

\[
\boxed{
\frac{c_\eta}{12\pi}D+1
}
\tag{ZWT7}

**distinct** contacts `e` satisfying

\[
\boxed{
 e\notin C_{rad},
\qquad
\alpha_e<a_D.
}
\tag{ZWT8}

Different stopped trains have disjoint contact-edge sets. Consequently ZWT5-ZWT7 recover a quadratic population of weak contacts but with additional train localization:

\[
\boxed{
\Omega_\eta(D)\text{ disjoint trains each carry }\Omega_\eta(D)\text{ weak contacts.}
}
\tag{ZWT9}

---

## 7. Directed crossing-graph formulation

Let `Gamma` be the stopped-train crossing graph. Its vertices are trains and its edges are rhombi; DT proves it is simple and triangle-free.

For every good rhombus orient the corresponding edge of `Gamma` toward one train whose opposite side pair satisfies ZWT1. Leave the `o(D^2)` exceptional rhombi unoriented.

Then ZWT2 says the total oriented indegree is

\[
(c_\eta-o(1))D^2,
\]

while ZWT5-ZWT6 say that `Omega_eta(D)` train vertices have oriented indegree `Omega_eta(D)`.

This is the exact combinatorial object on which a train-propagation closing theorem must operate. The present theorem does **not** assert that the weak links form one contiguous segment of a train, nor that stress is constant along a train.

---

## 8. Binding regression and exact next target

A large finite patch of an oblique rhombic grid can have `Theta(D)` trains in each of two direction families and `Theta(D^2)` crossings. One direction family may carry mechanically weak opposite side pairs at every crossing. Therefore ZWT alone is compatible with the known local/grid regression.

What is now special to the actual survivor is the simultaneous presence of:

- the ZSP `D+o(D)` contact path between diameter endpoints;
- ZHA's `Omega(D)` distinct loaded extreme attachments distributed along that route;
- current-main PI/PC exposed-hull/outer-pocket constraints;
- ZWT's `Omega(D)` weak-rich trains, each geometrically spanning `Omega(D)` rhombi.

The shortest next theorem is therefore not another train-count bound. It is a **train endpoint/exposure theorem**:

> Show that `Omega(D)` weak-rich stopped trains in the ZSP/ZHA geometry must contribute too many distinct endpoints to the outer face / exceptional faces, or must force a macroscopic train-direction atom incompatible with the convex-hull and diameter-terminal distribution.

The stopped-train endpoint bookkeeping must retain exceptional faces explicitly; importing the pure-disk identity `B=2T` would be invalid.

---

## 9. Classification

**Status:** proved report-level train-scale consequence of ZRI.  
**Level I:** still open.  
**External literature:** none.  
**Computation:** none.  
**Novelty:** the mature train topology is imported; the new content is the ZRI weak-stress localization lifted to a linear-by-linear train family in the general stopped-train topology.
