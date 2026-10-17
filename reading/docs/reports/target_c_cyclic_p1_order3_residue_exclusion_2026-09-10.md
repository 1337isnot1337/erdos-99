> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_p1_order3_residue_exclusion_2026-09-10.md) · source SHA-256 `efd7badecf1e5676cb9aa9675afc77f927ab180a7c2f455db3cd3f213813c38c`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 14 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-D2D054DDF3B0","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
LEVEL I STATUS: STILL OPEN

# Erdős Problem #99 — P1 physical factor cannot use the order-three 2-adic trace residue

**Date:** 2026-09-10  
**Run type:** exact exceptional-cluster 2-adic exclusion  
**Target:** cyclic primitive `d_H=1`, P1 arithmetic endpoint  
**Depends on:** P2/P3 reduction on PR #150; RL and FRM on this branch  
**External literature:** standard Newton-polygon root theorem only  
**Computation:** none

## 1. Result

Write

```math
m=q-2=ru,
\qquad r=2^k,
\qquad u\text{ odd}.
```

Let

```math
Y=2\cos\delta
```

be the physical P1 trace root of

```math
G_m(T)=C_m(T)+4T-6,
```

and let `h(T)` be its monic irreducible minimal polynomial over `Q`.

RL excludes the zero trace residue `T=0`. FRM proves that every nonzero residue trace other than `T=1` is either absent from `h mod 2` or appears with the full multiplicity `r`.

The only exceptional residue left by FRM is

```math
\bar T=1,
```

which corresponds to primitive third roots of unity and occurs only when `3|u`.

### Theorem O3 — order-three residue exclusion

For every P1 survivor,

```math
\boxed{T+1\nmid h(T)\pmod2.}
\tag{O3.1}
```

In particular, even when `3|u`, the irreducible physical factor cannot use the order-three trace cluster.

Combined with RL and FRM, this removes every exceptional residue:

### Corollary O3.1 — exact mod-two subset form

Write the squarefree odd-part trace polynomial as

```math
Q_u=(T+1)^\epsilon f_1\cdots f_s,
\qquad
\epsilon=1\iff3|u,
```

where every `f_j` is irreducible over `F_2` and distinct from `T,T+1`. Then every hypothetical P1 physical factor has

```math
\boxed{
h(T)\equiv\prod_{j\in J}f_j(T)^r\pmod2
}
\tag{O3.2}
```

for a nonempty subset `J`.

Thus the P1 factor problem is now literally a subset-of-nontrivial-odd-trace-orbits problem: zero residue is forbidden, order three is forbidden, and every selected remaining orbit is taken with exact multiplicity `2^k`.

---

## 2. The order-three Teichmuller trace is `-1`

Assume `3|u`. Since `u` is odd,

```math
u\equiv3\pmod6.
```

Let `omega` be a primitive third root of unity in the unramified quadratic extension of `Q_2`. Then

```math
\omega+\omega^{-1}=-1
```

and

```math
\omega^u=1.
```

Therefore

```math
\boxed{C_u(-1)=2.}
\tag{2.1}
```

Put

```math
X=T+1.
```

Exactly as in FRM, the trace root is double and its quadratic coefficient is a 2-adic unit. Hence

```math
\boxed{
C_u(-1+X)-2=X^2V(X),
\qquad V(0)\in\mathbb Z_2^\times.
}
\tag{2.2}
```

The unit statement can also be read modulo two from the squarefree odd-part factor `Q_u`: the residue `T=1` is a simple root of `Q_u`, so it is an exact double root of `C_u mod 2`.

---

## 3. Expand the full P1 trace polynomial at `-1`

As in FRM, define

```math
H_r(Y):=C_r(2+Y)-2.
```

For every power of two `r`,

```math
H_r(Y)\equiv Y^r\pmod4,
\qquad
H_r(0)=0.
\tag{3.1}
```

Since `C_m=C_r\circ C_u`, equations (2.2)-(3.1) give

```math
\begin{aligned}
G_m(-1+X)
&=C_r(C_u(-1+X))+4(-1+X)-6\\
&=H_r(X^2V(X))+4X-8.
\end{aligned}
\tag{3.2}
```

