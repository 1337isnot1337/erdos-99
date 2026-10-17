> Generated reading edition · [exact source](../../research/target_c_free_terminal_live_detour_pinching_2026-09-18.md) · source SHA-256 `713904d23f4651b32e7c34d6f5b67c966f0d3ce1dab5da3d80fb1c96c54fd243`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

# Target C-II — the live `0.00710` window is universally pinned to near-maximal outer detour

**Date:** 2026-09-18  
**Status:** proof-only terminal strengthening; theorem-state authority unchanged  
**Scope:** terminal full-core Type-II FREE subsequences with `pi D-q=o(D)` and `limsup t_D <= mu_*+0.00710`  
**Depends on:** correlated exact-`t` identity; hostile-audited two-bin theorem; shared routewise retention; complement train/rhombus incidence; disjoint dominant/complement outer-energy support; activated-endpoint pair-shield flex theorem; one-anchor closure-corank theorem  
**Certificate:** `research/verify_target_c_free_terminal_live_detour_pinching_2026_09_18.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The correlated `0.00704` gap proof reduced every putative terminal FREE survivor to a
one-variable necessary condition

```math
G_\varepsilon(\delta)\le0,
```

where `delta=(b-P_F)/D` is the normalized outer-walk detour defect.  That proof used
`epsilon=0.00704` only at the last scalar step.  At the current live endpoint

```math
\varepsilon_0=0.00710,
```

the same necessary condition remains valid.  It no longer excludes the whole interval,
but it permits only a very short terminal tail next to the maximal stability value.

The exact-rational certificate proves

```math
\boxed{\delta>0.017609.}
\tag{DP.1}
```

Since correlated stability gives

```math
a+2(r+\delta)\le 5\varepsilon_0=0.0355,
```

with

```math
r={Q-f\over D},
\qquad
a={\tau_D\over D}-{\pi\over2}-0.007707,
\qquad a,r,\delta\ge0,
```

( DP.1 ) immediately forces

```math
\boxed{a+2r<0.000282,}
\tag{DP.2}
```

and hence

```math
\boxed{a<0.000282,\qquad r<0.000141.}
\tag{DP.3}
```

Thus more than `99.20%` of the entire available correlated defect budget in the live
window is forced into outer detour.  The earlier live complement/detour dichotomy is
therefore superseded at this endpoint: near-maximal detour and near-pure pentagonal
transport are universal, not merely the small-complement branch.

Combining this with the activated-endpoint pair-shield theorem raises the universal
exact contact-flex floor from `1.1812298040D` to

```math
\boxed{
\liminf {m_D\over D}>1.1988388040.
}
\tag{DP.4}
```

The live diameter-locking theorem then forces the actual diameter derivative system to
have rank at least `(1.1988388040-o(1))D`, a matching to that many distinct actual
diameter bars, and signed derivative-incidence total exceeding

```math
\boxed{(2.3976776080-o(1))D.}
\tag{DP.5}
```

The same pinching sharpens the one-anchor closure-corank endpoint.  The exceptional-face
population lies in the narrow strip

```math
\boxed{
0.76138304549
<\liminf {f\over D}
\le\limsup {f\over D}
<0.76152404550,
}
\tag{DP.6}
```

and

```math
\boxed{
\liminf {P_5\over D}>0.76124204549.
}
\tag{DP.7}
```

Only `(0.000141+o(1))D` bounded exceptional faces can be superpentagonal.  If

```math
E_U=a_F+{x_A\over2}+{n_0+n_2\over2}
```

is the structural excess from the one-anchor corank theorem, then

```math
\boxed{
\limsup {\sigma_C\over D}
<0.15230481+{18\over5}\limsup {E_U\over D}.
}
\tag{DP.8}
```

In particular a sequence approaching the pair-shield counting floor has pure-contact
closure corank below `0.15230481D+o(D)`.

---

## 1. Reuse the correlated feasibility reduction at `epsilon=0.00710`

Put

```math
\Delta_2={\pi\over2\sqrt3},
\qquad
s_2=\sqrt{\Delta_2},
\qquad
g=0.007707,
\qquad
A_0=2s_2+g.
\tag{1.1}
```

For a terminal subsequence in the live window, the exact `t` identity gives

```math
\boxed{
a+2(r+\delta)\le5\varepsilon_0,
\qquad
\varepsilon_0={71\over10000}.
}
\tag{1.2}
```

The hostile-audited two-bin theorem bounds residual exact-orbit train mass by

```math
R\le r_2(A_0+a),
\qquad
r_2(C)={C-\sqrt{8\Delta_2-C^2}\over2}.
\tag{1.3}
```

Since `r_2` is increasing on the live interval, dropping only `r>=0` from (1.2)
gives the correlated residual envelope

```math
\boxed{
R\le\rho(\delta)
:=r_2(A_0+5\varepsilon_0-2\delta),
\qquad
0\le\delta\le\delta_{\max}:={5\varepsilon_0\over2}=0.01775.
}
\tag{1.4}
```

Shared routewise retention supplies dominant outer mass `z` and retained complement
O--O pair mass `p` with

```math
z+p\ge{\pi\over2}-R-o(1).
\tag{1.5}
```

The complement train/rhombus incidence theorem and disjoint directional-energy payment
are

```math
p(1-\delta)-{e_c\over2}
\le {R^2\over2}+o(1),
\tag{1.6}
```

```math
F(z)+e_c\le\delta,
\qquad
F(z):=z-6\sin(z/6).
\tag{1.7}
```

Exactly as in the correlated `0.00704` proof, eliminate `p,e_c,R` in the weakening
direction.  If `z_\delta` is the unique nonnegative solution of

```math
F(z_\delta)=\delta,
\tag{1.8}
```

then every survivor must satisfy

```math
\boxed{
G(\delta)
:={\pi\over2}
-\rho(\delta)
-z_\delta
-{\rho(\delta)^2\over2(1-\delta)}
\le0.
}
\tag{1.9}
```

No small-complement assumption appears in (1.9).

---

## 2. The live reduced margin is strictly decreasing

Write

```math
C(\delta)=A_0+5\varepsilon_0-2\delta,
\qquad
S(\delta)=\sqrt{8\Delta_2-C(\delta)^2}.
```

Then

```math
-\rho'(\delta)=1+{C(\delta)\over S(\delta)}.
\tag{2.1}
```

For `delta>0`, differentiating (1.8) gives

```math
z_\delta'={1\over1-\cos(z_\delta/6)}.
\tag{2.2}
```

Therefore

```math
G'(\delta)
=(-\rho')\left(1+{\rho\over1-\delta}\right)
-z_\delta'
-{\rho^2\over2(1-\delta)^2}.
\tag{2.3}
```

The exact certificate uses outward Machin and integer-square-root enclosures and proves,
uniformly on `[0,0.01775]`,

```math
\rho<0.044,
\qquad
z_\delta<1.567,
\tag{2.4}
```

```math
(-\rho')\left(1+{\rho\over1-\delta}\right)<2.139,
\tag{2.5}
```

while

```math
z_\delta'
>{72\over1.567^2}
>29.32.
\tag{2.6}
```

The last negative term in (2.3) only strengthens the inequality.  Hence

```math
\boxed{G'(\delta)<0}
\tag{2.7}
```

throughout the live stability interval, with continuity at `delta=0`.

---

## 3. Exact exclusion through `delta=0.017609`

Set

```math
\delta_0={17609\over10^6}=0.017609.
\tag{3.1}
```

The certificate gives the outward residual enclosure

```math
\boxed{
\rho(\delta_0)<0.008006.
}
\tag{3.2}
```

For

```math
z_0=1.562745
```

the alternating Taylor bound

```math
F(z_0)
\ge {z_0^3\over216}-{z_0^5\over155520}
>0.017609
\tag{3.3}
```

shows `z_{delta_0}<z_0`.  Therefore

```math
\begin{aligned}
G(\delta_0)
&>
{\pi\over2}
-0.008006
-1.562745
-{0.008006^2\over2(1-0.017609)}\\
&>1.27\times10^{-5}.
\end{aligned}
\tag{3.4}
```

Because `G` is decreasing, `G(delta)>0` for every `delta<=delta_0`.  This contradicts
the necessary condition (1.9).  Thus every live terminal survivor satisfies

```math
\boxed{\delta>0.017609,}
```

proving (DP.1).

A non-load-bearing numerical solve places the zero of the same reduced function near
`0.01760958397`; the certified cut leaves a visible rational margin and does not rely on
that decimal.

---

## 4. The remaining scalar defects collapse

From (1.2) and (DP.1),

```math
a+2r
<0.0355-2(0.017609)
=0.000282.
\tag{4.1}
```

This proves (DP.2)--(DP.3).  Equivalently, the allowed detour interval has collapsed to

```math
\boxed{
0.017609<\delta\le0.01775,
}
\tag{4.2}
```

whose width is only `0.000141`.

The exact terminal face ledger is

```math
{f\over D}
={M_*+2a-\delta-r\over5}+o(1),
\qquad
M_*=4s_2+2g.
\tag{4.3}
```

For the lower bound, (1.2) gives

```math
r\le{5\varepsilon_0-a-2\delta\over2}
\le\delta_{\max}-\delta,
```

so

```math
M_*+2a-\delta-r
\ge M_*-\delta_{\max}.
\tag{4.4}
```

For the upper bound, use

```math
2a\le10\varepsilon_0-4r-4\delta
```

to get

```math
M_*+2a-\delta-r
\le M_*+10\varepsilon_0-5\delta
\le M_*+10\varepsilon_0-5\delta_0.
\tag{4.5}
```

The exact certificate evaluates (4.4)--(4.5) to (DP.6).

At most `(Q-f)=rD+o(D)` bounded exceptional faces can have degree at least six, so

```math
P_5\ge f-rD-o(D).
```

Using the maximal permitted `r` in the weakening direction gives

```math
{P_5\over D}
\ge {M_*+5\delta-15\varepsilon_0\over5}-o(1)
>{M_*+5\delta_0-15\varepsilon_0\over5}-o(1),
\tag{4.6}
```

which is (DP.7).

---

## 5. Universal pair-shield flex floor rises to `1.1988388040D`

The activated-endpoint pair-shield theorem gives, in the stalled case,

```math
m_D\ge {b-f\over2}
+a_F+{x_A\over2}+{n_0+n_2\over2}+p_U,
\tag{5.1}
```

where all correction terms are nonnegative.  Complete activation gives the still larger
`(q-k)-1` dimension, so it is enough to bound `(b-f)/2`.

Using

```math
{b\over D}=\pi+\delta+o(1)
```

and (4.3),

```math
{b-f\over2D}
={\pi\over2}-{M_*\over10}
+{3\over5}\delta
+{1\over10}r
-{1\over5}a
+o(1).
\tag{5.2}
```

Now retain the full correlation (1.2):

```math
-{a\over5}
\ge-\varepsilon_0+{2\over5}(r+\delta).
```

Hence

```math
\boxed{
{b-f\over2D}
\ge
{\pi\over2}-{M_*\over10}-\varepsilon_0
+\delta+{r\over2}-o(1).
}
\tag{5.3}
```

Insert `delta>delta_0` and `r>=0`.  The certificate proves

```math
{\pi\over2}-{M_*\over10}-0.00710+0.017609
>1.1988388040.
\tag{5.4}
```

This proves (DP.4).  The live diameter-locking theorem immediately gives (DP.5).

This is a genuine increase in the universal live exact-flex reservoir, not a new case
split.  The previous `1.1984798040D` pair-shield floor was conditional on the
small-complement branch; the present `1.1988388040D` floor holds for every survivor in
the live `0.00710` window.

---

## 6. Sharpened one-anchor corank tradeoff

The one-anchor theorem gives

```math
\sigma_C\le {f\over5}+{18\over5}E_U,
\qquad
E_U:=a_F+{x_A\over2}+{n_0+n_2\over2}.
\tag{6.1}
```

The upper edge of (DP.6) gives

```math
\boxed{{f\over5D}<0.15230481+o(1).}
\tag{6.2}
```

Therefore

```math
\boxed{
{\sigma_C\over D}
<0.15230481+{18\over5}{E_U\over D}+o(1),
}
\tag{6.3}
```

which is (DP.8).  Combining (5.1), the finite corank/flex tradeoff, and (6.2) also gives

```math
\boxed{
{m_D\over D}
>1.1988388040
+{p_U\over D}
+{5\over18}\left({\sigma_C\over D}-0.15230481\right)_+
-o(1).
}
\tag{6.4}
```

Thus a survivor that tries to use a macroscopic pure-contact closure corank above
`0.15230481D` pays it back into the already large exact finite flex manifold at rate
`5/18`.

---

## 7. Remaining obstruction

The live scalar endpoint is now much narrower than the previous normal form suggested.
Every survivor in the `0.00710` window simultaneously has:

- outer detour in the width-`0.000141D` strip (4.2);
- total train-slack/superpentagon defect `a+2r<0.000282`;
- more than `0.761242D` pentagonal exceptional faces;
- more than `1.1988388040D` exact contact-flex dimensions; and
- pure-contact closure corank below `0.15230481D` at the pair-shield structural endpoint.

The remaining low-flex combinatorial object is therefore an almost-pure pentagonal
one-anchor internal 4-core, with sparse `K_5`-type dual closure modes, while the actual
diameter thrackle must positively lock a `>1.1988D` exact contact-flex manifold.

The next useful step is no longer another scalar optimization of `a,r,delta`.  The
reduced feasibility root is already being used directly.  Closure requires a geometric
incompatibility between that pentagonal one-anchor core and the positive-spanning
straight-line diameter system, or a source-level finite deformation through the
diameter cusp.

No theorem-state file is changed.

**Disposition:** proved universal live detour pinching `delta>0.017609`, collapsed the
remaining scalar defects to `a+2r<0.000282`, raised the universal pair-shield exact-flex
floor to `1.1988388040D`, tightened the pentagon population and one-anchor corank
constants, and reduced the live obstruction to a near-pure pentagonal one-anchor core
locked by the actual diameter thrackle.  C-II remains open.
