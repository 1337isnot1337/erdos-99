# Target C — Section 118 companion: sharp correlated-slack envelope

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Status:** proof-only sharpening of Section 118; theorem state unchanged.

The main Section-118 report proves the exact canonical slack decomposition

\[
\sigma=x+y+z+w,
\]

\[
x=U-|S|,
\qquad y=|S|-2\alpha,
\qquad z=2\alpha-C,
\qquad w=C-M.
\tag{118.S1}
\]

All four terms are nonnegative. This companion keeps two additional correlations that
the first one-variable relaxation discards. They raise the safe explicit window to

\[
\boxed{\sigma\le0.0088}
\]

and give

\[
\boxed{\mu=0.9762439137425688\ldots .}
\]

The scalar envelope of this sharpened relaxation is

\[
\boxed{\sigma_{\rm env}=0.00897587622448\ldots,\qquad
\mu_{\rm env}=0.97624796424817\ldots .}
\]

## 1. Shared face currency reduces `15 z` to `10 z`

Pass once more to a common subsequence on which the bounded normalized local
quantities

\[
Q_D/D,\qquad c_D/D,\qquad s_D/D
\]

all converge. Write their limits as `q,c,s_0`. The retained Section-101 face ledger
gives

\[
\boxed{2s_0+c+q\le z,}
\tag{118.S2}
\]

and in particular

\[
q+c\le z.
\tag{118.S3}
\]

On this same subsequence the non-tooth directional bad-end categories satisfy

- bounded nonquadrilateral boundary: at most `5q`;
- nonprincipal macroscopic routes: at most `z+C_tail`;
- exceptional micro routes: at most `3z+6c`.

Therefore their total is at most

\[
4z+5q+6c+C_{tail}
\le10z+C_{tail}.
\tag{118.S4}
\]

The tiny-span and integrated-tooth terms from Section 118 are unchanged. Using

\[
C_{tail}\le{x\over2}+{5\over3}w,
\]

the directional bad-train concentration becomes

\[
\boxed{
B(x,y,z,w)
\le Q_{\rm tooth}(y)+y+{3\over2}x+10z+{35\over3}w.
}
\tag{118.S5}
\]

Here `Q_tooth(t)` is the unique nonnegative solution of

\[
\sin Q+\sqrt3(1-\cos Q)-Q={t\over2}.
\tag{118.S6}
\]

The common-subsequence formulation is essential: separate limsups for `q` and `c`
would not imply (118.S3).

## 2. The remaining slack maximization is analytic

Because

\[
{3\over2}<10<{35\over3},
\]

and `x+y+z+w=sigma`, (118.S5) yields

\[
B
\le {35\over3}\sigma
+Q_{\rm tooth}(y)-{32\over3}y.
\tag{118.S7}
\]

Put

\[
F(Q)=\sin Q+\sqrt3(1-\cos Q)-Q.
\]

Then `F(Q_tooth(y))=y/2`, and

\[
F'(Q)=\cos Q+\sqrt3\sin Q-1
\]

is strictly increasing on `(0,pi/3)`. Hence

