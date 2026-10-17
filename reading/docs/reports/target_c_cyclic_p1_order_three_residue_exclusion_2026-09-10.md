> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_p1_order_three_residue_exclusion_2026-09-10.md) · source SHA-256 `5bce2f944ee0cdf594908919dd14925abb7253321c3ca3f53c7fc44331149836`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-52C7388CD1FB","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
LEVEL I STATUS: STILL OPEN

# Erdős Problem #99 — cyclic P1 cannot use the order-three 2-adic residue block

**Date:** 2026-09-10  
**Repository branch:** `research/target-c-p1-residue-saturation-2026-09-10`  
**Run type:** exact exceptional Newton-cluster exclusion  
**Target:** cyclic primitive `d_H=1`, P1 endpoint  
**Depends on:** NRS on this branch, PR #152 residue localization, PR #153 cyclotomic-factor classification, SC Littlewood closure  
**External literature:** standard Newton-polygon theorem only  
**Computation:** none

## 1. Result

Write

$$
m=ru,
\qquad r=2^k,
\qquad u\text{ odd},
$$

and let `M(Z)` be the monic minimal polynomial of the physical P1 root. PR #152 excludes the residue root `Z=1`; NRS proves exact multiplicity saturation for every nontrivial odd-order residue block except order three.

The only untreated block is

$$
\phi_3(Z):=Z^2+Z+1
$$

over `F_2`, corresponding to nontrivial cube roots.

### Theorem O3X — order-three residue exclusion

For every P1 candidate,

$$
\boxed{
\phi_3(Z)\nmid\overline M(Z).
}
\tag{O3X.1}
$$

This holds whether `m` is odd or even.

Combining O3X with PR #152 and NRS gives the complete mod-two normal form:

### Corollary — complete residue saturation normal form

There is a squarefree self-reciprocal polynomial

$$
B(Z)\mid S_u(Z)
$$

such that

$$
\gcd(B,(Z+1)\phi_3)=1
$$

and

$$
\boxed{
\overline M(Z)=B(Z)^r.
}
\tag{O3X.2}
$$

Therefore

$$
\boxed{
\deg M=r\deg B.
}
\tag{O3X.3}
$$

Every characteristic-two residue block used by the physical factor is a complete odd-cyclotomic block, saturated to exactly the `2^k` multiplicity supplied by the Littlewood polynomial, and neither the trivial nor order-three block may occur.

This recovers both previously excluded odd parts `u=1` and `u=3` as immediate degenerate cases: there is then no admissible nonconstant `B`.

---

## 2. Setup in the reciprocal variable

The reciprocal P1 polynomial is

$$
F_m(Z)
=(Z^m+1)^2+4Z^{m-1}(Z-1)^2.
\tag{2.1}
$$

The P1 Littlewood closure gives

$$
M\mid P,
\qquad
\overline P=S_m
=(Z+1)^{r-1}S_u^r.
\tag{2.2}
$$

Because `u` is odd, every irreducible factor of `S_u`, including `phi_3` when `3|u`, occurs in `S_m` with exact multiplicity `r`.

Thus if

$$
\phi_3\mid\overline M,
$$

the exponent of `phi_3` in `bar M` is at most

$$
\boxed r.
\tag{2.3}
$$

We prove that every possible noncyclotomic local lift of this residue block needs strictly more than `r` copies.

---

## 3. Teichmüller lift of the cube-root residue

Assume `3|u`. Let

$$
\xi\in\mathbf F_4
$$

be a primitive cube root and let

$$
\zeta\in\mathcal O_K,
\qquad K/\mathbf Q_2\text{ unramified quadratic},
$$

be its Teichmüller lift. Then

$$
\zeta^2+\zeta+1=0,
\qquad
\zeta^u=1,
\qquad
\zeta^m=1.
\tag{3.1}
$$

In particular

$$
\zeta+\zeta^{-1}=-1.
$$

Evaluate (2.1):

$$
\begin{aligned}
F_m(\zeta)
&=4\left(1+\zeta^{-1}(\zeta-1)^2\right)\\
&=4(\zeta+\zeta^{-1}-1)\\
&=-8.
\end{aligned}
$$

Hence

$$
\boxed{v_2(F_m(\zeta))=3.}
\tag{O3X.4}
$$

This is exactly why NRS's generic `(0,2)` Newton edge did not cover order three.

As in NRS, for every power of two `r`,

$$
F_m(Z)\equiv(Z^u+1)^{2r}\pmod4.
\tag{3.2}
$$

Since `Z^u+1` has a simple root at `xi`, after putting

$$
Z=\zeta+X
$$

the coefficient of `X^(2r)` is a unit and every coefficient of degrees `1,...,2r-1` is divisible by four.

The only additional datum needed is the exact valuation of the linear coefficient.

---

## 4. The linear coefficient

Differentiate (2.1):

