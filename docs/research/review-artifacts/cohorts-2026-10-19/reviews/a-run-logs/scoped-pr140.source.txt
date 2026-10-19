<!-- theorem-state: {"artifact_id":"ART-C9D48BD05340","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-a"} -->
# Independent audit of the balanced-triad relay

**Disposition:** PASS for the fixed-anchor translation lemma and the stated
four-label fixture, at the exact source head below. No canonical claim,
frontier, theorem state, or candidate lifecycle is changed by this audit.

## Exact source and review scope

- Reviewed PR #107 at `12fbd21a8dbded545743579cf3ac34e2c54f1496`.
- Exact investigation: `audit-pr107-balanced-triad-macbook-20261019`.
- Refined scope key: `31b1c50fec63af74ebee4607da509128cb2b095002d3a0abc5601cccc17e4a5d`.
- PR base: `7d0a450fe66991036541023f95c44c064a04b6a8`.
- Baseline state / priority / catalogue: `2026-10-15.publication.2` /
  `public-frontier.3` / `public-frontier.9`.
- Source package: `research-packages/e99-pass-20261018-local-02/`.
- The pinned package files matched these SHA-256 values:

  | File | SHA-256 |
  | --- | --- |
  | README.md | 659c2f4ba8edea3810938161713881d3b4f7421c556b5fc5c00be4ad06e53468 |
  | SOURCES.json | 709f4dac761412ece96a3f793de5fe9ba29fddcf28ae1dd7f0086b1c16e5d19e |
  | TASK.json | 234fff4c1284a0f8e40f111434f677a9a3ef1c9a1adfbcd77d311c928c04c68f |
  | VERIFY.json | ce17e2a215ef07f9af95d959bb9151b3ac5362a25d5036493ee87e1fbe833a85 |
  | verify.py | 21006b00b22e72a6ecca45e222ee356b400693ab3ac5a3cc71095bc3fe7cb82c |

  The six source inputs also matched their pinned bytes at the stated base.

- The package is marked `unreviewed`. The assignment's `existing_checks` list
  was empty (coverage unknown). Live PR #107 had no reviews, and the handoff
  snapshot contained its producer result but no completed audit of this exact
  source. Discussion #83's Target A handoffs concern the separate locked-sector
  work. PR #117's phase-integrated sink bound and PR #102's source-image Hall
  formula are complementary, not dependencies of this geometric claim.

I derived the projection obstruction from the stated contact geometry before
reading PR #107's proof text. I then inspected its full package and replayed its
exact checker from bytes retrieved with `git show` at the pinned head. This
report records a separate proof reconstruction and a separately implemented
pair checker.

The reviewed candidate is the fixed-anchor lemma stated below. Its hypotheses
are three retained unit contacts with balanced planar 120-degree normals and
a common translation of the component while all anchors remain fixed. It can
affect the feasible displacement set at that interface; it could affect the
support cost W(d) only after an actual source embedding. The falsification
experiment was the exact full-pair replay of the four-label fixture plus the
two-anchor and unit-displacement boundary controls. The stopping rule is to
end this review once those proof and pair checks agree; moving anchors and
source extraction are separate questions.

## Reconstructed interface lemma

Let a point `p` belong to a rigid component translated by `t`, while three
exterior labels `q_0,q_1,q_2` remain fixed. Assume
\[
n_i=p-q_i,\qquad |n_i|=1,\qquad n_i\cdot n_j=-\tfrac12\ (i\ne j).
\]

The three planar normals are a balanced 120-degree triad. In an orthonormal
basis with `e=n_0`, the other two are
\(-e/2+\sqrt3 f/2\) and \(-e/2-\sqrt3 f/2\), up to order. Hence
\[
\sum_i n_i=0,\qquad \sum_i n_i n_i^{T}=\tfrac32 I.
\]

For any unit direction `u`, put `x_i=n_i\cdot u`. Then
\[
\sum_i x_i=0,\qquad \sum_i x_i^2=\tfrac32,\qquad -1\le x_i\le1.
\]
At least one `x_i\le-1/2`. Otherwise all `x_i>-1/2`. On
`(-1/2,1]`, `(x_i-1)(x_i+1/2)\le0`, so
`x_i^2\le x_i/2+1/2`, with equality only at `x_i=1`. Summing gives
`3/2=\sum_i x_i^2\le\sum_i(x_i/2+1/2)=3/2`. Equality would force every
`x_i=1`, contradicting `\sum_i x_i=0`. Applying the proved claim to
`-u` also shows that at least one `x_i\ge1/2`.

For `t=ru` with `r>0`, the moved contact has squared-distance change
\[
|p+t-q_i|^2-1=r^2+2r x_i.
\]
For an index with `x_i\le-1/2`, this is at most `r^2-r<0` whenever
`0<r<1`. Thus every such translation violates a retained unit-separation
lower bound. The strict threshold is sharp for lower bounds alone: at a unit
translation in a triad direction, the projection triple is
`(1,-1/2,-1/2)`, and all three moved distances are at least one.

