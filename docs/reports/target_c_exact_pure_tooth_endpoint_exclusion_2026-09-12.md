<!-- theorem-state: {"artifact_id":"ART-7AF291FFD7E3","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II — exact pure-tooth endpoint exclusion

**Date:** 2026-09-12
**Classification:** conditional/proof-only endpoint exclusion; noncanonical
**LEVEL I STATUS:** STILL OPEN. C-II REMAINS OPEN.

This note excludes one exact endpoint of the full-core triangular-tooth branch
using the audited-working Type-II phase-gap theorem. It does not claim a
quantitative stability result or an all-regime C-II closure.

## 1. Exact endpoint ledger

Assume the proof-only Section-126 endpoint hypotheses:

\[
\text{one unloaded positive-contact component},\qquad
A=B,\qquad T_{\triangle}=q,\qquad Q^+=0.
\]

The corrected endpoint ledger gives

\[
e_{BB}=k=d_H=s_Z=Q=u_B=c_B=0,\qquad h=q.
\tag{PE.1}
\]

The same endpoint has no bounded nonquadrilateral face, so \(f=0\). Its
occurrence-counted outer walk has \(b=2q\), and the complete stopped-train ledger
therefore gives

\[
T_{\rm train}={b+Q\over2}+2f=q.
\tag{PE.2}
\]

Here \(T_{\triangle}\) is the augmented-cell triangular-face count, whereas
\(T_{\rm train}\) is the number of stopped contact trains; they are not identified
outside this exact endpoint.

## 2. Audited-working Type-II phase gap

The audited-working structural omnibus §142 gives, for every Type-II full-core
sequence,

\[
\liminf_{D\to\infty}{T_{\rm train}-q\over D}
\ge
\gamma,\qquad
\gamma:=2\sqrt{\Delta_2}-{\pi\over2}
=0.333829286933018\ldots>0,
\tag{PE.3}
\]

where \(\Delta_2=\pi/(2\sqrt3)\). The proof uses the exact all-defect identity

\[
T_{\rm train}-q=2f-k
\]

and retains bridges, singleton trains, exceptional faces, and occurrence
multiplicity. §142 is audited-working/proof-only, not a canonical theorem-state
dependency.

## 3. Contradiction at the exact endpoint

Under (PE.2),

\[
{T_{\rm train}-q\over D}=0
\]

for every member of the endpoint sequence. This contradicts (PE.3) once the
sequence is in the Type-II asymptotic range. Therefore, conditional on audited
§142,

\[
\boxed{\text{the exact one-cell, all-two-edge-tooth endpoint cannot occur along
an unbounded Type-II C-II sequence}.}
\tag{PE.4}
\]

No KKT coefficient floor, full-source affine-kernel extension, or deletion of
contact-isolated source points is used.

## 4. Remaining quantitative gap

The exclusion is exact at \(T_{\triangle}=q\), \(Q^+=0\), and one unloaded
component. It does not exclude near-endpoint sequences with

\[
T_{\triangle}=q-o(D),\qquad Q^+=o(D),
\]

because §142 only forces a linear stopped-train surplus
\(T_{\rm train}-q\), which may be supplied by nonexact bounded-face/topological
currency. A closing argument still needs a stability inequality linking
\(T_{\rm train}-q=2f-k\) to the loss \(q-T_{\triangle}\), or a source-preserving
finite diameter descent. The macroscopic inactive-container branch is also
untouched.
