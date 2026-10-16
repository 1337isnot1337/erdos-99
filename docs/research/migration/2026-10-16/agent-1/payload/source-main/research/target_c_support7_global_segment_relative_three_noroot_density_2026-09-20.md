# Target C: rank-density barrier through three no-root four-cycles

Date: 2026-09-20

Status: exact finite result for the global four-cycle metric-basis subproblem. This does not reduce the current 3,874-state generic-H6 endpoint and does not close C-II.

The companion verifier is

`research/verify_target_c_support7_global_segment_relative_three_noroot_density_2026_09_20.py`.

## Statement

Use the notation of the relative four-cycle normal-form audit. Let `M` be the 85-dimensional four-cycle span modulo the 56 automatic side-triangle rows, let `T` be the 15-dimensional ground-root star space, let `Q=M/T`, and put

`delta(A) = r_M(A) - r_Q(A)`.

The previous verifier proved

`3 delta(A) <= |A|`

for every four-cycle family containing at most two cycles that avoid root `0`.

The new verifier proves the same inequality for every family containing exactly three no-root cycles. Therefore

> If `A` contains at most three four-cycles avoiding root `0`, then

> `3 delta(A) <= |A|`.

A sufficient family has `delta(A)=15`, so any sufficient family with at most three no-root cycles has at least 45 rows. Consequently:

> Every hypothetical sufficient 44-cycle family contains at least four no-root four-cycles.

Since the committed 45-cycle family `F` contains only root-0 cycles, those four no-root cycles are necessarily outsiders relative to `F`. Combined with the previously certified seven-exchange barrier, any hypothetical sufficient 44-cycle replacement still needs at least eight outsiders, now with at least four of them no-root.

This is not yet a proof that 45 is globally minimal. Families containing four or more no-root cycles remain untreated by this density result.

## Exact coordinate model

The verifier independently rebuilds the same exact model used by the two-no-root audit:

- 210 simple `K8` four-cycle rows in the 168-edge `L(K8)` chain space;
- quotient by the 56 automatic side-triangle rows;
- exact ranks `r_M=85`, `dim T=15`, and `r_Q=70`;
- 35 root-0 quotient blocks, each with local form `(1,0)`, `(0,1)`, `(1,-1)`; and
- 105 no-root four-cycles, each supported on exactly four local quotient blocks.

All coordinate construction is exact over `Fraction`. The resulting `M` and `Q` coordinates are integral.

## Reduction for three no-root cycles

Fix three no-root rows. The `C(105,3)=187460` unordered triples split into exactly 77 orbits under relabeling by `S_7`. Their touched-block counts range from 4 through 12, with distribution

```text
4: 1 orbit
7: 2 orbits
8: 5 orbits
9: 6 orbits
10: 13 orbits
11: 31 orbits
12: 19 orbits
```

As in the two-no-root proof, untouched incomplete root-0 blocks cannot participate in a quotient relation, while an untouched complete block costs three rows and contributes at most one relative direction. They can therefore be stripped from the hard part without weakening the factor-three inequality.

Inside the touched blocks, let

- `c` be the number of complete root-0 blocks,
- `p` be the number of root-0 rows selected in incomplete blocks, and
- `k` be the extra `Q`-kernel dimension supplied by the three no-root rows after quotienting by the selected root-0 spans.

Then

`n = 3 + 3c + p`,

while the total `Q`-kernel dimension is `c+k`. Since `delta<=c+k`,

`n - 3 delta >= 3 + p - 3k`.

If this crude lower bound is nonnegative, the desired inequality is already proved. Only negative crude-defect states require the exact `T`-rank calculation. They occur in the two regimes

- `k=2` with `p<=2`, or
- `k=3` with `p<=5`.

No `k<=1` state can violate the inequality.

For `k=3`, every touched block must annihilate all three external quotient directions. For `k=2`, every nontrivial local quotient kernel must be the same two-dimensional plane in the three external coefficients; a local one-dimensional kernel would force the global kernel dimension below two. The verifier uses this characterization to enumerate exactly the potentially dangerous states rather than all `8^m` local block selections.

The finite ledger contains

```text
k=2, p<=2:   250949 states
k=3, p<=5:   755754 states
---------------------------
total:       1006703 states
```

## Exact rank certification without floating point

For each candidate state, the verifier constructs a basis of all selected-row relations that vanish in `Q`:

1. one local relation for every complete root-0 block, using
   `(1,0) - (0,1) - (1,-1) = 0`; and
2. `k` lifted relations from an integral basis of the external quotient-kernel.

The `T`-images of these relations form an integer matrix with at most 15 rows and 15 columns. Its rank is exactly `delta`.

To avoid more than a million repeated rational eliminations, the verifier computes these small ranks modulo

`P = 2^127 - 1`.

This is still an exact proof decision, not probabilistic modular evidence:

- a Lucas-Lehmer test in the verifier certifies that `P` is prime;
- every relation row encountered in the complete scan is checked to have squared Euclidean norm at most `1215`; and
- the verifier checks `P^2 > 1215^15`.

If the modular rank is `r`, every `(r+1)`-minor vanishes modulo `P`. Hadamard's inequality gives absolute value strictly below `P` for every such integer minor, so each minor is actually zero over `Z`. Reduction modulo `P` cannot increase rational rank, hence the modular and rational ranks are equal for every candidate matrix.

No floating-point or un-certified finite-field rank decision is used.

## Complete shard audit

The 77 orbit representatives were audited in seven disjoint ranges:

```text
range   candidates   k=2      k=3      min defect   negative
0:15       66887      14826     52061        2          0
15:29     181792      40226    141566        2          0
29:39     103035      23582     79453        2          0
39:49     110433      27226     83207        2          0
49:59     138062      35091    102971        2          0
59:69     225830      61110    164720        2          0
69:77     180664      48888    131776        2          0
-------------------------------------------------------------
total    1006703     250949    755754        2          0
```

Every shard returned `PASS`. The exact minimum value of

`|A_local| - 3 delta(A_local)`

among all 1,006,703 candidate states is `2`.

The shard commands are

```bash
python3 research/verify_target_c_support7_global_segment_relative_three_noroot_density_2026_09_20.py --orbit-start 0  --orbit-end 15
python3 research/verify_target_c_support7_global_segment_relative_three_noroot_density_2026_09_20.py --orbit-start 15 --orbit-end 29
python3 research/verify_target_c_support7_global_segment_relative_three_noroot_density_2026_09_20.py --orbit-start 29 --orbit-end 39
python3 research/verify_target_c_support7_global_segment_relative_three_noroot_density_2026_09_20.py --orbit-start 39 --orbit-end 49
python3 research/verify_target_c_support7_global_segment_relative_three_noroot_density_2026_09_20.py --orbit-start 49 --orbit-end 59
python3 research/verify_target_c_support7_global_segment_relative_three_noroot_density_2026_09_20.py --orbit-start 59 --orbit-end 69
python3 research/verify_target_c_support7_global_segment_relative_three_noroot_density_2026_09_20.py --orbit-start 69 --orbit-end 77
```

## Next finite layer

For four no-root cycles the same crude defect becomes

`4 + p - 3k`.

A possible violation is therefore restricted to

- `k=2` with `p<=1`,
- `k=3` with `p<=4`, or
- `k=4` with `p<=7`.

That is the next finite target if the global 45-cycle minimality route is continued.

For C-II itself, the direct bottleneck remains the current 3,874 generic-H6 states. The state-specific exact forced-segment-order scan remains the more direct closure route, followed by quantitative sine-law metric compatibility for whatever survives.
