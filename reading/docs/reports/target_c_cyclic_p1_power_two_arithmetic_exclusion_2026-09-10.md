> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_p1_power_two_arithmetic_exclusion_2026-09-10.md) · source SHA-256 `23c88f8a681a08b05a190d5e433a1999c2866a44711d6589c472561f034489b7`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-7B317700323B","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic P1: power-of-two arithmetic exclusion

**Date:** 2026-09-10  
**Repository branch:** `research/target-c-p1-arithmetic-2026-09-10`  
**Run type:** exact algebraic-degree / 2-adic Newton-polygon reduction  
**Target:** cyclic primitive `d_H=1`, P1 endpoint  
**Depends on:** PR #118 signed-closure theorem SC.1 and the P1 angle equation SC.9  
**Computation:** not used in the proof

## LEVEL I STATUS

`STILL OPEN`

The P1 endpoint has a genuinely arithmetic obstruction. Put

```math
m:=q-2,
\qquad
x:=\frac\delta2,
\qquad
z:=e^{i\delta},
\qquad
Y:=z+z^{-1}=2\cos\delta.
```

SC.9 gives

```math
\cos(mx)=2\sin x,
\tag{P2.1}
```

while SC.10--SC.11 give a Littlewood polynomial

```math
P(Z)=\sum_{j=0}^{m-1}\varepsilon_j Z^j,
\qquad \varepsilon_j\in\{\pm1\},
\tag{P2.2}
```

of degree at most `m-1` satisfying

```math
P(z)=0.
\tag{P2.3}
```

This report proves:

### Theorem P2 — power-of-two P1 exclusion

If

```math
\boxed{m=q-2=2^k\ge4,}
```

then the cyclic P1 endpoint is impossible.

Equivalently, no sufficiently large P1 survivor can have `q-2` a power of two.

The proof does not assume that the relevant Chebyshev polynomial is irreducible. It only uses a lower bound on the degree of **every** irreducible factor, obtained from one 2-adic Newton polygon.

---

## 1. Eliminate the half-angle and obtain the trace polynomial

Square (P2.1):

```math
\cos^2(mx)=4\sin^2x.
```

Using

```math
2\cos^2(mx)=1+\cos(2mx),
\qquad
2\sin^2x=1-\cos(2x),
```

and `2x=delta`, we get

```math
1+\cos(m\delta)=4-4\cos\delta,
```

hence

```math
\boxed{\cos(m\delta)+4\cos\delta-3=0.}
\tag{P2.4}
```

Let `C_n(T)` be the monic integer trace-Chebyshev sequence

```math
C_0(T)=2,
\qquad
C_1(T)=T,
\qquad
C_n(T)=T C_{n-1}(T)-C_{n-2}(T).
\tag{P2.5}
```

Thus

```math
C_n(2\cos\theta)=2\cos(n\theta).
```

Equation (P2.4) says exactly

```math
\boxed{G_m(Y)=0,}
\qquad
G_m(T):=C_m(T)+4T-6\in\mathbb Z[T].
\tag{P2.6}
```

For reference, the corresponding reciprocal polynomial for `z` is

```math
\begin{aligned}
F_m(Z)
&:=Z^mG_m(Z+Z^{-1})\\
&=Z^{2m}+4Z^{m+1}-6Z^m+4Z^{m-1}+1\\
&=(Z^m+1)^2+4Z^{m-1}(Z-1)^2.
\end{aligned}
\tag{P2.7}
```

No irreducibility assertion about `F_m` or `G_m` is needed below.

---

## 2. The Littlewood closure gives a factor of degree at most `(m-1)/2`

Equation (P2.3) gives

```math
[\mathbb Q(z):\mathbb Q]\le m-1.
\tag{P2.8}
```

Because `0<delta<pi`, `z` is nonreal, whereas

```math
Y=z+z^{-1}=2\cos\delta
```

is real. Also `z` satisfies

```math
Z^2-YZ+1=0
\tag{P2.9}
```

over `Q(Y)`. Under the distinguished real embedding, every element of `Q(Y)` is real, so `z` does not belong to `Q(Y)`. Therefore

```math
\boxed{[\mathbb Q(z):\mathbb Q(Y)]=2.}
\tag{P2.10}
```

Combining (P2.8)--(P2.10),

```math
\boxed{
[\mathbb Q(Y):\mathbb Q]
\le\frac{m-1}{2}.
}
\tag{P2.11}
```

Since `Y` is a root of `G_m`, the irreducible factor of `G_m` containing the geometric P1 root `Y` therefore has degree at most `(m-1)/2`.

This is the only use of the Littlewood polynomial. In particular, we do **not** need to classify all Littlewood zeros on the unit circle.

---

## 3. Doubling identity for the trace-Chebyshev sequence

The trace identity

```math
(u^n+u^{-n})^2-2=u^{2n}+u^{-2n}
```

gives

```math
\boxed{C_{2n}(T)=C_n(T)^2-2.}
\tag{P2.12}
```

For `j>=0`, define

```math
H_j(X):=C_{2^j}(2+X)-2.
\tag{P2.13}
```

