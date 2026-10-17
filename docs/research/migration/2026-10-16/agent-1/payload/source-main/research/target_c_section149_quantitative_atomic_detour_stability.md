# Target C §149 — quantitative atomic endpoint / outer-detour stability

**Date:** 2026-09-12  
**Lifecycle:** proof-only research candidate; theorem-state authority unchanged.  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

Section 148 treats the endpoint `b-per(F)=o(D)`.  This note removes that zero-detour
hypothesis.  It proves an explicit tradeoff between

1. the normalized old outer-walk detour,
2. the squared mass of outer endpoint atoms after quotienting by the `60 degree`
   rhombic phase orbit, and
3. the bounded-defect endpoint capacity required by the quadratic train-crossing
   density.

The phase-orbit quotient is essential.  Total atomic mass is not quantitatively stable
under weak convergence: a fine atomic quadrature can approximate the uniform circular
measure.  In contrast, §142's quadratic crossing density controls an `ell^2` mass of
`pi/3` phase orbits, and that is exactly the quantity a Fejer-kernel estimate can
control from outer detour.

Throughout put

\[
\Delta_2={\pi\over2\sqrt3},
\qquad s_2:=\sqrt{\Delta_2}.
\]

Work along a Type-II subsequence for which

\[
\delta_D:={b-\operatorname{per}(F)\over D}\to\delta\ge0.
\tag{149.1}
\]

Canonical Type II gives

\[
{\operatorname{per}(F)\over D}\to\pi,
\qquad
{R_4\over D^2}\to\Delta_2.
\tag{149.2}
\]

Pass further so the normalized stopped-train count and all endpoint measures used below
converge.

---

## 149.1 Fourier control from projection variation

Let

\[
\nu_D:={1\over D}
\sum_{e\in\partial_{out}C}^{occ}\delta_{\theta_e}
\]

be the projective outer-walk direction measure and let `nu` be a weak limit.  Its total
mass is

\[
M:=\nu(\mathbb T)=\pi+\delta,
\qquad
\mathbb T=\mathbb R/\pi\mathbb Z.
\tag{149.3}
\]

As in §148, projection variation of the actual repeated outer walk and Type-II disk
convergence give

\[
C\nu(\alpha):=
\int_{\mathbb T}|\cos(\theta-\alpha)|\,d\nu(\theta)
\ge2
\qquad(\alpha\in\mathbb T).
\tag{149.4}
\]

Put

\[
g(\alpha):=C\nu(\alpha)-2\ge0.
\]

Since

\[
\int_0^\pi|\cos t|dt=2,
\]

\[
{1\over\pi}\int_0^\pi g(\alpha)d\alpha={2\delta\over\pi}.
\tag{149.5}
\]

For `n>=1` define the projective Fourier moment

\[
\widehat\nu(n):=
\int_0^\pi e^{-2in\theta}\,d\nu(\theta).
\]

The Fourier series

\[
|\cos t|
={2\over\pi}
+{4\over\pi}
\sum_{n\ge1}{(-1)^n\over1-4n^2}\cos(2nt)
\tag{149.6}
\]

shows that the `n`-th complex Fourier coefficient of `g` has modulus

\[
{2\over\pi(4n^2-1)}|\widehat\nu(n)|.
\]

Because `g>=0`, every Fourier coefficient has modulus at most its mean (149.5).
Therefore

\[
\boxed{
|\widehat\nu(n)|
\le\delta(4n^2-1)
\qquad(n\ge1).
}
\tag{149.7}
\]

This is the quantitative replacement for §148's exact statement that all nonzero
moments vanish when `delta=0`.

---

## 149.2 Quotient by the rhombic phase orbit

Identify projective directions modulo the relation

\[
\theta\sim\theta+{\pi\over3}.
\]

Equivalently push `nu` forward by

\[
\theta\longmapsto e^{6i\theta}.
\]

Let the atoms of this quotient measure have masses

\[
A_1,A_2,\ldots .
\]

Thus `A_j` is the total outer-endpoint atomic mass in one complete three-direction
phase orbit

\[
\{\theta,\theta+\pi/3,\theta+2\pi/3\}.
\]

