# Target C support-seven H6: third exact face-(2,3) extension

Date: 2026-09-19

Status: exact finite reduction inside the generic H6 branch. The theorem-state authority is unchanged. C-II remains open.

## Result

The previously certified generic-H6 endpoint

\[
4841=3853\,C_7+988\,(C_3\sqcup C_4)
\]

is reduced to

\[
\boxed{4805=3823\,C_7+982\,(C_3\sqcup C_4)}.
\]

Thus 36 additional labelled generic-H6 cells are excluded: 30 of type `C7` and 6 of type `C3+C4`.

The excluded ground-pattern census is

```text
235   5
236   2
245   3
256  24
346   1
356   1
```

The surviving ground-pattern census is

```text
145      4
156     16
235    654
236   1278
237     16
245    474
256   1204
345     21
346    479
347      4
356    655
```

## Certificate rule

For each listed cell, physical faces 2 and 3 each have the same 20 closed local branches used in the preceding exact reductions: ten admissible cyclic gap orders times the low/high median branch. A cell is removed only after all `20 x 20` branch products are covered. A product is covered either because one constituent local branch already has an exact one-face contradiction, or because the simultaneous pair has an exact two-face contradiction.

The discovery pass used HiGHS only to locate candidate dual supports. The committed verifier converts every accepted support to exact rational arithmetic and checks nonnegative inequality multipliers, normalized strict weight, exact cancellation of all 85 affine variables, unrestricted equality multipliers, and a nonpositive forced constant. The discovery run exactified all 36 candidate cells with zero failures.

For this batch the exact branch coverage uses 1,014 one-face certificates and 1,330 two-face product certificates, 2,344 exact rational certificates in total. The largest dual denominator encountered in the discovery run is

```text
3575688275930909083760258
```

## Scope and next target

This batch completes exactification of the 36 numerical face-(2,3) candidates that remained in the first 700 positions of the earlier 4,944-cell one-face endpoint after the previous two extension batches. It is not an exhaustive scan of all 4,805 survivors.

The immediate linear target is to continue fixed-pair scanning beyond that range and to impose the reflected hull pair `(3,4)`. The hull reflection fixing vertex 0 and exchanging `1<->5` and `2<->4` maps the physical face pair `(2,3)` to `(4,3)`, so the present asymmetric survivor census itself indicates additional reflected exclusions should exist. After the finite affine branch cuts plateau, the remaining generic cells still have to satisfy the complete reciprocal metric compatibility equations, including the independent `K7` sine-law consistency relations and all seven equilateral-pentagon closures. Reciprocal-collinearity walls remain a separate nongeneric branch.

Verifier: `research/verify_target_c_support7_h6_two_face_23_extension3_2026_09_19.py`.
