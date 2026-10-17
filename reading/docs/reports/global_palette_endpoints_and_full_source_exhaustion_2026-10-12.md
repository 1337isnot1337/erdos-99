> Generated reading edition · [exact source](../../../docs/reports/global_palette_endpoints_and_full_source_exhaustion_2026-10-12.md) · source SHA-256 `e0ac1c388070ae91c00e716d1b511924978c029ba90797a6ba562b12e811450c`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-AB692686F9CB","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# Erdős Problem #99 — finite global endpoints and full-source exhaustion

**Date:** 2026-10-12
**Repository commit:** fddaa626be2c45cf7199007e34851f30457f0cb6
**State version:** 2026-10-10.audit.234
**Run type:** global replacement research / certified regression
**Target:** Level I, whole-source endpoint methods
**Starting status:** open; no claim about a new global minimizer
**Active prompt:** `docs/prompts/erdos_problem_99_GPT6_ASTRA_FULL_SOLUTION_PROMPT.md`
**External input:** exact rational Packomania coordinate data, reused with hashes
**Computation:** `research/verify_global_palette_transversal_2026_10_12.py`

## LEVEL I STATUS

**STILL OPEN.** The general endpoint formulation is an **unreviewed candidate**;
the finite failure is a **regression**. No canonical frontier is promoted.

## 1. Global endpoint rather than a local flex

Given a complete n-label source P of diameter D, assign a finite set O_i of
possible new planar positions to each label. A strict competitor exists within
these palettes exactly when there are choices y_i in O_i with

$$
1\le |y_i-y_j|<D\quad\text{for every }i\ne j.
$$

Make a graph with vertices (i,a), one for each label/option pair. Join any two
options of the same label, and join options of different labels when their
distance is less than one or at least D. The desired endpoint is exactly an
independent transversal, one vertex from every label class.

```text
full-source independent transversal -> n planar unit-separated endpoint sites
of diameter < D -> contradiction if the source is a global minimizer.
```

The endpoint may change every contact and every diameter pair. No feasible
interpolating path, source isometry, common carrier or pinned boundary is
required. This is the reason it can improve strict local minima.

This equivalence is not a Level I proof: one must still supply palettes and
prove an independent transversal for every sufficiently large triangle-free
global minimizer. An assignment for a few labels does not meet that endpoint.

## 2. Exact arithmetic and complete finite search

For interval coordinates the implementation constructs two Boolean systems.

- A sufficient system permits an option pair only when its distance is certified
  to satisfy both bounds. A satisfying assignment gives a strict competitor.
- A permissive system forbids an option pair only when it is certainly invalid.
  Every genuinely feasible geometric assignment survives this system. Proving
  it unsatisfiable therefore excludes every palette assignment, even when some
  distance comparisons are unresolved by the intervals.

Arc consistency deletes a colour only if it has no compatible surviving choice
at a neighboring label. Such a deletion cannot remove a satisfying assignment.
When propagation stops with unresolved choices, the solver branches on every
remaining choice of one label and repeats. Each branch fixes a non-singleton
domain, so the finite recursion terminates. Rejecting every branch is an exact
exhaustion. No numerical solver status is used as an infeasibility certificate.

An independent enumeration checks the propagation/branching kernel on small
unrestricted, forbidden-pair, and odd-cycle systems. The final geometric
assignment is separately checked over every chosen pair.

## 3. One palette crosses the canonical local obstruction

Let P consist of the vertices of the regular unit 43-gon. Its exact radius and
diameter are

$$
R=\frac1{2\sin(\pi/43)},\qquad
D=\frac1{2\sin(\pi/86)}.
$$

Canonical `docs/theory/02-nonlinear-and-regressions.md`, Proposition 13.1,
supplies strict local diameter minimality modulo congruence, since 43 is prime.
Its contact and diameter graphs are both 43-cycles; the contact graph is
triangle-free. Proposition 14.1 supplies its stress identities, though those
identities are not used in the endpoint certificate.

Choose alpha=17/20 and the three translation vectors

$$
u_0=(1,0),\quad
u_1=(-1/2,\sqrt3/2),\quad
u_2=(-1/2,-\sqrt3/2),
$$

with options O_i={alpha p_i+u_0, alpha p_i+u_1, alpha p_i+u_2}. The sufficient
system finds an assignment in 13 search nodes. The independent full-pair check
certifies all 903 pairs, minimum squared distance greater than 1.01 and endpoint
squared diameter less than 185. The source has D^2>187.4262. Thus this is a
genuine planar strict competitor despite the source's local obstruction.

