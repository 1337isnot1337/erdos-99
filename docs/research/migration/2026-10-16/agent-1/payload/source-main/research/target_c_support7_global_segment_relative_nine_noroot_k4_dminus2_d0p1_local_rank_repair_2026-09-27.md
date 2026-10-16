# Target C: repaired nine-no-root k=4, D=-2, d_root=0, p=1 support closure

Date of source result: 2026-09-27. Source branch: `target-c-nine-k4-dm2-local-rank-repair-20260927`.

**Status:** unreviewed exact support-level candidate for one arithmetic profile. It does not close the other nine-no-root branch, C-II, or Level I.

Companion verifier:
`research/verify_target_c_support7_global_segment_relative_nine_noroot_k4_dminus2_d0p1_local_rank_repair_2026_09_27.cpp`.

## Exact local-rank counterexample

For the triangle block `b={1,2,5}`, take the three distinct tetrahedral supports
`{1,2,3,5}`, `{1,2,4,5}`, and `{1,2,5,6}`. In the exact local quotient coordinates used by the support-seven model, the corresponding quotient vectors are `(-1,1)`, `(-1,1)`, and `(1,0)`. The coefficient rows on the three external coordinates are

```text
(-1, -1, 1)
( 1,  1, 0)
```

and are linearly independent over the rationals. Thus no repeated containing support does not imply local rank one. A repeated containing support still forces rank two.

## Sound support relaxation

The profile has `rank(P)=5`, generalized weights at least `(3,4,6,7,9)`, and at most 20 touched triangle blocks. For an actual-empty block with occurrence set `I_b`, the verifier permits:

- repeated containing support: rank two only, requiring `|I_b|>=4`;
- no repeated support and `|I_b|<3`: no actual-empty assignment;
- no repeated support and `|I_b|=3`: rank one only, since rank two would violate `d_2>=4`;
- no repeated support and `|I_b|>=4`: either rank one or rank two.

For chosen local dimensions, it imposes only the necessary generalized-weight pair conditions:

- line-line: intersection size at least 3, or union size at least 4;
- plane-line: intersection size at least 3, or union size at least 6;
- plane-plane: intersection size at least 4, or intersection at least 3 and union at least 6, or union at least 7.

The selected singleton is relaxed: if touched its local line may vanish; otherwise it may be any line supported in its occurrence set. Complete-root row independence and `rank(H(T))-rank(H(C))>=4` are enforced. Replacing actual coordinate supports by occurrence sets and forgetting orientations only enlarges the search.

## Exact finite computation

The verifier checks the independent Burnside orbit counts and canonical augmentation for support multisets of sizes zero through nine. It reports:

- raw legal size-nine extensions: `966977`;
- raw extensions with `h<=20`: `239349`;
- size-nine S7 orbits with `h<=20`: `33920`;
- relaxed dimension assignments reaching the final profile test: `2166`;
- support-level survivors: `0`.

Support/orbit decisions are exact integer combinatorics. Triangle-row ranks are computed modulo `2^31-1`; the verifier checks this Mersenne prime by Lucas-Lehmer. The Hadamard bound `(2^31-1)^2 > 3^15` makes these ranks exact over the rationals for rows of squared norm three and rank at most fifteen.

The zero-survivor result excludes actual states in this one profile, conditional on the stated support-seven reductions. It is not a canonical theorem or a geometric realization result.
