<!-- theorem-state: {"artifact_id":"ART-C3C583D64122","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — ZHT: the heavy chain fills into a consecutive macroscopic bridge trunk

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-deep-harmonic-capture`  
**Run type:** closing-proof continuation / bridge-force coherence  
**Target:** Target C, Gate C-II / Level I  
**Depends on:** ZHH, C18, C23, C66  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

ZHH localizes a nested chain of macroscopic bridges inside one unloaded harmonic cell. A chain in the bridge-tree ancestor order may skip intervening bridge edges. This report proves that, in the near-zero response phase, there are in fact no light gaps between the C66 star center and the deepest ZHH cut.

The reason is mechanical. The deepest cut carries a fixed positive mass of diameter reactions incident to the C66 center `z`. Every ancestor bridge is crossed by those same star edges. C18 puts all diameter directions incident to `z` inside a cone of width asymptotically `50.761` degrees, strictly below `60` degrees. Their vector resultant therefore cannot cancel. The complete nonstar beta mass is `o(1)` by C66, so it cannot cancel a fixed star resultant either.

Hence **every** bridge on the complete tree route from `z` to the deepest ZHH cut has stress `Omega_eta(D)`. The same harmonic cell contains this entire consecutive bridge trunk.

---

## 1. Starting ZHH cut

Assume

\[
S_{br}\ge\eta D^2,
\qquad
D\varepsilon\to0.
\tag{1.1}
\]

ZHH gives a nested chain of bridges

\[
e_1\prec\cdots\prec e_L,
\qquad
L\ge\frac{\eta^2}{16\pi}D,
\tag{1.2}
\]

with

\[
\alpha_{e_j}\ge\frac{\eta}{4\pi}D.
\tag{1.3}
\]

Root the global contact bridge tree at the block containing the C66 center `z`, and let `e_L` be the deepest selected bridge.

Its crossing beta mass obeys

\[
w_{e_L}\ge\frac{\eta}{4\pi}.
\tag{1.4}
\]

C66 gives total nonstar beta mass

\[
\tau_z:=\sum_{g\not\ni z}\beta_g
\le C_0D\varepsilon=o(1).
\tag{1.5}
\]

Therefore the star edges incident to `z` and crossing `e_L` have total beta mass

\[
s_L\ge\frac{\eta}{4\pi}-\tau_z.
\tag{1.6}
\]

For sufficiently large members,

\[
\boxed{s_L\ge\frac{\eta}{8\pi}.}
\tag{1.7}
\]

Choose one actual star edge `zy_0` crossing `e_L`, and put

\[
u_0=\frac{y_0-z}{D}.
\tag{1.8}
\]

---

## 2. Every star direction has positive uniform projection on `u_0`

C18 gives an explicit angle bound `Theta(D)` between any two diameter chords incident to one source point, with

\[
\Theta(D)\to\theta_\infty
=\frac{5\pi}{6}-\sqrt3
<\frac\pi3.
\tag{2.1}
\]

Hence for all sufficiently large members,

\[
\Theta(D)<\frac\pi3.
\tag{2.2}
\]

If `zy` is any diameter edge incident to `z`, then

\[
u_0\cdot\frac{y-z}{D}
\ge\cos\Theta(D)
>\frac12.
\tag{2.3}
\]

Thus all star reaction directions have a common strictly positive projection.

---

## 3. Every ancestor bridge has macroscopic stress

Let `f=uv` be **any** bridge on the complete bridge-tree path from the block of `z` to the descendant side of `e_L`. Orient it so `u` is on the descendant side and `v` on the `z` side.

Every star edge crossing `e_L` also crosses `f`. C23's exact cut-force identity, divided by `D`, is

\[
\frac{\alpha_f}{D}(u-v)
=
\sum_{g\pitchfork f}\beta_g r_g,
\tag{3.1}
\]

where each `r_g` is the corresponding unit diameter direction oriented from the descendant side toward the root side or vice versa consistently with (3.1). For the star edges `zy` whose partner `y` is descendant, their contribution has unit direction `(y-z)/D`.

Project (3.1) onto `u_0`. The fixed star subfamily crossing `e_L` contributes more than `s_L/2` by (2.3). All additional star edges crossing `f` also have positive projection and may be discarded from the lower bound. The complete nonstar contribution has norm at most `tau_z` and hence projection at least `-tau_z`.

Therefore

\[
\frac{\alpha_f}{D}
\ge
u_0\cdot\frac{\alpha_f}{D}(u-v)
>
\frac{s_L}{2}-\tau_z.
\tag{3.2}
\]

Using (1.7) and eventually `tau_z<=eta/(32pi)`,

\[
\boxed{
\alpha_f\ge\frac{\eta}{32\pi}D.
}
\tag{ZHT1}
\]

So every bridge between `z` and the deepest ZHH cut is macroscopic. There are no light bridge gaps.

---

## 4. The full bridge-tree trunk is linearly long

Let

\[
f_1,\ldots,f_H
\tag{4.1}
\]

be all bridge edges on the complete tree route from the block containing `z` through `e_L`. Because the selected ZHH chain has `L` comparable bridge edges ending at `e_L`,

\[
H\ge L.
\tag{4.2}
\]

Therefore

\[
\boxed{
H\ge\frac{\eta^2}{16\pi}D,
\qquad
\alpha_{f_j}\ge\frac{\eta}{32\pi}D
\quad(1\le j\le H).
}
\tag{ZHT2}
\]

The total stress on this **consecutive** trunk obeys

\[
\boxed{
\sum_{j=1}^H\alpha_{f_j}
\ge
\frac{\eta^3}{512\pi^2}D^2.
}
\tag{ZHT3}
\]

ZHH's selected heavy subchain has the stronger stress constant `eta^3/(64pi^2)`; ZHT's gain is structural completeness of the trunk.

---

## 5. The complete trunk lies in one harmonic cell

ZHH supplies an unloaded component `I_*` and a nonempty assigned family of star diameter edges `zy` crossing `e_L`, with both endpoints in `A_*`.

Choose one such `zy`. Since `I_*` is connected, there is a contact path from `z` to `y` through `I_*`. Every bridge `f_j` on the root-to-`e_L` tree route separates `z` from `y`, so every such contact path must use `f_j`.

Therefore

\[
\boxed{
\{f_1,\ldots,f_H\}\subset E_*.
}
\tag{ZHT4}
\]

The same single harmonic cell contains the entire consecutive macroscopic trunk.

ZHA consequently gives

\[
\boxed{|A_*|\ge H+1\ge\frac{\eta^2}{16\pi}D+1.}
\tag{ZHT5}
\]

and an almost-perfect uniformly-short component-response matching of size at least

\[
\boxed{
\frac{H-1}{2}
\ge
\frac{\eta^2}{32\pi}D-\frac12.
}
\tag{ZHT6}
\]

---

## 6. Directional coherence of the trunk

Let `S_f` be the vector sum of all star diameter reactions crossing an ancestor bridge `f`, normalized by `D`, and `N_f` the nonstar contribution. All star directions lie in the C18 cone at `z`, while

\[
\|N_f\|\le\tau_z=o(1).
\tag{6.1}
\]

The fixed subfamily from `e_L` gives

\[
\|S_f\|\ge s_L\cos(\Theta(D)/2)
\ge c_\eta>0
\tag{6.2}
\]

for large members. Hence

\[
\frac{S_f+N_f}{\|S_f+N_f\|}
\]

is at angular distance `o(1)` from the convex cone generated by the star directions. By the exact cut-force identity, this normalized resultant is the oriented unit direction of the bridge.

Thus every trunk bridge direction lies in the common C18 star cone up to `o(1)` angular error:

\[
\boxed{
\operatorname{dir}(f_j)
\subset
\text{one cone of width }\Theta(D)+o(1)
<\frac\pi3-o(1).
}
\tag{ZHT7}
\]

This is stronger than merely saying the supporting lines pass close to `z`.

ZBL/C68 additionally gives, for every fixed `xi>0`, that all but `o(D)` trunk bridges satisfy

\[
\bigl||u-z|-|v-z|\bigr|>1-\xi.
\tag{6.3}
\]

So almost the whole consecutive macroscopic trunk consists of near-radial unit bridges with mutually coherent directions.

---

## 7. Exact target implication

The bridge-dominant near-zero survivor now contains one harmonic cell with a complete trunk normal form:

```text
H >= eta^2 D/(16pi) consecutive bridge-tree edges,
every trunk bridge alpha_e >= eta D/(32pi),
all trunk bridges lie in one harmonic cell,
all trunk directions lie in one <60-degree cone up to o(1),
all but o(D) trunk bridges make near-unit radial progress from z,
|A_*| >= H+1,
short positive response matching size >= (H-1)/2,
cell/trunk carry Omega_eta(D^2) mechanical stress.
```

The remaining geometry is entirely in the two-edge-connected bridge blocks between consecutive trunk edges. No light articulation gap remains.

A sufficient next theorem is:

> **ZHT block-corridor exclusion.** Exclude a triangle-free global minimizer containing a single unloaded harmonic cell whose bridge-block tree has an `Omega(D)` consecutive trunk of `Omega(D)`-stress unit bridges in one sub-60-degree cone, with the ZHT attachment/response data.

A valid substitute is `epsilon=Omega(1/D)`, a strict sub-`D` competitor, or the exact face inequality.

---

## 8. Regressions and limits

- The bridge-tree trunk is not itself an edge-by-edge contact path; consecutive bridges may be separated by two-edge-connected blocks.
- A thin truss/ladder can abstractly carry a large nearly axial force through many blocks with tiny transverse brace stresses. ZHT does not yet rule that out.
- The cone width is below `60` degrees, not the `15`-degree threshold of Theorem P.
- Contact-isolated source points remain outside the force-visible cell.

---

## 9. Dependencies

- ZHH;
- C18 shared-endpoint diameter-angle bound;
- C23 exact bridge cut-force identity;
- C35/C41 through ZHH's cell assignment;
- C66 stress-star concentration;
- ZHA for attachment/matching consequences.

No new external literature is imported.

---

## 10. Promotion recommendation

**Hold as report.** It is downstream of report-level ZR/ZF and stacked PR #108/#111.

---

## 11. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

ZHT:
Let e_L be the deepest bridge of the ZHH heavy chain. Its cut has crossing mass
w>=eta/(4pi). Under D epsilon->0, nonstar beta mass is o(1), so star edges incident to
the C66 center z and crossing e_L carry at least eta/(8pi) beta mass for large D.
C18 puts every z-star direction within <60 degrees of any one of them.

Every bridge f on the complete tree route from z to e_L is crossed by that same fixed
star subfamily. Projecting C23's vector cut law onto one star direction and subtracting
the o(1) nonstar contribution gives
    alpha_f >= eta D/(32pi)
for every such f.

The complete trunk has at least eta^2 D/(16pi) bridge edges because it contains the ZHH
nested chain. One assigned z-star diameter edge crosses e_L and hence the whole trunk;
its path through the ZHH harmonic cell forces every trunk bridge into that same cell.
Thus the cell contains an Omega(D)-long *consecutive* macroscopic bridge trunk with no
light bridge gaps. All trunk directions lie in the common C18 star cone up to o(1), and
C68 makes all but o(D) bridge edges near-radial.

ZHA gives |A_*|>=H+1 and a uniformly-short positive response matching of size
>=(H-1)/2 inside the same cell.
```
