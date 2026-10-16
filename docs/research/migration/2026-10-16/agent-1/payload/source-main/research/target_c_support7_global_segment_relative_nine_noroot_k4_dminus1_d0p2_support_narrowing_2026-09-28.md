# Target C support narrowing for the nine-no-root D=-1, p=2 branch

Date: 2026-09-28

Status: exact support-level narrowing. The branch remains open.

Current-main arithmetic gives external code dimension five, generalized weights at least (2,4,5,7,8), and at most 24 touched triangle blocks. The root cost p=2 has two possibilities: one selected pair block or two selected singleton blocks.

The support search uses the repaired local-rank rule. Repeated containing support forces local rank two. Without repetition, incidence below two cannot be empty; incidence two or three permits only rank one; incidence at least four permits either rank. Pairwise filters use only necessary consequences of the generalized weights. Complete blocks are required to be independent, and the touched triangle-row span must retain four dimensions modulo the complete rows.

Canonical augmentation gives 121,458 size-nine support orbits. Exactly 103,247 satisfy the touched-block bound. The relaxed selected-pair search leaves 2 support orbits. The relaxed two-singleton search leaves 13 support orbits, including those same 2.

This is a strict relaxation, so every actual state is among those survivors. The subsequent orientation-aware audit closes the selected-pair profile and removes three of the thirteen two-singleton support representatives.

The support census was executed exactly during this run. No new support verifier source is committed with this note.