> Generated reading edition · [exact source](../../../docs/audits/target_c_acute_binary_sink_run_payment_independent_audit_2026-10-09.md) · source SHA-256 `494d9aed4956683e19c6857a19a0c7e4e67a22cb986d77dbad3e2fae4ad0c8ca`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 5 paragraph(s) with malformed inline math are preserved as explicit source excerpts rather than guessed equations.

<!-- theorem-state: {"artifact_id":"ART-5C1E9BE14C90","canonical":true,"claim_ids":["C-ACUTE-BINARY-SINK-WITNESS-DEBT","C-BINARY-SINK-OWNER-RUN-TRADEOFF","C-LOADED-BINARY-SINK-DOUBLE-RECURRENCE","C-LOADED-SINK-TRAIN-WITNESS-TRADEOFF"],"claim_statuses":{"C-ACUTE-BINARY-SINK-WITNESS-DEBT":"canonical","C-BINARY-SINK-OWNER-RUN-TRADEOFF":"canonical","C-LOADED-BINARY-SINK-DOUBLE-RECURRENCE":"canonical","C-LOADED-SINK-TRAIN-WITNESS-TRADEOFF":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit: acute binary sink witness and loaded-run payments

**Date:** 2026-10-09
**Audit base:** `origin/main=cd94ab982e7ce410eab229ef546222ac7ffda7fa`, state `2026-10-09.audit.177`.
**Target:** C-II. C-I is closed; C-II and Level I remain open.
**Frozen source branch:** `research/sol/target-c-owner-order-closure-20261006` at `bf288c82e8a62466d5580025c94e750a177e63e2` (47 commits ahead, 204 behind main).
**Run type:** independent audit and promotion. The exact live endpoint remains a source-realized face-coupled finite move checking every full-source lower and actual-diameter upper constraint.

## Audited source claims

The frozen branch contains the following proof-only inputs:

| Artifact | SHA-256 | Disposition |
|---|---|---|
| `research/target_c_acute_horn_sink_obstruction_2026-10-05.md` | `47fac27bcecd5821fc1cd7271b19d905306686396ff61573759c0dbe11970662` | PASS for the exact acute two-owner clause reduction and (m+1) distinct-witness debt. |
| `research/target_c_loaded_sink_owner_run_payment_2026-10-05.md` | `e53f1372d626b70302e9a8e145d96d23ca200de1c4055b11c9cd5d11079b4978` | PASS WITH NARROWED SCOPE for the mixed unloaded-witness / loaded-run inequality. |
| `research/target_c_loaded_sink_double_recurrence_2026-10-05.md` | `ad8d450606741c12f63e931ed202754258ebca28738d87efc6d2632ff4151019` | PASS WITH NARROWED SCOPE for two repeated owners at an all-loaded conflict edge. |
| `research/target_c_outer_train_run_budget_for_loaded_sinks_2026-10-05.md` | `9a448e673248017070669a0a2c782fc58b7efe041f562a24237006db9b01ef67` | The stated outer run upper bound is already subsumed by canonical Audit.127 when cuts are pairwise disjoint. The new lower bound on train count survives only in that exact scope. |
| `research/target_c_unloaded_sink_outer_occurrence_payment_2026-10-05.md` | `917f0764ddbc79f62971a3d9c72af4ea77a23a09833ff977fd2285a8376a202e` | Not audited in this artifact; no conclusion using its (6(b-q+Z_{out})) estimate is promoted. |

The audit recommends promoting the four results as `C-ACUTE-BINARY-SINK-WITNESS-DEBT`,
`C-BINARY-SINK-OWNER-RUN-TRADEOFF`,
`C-LOADED-BINARY-SINK-DOUBLE-RECURRENCE`, and
`C-LOADED-SINK-TRAIN-WITNESS-TRADEOFF`. The source's general unloaded-witness
occurrence cap remains unreviewed.

## 1. Exact scope and statement

Use a finite unit-separated source (A) of diameter (D\ge7) with a
two-dimensional convex hull of the actual diameter endpoints (B). Consider an
actual small O--O owner system with translation-cloud diameter

```math
s<\gamma_D=D-\sqrt{D^2-1},
```

independent binary selection of every owner, exact preservation of every old
unit contact in every binary state, and pairwise acute nonzero owner translations
$`\Delta_i\cdot\Delta_j>0`$. Every selected clause witness is an old
noncontact pair between the two owner labels defining that clause. Contact
isolates remain source points; the theorem neither deletes nor moves them.

Reduce each pair's forbidden binary states to irreducible 2-SAT clauses, leaving
unary forced-zero clauses separately identified. A **binary sink** is a strongly
connected sink component (S) of the simple implication digraph, with
$`m=|S|\ge2`$, having an internal binary incompatibility edge. If the lower
formula has only the all-zero model and has no unary forced-zero clause, every
sink component of size at least two has such an internal incompatibility.

For a sink (S), choose (m) distinct implication arcs covering every owner
(a directed spanning out-arborescence plus one further arc) and one internal
incompatibility witness. This is its **covering packet**. Let (u(S)) count
packet witnesses with at least one endpoint outside (B). Let (r_i) be the
number of cyclic loaded-hull runs carrying owner (i), and set
$`R(S)=\sum_{i\in S}r_i`$.

The audited conclusions are:

1. The (m+1) witnesses in the covering packet are distinct physical source
   pairs.
2. For (D\ge7),
   ```math
   u(S)+R(S)-m\ge1.
   
   ```
   For pairwise disjoint binary sinks (S_a),
   ```math
   \sum_a u(S_a)+\sum_a\bigl(R(S_a)-|S_a|\bigr)\ge t.
   
   ```
3. If the covering packet is entirely loaded-loaded, and it is enlarged to
   include one incoming and one outgoing implication witness at each endpoint
   of an internal incompatibility edge (ab), with every witness in this
   combined packet still loaded-loaded, then
   ```math
   r_a\ge2,\qquad r_b\ge2,\qquad R(S)\ge m+2.
   
   ```
   The same lower bound sums over pairwise disjoint such sinks.
4. If the O--O cuts are, in addition, pairwise disjoint proper crosscuts in the
   canonical owner system of Audit.127, with train count (T_{OO}), then for
   any pairwise disjoint sink family and covering packets as above,
   ```math
   T_{OO}+\sum_a u(S_a)\ge\sum_a(|S_a|+1).
   
   ```
   If all selected packets are loaded-loaded and include the endpoint witnesses
   in item 3, the sharper conclusion is
   ```math
   T_{OO}\ge\sum_a(|S_a|+2).
   
   ```

Items 1--3 do not require pairwise-disjoint cuts. Item 4 does. It is a finite
owner-system theorem, not a global-minimizer theorem or a motion result.

## 2. Independent proof

### One physical pair has at most one binary role

For a noncontact pair between distinct owners (i,j), write its old vector as
$`r`$, put
$`\Phi_{ab}=|r+b\Delta_j-a\Delta_i|^2-1`$, and note
$`\Phi_{00}>0`$. Direct expansion gives

```math
\Phi_{11}-\Phi_{10}-\Phi_{01}+\Phi_{00}
=-2\Delta_i\cdot\Delta_j<0.
```

If both singleton states 10 and 01 violate the strict lower bound, then
$`\Phi_{10},\Phi_{01}\le0`$, so
$`\Phi_{11}=\Phi_{10}+\Phi_{01}-\Phi_{00}-2\Delta_i\cdot\Delta_j<0`$.
Thus the bad-state set cannot be exactly $`\{10,01\}`$.

With state 00 good, the possible nonempty bad sets are
$`\{10\},\{01\},\{11\},\{10,11\},\{01,11\},\{10,01,11\}`$.
Their reductions are, respectively, one implication, the reverse implication,
one binary incompatibility, a unit clause forcing (i=0), a unit clause
forcing (j=0), or two unit clauses forcing both to zero. Therefore one physical
pair cannot witness both directions of an implication or both an implication
and an incompatibility. The last case is unary information and is excluded from
the binary-only sink obstruction claim.

### Sink witness count

A strongly connected simple digraph on (m\ge2) vertices contains a directed
spanning out-arborescence with (m-1) distinct arcs and at least one further
arc. Those (m) arcs touch every vertex. Each selected implication arc needs a
physical witness; the pair-role calculation forces distinct arcs to use distinct
physical pairs. An internal incompatibility witness is a different role and
therefore a different physical pair. This gives (m+1) distinct witnesses.

If the all-zero assignment is the only satisfying assignment of a binary-only
lower formula, setting one sink SCC to one and all other variables to zero would
satisfy every implication unless the sink has an internal incompatibility.
Thus the stated sink obstruction follows. This argument is only about the
reduced lower formula; it does not establish that upper-diameter or unary
rhombus constraints are safe.

### Loaded witnesses are distinct loaded-hull sides


**Source formatting excerpt (unbalanced inline math in the original):**

```text

For any old lower witness, the relative displacement changes by at most (s),
so its old length satisfies (1<|pq|\le1+s\). For (D\ge7),
```

```math
s<\gamma_D<\frac1{2D-1}\le\frac1{13}<\frac1{12},
```


**Source formatting excerpt (unbalanced inline math in the original):**

```text
and hence (1<|pq|<14/13<13/12\). By canonical
`C-LOADED-NEAR-UNIT-ADJACENCY`, every witness with both endpoints in (B) is
an actual side of the loaded hull. Different physical witness pairs give
different loaded-hull sides, and each side has two distinct owner labels from
the same sink.
```



Let (E_S) count these loaded-hull sides whose endpoints carry distinct owners
in (S). Mark the loaded-hull word by whether a vertex owner lies in (S). In
each marked path component, compress adjacent equal-owner vertices into maximal
owner runs: at most one transition side occurs between consecutive runs. If the
whole cycle is marked, there are at most as many transition sides as owner
runs. Summing gives
```math
E_S\le R(S).
```
Exactly (m+1-u(S)) covering-packet witnesses are loaded-loaded, so
$`m+1-u(S)\le E_S\le R(S)`$, proving item 2. Physical witness packets for
different SCCs are disjoint because each selected pair witnesses an internal
clause whose two owner labels belong to that SCC.

### Double recurrence at a fully loaded conflict

Fix an internal incompatibility edge (ab). In the strongly connected
implication component, (a) has an incoming and an outgoing implication arc
inside (S), and so does (b). At each endpoint those two arcs are distinct;
the acute pair-role calculation makes their physical witnesses distinct from
each other and from the incompatibility witness. If the combined witness packet
is loaded-loaded, (a) is incident with three distinct loaded-hull transition
sides, as is (b). A cyclic owner run has at most two transition sides, hence
$`3\le2r_a`$ and $`3\le2r_b`$, so both run counts are at least two.



**Source formatting excerpt (unbalanced inline math in the original):**

```text
The covering arborescence packet also puts every owner of (S) on the loaded
hull. Thus each owner has at least one run, and the two conflict endpoints
contribute one extra run each: (R(S)\ge m+2\). For disjoint sinks this sums.
```



For item 4, if a sink has any loaded-loaded packet witness, its two distinct
owner endpoints both occur on the loaded hull. Consequently every owner in
that sink with a positive run has a nonempty outer-walk complement. Audit.127's
canonical `C-OO-OVERLAP-AWARE-ROOT-RUN-CAPACITY` applies to the union of those
owners, giving $`\sum R(S_a)\le T_{OO}`$ over sinks with at least one
loaded-loaded witness. A sink with none has (u(S_a)=|S_a|+1), so it contributes
zero to the loaded-witness count. Therefore
```math
\sum_a(|S_a|+1-u(S_a))\le T_{OO},
```
which is the mixed terminal tradeoff. In the all-loaded case, every owner in
each sink has a loaded occurrence and, since $`|S_a|\ge2`$, a nonempty
complement. Audit.127 then gives $`\sum_aR(S_a)\le T_{OO}`$; item 3 gives
$`\sum_a(|S_a|+2)\le T_{OO}`$.

## 3. Hostile checks and limitations


**Source formatting excerpt (unbalanced inline math in the original):**

```text

- **Acuteness is load-bearing.** If the dot product is negative, one pair can
  have bad states exactly 10 and 01. For example, take
  $`r=(201/200,0)`$, $`\Delta_i=(1/20,3/50)`$, and
  $`\Delta_j=(1/20,-3/50)`$. Then
  $`|r|^2=40401/40000>1`$,
  $`|r-\Delta_i|^2=|r-\Delta_j|^2=36625/40000<1`$, but
  $`|r+\Delta_j-\Delta_i|^2=40977/40000>1`$. This is an exact pair-level
  algebraic regression, not a source configuration.
- **Unary blockers are not sink conflicts.** A unary force-zero clause can
  make zero the only model without an internal incompatibility edge. The
  (m+1) sink conclusion is therefore only for a binary-only formula or an
  explicitly supplied internal conflict.
- **All-loaded coverage matters.** If only the three endpoint witnesses at
  (a,b) are loaded while the covering arcs for other owners are unloaded,
  the two repeated endpoint runs still follow, but (R(S)\ge m+2) and the
  train-count conclusion do not follow.
- **Disjointness matters for train count.** The branch's direct terminal
  occurrence argument is not promoted for a merely noncrossing family. The
  (T_{OO}) claims above use Audit.127's explicit pairwise-disjoint proper
  crosscut premise. The loaded-hull recurrence claims do not need that premise.
- **Near-unit scope matters.** The side conversion is used only with
  (D\ge7) and (s<\gamma_D\); no loaded-cycle conclusion is asserted for a
  longer witness pair or a degenerate loaded hull.
- The selected binary owner system is not a physical source move. Every source
  point, including contact isolates, remains retained; no lower or upper
  feasibility of a nonzero owner selection is concluded.
- The companion unloaded endpoint estimate (6(b-q+Z_{out})) is outside this
  audit. The source sink notes supply no verifier for the analytic claims here;
  no sampled computation is treated as proof.
```



## 4. Canonical dependencies and frontier effect

New theorem IDs and dependencies:



**Source formatting excerpt (unbalanced inline math in the original):**

```text
| ID | Exact result | Dependencies |
|---|---|---|
| `C-ACUTE-BINARY-SINK-WITNESS-DEBT` | One acute physical pair has at most one irreducible binary role; an internally obstructed (m\)-owner sink needs (m+1) distinct physical lower witnesses. | Exact algebra in this report. |
| `C-BINARY-SINK-OWNER-RUN-TRADEOFF` | (u(S)+R(S)-|S|\ge1), including the sum over pairwise disjoint sinks. | `C-ACUTE-BINARY-SINK-WITNESS-DEBT`; `C-LOADED-NEAR-UNIT-ADJACENCY`. |
| `C-LOADED-BINARY-SINK-DOUBLE-RECURRENCE` | A fully loaded covering packet at an internal conflict forces two distinct repeated owners and (R(S)\ge |S|+2). | `C-ACUTE-BINARY-SINK-WITNESS-DEBT`; `C-LOADED-NEAR-UNIT-ADJACENCY`. |
| `C-LOADED-SINK-TRAIN-WITNESS-TRADEOFF` | With pairwise-disjoint proper O--O cuts, (T_{OO}+\sum u(S_a)\ge\sum(|S_a|+1)); fully loaded packets force (T_{OO}\ge\sum(|S_a|+2)). | `C-BINARY-SINK-OWNER-RUN-TRADEOFF`; `C-LOADED-BINARY-SINK-DOUBLE-RECURRENCE`; `C-OO-OVERLAP-AWARE-ROOT-RUN-CAPACITY`. |
```



The branch's Section 2 bound $`\sum r_i\le T_{OO}`$ is already canonical in
Audit.127 for its disjoint-cut scope. The new contribution is the lower
recurrence cost and its exact combination with that upper capacity.

In the canonical terminal Type-II regime where `C-OO-TERMINAL-TRAIN-POPULATION`
gives (T_{OO}=o(D)), the all-loaded consequence excludes a linear number of
owners in such disjoint binary sinks: (M+2t\le T_{OO}=o(D)). It does not
charge upstream implication basins, sinks paid by unloaded witnesses, unary
rhombus blockers, or inactive diameter exceptions. It therefore narrows one
owner-order subcase but does not change the source-realized face-coupled
finite-move endpoint, C-II status, or Level I status.

**Verdict:** PASS for the exact acute witness debt; PASS WITH NARROWED SCOPE for
the owner-run and loaded-only recurrence theorems; PASS — already subsumed for
the disjoint-cut run upper bound; no promotion of the unloaded-witness
occurrence cap. No external literature or computational proof premise was
used.
