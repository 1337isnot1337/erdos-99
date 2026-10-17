# Target C-II — retained `g=0.0077` endpoint margin forces residual slack and raises the floor to `1.843578`

**Date:** 2026-09-15  
**Status:** proof-only downstream strengthening  
**Scope:** full-core Type-II branch  
**Dependencies:** corrected uniform strong-branch orbit capacity at `g=0.0077`; residual-stability theorem at `1.843577`; hostile-audited shared endpoint retention and complement-rhombus incidence  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The current residual-stability theorem proves

\[
\liminf {q-k\over D}\ge1.843577
\]

but deliberately discards the positive one-orbit capacity deficit at the matched
atomic endpoint

\[
C_{77}=2\sqrt{\Delta_2}+0.0077,
\qquad
\Delta_2={\pi\over2\sqrt3}.
\]

That loss is visible at the theorem's weakest scalar corner.  There the residual
parameter is set to `h=0`; residual stability would then force the dominant exact
`pi/3` orbit to have mass exactly `C77` with no residual orbit mass.  But the exact
`g=.0077` capacity certificate proves that one orbit of mass `C77` falls short of the
required crossing density by more than `6.6e-6`.

Retaining this endpoint deficit forces a small but strictly positive residual slack

\[
\boxed{h>5.49\times10^{-6}.}
\]

Putting that mandatory slack back into the already-audited survivor function gives

\[
\boxed{
\liminf_{D\to\infty}{q-k\over D}\ge1.843578.
}
\]

The gain is numerically small, but it removes a false equality corner rather than
retuning an existing decimal coefficient.

---

## 1. Parent residual variables

Use the parent notation

\[
t={q-k\over D},
\qquad
\kappa={k\over D},
\qquad
\delta={d_{out}\over D},
\]

\[
U={9t\over2}-2\pi-2\delta-\kappa/2,
\]

and let `M` be the mass of a dominant exact projective `pi/3` orbit.  Put

\[
h:=U-C_{77},
\qquad
R:=U-M.
\]

The `g=.0077` residual-stability theorem proves, throughout the live interval
`C77<=U<=2.013`,

