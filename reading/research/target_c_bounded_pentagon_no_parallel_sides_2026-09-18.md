> Generated reading edition · [exact source](../../research/target_c_bounded_pentagon_no_parallel_sides_2026-09-18.md) · source SHA-256 `88b604141fcb7c62049273c10836a3a37338187d6b94deed5a2f46c36b7b01a0`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

# Target C-II — bounded unit-contact pentagon faces have no parallel side pair

**Date:** 2026-09-18  
**Status:** proof-only local structural lemma; theorem-state authority unchanged  
**Scope:** strictly convex bounded pentagonal faces of the complete unit-contact graph  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

A small local fact used implicitly in the one-anchor corank argument has useful
independent consequences.

## Lemma — no projectively parallel side pair on a bounded contact pentagon

Let `F` be a strictly convex bounded face of the complete unit-contact graph and assume
`F` has five sides.  Every side has length one.  Then no two sides of `F` are
projectively parallel.

### Proof

Assume two side vectors are projectively parallel.  Strict convexity prevents two
distinct oriented boundary sides from having the same direction, so the two unit side
vectors are exact negatives, say `a` and `-a`.

Let the other three oriented unit side vectors be `v_1,v_2,v_3`.  Boundary closure
gives

```math
 a-a+v_1+v_2+v_3=0,
```

hence

```math
 v_1+v_2+v_3=0.
\tag{P.1}
```

Three unit vectors summing to zero are separated by exactly `2pi/3` in oriented angle.
Their three directions partition the circle into three open arcs of angle `2pi/3`.
The two additional directions `a,-a` cannot coincide with a `v_i` and can occupy at
most two of those arcs.  Therefore at least one pair of the `v_i` is consecutive in
the cyclic edge-direction order of the pentagon, with exterior turn exactly `2pi/3`.

The corresponding interior angle is `pi/3`.  If the two unit boundary sides meeting at
that vertex have other endpoints `x,z`, then

```math
 |x-z|^2=1+1-2\cos(\pi/3)=1.
```

Thus `xz` is another unit contact.  Strict convexity puts the segment `xz` in the
interior of `F`, so the complete unit-contact graph contains a chord cutting the
supposed face.  Contradiction.

Hence a bounded strictly convex unit-contact pentagon has no projectively parallel
side pair.  `square`

---

## Corollary 1 — two-outside residual faces have degree at least six

In the maximal two-anchor residual system, an `n_2` face has two trains to the
outer/activated side.  Maximality says their two side directions are projectively
parallel; otherwise the face would activate.  The lemma therefore excludes degree
five.  Hence every `n_2` face has

```math
 \deg F\ge6,
 \qquad
 x(F):=\deg F-5\ge1.
```

Writing

```math
 x_U:=\sum_{F\in U}(\deg F-5),
```

we get the exact finite charge

```math
\boxed{n_2\le x_U.}
\tag{P.2}
```

Since `x_A+x_U=Q-f`, the terminal correlated variable
`r=(Q-f)/D` also controls the density of `n_2` residual faces.

---

## Corollary 2 — mutual one-anchor parallel links consume degree excess

A mutually parallel one-anchor link joins two `n_1` residual faces and is
projectively parallel, at each endpoint, to that endpoint's unique outside train.
Thus each endpoint face contains a projectively parallel side pair and cannot be a
pentagon.  Each endpoint contributes at least one unit of degree excess.

Such links form a matching because a strictly convex face has at most one internal
side projectively parallel to its outside anchor.  If `p_U` is their number, their
`2p_U` endpoint faces are distinct.  Therefore

```math
\boxed{2p_U\le x_U.}
\tag{P.3}
```

The one-anchor corank theorem shows that every such link supplies an exact finite flex.
Equation (P.3) identifies the scalar currency that pays for those extra flexes: they
can only occur on degree-excess faces.

---

## Corollary 3 — degree-pure endpoint normal form

If a stalled terminal sequence satisfies

```math
 {Q-f\over D}\to0,
```

then automatically

```math
 {n_2\over D}\to0,
 \qquad
 {p_U\over D}\to0.
```

Thus the degree-pure one-anchor endpoint cannot use a linear population of either
parallel outside pairs or mutual parallel internal links.  Its remaining obstruction
is the nonparallel one-anchor relation network isolated in the new corank theorem.

This does not close C-II.  It removes a local pentagonal escape and makes the
`K_5` one-anchor dual block the clean degree-pure target.

No theorem-state file is changed.

**Disposition:** proved a finite no-parallel-side theorem for bounded contact
pentagons and extracted the exact charges `n_2<=x_U` and `2p_U<=x_U`; C-II remains
open.
