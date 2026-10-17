# Target C: combine all-clean-fan and zero-class kernel incidence for Profile B

Date: 2026-09-22

Status: rigorous strengthening of the remaining eight-no-root `k=6,D=-1,p=9` Profile B finite audit. No closure is claimed until the strengthened complete cover executes.

The two inputs are:

- `research/target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_profile_b_all_clean_fans_2026-09-22.md`, which requires one fixed nine-singleton source basis to satisfy every three-clean `8 -> 7 -> 6 -> 5` puncture fan; and
- `research/target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_profile_b_kernel_incidence_2026-09-22.md`, which proves the exact zero-source-class incidence restrictions among the seven six-row children of a fixed clean seven-row shadow.

The combined verifier is

`research/verify_target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_profile_b_all_clean_fans_2026_09_22.py`.

## 1. Use zero classes, not only disappearing blocks

Let the nine actual source singleton replacement classes be the basis

```text
x_1,...,x_9
```

of the nine-dimensional source quotient `V_8`.

For a descendant quotient, a source basis class can map to zero in two ways relevant to the finite representation: its block can cease to be virtual-complete, or the descended replacement functional can remain on a complete block but lie in the descendant canonical column span. Therefore block disappearance alone is weaker than the actual puncture-kernel condition.

The strengthened verifier computes, over `Q`, the extra rank of every individual chosen source class in each descendant canonical quotient. It records

```text
Z = {a : image of x_a is zero}.
```

Because the source classes form a basis, these sets are exactly the coordinate basis vectors lying in the corresponding puncture kernel.

## 2. Cross-fan seven-row incidence

For each three-clean source coordinate `i`, the map

```text
V_8 -> V_{7,i}
```

has a one-dimensional kernel `L_i`. The all-clean-fans dependency-dual argument proves that `L_i` and `L_j` are distinct for distinct three-clean coordinates `i,j`.

Hence

```text
|Z_{7,i}| <= 1,
```

and if `Z_{7,i}={a}` then the same label `a` cannot belong to `Z_{7,j}` for another three-clean `j`. Otherwise the nonzero source basis vector `x_a` would lie in two distinct kernel lines.

This is strictly stronger than the earlier block-disappearance version because it also detects a complete descendant block whose replacement class becomes zero modulo the descendant canonical span.

## 3. Incidence inside every clean fan

Fix one three-clean source coordinate and its seven-row quotient `V_7`. The seven further coordinate punctures give pairwise distinct one-dimensional kernels in `V_7`; pulled back to `V_8`, they give seven distinct two-dimensional kernel planes through the common source-to-seven kernel line `K_0`.

The committed kernel-incidence argument yields two cases for the exact zero-class sets:

```text
Z_7 = empty:
    at most one of the seven six-row children can have |Z_6|=2;

Z_7 = {a}:
    a belongs to every Z_6;
    whenever Z_6 has a second label b, those second labels are pairwise
    distinct across the seven six-row children.
```

The strengthened wrapper now evaluates these zero sets for every three-clean fan, not only for the originally selected clean fan.

## 4. Combined necessary condition

A chosen fixed nine-block source basis is retained only if all of the following hold simultaneously:

1. the existing actual-state source realization and exact defect `-1` checks;
2. at least two exact three-clean source coordinates;
3. `d_7=3`, `d_6=3`, and `d_5 in {2,3}` throughout every three-clean fan;
4. exact image ranks `8`, `7`, and `3+d_5` for the same nine source classes at every level;
5. the complete-block disappearance bounds at every level;
6. distinct zero-basis labels across the first punctures of different three-clean fans; and
7. the exact seven-child zero-class kernel-incidence pattern inside every clean fan.

All new quotient-rank decisions use exact rational elimination. A genuine Profile B source must satisfy these conditions, so a zero result over the complete 20,451-orbit cover excludes Profile B.

The finite cover still has not executed because the available GitHub Actions jobs fail before runner acquisition. Profile B therefore remains open, but the surviving finite target is smaller and now couples every guaranteed clean fan through the same source basis.
