> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_d1_s1_subset_product_identity_2026-09-10.md) · source SHA-256 `aa1d9f79e78fe809988a4a296c6da2345aa951df99acbe97c91615f6649a96fc`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-B3A2C9772328","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic S1 closure as an exact subset-product/run-boundary identity

**Date:** 2026-09-10  
**Run type:** exact algebraic reduction of the S1 shell closure  
**Target:** cyclic primitive `d_H=1`, S1 endpoint  
**Depends on:** D1 exact S1 difference-body normal form; AC canonical short antipodal cycle edge; SC signed closure  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`.

The P1 endpoint has now been excluded.  The sole cyclic `d_H=1` survivor is S1: one genuine short antipodal cycle edge `g`, no parallel shell sides, and all remaining antipodal states actual diameter states.

SC writes the S1 primal closure as two trigonometric equations in the ordinary sign word.  Those two equations collapse to one exact polynomial identity that uses the same reciprocal five-term polynomial that arose in P1.

Put

```math
m:=q-2,
\qquad
z:=e^{i\delta},
\qquad
\delta=2\arcsin\frac1{2D}.
```

Let

```math
P(Z)=\sum_{k=0}^{m-1}\varepsilon_k Z^k,
\qquad \varepsilon_k\in\{+1,-1\},
\tag{SI.1}
```

be the ordinary S1 sign polynomial after the two defect-adjacent signs have been removed and centered as below.

Define the P1 reciprocal polynomial

```math
\boxed{
F_m(Z):=(Z^m+1)^2+4Z^{m-1}(Z-1)^2.
}
\tag{SI.2}
```

Then the complete S1 closure is equivalent to

```math
\boxed{
F_m(z)=(z-1)^2P(z)^2.
}
\tag{SI.3}
```

If

```math
S_m(Z):=1+Z+\cdots+Z^{m-1}
```

and `Q in {0,1}[Z]` marks the negative coefficients of `P`, so

```math
P=S_m-2Q,
\tag{SI.4}
```

then SI.3 is exactly equivalent to the 0/1 subset-product equation

```math
\boxed{
z^{m-1}\Phi_6(z)
+(z-1)^2Q(z)(S_m(z)-Q(z))=0,
}
\tag{SI.5}
```

where

```math
\Phi_6(Z)=Z^2-Z+1.
```

Equivalently,

```math
\boxed{
Q(z)(S_m(z)-Q(z))
=-\frac{z^{m-1}\Phi_6(z)}{(z-1)^2}.
}
\tag{SI.6}
```

On the unit circle the right side has positive real centered phase:

```math
\boxed{
Q(z)(S_m(z)-Q(z))
=\lambda_D z^{m-1},
\qquad
\lambda_D:=\frac{2\cos\delta-1}{4\sin^2(\delta/2)}>0.
}
\tag{SI.7}
```

Thus the two complementary ordinary sign subsets have centered evaluations on the same real line and an exact positive product.

There is a second factorization.  Put

```math
A_-(Z):=1+(Z-1)Q(Z),
```

```math
A_+(Z):=1+(Z-1)(S_m(Z)-Q(Z))
=Z^m-(Z-1)Q(Z).
```

Then SI.5 is equivalent to

```math
\boxed{
A_-(z)A_+(z)
=-z^{m-1}(z-1)^2.
}
\tag{SI.8}
```

The centered-real closure implies

```math
A_+(z)=z^m\overline{A_-(z)},
```

so

```math
\boxed{|A_-(z)|=|A_+(z)|=|z-1|.}
\tag{SI.9}
```

Each `A_+` or `A_-` is a run-boundary polynomial: if the corresponding 0/1 set is the disjoint union of intervals `[a_j,b_j]`, then

```math
\boxed{
1+(Z-1)\sum_j\sum_{k=a_j}^{b_j}Z^k
=1+\sum_j(Z^{b_j+1}-Z^{a_j}).
}
\tag{SI.10}
```

Hence S1 is reduced to a small-value equation for a sparse `0,±1` polynomial supported exactly at sign-run boundaries.

This is a strict strengthening of the presentation of SC: the nonlinear short-state angle disappears from the final algebraic equation.  Its only effect is encoded through the fact that `z` lies in the S1 interval rather than at the P1 endpoint.

---

## 1. Center the ordinary sign word

SC fixes the two signs adjacent to the unique short antipodal state to be opposite.  Normalize them as

```math
\varepsilon_0^{full}=1,
\qquad
\varepsilon_1^{full}=-1.
```

For the remaining `m=q-2` ordinary difference-body edges, write

```math
\varepsilon_k:=\varepsilon_{k+2}^{full},
\qquad 0\le k\le m-1.
```

D1/SC give their directions as

```math
\theta_{k+2}
=\left(k+\frac32+\frac s2\right)\delta,
```

where

```math
(q+s)\delta=\pi.
```

Since `q=m+2`,

```math
\theta_{k+2}
=\frac\pi2+\left(k-\frac{m-1}{2}\right)\delta.
\tag{1.1}
```

Therefore

```math
\sum_{k=0}^{m-1}\varepsilon_k e^{i\theta_{k+2}}
=i z^{-(m-1)/2}P(z).
\tag{1.2}
```

SC's real closure equation says the real part of (1.2) is zero.  Hence

```math
z^{-(m-1)/2}P(z)\in\mathbb R.
\tag{1.3}
```

Its imaginary closure equation gives the exact value

```math
\boxed{
z^{-(m-1)/2}P(z)=2\sin\frac\tau2,}
\tag{1.4}
```

where SC uses

```math
\tau=\pi-2\eta,
\qquad
\eta=\arcsin\left(D\sin\frac G2\right).
```

Thus

```math
\boxed{
P(z)=2\sin\frac\tau2\,z^{(m-1)/2}.
}
\tag{1.5}
```

No parity assumption on `m` is needed; the half-power is only a convenient complex phase and disappears after squaring.

---

## 2. Eliminate the short-state angle

D1 gives

```math
G=(s+2)\delta.
```

Using `(m+2+s)delta=pi`,

```math
\boxed{G=\pi-m\delta.}
\tag{2.1}
```

Also

```math
\sin\frac\tau2=\cos\eta,
```

so

```math
\sin^2\frac\tau2
=1-D^2\sin^2\frac G2
=1-D^2\cos^2\frac{m\delta}{2}.
\tag{2.2}
```

Since

```math
D=\frac1{2\sin(\delta/2)},
\tag{2.3}
```

squaring (1.5) gives

```math
P(z)^2
=4\left(1-D^2\cos^2\frac{m\delta}{2}\right)z^{m-1}.
\tag{2.4}
```

Multiply by `(z-1)^2`.  On the unit circle,

```math
(z-1)^2=-4z\sin^2\frac\delta2.
\tag{2.5}
```

Therefore

```math
\begin{aligned}
(z-1)^2P(z)^2
&=-16z^m\sin^2\frac\delta2
+4z^m\cos^2\frac{m\delta}{2}\\
&=4z^{m-1}(z-1)^2+(z^m+1)^2\\
&=F_m(z).
\end{aligned}
```

This proves SI.3.

The P1 boundary corresponds to `tau=0`, hence `P(z)=0`, and SI.3 reduces to the P1 equation `F_m(z)=0`.  Thus S1 and P1 are genuinely one algebraic family: S1 is the nonzero-right-hand-side interior, P1 the vanishing boundary.

---

## 3. Convert to a 0/1 subset-product identity

Write

```math
P=S_m-2Q,
```

where each coefficient of `Q` is `1` exactly where the corresponding sign of `P` is `-1`.

Since

```math
(z-1)S_m(z)=z^m-1,
```

we have

```math
(z-1)^2S_m(z)^2=(z^m-1)^2.
```

Thus

```math
(z-1)^2P^2
=(z^m-1)^2
-4(z-1)^2Q(S_m-Q).
\tag{3.1}
```

Subtract this from SI.2:

```math
\begin{aligned}
F_m-(z-1)^2P^2
&=(z^m+1)^2-(z^m-1)^2\\
&\quad+4z^{m-1}(z-1)^2
+4(z-1)^2Q(S_m-Q)\\
&=4z^{m-1}\bigl[z+(z-1)^2\bigr]
+4(z-1)^2Q(S_m-Q)\\
&=4\left[z^{m-1}\Phi_6(z)
+(z-1)^2Q(S_m-Q)\right].
\end{aligned}
```

Using SI.3, the left side vanishes.  This proves SI.5-SI.6.

For `z=e^{i delta}`,

```math
\Phi_6(z)=z(2\cos\delta-1),
```

and

```math
(z-1)^2=-4z\sin^2(\delta/2).
```

Substitution gives SI.7.

---

## 4. Complementary run-boundary factorization

Set

```math
B(Z):=(Z-1)Q(Z).
```

Then

```math
A_-=1+B,
\qquad
A_+=Z^m-B.
```

Their product is

```math
\begin{aligned}
A_-A_+
&=Z^m+B(Z^m-1)-B^2\\
&=Z^m+(Z-1)^2Q(S_m-Q).
\end{aligned}
```

By SI.5,

```math
A_-A_+
=Z^m-Z^{m-1}\Phi_6(Z)
=-Z^{m-1}(Z-1)^2
```

at `Z=z`.  This is SI.8.

From (1.3), both centered values

```math
z^{-(m-1)/2}P(z)
\quad\text{and}\quad
z^{-(m-1)/2}S_m(z)
```

are real.  Hence so are

```math
z^{-(m-1)/2}Q(z)
```

and

```math
z^{-(m-1)/2}(S_m-Q)(z).
```

A direct conjugation then gives

```math
\begin{aligned}
z^m\overline{A_-(z)}
&=z^m+z^m(z^{-1}-1)\overline{Q(z)}\\
&=z^m-(z-1)Q(z)\\
&=A_+(z).
\end{aligned}
```

Therefore

```math
A_-(z)A_+(z)=z^m|A_-(z)|^2.
```

Compare with SI.8 and divide by `z^m`:

```math
|A_-(z)|^2
=-z^{-1}(z-1)^2
=|z-1|^2.
```

This proves SI.9; the same holds for `A_+`.

---

## 5. Run-boundary interpretation

Let a 0/1 polynomial `R` have support equal to a disjoint union of integer intervals

```math
[a_1,b_1]\sqcup\cdots\sqcup[a_t,b_t]
\subseteq\{0,\ldots,m-1\}.
```

Then

```math
\begin{aligned}
1+(Z-1)R(Z)
&=1+\sum_{j=1}^t(Z-1)\sum_{k=a_j}^{b_j}Z^k\\
&=1+\sum_{j=1}^t(Z^{b_j+1}-Z^{a_j}).
\end{aligned}
```

This proves SI.10.

Apply this to `R=S_m-Q`, the positions carrying ordinary sign `+1`.  The full SC sign word starts with the fixed defect pair `+,-`.  If the ordinary positive-sign set has `t_+` runs, then SC's seam convention gives the odd antipodal cycle length

```math
\boxed{\nu=1+2t_+.}
\tag{5.1}
```

Indeed the fixed defect pair contributes one sign change, while the ordinary positive runs contribute exactly two additional sign-boundary events each, including endpoints through the projective seam convention.

Thus the support of `A_+` is literally the endpoint set of the positive sign runs that form the retained odd-cycle spine around the canonical short edge `g`.

S1 has therefore been reduced to:

```text
choose a 0/1 subset R of {0,...,m-1};
its run-boundary polynomial A_R=1+(Z-1)R has support only at run endpoints;
for z=e^{i delta} in the exact D1 S1 interval,
    |A_R(z)|=|z-1|;
