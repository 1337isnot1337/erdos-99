# Target C-II — modern train slack forces a high-`t` pentagon sea

**Date:** 2026-09-15  
**Status:** proof-only full-core structural strengthening  
**Scope:** canonical full-core/no-macroscopic-container Type-II branch  
**Dependencies:** modern scope-safe train-slack floor `tau_D/D>=rho+0.007707-o(1)`; canonical Sections 63/67/85; triangle-free contact embedding  
**Certificate:** `research/verify_target_c_high_t_pentagon_sea.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The modern all-train theorem and the newly closed low-`t` branch force a large
train-boundary slack in every remaining full-core survivor:

\[
\boxed{
\liminf {\tau_D\over D}
\ge\rho+0.007707
=0.7467921332\ldots,
}
\tag{PS.1}
\]

where `rho=cos rho` is the Dottie number.  In a bounded high-`t` window, the exact
post-endpoint ledger then has very little room for high-degree exceptional faces or
outer-walk detour.  The remaining nonquadrilateral faces must therefore contain a
linear population of actual pentagons.

Let `f_5` denote the number of bounded contact faces of degree exactly five.  Then the
following safe staircase holds:

\[
\boxed{
\begin{array}{c|c}
\text{full-core window} & \liminf f_5/D\\ \hline
 t\le1.850 & \ge0.243\\
 t\le1.855 & \ge0.228\\
 t\le1.860 & \ge0.213
\end{array}}
\tag{PS.2}
\]

The live band `1.844<t<=1.855` from the high-`t` low-energy O--O path theorem thus
contains at least

\[
\boxed{0.228D-o(D)}
\tag{PS.3}

bounded pentagonal faces.  The wider dominant O--O band through `t<=1.860` still
contains at least `0.213D-o(D)` pentagons.

---

## 1. Face-degree currency

The contact graph is triangle-free: a 3-cycle of unit contacts would be a unit
equilateral triangle, excluded in Target C-II.  Therefore every bounded face has degree
at least four.

Let

\[
f:=\#\{\text{bounded nonquadrilateral contact faces}\}
\]

and retain the canonical degree defect

\[
Q:=\sum_P(\deg P-4),
\tag{PS.4}
\]

where the sum is over bounded nonquadrilateral faces.  Then

\[
Q-f
=\sum_P(\deg P-5).
\tag{PS.5}
\]

Every face of degree at least six contributes at least one to the right side.  Hence,
if `f_{>=6}` is the number of bounded faces of degree at least six,

\[
f_{\ge6}\le Q-f.
\tag{PS.6}
\]

Since

\[
f=f_5+f_{\ge6},
\]

we obtain the finite inequality

\[
\boxed{
f_5\ge f-(Q-f).
}
\tag{PS.7}
\]

Thus it suffices to force many nonquadrilateral faces while keeping the degree-above-
five currency small.

---

## 2. Train slack forces many nonquadrilateral faces when `t` is bounded above

Put

\[
U:=q-k=tD.
\]

The canonical train-boundary slack is

\[
\tau_D=U+2f-2\sqrt{R_4}.
\tag{PS.8}
\]

Therefore exactly

\[
\boxed{
2f=\tau_D-U+2\sqrt{R_4}.
}
\tag{PS.9}
\]

Assume a full-core survivor sequence lies in a fixed window

\[
t\le T.
\tag{PS.10}
\]

Using (PS.1) and the canonical Type-II limit

\[
{\sqrt{R_4}\over D}\to\sqrt{\Delta_2},
\qquad
\Delta_2={\pi\over2\sqrt3},
\tag{PS.11}
\]

we obtain

\[
\boxed{
\liminf {f\over D}
\ge
{\rho+0.007707-T+2\sqrt{\Delta_2}\over2}.
}
\tag{PS.12}

At `T=1.855` this is approximately `0.39820887`.  Thus the live high-`t` band already
contains almost `0.4D` nonquadrilateral bounded faces.

---

## 3. The same ledger caps all non-pentagonal defect plus outer detour

Define

\[
X_D:=(Q-f)+(b-p).
\tag{PS.13}
\]

Both summands are nonnegative.  The exact post-endpoint decomposition is

\[
U
={2p+2\sqrt{R_4}\over5}
+{2\over5}(Q-f)
+{2\over5}(b-p)
+{1\over5}\tau_D.
\tag{PS.14}
\]

Solving for `X_D` gives

\[
\boxed{
X_D
={5\over2}U-p-\sqrt{R_4}-{1\over2}\tau_D.
}
\tag{PS.15}
\]

Use `t<=T`, the lower train-slack floor (PS.1), and the canonical limits

\[
{p\over D}\to\pi,
\qquad
{\sqrt{R_4}\over D}\to\sqrt{\Delta_2}.
\]

Then

\[
\boxed{
\limsup {X_D\over D}
\le
{5T\over2}
-\pi
-\sqrt{\Delta_2}
-{\rho+0.007707\over2}.
}
\tag{PS.16}

At `T=1.855` the right side is about `0.17019847`.  Thus all degree-six-and-higher
excess together with all metric outer-walk detour costs less than `0.171D` asymptotically.

---

## 4. Subtract the high-degree budget from the nonquadrilateral population

Because `b-p>=0`,

\[
Q-f\le X_D.
\tag{PS.17}
\]

Combining (PS.7), (PS.12), and (PS.16) gives

\[
\begin{aligned}
\liminf {f_5\over D}
&\ge
{\rho+0.007707-T+2\sqrt{\Delta_2}\over2}\\
&\quad-\left[
{5T\over2}
-\pi
-\sqrt{\Delta_2}
-{\rho+0.007707\over2}
\right]\\
&=
\boxed{
\rho+0.007707-3T+\pi+2\sqrt{\Delta_2}.
}
\end{aligned}
\tag{PS.18}
\]

The cancellation is useful: the pentagon floor depends on only one modern train
constant and the near-disk limits.

The exact companion certificate proves

\[
\begin{array}{rcl}
T=1.850&:& f_5/D>0.2430103\ldots,\\
T=1.855&:& f_5/D>0.2280103\ldots,\\
T=1.860&:& f_5/D>0.2130103\ldots,
\end{array}
\]

with more than `10^-5` margin above the rounded coefficients in (PS.2).

---

## 5. Structural meaning in the live high-`t` path

The current high-`t` low-energy path theorem applies on

\[
1.844<t\le1.855
\]

and produces more than `0.0184D-o(D)` pairwise noncrossing O--O cuts on one exact
dual path, with a common diameter-routing hub.  The hub theorem then makes a live
count-optimal adjacent strip one-sided.

Equation (PS.3) adds an independent global feature to the same survivor:

```text
>0.0184 D low-energy O--O cuts on one dual path
+ one-sided diameter switching away from the hub
+ <=341 moving diameters on one live strip
+ exact layer reaction generated by <=2 of those bars
+ at least 0.228 D bounded pentagons globally.
```

The pentagons are not yet localized to the selected strip.  A closure step must avoid
the unsupported inference that a global pentagon count automatically places pentagons
next to the low-energy path.

The natural next target is an incidence/shoulder theorem: charge pentagonal corners to
selected O--O path layers or prove that avoiding the path consumes too much outer-walk,
train-boundary, or angular-defect currency.  This is the same type of finite occupancy
bridge that was useful in the former low-`t` pentagon-sea branch, but the present
constants are derived from the modern high-`t` train slack instead.

---

## 6. Scope and non-implications

- The theorem is full-core Type-II only.
- It is conditional on the stated upper endpoint `t<=T`; it does not give a global
  pentagon floor for arbitrarily large `t`.
- `b` is the canonical occurrence-counted outer contact-face walk.
- `Q` is the global bounded-face degree defect, with no local induced-cell substitution.
- A pentagonal face here is a bounded contact face of degree five; no convexity or
  regularity is assumed.
- The theorem does not place these faces beside the high-`t` O--O path and does not
  yield a source-level deformation by itself.

**Disposition:** proved proof-only modern high-`t` pentagon-face staircase.  C-II and
Level I remain open.
