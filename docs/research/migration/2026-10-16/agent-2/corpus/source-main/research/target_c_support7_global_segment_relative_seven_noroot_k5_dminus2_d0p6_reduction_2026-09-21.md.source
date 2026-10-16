# Target C: reduce seven-no-root `D=-2,k=5,d=0,p=6`

Date: 2026-09-21

Status: rigorous reduction, not yet a branch closure.

A hypothetical seven-no-root state in

`D=-2, k=5, d=0, p=6`

has a rank-two coefficient-constraint space `P <= Q^7`. The all-depth deletion theorem for defect `-2` says that every one- and two-coordinate puncture preserves `rank(P)=2`. Combining that synchronization with the six-row `k=4` containment theorem and the exact deficiency-one singleton-capacity censuses forces a much narrower state:

- every one-row deletion has six-row virtual canonical deficiency exactly two and `q=6`;
- therefore the six incomplete root rows of the seven-row state are six singleton blocks, and all six replace virtual-canonical complete blocks in every one-row deletion;
- every singleton block is touched by at least two of the seven no-root rows;
- every two-row deletion has five-row virtual canonical deficiency exactly two and at least five of the six singleton blocks replace virtual-canonical complete blocks.

The remaining finite obstruction is therefore an exact synchronized six-row `d=2` singleton-capacity problem, rather than an unrestricted seven-row `p=6` search.

Companion arithmetic checker:

`research/verify_target_c_support7_global_segment_relative_seven_noroot_k5_dminus2_d0p6_reduction_2026_09_21.py`

Companion exact finite-search scaffold:

`research/verify_target_c_support7_global_segment_relative_six_noroot_k4_d2_singleton_capacity_2026_09_21.py`

## One-row deletion forces `d_6=2,q_6=6`

Let `B` be a hypothetical seven-row state in the branch. Since `D(B)=-2`, the established all-depth deletion identity and the closed at-most-six-no-root theorem imply that deleting one or two no-root rows cannot lower the quotient rank. Thus each one-row deletion has six no-root rows, rank-two coefficient space, and every further coordinate deletion still has rank two.

For any one-row deletion `B_i`, the exact defect transport identity gives

`D(B_i)=0`.

The root-row set is unchanged by deleting a no-root row, so its incomplete-root cost is still

`p=6`.

Apply the synchronized six-row `k=4` containment theorem. If `d_6` is virtual canonical complete-block deficiency and `q_6` is the number of virtual-canonical complete blocks changed to incomplete states, then

`0 = D(B_i) >= 6 + 6 + 3 d_6 - 3 q_6`,

with `d_6>=1` and `q_6<=6`.

Before using any capacity information, the only possibilities are

```text
d_6   q_6
 1     5
 1     6
 2     6
```

The first two are impossible from the already certified deficiency-one singleton-capacity obstruction. Every synchronized six-row `d=1` virtual state has at most three canonical-complete blocks admitting any compatible singleton.

If `(d_6,q_6)=(1,5)`, five canonical-complete blocks are changed to nonempty incomplete states with total incomplete cost six. Each such replacement costs one row if it is a singleton and two if it is a pair. Therefore at least four of those five replacements are singletons. That requires at least four singleton-compatible canonical-complete blocks, but the exact maximum is three.

If `(d_6,q_6)=(1,6)`, total cost six forces all six replacements to be singletons, again impossible.

Hence every one-row deletion satisfies

`d_6=2, q_6=6`.

Since the total incomplete cost is six, `q_6=6` also forces the actual seven-row incomplete part to consist of exactly six singleton blocks. There is no pair block and no additional incomplete block. Each of those six singleton blocks is virtual-canonical complete in every one-row deletion.

A singleton block cannot be touched by only one of the seven no-root rows: deleting its unique touching row would make it untouched in the six-row shadow, so its empty local constraint would be zero and it would be virtual-canonical empty, contradicting `q_6=6`. Thus each singleton has no-root touch multiplicity at least two.

## Two-row deletion forces `d_5=2,q_5>=5`

Delete any coordinate pair. The same defect transport identity gives

`D(B_{ij})=2`.

Its coefficient space still has rank two, so this is a five-no-root `k=3` shadow. Its incomplete-root cost remains six before stripping untouched root rows.

Choose either of the two deleted coordinates first. The resulting synchronized six-row shadow has `d_6=2`. The five-row virtual canonical complete set is contained in the six-row one, so row-nullity monotonicity gives

`d_5<=2`.

The repaired five-row `k=3` theorem gives `d_5>=1` and

`2 >= 5 + 6 + 3 d_5 - 3 q_5`,

where `q_5<=6`.

If `d_5=1`, this inequality requires `q_5>=4`. But all actual incomplete blocks are already known to be singletons, so this would require at least four canonical-complete blocks admitting their compatible singleton state. The exact five-row deficiency-one capacity census has maximum three. Hence `d_5=1` is impossible.

Therefore every pair deletion has

`d_5=2`.

Substituting this into the containment inequality gives

`q_5>=5`.

Thus in every pair deletion at most one of the six actual singleton blocks can be virtual-canonical empty.

## Exact finite bottleneck

The branch is now reduced to the following finite question:

> Can a synchronized six-no-root rank-two coefficient plane of virtual deficiency two contain six singleton-compatible canonical-complete blocks such that, after each of its six coordinate deletions, the projected virtual deficiency is still two and at least five of those same six blocks remain virtual-canonical complete?

The new verifier starts only from repaired five-row `d=2` rank-two parents with at least five singleton-compatible canonical-complete blocks. This is an exhaustive cover for the reduced branch: every coordinate deletion of a hypothetical six-row shadow has exactly those two properties. It augments each parent by every sixth no-root row, enumerates every rank-two six-row plane projecting to that parent, enforces synchronization and `d_6=2`, and finally searches for a common six-block set satisfying the five-of-six condition in all six projected shadows. This is substantially smaller than scanning every five-row `d=1` or `d=2` parent.

The exact census has not been completed in this run. A GitHub Actions attempt could not execute: all matrix jobs failed before any workflow steps were reported, and no usable job logs were produced. This is not mathematical evidence in either direction. The failing workflow was removed; the exact verifier remains committed for a later runner-backed execution.

No branch closure is claimed here.
