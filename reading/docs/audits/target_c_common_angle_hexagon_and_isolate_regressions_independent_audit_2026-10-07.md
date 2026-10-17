> Generated reading edition · [exact source](../../../docs/audits/target_c_common_angle_hexagon_and_isolate_regressions_independent_audit_2026-10-07.md) · source SHA-256 `446c4adb88f8c7e28b33bfff6fa87a0ac7d7f5eed29d6e5b1cecd100c9717e78`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-5161FCF4FFE8","canonical":false,"claim_ids":["C-COMMON-ANGLE-HEXAGON-NONHORN-REGRESSION","C-RETAINED-ISOLATE-COMMON-ANGLE-UPPER-REGRESSION"],"claim_statuses":{"C-COMMON-ANGLE-HEXAGON-NONHORN-REGRESSION":"regression","C-RETAINED-ISOLATE-COMMON-ANGLE-UPPER-REGRESSION":"regression"},"index":"docs/state/artifact-index.jsonl","status":"regression","target":"target-c"} -->
# Independent audit: common-angle hexagon closure and isolate upper check

Date: 2026-10-07. Audit base: `c4bee27a0cd3b971f386fa0b16c26082b867e4e9`, state `2026-10-07.audit.94`; Target C C-II remains open. Frozen source: Worker 1 branch `research/sol/target-c-owner-order-closure-20261006` at `bf288c82e8a62466d5580025c94e750a177e63e2`. Source report `docs/reports/target_c_common_angle_train_closure_and_full_endpoint_2026-10-06.md` SHA-256 is `176b0eae82355d398d6674ce0e047446e443feb6ea11d31e4f1e9f9d45df9233`; its exact verifier `research/verify_target_c_common_angle_train_endpoint_2026_10_06.py` SHA-256 is `a5feeb67ff9b97123c016f5cccf9d839928c8cfb41f0ac55951de42a4efab14b`; captured verifier output SHA-256 is `fb1bc03761f7dadab87e5b5672c21d12c2e9dc2291f341552996edb33a21593f`.

## Verdict

**REGRESSION VALID — promote two narrow finite claims.** The independent-side-bit closure relation for one regular-hexagon face is not Horn-representable, even after existential Horn auxiliaries. Separately, a common-angle motion that strictly shortens the six-point core can lengthen the unique actual diameter when a contact isolate is retained. These are local guards only; they establish no feasible common-angle move for a canonical source and no C-II or Level I consequence.

The audit treats the two claims separately. It does not audit the surrounding all-source common-angle reduction, the pentagon-component propagation, the active-diameter amplitude thresholds, or any proposed arbitrary-source motion.

## 1. The six-side closure relation is not Horn

Let the cyclic unit edge vectors of a regular hexagon be

```text
w0=(1,0), w1=(1/2,sqrt(3)/2), w2=(-1/2,sqrt(3)/2),
w3=(-1,0), w4=(-1/2,-sqrt(3)/2), w5=(1/2,-sqrt(3)/2).
```

For six independent Boolean side choices `x_j`, rotate side `j` by a common angle `theta` exactly when `x_j=1`. Since `sum_j w_j=0`, the new edge sum is

```text
sum_j Rot(x_j*theta) w_j
  = (Rot(theta)-I) sum_j x_j w_j.
```

For `theta` not a multiple of `2*pi`, `Rot(theta)-I` is invertible. Thus the exact closure relation is

```text
R = {x in {0,1}^6 : sum_j x_j*w_j = 0}.
```

Its ten assignments are counted without computation: the empty set; the three opposite pairs; the two alternating triples; the three four-element complements of opposite pairs; and the full set. No one-element or five-element subset balances. In particular

```text
a=(1,0,0,1,0,0) in R,
b=(1,0,1,0,1,0) in R,
a meet b=(1,0,0,0,0,0) not in R.
```

