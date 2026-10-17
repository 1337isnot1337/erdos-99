> Generated reading edition · [exact source](../../../docs/reports/target_c_detour_explicit_surplus_0465_2026-09-09.md) · source SHA-256 `dc80e0590301dfdb71ba1a8895df7e6de9044c6550844fd45a77eb01a6da8bbb`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-E3A79F8C7B57","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — pocket detour raises the explicit pinned/contact floor to 0.465

**Date:** 2026-09-09  
**Repository base:** current `research/target-c-pocket-detour-area-2026-09-09` after OD  
**Run type:** explicit asymptotic branch exclusion  
**Target:** Target C C-II after PI/JC/GS/PC/OD  
**Depends on:** PI area floor, GU attachment-cell bound, JC joint cavity budget, CC exceptional-face area bound, PC exact pocket ledger, OD detour-area theorem  
**External input:** none beyond the dependencies already present in `main`  
**LEVEL I STATUS:** STILL OPEN

The current explicit post-ZF bound from GS is

```math
\liminf\frac{e_{BB}+2s_C}{D}
\ge0.4647922503\ldots .
```

OD supplies an independent geometric restriction on the same near-threshold cavity regime: quadratic outer-pocket area requires a linear excess of the unit-contact outer-walk length over the true force-hull perimeter.

Combining OD with the actual-perimeter form of JC gives the clean explicit improvement

```math
\boxed{
\liminf_{D\to\infty}
\frac{e_{BB}+2s_C}{D}
\ge0.465.
}
\tag{DE.1}
```

No quantitative constant-width stability theorem is needed for DE.1.  The gain over GS is small but rigorous, and the derivation exposes a new scalar `R(lambda)` measuring how close any near-threshold survivor must be simultaneously to `h/D=pi/2` and `per(F)/D=pi`.

---

## 1. Normalized variables and the PI/GU gap floor

Along an arbitrary unbounded post-ZF survivor sequence, pass to a subsequence on which

```math
\lambda
:=\lim\frac{e_{BB}+2s_C}{D}
```

exists.  If necessary pass further so the bounded normalized quantities below also converge. Put

```math
t:=\lim\frac{e_{BB}}D,
\qquad
y:=\lim\frac hD,
\qquad
p:=\lim\frac{P_F}D,
\qquad
u:=\lim\frac QD,
\tag{DE.2}
```

where `P_F=per(F)`. Then

```math
0\le t\le\lambda,
\qquad 0\le p\le\pi.
\tag{DE.3}
```

Also `P_F>=q>=h`, because the `q` consecutive hull sides are unit-separated and `h<=q`. Hence

```math
0\le y\le p.
\tag{DE.4}
```

PI gives

```math
A_{PI}:=rac12\sin(2\rho)
=0.4978566363242109995\ldots,
\tag{DE.5}
```

where `rho=cos rho=0.7390851332...`.

GU's attachment-cell estimate gives the relaxed asymptotic lower bound

```math
\boxed{
\liminf\frac G{D^2}
\ge
L(\lambda)
:=A_{PI}-\frac\pi4\lambda^2.
}
\tag{DE.6}
```

The exact ZK form only strengthens DE.6 when `d_H+s_Z>0`; the relaxation is sufficient here.

---

## 2. JC forces a small combined perimeter/density deviation

The actual-perimeter form of JC gives

```math
E_{out}+Q
\le
 e_{BB}+\min\{h,P_F-h\}
\le e_{BB}+P_F-h.
\tag{DE.7}
```

JC's joint isoperimetric estimate and the ZG/GU charging relation therefore give

```math
\limsup\frac G{D^2}
\le
\frac{(t+p-y)^2}{4\pi}.
\tag{DE.8}
```

Since `t<=lambda`, every survivor limit must satisfy

```math
L(\lambda)
\le
\frac{(\lambda+p-y)^2}{4\pi}.
\tag{DE.9}
```

The quantity in parentheses is nonnegative by DE.3-DE.4. Taking square roots gives

```math
y-p
\le
\lambda-2\sqrt{\pi L(\lambda)}.
\tag{DE.10}
```

Define

```math
\boxed{
R(\lambda)
:=
\lambda+\frac\pi2
-2\sqrt{\pi L(\lambda)}.
}
\tag{DE.11}
```

Write

```math
z:=y-\frac\pi2,
\qquad
\varepsilon:=\pi-p\ge0.
\tag{DE.12}
```

