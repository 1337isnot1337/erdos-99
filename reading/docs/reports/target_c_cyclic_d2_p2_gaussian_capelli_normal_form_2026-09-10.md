> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_d2_p2_gaussian_capelli_normal_form_2026-09-10.md) · source SHA-256 `6e97985943b5fec55fb9124277a22d55393cc5720d7690e4d3d69fa327973c70`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 1 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-4896C984FFEF","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic `d_H=2`, P2: Gaussian lacunary factor and complete Capelli audit

**Date:** 2026-09-10  
**Repository branch:** `research/post-zf-currency-coupling-2026-09-09`  
**Run type:** exact algebraic reduction / bivariate irreducibility audit  
**Target:** even-`m` P2 subphase  
**Depends on:** P2A reciprocal lift  
**External literature:** Capelli's binomial irreducibility criterion; Filaseta's 2023 lacunary theorem is discussed only as a conditional bridge and is **not** imported over `Q(i)` without a coefficient-field justification  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

P2A gives, for even

```math
m=2n,
```
the Gaussian factorization

```math
R_m(Z)=Z^mH_m(Z+Z^{-1})=F_n^+(Z)F_n^-(Z),
```
where

```math
\boxed{
F_n^\pm(Z)
=Z^{2n}-1\pm iZ^{n-1}(4Z^2-6Z+4).
}
\tag{GC.1}
```

The new point is that each `F_n^+` is a fixed bivariate lacunary specialization whose complete Capelli test can be solved exactly over the Gaussian rational function field.

Put

```math
A(X):=4X^2-6X+4,
```

and

```math
\boxed{
\mathcal F(X,Y):=X^2Y^2+iA(X)Y-1\in\mathbb Z[i][X,Y].
}
\tag{GC.2}
```

Then

```math
\boxed{
F_n^+(X)=\mathcal F(X,X^{n-1}).
}
\tag{GC.3}
```

### Theorem GC — complete Gaussian Capelli audit

For every integer `t>=0` and every integer `ell>=1`, each of

```math
\boxed{
\mathcal F^+_{t,\ell}(X,Y)
:=-1+iA(X)X^tY^\ell+X^{2+2t}Y^{2\ell},
}
\tag{GC.4}
```

and

```math
\boxed{
\mathcal F^-_{t,\ell}(X,Y)
:=-X^{2t}+iA(X)X^tY^\ell+X^2Y^{2\ell}
}
\tag{GC.5}
```

is a power of `X` times an irreducible polynomial in `Q(i)[X,Y]` (equivalently, after removal of its maximal monomial factor, in `Z[i][X,Y]`).

Moreover:

### Theorem GC-R — no reciprocal factor

For every `n>=2`,

```math
\boxed{F_n^+(X)\text{ has no nonconstant reciprocal factor in }\mathbb Q(i)[X].}
\tag{GC.6}
```

Therefore every algebraic hypothesis in the **bivariate/reciprocal part** of Filaseta's lacunary specialization mechanism is satisfied by `mathcal F` over `Q(i)`.

What is not yet asserted is that Filaseta's integer-coefficient one-variable theorem extends verbatim from `Q` to `Q(i)`.  Establishing that coefficient-field bridge would imply that `F_n^+` is irreducible over `Q(i)` for all sufficiently large `n`, and then would force `H_{2n}` irreducible over `Q`, closing the entire sufficiently-large even-`m` P2 branch.

---

## 1. The base quadratic is irreducible

View `mathcal F` as a quadratic in `Y` over

```math
K_0:=\mathbb Q(i)(X).
```

Its discriminant is

```math
\begin{aligned}
\Delta
&=(iA)^2+4X^2\\
&=-A(X)^2+4X^2\\
&=\boxed{-16(X-1)^2(X^2-X+1).}
\end{aligned}
\tag{1.1}
```

The factor `X^2-X+1` is not a square in `K_0`, so `Delta` is not a square in `K_0`. Hence `mathcal F` is irreducible in `K_0[Y]` and therefore primitive irreducible in `Q(i)[X,Y]`.

Let

```math
s:=\sqrt{X^2-X+1}
```

and

```math
L:=K_0(s).
```

Define

```math
\boxed{
u:=s-(X-1),
\qquad
v:=s+(X-1).}
\tag{1.2}
```

Then

```math
\boxed{uv=X}
\tag{1.3}
```

and

```math
v-u=2(X-1)=2uv-2,
```
so

```math
\boxed{v=\frac{u-2}{1-2u}.}
\tag{1.4}
```

Thus

```math
\boxed{L=\mathbb Q(i)(u)}
\tag{1.5}
```