and the number of positive runs is (nu-1)/2 for the canonical antipodal odd cycle.
```

This is the correct sparse object for the next S1 attack.

---

## 6. Regression audit

### No C17 diameter-cycle import

The odd cycle in `A(F)` contains the canonical short edge `g`, so it is **not** a cycle of the full diameter graph.  C17's lower bound for genuine diameter cycles does not apply to `nu`.  No `Omega(sqrt D)` lower bound on the S1 antipodal-cycle length is claimed here.

### No universal sparse-polynomial lower bound

Arbitrary run-boundary polynomials can have values much smaller than `|z-1|` near roots of unity.  SI.9 is an exact equation, not by itself a contradiction.  The next proof must use the S1 admissibility/KKT constraints on the run composition, not only coefficient sparsity.

### Half-integral centering

When `m` is even, `z^{(m-1)/2}` is used only as a complex phase.  All polynomial identities SI.3-SI.10 have integral exponents.

### Squaring

SI.3 was obtained by squaring the signed closure, but the original SC real equation fixes the centered sign of `P(z)` by (1.4).  Every S1 source therefore satisfies SI.3.  The polynomial equation alone may have extraneous roots; it is used only as a necessary condition unless the sign is restored.

### P1 boundary

At the P1 endpoint the defect angle `tau` tends to zero and `P(z)` tends to zero.  The already-excluded P1 polynomial `F_m(z)=0` is exactly the boundary of SI.3; no separate polynomial has been introduced artificially.

---

## 7. Next exact targets

The remaining S1 problem now has three concrete attacks.

1. **Run-boundary/KKT spine.**  CS says both KKT endpoint facets lie on retained cycle edges of `A(F)-g`.  Translate those marked cycle edges into marked sign-run boundaries of `A_+` and combine the two EU/WT endpoint cuts with SI.9.

2. **Small-value rigidity.**  Classify admissible run-boundary polynomials satisfying
   ```math
   |A_+(e^{i\delta})|=2\sin(\delta/2)
   
   ```
   in the D1 interval
   ```math
   0<s<\Delta_2/\delta-2.
   
   ```
   The arbitrary-polynomial problem is false; the admissible maximal-thrackle run word is the essential restriction.

3. **Deformation to the P1 boundary.**  SI.3 shows S1 lies in the same algebraic family as P1.  Prove that any S1 admissible sign word preserving local shell optimality can be continued in `s` until `P(z)=0`, contradicting the completed P1 exclusion, unless it reaches the Reinhardt `s=0` endpoint first.  The obstruction must be a discrete run change or a KKT support singularity; both are now identifiable.

---

## Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| centered ordinary closure (1.4) | proved | direct rewrite of SC |
| `F_m(z)=(z-1)^2P(z)^2` | proved | D1 angle elimination |
| subset-product identity SI.5 | proved | exact `P=S_m-2Q` algebra |
| positive centered product SI.7 | proved | unit-circle identities |
| run-boundary factorization SI.8-SI.10 | proved | telescoping |
| cycle-run count `nu=1+2t_+` | proved | SC seam convention |
| C17 lower bound on `nu` | false/not used | cycle contains short edge |
| S1 exclusion | open | needs admissibility/KKT input beyond sparse identity |
| Level I | still open | S1, d_H=2 audit branch, d_H=0/global population remain |

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN. P1 is closed; S1 is the sole cyclic d_H=1 branch.

Let m=q-2, z=e^{i delta}, and P=sum epsilon_k Z^k be the m ordinary S1 signs.
SC directions center as
  theta_{k+2}=pi/2+(k-(m-1)/2)delta,
so
  z^{-(m-1)/2}P(z)=2 sin(tau/2).
D1 gives G=pi-m delta and D=1/[2 sin(delta/2)]. Eliminating tau yields
  F_m(z)=(z-1)^2 P(z)^2,
where
  F_m=(z^m+1)^2+4z^(m-1)(z-1)^2.

Write P=S_m-2Q, Q in {0,1}[Z]. Then exactly
  z^(m-1) Phi_6(z)+(z-1)^2 Q(z)(S_m(z)-Q(z))=0,
or on |z|=1,
  Q(z)(S_m-Q)(z)=lambda_D z^(m-1),
  lambda_D=(2cos delta-1)/(4 sin^2(delta/2))>0.

Define complementary run-boundary polynomials
  A_-=1+(Z-1)Q,
  A_+=1+(Z-1)(S_m-Q)=Z^m-(Z-1)Q.
Then
  A_-(z)A_+(z)=-z^(m-1)(z-1)^2,
  A_+(z)=z^m conjugate(A_-(z)),
so
  |A_-(z)|=|A_+(z)|=|z-1|.
If a sign subset is a union of runs [a_j,b_j],
  A=1+sum_j(Z^(b_j+1)-Z^a_j),
so A is supported exactly on sign-run boundaries. For the positive ordinary signs,
  antipodal odd-cycle length nu=1+2*(number of positive runs).

Next: mark the two KKT endpoint cycle edges inside this run-boundary word and combine
SI.9 with EU/WT, or prove an admissible S1 word deforms to the now-impossible P1 boundary.
```
