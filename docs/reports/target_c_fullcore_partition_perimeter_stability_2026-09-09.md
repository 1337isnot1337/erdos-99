<!-- theorem-state: {"artifact_id":"ART-E312B3110C3F","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_fullcore_partition_perimeter_stability_2026-09-09.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=e1ca17adb7f35f9c26db2c393e5c51e366f03e11; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — minimal full-core interface collapses to two actual half-disk carriers

**Date:** 2026-09-09  
**Repository branch:** `research/post-uf-attachment-fill-2026-09-09`  
**Run type:** perimeter-equality stability / paired near-geodesic extraction  
**Target:** equality branch of FP  
**Depends on:** FP, HG, C36/C44/C49, HBd, finite Oler, planar finite-perimeter compactness  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

FP proves throughout the full-core near-circle branch

\[
Q_B=K_I-\pi D+2s_B+o(D),
\qquad
K_I\ge(\pi+2-o(1))D.
\]

Consider the minimal loaded-interface branch

\[
\boxed{Q_B=(2+o(1))D.}
\tag{PS.0}
\]

Then FP forces

\[
s_B=o(D),
\qquad
K_I=(\pi+2+o(1))D.
\tag{PS.1}
\]

The new conclusion is that the two HG semicircle groups cannot remain macroscopically fragmented.

For each of the two dominant semicircle groups there is one unloaded harmonic component `J_i` such that

\[
\boxed{
|J_i|=(\Delta/2+o(1))D^2,
\qquad
\operatorname{area}(\operatorname{conv}J_i)
=(\pi/8+o(1))D^2,
}
\tag{PS.2}
\]

\[
\boxed{
\operatorname{per}(\operatorname{conv}J_i)
=\left(1+\frac\pi2+o(1)\right)D,
}
\tag{PS.3}
\]

and every other component in that semicircle group has total population `o(D^2)` and total convex-hull perimeter `o(D)`.

Moreover

\[
\boxed{
\operatorname{conv}(J_i)/D\to C_i
}
\tag{PS.4}
\]

in Hausdorff distance, where `C_1,C_2` are complementary radius-`1/2` semicircles.

Finally the internal contact graph of each `J_i` contains a simple unit-contact path `P_i` whose endpoints `a_i,b_i` satisfy

\[
|a_i-b_i|=D-o(D),
\qquad
|P_i|=D+o(D),
\tag{PS.5}
\]

and

\[
\max_{p\in P_i}\operatorname{dist}(p,[a_i,b_i])=o(D).
\tag{PS.6}
\]

The two endpoint chords converge to the same diameter of the limiting disk, from the two complementary semicircle sides. Thus the minimal-interface full-core branch contains two actual paired near-geodesic contact paths.

This recovers the two-carrier geometry of TS without assuming the cap-cost equality `S/D->2`; the hypothesis is instead the geometrically meaningful minimal interface defect PS.0.

---

## 1. Equality in FP is equality in each semicircle perimeter budget

HG gives two dominant groups `G_1,G_2`. For each group put

\[
U_{i,D}:=\bigcup_{r\in G_i}K_r,
\qquad
K_r:=\operatorname{conv}(I_r).
\]

The FP proof gives

\[
\sum_{r\in G_i}\operatorname{per}(K_r)
\ge
\left(1+\frac\pi2-o(1)\right)D,
\tag{1.1}
\]

while every internal outer-face walk satisfies

\[
k_r\ge\operatorname{per}(K_r).
\tag{1.2}
\]

Summing both groups and using PS.1 gives

\[
\sum_r k_r=(\pi+2+o(1))D.
\]

All terms are nonnegative, so every lower bound used above is asymptotically sharp. In particular, for `i=1,2`,

\[
\boxed{
\sum_{r\in G_i}k_r
=
\sum_{r\in G_i}\operatorname{per}(K_r)
=
\left(1+\frac\pi2+o(1)\right)D,
}
\tag{1.3}
\]

and

\[
\boxed{
\sum_{r\in G_i}
\left(k_r-\operatorname{per}(K_r)\right)=o(D).
}
\tag{1.4}
\]

The nondominant groups have total outer-walk length and convex-hull perimeter `o(D)`.

HG/FP also gives, after scaling by `D`,

\[
\chi_{U_{i,D}/D}\to\chi_{C_i}
\quad\hbox{in }L^1,
\tag{1.5}
\]

where `C_i` is a semicircle of radius `1/2` and

\[
\operatorname{Per}(C_i)=1+\frac\pi2.
\]

---

## 2. A perimeter-minimizing convex partition of a connected cap has one macroscopic cell

We isolate the only geometric stability input needed here.

### Lemma PS.1 — no macroscopic fragmentation at perimeter equality

Let `C` be a bounded connected Lipschitz convex set in the plane. For each `j`, let

\[
K_{j,1},\ldots,K_{j,m_j}
\]

be compact convex sets with pairwise disjoint interiors, contained in an `o(1)` Hausdorff neighborhood of `C`. Assume

\[
\chi_{\cup_rK_{j,r}}\to\chi_C
\quad\hbox{in }L^1
\tag{2.1}
\]

and

\[
\sum_r\operatorname{per}(K_{j,r})
\to\operatorname{Per}(C).
\tag{2.2}
\]

Then, after choosing a largest-area member `K_{j,*}`,

\[
|K_{j,*}|\to|C|,
\qquad
\operatorname{per}(K_{j,*})\to\operatorname{Per}(C),
\tag{2.3}
\]

and

\[
\sum_{r\ne *}|K_{j,r}|\to0,
\qquad
\sum_{r\ne *}\operatorname{per}(K_{j,r})\to0.
\tag{2.4}
\]

#### Proof

The planar isoperimetric inequality gives

\[
\operatorname{per}(K_{j,r})\ge2\sqrt{\pi|K_{j,r}|}.
\]

Since the total perimeter is bounded and the total area tends to `|C|>0`, the largest cell has area bounded below by a positive constant along every subsequence.

Suppose (2.3) fails. Then for some `eta>0`, after a subsequence,

\[
\eta\le |K_{j,*}|\le |C|-\eta.
\tag{2.5}
\]

The convex sets `K_{j,*}` have uniformly bounded diameter and perimeter, so by compactness they converge in `L^1`, after another subsequence, to a convex finite-perimeter set `E subset C` with

\[
0<|E|<|C|.
\]

Let

\[
R_j:=\bigcup_{r\ne *}K_{j,r}.
\]

Then `R_j` has uniformly bounded perimeter because

\[
\operatorname{Per}(R_j)
\le
\sum_{r\ne *}\operatorname{per}(K_{j,r}).
\]

Using (2.1), after compactness

\[
\chi_{R_j}\to\chi_{C\setminus E}
\quad\hbox{in }L^1.
\]

Lower semicontinuity of perimeter gives

\[
\liminf_j
\sum_r\operatorname{per}(K_{j,r})
\ge
\operatorname{Per}(E)+
\operatorname{Per}(C\setminus E).
\tag{2.6}
\]

For a finite-perimeter partition of a connected Lipschitz set,

\[
\operatorname{Per}(E)+
\operatorname{Per}(C\setminus E)
=
\operatorname{Per}(C)+2\operatorname{Per}(E;C).
\tag{2.7}
\]

The relative perimeter is strictly positive because both `E` and `C\setminus E` have positive area; equivalently this follows from the relative isoperimetric inequality in `C`. Thus the right side of (2.6) is strictly larger than `Per(C)`, contradicting (2.2).

Hence `|K_{j,*}|->|C|`. Since the other interiors are disjoint and their union fills `C` in measure, their total area tends to zero.

Lower semicontinuity gives

\[
\liminf\operatorname{per}(K_{j,*})\ge\operatorname{Per}(C).
\]

But the sum of all perimeters tends to `Per(C)`, so equality holds and the residual perimeter sum tends to zero. This proves (2.3)-(2.4). `square`

The lemma uses no special packing property; it is the exact equality structure of the perimeter lower-semicontinuity step in FP.

---

## 3. Apply the partition lemma to each HG semicircle group

Scale by `D` and apply Lemma PS.1 to (1.3)-(1.5). For each `i` choose the largest-area component hull

\[
K_i^*:=\operatorname{conv}(J_i).
\]

Then

\[
\frac{\operatorname{area}(K_i^*)}{D^2}	o\frac\pi8,
\qquad
\frac{\operatorname{per}(K_i^*)}{D}	o1+\frac\pi2,
\tag{3.1}
\]

and all remaining component hulls in `G_i` have total area `o(D^2)` and total perimeter `o(D)`.

Because `K_i^*/D` is convex, lies asymptotically in `C_i`, and has area tending to `area(C_i)`, every Hausdorff-convergent subsequence has limit exactly `C_i`. Hence

\[
K_i^*/D\to C_i
\]

in Hausdorff distance, proving PS.3-PS.4.

---

## 4. Population also concentrates in the same component

Apply finite Oler to every remaining component `I_r` in `G_i\setminus{J_i}` inside its own convex hull `K_r`:

\[
\frac{\sqrt3}{2}(|I_r|-1)
\le
\operatorname{area}(K_r)
+\frac{\sqrt3}{4}\operatorname{per}(K_r).
\tag{4.1}
\]

The residual total area is `o(D^2)` and the residual total perimeter is `o(D)`. HBd gives `c_I=o(D)`, so the accumulated `-1` term is `o(D^2)`. Therefore

\[
\sum_{r\in G_i,\ r\ne J_i}|I_r|=o(D^2).
\tag{4.2}
\]

HG gives total group population

\[
\sum_{r\in G_i}|I_r|
=(\Delta/2+o(1))D^2.
\]

Hence

\[
|J_i|=(\Delta/2+o(1))D^2,
\]

proving PS.2.

Thus minimal interface defect recovers two **actual** positive-density harmonic carriers without the earlier assumption `S/D->2`.

---

## 5. Their internal outer walks are themselves perimeter-minimal

Equation (1.4), together with the residual perimeter/outer-walk estimates, gives

\[
\boxed{
k(J_i)=
\left(1+\frac\pi2+o(1)\right)D,}
\tag{5.1}
\]

and

\[
\boxed{
k(J_i)-\operatorname{per}(K_i^*)=o(D).}
\tag{5.2}
\]

So the outer contact walk of each giant component has asymptotically no length to spend on macroscopic indentations, bridges, or repeated detours beyond the perimeter of its semicircular convex hull.

---

## 6. A near-geodesic contact path runs along each flat interface

Fix one carrier `J=J_i`, write `K=conv(J)`, and orient the limiting semicircle so its flat diameter is horizontal.

Hausdorff convergence `K/D->C_i` gives hull vertices `a,b in J` near the two endpoints of the limiting flat diameter such that

\[
|a-b|=D-o(D).
\tag{6.1}
\]

Choose distinguished occurrences of `a,b` on the outer-face boundary walk of the connected plane graph `C[J]`. Extreme vertices occur on that walk in convex-hull cyclic order. Split the outer walk into its two `a`--`b` subwalks.

One subwalk contains, in order, all convex-hull vertices on the curved side of `K`. Its length is at least the length of that convex boundary chain, which by Hausdorff convergence is

\[
\left(\frac\pi2-o(1)\right)D.
\tag{6.2}
\]

The complete outer walk has length (5.1). Therefore the complementary subwalk `W_flat` satisfies

\[
|W_{flat}|
\le
\left(1+\frac\pi2+o(1)\right)D
-
\left(\frac\pi2-o(1)\right)D
=D+o(D).
\tag{6.3}
\]

Triangle inequality and (6.1) give the reverse bound

\[
|W_{flat}|\ge|a-b|=D-o(D).
\]

Hence

\[
\boxed{|W_{flat}|=D+o(D).}
\tag{6.4}
\]

Erase loops from `W_flat`. The resulting simple unit-contact path `P_i` keeps endpoints `a,b`, cannot be longer, and cannot be shorter than their Euclidean separation. Thus

\[
|P_i|=D+o(D),
\qquad
|a-b|=D-o(D),
\]

which proves PS.5.

Let `L_i=|P_i|` and `d_i=|a-b|`. Every path vertex lies in the ellipse with foci `a,b` and major-axis length `L_i`. Its maximum distance from `[a,b]` is at most

\[
\frac12\sqrt{L_i^2-d_i^2}=o(D),
\]

proving PS.6.

The two limiting semicircles are complementary, so both chords `[a_i,b_i]/D` converge to the same diameter segment of the limiting disk. The paths lie in the respective giant harmonic components and approach that interface from the two sides at normalized scale.

---

## 7. Directional concentration

Orient the unit edges of `P_i` from `a_i` to `b_i`, let their vectors be `v_1,...,v_N`, and put

\[
u_i=(b_i-a_i)/|b_i-a_i|.
\]

Then

\[
\sum_jv_j=b_i-a_i
\]

and therefore

\[
\sum_j(1-u_i\cdot v_j)
=N-|a_i-b_i|=o(D).
\tag{7.1}
\]

Consequently, for every fixed `theta>0`, only `o(D)` edges of `P_i` make angle at least `theta` with the common interface direction. Thus both interface paths are asymptotically straight in the same quantitative sense as the ZSP near-geodesic path on PR #111, but here the paths occur as a paired geometric consequence of full-core partition equality rather than bridge-stress concentration.

---

## 8. What this closes and what remains

PS eliminates the remaining macroscopic-fragmentation escape inside the minimum-interface branch.

The branch now has the concrete normal form

```text
force hull / D -> disk;
two actual harmonic components J1,J2;
|Ji|=(Delta/2+o(1))D^2;
conv(Ji)/D -> complementary semicircles;
outer-walk length(Ji)=(1+pi/2+o(1))D;
all other harmonic population=o(D^2);
all other harmonic hull perimeter=o(D);
s_B=o(D);
Q_B=(2+o(1))D;
two simple unit-contact paths Pi with
    |Pi|=D+o(D),
    endpoint span=D-o(D),
    tube width=o(D),
    common limiting diameter direction.
```

This is substantially narrower than the earlier two-group HG endpoint and stronger than TS in one respect: it is triggered by the exact interface-defect equality rather than by a separate assumption on total graph diameter `S`.

It still does not prove Level I. Two staggered near-straight rows with dense near-60-degree rhombic fillings on opposite sides are a plausible leading-order regression. The remaining theorem must use positive equilibrium/KKT support, exact global attainment, or a boundary-order packing loss to exclude that paired configuration.

---

## 9. Next target

The shortest new target is a **paired near-geodesic interface theorem**:

> Two positive-density harmonic components of a triangle-free global minimizer cannot simultaneously fill complementary half-disks at Oler density while each has a `D+o(D)` free-boundary contact path converging to the common diameter and while the loaded hull uses all but `o(D)` of its one remaining interior-contact slots.

A single near-geodesic path is not enough; PR #111 already exhibits that obstruction. The paired geometry is the genuinely new ingredient supplied by PS.
