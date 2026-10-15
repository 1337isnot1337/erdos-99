# Target C — bounded-face train endpoint fans are crossing-free

**Date:** 2026-09-12  
**Status:** canonical in `2026-10-05.audit.55` as `C-BOUNDED-FACE-ENDPOINT-FAN` after independent reconstruction under the current core convention.  
**LEVEL I STATUS:** STILL OPEN. C-II REMAINS OPEN.

Two complete stopped trains terminating on the same bounded stopping face cannot
cross. Consequently, two trains joining the same pair of bounded stopping faces are
impossible in every direction case: disjoint pairs are handled by the two-face cut,
and crossing pairs by the prefix cut below.

The implication chain is

```text
two trains share a bounded stopping face and cross
  -> close their prefixes through that empty face
  -> Jordan shore contains no loaded endpoint
  -> positive KKT contact resultants along at most two train directions
  -> directions are parallel, or equilibrium is impossible
  -> parallel case gives a mixed-flex contradiction.
```

## 1. Prefix cut

Let `F` be a bounded nonquadrilateral face and let `tau_1,tau_2` be distinct complete
train midpoint paths with one terminal occurrence on `F`. Canonical train geometry
gives simple paths crossing at most once. If they cross at `x`, take the two prefixes
from their terminal midpoints to `x` and close them by an arc in the open interior of
`F`; after smoothing in empty face/rhombus interiors this is a simple Jordan curve
`Gamma` contained in the full source hull `K`.

Let `S` be the nonisolated positive-contact-core vertices in `Int(Gamma)`. A selected
terminal edge crosses the curve, so `S` is nonempty. Active diameter endpoints are
extreme points of `K` and cannot lie in `Int(Gamma)`, hence no active diameter row
crosses the cut. The only contact rows crossing the cut are the selected train edges.

For prefix `i`, all crossed contact edges have one projective direction `u_i` and one
coherent outside-to-inside orientation. Summing the positive KKT equilibrium equations
over `S` therefore gives

\[
\epsilon_1 A_1u_1+\epsilon_2 A_2u_2=0,
\qquad A_1,A_2>0,
\tag{1.1}
\]

where `epsilon_i` records orientation. Nonparallel projective directions cannot satisfy
(1.1). If the directions are parallel, the piecewise velocity `Ju` on `S` and zero
outside annihilates every active contact and diameter row; the canonical mixed-rank
theorem makes this non-Euclidean flex impossible.

Thus two trains sharing a bounded stopping face cannot cross.

## 2. Endpoint consequence

If two trains join the same pair of bounded stopping faces and are disjoint, close
their full paths through the two open face interiors. The same KKT shore sum rules out
different directions and the audited parallel pair-cut theorem rules out equal
directions. If they cross, the prefix argument above applies. Hence no two distinct
complete trains join the same two bounded faces.

The result does not cover outer-face repetitions or local train segments that have not
been globalized to full stopping faces. Contact-isolated source points remain outside
the core KKT sum and are not deleted.

**Classification:** canonical at the exact bounded-face crossing-free scope registered in audit.55.
