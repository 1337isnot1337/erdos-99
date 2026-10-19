<!-- theorem-state: {"artifact_id":"ART-4114FE9E2D0A","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-provenance: {"destination_status": "unreviewed_noncanonical", "source_blob": "7436dfced68ebe4bb42b06d423a63aab8aa22741", "source_branch_refs": ["refs/heads/research/level-i-closure-20261007"], "source_commit": "3457d175bafad554b71c442a3a3667b077025dcf", "source_lifecycle": "unreviewed", "source_path": "docs/reports/target_c_isolate_normalization_core_diameter_replacement_2026-10-07.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "c3e1baac507b2ad0e28e5de1d69c5eb8db619e21a4d9370b5103d08df615828e"} -->

> **Imported unreviewed branch research.** Source branch status is historical only; no destination claim is promoted.

# Target C: isolate normalization and core diameter replacement

**Date:** 2026-10-07  
**Repository commit:** `a0b2e33d15aaab006bf54bab54122ecf3d7209cd`  
**State version:** `2026-10-08.audit.127`  
**Run type:** closing-proof bridge  
**Target:** C-II, with no full-core or macroscopic-container restriction  
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md`  
**Classification:** proved candidate awaiting independent audit/promotion; unreviewed and noncanonical in the artifact registry.

## Level I status

STILL OPEN. No endpoint is constructed in this report.

## 1. Canonical endpoint and dependency chain

Use the contact-minimal, then actual-diameter-pair-minimal triangle-free global
minimizer $P$, with $D=D(n)\ge9$. Retain all source labels. Let $V$ be
the nonisolated contact core, $Z$ the contact isolates, and $v=|V|$.
Every old actual diameter pair has both endpoints in $V$.

Audit.120 proves that a feasible noncongruent contact-isometry of the core
shortens at least one old diameter pair, and a full-source endpoint with the
exact contact graph must replace every shortened pair with at least as many
new diameter pairs. Its full-source count includes isolate-involving pairs.

The bridge here is:

```text
explicit isolate contraction, with all lower constraints checked
 -> all isolate-involving diameter equalities are opened without moving the core
 -> Audit.120 forces at least as many replacements inside V as losses inside V
 -> an endpoint with no new core diameter pair is impossible
 -> universal construction of that endpoint would close C-II and then Level I
