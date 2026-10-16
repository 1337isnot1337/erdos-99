# Target C-II — terminal FREE route/perimeter conservation and train–pentagon normal form

**Date:** 2026-09-18
**Status:** proof-only structural theorem; theorem-state authority unchanged
**Scope:** full-core Type-II terminal FREE survivor sequences with `pi D-q=o(D)`
**Depends on:** exact Type-II route/train identities; scope-safe matched all-train gap `g=0.007707`; terminal FREE chamber-interface package; exact singleton/rhombic stopped-train decomposition; degree arithmetic for bounded exceptional faces
**Certificate:** `research/verify_target_c_free_terminal_route_perimeter_train_pentagon_2026_09_18.py`
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The current terminal FREE package ends with the classwise floor

\[
\max\{Q+2f,\ b-\operatorname{per}F\}
\ge(1.434249460295936\ldots-o(1))D.
\]

That form hides two pieces of structure which are useful for the next geometric step.
First, the exact route/train handshake forces a much larger sum of actual outer-walk
detour and the **global occurrence-counted exceptional-face perimeter**. Second, the
matched all-train gap forces roughly twice as much stopped-train slack as the older
high-`t` package. Near the scalar classwise endpoint, these two facts make the
exceptional side pentagon-dominated and convert it into an explicit singleton-versus-
rhombic-pentagon train dichotomy.

Put

\[
s_2:=\sqrt{\frac\pi{2\sqrt3}},\qquad g:=0.007707,
\]

and define

\[
M_g:=4s_2+2g
=3.824665227455829\ldots,
\tag{TP.1}
\]

\[
C_g:=\frac{3M_g}{8}
=1.434249460295936\ldots,
\tag{TP.2}
\]

\[
\tau_g:=\frac\pi2+g
=1.578503326794896\ldots .
\tag{TP.3}
\]

Let

\[
\lambda_D:=b-\operatorname{per}(F),
\qquad
P_{\rm exc}:=Q+4f,
\qquad
E_{\rm exc}:=Q+2f.
\]

The first main conclusion is

\[
\boxed{
\lambda_D+P_{\rm exc}
\ge (M_g-o(1))D.
}
\tag{TP.4}
\]

Hence

\[
\boxed{
\max\{\lambda_D,P_{\rm exc}\}
\ge (M_g/2-o(1))D
=(1.912332613727915\ldots-o(1))D.
}
\tag{TP.5}
\]

This is stronger than the old `1.434...D` classwise statement in the outer branch,
and on the exceptional branch it lands directly on the occurrence-counted global
perimeter which is closest to the Sections 122–123 detour ledger.

The second main conclusion is the terminal stopped-train slack floor

\[
\boxed{
\tau_D:=T-2\sqrt{R_4}
\ge(\tau_g-o(1))D.
}
\tag{TP.6}
\]

Using the exact decomposition

\[
2\tau_D=\rho_{\rm rec}+\sigma_R,
\qquad
\rho_{\rm rec}=2S_D,
\]

where `S_D` is the singleton stopped-train count and `sigma_R` is the strict-rhombus
train-isoperimetric slack, every terminal FREE survivor has the dichotomy

\[
\boxed{
S_D\ge(0.789251663397448\ldots-o(1))D
}
\tag{TP.7}
\]

or

\[
\boxed{
\sigma_R\ge(1.578503326794896\ldots-o(1))D.
}
\tag{TP.8}
\]

In the second branch the strict-rhombus stopped-train crossing graph has Mantel
deficit

\[
\boxed{
\frac{T_R^2}{4}-R_4
\ge(0.907344013935981\ldots-o(1))D^2.
}
\tag{TP.9}
\]

Finally there is a quantitative stability statement around the current classwise
minimum. Fix `epsilon>=0`. If

\[
\lambda_D\le(C_g+\varepsilon+o(1))D,
\qquad
E_{\rm exc}\le(C_g+\varepsilon+o(1))D,
\tag{TP.10}
\]

then

\[
\boxed{
P_{\rm exc}\ge
\left(\frac{5M_g}{8}-\varepsilon-o(1)\right)D,
}
\tag{TP.11}
\]

\[
\boxed{
f\ge
\left(\frac{M_g}{8}-\varepsilon-o(1)\right)D,
\qquad
Q-f\le(4\varepsilon+o(1))D,
}
\tag{TP.12}
\]

and the number `P_5` of bounded pentagonal contact faces obeys

