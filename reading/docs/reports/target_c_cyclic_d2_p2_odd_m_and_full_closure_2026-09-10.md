> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_d2_p2_odd_m_and_full_closure_2026-09-10.md) · source SHA-256 `7f2cfa4b69368f03436fa4fa91da7eca888f7344dab3d1309efda26f2e984913`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-1349EAD9D1A8","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic `d_H=2`, P2: odd-`m` square-lift closure and complete sufficiently-large P2 exclusion

**Date:** 2026-09-10  
**Repository branch:** `research/post-zf-currency-coupling-2026-09-09`  
**Run type:** exact arithmetic subphase closure  
**Target:** odd `m=q-4`, then full P2  
**Depends on:** P2A; Schinzel Theorem 74 arbitrary-field finite-matrix reduction; OK square-cover Kummer/cyclic-isogeny theorem; ES even-`m` closure  
**External theorem:** same Schinzel 74 input audited in ES  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

ES excludes P2 for all sufficiently large even

$$
m=q-4.
$$

For odd `m`, the reciprocal lift does not factor over `Q(i)[Z]` using an integral half-power of `Z`. After the harmless substitution

$$
Z=T^2,
$$

it does. The resulting factors are specializations of the fixed square-cover curve `mathcal G`, and OK proves all primitive rank-two monomial pullbacks of that curve irreducible.

This closes the remaining parity and therefore the entire sufficiently-large P2 subphase.

### Theorem OS — odd-`m` P2 closure

For every sufficiently large odd integer

$$
m=q-4,
$$

the trace polynomial

$$
\boxed{
H_m(X)=2T_m(X/2)+16X^2-48X+34
}
\tag{OS.1}
$$

is irreducible over `Q`.

Consequently no cyclic P2 survivor exists for sufficiently large odd `m`.

Combining with ES gives:

### Corollary P2X — complete sufficiently-large P2 exclusion

There is an integer `M_0` such that for every

$$
\boxed{m=q-4\ge M_0,}
$$

there is **no** cyclic `d_H=2` P2 survivor.

Equivalently, the branch

$$
(r_\parallel,a_{short})=(2,0)
$$

is eliminated completely in the asymptotic Target C regime.

The surviving `d_H=2` branches are only

$$
\boxed{PS=(1,1),\qquad S2=(0,2).}
\tag{P2X.1}
$$

---

## 1. Odd reciprocal lift after `Z=T^2`

P2A gives for every `m`

$$
R_m(Z)
:=Z^mH_m(Z+Z^{-1})
=(Z^m-1)^2+Z^{m-2}A(Z)^2,
\tag{1.1}
$$

where

$$
A(Z)=4Z^2-6Z+4.
$$

Assume now

$$
m\ge3
$$

is odd. Substitute

$$
Z=T^2.
$$

Then

$$
\begin{aligned}
R_m(T^2)
&=(T^{2m}-1)^2+T^{2m-4}A(T^2)^2\\
&=G_m^+(T)G_m^-(T),
\end{aligned}
\tag{1.2}
$$

with

$$
\boxed{
G_m^\pm(T)
:=T^{2m}-1\pm iT^{m-2}A(T^2).
}
\tag{1.3}
$$

Each factor has degree exactly

$$
2m.
$$

---

## 2. `G_m^+` is a large-gap specialization of the fixed square-cover curve

OK defines

$$
\boxed{
\mathcal G(X,Y)
=X^4Y^2+iA(X^2)Y-1.
}
\tag{2.1}
$$

Put

$$
N:=m-2.
$$

Then

$$
\boxed{
\mathcal G(T,T^N)
=T^{4+2N}+iA(T^2)T^N-1
=G_m^+(T),
}
\tag{2.2}
$$

because

$$
4+2N=4+2m-4=2m.
$$

Thus `G_m^+` is exactly the one-parameter Schinzel specialization of the **fixed** polynomial `mathcal G` along the primitive exponent vector

$$
(1,N).
$$

OK proves `mathcal G` geometrically irreducible over

$$
K=\mathbb Q(i)
$$

and, more strongly, proves every full-rank monomial pullback whose exponent matrix has first Smith invariant one is irreducible over `K`.

---

## 3. Schinzel's rank-one/rank-two alternatives both collapse

Apply the arbitrary-field finite-matrix theorem from ES to the fixed polynomial `mathcal G` and the specialization

$$
\mathcal G(T,T^N).
$$

