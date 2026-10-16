# Target C: six-no-root `k=6` closure

Date: 2026-09-20

Status: exact closure of both synchronized `k=6` six-no-root counterexample cases. Combined with the deletion-shadow synchronization theorem, any remaining six-no-root factor-three counterexample must now have `k=4` or `k=5`. This does not yet prove the full six-no-root inequality, reduce the 3,874-state generic-H6 endpoint, or close C-II.

Companion verifier:

`research/verify_target_c_support7_global_segment_relative_six_noroot_k6_2026_09_20.py`

## Starting point

For a block-reduced family `A` with six no-root four-cycles, write

`D(A)=|A|-3 delta(A)`

and retain the established local-block notation

`|A|=6+3c+p`,

where `c` is the number of complete touched root-0 quotient blocks and `p` is the number of selected root-0 rows in incomplete touched blocks.

The deletion-shadow synchronization theorem reduces every hypothetical counterexample to six exact boundary cases. For `k=6` only two remain:

- `D=-2`, `p=10`;
- `D=-1`, `p=11`.

The same theorem proves that every nonempty incomplete block is touched by at least two of the six no-root cycles.

## Local form when `k=6`

Here the external coefficient-constraint space has rank zero. Therefore each touched quotient block must impose zero local constraint on the six external coefficients.

A touched block can consequently be only one of the following:

- complete;
- a two-row pair, which spans the local two-dimensional quotient block;
- a singleton whose line contains every nonzero local component of all six no-root cycles.

An empty touched block is impossible, because at least one no-root local component is nonzero and an empty block would impose a nonzero coefficient constraint.

By deletion-shadow synchronization, every incomplete block is nonempty and hence has no-root support multiplicity at least two.

Let

- `U` be the number of touched blocks;
- `q` be the number of incomplete blocks;
- `s` be the number of singleton incomplete blocks.

The other `q-s` incomplete blocks are pairs. Thus

`p = s + 2(q-s) = 2q-s`,

so

`s=2q-p`,

and

`c=U-q`.

For a fixed six-set, it is therefore enough to know how many touched blocks have support multiplicity at least two and how many of those have all six local components on one projective root line. No enumeration of pair choices is needed for the upper bound below.

## Immediate ambient-rank cutoff

The ground-root space `T` has dimension 15, so always

`delta(A)<=15`.

If `c>=10`, then at the smaller boundary value `p=10`,

`D(A) >= 6+3*10+10-3*15 = 1`.

The `p=11` case has still more slack. Therefore a `k=6` counterexample would have to satisfy

`c<=9`.

This is used as a cheap prefilter before any rank calculation.

## All-complete domination

Fix the six no-root rows and complete every touched root-0 block. Call the resulting superfamily `F`.

Because

`delta(X)=dim(span_M(X) intersect T)`,

adding rows cannot decrease `delta`, so

`delta(A)<=delta(F)`.

For `F`, every quotient block is complete. The companion verifier constructs the exact `T`-relation matrix consisting of

- one complete-block relation row `H_b` for every touched block;
- one adjusted `T` row for each of the six no-root cycles.

Its rank is exactly `delta(F)`. If this rank is `rho`, every admissible state with `c` complete blocks and boundary value `p` obeys

`D(A) >= 6+3c+p-3 rho`.

Thus the local-state problem collapses to an all-complete rank plus the integer `q`.

## Exhaustive six-set cover

The verifier does not need to build the canonical list of 325,911 six-subset `S_7` orbits.

It first reconstructs the established four-subset orbit decomposition and performs the same stabilizer augmentation used by the five-no-root verifier, stopping before its final duplicate-removal step. This produces 20,475 five-subset candidates. There are 20,451 actual five-subset orbits; the extra 24 candidates are duplicate orbit representatives.

The 20,475 candidates still cover every five-subset orbit. Extending each by all 100 no-root cycles not already present therefore covers every six-subset orbit: given any six-set, delete one row, relabel that five-set to a covered representative, and the deleted row appears among the 100 extensions.

The raw extension count is

`20,475 * 100 = 2,047,500`.

After applying the exact `k=6` local conditions, the support-multiplicity condition, and the necessary `c<=9` cutoff, only 68,780 distinct labeled six-sets remain. Of these,

- 46,849 admit a `p=10` count profile;
- 46,792 admit a `p=11` count profile.

These are a cover, not a claim that 68,780 is an orbit count.

## Exact all-complete ranks

For the 68,780 surviving six-sets, the all-complete rank census is

```text
rho=5          1
rho=6        243
rho=7        154
rho=8      6,171
rho=9     20,079
rho=10    40,256
rho=11     1,876
```

No survivor has all-complete relative rank above 11.

The verifier evaluates the defect lower bound for every admissible `(six-set,q)` profile. At `p=10` the census is

```text
lower bound 7        92
lower bound 10    2,123
lower bound 13   37,230
lower bound 16   45,082
lower bound 19   11,731
lower bound 22      326
```

so the minimum is

`7`.

At `p=11` the census is

```text
lower bound 8       374
lower bound 11    8,073
lower bound 14   39,799
lower bound 17   11,731
lower bound 20      326
```

so the minimum is

`8`.

These are lower bounds for all actual local state choices with the same count profile; pair orientations and singleton locations do not need separate reranking.

Hence neither synchronized `k=6` boundary can have negative defect.

Therefore

`k=6` is impossible for a hypothetical six-no-root counterexample.

The synchronized six-case table reduces to four cases:

```text
D(B)   k(B)   p(B)
-2       4      4
-2       5      7
-1       4      5
-1       5      8
```

## Exactness of the modular ranks

All relation rows are integer vectors in the 15-dimensional ground-root coordinate space. Across the entire surviving cover, the maximum squared row norm is

`12`.

Ranks are computed modulo

`P=2^127-1`.

The verifier runs the Lucas-Lehmer primality check for `P` and verifies

`P^2 > 12^15`.

If a nonzero rational/integer minor of size at most 15 vanished modulo `P`, its determinant would have absolute value at least `P`, while Hadamard gives squared determinant at most `12^15`, a contradiction. Thus every modular rank used above equals the rational rank.

## Next target

The six-no-root layer is now reduced to `k=4` and `k=5` only.

The same all-complete domination bound should be tested first on the four synchronized boundary points `(k,p)=(4,4),(4,5),(5,7),(5,8)`. Unlike `k=6`, empty touched blocks can occur because the global coefficient-constraint space has rank two or one. The next verifier should enumerate only obtainable global constraint spaces and use the synchronized support-overlap rule before any exact local reranking.

The direct C-II endpoint remains

`3874 = 3076 C7 + 798 (C3 disjoint-union C4)`.

No theorem-state authority file is changed by this result.
