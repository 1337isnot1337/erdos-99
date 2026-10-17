> Generated reading edition · [exact source](../../../docs/reports/target_c_completion_shell_nearcircle_2026-09-09.md) · source SHA-256 `81819f785b18f5b47a3c834d7f010f2e1947e99bcc17ca040a26a35187189448`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-8923569D8C1F","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — completion-shell collapse of the DG endpoint

**Date:** 2026-09-09  
**Repository base:** PR #119 after DG  
**Run type:** exact convex completion / packing consequence  
**Target:** post-ZF `x_B=o(D)` branch  
**Depends on:** C65 full diameter visibility, OP finite Oler absorption, DG.6  
**External web search:** not used  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

DG proves that a post-ZF sequence with sublinear outer-walk excess

$$
x_B=b-q=o(D)
$$

has

$$
q/D\to\pi,
\qquad
\operatorname{per}(F)/D\to\pi,
\qquad
M_D:=D-\min_\theta w_F(\theta)=o(D).
$$

This report turns the last statement into a source-wide completion theorem. Every source point outside the force hull lies within distance `M_D` of the force hull. Unit separation then bounds the external population by the area of an `M_D+1/2` outer parallel strip, so the number of external C65 rattlers is `o(D^2)`.

OP then forces the force hull itself to carry asymptotically all of the global packing capacity. Consequently

$$
\boxed{
\operatorname{area}(F)/D^2\to\pi/4,
}
$$

and every normalized Hausdorff subsequential limit of `F/D` is the disk of diameter one.

Thus DG's small-outer-walk endpoint is not merely asymptotically constant-width. It is asymptotically isodiametric/circular.

A second exact observation records the loaded-boundary contact consequence:

$$
\boxed{e_{BB}\ge q-x_B.}
$$

Hence in the same endpoint

$$
\liminf_{D\to\infty} e_{BB}/D\ge\pi.
$$

Together with DG.7, a surviving small-outer-walk source must therefore combine an almost complete unit-contact cycle on the loaded hull, a near-circular force hull, and a linear `Q+2s_Z` defect.

---

## 1. The diameter-completion region of a nearly constant-width body

For a convex body `F` of diameter at most `D`, define its diameter-completion region

$$
\mathcal C_D(F)
:=\bigcap_{p\in F}\overline B(p,D).
\tag{1.1}
$$

A point lies in `C_D(F)` exactly when it can be added without making its distance from any point of `F` exceed `D`.

Put

$$
w_{min}(F):=\min_{|u|=1}w_F(u),
\qquad
M:=D-w_{min}(F)\ge0.
\tag{1.2}
$$

### Theorem DC.1 — exact completion-shell bound

$$
\boxed{
\mathcal C_D(F)\subseteq F+M\overline B(0,1).
}
\tag{DC.1}
$$

Equivalently, every `x in C_D(F)` satisfies

$$
\boxed{
\operatorname{dist}(x,F)\le D-w_{min}(F).
}
\tag{DC.2}
$$

### Proof

The assertion is trivial for `x in F`. Let `x notin F`, let `y` be a nearest point of the closed convex body `F`, and put

$$
t:=|x-y|>0,
\qquad
u:=\frac{x-y}{t}.
$$

The nearest-point property gives the supporting inequality

$$
\nu\cdot p\le\nu\cdot y
\qquad(p\in F),
$$

so

$$
h_F(\nu)=\nu\cdot y.
$$

Choose an opposite support point `p_- in F` with

$$
\nu\cdot p_-
=\min_{p\in F}\nu\cdot p
=h_F(\nu)-w_F(\nu).
$$

Then

$$
\nu\cdot(x-p_-)
=t+w_F(\nu)
\ge t+w_{min}(F).
$$

Hence

$$
|x-p_-|
\ge t+w_{min}(F).
\tag{1.3}
$$

If `x in C_D(F)`, the left side is at most `D`. Therefore

$$
t\le D-w_{min}(F)=M.
$$

This proves DC.1-DC.2. `square`

For exact constant width `w_min(F)=D`, this recovers diametric completeness directly:

$$
\mathcal C_D(F)=F.
$$

No external completeness theorem is needed.

---

## 2. Every C65 source point lies in the completion region

Let `A` be the C65 source and let

$$
F=\operatorname{conv}V(C)
$$

be its force hull. Every source point `a in A` is at distance at most `D` from every force-core vertex. By convexity of the norm, if

