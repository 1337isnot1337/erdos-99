> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_d1_p1_algebraic_degree_obstruction_2026-09-10.md) · source SHA-256 `f0a88031bbeefd0259296039d52899a2bb93c46f20e31379c09d48b8c074758b`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-38383D0278FB","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdos Problem #99 - P1 fixed-angle closure forces an anomalously low algebraic degree

**Date:** 2026-09-10  
**Repository base:** PR #118 head `57a2ad7b3af5d541ea8b190853dab584a1dbe909`  
**Run type:** exact algebraic reduction  
**Target:** cyclic primitive `d_H=1`, P1 endpoint  
**Depends on:** D1 exact P1 normal form and SC P1 Littlewood closure  
**New external literature:** none  
**Computation:** none in the proof

## LEVEL I STATUS

**STILL OPEN.**

The P1 endpoint already has two exact equations:

1. its geometric angle `delta` is fixed by
   
   ```math
   (q-2)\frac\delta2\text{ through }
   \cos\left((q-2)\frac\delta2\right)=2\sin\frac\delta2;
   ```

2. the remaining `q-2` primal side vectors give a Littlewood polynomial of degree
   `q-3` vanishing at `z=e^{i delta}`.

This report eliminates the half-angle and converts those statements into a sharp
algebraic-degree obstruction.

Put

```math
m:=q-2,
\qquad
z:=e^{i\delta},
\qquad
y:=z+z^{-1}=2\cos\delta.
\tag{ADG.1}
```

Then a P1 survivor must satisfy

```math
\boxed{H_m(y)=0,}
\tag{ADG.2}
```

where

```math
\boxed{
H_m(Y):=D_m(Y)+4Y-6
}
\tag{ADG.3}
```

and `D_m` is the monic Dickson/Chebyshev polynomial determined by

```math
D_0(Y)=2,
\qquad
D_1(Y)=Y,
\qquad
D_m(Y)=Y D_{m-1}(Y)-D_{m-2}(Y).
\tag{ADG.4}
```

Equivalently,

```math
D_m(2\cos\theta)=2\cos(m\theta).
```

At the same time the SC Littlewood closure forces

```math
\boxed{
[\mathbf Q(y):\mathbf Q]\le\frac{m-1}{2}.
}
\tag{ADG.5}
```

Therefore P1 is excluded as soon as one proves that the irreducible factor of `H_m`
containing the physical root `y=2 cos delta` has degree greater than `(m-1)/2`.

This is a substantially weaker arithmetic target than proving all of `H_m`
irreducible.

---

## 1. Eliminate the P1 half-angle

SC gives the exact P1 geometric equation

```math
\cos(mx)=2\sin x,
\qquad
x:=\frac\delta2.
\tag{1.1}
```

Square both sides:

```math
\cos^2(mx)=4\sin^2x.
```

Use

```math
\cos^2(mx)=\frac{1+\cos(2mx)}2,
\qquad
\sin^2x=\frac{1-\cos(2x)}2.
```

Since `2x=delta`,

```math
1+\cos(m\delta)=4(1-\cos\delta),
```
so

```math
\boxed{
\cos(m\delta)+4\cos\delta-3=0.
}
\tag{ADG.6}
```

Set `y=2 cos delta`. By ADG.4,

```math
D_m(y)=2\cos(m\delta).
```

Multiplying ADG.6 by two yields

```math
D_m(y)+4y-6=0,
```
which proves ADG.2--ADG.3.

### Squaring caveat

ADG.2 is a necessary condition only. Squaring may add roots of `H_m` corresponding
to the wrong sign in (1.1). This is harmless for the degree obstruction: the physical
P1 value is still a root of `H_m`.

---

## 2. `H_m` is monic integral of degree `m`

The recurrence ADG.4 immediately gives

```math
D_m\in\mathbf Z[Y]
```

and makes `D_m` monic of degree `m` for every `m>=1`. Hence

```math
\boxed{H_m\in\mathbf Z[Y]\text{ is monic of degree }m.}
\tag{ADG.7}
```

Therefore the physical `y` is an algebraic integer.

The associated reciprocal polynomial in `z` is obtained by multiplying
`H_m(z+z^{-1})` by `z^m`:

```math
\boxed{
G_m(z)
:=z^m H_m(z+z^{-1})
=z^{2m}+4z^{m+1}-6z^m+4z^{m-1}+1.
}
\tag{ADG.8}
```

Two useful exact decompositions are

```math
\boxed{
G_m(z)
=(z^m-1)^2+4z^{m-1}(z^2-z+1),
}
\tag{ADG.9}
```

and

```math
\boxed{
G_m(z)
=(z^m+1)^2+4z^{m-1}(z-1)^2.
}
\tag{ADG.10}
```

These identities may be useful for an all-`m` irreducibility/factor-degree theorem.

---

## 3. Insert the Littlewood closure

SC proves that P1 requires a Littlewood polynomial

```math
P(Z)=\sum_{k=0}^{m-1}\epsilon_k Z^k,
\qquad
\epsilon_k\in\{+1,-1\},
\tag{3.1}
```

such that

```math
\boxed{P(z)=0.}
\tag{ADG.11}
```

Thus the minimal polynomial of `z` over `Q` divides `P`, and consequently

```math
\boxed{
[\mathbf Q(z):\mathbf Q]\le m-1.
}
\tag{ADG.12}
```

No assertion that `z` is a root of unity is used.

---

## 4. Pass from `z` to the real trace `y=z+z^{-1}`

Because

```math
y=z+z^{-1},
```

we have

```math
z^2-yz+1=0.
\tag{4.1}
```

Therefore