No path feasibility is claimed. The certificate is finite and concerns a
known nonglobal source; it is not evidence of a triangle-free global minimizer.

## 4. Retaining the whole population defeats every assignment of that palette

Add 132 strict interior isolates to the same rim. Their decimal coordinates
come from [the primary 132-point table](https://www.packomania.com/cci/txt/cci132.txt),
treated as exact rational data. The verifier recomputes their minimum pair
distance and applies a rational strict inflation. No optimality assertion about
the table is imported.

The exact source has 175 labels. Its only unit contacts and actual diameter
pairs remain those of the rim. The verifier checks the interior pairs directly;
the radius gap greater than one certifies every rim/interior lower bound, and
the sum of radii less than D certifies every cross upper bound. Exact sine chord
identities handle the unit and diameter equalities on the rim; all other rim
chords have strict bounds. Consequently no isolate is omitted or silently
treated as a contact point.

For precisely the same alpha and palette, the permissive full-source system has
2039 constrained label pairs and is unsatisfiable in four exhaustive search
nodes. This certifies failure of **all 3^175 possible assignments**, not failure
of one numerical colour choice. It makes no claim about other alpha values,
other palettes, or arbitrary planar endpoints.

The filled source itself is also nonglobal. An independent 175-label rational
packet from [the primary 175-point table](https://www.packomania.com/cci/txt/cci175.txt),
again strictly rescaled from its measured minimum distance, has every one of
15225 pair distances greater than one and squared diameter less than 183.2352,
strictly below the source. The verifier checks that alternative independently.
The palette therefore misses an existing complete-source strict competitor.

This is a method-level regression: improving the loaded rim can coexist with
failure of every corresponding full-source choice. Neither omission of inactive
points nor a finite restricted search may be used to infer global closure.

## 5. Provenance and verification

The destination retains the attribution record with both primary URLs and
expected SHA-256 values. It does not include the Packomania coordinate tables.
The inspected [Packomania homepage](https://www.packomania.com/) and
[submission-format page](https://www.packomania.com/hints.html) did not provide
an explicit redistribution grant. The 132/175 computations therefore require
authorized coordinate files supplied through the external fixture-directory
argument; no source-branch fixture path is assumed.

The 43-gon endpoint is independently reproducible without external tables:

```sh
python3 research/verify_global_palette_transversal_2026_10_12.py --core-only
```

The directed-integer interval helper used by the destination verifier is
included at research/exact_trig_intervals_2026_10_12.py. Machin's identity and
alternating arctangent sums enclose pi; Taylor remainders enclose sine and
cosine. Interval operations round outwards on a 10^50 grid, and square roots
use integer lower/upper bounds. No floating point participates in
certification. Numerical mixed-integer probes were discovery material only;
the final conclusions do not depend on them.

To replay the 132/175 source controls after obtaining authorized local data:

```sh
python3 research/verify_global_palette_transversal_2026_10_12.py \
  --fixture-dir <local-authorized-Packomania-data-directory>
```

The verifier checks both expected SHA-256 values before parsing.

| Claim | Classification | Exact limit |
| --- | --- | --- |
| Independent transversal iff a finite palette endpoint exists | Unreviewed candidate | Needs a complete palette/transversal theorem for global minimizers |
| Regular 43-gon has a finite three-translation strict competitor | Unreviewed candidate | Known nonglobal finite source |
| Same palette admits no full 175-label endpoint | Regression | One exact alpha/palette, all assignments exhausted |
| Independent 175-label strict competitor | Regression witness | Refutes global optimality of the fixture, not Level I |
| Small-palette closure inferred from rim improvement | Rejected attempt | Full-source incompatibility certificate |

## 6. Continuing global obligation

The remaining endpoint is still an n-point planar strict competitor for every
sufficiently large triangle-free global minimizer, or an unbounded family of
triangle-free global minimizers with independently proved optimality. The
finite palette method can validate rearrangements across local barriers, but
the fixed three-translation family does not supply a universal extraction.
The complete inactive population must participate in any next construction.

## Autonomous audit (2026-10-15)

The [PR958 AI audit](../audits/pr958_autonomous_proof_audit_2026-10-15.md)
records the complete proof and certificate review, scope, source provenance and
JSON proof replay. All checkers require assertions and refuse optimized Python.
The reports remain noncanonical and unreviewed. The source AI audit is provenance,
not a destination exact-head review; no canonical claim is promoted.
