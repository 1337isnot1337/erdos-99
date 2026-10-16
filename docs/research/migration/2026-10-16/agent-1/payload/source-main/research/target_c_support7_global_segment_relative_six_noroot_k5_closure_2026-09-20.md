# Target C: six-no-root `k=5` closure

Date: 2026-09-20

Status: exact closure of both synchronized `k=5` six-no-root counterexample cases. Combined with the deletion-shadow synchronization theorem and the committed `k=6` closure, any remaining six-no-root factor-three counterexample must now have `k=4`. This does not yet prove the full six-no-root inequality, reduce the 3,874-state generic-H6 endpoint, or close C-II.

Companion verifier:

`research/verify_target_c_support7_global_segment_relative_six_noroot_k5_2026_09_20.py`

## Starting point

Let `A` be a block-reduced family with exactly six no-root four-cycles and write

`D(A)=|A|-3 delta(A)`.

The deletion-shadow synchronization theorem leaves, in the `k=5` branch, only

```text
D(A)   k(A)   p(A)   deletion k   deletion p
 -2      5      7         4            7
 -1      5      8         4            8
```

Every one of the six no-root deletion shadows therefore has five no-root rows, `k=4`, and the same value of `p`.

For `k=5` on six external rows, the global coefficient-constraint space `P` is a line in the six external coefficients.

If a primitive generator of `P` were supported on only one external coordinate, deleting that coordinate would project `P` to zero, giving deletion `k=5` rather than `k=4`. Hence every synchronized candidate satisfies

`support(P) >= 2`.

The support-overlap corollary from deletion synchronization also gives:

> every nonempty incomplete root-0 block in a hypothetical six-no-root counterexample is touched by at least two of the six no-root cycles.

## Six-row virtual canonical state

Fix the six no-root rows and an obtainable rank-one line `P`.

For each touched root-0 block `b`, let `E_b` be its empty-state coefficient constraint. Define a virtual canonical state exactly as in the established five-no-root `k=4` containment theorem:

- `b` is empty when `E_b subset P`;
- `b` is complete otherwise.

Let `C` be the canonical complete-block set, `c=|C|`, and let `H(C)` be the span in the 15-dimensional `T` space of the complete-block relation rows `h_b`, `b in C`.

Write

`d = c - rank H(C)`.

## Lifting the five-no-root containment theorem

The key point is that the committed five-no-root `k=4` containment theorem propagates to this six-row canonical state.

Fix an external coordinate `i` and delete the corresponding no-root row. Let `pi_i` denote deletion of coordinate `i` in coefficient space and set

`P_i = pi_i(P)`.

Because `support(P)>=2`, every `P_i` is still a nonzero line. Thus the deletion shadow lies in the five-no-root `k=4` setting.

Let `C_i` be the virtual canonical complete-block set for the five-row deletion and line `P_i`.

If `b` is canonical-empty for the six-row state, then `E_b subset P`, so after projection

`pi_i(E_b) subset P_i`.

Therefore `b` is also canonical-empty after deletion. Hence

`C_i subset C`.

The five-no-root theorem gives

`|C_i| - rank H(C_i) >= 2`.

Adding complete-block rows cannot reduce row nullity, so

`d = |C|-rank H(C) >= |C_i|-rank H(C_i) >= 2`.

Now let

`N = null(P)`

and

`N_i = {alpha in N : alpha_i=0}`.

For `alpha in N_i`, delete coordinate `i`. The resulting five-vector lies in `null(P_i)`. The five-no-root containment theorem says its external `T` relation lies in `H(C_i)`.

Lifting back to six coordinates changes nothing. On every block in `C\C_i`, the projected empty constraint is contained in `P_i`, so the combined local quotient demand of `alpha` is zero there. Thus the six-row canonical relation is the same five-row relation and lies in

`H(C_i) subset H(C)`.

It remains to span all of `N`. Since `P` has support at least two, there exist coordinates `i,j` for which

`N = N_i + N_j`.

One way to see this is that every `N_i` has dimension four, and one can choose `i,j` so that imposing both coordinate zeros together with the single equation defining `N` leaves dimension three. Hence

`dim(N_i+N_j)=4+4-3=5=dim N`.

Therefore every external relation from `null(P)` lies in `H(C)`.

So the six-row virtual canonical state inherits exactly the structural facts needed from the five-row theorem:

`d>=2`,

and

`external relations subset H(C)`.

## Propagation to an actual state

Fix an actual local state with the same global line `P`.

Let `q` be the number of canonical-complete blocks changed to incomplete states. A canonical-complete block cannot become empty, because by definition its empty constraint is not contained in `P`. Thus every such block contributes at least one selected root-0 row.

Let `p` be the total number of selected root-0 rows in all incomplete blocks.

Changes from complete to compatible singleton or pair states alter external relation rows only by multiples of the corresponding complete-block relation `h_b`. Changes on canonical-empty blocks to other compatible incomplete states have zero local quotient demand for every vector in `null(P)`. Extra complete blocks outside `C` can increase `delta` by at most one while adding three rows, so their contribution cancels in the defect bound.

