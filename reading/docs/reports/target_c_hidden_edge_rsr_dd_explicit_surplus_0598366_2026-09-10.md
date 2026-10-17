> Generated reading edition · [exact source](../../../docs/reports/target_c_hidden_edge_rsr_dd_explicit_surplus_0598366_2026-09-10.md) · source SHA-256 `ad9e0bd0fea9f6c2b7e6b45f9907516a81838a005a8913ca3fba6bb390e2bd8f`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-47469C6DE3CC","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_hidden_edge_rsr_dd_explicit_surplus_0598366_2026-09-10.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=7fe52b00d1e7a03d0c16fd37dc458da0ec2a375a; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — hidden-edge attachment stability raises the generic post-ZF floor above 0.598366

**Date:** 2026-09-10  
**Branch base:** `5924a78cd5782ad291ad87c8904334982d7a025e`  
**Depends on:** HE, RD, RX, FSDB, RSJ  
**Run type:** exact compact optimization / rational certificate  
**Target:** Target C, C-II after ZF

## LEVEL I STATUS

`STILL OPEN`.

HE proves the uniform attachment-cell capacity

$$
\boxed{
\limsup\frac1{D^2}
\sum_r\operatorname{area}(\operatorname{conv}A_r)
\le c_{HE}\lambda^2,
\qquad
c_{HE}:=\frac\pi4-\frac3{4000},
}
\tag{HX.1}
$$

for every post-ZF sequence with

$$
\lambda:=\limsup\frac{e_{BB}+2s_C}{D}<3/5.
$$

Re-running the RSR/DD optimizer with this coefficient gives an exact threshold
`lambda_HE` satisfying

$$
\boxed{
\liminf_{D\to\infty}
\frac{e_{BB}+2s_C}{D}
\ge\lambda_{HE}>0.598366.
}
\tag{HX.2}
$$

Numerically, for orientation only,

$$
\boxed{
y_{HE}=1.5245283152144573698\ldots,}
\tag{HX.3}
$$

$$
\boxed{
p_{HE}=3.0231381569965496279\ldots,}
\tag{HX.4}
$$

$$
\boxed{
\lambda_{HE}=0.5983667958145539442\ldots .
}
\tag{HX.5}
$$

The exact theorem is HX.2.  A companion `fractions.Fraction` verifier certifies the
six-decimal extension with no floating-point dependency.

---

## 1. Strengthened RSR/DD system

Retain

$$
\Phi(y)=\frac{y+\sin y}{4},
\qquad
c_R=\frac\pi{(\pi-2)^2},
\qquad
\Psi(p)=c_R\left(\frac p2-1\right)^2,
\tag{1.1}
$$

and

$$
A(y,p)=\max\{\Phi(y),\Psi(p)\}.
\tag{1.2}
$$

As in RX, it is safe to enlarge the DB domain to

$$
\widetilde{\mathcal R}
=
\{(y,p):2\rho\le y\le\pi,\ y\le p\le\min\{2y,\pi\}\}.
\tag{1.3}
$$

For a candidate surplus `lambda<3/5`, HE and the two RD cavity estimates give

$$
\boxed{
A(y,p)-c_{HE}\lambda^2
\le\frac{(\lambda+p-y)^2}{4\pi},
}
\tag{1.4}
$$

and

$$
\boxed{
A(y,p)-c_{HE}\lambda^2
\le
\Delta(y,p):=
\frac2{\sqrt3}y^{3/2}\sqrt{2y-p}.
}
\tag{1.5}
$$

If `lambda>=3/5`, HX.2 is immediate, so these inequalities cover every sequence that
could violate the claimed bound.

Define `R_HE(A,m)` as the positive root of

$$
\boxed{
(4\pi c_{HE}+1)\lambda^2
+2m\lambda+m^2-4\pi A=0.
}
\tag{1.6}
$$

Then the JC threshold is

$$
J_{HE}(y,p)=R_{HE}(A(y,p),p-y),
\tag{1.7}
$$

and the DD threshold is

$$
D_{HE}(y,p)
=
\sqrt{
\max\left\{0,
\frac{A(y,p)-\Delta(y,p)}{c_{HE}}
\right\}
}.
\tag{1.8}
$$

Every survivor in the relevant range satisfies

$$
\lambda\ge\max\{J_{HE}(y,p),D_{HE}(y,p)\}.
\tag{1.9}
$$

---

## 2. Fixed-`y` minimization

The FSDB/RSR area crossover is unchanged:

$$
\boxed{
p_e(y)=2+2\sqrt{\frac{\Phi(y)}{c_R}}.}
\tag{2.1}
$$