\[
\boxed{
P_5\ge
\left(\frac{M_g}{8}-5\varepsilon-o(1)\right)D.
}
\tag{TP.13}
\]

At `epsilon=0`, the scalar endpoint therefore has

\[
\boxed{
P_5\ge(0.478083153431979\ldots-o(1))D,
}
\tag{TP.14}
\]

and all but `o(D)` of the exceptional degree excess is pentagonal.

Combining this stability statement with the terminal train dichotomy gives a more
geometric normal form. In the rhombic branch of (TP.8), if (TP.10) holds and

\[
0\le\varepsilon<0.0324764976145998\ldots,
\]

then the number `I_5` of strict-rhombus/pentagon boundary incidences satisfies

\[
\boxed{
I_5\ge
(0.811912440364997\ldots-25\varepsilon-o(1))D.
}
\tag{TP.15}
\]

Consequently at least

\[
\boxed{
(0.405956220182498\ldots-12.5\varepsilon-o(1))D
}
\tag{TP.16}
\]

distinct non-singleton rhombic stopped trains terminate at a pentagon, and at least

\[
\boxed{
(0.162382488072999\ldots-5\varepsilon-o(1))D
}
\tag{TP.17}
\]

distinct pentagons touch the strict-rhombus complex.

Thus a terminal FREE survivor cannot remain near the scalar interface minimum while
keeping the train network diffuse. Near that minimum it has either roughly `0.789D`
singleton trains or a quadratic rhombic Mantel deficit together with a linear
rhombic-pentagon interface.

---

## 1. Exact route/perimeter conservation

The Type-II route/train identity is finite and exact:

\[
\boxed{b+P_{\rm exc}=2T.}
\tag{1.1}
\]

The matched all-train theorem gives

\[
\boxed{
\frac{T-q/2}{D}\ge2s_2+g-o(1).
}
\tag{1.2}
\]

On the terminal branch

\[
\pi D-q=o(D).
\tag{1.3}
\]

Also every force-hull side joins two source points, so

\[
q\le\operatorname{per}(F)\le\pi D.
\]

Hence

\[
\operatorname{per}(F)-q=o(D).
\tag{1.4}
\]

Subtract `per(F)` from (1.1) and use (1.2):

\[
\begin{aligned}
\lambda_D+P_{\rm exc}
&=2T-\operatorname{per}(F)\\
&\ge q+(4s_2+2g-o(1))D-\operatorname{per}(F)\\
&=(M_g-o(1))D.
\end{aligned}
\]

This proves (TP.4), and (TP.5) follows by the elementary minimax
`max(x,y)>=(x+y)/2`.

The sum (TP.4) is sharp for the relaxed terminal scalar system. The equal split
`lambda=P_exc=M_g/2` is feasible at

\[
t=\frac{4\pi+3\gamma_g}{5},
\qquad
\frac fD=\frac QD=\frac{M_g}{10},
\]

where

\[
\gamma_g:=2s_2-\frac\pi2+g.
\]

So no larger universal constant in (TP.5) follows from the same scalar inputs alone.

---

## 2. The terminal train slack is `pi/2+g`

The modern stopped-train slack is

\[
\tau_D:=(q-k)+2f-2\sqrt{R_4}.
\tag{2.1}
\]

The exact stopped-train identity

\[
T=q+2f-k
\tag{2.2}
\]

therefore gives

\[
\boxed{\tau_D=T-2\sqrt{R_4}.}
\tag{2.3}
\]

Canonical Type-II rhombus saturation gives

\[
\frac{\sqrt{R_4}}D\to s_2.
\tag{2.4}
\]

From (1.2) and terminality,

\[
\frac TD
\ge\frac\pi2+2s_2+g-o(1).
\]

Subtract `2s_2` using (2.3)–(2.4):

\[
\boxed{
\frac{\tau_D}{D}\ge\frac\pi2+g-o(1)=\tau_g-o(1).
}
\tag{2.5}
\]

This proves (TP.6). It is substantially larger than the `0.7467921D` train-slack
floor used by the older `t<=1.8623` pentagon/train package; no bounded-`t` hypothesis
is needed here beyond the terminal FREE branch itself.

---

## 3. Singleton versus rhombic-train slack

The exact stopped-train decomposition is

\[
\boxed{
\rho_{\rm rec}=2S_D,
\qquad
2\tau_D=\rho_{\rm rec}+\sigma_R.
}
\tag{3.1}
\]

If

\[
\rho_{\rm rec}\ge(\tau_g-o(1))D,
\]

