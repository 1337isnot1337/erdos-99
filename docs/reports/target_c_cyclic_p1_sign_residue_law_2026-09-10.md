<!-- theorem-state: {"artifact_id":"ART-AB0757A2D24E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
LEVEL I STATUS: STILL OPEN

# Erdős Problem #99 — cyclic P1 sign-residue law and maximal odd-degree exclusion

**Date:** 2026-09-10  
**Repository branch:** `research/target-c-p1-residue-saturation-2026-09-10`  
**Run type:** exact Littlewood-sign / local-residue theorem  
**Target:** cyclic primitive `d_H=1`, P1 endpoint  
**Depends on:** complete mod-two normal form NRS/O3X on this branch, SC P1 Littlewood closure, reciprocal P1 identity  
**External literature:** none  
**Computation:** none

## 1. Result

Let

\[
m=ru,
\qquad r=2^k,
\qquad u\text{ odd},
\]

and let

\[
P(Z)=\sum_{j=0}^{m-1}\varepsilon_jZ^j,
\qquad \varepsilon_j\in\{+1,-1\},
\]

be the P1 Littlewood annihilator supplied by SC.

Write it uniquely as

\[
\boxed{
P(Z)=S_m(Z)-2Q(Z),
\qquad
S_m(Z)=1+Z+\cdots+Z^{m-1},
}
\tag{SRL.1}
\]

where

\[
Q(Z)\in\{0,1\}[Z]
\]

is the indicator polynomial of the negative signs.

Let `M` be the physical P1 root's minimal polynomial. NRS/O3X give

\[
\overline M(Z)=B(Z)^r,
\]

where `B` is squarefree self-reciprocal,

\[
B\mid S_u,
\qquad
\gcd(B,(Z+1)(Z^2+Z+1))=1.
\]

The new theorem reconstructs the parity pattern of the negative signs on every selected residue block.

### Theorem SRL — exact sign-residue law

In `F_2[Z]`,

\[
\boxed{
B(Z)\mid
 (Z+1)Q(Z)
 +Z^{(u+1)/2}
 +Z^{(u-1)/2}
 +1.
}
\tag{SRL.2}
\]

Equivalently, in the quotient `F_2[Z]/(B)`,

\[
\boxed{
Q(Z)\equiv
 Z^{(u-1)/2}+(Z+1)^{-1}.
}
\tag{SRL.3}
\]

Thus the Littlewood sign word is not arbitrary even after the complete mod-two factor support has been chosen: its negative-sign indicator has one prescribed residue class modulo `B`.

This yields an exact phase exclusion.

### Corollary SRL-M — maximal odd trace degree is impossible

Assume

\[
r=1,
\qquad m=u\ge5\text{ odd}.
\]

Then the physical minimal polynomial cannot have reciprocal degree

\[
\boxed{\deg M=m-1.}
\tag{SRL.4}
\]

Equivalently, the complete mod-two block

\[
B=S_m
\]

is impossible.

Therefore every odd P1 candidate with `m>=5` must omit at least one complete reciprocal mod-two residue block. In particular

\[
\boxed{\deg M\le m-3.}
\tag{SRL.5}
\]

For example, if `m=p>=5` is an odd prime and `Phi_p` is irreducible over `F_2` (equivalently `ord_p(2)=p-1`), then no P1 candidate exists at all, because the only nonzero admissible mod-two block is the full `S_p=Phi_p` block.

---

## 2. Evaluate the Littlewood relation at a selected 2-adic residue root

Let

\[
\xi
\]

be any root of `B` in a finite extension of `F_2`. By the complete residue theorem, `xi` has odd order dividing `u` and has order neither one nor three.

Let `K/Q_2` be the unramified extension containing the Teichmüller lift

\[
\zeta
\]

of `xi`, and let

\[
\alpha
\]

be any local root of `M` reducing to `zeta`.

Since `M|P`,

\[
P(\alpha)=0.
\]

Using SRL.1,

\[
\boxed{
S_m(\alpha)=2Q(\alpha).
}
\tag{2.1}

Because `xi!=1`, the denominator `alpha-1` is a 2-adic unit. Write

\[
S_m(\alpha)=\frac{\alpha^m-1}{\alpha-1}.
\tag{2.2}

The reciprocal P1 polynomial satisfies the exact identity

\[
\boxed{
(\alpha^m+1)^2
=-4\alpha^{m-1}(\alpha-1)^2.
}
\tag{2.3}

Define

\[
R_\alpha
:=
\frac{\alpha^m+1}{2(\alpha-1)}.
\tag{2.4}

Equation (2.3) gives

\[
\boxed{
R_\alpha^2=-\alpha^{m-1}.
}
\tag{2.5}

Also

\[
\begin{aligned}
Q(\alpha)
&=\frac{S_m(\alpha)}2\\
&=\frac{\alpha^m-1}{2(\alpha-1)}\\
&=R_\alpha-\frac1{\alpha-1}.
\end{aligned}
\tag{2.6}

Reduce modulo the maximal ideal. Since `xi^m=1`,

\[
\overline{R_\alpha}^{\,2}=\xi^{-1}.
\]

The finite residue field has characteristic two, so squaring is an automorphism. Since `xi^u=1` and `u` is odd,

\[
\left(\xi^{(u-1)/2}\right)^2
=\xi^{u-1}
=\xi^{-1}.
\]

Therefore

\[
\boxed{
\overline{R_\alpha}=\xi^{(u-1)/2}.
}
\tag{2.7}

Reducing (2.6), where subtraction equals addition in characteristic two, gives

\[
\boxed{
Q(\xi)
=\xi^{(u-1)/2}+\frac1{\xi+1}.
}
\tag{SRL.6}

Multiply by `xi+1`:

\[
(\xi+1)Q(\xi)
+\xi^{(u+1)/2}
+\xi^{(u-1)/2}
+1
=0.
\]

Every root of the squarefree polynomial `B` satisfies this identity, so `B` divides the displayed polynomial. This proves SRL.2-SRL.3. `square`

---

## 3. Solve the residue law when the full odd block is selected

Now assume

\[
r=1,
\qquad m=u\text{ odd},
\qquad B=S_u.
\]

In `F_2[Z]/(S_u)`, `Z^u=1`. The inverse of `Z+1` has the explicit representative

\[
\boxed{
A_u(Z):=1+Z^2+Z^4+\cdots+Z^{u-1}.
}
\tag{3.1}

Indeed

\[
(Z+1)A_u(Z)
=S_u(Z)+Z^u
\equiv1\pmod{S_u}.
\tag{3.2}

Put

\[
e:=\frac{u-1}{2}.
\]

SRL.3 becomes

\[
Q(Z)\equiv
R_u(Z):=Z^e+A_u(Z)
\pmod{S_u}.
\tag{3.3}

Both `Q` and `R_u` have degree at most `u-1`. Since `S_u` has degree `u-1`, there are only two possibilities in `F_2[Z]`:

\[
\boxed{
Q=R_u
\quad\text{or}\quad
Q=R_u+S_u.
}
\tag{3.4}

The second possibility is exactly the coefficientwise complement of the first and therefore changes `P` to `-P`. Thus the Littlewood word is determined up to global sign.

---

## 4. Its value at `Z=-1` is forced

We compute `R_u(-1)` over the integers using the same `0/1` representative.

The even-power polynomial `A_u` has

\[
\frac{u+1}{2}
\]

terms, all equal to `+1` at `Z=-1`.

If `e` is even, the monomial `Z^e` is already present in `A_u`, so addition in `F_2` deletes it. Thus the integer `0/1` representative `R_u` has

\[
R_u(-1)=\frac{u-1}{2}.
\]

If `e` is odd, `Z^e` is not present in `A_u`; adding it contributes `-1` at `Z=-1`. Again

\[
R_u(-1)=\frac{u+1}{2}-1
=\frac{u-1}{2}.
\]

Therefore in either case

\[
\boxed{
R_u(-1)=\frac{u-1}{2}.
}
\tag{4.1}

Since

\[
S_u(-1)=1
\qquad(u\text{ odd}),
\]

we obtain from `P=S_u-2Q`

\[
P(-1)=2-u
\]

for `Q=R_u`, and the negative value for the complementary choice. Hence

\[
\boxed{|P(-1)|=u-2.}
\tag{SRL.7}

---

## 5. Maximal degree forces `P` to be the minimal polynomial

Still assume `r=1`, `B=S_u`. The complete mod-two normal form gives

\[
\deg M=\deg B=u-1=m-1.
\]

But SC's Littlewood polynomial also has degree exactly `m-1`, and `M|P`. Since both are primitive with leading coefficient of absolute value one,

\[
\boxed{P=\pm M.}
\tag{5.1}

The reciprocal P1 polynomial at `Z=-1` is

\[
F_m(-1)=16
\qquad(m\text{ odd}).
\tag{5.2}

Since `M` is a monic integer factor of `F_m`,

\[
M(-1)\mid16.
\tag{5.3}

Moreover

\[
\overline M(-1)
=\overline M(1)
=S_u(1)
=u
\equiv1\pmod2.
\]

So `M(-1)` is odd. The only odd integer divisors of `16` are `+/-1`. Thus

\[
\boxed{|M(-1)|=1.}
\tag{5.4}

Equations (5.1), SRL.7, and (5.4) imply

\[
u-2=1.
\]

Hence `u=3`. But O3X already excludes the order-three residue block, so the full-block case is impossible there as well. In particular for every

\[
u=m\ge5,
\]

we have a contradiction. This proves SRL.4. `square`

---

## 6. Degree gap for every odd `m>=5`

For `r=1`, the complete normal form is

\[
\overline M=B,
\]

where `B` is squarefree, self-reciprocal, and has only nontrivial odd-order roots other than order three.

SRL-M shows `B` is a proper divisor of `S_m`.

Every nontrivial self-reciprocal factor omitted from `S_m` has degree at least two: the only possible degree-one root in `F_2` is `Z=1`, already absent from `S_m/(Z+1)` for odd `m`, and reciprocal nontrivial odd-order roots occur either in a self-reciprocal block of degree at least two or in a reciprocal pair of equal positive degree.

Therefore

\[
\deg B\le(m-1)-2=m-3.
\]

Since `deg M=deg B` for `r=1`, this proves SRL.5.

---

## 7. Prime odd-part corollary

Let

\[
m=p\ge5
\]

be prime. Then

\[
S_p=\Phi_p.
\]

If `2` is primitive modulo `p`, equivalently

\[
\operatorname{ord}_p(2)=p-1,
\]

then `Phi_p` is irreducible over `F_2`.

The physical `B` is nonconstant, because `M` is nonconstant. Hence the only possible choice is

\[
B=\Phi_p=S_p.
\]

SRL-M excludes that choice. Therefore:

\[
\boxed{
 m=p\ge5\text{ prime and }\operatorname{ord}_p(2)=p-1
 \Longrightarrow \text{P1 impossible}.
}
\tag{SRL.8}

This adds an exact arithmetic family beyond the previously recorded `m=2^k` and `m=3\cdot2^k` exclusions. No claim is made that infinitely many such primes are known.

---

## 8. Additional special-value consequence

The complete mod-two normal form also gives a useful universal fact.

Since `B` is coprime to `Z+1`,

\[
\overline M(1)=1.
\]

Writing

\[
M(Z)=Z^d h(Z+Z^{-1})
\]

for the minimal trace polynomial `h`,

\[
M(1)=h(2).
\]

Because `M|F_m`, equivalently `h|G_m=C_m+4T-6`,

\[
h(2)\mid G_m(2)=4.
\]

But `h(2)` is odd, hence `h(2)=+/-1`. In fact `h(2)>0`: `G_m(T)>0` for every real `T>2`, so no real conjugate root of `h` exceeds two, and complex conjugate pairs contribute positive factors to `h(2)=prod(2-Y_i)`. Therefore

\[
\boxed{h(2)=1.}
\tag{SRL.9}

Thus

\[
2-Y=4\sin^2(\delta/2)=D^{-2}
\]

is an algebraic unit of norm one in the P1 trace field. This is not yet a contradiction, but it is a useful exact arithmetic constraint for the remaining proper-block cases.

---

## 9. Audit / regressions

- SRL uses the actual `0/1` negative-sign indicator `Q`; it is not merely a formal mod-two quotient.
- The local root `alpha` may be any 2-adic conjugate above a selected residue root. Only its residue and the exact P1 identity are used.
- The square root in (2.7) is unique because Frobenius squaring is an automorphism of every finite field of characteristic two.
- The exponent `(u-1)/2` works simultaneously for every residue order dividing `u` because its square exponent is `u-1`, congruent to `-1` modulo every such order.
- The maximal-degree exclusion is stated only for `r=1`; for `r>1`, SRL still determines the grouped parity pattern modulo `B`, but not the exact integer sign count in each residue class.
- The prime corollary requires `ord_p(2)=p-1`; no unproved Artin-type infinitude assertion is made.
- SRL does not close arbitrary P1. Proper selected residue blocks remain possible.

---

## 10. Next target

The remaining arithmetic problem has acquired an extra exact constraint:

1. `bar M=B^r`, with complete saturated residue blocks and no order one/three;
2. `B` divides the explicit sign-residue polynomial in SRL.2;
3. `h(2)=1`, so `D^{-2}=2-Y` is a norm-one algebraic unit;
4. modulo three, `M` divides
   \[
   (Z^{m-1}+1)(Z^{m+1}+1).
   \]

For `r=1`, every surviving factor has `deg M<=m-3`. The shortest next theorem is to combine SRL.2 with the restricted star-run/sign-change structure from the cyclic tree geometry, rather than treating `Q` as an arbitrary `0/1` polynomial.

For general `r`, reduce `Q` modulo `Z^u-1`; SRL prescribes its parity vector on every selected block. The quotient `P/M` has degree at most `m-1-r deg B`, so a large `B` leaves very little freedom to lift that parity pattern to an actual Littlewood sign word.

---

## 11. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Write the P1 Littlewood word as P=S_m-2Q, Q in {0,1}[Z].
For every selected mod-2 residue root xi of B, choose a 2-adic root alpha of M reducing
to its Teichmuller lift. Since P(alpha)=0,
    Q(alpha)=S_m(alpha)/2.
Using
    (alpha^m+1)^2=-4 alpha^(m-1)(alpha-1)^2,
define R=(alpha^m+1)/(2(alpha-1)). Then R^2=-alpha^(m-1) and
    Q(alpha)=R-1/(alpha-1).
Reducing mod2 gives
    Q(xi)=xi^((u-1)/2)+1/(xi+1).
Hence
    B | (Z+1)Q + Z^((u+1)/2)+Z^((u-1)/2)+1   mod2.

If r=1 and B=S_u, inverse of Z+1 mod S_u is
    A_u=1+Z^2+...+Z^(u-1).
Thus Q is exactly R_u=Z^((u-1)/2)+A_u or its coefficient complement.
Both choices give
    |P(-1)|=u-2.
But deg M=u-1=deg P forces P=+/-M. Since F_u(-1)=16 and M(-1) is odd,
    |M(-1)|=1.
Contradiction for u>=5. O3X handles u=3.
Therefore odd m>=5 never has deg M=m-1; in fact deg M<=m-3.
If m=p prime and ord_p(2)=p-1, Phi_p is the only nonzero mod-2 block, so P1 is
excluded completely.
Also universally h(2)=1, so D^-2=2-Y is a norm-one algebraic unit.
```
