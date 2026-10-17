> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_d1_s1_q13_kkt_psd_regression_2026-09-10.md) · source SHA-256 `a1313b6c1169966d126958c4565d5e4c8a620f43ed05e25f57ee8f8caf56b22b`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-24F04EF50937","canonical":false,"claim_ids":["C-S1-Q13"],"claim_statuses":{"C-S1-Q13":"regression"},"index":"docs/state/artifact-index.jsonl","status":"regression","target":"target-c"} -->
# Erdős Problem #99 — a q=13 S1 shell survives closure, full KKT, rigidity, and PSD

**Date:** 2026-09-10  
**Run type:** exact-algebra / high-precision numerical regression  
**Target:** cyclic primitive `d_H=1`, S1 endpoint  
**Depends on:** SI S1 subset-product identity on this branch; D1/AC cyclic S1 reconstruction  
**Proof status:** exact polynomial reduction plus numerical certification of geometry/stress; this is a regression, not a Level I counterexample

## LEVEL I STATUS

`STILL OPEN`.

The new SI identity suggested that S1 might be algebraically empty, or that every exact S1 shell might fail the full KKT/PSD package.  Both shortcuts are false.

There is a concrete `q=13` S1 sign word whose exact closure equation has a root in the strict S1 interval.  Reconstructing the equilateral polygon at that root gives:

- exactly 13 unit shell contacts and no other unit contacts;
- exactly 12 diameter pairs;
- the 12 diameter pairs form a connected spanning tree;
- mixed rigidity rank `23=2q-3`;
- a two-dimensional bar self-stress space, hence a one-dimensional normalized KKT family;
- a relative-interior normalized KKT stress with every contact coefficient positive and every diameter coefficient positive;
- a PSD stress matrix of rank `10=q-3`;
- both normalized KKT endpoint stresses PSD of the same rank, with one diameter coefficient zero at each endpoint.

Thus the following proposed S1 closures are invalid:

```text
S1 closure equation has no strict interior solution;
S1 full KKT positivity is impossible;
S1 maximal-rank PSD stress is impossible;
S1 KKT endpoints must leave the PSD cone.
```

The global Target C proof must use information beyond the isolated shell equality/KKT/PSD package, most likely the full-source packing/population constraints.

---

## 1. Exact sign word

Take

```math
q=13,
\qquad
m=q-2=11.
```

Use the two fixed defect-adjacent full signs

```math
+,-
```

and the ordinary SI/SC sign word

```math
\boxed{
(-,+,-,-,+,+,+,-,-,+,-).
}
\tag{R13.1}
```

The ordinary word is palindromic, so the centered-real SC equation is automatic for every real `delta`.

Its positive-sign run structure gives a canonical antipodal odd-cycle length seven under the SC seam convention.

---

## 2. Exact trace polynomial for the closure root

Insert (R13.1) into the SI subset-product equation.  After removing a trivial factor `Z`, the resulting reciprocal polynomial is

```math
\begin{aligned}
J(Z)=\;&Z^{20}-2Z^{19}+2Z^{18}-2Z^{16}+2Z^{15}-Z^{14}+Z^{13}-Z^{12}\\
&-2Z^{11}+5Z^{10}-2Z^9-Z^8+Z^7-Z^6+2Z^5-2Z^4+2Z^2-2Z+1.
\end{aligned}
\tag{R13.2}
```

It is reciprocal of degree twenty.  Writing

```math
T=Z+Z^{-1}
```

gives the exact trace polynomial

```math
\boxed{
\begin{aligned}
H(T)=\;&T^{10}-2T^9-8T^8+18T^7+17T^6-52T^5+T^4\\
&+51T^3-22T^2-13T+11.
\end{aligned}}
\tag{R13.3}
```

The relevant real root is

```math
\boxed{
T_*=1.94199413054336852922749320256483167619\ldots
}
\tag{R13.4}
```

and therefore

```math
\boxed{
\delta_*=\arccos(T_*/2)
=0.24143000751202257239399313530418313626\ldots .
}
\tag{R13.5}
```

For `q=13`, the strict S1 interval is

```math
\delta_{P1}<\delta<\frac\pi{13},
```

where numerically

```math
\delta_{P1}=0.2413833791241437\ldots,
\qquad
\frac\pi{13}=0.2416609733530610\ldots .
```

Thus (R13.5) lies strictly inside the S1 interval, not at either P1 or Reinhardt boundary.

The associated exact D1 quantities are

```math
D=4.15206390869976241099491081968056393\ldots,
\tag{R13.6}
```

```math
G=\pi-m\delta
=0.485862570957544942128718894933488385\ldots,
\tag{R13.7}
```

```math
\tau
=0.0990340932801865191022759741709044905\ldots,
\tag{R13.8}
```

and the canonical short antipodal edge has length

```math
|g|=4.07964378821875417587381298479031122\ldots<D.
\tag{R13.9}
```

The short edge is also strictly above the P1 tie length:

```math
|g|>\sqrt{D^2-1}.
```