is a rational function field.

A direct expansion also gives

```math
\boxed{
\frac{-A(X)+4(X-1)s}{2}=-u^2,
\qquad
\frac{-A(X)-4(X-1)s}{2}=-v^2.
}
\tag{1.6}
```

These identities make every Capelli root monomial in `u,v`.

---

## 2. The `+t` bivariate specialization

Put

```math
T:=Y^\ell.
```

Then GC.4 is the quadratic

```math
X^{2+2t}T^2+iA(X)X^tT-1.
\tag{2.1}
```

Its discriminant is `X^{2t}Delta`, so its splitting field over `K_0` is still `L`.
Using (1.6), its two roots are

```math
\boxed{
\beta_1=-iu^{-t}v^{-(t+2)},
\qquad
\beta_2=-iu^{-(t+2)}v^{-t}.
}
\tag{2.2}
```

We claim that for each root `beta`:

1. `beta` is not a `p`th power in `L` for any prime `p`;
2. in particular `beta` is not a square;
3. therefore the exceptional Capelli form `-4 gamma^4` is also impossible.

In `L=Q(i)(u)`, the rational function

```math
v=\frac{u-2}{1-2u}
```
has one simple zero at `u=2` and one simple pole at `u=1/2`; the function `u` has one simple zero at `u=0` and one simple pole at infinity.

For `beta_1`, the four divisor orders are, up to sign,

```math
t,\quad t,\quad t+2,\quad t+2.
\tag{2.3}
```

Thus an odd prime `p` dividing all divisor orders would divide both `t` and `t+2`, hence divide `2`, impossible. So `beta_1` is not an odd `p`th power. The same argument applies to `beta_2`.

For `p=2`:

- if `t` is odd, the divisor at `u=0` has odd order, so `beta_j` is not a square;
- if `t` is even, the rational-function monomial part is a square, and a square root would require the constant `-i` to be a square in `Q(i)`.

But `-i` is not a square in `Q(i)`. If

```math
(a+bi)^2=-i,
\qquad a,b\in\mathbb Q,
```
then `a^2-b^2=0` and `2ab=-1`, forcing `a^2=1/2` up to sign, impossible in `Q`.

Since the constant field `Q(i)` is algebraically closed in the rational function field `Q(i)(u)`, `-i` cannot acquire a square root inside `L` either.

Hence no `beta_j` is a square.

Finally if

```math
\beta_j=-4\gamma^4,
```
then

```math
\beta_j=(2i\gamma^2)^2
```
would be a square, already excluded.

Capelli's criterion therefore says

```math
T^\ell-\beta_j
```
is irreducible over `L` for every `ell>=1`.  Applying Capelli to the irreducible quadratic (2.1) yields irreducibility of GC.4 over `K_0[Y]`, and Gauss's lemma gives irreducibility in `Q(i)[X,Y]`. `square`

---

## 3. The `-t` bivariate specialization

Now consider GC.5 as a quadratic in

```math
T=Y^\ell:
```

```math
X^2T^2+iA(X)X^tT-X^{2t}.
\tag{3.1}
```

Its two roots in the same field `L` are

```math
\boxed{
\gamma_1=-iu^tv^{t-2},
\qquad
\gamma_2=-iu^{t-2}v^t.
}
\tag{3.2}
```

Their divisor orders are, up to sign,

```math
t,\quad t,\quad t-2,\quad t-2.
\tag{3.3}
```

Again every odd common prime divisor would divide `gcd(t,t-2)`, hence divide two, impossible. For `p=2`, odd `t` gives an odd divisor order, while even `t` reduces squarehood to squarehood of the constant `-i`, which was excluded above.

Thus no `gamma_j` is a `p`th power for any prime `p`, and no exceptional `-4` fourth-power form occurs. Capelli gives irreducibility over `K_0[Y]` after removing the maximal common power of `X`.

Explicitly the common monomial factor is

```math
X^{d_t},
\qquad
 d_t:=\min\{2t,t,2\}.
\tag{3.4}
```

After dividing by `X^{d_t}`, the polynomial is primitive over the UFD `Z[i][X]`, so Gauss's lemma gives the asserted irreducibility. `square`

---

## 4. `F_n^+` has no reciprocal factor

The reciprocal polynomial is

```math
\widetilde{F_n^+}(X)
=X^{2n}F_n^+(1/X).
```

Since

```math
X^2A(1/X)=A(X),
```
we get

```math
\boxed{
\widetilde{F_n^+}(X)=-F_n^-(X).
}
\tag{4.1}
```

If a nonconstant reciprocal irreducible polynomial `g` divided `F_n^+`, then its reciprocal is a unit multiple of itself, so `g` would also divide `F_n^-`.

