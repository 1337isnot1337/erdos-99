> Generated reading edition · [exact source](../../../docs/audits/target_c_cyclic_d2_path_inference_audit_2026-09-10.md) · source SHA-256 `463ca91759918b974213e99ee8eae199179abf1ae567ec56a3c3dbc4b5ba3b26`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-86D77F35E038","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C audit — cyclic `d_H=2` path inference is not proved

**Date:** 2026-09-10  
**Audited branch:** `research/cyclic-d2-completion-paths-2026-09-09` / PR #141  
**Also affects:** PR #139 P2 exclusion  
**Classification:** blocking proof gap, not a counterexample to the theorem  

## Status

`LEVEL I STATUS: STILL OPEN`.

PR #141's CP2 report correctly proves that, after inserting the two canonical short completion states, the actual diameter states in each `d_H=2` component occupy one contiguous projective block and that consecutive actual states in that block share an endpoint.

The next inference in CP2 Section 5 is not valid as written:

> every consecutive pair of edges shares an endpoint, so the ordered edge list is an Euler trail; since the component is a tree, it is a path.

Pairwise consecutive incidence does **not** imply that the edge list is a trail. The shared endpoint of `e_{i-1},e_i` can equal the shared endpoint of `e_i,e_{i+1}`. A three-edge star already has an ordering

```text
va, vb, vc
```

in which every consecutive pair shares `v`, but no traversal can use those three edges in that order as a trail. The middle edge would have to enter and leave through the same endpoint `v`.

Therefore CP2.2 (both diameter components are paths) and CP2.3 (each component lies on one universal circle) are not established by the current proof.

## 1. What CP2 Section 4 actually proves

Let one diameter-tree component have projectively ordered edges

$$
e_1,e_2,\ldots,e_m.
$$

The valid output of CP2 Section 4 is

$$
\boxed{e_i\cap e_{i+1}\ne\varnothing\quad(1\le i<m).}
\tag{A.1}
$$

This gives a Hamiltonian path through the corresponding vertices of the line graph, but it does not orient the original edges into an Euler trail.

To obtain a trail one needs the additional endpoint-alternation property

$$
\boxed{
(e_{i-1}\cap e_i)\ne(e_i\cap e_{i+1})
\quad(1<i<m).
}
\tag{A.2}
$$

No proof of A.2 appears in CP2.

## 2. The local diameter geometry does not supply A.2 automatically

The exact minimum projective gap is compatible with a same-center fan.

Fix `D>1` and

$$
\delta=2\arcsin\frac1{2D}.
$$

Take a point `v` and three points `a,b,c` on the radius-`D` circle centered at `v`, with consecutive angular separations `delta`. Then

$$
|va|=|vb|=|vc|=D,
$$

while

$$
|a-b|=|b-c|=1.
$$

Thus the three oriented diameter states can occur at consecutive radius-`D` directions with exactly the unit Minkowski-step metric used in CP2 Section 4, yet the consecutive edge pairs

$$
va,vb
\quad\text{and}\quad
vb,vc
$$

share the same endpoint `v`.

This is only a local regression, not a complete Target C source. Its purpose is narrower: the radius-`D`/unit-step calculation does not imply endpoint alternation. Any repair has to use an additional global property of the completed convex thrackle, the two-component topology, KKT structure, or shell geometry.

## 3. Downstream dependency

The following reports use the unproved path conclusion to assign one fixed component circle and one fixed component-circle center:

- `target_c_cyclic_d2_ps_exclusion_2026-09-09.md` (PSX);
- `target_c_cyclic_d2_s2_exclusion_2026-09-09.md` (S2X);
- PR #139's `target_c_cyclic_d2_p2_exclusion_2026-09-09.md` (PX).

For example, PX begins by putting both diameter-tree components on circles of radius

$$
R_D=\frac{D}{2\cos(\delta/2)}
$$

and compares the single fixed vector between their circle centers at the two P2 rectangles. That fixed-center object depends on CP2.2--CP2.3. The same dependency occurs in PSX/S2X.

Hence, until A.2 or an equivalent replacement theorem is proved, the current evidence does **not** justify the claims

```text
P2 impossible,
PS impossible,
S2 impossible,
therefore the whole d_H=2 cyclic phase is closed.
```

This audit does not prove any of those claims false. It marks their present proofs as incomplete.

## 4. Exact repair target

The shortest repair is one of the following.

### Route A — endpoint alternation

Prove A.2 for every interior state in each actual-diameter block. Then the projective ordering really is an Euler trail. Since the component is a tree, it is a path, and the existing circle-center arguments can resume.

A valid proof must rule out a run

$$
va_1,va_2,va_3
$$

of three consecutive actual diameter states sharing the same source vertex. Minimum direction gap alone does not do this.

### Route B — retain caterpillar fans

Do not force the component to be a path. Use the maximal-thrackle structure directly: removing the two short cycle edges leaves two cycle-spine paths with possible direct diameter leaves attached to spine vertices. Classify the projective fan runs around each spine vertex, then replace the single component-circle center by a spine/fan transfer law. If the two defect states still force a global invariant, the P2/PS/S2 exclusions can be rebuilt without A.2.

Route B is more work but matches the known diameter-star regression honestly.

## 5. Audit verdict

| Claim | Verdict |
| --- | --- |
| two short states cut the projective order into the two component blocks | supported by CP2 Section 4 |
| consecutive actual states inside a block share an endpoint | supported by CP2 Section 4 + DG |
| this edge ordering is automatically an Euler trail | **false inference** |
| each component is therefore a path | unproved |
| each component has one universal circle center | unproved |
| PX/PSX/S2X circle-center contradictions | blocked by the same gap |
| `d_H=2` itself is possible | not established by this audit |

## Compact handoff

```text
BLOCKING AUDIT, not theorem counterexample.

CP2 proves only:
    e_i intersects e_{i+1}
for consecutive projective diameter states in each component block.
It then treats the ordered edges as an Euler trail. That requires the additional
endpoint-alternation lemma
    (e_{i-1} cap e_i) != (e_i cap e_{i+1}),
which is not proved.
A star ordering va,vb,vc is the elementary graph counterexample; the exact local
D/D/1 geometry also permits a same-center fan with angular step delta.

Therefore CP2 path/circle conclusions are currently unproved, and the P2/PS/S2
exclusions that compare fixed component-circle centers cannot yet be promoted.

Repair target: prove endpoint alternation using genuinely global Target C input, or
rebuild the defect comparison with the honest caterpillar/spine-plus-leaves normal form.
```
