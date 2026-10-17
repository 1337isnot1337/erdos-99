> Generated reading edition · [exact source](../../../docs/audits/target_c_exterior_cap_moved_core_refill_independent_audit_2026-10-09.md) · source SHA-256 `7f16f0745a5cc5b41ec6e7b099f6adc802cd559bb0dc8229e296652e29782a30`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-3C98A5047D35","canonical":false,"claim_ids":["C-EXTERIOR-CAP-MOVED-CORE-REFILL-NONGLOBAL-REGRESSION"],"claim_statuses":{"C-EXTERIOR-CAP-MOVED-CORE-REFILL-NONGLOBAL-REGRESSION":"regression"},"index":"docs/state/artifact-index.jsonl","status":"regression","target":"target-c"} -->
# Independent audit: moved-core refill in a nonglobal exterior-cap family

**Audit base:** `origin/main=f2ebd2b16634e31bbbba1b473d0d9ff423cc0bdd`, state `2026-10-09.audit.182`.
**Frozen source:** `origin/research/sol/target-c-exterior-cap-closure-20261006` at `f4a362727779f6afc0f01738015112c04fdb73d5`.
**Source report:** `docs/reports/target_c_exterior_cap_separator_motion_and_interior_refill_2026-10-06.md`, SHA-256 `0192a54ab219b0a6bdfd4ea012138d82c59a219e59b13ad4b6a395a3081abfce`.
**Finite verifier:** `research/verify_target_c_exterior_cap_separator_refill_2026_10_06.py`, SHA-256 `a413e20ad53f1ba5685ff7d193ae157074b64793b94d618293289c84a8083c59`.

**Publication reading note:** the frozen source-report path above is historical
provenance and is excluded from this corpus. The independent reconstruction below
is the retained standalone proof of this scoped regression. Its source geometry
is supplied in the [paired-cap report](../reports/target_c_paired_cap_spoke_global_comparison_2026-10-06.md)
and [paired-cap audit](target_c_paired_cap_spoke_global_comparison_independent_audit_2026-10-07.md);
the [retained verifier](../../../research/verify_target_c_exterior_cap_separator_refill_2026_10_06.py)
replays the finite example. No unavailable historical report or private checkout
is needed to read this proof or execute that check.

## Verdict

**REGRESSION VALID — promote `C-EXTERIOR-CAP-MOVED-CORE-REFILL-NONGLOBAL-REGRESSION`.** For every integer `M>=20`, the explicit six-spoke source from the paired-cap report admits a same-cardinality, triangle-free endpoint of diameter strictly below its original `D=2M`: delete the two negative ends of the actual core-contact cut, translate the two retained core shores toward the cut by `1/10`, retain every scaled lattice isolate, and add two explicit sites inside the force hull. A first endpoint has exact squared diameter `4M^2-(2/5)M+1/25`; a small common finite downward move of the two new sites opens their four contacts and keeps every pair below `2M`.

This is a nonglobal finite family, not a counterexample to Target C. It fails the canonical mixed-rigidity and linear loaded-diameter-density hypotheses: `v=6M`, `e=6M`, `h=3`, so `e+h=6M+3<12M-2`; also `q/D=3/M`. No canonical cap extraction or refill follows. The result is useful as a guardrail because it shows that moved-core refill can occur in sources with positive equilibrium and large paired caps once the canonical rigidity and density conditions are removed.

## Exact statement audited

Use the triangular lattice with basis `e1=(1,0)`, `e2=(1/2,sqrt(3)/2)`, and cyclic unit rays `v_j`. Let

```text
T_M = {k v_j : 1<=k<=M, 0<=j<6}
s   = 1 + 1/(100 M^2)
R_0 = M - 1/4
I_M = {ell in Lambda : |ell|<=R_0 and dist(ell,T_M)>1}
A_M = T_M union s I_M.
```

The exact source geometry and its positive KKT stress are already canonical under `C-PAIRED-CAP-SPOKE-NONGLOBAL-REGRESSION`. Put `w=e2-e1`, so `|w|=1` and `w dot (i e1+j e2)=(j-i)/2`. Let the negative and positive core shores be `T_-={p in T_M:w dot p<0}` and `T_+={p in T_M:w dot p>0}`. The line contains no point of `T_M`. Delete `e1` and `-e2`, translate each retained `p in T_-` to `p+(1/10)w`, each retained `p in T_+` to `p-(1/10)w`, and leave all points of `sI_M` fixed. Add

```text
y_3 = 4 e1 - e2 + (1/10)w
y_5 = 6 e1 - e2 + (1/10)w.
```

The resulting source has the same cardinality. It is unit-separated, has six old contacts removed and four new contacts, and its exact maximum squared distance is

```text
D_1^2 = 4 M^2 - (2/5) M + 1/25 < 4 M^2.
```

Each new site initially makes one unit triangle with its two consecutive core anchors. Moving both new sites by a sufficiently small common positive distance in the Cartesian direction `(0,-sqrt(3))` opens all four new contacts. Because all other involving pairs have strict lower and upper margins and the source is finite for each `M`, a positive finite step exists that preserves all other constraints. The resulting endpoint is triangle-free and still has diameter below `2M`.

## Independent reconstruction

