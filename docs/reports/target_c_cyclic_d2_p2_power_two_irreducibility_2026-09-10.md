<!-- theorem-state: {"artifact_id":"ART-7FBEBB59CEC2","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic `d_H=2`, P2: power-of-two trace polynomial is 2-adically irreducible

**Date:** 2026-09-10  
**Repository branch:** `research/post-zf-currency-coupling-2026-09-09`  
**Run type:** exact arithmetic closure of an infinite P2 subsequence  
**Target:** P2 subphase of the cyclic `d_H=2` endpoint  
**Depends on:** P2A algebraic degree sieve; P2N power-of-two first Newton sieve  
**External literature:** only standard facts about valuations in finite extensions of `Q_2`; the proof below is direct and does not require higher-order Newton/Montes theory  
**Computation:** none used in the proof

## LEVEL I STATUS

`STILL OPEN`

P2N left one possible arithmetic escape when

\[
m=q-4=2^k:
\]

the trace polynomial

\[
H_m(X)=2T_m(X/2)+16X^2-48X+34
\]

might split into two degree-`m/2` factors.  That escape is impossible.

### Theorem P2I — power-of-two irreducibility

For every

\[
\boxed{m=2^k\ge4,}
\]

the polynomial

\[
\boxed{H_m(X)=2T_m(X/2)+16X^2-48X+34}
\tag{P2I.1}
\]

is irreducible over `Q_2`, hence irreducible over `Q`.

Consequently its physical factor has degree

\[
r_m=m.
\]

P2A then gives an immediate geometric consequence:

### Corollary P2I.1 — P2 exclusion on the power-of-two ladder

No sufficiently large cyclic P2 survivor can satisfy

\[
\boxed{q-4=2^k.}
\tag{P2I.2}
\]

Thus P2 is rigorously eliminated for the infinite shell-cardinality subsequence

\[
q=2^k+4.
\]

This is an actual subphase closure, not computational evidence.

---

## 1. Chebyshev trace notation and exact doubling identity

Put

\[
S_j(X):=2T_j(X/2).
\]

Then

\[
S_{2j}(X)=S_j(X)^2-2.
\tag{1.1}
\]

Write

\[
m=2n,
\qquad n=2^{k-1}.
\]

Using (1.1),

\[
\begin{aligned}
H_{2n}(X)
&=S_{2n}(X)+16X^2-48X+34\\
&=S_n(X)^2-2+16X^2-48X+34\\
&=\boxed{S_n(X)^2+16(X-1)(X-2).}
\end{aligned}
\tag{1.2}
\]

After the translation

\[
X=2+Y,
\]
put

\[
A_n(Y):=S_n(2+Y),
\qquad
F_m(Y):=H_m(2+Y).
\]

Then

\[
\boxed{F_m(Y)=A_n(Y)^2+16Y(Y+1).}
\tag{1.3}
\]

Translation preserves irreducibility, so it is enough to prove `F_m` irreducible over `Q_2`.

---

## 2. Two exact mod-eight congruences

P2N proved by the doubling recurrence that for every power of two `r>=2`,

\[
S_r(2+Y)
\equiv
2+4Y^{r/2}+Y^r
\pmod8.
\tag{2.1}
\]

Apply this first with `r=n`:

\[
\boxed{
A_n(Y)
=2+Y^n+4Y^{n/2}+8B(Y)
}
\tag{2.2}
\]

for some `B(Y) in Z[Y]`.

Apply P2N directly with `r=m=2n` to the shifted trace polynomial.  Equivalently square (2.2) in (1.3).  One obtains

\[
\boxed{
F_m(Y)
\equiv
4+4Y^n+Y^{2n}
\pmod8.
}
\tag{2.3}
\]

Thus:

- the constant coefficient has 2-adic valuation exactly `2`;
- the coefficient of `Y^n` has valuation exactly `2`;
- the leading coefficient is `1`;
- every other nonleading coefficient is divisible by `8`.

---

## 3. Every root has valuation exactly `1/n`

Let

\[
\alpha\in\overline{\mathbb Q}_2
\]

be any root of `F_m`, and normalize the 2-adic valuation by

\[
v(2)=1.
\]

We claim

\[
\boxed{v(\alpha)=1/n.}
\tag{3.1}
\]

First `v(alpha)>0`.  If `v(alpha)<0`, the monic leading term `alpha^{2n}` has strictly smaller valuation than every lower-degree term and cannot cancel.  If `v(alpha)=0`, (2.3) shows the leading term has valuation zero while every lower coefficient has positive valuation, again giving a unique lowest-valuation term.

Now put

\[
t:=v(\alpha)>0.
\]

From (2.3), the valuations of the three distinguished terms are

\[
2nt,
\qquad
2+nt,
\qquad
2.
\]

Every other term has valuation at least

\[
3+jt>3.
\]

If `t<1/n`, then

\[
2nt<2
\]

and the leading term is uniquely of smallest valuation.

If `t>1/n`, then the constant term has valuation `2`, while

\[
2nt>2,
\qquad
2+nt>3,
\]

so the constant term is uniquely smallest.

Both cases contradict the nonarchimedean cancellation rule for a zero sum. Therefore necessarily

\[
t=1/n.
\]

This proves (3.1) directly; no Newton-polygon theorem is required. `square`

---

## 4. The refined value `v(alpha^n+2)` has denominator `2n`

Since

\[
v(\alpha)=1/n>0,
\]
we have

\[
v(1+\alpha)=0.
\]

At a root of `F_m`, equation (1.3) gives

\[
A_n(\alpha)^2=-16\alpha(1+\alpha).
\]

Hence

\[
\boxed{
v(A_n(\alpha))
=2+\frac1{2n}.}
\tag{4.1}
\]

Now use the exact congruence (2.2):

\[
A_n(\alpha)-(2+\alpha^n)
=4\alpha^{n/2}+8B(\alpha).
\]

The first term on the right has valuation

\[
2+\frac12=\frac52,
\]

and the second has valuation at least `3`, because `B` has integral coefficients and `v(alpha)>0`.

For `n>=2`,

\[
2+\frac1{2n}<\frac52.
\]

Therefore the correction from `A_n(alpha)` to `2+alpha^n` has strictly larger valuation than `A_n(alpha)` itself.  The ultrametric inequality is then exact and gives

\[
\boxed{
v(\alpha^n+2)
=2+\frac1{2n}
=\frac{4n+1}{2n}.}
\tag{4.2}
\]

Since `4n+1` is odd and coprime to `n`, the fraction in (4.2) is in lowest terms and has denominator exactly `2n`.

This is the second 2-adic layer that P2N did not use.

---

## 5. A degree-`n` factor is impossible

Let

\[
K:=\mathbb Q_2(\alpha),
\qquad
d:=[K:\mathbb Q_2],
\]

and let `e` be the ramification index of `K/Q_2`.

The value group of `K` is

\[
\frac1e\mathbb Z.
\tag{5.1}
\]

Because

\[
v(\alpha)=1/n,
\]
we must have

\[
n\mid e.
\tag{5.2}
\]

Also

\[
e\mid d,
\qquad
d\le\deg F_m=2n.
\]

Thus the degree of the minimal polynomial of any root is a multiple of `n`; the only possibilities below the total degree are

\[
d=n
\quad\text{or}\quad
d=2n.
\tag{5.3}
\]

Suppose for contradiction that

\[
d=n.
\]

Then (5.2) forces

\[
e=n,
\]
so every element of `K` must have valuation in

\[
\frac1n\mathbb Z.
\]

But the element

\[
\alpha^n+2\in K
\]
has, by (4.2), valuation

\[
\frac{4n+1}{2n},
\]
whose reduced denominator is `2n`. This is not an element of `(1/n)Z`.

Contradiction.

Therefore every root has degree

\[
\boxed{d=2n=m.}
\]

Hence `F_m`, and therefore `H_m`, is irreducible over `Q_2`. This proves P2I. `square`

---

## 6. Insert the P2A geometry

P2A shows that a P2 survivor with

\[
m=L_A+L_B
\]
forces

\[
\max(L_A,L_B)\ge r_m+1,
\]
where `r_m` is the degree of the rational irreducible factor of `H_m` containing the physical root.

P2I gives

\[
r_m=m.
\]

Thus P2A would require

\[
\max(L_A,L_B)\ge m+1,
\]
which is impossible because

\[
L_A+L_B=m,
\qquad
L_A,L_B\ge0.
\]

Therefore no P2 survivor exists when `m=q-4` is a power of two. `square`

---

## 7. Relation to the first Newton sieve

P2N obtained a one-segment ordinary Newton polygon of slope

\[
-1/n.
\]
Its residual polynomial is inseparable over `F_2`, so that first polygon alone permits a split into two degree-`n` factors.

P2I resolves exactly that repeated residual root.  Instead of constructing the formal second-order Newton polygon, it computes the refined value

\[
v(\alpha^n+2)=2+1/(2n).
\]

A hypothetical degree-`n` field has value group `(1/n)Z`, so this single refined value already detects the missing ramification factor `2` and forces total ramification index at least `2n`.

Thus P2I is the elementary valuation-theoretic content of the second Newton/Montes step.

---

## 8. Regression audit

### First Newton polygon alone

Not overclaimed. Its denominator is only `n=m/2`, so P2N correctly retained the `n+n` split. P2I uses genuinely new second-level information.

### Root choice

The proof applies to **every** root of `F_m`, not merely the physical real root. Therefore irreducibility over `Q_2` follows directly.

### Valuation of `8B(alpha)`

Safe because `B in Z[Y]` and `v(alpha)>0`; each monomial has valuation at least zero before the factor `8`.

### Cancellation in `A_n(alpha)-(2+alpha^n)`

The correction has valuation at least `5/2`, strictly above `2+1/(2n)`. Hence no cancellation can change (4.2).

### Small case

The proof assumes `n>=2`, equivalently `m>=4`.  This contains the entire sufficiently-large power-of-two subsequence relevant to Target C.

### Level I

Still open.  This closes only the P2 subphase on the infinite arithmetic subsequence `q-4=2^k`; S2/PS remain, and P2 for general `m` remains open.

---

## 9. Next targets

The proof suggests two concrete continuations.

1. **Generalize the valuation refinement.**  Find broad classes of `m=2n` for which the first trace polynomial congruence forces `v(alpha)=1/n` and a second Chebyshev approximation produces a valuation with denominator `2n`. Any such class gives a new exact P2 exclusion.
2. **Use the same ramification mechanism on S/PS cells.**  Their closure has nonzero but explicit defect terms.  If those terms can be algebraized by adjoining the two cell square roots, the field-degree cost may still exceed the staircase closure degree.

The first route is arithmetic and finite. The second would attack the full two-cell branch rather than only P2.
