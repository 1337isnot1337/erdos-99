<!-- migration-source: path=docs/reports/target_c_ma_dirichlet_joint_floor_0599785_2026-09-10.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=007fb1c5bbd31a91b2c5dc845e8abfd913f25d60; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — MA plus Dirichlet detour raises the post-ZF floor to 0.599785

**Date:** 2026-09-10  
**Repository state:** branch `research/c-ii-cyclic-gap-2026-09-10`, after MAJC endpoint exclusion  
**Run type:** exact asymptotic inequality synthesis / closing-proof continuation  
**Target:** Target C, C-II after ZF/DB/FS/MA/JC/DD/CC  
**External web search:** not used  
**Computation:** decimal evaluation only; proof is analytic

## LEVEL I STATUS

`STILL OPEN`

The MAJC endpoint exclusion can be made quantitative. Keep the exact DB defect

\[
z:=\frac{Q+2s_Z}{D}
\]

inside the Dirichlet outer-pocket estimate and use CC's sharp exceptional-face area
bound. On the only interval where the new competition can beat the MA/JC floor, the
largest possible cavity capacity occurs at `z=0`.

The result is

\[
\boxed{
\liminf_{D\to\infty}
\frac{e_{BB}+2s_C}{D}
\ge
\lambda_{MADD}
=0.5997852332423223371\ldots .
}
\tag{MD.1}
\]

This is a strict explicit improvement over

\[
\lambda_{MAJC}=0.5937285472681860970\ldots .
\]

The constant `lambda_MADD` is defined analytically below as the unique crossover of
two monotone one-variable thresholds. No numerical optimization is a proof input.

---

## 1. Normalized variables

Take an arbitrary unbounded audited post-ZF survivor sequence. Pass to a subsequence on
which

\[
\lambda:=\lim\frac{e_{BB}+2s_C}{D},
\qquad
y:=\lim\frac hD
\]

exist. DB gives

\[
y\ge2\rho,
\qquad
\rho=\cos\rho.
\tag{1.1}
\]

Pass further so

\[
z:=\lim\frac{Q+2s_Z}{D}
\]

exists. DB's exact defect inequality gives

\[
\boxed{
0\le z\le u(y):=y-2\cos(y/2).
}
\tag{1.2}
\]

The function `u` is strictly increasing and vanishes at `y=2rho`.

MA gives the force-hull area floor

\[
\liminf\frac{\operatorname{area}F}{D^2}
\ge
\Phi(y):=\frac{y+\sin y}{4},
\tag{1.3}
\]

while GU gives

\[
\limsup
\frac{\sum_r\operatorname{area}(P_r)}{D^2}
\le\frac\pi4\lambda^2.
\tag{1.4}
\]

Hence the attachment-cell gap obeys

\[
\boxed{
\liminf\frac GD^2
\ge
\Phi(y)-\frac\pi4\lambda^2.
}
\tag{1.5}
\]

---

## 2. Keep the DB defect inside the cavity estimate

Write `P_F=per(F)`. ZE gives

\[
\frac{b-P_F}{D}
=2y-z-\frac{P_F}{D}+o(1).
\tag{2.1}
\]

MA's perimeter part gives

\[
\frac{P_F}{D}
\ge
p_0(y)-o(1),
\qquad
p_0(y):=y+2\cos(y/2).
\tag{2.2}
\]

Since

\[
2y-p_0(y)=u(y),
\]

(2.1)--(2.2) imply

\[
\boxed{
\limsup\frac{b-P_F}{D}
\le u(y)-z.
}
\tag{2.3}
\]

For the total old-contact chain length, DD/OD give exactly

\[
L_{chain}
=2h-(Q+2s_Z)-e_{BB}+c_B.
\tag{2.4}
\]

PC gives

\[
e_{BB}=d_P+Q+2(d_H+s_Z)+c_B
=d_P+2d_H+(Q+2s_Z)+c_B.
\tag{2.5}
\]

Thus

\[
c_B\le e_{BB}-(Q+2s_Z)
\]

and therefore

\[
\boxed{
\limsup\frac{L_{chain}}D
\le2(y-z).
}
\tag{2.6}
\]

DD's global Dirichlet-dual detour theorem now yields

\[
\boxed{
\limsup\frac{H_{out}}{D^2}
\le
\frac1{\sqrt6}
[2(y-z)]^{3/2}\sqrt{u(y)-z}.
}
\tag{2.7}
\]

CC gives the exact exceptional-face estimate

\[
A_{exc}
\le\frac{Q^2+24Q}{4\pi}.
\tag{2.8}
\]

Since `Q/D<=z+o(1)`, this gives

\[
\boxed{
\limsup\frac{A_{exc}}{D^2}
\le\frac{z^2}{4\pi}.
}
\tag{2.9}
\]

Finally ZG/GU gives

\[
G\le H_{out}+A_{exc}+O(D).
\tag{2.10}
\]

Consequently every survivor limit satisfies

