<!-- theorem-state: {"artifact_id":"ART-9DE8B5F3FC67","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — SAC: slope-one attachment cells have vanishing area and force a narrow diameter-density window

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-nearzero-physical-carrier`  
**Run type:** geometric capacity synthesis / slope-one feasible-region reduction  
**Target:** Target C C-II, S1E/SCC/SOC endpoint  
**Depends on:** S1E, SCC, SOC, C40, C49, PI, JC actual-perimeter capacity  
**New external literature:** none  
**Computation:** scalar root evaluation only; theorem constants are characterized analytically

## LEVEL I STATUS

**STILL OPEN.**

At the RCC slope-one endpoint, SCC proves that the force-visible contact core has only `o(D^2)` vertices. More importantly for the PI/JC scalar balance, its harmonic attachment cells themselves occupy only `o(D^2)` area.

Assume

\[
D\varepsilon\to0,
\qquad
L:=e_{BB}+2s_C=D+o(D).
\tag{SAC.1}
\]

Let

\[
P_r:=\operatorname{conv}A_r
\]

be the harmonic attachment polygons.

### Theorem SAC.1 — attachment-area collapse

Under SAC.1,

\[
\boxed{
\sum_r \operatorname{area}(P_r)=o(D^2).
}
\tag{SAC.2}
\]

Consequently the C49 attachment gap

\[
G:=\operatorname{area}(F)-\sum_r\operatorname{area}(P_r)
\]

satisfies

\[
\boxed{G=\operatorname{area}(F)-o(D^2).}
\tag{SAC.3}
\]

Pass to any subsequence on which

\[
y:=\lim h/D,
\qquad
p:=\lim \operatorname{per}(F)/D,
\qquad
t:=\lim e_{BB}/D
\]

exist. S1E gives `h=q-o(D)`, and SAC.1 gives `0<=t<=1`.

PI and the actual-perimeter form of JC then imply

\[
\boxed{
A_{PI}(y)
\le
\frac{(t+\min\{y,p-y\})^2}{4\pi},
}
\tag{SAC.4}
\]

where

\[
A_{PI}(y)=
\begin{cases}
\frac12\sin y,& y\le\pi/2,\\[3pt]
\frac12,& y\ge\pi/2.
\end{cases}
\]

Using only `t<=1` and `p<=pi`, every slope-one survivor must satisfy

\[
\boxed{
A_{PI}(y)
\le
\frac{(1+\min\{y,\pi-y\})^2}{4\pi}.
}
\tag{SAC.5}
\]

This gives an explicit compact density window.

Let `y_-` be the unique root in `(2rho,pi/2)` of

\[
\boxed{
\frac12\sin y
=
\frac{(1+y)^2}{4\pi},
}
\tag{SAC.6}
\]

and define

\[
\boxed{y_+:=1+\pi-\sqrt{2\pi}.}
\tag{SAC.7}
\]

Numerically,

\[
\boxed{y_-=1.503816367367697\ldots,}
\tag{SAC.8}
\]

\[
\boxed{y_+=1.634964378958793\ldots.}
\tag{SAC.9}
\]

Then

\[
\boxed{
y_-\le\liminf h/D
\le\limsup h/D\le y_+,
}
\tag{SAC.10}
\]

and, because `q-h=o(D)`, the same window holds for `q/D`.

This improves the slope-one lower density from DB's `2rho=1.4781702664...` to `1.5038163673...` and, for the first time on this branch, supplies a nontrivial **upper** density bound below `pi`.

---

## 1. The giant attachment polygon is thin

SCC constructs the unique giant harmonic component `I_*` and actual diameter attachments `z,a in A_*`, `|z-a|=D`, such that every vertex of `I_*` lies in an `o(D)`-width strip around the line `za`.

Every attachment terminal `b in A_*` has at least one unit contact to a vertex of `I_*`. Therefore `b` lies in the unit neighborhood of that strip. The attachment polygon

\[
P_*:=\operatorname{conv}A_*
\]

is contained in the convex hull of that unit neighborhood.

The strip has longitudinal extent `D+o(D)` and transverse width `o(D)`. Enlarging it by a unit changes each scale by only `O(1)`. Hence

\[
\boxed{
\operatorname{area}(P_*)=o(D^2).
}
\tag{SAC.11}
\]

No cyclic-interval assumption on `A_*` is used.

---

## 2. Singleton attachment cells contribute only linear area

SOC proves that all but `o(D)` non-giant harmonic components are singletons, and that the total number of harmonic components is `O(D)`.

For a singleton component `I_r`, C40 gives

\[
\operatorname{diam}(A_r)\le\delta_r+2=2.
\]

Thus by the planar isodiametric inequality

\[
\operatorname{area}(P_r)\le\pi.
\]

There are only `O(D)` such cells, so

\[
\boxed{
\sum_{r\ singleton}\operatorname{area}(P_r)=O(D)=o(D^2).
}
\tag{SAC.12}
\]

The constant `pi` is deliberately crude; only the order matters.

---

## 3. The remaining nonsingleton cells also have vanishing total area

Let `R` be the set of nonsingleton harmonic components other than `I_*`.

S1E gives

\[
T_D:=\sum_{r\in R}\delta_r=o(D).
\tag{3.1}
\]

Every `r in R` has `delta_r>=1`, so

\[
|R|\le T_D=o(D).
\tag{3.2}
\]

Again C40 gives

\[
\operatorname{diam}(A_r)\le\delta_r+2.
\]

Therefore

\[
\sum_{r\in R}\operatorname{area}(P_r)
\le
\frac\pi4\sum_{r\in R}(\delta_r+2)^2.
\tag{3.3}
\]

Now

\[
\sum_{r\in R}\delta_r^2
\le
\left(\sum_{r\in R}\delta_r\right)^2
=T_D^2=o(D^2),
\]

while

\[
\sum_{r\in R}\delta_r=o(D),
\qquad
|R|=o(D).
\]

Hence the right side of (3.3) is `o(D^2)`. Together with SAC.11-SAC.12 this proves SAC.2.

C49 gives pairwise interior-disjoint attachment polygons, but disjointness is not even needed for this upper estimate.

---

## 4. Remove the attachment-cell subtraction from the PI lower bound

By definition,

\[
G=\operatorname{area}(F)-\sum_r\operatorname{area}(P_r).
\]

SAC.2 proves SAC.3.

PI gives along the selected subsequence

\[
\liminf \frac{\operatorname{area}(F)}{D^2}
\ge A_{PI}(y).
\tag{4.1}
\]

Thus

\[
\boxed{
\liminf\frac GD^2\ge A_{PI}(y).
}
\tag{SAC.13}
\]

This is much stronger at slope one than the generic GU estimate

\[
G/D^2\ge A_{PI}(y)-\frac\pi4L^2/D^2-o(1),
\]

because the latter discards the special SCC geometry and would subtract approximately `pi/4` at `L/D=1`.

---

## 5. Actual-perimeter JC capacity

The joint cavity proof before the Cauchy relaxation gives

\[
E_{out}+Q
\le
 e_{BB}+\min\{h,\operatorname{per}(F)-h\}.
\tag{5.1}
\]

The same isoperimetric summation as JC then gives

\[
\boxed{
G
\le
\frac{(e_{BB}+\min\{h,\operatorname{per}(F)-h\})^2}{4\pi}
+o(D^2).
}
\tag{SAC.14}
\]

The `O(D)` charging error vanishes after division by `D^2`.

Divide by `D^2` and pass to the subsequence. Since

\[
\frac{e_{BB}}D\to t,
\qquad
\frac hD\to y,
\qquad
\frac{\operatorname{per}(F)}D\to p,
\]

SAC.13 and SAC.14 give SAC.4.

At slope one,

\[
0\le t=\lim e_{BB}/D\le\lim L/D=1.
\tag{5.2}
\]

Cauchy's perimeter-diameter inequality gives `p<=pi`. Therefore

\[
\min\{y,p-y\}
\le
\min\{y,\pi-y\}.
\]

Replacing `t` by one and `p` by `pi` only enlarges the right side, so every survivor satisfies SAC.5.

---

## 6. Solve the scalar feasibility window

### Lower half: `y<=pi/2`

Then

\[
\min\{y,\pi-y\}=y,
\]

and SAC.5 becomes

\[
\frac12\sin y
\le
\frac{(1+y)^2}{4\pi}.
\tag{6.1}
\]

Define

\[
f(y):=\frac12\sin y-\frac{(1+y)^2}{4\pi}.
\]

At `y=2rho`,

\[
f(2rho)>0,
\]

while `f(pi/2)<0`.

Moreover

\[
f'(y)=\frac12\cos y-\frac{1+y}{2\pi}.
\]

On `[2rho,pi/2]`, `cos y` is decreasing. At the left endpoint `rho=cos rho` and elementary numerical enclosure gives `f' <0`; alternatively one may use `2rho>1.47` and `cos(1.47)<0.102` to get the same strict sign. Thus there is a unique root `y_-` and feasibility requires

\[
y\ge y_-.
\]

The root is characterized exactly by SAC.6; SAC.8 is only its decimal evaluation.

### Upper half: `y>=pi/2`

Now

\[
A_{PI}(y)=\frac12,
\qquad
\min\{y,\pi-y\}=\pi-y.
\]

SAC.5 becomes

\[
\frac12
\le
\frac{(1+\pi-y)^2}{4\pi}.
\]

All quantities are nonnegative, so this is equivalent to

\[
1+\pi-y\ge\sqrt{2\pi},
\]

or

\[
\boxed{y\le1+\pi-\sqrt{2\pi}=y_+.}
\]

This proves SAC.10.

---

## 7. Consequences for the SOC visible skeleton

Because `h=q-o(D)`, SAC gives

\[
\boxed{
q/D\in[y_-,y_+]+o(1).
}
\tag{7.1}
\]

SOC then sharpens its two linear lower bounds from `2rho-1` to `y_--1`:

\[
\boxed{
x_B\ge(y_--1)D+2s_C-o(D),}
\tag{SAC.15}
\]

and

\[
\boxed{N_1\ge(y_--1)D+s_C-o(D),}
\tag{SAC.16}
\]

where `N_1` is the number of singleton harmonic components.

Numerically,

\[
\boxed{y_--1=0.503816367367697\ldots .}
\tag{SAC.17}
\]

Thus more than half a diameter's worth of both outer-walk excess and singleton-component count is mandatory at the slope-one endpoint.

---

## 8. External-population split

The existing OP/ER bound

\[
Z_{ext}
\ge
n-\frac{2h^2}{\pi\sqrt3}-h-O(1)
\]

shows that whenever a slope-one subsequence has

\[
y<\pi/2,
\]

it necessarily contains a positive quadratic population outside the force hull:

\[
\liminf\frac{Z_{ext}}{D^2}
\ge
\frac\pi{2\sqrt3}
-
\frac{2y^2}{\pi\sqrt3}
>0.
\tag{SAC.18}
\]

At the lower endpoint `y=y_-`, the coefficient is approximately `0.07569`.

For `y>=pi/2`, this particular external-population estimate becomes nonpositive and gives no information. SAC therefore reduces the global SCC remainder to a useful two-subphase split:

1. `y<pi/2`: a quantitatively quadratic **external** force-hull population is mandatory;
2. `pi/2<=y<=y_+`: the diameter support itself is dense enough that the OP/ER external lower bound no longer closes, and one must instead exploit the near-maximal diameter support / singleton cloud.

---

## 9. Regression audit

- SAC.2 uses the **slope-one SCC strip theorem**. It is false as a generic post-ZF statement.
- The singleton count is only `O(D)`, so constant area per singleton is harmless and is treated honestly.
- The `o(D)` total graph diameter of the remaining nonsingletons is essential; `o(D)` component count alone would not control their total attachment area.
- SAC.4 uses the actual-perimeter form of JC before the `per(F)<=pi D` relaxation.
- The final window SAC.10 intentionally weakens `t` to one and `p` to `pi`. It is therefore a necessary condition, not an equality classification.
- No claim is made that all invisible points lie outside `F`.
- The lower root is below `pi/2`; the upper bound is above `pi/2`, so both branches remain genuinely possible.

---

## 10. Next target

The slope-one phase is now confined to

\[
1.50381636\ldots\le h/D=q/D+o(1)\le1.63496438\ldots,
\]

with

\[
N_1\ge0.50381636\ldots D+s_C-o(D),
\]

and one diameter-spanning `o(D)`-width giant cell.

The next target should retain the variables discarded in SAC.5 instead of immediately taking `t=1`, `p=pi`. Near the lower endpoint, equality forces simultaneously

- `s_C=o(D)` and hence `t->1`;
- `p->2y` rather than merely `p<=pi`;
- `Q+2(d_H+s_Z)=o(D)`;
- almost every singleton is an exact three-contact tripod.

That is a much more rigid combinatorial/geometric endpoint. Proving the corresponding stability statement and combining it with the noncrossing tripod cloud is the shortest next attack.

## 11. Compact handoff

```text
SAC at RCC slope one.
SCC: one giant harmonic component lies in an o(D)-width strip; all other component
graph diameters sum to o(D). SOC: c_I=O(D), and all but o(D) non-giant components
are singletons.

Every attachment terminal of the giant lies within 1 of its strip, so giant attachment
area=o(D^2). Singleton cells have diam(A_r)<=2 and there are O(D), hence total O(D)
area. Remaining nonsingleton cells satisfy sum delta_r=o(D), so their total
isodiametric area is o(D^2). Therefore
    sum_r area(conv A_r)=o(D^2),
    G=area(F)-o(D^2).

Let y=h/D, p=per(F)/D, t=e_BB/D. PI + actual-perimeter JC give
    A_PI(y) <= (t+min(y,p-y))^2/(4pi).
At slope one t<=1 and p<=pi, hence
    A_PI(y) <= (1+min(y,pi-y))^2/(4pi).
Solving gives
    y_- <= y <= y_+,
    y_-=1.503816367367697...,
    y_+=1+pi-sqrt(2pi)=1.634964378958793....
Since q-h=o(D), same window holds for q/D.
Then SOC improves to
    x_B >= (y_--1)D+2s_C-o(D),
    N_singleton >= (y_--1)D+s_C-o(D),
with y_--1=0.503816367367697....
```
