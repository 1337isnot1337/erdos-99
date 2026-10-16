# Target C: close the nine-no-root k=6, D=-2, d_root=1, p=4 six-support slice

Date: 2026-10-03
Base main: `af24b1f7dad924fa564786b2796010bbbdda717e`
Status: exact finite closure of the `m=6` support slice inside the nine-no-root
`k=6, D=-2, d_root=1, p=4` branch. Target C-II and Level I remain open.

Companion verifier:
`research/verify_target_c_nine_noroot_k6_dminus2_d1p4_m6_closure_2026_10_03.py`.

The exact committed verifier was executed after the repository write. Its SHA-256 is

`6319d8e2d75273bb82d2f8679ccf507879e33a535591ff876531a7d6adfa72b8`.

## Structural input

The carried-forward nine-row deletion, depth-three synchronization,
singleton-generator, and support-compression reductions force:

- rank `P=3` on nine external coordinates;
- generalized weights `(d1,d2,d3)(P)>=(3,4,6)`;
- exactly four touched singleton root blocks;
- no touched empty block and no selected pair block;
- every singleton touched by at least four no-root cycles;
- touched-complete root nullity at most one;
- required external relation-rank increment exactly six.

In the `m=6` slice, the only support family is, up to `S_7`, the five
tetrahedral faces of a five-set `W` plus one extra tetrahedron `G`, with
`|G intersect W|=3` or `2`. The only support multiplicity profile surviving
the support/root filters is `(3,2,1,1,1,1)`; the profile
`(2,2,2,1,1,1)` has no survivor.

The verifier regenerates the support/root census directly and scans every
remaining cycle orientation and singleton local direction without further
stabilizer quotienting.

## Exact census

For `|G intersect W|=3`:

```text
support/root skeletons:          61
oriented states:              14823
singleton-direction states: 1200663
rank-three coefficient states: 44664
generalized-weight admissible:   432
external increment census:    {0: 432}
```

For `|G intersect W|=2`:

```text
support/root skeletons:         25
oriented states:              6075
singleton-direction states: 492075
rank-three coefficient states: 25650
generalized-weight admissible:   0
```

Thus the overlap-two support type dies at the generalized-weight test. Every
one of the 432 overlap-three generalized-weight survivors has external
relation-rank increment zero, while a genuine branch survivor requires
increment six. Therefore no `m=6` state exists.

## Exactness

The coefficient calculations are exact integer/rational calculations. Final
root/relation ranks are evaluated modulo the Mersenne prime `2^127-1`, whose
primality is checked by Lucas-Lehmer in the verifier. The largest squared
Euclidean norm of any integer relation row encountered is `46`; the verifier
checks

```text
(2^127-1)^2 > 46^15.
```

Hadamard's inequality therefore makes every modular rank decision exact over
`Q`. The verifier completed with `PASS`.

## Consequence

There is no nine-no-root state with

```text
k=6, D=-2, d_root=1, p=4, m=6.
```

This note claims only the `m=6` closure. Separate work exists for the
`m=3,m=4,m=5` slices; a full `p=4` closure requires carrying those
certificates onto a common current-main branch and auditing them jointly.
