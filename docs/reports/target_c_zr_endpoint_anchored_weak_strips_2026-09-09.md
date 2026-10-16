<!-- theorem-state: {"artifact_id":"ART-FFFDFA8AC9D1","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — ZEA: macroscopic weak strips are anchored at stopped-train endpoints

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-weak-transverse-train`  
**Base:** stacked on PR #111  
**Run type:** exact train endpoint geometry  
**Target:** Target C, ZCQ-ZRI-ZWT-ZWG branch  
**Depends on:** DT, ZRP, ZWT, ZWG  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

ZWG shows that on a stopped train the strongly-radial contacts occupy only boundedly many intervals and hence every weak-rich train has a macroscopic contiguous nonradial strip. The hyperbolic-cone geometry is stronger: one train can never meet both radial-cone signs.

Therefore, apart from at most one contact in the tiny central band about the C66 center `z`, the strongly-radial train contacts form at most one interval. The nonradial contacts consist of a prefix and a suffix, plus at most one central exceptional contact. Every ZWT weak-rich train consequently has a macroscopic nonradial prefix or suffix that reaches an actual stopped-train endpoint.

Thus the `Omega(D)` weak transverse strips in the near-zero branch are not arbitrary internal fault bands. A linear family of them is anchored on the actual outer/nonquadrilateral stopping system.

---

## 1. Midpoint coordinates and radial cones

Use ZWG notation. Fix one stopped train with contact-edge direction `u`. Write train-edge midpoints as

\[
m_j=(x_j,y_j)
\]

in the orthonormal basis `(u,Ju)`, after translating `z` to the origin and orienting the train so `y_j` increases.

DT gives

\[
 y_{j+1}-y_j>\frac{\sqrt3}{2},
\qquad
|x_{j+1}-x_j|<\frac12.
\]

Hence for every `i<j`,

\[
\boxed{
|x_j-x_i|
<\frac1{\sqrt3}(y_j-y_i).
}
\tag{ZEA1}

Let

\[
c_*:=\cos15^\circ,
\qquad
s_*:=\sin15^\circ.
\]

ZWG computes the exact strongly-radial locus for the unit contact centered at `(x,y)`:

\[
|x|>g(|y|),
\qquad
 g(t)=\frac{c_*}{2}\sqrt{1+\frac{4t^2}{s_*^2}}.
\tag{1.1}
\]

The two signs are the disjoint cones

\[
\mathcal C_+: x>g(|y|),
\qquad
\mathcal C_-: x<-g(|y|).
\]

Since

\[
g(t)
\ge
\frac{c_*}{s_*}t
=
\cot15^\circ\,t,
\tag{1.2}
\]

and

\[
\cot15^\circ>\frac1{\sqrt3},
\tag{1.3}
\]

the train slope is much smaller than either cone slope.

---

## 2. A stopped train cannot meet both radial-cone signs

Suppose for contradiction that train edges `i<j` satisfy

\[
x_i>g(|y_i|)
\]

and

\[
x_j<-g(|y_j|).
\]

Then

\[
|x_j-x_i|
>
 g(|y_i|)+g(|y_j|).
\tag{2.1}
\]

By (1.2),

\[
g(|y_i|)+g(|y_j|)
\ge
\cot15^\circ\,(|y_i|+|y_j|).
\tag{2.2}
\]

For arbitrary real `y_i<y_j`,

\[
|y_i|+|y_j|
\ge
 y_j-y_i.
\tag{2.3}
\]

Therefore

\[
|x_j-x_i|
>
\cot15^\circ\,(y_j-y_i)
>
\frac1{\sqrt3}(y_j-y_i),
\]

contradicting ZEA1.

The same proof with signs reversed excludes an edge in `C_-` followed by an edge in `C_+`.

Thus:

### Theorem ZEA.1 — one radial sign per train

\[
\boxed{
\text{A stopped train meets at most one of }\mathcal C_+,\mathcal C_-.
}
\tag{ZEA2}

---

## 3. Radial interval structure with the central band retained

ZWG proves that outside the absolute central band

\[
|y|\le t_0,
\qquad t_0<0.021,
\]

the relevant hyperbola boundary outruns the train slope. Since consecutive train midpoints differ in `y` by more than `sqrt3/2`, at most one train edge lies in this central band.

By ZEA2 only one radial sign can occur. On the negative-`y` side the corresponding cone excess is monotone in one direction; on the positive-`y` side it is monotone in the other. Consequently the strongly-radial index set is one interval, except that the possible single central train edge may split it into two adjacent intervals.

Therefore the nonradial train edges have the form

\[
\boxed{
\text{prefix}\ \cup\ \text{suffix}\ \cup\ \text{at most one central edge}.
}
\tag{ZEA3}

Both the prefix and suffix, when nonempty, reach actual endpoints of the stopped train.

---

## 4. Every weak-rich train has an endpoint-anchored macroscopic nonradial strip

Let `tau` be ZWT weak-rich. ZWT gives at least

\[
 k_\eta D,
\qquad
k_\eta:=\frac{c_\eta}{12\pi}+o(1),
\]

distinct nonradial contacts on `tau`.

By ZEA3, after removing the possible one central edge, these contacts lie in a prefix and a suffix. Hence one endpoint interval contains at least

\[
\frac{k_\eta D-1}{2}
\]

nonradial contacts.

Thus:

### Theorem ZEA.2 — endpoint-anchored weak strip

Every weak-rich train contains a contiguous nonradial prefix or suffix of length

\[
\boxed{
\left(\frac{c_\eta}{24\pi}-o(1)\right)D
}
\tag{ZEA4}

that reaches one endpoint of the stopped train.

This improves the safe factor `1/4` in ZWG to an asymptotic factor `1/2` and, more importantly, fixes one end of the strip on the stopping topology.

---

## 5. A linear family of distinct stopped incidences is forced

ZWT supplies

\[
N_{wr}
\ge
\left(\frac{3\sqrt3}{8}c_\eta-o(1)\right)D
\]

weak-rich trains.

Choose one endpoint-anchored macroscopic strip from each. Distinct stopped trains have disjoint contact-edge sets, so their endpoint contact edges are distinct.

A nontrivial stopped train endpoint is precisely a train contact edge whose other incident face is the outer face or a bounded nonquadrilateral face. Therefore the selected strips yield the same number of distinct outer/nonquadrilateral face-edge incidences.

Hence:

\[
\boxed{
E_{stop}
\ge
\left(\frac{3\sqrt3}{8}c_\eta-o(1)\right)D,
}
\tag{ZEA5}

where `E_stop` counts distinct defect-face incidences used by the selected weak strips.

C42 already bounds the complete outer/nonquadrilateral incidence population by `O(D)`, so ZEA5 is not itself a contradiction. Its content is localization: a fixed positive fraction of the available defect topology is consumed by endpoints of macroscopic weak strips.

---

## 6. Mechanical weakness on the anchored strips

Use the explicit ZLS scale

\[
a_D=\sqrt{D\varepsilon}\to0.
\]

The total number of nonradial contacts with `alpha_e>=a_D` is `o(D^2)`.

The selected endpoint-anchored strips are edge-disjoint and each has length `Omega_eta(D)`. Exactly as in ZWG, for every fixed `rho>0`, only `o(D)` selected strips can contain at least `rho D` mechanically visible contacts.

After a diagonal choice `rho_D->0`, all but `o(D)` selected strips satisfy

\[
\boxed{
\#\{e\text{ in anchored strip}:\alpha_e\ge a_D\}=o(D).
}
\tag{ZEA6}

Thus the branch contains a linear family of endpoint-anchored, macroscopic, asymptotically weak transverse strips.

---

## 7. Exact next split by stopping-face type

Every selected strip ends in one of two places.

### Outer-anchored strip

Its terminal train edge belongs to the outer boundary walk. The strip penetrates `Omega_eta(D)` rhombi into the force-visible core while remaining nonradial and mechanically weak on density `1-o(1)`.

### Exceptional-face-anchored strip

Its terminal train edge lies on a bounded nonquadrilateral face. The strip penetrates `Omega_eta(D)` rhombi away from that exceptional face.

The total bounded exceptional-face degree is

\[
\sum_{F\text{ non4}}\deg F
=Q+4f
=O(D),
\]

and the outer boundary walk has length `b=O(D)`. Thus linear many anchored strips fit the existing endpoint budget, but only at linear density. A closing theorem now has to exploit their **macroscopic penetration depth**, not endpoint cardinality alone.

---

## 8. Binding regression

A clipped oblique rhombic grid can have linearly many long transverse trains terminating on its outer boundary. Therefore even ZEA's outer-anchored strip family is not forbidden by local rhombic geometry.

What that regression lacks from the actual survivor is the simultaneous ZSP/ZHA structure:

- one `D+o(D)` diameter contact path;
- linear many loaded extreme attachments along the bridge trunk;
- almost all mechanical stress on a radial path forest;
- current-main PI/PC/HB outer-pocket and loaded-contact constraints.

The next theorem must couple anchored strip penetration with those global constraints.

---

## 9. Classification

**Status:** proved report-level endpoint localization theorem.  
**Level I:** still open.  
**External literature:** none.  
**Computation:** none.