This is the exact exceptional-cluster expansion.

---

## 4. Case `r>=2`

Assume

```math
r=2^k\ge2.
```

From (3.2):

- the constant coefficient is exactly `-8`, with valuation `3`;
- the coefficient of `X` is exactly `4`, with valuation `2`;
- every coefficient of degrees `2,...,2r-1` has valuation at least `2`;
- the coefficient of `X^(2r)` is a 2-adic unit, coming from `(X^2V)^r`.

Therefore the lower Newton polygon begins

```math
\boxed{
(0,3)\longrightarrow(1,2)\longrightarrow(2r,0).
}
\tag{4.1}
```

The first segment has slope `-1` and length one. The second has slope

```math
\boxed{-\frac2{2r-1}.}
\tag{4.2}
```

Because `2r-1` is odd, this fraction is reduced. Thus every local irreducible factor supported on the second segment has degree divisible by

```math
\boxed{2r-1.}
\tag{4.3}
```

### The slope-minus-one root is exactly `T=1`

Since `r>=2`, `m=ru` is divisible by six. Hence

```math
C_m(1)=2\cos(m\pi/3)=2
```

and

```math
G_m(1)=2+4-6=0.
```

In the coordinate `X=T+1`, this root is

```math
X=2,
```

which has 2-adic valuation one. It is therefore exactly the unique root on the first Newton segment.

Now `h` is the irreducible minimal polynomial of the physical root `Y`, which is close to `2` and in particular is not `1`. If `h` contained the local factor `T-1`, then `h(1)=0`; irreducibility over `Q` would force

```math
h=T-1,
```

contrary to `Y ne1`.

Therefore every root of `h` reducing to `T=1` must lie on the second Newton segment.

If

```math
(T+1)^a\Vert h\pmod2,
```

then `a` is the total local degree of those roots. By (4.3), if `a>0` then

```math
\boxed{a\ge2r-1.}
\tag{4.4}
```

---

## 5. Littlewood multiplicity contradicts the large cluster

Let

```math
M(Z)=Z^d h(Z+Z^{-1})
```

be the reciprocal minimal polynomial of the P1 Littlewood root `z`, so `M|P` and

```math
P\equiv S_m\pmod2.
```

The trace residue `T=1` corresponds to the two primitive third roots `bar omega,bar omega^{-1}`. Since `3|u`, each is a nontrivial `u`-th root. In

```math
S_m(Z)=\frac{Z^{ru}-1}{Z-1}
```

each nontrivial `u`-th root has multiplicity exactly `r` in characteristic two.

If `(T+1)^a|h mod 2`, then each primitive third root has multiplicity `a` in `M mod 2`. Divisibility `M|S_m mod 2` therefore gives

```math
\boxed{a\le r.}
\tag{5.1}
```

For `r>=2`, (4.4) and (5.1) are incompatible because

```math
2r-1>r.
```

Hence

```math
(T+1)\nmid h\pmod2
```

for every `r>=2`.

---

## 6. Case `r=1`

Now `m=u` is odd and divisible by three. Equation (3.2) becomes

```math
G_u(-1+X)=X^2V(X)+4X-8.
```

The relevant Newton points are

```math
(0,3),\qquad(1,2),\qquad(2,0).
```

The point `(1,2)` lies strictly above the segment from `(0,3)` to `(2,0)`, whose slope is

```math
\boxed{-\frac32.}
```

Thus every local irreducible factor above the order-three residue has degree divisible by two. Consequently if

```math
(T+1)^a\mid h\pmod2,
```

then

```math
\boxed{a\ge2.}
\tag{6.1}
```

But the Littlewood reduction contains each primitive third root with multiplicity exactly

```math
r=1,
```

so again

```math
a\le1.
```

Contradiction.

This proves O3 for `r=1` as well. `square`

---

## 7. Unified mod-two normal form

Combine three exact theorems:

1. **RL:** the zero trace factor `T` is absent;
2. **O3:** the order-three trace factor `T+1` is absent;
3. **FRM:** every other selected irreducible trace factor occurs with exponent exactly `r`.

Therefore, if

