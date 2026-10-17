> Generated reading edition · [exact source](../../../docs/reports/target_c_pi_detour_feedback_surplus_04694_2026-09-09.md) · source SHA-256 `5570c92b262696b7449644c17ecdf6ba27135e185d55bd0df27a9965fa166718`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-D550830701C8","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — PI/detour feedback raises the explicit pinned/contact floor to 0.4694

**Date:** 2026-09-09  
**Repository base:** current PR #138 branch after ED  
**Run type:** finite bootstrap / explicit asymptotic branch exclusion  
**Target:** Target C C-II after PI/JC/PC/WD/ED  
**LEVEL I STATUS:** STILL OPEN

ED proved

$$
\liminf\frac{e_{BB}+2s_C}{D}\ge0.4673
$$

using PI only through its universal force-hull area constant

$$
A_{PI}=\frac12\sin(2\rho)=0.4978566363\ldots .
$$

But PI contains more information.  If

$$
y:=h/D,
$$

then its projective-circle argument gives the asymptotic area floor

$$
\boxed{
\frac{area(F)}{D^2}
\ge
\frac12\sin\bigl(\min\{y,\pi/2\}\bigr)-o(1).
}
\tag{PF.1}
$$

The JC/WD detour budget simultaneously forces `y` into a narrow interval around `pi/2`.  Therefore PF.1 improves toward the maximal two-diameter-chord value `1/2`.  Feeding that improvement back into JC shrinks the allowed interval again.

Two explicit feedback steps already give

$$
\boxed{
\liminf_{D\to\infty}
\frac{e_{BB}+2s_C}{D}
\ge0.4694.
}
\tag{PF.2}
$$

No limiting fixed-point claim is needed.

---

## 1. Diameter-density form of PI

PI proves that among `h` actual diameter directions there are two at projective angle at least

$$
\min\left\{(h-1)\delta_D,\frac\pi2-\delta_D\right\},
\qquad
\delta_D=2\arcsin\frac1{2D}.
\tag{PF.3}
$$

Two diameter chords at projective angle `phi` span area

$$
\frac{D^2}{2}\sin\phi
$$

inside the force hull.

If `h/D->y`, then

$$
(h-1)\delta_D\to y,
\qquad
\frac\pi2-\delta_D\to\frac\pi2.
$$

Hence PF.1 follows directly.

In particular, if

$$
\left|y-\frac\pi2\right|\le R
\tag{PF.4}
$$

with `0<=R<pi/2`, then

$$
\boxed{
\liminf\frac{area(F)}{D^2}
\ge\frac12\cos R.
}
\tag{PF.5}
$$

Indeed the smallest value of `sin(min{y,pi/2})` on the interval in PF.4 occurs at `y=pi/2-R`.

---

## 2. Any JC budget also gives a two-sided bound on `y-pi/2`

Retain ED's notation

$$
z:=y-\frac\pi2,
\qquad
\varepsilon:=\pi-p\ge0,
$$

where `p=per(F)/D`.

Suppose a lower attachment-gap estimate gives

$$
\liminf\frac G{D^2}\ge L>0.
$$

The exact JC/PC pocket/face upper bound then gives

$$
z+\varepsilon+r+3d+2s+c
\le
\lambda+\frac\pi2-2\sqrt{\pi L},
\tag{PF.6}
$$

where

$$
r=\lambda-t\ge0,
\quad d=d_H/D\ge0,
\quad s=s_Z/D\ge0,
\quad c=c_B/D\ge0.
$$

Write the right side as `R` and assume `R>=0` (otherwise there is already a contradiction).  Dropping nonnegative terms gives

$$
z+\varepsilon\le R.
\tag{PF.7}
$$

On the other hand the chain-chord detour is nonnegative:

$$
\frac{U_{det}}D
=2z+\varepsilon-\nu-2s
\ge0,
\qquad \nu:=Q/D\ge0.
\tag{PF.8}
$$

Hence

$$
2z+\varepsilon\ge0.
\tag{PF.9}
$$

If `z>=0`, PF.7 gives `z<=R`.  If `z<0`, PF.9 gives `epsilon>=-2z`, so

$$
z+\varepsilon\ge-z.
$$

Together with PF.7 this gives `-z<=R`. Thus:

### Lemma PF.1 — JC/detour density localization

Every such survivor satisfies

$$
\boxed{
\left|\frac hD-\frac\pi2\right|
=|z|
\le R.
}
\tag{PF.10}
$$

This is the feedback bridge from cavity capacity back to PI.

