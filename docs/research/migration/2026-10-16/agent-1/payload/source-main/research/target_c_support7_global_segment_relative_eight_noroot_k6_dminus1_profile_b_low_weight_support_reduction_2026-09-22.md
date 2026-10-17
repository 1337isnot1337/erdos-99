# Target C: Profile B low-weight coefficient reduction

Date: 2026-09-22

Status: rigorous structural reduction of the sole remaining eight-no-root `k=6,D=-1,p=9` Profile B. Coefficient words of weight two are impossible. If a coefficient word of weight three exists, deleting the support of a minimum one is forced to a single five-row rank-one endpoint: `D=2,k=4,p=6,d_root=1`, virtual deficiency three, with six singleton replacement functionals of extra rank six. Thus `d_1(P)>=3`; either this one five-row residual occurs or `d_1(P)>=4`, in which case all eight source coordinates are three-clean. Profile B is not closed by this note.

Companion files:

- `research/verify_target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_profile_b_low_weight_support_reduction_2026_09_22.py`
- `research/verify_target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_profile_b_weight3_five_row_residual_2026_09_22.py`
- `research/verify_target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_profile_b_low_weight_filtered_all_clean_fans_2026_09_22.py`

The first checker is pure arithmetic/projective enumeration and has been run locally. The second is a new exact finite audit for the one residual below. The third inserts the proved weight-two exclusion before the existing expensive all-clean-fans source audit.

## 1. Input

The remaining Profile B has

```text
D(B)=-1,
t=8,
k=6,
p=9,
d_root=0,
global virtual deficiency d_v=3,
all nine changed virtual-complete blocks singleton blocks.
```

Its coefficient space is a rank-two plane

```text
P <= Q^8.
```

The all-depth seven-no-root deletion theorem already gives the generalized-weight bounds

```text
d_1(P)>=2,
d_2(P)>=4.
```

The second inequality is important below. If a nonzero word `w in P` has support `S` of size `r<4`, deleting `S` kills exactly one coefficient direction, not both. Indeed `rank pi_S(P)=0` would mean `support(P) subset S`, contradicting `d_2(P)>=4`. Hence

```text
rank pi_S(P)=1.
```

The defect identity gives

```text
D(B\S) = -1 + 2r - 3 = 2r-4.
```

The child has `t'=8-r`, rank-one coefficient space, and therefore

```text
k' = t'-1 = 7-r.
```

Substituting in the exact root arithmetic

```text
D = t' + p' + 3 d_root' - 3 k'
```

shows in both `r=2` and `r=3` cases that

```text
p' + 3 d_root' = 9,
```

so

```text
(p',d_root') in {(9,0),(6,1),(3,2),(0,3)}.
```

Every incomplete row retained from the source is still a singleton row. Let `d` be the child's virtual-canonical complete-row deficiency and let `s` be the extra rank of the actual canonical-complete singleton replacement functionals.

Because the child virtual-complete set is a subset of the source virtual-complete set,

```text
d <= d_v = 3.
```

The rank-one containment theorems below give `d>=2`, so always

```text
d in {2,3}.
```

For an all-singleton rank-one child the established replacement-functional accounting is

```text
D_child >= t' + p' + 3d - 3s.
```

Also trivially

```text
s <= p'.
```

## 2. Weight two is impossible

Assume a minimum word has weight two. Delete its support.

The child has

```text
t'=6,
rank(P')=1,
k'=5,
D_child=0.
```

Moreover the projected coefficient line has support at least

```text
d_2(P)-2 >= 2,
```

so it is a synchronized six-row rank-one state. The exact synchronized six-row containment theorem gives `d>=2`, hence `d in {2,3}`.

The functional inequality requires

```text
s >= 4 + p'/3   when d=2,
s >= 5 + p'/3   when d=3.
```

### `d=2`

For `p' in {9,6,3,0}`, the required extra ranks are respectively

```text
7,6,5,4.
```

The committed exact all-touch six-row audit

`research/verify_target_c_support7_global_segment_relative_six_noroot_k5_alltouch_capacity_2026_09_21.py`

proves that every synchronized six-row rank-one virtual state of deficiency two has singleton capacity at most three. Thus `s<=3`, contradiction in every case.

### `d=3`

For `p' in {9,6,3,0}`, the required extra ranks are

```text
8,7,6,5.
```

If `p'<=6`, this already contradicts `s<=p'`: `7>6`, `6>3`, and `5>0`.

The only remaining possibility would be `p'=9`, requiring `s>=8`. The committed exact audit

