> Generated reading edition · [exact source](../../../docs/reports/target_c_two_body_hinge_integration_2026-08-31.md) · source SHA-256 `9c60292d661451a0690a65918766ce0e2beca719815f2f0590722d4a9d93a03f`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-B6E792CD886B","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C: two-body hinge integration

**Date:** 2026-08-31  
**Repository base:** `12042561` (main after bounded-star C58 / PR #60)  
**Run type:** exact finite integration theorem  
**Target:** Target C Gate C-I  
**Depends on:** C6 strict simultaneous weak release, C57 extreme-null-body rigidity, C58 bounded zero-transfer star forest

## LEVEL I STATUS

**STILL OPEN.**

C57-C58 reduce a surviving selected-kernel shear to rigid full-diameter null bodies whose different-motion midpoints are bounded zero-transfer star forests. The two-body part of that obstruction is not genuine.

If a relative-interior fixed-diameter critical velocity is rigid on two source bodies meeting in one source vertex, the relative infinitesimal rotation integrates to an actual same-diameter motion. For an active cross-body pair with zero first derivative, tangency makes the two endpoint rays collinear with the hinge. A unit contact must lie on the same ray and therefore lengthens under rotation; a diameter pair must lie on opposite rays and therefore shortens. Strict first-order rows stay strict and inactive rows keep slack.

Thus two null bodies cannot be the final C-I obstruction. A survivor needs at least three distinct rigid-body motion classes, or active vertices outside the relevant null-body cover.

## 1. Rigid-body hinge normalization

Let `P,Q` be source-vertex sets with

```math
P\cap Q=\{x\}.
\tag{C59.1}
```

Let a fixed-diameter critical velocity restrict to infinitesimal rigid motions

```math
v(p)=t_P+\omega_PJp\quad(p\in P),
\qquad
v(q)=t_Q+\omega_QJq\quad(q\in Q).
\tag{C59.2}
```

If `omega_P=omega_Q`, equality of the two velocities at the shared vertex `x` gives `t_P=t_Q`; the two restrictions are one rigid motion. Assume instead

```math
\delta:=\omega_P-\omega_Q\ne0.
```

Subtract the global infinitesimal rigid motion of `Q`. Pair-distance derivatives are unchanged. Then

```math
v(q)=0\quad(q\in Q),
\qquad
\boxed{v(p)=\delta J(p-x)\quad(p\in P).}
\tag{C59.3}
```

So the relative motion is exactly rotation about the shared source point `x`.

## 2. Exact finite cross-pair formula

For exclusive endpoints `p in P\setminus\{x\}` and `q in Q\setminus\{x\}`, put

```math
a=p-x,\qquad b=q-x.
```

Rotate `P` through angle `theta` about `x`, keeping `Q` fixed:

```math
p(\theta)=x+R_\theta a.
```

The squared cross distance is

```math
f_{pq}(\theta)
=|a|^2+|b|^2-2(R_\theta a)\cdot b,
\tag{C59.4}
```

with

```math
f'_{pq}(0)=-2(Ja)\cdot b.
\tag{C59.5}
```

Hence zero first variation is equivalent to collinearity of `a` and `b`.

## 3. Stationary unit contacts lengthen

### Lemma C59.1

If

```math
|p-q|=1,
\qquad
f'_{pq}(0)=0,
```

then `p-x` and `q-x` point along the same ray from `x`, and

```math
\boxed{
f_{pq}(\theta)
=1+2|p-x||q-x|(1-\cos\theta)
\ge1.}
\tag{C59.6}
```

It is strict for nonzero sufficiently small `theta`.

#### Proof

Collinearity leaves same or opposite rays. Opposite rays would give

```math
|p-q|=|p-x|+|q-x|\ge2,
```

because both exclusive source points are at least unit distance from `x`. Therefore the rays are the same. Writing the positive radii as `r,s`, one has `|r-s|=1`, and (C59.4) becomes

```math
(r-s)^2+2rs(1-\cos\theta).
```

This is (C59.6). $`\square`$

## 4. Stationary diameter pairs shorten

### Lemma C59.2

If

```math
|p-q|=D,
\qquad
f'_{pq}(0)=0,
```

then `p-x` and `q-x` point along opposite rays from `x`, and

```math
\boxed{
f_{pq}(\theta)
=D^2-2|p-x||q-x|(1-\cos\theta)
\le D^2.}
\tag{C59.7}
```

It is strict for nonzero sufficiently small `theta`.

#### Proof

If the collinear rays were the same, then, because exclusive source points satisfy

```math
1\le|p-x|,|q-x|\le D,
```

one would have

```math
|p-q|=igl||p-x|-|q-x|\bigr|\le D-1<D,
```

a contradiction. Hence the rays are opposite. Their positive radii `r,s` satisfy `r+s=D`, and (C59.4) becomes

```math
(r+s)^2-2rs(1-\cos\theta),
```

which is (C59.7). $`\square`$

## 5. Theorem C59 — finite two-body hinge integration

Assume:

1. every source vertex incident to an active unit or diameter constraint is in `P union Q`;
2. `P cap Q={x}`;
3. `v in ri K_D(A)` restricts to rigid motions on `P,Q`;
4. those rigid motions differ.

Then for all sufficiently small nonzero `theta` of the sign matching the relative angular velocity, the finite rotation of `P` about `x` with `Q` fixed satisfies

```math
|p_i(\theta)-p_j(\theta)|\ge1
\quad\text{for all pairs},
\tag{C59.8}
```

and

```math
\operatorname{diam}A(\theta)=D.
\tag{C59.9}
```

Every weak active row becomes strict. Hence a weak unit contact contradicts contact minimality.

### Proof

Internal distances in each body are preserved exactly. For a cross active row:

- if its signed first variation is strict, the corresponding inequality remains strict for small `theta` of the matching sign;
- if its first variation is zero, Lemma C59.1 handles a unit row and Lemma C59.2 handles a diameter row.

All initially inactive pairs have strict slack in `(1,D)` and retain it after shrinking `theta`. Vertices incident to no active row may be held fixed; their finitely many strict slacks also persist.

A normalized extreme null body carries at least one positive diameter edge. Such an edge is internal to one rigid body, so its length remains exactly `D`; therefore the new diameter is exactly `D`, not merely at most `D`.

Because `v` is relative-interior, every weak active row has strict signed derivative. No weak row can be internal to one rigid body, where its derivative would be zero. Thus every weak row becomes strict. No new contact appears, so a weak unit contact is removed, contradicting contact minimality. $`\square`$

## 6. Exact effect on the C58 bounded-star branch

C58 proves that if two null-face extreme bodies rotate differently, their midpoint positive diameter graph is a degree-at-most-five star forest and every sufficiently large star has a source-preserving one-vertex contact separator.

C59 shows that none of that two-body structure can itself prevent finite release once the active source is covered by the two bodies. The zero-transfer star forest is therefore a necessary electrical signature of pairwise shear, not a two-body higher-order lock.

Any remaining C-I obstruction must have at least one of the following forms:

1. **multi-body pin cycle:** at least three genuinely different rigid-body motions are simultaneously required;
2. **null-face coverage defect:** some active vertex is not contained in the body cover used by the relative-interior release velocity.

## 7. Three-body kinematic identity

The next branch already has an exact first reduction. Let three rigid-motion classes `A,B,C` have distinct angular rates and pairwise shared hinge vertices

```math
x_{AB},\quad x_{BC},\quad x_{CA}.
```

Write their rigid velocity fields as

```math
v_X(p)=t_X+\omega_XJp.
```

Equality of the two body velocities at each shared vertex gives

```math
t_B-t_A=(\omega_A-\omega_B)Jx_{AB},
```

and cyclic analogues. Summing and multiplying by `-J` yields

```math
(\omega_A-\omega_B)x_{AB}
+(\omega_B-\omega_C)x_{BC}
+(\omega_C-\omega_A)x_{CA}=0.
\tag{C59.10}
```

The coefficients sum to zero and are not all zero. Therefore

```math
\boxed{x_{AB},x_{BC},x_{CA}\text{ are collinear}.}
\tag{C59.11}
```

So the next obstruction is not an arbitrary three-body pin triangle: every flexible three-motion triangle has its three actual source hinges on one line.

## 8. Regression and scope

- The unit-square zero-transfer network is not a counterexample: it is one rigid null body, not two one-vertex bodies.
- A two-body one-sum contact network can certainly have zero electrical transfer; C59 does not try to exclude that response. It proves the corresponding mechanical hinge is integrable.
- The proof uses the global source inequalities around the shared source hinge, not generic rigidity.
- C59 does not resolve finite compatibility around three or more rigid bodies.

## 9. Next exact target

### C60 collinear multi-body hinge collapse

Use (C59.11), C58's bounded-star/separator structure for every different-motion pair, and unit-distance geometry to show that three distinct null-body motions cannot coexist in a contact-minimal global minimizer, or that their collinear hinge motion integrates to a same-diameter release.

The strongest useful special case is three bodies whose union covers every active vertex. If that case integrates, the only remaining C-I issue is null-face coverage.

## 10. Compact handoff

**LEVEL I STATUS:** still open.

**C59:** a relative rotation of two rigid source bodies about their single shared source vertex integrates finitely. Stationary cross-body unit contacts lengthen; stationary cross-body diameter pairs shorten. Therefore a two-body null hinge cannot be the final weak-contact obstruction.

**Remaining C-I alternatives:** at least three distinct rigid-body motions, or a null-face active-vertex coverage defect.

**Next:** three distinct motion classes have collinear pairwise source hinges by (C59.10); combine that exact collinearity with C58's bounded zero-transfer star forests.