But

```math
F_n^++F_n^-=2(X^{2n}-1),
```

```math
F_n^+-F_n^-=2iX^{n-1}A(X).
```

Hence any common nonconstant factor would divide both

```math
X^{2n}-1
```

and

```math
A(X).
```

This gcd is one. Indeed a nonzero root `rho` of

```math
A(X)=2(2X^2-3X+2)
```
satisfies

```math
\rho+\rho^{-1}=\frac32.
\tag{4.2}
```

If `rho` were a root of unity, then `rho+rho^{-1}` would be an algebraic integer. A rational algebraic integer is an integer, but `3/2` is not an integer. Thus no root of `A` is a root of unity.

Therefore

```math
\gcd(F_n^+,F_n^-)=1
```
and `F_n^+` has no nonconstant reciprocal factor. This proves GC-R. `square`

---

## 5. Exact interface with Filaseta's theorem

Filaseta, *On the Factorization of lacunary polynomials*, Theorem 4.1 (2023), states over `Z` that for

```math
F(X,Y)=\sum_{j=0}^r f_j(X)Y^j
```
with the stated primitive/nonzero-end hypotheses, the nonreciprocal part of

```math
F(X,X^N)
```
is not reducible for sufficiently large `N` provided the two families obtained from every `N=kell+t` and `N=kell-t` are powers of `X` times irreducible bivariate polynomials for every `t>=0, ell>=1`.

For our fixed Gaussian polynomial GC.2, GC.4-GC.5 are exactly those two bivariate families with `r=2`.

Sections 1-3 prove their irreducibility over `Q(i)` for **every** `t,ell`, while Section 4 removes reciprocal factors from the one-variable specialization.

The remaining issue is solely the coefficient field:

> Filaseta's printed theorem is formulated for `Z/Q`.  Before applying it to `Z[i]/Q(i)`, one must either cite a number-field version with matching hypotheses or reproduce the one-variable lacunary reduction over the Gaussian number field.

No such bridge is silently assumed in this report.

### Conditional consequence GC-F

If Theorem 4.1 admits the required `Q(i)` coefficient-field extension, then for all sufficiently large `n`,

```math
\boxed{F_n^+\text{ is irreducible over }Q(i).}
\tag{5.1}
```

Together with conjugation the same holds for `F_n^-`.

Now suppose `H_{2n}` had a proper factor `h in Q[X]` of degree `r`. Its reciprocal lift

```math
X^r h(X+X^{-1})
```
is a reciprocal polynomial of degree `2r` dividing

```math
R_{2n}=F_n^+F_n^-.
```

If `F_n^+` and `F_n^-` are irreducible and coprime over `Q(i)`, every nontrivial factor of `R_{2n}` over `Q(i)` is, up to units, one of

```math
F_n^+,
\quad
F_n^-,
\quad
F_n^+F_n^-.
```

The first two are nonreciprocal by GC-R, so the reciprocal lift cannot equal either. Thus it must be the whole product, forcing `h=H_{2n}`.

Hence the coefficient-field bridge would imply

```math
\boxed{H_{2n}\text{ irreducible over }Q\text{ for all sufficiently large }n,}
\tag{5.2}
```
and P2A would exclude the complete sufficiently-large **even-`m`** P2 phase.

---

## 6. Regression and scope audit

### Filaseta over `Q(i)`

Not assumed. The conditional conclusion is isolated explicitly.

### Capelli exceptional fourth-power case

Handled: `-4gamma^4` is itself a square, while every root beta/gamma above is proved nonsquare.

### Even `t`

Divisor parity alone does not exclude a square. The constant `-i` obstruction is essential and is proved in the Gaussian constant field.

### Reciprocal factors

Excluded directly by `gcd(F_n^+,F_n^-)=1`; no general lacunary reciprocal theorem is needed.

### Power-of-two P2I

Unaffected and stronger on its subsequence: P2I is unconditional and already closes `m=2^k` without any Filaseta bridge.

### Level I

Still open. Even after a future GC-F bridge, odd-`m` P2 and the PS/S2 branches would remain.

---

## 7. Shortest next lemma

The shortest arithmetic lemma is now exact:

> **Gaussian lacunary bridge.** Prove or import a number-field version of Filaseta Theorem 4.1 valid over `Q(i)` for the fixed polynomial `mathcal F(X,Y)=X^2Y^2+i(4X^2-6X+4)Y-1`.

All bivariate irreducibility and reciprocal-factor hypotheses have already been checked. A valid bridge closes P2 for every sufficiently large even `m`.
