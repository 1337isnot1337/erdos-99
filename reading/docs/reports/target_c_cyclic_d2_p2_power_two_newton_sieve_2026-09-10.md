> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_d2_p2_power_two_newton_sieve_2026-09-10.md) · source SHA-256 `3ab994926055f25d54d990b0f6d1132fb1e9bb301d9eff88c21dd6d5eea1c091`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-58A405EBD380","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic `d_H=2`, P2: power-of-two 2-adic Newton sieve

**Date:** 2026-09-10  
**Repository branch:** `research/post-zf-currency-coupling-2026-09-09`  
**Run type:** exact arithmetic theorem / infinite P2 subclass reduction  
**Target:** P2 subphase of the cyclic `d_H=2` endpoint  
**Depends on:** P2A algebraic degree sieve  
**External literature:** only the standard Newton-polygon factor-degree theorem  
**Computation:** none used in the proof

## LEVEL I STATUS

`STILL OPEN`

P2A reduced the P2 branch to the degree `r_m` of the irreducible factor containing the physical root of

```math
H_m(X)=2T_m(X/2)+16X^2-48X+34,
\qquad m=q-4.
```

For the infinite subsequence `m=2^k`, the Chebyshev doubling recurrence gives an unusually rigid 2-adic Newton polygon.

### Theorem P2N — power-of-two Newton sieve

Let

```math
m=2^k\ge4.
```

Then every irreducible factor of `H_m` over `Q` has degree divisible by

```math
\boxed{m/2.}
\tag{P2N.1}
```

Consequently `H_m` has only two possible rational factorization types:

1. `H_m` is irreducible of degree `m`; or
2. `H_m` is the product of exactly two irreducible factors, each of degree `m/2`.

In particular the physical factor degree satisfies

```math
\boxed{r_m\in\{m/2,m\}.}
\tag{P2N.2}
```

Combining with P2A:

- if `r_m=m`, P2 is impossible;
- if a P2 survivor exists with `r_m=m/2`, both staircase lengths are positive and
  
  ```math
  \boxed{\max(L_A,L_B)\ge m/2+1,}
  \tag{P2N.3}
  ```

  hence
  
  ```math
  \boxed{|L_A-L_B|\ge2.}
  \tag{P2N.4}
  ```


Thus on the power-of-two subsequence the only arithmetic escape is an exact half-degree split of `H_m`, accompanied by a strictly unbalanced two-tree decomposition.

---

## 1. Monic Chebyshev trace recurrence

Write

```math
S_n(X):=2T_n(X/2).
```

Then

```math
S_1(X)=X,
\qquad
S_{2n}(X)=S_n(X)^2-2.
\tag{1.1}
```

For

```math
A_m(Y):=S_m(2+Y),
```
we therefore have

```math
A_{2m}(Y)=A_m(Y)^2-2.
\tag{1.2}
```

Starting with

```math
A_2(Y)=S_2(2+Y)=(2+Y)^2-2=2+4Y+Y^2,
```
we obtain the following exact congruence by induction.

### Lemma P2N.1

For every power of two `m>=2`,

```math
\boxed{
S_m(2+Y)
\equiv
2+4Y^{m/2}+Y^m
\pmod 8.
}
\tag{1.3}
```

### Proof

The formula is exact modulo eight for `m=2`. Assume

```math
A_m(Y)\equiv2+4Y^{m/2}+Y^m\pmod8.
```

Squaring and subtracting two gives

```math
\begin{aligned}
A_{2m}(Y)
&\equiv
(2+4Y^{m/2}+Y^m)^2-2\\
&\equiv
2+4Y^m+Y^{2m}
\pmod8,
\end{aligned}
```

because every other cross term is divisible by eight. This is exactly (1.3) with `2m` in place of `m`. `square`

---

## 2. Add the fixed P2 trace perturbation

At `X=2+Y`,

```math
16X^2-48X+34
=2+16Y+16Y^2.
\tag{2.1}
```

Thus for `m>=4`, Lemma P2N.1 gives

