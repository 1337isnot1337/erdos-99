# Target C: close the Profile B weight-three coefficient residual by unstripped cost

Date: 2026-09-22

Status: rigorous closure of the coefficient-minimum-weight-three subcase of the sole remaining eight-no-root `k=6,D=-1,p=9` Profile B. Combined with the already-proved weight-two exclusion, this upgrades the source coefficient plane to `d_1(P)>=4`. Hence all eight source coordinates are three-clean. This does not by itself close Profile B or Target C-II.

Companion arithmetic regression guard:

`research/verify_target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_profile_b_weight3_unstripped_closure_2026_09_22.py`

The proof reuses the exact five-row functional censuses

- `research/verify_target_c_support7_global_segment_relative_five_noroot_k4_p7_d2_functional_2026_09_21.py`; and
- `research/verify_target_c_support7_global_segment_relative_five_noroot_k4_p7_d3_functional_2026_09_21.py`.

It also uses the rank-uniform accounting proved in

`research/target_c_support7_global_segment_relative_eight_noroot_k6_functional_rank_reduction_2026-09-22.md`.

## 1. The earlier weight-three residual stripped rows unnecessarily

The remaining Profile B source has

```text
D=-1,
t=8,
rank(P)=2,
p=9,
d_v=3,
q=9,
nine singleton changed blocks.
```

The committed low-weight reduction already proves

```text
d_2(P)>=4
```

and excludes coefficient words of weight two. It then treated a hypothetical weight-three word by deleting its support and repartitioning the retained root state into a stripped child with possible costs `p' in {9,6,3,0}`. That bookkeeping is valid as a stripped description, but it loses a stronger inequality already available elsewhere in the repository.

Deleting no-root rows does not delete selected root rows. Under the unstripped convention used in the later eight-no-root sharpening, all nine selected singleton root rows remain in the child row set. A row whose block becomes untouched imposes no external coefficient constraint and no relative `T` relation, but it still contributes one selected row to the defect. Likewise an incomplete state on a virtual-empty block has zero quotient demand. Therefore the rank-uniform replacement-functional inequality applies with the original cost

```text
p=9,
```

not merely with the stripped cost of the retained virtual-complete changed blocks.

This is exactly the scope of the already-proved bound

```text
D >= t+p+3d-3s,
```

where `d` is virtual-complete deficiency and `s` is the extra rank gained by the compatible replacement functionals modulo the canonical relation-column span.

## 2. Delete the support of a hypothetical weight-three word

Assume for contradiction that `P` contains a nonzero word `w` of weight three. Let

```text
S = supp(w),
|S|=3.
```

Puncturing the three coordinates in `S` kills at least the line spanned by `w`. It cannot kill all of `P`: if the projected coefficient rank were zero, the union support of `P` would be contained in `S`, giving

```text
d_2(P)<=3,
```

contrary to the established `d_2(P)>=4`.

Hence the coefficient rank drops by exactly one:

```text
rank(P|_{[8]\S})=1.
```

The exact deletion-transport identity therefore gives

```text
D_5 = -1 + 2|S| - 3(1)
    = -1 + 6 - 3
    = 2.
```

The child has

```text
t=5,
rank(P_5)=1,
k=4,
D_5=2,
p=9
```

in the unstripped accounting.

Virtual-complete sets only shrink under puncturing, so

```text
d_5<=d_v=3.
```

The committed five-row rank-one containment theorem gives

```text
d_5>=2.
```

Thus only

```text
d_5 in {2,3}
```

is possible.

## 3. Deficiency two is impossible

Let `s_5` be the extra rank of the actual canonical-complete singleton replacement functionals in the five-row child. The rank-uniform inequality gives

```text
2 >= 5 + 9 + 3*2 - 3s_5
  = 20 - 3s_5.
```

Therefore

```text
s_5>=6.
```

In particular the child has at least six compatible canonical-complete singleton blocks.

The committed exact five-row rank-one deficiency-two functional census exhausts every such virtual-canonical state with singleton capacity at least five. Its exact result is stronger than needed:

```text
capacity 5: singleton extra rank 2, 2 states;
capacity 6: singleton extra rank 2, 7 states;
maximum singleton extra rank = 2.
```

Thus `s_5<=2`, contradicting `s_5>=6`.

Hence

```text
d_5 != 2.
```

The filename of that audit contains `p7` because it was first introduced for a `p=7` branch. Its enumeration itself is over all five-row rank-one `d=2` virtual states with at least five compatible singleton-complete blocks, so the certified span bound applies here unchanged.

## 4. Deficiency three is impossible

Now suppose

```text
d_5=3.
```

The same unstripped functional inequality gives

```text
2 >= 5 + 9 + 3*3 - 3s_5
  = 23 - 3s_5,
```

so

```text
s_5>=7.
```

Thus the child has singleton capacity at least seven.

The committed exact five-row rank-one deficiency-three functional census exhausts every `d=3` virtual-canonical state with singleton capacity at least seven. Its exact census has maximum singleton-functional extra rank six:

```text
max s = 6.
```

Therefore

```text
s_5<=6<7,
```

again a contradiction.

Hence

```text
d_5 != 3.
```

Both possible deficiencies are impossible. Therefore the assumed coefficient word of weight three cannot exist.

## 5. Consequence: every source coordinate is three-clean

The previous low-weight argument already excluded weights below three. The present argument excludes weight three. Therefore the rank-two source coefficient plane satisfies

```text
d_1(P)>=4.
```

Equivalently, no nonzero coefficient word has support of size at most three.

For every source coordinate `i` and every deletion set `S` with

```text
i in S,
1<=|S|<=3,
```

puncturing `S` preserves coefficient rank two. Otherwise a nonzero coefficient word supported inside `S` would exist. Thus every one of the eight source coordinates is three-clean.

This removes the separate five-row weight-three residual as a closure obligation. The verifier

`research/verify_target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_profile_b_weight3_five_row_residual_2026_09_22.py`

remains a valid independent finite crosscheck, but Profile B no longer depends on executing it.

## 6. Effect on the remaining Profile B audit

The remaining Profile B source must now satisfy simultaneously

```text
rank(P)=2,
d_1(P)>=4,
d_2(P)>=4,
d_v=3,
nine singleton source replacement classes forming a basis of V_8,
all eight source coordinates three-clean.
```

Consequently every source coordinate participates in the proved clean puncture fan:

```text
8 -> 7 -> 6 -> 5,
```

with

```text
d_7=3,
d_6=3,
d_5 in {2,3},
```

and with the same fixed nine source singleton basis required to attain image ranks `8`, `7`, and `3+d_5` respectively.

The external-kernel geometry therefore applies to all eight first-deletion fans, not merely the two-to-five fans that were possible under `d_1(P)=3`. The low-weight source prefilter should now reject every source plane with `d_1(P)<4` before the expensive fixed-nine and external-kernel tests.

Profile B itself remains open until those strengthened all-eight-fan conditions are closed analytically or their finite cover is executed with zero survivors.
