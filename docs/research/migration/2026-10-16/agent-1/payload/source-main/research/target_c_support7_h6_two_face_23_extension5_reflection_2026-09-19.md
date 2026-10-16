# Target C support-seven H6: face-(2,3) extension V with reflection closure

Date: 2026-09-19

Status: exact finite reduction inside the generic H6 branch. The theorem-state authority is unchanged. C-II remains open.

## Result

The previous exact reflection-closed generic-H6 endpoint is

\[
4464=3580\,C_7+884\,(C_3\sqcup C_4).
\]

Continuing the fixed physical-face pair `(2,3)` scan through positions 1200 through 1699 of the 4,944-cell one-face-adaptive endpoint produces 94 additional direct exclusions that are still members of the 4,464-state reflection-closed endpoint. Every one of those 94 exclusions exactifies successfully.

The exact H6 hull reflection maps those 94 states to 94 distinct additional current survivors. The direct and reflected sets are disjoint. Closing the new exclusions under reflection therefore removes

\[
94+94=\boxed{188}
\]

states and gives the new explicit exact endpoint

\[
\boxed{4276=3422\,C_7+854\,(C_3\sqcup C_4)}.
\]

The direct 94 exclusions split as

```text
C7       79
C3+C4    15
```

and by normalized ground sign pattern as

```text
235   11
236   13
245    5
256   51
356   14
```

Their 94 reflected partners split by pattern as

```text
235   14
236   51
256   13
346    5
356   11
```

Thus the full 188-state reflection-closed exclusion batch has pattern counts

```text
235   25
236   64
245    5
256   64
346    5
356   25
```

and graph counts

```text
C7       158
C3+C4     30
```

The remaining explicit survivor census is

```text
145       4
156      16
235     580
236    1070
237      16
245     460
256    1070
345      16
346     460
347       4
356     580
```

These counts sum to 4,276 and are exactly invariant under the committed reflection pairing

```text
145 <-> 347
156 <-> 237
235 <-> 356
236 <-> 256
245 <-> 346
345 self
```

## Exact certificate layer

For each of the 94 direct candidates, retain the full twenty-way closed local branch cover at physical face 2 and again at physical face 3: ten cyclic force-gap orders times the two median branches. The global system is the committed 85-variable complete-angle affine lift.

A one-face branch is marked dead only after numerical LP support is recovered as an exact rational Farkas certificate. Every branch that remains locally live at face 2 is paired with every locally live branch at face 3. The state is excluded only when every such two-face product also has an exact rational Farkas contradiction. Thus each accepted direct exclusion covers all `20*20` local branch products. Floating-point LP values are discovery data only.

The 94 direct states use exactly

\[
2535+4333=\boxed{6868}
\]

exact rational certificates:

```text
one-face dead-branch certificates       2535
two-face live-product certificates      4333
total                                   6868
```

Their exact forced constants split as

```text
strictly negative   6426
zero                 442
```

with zero exactification failures. The largest active rational dual denominator in the batch is

```text
2571181654016275976801158271
```

The reflected 94 states require no new floating-point or LP assumption. Their impossibility is transported by the already-certified exact H6 reflection involution.

Certificate:

`research/verify_target_c_support7_h6_two_face_23_extension5_reflection_2026_09_19.py`

## Discovery and validation

The numerical discovery scan over positions 1200 through 1699 tested the fixed face pair `(2,3)` and found 94 candidates, with no LP failures. Filtering against the exact state-level reflection closure showed that all 94 candidates were still members of the current 4,464-state endpoint; none was an already-excluded overlap.

Exactification was run in three deterministic contiguous chunks:

```text
candidate range   good   failures   certificates   negative   zero
0..31               32       0          2154          2015      139
32..63              32       0          2228          2082      146
64..93              30       0          2486          2329      157
```

The totals are 94 good, zero failures, 6,868 certificates, 6,426 negative forced constants, and 442 zero forced constants.

An independent reconstruction of the exact 14,174-state reflection map verified involutivity, confirmed that the direct and reflected 94-state sets are disjoint subsets of the 4,464-state endpoint, and reproduced the 4,276-state final graph and pattern census above.

## Remaining finite work

The same fixed face-`(2,3)` branch test remains unscanned beyond position 1700 of the 4,944-cell one-face-adaptive ordering. Because the current survivor set is kept reflection-closed, a separate reflected face-`(3,4)` scan is unnecessary: every new `(2,3)` exclusion can immediately be closed under the exact hull reflection.

The higher-leverage nonlinear route remains to impose the common `L(K8)` segment-order constraints, all-root interior-domination disjunctions, and the sufficient 45 four-cycle metric conditions on the explicit 4,276 survivors, using the exact rational sine-interval certificate machinery. The seven-outsider minimization layer for replacing the selected 45-cycle metric family is also unresolved, but improving that basis size does not itself remove generic-H6 states.

Reciprocal-collinearity walls remain a separate nongeneric branch.
