# Target C orientation audit for the nine-no-root D=-1, p=2 branch

Date: 2026-09-28

Status: exact orientation-aware narrowing from an executed local computation. The verifier source could not be persisted through the repository connector in this run, so this note does not promote any profile to repository-audited closure.

For an oriented nine-cycle family, each touched triangle block has an exact coefficient constraint space obtained from the two rational quotient-coordinate rows at that block. Empty blocks use that full rowspace. A selected singleton contributes one of the three exact local constraint lines. A selected pair contributes no external coefficient constraint.

The aggregate constraint rowspace has dimension four because the external coefficient code has dimension five. For any four-dimensional aggregate rowspace W on nine coordinates, the required generalized weights (2,4,5,7,8) are equivalent to three column conditions: no zero column, every three columns have rank at least two, and every six columns have rank at least three. These conditions were checked over the rationals.

Selected-pair computation. The prior support search left only representatives 6 and 13. Representative 6 has 729 orientation assignments and representative 13 has 27. Exact subset-span enumeration produced 53,455 rank-four candidate spaces for representative 6 and 1,006 for representative 13. Nine spaces for representative 6 passed the generalized-weight test; none for representative 13 did. For those nine spaces, all necessary complete-row-independence and four-dimensional face-capacity tests failed, including all 135 touched-pair placements. The executed search therefore found no selected-pair state.

Two-singleton computation. The search was enlarged by allowing any empty-block constraint spaces together with at most two singleton-line sources, including combinations that need not correspond to a legal root-state assignment. For each admissible four-dimensional W, every block whose empty constraint lies in W was treated as virtually empty. This can only reduce the virtual complete set, so complete-row independence and face-capacity remain necessary tests for every actual state. All 27 orientations of representative 5, all 27 of representative 12, and all 27 of representative 13 had zero relaxed structural survivors.

Computational result: the selected-pair profile has zero survivors, and representatives 5, 12, and 13 have zero survivors in the two-singleton profile. Ten support representatives remain in the two-singleton profile.

Repository status: because the exact verifier source is not committed, treat these zero-survivor results as executed computational evidence plus a recorded proof reduction, not yet as a fully auditable finite certificate. The next step is either to persist/reimplement the verifier in-repository or independently reproduce these counts, then continue with the remaining ten representatives.