$$
\begin{aligned}
F_m'(Z)
={}&2(Z^m+1)mZ^{m-1}\\
&+4(m-1)Z^{m-2}(Z-1)^2\\
&+8Z^{m-1}(Z-1).
\end{aligned}
\tag{4.1}
$$

At `Z=zeta`, using `zeta^m=1`,

$$
\frac{F_m'(\zeta)}4
=
 m\zeta^{-1}
 +(m-1)\zeta^{-2}(\zeta-1)^2
 +2\zeta^{-1}(\zeta-1).
\tag{4.2}
$$

### Even `m`, equivalently `r>=2`

Modulo two, the first and third terms vanish while `m-1` is odd. Therefore

$$
\frac{F_m'(\zeta)}4
\equiv
\xi^{-2}(\xi-1)^2
\not=0
\pmod2.
$$

Hence

$$
\boxed{v_2(F_m'(\zeta))=2.}
\tag{O3X.5e}
$$

### Odd `m`, equivalently `r=1`

Now `m` is odd and `m-1` is even. Modulo two only the first term survives:

$$
\frac{F_m'(\zeta)}4
\equiv\xi^{-1}\not=0.
$$

Thus again

$$
\boxed{v_2(F_m'(\zeta))=2.}
\tag{O3X.5o}
$$

The same linear valuation occurs in both parity cases, but the Newton lower hull differs because the endpoint length `2r` differs.

---

## 5. Odd `m`: immediate multiplicity contradiction

Suppose

$$
r=1.
$$

The local coefficient valuations are:

- degree `0`: exactly `3` by O3X.4;
- degree `1`: exactly `2` by O3X.5o;
- degree `2`: exactly `0` by the mod-two multiplicity calculation.

The line from `(0,3)` to `(2,0)` has height `3/2` at degree one, below the actual point `(1,2)`. Hence the lower Newton polygon begins with the single segment

$$
\boxed{(0,3)\longrightarrow(2,0)}
\tag{O3X.6}
$$

of slope

$$
-3/2.
$$

Every irreducible local factor above the cube-root residue therefore has degree divisible by `2`, in particular at least two. Consequently any rational factor using this residue block has

$$
\phi_3^e\mid\overline M
\qquad\text{with }e\ge2.
$$

But the Littlewood ceiling (2.3) is `r=1`. Contradiction.

Thus O3X.1 holds when `m` is odd.

---

## 6. Even `m`: split off the unique cyclotomic slope

Now assume

$$
r\ge2.
$$

The local coefficient valuations give the points

$$
(0,3),
\qquad
(1,2),
\qquad
(2r,0),
$$

while every coefficient of degrees `2,...,2r-1` has valuation at least two.

Therefore the lower Newton polygon is exactly

$$
\boxed{
(0,3)\longrightarrow(1,2)
\longrightarrow(2r,0).
}
\tag{O3X.7}
$$

The two slopes are

$$
-1
\qquad\text{and}\qquad
-\frac2{2r-1}.
\tag{6.1}
$$

The first segment has horizontal length one. There is therefore exactly one local root reducing to `xi` with

$$
v_2(Z-\zeta)=1.
$$

Because `6|m`, PR #153 proves that `F_m` has the exact cyclotomic factor

$$
\Phi_6(Z)=Z^2-Z+1.
$$

Over `K`, its root reducing to `xi` is

$$
-\zeta,
$$

and

$$
(-\zeta)-\zeta=-2\zeta
$$

has valuation one. Hence the unique first-segment root is precisely the known primitive-sixth-root lift.

PR #153 also proves that the physical P1 minimal polynomial `M` is noncyclotomic. Therefore `M` cannot contain this first-segment root: if `M(-zeta)=0` in an algebraic closure of `Q_2`, then the algebraic number `-zeta` satisfies `M` and its rational minimal polynomial `Phi_6` divides `M`, contradicting irreducibility/noncyclotomicity.

Thus if `M` uses the residue factor `phi_3`, it must use a root on the second Newton segment.

That segment has slope

$$
-\frac2{2r-1}
$$

in lowest terms because `2r-1` is odd. Every irreducible local factor containing one of its roots has degree divisible by

$$
2r-1.
$$

Hence its reduction contributes at least

$$
\boxed{2r-1}
\tag{O3X.8}
$$

copies of the local residue root. After the unramified Frobenius conjugate is restored, this means

$$
\phi_3^{\,2r-1}\mid\overline M.
$$

But

$$
2r-1>r
\qquad(r\ge2),
$$

contradicting the Littlewood ceiling (2.3).

Therefore O3X.1 also holds for even `m`. `square`

---

## 7. Complete mod-two normal form

PR #152 proves

$$
Z+1\nmid\overline M.
$$

O3X proves

$$
\phi_3\nmid\overline M.
$$

Every remaining residue factor has odd order different from one and three, so NRS applies and forces its exponent to equal exactly `r`.

Since `S_u` is squarefree, let `B` be the product of the distinct remaining residue factors used by `M`. Then

$$
\boxed{\overline M=B^r,}
$$

with

$$
B\mid S_u,
\qquad
B\text{ squarefree},
\qquad
\gcd(B,(Z+1)(Z^2+Z+1))=1.
$$

Reciprocity of `M` forces reciprocity of `B`, exactly as in NRS.

This proves O3X.2-O3X.3.

---

## 8. Immediate family consequences

### `u=1`

`S_u=1`, so no nonconstant `B` exists. P1 is impossible. This recovers the power-of-two family.

### `u=3`

`S_3=Z^2+Z+1`, but O3X excludes this entire block. Again no nonconstant `B` exists. This recovers the `3*2^k` family from PR #150, now as a consequence of the general residue theorem.

### General `u`

Only odd-order residue factors whose order divides `u` but is neither `1` nor `3` may occur. Each occurs with exact multiplicity `r`.

Thus the 2-adic endpoint is now completely classified at the multiplicity level.

---

## 9. Interaction with PR #153 and mod three

PR #153 gives independently

$$
F_m(Z)\equiv
(Z^{m-1}+1)(Z^{m+1}+1)
\pmod3.
$$

The physical characteristic-zero factor is noncyclotomic, yet O3X/NRS force

$$
\overline M=B^{2^k}
$$

with `B` squarefree and assembled from complete odd-cyclotomic residue blocks of orders dividing `u`, excluding orders one and three.

Therefore the remaining P1 problem has become a simultaneous two-prime factor problem:

> classify noncyclotomic reciprocal irreducible `M|F_m` whose mod-two reduction is an exact `2^k`th power of a squarefree self-reciprocal divisor of `S_u` with no order-one or order-three block, while `M mod 3` divides the product of the two adjacent binomials `Z^(m-1)+1` and `Z^(m+1)+1`.

This is substantially narrower than generic irreducibility of `F_m`.

---

## 10. Audit / edge cases

- The primitive cube root used in the local calculation is the Teichmüller order-three lift `zeta`, not the characteristic-zero primitive-sixth root. They reduce to the same nontrivial residue in characteristic two.
- For even `m`, the slope-`-1` root is identified with `-zeta`, the primitive-sixth root. The noncyclotomic classification from PR #153 is essential for excluding that one local branch from `M`.
- The second segment denominator is exactly `2r-1`; no irreducibility of the whole second cluster is claimed.
- For odd `m`, there is no `Phi_6` factor and the direct slope `-3/2` already exceeds the Littlewood multiplicity budget.
- The conclusion is about the physical irreducible factor `M`, not every noncyclotomic factor of `F_m`.
- O3X does not yet contradict the existence of `B` for odd parts having divisors other than one and three.

---

## 11. Next theorem

The complete mod-two classification leaves no unresolved 2-adic residue type. The next useful theorem should now use a second prime rather than refine the same Newton calculation.

A concrete target is:

> **Two-prime block incompatibility.** Let `M` be a noncyclotomic reciprocal irreducible factor of `F_m` with `deg M<=m-1`. If
> 

$$

> \overline M^{(2)}=B^{2^k}
> 
$$


> for a squarefree self-reciprocal `B|S_u` with no order-one/order-three block, prove that the mod-three factorization
> 

$$

> \overline F_m^{(3)}=(Z^{m-1}+1)(Z^{m+1}+1)
> 
$$


> cannot accommodate `M`.

The first cases to attack are odd part `u=p` prime. Then the entire mod-two residue support lies over the single odd cyclotomic family `Phi_p`, and the degree of `M` is quantized by the Frobenius orbit size of `2` modulo `p`.

---

## 12. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Complete the NRS residue classification at order 3.
Let phi_3=Z^2+Z+1 and zeta be the 2-adic Teichmuller cube root.
For 3|u:
    F_m(zeta)=-8, so v=3.
Also F_m == (Z^u+1)^(2r) mod4 and the X^(2r) coefficient at Z=zeta+X is a unit.
Direct differentiation gives v(F'_m(zeta))=2.

If r=1, the Newton hull is
    (0,3)->(2,0), slope -3/2.
Any local factor uses >=2 copies of phi_3, but S_m supplies only r=1. Impossible.

If r>=2, the hull is
    (0,3)->(1,2)->(2r,0).
The unique slope -1 root is -zeta, the known Phi_6 root (6|m). PR #153 proves the
physical M is noncyclotomic, so M cannot use it. Every remaining root is on slope
    -2/(2r-1),
forcing local degree/exponent >=2r-1>r, again exceeding the Littlewood multiplicity.
Thus phi_3 never divides M mod2.

Together with PR #152 and NRS:
    M mod2 = B^r,
where r=2^k and B is squarefree self-reciprocal, B|S_u, and B contains neither
Z+1 nor Z^2+Z+1.  Hence deg M=r deg B.
This recovers u=1 and u=3 exclusions and leaves a two-prime block incompatibility problem.
```