On `p<=p_e(y)`, the area currency is `Phi(y)`.  For fixed `y`:

- `J_HE` strictly decreases as `p` increases, because `m=p-y` increases;
- `D_HE` strictly increases, because the detour term decreases.

For `p>=p_e(y)`, both thresholds strictly increase.  The DD statement is immediate.
For JC, on the RSR-active branch

$$
\Psi(p)-c_{HE}\lambda^2
=\frac{(\lambda+p-y)^2}{4\pi}.
$$

Implicit differentiation gives a positive `p` derivative precisely when

$$
\pi c_R(p-2)>\lambda+p-y.
$$

As in RSJ/RX, `p>3`, `c_R>2`, `lambda<1`, and `p-y<=pi`, so the inequality holds
with room.

Therefore no fixed-`y` minimizer lies to the right of `p_e(y)`.

---

## 3. Crossover values move in opposite directions

For `y>=y_R`, put

$$
u(y)=2y-p_e(y)
$$

and

$$
E(y)=
\Phi(y)-\frac2{\sqrt3}y^{3/2}\sqrt{u(y)}.
\tag{3.1}
$$

RX proves `E'(y)<0` on `[y_R,pi/2]`.

Define

$$
\boxed{
d_{HE}(y)=\sqrt{\max\{0,E(y)/c_{HE}\}},}
\tag{3.2}
$$

and

$$
\boxed{
r_{HE}(y)=R_{HE}(\Phi(y),p_e(y)-y).}
\tag{3.3}
$$

Thus `d_HE` strictly decreases until it reaches zero.

For `r_HE`, let `m(y)=p_e(y)-y`.  RX gives `m'(y)<0`.  Differentiating

$$
\Phi(y)-c_{HE}r_{HE}^2
=\frac{(r_{HE}+m)^2}{4\pi}
$$

gives

$$
\left[
2c_{HE}r_{HE}+\frac{r_{HE}+m}{2\pi}
\right]r_{HE}'
=
\Phi'(y)-\frac{(r_{HE}+m)m'}{2\pi}>0.
$$

Hence

