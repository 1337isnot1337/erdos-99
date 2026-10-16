# Target C: partial exact Profile-B orbit-100 lift audit

Date: 2026-09-22

Status: exact finite subcensus, unreviewed candidate awaiting promotion. This
artifact records a bounded computation only; it is not a closure of Profile B,
Target C-II, or Level I.

## Input and finite universe

The remaining canonical branch on current `origin/main` is the eight-no-root
`k=6,D=-1,p=9` Profile B branch. The coverage-correct six-row verifier

```text
research/verify_target_c_support7_global_segment_relative_six_noroot_k4_d3_profile_b_singleton_functional_2026_09_22.py
```

enumerates the first 100 of the 20,451 exact `S_7` orbit representatives of
five no-root cycles. For each repaired five-row rank-two parent it enumerates
all 100 admissible added no-root cycles, all rank-two coefficient planes
projecting to that parent, all synchronized six-row states, all five-row
punctures, and the exact common seven-block basis condition. Relation and
functional ranks are certified by the repository's exact rational/local
machinery (the verifier's Mersenne-prime checks include Hadamard bounds).

The companion two-row lift test is

```text
research/verify_target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_profile_b_global_lift_2026_09_22.py
```

It exhausts every rank-two seven-row and eight-row lift of a six-row survivor,
requiring the clean seven-row rank-two fan, deficiency three, compatible
singleton span eight, all synchronized six-row shadows, and then the
eight-row deficiency-three/full-span-nine conditions.

## Exact result for orbit range `[0,100)`

The six-row verifier returned:

```text
five_parent_d=3                         2226
five_parent_full_span_d=3               1340
five_parent_d=2                          248
five_parent_full_span_d=2                  4
parent_extensions                    134400
candidate_P6                         212471
synchronized_P6                      39406
synchronized_d3                       1133
six_d3_capacity_at_least_7              854
all_five_projections_full                502
common_seven_basis_block_set             502
six_full_singleton_span_7                502
```

Thus the range contains 502 exact six-row Profile-B candidates after the
common-basis/full-puncture filters. This is a survivor census, not a theorem
about the remaining 20,351 orbit representatives.

For the first 20 retained candidates (the verifier deliberately stores only
the first 20 examples), the exact global-lift checker returned `False` in every
case. Each failure occurred before any eight-row extension: there was no
seven-row lift satisfying the clean rank-two fan, deficiency-three, and exact
singleton-functional rank-eight test. The per-candidate checks used 99 restored
no-root rows and 123--162 candidate seven-row coefficient planes, with 0 or 2--6
deficiency-three clean seven-row states but zero full-span-eight states.

## What this proves and does not prove

The zero result for these 20 explicit six-row candidates is an exact finite
fact. It proves that those candidates cannot be the six-row shadow of a
Profile-B source through the tested two-row lift. It does **not** imply that the
other 502−20 candidates, nor the remaining orbit representatives, fail; no
global Profile-B conclusion is claimed. A complete cover or a structural
argument is still required before Target C-II can be promoted.

Reproduction of the six-row range is:

```text
python3 research/verify_target_c_support7_global_segment_relative_six_noroot_k4_d3_profile_b_singleton_functional_2026_09_22.py --orbit-start 0 --orbit-end 100
```

The 20-sample lift check was run by importing the verifier's exact
`has_global_profile_b_lift` routine on each stored survivor. It is intentionally
not registered as a full-cover certificate.