\[
{dQ_{\rm tooth}\over dy}={1\over2F'(Q_{\rm tooth})}
\]

is strictly decreasing. The function

\[
Q_{\rm tooth}(y)-{32\over3}y
\]

has a unique maximizer at the solution `Q_0` of

\[
\boxed{F'(Q_0)={3\over64}.}
\tag{118.S8}
\]

Numerically,

\[
Q_0=0.0272815201203263\ldots,
\]

\[
y_0:=2F(Q_0)=0.00128228501806740\ldots,
\]

and

\[
\kappa_0:=Q_0-{32\over3}y_0
=0.0136038132609408\ldots .
\tag{118.S9}
\]

For every `sigma>=y_0`,

\[
\boxed{
B(x,y,z,w)
\le B_*(\sigma):={35\over3}\sigma+\kappa_0.
}
\tag{118.S10}
\]

## 3. The area perturbation is `10 sigma / 3`

Section 118 gives

\[
\delta\le{10\over3}w,
\qquad
\tau\le x+{10\over3}w.
\]

Define

\[
r=x+{10\over3}w.
\]

Since `x+w<=sigma`,

\[
\boxed{r\le{10\over3}\sigma.}
\tag{118.S11}
\]

Thus the circular-segment area floor can be taken as

\[
\boxed{
A_*(\sigma)
={\pi\over4}
-G(\theta)
-2G\left(\phi_8+{10\sigma\over3}\right)
-G\left({10\sigma\over3}\right),
}
\tag{118.S12}
\]

where `G(t)=(t-sin t)/8` and `phi_8=2pi-2theta_8`. The two smaller principal gaps are
at most `phi_8+r`, while the total tail gap mass is at most `r`; superadditivity of `G`
then gives (118.S12).

For the explicit one-variable theorem we deliberately keep the other two quantities
coarse:

\[
{T_D\over D}
\le C_T(\sigma)+o(1),
\qquad
C_T(\sigma)=U(\theta)+2\sigma,
\tag{118.S13}
\]

and

\[
{E_D\over D}\le\sigma+o(1).
\tag{118.S14}
\]

The signed-return/DP theorem therefore forces

\[
\boxed{
\lambda\sigma
\ge
(2-\sqrt3)
\left[A_*(\sigma)-2C_T(\sigma)B_*(\sigma)\right]_+,
}
\tag{118.S15}
\]

where `lambda=sin(theta/2)`.

## 4. Safe contradiction at `sigma=0.0088`

Let `theta_22` solve `sigma(theta_22)=0.0088`. Then

\[
\boxed{
\theta_22=2.704779235215494\ldots,
\qquad
\mu_22=0.9762439137425688\ldots .
}
\tag{118.S16}
\]

The stability rectangle retains large room:

\[
{10\over3}\sigma=0.0293333333\ldots<0.1,
\]

and the main-region tangent extent is

\[
U(\theta_22)+{10\over3}\sigma
=1.86048573180023\ldots<\pi.
\]

The scalar inputs are

\[
A_*=0.4703752868004241\ldots,
\]

\[
C_T=1.848752398466895\ldots,
\qquad
B_*=0.1162704799276074\ldots .
\]

Hence

\[
A_*-2C_TB_*
=0.0404646295263018\ldots>0.
\tag{118.S17}
\]

The signed-return lower bound forces normalized route excess at least

\[
0.0111063071953309\ldots,
\]

while only `0.0088` is available. The contradiction margin is

\[
\boxed{0.0023063071953309\ldots .}
\tag{118.S18}
\]

Therefore every sufficiently large full-core Type-II survivor contains a
quadratic-area locally rhombus-saturated harmonic carrier with

\[
\boxed{
\operatorname{diam}(P_*)
\ge(0.9762439137425688\ldots-o(1))D.
}
\tag{118.S19}
\]

## 5. Envelope of the sharpened relaxation

Define

\[
H_*(s)
={2-\sqrt3\over\lambda(s)}
\left[A_*(s)-2C_T(s)B_*(s)\right]-s.
\]

On the current window `A_*` decreases while `C_T`, `B_*`, and `lambda` increase, so
`H_*` is strictly decreasing. The unique zero is

\[
\boxed{
\sigma_{\rm env}=0.00897587622448\ldots,
}
\]

with

\[
\boxed{
\theta_{\rm env}=2.70481662472814\ldots,
\qquad
\mu_{\rm env}=0.97624796424817\ldots .
}
\tag{118.S20}
\]

At the root the retained area scalar is still positive (`0.03270...`), so the envelope
comes from equality in the signed-return inequality rather than collapse of the DP
residual.

This is still a full-core carrier theorem, not a proof of C-II or Level I. The separate
macroscopic inactive-container branch is untouched.
