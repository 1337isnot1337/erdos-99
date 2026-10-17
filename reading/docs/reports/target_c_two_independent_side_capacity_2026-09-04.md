> Generated reading edition · [exact source](../../../docs/reports/target_c_two_independent_side_capacity_2026-09-04.md) · source SHA-256 `e4f023a63a4cd6ce08edd6ee35ecc5a7659d79c89cbba8f685ed88fd05463f5b`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-7E0799EF0D13","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C two independent side capacities

**Date:** 2026-09-04  
**Branch:** `research/target-c-c97-caterpillar-fan-capacity-2026-09-04`  
**Run type:** audited replacement for the retracted cross-wall argument  
**Target:** pure-rhombic C80-C96 chain-face branch  
**Status:** LEVEL I STILL OPEN

## 1. Result

The two C90 boundary sides cannot be combined into one Cartesian train block. They can, however, be bounded independently. Combining those two valid one-side capacities with the exact three-phase train-orbit bookkeeping gives:

### Theorem TS1 — audited train surplus

Every asymptotic canonical pure-rhombic C80-C96 chain-face survivor satisfies

`liminf T/D > 2.9328`.

The proof never forms a Cartesian rectangle containing trains from both boundary sides.

Write

`Delta=pi/(2sqrt(3))`.

## 2. One boundary side, with both residual phases mixed

Fix one of the two C90 boundary arcs `L,U`. Let `aD+o(D)` chain-neighbor residual trains have both terminals on this side.

For a residual train `sigma`, let `J_sigma` be its consecutive interval of exact chain trains `P` crossed by `sigma`.

Call a row short if

`|J_sigma|<=D/2`

and long otherwise.

Any two long rows on the same side have overlapping `P` intervals, hence share an exact chain train. If the two residual trains crossed each other, those three trains would form a triangle in the C77 train-intersection graph. Thus the two residual trains do not cross. Their same-side boundary caps are therefore nested, because two disjoint cap intervals could not both contain more than half of the ordered `P` terminals.

Orient each same-side residual train into its boundary cap. C77 crossing orientation then gives one common sign of transverse projection against the exact chain direction `u`. Every actual train crossing has acute projective angle strictly greater than `pi/3`, so for every such residual unit vector `v`,

`|Ju dot v|>sqrt(3)/2`.

Take the first `j` long rows in nested order. They cross a common interval of `d_j` consecutive exact chain trains. This is exactly the one-side C91 Cartesian translation stack, so the four source corners have displacements

`U=d_j u`,

`V=sum_(k=1)^j v_k`.

Hence

`|V|>(sqrt(3)/2)j`.

Both parallelogram diagonals are source differences of length at most `D`, giving

`d_j^2+3j^2/4<D^2`.

Thus a one-side long-wall population `ell D+o(D)` carries at most

`G(ell)D^2+o(D^2)`

exact-chain crossings, where

`G(z)=integral_0^z sqrt(1-3t^2/4) dt`.

A short row contributes at most `D/2` crossings. Since

`G'(z)=sqrt(1-3z^2/4)>1/2`

for `0<=z<1`, replacing short-row population by long-row population can only increase the upper bound. Therefore:

### Lemma TS2 — full one-side capacity

Any side population `aD+o(D)`, with arbitrary mixture of the two residual `+-pi/3` phases, contributes at most

`G(a)D^2+o(D^2)`

crossings with the exact chain family `P`.

## 3. Opposite-side trains do not cross

Let `sigma` have both terminals in the interior of `L`, and `rho` both terminals in the interior of `U`. Their four boundary endpoints do not alternate. Proper arcs in a disk therefore have even mod-two intersection number. C77 says two trains cross at most once. Hence they do not cross.

### Lemma TS3 — side localization

A non-chain `L` train and a non-chain `U` train never cross.

This lemma is used only for phase-orbit bad-crossing bookkeeping; it is **not** used to form a cross-side Cartesian block.

## 4. Phase-orbit bookkeeping with an exact-chain center

Pass to a subsequence with

`x=T/D<3`,

`r=x-2<1`.

C87 gives `q/D>=2+o(1)`. The exposed-hull atomic-mass bound used in C92 then implies that the total limiting atomic train population outside the exact `D` chain trains `P` is at most

`rD+o(D)`.

Positive-density train crossings occur only between projective phases differing by `pi/3`, so the limiting phase graph splits into three-point phase orbits.

Consider the orbit containing the exact chain direction `A`. Let `S` be the residual phase population adjacent to `A` in the phase-support graph. Split `S` by boundary side, with populations