Then

```math
H_0(X)=X
```

and (P2.12) gives the exact recursion

```math
\boxed{H_{j+1}=H_j(H_j+4).}
\tag{P2.14}
```

Modulo four this yields inductively

```math
\boxed{H_j(X)\equiv X^{2^j}\pmod4.}
\tag{P2.15}
```

Indeed it is true for `j=0`, and

```math
H_{j+1}=H_j^2+4H_j\equiv H_j^2\pmod4.
```

---

## 4. One-edge 2-adic Newton polygon

Now assume

```math
m=2^k\ge4.
```

By definition of `G_m`,

```math
\begin{aligned}
G_m(2+X)
&=C_m(2+X)+4(2+X)-6\\
&=H_k(X)+4X+4.
\end{aligned}
\tag{P2.16}
```

Equation (P2.15) therefore gives

```math
\boxed{G_m(2+X)\equiv X^m\pmod4.}
\tag{P2.17}
```

More explicitly:

- the constant coefficient is exactly `4`, hence has 2-adic valuation `2`;
- the leading coefficient is `1`, hence has valuation `0`;
- every intermediate coefficient is divisible by `4`, hence has valuation at least `2`.

Therefore the lower 2-adic Newton polygon of `G_m(2+X)` consists of the single segment

```math
(0,2)\longrightarrow(m,0),
\tag{P2.18}
```

with slope

```math
-\frac2m=-\frac1{m/2}.
\tag{P2.19}
```

The Newton-polygon root theorem says that every root in an algebraic closure of `Q_2` has 2-adic valuation `2/m`. Consequently, if an irreducible factor over `Q_2` has degree `d`, the valuation of its constant term is

```math
\frac{2d}{m},
```

which is an integer. Hence

```math
\boxed{\frac m2\mid d.}
\tag{P2.20}
```

Every irreducible factor over `Q` splits over `Q_2` into factors of this kind, so every nonconstant irreducible factor of `G_m` over `Q` has degree at least

```math
\boxed{m/2.}
\tag{P2.21}
```

This is weaker than irreducibility and is exactly strong enough for P1.

---

## 5. Contradiction

The geometric P1 root `Y` lies in some irreducible factor of `G_m` over `Q`.

By (P2.11), that factor has degree at most

```math
\frac{m-1}{2}.
```

By (P2.21), it has degree at least

```math
\frac m2.
```

These inequalities are incompatible.

Therefore no P1 source exists when `m=q-2` is a power of two at least four. This proves Theorem P2. `square`

---

## 6. Stronger algebraic reduction for the general P1 problem

The proof isolates the exact general arithmetic target.

For arbitrary `m=q-2`, a P1 survivor requires the distinguished real root

```math
Y=2\cos\delta
```

of

```math
G_m(T)=C_m(T)+4T-6
```

to satisfy

```math
\boxed{
\deg_{\mathbb Q}Y\le\frac{m-1}{2}.
}
\tag{P2.22}
```

Thus **any** theorem showing that the irreducible factor of `G_m` containing the P1 root has degree at least `m/2` closes P1 completely.

Exact symbolic factorization for finite `m` strongly suggests the much stronger pattern that `G_m` is irreducible unless `6|m`, and when `6|m` its only rational factorization is

```math
G_m(T)=(T-1)H_{m-1}(T)
```

with `H_{m-1}` irreducible. This observation is computational evidence only and is not used in Theorem P2.

The factor `T-1` when `6|m` is elementary:

```math
C_m(1)=2\cos(m\pi/3)=2,
```

so `G_m(1)=0`. The geometric P1 root tends to `2`, not `1`, so a proof that all remaining factors have degree at least `m/2` would still close those cases.

---

## 7. Regression and scope audit

- The argument uses the exact P1 parallel-side endpoint. It does not apply directly to the S1 interior defect.
- Squaring (P2.1) introduces extra roots of `G_m`, but this is harmless: the actual P1 root remains a root, and the proof only lower-bounds the degree of every factor in the power-of-two case.
- The Newton-polygon argument is exact; no numerical root approximation is used.
- No claim is made that a general unit-circle Littlewood zero is cyclotomic. That statement is false in general and is unnecessary here.
- `m=2` is below the intended sufficiently-large regime and is not needed. It can be checked separately if desired.
- LEVEL I remains open because arbitrary `m`, S1, `d_H=2`, and the other post-ZF branches remain.

---

## 8. Next target

The arithmetic endpoint is now:

> Prove that the distinguished root near `2` of `G_m(T)=C_m(T)+4T-6` has algebraic degree at least `m/2` for every `m>=3`.

Three concrete continuations are available:

1. extend the 2-adic Newton argument from `m=2^k` using the odd part of `m` and the exact factorization of `C_m mod 2`;
2. prove directly that every factor of `G_m` of degree `<m/2` is the elementary `T-1` factor occurring when `6|m`;
3. import a precise irreducibility/factor-degree theorem for Dickson/Chebyshev polynomials plus a linear perturbation, if its hypotheses match this exact polynomial.

The second formulation is strictly weaker than full irreducibility and is the preferred target.
