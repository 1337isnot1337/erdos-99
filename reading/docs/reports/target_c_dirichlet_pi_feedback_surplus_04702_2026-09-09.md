> Generated reading edition · [exact source](../../../docs/reports/target_c_dirichlet_pi_feedback_surplus_04702_2026-09-09.md) · source SHA-256 `2d45b04e49b6b9279893e22e46f2c841afe7e77733ebe3f80e29a0ee77da8c72`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-4475F0949018","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Dirichlet pocket functional plus PI feedback raises the surplus floor to 0.4702

**Date:** 2026-09-09  
**Repository base:** current `research/target-c-sharp-pocket-functional-2026-09-09` after DD  
**Run type:** explicit finite-bootstrap exclusion  
**Target:** Target C C-II after PI/JC/PC/DD  
**LEVEL I STATUS:** STILL OPEN

The merged PF theorem gives

$$
\liminf\frac{e_{BB}+2s_C}{D}\ge0.4694
$$

using the WD outer-pocket constant `sqrt(2)/pi`.  DD replaces that constant by the stronger self-contained value `1/sqrt(6)`.

Running the same two finite PI/detour feedback steps gives

$$
\boxed{
\liminf_{D\to\infty}
\frac{e_{BB}+2s_C}{D}
\ge0.4702.
}
\tag{DP.1}
$$

No infinite bootstrap, numerical optimizer, or new external theorem is used.

---

## 1. Reuse the exact PF bootstrap

For a candidate subsequential limit

$$
\lambda:=\lim\frac{e_{BB}+2s_C}{D},
$$

define

$$
A_{PI}:=\frac12\sin(2\rho),
\qquad \rho=\cos\rho,
$$

and

$$
L_0(\lambda)
:=A_{PI}-\frac\pi4\lambda^2,
\tag{DP.2}
$$

$$
R_0(\lambda)
:=\lambda+\frac\pi2-2\sqrt{\pi L_0(\lambda)}.
\tag{DP.3}
$$

PF proves that this JC budget forces

$$
\left|\frac hD-\frac\pi2\right|\le R_0.
$$

The diameter-density form of PI then gives the improved force-hull area floor `cos(R_0)/2`.  Set

$$
L_1(\lambda)
:=\frac12\cos R_0(\lambda)-\frac\pi4\lambda^2,
\tag{DP.4}
$$

$$
R_1(\lambda)
:=\lambda+\frac\pi2-2\sqrt{\pi L_1(\lambda)}.
\tag{DP.5}
$$

Apply the same implication once more:

$$
L_2(\lambda)
:=\frac12\cos R_1(\lambda)-\frac\pi4\lambda^2,
\tag{DP.6}
$$

$$
R_2(\lambda)
:=\lambda+\frac\pi2-2\sqrt{\pi L_2(\lambda)}.
\tag{DP.7}
$$

These are two finite theorem applications, exactly as in PF.

---

## 2. Replace the WD cavity constant by DD

PF/ED's exact-defect reduction gives, with

$$
\nu:=\lim Q/D,
$$

$$
\frac{L_{chain}}D
\le\pi+2R_2-\lambda-\nu,
\tag{DP.8}
$$

$$
\frac{U_{det}}D
\le2R_2-\nu,
\qquad
0\le\nu\le2R_2.
\tag{DP.9}
$$

DD proves

$$
H_{out}
\le
\frac1{\sqrt6}
L_{chain}^{3/2}U_{det}^{1/2}.
\tag{DP.10}
$$

The exceptional-face bound remains

$$
\limsup\frac{A_{exc}}{D^2}
\le\frac{\nu^2}{4\pi}.
\tag{DP.11}
$$

Thus every survivor must satisfy

$$
L_2(\lambda)
\le
\max_{0\le\nu\le2R_2}
\left\{
\frac1{\sqrt6}
(\pi+2R_2-\lambda-\nu)^{3/2}
(2R_2-\nu)^{1/2}
+
\frac{\nu^2}{4\pi}
\right\}.
\tag{DP.12}
$$

---

## 3. Positive exceptional-face density still decreases the capacity

Put

$$
A:=\pi+2R_2-\lambda,
\qquad B:=2R_2,
$$

and

$$
F(\nu)
:=
\frac1{\sqrt6}(A-\nu)^{3/2}(B-\nu)^{1/2}
+
\frac{\nu^2}{4\pi}.
$$

For `0<=nu<B`,

$$
F'(\nu)
=-
\frac1{2\sqrt6}
\sqrt{\frac{A-\nu}{B-\nu}}
\bigl(3(B-\nu)+(A-\nu)\bigr)
+
\frac{\nu}{2\pi}.
\tag{DP.13}
$$

For `lambda<=0.4702`, the finite bootstrap is monotone and gives

$$
R_2\le R_2(0.4702)
=0.0160758902\ldots,
$$

so

$$
B<0.033.
$$

Also

$$
A-\nu\ge A-B=\pi-\lambda>2.67.
$$