So this is genuinely S1.

---

## 3. Reconstructed convex equilateral polygon

Use the D1/SC projective half-edge directions

```math
\theta_0=-\tau/2,
\qquad
\theta_1=\tau/2,
```

and, for `0<=k<=10`,

```math
\theta_{k+2}
=\frac\pi2+(k-5)\delta.
```

Multiply these thirteen unit directions by the full signs

```math
(+,-,-,+,-,-,+,+,+,-,-,+,-),
```

sort the resulting oriented side vectors cyclically, and take cumulative sums.

The closure residual at 50-digit evaluation is below `10^-45`; the double-precision coordinates used for the graph/stress audit close to below `7e-14`.

The reconstructed polygon is strictly convex.  Direct distance classification gives exactly the cycle contacts

```math
(0,1),(1,2),\ldots,(11,12),(12,0)
```

at length one and exactly the following twelve diameter pairs:

```math
\boxed{
\begin{array}{llll}
(0,6),&(0,7),&(1,7),&(1,8),\\
(1,9),&(2,9),&(3,9),&(4,9),\\
(4,10),&(4,11),&(5,11),&(5,12).
\end{array}}
\tag{R13.10}
```

Every other pair lies strictly between one and `D` at the numerical certificate precision.

The graph in (R13.10) is a spanning tree on thirteen vertices.  Its degree sequence in shell order is

```math
(2,3,1,1,3,2,1,2,1,4,1,2,1).
\tag{R13.11}
```

Thus it is an honest `d_H=1` diameter tree, not a hidden unicyclic or disconnected case.

---

## 4. Mixed rigidity and normalized KKT family

Form the ordinary planar bar-rigidity matrix with the 13 cycle contacts followed by the 12 diameter rows in (R13.10).

Numerically,

```math
\boxed{\operatorname{rank}R=23=2q-3.}
\tag{R13.12}
```

There are 25 mixed rows, so the self-stress space has dimension two.

Use the Target C sign convention

```math
\omega=(\alpha,-\beta),
```

where `alpha` is positive on contacts and `beta` positive on diameter constraints.  The self-stress plane intersects this sign orthant in a nondegenerate cone.  Normalizing

```math
\sum_h\beta_h=1
```

gives a line segment.

A symmetric interior point of that segment has contact weights

```math
\begin{aligned}
\alpha\approx(&1.2849780367,
1.2480632991,
1.2480632991,
1.2480632991,
1.2849780367,\\
&1.3639305825,
1.3483102688,
1.3752517571,
1.3752517571,
1.3752517571,\\
&1.3752517571,
1.3483102688,
1.3639305825),
\end{aligned}
\tag{R13.13}
```

and diameter weights, in the order (R13.10),

```math
\begin{aligned}
\beta\approx(&0.1022450943,
0.1051513978,
0.05283118555,
0.07977267389,\\
&0.08760465167,
0.07239499680,
0.07239499680,
0.08760465167,\\
&0.07977267389,
0.05283118555,
0.1051513978,
0.1022450943).
\end{aligned}
\tag{R13.14}
```

All coefficients are well separated from zero.  In particular this is not a near-boundary numerical artifact.

---

## 5. PSD stress matrix

Let

```math
\Omega=L_C(\alpha)-L_H(\beta)
```

be the Target C stress matrix of the interior normalized stress.

Its eigenvalues are numerically

```math
\begin{aligned}
&-1.1\times10^{-15},\quad
1.3\times10^{-16},\quad
6.0\times10^{-16},\\
&1.1039011469,
1.1080515683,
2.0647318267,
2.1266409006,
3.4012011086,\\
&3.5545910373,
4.4195155072,
4.4726994612,
5.0104629251,
5.2174739221.
\end{aligned}
\tag{R13.15}
```

Thus, at numerical precision,

```math
\boxed{\Omega\succeq0,\qquad \operatorname{rank}\Omega=10=q-3.}
\tag{R13.16}
```

The first three values are the affine kernel and are at floating-point roundoff scale; the positive spectrum has a gap above `1.10`.

---

## 6. Both KKT endpoints remain PSD

Parameterize the normalized stress line so that the interior midpoint is `t=0`.  The positivity interval is numerically

```math
-0.4690501007991555\ldots
\le t\le
0.4690501007991708\ldots .
\tag{R13.17}
```

At the negative endpoint, exactly the diameter edge

```math
\boxed{(1,7)}
```

has zero beta coefficient.  At the positive endpoint, exactly

```math
\boxed{(4,11)}
```

has zero beta coefficient.

All contact coefficients remain at least

```math
1.1529\ldots>0,
```

and all other diameter coefficients remain positive, with the smallest nonzero endpoint beta above

```math
0.0160.
```

At both endpoints the smallest positive stress-matrix eigenvalue is

```math
1.0508556\ldots,
```

while the three affine eigenvalues remain at roundoff scale.  Hence both endpoints satisfy the same numerical PSD/rank pattern

