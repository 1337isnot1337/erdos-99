> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_reinhardt_polygonal_match_2026-09-09.md) · source SHA-256 `ab9db94ff5a08cfba910b32f833e8a8b3acbab59de9f4c3ebe3bbc5b50ad3b2d`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-16F8C673845F","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic endpoint: Reinhardt/polygonal-isoperimetric scale matching

**Date:** 2026-09-09  
**Repository base:** PR #118 after DP, reconciled with main `6ed9d78ae146b68fd9b14c3c3486b048f3d59074`  
**Run type:** sharp discrete isoperimetric refinement  
**Target:** Target C cyclic primitive endpoint  
**Depends on:** DP exact difference-body lower bound and `q/D->pi`; classical polygonal isoperimetric inequality; Reinhardt's perimeter-diameter inequality for convex polygons  
**External references:**
- G. Fejes Tóth, *Finite variations on the isoperimetric problem*, arXiv:2202.09920, reviewing Reinhardt's 1922 theorem `p<=2n sin(pi/(2n)) d` and its equality theory.
- Basudeb Datta, *A Discrete Isoperimetric Problem*, Geometriae Dedicata 64 (1997), 55-68, proving the same universal perimeter bound and equality characterization.
- Classical polygonal isoperimetry: `P^2>=4N tan(pi/N) A`, equality for the regular `N`-gon.

## LEVEL I STATUS

`STILL OPEN`

DP proved for every cyclic primitive survivor

$$
\frac qD\to\pi,
\qquad
0\le t_D:=\pi D-q\le\frac{\pi}{12D}+O(D^{-2}).
$$

Two sharp discrete convex-polygon inequalities improve this by a factor two and, crucially, give the **matching lower bound**:

$$
\boxed{
\pi D-q
=
\frac{\pi}{24D}+O(D^{-2}).}
\tag{RP.1}

This now holds in all three cyclic diameter-topology phases `d_H=0,1,2`, not only the unicyclic phase.

Consequently, if the projective diameter-direction gaps are `g_i` and