\[
\boxed{0\le R\le c h,
\qquad c=1.05.}
\tag{EM.1}

Let `Psi(W)` denote the maximum of the three scope-correct one-orbit capacity branches:

1. the strong `1/10` physical pair-deficit branch;
2. the `2/29` fallback branch while the center mass is at most `K=2/sqrt3`;
3. the generic high-center branch.

The exact `g=.0077` certificate gives

\[
\boxed{
\Delta_2-\Psi(C_{77})>6.6\times10^{-6}.
}
\tag{EM.2}

The strong branch controls this minimum margin; the fallback and high-center endpoint
margins are much larger.

---

## 2. A coarse upper Lipschitz bound for the one-orbit capacity

The endpoint deficit can be spent only after controlling how fast `Psi(W)` may grow
for `W>C77`.  A deliberately coarse bound is sufficient.

For the strong and fallback branches write

\[
\Phi_\alpha(W,C)
=C(W-C)
-\alpha {3C-W\over C}
\left({W+C\over2}-K\right)^2,
\]

where `alpha=1/10` or `2/29`.  Put

\[
e={W+C\over2}-K,
\qquad
q=3-{W\over C}.
\]

Then

\[
\Phi_{\alpha,W}
=C+\alpha{e^2\over C}-\alpha q e.
\tag{EM.3}

### Strong branch

At its unique optimizer `C_*(W) in (W/3,W/2)`, the envelope theorem gives

\[
\Psi_s'(W)=\Phi_{1/10,W}(W,C_*(W)).
\]

The exact verifier bounds this by

\[
\boxed{\Psi_s'(W)<1.04}
\tag{EM.4}
\]

for `C77<=W<=2.013`.

### Fallback branch

The fallback is evaluated at the moving strong/fallback boundary

\[
C_s(W)=W-{W-K\over r_*},
\qquad
r_*:=\sqrt{20/29},
\]

so

\[
B_0'(W)
=\Phi_{2/29,W}(W,C_s(W))
+\Phi_{2/29,C}(W,C_s(W))C_s'(W).
\tag{EM.5}

Here both `Phi_C` and `C_s'` are negative.  The moving-boundary term is therefore
positive and cannot be omitted.  Bounding it explicitly, the exact verifier gives

\[
\boxed{B_0'(W)<1.04.}
\tag{EM.6}

### High-center branch

The generic branch is

\[
B_H(W)=K(W-K),
\]

hence

\[
\boxed{B_H'(W)=K={2\over\sqrt3}<1.16.}
\tag{EM.7}

Therefore the maximum of the three branch capacities is Lipschitz on the whole live
interval with the safe constant

\[
\boxed{
\Psi(W_2)-\Psi(W_1)
\le {6\over5}(W_2-W_1)
\quad(C_{77}\le W_1\le W_2\le2.013).
}
\tag{EM.8}

The certificate actually finds branch derivative upper bounds approximately
`1.02628`, `1.03570`, and `1.15471`; `6/5` is intentionally loose.

---

## 3. The endpoint deficit forces `h>5.49e-6`

The exact orbit decomposition gives

\[
\Delta_2
\le \Psi(M)+{R^2\over4}.
\tag{EM.9}

Set

\[
h_0={549\over10^8}=5.49\times10^{-6}.
\]

Assume `h<=h0`.

### Case 1: `M>=C77`

Since

\[
M-C_{77}
=(U-R)-C_{77}
=h-R
\le h,
\]

(EM.8), (EM.1), and (EM.9) give

\[
\begin{aligned}
\Delta_2-\Psi(C_{77})
&\le \Psi(M)-\Psi(C_{77})+{R^2\over4}\\
&\le {6\over5}h+{c^2h^2\over4}\\
&\le {6\over5}h_0+{c^2h_0^2\over4}.
\end{aligned}
\]

The exact rational certificate checks

\[
{6\over5}h_0+{1.05^2h_0^2\over4}
<6.589\times10^{-6}
<6.6\times10^{-6},
\]

contradicting (EM.2).

### Case 2: `M<C77`

The already-proved lower-side capacity monotonicity gives

\[
\Psi(M)<\Psi(C_{77})
\]

on the only localization interval needed by residual stability.  Thus (EM.9) yields

\[
\Delta_2-\Psi(C_{77})
<{R^2\over4}
\le {c^2h_0^2\over4},
\]

which is far smaller than `6.6e-6`, again contradicting (EM.2).

Therefore every survivor satisfies

\[
\boxed{h>h_0=5.49\times10^{-6}.}
\tag{EM.10}

---

## 4. Reinsert the mandatory slack into the survivor system

Put

\[
x={\kappa\over2},
\qquad c=1.05.
\]

The parent residual theorem gives

\[
2\delta+x+h
=R_t:={9t\over2}-2\pi-C_{77},
\tag{EM.11}

and survivor capacity

\[
Q(t,h,x)
=F^{-1}(\delta)
+{c^2h^2\over2(1-\delta)}
-\left(\pi-{t\over2}-x-ch\right),
\tag{EM.12}

where

\[
F(z)=z-6\sin(z/6),
\qquad
\delta={R_t-x-h\over2}.
\]

Survival requires

\[
Q(t,h,x)\ge0.
\tag{EM.13}

At `t<=1.843578`, the exact certificate checks

\[
U<2.013,
\qquad
\delta<0.051,
\qquad
h<0.101.
\]

The parent derivative estimates therefore continue to hold, with the explicit safe
bounds

\[
\boxed{Q_x<-2.7,}
\qquad
\boxed{Q_h<-2.5.}
\tag{EM.14}

Also `Q_t>0` directly from (EM.12), since `partial_t delta=9/4` and every displayed
`t`-dependent contribution has positive derivative.

Consequently, for fixed `t`, survivor capacity is maximized at the smallest allowed
`x` and `h`.  By (EM.10), it is enough to test the limiting corner

\[
\boxed{x=0,\qquad h=h_0.}
\tag{EM.15}

---

## 5. Exact corner certificate at `1.843578`

At (EM.15), define

\[
\delta_h(t)
={1\over2}
\left({9t\over2}-2\pi-C_{77}-h_0\right),
\tag{EM.16}

\[
r_h(t)
={c^2h_0^2\over2(1-\delta_h(t))},
\tag{EM.17}

and

\[
Z_h(t)
=\pi-{t\over2}-ch_0-r_h(t).
\tag{EM.18}

Because `F` is increasing on the relevant interval, `Q(t,h0,0)<0` is equivalent to

\[
\boxed{F(Z_h(t))>\delta_h(t).}
\tag{EM.19}

The exact verifier

`research/verify_target_c_endpoint_margin_residual_slack_floor_1843578.py`

uses rational Machin bounds for `pi`, integer-square-root enclosures for every radical,
and alternating-series enclosures for `sin`.  At

\[
t=1.843578
\]

it proves

\[
\boxed{
F(Z_h)-\delta_h
>1.3\times10^{-6}.
}
\tag{EM.20}

Since `Q_t>0`, every smaller `t` is excluded as well.  Therefore

\[
\boxed{
\liminf_{D\to\infty}{q-k\over D}
\ge1.843578.
}
\tag{EM.21}

For orientation only, the relaxed scalar equation with `h=h0` has a numerical root
near

\[
1.84357863.
\]

The same exact verifier confirms that this relaxation no longer excludes
`t=1.843579`, so no stronger rounded claim is made.

---

## 6. Frontier effect

The previous `1.843577` endpoint was attained only after erasing a positive atomic
capacity margin and then allowing `h=0`.  Those two operations are incompatible.
The present theorem restores that compatibility constraint and removes the equality
corner.

The numerical gain is only `10^-6` in `t`; further tuning of this endpoint margin is
therefore low-value.  The structurally stronger current object remains the independently
proved `t<=1.844` complete train rectangle:

```text
>0.003D ordered smallest-leaf outer-to-outer cuts on one dual-tree backbone
x
>0.35D common exact-center crossing trains
+
two-sided actual-diameter KKT bracing on every leaf cut.
```

A source-level closure should exploit reuse/correlation of those actual diameter
braces across consecutive backbone strips rather than pursue another sixth decimal.

**Disposition:** proved proof-only residual endpoint strengthening. C-II and Level I remain open.