`lambda D+o(D)`, `mu D+o(D)`,

where `lambda>=mu>=0`.

All other atomic population, including extra chain-parallel `A` trains, a possible third vertex of an `A-B-C` path, and atoms in other phase orbits, has total at most

`qD+o(D)`,

where

`lambda+mu+q<=r`.

By Lemma TS2, crossings from the exact `P` trains to `S` contribute at most

`[G(lambda)+G(mu)]D^2+o(D^2)`.

Inside the chain three-phase orbit, triangle-freeness leaves only a star or a path. In either case, after removing the exact `P` contribution, every remaining chain-orbit edge incident to `S` can be charged to a complement train on the **same boundary side**. If `yD` of the complement is placed in this orbit, Lemma TS3 bounds that contribution by

`lambda y D^2+o(D^2)`.

The remaining `(q-y)D+o(D)` atomic population lies in other three-point phase orbits. Weighted Mantel gives at most

`(q-y)^2D^2/4+o(D^2)`

crossings there.

The function

`lambda y+(q-y)^2/4`

is convex in `y`, so its maximum on `[0,q]` occurs at an endpoint. Therefore the total leading rhombus crossing coefficient obeys

### Lemma TS4 — two-side phase capacity

`Delta <= G(lambda)+G(mu)+max(lambda q,q^2/4)`

with

`lambda>=mu>=0`, `lambda+mu+q<=r`.

## 5. Reduce to one scalar upper relaxation

Put

`s=lambda+mu`.

The function `G` is concave, so

`G(lambda)+G(mu)<=2G(s/2)`.

Also `lambda<=s`. For fixed `s`, the bad term increases with the available complement population, so replace `q` by `r-s`. Every survivor must therefore satisfy, for some `0<=s<=r`,

`Delta <= 2G(s/2)+max(s(r-s),(r-s)^2/4)`.

This relaxation deliberately discards side imbalance information; it remains an upper bound.

## 6. Algebraic upper polynomial

For `0<=z<=1`,

`sqrt(1-z)<=1-z/2-z^2/8-z^3/16`.

Indeed the right side is nonnegative and its square minus `1-z` equals

`z^4(z^2+4z+20)/256>=0`.

Apply this with `z=3t^2/4` and integrate. For `0<=s<1`,

`2G(s/2) <= P(s)`

where

`P(s)=s-s^3/32-9s^5/10240-27s^7/458752`.

Thus it is enough to bound

`H_r(s)=P(s)+max(s(r-s),(r-s)^2/4)`.

The two bad terms are equal at `s=r/5`.

For `0<=s<=r/5`,

`H_r(s)=P(s)+(r-s)^2/4`.

Its derivative is positive throughout `r<=0.9328`: the negative polynomial corrections are tiny on `s<=0.18656`, while the leading derivative is at least `1-r/2>0.53`. Hence this branch is increasing up to `s=r/5`.

For `r/5<=s<=r`,

`H_r(s)=P(s)+rs-s^2`.

Its second derivative is strictly below `-2`, so this branch is strictly concave.

For fixed `s`, the original maximum bad term is nondecreasing in `r`; hence it suffices to check

`r=0.9328`.

At this value the concave second branch has its unique critical point between

`0.92459` and `0.92460`:

`H'_(0.9328)(0.92459)>0`,

`H'_(0.9328)(0.92460)<0`.

Direct rational-decimal evaluation of the displayed polynomial gives

`H_(0.9328)(0.92459)<0.906852986`,

and

`H'_(0.9328)(0.92459)<0.000008`.

Concavity therefore bounds the true maximum over the remaining interval of length `0.00001` by

`0.906852986+8*10^(-11)<0.906852987`.

The first branch is smaller because it is increasing only to the common switch value at `s=r/5`, far below this maximum.

Finally the elementary decimal bounds

`pi>3.1415926`, `sqrt(3)<1.7320509`

give

`Delta>0.9068996`.

Thus

`max_(0<=s<=0.9328) H_(0.9328)(s)<0.906852987<Delta`,

a contradiction.

Therefore no asymptotic survivor has `r<=0.9328`, i.e.

`T/D<=2.9328`.

This proves Theorem TS1.

## 7. Frontier

The audited low-train window is now

`2.9328 < T/D < 3`.

This replaces the retracted cross-wall constants. The gap to `3` is about `0.0672D`. Closing it requires genuinely new geometry: the two side walls must remain independent unless a valid cross-side realization theorem is proved.