\[
\boxed{
\Phi(y)-\frac\pi4\lambda^2
\le
U(y,z):=
\frac1{\sqrt6}[2(y-z)]^{3/2}\sqrt{u(y)-z}
+\frac{z^2}{4\pi}
}
\tag{2.11}
\]

for some `z in [0,u(y)]`.

---

## 3. On the critical interval, positive DB defect only reduces capacity

We only need

\[
I=[2\rho,3/2].
\]

First note `2rho>7/5`. Also `u` is increasing. The alternating Taylor lower bound

\[
\cos(3/4)
>
1-\frac{(3/4)^2}{2}
+\frac{(3/4)^4}{24}
-\frac{(3/4)^6}{720}
=\frac{239759}{327680}
>\frac{29}{40}
\]

gives

\[
0\le u(y)\le u(3/2)<\frac1{20}
\qquad(y\in I).
\tag{3.1}
\]

Fix `y in I` and put

\[
x=y-z,
\qquad v=u(y)-z.
\]

For `0<=z<u(y)`, differentiation of (2.11)'s capacity gives

\[
\begin{aligned}
\partial_zU
={}&-rac1{\sqrt6}
\left[
3(2x)^{1/2}v^{1/2}
+\frac{(2x)^{3/2}}{2v^{1/2}}
\right]
+\frac{z}{2\pi}.
\end{aligned}
\tag{3.2}
\]

Now

\[
x\ge y-u(y)=2\cos(y/2)\ge2\cos(3/4)>\frac{29}{20},
\]

so `(2x)^(3/2)>4`. Also `sqrt(v)<1/4`, `1/sqrt(6)>2/5`,
`z<1/20`, and `pi>3`. Keeping only the second negative term in (3.2) gives

\[
\partial_zU
<-rac25\cdot8+\frac1{120}<0.
\tag{3.3}
\]

Therefore

\[
\boxed{
\max_{0\le z\le u(y)}U(y,z)=U(y,0)
}
\tag{3.4}
\]

throughout the critical interval.

Define

\[
H(y):=
\frac1{\sqrt6}(2y)^{3/2}\sqrt{u(y)}
\tag{3.5}
\]

and

\[
\boxed{
T(y):=
\sqrt{
\frac4\pi\,[\Phi(y)-H(y)]
}
}
\tag{3.6}
\]

whenever the radicand is nonnegative. Equations (2.11) and (3.4) imply

\[
\boxed{\lambda\ge T(y).}
\tag{3.7}
\]

---

## 4. The detour threshold decreases on the critical interval

Write

\[
H(y)=\frac1{\sqrt6}(2y)^{3/2}u(y)^{1/2},
\qquad
u'(y)=u'(y)=1+\sin(y/2)>1.
\]

For `y>2rho`,

\[
H'(y)
>
\frac1{\sqrt6}
\frac{(2y)^{3/2}}{2\sqrt{u(y)}}.
\tag{4.1}
\]

On `I`, `2y>14/5`, hence `(2y)^(3/2)>4`, while (3.1) gives
`2sqrt(u)<1/2`. Therefore

\[
H'(y)>\frac25\cdot8>3.
\tag{4.2}
\]

But

\[
0\le\Phi'(y)=\frac{1+\cos y}{4}\le\frac12.
\]

Hence