Then DE.10 is exactly

```math
\boxed{z+\varepsilon\le R(\lambda).}
\tag{DE.13}
```

If `R(lambda)<0`, no survivor is possible already.  Otherwise `epsilon>=0` gives

```math
z\le R(\lambda)
\tag{DE.14}
```

and therefore

```math
\boxed{2z+\varepsilon\le2R(\lambda).}
\tag{DE.15}
```

This is the key scalar consequence of the JC lower/upper comparison.

---

## 3. Convert DE.15 into an outer-pocket area bound

OD gives the exact post-ZF formulas

```math
L_{chain}
=2h-Q-2s_Z-e_{BB}+c_B,
\tag{DE.16}
```

```math
U_{det}
=b-P_F
=2h-Q-2s_Z-P_F.
\tag{DE.17}
```

PC gives

```math
e_{BB}=d_P+Q+2(d_H+s_Z)+c_B,
```

so in particular

```math
c_B\le e_{BB}-Q.
\tag{DE.18}
```

Divide DE.16 by `D`, use DE.18, and discard nonpositive terms:

```math
\begin{aligned}
\limsup\frac{L_{chain}}D
&\le
2y-\nu-t+(t-\nu)\\
&=2y-2\nu\\
&\le\pi+2R(\lambda)-2\nu.
\end{aligned}
\tag{DE.19}
```

Similarly DE.17 gives

```math
\begin{aligned}
\limsup\frac{U_{det}}D
&\le
2y-\nu-p\\
&=2z+\varepsilon-\nu\\
&\le2R(\lambda)-\nu.
\end{aligned}
\tag{DE.20}
```

Since `U_det>=0`, DE.20 also implies

```math
\boxed{0\le\nu\le2R(\lambda).}
\tag{DE.21}
```

OD states

```math
H_{out}
\le
C_E L_{chain}^{3/2}U_{det}^{1/2},
\qquad
C_E:=\frac\pi{4\sqrt2}.
\tag{DE.22}
```

Using DE.19-DE.20 and then relaxing the negative `nu` terms gives

```math
\boxed{
\limsup\frac{H_{out}}{D^2}
\le
C_E
(\pi+2R)^{3/2}
\sqrt{2R}.
}
\tag{DE.23}
```

where `R=R(lambda)`.

---

## 4. Exceptional bounded faces are also tiny in this regime

CC proves

```math
A_{exc}
\le
\frac{Q^2+O(Q)}{4\pi}.
\tag{DE.24}
```

Together with DE.21,

```math
\boxed{
\limsup\frac{A_{exc}}{D^2}
\le
\frac{R(\lambda)^2}{\pi}.
}
\tag{DE.25}
```

ZG/GU charges the full attachment-cell gap by the outer pockets and exceptional bounded faces up to `O(D)`:

```math
G\le H_{out}+A_{exc}+O(D).
\tag{DE.26}
```

Therefore every survivor limit must satisfy

```math
\boxed{
L(\lambda)
\le
U(\lambda)
:=
C_E(\pi+2R(\lambda))^{3/2}\sqrt{2R(\lambda)}
+rac{R(\lambda)^2}{\pi}.
}
\tag{DE.27}
```

This is the new one-variable necessary condition.

---

## 5. Monotonicity on the required interval

We only need to exclude `lambda<0.465`.

On the interval where `L(lambda)>0`,

```math
L'(\lambda)=-\frac\pi2\lambda<0.
\tag{DE.28}
```

From DE.11,

```math
R'(\lambda)
=1+
\frac{\pi^2\lambda}{2\sqrt{\pi L(\lambda)}}
>0.
\tag{DE.29}
```

The right side `U(lambda)` in DE.27 is an increasing function of nonnegative `R`, while `R(lambda)` is increasing. Hence `U(lambda)` increases with `lambda`.

Therefore, for every `lambda<=0.465`,

```math
L(\lambda)\ge L(0.465),
\qquad
U(\lambda)\le U(0.465),
\tag{DE.30}
```

whenever `R(lambda)>=0`; if `R(lambda)<0`, DE.13 is already impossible.

It is enough to check the endpoint `lambda=0.465`.

---

## 6. Explicit endpoint check

Using the established value of `rho`,

```math
A_{PI}
=0.4978566363242109995909\ldots .
```

At