```math
[\mathbf Q(z):\mathbf Q(y)]\le2.
```

For a genuine P1 source, `0<delta<pi`, so `z=e^{i delta}` is nonreal. But the field
`Q(y)` is contained in `R` under the physical embedding because `y=2 cos delta` is
real. Hence

```math
z\notin\mathbf Q(y).
```

Thus the extension is genuinely quadratic:

```math
\boxed{
[\mathbf Q(z):\mathbf Q(y)]=2.
}
\tag{ADG.13}
```

Combining with ADG.12 gives

```math
2[\mathbf Q(y):\mathbf Q]
=[\mathbf Q(z):\mathbf Q]
\le m-1.
```

This proves the central degree bound

```math
\boxed{
[\mathbf Q(y):\mathbf Q]\le\frac{m-1}{2}.
}
\tag{ADG.14}
```

Since the degree is integral, for even `m` this may be read as at most `(m-2)/2`.

---

## 5. Exact arithmetic closing lemma for P1

Let `F_m(Y)` denote the irreducible factor over `Q` of `H_m(Y)` that contains the
physical P1 root

```math
y_m=2\cos\delta_m,
```

where `delta_m` is the unique geometric P1 solution of the original unsquared equation
SC.9.

Then

```math
\deg F_m=[\mathbf Q(y_m):\mathbf Q].
```

Therefore:

### Theorem ADG - P1 algebraic-degree reduction

A P1 survivor with `m=q-2` can exist only if

```math
\boxed{
\deg F_m\le\frac{m-1}{2}.
}
\tag{ADG.15}
```

Consequently the following purely arithmetic statement would eliminate the complete
P1 branch:

> **ADG closing lemma.** For every sufficiently large `m`, the irreducible factor of
> `H_m(Y)=D_m(Y)+4Y-6` containing the physical root `y_m` has degree
> `>(m-1)/2`.

This does **not** require `H_m` itself to be irreducible.

---

## 6. One explicit cyclotomic factor is geometrically irrelevant

There is a simple exact exceptional factor that any factor theorem must retain.
Evaluate at `Y=1=2 cos(pi/3)`:

```math
H_m(1)
=2\cos(m\pi/3)+4-6
=2\cos(m\pi/3)-2.
```

Hence

```math
\boxed{Y-1\mid H_m(Y)\iff 6\mid m.}
\tag{ADG.16}
```

This factor corresponds in `z` to

```math
z^2-z+1=\Phi_6(z).
```

It cannot contain the physical P1 root for the large-diameter regime, because
`delta_m ->0` and therefore

```math
y_m=2\cos\delta_m\to2,
```

whereas the cyclotomic factor has `y=1`.

Thus a future irreducibility statement should be formulated, at most, as

```math
H_m/(Y-1)^{[6\mid m]}
```

rather than incorrectly claiming that every `H_m` is irreducible.

---

## 7. Modular identities and a dead easy route

Reducing ADG.8 modulo two gives

```math
\boxed{
G_m(z)\equiv(z^m+1)^2\pmod2.
}
\tag{ADG.17}
```

Every P1 Littlewood polynomial satisfies

```math
P(z)\equiv1+z+\cdots+z^{m-1}
=\frac{z^m-1}{z-1}\pmod2.
\tag{ADG.18}
```

In characteristic two, `z^m+1=z^m-1`, so these reductions are highly compatible.
Therefore a naive mod-two contradiction cannot close P1.

Modulo three,

```math
\boxed{
G_m(z)
\equiv(z^{m-1}+1)(z^{m+1}+1)\pmod3.
}
\tag{ADG.19}
```

This may be useful in combination with a second prime or the restricted P1 sign-run
structure, but by itself it is only a factorization identity.

---

## 8. Computational discovery, explicitly nonproof

A separate exact-arithmetic experiment motivated the closing lemma but is **not** used
above.

For `2<=m<=100`, symbolic factorization over `Q` gives the pattern

```math
H_m(Y)\text{ irreducible if }6\nmid m,
```

and

```math
H_m(Y)=(Y-1)Q_{m-1}(Y)
```

with `Q_{m-1}` irreducible if `6|m`.

If this pattern holds for all sufficiently large `m`, ADG.15 immediately excludes P1,
because the physical factor then has degree `m` or `m-1`, both strictly greater than
`(m-1)/2`.

This pattern is recorded only as a theorem-discovery target. Finite factorization is
not evidence for Level I and is not promoted into any proof statement.

---

## 9. Regression audit

- Squaring SC.9 may introduce spurious roots of `H_m`; the physical root still obeys
  ADG.2, which is all the degree argument needs.
- The Littlewood polynomial need not be irreducible and its unit-circle root need not
  be cyclotomic.
- The real-field degree is exactly half the `z`-degree because the physical `z` is
  nonreal while `Q(y)` is real under the chosen embedding.
- `Y-1` really is an exceptional factor when `6|m`; it must not be silently discarded
  from an all-`m` factorization claim. It is geometrically irrelevant to large P1.
- The factorization experiment through `m=100` is not a proof dependency.
- No conclusion about S1 is made here.

---

## 10. Next target

Prove the ADG closing lemma.

The most promising exact formulations are:

1. prove
   
   ```math
   H_m(Y)/(Y-1)^{[6\mid m]}
   ```

   irreducible over `Q`;
2. prove only that every noncyclotomic factor of `H_m` having a real root in the
   physical interval near `2` has degree `>(m-1)/2`;
3. exploit ADG.9--ADG.10 together with the P1 sign/run restrictions to rule out a
   low-degree reciprocal factor without classifying all factors.

Any one of these closes P1 completely.