The `m`-th Fourier moment of the quotient is exactly

\[
\widehat\nu(3m).
\]

Fix an integer `N>=2`.  The Fejer kernel on the quotient circle is

\[
K_N(t)=
\sum_{|m|<N}\left(1-{|m|\over N}\right)e^{imt}
\ge0,
\qquad K_N(0)=N.
\]

Hence

\[
\begin{aligned}
N\sum_jA_j^2
&\le
\iint K_N(x-y)d\bar\nu(x)d\bar\nu(y)\\
&=
M^2+2\sum_{m=1}^{N-1}
\left(1-{m\over N}\right)|\widehat\nu(3m)|^2.
\end{aligned}
\tag{149.8}
\]

Use (149.7) at frequency `3m`.

### Theorem 149.A — outer phase-orbit atomic `ell^2` bound

For every integer `N>=2`,

\[
\boxed{
\sum_jA_j^2
\le U_N(\delta),
}
\tag{149.9}
\]

where

\[
\boxed{
U_N(\delta)
:={ (\pi+\delta)^2\over N}
+{2\delta^2\over N}
\sum_{m=1}^{N-1}
\left(1-{m\over N}\right)(36m^2-1)^2.
}
\tag{149.10}
\]

In particular `U_N(0)=pi^2/N`, and sending `N->infinity` recovers the §148 fact that
there are no outer atoms at zero normalized detour.

---

## 149.3 Quadratic rhombus crossings force train-orbit `ell^2` mass

Let

\[
{T\over D}\to x>0
\]

and let `mu` be the weak limit of the empirical projective stopped-train direction
probability measures.  Group its atoms into the same `pi/3` phase orbits and let

\[
S_1,S_2,\ldots
\]

be the total train-probability mass of those orbits.

The audited §142 area-saturation argument says that all but `o(D^2)` rhombus crossings
occur between train directions whose limiting projective separation is exactly
`pi/3`.  Hence limiting quadratic crossings split among these phase orbits.

Inside one orbit, the finite train-crossing graph is triangle-free.  Weighted Mantel
therefore bounds its normalized crossing density by `S_j^2/4`.  Summing over phase
orbits and using `R_4/D^2->Delta_2` gives

\[
\boxed{
\sum_jS_j^2
\ge {4\Delta_2\over x^2}.
}
\tag{149.11}
\]

This is stronger information than the scalar atomic-mass inequality when endpoint
capacity is measured in the same phase quotient.

---

## 149.4 Endpoint capacity in `ell^2`

For orbit `j`, let `C_j` be the normalized limiting bounded-defect endpoint incidence
mass in that orbit.  A train in that orbit has two terminal face-side incidences, so
shrinking fixed orbit neighborhoods after taking the source limit gives

\[
2xS_j\le A_j+C_j.
\tag{149.12}
\]

Let

\[
B:=\liminf {Q+4f\over D}.
\]

The exact §143 endpoint multigraph gives

\[
\sum_jC_j\le B.
\]

Using `ell^1>=ell^2`, (149.12), the reverse triangle inequality in `ell^2`,
(149.11), and (149.9),

\[
\begin{aligned}
B
&\ge\|(C_j)\|_2\\
&\ge2x\|(S_j)\|_2-\|(A_j)\|_2\\
&\ge4\sqrt{\Delta_2}-\sqrt{U_N(\delta)}.
\end{aligned}
\]

Thus:

### Theorem 149.B — all-regime atomic endpoint / detour tradeoff

For every fixed integer `N>=2`, every Type-II subsequential limit satisfies

\[
\boxed{
\liminf {Q+4f\over D}
\ge
\left(4\sqrt{\Delta_2}-\sqrt{U_N(\delta)}\right)_+,
}
\tag{149.13}
\]

where

\[
\delta=\lim {b-\operatorname{per}(F)\over D}.
\]

Since `f<=Q`,

\[
\boxed{
\liminf {Q\over D}
\ge {1\over5}
\left(4\sqrt{\Delta_2}-\sqrt{U_N(\delta)}\right)_+.
}
\tag{149.14}
\]