If a nontrivial nonreciprocal factorization persists for arbitrarily large `N`, Schinzel supplies a bounded integer matrix of rank

$$
r\le2
$$

whose row lattice contains

$$
(1,N).
$$

### Rank one

Exactly as in ES, a rank-one row `(a,b)` satisfying

$$
(1,N)=\lambda(a,b),
\qquad\lambda\in\mathbb Z,
$$

must have

$$
\lambda=\pm1,
\quad a=\pm1,
\quad b=\pm N.
$$

This contradicts the fixed Schinzel entry bound for sufficiently large `N`.

### Rank two

The primitive row-lattice vector `(1,N)` forces

$$
\gcd(\text{entries of }M)=1.
$$

OK-CI proves every such rank-two monomial pullback of `mathcal G` irreducible over `Q(i)`.

Therefore no rank-two factorization source remains.

Hence the nonreciprocal part of

$$
G_m^+
$$

is irreducible for every sufficiently large odd `m`.

---

## 4. `G_m^+` has no reciprocal factor

The reciprocal calculation is exact and parallel to GC-R.

Since

$$
T^4A(T^{-2})=A(T^2),
$$

we have

$$
\begin{aligned}
T^{2m}G_m^+(T^{-1})
&=1-T^{2m}+iT^{m+2}A(T^{-2})\\
&=1-T^{2m}+iT^{m-2}A(T^2)\\
&=-G_m^-(T).
\end{aligned}
\tag{4.1}

Thus the reciprocal of `G_m^+` is `-G_m^-`.

Any common factor of `G_m^+` and `G_m^-` divides both