Consequently the same containment accounting as in the five-no-root theorem gives

`delta(A) <= c-d`

up to those canceling extra completions, and therefore

`D(A) >= 6 + p + 3d - 3q`.

For `d>=4`, the crude `q<=p` bound already gives

- at `p=7`: `D(A)>=4`;
- at `p=8`: `D(A)>=2`.

Only `d=2` and `d=3` require any finite audit.

## Exact six-subset cover

The verifier starts from the exact 20,451 `S_7` orbit representatives of five no-root cycles already constructed by the five-no-root verifier.

It labels all

`C(105,5)=96,560,646`

five-subsets by orbit id in a temporary `int32` table.

For each five-orbit representative, it takes one extension from each orbit of the parent stabilizer on the remaining no-root cycles. A six-child is retained only when that parent orbit id is minimal among the orbit ids of all six five-deletion parents.

This is the standard canonical-augmentation cover: every six-subset orbit has at least one retained child by choosing a minimal deletion parent and relabeling that parent to its representative.

The resulting cover has

`325,955`

six-subset representatives. The independently committed Burnside count is

`325,911`

six-subset orbits, so the augmentation list has 44 excess representatives. Duplicates are harmless for the maximum/capacity assertions below.

## Low-deficiency scan

For every cover representative, the verifier enumerates every obtainable rank-one line `P` arising from an empty or singleton local constraint. There are

`3,702,924`

virtual canonical states in the augmentation cover.

Their complete-block deficiency census is

```text
d=2          148
d=3       18,600
d=4      422,241
d=5    1,933,839
d=6    1,018,539
d=7      277,487
d=8       31,217
d=9          785
d=10          68
```

This independently cross-checks `d>=2` everywhere in the cover.

After imposing the necessary synchronized condition `support(P)>=2`, only

- 39 cover states with `d=2`;
- 2,825 cover states with `d=3`

remain.

## Singleton-capacity obstruction

For a canonical-complete block to be changed to a singleton in a hypothetical counterexample, two conditions are necessary:

1. the singleton local constraint is contained in `P`;
2. the block is touched by at least two of the six no-root cycles, by the support-overlap corollary.

The exact capacity census over the low-deficiency cover is

```text
d=2:
compatible shared singleton blocks   cover states
1                                      9
2                                     30

 d=3:
compatible shared singleton blocks   cover states
0                                    969
1                                    906
2                                    942
3                                      8
```

Thus

`singleton_capacity <= 2` for `d=2`,

and

`singleton_capacity <= 3` for `d=3`.

If `q` canonical-complete blocks are made incomplete and only `s` of them can be singletons, the selected-row cost of those `q` blocks is at least

`2q - min(q,s)`.

Hence:

- `d=2,p=7,s<=2` implies `q<=4`;
- `d=2,p=8,s<=2` implies `q<=5`;
- `d=3,p=7,s<=3` implies `q<=5`;
- `d=3,p=8,s<=3` implies `q<=5`.

Substituting into

`D(A) >= 6+p+3d-3q`

gives

```text
(d,p)   defect lower bound
(2,7)          7
(2,8)          5
(3,7)          7
(3,8)          8
```

Together with the `d>=4` bounds, every synchronized `k=5` state has

`D(A)>=2`.

Therefore neither `D=-2,p=7` nor `D=-1,p=8` can occur.

So:

> the six-no-root `k=5` branch contains no factor-three counterexample.

## Exactness

The orbit construction and local-constraint enumeration are exact integer combinatorics.

Complete-block ranks are computed modulo

`P=2^127-1`.

The imported base verifier runs the Lucas-Lehmer primality check. Every complete-block relation row has squared Euclidean norm at most 12, and the verifier checks

`P^2 > 12^15`.

Every relevant determinant has order at most 15, so Hadamard's bound makes each modular rank equal to the rational rank.

The containment step itself is proved by lifting the already committed exact five-no-root `k=4` containment theorem through deletion; it is not inferred from finite-field sampling.

## Updated six-no-root target

The six synchronized counterexample cases were

```text
D(B)   k(B)   p(B)
-2       4      4
-2       5      7
-2       6     10
-1       4      5
-1       5      8
-1       6     11
```

The committed `k=6` closure removes the last pair, and this result removes the `k=5` pair.

Only

```text
D(B)   k(B)   p(B)
-2       4      4
-1       4      5
```

remain in the six-no-root metric-basis route.

The next target should use the five-no-root `k=3` canonical containment theorem on the six deletion shadows to lift a rank-two coefficient-space containment statement for six-row `k=4`, then audit only the synchronized `p=4,5` residuals.

The direct C-II endpoint remains

`3874 = 3076 C7 + 798 (C3 disjoint-union C4)`.

No theorem-state authority file is changed by this result.
