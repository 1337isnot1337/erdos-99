<!-- theorem-state: {"artifact_id":"ART-A59AF7A82F4B","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C: p=6 local-rank tags are safe monotone prefilters

**Date:** 2026-10-04
**Repository commit:** `d3e6c2e1fdd3abcea10647a0e98d0d780fceae87`
**State version:** `2026-09-14.audit.51`
**Run type:** audit
**Target:** C
**Starting status:** unreviewed research artifacts
**External literature search:** not used

## Scope

This records the useful surviving result from source branch
`target-c-p6-local-rank-audit-20260927` at exact tip
`347accbe83a3449bf48626f4f45c505a29aa6bce`, then checks the same logic against the
current p=6, e=8 support verifier. No pull request was opened for the source branch.
The p=6 profiles are finite support-level reductions, not a C-II or Level I result.

For an actual-empty block `b`, write `r_b=dim(E_b)` and let `I_b` be its set of
external-cycle coordinates. The support tag is `tau_b=2` when a containing
tetrahedral support repeats and `tau_b=1` otherwise. Repetition forces rank two;
without repetition the actual rank can still be two. Thus `tau_b <= r_b`, and using
the tag as the exact rank would be invalid.

## Why the audited prefilters remain sound

The relevant generalized weights are `(d1,d2,d3)>=(2,4,5)` in a three-dimensional
coefficient space.

- A tagged rank-two block has `|I_b|>=4`, which is necessary because its actual rank
  is two.
- A tagged rank-one block is kept whenever `|I_b|>=2`. If its actual rank is two,
  this only admits extra support sets, since such an actual block requires at least
  four coordinates.
- For two actual local spaces, the necessary support conditions are: rank `(1,1)`
  requires intersection size at least two or union size at least four; `(2,1)`
  requires intersection size at least two or union size at least five; `(2,2)`
  requires intersection size at least two. Replacing an actual rank two by tag one
  weakens these pair filters, so it cannot discard an actual state.
- The quantity `z` counts rank-one empty blocks with exactly two incidences. Any
  rank-two block needs at least four incidences. Therefore every two-incidence
  empty block is genuinely rank one, and the tag-based count of `z` is exact.

The branch report applies this argument to three p=6 certificates. The current e=8
verifier uses the same monotone tags and only counts `z` at incidence two, so the
same proof justifies its zero-survivor result. Its old docstring incorrectly stated
that the tag equals actual rank for every nonrepeated block; that wording is corrected
in the accompanying change.

## Exact verifier runs

Run the listed Python programs from the repository root. The first three audit the
branch's e=3, e=5, and e=6,m=6 cases. The fourth checks the current e=8 case.
These finite verifiers do not certify geometric realization or global optimality.

| Profile | Verifier | Result |
| --- | --- | --- |
| `k=5,D=-1,d_root=0,p=6,e=3,m=4` | `research/verify_target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d0p6_e3_m4_weight_closure_2026_09_26.py` | PASS; exact final rank census `{4:30, 5:1097, 6:835}` |
| `k=5,D=-1,d_root=0,p=6,e=5` | `research/verify_target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d0p6_e5_mod2_closure_2026_09_26.py` | PASS; all 10,623,069 retained phase/quintuple pairs have rank over `F2` greater than three |
| `k=5,D=-1,d_root=0,p=6,e=6,m=6` | `research/verify_target_c_p6_e6_m6_closure_2026_09_26.py` | PASS; all 18,711 retained phase/sextuple pairs have rank over `F2` greater than three |
| `k=5,D=-1,d_root=0,p=6,e=8` | `research/verify_target_c_p6_e8_support_closure_2026_09_26.py` | PASS; three pairwise-compatible support orbits yield three octuples, each with exact `z=4`; none has `z<=3` |

The first three conclusions survive the local-rank issue because their certificate
filters only use rank tags monotonically and rebuild the actual local rows before the
final obstruction. The fourth survives because its only rank-one count is forced by
incidence two, and all tag-based pair filters are weaker necessary conditions.

## Claim classification

This is an audit note, not a theorem promotion. The local-rank monotonicity argument
and finite profile closures remain research evidence; the Level I and Target C-II
statuses are unchanged.