\[
\delta_D=2\arcsin\frac1{2D},
$$

then

$$
\boxed{
\sum_i(g_i-\delta_D)
=
\frac{d_H}{D}+O(D^{-3}).}
\tag{RP.2}

In particular, for `d_H=0`,

\[
\boxed{
0\le g_i-\delta_D=O(D^{-3})
\quad\text{for every diameter-direction gap}.}
\tag{RP.3}

The cyclic source is therefore asymptotically extremal not only for continuous perimeter-diameter, but at the exact discrete Reinhardt scale.

---

## 1. Polygonal isoperimetry sharpens the DP upper side

The difference body `F-F` is a centrally symmetric convex polygon. Since `F` has `q` sides, `F-F` has at most `2q` sides. DP gives

\[
\operatorname{per}(F-F)=2q.
\tag{1.1}

The classical polygonal isoperimetric inequality says that every convex polygon with at most `N` sides and perimeter `P` satisfies

\[
\boxed{
A\le\frac{P^2}{4N\tan(\pi/N)}.}
\tag{1.2}

The right side is increasing with `N`, so with `N=2q`,

\[
\boxed{
\operatorname{area}(F-F)
\le
\frac{q}{2\tan(\pi/(2q))}.}
\tag{1.3}

Using

\[
\cot x
=\frac1x-\frac x3-\frac{x^3}{45}+O(x^5),
$$

we obtain

$$
\boxed{
\frac{q}{2\tan(\pi/(2q))}
=
\frac{q^2}{\pi}
-
\frac\pi{12}
-
\frac{\pi^3}{720q^2}
+O(q^{-4}).}
\tag{1.4}

The continuous isoperimetric upper used in DP was only `q^2/pi`; the discrete side count supplies the fixed extra saving `pi/12+o(1)`.

---

## 2. Compare to the exact DA lower bound

DP/DA gives

\[
\operatorname{area}(F-F)
\ge
D^2\left[
(h-1)\sin\delta_D
+
\sin((h-1)\delta_D)
\right].
\tag{2.1}

Write

\[
d:=d_H\in\{0,1,2\},
\qquad
h=q-d,
\qquad
q=\pi D-t_D.
$$

DP already gives `t_D=O(D^{-1})`. The expansions from DP therefore sharpen uniformly in bounded `d` to

$$
\boxed{
D^2\left[
(h-1)\sin\delta_D
+
\sin((h-1)\delta_D)
\right]
=
\pi D^2-\frac\pi6+O(D^{-1}).}
\tag{2.2}

On the other hand, (1.4) and `q=pi D-t_D` give

\[
\begin{aligned}
\operatorname{area}(F-F)
&\le
\frac{(\pi D-t_D)^2}{\pi}
-\frac\pi{12}+O(D^{-2})\\
&=
\pi D^2-2Dt_D-\frac\pi{12}+O(D^{-2}),
\end{aligned}
\tag{2.3}

because `t_D^2=O(D^{-2})`.

Combining (2.2) and (2.3),

\[
-\frac\pi6+O(D^{-1})
\le
-2Dt_D-\frac\pi{12}+O(D^{-2}).
$$

Hence:

### Theorem RP.1 — discrete upper deficit

$$
\boxed{
 t_D
\le
\frac\pi{24D}+O(D^{-2}).}
\tag{RP.4}

This improves the DP bound `pi/(12D)` by a factor two.

---

## 3. Reinhardt gives the matching lower deficit

Reinhardt's universal theorem for a convex `q`-gon of diameter `D` and perimeter `P` is

\[
\boxed{
P\le 2q\sin\frac{\pi}{2q}\,D.}
\tag{3.1}

Our cyclic force hull is equilateral with exactly `q` unit sides, hence

\[
P=q.
$$

Therefore

$$
\boxed{
D\ge\frac1{2\sin(\pi/(2q))}.}
\tag{3.2}

For large `q`,

\[
\frac1{2\sin(\pi/(2q))}
=
\frac q\pi
+
\frac\pi{24q}
+O(q^{-3}).
\tag{3.3}

Multiply by `pi` and rearrange:

\[
\boxed{
\pi D-q
\ge
\frac{\pi^2}{24q}+O(q^{-3}).}
\tag{3.4}

DP gives `q/(pi D)->1`, so

\[
\frac{\pi^2}{24q}
=
\frac\pi{24D}+O(D^{-3})
$$

once `t_D=O(D^{-1})` is used. Thus:

### Theorem RP.2 — Reinhardt lower deficit

$$
\boxed{
 t_D
\ge
\frac\pi{24D}+O(D^{-3}).}
\tag{RP.5}

Combining RP.4 and RP.5 proves RP.1. `square`

No equality characterization is needed for this asymptotic conclusion. Reinhardt equality is attained whenever `q` is not a power of two; the extremizers are the Reinhardt/clipped-Reuleaux polygons reviewed by Fejes Tóth and Datta.

---

## 4. Diameter-direction gap excess improves by one order

Let the `h` projective diameter gaps be `g_i`. C67 gives

\[
g_i\ge\delta_D,
\qquad
\sum_i g_i=\pi.
$$

Hence the total gap excess is exactly

$$
E_{dir}
:=
\sum_i(g_i-\delta_D)
=
\pi-h\delta_D.
\tag{4.1}

Use

\[
h=q-d_H
=\pi D-t_D-d_H,
$$

$$
\delta_D
=
\frac1D+\frac1{24D^3}+O(D^{-5}),
$$

and RP.1:

$$
t_D
=
\frac\pi{24D}+O(D^{-2}).
$$

Then

$$
\begin{aligned}
h\delta_D
&=
\left(\pi D-d_H-\frac\pi{24D}+O(D^{-2})\right)
\left(\frac1D+\frac1{24D^3}+O(D^{-5})\right)\\
&=
\pi-\frac{d_H}{D}+O(D^{-3}).
\end{aligned}
$$

Therefore

$$
\boxed{
E_{dir}
=
\frac{d_H}{D}+O(D^{-3}),}
$$

which is RP.2.

For `d_H=0`, `E_dir=O(D^{-3})`. Since every summand `g_i-delta_D` is nonnegative, each individual gap obeys RP.3.

This is a substantial rigidity upgrade: the unicyclic cyclic branch has projective diameter directions uniformly spaced to **third order in the total angular budget**.

---

## 5. Local normal-cone interpretation

Let `theta_b` be the exterior turning angle of the convex unit force hull at loaded vertex `b`, and let `deg_H(b)` be its full diameter degree.

For any incident diameter edge `bk`, the unit direction from `k` to `b` is a strict support normal at `b`. For each of the two adjacent unit hull sides `bc`, the diameter support inequality gives

$$
\frac{b-k}{D}\cdot(b-c)
\ge\frac1{2D}.
$$

Thus every incident diameter normal lies at angular distance at least

$$
a_D:=\arcsin\frac1{2D}
=\delta_D/2
$$

from each boundary ray of the normal cone at `b`.

Distinct incident diameter directions are separated by at least `delta_D`. Therefore `deg_H(b)` such directions fit only if

$$
\boxed{
\theta_b
\ge
\deg_H(b)\,\delta_D.}
\tag{RP.6}

Summing over all `b`,

\[
\sum_b\theta_b=2\pi,
\qquad
\sum_b\deg_H(b)=2h,
$$

so the total local normal-cone slack is

$$
\boxed{
\sum_b
\left(
\theta_b-\deg_H(b)\delta_D
\right)
=2(\pi-h\delta_D)
=
\frac{2d_H}{D}+O(D^{-3}).}
\tag{RP.7}

Every summand is nonnegative.

In particular, for `d_H=0`,

\[
\boxed{
0\le
\theta_b-\deg_H(b)\delta_D
=O(D^{-3})
\quad\text{for every loaded vertex }b.}
\tag{RP.8}

So the exterior angle at every vertex is locked to its integer diameter degree times the minimum projective gap, with only third-order slack.

---

## 6. Interpretation of the three diameter phases

### `d_H=0`

\[
\pi D-q
=
\frac\pi{24D}+O(D^{-2}),
$$

$$
E_{dir}=O(D^{-3}),
$$

and every local cone satisfies

$$
\theta_b
=
\deg_H(b)\delta_D+O(D^{-3}).
$$

This is the exact asymptotic scale of regular odd shells and Reinhardt perimeter extremizers.

### `d_H=1`

The same perimeter deficit holds, while

$$
E_{dir}=D^{-1}+O(D^{-3}).
$$

All deviation from perfect projective spacing has total budget one minimum-gap scale.

### `d_H=2`

Again the same perimeter deficit, and

$$
E_{dir}=2D^{-1}+O(D^{-3}).
$$

Only two minimum-gap scales of total angular defect remain.

Thus `d_H` has become literally the leading-order number of projective-gap units available for all diameter-topology irregularity.

---

## 7. Relation to Reinhardt extremizers

Reinhardt's upper bound is sharp for every `q` having an odd factor; all exact maximizers are equilateral and arise from clipped Reuleaux/Reinhardt constructions. For `q=2^s`, the sharp maximum is strictly below the Reinhardt upper bound, although known constructions approach it very closely as `q` grows.

RP proves only asymptotic saturation of the universal Reinhardt **upper bound**. It does not assert exact membership in the Reinhardt equality family or exclude powers of two.

The next stability theorem should exploit the much stronger Target C data absent from the pure Reinhardt problem:

- every vertex is an actual diameter endpoint;
- the diameter graph is a convex geometric thrackle with only `d_H<=2` tree components;
- every KKT stress keeps the full unit cycle positive;
- the projective diameter gaps have total excess `d_H/D+O(D^-3)`.

---

## 8. Regression audit

### Regular odd shell

It satisfies Reinhardt equality exactly and has

$$
D=\frac1{2\sin(\pi/(2q))}.
$$

Therefore

$$
\pi D-q
=
\frac\pi{24D}+O(D^{-3}),
$$

matching RP.1.

### Nonregular Reinhardt polygons

For composite `q` with odd factor, nonregular equilateral Reinhardt polygons also attain the same perimeter bound. RP deliberately does not claim regularity from perimeter saturation alone.

### Power-of-two `q`

Reinhardt's bound is not attained exactly, but the universal upper remains valid. RP is asymptotic and does not use equality.

### Polygonal side count

If `F-F` has fewer than `2q` sides, the polygonal isoperimetric upper only decreases. Using `2q` is therefore safe and potentially nonsharp.

---

## 9. Next theorem

The cyclic branch is now at the discrete extremal scale:

$$
q
=
\pi D-\frac\pi{24D}+O(D^{-2}).
$$

The best next target is a **Reinhardt stability with diameter-thrackle labels**:

> show that an equilateral `q`-gon at this perimeter scale, with every vertex diametral and only `d_H<=2` units of projective-gap defect, must have the same diameter incidence code as a Reinhardt polygon, and then use the Target C stress/rattler constraints to exclude that code or reduce it to the regular odd shell.

The local locking RP.8 makes the `d_H=0` case especially rigid and should be attacked first.

---

## 10. Promotion recommendation

**Hold as report pending independent audit.**

The polygonal and Reinhardt inequalities are classical external inputs. All Target C reductions and asymptotic matching are proved explicitly here.

---

## 11. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

DP gave t_D=pi D-q=O(1/D).

Polygonal isoperimetry on F-F (<=2q sides, perimeter 2q):
  area(F-F) <= q/[2 tan(pi/(2q))]
            = q^2/pi-pi/12+O(q^-2).
DA lower:
  area(F-F) >= pi D^2-pi/6+O(D^-1).
Hence
  t_D <= pi/(24D)+O(D^-2).

Reinhardt:
  per(F)=q <= 2q sin(pi/(2q)) D,
so
  D >=1/[2sin(pi/(2q))]
and
  t_D >= pi/(24D)+O(D^-3).
Therefore
  pi D-q=pi/(24D)+O(D^-2)
for all d_H=0,1,2.

Projective diameter gap excess:
  E_dir=pi-h delta_D=d_H/D+O(D^-3).
For d_H=0 every individual gap is
  g_i=delta_D+O(D^-3).

Local normal-cone packing gives
  theta_b >= deg_H(b) delta_D,
and total slack
  sum_b(theta_b-deg_H(b)delta_D)
    =2d_H/D+O(D^-3).
For d_H=0 every vertex has
  theta_b=deg_H(b)delta_D+O(D^-3).

Next: Reinhardt stability with the actual diameter-thrackle incidence labels.
```