---

## 3. Define the finite bootstrap

Fix a candidate `lambda` and define the initial universal PI gap floor

$$
\boxed{
L_0(\lambda)
:=A_{PI}-\frac\pi4\lambda^2,
\qquad
A_{PI}=\frac12\sin(2\rho).
}
\tag{PF.11}
$$

Define

$$
\boxed{
R_0(\lambda)
:=
\lambda+\frac\pi2
-2\sqrt{\pi L_0(\lambda)}.
}
\tag{PF.12}
$$

If `R_0<0`, the JC inequality is impossible. Otherwise PF.10 gives

$$
|y-\pi/2|\le R_0.
$$

Use PF.5 to improve the force-hull area floor, and define

$$
\boxed{
L_1(\lambda)
:=
\frac12\cos R_0(\lambda)
-\frac\pi4\lambda^2.
}
\tag{PF.13}
$$

Then define the new JC budget

$$
\boxed{
R_1(\lambda)
:=
\lambda+\frac\pi2
-2\sqrt{\pi L_1(\lambda)}.
}
\tag{PF.14}
$$

Apply PF.10 again:

$$
|y-\pi/2|\le R_1.
$$

One more PI feedback gives

$$
\boxed{
L_2(\lambda)
:=
\frac12\cos R_1(\lambda)
-\frac\pi4\lambda^2,
}
\tag{PF.15}
$$

and the corresponding final budget

$$
\boxed{
R_2(\lambda)
:=
\lambda+\frac\pi2
-2\sqrt{\pi L_2(\lambda)}.
}
\tag{PF.16}

No limit is taken in this recursion.  PF.11-PF.16 are just two finite applications of already-proved implications.

---

## 4. Use the final budget in the exact WD/PC cavity bound

ED's exact-defect argument applies with **any** valid JC budget `R`.  Therefore, with `R=R_2(lambda)`, it gives