```math
\boxed{
H_m(2+Y)
\equiv
4+4Y^{m/2}+Y^m
\pmod8.
}
\tag{2.2}
```

Let

```math
H_m(2+Y)=\sum_{j=0}^m c_jY^j.
```

Equation (2.2) implies

```math
\nu_2(c_0)=2,
\qquad
\nu_2(c_m)=0,
\tag{2.3}
```

while

```math
\nu_2(c_{m/2})=2
\tag{2.4}
```

and every other internal coefficient has

```math
\nu_2(c_j)\ge3.
\tag{2.5}
```

The leading coefficient is one because `S_m`, hence `H_m`, is monic.

---

## 3. The lower 2-adic Newton polygon is one segment

Plot the coefficient points

```math
(j,\nu_2(c_j)).
```

The straight line from

```math
(0,2)
\quad\text{to}\quad
(m,0)
```

has height

```math
2-\frac{2j}{m}.
\tag{3.1}
```

For every internal index `0<j<m` this height is strictly less than two.  Equations (2.4)-(2.5) put every internal coefficient point strictly above that line. Therefore the lower Newton polygon consists of the single edge

```math
\boxed{(0,2)\longrightarrow(m,0),}
\tag{3.2}
```

of slope

```math
-\frac2m=-\frac1{m/2}.
\tag{3.3}
```

The slope is in lowest terms because `m/2` is a power of two.

By the standard Newton-polygon factor-degree theorem, every irreducible factor over `Q_2` attached to this polygon has degree divisible by the denominator of the reduced slope, namely `m/2`.

Any irreducible factor over `Q` factors further over `Q_2`; its degree is the sum of the degrees of its `Q_2` factors. Hence its rational degree is also divisible by `m/2`.

Since the total degree of `H_m` is `m`, P2N.1-P2N.2 follow. `square`

---

## 4. Insert the P2A staircase degree sieve

P2A proves that when both P2 staircase lengths are positive,

```math
\max(L_A,L_B)\ge r_m+1.
\tag{4.1}
```

If `H_m` is irreducible, then `r_m=m`, while

```math
L_A+L_B=m,
```

so (4.1) is impossible.

Suppose instead that the physical factor has degree `m/2`. Then (4.1) gives

```math
\max(L_A,L_B)\ge m/2+1.
```

Since their sum is `m`, the other staircase has length at most `m/2-1`, proving the imbalance (P2N.4).

If one staircase had length zero, P2A already gives a Littlewood polynomial of degree `m-1` vanishing at the physical `z`. The minimal polynomial of `z` has degree

```math
2r_m\ge m,
```

so this is impossible. Thus any half-degree escape has both staircase lengths positive. `square`

---

## 5. What this proves and what it does not

This is an infinite theorem, not a finite factorization experiment.

It proves that for every power-of-two `m`, P2 has only one possible arithmetic escape:

```text
H_m splits exactly m/2 + m/2,
physical factor degree = m/2,
both diameter-tree staircases nonempty,
one staircase has length >=m/2+1,
the other has length <=m/2-1.
```

The exact factor audit through `m=60` finds `H_m` irreducible for every checked power of two, so no checked value realizes the half-degree escape. That computation remains evidence only.

The next arithmetic target on this subsequence is therefore much smaller than P2-I:

> exclude a factor of degree exactly `m/2` from `H_m` when `m` is a power of two.

A second geometric target is to exclude the forced component imbalance (P2N.4) directly from the P2 two-rectangle / four-block geometry. Either result kills P2 on the full power-of-two subsequence.

---

## 6. Regression audit

### Newton polygon versus irreducibility

A one-edge Newton polygon of slope `-2/m` does **not** prove irreducibility because the reduced denominator is only `m/2`. The possible split into two degree-`m/2` factors is retained explicitly.

### Translation

Replacing `X` by `2+Y` is an automorphism of `Q[X]`, so it preserves rational factor degrees.

### P2A zero-length branch

Handled separately in Section 4; no division by an empty staircase polynomial is used.

### Finite SymPy factorization

Not used. P2N is a direct 2-adic theorem valid for every power-of-two `m>=4`.