$$
p=\sum_i\lambda_i v_i\in F,
\qquad
\lambda_i\ge0,
\qquad
\sum_i\lambda_i=1,
$$

then

$$
|a-p|
\le\sum_i\lambda_i|a-v_i|
\le D.
$$

Thus

$$
\boxed{A\subseteq\mathcal C_D(F).}
\tag{2.1}
$$

Combining with DC.1,

$$
\boxed{
A\subseteq F+M\overline B,
\qquad
M=D-w_{min}(F).
}
\tag{2.2}
$$

In particular every source point outside `F` lies in the outer parallel strip of thickness `M`.

---

## 3. A direct packing bound for external source points

Let

$$
Z_{ext}:=|A\setminus F|.
$$

Around every external source point put the open disk of radius `1/2`. Unit separation makes these disks pairwise disjoint.

For each external center `x`, choose a line separating `x` from the convex body `F`. At least one closed half-disk of radius `1/2` centered at `x` lies in the exterior side of that line and therefore outside `F`. Its area is `pi/8`.

These chosen half-disks remain pairwise disjoint because the full radius-`1/2` disks are disjoint. By (2.2), every full disk lies in

$$
F+(M+1/2)\overline B.
$$

Therefore the chosen exterior half-disks all lie in the parallel strip

$$
(F+(M+1/2)\overline B)\setminus F.
$$

Steiner's formula gives

$$
\operatorname{area}(F+t\overline B)-\operatorname{area}(F)
=t\operatorname{per}(F)+\pi t^2.
$$

Hence:

### Theorem DC.2 — external-population shell bound

$$
\boxed{
Z_{ext}\frac\pi8
\le
(M+1/2)\operatorname{per}(F)
+\pi(M+1/2)^2.
}
\tag{DC.3}
$$

Equivalently,

$$
\boxed{
Z_{ext}
\le
\frac8\pi(M+1/2)\operatorname{per}(F)
+8(M+1/2)^2.
}
\tag{DC.4}
$$

This is finite and uses only unit separation, convexity, and source diameter.

Since `per(F)<=pi D`, if

$$
M=o(D),
$$

then

$$
\boxed{Z_{ext}=o(D^2).}
\tag{DC.5}
$$

---

## 4. DG's small-outer-walk branch has only subquadratic external population

DG.6 proves

$$
x_B=o(D)
\quad\Longrightarrow\quad
M=D-w_{min}(F)=o(D).
$$

Apply DC.5:

### Corollary DC.3

Every post-ZF sequence with

$$
x_B=o(D)
$$

satisfies

$$
\boxed{Z_{ext}=o(D^2).}
\tag{4.1}
$$

This removes the quadratic external-rattler escape that remains available under the universal DB area floor alone.

---

## 5. OP plus global density forces maximal force-hull area

OP proves the exact finite capacity bound for all source points lying in `F`:

$$
\boxed{
n-Z_{ext}
\le
\frac2{\sqrt3}\operatorname{area}(F)
+\frac12\operatorname{per}(F)+1.
}
\tag{5.1}
$$

For global minimizers,

$$
\frac n{D^2}\to
\Delta:=\frac\pi{2\sqrt3}.
\tag{5.2}
$$

In the DG endpoint, DC.3 gives `Z_ext=o(D^2)` and `per(F)=O(D)`. Divide (5.1) by `D^2` and take lower limits:

$$
\Delta
\le
\frac2{\sqrt3}
\liminf\frac{\operatorname{area}(F)}{D^2}.
$$

Since

$$
\frac{\sqrt3}{2}\Delta=\frac\pi4,
$$

we obtain

$$
\liminf\frac{\operatorname{area}(F)}{D^2}
\ge\frac\pi4.
$$

The isodiametric inequality gives the reverse bound for every `F`:

$$
\operatorname{area}(F)
\le\frac\pi4D^2.
$$

Therefore:

### Theorem DC.4 — near-circular force hull

If `x_B=o(D)` along an unbounded post-ZF sequence, then

$$
\boxed{
\frac{\operatorname{area}(F)}{D^2}
\longrightarrow\frac\pi4.
}
\tag{DC.6}
$$

After translations, every Hausdorff-convergent subsequence of `F/D` converges to the disk of diameter one.

### Justification of the last statement

The normalized bodies have uniformly bounded diameter, so after translations the Blaschke selection argument gives Hausdorff-convergent subsequences. Area is continuous under convex-body Hausdorff convergence in the plane. Any limit has diameter at most one and area `pi/4`. Equality in the planar isodiametric inequality forces the limit to be the diameter-one disk.