`research/verify_target_c_support7_global_segment_relative_six_noroot_k5_d3_capacity8_functional_2026_09_21.py`

exhausts synchronized six-row rank-one `d=3` states with singleton capacity at least eight and proves that the span of all compatible singleton replacement functionals has extra rank at most four. Contradiction.

Therefore

> Profile B has no coefficient word of weight two.

Together with the pre-existing `d_1(P)>=2`, this proves

```text
d_1(P)>=3.
```

## 3. A weight-three word has only one surviving child profile

Now suppose a minimum word has weight three and delete its support.

The child has

```text
t'=5,
rank(P')=1,
k'=4,
D_child=2.
```

The five-row rank-one containment theorem applies without a support restriction and gives `d>=2`; hence again `d in {2,3}`.

The functional inequality requires

```text
s >= 3 + p'/3   when d=2,
s >= 4 + p'/3   when d=3.
```

### `d=2`

The four root possibilities require extra ranks

```text
p'=9 -> s>=6,
p'=6 -> s>=5,
p'=3 -> s>=4,
p'=0 -> s>=3.
```

The last two contradict `s<=p'`. For `p'=6,9`, any realization has singleton capacity at least five. The committed exact audit

`research/verify_target_c_support7_global_segment_relative_five_noroot_k4_p7_d2_functional_2026_09_21.py`

proves that every five-row rank-one `d=2` state with singleton capacity at least five has singleton-functional extra rank exactly two. Thus `d=2` is impossible.

### `d=3`

The four root possibilities require

```text
p'=9 -> s>=7,
p'=6 -> s>=6,
p'=3 -> s>=5,
p'=0 -> s>=4.
```

Again `p'<=3` is impossible from `s<=p'`. At `p'=9`, the exact audit

`research/verify_target_c_support7_global_segment_relative_five_noroot_k4_p7_d3_functional_2026_09_21.py`

proves that every `d=3` state with singleton capacity at least seven has functional extra rank at most six, so `p'=9` is impossible.

Exactly one arithmetic/functional endpoint remains:

```text
p'=6,
d_root'=1,
d=3,
s=6.
```

Since `s=p'=6`, all six retained incomplete rows must be canonical-complete singleton replacements and their six replacement functionals must be independent modulo the canonical relation-column span.

This is the purpose of the new five-row residual verifier. It lowers the old capacity threshold from seven to six and asks exactly whether extra rank six occurs.

## 4. Projective classification after the weight-two exclusion

Write a `2 x 8` generator matrix for `P`, let `z` be the number of zero columns, and split the `8-z` nonzero columns into projective classes of multiplicities `m_1,...,m_h`.

Every nonzero codeword has weight

```text
(8-z) - m_i
```

for one projective class, or full nonzero support when its kernel misses all classes. Thus

```text
d_1(P) = (8-z) - max_i m_i.
```

The arithmetic checker exhausts the integer partitions of `8-z` under

```text
d_2(P)=8-z>=4,
d_1(P)>=3.
```

If `d_1(P)=3`, the number of three-clean coordinates can only be

```text
2,3,4,5.
```

The sharp low-clean profiles are:

```text
2 clean: z=2, projective multiplicities (3,3);
3 clean: z=3, multiplicities (1,2,2);
4 clean: z=4, multiplicities (1,1,1,1).
```

All remaining `d_1=3` profiles have five clean coordinates. If instead

```text
d_1(P)>=4,
```

there is no coefficient word of weight at most three, so all eight coordinates are three-clean.

Therefore the remaining source split is now exact:

1. `d_1(P)=3`, forcing the one five-row `p'=6,d=3,s=6` residual above; or
2. `d_1(P)>=4`, in which case the existing all-clean-fans constraints apply simultaneously to all eight source coordinates.

## 5. New finite target

The smallest unresolved computation is now the five-row rank-one residual, not the full eight-row lift.

The new verifier

`research/verify_target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_profile_b_weight3_five_row_residual_2026_09_22.py`

exhausts all 20,451 five-no-root orbit representatives, all obtainable rank-one coefficient lines, and every virtual-canonical deficiency-three state with singleton capacity at least six. It computes the exact compatible singleton-functional span and records states of extra rank six.

A full-cover zero result would prove `d_1(P)>=4`. At that point every source coordinate is three-clean, so the current fixed-nine/all-clean-fans Profile B audit can be strengthened from "every clean fan" to all eight puncture fans without qualification.

No result of that finite census is claimed here because the persistent execution runner and GitHub Actions runners are currently unavailable. The script has been syntax-compiled locally; the pure arithmetic/projective checker was executed locally and passed.