\[
\frac{L_{chain}}D
\le
\pi+2R_2-\lambda-\nu,
\tag{PF.17}
$$

$$
\frac{U_{det}}D
\le
2R_2-\nu,
\qquad
0\le\nu\le2R_2.
\tag{PF.18}
$$

WD and the CC exceptional-face estimate then give

$$
\limsup\frac{H_{out}+A_{exc}}{D^2}
\le
F_{\lambda,R_2}(\nu),
\tag{PF.19}
$$

where

$$
F_{\lambda,R}(\nu)
=
\frac{\sqrt2}{\pi}
(\pi+2R-\lambda-\nu)^{3/2}
(2R-\nu)^{1/2}
+
\frac{\nu^2}{4\pi}.
\tag{PF.20}
$$

Exactly as in ED, this function is strictly decreasing in `nu` throughout the range needed below.  For completeness, at `lambda<=0.4694` the monotonicity of the bootstrap gives

$$
R_2\le R_2(0.4694)
=0.0133820546\ldots,
$$

so `2R_2<0.027`.  The derivative bound

$$
F'(\nu)
\le
-
\frac{\sqrt2}{2\pi}
\frac{(\pi-\lambda)^{3/2}}{\sqrt{2R_2}}
+
\frac{2R_2}{2\pi}
$$

is then less than `-6+0.005<0`. Hence the maximum occurs at `nu=0`.

Thus every survivor with `lambda<=0.4694` must satisfy

$$
\boxed{
L_2(\lambda)
\le
V_2(\lambda)
:=
\frac{\sqrt2}{\pi}
(\pi+2R_2(\lambda)-\lambda)^{3/2}
\sqrt{2R_2(\lambda)}.
}
\tag{PF.21}
$$

---

## 5. Monotonic endpoint reduction

On the interval relevant here all `R_j` lie in `(0,0.02)`.

- `L_0(lambda)` is strictly decreasing.
- Therefore `R_0(lambda)` is strictly increasing.
- Since cosine decreases on this interval, `L_1(lambda)` is strictly decreasing.
- Hence `R_1(lambda)` is strictly increasing.
- Then `L_2(lambda)` is strictly decreasing and `R_2(lambda)` is strictly increasing.

More explicitly, whenever `L_j'<0`,

$$
R_j'
=1-
\frac{\pi L_j'}{\sqrt{\pi L_j}}
>1.
\tag{PF.22}
$$

Therefore

$$
\frac d{d\lambda}(\pi+2R_2-\lambda)
=2R_2'-1>0,
$$

and `V_2(lambda)` is strictly increasing.

Thus it is enough to test PF.21 at the endpoint `lambda=0.4694`.

---

## 6. Explicit endpoint calculation

Take

$$
\boxed{\lambda_*=0.4694.}
$$

Using `rho=0.7390851332151606...`, the finite bootstrap gives

$$
\boxed{
L_0=0.32480486385053203\ldots,
\qquad
R_0=0.01989479076314416\ldots,
}
\tag{PF.23}
$$

$$
\boxed{
L_1=0.32684928011514597\ldots,
\qquad
R_1=0.01354658178136292\ldots,
}
\tag{PF.24}
$$

$$
\boxed{
L_2=0.32690235075840770\ldots,
\qquad
R_2=0.01338205451058361\ldots .
}
\tag{PF.25}

The WD/PC upper side of PF.21 is

\[
\boxed{
V_2(\lambda_*)
=0.32653926514946385\ldots .
}
\tag{PF.26}

Therefore

\[
\boxed{
L_2(\lambda_*)-V_2(\lambda_*)
=0.00036308560894383\ldots>0.
}
\tag{PF.27}

This contradicts the necessary condition PF.21.  By Section 5, every smaller `lambda` is excluded as well.  This proves PF.2.

The final numerical margin is over `3.6e-4`, still many orders of magnitude above the displayed decimal precision.

---

## 7. Interpretation

The feedback has a clear geometric meaning.

1. A low pinned/contact currency forces a large PI/GU attachment-cell gap.
2. JC says a large gap can be carried only if `h/D` and `per(F)/D` are close to the old equality geometry.
3. WD says the outer-pocket part additionally needs chain–chord detour.
4. Those two requirements force `h/D` close to `pi/2` from **both** sides.
5. But PI becomes strongest near `h/D=pi/2`: two actual diameter chords are then forced asymptotically orthogonal, giving force-hull area close to `D^2/2`.
6. The larger area floor restarts the loop with less available cavity budget.

This is a genuine positive-feedback mechanism between diameter-direction geometry and source-capacity geometry.

---

## 8. Further finite iterations

One may continue the recursion

\[
L_{j+1}(\lambda)
=
\frac12\cos R_j(\lambda)
-
\frac\pi4\lambda^2,
$$

$$
R_{j+1}(\lambda)
=
\lambda+\frac\pi2
-2\sqrt{\pi L_{j+1}(\lambda)}.
$$

Numerically the improvement after two steps is already nearly saturated.  No asymptotic fixed-point value is asserted here; doing so would require a separate convergence/uniqueness audit.  The finite two-step proof above is sufficient for the clean explicit constant `0.4694`.

---

## 9. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| density-sensitive PI floor PF.1 | proved | PI finite angle formula + limit |
| JC/detour two-sided localization PF.10 | proved | JC upper + nonnegative chain detour |
| finite bootstrap PF.11-PF.16 | proved | two repeated applications of PI + JC |
| final WD/PC capacity PF.21 | proved | ED exact-defect argument with `R_2` |
| monotonic endpoint reduction | proved | induction using `L_j'<0`, `R_j'>1` |
| explicit floor `0.4694` | proved asymptotically | endpoint margin PF.27 |
| infinite fixed-point limit | not claimed | unnecessary for finite result |
| Level I | still open | high-surplus global structure remains |

---

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

PI in diameter-density form:
    area(F)/D^2 >= (1/2) sin(min{h/D,pi/2})-o(1).
Any JC budget R plus nonnegative chain detour gives
    |h/D-pi/2| <= R.
Therefore PI upgrades to
    area(F)/D^2 >= (1/2)cos R-o(1).

For candidate lambda define
    L0=A_PI-(pi/4)lambda^2,
    R0=lambda+pi/2-2sqrt(pi L0),
    L1=(1/2)cos R0-(pi/4)lambda^2,
    R1=lambda+pi/2-2sqrt(pi L1),
    L2=(1/2)cos R1-(pi/4)lambda^2,
    R2=lambda+pi/2-2sqrt(pi L2).
Exact PC/WD then requires
    L2 <= (sqrt2/pi)(pi+2R2-lambda)^(3/2)sqrt(2R2)
for lambda<=0.4694.

At lambda=0.4694:
    L0=0.32480486385053203, R0=0.01989479076314416,
    L1=0.32684928011514597, R1=0.01354658178136292,
    L2=0.32690235075840770, R2=0.01338205451058361,
    RHS=0.32653926514946385,
    margin=0.00036308560894383>0.
Hence
    liminf (e_BB+2s_C)/D >= 0.4694.
```