\[
T^{2m}-1
$$

and

$$
T^{m-2}A(T^2).
$$

The root `T=0` does not divide `T^{2m}-1`. If a root of unity `T` were a zero of `A(T^2)`, then

$$
\rho:=T^2
$$

would be a root of unity satisfying

$$
2\rho^2-3\rho+2=0,
$$

hence

$$
\rho+\rho^{-1}=\frac32.
$$

But a root of unity and its inverse are algebraic integers, so their sum is an algebraic integer; the rational number `3/2` is not an integer and therefore not a rational algebraic integer. Contradiction.

Hence

$$
\boxed{\gcd(G_m^+,G_m^-)=1.}
\tag{4.2}
$$

If `G_m^+` had a nonconstant reciprocal factor, that factor would also divide its reciprocal `-G_m^-`, contradicting (4.2).

Thus `G_m^+` has no nonconstant reciprocal factor. Schinzel's nonreciprocal-part conclusion from Section 3 upgrades to

$$
\boxed{
G_m^+\text{ irreducible over }Q(i)
\quad\text{for all sufficiently large odd }m.
}
\tag{4.3}
$$

By conjugation the same holds for `G_m^-`, and (4.2) keeps the two factors coprime.

---

## 5. Degree separation forces `H_m` irreducible

Suppose for contradiction that an odd-degree

$$
H_m\in\mathbb Q[X],
\qquad\deg H_m=m,
$$

is reducible.

Choose a nonconstant irreducible factor

$$
h(X)\in\mathbb Q[X]
$$

of minimal degree

$$
r.
$$

Because `m` is odd and the complementary factor is nonconstant,

$$
\boxed{r\le\frac{m-1}{2}.}
\tag{5.1}
$$

Form its reciprocal trace lift

$$
U(Z):=Z^rh(Z+Z^{-1}).
\tag{5.2}
$$

This is a nonconstant polynomial of degree

$$
2r
$$

which divides

$$
R_m(Z)=Z^mH_m(Z+Z^{-1}).
$$

Substitute `Z=T^2`. Then

$$
U(T^2)
$$

is a nonconstant polynomial dividing

$$
R_m(T^2)=G_m^+(T)G_m^-(T),
$$

and

$$
\deg U(T^2)=4r.
$$

By (5.1),

$$
\boxed{
4r\le2m-2<2m.
}
\tag{5.3}
$$

But Sections 3-4 give the complete factorization of `R_m(T^2)` over `Q(i)` into two coprime irreducible factors, each of degree exactly

$$
2m.
$$

Every nonconstant divisor therefore has degree at least `2m`, contradicting (5.3).

Hence

$$
\boxed{H_m\text{ is irreducible over }Q}
$$

for every sufficiently large odd `m`. This proves OS. `square`

---

## 6. P2A now excludes the odd P2 geometry

P2A lets `r_m` denote the degree of the irreducible factor of `H_m` containing the physical root

$$
x=2\cos\delta.
$$

OS gives

$$
\boxed{r_m=m}
$$

for all sufficiently large odd `m`.

P2A then requires, for positive staircase lengths `a,b` with `a+b=m`,

$$
\max(a,b)\ge r_m+1=m+1,
$$

impossible.

The zero-length staircase case is also impossible by P2A's separate minimal-polynomial degree comparison.

Therefore no sufficiently large odd-`m` P2 survivor exists.

Combine with ES, which already gives the even case. This proves P2X. `square`

---

## 7. Regression audit

### Why substitute `Z=T^2` only in the odd case?

For even `m`, GC already factors `R_m(Z)` directly over `Q(i)`. For odd `m`, the exponent `(m-2)/2` is half-integral, so `Z=T^2` is the natural integral cover.

### Does the square cover introduce new factorization?

OK proves it does not: `mathcal G` is geometrically irreducible and every primitive rank-two monomial pullback remains irreducible.

### Does `U(T^2)` have to be irreducible?

No. The degree argument does not require it. Any nonconstant divisor of a product of the two coprime irreducibles `G_m^+,G_m^-` must contain at least one of them and therefore has degree at least `2m`. Since `deg U(T^2)<2m`, contradiction.

### Could a proper factor of `H_m` have degree greater than `m/2` only?

No. In any nontrivial factorization of an odd-degree polynomial, one of the factors has degree at most `(m-1)/2`; choose an irreducible factor inside the smaller side.

### Reciprocal factors of `G_m^+`

Excluded explicitly by the gcd with `G_m^-`, exactly as in GC-R.

### Small `m`

No finite threshold is claimed explicitly because Schinzel's bound is not optimized here. Target C needs only the sufficiently-large regime.

### Level I

Still open. Eliminating P2 removes one full `d_H=2` defect branch, but PS and S2 remain. The `d_H=1` tree and `d_H=0` exact Reinhardt/dense-interior branches also remain.

---

## 8. What this changes

Before this report, P2 was reduced to arithmetic and rigorously excluded only on selected infinite subsequences, then all sufficiently large even `m` by ES.

Now:

$$
\boxed{
P2=(r_\parallel,a_{short})=(2,0)
\text{ is impossible for every sufficiently large cyclic survivor.}
}
$$

Thus a large `d_H=2` counterexample must contain at least one **genuine short antipodal difference-body vertex pair**:

$$
\boxed{a_{short}\ge1.}
\tag{8.1}
$$

Equivalently at least one of the two D2C defect parameters is strict interior:

$$
0<s_j<s_P(D),
$$

so at least one completion chord has

$$
\sqrt{D^2-1}<L_j<D.
$$

The complete `d_H=2` frontier is now PS/S2, where the SCE error is genuinely nonzero and carries geometric information. The next attack should use that nonzero defect rather than continue P2 arithmetic.

---

## 9. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

For odd m, substitute Z=T^2 in
  R_m(Z)=Z^m H_m(Z+Z^-1)=(Z^m-1)^2+Z^(m-2)A(Z)^2.
Then
  R_m(T^2)=G_m^+(T)G_m^-(T),
  G_m^±=T^(2m)-1 ± i T^(m-2)A(T^2).
Define fixed
  mathcalG(X,Y)=X^4Y^2+iA(X^2)Y-1.
Then G_m^+(T)=mathcalG(T,T^(m-2)).

OK proves every primitive rank-two pullback of mathcalG irreducible over Q(i).
Schinzel 74 on the primitive vector (1,m-2): rank1 impossible for large m; rank2
irreducible by OK-CI. Reciprocal(G+)= -G-, and gcd(G+,G-)=1, so G± are eventually
irreducible, each degree 2m.

If odd-degree H_m were reducible, choose a factor h of degree r<=(m-1)/2. Its trace
lift U(Z)=Z^r h(Z+Z^-1) divides R_m; hence U(T^2) divides G+G- but has degree
4r<=2m-2. A nonconstant divisor of two coprime degree-2m irreducibles has degree at
least 2m. Contradiction. Thus H_m irreducible for all sufficiently large odd m.
P2A excludes odd P2. ES excludes even P2.

P2 is therefore completely eliminated for sufficiently large D. Remaining d_H=2:
PS and S2, so every survivor has at least one genuine short antipodal defect cell.
```
