> Generated reading edition · [exact source](../../../docs/audits/target_c_rhombus_edge_completion_collision_independent_audit_2026-10-08.md) · source SHA-256 `fbe1b5dce072ba796189bcad5aae5cd7af9903509d26f074241160b27fd10bc9`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-A572EACDB307","canonical":false,"claim_ids":["C-RHOMBUS-EDGE-COMPLETION-COLLISION-REGRESSION"],"claim_statuses":{"C-RHOMBUS-EDGE-COMPLETION-COLLISION-REGRESSION":"regression"},"index":"docs/state/artifact-index.jsonl","status":"regression","target":"target-c"} -->
# Independent audit — strict rhombus edge-completion collision

**Date:** 2026-10-08  
**Audit base:** `cc5c85486a8c07d3b4501b039d6a4ff70e8fdccc`, state `2026-10-08.audit.141`  
**Target:** C-II; C-II and Level I remain open.  
**Frozen source:** `research/sol/target-c-exterior-cap-closure-20261006` at `f4a362727779f6afc0f01738015112c04fdb73d5`.  
**Source report:** `docs/reports/target_c_exterior_cap_mixed_boundary_wall_capacity_2026-10-06.md`, SHA-256 `601865a16cd7c444696606e9cca2b09a47c494448d7aa050152baa3bad38a484`.  
**Source verifier:** `research/verify_target_c_exterior_cap_separator_refill_2026_10_06.py`, SHA-256 `a413e20ad53f1ba5685ff7d193ae157074b64793b94d618293289c84a8083c59`.

## Verdict

**REGRESSION VALID**, at the exact local scope below. The report names a strict-rhombus edge-completion obstruction but leaves its coordinates and arithmetic in the verifier. I reconstructed the geometry directly and reran only the verifier's `rhombus_regression()` function at the frozen source commit.

## Exact statement

There is a strictly convex unit rhombus with all four sides at unit distance and both diagonals strictly longer than one, for which the equilateral completion of one side on the rhombus side lies strictly inside the rhombus but is at distance less than one from the opposite rhombus vertex. Therefore the local data “unit edge plus strict unit rhombus” does not certify that the edge's same-side equilateral completion is a feasible inserted point.

The example is finite and nonglobal. It does not refute any theorem about canonical global minimizers, and it does not provide or deny a packet in the hypotheses of `C-EXTERIOR-CELL-WEAK-GUARD-LEDGER`.

## Independent exact reconstruction

Let

```math
A=(0,0),\quad B=(1,0),\quad D=(3/7,2\sqrt{10}/7),\quad C=B+D.
```

The side vectors are $`u=B-A=(1,0)`$ and $`v=D-A=(3/7,2\sqrt{10}/7)`$. Both have squared norm one, since $`9+40=49`$. The diagonals satisfy

```math
|C-A|^2=|u+v|^2=20/7>1,
\qquad |B-D|^2=|u-v|^2=8/7>1.
```

Thus the four points are unit-separated, the rhombus is strict, and its only unit contacts are its four sides. In particular, the contact graph is a triangle-free four-cycle. The angle between $`u`$ and $`v`$ has cosine $`3/7`$, so it lies strictly between $`\pi/3`$ and $`\pi/2`$.

The same-side equilateral completion of $`AB`$ is

```math
Q=(1/2,\sqrt3/2).
```

It lies in the rhombus interior: in the basis $`(u,v)`$,

```math
Q=\alpha u+\beta v,\qquad
\alpha=(20-3\sqrt{30})/40,\quad \beta=7\sqrt{30}/40,
```

and $`0<\alpha<1`$, $`0<\beta<1`$. Yet its distance from $`D=v`$ satisfies

```math
|Q-D|^2=\frac{11-2\sqrt{30}}7.
```

Since $`120<121`$, $`11-2\sqrt{30}>0`$; since $`\sqrt{30}>2`$, $`11-2\sqrt{30}<7`$. Hence $`0<|Q-D|^2<1`$. Inserting $`Q`$ therefore violates unit separation with the old vertex $`D`$, despite the strict diagonals and the fact that $`Q`$ is an interior point.

The four-point rhombus itself is not a global minimizer for four points: the unit square has smaller diameter. This confirms the regression's local scope.

## Certificate review and limits

The source verifier's `rhombus_regression()` encodes the side and diagonal numerators and the exact integer comparisons needed for $`0<(11-2\sqrt{30})/7<1`$; it uses no floating-point tolerance. I reran that function at commit `f4a362727779f6afc0f01738015112c04fdb73d5` with `PYTHONPATH=research`; it returned the stated coordinates and certified range. The verifier's metadata is not evidence of global optimality, source extraction, or a packet theorem. The barycentric interior check and all scope restrictions above are independently derived here.

This regression blocks only the generic same-side edge-completion inference under the listed local rhombus hypotheses. It is not a counterexample to `C-EXTERIOR-CELL-WEAK-GUARD-LEDGER`, whose full-source and weak-guard hypotheses are not supplied by this nonglobal four-point rhombus; the colliding opposite vertex is exactly the lower-distance check that a candidate packet must include. It also does not alter the canonical `C-RHOMBUS-POP` theorem or the C-II frontier.

## Canonical disposition

Promote the exact local result as regression `C-RHOMBUS-EDGE-COMPLETION-COLLISION-REGRESSION`. It refutes neither canonical globality claims nor the weak-guard packet ledger; it records why completing a unit contact edge does not by itself furnish a source-safe interior packet site. C-I remains closed, C-II remains open, and Level I remains open.