Therefore the magnitude of the negative term in DP.13 is greater than `5`, whereas

$$
\frac{\nu}{2\pi}<0.006.
$$

Hence

$$
\boxed{F'(\nu)<0}
\tag{DP.14}
$$

throughout the relevant interval.  The maximum in DP.12 occurs at `nu=0`.

Every survivor with `lambda<=0.4702` must therefore satisfy

$$
\boxed{
L_2(\lambda)
\le
V_D(\lambda)
:=
\frac1{\sqrt6}
(\pi+2R_2(\lambda)-\lambda)^{3/2}
\sqrt{2R_2(\lambda)}.
}
\tag{DP.15}
$$

---

## 4. Monotonicity

PF proves inductively on the relevant interval that

- each `L_j(lambda)` is strictly decreasing;
- each `R_j(lambda)` is strictly increasing;
- in fact `R_j'(lambda)>1`.

Therefore

$$
\pi+2R_2(\lambda)-\lambda
$$

is increasing, so `V_D(lambda)` is increasing.  To exclude every `lambda<=lambda_*`, it is enough to test DP.15 at `lambda_*`.

---

## 5. Endpoint `lambda_*=0.4702`

Take

$$
\boxed{\lambda_*=0.4702.}
$$

With

$$
\rho
=0.7390851332151606416553120877\ldots,
$$

the two finite feedback steps give

$$
\boxed{
L_0
=0.3242144957590694118167\ldots,
\qquad
R_0
=0.0225316844847949784549\ldots,
}
\tag{DP.16}
$$

$$
\boxed{
L_1
=0.3262309456028315236922\ldots,
\qquad
R_1
=0.0162645005230745397146\ldots,
}
\tag{DP.17}
$$

$$
\boxed{
L_2
=0.3262917273984089741622\ldots,
\qquad
R_2
=0.0160758901140228867808\ldots .
}
\tag{DP.18}

The right side of DP.15 is

\[
\boxed{
V_D(\lambda_*)
=0.3254071976036928745110\ldots .
}
\tag{DP.19}

Hence

\[
\boxed{
L_2(\lambda_*)-V_D(\lambda_*)
=0.0008845297947160996512\ldots>0.
}
\tag{DP.20}

This contradicts DP.15.  Monotonicity excludes every smaller `lambda`.  Therefore DP.1 follows.

The endpoint margin is almost `9e-4`, safely above the displayed numerical precision.

---

## 6. Comparison with the current merged frontier

The explicit post-ZF pinned/contact floor has moved through

\[
0.4633168954\ldots\quad\text{(JC)},
$$

$$
0.4647922503\ldots\quad\text{(GS)},
$$

$$
0.4694\quad\text{(merged PF)},
$$

and now

$$
\boxed{0.4702}\quad\text{(DD + finite PI feedback)}.
$$

The conceptual change is more important than the numerical increment: the limiting pocket functional is controlled by the Dirichlet dual of mean transverse height, not by a generic convex isoperimetric or `L^2` estimate.

---

## 7. Further progress available but not claimed here

The two-step feedback is close to its fixed point but not exact.  Additional finite iterations can improve the constant slightly.  More importantly, DP still relaxes several finite currencies after the exact JC step.  A closing proof will require a new upper/global incompatibility, not indefinite iteration of this scalar mechanism.

The next structural targets remain:

1. the `s_Z=0` rigidity-circuit phase;
2. a quantitative upper restriction on the loaded-contact/pinned-stress currency from the planar contact embedding;
3. transfer of RA's rattler-free representative into the Target A stress-sector/source-capacity endpoint.

---

## 8. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| DD replacement in PF/ED | proved | identical exact chain/detour inputs |
| `F(nu)` decreasing for `lambda<=0.4702` | proved | derivative bound DP.13-DP.14 |
| one-variable condition DP.15 | proved | DD + exact-defect budget |
| explicit `0.4702` floor | proved asymptotically | endpoint margin DP.20 |
| optimal scalar floor | not claimed | finite feedback / residual relaxations remain |
| Level I | still open | high-surplus structural closure remains |

---

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Use the merged PF two-step bootstrap L0,R0,L1,R1,L2,R2.
Exact PC/ED gives
    L_chain/D <= pi+2R2-lambda-Q/D,
    U_det/D   <= 2R2-Q/D.
DD improves the pocket bound to
    H_out <= (1/sqrt6)L_chain^(3/2)U_det^(1/2).
The total cavity capacity as a function of nu=Q/D is strictly decreasing
for lambda<=0.4702, so nu=0 is worst. Therefore every survivor needs
    L2(lambda)
      <= (1/sqrt6)(pi+2R2(lambda)-lambda)^(3/2)sqrt(2R2(lambda)).
At lambda=0.4702:
    L2=0.3262917273984089742...,
    R2=0.0160758901140228868...,
    RHS=0.3254071976036928745...,
    margin=0.0008845297947160997...>0.
Hence
    liminf (e_BB+2s_C)/D >= 0.4702.
```