The tangent cone at `t=0` is also `{0}`: its linearized inequalities are
`n_i\cdot v\ge0` for all `i`; summing gives zero, so all three dot
products vanish, and the normals span the plane. The exact nonlinear result is
stronger in the stated range: it excludes every nonzero feasible translation
with length below one. It does not exclude arbitrary lower-bound-feasible
translations of length at least one.

## Full four-label fixture and pair ledger

Take
\[
p=(0,0),\quad q_0=(1,0),\quad
q_1=(-1/2,\sqrt3/2),\quad q_2=(-1/2,-\sqrt3/2).
\]
Its six squared pair distances are:

| Pair | Squared distance | Lower bound (>=1) | Diameter upper bound (<=3) |
| --- | ---: | --- | --- |
| `p,q_0` | 1 | pass, active | pass |
| `p,q_1` | 1 | pass, active | pass |
| `p,q_2` | 1 | pass, active | pass |
| `q_0,q_1` | 3 | pass | pass, active |
| `q_0,q_2` | 3 | pass | pass, active |
| `q_1,q_2` | 3 | pass | pass, active |

Therefore the source has diameter `D=sqrt(3)`, and its unit-contact graph
is the triangle-free star `K_{1,3}`. All three leaf pairs are actual
diameter pairs; no source label is omitted.

For a translation `t=ru` of `p` with all leaves fixed, write
`x_i=n_i\cdot u`. The three lower bounds imply
`x_i>=-r/2` for all `i`. Since some `x_i<=-1/2`, they force
`r>=1`. The three actual-diameter upper bounds imply
`x_i<=1/r-r/2` for all `i`. Since some `x_i>=1/2`, they force
`1/2<=1/r-r/2`, or `r^2+r-2<=0`, hence `r<=1`. Thus
`r=1`. At equality all six inequalities require
`-1/2<=x_i<=1/2`, which gives
`sum_i x_i^2<=3/4`, contradicting `sum_i x_i^2=3/2`.
Consequently `t=0` is the only endpoint satisfying the complete lower and
diameter-upper pair ledger with the three leaves fixed. Leaf-to-leaf pairs
remain at squared distance 3 throughout; the proof checks every changed pair
as well as these unchanged active upper pairs.

## Boundary controls and independent replay

1. **Remove one exterior contact.** Delete `q_0` and translate `p` to
   `(1/10,0)`, keeping `q_1,q_2` fixed. The three remaining squared
   distances are `111/100,111/100,3`; all satisfy the lower bound 1 and the
   diameter upper bound 3. The nonzero move is feasible, so the third fixed
   contact is necessary for the small-motion obstruction.
2. **Unit displacement with the full triad.** Translate `p` to `(-1,0)`.
   The six squared distances are `4,1,1,3,3,3`. Every lower bound passes,
   but pair `p,q_0` violates the actual diameter upper bound 3. This verifies
   both the sharp lower-bound threshold at length one and the need for the
   upper-pair ledger to rule out that endpoint in this fixture.

The independent checker
`research/verify_target_a_balanced_triad_relay_audit_2026_10_19.py` uses exact
rational coefficients for `Q(sqrt(3))` and checks every pair in the fixture
and both controls. The source checker was also replayed unchanged from the
hash-verified pinned bytes. These computations verify the concrete
coordinates and boundary cases; the all-direction result follows from the
proof above, not from sampling directions.

## Scope, comparison, and remaining lemma

This is an exact conditional interface obstruction for a rigid common
translation with all three anchors fixed. The four-label source is a finite
triangle-free fixture, not a global minimizer and not an extracted Target A
monomer domain. The audit does not address moving anchors, rotations, internal
deformation, several moving components, or source-wide extraction. Contact
isolates outside the four-label fixture are not inferred to be rigid. The audit
proves no bound for W(d), d_sc, Delta_Lambda, j_*, or T_Z; the theorem-state
remains unchanged.

Sections 157 and 160–162 treat the specified free five-block architecture;
this balanced exterior interface neither contradicts nor improves its sharp
local rate. PR #117 studies a phase-integrated source-demand/sink ledger, while
PR #102 studies source-image Hall overlap. Neither supplies the fixed-anchor
triad extraction.

The next lemma is to prove or refute that an actual gap-facing label in a
globally derived Target A monomer domain has three fixed balanced exterior unit
contacts under the proposed motion. If an anchor moves, the replacement
architecture must instead audit every changed lower source pair and every
active or inactive diameter upper pair, including contact isolates, before it
can affect the canonical support or Schur endpoint. A source embedding and its
payment into that endpoint remain open.

## Provenance

Source package author: OpenAI Codex, GPT-6 Luna; its proof note and checker
were AI-produced. Independent review: OpenAI Codex `macbook-08` reviewer
session, GPT-6 Luna xhigh, on the exact PR #107 head named above. This is an
agent mathematical audit, not external human peer review. The report and
checker are offered under Apache-2.0; no third-party proof text or source code
is copied.
