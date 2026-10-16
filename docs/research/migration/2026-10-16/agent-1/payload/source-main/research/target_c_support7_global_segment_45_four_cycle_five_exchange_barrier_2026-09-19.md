# Target C support-seven: a five-exchange barrier for the 45-cycle metric test

Date: 2026-09-19

Status: exact structural refinement of the generic reciprocal metric layer. The theorem-state authority is unchanged. C-II remains open.

## Result

The selected metric family `F` contains 45 simple four-cycles in `K8`. The preceding exact exchange verifier proved that no sufficient 44-cycle family can be obtained from `F` using at most four cycles outside `F`.

The new exact finite audit rules out the next case as well:

\[
\boxed{\text{Any sufficient 44-cycle family must use at least six cycles outside }F.}
\]

Equivalently, a hypothetical sufficient 44-cycle family must omit at least seven of the current 45 selected cycles and introduce at least six external simple four-cycles.

Certificate:

`research/verify_target_c_support7_global_segment_45_four_cycle_five_exchange_barrier_2026_09_19.py`

The new verifier imports and reruns the preceding four-exchange verifier, then audits every five-outsider case exactly.

## Why only quotient ranks two and three matter

Let `E` be the five external cycles and let `d(E)` be the rank of their images modulo

\[
W=\operatorname{span}(\mathrm{SIDE}\cup F).
\]

A 44-cycle family with five external cycles contains 39 members of `F`, so it removes six selected cycles. If `R` is that six-cycle removal set, the missing ground information has dimension `t(R)`, the number of three-coordinate ground blocks touched by `R`.

The five external cycles provide a `W`-valued kernel of dimension

\[
5-d(E).
\]

Hence a necessary condition is

\[
t(R)\le 5-d(E).
\tag{1}
\]

Six removed selected cycles touch at least two three-coordinate blocks, so `t(R)>=2`. The 165 external cycles occupy 105 projective quotient classes, each of size at most two, so five external cycles use at least three projective classes and have quotient rank at least two. Therefore only

\[
d(E)=2\quad\text{or}\quad d(E)=3
\]

can satisfy (1).

For `d(E)=3`, the kernel has dimension two and `t(R)=2`. Six removals across exactly two three-coordinate blocks force the pattern `3+3`: two complete ground blocks.

For `d(E)=2`, the kernel has dimension three and `t(R)<=3`. The only removal patterns are:

- `3+3` across two blocks;
- `3+2+1` across three blocks;
- `2+2+2` across three blocks.

No other six-coordinate pattern can satisfy the dimension condition.

## Exact candidate enumeration

The preceding verifier gives 105 projective quotient directions: 45 singleton classes and 60 two-cycle classes. After deleting zero quotient coordinates, every primitive class direction lies in

\[
\{-1,0,1\}^{59}.
\]

The new verifier enumerates the span of every triple of the 105 projective directions over `F_251`. Equal reduced row spaces are pooled, and every five-cycle subset of every pooled flat with cycle capacity at least five is placed in the candidate ledger.

This finite-field step is exact, not heuristic. Any rational-rank-at-most-three five-set uses at least three projective classes, so its classes occur in one of the enumerated triple spans after reduction modulo 251. Conversely, for these `{-1,0,1}` columns, a nonzero `4x4` minor has absolute value at most 16 by Hadamard, and a nonzero `3x3` minor has absolute value less than 6. Both bounds are below 251. Therefore a `3x3` or `4x4` minor vanishes modulo 251 if and only if it vanishes over the integers for the rank decisions used here. The rank-two/rank-three classification is therefore rationally exact.

The pooled-flat cycle-capacity histogram is

```text
capacity 5: 76950 flats
capacity 6: 30800 flats
capacity 7:   900 flats
capacity 8:  1140 flats
```

After deduplication this gives exactly

\[
\boxed{332250}
\]

five-outsider candidate sets with quotient rank at most three.

Their exact ranks are

```text
rank 3: 332130
rank 2:    120
```

There are no rank-one candidates.

## Exact kernel construction

For each five-set, the verifier chooses exact independent quotient columns using the mod-251 pivots. Because the rank equality is certified by the minor bound above, Cramer's rule on the pivot coordinates gives an integer basis for the exact quotient kernel. Every resulting Cramer relation is then checked coordinate-by-coordinate over the integers in all 59 quotient coordinates.

The corresponding `W`-valued directions are formed in the 45 selected-cycle coordinates. Those coordinates are stored after multiplying by two, so all subsequent compensation tests are integral.

No floating-point arithmetic or optimization solver is used in this audit.

## Rank-three audit

For the 332130 rank-three five-sets, the quotient kernel is two-dimensional. The six removed selected cycles must be exactly two full three-coordinate ground blocks.

There are

\[
\binom{15}{2}=105
\]

such removal patterns per external five-set, representing

\[
332130\cdot105=\boxed{34873650}
\]

exact two-block compensation tests.

The verifier compresses those 105 tests without weakening them. On each candidate block, both kernel directions must restrict to a multiple of

\[
(1,-1,-1).
\]

Two blocks can recover the two missing ground equations exactly only if the resulting `2x2` coefficient matrix is nonsingular. No rank-three five-set passes this test.

## Rank-two audit

There are exactly 120 rank-two external five-sets. Their quotient kernels are three-dimensional.

For the `3+3` case, the verifier performs exact rational row-rank containment on each of the 105 pairs of full blocks:

\[
120\cdot105=\boxed{12600}
\]

checks. None succeeds.

For three touched blocks, the missing ground directions are independent and already have dimension three. Therefore successful compensation would force the projected three-dimensional kernel row space to equal the three-dimensional target ground row space. The verifier tests this exactly by blockwise proportionality followed by a `3x3` integer determinant.

The number of three-block removal patterns per rank-two five-set is

\[
15\cdot14\cdot13\cdot3\cdot3
+\binom{15}{3}3^3
=24570+12285
=36855.
\]

Across all 120 rank-two five-sets this gives

\[
120\cdot36855=\boxed{4422600}
\]

exact three-block checks. None succeeds.

Thus the five-external layer is empty.

## Validation

The 332250-set ledger was exhaustively run in five deterministic slices:

```text
[0, 80000)       rank 3: 79983   rank 2: 17
[80000, 160000)  rank 3: 79982   rank 2: 18
[160000, 240000) rank 3: 79981   rank 2: 19
[240000, 320000) rank 3: 79953   rank 2: 47
[320000, 332250) rank 3: 12231   rank 2: 19
```

Every slice returned `PASS`. The slice totals reproduce exactly 332130 rank-three and 120 rank-two cases. An independent exact integer implementation reproduced the same rank counts and no-compensation result.

## Consequence and next target

Combining this audit with the preceding zero-through-four-outsider barrier gives

\[
\boxed{|E|\ge6}
\]

for any 44-cycle sufficient family among the 210 simple `K8` four-cycles.

The first unresolved exchange layer is therefore six external cycles. A 44-cycle family at that depth removes seven selected cycles. If `d` is the quotient rank of the six external cycles, the available `W` kernel has dimension `6-d`, while seven removed selected coordinates touch at least three ground blocks. Hence the first potentially viable six-external cases require `d<=3`. The next finite search should enumerate rational-rank-at-most-three six-sets of the 165 external cycles and test the corresponding `3+3+1`, `3+2+2`, and lower-rank three/four-block compensation patterns.

This result concerns only minimization of the simple-four-cycle metric completion layer. It does not exclude additional generic-H6 states by itself, does not prove global minimality of the 45-cycle test, and does not change the C-II theorem state. The explicit reflection-closed generic-H6 endpoint remains 4464 states.