<!-- theorem-state: {"artifact_id":"ART-326DC0CF7AC1","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — exact detour/defect coupling raises the pinned/contact floor to 0.4673

**Date:** 2026-09-09  
**Repository base:** current PR #138 branch after PC/WD/WE  
**Run type:** exact-defect asymptotic branch exclusion  
**Target:** Target C C-II after PI/JC/PC/WD  
**LEVEL I STATUS:** STILL OPEN

WE proved

\[
\liminf\frac{e_{BB}+2s_C}{D}\ge0.4658
\]

by discarding the negative `Q,s_Z,d_H,c_B` terms in the near-equality cavity ledger.  Those losses are avoidable.  The actual-perimeter JC identity and PC exact remainder show that every one of those defects also consumes the same small near-equality budget `R(lambda)`.

Keeping that coupling gives

\[
\boxed{
\liminf_{D\to\infty}
\frac{e_{BB}+2s_C}{D}
\ge0.4673.
}
\tag{ED.1}
\]

The improvement is still not claimed optimal, but it is no longer a fourth-decimal perturbation of the original JC threshold: the surviving scalar interval has been cut by about `0.004` above JC and about `0.0025` above GS.

---

## 1. Normalized variables

Pass to a convergent post-ZF subsequence and put

\[
\lambda:=\lim\frac{e_{BB}+2s_C}{D},
\qquad
t:=\lim\frac{e_{BB}}D,
\tag{ED.2}
\]

\[
y:=\lim\frac hD,
\qquad
p:=\lim\frac{P_F}D,
\qquad
u:=\lim\frac QD,
\tag{ED.3}
\]

\[
d:=\lim\frac{d_H}{D},
\qquad
s:=\lim\frac{s_Z}{D},
\qquad
c:=\lim\frac{c_B}{D}.
\tag{ED.4}
\]

All these quantities are nonnegative, and

\[
0\le t\le\lambda,
\qquad
p\le\pi,
\qquad
p\ge q/D\ge y.
\tag{ED.5}
\]

Define as before

\[
A_{PI}:=\frac12\sin(2\rho),
\qquad
L(\lambda):=A_{PI}-\frac\pi4\lambda^2,
\tag{ED.6}
\]

and

\[
R(\lambda)
:=
\lambda+\frac\pi2
-2\sqrt{\pi L(\lambda)}.
\tag{ED.7}
\]

PI/GU gives

\[
\liminf\frac G{D^2}\ge L(\lambda).
\tag{ED.8}
\]

---

## 2. Exact JC pocket/face perimeter currency

PC gives

\[
a=q-e_{BB}+c_B
\tag{ED.9}
\]

and

\[
x_B=q-Q-2(d_H+s_Z).
\tag{ED.10}
\]

OP's exact pocket-perimeter excess is

\[
E_{out}=x_B+P_F-q-a.
\tag{ED.11}
\]

Substitute ED.9-ED.10:

\[
\begin{aligned}
E_{out}+Q
&=P_F-q-2(d_H+s_Z)+e_{BB}-c_B\\
&=P_F-h+e_{BB}-3d_H-2s_Z-c_B.
\end{aligned}
\]

Thus the exact finite identity is

\[
\boxed{
E_{out}+Q
=P_F-h+e_{BB}-3d_H-2s_Z-c_B.
}
\tag{ED.12}
\]

JC used the corresponding upper bound after dropping the final nonnegative terms.  Here they are retained.

The pocket/exceptional-face isoperimetric argument gives

\[
H_{out}+A_{exc}
\le
\frac{(E_{out}+Q)^2}{4\pi}+o(D^2).
\tag{ED.13}
\]

ZG/GU gives

\[
G\le H_{out}+A_{exc}+O(D).
\tag{ED.14}
\]

Therefore ED.8, ED.12-ED.14 imply

\[
L(\lambda)
\le
\frac{(p-y+t-3d-2s-c)^2}{4\pi}.
\tag{ED.15}
\]

The quantity in parentheses is nonnegative because its finite predecessor is `E_out+Q`.

---

## 3. Exact near-equality budget

Write

\[
z:=y-\frac\pi2,
\qquad
\varepsilon:=\pi-p\ge0,
\qquad
r:=\lambda-t\ge0.
\tag{ED.16}
\]

Taking square roots in ED.15 and rearranging gives

\[
\boxed{
z+\varepsilon+r+3d+2s+c
\le R(\lambda).
}
\tag{ED.17}
\]

This is the exact-defect strengthening of DE/WE's

\[
z+\varepsilon\le R(\lambda).
\]

Every loss of direct loaded-contact density (`r`), every diameter tree-component defect, every extra mixed-row dependence, and every non-hull loaded-loaded contact spends the same near-JC-equality budget.

Since `epsilon>=0`, ED.17 also gives

\[
z\le R-r-3d-2s-c.
\tag{ED.18}
\]

---

## 4. Exact chain and detour bounds

WD/OD gives

\[
L_{chain}
=2h-Q-2s_Z-e_{BB}+c_B.
\tag{ED.19}
\]

Normalize and substitute `t=lambda-r`:

\[
\frac{L_{chain}}D
=\pi+2z-\nu-2s-\lambda+r+c.
\tag{ED.20}
\]

Apply ED.18:

\[
\begin{aligned}
\frac{L_{chain}}D
&\le
\pi+2R-\lambda-\nu-r-6d-6s-c.
\end{aligned}
\]

Hence

\[
\boxed{
\frac{L_{chain}}D
\le
\pi+2R(\lambda)-\lambda-\nu.
}
\tag{ED.21}
\]

The total chain-chord detour is

\[
U_{det}
=b-P_F
=2h-Q-2s_Z-P_F.
\tag{ED.22}
\]

Thus

\[
\frac{U_{det}}D
=2z+\varepsilon-\nu-2s.
\tag{ED.23}
\]

From ED.17 and `epsilon>=0`,

\[
2z+\varepsilon
=z+(z+\varepsilon)
\le2R-2r-6d-4s-2c.
\]

Therefore

\[
\boxed{
\frac{U_{det}}D
\le
2R(\lambda)-\nu.
}
\tag{ED.24}
\]

Since `U_det>=0`, necessarily

\[
\boxed{0\le\nu\le2R(\lambda).}
\tag{ED.25}
\]

The important new feature is the explicit `-lambda` in ED.21.  It survives because any attempt to recover chain length through non-hull loaded contacts `c_B` is paid twice through the exact JC budget ED.17.

---

## 5. Joint outer-pocket / exceptional-face capacity

WD gives

\[
H_{out}
\le
C_W L_{chain}^{3/2}U_{det}^{1/2},
\qquad
C_W:=\frac{\sqrt2}{\pi}.
\tag{ED.26}
\]

CC gives

\[
\limsup\frac{A_{exc}}{D^2}
\le\frac{\nu^2}{4\pi}.
\tag{ED.27}
\]

Using ED.21, ED.24, define for fixed `lambda` and `R=R(lambda)`

\[
\boxed{
F_{\lambda,R}(\nu)
:=
C_W(\pi+2R-\lambda-\nu)^{3/2}
(2R-\nu)^{1/2}
+\frac{\nu^2}{4\pi},
}
\tag{ED.28}
\]

for

\[
0\le\nu\le2R.
\]

Then every survivor must satisfy

\[
\boxed{
L(\lambda)
\le
\max_{0\le\nu\le2R(\lambda)}F_{\lambda,R(\lambda)}(\nu).
}
\tag{ED.29}
\]

---

## 6. In the relevant range, exceptional-face density only hurts

We now show that the maximum in ED.29 occurs at `nu=0` throughout the interval needed for ED.1.

Put

\[
A:=\pi+2R-\lambda,
\qquad
B:=2R.
\]

For `0<=nu<B`, differentiation gives

\[
\begin{aligned}
F'(\nu)
={}&-
\frac{C_W}{2}
\sqrt{\frac{A-\nu}{B-\nu}}
\bigl(3(B-\nu)+(A-\nu)\bigr)
+\frac{\nu}{2\pi}.
\end{aligned}
\tag{ED.30}
\]

For every `nu in [0,B]`,

\[
A-\nu
\ge A-B
=\pi-\lambda,
\tag{ED.31}
\]

and

\[
B-\nu\le B,
\qquad
3(B-\nu)+(A-\nu)\ge A-\nu\ge\pi-\lambda.
\]

Therefore

\[
F'(\nu)
\le
-
\frac{C_W}{2}
\frac{(\pi-\lambda)^{3/2}}{\sqrt B}
+rac{B}{2\pi}.
\tag{ED.32}
\]

For `lambda<=0.4673`, monotonicity of `R` gives

\[
R\le R(0.4673)
=0.0129957122\ldots,
\]

so

\[
B<0.026.
\tag{ED.33}
\]

Also

\[
\pi-\lambda>2.674.
\]

Using `C_W=sqrt(2)/pi`, the negative term in ED.32 has magnitude greater than `6`, whereas

\[
\frac{B}{2\pi}<0.005.
\]

Thus

\[
\boxed{F'(\nu)<0}
\tag{ED.34}
\]

throughout the entire interval.  Hence

\[
\boxed{
\max_{0\le\nu\le2R}F_{\lambda,R}(\nu)
=F_{\lambda,R}(0)
=C_W(\pi+2R-\lambda)^{3/2}\sqrt{2R}.
}
\tag{ED.35}
\]

So a positive linear exceptional-face degree cannot rescue the near-threshold state: it reduces the available contact-chain and detour budgets faster than its own `Q^2` area term grows.

---

## 7. One-variable necessary condition

Combining ED.29 and ED.35, every survivor with `lambda<=0.4673` must satisfy

\[
\boxed{
L(\lambda)
\le
V(\lambda)
:=
\frac{\sqrt2}{\pi}
\bigl(\pi+2R(\lambda)-\lambda\bigr)^{3/2}
\sqrt{2R(\lambda)}.
}
\tag{ED.36}
\]

As in DE/WE,

\[
L'(\lambda)<0,
\qquad
R'(\lambda)>0.
\]

Moreover

\[
\frac{d}{d\lambda}
\bigl(\pi+2R(\lambda)-\lambda\bigr)
=2R'(\lambda)-1>0.
\]

Hence `V(lambda)` is increasing wherever `R>=0`.  It is enough to check the endpoint `lambda=0.4673`.

---

## 8. Endpoint `lambda_*=0.4673`

At

\[
\lambda_*=0.4673,
\]

using the established PI constant gives

\[
\boxed{
L(\lambda_*)
=0.32634979701580624\ldots,
}
\tag{ED.37}
\]

\[
\boxed{
R(\lambda_*)
=0.01299571220274531\ldots,
}
\tag{ED.38}
\]

and

\[
\boxed{
V(\lambda_*)
=0.32202852957119010\ldots .
}
\tag{ED.39}
\]

Thus

\[
\boxed{
L(\lambda_*)-V(\lambda_*)
=0.00432126744461614\ldots>0.
}
\tag{ED.40}
\]

This contradicts ED.36.  By the monotonicity in Section 7, every smaller `lambda` is also excluded.  Therefore ED.1 holds.

---

## 9. What the optimizer geometry now says without using an optimizer

The proof itself identifies the direction in which the surviving near-threshold state must move:

- `t=e_BB/D` must approach `lambda`; pinned stress `s_C` cannot absorb much of the currency;
- `d_H/D`, `s_Z/D`, and `c_B/D` must be small because each consumes ED.17;
- `Q/D` is driven to zero by the strict monotonicity ED.34;
- `h/D` must lie slightly above `pi/2` while `P_F/D` is close to `pi`, because the required outer-pocket area needs nonzero detour but JC penalizes moving too far from the perimeter maximum.

These are consequences of the inequalities, not a claim that the exact extremizer exists.

---

## 10. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| exact identity ED.12 | proved | OP/PC/ZT substitution |
| exact budget ED.17 | proved asymptotically | PI/GU lower + JC exact currency |
| chain bound with `-lambda`, ED.21 | proved | WD exact formula + ED.17 |
| detour bound ED.24 | proved | same budget |
| `F(nu)` strictly decreasing for `lambda<=0.4673` | proved | elementary derivative bound with wide margin |
| one-variable condition ED.36 | proved | WD + CC + monotonicity in `nu` |
| explicit floor `0.4673` | proved asymptotically | endpoint margin `>0.0043` |
| optimal PC/WD/JC constant | not claimed | further `h/D` and PI dependence remains |
| Level I | still open | high-surplus global geometry remains |

---

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Exact JC/PC currency:
    E_out+Q = P_F-h+e_BB-3d_H-2s_Z-c_B.
Let lambda=(e_BB+2s_C)/D,
    t=e_BB/D,
    y=h/D, p=P_F/D,
    z=y-pi/2, epsilon=pi-p,
    r=lambda-t,
    d=d_H/D, s=s_Z/D, c=c_B/D,
    nu=Q/D.
PI/GU + JC imply
    z+epsilon+r+3d+2s+c <= R(lambda),
    R=lambda+pi/2-2sqrt(pi[A_PI-(pi/4)lambda^2]).

Then PC/WD give
    L_chain/D <= pi+2R-lambda-nu,
    U_det/D   <= 2R-nu,
    0<=nu<=2R.
Therefore
    G/D^2 <=
      max_nu { (sqrt2/pi)(pi+2R-lambda-nu)^(3/2)(2R-nu)^(1/2)
               +nu^2/(4pi) }.
For lambda<=0.4673 the expression is strictly decreasing in nu, so nu=0 is worst.
Thus every survivor would need
    A_PI-(pi/4)lambda^2
      <= (sqrt2/pi)(pi+2R-lambda)^(3/2)sqrt(2R).
At lambda=0.4673:
    LHS=0.32634979701580624...,
    RHS=0.32202852957119010...,
    gap=0.00432126744461614...>0.
Hence
    liminf (e_BB+2s_C)/D >= 0.4673.
```
