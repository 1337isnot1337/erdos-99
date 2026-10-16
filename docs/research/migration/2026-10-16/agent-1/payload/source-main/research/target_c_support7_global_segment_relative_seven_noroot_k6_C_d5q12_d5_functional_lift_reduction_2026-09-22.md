# Target C: seven-row functional lift obstruction for `C:(5,12,12)`, `d_6=5`

Date: 2026-09-22

Status: rigorous strengthening of the sole remaining six-row-shadow branch in the current eight-no-root `k=7` finite split. It reduces closure to a one-cycle seven-row functional-rank census. No full-cover execution is claimed in this note.

Companion files:

- `research/verify_target_c_support7_global_segment_relative_seven_noroot_k6_C_d5q12_d5_functional_threshold_2026_09_22.py`
- `research/verify_target_c_support7_global_segment_relative_seven_noroot_k6_C_d5q12_d5_functional_lift_2026_09_22.py`

The older full-span lift multiplicity audit remains a valid independent route. The new target is strictly local to one restored cycle and avoids proving a two-cycle multiplicity statement.

## 1. Six-row input

The only unresolved profile is

```text
C: D_8=-1, p=12, (d_v,q,s)=(5,12,12).
```

The committed good-pair reduction gives a synchronized six-row rank-one shadow with

```text
D_6=3,
p_6=12,
d_6=5.
```

The established replacement-functional bound at six rows is

```text
D_6 >= 6 + p_6 + 3 d_6 - 3 s_6.
```

Hence `s_6>=10`. If the six-row virtual-complete set has `c_6` blocks, its canonical relation matrix has `c_6+5` rows and rank `c_6-5`, so its functional quotient has dimension exactly ten. Therefore every surviving six-row shadow has full quotient rank

```text
s_6=10.
```

This is the already committed six-row functional-witness condition.

## 2. One restored cycle is forced to `d_7=5`

Restore either member of the selected deletion pair. The pair is `p=12` retaining, and deletion loss in the selected incomplete-root cost is nonnegative. Therefore each one-row deletion also preserves all twelve singleton rows:

```text
p_7=12.
```

The committed defect transport for this selected pair gives

```text
D_7=1.
```

The seven-row containment reduction leaves only

```text
d_7=4 with singleton capacity >=10,
```

or

```text
d_7=5 with singleton capacity >=11.
```

The separately proved deficiency-monotonicity lemma gives `d_7>=d_6=5` for every compatible line lift. Hence every one-cycle intermediate state of an actual target must satisfy

```text
d_7=5,
singleton capacity >=11.
```

## 3. Seven-row replacement functionals must fill an 11-dimensional quotient

The replacement-functional accounting used in the committed five- and six-row audits is row-count uniform. For a synchronized rank-one state with `t` external rows, incomplete-root cost `p`, virtual-complete deficiency `d`, and singleton-functional extra rank `s_t`, it gives

```text
D_t >= t + p + 3 d - 3 s_t.
```

The same construction at seven rows uses the six-dimensional nullspace of the coefficient line. If the seven-row virtual-complete set has `c_7` blocks, the canonical relation matrix has

```text
c_7 + 6
```

rows and rank

```text
c_7 - d_7 = c_7 - 5.
```

Thus the functional quotient has dimension exactly

```text
(c_7+6) - (c_7-5) = 11.
```

Substitute the forced seven-row parameters into the functional bound:

```text
1 >= 7 + 12 + 3*5 - 3 s_7
  = 34 - 3 s_7.
```

Therefore

```text
s_7 >= 11.
```

Since the quotient itself has dimension eleven, an actual target must attain

```text
s_7 = 11.
```

This is stronger than the previous one-cycle necessary condition, which only asked that the singleton blocks retained from the six-row state continue to span the old ten-dimensional quotient.

## 4. Safe finite over-approximation

For each six-row `d_6=5` full-functional witness, enumerate every compatible one-cycle lift. Keep only lifts with

```text
d_7=5,
capacity >=11,
```

and, as a cheap necessary prefilter, whose retained six-row singleton functionals still have extra rank ten.

For each surviving seven-row lift, form its virtual-canonical relation matrix and every compatible singleton replacement functional of every virtual-complete block.

A block can in principle admit more than one compatible singleton state at seven rows. The finite verifier deliberately inserts all of those state functionals simultaneously. An actual all-singleton profile can choose only one state per selected block, so this can only increase the computed span. Consequently

> if the span of this over-approximating family has extra rank at most ten for every qualifying lift, then no actual target can attain the necessary seven-row extra rank eleven.

This proves the `d_6=5` branch impossible without pairing two one-cycle lifts.

## 5. Exact rank certificate

The finite verifier uses the existing `P=2^127-1` exact-rank certificate and checks Lucas-Lehmer primality. It records the maximum squared norm and width of every functional matrix used in a rank decision and checks the corresponding Hadamard inequality against `P^2`, together with the relation-row norm bound. A successful full execution is therefore an exact rational-rank certificate, not probabilistic finite-field evidence.

The new verifier reuses the existing full-span verifier's incremental one-cycle profile construction and replaces the two-lift multiplicity endpoint by a seven-row singleton-functional span computation.

## 6. Completion criterion

The exact six-row augmentation cover has 325,955 representatives. A disjoint full-cover execution of the new verifier closes the remaining branch if every shard reports

```text
seven_full_rank_lifts 0
max_seven_extra_rank <= 10
functional_hadamard_exact_rank_bound True
relation_hadamard_exact_rank_bound True
PASS
```

No such full-cover output is recorded here. Until it is, `C:(5,12,12)` remains open in this finite split, and the canonical Target C-II theorem state remains open.
