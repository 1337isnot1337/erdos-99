> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_d2_p2_even_m_schinzel_closure_2026-09-10.md) · source SHA-256 `5238c3fa85b5cd388f780aa111dd756cd4052f9c8c0e6171f08d8d8963cd3b78`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-DF8FD976F468","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic `d_H=2`, P2: sufficiently large even `m` excluded by Schinzel + cyclic-isogeny rigidity

**Date:** 2026-09-10  
**Repository branch:** `research/post-zf-currency-coupling-2026-09-09`  
**Run type:** literature-grounded arithmetic subphase closure  
**Target:** P2 with even `m=q-4`  
**Depends on:** P2A algebraic degree sieve; GC Gaussian factorization and reciprocal-factor exclusion; PK primitive-character Kummer rigidity; CI cyclic-isogeny irreducibility  
**External theorem:** A. Schinzel, *Polynomials with Special Regard to Reducibility* (Cambridge, 2000), Theorem 74, in Chapter 2 “Lacunary polynomials over an arbitrary field”; finite-matrix consequence as spelled out by Sawin–Shusterman–Stoll, *Irreducibility of polynomials with a large gap*, proof of Theorem 1.2  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

The P2 arithmetic route had one remaining scope question: GC originally used Filaseta only conditionally because its printed theorem was over `Z/Q`, while our natural Gaussian factor

$$
F_n^+(Z)=Z^{2n}-1+iZ^{n-1}(4Z^2-6Z+4)
$$

lives over

$$
K=\mathbb Q(i).
$$

PK and CI removed the algebraic part of that issue directly over `K`. The remaining finite-matrix reduction is supplied by Schinzel's Theorem 74, whose chapter scope is explicitly **arbitrary field**. Sawin–Shusterman–Stoll spell out exactly the rank-`<=2` matrix consequence needed here and explicitly contrast the older Schinzel 1969 theorem as the version stated over `Q`.

This closes the sufficiently large even-`m` P2 branch.

### Theorem ES — even-`m` P2 closure

There is an integer

$$
M_0
$$

such that no cyclic P2 survivor exists with

$$
\boxed{m=q-4\ge M_0\quad\text{and}\quad m\text{ even}.}
\tag{ES.1}
$$

Equivalently, all sufficiently large P2 survivors, if any, must have odd shell cardinality `q`.

More precisely, writing

$$
m=2n,
$$

the Gaussian factor

$$
\boxed{
F_n^+(Z)=Z^{2n}-1+iZ^{n-1}(4Z^2-6Z+4)
}
\tag{ES.2}
$$

is irreducible over `Q(i)` for every sufficiently large `n`. Consequently

$$
\boxed{
H_{2n}(X)=2T_{2n}(X/2)+16X^2-48X+34
}
\tag{ES.3}
$$

is irreducible over `Q` for every sufficiently large `n`. P2A then excludes the corresponding P2 geometry.

---

## 1. Exact literature scope of the large-gap theorem

Schinzel's 2000 book divides its field scope explicitly. Chapter 2, containing the cited Theorem 74, is titled

> Lacunary polynomials over an arbitrary field.

The book introduction states that results valid only over finite fields, local fields, or the rational field are not included.

Sawin–Shusterman–Stoll prove their Theorem 1.2 by invoking Schinzel [Sch00, Theorem 74]. Their proof extracts the following finite-matrix consequence for a fixed bivariate Laurent polynomial `F` specialized along `(1,N)`:

1. for some `1<=r<=2`, there is an integer `r x 2` matrix `M` of rank `r`;
2. `(1,N)` is an integral linear combination of the rows of `M`;
3. all entries of `M` are bounded by a constant depending only on the fixed polynomial `F`;
4. factorization of the nonreciprocal part of the one-variable specialization is inherited from the corresponding rank-`r` monomial pullback.

They then add: “see also [Sch69, Theorem 2], where the result is stated over Q and explicit bounds are given.” That contrast is exactly the coefficient-field issue that had been left open in GC.

Our field

$$
K=\mathbb Q(i)
$$

has characteristic zero, so it lies in the arbitrary-field scope relevant here.

No extension of Filaseta's integer-coefficient theorem is used below.

---

## 2. Put the Gaussian P2 factor in Schinzel's specialization form

Define the fixed polynomial

$$
\boxed{
\mathcal F(X,Y)
=X^2Y^2+i(4X^2-6X+4)Y-1
\in K[X,Y].
}
\tag{2.1}
$$

GC proves `mathcal F` irreducible over `K`, and for every `n>=1`,

$$
\boxed{
\mathcal F(X,X^{n-1})=F_n^+(X).
}
\tag{2.2}
$$

Thus the specialization exponent vector is

$$
(1,N),
\qquad N=n-1.
$$

Schinzel 74 therefore supplies a bounded rank-`r` monomial matrix if the nonreciprocal part of `F_n^+` has a nontrivial factorization for arbitrarily large `n`.

We now eliminate both possible ranks.

---

