# Target C: close the nine-no-root k=4, D=-1, d_root=0, p=2 selected-pair profile

Date: 2026-09-28

Status: exact closure of the selected-pair subprofile. This does not close the
two-singleton subprofile of the same arithmetic branch.

## Support stage

The executed fail-closed support verifier

`research/verify_target_c_support7_global_segment_relative_nine_noroot_k4_dminus1_d0p2_selected_pair_support_reimplementation_2026_09_28.cpp`

searches a strict superset of every realizable selected-pair state using only
one-sided local-rank consequences, generalized-weight necessary conditions,
complete-row independence, and the four-dimensional face-local rank gap. Its
exact census leaves only two `S_7` support-multiset orbits:

1. `[0123]^3 [0124]^3 [0134] [0234] [1234]`;
2. `[0123]^3 [0124] [0134] [0145] [0234] [0245] [1234]`.

The executed source blob is
`af06b37d42eb417357f9f7e7eac40092c46db7ae`.

## Orientation stage

For each of those two supports, the persisted exact rational verifier

`research/verify_target_c_support7_global_segment_relative_nine_noroot_k4_dminus1_d0p2_selected_pair_orientation_2026_09_28.py`

enumerates all cycle orientations and all rank-four parity-check spaces generated
by touched empty-block quotient spaces.

For a rank-four parity-check matrix `A` on nine coordinates, the companion
lemma proves

`(d1,d2,d3,d4,d5)(ker A) >= (2,4,5,7,8)`

is equivalent to: every column is nonzero, every three columns have rank at
least two, and every six columns have rank at least three. The verifier checks
those conditions over `Q` and then recomputes all five generalized weights
directly for every passing parity-check space.

The recorded exact rational census is:

- support `[0123]^3 [0124] [0134] [0145] [0234] [0245] [1234]`:
  `729` orientation assignments, `53455` rank-four candidate spaces,
  `9` weight-admissible spaces, and `0` structural survivors;
- support `[0123]^3 [0124]^3 [0134] [0234] [1234]`:
  `27` orientation assignments, `1006` rank-four candidate spaces,
  `0` weight-admissible spaces.

For the first support, all nine weight-admissible spaces have exact generalized
weights `(2,4,5,7,9)`; all `144` final selected-pair placements fail
complete-row independence before the capacity test.

All coefficient-space and triangle-row ranks in the orientation verifier use
Python `Fraction` arithmetic.

## Conclusion

There is no nine-no-root state in the

`k=4, D=-1, d_root=0, p=2`

branch whose selected incomplete-root profile is one selected pair.

The remaining finite subprofile in this arithmetic branch is two selected
singletons. It must be closed separately before the entire `D=-1,p=2` branch
is closed.
