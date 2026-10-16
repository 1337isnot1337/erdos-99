<!-- theorem-state: {"artifact_id":"ART-1E9C1D8BE14B","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — endpoint train-end balance

**Date:** 2026-09-12  
**Target:** Target C-II  
**Classification:** unreviewed candidate; finite endpoint handoff  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This note extracts the exact first-order balance left by canonical Section 96 at the
new endpoint. It does not claim the missing deformation or exact-triangle theorem.
The useful conclusion is that the three forbidden-gap corridors carry precisely half
of the outer-walk edge mass. If those corridors are visible to the rhombic train
complex, they carry half of its train ends. The only way to avoid that conclusion is a
linear rhombus-free boundary/bridge corridor, which is the surviving geometric
obstruction and is now isolated as a separate target.

## 1. Endpoint constants

Use the canonical Section-96 endpoint notation

\[
\theta_4=2.423405458475313\ldots,
\qquad
\sigma_4:=\sin\theta_4=0.658020712164235\ldots,
\]

so that

\[
\frac32\sigma_4=3\theta_4-2\pi=:\alpha_4
=0.987031068246352\ldots .
\tag{97.1}
\]

Along a wrapping sequence with normalized cell diameter tending to
`\mu_4`, Section 96 gives

\[
\frac{a_D}{D}\to\alpha_4,
\qquad
\frac{s_D+c_D+Q_D}{D}\to0,
\tag{97.2}
\]

and the exact local face identity gives

\[
\frac{L_D}{D}\to4\alpha_4=6\sigma_4.
\tag{97.3}
\]

The three distinguished forbidden gaps have outer contact routes of total length

\[
S_D=3\sigma_4D+o(D)=2\alpha_4D+o(D).
\tag{97.4}
\]

The equality in (97.4) uses the endpoint equality case in the Section-96 route lower
bound. The remaining attachment intervals have total route length

\[
L_D-S_D=2\alpha_4D+o(D)=3\sigma_4D+o(D).
\tag{97.5}
\]

Therefore

\[
\boxed{S_D=\frac12L_D+o(D).}
\tag{97.6}
\]

This is the endpoint train-end balance at the outer-walk level. It uses the new
Section-96 outer-walk charge; the older Section-94 endpoint has a different constant
and does not imply (97.6).

## 2. Finite rhombic-boundary accounting

Let `\mathcal R_D` be the strict-rhombus complex in the harmonic carrier, including
all components and hole boundaries, and let

\[
B_D:=\text{the number of physical boundary-edge occurrences of }\mathcal R_D.
\]

The canonical train theorem gives

\[
\boxed{B_D=2T_D,}
\tag{97.7}
\]

where `T_D` is the number of local train segments. Every edge occurrence of the outer
contact walk that is incident to a strict rhombus is one boundary occurrence of
`\mathcal R_D`.

Let `b_D` count outer-walk edge occurrences that are incident to no strict rhombus.
Split it as

\[
b_D=b_D^{\mathrm{bridge}}+b_D^{\mathrm{exc}},
\tag{97.8a}
\]

where `b_D^{bridge}` counts edge occurrences whose two sides are in the outer face
(equivalently, bridge occurrences in the induced carrier graph), and
`b_D^{exc}` counts occurrences facing a bounded nonquadrilateral face. The exact
Section-82 face ledger gives

\[
\sum_{f\text{ nonquadrilateral}}\deg f
\le5Q_D.
\]

Consequently the finite boundary accounting inequality is

\[
\boxed{b_D^{\mathrm{exc}}\le5Q_D,\qquad
L_D\le B_D+5Q_D+b_D^{\mathrm{bridge}}.}
\tag{97.8}
\]

This inequality allows repeated outer-face occurrences and bridges. It is therefore
safe in the current carrier topology.

If `b_D=o(D)`, (97.2), (97.3), and (97.8) imply

\[
B_D\ge L_D-o(D).
\]

The reverse inequality is the canonical Section-82/89 boundary estimate
`B_D\le L_D+5Q_D`. Hence `B_D=L_D+o(D)` and

\[
\frac{B_D}{D}\to6\sigma_4,
\qquad
\frac{T_D}{D}\to3\sigma_4.
\tag{97.9}
\]

In this rhombically visible subcase, the three distinguished corridors contain

\[
3\sigma_4D+o(D)=T_D+o(D)
\tag{97.10}
\]

train-end edge occurrences, exactly half of all `2T_D` train ends. At least half of
these occurrences belong to distinct trains, and at least one of the three corridors
is incident with `\sigma_4D/2-o(D)` distinct train segments. More refined endpoint
pairing would require an order theorem for trains whose two ends lie on the same
special corridor; (97.10) deliberately does not assume such a theorem.

## 3. The actual remaining dichotomy

The endpoint balance gives the following exact split:

```text
Section 96 endpoint
  -> three corridor length = 3 sigma_4 D + o(D)
  -> outer-walk length = 6 sigma_4 D + o(D)
  -> corridors carry half of the outer-walk edge mass
  -> either
       (a) b_D=o(D), so half of the rhombic train ends lie on the corridors, or
       (b) b_D=Omega(D), so a linear rhombus-free/bridge boundary corridor survives.
```

Case (a) is the quantitative interaction input needed by the ordered-grid route. The
three corridors are near-geodesic unit paths, while the complete ordered grid lies in
the same carrier. A closing theorem must show that the half-mass endpoint placement
forces either a forbidden three-phase junction or a source-preserving strict decrease.

Case (b) is not a bookkeeping artifact. Since `Q_D=o(D)`, (97.8) shows that
`b_D=Omega(D)` forces `b_D^{bridge}=Omega(D)`: a linear number of outer-face bridge
occurrences survives in the induced carrier graph. The canonical positive-contact
bridge theory controls a bridge only after its cut is interpreted in the full
positive graph; a local carrier bridge may have an alternate route through other
attachment cells. The binding doubled near-geodesic-corridor regression permits a
linear boundary path with little rhombic area attached to it. Any argument that
silently replaces `L_D` by `B_D`, or silently promotes a local bridge to a universal
full-source bridge, would therefore be invalid.

## 4. Candidate closing implication

The precise next lemma is

\[
\boxed{
b_D=\Omega(D)
\Longrightarrow
\text{a source-preserving deformation decreases the actual global diameter,}
}
\tag{97.11}
\]

under the canonical contact-minimal and diameter-pair-minimal normalization, with all
contact-isolated points retained. If (97.11) is proved, the remaining `b_D=o(D)`
branch has a linear family of ordered train ends on the three near-geodesic corridors,
and the corresponding train-grid interaction theorem is the only remaining
quadratic-core obligation.

No KKT coefficient lower bound is needed for (97.11), but the deformation must retain
all old unit contacts and all source points. A bridge count alone is insufficient:
the intervening two-edge-connected blocks can carry nontrivial geometry, as recorded
in the repository's bridge-route regression.

## 5. Claim classification and dependencies

| Claim | Classification |
|---|---|
| endpoint split (97.6) | unreviewed candidate pending endpoint equality audit |
| boundary accounting (97.8) | proved finite candidate |
| train-end half-mass conclusion under `b_D=o(D)` | proved conditional candidate |
| deformation implication (97.11) | open target |
| C-II closure | open |

Dependencies are canonical `C-WRAP-OUTER-WALK-GAP`,
`C-HARMONIC-CARRIER-QUAD`, `C-HARMONIC-TRAIN-BUDGET`, and
`C-EXPLICIT-ORDERED-GRID`. The note retains bridges, repeated outer-face edges, and
contact-isolated source points throughout.

