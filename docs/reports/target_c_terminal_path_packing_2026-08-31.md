<!-- theorem-state: {"artifact_id":"ART-F3E4B27BD5CF","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C: C-II has linearly many disjoint terminal connections

**Date:** 2026-08-31
**Repository state:** `a7f0e96` (`origin/main` before this promotion)
**Run type:** proof / graph-theoretic C-II reduction
**Target:** Target C-II, non-additive response branch
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md`
**External web search:** not used beyond the already audited circular-minor and Gallai inputs
**Computation:** not used

## LEVEL I STATUS

**Later refinement:** the connected-quotient report
[target_c_terminal_path_packing_connected_refinement_2026-08-31.md](target_c_terminal_path_packing_connected_refinement_2026-08-31.md)
improves the numerical packing bound from `q/5` to `(q-1)/4`. TP5 remains valid
and supplies the same circular-planar pairing mechanism.

**STILL OPEN.**

In fully force-visible C-II, every loaded boundary vertex has contact degree at most
three and every other contact vertex has degree at most five. Gallai's exact
T-path formula then forces at least one fifth of the force-visible terminals into
pairwise vertex-disjoint terminal paths. Pairing those paths gives linearly many
terminal-disjoint circular two-connections and hence linearly many strict circular
response minors. This is topological information only; no numerical lower bound
on any individual minor follows.

## 1. Starting endpoint

SEPq excludes additive response by showing that the absence of two disjoint
terminal paths creates a forbidden high-degree separator. The converse graph
count is:

```
C-II degree caps + q force-visible terminals
    -> nu_T >= q/5 disjoint T-paths
    -> at least floor(q/10) terminal-disjoint circular 2-connections
    -> at least floor(q/10) strict circular minors.
```

## 2. Strongest genuinely new audited theorem

### Theorem TP5 (terminal-path packing)

Let G be a connected finite graph with terminal set T, |T|=q>=4. Assume

```
degree(v) <= 5 for v outside T,
degree(t) <= 3 for t in T.
```

A T-path has two distinct endpoints in T and no internal vertex in T. If nu_T(G)
is the maximum number of pairwise vertex-disjoint T-paths, then

```
nu_T(G) >= q/5.
```

If G is also a positive circular-planar network with T on the boundary in cyclic
order, it contains at least

```
floor(q/10)
```

pairwise terminal-disjoint circular two-connections. Every one gives a strict
size-two circular minor of the response matrix.

### Scope

This is a finite graph and planar-network theorem. It applies to the full
nonisolated contact graph in fully force-visible C-II after choosing a
relative-interior stress. It does not give a numerical lower bound for a strict
minor, and it does not apply to a non-maximal selected contact support in C-I.

### Proof

Gallai's T-path min-max theorem gives

```
nu_T(G) =
  min_X ( |X| + sum_K floor(|T intersect K|/2) ),
```

where K ranges over the components of G-X.

Fix a nonempty X. Write x0=|X outside T|, x1=|X intersect T|, and

```
F_X = sum_K floor(|T intersect K|/2).
```

Let N_X be the number of components of G-X containing a terminal. Since G is
connected, each such component has an edge to X. Distinct components require
distinct crossing edges. The degree assumptions therefore give

```
N_X <= 5*x0 + 3*x1.
```

For every terminal-bearing component K, with t_K terminals,

```
t_K <= 2*floor(t_K/2) + 1.
```

Consequently,

```
q = x1 + sum_{K: t_K>0} t_K
  <= x1 + 2*F_X + N_X
  <= 5*x0 + 4*x1 + 2*F_X
  <= 5*(x0+x1+F_X).
```

The last parenthesis is the Gallai expression for X, so every nonempty X has
value at least q/5. For X empty, connectedness gives floor(q/2), which is also
at least q/5 for q>=4. Taking the minimum proves nu_T(G)>=q/5.

Pair a maximum T-path packing arbitrarily. The four boundary endpoints of any
two paired paths cannot alternate around the disk, because the embedded paths
would then intersect. Each pair is therefore a circular two-connection. The
pairs are terminal-disjoint, and the circular-minor connection theorem makes
each associated size-two minor strict. This proves the theorem.

## 3. Exact Target C-II implication

In fully force-visible C-II, C26 and C35 give the degree hypotheses for the
positive contact graph C with terminal set T=B_+. C34 gives

```
2*|B_+| >= ceil(D)+2.
```

Thus

```
nu_(B_+)(C) >= |B_+|/5 >= (ceil(D)+2)/10,
```

and there are at least

```
floor(|B_+|/10) >= floor((ceil(D)+2)/20)
```

pairwise terminal-disjoint strict circular minors. Their number is linear in D.

This rules out any remaining non-additive response normal form with only a bounded
number of circular connections. It does not rule out arbitrarily small strict
minors: the contact conductances can be uneven, and the canonical stack has no
uniform individual stress lower bound.

## 4. Dependencies and literature imports

- `docs/reports/target_c_additive_response_separator_obstruction_2026-08-31.md`,
  Theorem SEPq: the separator mechanism in the additive special case.
- `docs/reports/target_c_force_visible_endpoint_count_2026-08-31.md`, C34:
  2*|B_+| >= ceil(D)+2.
- `docs/reports/target_c_loaded_boundary_attachment_2026-08-31.md`, C35, and
  the C26 result in the fully-visible bridge frontier: the degree bounds.
- The Gallai T-path formula is Theorem 2 in T. Kaiser,
  [*Disjoint T-paths in tough graphs*](https://iti.mff.cuni.cz/series/2005/270.pdf).
- Strictness of a circular minor is Lemma 3.4 in S. Forcey,
  [*Kalmanson-Kron reconstruction*](https://sforcey.github.io/sf34/kron.pdf),
  recording the Curtis--Ingerman--Morrow connection criterion.

## 5. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| nu_T(G) >= q/5 under the degree caps | proved with literature input | Gallai's exact formula plus the crossing-degree count. |
| Paired paths give circular two-connections | proved | Disk planarity forces each disjoint path pair to be noncrossing. |
| Each paired connection gives a strict response minor | literature import | Forcey Lemma 3.4 under positive circular-planar conductances. |
| C-II has a linear family of strict circular minors | proved | TP5, C34, C26, and C35. |
| The strict minors have a uniform positive numerical size | not proved | No individual contact-stress lower bound is canonical. |
| Non-additive response equality is impossible | not proved | Many strict minors may coexist with equality. |
| Target C is closed | not proved | C-I and the remaining C-II bridge/bulk branches remain. |

## 6. Regression tests and no-go results

| Regression | Result | Reason |
| --- | --- | --- |
| Five-leaf degree-five star | passes | It attains the q/5 scale and shows the degree-only constant is sharp. |
| Six-leaf star | outside scope | Its interior hub has degree six. |
| A path with many terminals | passes | It has many disjoint T-paths. |
| q=3 terminal triangle | outside scope | The q>=4 empty-set Gallai value is essential. |

TP5 gives strictness but not magnitude. A sequence of positive-conductance
networks can keep selected circular minors arbitrarily small. It therefore does
not yet produce the C41 trace gap or a packing contradiction.

## 7. Exact remaining lemma

> **Strict-minor transport.** In fully force-visible C-II, the linear family of
> terminal-disjoint circular connections from TP5 forces either a quantitative
> lower bound on the C41 response diameter defect or an exact incompatibility with
> the C42 rhombic bulk and global packing inequalities.

No uniform bound may be assumed without proving how unit-contact geometry and
global optimality supply it.

## 8. Canonical promotion recommendation

**Promote now — proof audited and frontier changes.**

Promote the result into:

- `docs/targets/target-c/01-force-hull-and-shear.md`;
- `docs/targets/target-c/README.md`; and
- `docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md`.

## 9. Compact handoff

```
LEVEL I STATUS: STILL OPEN.

Strongest new theorem:
Under loaded degree <=3 and unloaded degree <=5, Gallai gives nu_T >= |T|/5.
In a circular-planar embedding this yields floor(|T|/10) pairwise terminal-
disjoint strict circular minors.

Exact C-II effect:
C34 makes |B_+| >= (ceil(D)+2)/2, hence there are at least
floor((ceil(D)+2)/20) strict circular-minor witnesses.

Binding limitation:
The witnesses may be arbitrarily small numerically. This does not yet produce
the C41 trace gap or exclude non-additive equality.

Highest-value next lemma:
Transport the linear strict-minor family into a quantitative response/area/container
inequality using the unit-contact geometry and global optimality.
```