then

\[
S_D\ge(\tau_g/2-o(1))D,
\]

which is (TP.7).

Otherwise, (2.5) and (3.1) give

\[
\sigma_R
=2\tau_D-\rho_{\rm rec}
\ge(\tau_g-o(1))D,
\]

which is (TP.8).

Let `T_R` be the non-singleton strict-rhombus stopped-train count. The exact
rhombic-train relation is

\[
\sigma_R=2T_R-4\sqrt{R_4},
\]

so

\[
\frac{T_R^2}{4}-R_4
=\frac{\sigma_R\sqrt{R_4}}2+\frac{\sigma_R^2}{16}.
\tag{3.2}
\]

Use (2.4) and (TP.8). The normalized lower bound is

\[
\frac{\tau_gs_2}{2}+\frac{\tau_g^2}{16}
=0.907344013935981\ldots,
\]

proving (TP.9).

---

## 4. Stability of the classwise endpoint forces pentagons

Write

\[
F_D:=\frac fD,
\qquad
\bar Q_D:=\frac QD,
\qquad
L_D:=\frac{\lambda_D}{D}.
\]

Set

\[
r_D:=Q-f=\sum_{C\,\mathrm{exc}}(\deg C-5)\ge0.
\tag{4.1}
\]

Then exactly

\[
\frac{E_{\rm exc}}D=3F_D+\frac{r_D}{D},
\qquad
\frac{P_{\rm exc}}D=5F_D+\frac{r_D}{D}.
\tag{4.2}
\]

The constant in the existing classwise theorem satisfies

\[
C_g=\frac{3M_g}{8}.
\tag{4.3}
\]

Assume (TP.10). From (TP.4),

\[
\frac{P_{\rm exc}}D
\ge M_g-C_g-\varepsilon-o(1)
=\frac{5M_g}{8}-\varepsilon-o(1),
\]

which proves (TP.11).

Subtract the two equations in (4.2):

\[
\frac{P_{\rm exc}-E_{\rm exc}}D=2F_D.
\]

Using (TP.11) and the upper bound on `E_exc` in (TP.10),

\[
2F_D
\ge\frac{M_g}{4}-2\varepsilon-o(1),
\]

hence

\[
F_D\ge\frac{M_g}{8}-\varepsilon-o(1).
\tag{4.4}
\]

Now use `E_exc/D=3F_D+r_D/D` together with (TP.10) and (4.4):

\[
\frac{r_D}{D}
\le C_g+\varepsilon
-3\left(\frac{M_g}{8}-\varepsilon\right)+o(1)
=4\varepsilon+o(1).
\tag{4.5}
\]

Equations (4.4)–(4.5) prove (TP.12).

Let `P_5` be the number of bounded pentagonal contact faces. Degree arithmetic gives

\[
P_5\ge2f-Q=f-(Q-f)=f-r_D.
\tag{4.6}
\]

Insert (4.4)–(4.5):

\[
\frac{P_5}{D}
\ge\frac{M_g}{8}-5\varepsilon-o(1),
\]

which proves (TP.13). At `epsilon=0`, `M_g/8=0.478083153431979...`, proving
(TP.14).

Thus the scalar minimizer is not merely “exceptional-face heavy.” It is
pentagon-dominated: the total superpentagonal degree excess `Q-f` is sublinear.

---

## 5. Rhombic branch forces a pentagon interface near the scalar endpoint

Let `I_5` count boundary occurrences having a strict rhombus on one side and a bounded
pentagon on the other. The exact occurrence argument from the stopped-train/pentagon
ledger gives

\[
\boxed{
I_5\ge5(2f-Q)-\rho_{\rm rec}.
}
\tag{5.1}
\]

For completeness, `2f-Q=f-r_D`, so (4.4)–(4.5) imply

\[
\frac{2f-Q}{D}
\ge\frac{M_g}{8}-5\varepsilon-o(1).
\tag{5.2}
\]

In the rhombic branch selected in Section 3,

\[
\rho_{\rm rec}< (\tau_g+o(1))D.
\]

Insert this and (5.2) into (5.1):

\[
\frac{I_5}{D}
\ge
\frac{5M_g}{8}-\tau_g-25\varepsilon-o(1).
\tag{5.3}
\]

The constant is

\[
\frac{5M_g}{8}-\tau_g
=0.811912440364997\ldots .
\]

This proves (TP.15). It stays positive exactly for