The paired-cap audit supplies the exact source facts: `T_M` has `6M` vertices, the central hexagon and six radial chains give exactly `6M` contacts, the only diameter pairs are the three opposite pairs of radius-`M` tips, and all scaled cloud labels are strict contact isolates. In the `w`-cut, exactly two old contacts cross, `{e1,e2}` and `{-e1,-e2}`; their negative endpoints are `e1` and `-e2`. The removed labels are nonadjacent, each has contact degree three, and neither is a diameter endpoint. Thus six and only six old contacts are lost. Every remaining old contact has both endpoints in one shore and is preserved by the common shore translation.

For lower constraints, distinct lattice points have squared lattice norm in the positive integers `1,3,4,...`. After deleting the two crossing unit contacts, every remaining cross-shore core pair began at distance at least `sqrt(3)`; its relative translation is at most `1/5`, so it stays above `sqrt(3)-1/5>1`. Same-shore core distances are unchanged. Every old cloud-core distance began at least `sqrt(3)-1/(100M)` after scaling and loses at most `1/10` under the core motion, hence remains above one. Cloud-cloud distances are unchanged and exceed one.

Each `q_k=(k+1)e1-e2`, for `k=3,5`, has exactly two unit core neighbors, `k e1` and `(k+1)e1`; both are in the negative shore and move with `y_k`, preserving exactly those two contacts. Every other same-shore core distance is at least `sqrt(3)`. The loaded force hull is a regular hexagon of circumradius `M` and inradius `sqrt(3)M/2>6`; `|y_3|^2=12.51` and `|y_5|^2=30.31`, so both new sites lie strictly inside it. For opposite-shore core points, projection on the unit vector `w` gives

```text
w dot(p' - y_k) >= (k+3)/2 - 1/5 >= 14/5 > 1.
```

Here the minimum uses `w dot p>=1/2` on the positive lattice shore. The source report says this projected separation is greater than `3`; for `k=3` the displayed lower bound is `14/5`, so that stronger sentence is not correct. The repaired bound above is enough for every required lower constraint.

For a cloud index `ell`, if `|q_k-ell|>=sqrt(3)`, then

```text
|y_k-s ell| >= sqrt(3)-1/10-1/(100M) > 1.
```

If `|q_k-ell|=1`, the point is excluded from `I_M` unless it is one of `(k+1,-2)` or `(k+2,-2)` in lattice coordinates. For those two possible cloud indices, the squared distances before the small cloud scaling are respectively `111/100` and `121/100`; the scaling displacement is at most `1/(100M)`, so both remain strictly above one. Also `|y_3-y_5|=2`. These cases exhaust every lower pair involving the new sites.

For upper constraints, the two opposite-tip pairs in directions `e1` and `e2` have squared length `4M^2-4M/10+4/100`; the opposite pair in direction `w` has squared length `4M^2-8M/10+4/100`, which is smaller for `M>=20`. A non-diameter core pair initially has length at most `2M-1`; its change is at most `1/5`, still below `D_1`. Core-cloud distances are at most `M+1/10+sR_0 < 2M-7/50`. Also

```text
D_1^2 - (2M-7/50)^2 = (4/25)M + 51/2500 > 0,
```

so `2M-7/50<D_1`. Each inserted site has radius below six, so its distance to any retained old point is below `M+61/10 < 2M-7/50 < D_1` for `M>=20`; the new sites are two units apart. This proves the exact maximum formula and leaves positive upper slack at every pair for the later small downward step.

The four new contact vectors have strictly positive dot product with the downward velocity, so squared distance increases to first order. The other finitely many pairs involving either new site are strictly inside `(1,2M)` before the step. Continuity therefore supplies a common positive finite step small enough to preserve both bounds while making all four contacts strict. All old contacts survive, no other contact is created, and the endpoint contact graph is a subgraph of the triangle-free old core graph, hence triangle-free.

## Certificate boundary and hostile scope

I inspected and reran the exact `Fraction`/integer certificate at the frozen branch tip. It checks every pair of the source, first endpoint, and triangle-free endpoint for `M=20` and `M=32` (2,158,200 and 16,270,713 pair checks respectively), verifies the exact diameter formula, contact counts, retained cloud labels, the two triangles at the first endpoint, and the finite downward step. It also checks two separate finite local regressions. It does **not** prove the all-`M` analytic argument, KKT equilibrium, macroscopic cap estimates, canonical mixed rigidity, or global optimality; the proof and canonical source-family regression supply those boundaries.

The local strict-rhombus completion blocker in the source is already represented by canonical `C-RHOMBUS-EDGE-COMPLETION-COLLISION-REGRESSION`; the partial-wall example is likewise a separate local guardrail. Neither is re-registered here. The present theorem adds the distinct all-`M` moved-core/refill endpoint and remains strictly nonglobal.

| Audit item | Verdict |
| --- | --- |
| Source family and positive-stress scope | PASS — already canonical under `C-PAIRED-CAP-SPOKE-NONGLOBAL-REGRESSION` |
| Exact moved-core same-cardinality endpoint | PASS — promote as a regression |
| Triangle-free finite endpoint | PASS — finite step follows from strict margins; certificate confirms `M=20,32` |
| Source claim that the opposite-shore projection exceeds `3` | NARROWED — the uniform lower bound needed here is `(k+3)/2-1/5`, at least `14/5` |
| Canonical cap refill or C-II/Level I conclusion | NOT CLAIMED |

The active C-II endpoint is unchanged: a canonical full-source finite move or discrete replacement must still check every lower and upper constraint and force strict contact loss at diameter `D` or a strict sub-`D` competitor.
