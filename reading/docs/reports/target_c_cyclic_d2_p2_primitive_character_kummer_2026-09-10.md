> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_d2_p2_primitive_character_kummer_2026-09-10.md) · source SHA-256 `4ffcaae702d6a484e6ac02af63b0136d36deee127125b06480bae459ab3d7bbb`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-06C2A6E14EA2","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic `d_H=2`, P2: primitive-character Kummer rigidity on the Gaussian curve

**Date:** 2026-09-10  
**Repository branch:** `research/post-zf-currency-coupling-2026-09-09`  
**Run type:** exact function-field/Kummer theorem  
**Target:** arithmetic closure of the P2 Gaussian lacunary route  
**Depends on:** GC parameterization of the Gaussian base curve  
**External literature:** only Capelli's standard binomial criterion for the corollary; the nonpower theorem is proved directly  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

GC reduces the even-`m` P2 arithmetic problem to the fixed Gaussian curve

$$
\mathcal F(X,Y)=X^2Y^2+i(4X^2-6X+4)Y-1=0
$$
over
$$
K:=\mathbb Q(i).
$$

The missing lacunary step eventually asks whether finite monomial pullbacks of this curve can split. The basic obstruction is now completely explicit: **no primitive torus character becomes a proper power in the function field of the curve.**

### Theorem PK — primitive-character Kummer rigidity

Let

$$
C/K:\quad \mathcal F(X,Y)=0,
$$

and let

$$
K(C)
$$

be its function field. For every primitive integer pair

$$
(r,s)\in\mathbb Z^2,
\qquad \gcd(r,s)=1,
$$

put

$$
\chi_{r,s}:=X^rY^s\in K(C)^\times.
$$

Then for every prime `p`,

$$
\boxed{\chi_{r,s}\notin K(C)^p.}
\tag{PK.1}
$$

In particular `chi_{r,s}` is never a square. Consequently, for every integer `k>=1`,

$$
\boxed{T^k-\chi_{r,s}\text{ is irreducible over }K(C).}
\tag{PK.2}
$$

The exceptional Capelli obstruction when `4|k` cannot occur either.

This theorem is uniform in the primitive character `(r,s)`; it is much stronger than checking the particular `+t/-t` characters in GC one at a time.

---

## 1. Rational parameterization of the curve

GC introduced

$$
S:=\sqrt{X^2-X+1},
\qquad
u:=S-(X-1),
\qquad
v:=S+(X-1).
$$

To avoid collision with later valuation notation, rename GC's `u` as `u` here. Thus

$$
u=S-(X-1),
\qquad
v=S+(X-1).
$$

GC proves

$$
uv=X,
\qquad
v=\frac{u-2}{1-2u},
$$

so

$$
K(C)=K(u).
\tag{1.1}
$$

For the branch corresponding to `mathcal F(X,Y)=0`, the `t=0` root formula in GC gives

$$
\boxed{
X=u\,v
=\frac{u(u-2)}{1-2u},
\qquad
Y=-iu^{-2}.
}
\tag{1.2}
$$

The conjugate parameterization `Y=-iv^{-2}` is obtained by the involution interchanging `u,v`; either one gives the same function field and the same conclusion.

---

## 2. Four decisive valuations

Work in the rational function field

$$
K(u)=\mathbb Q(i)(u).
$$

The only places needed are

$$
u=0,
\qquad
u=2,
\qquad
u=\frac12,
\qquad
\nu=\infty.
$$

From (1.2):

$$
\begin{array}{c|rrrr}
 & u=0 & u=2 & u=1/2 & u=\infty\\ \hline
\operatorname{ord}(X) & 1 & 1 & -1 & -1\\
\operatorname{ord}(Y) & -2 & 0 & 0 & 2
\end{array}
\tag{2.1}
$$

Therefore for

$$
\chi_{r,s}=X^rY^s
$$
we have

$$
\boxed{
\begin{array}{c|rrrr}
 & 0 & 2 & 1/2 & \infty\\ \hline
\operatorname{ord}(\chi_{r,s})
 & r-2s & r & -r & -r+2s.
\end{array}}
\tag{2.2}
$$

These four integers already rule out every odd prime power.

---

## 3. No odd prime power

Suppose for some odd prime `p` that

$$
\chi_{r,s}=f^p
$$

in `K(C)`. Every discrete valuation of a `p`th power is divisible by `p`. In particular (2.2) gives

$$
p\mid r,
\qquad
p\mid(r-2s).
$$

Hence

$$
p\mid2s.
$$

Since `p` is odd,

$$
p\mid s.
$$

Thus `p` divides both `r` and `s`, contradicting

$$
\gcd(r,s)=1.
$$

Therefore

$$
\boxed{
\chi_{r,s}\notin K(C)^p
\quad\text{for every odd prime }p.
}
\tag{3.1}
$$

---

## 4. The square case and the Gaussian constant obstruction

Suppose

$$
\chi_{r,s}=f^2.
$$

The valuation at `u=2` gives

$$
r\equiv0\pmod2.
$$

Because `(r,s)` is primitive, `s` must then be odd.

Using `Y=-iu^{-2}`,

$$
\begin{aligned}
\chi_{r,s}
&=X^r(-i)^s u^{-2s}\\
&=(-i)^s\left(X^{r/2}u^{-s}\right)^2.
\end{aligned}
\tag{4.1}
$$

Write

$$
s=2j+1.
$$

Then

$$
(-i)^s
=(-i)\left((-i)^j\right)^2.
$$