```math
\boxed{\Omega_{\pm}\succeq0,\qquad\operatorname{rank}\Omega_{\pm}=q-3.}
\tag{R13.18}
```

Because the stress matrix depends affinely on the normalized stress parameter and the PSD cone is convex, the entire normalized KKT segment is numerically PSD once the endpoint certification is accepted.

This mirrors the universal-PSD behavior required in the Target C survivor, rather than violating it.

---

## 7. What this regression kills

The q=13 shell refutes several attractive but insufficient S1 strategies.

### Closure-only exclusion

False.  SI/SC has a strict S1 root.

### Full-support KKT sign exclusion

False.  There is a relative-interior stress with all 25 active coefficients of the required signs.

### Maximal-rank PSD exclusion

False.  The interior stress matrix has the exact expected affine nullity three and a large positive spectral gap.

### Endpoint-PSD exclusion

False.  Both endpoint stresses remain PSD and lose one diameter coefficient exactly as the abstract one-dimensional KKT picture permits.

### Generic local shell theorem

Any theorem using only

```text
strict convex equilateral shell
+ contact cycle
+ spanning diameter tree
+ full-support KKT
+ maximal-rank PSD
+ endpoint PSD
```

cannot exclude S1, because this finite shell realizes that package numerically.

The remaining global proof must use a hypothesis absent from this regression: the existence and optimal packing of the full `n-q` source population, the asymptotic `q,D,n` relation, or another genuinely global-minimizer consequence.

---

## 8. What is and is not certified

This report is deliberately classified as a **regression**, not a proof that S1 occurs in a global Erdős-99 minimizer.

Exact/algebraic components:

- the sign word;
- the reciprocal/trace closure polynomial;
- the S1 interval equations;
- the reconstruction formulas.

High-precision numerical components:

- the distinguished root value;
- pair-distance classification;
- rigidity rank;
- positive KKT cone;
- PSD spectra.

All displayed numerical margins are large compared with the residual precision, but no interval-arithmetic proof is claimed here.

If this regression later becomes proof-critical, the trace root can be isolated by rational interval arithmetic and the stress signs/PSD principal minors can be certified over the resulting algebraic interval.

---

## 9. Next target after this regression

The S1 endgame must now distinguish a **global source minimizer** from the q=13 shell regression.

The best next targets are:

1. combine UFB's complete-source hull/population theorem with the exact S1 short antipodal defect and derive a packing loss that cannot be repaired by the interior points;
2. use ID's cross-index diameter descent together with the S1 exact defect parameter to force a stronger finite difference in `D(n)-D(n-q)`;
3. prove an asymptotic S1 stability theorem that uses `q~pi D`, not only finite KKT/PSD data; the q=13 example must then appear as an explicitly finite regression rather than a contradiction.

A shell-only KKT/PSD attack should not be pursued further without an additional asymptotic/global ingredient.

---

## Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| exact q=13 SI polynomial | exact algebra | direct substitution/factorization |
| strict S1 root | high-precision numerical, easily interval-certifiable | root lies well inside endpoint interval |
| exact contact/diameter counts | numerical regression | positive gaps in pair distances |
| diameter graph is a tree | numerical regression from certified edge list | 12 connected edges on 13 vertices |
| mixed rank `23` | numerical regression | SVD with large nonzero gap |
| full positive KKT stress | numerical regression | coefficients have substantial margins |
| interior PSD rank `10` | numerical regression | three roundoff zeros, positive gap >1.10 |
| endpoint PSD rank `10` | numerical regression | positive gap >1.05 |
| global Erdős-99 minimizer | not claimed | no full source population / global optimality certificate |
| Level I | still open | global packing remains essential |

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

S1 shell-only exclusion is false.  At q=13, m=11, use ordinary signs
  - + - - + + + - - + -
with the fixed defect signs +,-.  The SI equation gives the reciprocal degree-20
polynomial R13.2, equivalently trace polynomial
  H(T)=T^10-2T^9-8T^8+18T^7+17T^6-52T^5+T^4+51T^3-22T^2-13T+11.
It has the relevant root
  T*=1.9419941305433685...,
  delta*=0.24143000751202257...,
strictly between the q=13 P1 and Reinhardt endpoints.
Reconstruction gives D=4.152063908699762..., exactly 13 cycle contacts and exactly
12 diameter pairs forming a spanning tree.

The 25-row mixed rigidity matrix has rank 23 and a 2D self-stress space.  After
normalizing sum beta=1 there is a full-positive KKT interval.  Its midpoint has all
alpha>1.24 and all beta>0.052.  The stress matrix has affine nullity three and positive
spectrum starting at 1.1039.  At the two KKT endpoints exactly one beta vanishes,
for edges (1,7) and (4,11), while both endpoint stress matrices remain PSD with
positive spectral gap >1.05.

Therefore S1 is compatible, at finite shell level, with:
  equilateral convex shell + contact cycle + spanning diameter tree
  + full KKT + mixed rigidity + maximal-rank PSD + PSD KKT endpoints.
The proof must now use genuinely global source packing/asymptotic information.
```
