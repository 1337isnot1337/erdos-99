> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_d2_p2_odd_square_cover_kummer_2026-09-10.md) · source SHA-256 `89de258d5ea13b9ce14d56925ae83cad8745beadd6e513817a4708b6098e856b`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-194B0F7B8525","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic `d_H=2`, P2: primitive-character Kummer rigidity on the odd square-cover curve

**Date:** 2026-09-10  
**Repository branch:** `research/post-zf-currency-coupling-2026-09-09`  
**Run type:** exact function-field theorem  
**Target:** odd-`m` P2 arithmetic branch  
**Depends on:** GC/PK parameterization of the Gaussian P2 curve; CI methodology  
**External literature:** standard Capelli binomial criterion and Smith normal form only  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

ES closes all sufficiently large even `m=q-4` P2 survivors. For odd `m`, the reciprocal lift naturally becomes Gaussian only after the substitution `Z=T^2`. This introduces the fixed square-cover curve

```math
\boxed{
\mathcal G(X,Y)
:=\mathcal F(X^2,Y)
=X^4Y^2+i(4X^4-6X^2+4)Y-1.
}
\tag{OK.1}
```

The possible new obstruction is that a primitive torus character might become a proper power after this quadratic pullback. It does not.

### Theorem OK — primitive-character Kummer rigidity on the square cover

Let

```math
K=\mathbb Q(i),
\qquad
C_2/K:\ \mathcal G(X,Y)=0.
```

For every primitive pair

```math
(r,s)\in\mathbb Z^2,
\qquad \gcd(r,s)=1,
```

put

```math
\chi_{r,s}:=X^rY^s\in K(C_2)^\times.
```

Then for every prime `p`,

```math
\boxed{\chi_{r,s}\notin K(C_2)^p.}
\tag{OK.2}
```

Consequently for every integer `k>=1`,

```math
\boxed{T^k-\chi_{r,s}\text{ is irreducible over }K(C_2).}
\tag{OK.3}
```

The Capelli `4|k` exceptional form is also impossible.

As in CI, this implies:

### Corollary OK-CI — every primitive rank-two monomial pullback of `mathcal G` is irreducible

If

```math
M\in\mathbb Z^{2\times2},
\qquad \det M\ne0,
\qquad \gcd(\text{entries of }M)=1,
```

then the monomial pullback

```math
\phi_M^*\mathcal G
```

is irreducible in

```math
K[U^{\pm1},V^{\pm1}].
\tag{OK.4}
```

Thus the square substitution needed for odd `m` introduces no new rank-two factorization obstruction.

---

## 1. Function field of the square-cover curve

PK parameterizes the original Gaussian curve

```math
C:\ \mathcal F(x,y)=0
```

by

```math
K(C)=K(u),
\qquad
x=\frac{u(u-2)}{1-2u},
\qquad
y=-iu^{-2}.
\tag{1.1}
```

The map

```math
C_2\longrightarrow C,
\qquad
(X,Y)\longmapsto(X^2,Y)
```

therefore gives

```math
\boxed{
K(C_2)=K(u,t),
\qquad
t^2=\frac{u(u-2)}{1-2u},
\qquad X=t,
\qquad Y=-iu^{-2}.
}
\tag{1.2}
```

The rational function

```math
x(u)=\frac{u(u-2)}{1-2u}
```

has simple zeros at `u=0,2` and simple poles at `u=1/2,infinity`. Hence it is not a square even in

```math
\overline K(u).
```

Therefore the quadratic extension in (1.2) is geometrically irreducible. In particular `C_2` is geometrically integral and its constant field inside `K(C_2)` is exactly `K`.

This also proves directly that `mathcal G` is irreducible over `K`.

---

## 2. Four ramified valuations

The quadratic cover

```math
t^2=x(u)
```

ramifies at each of the four odd-order zero/pole places of `x`:

```math
u=0,
\qquad u=2,
\qquad u=1/2,
\qquad u=\infty.
```

Let the corresponding places of `K(C_2)` be denoted by the same symbols. Their ramification index over `K(u)` is two.

Hence

```math
\operatorname{ord}(t)
=(1,1,-1,-1)
\tag{2.1}
```

at those four places.

Because

```math
Y=-iu^{-2},
```

and pullback doubles the base valuation of `u`,

```math
\operatorname{ord}(Y)
=(-4,0,0,4).
\tag{2.2}
```

Therefore for

```math
\chi_{r,s}=X^rY^s=t^rY^s
```

we have the exact divisor-order vector

```math
\boxed{
\bigl(
 r-4s,
 r,
 -r,
 -r+4s
\bigr).
}
\tag{2.3}
```

This is the square-cover analogue of PK's vector `(r-2s,r,-r,-r+2s)`.

---

## 3. No odd prime power

Suppose

```math
\chi_{r,s}=f^p
```

for an odd prime `p`.

Every valuation of a `p`th power is divisible by `p`. From the second and first entries of (2.3),

```math
p\mid r,
\qquad
p\mid(r-4s).
```

Thus

```math
p\mid4s.
```

Since `p` is odd,

```math
p\mid s.
```

This contradicts