Every Horn relation is closed under coordinatewise meet. For an implication clause, if a meet makes every antecedent true, both original assignments made them true, so both made the consequent true; the meet does too. The same argument covers an all-negative Horn clause. Existential projection preserves meet closure: choose witnesses for two visible assignments, meet the full assignments and their witnesses, and project. Since `R` is not meet-closed, no Horn formula with any number of existential auxiliary variables represents `R` exactly.

This is scoped to six independent side bits on this single face relation. The six-point construction has a 6-cycle as its complete unit-contact graph, so its sides have no extra local rhombus equality. The proof does not show that the assignment relation of an arbitrary train/face network, after its variable identifications and other constraints, is non-Horn.

## 2. Exact local realizations and verifier boundary

For each `x` in `R`, the rotated edge vectors sum to zero and each retains unit length. At angle zero, every nonconsecutive vertex pair in the regular hexagon has length `sqrt(3)` or `2`. By continuity, for sufficiently small nonzero `theta` all nonconsecutive distances remain strictly above one; the polygon remains strictly convex because each successive edge turn stays in `(0,pi)`. Thus each closure state gives a physical six-point 6-cycle near the regular hexagon.

I inspected and ran the frozen exact `Q(sqrt(3))` verifier:

```sh
python3 research/verify_target_c_common_angle_train_endpoint_2026_10_06.py
```

Its deterministic output is preserved at `research/target_c_common_angle_train_endpoint_certificate_2026_10_07.json`. It enumerates 64 bit states and finds ten closed states; it checks the meet witness, 300 core contact/noncontact lower comparisons at `tan(theta/2)=+/-1/10`, and 420 exact pair-change identities including the isolate. Exact rational coefficients and the `Q(sqrt(3))` sign routine are used throughout. The algebraic count and meet argument above do not depend on those samples.

## 3. A retained isolate invalidates one core-only upper endpoint

Integrate the same edge list from `p0=(0,0)`. The six-point core has contact cycle `p0,...,p5,p0`; its three diameters have squared length four. Add the fixed point `z=(-4,0)`. Direct pair distances show the seven-point source is unit-separated, `z` is a contact isolate, and its unique actual diameter pair is `p2,z`, where `p2=(3/2,sqrt(3)/2)` and `|p2-z|^2=31`.

Use the alternating state `b=(1,0,1,0,1,0)` and `t=tan(theta/2)=1/10`. Its selected prefix at `p2` is `y2=w0`, hence

```text
p2' = p2 + (Rot(theta)-I)w0,
cos(theta)=99/101, sin(theta)=20/101.
```

Exact expansion gives

```text
|p2'-z|^2 - |p2-z|^2 = (20*sqrt(3)-18)/101 > 0.
```

The verifier checks that all 15 core pairs after this motion are strictly below four, while the retained isolate's unique old diameter pair grows. This proves the stated upper-check regression: the core-only strict sub-diameter endpoint does not extend with this frozen isolate. The verifier does **not** establish lower feasibility of every isolate-to-core pair after the move, and the audit does not claim a full-source competitor or a globally optimal seven-point source.

## 4. Hostile scope checks and disposition

| Claim | Verdict | Canonical disposition |
| --- | --- | --- |
| Independent six-side regular-hexagon closure relation is not Horn-representable, including after existential Horn auxiliaries | REGRESSION VALID | Promote `C-COMMON-ANGLE-HEXAGON-NONHORN-REGRESSION` |
| The alternating strict core endpoint grows the actual diameter after retaining `z=(-4,0)` | REGRESSION VALID | Promote `C-RETAINED-ISOLATE-COMMON-ANGLE-UPPER-REGRESSION` |
| General coupled train network has a non-Horn assignment relation | NOT CLAIMED | No conclusion; variable identifications and external clauses may change the relation |
| A beneficial pattern exists in a canonical source, or the isolate move is a full feasible endpoint | NOT PROVED | Neither follows from this finite example |
| C-II or Level I closure | NOT PROVED | Both remain open |

The seven-point example has an actual diameter endpoint at a contact isolate, so it is outside the canonical mixed-rigidity hypotheses. It does not contradict the active face-coupled quarter-fold audit, which requires the full-source old upper inequalities to pass. No source branch or worktree was modified.