\[
\boxed{[T(y)^2]' <0}
\tag{4.3}
\]

wherever `T` is real. Thus `T` is strictly decreasing on the critical interval.

---

## 5. The independent MA/JC threshold increases

The MA/JC report already proves that after minimizing over the actual force-hull
perimeter, every survivor with diameter density `y` satisfies

\[
\boxed{\lambda\ge R(y),}
\tag{5.1}
\]

where `R(y)` is the positive root of

\[
\boxed{
(\pi^2+1)R^2
+4\cos(y/2)R
+4\cos^2(y/2)
-\pi(y+\sin y)=0.
}
\tag{5.2}
\]

and `R(y)` is strictly increasing for `y>=2rho`.

At the left endpoint `u(2rho)=0`, so

\[
T(2\rho)^2=\frac4\pi\Phi(2\rho).
\]

The defining MAJC equality gives

\[
\Phi(2\rho)-\frac\pi4R(2\rho)^2
=\frac{(R(2\rho)+2\rho)^2}{4\pi}>0.
\]

Therefore

\[
\boxed{R(2\rho)<T(2\rho).}
\tag{5.3}
\]

At `y=3/2` the inequalities reverse. First, the alternating Taylor estimates

\[
\cos(3/4)
<1-\frac{(3/4)^2}{2}+\frac{(3/4)^4}{24}
=\frac{1499}{2048},
\]

\[
\sin(3/2)
>
\frac32-\frac{(3/2)^3}{6}+\frac{(3/2)^5}{120}
-\frac{(3/2)^7}{5040}
=\frac{71493}{71680}
\]

and `3141/1000<pi<22/7` give

\[
Q_R(3/2,3/5)
<-rac{926114759}{32112640000}<0,
\]

where `Q_R` denotes the left side of (5.2). Since `Q_R` increases in `R`,

\[
\boxed{R(3/2)>3/5.}
\tag{5.4}
\]

Second, the same cosine upper bound gives

\[
u(3/2)>
\frac32-2\frac{1499}{2048}
=\frac{37}{1024}
>\frac9{250}.
\]

Hence

\[
\sqrt{u(3/2)}>\frac3{16}.
\]

Using `1/sqrt(6)>2/5`, `3^(3/2)>5`, and `Phi(3/2)<5/8`,

\[
H(3/2)>
\frac25\cdot5\cdot\frac3{16}
=\frac38.
\]

Therefore

\[
T(3/2)^2
<\frac4\pi\left(\frac58-\frac38\right)
=\frac1\pi
<\frac13
<\left(\frac35\right)^2.
\]

Thus

\[
\boxed{T(3/2)<3/5<R(3/2).}
\tag{5.5}
\]

By continuity, strict monotonicity of `R`, and strict decrease of `T`, there is a
unique

\[
\boxed{y_*\in(2\rho,3/2)}
\tag{5.6}
\]

such that

\[
R(y_*)=T(y_*).
\tag{5.7}
\]

For `y in I`, every survivor satisfies

\[
\lambda\ge\max\{R(y),T(y)\},
\]

whose unique global minimum is the crossover value

\[
\boxed{\lambda_{MADD}:=R(y_*)=T(y_*).}
\tag{5.8}
\]

For `y>=3/2`, monotonicity gives

\[
\lambda\ge R(y)\ge R(3/2)>3/5>\lambda_{MADD},
\]

so (5.8) is the global threshold for all `y>=2rho`. This proves MD.1. `square`

---

## 6. Numerical evaluation and endpoint localization

Solving the two analytic equations (5.2) and (5.7) gives

\[
\boxed{
y_*=1.4937010344306311087\ldots,}
\tag{6.1}
\]

\[
\boxed{
\lambda_{MADD}=0.5997852332423223371\ldots .
}
\tag{6.2}
\]

At this point

\[
u(y_*)=0.02603694249391398686\ldots .
\]

Every sequence approaching the new endpoint must force all inequalities used in the
minimization to equality. In particular

\[
\boxed{
\frac hD\to y_*,
\qquad
\frac{Q+2s_Z}{D}\to0,
\qquad
\frac{\operatorname{per}F}{D}\to p_0(y_*),
}
\tag{6.3}
\]

and the MA/JC relaxation gives

\[
\boxed{
\frac{e_{BB}}D\to\lambda_{MADD},
\qquad
\frac{s_C}{D}\to0.
}
\tag{6.4}
\]

The normalized chain--chord detour tends to

\[
\frac{b-P_F}{D}
\to u(y_*)>0.
\tag{6.5}
\]

Thus the new endpoint is not the DB-equality regime. It is a zero-face-defect,
positive-detour regime in which the full quadratic attachment-cell gap must be carried
by outer pockets.

---

## 7. Regression audit

- **Regular odd shell:** has `y->pi` and loaded/contact currency near `pi`, far above
  MD.1.
- **Dense isolated shell fillings:** may reproduce radial force-hull geometry but do
  not supply the global post-ZF/DB/PC source certificate.
- **Giant exceptional face:** the maximizing cavity on the critical interval has
  `z=0`; exceptional-face defect only lowers the available capacity there.
- **Many thin pockets:** DD allows them, but they cannot collectively beat the
  zero-defect chain capacity used in `T(y)`.
- **Half-weight matching and response trace regressions:** unused.

The decisive source-specific information is the conjunction of FS/MA circle geometry,
DB's exact topology defect, and the PC/DD outer-pocket decomposition.

---

## 8. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| defect-aware cavity bound (2.11) | proved | DD + PC chain identity + CC exceptional-face bound |
| `z=0` maximizes critical cavity capacity | proved | derivative estimate (3.2)--(3.3) |
| `T(y)` decreases on `[2rho,3/2]` | proved | explicit derivative domination |
| MA/JC threshold `R(y)` increases | proved in MAJC | exact implicit derivative |
| unique crossover and global minimum | proved | opposite endpoint signs + monotonicity |
| explicit floor `0.5997852332...` | proved asymptotically | analytic crossover; decimal is evaluation only |
| Level I | still open | endpoint outer-pocket geometry is not yet excluded |

---

## 9. Exact next obligation

At the MADD endpoint, `z=o(1)` but the normalized detour

\[
u_*:=y_*-2\cos(y_*/2)=0.02603694249\ldots
\]

is positive. Equality requires the DD outer-pocket bound to carry essentially the
entire attachment-cell gap while the force hull simultaneously approaches MA's
one-missing-arc cyclic extremal.

The next closing implication is therefore an **outer-pocket equality incompatibility**:
prove that a unit-contact outer walk in the MA one-gap force-hull geometry cannot
asymptotically saturate

\[
H_{out}
\le\frac1{\sqrt6}L_{chain}^{3/2}\sqrt{b-P_F}
\]

at the required MADD values. A fixed positive loss would exclude the endpoint and
raise the threshold again; an exact structural conflict with the one-gap force hull
would close this branch outright.

No further scalar iteration should be attempted before auditing this equality geometry.
