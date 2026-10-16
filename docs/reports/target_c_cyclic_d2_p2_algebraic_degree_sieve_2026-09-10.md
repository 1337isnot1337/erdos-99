<!-- theorem-state: {"artifact_id":"ART-92D02481E30D","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic `d_H=2`, P2: exact algebraic degree sieve

**Date:** 2026-09-10  
**Repository branch:** `research/post-zf-currency-coupling-2026-09-09`  
**Run type:** exact algebraic reduction / arithmetic endgame  
**Target:** P2 subphase of the cyclic `d_H=2` endpoint  
**Depends on:** SCE two-staircase closure; D2C two defect cells  
**External literature:** none used in the theorem below  
**Computation:** exact symbolic factorization of the trace polynomial through `m=60` is reported only as evidence for the final conjectural arithmetic lemma; it is not a proof dependency

## LEVEL I STATUS

`STILL OPEN`

In P2 both D2C cells are parallel:

\[
G_1=G_2=\Delta_2:=2\arcsin(1/D),
\qquad
W_1=W_2=0.
\]

Thus SCE has **zero error**, rather than merely `O(1/D)` error.  The resulting exact complex closure can be eliminated against the P2 angular equation and converted into a low-degree integer polynomial vanishing at the physical direction parameter.

This yields a sharp degree sieve.

Put

\[
\delta:=2\arcsin\frac1{2D},
\qquad
m:=q-4,
\qquad
z:=e^{i\delta},
\qquad
w:=e^{i\Delta_2}.
\]

Let

\[
a:=L_A,
\qquad
b:=L_B,
\qquad
a+b=m,
\]

and let the two staircase Littlewood polynomials be

\[
P_A(Z)=\sum_{j=0}^{a-1}\varepsilon^A_jZ^j,
\qquad
P_B(Z)=\sum_{j=0}^{b-1}\varepsilon^B_jZ^j,
\qquad
\varepsilon^X_j\in\{\pm1\},
\]

with the convention `P_X=0` when the corresponding length is zero.

### Theorem P2A — algebraic degree sieve

Every P2 survivor satisfies

\[
\boxed{
P_A(z)+z^a wP_B(z)=0,
}
\tag{P2A.1}
\]

\[
\boxed{
z^m w^2=-1,
}
\tag{P2A.2}
\]

and therefore

\[
\boxed{
P_A(z)^2+z^{a-b}P_B(z)^2=0.
}
\tag{P2A.3}
\]

After clearing a possible negative exponent, `z` is a root of the nonzero integer polynomial

\[
\boxed{
Q_{A,B}(Z)
:=Z^{(b-a)_+}P_A(Z)^2
 +Z^{(a-b)_+}P_B(Z)^2,
}
\tag{P2A.4}
\]

with

\[
\boxed{
\deg Q_{A,B}\le2\max(a,b)-2
}
\tag{P2A.5}
\]

when `a,b>0`.  If one staircase length is zero, the unsquared closure already gives a Littlewood polynomial of degree `m-1` vanishing at `z`.

Now put

\[
x:=z+z^{-1}=2\cos\delta
\]

and define the monic trace polynomial

\[
\boxed{
H_m(X)
:=2T_m(X/2)+16X^2-48X+34.
}
\tag{P2A.6}
\]

Then

\[
\boxed{H_m(x)=0.}
\tag{P2A.7}
\]

Let `h_m` be the irreducible factor of `H_m` over `Q` containing this physical root `x`, and put

\[
r_m:=\deg h_m.
\]

Since `x` is real while `z=e^{i\delta}` is nonreal and satisfies

\[
z^2-xz+1=0,
\]

we have the exact degree doubling

\[
\boxed{[\mathbb Q(z):\mathbb Q]=2r_m.}
\tag{P2A.8}
\]

Consequently, if `a,b>0`,

\[
\boxed{\max(a,b)\ge r_m+1.}
\tag{P2A.9}
\]

In particular:

\[
\boxed{r_m\ge m-1\quad\Longrightarrow\quad\text{P2 is impossible}.}
\tag{P2A.10}
\]

The implication also covers the zero-length staircase case, because then `P_X(z)=0` would give a polynomial of degree `m-1<2r_m`.

Thus the complete P2 geometry is reduced to one explicit arithmetic statement about the degree of the physical factor of `H_m`.

---

## 1. Exact zero-error SCE closure

SCE gives, after rotating by the A phase,

\[
P_A(z)+e^{i(a\delta+G_1)}P_B(z)=E.
\]

In P2,

\[
G_1=\Delta_2,
\qquad
W_1=W_2=0,
\]

so the transition error vector is exactly zero. Therefore

\[
P_A(z)+z^a wP_B(z)=0,
\]

which is P2A.1.

The P2 half-circle angle equation is

\[
(q-4)\delta+2\Delta_2=\pi.
\]

Since `m=q-4`, exponentiation gives

\[
z^mw^2=e^{i(m\delta+2\Delta_2)}=-1,
\]

which is P2A.2.

Squaring P2A.1 gives

\[
P_A(z)^2=z^{2a}w^2P_B(z)^2.
\]

Use

\[
w^2=-z^{-m}=-z^{-(a+b)}
\]

to obtain

\[
P_A(z)^2=-z^{a-b}P_B(z)^2.
\]

This proves P2A.3.

If `a>=b`, P2A.3 is already polynomial and equals

\[
P_A(z)^2+z^{a-b}P_B(z)^2=0.
\]

If `b>a`, multiply by `z^{b-a}`. This is exactly P2A.4.

For `a>b`, its two summands have degrees

\[
2a-2
\quad\text{and}\quad
(a-b)+(2b-2)=a+b-2=m-2,
\]

so the degree is at most `2a-2`. The symmetric argument handles `b>a`; if `a=b`, the degree is at most `2a-2`. Thus P2A.5 holds.

The polynomial is nonzero. If `a\ne b`, the summand belonging to the longer staircase has strictly larger degree and leading coefficient `1`. If `a=b`, its constant coefficient is

\[
(\varepsilon^A_0)^2+(\varepsilon^B_0)^2=2.
\]

---

## 2. Eliminate the P2 angle by a monic Chebyshev perturbation

The chord definitions give

\[
\sin(\Delta_2/2)=\frac1D
=2\sin(\delta/2).
\]

Hence

\[
\cos\Delta_2
=1-2\sin^2(\Delta_2/2)
=1-\frac2{D^2}.
\]

Also

\[
\cos\delta=1-\frac1{2D^2},
\]

so

\[
\boxed{\cos\Delta_2=4\cos\delta-3.}
\tag{2.1}
\]

With

\[
x=z+z^{-1}=2\cos\delta,
\]
we get

\[
w+w^{-1}=2\cos\Delta_2=4x-6.
\tag{2.2}
\]

From P2A.2,

\[
w^2=-z^{-m},
\qquad
w^{-2}=-z^m.
\]

Therefore

\[
(w+w^{-1})^2
=w^2+w^{-2}+2
=2-z^m-z^{-m}.
\]

Insert (2.2):

\[
z^m+z^{-m}+(4x-6)^2-2=0.
\tag{2.3}
\]

The standard trace identity is

\[
z^m+z^{-m}=2T_m(x/2).
\]

Thus

\[
2T_m(x/2)+16x^2-48x+34=0,
\]
which proves P2A.7.

For `m>=3`, `2T_m(X/2)` is a monic integer polynomial of degree `m`, so `H_m` is monic of degree `m`.

---

## 3. Reciprocal sum-of-squares form

The trace polynomial has an unexpectedly rigid reciprocal lift. Define

\[
R_m(Z):=Z^mH_m(Z+Z^{-1}).
\]

A direct expansion gives

\[
\boxed{
R_m(Z)
=(Z^m-1)^2
+Z^{m-2}(4Z^2-6Z+4)^2.
}
\tag{3.1}
\]

Equivalently,

\[
\begin{aligned}
R_m(Z)
={}&Z^{2m}+1
+16(Z^{m+2}+Z^{m-2})\\
&-48(Z^{m+1}+Z^{m-1})
+66Z^m.
\end{aligned}
\tag{3.2}
\]

The physical `z` is a unit-circle root of this explicit reciprocal polynomial.

For even `m`, (3.1) factors over the Gaussian rationals as

\[
R_m(Z)
=F_m^+(Z)F_m^-(Z),
\]

where

\[
\boxed{
F_m^\pm(Z)
=Z^m-1
\pm iZ^{m/2-1}(4Z^2-6Z+4).
}
\tag{3.3}
\]

This Gaussian factorization is exact and may be the most efficient route to the missing arithmetic lemma for even `m`.

---

## 4. Exact degree doubling

Let `h_m` be the irreducible `Q`-factor of `H_m` containing the physical real root `x`, with degree `r_m`.

Since

\[
x=2\cos\delta\in\mathbb R,
\]
all elements of `Q(x)` are real under the physical embedding.

But

\[
z=e^{i\delta}\notin\mathbb R
\]
for a genuine large shell, and `z` is a root of

\[
Z^2-xZ+1.
\]

Therefore `z` cannot belong to `Q(x)`. Hence

\[
[\mathbb Q(z):\mathbb Q(x)]=2,
\]
so

\[
[\mathbb Q(z):\mathbb Q]=2r_m.
\]

This proves P2A.8.

---

## 5. Degree sieve against staircase closure

Assume first that `a,b>0`. Since the nonzero integer polynomial `Q_{A,B}` vanishes at `z`, the minimal polynomial of `z` divides it. Thus

\[
2r_m
\le\deg Q_{A,B}
\le2\max(a,b)-2.
\]

Therefore

\[
\max(a,b)\ge r_m+1,
\]
which is P2A.9.

Now suppose

\[
r_m\ge m-1.
\]

If both staircase lengths are positive, then

\[
\max(a,b)\le m-1,
\]
contradicting P2A.9.

If, say, `a=0`, P2A.1 becomes

\[
wP_B(z)=0.
\]

Thus

\[
P_B(z)=0,
\]
where `P_B` has degree `m-1`. But the minimal polynomial of `z` has degree

\[
2r_m\ge2m-2>m-1
\]
for `m>1`, impossible. The case `b=0` is identical.

Hence `r_m>=m-1` excludes P2 completely. This proves P2A.10. `square`

---

## 6. Exact computational evidence for the arithmetic endpoint

Factoring `H_m` over `Q` exactly for every

\[
3\le m\le60
\]
produces the following uniform pattern:

1. if
   \[
   m\not\equiv3\pmod6,
   \]
   then `H_m` is irreducible of degree `m`;
2. if
   \[
   m\equiv3\pmod6,
   \]
   then
   \[
   H_m(X)=(X-1)J_m(X),
   \]
   where `J_m` is irreducible of degree `m-1`.

The linear factor is explained exactly:

\[
H_m(1)
=2T_m(1/2)+2
=2\cos(m\pi/3)+2,
\]
so `X-1` occurs precisely when `m=3 mod 6`.

The physical root satisfies

\[
x=2\cos\delta\to2,
\]
so it is not the root `x=1`.  Thus every checked `m<=60` has

\[
r_m\ge m-1,
\]
and P2A.10 rigorously excludes P2 for every corresponding `q=m+4` once the exact factorization has been independently reproduced.

This finite computation is evidence, not a proof of the eventual statement.

### Arithmetic target P2-I

Prove for every sufficiently large `m` that the physical factor of

\[
H_m(X)=2T_m(X/2)+16X^2-48X+34
\]
has degree at least `m-1`.

The observed stronger statement is:

\[
\boxed{
H_m\text{ is irreducible unless }m\equiv3\pmod6,
\text{ in which case }H_m/(X-1)\text{ is irreducible}.}
\tag{P2-I}
\]

P2-I would close the complete P2 subphase immediately.

For even `m`, the Gaussian factorization (3.3) gives an equivalent-looking target: prove the physical Gaussian factor `F_m^\pm` is irreducible of degree `m` over `Q(i)`.

No such irreducibility theorem is asserted here without proof.

---

## 7. Regression audit

### Square

The finite square `q=4` has `m=0` and lies outside the large-`m` statement.  It remains a binding P2 regression.

### SSR selected-support regression

SSR lies at `s_1=s_2=0`, not at the P2 endpoint `s_j=s_P(D)`.  SCE then has nonzero transition midpoint terms, so P2A.1 does not apply.  The exact regular-shell regression is therefore not falsely excluded.

### General Littlewood roots on the unit circle

No zero-free-arc or cyclotomic claim is used.  Such claims would be false in this generality. The only polynomial conclusion is the exact degree comparison P2A.9.

### Factorization data

The `m<=60` pattern is not promoted to a theorem. The proof endpoint is explicitly isolated as P2-I.

---

## 8. What this changes

P2 is no longer a two-staircase geometric closure problem. It is reduced to one explicit algebraic-degree question.

The chain is

```text
P2 parallel cells
  -> SCE transition error exactly zero
  -> low-degree integer closure polynomial Q_AB(z)=0
  -> explicit trace equation H_m(z+z^-1)=0
  -> deg_Q(z)=2 r_m
  -> max(L_A,L_B) >= r_m+1.
```

The empirically correct-looking bound `r_m>=m-1` is already stronger than necessary and would make the chain impossible because `L_A+L_B=m`.

This is a precise arithmetic theorem request, not a vague sign-code classification.
