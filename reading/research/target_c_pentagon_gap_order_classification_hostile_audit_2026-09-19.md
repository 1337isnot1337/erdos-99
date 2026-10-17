> Generated reading edition · [exact source](../../research/target_c_pentagon_gap_order_classification_hostile_audit_2026-09-19.md) · source SHA-256 `d96dd3b83af222129c89d49141a03b8176581dd31cc5a07159d856e61036e4c4`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "a9f5ca10ce37ae22e83033e28d1a1ea613fb91e4", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_pentagon_gap_order_classification_hostile_audit_2026-09-19.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "470d2a8b7b78b8afcfc0230d8d652fe9f602becc0cbc6d30342f00ae8a642a56"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — physical pentagon gap-order classification

**Date:** 2026-09-19  
**Audited source:** `research/target_c_pentagon_gap_order_classification_2026-09-19.md`  
**Certificate:** `research/verify_target_c_pentagon_gap_order_2026_09_19.py`  
**Verdict:** PASS at the stated local scope  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The audited claim is local: the consecutive direction gaps of any strict closed equilateral force pentagon obey five cyclic sign/equality constraints, which leave ten strict order types and a completely classified equality boundary. This audit does not claim that those ten order cones are sufficient for force closure, and it does not eliminate a support-seven reciprocal orbit by itself.

## 1. Closure-to-cosine identities

Let the unit directions be `u_0,...,u_4` in cyclic order with gaps `T,A,B,D,E`. From

$$
u_4+u_0+u_1=-(u_2+u_3),
$$

squared norms give

$$
3+2\{\cos E+\cos T+\cos(E+T)\}
=2+2\cos B,
$$

hence

$$
\cos B=\frac12+\cos E+\cos T+\cos(E+T).
$$

Likewise

$$
u_0+u_1+u_2=-(u_3+u_4)
$$

gives

$$
\cos D=\frac12+\cos T+\cos A+\cos(T+A).
$$

So the two identities used by the source have the correct constants and pairings.

## 2. Monotonicity has the correct sign and branch

For fixed `T`, write

$$
R_T(z)=\frac12+\cos T+\cos z+\cos(T+z).
$$

Then

$$
R_T'(z)
=-\sin z-\sin(T+z)
=-2\cos(T/2)\sin(z+T/2).
$$

The physical pentagon bounds give `0<T<2pi/3`, so `cos(T/2)>0`. They also give `T+A<pi` and `T+E<pi`. Every `z` between `A` and `E` therefore satisfies

$$
0<z+T/2<\pi.
$$

Thus `R_T'(z)<0` on the entire interval used in the comparison.

At the endpoints, `R_T(E)=cos B` and `R_T(A)=cos D`, with physical `0<B,D<2pi/3`. Hence both endpoint values lie strictly in `(-1,1)`. Since `R_T` is monotone, its whole interval image lies between those endpoint values, so there is no hidden arccos domain or branch failure. Therefore

$$
f_T(z)=\arccos R_T(z)
$$

is real and strictly increasing. The source's conclusion

$$
\operatorname{sgn}(A-E)=\operatorname{sgn}(D-B)
$$

has the correct direction. In particular equality is biconditional, not merely one-way.

## 3. Cyclic indexing check

With `(T,A,B,D,E)=(x_k,x_{k+1},x_{k+2},x_{k+3},x_{k-1})`, the preceding relation becomes

$$
\operatorname{sgn}(x_{k+1}-x_{k-1})
=
\operatorname{sgn}(x_{k+3}-x_{k+2}),
$$

exactly as stated. Rotating `k` gives five constraints; no reflection convention or reciprocal-edge sign enters this local lemma.

## 4. Finite classification check

The verifier enumerates all `120` strict permutations of five labelled gaps. Exactly ten satisfy all five sign constraints. It independently checks that these ten form one full dihedral orbit and that the canonical cyclic rank vector is

$$
(1,5,2,3,4).
$$

The minimum/maximum adjacency corollary is checked directly on all ten orders.

For equality cases the verifier does not assume that a weak order is the limit of a strict admissible order. It first enumerates all `541` ordered set partitions on five labelled entries and applies the three-valued sign relation directly. Exactly `21` survive, with number-of-level distribution

$$
10\text{ with five levels},
\qquad
10\text{ with three levels},
\qquad
1\text{ with one level}.
$$

So the claims that two-level and four-level cases are impossible do not come from a genericity argument.

The verifier then separately checks that every surviving weak order is a coarsening of at least one of the ten strict orders. This justifies the closed-cone statement: the union of the ten closed strict-order cones really covers all equality cases.

## 5. Three-level structure check

Every three-level weak order has multiplicities `1+2+2`, and the singleton rank is always an extreme rank. The ten patterns split into two five-element dihedral orbits according to whether the singleton is the minimum or maximum. Representatives in cyclic `(T,A,B,D,E)` coordinates are

$$
(0,2,1,1,2)
\quad\text{and}\quad
(2,0,1,1,0).
$$

Thus a nonregular equality case can be relabelled as

$$
A=E,\qquad B=D,
$$

with exactly one of

$$
T<B=D<A=E
$$

or

$$
A=E<B=D<T.
$$

## 6. Equality-wall parameterization

Under `A=E`, strict monotonicity gives `B=D`. Put `gamma=A+T/2`. The turn sum gives `B=pi-gamma`. Substitution into the exact cosine identity gives

$$
-\cos\gamma
=\frac12+\cos T+2\cos\gamma\cos(T/2).
$$

Writing `c=cos(T/2)` and `cos T=2c^2-1` yields

$$
-(1+2c)\cos\gamma=2c^2-\frac12.
$$

Since `c>0`, division by `1+2c` is safe, and factorization gives

$$
\cos\gamma=\frac12-c.
$$

The source parameterization follows. Because `0<gamma<pi`, the principal `arccos` is the correct branch.

At the all-equal point the sum forces each gap to be `2pi/5`. Conversely, if the singleton `T` in a three-level pattern were the maximum while `T<2pi/5`, the sum would be strictly less than `5T<2pi`; if it were the minimum while `T>2pi/5`, the sum would be strictly greater than `5T>2pi`. This validates the source's ordering on the two sides of the regular point.

## 7. Scope guard

The new order theorem is necessary, not sufficient. The ten cones still contain many nonphysical turn vectors because they omit the actual trigonometric force-closure equations. It is valid to use them as a rigorous subdivision or pruning layer in the remaining `H7b`/`H8` work, but invalid to call a reciprocal orbit realizable merely because one cone survives its affine constraints.

No claim is made here about the reciprocal-collinearity walls, `H7a`, `H6`, or direct elimination of the twelve current convex `H8` orbits. C-II remains open.