## 3. Rank one is impossible for large `n`

Let

$$
M=(a,b)
$$

have rank one, and suppose

$$
(1,N)=\lambda(a,b)
$$

for an integer `lambda`.

The first coordinate gives

$$
1=\lambda a.
$$

Hence

$$
\lambda=\pm1,
\qquad
a=\pm1,
$$

and therefore

$$
b=\pm N.
$$

Schinzel's matrix entries are bounded by a constant `C_mathcalF` depending only on the fixed polynomial `mathcal F`. Thus

$$
N\le C_{\mathcal F}
$$

in the rank-one case.

Consequently for all sufficiently large `n`,

$$
\boxed{r\ne1.}
\tag{3.1}
$$

The only possible matrix has rank two.

---

## 4. CI eliminates every rank-two pullback

Let

$$
M\in\mathbb Z^{2\times2}
$$

be a full-rank matrix supplied by Schinzel, with

$$
(1,N)
$$

an integral row combination.

Because `(1,N)` is primitive, no integer `d>1` can divide every entry of `M`: if it did, every integral row combination would have both coordinates divisible by `d`.

Thus

$$
\gcd(\text{entries of }M)=1.
$$

Equivalently, the first Smith invariant of `M` is one.

CI proves exactly that every such rank-two monomial pullback of `mathcal F` is irreducible over `K=Q(i)`:

$$
\boxed{
\phi_M^*\mathcal F\text{ is irreducible in }K[Y_1^{\pm1},Y_2^{\pm1}].
}
\tag{4.1}
$$

The proof of CI is internal: Smith normal form reduces the pullback to one cyclic Kummer cover, and PK proves every primitive character on the Gaussian curve is Kummer-primitive.

Therefore the rank-two matrix supplied by Schinzel cannot account for any nontrivial factorization of the nonreciprocal part of `F_n^+`.

Together with Section 3, Schinzel's finite-matrix theorem gives:

### Corollary ES.1

For every sufficiently large `n`, the nonreciprocal part of

$$
F_n^+
$$

is irreducible over `Q(i)`.

---

## 5. GC-R upgrades nonreciprocal-part irreducibility to full irreducibility

GC-R proves for every `n>=2` that

$$
\boxed{F_n^+\text{ has no nonconstant reciprocal factor over }Q(i).}
\tag{5.1}
$$

Hence the reciprocal part is a unit. The nonreciprocal part is the whole polynomial up to a Gaussian constant and monomial unit.

Corollary ES.1 therefore gives

$$
\boxed{
F_n^+\text{ is irreducible over }Q(i)
\quad\text{for all sufficiently large }n.
}
\tag{5.2}
$$

Complex conjugation gives the same conclusion for

$$
F_n^-.
$$

GC-R also proves

$$
\gcd(F_n^+,F_n^-)=1.
\tag{5.3}
$$

---

## 6. The trace polynomial `H_{2n}` is then irreducible over `Q`

P2A gives the reciprocal lift

$$
\boxed{
R_{2n}(Z)
:=Z^{2n}H_{2n}(Z+Z^{-1})
=F_n^+(Z)F_n^-(Z).
}
\tag{6.1}
$$

Suppose for contradiction that

$$
H_{2n}=AB
$$

with nonconstant

$$
A,B\in\mathbb Q[X].
$$

Let

$$
a=\deg A.
$$

Then

$$
\widetilde A(Z):=Z^aA(Z+Z^{-1})
$$

is a nonconstant reciprocal polynomial in `Q[Z]` dividing `R_{2n}`.

Over `Q(i)`, equations (5.2)-(5.3) say that the complete irreducible factorization of `R_{2n}` has exactly the two coprime factors

$$
F_n^+,
\qquad F_n^-.
$$

Therefore a nonconstant proper factor is, up to a unit, either `F_n^+` or `F_n^-`.

But `\widetilde A` is reciprocal, whereas GC-R says neither `F_n^+` nor `F_n^-` has a nonconstant reciprocal factor; in particular neither is itself reciprocal up to a unit.

Thus `\widetilde A` cannot be a proper factor of `R_{2n}`. The only reciprocal products of the two irreducible factors are a unit and their full product.

Hence `A` is a unit or `A=H_{2n}` up to a rational unit, contradiction to a proper factorization.

Therefore

$$
\boxed{
H_{2n}\text{ is irreducible over }\mathbb Q
\quad\text{for all sufficiently large }n.
}
\tag{6.2}

---

## 7. Insert the P2A degree sieve

For P2 with

