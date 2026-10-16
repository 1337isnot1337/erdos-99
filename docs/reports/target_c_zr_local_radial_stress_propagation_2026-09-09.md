<!-- theorem-state: {"artifact_id":"ART-A2834ADD97C9","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — ZLS: regular rhombic vertices propagate radial stress almost straight

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-weak-transverse-train`  
**Base:** stacked on PR #111  
**Run type:** local KKT propagation inside the ZRI quadratic rhombic bulk  
**Target:** Target C, bridge-dominant near-zero / ZCQ-ZRI branch  
**Depends on:** C42/C51, ZRP/C68, ZCQ, ZRI  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

ZRI says almost every strict rhombus has at least two weak nonradial sides. This report converts that face statement into a vertexwise KKT normal form.

Outside `o(D^2)` vertices, the force-visible core is an unloaded degree-four vertex surrounded entirely by strict rhombi, and every incident nonradial contact has KKT stress below an explicit scale tending to zero. At such a vertex:

- zero or one radial contact implies **all** incident stress is tiny;
- two radial contacts must nearly cancel: their stresses differ by at most twice the weak scale, and whenever their stresses dominate that scale their directions are nearly exactly opposite.

Consequently a radial contact carrying macroscopic or moving-scale stress can traverse a long run of regular vertices only as an almost-straight, almost-constant-stress strand. The two-dimensional bulk can redirect such a load only through the exceptional vertex set.

---

## 1. Quantitative weak scale from C68

Put

\[
\delta_D:=D\varepsilon\to0.
\tag{1.1}
\]

ZRP uses

\[
c_*:=\cos15^\circ,
\qquad
\sigma_*:=1-c_*^2=\sin^2 15^\circ>0.
\]

For the nonradial contact set

\[
E_{nr}:=C\setminus C_{rad},
\]

ZRP gives

\[
\sum_{e\in E_{nr}}\alpha_e
\le
\frac{Q_z}{\sigma_*}.
\tag{1.2}
\]

C68 gives

\[
Q_z\le C_0D^3\varepsilon
=C_0D^2\delta_D.
\tag{1.3}
\]

Hence

\[
\boxed{
\sum_{e\in E_{nr}}\alpha_e
\le C_1D^2\delta_D,
\qquad C_1:=C_0/\sigma_*.
}
\tag{ZLS1}

Choose the explicit weak threshold

\[
\boxed{
a_D:=\sqrt{\delta_D}.}
\tag{1.4}
\]

Then `a_D->0`, and the number of nonradial contacts with

\[
\alpha_e\ge a_D
\]

is at most

\[
C_1D^2\frac{\delta_D}{a_D}
=C_1D^2\sqrt{\delta_D}
=o(D^2).
\tag{1.5}
\]

Thus the ZRI good-face scale can be fixed explicitly as `a_D=sqrt(delta_D)` after enlarging the exceptional face family by only `o(D^2)` faces.

---

## 2. All but O(D) deep vertices have degree four

Let `V_def` be the set of contact-core vertices incident with the outer face or with a bounded nonquadrilateral face.

C42 bounds the total outer/nonquadrilateral face-edge incidence by `O(D)`; every vertex of `V_def` is incident with at least one such face-edge incidence. Therefore

\[
\boxed{|V_{def}|=O(D).}
\tag{2.1}
\]

Take `v notin V_def`. It is an interior plane vertex and every incident face is a strict rhombus. Every rhombus angle lies strictly in

\[
(\pi/3,2\pi/3).
\]

The angles around `v` sum to `2pi`. Therefore `deg_C(v)<=3` is impossible. Triangle-free unit separation gives `deg_C(v)<=5`. Hence

\[
\deg_C(v)\in\{4,5\}.
\tag{2.2}
\]

The exact planar curvature identity is

\[
\sum_{v\in V(C)}(4-\deg_C v)
=4+b+Q.
\tag{2.3}
\]

Indeed `e=2v-2-(b+Q)/2` and the left side is `4v-2e`.

Let `N_5` be the number of degree-five vertices outside `V_def`. Their contribution to (2.3) is `-N_5`; every vertex in `V_def` has degree at least one, hence contribution at most three. Therefore

\[
4+b+Q
\le
-N_5+3|V_{def}|,
\]

so

\[
\boxed{N_5=O(D).}
\tag{ZLS2}

Consequently all but `O(D)` contact-core vertices are interior degree-four vertices surrounded entirely by strict rhombi.

Every loaded terminal is extreme and lies on the outer face, so these deep degree-four vertices are unloaded.

---

## 3. Regular vertices

Call a core vertex **regular** when

1. it is outside `V_def`;
2. it has degree four;
3. none of its incident rhombi belongs to the `o(D^2)` ZRI exceptional face family at threshold `a_D`.

By ZCQ, `v=Omega_eta(D^2)`. Sections 1-2 show

\[
\boxed{
\#\{\text{nonregular core vertices}\}=o(D^2).
}
\tag{ZLS3}

At a regular vertex every nonradial incident contact satisfies

\[
\boxed{\alpha_e<a_D.}
\tag{3.1}
\]

The vertex is unloaded, so its exact KKT equilibrium is purely contact-mechanical:

\[
\sum_{e=vw\in C}\alpha_e\frac{w-v}{|w-v|}=0.
\tag{3.2}
\]

All contact lengths are one.

---

## 4. Local equilibrium classification

ZRP gives radial degree at most two away from `z`. A regular vertex is deep and hence not `z`.

### Case 0: no radial contacts

All four incident contacts are nonradial and satisfy `alpha<a_D`. Hence

\[
\boxed{
\sum_{e\ni v}\alpha_e<4a_D.
}
\tag{ZLS4}

### Case 1: exactly one radial contact

Let its stress be `A`. The other three contact-force vectors have total norm less than `3a_D`. Equilibrium forces

\[
A<3a_D.
\]

Thus

\[
\boxed{
\sum_{e\ni v}\alpha_e<6a_D.
}
\tag{ZLS5}

So a regular vertex carrying stress much larger than `a_D` cannot have radial degree zero or one.

### Case 2: two radial contacts

Let their stresses be `A,B>0` and outward unit force directions from `v` be `u_1,u_2`. The remaining two nonradial forces have total norm less than `2a_D`, so

\[
\boxed{
|Au_1+Bu_2|<2a_D.
}
\tag{ZLS6}

Immediately,

\[
\boxed{|A-B|<2a_D.}
\tag{ZLS7}

Let `theta in (0,pi]` be the smaller angle between `u_1,u_2`, and put

\[
\phi:=\pi-\theta.
\]

Then

\[
|Au_1+Bu_2|^2
=(A-B)^2+4AB\sin^2(\phi/2).
\]

Using ZLS6,

\[
\boxed{
\sin(\phi/2)
<
\frac{a_D}{\sqrt{AB}}.
}
\tag{ZLS8}

Thus whenever `min(A,B)` dominates `a_D`, the two radial contacts are asymptotically opposite and have asymptotically equal stresses.

---

## 5. Moving-scale strong radial continuation

Let `lambda_D>0` be any scale satisfying

\[
\boxed{
\frac{a_D}{\lambda_D}\to0.
}
\tag{5.1}
\]

Suppose a regular vertex is incident with a radial contact of stress at least `lambda_D`.

Cases 0-1 are impossible for large `D`. Therefore there is a unique second radial contact. By ZLS7 its stress is at least

\[
\lambda_D-2a_D
=(1-o(1))\lambda_D.
\tag{5.2}
\]

By ZLS8 its direction differs from exact straight continuation by

\[
\boxed{
\phi=O(a_D/\lambda_D)=o(1).
}
\tag{ZLS9}

Thus a strong radial edge has a unique almost-straight continuation through every regular endpoint.

---

## 6. Propagation over a long regular run

Orient a radial path component outward from smaller radius to larger radius. Suppose

\[
e_0,e_1,\ldots,e_L
\]

is a consecutive radial path run whose internal vertices are all regular, with

\[
\alpha_{e_0}\ge\lambda_D.
\]

Repeated ZLS7 gives

\[
\boxed{
|\alpha_{e_j}-\alpha_{e_0}|<2ja_D.
}
\tag{6.1}
\]

Every strongly-radial edge changes radius by more than `c_*`, so an outward run inside a diameter-`D` source has

\[
L< D/c_*+1.
\tag{6.2}
\]

Hence

\[
\boxed{
|\alpha_{e_j}-\alpha_{e_0}|
=O(Da_D).
}
\tag{ZLS10}

If the entry scale satisfies the stronger condition

\[
\boxed{
\lambda_D\gg Da_D,
}
\tag{6.3}
\]

then the entire run retains stress `(1-o(1))alpha_{e_0}`.

Similarly, summing ZLS8 along the run gives total turning

\[
\sum\phi_j
=O\!\left(\frac{La_D}{\lambda_D}\right)
=O\!\left(\frac{Da_D}{\lambda_D}\right).
\tag{6.4}
\]

Thus under (6.3),

\[
\boxed{
\text{total turning along the regular run}=o(1).
}
\tag{ZLS11}

For an actual fixed-fraction macroscopic stress `lambda_D=cD`, conditions (5.1) and (6.3) hold because `a_D->0`. Therefore any `Theta(D)`-stress radial load that enters a regular bulk run propagates through it with only `o(D)` stress loss and `o(1)` total angular turn.

---

## 7. Relation to ZAC/ZDC moving corridor scales

ZAC/ZDC choose a selected-corridor stress scale

\[
\widetilde\gamma_DD
\]

with

\[
\delta_D/\widetilde\gamma_D\to0.
\]

The explicit ZAC choice has `widetilde gamma_D` decaying only as a small power of `delta_D`, whereas

\[
a_D=\sqrt{\delta_D}.
\]

Therefore

\[
\boxed{
 a_D/\widetilde\gamma_D\to0.
}
\tag{7.1}
\]

At regular vertices the selected corridor load thus has unique almost-straight radial continuation. The stronger whole-run condition `widetilde gamma_D >> a_D` controls accumulated **angle** over `O(1)`-diameter blocks; a run of length `Theta(D)` additionally needs comparison with `Da_D`, which is not automatic.

This distinction is retained explicitly.

---

## 8. Train-scale interpretation

A typical ZRI rhombus with two radial opposite sides and two weak transverse sides is now a mechanically precise strip cell:

- the transverse opposite side pair has stress `<a_D`;
- at a regular vertex, any radial stress much larger than `a_D` must pass into the opposite radial direction with almost equal weight.

Thus ZWT's weak-rich trains are not merely lines containing many small coefficients. Where they cross a mechanically significant radial strand at regular vertices, the weak train produces only an `O(a_D)` perturbation of a nearly straight through-load.

The oblique-grid regression survives exactly in this form: a family of nearly straight load-bearing strands may be cross-braced by a quadratic population of weak transverse train edges.

---

## 9. Exact remaining obstruction

ZLS identifies where a closing proof must act. A macroscopic radial load can change direction or terminate only by encountering one of:

1. the `o(D^2)` nonregular vertices;
2. a region where the radial stress has already fallen to the weak scale;
3. loaded/outer/exceptional topology.

Pure local equilibrium cannot exclude concentrating all significant mechanical events on this exceptional set. The next global theorem must show that the ZSP/ZHA/PI geometry does not provide enough exceptional events to support the required `D^2` stress while the quadratic rhombic bulk remains weakly braced.

---

## 10. Classification

**Status:** proved report-level local KKT propagation theorem.  
**Level I:** still open.  
**External literature:** none.  
**Computation:** none.