```

The contraction is an additional proved step, not a license to omit isolates
from the original endpoint feasibility check.

## 2. Finite isolate normalization

Let $Q$ be any finite unit-separated placement of the full label set with
diameter at most $D>0$, the exact old contact graph, and nonempty core $V$.
For $i\in V$ keep $Q_i$ fixed. Put

\[
w={1\over v}\sum_{i\in V}Q_i,
\qquad Q_z(t)=(1-t)Q_z+tw\quad(z\in Z).
\]

If $Z\ne\varnothing$, set

\[
\sigma=\min_{\{i,j\}:\{i,j\}\cap Z\ne\varnothing}
             (|Q_i-Q_j|^2-1)>0,
\qquad t_0={\sigma\over8D^2}.
\]

For every $0<t\le t_0$, this placement retains the exact contact graph
and has diameter at most $D$. Every isolate-involving pair is strictly
below $D$ and strictly above one. More precisely, its squared lower margin
is at least $\sigma/2$, and its upper distance is at most

\[
D(1-t/v)\quad\text{for a core--isolate pair},
\qquad D(1-t)\quad\text{for an isolate--isolate pair}.
\]

### Proof

All isolate-involving lower distances in $Q$ are strictly above one
because its contact graph is exactly the old graph. Thus $\sigma>0$.
Also $\sigma\le D^2-1<D^2$, so $0<t_0<1/8$.

For every source label $z$, $ |Q_z-w|\le D$, by averaging the
core-point distance bounds. Each moved label has displacement at most $tD$.
An isolate-involving pair therefore changes its difference vector by at most
$2tD$. With old pair length at most $D$,

\[
|Q_i(t)-Q_j(t)|^2
\ge |Q_i-Q_j|^2-4tD^2
\ge1+\sigma/2>1.
\]

For a retained core point $Q_i$, its own zero term in the average gives

\[
|w-Q_i|\le {v-1\over v}D.
\]

Convexity of the norm now gives

\[
|Q_z(t)-Q_i|
\le(1-t)|Q_z-Q_i|+t|w-Q_i|
\le D(1-t/v)<D.
\]

Two isolates move by the same affine contraction, so their distance is
multiplied exactly by $1-t$. Core pairs do not change. These statements
check every pair in the full source and prove the lemma. If $Z$ is empty,
there is no normalization to perform.

In particular, if $Q$ already has diameter $D(n)$, the normalized source
must still have diameter $D(n)$ by global minimality. That diameter is
realized entirely inside the retained core. This observation uses an actual
same-cardinality full-source placement; it does not assert that any proposed
core placement admits an isolate extension.

## 3. Mandatory replacements inside the core

Assume $Q$ is a same-cardinality full-source unit-separated placement with
diameter at most $D$, the exact contact graph of the canonical source $P$,
and a noncongruent restriction to $V$. Let $L$ be the number of old core
diameter pairs shortened in $Q$, and let $N_V$ be the number of formerly
inactive core pairs that become diameter pairs in $Q$. Then

\[
\boxed{N_V\ge L\ge1.}
\]

### Proof

Apply Section 2 to $Q$. It produces an endpoint $Q'$ with the same
core coordinates and exact contact graph, and with no isolate-involving
diameter pair. It remains a global minimizer because it is a unit-separated
same-cardinality placement of diameter at most $D(n)$. The contact graph
is still triangle-free and has the canonical minimal contact count.

Audit.120 gives $L\ge1$ on the noncongruent core. The secondary minimum
applied to the *full source* $Q'$ gives

\[
|H(P)|\le|H(Q')|=|H(P)|-L+N_V.
\]

Here the old diameter graph lies inside $V$ by the canonical normal form,
and the new diameter graph lies inside $V$ by the explicit normalization.
Thus $N_V\ge L$. No isolate label was deleted, and no isolate lower
constraint was omitted.

A useful sufficient contradiction is therefore a full-source contact-isometry
with noncongruent core, diameter at most $D$, and $N_V=0$. Such an
endpoint may initially have new isolate-involving diameter pairs: Section 2
opens them. It must still satisfy all isolate-involving lower bounds and the
weak upper bound before normalization.

## 4. Actual-diameter cubic moment, without a move-size hypothesis

For any noncollinear global minimizer $A$ with $D\ge2$, let $d_H(x)$
be its actual-diameter degree and put

\[
\delta_K={\pi D^2\over4}-\operatorname{area}(\operatorname{conv}A).
\]

The finite inequality in canonical Audit.126 has the following zero-width
consequence:

\[
\boxed{\sum_{x:d_H(x)>2}(d_H(x)-1)^3
       \le6144D\delta_K.}
\]

Indeed, the finite source has a positive gap between $D$ and all strictly
shorter pair lengths. For all sufficiently small $c>0$, its graph of pairs
of length at least $D-c/D$ is exactly $H$. Also
$B_c=1+\lceil20\sqrt c\rceil=2$, the diameter threshold holds, and
$M_c=2(4\sqrt c+1)^2\to2$. Apply Audit.126 and let $c\downarrow0$.
No uniform inactive gap across sources is assumed; this is a finite-source
limit first.

Canonical `C-FS-GEOM` gives $\delta_K<\pi\sqrt3D/4$. Hence, with

\[
C_0=1536\pi\sqrt3,
\]

\[
\sum_x(d_H(x)-2)_+^3<C_0D^2.
\]

For every subgraph $F\subseteq H$ and every vertex cover $S$ of size
$s>0$, Hölder's inequality gives

\[
|E(F)|\le\sum_{x\in S}d_H(x)
<2s+C_0^{1/3}s^{2/3}D^{2/3}.
\]

Apply this at the *actual new global source* $Q'$ from Section 3, rather
than transporting an inactive-pair budget across an arbitrary displacement.
If $S=\{i\in V:Q_i\ne P_i\}$ after any chosen isometric alignment of $Q$ with $P$,
every new core diameter pair meets $S$. Therefore

\[
\boxed{(N_V-2s)_+^3<C_0s^2D^2,\qquad
       (L-2s)_+^3<C_0s^2D^2.}
\]

If $L\ge(\kappa-o(1))D$ along a sequence, this forces

\[
\liminf{s\over\sqrt D}\ge{\kappa^{3/2}\over\sqrt{C_0}}.
\]

The graph of new core diameter pairs also has a matching of size $\nu$
satisfying

\[
\liminf{\nu\over\sqrt D}\ge
{\kappa^{3/2}\over2\sqrt{C_0}}.
\]

For the last statement, the endpoints of a maximum matching form a vertex
cover of size $2\nu$; insert that cover into the preceding finite bound.
If either normalized quantity has no finite subsequential limit, the
corresponding lower bound is automatic. Otherwise divide the finite bound
by $D$ along a subsequence attaining its finite liminf.

These are support obstructions, not a new existence mechanism. In particular,
the bound on changed labels could also be obtained by covering the shortened
old pairs at the old source. The replacement-bank conclusion locates a
separate matching inside the actual endpoint core. No amplitude bound,
uniform stress weight, or uniform spectral gap is used.

## 5. Dependencies, regressions, and computation boundary

| Input | Canonical scope used |
| --- | --- |
| `C-ZRF`, [Section 57](../targets/target-c/57-zr-zf-rigidity-audit.md) | Old actual diameter endpoints are in the nonisolated core; isolates remain in the full source. |
| `C-FINITE-CONTACT-ISOMETRY-DIAMETER-GAIN` and `C-FINITE-CONTACT-ISOMETRY-DIAMETER-REPLACEMENT`, [Audit.120](../audits/target_c_contact_isometry_energy_independent_audit_2026-10-08.md) | Noncongruent contact-isometry under old-diameter upper bounds shortens an old core diameter; full-source secondary minimality controls replacements. |
| `C-INACTIVE-NEAR-DIAMETER-CUBIC-BUDGET`, [Audit.126](../audits/target_c_inactive_diameter_cubic_budget_independent_audit_2026-10-08.md) | Finite deficit-weighted moment, used at each actual source separately. |
| `C-FS-GEOM`, [Section 58](../targets/target-c/58-full-source-geometry-audit.md) | Noncollinear global-source isodiametric deficit is strictly below $\pi\sqrt3D/4$. |

The regular-shell, finite-hinge/heptagon, and fan-reflection regressions do
not invalidate these statements. None supplies the assumed globally feasible
noncongruent endpoint with the exact contact graph. The fan example can fail
the lower constraints before isolate normalization; Section 2 cannot repair
that failure. Newly created unit contacts are also outside Section 2's
hypotheses: such labels are not contact isolates at the endpoint.

The accompanying standard-library verifier is
`research/verify_target_c_isolate_diameter_normalization_2026_10_07.py`.
It uses rational coordinates and squared distances to check the simultaneous
contraction of two isolates with active upper equalities, exact contact-graph
retention, all pairwise lower and upper bounds, and the need for the strict
isolate/noncontact hypothesis and an anchor in the retained hull. These finite
fixtures are nonglobal. The verifier does not establish global optimality,
the general normalization lemma, the cubic inequality, or an endpoint.
Those deductions above are analytic. No external theorem is imported.

The new verifier passed 84 all-pair checks at three rational contraction
times, retained five contacts, opened two isolate-involving diameter pairs,
and checked both negative hypothesis fixtures. The existing Audit.126
verifier also passed its 7,007 source-pair checks, 647 algebra checks, 39,675
cover bounds, and 3,300 matching bounds. These are the finite scopes printed
by the scripts, not global-optimality certificates. The theorem-state checker
and `git diff --check` passed after regenerating the artifact index; this
report's generated header remains `canonical=false` and `status=unreviewed`.

## 6. Frontier and promotion recommendation

No canonical state change is made. The proof draft strengthens the mandatory
replacement location after a full-source postprocessing step. It removes
isolate-involving *upper equalities* from the final replacement count, but
neither their lower constraints nor their population nor their initial
upper bounds. A linear replacement bank also has a dispersed endpoint
matching without an inverse-diameter move-size assumption.

**Recommendation: unreviewed.** Preserve the proof draft and exact fixtures;
independently audit before any promotion. The general existence of a
noncongruent contact-isometric endpoint remains unproved.

The exact next obligation is: for every sufficiently large canonical C-II
source, construct a same-cardinality full-source placement with the exact
contact graph, diameter at most $D$, noncongruent core, and no new core
diameter pair. This report supplies the contradiction once that placement
exists. Both canonical C-II branches remain open, and the Level I objective
is not complete.