Thus every subsequential limit is the same disk, up to translation.

---

## 6. Almost all loaded hull intervals are direct unit contacts

The outer contact walk is partitioned into `q` walks between consecutive loaded hull vertices. If their positive integer lengths are

$$
\ell_1,\ldots,\ell_q,
$$

then

$$
\sum_i(\ell_i-1)=b-q=x_B.
\tag{6.1}
$$

At most `x_B` of these intervals can have length greater than one. Every remaining interval has length exactly one and is therefore the straight unit contact between its two consecutive loaded hull vertices.

These good hull sides are distinct loaded-loaded contact edges. Consequently:

### Theorem DC.5 — loaded boundary contact floor

$$
\boxed{
e_{BB}\ge q-x_B.
}
\tag{DC.7}
$$

In particular, in the DG endpoint,

$$
\boxed{
\liminf_{D\to\infty}\frac{e_{BB}}D\ge\pi.
}
\tag{DC.8}
$$

because `q/D->pi` and `x_B/D->0`.

This is a second independent degeneration: nearly the entire loaded force-hull cycle is an actual unit-contact cycle.

---

## 7. Combined endpoint after DG + DC

A hypothetical post-ZF sequence with `x_B=o(D)` must now satisfy simultaneously

$$
\boxed{
q/D\to\pi,
\qquad
per(F)/D\to\pi,
\qquad
area(F)/D^2\to\pi/4,
}
$$

$$
\boxed{
F/D\to\text{the diameter-one disk in Hausdorff shape},
}
$$

$$
\boxed{
Z_{ext}=o(D^2),
\qquad
\liminf_{D\to\infty} e_{BB}/D\ge\pi,
}
$$

and from DG.7,

$$
\boxed{
\liminf h/D\ge3\pi/5,
\qquad
\liminf(Q+2s_Z)/D\ge\pi/5.
}
$$

Thus the small-outer-walk branch is reduced to a near-circular, nearly unit-contact loaded boundary with a mandatory linear exceptional-face/mixed-stress defect.

The regular odd-shell regression still exhibits the boundary geometry qualitatively, so geometry alone cannot finish the argument. The missing input must use the global packing/core population or the mixed-stress/contact structure.

---

## 8. Exact next target

The remaining endpoint now has a particularly rigid simultaneous profile:

1. force hull asymptotically disk-like and isodiametric;
2. almost every loaded hull side is a unit contact;
3. external rattlers are subquadratic;
4. global packing inside the force hull is asymptotically Oler-saturated;
5. nevertheless `Q+2s_Z>= (pi/5-o(1))D`.

A closing theorem can therefore target **stability of Oler saturation under a nearly complete unit-contact hull cycle**. It is enough to prove that a near-disk unit-separated packing whose boundary has `pi D-o(D)` consecutive unit contacts cannot simultaneously carry the displayed linear bounded-face/mixed-stress defect without losing a positive boundary-order amount of Oler capacity.

No such final stability theorem is claimed here.

---

## 9. Compact handoff

```text
LEVEL I STATUS: STILL OPEN

Let M=D-min_width(F).
For the diameter-completion region
    C_D(F)=intersection_{p in F} B(p,D),
nearest-point/support geometry gives exactly
    C_D(F) subset F+M B.
Every source point lies in C_D(F).

External unit-separated points therefore lie in the M-thick outer shell. Choosing
an exterior half of each disjoint radius-1/2 packing disk gives
    Z_ext*pi/8
      <= (M+1/2) per(F)+pi(M+1/2)^2.
Thus M=o(D) implies Z_ext=o(D^2).

DG gives M=o(D) whenever x_B=o(D). OP then gives
    n-Z_ext <= (2/sqrt3)area(F)+per(F)/2+1.
Since n/D^2->pi/(2sqrt3), Z_ext=o(D^2), and area(F)<=pi D^2/4,
    area(F)/D^2 -> pi/4.
Hence normalized F tends to the disk.

Also at most x_B hull intervals have length >1, so
    e_BB >= q-x_B.
In the same endpoint liminf e_BB/D >= pi.

Final x_B=o(D) profile:
    q/D->pi,
    per(F)/D->pi,
    area(F)/D^2->pi/4,
    F/D->disk,
    Z_ext=o(D^2),
    liminf e_BB/D >= pi,
    h/D>=3pi/5-o(1),
    (Q+2s_Z)/D>=pi/5-o(1).
```
