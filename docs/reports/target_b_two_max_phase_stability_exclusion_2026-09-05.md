<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "c6b3e504cfdc211d1af85c8bc46124e95d6197a6", "source_canonical": false, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "unreviewed", "source_path": "docs/reports/target_b_two_max_phase_stability_exclusion_2026-09-05.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "ffc992d0bda71d5f1ae457384f8a396e1ddfe0c6f03812ae53909584181bcca9"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle was `unreviewed`; it is retained as provenance only. Destination status remains unreviewed/noncanonical.

# Erdős Problem #99 — Target B two-largest-tie phase stability exclusion

**Date:** 2026-09-05  
**Run type:** new ordered stability closure  
**Target:** remaining near-saturated coherent three-phase class-size regime  
**Depends on:** balanced phase stability exclusion; unique-max interval extraction; trimmed-grid phase-star exclusion  
**LEVEL I STATUS:** STILL OPEN

## 1. Purpose

The unique-max stability theorem excludes every near-saturated coherent three-phase core whose largest class is separated by a fixed fraction from the other two. The remaining class-size regime has two asymptotically largest classes.

This report closes that regime.

Let the coherent phase classes have sizes

`|A|=|B|=M`, `|C|=a<=M`.

The Theorem-51 extremal bound is

`E<=M(M+a)`.

Assume

`E=M(M+a)-o(M^2)`

and that the coherent core carries all but `o(M^2)` of the quadratic rhombus crossings.

Then no sufficiently large pure-rhombic global minimizer can realize this endpoint.

## 2. Stability algebra when the third class has a fixed gap

Write

`e_AB=M^2-x`,

`e_AC=Ma-y`,

`e_BC=z`.

Thus

`E=M(M+a)-x-y+z`.

Every transversal triple contains at most two crossing edges. Counting triples gives

`a e_AB + M e_AC + M e_BC <= 2M^2 a`.

Substitute the three edge counts:

`a(M^2-x)+M(Ma-y)+Mz <= 2M^2a`.

After cancellation,

`Mz<=ax+My`.

Put

`s=a/M`.

Then

`z<=s x+y`.

The extremal deficit is

`delta:=M(M+a)-E=x+y-z`.

Therefore

### Lemma TM1 — tied-max deficit controls the largest-pair nonedges

`delta >= (1-s)x`.

Consequently, if for some fixed `kappa>0`

`s<=1-kappa`

and `delta=o(M^2)`, then

`x=o(M^2)`.

So the `A`–`B` pair is `1-o(1)` complete.

## 3. Extract a complete `M-o(M)` grid

The coherent classes `A,B` are each pairwise noncrossing. Every train of `B` therefore crosses a consecutive interval of the ordered `A` family.

By the audited interval-bigraph extraction theorem, `x=o(M^2)` yields subfamilies

`A' subset A`, `B' subset B`

with

`|A'|=M-o(M)`,

`|B'|=M-o(M)`

such that every `A'` train crosses every `B'` train.

The third coherent class `C` is allowed to contribute arbitrary signed displacement in its coherent projective direction, of total magnitude at most `a+o(M)`. The trimmed-grid theorem already optimizes over exactly this worst cancellation.

For the extracted grid,

`t=|B'|/|A'|=1-o(1)`,

`s=a/M<=1-kappa+o(1)`.

At the tied value `t=1`, the trimmed-grid constrained minimum satisfies

`F(s,1)=3`

for every `0<=s<=1`.

Therefore

`D^2 >= (3-o(1))M^2`.

On the other hand near saturation gives

`R=(1+s+o(1))M^2`,

and `T=O(M)`, so

`n=(1+s+o(1))M^2`.

The strict translated-lattice comparison gives

`D(n)^2 < (c(1+s)+o(1))M^2`,

where

`c=2sqrt(3)/pi`.

Since `s<=1`,

`c(1+s)<=2c=4sqrt(3)/pi=2.2053155817...<3`.

Contradiction.

### Corollary TM2 — fixed-gap two-max endpoint is impossible

For every fixed `kappa>0`, no near-saturated coherent endpoint with

`|A|=|B|=M`, `|C|<= (1-kappa)M`

survives.

## 4. Asymptotically balanced third class

It remains to treat

`a/M ->1`.

Put

`m=a`.

Then

`M-m=o(M)`.

Delete any `M-m` trains from `A` and any `M-m` trains from `B`, leaving equal-size classes

`A_0,B_0,C`

of size `m`.

Deleting those `o(M)` trains removes at most `o(M^2)` crossing edges. Hence the induced equal-size tripartite graph has

`E_0 >= E-o(M^2)`.

But

`E=M(M+m)-o(M^2)`

and

`M(M+m)-2m^2=(M-m)(M+2m)=o(M^2)`.

Since `m~M`, it follows that

`E_0=(2-o(1))m^2`.

The balanced stability theorem now gives a pair among `A_0,B_0,C` with only `o(m^2)` missing crossings. Ordered interval extraction gives a complete

`(m-o(m)) x (m-o(m))`

grid.

The `o(M)` deleted trains contribute at most `o(m)` directly to any selected train-coordinate diagonal, so they can be absorbed into the external error in the trimmed-grid theorem. The remaining non-core crossing error is `o(m^2)` by hypothesis.

Therefore the balanced trimmed-grid argument gives

`D^2 >= (3-o(1))m^2`.

Meanwhile

`R=E+o(M^2)=(2-o(1))m^2`,

so

`n=(2-o(1))m^2`

and the lattice comparison gives

`D^2<(2c+o(1))m^2<3m^2`,

again a contradiction.

### Corollary TM3 — asymptotically balanced two-max endpoint is impossible

No near-saturated coherent endpoint with

`|A|=|B|=M`, `|C|/M->1`

survives.

## 5. Full two-max closure

Any sequence with two equal largest class sizes has a subsequence on which either

1. `a/M<=1-kappa` for some fixed `kappa>0`, or
2. `a/M->1`.

TM2 excludes the first case and TM3 excludes the second.

### Theorem TM4 — two-largest-tie endpoint exclusion

No sufficiently large pure-rhombic global-minimizer sequence can have a coherent three-phase core with

`|A|=|B|=M>=|C|`,

`E=M(M+|C|)-o(M^2)`,

and only `o(M^2)` quadratic crossings outside that coherent core.

Combined with the audited unique-max stability theorem, **every class-size regime of a near-saturated coherent Theorem-51 phase core is now excluded**.

## 6. Exact remaining Target B gate

The class-size/equality endpoint is no longer the obstruction.

The remaining Target B task is upstream:

> prove that every surviving pure-rhombic global-minimizer branch reaching the dense coherent three-phase reduction is sufficiently close to the Theorem-51 crossing upper bound, with the `o(D^2)` pruning and boundary-order errors controlled strongly enough to invoke the stability exclusions above.

Equivalently, future work should target the **near-saturation transfer**, not further classify equality phase stars.