\[
\varepsilon<0.0324764976145998\ldots .
\]

Every non-singleton stopped train has only two terminal occurrences, so the number of
distinct rhombic trains terminating at pentagons is at least `I_5/2`. Every pentagon
has five boundary occurrences, so the number of distinct pentagons touching a strict
rhombus is at least `I_5/5`. These are (TP.16)–(TP.17).

---

## 5.1 A linear family of empty multi-rhombic pentagons

The incidence lower bound also forces a genuinely local geometric population. Let

\[
X_2:=\#\{P\text{ pentagonal}:d_R(P)\ge2\},
\]

where `d_R(P)` is the number of sides of `P` whose opposite face is a strict
rhombus. Since pentagons outside `X_2` contribute at most one rhombic incidence and
members of `X_2` contribute at most five,

\[
I_5\le P_5+4X_2.
\]

Every pentagon contributes one unit to `Q`, so `P_5<=Q`. Therefore

\[
\boxed{X_2\ge\frac{I_5-Q}{4}.}
\tag{5.4}
\]

Under the balanced hypotheses (TP.10), (4.4) and
`E_exc=Q+2f<= (C_g+epsilon+o(1))D` give

\[
\frac QD
\le C_g+\varepsilon
-2\left(\frac{M_g}{8}-\varepsilon\right)+o(1)
=\frac{M_g}{8}+3\varepsilon+o(1).
\tag{5.5}
\]

Combine (5.4), (5.5), and (TP.15):

\[
\boxed{
\frac{X_2}{D}
\ge
\frac{2s_2-\pi/2}{4}
-7\varepsilon-o(1)
=
0.083457321733255\ldots-7\varepsilon-o(1).
}
\tag{5.6}
\]

The cancellation of `g` in (5.6) is exact. The lower bound stays positive for

\[
\varepsilon<0.0119224745333221\ldots .
\tag{5.7}
\]

The isolate-host theorem says that a bounded contact face containing a source point
in its interior has degree at least seven. Hence every pentagon counted by `X_2` is
source-empty. Thus, near the balanced terminal endpoint, the rhombic branch contains
at least

\[
\boxed{(0.083457321733255\ldots-7\varepsilon-o(1))D}
\]

actual empty convex unit-edge pentagons with at least two strict-rhombus neighbors.
This extends the multi-rhombic-pentagon object beyond the old `t<=1.8623` range; the
price is a smaller coefficient and the balanced-interface hypothesis.

---

## 6. Resulting terminal FREE normal form

Fix a small `epsilon>0`. Every terminal FREE survivor now falls into at least one of
four concrete regimes:

1. **outer-heavy:**
   `lambda_D >= (C_g+epsilon-o(1))D`;
2. **exceptional-heavy:**
   `Q+2f >= (C_g+epsilon-o(1))D`;
3. **balanced/singleton:** both interface classes are within `epsilon D` of the scalar
   minimum, but `S_D >= (0.7892516633...-o(1))D`;
4. **balanced/rhombic-pentagon:** both interface classes are within `epsilon D` of the
   scalar minimum, while the strict-rhombus train graph has at least
   `(0.9073440139...-o(1))D^2` Mantel deficit and, for
   `epsilon<0.03247649...`, at least
   `(0.8119124403...-25epsilon-o(1))D` rhombus/pentagon boundary incidences.

The fourth branch has a linear family of pentagon-ending rhombic trains even though
the older pentagon-sea theorem was restricted to `t<=1.8623`. The present statement
uses terminality and the matched all-train gap instead of that bounded-`t` hypothesis.

This still does not close C-II. The remaining geometry is now more explicit:

- the outer-heavy branch needs a terminal near-disk upper budget or a
  source-preserving diameter descent for the actual outer-walk detour;
- the exceptional-heavy branch needs localization of the large **global**
  `P_exc` occurrence currency into the harmonic-cell Sections 122–123 ledger;
- the singleton branch needs a flex/endpoint argument for roughly `0.789D` contact
  edges which terminate no rhombus train;
- the balanced rhombic branch needs to route the linear pentagon-ending train family
  against the terminal FREE reflection structure or show that its quadratic Mantel
  deficit is incompatible with the same first-order rhombus-count deficit.

No theorem-state promotion is claimed.

**Disposition:** proved terminal route/perimeter conservation, a `pi/2+g` stopped-train
slack floor, the resulting strong singleton/rhombic dichotomy, and a stable
pentagon-interface normal form near the current classwise endpoint. C-II remains
open.