$$
\boxed{r_{HE}'(y)>0.}
\tag{3.4}
$$

At `y=y_R`, the DD detour is zero, so `d_HE(y_R)>r_HE(y_R)`.  At
`y=pi/2`, RX proves `E<0`, so `d_HE=0<r_HE`.  Therefore there is a unique

$$
\boxed{y_{HE}\in(y_R,\pi/2)}
\tag{3.5}
$$

with

$$
\boxed{d_{HE}(y_{HE})=r_{HE}(y_{HE}).}
\tag{3.6}

---

## 4. Pre-transition optimum decreases with `y`

For `y<=y_HE`, let `lambda(y)` be the unique pre-crossover point where the JC and DD
thresholds agree.  Put

\[
S=\Phi(y)-c_{HE}\lambda^2.
\tag{4.1}
$$

The equality equations give

$$
p-y=2\sqrt{\pi S}-\lambda,
\qquad
2y-p=\frac{3S^2}{4y^3}.
\tag{4.2}
$$

Eliminating `p`,

$$
F(y,\lambda)
:=
y+\lambda-2\sqrt{\pi S}-\frac{3S^2}{4y^3}=0.
\tag{4.3}
$$

At fixed `y`,

$$
F_\lambda
=1+
\frac{2c_{HE}\sqrt\pi\,\lambda}{\sqrt S}
+
\frac{3c_{HE}\lambda S}{y^3}>0.
\tag{4.4}
$$

At fixed `lambda`,

$$
F_y
=1-
\frac{\sqrt\pi\,\Phi'(y)}{\sqrt S}
-
\frac{3S\Phi'(y)}{2y^3}
+
\frac{9S^2}{4y^4}.
\tag{4.5}
$$

The HE system is pointwise stronger than RX, so every crossing satisfies the already
certified

$$
\lambda>299/500.
\tag{4.6}
$$

Also

$$
y>7/5,
\qquad
\Phi'(y)<7/25.
\tag{4.7}
$$

Since `pi>3`,

$$
c_{HE}>\frac34-\frac3{4000}.
$$

Together with `Phi<9/14` and (4.6),

$$
S
<
\frac9{14}
-
\left(\frac34-\frac3{4000}\right)
\left(\frac{299}{500}\right)^2
<\frac38.
\tag{4.8}
$$

Equation (4.2) then gives `2y-p<1/25`, hence `p-y>34/25`.  JC equality and
`pi<22/7` give

$$
S>3/10.
\tag{4.9}
$$

As in BRD/BF,

$$
\sqrt{\pi/S}<13/4.
$$

Discarding the positive final term in (4.5),

$$
F_y
>
1-rac{91}{100}-\frac{45}{784}
=
\boxed{\frac{639}{19600}>0.}
\tag{4.10}
$$

Therefore

$$
\boxed{\lambda'(y)=-F_y/F_\lambda<0.}
\tag{4.11}
$$

The pre-transition optimum strictly decreases.

---

## 5. Unique global optimizer

Before `y_HE`, the fixed-`y` minimum is the JC/DD crossing and decreases with `y`.
After `y_HE`, the fixed-`y` minimum is the area-crossover JC value `r_HE(y)` and
increases with `y`.  Therefore the unique global minimum is

$$
\boxed{
(y,p)=(y_{HE},p_e(y_{HE})).
}
\tag{5.1}

Define

\[
\boxed{
\lambda_{HE}:=d_{HE}(y_{HE})=r_{HE}(y_{HE}).
}
\tag{5.2}

Equivalently, `(y,p,lambda)` is the unique solution in

\[
y_R<y<\pi/2,
\qquad p=p_e(y),
\qquad 0<\lambda<3/5
$$

of

$$
\boxed{
\Phi(y)=c_R\left(\frac p2-1\right)^2,
}
\tag{5.3}
$$

$$
\boxed{
\Phi(y)-c_{HE}\lambda^2
=\frac{(\lambda+p-y)^2}{4\pi},
}
\tag{5.4}
$$

$$
\boxed{
\Phi(y)-c_{HE}\lambda^2
=\frac2{\sqrt3}y^{3/2}\sqrt{2y-p}.
}
\tag{5.5}

---

## 6. Exact certificate for `lambda_HE>0.598366`

Take the rational point

\[
\boxed{y_0=\frac{190566}{125000}=1.524528.}
\tag{6.1}
$$

The companion verifier uses exact `Fraction` arithmetic with Machin bounds for `pi`,
alternating Taylor bounds for `sin(y_0)`, and rational square-root brackets.  It proves

$$
0.5115690450
<\sqrt{\Phi(y_0)/c_R}
<0.5115690451.
\tag{6.2}
$$

At `lambda=0.598366`, an outward-rounded evaluation of the JC residual is strictly
negative, while at `lambda=0.598367` an inward-rounded evaluation is strictly positive.
Therefore

$$
\boxed{
0.598366<r_{HE}(y_0)<0.598367.
}
\tag{6.3}
$$

The same verifier proves

$$
\boxed{d_{HE}(y_0)>0.598367.}
\tag{6.4}
$$

Hence `d_HE(y_0)>r_HE(y_0)`, so `y_0<y_HE`.  Since `r_HE` is strictly increasing,

$$
\lambda_{HE}
=r_{HE}(y_{HE})
>r_{HE}(y_0)
>0.598366.
$$

This proves HX.2.

---

## 7. Numerical orientation

High-precision solution of (5.3)--(5.5) gives

$$
y_{HE}
=1.52452831521445736977160144476\ldots,
$$

$$
p_{HE}
=3.02313815699654962788235236509\ldots,
$$

and

$$
\lambda_{HE}
=0.59836679581455394420967160068\ldots .
$$

The explicit improvement over the BVE feedback threshold is approximately

$$
2.6553\times10^{-5}.
$$

---

## 8. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| HE cavity system | proved | HE attachment coefficient inserted into RD |
| fixed-`y` optimizer | proved | opposite monotonicity before crossover; both increase after |
| unique transition `y_HE` | proved | `d_HE` decreases, `r_HE` increases, endpoint signs |
| pre-transition optimum decreases | proved | `F_y>639/19600` |
| unique global optimizer | proved | two monotone branches meet once |
| `lambda_HE>0.598366` | exact rational certificate | companion verifier |
| long decimal | numerical orientation only | not a proof dependency |
| Level I | still open | no contradiction for all larger-surplus survivors |

---

## 9. Next run

The hidden-edge theorem used only one forced edge and a Lipschitz width deficit.  It
left two large sources of slack:

1. the external force-hull point hides an entire boundary arc, not merely one chord;
2. an RD/HE near-endpoint has linearly many singleton harmonic cells and almost all
   outer pockets triangular.

The next geometric target is to show that several disjoint attachment cells must pay
hidden-edge perimeter deficits simultaneously, rather than allowing the one
macroscopic cell to consume the entire quadratic budget alone.