# Target C: direct global fixed-basis lift for the remaining `k=6, D=-1` Profile A

Date: 2026-09-22

Status: proved a stronger global consistency condition and implemented it as an exact rational lift audit. No closure is claimed until the finite cover executes.

Companion verifier:

`research/verify_target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_profile_a_global_fixed_basis_2026_09_22.py`

## 1. Global Profile A is an eight-class basis

The only remaining deficiency-two global profile is

```text
d_8 = 2,
q = 8,
seven singleton replacements + one pair replacement.
```

The rank-two replacement-functional quotient has dimension

```text
s_8 = 8 - 2 + 2 = 8.
```

The eight actual replacement classes span this quotient, so they are a basis.

Choose one of the guaranteed three-clean external coordinates and delete it. The committed reduction forces the resulting seven-row state to have

```text
d_7 = 2,
s_7 = 7,
```

with the descended actual replacements spanning the quotient. The unique pair must survive this puncture: if it disappeared, only singleton replacements would span the seven-dimensional quotient, contradicting the already-proved nonexistence of a depth-two-synchronized seven-row `d=2` full-singleton state.

Delete any further coordinate. Every resulting six-row state is synchronized and the committed Profile A reduction forces

```text
d_6 = 2,
s_6 = 6,
exactly five surviving singleton replacement blocks,
the same pair block surviving,
```

with those six actual classes spanning the quotient. A further puncture has `d_5=2` and quotient dimension five.

Thus an actual global Profile A realization supplies one fixed eight-class basis whose images have exact ranks

```text
8 -> 7 -> 6 -> 5
```

through the selected clean puncture fan.

## 2. Why the six-row audit is an exhaustive seed

After deleting the chosen three-clean coordinate and any second coordinate, the actual state is one of the synchronized six-row `d=2` Profile A states covered by the corrected 20,451-orbit audit. Its five surviving singleton blocks are exactly the five singleton-compatible complete blocks of that six-row state, and the actual pair block is one of the pair candidates already checked there.

Conversely, to test whether such a six-row candidate could arise globally, restore one row and enumerate every realizable rank-two coefficient plane that projects to the fixed six-row plane. The rank-two local-basis argument used by the established six-row extension engine is exhaustive: a realizable rank-two plane has a basis supplied either by one rank-two local constraint or by rank-one local constraints on two distinct blocks. Applying the same construction again restores the eighth row.

The seven-row lift is required to be the clean shadow: every one- and two-coordinate puncture retains coefficient rank two, and its virtual deficiency is two. At eight rows every one-coordinate puncture retains coefficient rank two and the virtual deficiency is two.

## 3. Reconstructing the two missing global singleton blocks

The six-row seed has exactly five actual singleton blocks. The global profile has seven. Therefore every genuine lift is obtained by adjoining exactly two further global singleton blocks.

For each eight-row coefficient plane the verifier lists every virtual-complete block with a compatible singleton state. Singleton compatibility on a virtual-complete block is unique, so the states of the five seed blocks are forced to agree with their eight-row states. It then chooses every pair of additional singleton-compatible blocks distinct from the pair block.

This produces a candidate fixed global replacement set

```text
seven singleton block/state pairs + one fixed pair block/state.
```

No independent state choices are allowed after puncturing. Each replacement class descends with the same local state when its block remains virtual-complete and maps to zero otherwise.

## 4. Structural filters from basis loss

Because the eight global classes form a basis, the selected puncture maps give immediate loss bounds.

At seven rows the quotient dimension is seven, so at most one of the eight basis blocks can disappear.

At six rows the committed exact Profile A form is stronger than the dimension bound: in every one-coordinate deletion of the clean seven-row state, the pair survives and exactly five of the seven global singleton blocks survive. The verifier imposes this exact count in all seven six-row shadows.

At five rows the quotient dimension is five, so at most three of the eight global basis blocks can disappear in any of the 21 distinct double punctures of the clean seven-row state.

These are only cheap necessary filters. Surviving block counts do not by themselves guarantee the required quotient ranks.

## 5. Exact fixed-basis rank test

For every structurally eligible global eight-block set, the verifier reconstructs the canonical relation space and replacement functionals and requires exact rational extra rank

```text
8 at the global eight-row state,
7 at the selected clean seven-row state,
6 in each of its seven six-row punctures,
5 in each of its 21 five-row double punctures.
```

All of these new decisions use direct `Fraction` elimination over `Q`. The five singleton states and pair state inherited from the six-row seed are kept fixed throughout. The 42 ordered two-step punctures of the clean seven-row state are deduplicated to the 21 underlying five-row states before exact reranking.

The wrapper is installed on top of the already strengthened six-row common-basis audit, so a pair state is considered for global lifting only after the same six source classes have already been shown to span every five-row puncture of the seed state.

## 6. Consequence of a zero full cover

Every genuine Profile A realization has at least one three-clean coordinate. Choosing such a coordinate and any second deletion produces a six-row seed covered by the base audit, and the two exact lift stages reconstruct its original seven- and eight-row coefficient planes. Its actual seven singleton blocks and pair block then satisfy every fixed-basis condition above.

Therefore a complete 20,451-orbit execution with zero global fixed-basis survivors excludes Profile A rigorously.

This does not yet close Profile A because the runner infrastructure has not executed the finite cover. The remaining task is execution, not another local consistency gap in the selected `8 -> 7 -> 6 -> 5` fan.