```math
\gcd(r,s)=1.
```

Hence

```math
\boxed{
\chi_{r,s}\notin K(C_2)^p
\quad\text{for every odd prime }p.
}
\tag{3.1}
```

---

## 4. No square

Suppose

```math
\chi_{r,s}=f^2.
```

The valuation at `u=2` gives

```math
r\equiv0\pmod2.
```

Primitivity then forces `s` odd.

From (1.2),

```math
\begin{aligned}
\chi_{r,s}
&=t^r(-i)^su^{-2s}\\
&=(-i)^s
\left(t^{r/2}u^{-s}\right)^2.
\end{aligned}
\tag{4.1}
```

For odd `s`, the square class of the constant coefficient is exactly the square class of

```math
-i.
```

PK proves

```math
-i\notin K^2.
```

Because `C_2` is geometrically integral, `K` is algebraically closed in `K(C_2)`. Thus a square root of the algebraic constant `-i` in `K(C_2)` would already lie in `K`, impossible.

Therefore

```math
\boxed{
\chi_{r,s}\notin K(C_2)^2.
}
\tag{4.2}
```

Combining Sections 3-4 proves OK.2.

---

## 5. Capelli binomial criterion

Apply Capelli's standard binomial irreducibility criterion to

```math
T^k-\chi_{r,s}.
```

For every prime divisor `p|k`, OK.2 says `chi_{r,s}` is not a `p`th power.

If `4|k`, the exceptional possibility

```math
\chi_{r,s}=-4b^4
```

would make

```math
\chi_{r,s}=(2ib^2)^2
```

a square because `i in K`, contradicting Section 4.

Thus

```math
T^k-\chi_{r,s}
```

is irreducible for every `k>=1`. This proves OK.3. `square`

---

## 6. Cyclic-isogeny consequence

The proof of CI now repeats verbatim with `C_2` in place of `C`.

Let `M` be full rank with gcd of its entries one. Smith normal form gives

```math
UMV=\operatorname{diag}(1,k)
```

for unimodular `U,V`. Unimodular monomial changes preserve Laurent irreducibility. After those changes, the pullback is a single `k`th-root extension of a primitive target character.

OK.3 makes that Kummer extension irreducible over `K(C_2)`. Capelli composition and Gauss's lemma therefore show that the full rank-two monomial pullback is irreducible.

Hence

```math
\boxed{
\phi_M^*\mathcal G\text{ irreducible whenever }\gcd(M_{ij})=1.
}
```

This proves OK-CI. `square`

---

## 7. Regression audit

### Does the square pullback split the base curve?

No. The new square root satisfies

```math
t^2=x(u),
```
and `x(u)` has four odd-order divisor places. It cannot be a square even over the algebraic closure of the constant field.

### Could `-i` become a square in the quadratic function field?

No. Geometric integrality means the algebraic closure of `K` inside the function field remains `K`.

### Odd prime `p=2`

Separated correctly. The odd-prime argument uses invertibility of four modulo `p`; `p=2` is handled by the Gaussian constant class.

### Negative character exponents

Allowed exactly as in PK. The functions `X,Y` are nonzero in the function field and the valuation argument is unchanged.

### Noncyclic Smith kernel

Not claimed. OK-CI assumes first Smith invariant one, exactly as CI.

---

## 8. What this changes

The odd-`m` reciprocal-lift trick requires a square root of the reciprocal variable. That initially looked like it might destroy CI's primitive-character rigidity.

It does not. The square-cover curve has the stronger valuation pattern

```math
(r-4s,r,-r,-r+4s),
```

which gives the same Kummer conclusion.

Thus all rank-two monomial pullbacks that can arise from a primitive large-gap specialization of the fixed curve `mathcal G` are irreducible over `Q(i)`.

The next theorem should apply Schinzel 74 to

```math
\mathcal G(T,T^{2n-1})
```

and then use the degree separation in

```math
R_{2n+1}(T^2)
```

to force `H_{2n+1}` irreducible. If that goes through, P2 is eliminated completely for all sufficiently large `m`, both parities.

---

## 9. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Odd m uses the fixed square-cover curve
  mathcalG(X,Y)=mathcalF(X^2,Y).
PK parameterization gives
  K(C2)=Q(i)(u,t),
  t^2=u(u-2)/(1-2u), X=t, Y=-i u^-2.
The four places u=0,2,1/2,infinity ramify, giving
  ord X=(1,1,-1,-1),
  ord Y=(-4,0,0,4).
Hence primitive chi=X^rY^s has orders
  (r-4s,r,-r,-r+4s).
For odd p, pth power => p|r and p|4s => p|s, contradiction.
For p=2, r even and s odd, so
  chi=(-i)^s(t^(r/2)u^-s)^2,
and -i remains nonsquare because C2 is geometrically integral.
Thus no primitive character is any prime power; Capelli gives
  T^k-chi irreducible for all k.
Smith normal form then gives irreducibility of every full-rank monomial pullback of
mathcalG with first Smith invariant 1.

Next: Schinzel on mathcalG(T,T^(2n-1)) + degree separation in R_(2n+1)(T^2).
```