```math
\lambda_*=0.465
```

we obtain

```math
\boxed{
L(\lambda_*)
=0.3280339184435977388443\ldots,
}
\tag{DE.31}
```

```math
\boxed{
R(\lambda_*)
=0.0054771909833069851608\ldots,
}
\tag{DE.32}
```

and

```math
\boxed{
U(\lambda_*)
=0.3253673216023899578757\ldots .
}
\tag{DE.33}
```

Thus

```math
\boxed{
L(\lambda_*)-U(\lambda_*)
=0.0026665968412077809686\ldots>0.
}
\tag{DE.34}
```

This contradicts the necessary condition DE.27. By the monotonicity in Section 5, every smaller nonnegative `lambda` is excluded as well.

Hence no unbounded survivor sequence can have a subsequential limit below `0.465`. This proves DE.1.

The margin in DE.34 is over `2.6e-3`, much larger than the displayed decimal truncation.

---

## 7. Relation to GS and JN

GS gives the previous explicit floor

```math
0.4647922503\ldots .
```

using Groemer's quantitative stability theorem for near-maximal-perimeter convex bodies. DE instead uses the internal geometry of the OP pockets and raises the floor to the simple decimal `0.465`.

JN proved qualitatively that the old JC threshold `0.463316895...` is not attainable. DE explains one direct mechanism behind that nonattainment: near the JC equality point, `y` and `p` must make the total chain–chord detour tiny, and then OD leaves too little outer-pocket area to carry the PI/GU attachment gap.

DE does not supersede the constant-width interpretation of JN/GS. It gives an independent quantitative restriction that can be combined with those stability inputs in later optimization.

---

## 8. Regressions and limits

- `R(lambda)` is a **derived near-equality budget**, not a new independent defect variable.
- The proof deliberately relaxes `L_chain` by dropping negative `Q,s_Z` terms; retaining them can improve the numerical constant.
- DE.25 treats all exceptional-face area by the crude `Q^2` bound. Correlations between `Q` and the chain detour are also discarded.
- The simple constant `0.465` is not claimed optimal for OD+JC. A tighter multi-variable optimization can raise it.
- The regular odd-shell regression lies in a much larger loaded-contact regime and is unaffected.
- LEVEL I remains open: DE only raises the mandatory linear pinned/contact currency.

---

## 9. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| JC implies `z+epsilon<=R(lambda)` | proved | PI/GU lower gap + JC actual-perimeter upper gap |
| `Q/D<=2R(lambda)` | proved asymptotically | OD detour nonnegativity + DE.15 |
| outer-pocket bound DE.23 | proved | OD + PC exact chain formula |
| exceptional-face bound DE.25 | proved | CC + preceding `Q` bound |
| one-variable necessary condition DE.27 | proved | ZG/GU charging |
| monotonic endpoint reduction | proved | elementary derivatives |
| explicit `lambda>=0.465` | proved asymptotically | DE.34 has positive numerical margin |
| optimal OD+JC constant | not claimed | several relaxations remain |
| Level I | still open | high-surplus coexistence remains |

---

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Let lambda=(e_BB+2s_C)/D and
    L(lambda)=A_PI-(pi/4)lambda^2.
JC + PI/GU imply, with y=h/D and p=per(F)/D,
    L(lambda) <= (lambda+p-y)^2/(4pi).
Writing z=y-pi/2 and epsilon=pi-p gives
    z+epsilon <= R(lambda),
where
    R(lambda)=lambda+pi/2-2sqrt(pi L(lambda)).
Hence
    2z+epsilon <= 2R.

PC + OD then give
    L_chain/D <= pi+2R-2(Q/D),
    U_det/D   <= 2R-(Q/D),
so
    H_out/D^2 <= [pi/(4sqrt2)](pi+2R)^(3/2)sqrt(2R).
Also Q/D<=2R and
    A_exc/D^2 <= R^2/pi.
Thus every survivor must satisfy
    L(lambda) <= [pi/(4sqrt2)](pi+2R)^(3/2)sqrt(2R)+R^2/pi.

At lambda=0.465:
    L=0.3280339184435977...,
    R=0.0054771909833070...,
    RHS=0.3253673216023900...,
so L-RHS=0.0026665968412078...>0.
Monotonicity excludes every smaller lambda.
Therefore
    liminf (e_BB+2s_C)/D >= 0.465.
```