Thus `chi_{r,s}` could be a square in `K(u)` only if

$$
-i
$$

were a square in `K(u)`.

It is not. The constant field `K=Q(i)` is algebraically closed in the purely transcendental extension `K(u)`: any element of `K(u)` algebraic over `K` already lies in `K`. Thus a square root of `-i` in `K(u)` would give one in `K`.

If

$$
(a+bi)^2=-i,
\qquad a,b\in\mathbb Q,
$$

then

$$
a^2-b^2=0,
\qquad
2ab=-1.
$$

The first equation gives `b=±a`; the second then forces

$$
a^2=\frac12
$$

up to sign, impossible for rational `a`.

Hence

$$
\boxed{-i\notin K^2,}
\tag{4.2}
$$

and therefore

$$
\boxed{
\chi_{r,s}\notin K(C)^2.
}
\tag{4.3}
$$

Together with Section 3 this proves PK.1.

---

## 5. Capelli gives every cyclic Kummer cover irreducible

Use the standard binomial form of Capelli's criterion.

For a field `L` and `a in L^×`, the binomial

$$
T^k-a
$$

is irreducible over `L` if

1. `a` is not a `p`th power in `L` for every prime `p|k`; and
2. if `4|k`, then `a` is not of the exceptional form
   $$
   -4b^4.
   $$

Take

$$
L=K(C),
\qquad
a=\chi_{r,s}.
$$

PK.1 supplies condition 1 for every prime divisor of `k`.

For condition 2, if

$$
\chi_{r,s}=-4b^4,
$$

then, because `i in K`,

$$
\chi_{r,s}=(2ib^2)^2,
$$

contradicting the nonsquare result (4.3).

Therefore

$$
T^k-\chi_{r,s}
$$

is irreducible for every `k>=1`. This proves PK.2. `square`

---

## 6. Geometric interpretation

The coordinate characters of the two-dimensional torus are

$$
X^rY^s,
\qquad(r,s)\in\mathbb Z^2.
$$

Primitive characters are exactly those with `gcd(r,s)=1`. PK says that restricting any primitive torus character to the Gaussian P2 curve never turns it into a nontrivial power in the curve function field.

Equivalently, every cyclic Kummer cover obtained by adjoining a `k`th root of a primitive character stays connected/irreducible over `Q(i)`.

This is the exact property needed after a Smith-normal-form reduction of a finite monomial torus isogeny whose cokernel is cyclic.

---

## 7. Regression audit

### Negative exponents

Allowed. `X,Y` are nonzero rational functions in `K(C)`, so `X^rY^s` is defined for all integers `r,s`. The valuation argument is symmetric under sign changes.

### `r=0` or `s=0`

If `(r,s)` is primitive and `r=0`, then `s=±1`; the square obstruction still applies directly to `Y^{±1}`. If `s=0`, then `r=±1`, and the valuation at `u=2` immediately prevents every proper power.

### Odd prime dividing two

Explicitly excluded. The odd-prime step uses `p|2s => p|s`; `p=2` is handled separately by the nonsquare constant class.

### Could `-i` become a square in the rational function field?

No. Any putative square root is algebraic over the constant field and therefore constant.

### Capelli `-4` exception

Not omitted. Over `Q(i)` it is automatically a square, so PK's square obstruction excludes it.

### Conjugate branch

Interchanging `u` and `v` gives the other root of `mathcal F` as a quadratic in `Y`; the four-place divisor pattern is permuted, so the theorem is unchanged.

---

## 8. What this changes

GC individually checked a large family of special characters arising from Filaseta's `N=kell±t` substitutions. PK proves a uniform statement instead:

$$
\boxed{
\text{every primitive character of }(G_m)^2
\text{ is Kummer-primitive on }C.
}
$$

The next algebraic theorem is now finite and lattice-theoretic:

> if a rank-two monomial substitution has cyclic cokernel, reduce it by Smith normal form to adjoining a `k`th root of one primitive character, then invoke PK.

Schinzel's rank-two matrices in the large-gap theorem contain the primitive specialization vector in their row lattice, which forces first Smith invariant one. Thus PK is positioned to remove the remaining rank-two pullback reducibility obstruction without relying on a naive Gaussian extension of Filaseta's integer-square argument.

---

## 9. Promotion recommendation

**Hold as report pending independent audit.**

The proof is self-contained downstream of GC's exact rational parameterization. It does not assume any extension of Filaseta or Schinzel to `Q(i)`.

---

## 10. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

For C: mathcalF(X,Y)=0 over K=Q(i), GC gives K(C)=K(u) with
  X=u(u-2)/(1-2u),  Y=-i u^-2.
For primitive (r,s), chi=X^rY^s has valuations at u=0,2,1/2,infinity:
  r-2s, r, -r, -r+2s.
If chi is a pth power for odd p, then p|r and p|(r-2s), hence p|s,
contradicting gcd(r,s)=1.
If chi is a square, r is even, hence s is odd, and
  chi=(-i)^s (X^(r/2)u^-s)^2.
Its square class is therefore -i, which is nonsquare in Q(i) and remains nonsquare
in Q(i)(u). Thus no primitive character is a pth power for any prime p.
The Capelli -4 fourth-power exception is also a square over Q(i), so impossible.
Hence T^k-X^rY^s is irreducible in K(C)[T] for every k>=1.

Next: Smith-normal-form reduction of every cyclic-cokernel monomial pullback to this
binomial Kummer cover.
```
