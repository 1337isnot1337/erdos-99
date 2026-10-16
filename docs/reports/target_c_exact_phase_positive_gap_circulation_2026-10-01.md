<!-- theorem-state: {"artifact_id":"ART-5121C726D56F","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II — positive gap circulation blocks a spanning-tree leaf release

**Phase 2 preservation provenance:** PR #594, branch swarm/gap-reaction-cut-20261001, audited source head 02d4cc04e2df2e0f0aa1eb2a9ec3cf21cc53f18f. Its algebraic no-bridge circulation overlaps the current-main exact-phase circulation report from PR #648; this copy retains the additional finite chart-isolation analysis and labeled regression at unreviewed status.

`candidate lemma -> signed exact-phase diameter derivative rows -> a directed-cycle
geometry obstruction or a finite strict sub-D source competitor -> Level I`

**Date:** 2026-10-01<br>
**Starting shared HEAD:** `af823f5f8b998aadf652df9aed01b2dbc2882e75`<br>
**Research base:** `14b2c4cfd7e4ff828fbe62a8cfefebb4ca121e79`<br>
**State version:** `2026-09-14.audit.51`<br>
**Mission:** exact-phase gap graph, positive reactions, and finite leaf release.<br>
**Classification:** proved candidate awaiting promotion; exact labelled-geometry regression.<br>
**LEVEL I:** OPEN. C-I is closed; C-II remains open.<br>
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md`.<br>
**Literature:** none imported.

## 1. Dependencies and scope

Canonical inputs are normalized KKT equilibrium (shared theory, Theorem 4.1),
full actual contact/diameter support of a relative-interior stress on the
lexicographic representative (`56-ci-restored-frontier.md`), and mixed rigidity
on the nonisolated positive-contact core (`57-zr-zf-rigidity-audit.md`).
All contact-isolated source points are retained.

The route-local inputs below are **unpromoted**, and the application to that
route is conditional on their exact cut/chart hypotheses:

- `target_c_complete_grid_rank_switching_2026-10-01.md`: exact contact-preserving
  train shears, interval supports, and full derivative rank on a proper shore;
- `target_c_exact_phase_gap_graph_connectivity_2026-10-01.md`: the gap-incidence
  isomorphism and connectedness;
- `target_c_witness_cell_blocker_dichotomy_2026-10-01.md`: nonzero axial
  two-bar reactions at the exact-phase interfaces.

The new algebraic statements below are proved directly from explicit hypotheses.
They neither require nor promote the entire fixed-star extraction chain.

## 2. Positive-circulation theorem

Let one exact-phase shore have $m\ge1$ independent train coordinates.
For each actual diameter row write

\[
M_h=c_h\mathbf1_{[a_h,b_h]},\qquad
c_h=\sigma_h(r_h\cdot Ju).
\]

Discard empty rows and rows with $c_h=0$. Assume the remaining matrix has
rank $m$, and that a normalized KKT stress has $\beta_h>0$ on every
actual diameter. The signed gap graph has vertices $0,\ldots,m$. Put

\[
p_h=a_h-1,quad q_h=b_h,quad
f_h=\beta_h|c_h|>0.
\]

Orient its edge from $p_h$ to $q_h$ when $c_h>0$, and in the reverse
direction when $c_h<0$. Then:

1. $f$ is a strictly positive circulation;
2. the directed graph is strongly connected;
3. every actual nonzero row lies on a directed cycle;
4. every nonempty proper vertex cut has at least one edge in each direction;
5. the full multigraph has no bridges and has at least $m+1$ edges;
6. the diameter rows positively span $\mathbb R^m$.

### Proof

For every train shear all old contact first variations vanish. Pairing the
velocity with KKT equilibrium gives

\[
M^{\mathsf T}\beta=0. \tag{1}
\]

This uses stationarity at the actual source, rather than a generic stress on
an abstract graph. There is no diameter multiplier floor.

Apply the isomorphism

\[
L$x$=(x_1,x_2-x_1,\ldots,x_m-x_{m-1},-x_m)
\]

to the row sum in (1). Since

\[
L(\mathbf1_{[a,b]})=e_{a-1}-e_b,
\]

the resulting equation is exactly

\[
\sum_h f_h(e_{\mathrm{tail}(h)}-e_{\mathrm{head}(h)})=0. \tag{2}
\]

Summing (2) over a vertex set equates the outgoing and incoming positive
flows. Thus every nontrivial cut crossed by any edge is crossed in both
directions. Full rank makes the underlying graph connected, by the gap-rank
identity. If there were several strongly connected components, a source
component of the condensation DAG would have an outgoing edge and no
incoming edge, contradicting (2). This proves strong connectivity and the
cut assertion. Every directed edge therefore has a return path. No bridge
can lie on such a cycle. Every vertex has an outgoing edge, so there are
at least $m+1$ edges, counting multiplicity.

Finally, (1) with strictly positive coefficients expresses the negative of
each row as a positive combination of the other rows. Consequently the
positive cone of the rows is their linear span, which is all of
\(\mathbb R^m\). ∎

The statement concerns the **entire** diameter packet. A spanning-tree basis
is still available, but it cannot inherit the force constraints of the packet
by deleting its nonbasis rows.

## 3. Exact obstruction to basis-leaf release

Take any spanning-tree basis $T$, remove a basis edge $h_0$, and let $S$
be one component of the remaining tree. Define gap potentials

\[
z_j=\mathbf1_S(j),\qquad \theta_i=z_{i-1}-z_i.
\]

Then for every actual diameter row

\[
M_h\theta=c_h(z_{p_h}-z_{q_h}). \tag{3}
\]

All other basis rows vanish. Choose the overall sign of $z$ to make

\[
M_{h_0}\theta<0.
\]

The bidirectional-cut conclusion forces an actual diameter outside the
basis with

\[
M_h\theta>0.
\]

This holds for a leaf cut as a special case. It gives the precise failure of
the private-basis-edge proposal: the other direction across the same cut is
carried by a nonbasis diameter. No assertion about Euler paths is used.

More generally, if $M\theta\le0$ componentwise, (1) and positivity imply

\[
M\theta=0,
\]

and full rank implies $\theta=0$. Thus no nonzero contact-preserving train
velocity weakly shortens every active diameter.

## 4. Finite local isolation in the exact contact chart

Assume the explicit source chart

\[
P_v$t$=P_v+\sum_i\chi_i(v)(R_{t_i}u-u), \tag{4}
\]

with the coherent choice of shore indicators, has each contact of train $i$
crossing only cut $i$, and every other contact crossing none of these cuts.
Then (4) preserves every old contact exactly, for every sufficiently small
$t$: the corresponding unit vector becomes $R_{t_i}u$, and all other
contact vectors are unchanged. All source vertices, including contact
isolates, remain in the chart.

There exists a source-dependent $\epsilon>0$ such that

\[
0<\|t\|<\epsilon\quad\Longrightarrow\quad
\operatorname{diam}P$t$>D. \tag{5}
\]

Indeed, positive spanning gives

\[
\delta:=\min_{\|s\|=1}\max_h M_hs>0.
\]

For the finitely many old actual diameter pairs, Taylor expansion in (4)
is uniform:

\[
\tfrac12(|r_h$t$|^2-D^2)=M_ht+O(\|t\|^2).
\]

Hence the largest left side is at least

\[
\delta\|t\|-C\|t\|^2>0
\]

for sufficiently small nonzero $t$. This proves (5), even before testing
inactive pairs. It is a finite neighbourhood theorem, rather than an
unsupported integration of a first-order calculation.

No uniform lower bound for $\delta$, or uniform neighbourhood in $D$,
is asserted. Moves outside this chart, contact-opening moves, and distant
finite competitors are not excluded by this theorem.

## 5. Rational geometric regression

Put $u=(1,0)$, and take the five actual points

\[
o=(0,0),\quad x_\pm=(12,\pm5),\quad
y_\pm=(63/5,\pm16/5).
\]

Their minimum squared pair distance is $18/5>1$, their diameter is $13$,
and their only actual diameter bars are $ox_\pm,oy_\pm$. Thus they form a
genuine convex diameter thrackle, a four-leaf star.

Assign gap label 0 to $o$, 1 to both $x$'s, and 2 to both $y$'s.
The diameter rows are

\[
(5,0),\quad(-5,0),\quad(16/5,16/5),\quad(-16/5,-16/5).
\]

They have rank 2 and positive dependence with $\beta_h=1/4$. Their gap
graph is a doubled star with center 0. The weighted axial resultants of
the two train cuts are

\[
A_1u=(123/10)u,\qquad A_2u=(63/10)u.
\]

The internal strip reaction is exactly $6u\ne0$, positively generated
by $\tfrac14(12,5)+\tfrac14(12,-5)$. Its bars have opposite strict
transverse signs. The tree basis consisting of the first and third rows
has a private leaf at gap 1, but the candidate leaf velocity

\[
\theta=(-1,1)
\]

gives derivatives $(-5,5,0,0)$: the nonbasis diameter lengthens.

**Encoded:** actual Euclidean diameters, unit separation, convex thrackle,
ordered interval labels, full row rank, positive circulation, and a nonzero
positive two-bar axial resultant.

**Omitted:** an actual train/contact embedding of these gap labels, full
vertex KKT equilibrium, canonical mixed stress/kernel, a complete opposite
shore, the linear shore-size hypothesis, and global optimality. There are
no unit contacts in this five-point source. It is a regression against
the abstract tree-leaf shortcut, not a C-II source or Level I disproof.

## 6. Certificate and self-audit

Run `python3 research/verify_exact_phase_gap_circulation_2026_10_01.py`.
It uses rational arithmetic throughout, checks every proper cut in the
finite packets, and certifies the rational star and basis-leaf failure.
The general circulation, cut, and finite-isolation proofs do not depend
on finite enumeration.

| Assertion | Classification | Audit result |
| --- | --- | --- |
| Positive signed gap circulation | proved candidate awaiting promotion | direct KKT pairing and incidence transform |
| Strong connectivity, no bridges, positive spanning | proved candidate awaiting promotion | every proper cut balances positive flow |
| Finite isolation within the exact train chart | conditional proved candidate | requires the explicit chart/cut property; full proof above |
| A private tree-basis leaf can shorten its diameter without another active diameter lengthening | rejected attempt / regression | every tree cut has a nonbasis opposite-direction edge |
| Connected gap graph plus abstract axial reactions contradicts diameter-thrackle geometry | rejected abstract strengthening | exact labelled five-point diameter star |

Contact-isolated vertices have not been removed; no local source is called
a global minimizer; no inactive pair is declared active; no asymptotic
quantity has been upgraded to exact equality.

## 7. Frontier effect and continued closing obligation

The new necessary object is a **strongly connected directed gap multigraph
with a strictly positive source KKT circulation**, rather than just an
undirected spanning-tree basis. Its elementary positive dependencies are
directed cycles. A cycle decomposition can be obtained by repeatedly
subtracting the minimum edge flow on a directed cycle; each subtraction
removes at least one positive edge, so the process terminates.

The next closing obligation is to prove that these directed cycles cannot
be realized simultaneously by actual diameter chords, their ordered train
cuts, the opposite complete shore, and the full canonical source stress;
or to build a source-preserving finite competitor outside the locally
isolated contact chart. The rational star proves that actual diameter
geometry and labelled axial resultants alone do not suffice.

This packet does not eliminate the fixed-star branch, nonconstant-phase
TB1, split-star O–O, inactive-interface, macroscopic inactive-container,
or higher-surplus full-core branches. Canonical state is unchanged.

**Promotion recommendation:** preserve as unreviewed research. A route
promotion needs an independent audit of the unpromoted cut/chart chain,
followed by the full state/prompt/dependency/certificate transaction.
