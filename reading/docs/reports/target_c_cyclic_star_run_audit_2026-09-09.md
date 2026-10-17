> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_star_run_audit_2026-09-09.md) · source SHA-256 `5672d224fcb8136f1322a5a31aaa2d9e345810cd22b4e1d15fcb0b27a060ebc3`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-2BFB2DDC46AB","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic ordinary-gap audit: path inference is false, star-run saturation survives

**Date:** 2026-09-09  
**Repository branch:** `research/cyclic-run-word-audit-2026-09-09`  
**Run type:** hostile proof correction + exact replacement theorem  
**Target:** cyclic `d_H=1` and the CP/CP2 path reductions  
**Depends on:** AC/AD on PR #118; DG on PR #119  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`.

A path inference used in the recent cyclic reductions is invalid:

```text
consecutive direction-list edges share an endpoint
=> the direction list is an Euler trail.
```

A star run `za,zb,zc` is the minimal counterexample. Both consecutive pairs share `z`, but no graph trail traverses all three edges in that order.

Therefore any downstream theorem that needs the diameter tree/component to be a path must supply an independent no-branching lemma. In particular the CP path step in PR #139 and the CP2 path step in PR #141 require re-audit.

The ordinary-gap argument does prove an exact replacement theorem.

### Theorem SR — star-run saturation

Let `H` be a spanning diameter tree on `q` loaded shell terminals with `h=q-1`. Suppose its `q-1` actual diameter states occur in one projective linear block

$$
e_0,e_1,\ldots,e_{q-2}
$$

and every consecutive projective gap is the ordinary radius-`D` unit-chord gap

$$
\delta=2\arcsin\frac1{2D}.
$$

Then:

1. every consecutive pair `e_j,e_{j+1}` shares exactly one terminal;
2. for every terminal `v`, all `deg_H(v)` incident diameter edges form one contiguous interval in the projective list;
3. the `q-2` ordinary transitions are partitioned exactly among the terminal stars, with terminal `v` owning `deg_H(v)-1` consecutive transitions;
4. each owned transition between `zy` and `zw` certifies the unit shell side `yw` whenever that projective transition is an ordinary one-endpoint support event.

The theorem permits arbitrary star runs. It is the strongest conclusion available from ordinary-gap sharing alone.

---

## Proof

DG says two vertex-disjoint diameter edges have projective separation at least `2delta`. Therefore every consecutive pair at gap `delta` shares a terminal.

For a vertex `v` of degree `d_v`, at most `d_v-1` adjacent pairs of the global linear edge list can consist of two edges incident to `v`. Equality occurs iff the full set of incident edges is contiguous.

Because `H` is a spanning tree,

$$
\sum_v(d_v-1)
=2(q-1)-q
=q-2.
$$

There are exactly `q-2` adjacent pairs in the direction block, and each has one unique shared endpoint. Hence the sum of realized star adjacencies reaches the sum of all vertexwise upper bounds. Equality therefore holds for every vertex, proving contiguity and the exact ownership count.

For an ordinary strict support event, two adjacent oriented diameter states sharing `z` differ by changing only the opposite support endpoint. Their difference is the corresponding primal shell-side vector. The difference-body edge has length one, so the two nonshared endpoints are joined by a unit shell side. `square`

---

## S1 consequence

In S1, AC gives one unique short antipodal state `g`. Removing it leaves all `q-1` actual diameter states in one ordinary-gap block. Thus SR applies.

The `q-2` H-H transitions certify `q-2` distinct shell sides. The only two shell sides not certified this way are the two support events adjacent to `g`. Hence S1 is an exact two-shell-side defect of the local Reinhardt side/antipode pattern.

AC still gives

$$
A(F)=H\cup\{g\},
$$

with `A(F)` one odd cycle plus direct leaves and `g` on the odd cycle. Therefore `H` is an opened-cycle caterpillar whose stars are projectively contiguous. A star run

$$
zy_0,zy_1,\ldots,zy_r
$$

has

$$
|zy_j|=D,
\qquad
|y_jy_{j+1}|=1,
$$

so its opposite endpoints form an exact unit chain on the radius-`D` circle centered at `z`.

No path or global concyclicity conclusion follows.

---

## P1 consequence

In P1, break the projective diameter order at the unique doubled Minkowski edge arising from the parallel shell-side pair. The remaining `q-1` actual diameter states again form one linear ordinary-gap block, so SR applies.

Therefore every diameter star is projectively contiguous and all `q-2` nonparallel shell sides are certified by exact common-diameter-center triangles. The two exceptional shell sides are precisely the parallel unit pair of the P1 rectangle.

Thus P1 is an exact two-side parallel defect of the same local Reinhardt pattern.

---

## Audit impact

The following implication must not be used:

$$
\text{star-run saturation}\Longrightarrow H\text{ is a path}.
$$

The correct structural object is a caterpillar/staircase with contiguous star runs. Any circular-path theorem must separately prove every star has degree at most two.

The next valid cyclic target is therefore a run-word theorem: keep the pendant/star multiplicities as integer variables and derive the exact shell-closure or marked-path equation in those variables.