\[
m=q-4=2n,
$$

P2A lets `r_m` be the degree of the irreducible factor of `H_m` containing the physical root

$$
x=2\cos\delta.
$$

Equation (6.2) gives

$$
\boxed{r_m=m.}
\tag{7.1}
$$

P2A proves that a P2 staircase decomposition with positive lengths `a,b` and

$$
a+b=m
$$

would require

$$
\max(a,b)\ge r_m+1=m+1,
$$

impossible.

If one staircase length is zero, P2A separately gives a degree-`m-1` Littlewood polynomial vanishing at `z=e^{i\delta}`, while the minimal polynomial of `z` has degree

$$
2r_m=2m,
$$

again impossible.

Thus no sufficiently large even-`m` P2 survivor exists. This proves ES. `square`

---

## 8. Scope and regressions

### This does not close all P2

The theorem closes

$$
m=q-4\text{ even},
$$

equivalently even `q`.

Odd-`m` P2 remains open. The Gaussian factorization `R_{2n}=F_n^+F_n^-` used here is tied to even `m`.

### P2I power-of-two theorem

P2I remains useful as an unconditional local arithmetic proof on the subsequence `m=2^k`. ES strictly extends the excluded even-`m` range asymptotically but uses Schinzel's large-gap theorem.

### Filaseta coefficient-field issue

No longer relevant to this closure. We do not assert that Filaseta's printed `Z/Q` proof extends to `Z[i]/Q(i)`. The direct PK/CI pullback theorem plus Schinzel's arbitrary-field finite-matrix reduction replaces that bridge.

### Standard reciprocal versus conjugate reciprocal

GC-R uses ordinary polynomial reciprocity over `Q(i)`, the same notion needed in the Schinzel nonreciprocal-part reduction. Complex conjugation is used only to pass irreducibility from `F_n^+` to `F_n^-`.

### Rank-two Smith condition

No hidden saturation assumption is used. The primitive vector `(1,N)` lying in the integral row lattice immediately forces gcd of all entries of `M` to be one, hence first Smith invariant one, exactly CI's hypothesis.

### Characteristic

The application field is `Q(i)`, characteristic zero. Any positive-characteristic qualifications in general arbitrary-field statements are irrelevant here.

### Level I

Still open. P2/odd-`m`, PS, S2, `d_H=1`, and the exact Reinhardt `d_H=0` dense-interior branch remain.

---

## 9. Literature audit trail

Primary source:

- A. Schinzel, *Polynomials with Special Regard to Reducibility*, Cambridge University Press, 2000, Theorem 74 in Chapter 2, **“Lacunary polynomials over an arbitrary field.”**
- Cambridge's published introduction states that the book omits results valid only over the rational field, finite fields, or local fields.

Operational restatement used here:

- W. Sawin, M. Shusterman, M. Stoll, *Irreducibility of polynomials with a large gap*, proof of Theorem 1.2. They derive the bounded rank-`<=2` integer-matrix reduction from Schinzel Theorem 74 and explicitly say of Schinzel 1969 Theorem 2: “where the result is stated over Q and explicit bounds are given.”

The application above uses only that finite-matrix reduction. All pullback irreducibility over the actual coefficient field `Q(i)` is proved internally in PK/CI.

---

## 10. What this changes

Before ES, the rigorous infinite P2 exclusion was only the power-of-two subsequence

$$
m=2^k.
$$

After ES:

$$
\boxed{
\text{every sufficiently large even }m=q-4\text{ is excluded.}
}
$$

Thus any large P2 counterexample must lie in the **odd-`m` arithmetic branch**.

The highest-value P2 continuation is now to build the odd-`m` analogue of the Gaussian factorization/curve and repeat the PK/CI/Schinzel mechanism. The full D2 continuation remains the PS/S2 two-cell closure.

---

## 11. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

For m=2n, P2A gives R_2n=F_n^+ F_n^- with
  F_n^+(Z)=Z^(2n)-1+i Z^(n-1)(4Z^2-6Z+4).
Write
  mathcalF(X,Y)=X^2Y^2+i(4X^2-6X+4)Y-1,
so F_n^+(X)=mathcalF(X,X^(n-1)).

Schinzel 2000 Theorem 74 lies in Chapter 2, "Lacunary polynomials over an arbitrary
field". SSS's proof of Theorem 1.2 spells out the needed consequence: any large-gap
factorization is controlled by a bounded integer matrix M of rank r<=2 whose row lattice
contains the primitive specialization vector (1,N).

For large N, r=1 is impossible because then M=(+/-1,+/-N), contradicting boundedness.
For r=2, the primitive row-lattice vector forces gcd(entries M)=1. CI proves every such
monomial pullback of mathcalF is irreducible over Q(i), using PK + Smith + Capelli.
Thus the nonreciprocal part of F_n^+ is eventually irreducible. GC-R says F_n^+ has no
reciprocal factor, so F_n^+ itself is eventually irreducible over Q(i).

Since R_2n=F_n^+F_n^- with two coprime irreducible conjugate nonreciprocal factors, any
proper Q-factor of H_2n would lift to a proper reciprocal factor of R_2n, impossible.
Hence H_2n is irreducible over Q for all sufficiently large n.
P2A then gives r_m=m and contradicts a+b=m.

Conclusion: no sufficiently large P2 survivor with even m=q-4 (equiv even q).
Remaining P2 branch: odd m. Also PS/S2, d_H=1, d_H=0 remain.
```
