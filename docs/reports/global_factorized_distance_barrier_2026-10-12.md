<!-- theorem-state: {"artifact_id":"ART-2DFEAD12DFB0","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# Global factorized-distance transformations: an exact barrier

**Date:** 2026-10-12
**Repository commit:** `ab6dd3336f9f8d440f2bada76edb32153391cddc`
**State version:** `2026-10-10.audit.234`
**Run type:** closing-proof exploration and regression
**Target:** independent whole-source Level I route
**Active prompt:** `docs/prompts/erdos_problem_99_GPT6_ASTRA_FULL_SOLUTION_PROMPT.md`
**Classification:** unreviewed candidate; rejected universal transformation route
**Level I:** STILL OPEN

## 1. Global objective and route selection

The objective is the literal claim in `docs/problem/statement.md`: for every
sufficiently large cardinality, every global minimizer has a unit equilateral
triangle. No Target A/B/C intermediate result is assumed in this report.

The run deliberately compares different global mechanisms before developing one:

| Mechanism | Intended implication | Initial assessment |
| --- | --- | --- |
| Finite inversion or other factorized remetrization | Open all shortest pairs relative to every longest pair, then normalize to unit separation | Exact obstruction proved below; universal route rejected |
| Continuous affine deformation | Lower the maximum/minimum distance ratio | Canonical tensor identity already obstructs a universal argument; not reopened |
| Changing contacts by a finite whole-source replacement | Retain source cardinality and make every pair strictly shorter than the old diameter | Still a direct global route; endpoint must check every lower and upper pair |
| Convex interpolation of Euclidean distance matrices | Contract every long pair while keeping unit pairs fixed | Works in higher dimension; planar realization is an unproved essential bridge |

The proposed transformation chain was

```text
triangle-free source admits a factorized remetrization improving max/min
 -> same-cardinality unit-separated planar source of diameter < D
 -> contradiction to global optimality.
```

The first implication is false even for nonglobal configurations with arbitrarily
large regular rims. This report does not assert that those configurations are
globally optimal or meet every necessary population condition of a global source.

## 2. Balanced-degree product obstruction

Let a finite planar source `P={p_i}` have minimum distance one and diameter `D>1`.
All source labels, including contact isolates, are retained. Suppose there are
nonnegative weights `a_e` on actual unit contacts `C` and `b_f` on actual diameter
pairs `H` such that

\[
\sum_{e\in C}a_e=\sum_{f\in H}b_f=1,
\qquad
\sum_{e\ni i}a_e=\sum_{f\ni i}b_f\quad\text{for every label }i.
\tag{1}
\]

Suppose a new Euclidean placement `Q={q_i}` obeys, for every source pair,

\[
|q_i-q_j|=s_i s_j |p_i-p_j|,\qquad s_i>0.
\tag{2}
\]

Then

\[
\frac{\operatorname{diam}Q}{\min_{i\ne j}|q_i-q_j|}\ge D.
\tag{3}
\]

In particular, unit normalization of `Q` cannot yield a strict-sub-`D`
competitor. This is a finite statement, with no smallness restriction, no motion
interval assumption, and no omission of new active pairs.

### Proof

For an old unit pair, its new length is `s_i s_j`; for an old diameter pair,
its new length is `D s_i s_j`. Taking weighted logarithms gives

\[
\begin{aligned}
\sum_H b_{ij}\log |q_i-q_j|
 -\sum_C a_{ij}\log |q_i-q_j|
 &=\log D
 +\sum_i\left(\sum_{H\ni i}b_f-\sum_{C\ni i}a_e\right)\log s_i\\
 &=\log D.
\end{aligned}
\]

Writing `M=max |q_i-q_j|` and `m=min |q_i-q_j|`, both positive, each weighted
average on the left is bounded above or below by `log M` or `log m`, respectively.
Thus `log(M/m)>=log D`. This proves (3). Extra source pairs can only increase
`M` or decrease `m`; their omission from the weighted certificate does not omit
them from the claimed inequality. ∎

Equivalently, the weighted geometric-mean quotient of the old diameter pairs and
the old unit pairs remains exactly `D`.

## 3. Arbitrarily large regular-rim obstruction

For each integer `m>=4`, take a regular `m`-gon of side length one. It is
unit-separated and triangle-free. Its diameter is

\[
D_m=\begin{cases}
1/\sin(\pi/m),&m\text{ even},\\
\cos(\pi/(2m))/\sin(\pi/m),&m\text{ odd}.
\end{cases}
\]

Give each rim edge contact weight `1/m`. Every rim vertex has contact incidence
`2/m`. For odd `m`, its `m` diameter edges have weight `1/m`, again giving
incidence `2/m`. For even `m`, its `m/2` antipodal pairs have weight `2/m`,
also giving incidence `2/m`. This proves (1).

One may add any finite collection of interior points for which the full source
remains unit-separated and has diameter `D_m`. Give every new label zero incidence
in both weighted graphs. The same certificate applies to the complete augmented
source, regardless of whether its extra labels are contact-isolated or have their
own contacts. Triangle-freeness of an augmented example must be checked separately;
the regular rim alone is triangle-free for all `m>=4`.

This is an obstruction family, not a family of global minimizers.

## 4. Why inversion belongs to the obstructed class

For an inversion with center `c` avoiding the finite source and radius parameter
`R>0`,

\[
I(p)=c+R^2\frac{p-c}{|p-c|^2},
\qquad
|I(p)-I(q)|=\frac{R^2|p-q|}{|p-c||q-c|}.
\]

The squared identity follows immediately by expanding the squared norm of the
displayed difference. Thus (2) holds with `s_i=R/|p_i-c|`. Similarities and
reflections also have the form (2); compositions preserve the form because the
positive factors multiply at each label. In the complex plane, a finite-valued
Möbius transformation has the explicit identity

\[
\left|\frac{az_i+b}{cz_i+d}-\frac{az_j+b}{cz_j+d}\right|
=\frac{|ad-bc|\,|z_i-z_j|}{|cz_i+d|\,|cz_j+d|},
\]

so it has the same obstruction directly. A source at a pole is not a finite
Euclidean competitor.

## 5. Independent checks and scope limits

`research/verify_global_factorized_distance_barrier.py` checks the balanced
incidences for every regular rim size from 4 through 101, and checks the exact
product cancellation for arbitrary positive rational vertex factors. It also
uses actual rational coordinates for the unit square and several inversion poles,
checks the inversion identity on every pair, and checks the full-source normalized
diameter inequality. The combinatorial tests alone are not embedding certificates;
the proof supplies the regular-polygon geometry and the rational square tests use
actual Euclidean coordinates.

The analytic theorem applies to any already realized placement satisfying (2).
It does not claim arbitrary vertex factors admit a planar realization. It does not
assert that balanced incidence follows from KKT equilibrium. It does not rule out
nonfactorized deformations, changing the rim, or replacing the entire packing.

No external theorem is imported. The public problem page was checked for the
literal quantifier and current public open status:
<https://www.erdosproblems.com/99>. The calculations above are independent.

## 6. Exact graph alternative for every source

The product barrier has a constructive converse for **abstract pair lengths**.
This is not a converse about planar coordinate realizability.

For a finite source with `D>1`, build a directed graph with two states `(i,+)`
and `(i,-)` at every source label. Each contact `ij` contributes arcs

\[
(i,+)\longrightarrow(j,-),\qquad(j,+)\longrightarrow(i,-),
\]

and each diameter pair contributes arcs

\[
(i,-)\longrightarrow(j,+),\qquad(j,-)\longrightarrow(i,+).
\]

Exactly one of the following holds.

1. There is a directed cycle. Its projected closed walk alternates actual contact
   and diameter edges. Give each contact and diameter edge the number of its
   occurrences in this walk, divided by half the walk length. Every appearance
   of a source label joins one edge of each color, so the two normalized weighted
   incidences agree at every label. This is the certificate (1), and all positive
   endpoint-factor remetrizations are blocked globally.
2. The directed graph is acyclic. There are half-integer values `z_i` satisfying

   \[
   z_i+z_j\ge1\quad(ij\in C),\qquad
   z_i+z_j\le-1\quad(ij\in H).
   \tag{4}
   \]

   Consequently, for some sufficiently small `lambda>0`, the abstract pair lengths

   \[
   \widetilde d_{ij}=e^{\lambda(z_i+z_j)}|p_i-p_j|
   \tag{5}
   \]

   are all at least one and all strictly below `D`. These are actual inequalities
   on the complete finite array, including pairs involving contact isolates. No
   Euclidean or planar realization of the array is asserted.

### Proof of the acyclic construction

Let `w(s)` be the longest directed-path length from state `s` to a sink. Every arc
`s->t` satisfies `w(s)-w(t)>=1`. The state flip `bar(s)` switches its sign, and
every arc `s->t` has the reversed flipped arc `bar(t)->bar(s)`. Define

\[
z_i=\frac{w(i,+)-w(i,-)}2.
\]

For a contact arc, averaging its path inequality with the reversed flipped arc
gives `z_i+z_j>=1`. The same calculation on a diameter arc gives
`-(z_i+z_j)>=1`. Thus (4) holds.

The old unit lengths in (5) grow strictly and every old diameter shrinks strictly.
Every inactive pair originally lies strictly between one and `D`. By finiteness,
all of those strict margins remain valid for a sufficiently small common positive
`lambda`. All source labels occur in this margin argument, whether or not they
occur in the two active graphs.

A directed cycle and (4) cannot coexist: summing (4) along the alternating walk
would assign the same vertex sum both a strictly positive and a strictly negative
edge sum. Together with the two constructions this proves the exact alternative.
It also proves that (1) exists if and only if the directed graph contains a cycle:
if (1) existed in the acyclic case, weighting (4) would contradict incidence
equality. ∎

The implementation `research/global_factorized_graph_alternative.py` returns an
explicit alternating walk or the rational `z_i`; it uses no numerical optimization.

## 7. Physical regression against abstract-to-planar inference

For the six-point pentagon-plus-center fixture already recorded in
`docs/problem/literature_baseline.md`, the actual contacts form `K_{1,5}` and every
actual diameter lies on the outer pentagon. The two-state graph is acyclic.
An explicit valid choice is

\[
z_i=-1/2\text{ on the five rim labels},\qquad z_{\rm center}=3/2.
\]

Its center-to-rim distances in (5) become `e^lambda`, while all rim distances are
multiplied by `e^-lambda`. For small positive `lambda`, normalizing by the new
minimum distance gives center-to-rim distances one and a pentagon of circumradius
`e^(-2lambda)<1`.

That normalized six-point array has no planar realization. The five rim points,
whose full mutual distance array is prescribed, form that scaled regular pentagon
up to a Euclidean isometry. A point equidistant from all five in the plane must be
its circumcenter, at distance `e^(-2lambda)`, rather than one. In three dimensions,
an apex at height `sqrt(1-e^(-4lambda))` does realize it.

This fixture is already known to attain the six-point planar diameter minimum in
the supplied baseline; the nonrealizability argument itself does not need that
global-optimality premise. It prevents promoting the graph alternative's abstract
improvement to a planar global competitor. Neither this example nor the graph
alternative settles the eventual quantifiers.

## 8. Frontier effect and continuation

**Promotion recommendation:** preserve as an unreviewed research artifact. No
canonical state or current Target A/B/C endpoint changes.

The universal inversion/Möbius route is rejected by an exact global product
invariant. A subsequent argument must change nonfactorizable distance data or
replace source labels' positions, rather than treating a large finite conformal
change as a cure for a first-order obstruction.

The next global question is whether a contact-changing replacement can retain all
source labels while shortening every old and newly active longest pair. Higher
dimensional distance-matrix interpolation is a separate candidate mechanism; its
planar realization must be proved rather than inferred from convex feasibility.

## Autonomous audit (2026-10-15)

The [PR #960 AI proof audit](../audits/pr960_autonomous_proof_audit_2026-10-15.md)
records the full argument, dependencies and computational repairs. The checkers
require assertions and refuse optimized Python. This remains noncanonical;
the destination independent exact-head AI-agent mathematical audit required for consequential promotion is not completed.
