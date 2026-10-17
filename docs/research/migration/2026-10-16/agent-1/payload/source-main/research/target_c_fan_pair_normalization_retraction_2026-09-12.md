# Target C — retraction of the fan density-floor normalization

**Date:** 2026-09-12  
**Status:** correction/regression; theorem-state authority unchanged.  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The exact bounded-face fan statements

\[
\sum_F {d_F\choose2}\le {T\choose2}-R,
\qquad
20f\le T(T-1)-2R,
\]

remain valid under the audited endpoint-fan scope. However, the subsequent density
floors `1.9359927839...`, `2.5147823986...`, and `2.3036394677...` were derived by
an invalid normalization and are retracted.

The canonical train ledger has `T=O(D)` and `f=O(D)` in the relevant C-II regime.
Therefore division of the exact inequality by `D^2` gives only

\[
0\le (T/D)^2-2R/D^2+o(1),
\]

because `20f/D^2=o(1)`. It does **not** give

\[
20(f/D)\le (T/D)^2-2\Delta_2.
\]

The latter false line was the load-bearing input to all three retracted convex
eliminations. Their constant verifiers checked arithmetic for the false scalar
inequality, not the missing scale conversion, so they do not certify a density floor.

No theorem-state mutation was made: the canonical state already says C-II is open.
The exact fan pair budget may still be useful in a near-Mantel regime where the
right-hand noncrossing-pair surplus is itself only `O(D)`, but no such regime is
established by the present ledger.

**Classification:** rejected density-floor derivation; retained finite fan pair lemma.
