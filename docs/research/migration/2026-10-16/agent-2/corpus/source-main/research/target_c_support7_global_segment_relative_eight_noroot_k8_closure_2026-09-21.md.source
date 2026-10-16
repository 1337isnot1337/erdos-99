# Target C: close the eight-no-root `k=8` layer

Date: 2026-09-21

Status: rigorous combinatorial closure of the rank-zero eight-no-root layer. Combined with the preceding reduction, no eight-no-root counterexample exists with `k=8`.

Companion checker:

- `research/verify_target_c_support7_global_segment_relative_eight_noroot_k8_closure_2026_09_21.py`

## 1. Starting point

The preceding eight-no-root reduction leaves only

```text
D=-2, d=0, p=14;
D=-1, d=0, p=15.
```

Here `B=R union E`, `|E|=8`, `k=8`, and the external quotient rank is zero. Every external row is an `M`-coloop, so deleting `t` external rows raises defect by exactly `2t`.

The same reduction proves the following two inputs.

1. Every triple deletion has incomplete-row count

   ```text
   p=14 branch: p_5 in {14,11};
   p=15 branch: p_5 in {15,12}.
   ```

   Thus every triple deletion loses either zero or three selected incomplete root rows.

2. For a six-row rank-zero shadow in which every incomplete block is touched by at least two of the six surviving external cycles,

   ```text
   global p=14, c<=7 => D_6>=5;
   global p=15, c<=7 => D_6>=6.
   ```

   The required pair-shadow defects are only `D_6=2` and `D_6=3`, respectively. Hence every pair deletion in either residual must leave at least one incomplete block of six-row support exactly one.

We also use the already committed exact six-row bounds

```text
p=11, c<=9, incomplete support>=2 => D>=8;
p=12, c<=8, incomplete support>=2 => D>=6.
```

Since global deficiency is zero and `k=8`, the global complete-block count satisfies `c+8<=15`, so every pair shadow has `c_6<=7`.

## 2. Low-support notation

For an incomplete root block, call its external support the subset of the eight no-root cycles that touch it. Only supports of size at most three can become support zero or one after deleting at most three external coordinates.

Let

- `a_i` be the total selected incomplete-row cost in blocks of exact support `{i}`;
- `b_ij` be the total selected incomplete-row cost in blocks of exact support `{i,j}`;
- `c_ijk` be the total selected incomplete-row cost in blocks of exact support `{i,j,k}`.

All these quantities are nonnegative integers.

For a triple `S={i,j,k}`, the selected incomplete-row cost lost on deleting `S` is

`a_i+a_j+a_k+b_ij+b_ik+b_jk+c_ijk`.

By the triple-shadow classification above, this loss belongs to `{0,3}`.

Similarly, deleting one or two external rows changes `p` by a multiple of three, because the defect and `k` values of the corresponding seven- and six-row shadows are fixed modulo three. Therefore

```text
a_i in {0,3},
a_i+a_j+b_ij in {0,3}.
```

## 3. Exact-support singletons are impossible

Assume `a_i=3` for some coordinate `i`.

For every two distinct `j,k != i`, the triple-loss equation for `{i,j,k}` already contains the full cost three from `a_i`. Nonnegativity therefore forces

```text
a_j=a_k=0,
b_ij=b_ik=b_jk=0,
c_ijk=0.
```

In particular, after deleting the pair `{i,j}`, no surviving incomplete block can have six-row support one. Such a block would have had global support contained in `{i,j,k}` for some `k` and not contained in `{i,j}`; every possible exact support of size at most three is zero by the displayed relations.

The pair deletion loses exactly the three rows counted by `a_i`, so its incomplete-row count is

```text
p_6=11 in the p=14 branch,
p_6=12 in the p=15 branch.
```

All surviving incomplete blocks have support at least two, while `c_6<=7`. The committed exact bounds then give

```text
D_6>=8 for p_6=11,
D_6>=6 for p_6=12,
```

contradicting the required `D_6=2` or `3`.

Hence

`a_i=0`

for every coordinate.

## 4. Exact-support pairs are impossible

With all `a_i=0`, the one- and two-row congruences give

`b_ij in {0,3}`.

Assume `b_ij=3`. For every `k` outside `{i,j}`, the triple-loss equation for `{i,j,k}` is already saturated by `b_ij`, so

```text
b_ik=b_jk=c_ijk=0.
```

After deleting `{i,j}`, no surviving incomplete block can have support one: any such block would have global support `{i,k}`, `{j,k}`, or `{i,j,k}` for some `k`, and all three possibilities have zero cost. Supports of size at least four cannot fall to size one after only two deletions.

Again the pair deletion loses exactly three rows, so `p_6=11` or `12`. The same exact six-row bounds contradict `D_6=2` or `3`.

Therefore

`b_ij=0`

for every pair.

## 5. The remaining exact-support triples form an impossible covering hypergraph

Now every triple-loss equation reduces to

`c_ijk in {0,3}`.

Form a 3-uniform hypergraph `H` on the eight external coordinates by declaring `{i,j,k}` an edge exactly when `c_ijk=3`.

Fix any pair `{i,j}`. Deleting that pair must leave an incomplete block of six-row support one; otherwise the conditional six-row `p=14` or `p=15` lower bound from the preceding reduction gives `D_6>=5` or `6`, contradicting `D_6=2` or `3`.

Because all exact-support one- and two-coordinate costs are zero, a surviving support-one block after deleting `{i,j}` must have had exact global support `{i,j,k}` for some `k`. Thus every pair of vertices lies in an edge of `H`.

So `H` is a 3-uniform pair-cover of an eight-element set. There are

`C(8,2)=28`

unordered pairs, while one triple covers only

`C(3,2)=3`

pairs. Therefore

`|E(H)| >= ceil(28/3)=10`.

But each edge carries selected incomplete-row cost exactly three. The total available incomplete-row cost is only 14 or 15, so

```text
p=14 => |E(H)|<=4,
p=15 => |E(H)|<=5.
```

This contradicts `|E(H)|>=10` in both branches.

## 6. Conclusion

Both residual rank-zero branches are impossible. Therefore

> No eight-no-root counterexample exists with `k=8`.

Equivalently, the entire eight-no-root rank-zero layer is closed without an eight-row orbit enumeration.

This does not yet close the full eight-no-root layer: the lower-nullity cases `k<=7` still require separate treatment. The next natural layer is `k=7`, where the external quotient rank is one and every one-row deletion is a seven-no-root `k=6` state.
