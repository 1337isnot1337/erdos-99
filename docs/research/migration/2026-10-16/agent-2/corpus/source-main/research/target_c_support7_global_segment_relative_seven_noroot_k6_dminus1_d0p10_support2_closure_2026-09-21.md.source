# Target C: close the final seven-no-root `k=6` branch

Date: 2026-09-21

Status: exact finite closure. This note closes the remaining seven-no-root `k=6` case

```text
D=-1, k=6, d=0, p=10.
```

Together with the preceding committed branch eliminations, the entire seven-no-root `k=6` layer is now closed.

Companion verifier:

- `research/verify_target_c_support7_global_segment_relative_seven_noroot_k6_dminus1_d0p10_support2_closure_2026_09_21.py`

## 1. Inputs already proved in the repository

The preceding structural reductions force every hypothetical state in the last `k=6` branch to satisfy all of the following.

- The seven-row virtual-canonical deficiency is `d_v=3`.
- All ten virtual-complete incomplete blocks are singleton blocks, so `q=10` and the total selected incomplete-root cost is `p=10`.
- The coefficient-constraint space `P<=Q^7` is a line of support exactly two.

Call the two support coordinates of a generator of `P` the support coordinates. The other five coordinates are zero coordinates.

Deleting a zero coordinate preserves the coefficient-line support at two, so every such deletion is a good six-row `k=5` shadow to which the committed synchronized six-row containment theorem applies.

For a zero-coordinate deletion, the exact six-row defect arithmetic leaves `p_i` equal to `7` or `10`: the `p_i=1,4` cases were already excluded. Since the six-row virtual-complete set is contained in the global one,

```text
d_i <= d_v = 3.
```

The exact six-row deficiency-two singleton-capacity bound is three. But:

- if `p_i=7` and `d_i=2`, the containment inequality forces `q_i>=6`, hence at least five singleton blocks;
- if `p_i=10` and `d_i=2`, it forces `q_i>=7`, hence at least four singleton blocks.

Both contradict capacity three. Therefore every zero-coordinate deletion has

```text
d_i=3.
```

If `p_i=7`, the containment inequality forces `q_i=7`, all singleton. If `p_i=10`, it forces `q_i>=8`, again all drawn from the ten global singleton blocks. Thus every one of the five zero-coordinate deletion shadows has

```text
coefficient support = 2,
d_i = 3,
singleton capacity >= 7.
```

This necessary condition is already enough to close the branch.

## 2. Exact six-row support-two census

The verifier reuses the established exact `S_7` six-subset augmentation cover. It scans all synchronized six-row coefficient lines of support exactly two. The total scanned support-two states are

```text
1,578,428.
```

Among them, exactly 393 have virtual deficiency three and singleton capacity at least seven. Their capacity profile is

```text
capacity 7:   76
capacity 8:  114
capacity 9:  139
capacity 10:  64
----------------
total:       393
```

Complete-block ranks are computed modulo `2^127-1`. The same committed Lucas-Lehmer and Hadamard certificate applies: the modulus is prime, complete relation rows have squared norm at most 12, and

```text
(2^127-1)^2 > 12^15.
```

Hence every modular complete-block rank used here equals the corresponding rational rank.

## 3. Extend every possible six-row shadow

Take each of the 393 six-row states and append every possible remaining no-root cycle. After deduplicating identical labeled seven-row `(cycle set, coefficient line)` children, the verifier obtains

```text
35,454
```

support-two seven-row children.

For each child it deletes each of the five zero coordinates of the seven-row coefficient line and recomputes the resulting six-row virtual-canonical state. A hypothetical counterexample from Section 1 must have all five of these shadows simultaneously satisfy

```text
d_i=3,
singleton capacity >=7.
```

The exact result is

```text
children with all five required shadows: 0.
```

Therefore no seven-row support-two coefficient line can have the five deletion shadows forced by the final `k=6` branch.

The verifier also retains the stronger downstream filters from the previous reduction, namely that at least two zero-coordinate shadows have capacity at least eight and that the seven-row state itself has `d_v=3` and singleton capacity at least ten. They are never reached: every child already fails the all-five-shadow condition.

## 4. Exact verifier output

A fresh run from the committed repository state completed with

```text
support2_states_scanned 1578428
support2_d3_cap7 {7: 76, 8: 114, 9: 139, 10: 64}
support2_d3_cap7_total 393
stages {'children': 35454}
survivor_count 0
unique_complete_sets_ranked 71625
hadamard_exact_rank_bound True
PASS: final seven-no-root k6,p10 support-two branch closed
```

The absence of an `all5_d3cap7` stage entry means its count is zero.

## 5. Conclusion

The final residual

```text
D=-1, k=6, d=0, p=10
```

is impossible. The earlier commits already closed every other seven-no-root `k=6` arithmetic branch. Hence

> no seven-no-root counterexample exists with `k=6`.

The next unresolved seven-no-root coefficient-rank layer is `k=7`.
