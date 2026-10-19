<!-- theorem-state: {"artifact_id":"ART-E9A5A4332059","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# Independent exact-head audit: affine flattening of the PR #958 colour lift

**Verdict: PASS on the exact affine-flattening criterion only.** This is an
independent audit of `GLOBAL-COLOUR-LIFT-AFFINE-FLATTENING-PR958`, not of the
other PR #958 routes. The launch candidate record is unreviewed, and the
theorem artifact index classifies the report and prior audit as unreviewed at
the reviewed base. This audit makes no theorem-state transaction and promotes
nothing. Level I, A, B and C-II stay open; C-I stays closed.

## Source pin and review coverage

- Destination repository: `1337isnot1337/erdos-99`.
- Exact reviewed base: `7d0a450fe66991036541023f95c44c064a04b6a8`.
- Theorem state: `2026-10-15.publication.2`; priority: `public-frontier.3`;
  catalogue: `public-frontier.9`.
- Frozen source PR #958 head: `0a72556e786024c9313c7d6287e26c20c1e9b9b8`.
- Reviewed report:
  `docs/reports/global_colouring_lift_and_planar_rank_barrier_2026-10-12.md`,
  destination SHA-256
  `ab1fc0f0d2cdd3b1f72b801a7b873d56f5db6bed68bfd231f29d88b5945538bc`.
- Existing finite checker:
  `research/verify_global_colouring_lift_rank_2026_10_12.py`, SHA-256
  `c1099da22d605d61de95c987f576116985d9bea02a68517da26ec0ab65c63b72`.
- Prior audit provenance:
  `docs/audits/pr958_autonomous_proof_audit_2026-10-15.md`, destination SHA-256
  `d32fa3e8b2d267d28e2963f653671989aee7584c5e456ca5e3730a7d8fa0b90a`.

The destination artifact index classifies both the report and prior audit as
unreviewed. The prior audit explicitly says it is source-side provenance, not a
destination exact-head review. The migration receipt records an earlier replay
of the finite checker, but that is computational coverage, not an independent
proof audit. The assigned broad card has `existing_checks: []`; the launch
overlap snapshot contains no matching colour-lift review. A private refresh was
attempted before submission, but the installed `gh` rejects `--slurp`, which the
refresh helper requires. Direct live GitHub queries at the final overlap check
found 24 open PRs and no open issues. The relevant PR #958 reviews were read in
full: PR #118 audits squared-distance interpolation and explicitly excludes
the colour lift/flattening criterion; PR #115 audits the finite palette
transversal equivalence and explicitly excludes the colour-lift route. PR #102
audits source-image Hall overlap, which is also separate. Discussion #83's four
current handoffs concern other scopes. No exact flattening audit was present.

## Exact claim and downstream decision

Let `p_1,...,p_n` be distinct points in `R^2` whose affine span is the plane.
Let `z_1,...,z_q` be vertices of a centered regular unit-edge simplex, let
each source label receive one color `c(i)`, and let `t > 0`. The specified
normalized lift is `(p_i, t z_{c(i)})/sqrt(1+t^2)`. The unnormalized lift has
the same affine rank, but does not itself supply strict metric improvement. Its affine dimension is at most two exactly when every
column of the centered color-coordinate matrix is in the column space of the
centered source-coordinate matrix.

This can affect the canonical quantity `D(n)` only if a color assignment
extracted from an actual source makes this particular lift a planar,
full-label, unit-separated strict-diameter competitor. The changed hypothesis
would be a source-derived proper two-coloring whose two classes lie on parallel
lines, with every isolate assigned and retained. If established for a global
minimizer, the endpoint would contradict global minimality; if it fails, the
criterion still leaves other planar rearrangements untouched.

The stopping condition for this bounded investigation is the exact rank proof
plus the finite falsification screens below. Without a separate source-derived
parallel-line coloring theorem, further algebra on this specified lift cannot
change `D(n)`; the next investigation must establish that extraction or build a
different planar endpoint.

## Independent proof reconstruction

Write `P` for the `n x 2` matrix with rows `p_i`, `Z` for the `n x (q-1)`
matrix with rows `z_{c(i)}`, and `J = I - 11^T/n`. Centering removes the
translation of the point set, and uniform positive normalization does not
change affine rank, so the lifted affine dimension is `rank([JP, t JZ])`. Noncollinearity gives `rank(JP)=2`; positivity of `t`
leaves the span of the color columns unchanged. Therefore

`rank([JP, t JZ]) <= 2  iff  col(JZ) subset col(JP)`.

The column inclusion is equivalent to a matrix `A` with `JZ = JP A`. Undoing
centering gives an affine map of the source plane taking each `p_i` to its
assigned simplex vertex. Conversely any such affine map gives that column
inclusion. This proves both directions of the criterion, including its need
for `t > 0` and a rank-two source.

If exactly two distinct colors are used, their centered color matrix has rank
one. Since `JP` has full column rank, `JZ = JP A` forces the affine map's
linear part `A` to have rank one. Its fibers in the source plane are parallel
lines. The two color classes lie on two distinct fibers.
Conversely, two classes lying on distinct parallel lines are the two level
sets of an affine scalar functional; rescaling and translating that functional
maps the classes to the two color vertices. Noncollinearity handles the case
where one class is a singleton: a parallel line through that point is distinct
from the line containing the other class.

If exactly three colors are used, any three vertices of a regular simplex are
noncollinear. Thus `rank(JZ)=2`. Under `JZ=JP A`, the matrix `A` has rank two,
so the associated affine map from the source plane is injective. Each of the
three color vertices has at most one source preimage; hence `n <= 3`. At the
boundary `n=3`, a noncollinear source has `col(JP)=1^perp` in `R^3`, as does
the centered three-color matrix, so the lift can flatten. The obstruction is
specific to this lift and begins at `n=4`.

When the two-color condition holds, planar realization preserves all distances
of the normalized lift. The strict-competitor consequence additionally needs a
finite unit-separated source with diameter `D > 1`, a proper contact coloring,
and a sufficiently small positive parameter: for equal-color pairs require
`t^2 < min(d_ij^2 - 1)`, with the empty minimum interpreted as infinity.
Properness makes this finite minimum positive. For different colors, the
unit-edge simplex gives new squared distance `(d_ij^2+t^2)/(1+t^2)`; for equal
colors it is `d_ij^2/(1+t^2)`. Thus different-color contacts remain unit,
equal-color pairs remain strictly separated, and every old pair above one
contracts. In particular the complete squared diameter is at most
`(D^2+t^2)/(1+t^2) < D^2`. All labels and all pair constraints are retained.
The criterion alone supplies neither this coloring nor its geometric hypothesis.

Integration clarification: the original audit used the unnormalized lift in
its definition but then asserted this normalized strict-competitor consequence.
Without normalization, cross-color squared distances increase by `t^2` and
equal-color distances are unchanged, so that consequence would be false. The
rank criterion is invariant under normalization; the metric conclusion here
uses the normalized unit-edge construction explicitly. Frozen predecessor
report and checker bytes are unchanged.

## Adversarial checks and predecessor boundary

I replayed the frozen finite checker and added an independent exact screen in
[`research-packages/e99-pass-20261018-homelab-10/verify.py`](../../research-packages/e99-pass-20261018-homelab-10/verify.py).
The checker uses exact `fractions.Fraction` Gaussian elimination on every
noncollinear 3- and 4-point subset of the `3 x 3` integer grid. Its three-color
barycentric coordinates are related to regular-simplex coordinates by an
invertible affine map; since this screen tests affine rank only, this change
preserves the checked condition. It checked 1,764 two-color four-point assignments;
240 flatten, and rank two agrees in every case with the parallel-level-line
test. All 456 surjective three-color assignments on noncollinear triples
flatten, while none of 4,536 surjective three-color assignments on
noncollinear four-point sets flatten. These finite screens are controls, not
the proof above.

The inherited controls exercise the useful failures: the alternating two-color
square has lift rank three, while the vertically two-colored rectangle has
rank two and an actual planar strict endpoint. The square prevents an inference
from “two colors” alone; the rectangle confirms the parallel-line case. A
three-color isolate example retains every label in the higher-dimensional
metric descent but does not establish planar realization.

This criterion is distinct from PR #960's squared-distance interpolation rank
obstruction. The PR #958 track correctly limits it to the specified lift. It
does not extract a parallel-line coloring from any global minimizer and does
not exclude arbitrary planar replacements.

## Commands and results

On the reviewed base, the inherited checker passed under the provisioned
CPython 3.14 environment with exact rational and SymPy arithmetic:

```sh
flock /home/cinna/.local/state/erdos99-pass/20261018-luna-xhigh/compute.lock \
  /home/cinna/.local/state/erdos99-pass/20261018-luna-xhigh/venv/bin/python \
  research/verify_global_colouring_lift_rank_2026_10_12.py
```

It passed the full-label lift fixtures (including the isolate), centered-Gram
ranks, square and rectangle lift ranks, the planar flattening control, and the
endpoint-only and infeasible-contraction controls. The independent finite
screen is reproduced by:

```sh
flock /home/cinna/.local/state/erdos99-pass/20261018-luna-xhigh/compute.lock \
  /home/cinna/.local/state/erdos99-pass/20261018-luna-xhigh/venv/bin/python \
  research-packages/e99-pass-20261018-homelab-10/verify.py
```

The screen passed with the exact counts above. Both commands were single-threaded
and run under the shared compute lock.

## Limits and next lemma

No part of this result establishes that a global minimizer has a bipartite
contact graph, that its two color classes are parallel, or that a different
planar rearrangement is impossible. The precise missing source statement for
this route is: every sufficiently large triangle-free global minimizer admits
a proper two-coloring of all labels, including contact isolates, whose classes
lie on parallel lines. A proof would give the planar competitor described
above; a counterexample to that restricted premise would close only this lift
route. The remaining alternative is a different source-derived planar
full-label endpoint satisfying every lower and upper pair constraint.

Prepared by OpenAI Codex (GPT-6 Luna xhigh) as the assigned independent AI-agent
reviewer. This is not human peer review, external validation, a global theorem
audit, or a canonical promotion.