Finally, with

\[
t:=\lim {q-k\over D},
\]

canonical `b+Q=2(q-k)` and `per(F)/D->pi` give the source-level inequality

\[
\boxed{
 t\ge
 {\pi+\delta\over2}
 +{1\over10}
 \left(4\sqrt{\Delta_2}-\sqrt{U_N(\delta)}\right)_+.
}
\tag{149.15}
\]

This is the desired all-regime extension of §148.  The right side is not claimed to be
monotone in `delta`; its value is that it uses exactly the same outer-detour currency
that remains live in the full-core branch.

---

## 149.5 Explicit stability above the §146 lower endpoint

The §146 candidate gives, in the notation

\[
t={q-k\over D},
\qquad\kappa={k\over D},
\qquad\varphi={f\over D},
\]

\[
t+4\varphi\ge4s_2+\kappa-o(1).
\tag{149.16}
\]

Also

\[
{Q\over D}=2t-\pi-\delta+o(1),
\qquad\varphi\le {Q\over D}.
\tag{149.17}
\]

Therefore

\[
\boxed{
\delta
\le {9\over4}(t-C_{146})-{\kappa\over4}+o(1)
\le {9\over4}(t-C_{146})+o(1),
}
\tag{149.18}
\]

where

\[
C_{146}={4\over9}(\pi+s_2).
\]

So a sequence close to the §146 lower endpoint automatically has quantitatively small
outer detour; no cap containment is required.

For `N=7`, the Fejer polynomial in (149.10) is explicit:

\[
\sum_{m=1}^{6}
\left(1-{m\over7}\right)(36m^2-1)^2
=687459,
\]

hence

\[
\boxed{
U_7(\delta)
={ (\pi+\delta)^2+1374918\,\delta^2\over7}.
}
\tag{149.19}
\]

Combining (149.13), `Q+4f<=5Q`, (149.17), and (149.18) gives a fully explicit
stability test.  For example, if

\[
t\le C_{146}+{1\over2000}+o(1),
\]

then

\[
\delta\le {9\over8000}+o(1).
\]

The bounded-endpoint upper estimate is

\[
{Q+4f\over D}
\le5\left(2C_{146}+{1\over1000}-\pi\right)+o(1)
<2.493+o(1).
\tag{149.20}
\]

For the lower estimate, the elementary enclosures

\[
3.14159<\pi<3.14160,
\qquad
1.73205<\sqrt3<1.73206
\]

imply

\[
0.95230<s_2<0.95232.
\]

At `delta<=9/8000`, (149.19) gives

\[
U_7(\delta)<1.289^2,
\]

and therefore (149.13) gives

\[
{Q+4f\over D}
>4(0.95230)-1.289-o(1)
=2.5202-o(1),
\tag{149.21}
\]

contradicting (149.20) for all sufficiently large `D`.

### Corollary 149.C — explicit first-order exclusion window

Within the audited-working Type-II dependency stack,

\[
\boxed{
\liminf {q-k\over D}
\ge C_{146}+{1\over2000}
=1.8200135379794445\ldots .
}
\tag{149.22}
\]

The numerical increment is not the main theorem.  The durable content is the
all-regime phase-orbit inequality (149.13)--(149.15), which can be recomposed with
future detour or diameter-moment bounds without redoing the atomic endpoint argument.

---

## 149.6 Surviving obstruction

Section 149 still does not close Type II.  Its Fejer estimate becomes weak once the
normalized outer detour is not small.  A survivor can in principle spend a substantial
linear outer-detour budget to realize phase-orbit atoms on the old outer walk while
using bounded defect faces for the remaining train endpoints.

The next useful composition is therefore not another optimization of `N`.  It is to
upper-bound or independently charge the same `delta=(b-per(F))/D` using

- the canonical §122 aggregate harmonic detour,
- the joint-payment chain §§134--140,
- the loaded-hull/tooth identities §§128--141, or
- a source-preserving deformation of a linear-detour outer interval.

The macroscopic inactive-container branch remains untouched.

No theorem-state authority is changed, no contact-isolated source point is removed,
and no full-source extension of §57 is used.