```math
Q_u=(T+1)^\epsilon f_1\cdots f_s
```

is the odd-part squarefree trace polynomial, then the physical factor satisfies

```math
\boxed{
h\equiv R(T)^r\pmod2,
\qquad
R=\prod_{j\in J}f_j,
}
\tag{7.1}
```

with `J` nonempty and containing no order-three factor.

In particular

```math
\boxed{
\deg h=r\deg R.
}
\tag{7.2}
```

The P1 Littlewood trace-degree bound

```math
\deg h\le\frac{ru-1}{2}
```

becomes the finite odd-part inequality

```math
\boxed{
\deg R\le\frac{u-1}{2}.
}
\tag{7.3}
```

When `3|u`, O3 removes one degree-one residue factor, so actually every allowed `R` is a factor of the complementary degree `(u-3)/2` part of `Q_u`.

---

## 8. Consequences for previously excluded families

### `u=1`

There is no nonzero odd-order trace residue. RL already leaves no possible factor. This recovers the power-of-two obstruction at the mod-two support level.

### `u=3`

The only nonzero odd-order trace residue is the order-three residue `T=1`. O3 removes it. Therefore no physical factor remains.

Thus O3 + RL rederive the support-level impossibility behind the two pure odd parts `u=1,3`; PR #150 retains the stronger direct Newton proofs as independent audited routes.

---

## 9. Regression audit

### Why the exact rational root matters for `r>=2`

The first Newton segment cannot simply be discarded because it has degree one. It is discarded only after identifying its unique root as the exact rational root `T=1`, which cannot lie in the irreducible minimal polynomial of the distinct physical root.

### No false path inference

This proof is purely arithmetic and does not use the invalid inference audited in PR #151 that consecutive incident diameter edges form an Euler trail.

### No full irreducibility

Nothing here asserts that `G_m` or its large complementary factors are irreducible over `Q` or `Q_2`.

### Multiplicity in the reciprocal lift

A trace factor `(T+1)^a` produces multiplicity `a` at each primitive third root under `T=Z+Z^{-1}`. Those roots are distinct in characteristic two because they have odd order three, so the comparison with `S_m` is legitimate.

---

## 10. New exact arithmetic target

There are now no exceptional residue classes left. A hypothetical P1 factor has

```math
h\equiv R^r\pmod2
```

for a squarefree product `R` of nonzero, non-order-three odd-part trace factors.

The highest-value next target is therefore:

> show that no proper subset `R` of the allowed odd-part trace orbits can lift to the irreducible factor of `G_{ru}` containing the distinguished largest real root while also satisfying the P1 degree bound.

For odd parts whose allowed trace roots form one Frobenius orbit, the mod-two support is already forced completely. In those cases the remaining Littlewood quotient has degree only `r-1`, which is the next natural finite target.

---

## 11. Promotion recommendation

**Hold as report-level theorem pending independent audit.**

O3 is exact downstream of the report-level P1 arithmetic reduction and uses no computation.

---

## 12. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

m=ru, r=2^k, u odd. Assume 3|u. The exceptional trace residue T=1 has
Teichmuller trace lift -1. Put X=T+1. Then
  C_u(-1+X)-2=X^2V(X), V(0) a 2-adic unit,
and for H_r(Y)=C_r(2+Y)-2,
  H_r(Y)==Y^r mod4.
Thus
  G_m(-1+X)=H_r(X^2V)+4X-8.

If r>=2 the Newton polygon starts
  (0,3)->(1,2)->(2r,0).
The first root is exactly T=1, a rational factor that cannot belong to the physical
irreducible h. Every other local factor has degree divisible by 2r-1. Therefore any
order-three exponent a in h mod2 satisfies a>=2r-1.
But reciprocal Littlewood divisibility gives a<=r. Contradiction.

If r=1, the initial segment is (0,3)->(2,0), so a>=2>1, again impossible.

Hence T+1 never divides h mod2.
Together with RL+FRM:
  h mod2=R(T)^r,
where R is a squarefree product of nonzero non-order-three odd-part trace factors.
Every selected residue orbit occurs at full multiplicity r; no exceptional orbit remains.
```
