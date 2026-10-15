<!-- theorem-state: {"artifact_id":"ART-67E2AAFD7B53","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — full-core Mantel endpoint stability

**Date:** 2026-09-14
**Repository commit:** ef941ab2b44aa393bdc461926769247b45754202
**State version:** 2026-09-14.audit.49
**Run type:** closing proof / exact asymptotic endpoint audit
**Target:** Target C-II / Level I
**Starting status:** canonical full-core near-disk branch with the promoted train-coupled surplus floor
**Active prompt:** docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md
**External literature search:** used for a near-miss scope check; no external theorem imported
**Computation:** not used

## LEVEL I STATUS

STILL OPEN

This report proves a new endpoint structure theorem, but it does not close
Target C-II. At the train-coupled floor the rhombus train-crossing graph is
asymptotically Mantel-extremal. Consequently it has an almost-balanced
almost-bipartite decomposition, and the three inverse-phase labels concentrate
on the two sides. The remaining missing step is a geometric completion theorem:
the resulting distinct-label crossing pair is only almost complete, not complete.

The candidate chain tested here is

```text
full-core floor endpoint
    -> exact train-count squeeze
    -> Mantel deficit o(T^2)
    -> almost-balanced bipartition and three-label concentration
    -> ? near-complete phase-pure grid / diameter contradiction
```

The last arrow is not proved. An abstract near-complete bipartite graph can have
no linear complete biclique, so graph stability alone cannot supply the missing
Cartesian grid.

## 1. Canonical endpoint input

Work in a canonical full-core, no-macroscopic-container Type-II sequence and
write

\[
\Delta_2:=\frac{\pi}{2\sqrt3},\qquad
\mu_{\rm TC}:=\frac{2\pi+2\sqrt{\Delta_2}}5,\qquad
f_{\rm TC}:=\frac{4\sqrt{\Delta_2}-\pi}{5}.
\]

Assume along a subsequence that

\[
\mu_D\longrightarrow\mu_{\rm TC}.
\tag{1.1}
\]

Let \(\mathcal R_D\) be the full strict-rhombus face complex, \(R_D\) its
number of faces, and \(T_D\) the number of global train tracks. The
occurrence-counted boundary identity is

\[
2T_D=B_{4,D}.
\tag{1.2}
\]

The promoted full-core loaded-chord and train-surplus statements, together with
the equality analysis in the current endpoint audit, give

\[
\frac{R_D}{D^2}\longrightarrow\Delta_2,\qquad
\frac{q-k}{D}\longrightarrow\mu_{\rm TC},\qquad
\frac{f_D}{D}\longrightarrow f_{\rm TC},
\tag{1.3}
\]

and

\[
\frac{B_{4,D}}2\le
q-k+2f_D
\quad\text{in the finite, unnormalised notation.}
\tag{1.4}
\]

The lower train-track bound is

\[
T_D\ge2\sqrt{R_D}.
\tag{1.5}
\]

Since

\[
\mu_{\rm TC}+2f_{\rm TC}=2\sqrt{\Delta_2},
\tag{1.6}
\]

(1.3)--(1.5) squeeze the track count:

\[
\boxed{\frac{T_D}{D}\longrightarrow
\tau_{\rm TC}:=2\sqrt{\Delta_2}.}
\tag{1.7}
\]

This is an equality statement at the scale \(D\). It does not assume that the
train-crossing graph is bipartite or that it contains an additive Cartesian
block.

## 2. A finite Mantel stability lemma

The following elementary lemma is the exact graph input used below.

### Lemma M — stability at the Mantel endpoint

Let \(G=(V,E)\) be a simple triangle-free graph with \(v=|V|\) and

\[
e=|E|=\frac{v^2}{4}-\varepsilon v^2,
\qquad \varepsilon\ge0.
\tag{2.1}
\]

As \(\varepsilon\to0\), there is a partition \(V=X\sqcup Y\) such that

\[
|X|=\frac v2+O(\sqrt\varepsilon\,v),\qquad
|Y|=\frac v2+O(\sqrt\varepsilon\,v),
\tag{2.2}
\]

\[
e(G[X])+e(G[Y])=O(\sqrt\varepsilon\,v^2),
\tag{2.3}
\]

and the number of missing cross edges satisfies

\[
|X||Y|-e(X,Y)=O(\sqrt\varepsilon\,v^2).
\tag{2.4}
\]

In particular, if \(\varepsilon=\varepsilon_j\to0\), then the graph is
asymptotically balanced and bipartite in edit distance.

#### Proof

For every edge \(xy\), triangle-freeness gives

\[
N(x)\cap N(y)=\varnothing,
\qquad d(x)+d(y)\le v.
\]

Summing over edges gives

\[
\sum_{z\in V}d(z)^2
=\sum_{xy\in E}(d(x)+d(y))
\le ve.
\tag{2.5}
\]

Since \(\sum_zd(z)=2e\), (2.1) and (2.5) imply

\[
\begin{aligned}
\sum_{z\in V}\left(d(z)-\frac v2\right)^2
&=\sum_zd(z)^2-v\sum_zd(z)+\frac{v^3}{4}\\
&\le ve-2ve+\frac{v^3}{4}
=\varepsilon v^3.
\end{aligned}
\tag{2.6}
\]

Choose a vertex \(x\) with
\[
|d(x)-v/2|\le\sqrt\varepsilon\,v.
\tag{2.7}
\]

Put \(X=N(x)\) and \(Y=V\setminus X\). The set \(X\) is independent,
and (2.7) gives (2.2). Because \(X\) is independent,

\[
e(X,Y)=\sum_{z\in X}d(z).
\tag{2.8}
\]

By Cauchy--Schwarz and (2.6),

\[
\left|\sum_{z\in X}\left(d(z)-\frac v2\right)\right|
\le\sqrt{|X|}\left(\sum_z\left(d(z)-\frac v2\right)^2\right)^{1/2}
=O(\sqrt\varepsilon\,v^2).
\tag{2.9}
\]

Together with \(|X|=v/2+O(\sqrt\varepsilon v)\), equations (2.8)--(2.9)
give

\[
e(X,Y)=\frac{v^2}{4}+O(\sqrt\varepsilon\,v^2).
\tag{2.10}
\]

Since \(e=v^2/4-\varepsilon v^2\), the number of edges internal to \(Y\) is

\[
e(Y)=e-e(X,Y)=O(\sqrt\varepsilon\,v^2).
\]

This proves (2.3). Finally
\[
|X||Y|=\frac{v^2}{4}+O(\varepsilon v^2)
\]
and (2.10) proves (2.4). \(\square\)

## 3. Mantel stability for the full-core floor endpoint

Let \(G_D^\circ\) be the train-crossing graph after the canonical phase-circle
cut deletes its \(O(D)\) exceptional crossing rhombi. Its vertex set is the
same global train set used in (1.2); only crossing edges are deleted. Thus,
with \(e_D=|E(G_D^\circ)|\),

\[
e_D=R_D-O(D).
\tag{3.1}
\]

The exact train-track geometry supplies a simple triangle-free graph: two
tracks cross at most once and no three tracks are pairwise crossing. Therefore
Lemma M applies with \(v=T_D\). By (1.3) and (1.7),

\[
\frac{e_D}{T_D^2}
\longrightarrow
\frac{\Delta_2}{4\Delta_2}
=\frac14.
\tag{3.2}
\]

Hence there is a partition

\[
\boxed{\mathcal T_D=X_D\sqcup Y_D}
\tag{3.3}
\]

such that

\[
|X_D|,|Y_D|=\frac{T_D}{2}+o(T_D),
\tag{3.4}
\]

\[
e(G_D^\circ[X_D])+e(G_D^\circ[Y_D])=o(T_D^2),
\tag{3.5}
\]

and

\[
|X_D||Y_D|-e_D(X_D,Y_D)=o(T_D^2).
\tag{3.6}
\]

The first conclusion is stronger than merely finding one dense bipartite
subgraph: it says that the entire endpoint crossing graph is close to a
balanced complete bipartite graph in edit distance. It is still only an
asymptotic statement; (3.6) allows a subquadratic but unstructured set of
missing crossings.

## 4. Three-label concentration

The canonical phase-circle cut assigns each train a reduced phase in an
interval of length \(\pi/3\) and a label

\[
\ell(\tau)\in\mathbb Z/3\mathbb Z.
\tag{4.1}
\]

Two trains with the same label have projective direction separation strictly
less than \(\pi/3\), whereas every strict-rhombus crossing has acute separation
strictly greater than \(\pi/3\). Consequently same-label train pairs are
nonedges of \(G_D^\circ\).

For \(i\in\mathbb Z/3\mathbb Z\), set

\[
x_i=|X_D\cap\ell^{-1}(i)|,\qquad
y_i=|Y_D\cap\ell^{-1}(i)|.
\tag{4.2}
\]

Let \(M_D\) be the missing-cross-edge count in (3.6). Every same-label cross
pair is missing, so

\[
\sum_{i=0}^2x_iy_i\le M_D=o(T_D^2).
\tag{4.3}
\]

It follows that the total minority label population is sublinear:

\[
\sum_{i=0}^2\min\{x_i,y_i\}
\le\sum_i\sqrt{x_iy_i}
\le\sqrt{3\sum_ix_iy_i}
=o(T_D).
\tag{4.4}
\]

Thus each phase label is concentrated, up to \(o(T_D)\) trains, on one side of
the Mantel partition. This does not say that the three labels occupy three
different sides; several labels may be concentrated on the same side.

Choose \(i\) maximizing \(x_i\) and \(j\) maximizing \(y_j\). By (3.4),

\[
x_i,y_j\ge \frac{T_D}{6}+o(T_D).
\tag{4.5}
\]

The labels \(i\) and \(j\) are distinct. Otherwise \(x_i y_i\) would be
\((1/36+o(1))T_D^2\), contradicting (4.3). Therefore the two families

\[
\mathcal A_D:=X_D\cap\ell^{-1}(i),\qquad
\mathcal B_D:=Y_D\cap\ell^{-1}(j)
\tag{4.6}
\]

have distinct phase labels, are internally noncrossing, have

\[
|\mathcal A_D|,|\mathcal B_D|\ge\frac{T_D}{6}+o(T_D),
\tag{4.7}
\]

and have only \(o(T_D^2)\) missing crossings between them:

\[
|\mathcal A_D||\mathcal B_D|
-e_{G_D^\circ}(\mathcal A_D,\mathcal B_D)
=o(T_D^2).
\tag{4.8}
\]

This is the strongest conclusion obtained from the endpoint equality and
three-label information alone:

\[
\boxed{\text{linear, internally noncrossing, distinct-label train families
with crossing density }1-o(1).}
\tag{4.9}
\]

## 5. Why this still does not produce the required Cartesian block

The target diameter theorem for a phase-pure train grid requires a complete
crossing rectangle (or another theorem that controls the missing-crossing
geometry). Equation (4.8) is not that hypothesis.

Here is an explicit graph-level obstruction. Let \(m\to\infty\), put
\[
p_m=(\log m)^{-1/2},
\qquad
k_m=\left\lceil4p_m^{-1}\log m\right\rceil,
\]
and choose a random bipartite graph on two \(m\)-vertex shores by retaining
each possible cross edge independently with probability \(1-p_m\). With
positive probability, simultaneously:

1. the number of retained edges is \(m^2-o(m^2)\); and
2. there is no \(K_{k_m,k_m}\).

Indeed, Chernoff's inequality gives (1). For (2), a union bound gives

\[
\binom{m}{k_m}^{\!2}(1-p_m)^{k_m^2}
\le
\exp\!\left(2k_m\log\frac{em}{k_m}-p_mk_m^2\right)
\longrightarrow0.
\tag{5.1}
\]

Since \(k_m=4(\log m)^{3/2}+O(1)=o(m)\), this graph is asymptotically
Mantel-extremal on \(2m\) vertices, is triangle-free, and has two labels
(label one shore \(0\), the other shore \(1\)), but has no complete bipartite
subgraph with both shores linear in \(m\). It is an abstract graph regression,
not a claim that the random graph is a train-crossing graph or a unit-separated
source.

Consequently the exact remaining question is geometric/topological, not
ordinary Mantel stability:

```text
near-complete crossing between two internally noncrossing train families
    + O(D) physical boundary/interface complexity
    + actual unit-rhombus embedding
    -> a complete linear-by-linear subgrid, or a direct diameter contradiction.
```

The existing canonical pseudosegment theorem supplies a complete grid of some
linear size from a fixed positive crossing density, but its absolute coefficient
does not approach one as the density tends to the Mantel endpoint. The endpoint
argument above therefore does not replace the missing penetration/common-order
theorem.

## 6. Exact frontier effect

This report adds a report-level endpoint reduction:

\[
\boxed{
\mu_D\to\mu_{\rm TC}
\Longrightarrow
\begin{cases}
T_D/D\to2\sqrt{\Delta_2},\\
R_D/T_D^2\to1/4,\\
\text{a balanced Mantel partition with }o(T_D^2)\text{ edits},\\
\text{a distinct-label phase-pure pair of size }\ge T_D/6+o(T_D),\\
\text{only }o(T_D^2)\text{ missing pair crossings.}
\end{cases}}
\tag{6.1}
\]

It removes the possibility that a floor endpoint is explained solely by a
five-sector \(C_5\)-blowup: that construction has edge density \(1/5\) in its
track graph, not the endpoint density \(1/4\). It does **not** remove a
near-complete bipartite graph with a subquadratic missing-edge set, and it does
not produce a same-cardinality smaller-diameter source.

No canonical theorem-state entry is changed. The result is conditional on the
existence of a full-core sequence attaining the scalar floor and remains
uniform only in the asymptotic sequence sense, not a finite threshold for all
minimizers.

## 7. Exact remaining lemma

A closure of this endpoint would follow from any one of:

1. a geometric near-complete-bipartite completion theorem for the actual
   train pseudosegments, with complete phase-pure shore product exceeding the
   Section-76 diameter threshold;
2. a boundary/interface estimate showing that the \(o(T_D^2)\) missing crossings
   in (4.8), together with the \(O(D)\) physical boundary, force a positive
   normalized diameter penalty; or
3. a source-preserving finite deformation using the near-complete pair directly,
   without first extracting a complete rectangle.

The theorem must retain holes, bridges, repeated boundary occurrences, and all
contact-isolated source coordinates. A graph completion assertion without those
source-level hypotheses would not close C-II.

## 8. Claim audit table

| Claim | Status | Dependencies | Reason |
| --- | --- | --- | --- |
| Floor endpoint identity (1.6) | canonical input | C-FULLCORE-TRAIN-SURPLUS-FLOOR | Exact promoted scalar floor and its equality rate |
| \(T_D/D\to2\sqrt{\Delta_2}\) | proved here, report-level | Section 85 and endpoint audit | Upper \(T_D\le q-k+2f_D\) and lower \(T_D\ge2\sqrt{R_D}\) squeeze |
| Lemma M | proved here, report-level | elementary triangle-free graph theory | Degree-square variance proof |
| Full-core train graph is simple and triangle-free | canonical input | Theorem 10.6 / Section 85 | Tracks cross at most once and have no triple crossing |
| Mantel edit-distance endpoint (3.3)--(3.6) | proved here, report-level | Lemma M and (3.1) | \(R_D/T_D^2\to1/4\) |
| Same-label train pairs are nonedges | proved here, report-level | canonical phase-circle cut and strict rhombi | Same-label separation is \(<\pi/3\), crossing requires \(>\pi/3\) |
| Label minority population is \(o(T_D)\) | proved here, report-level | (3.6) and same-label nonedges | Cauchy--Schwarz in (4.4) |
| Distinct-label near-complete pair of size \(T_D/6+o(T_D)\) | proved here, report-level | previous rows | Largest label on each Mantel shore cannot agree |
| Near-complete graph has a linear complete biclique | rejected as graph-only inference | random bipartite regression (5.1) | Missing density \(o(1)\) does not force a linear \(K_{a,b}\) |
| Near-complete train pair has a complete geometric grid | unresolved | holes/interfaces/common-order | Actual pseudosegment topology is not yet controlled at this endpoint |
| Level I | open | original quantifiers | Type I and non-endpoint Type-II branches remain |

## 9. Regression checks

| Regression/correction | Result | Exact hypothesis or failure |
| --- | --- | --- |
| Five-sector \(C_5\)-blowup | pass | It has \(R/T^2=1/5\), so it is not a Mantel-floor endpoint |
| Near-complete random bipartite graph | pass | It is only an abstract graph regression; no pseudosegment or source embedding is claimed |
| Sheared near-triangular lattice | pass | It has no fixed angle gap or global-optimality certificate |
| Square-grid / oblique-window regressions | pass | They do not provide an arbitrary-source completion theorem |
| Holes and boundary interfaces | pass | The endpoint theorem retains them; no common order is assumed |
| Contact-isolated points | pass | No isolate coordinate enters the train graph or the affine kernel |
| Positive local stress versus global optimality | pass | No local stress is used as a finite deformation certificate |
| Incident diameter edges imply an Euler path | pass | No such inference is used |
| C5 or random-graph stability implies a source competitor | rejected | Neither is a global-minimality or source-cardinality statement |

## 10. Literature imports and near misses

No external theorem is imported into the proof. The 2025 Fox--Pach--Suk
structure theorem for pseudosegments was checked as a near miss:
[arXiv:2312.01028](https://arxiv.org/abs/2312.01028), Theorem 2.12, gives
linear complete crossing subfamilies from a fixed positive crossing density.
Its conclusion has an unspecified absolute coefficient and does not give the
near-complete-bipartite completion needed in (4.8). The theorem's hypotheses
are collections of pseudosegments; it says nothing about unit separation,
diameter-minimizing source cardinality, the convex-hull diameter condition, or
source-preserving deformation. It therefore does not close this endpoint.

## 11. Computation

No script is logically required. The random graph in Section 5 is an existence
regression proved by the displayed union bound; it is not used as a numerical
certificate or as a geometric counterexample.

## 12. Corrections / supersessions

This report does not supersede a canonical theorem. It supersedes only the
informal possibility that the five-sector C5 warning by itself describes
the scalar floor endpoint: its edge-density ratio is \(1/5\), while (3.2)
forces \(1/4\) at the floor. A different near-complete bipartite obstruction
remains.

## 13. Promotion recommendation

**unreviewed** — preserve the endpoint theorem and its exact scope, but do not
promote it until the phase-cut/train-track identification and all endpoint
normalizations receive an independent audit. It is not a Level-I closure.

## 14. Handoff

1. **Strongest new theorem:** the scalar floor endpoint is Mantel-extremal and
   has a balanced near-bipartite train graph plus a linear distinct-label
   near-complete phase pair.
2. **Canonical dependency chain:** C-FULLCORE-TRAIN-SURPLUS-FLOOR →
   Section 85 train boundary currency → Theorem 10.6 train pseudosegments →
   C-PUNCTURED-PHASE labels.
3. **Exact remaining lemma:** turn the near-complete distinct-label pair into
   a source-level complete grid/diameter penalty while retaining holes and
   boundary occurrences.
4. **Binding dead route:** Mantel stability alone, and the abstract
   five-sector/random-graph models, do not supply that geometric completion.
5. **Files to read next:** docs/targets/target-c/73-pseudosegment-grid-extraction-audit.md,
   docs/targets/target-c/76-hole-stable-complete-grid-order-diameter-audit.md,
   docs/targets/target-c/90-dense-inverse-phase-crossing-core-audit.md, and
   the canonical Sections 122--123.
