> Generated reading edition · [exact source](../../../docs/audits/target_c_branch_aware_atomic_gap_0071_destination_independent_audit_2026-10-18.md) · source SHA-256 `37f2b8d87b41fa81528f318ba211d8e0db7dd24cedc9c31f32e5523615d9fe9e`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-1E42497B8891","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Destination exact-head audit: Target C branch-aware atomic gap 0.0071

Date: 2026-10-18. **Disposition: CONDITIONAL.** The matched-gap implication
reconstructs at its stated proof-only scope, conditional on the pair-payment
theorem and the listed train-measure inputs. Target C-II and Level I remain open.

## Exact source and review state

- Destination head reviewed: `7d0a450fe66991036541023f95c44c064a04b6a8`
  (tree recorded in the PR body).
- Theorem state: `2026-10-15.publication.2`; priority:
  `public-frontier.3`; catalogue: `public-frontier.9`.
- Candidate: `TARGET-C-BRANCH-AWARE-ATOMIC-GAP-0071-20260915`, currently
  `unreviewed` in the destination candidate registry.
- The destination candidate record explicitly says that an exact-head audit
  has not been claimed. A repository search found no existing destination audit
  for this ID. The prior source hostile audit is recorded as provenance only.
- The candidate report, source hostile audit, and both interval verifiers match
  the published SHA-256 and Git blob pins in `candidate.json` byte for byte.
  Their SHA-256 values are, respectively:

  | Artifact | SHA-256 |
  | --- | --- |
  | [`branch-aware proof`](../../research/target_c_branch_aware_iterative_pruning_atomic_gap_0071_2026-09-15.md) | `efe39d4523271be966ad4264959f8fa04474df6832d9bcd9fcc5513151b47ba6` |
  | [`source hostile audit`](../../research/target_c_branch_aware_iterative_pruning_atomic_gap_0071_hostile_audit_2026-09-15.md) | `0ecc90b876a568aa8ee9b57ad700fab712237083a8a072af4d19c3f91a480ba9` |
  | [`0.0071 interval verifier`](../../../research/verify_target_c_branch_aware_atomic_gap_0071.py) | `79ef18464e8d271af7b16b17310ada1d78526d3cfdb6f34ced58f6e52e94466c` |
  | [`Machin pi verifier`](../../../research/verify_target_c_branch_aware_atomic_gap_0071_pi_enclosure.py) | `f16635e93ffb5dc33d227eee6a44f6d721f6a503627fb43ec31bdf9c895f9009` |

The audit question is whether the branch-aware two-leaf minimax proves the
`0.0071` atomic train-measure floor, given the exact conditional pair-payment
bound, canonical full-core Type-II train-measure framework, and independent
strict-rhombus graph application. The affected quantities are only
`(T-q/2)/D`, `T_R/D`, and `sigma_R/D` at this proof-only scope.

## Independent reconstruction

Write `K=2/sqrt(3)`, `s=sqrt(Delta_2)`, `g=0.0071`, and assume for contradiction
that the absolute atomic train mass satisfies `A<=2s+g`. The generic orbit
square bound gives `W>=W_0=4s^2/(2s+g)` for a dominant exact `pi/3` orbit. With
`delta=W^2/4-E` and residual orbit mass `A-W`, Mantel's bound on all residual
orbits yields

```text
0 <= delta <= d_0 = s*g + g^2/4.
```

Writing the dominant three phase masses as `C>=U>=V`, `C+U+V=W`, and
`z=C-W/2`, triangle-freeness gives `E<=C(U+V)`, hence
`|z|<=sqrt(delta)`. For the two center-leaf pairs let `x,y` be missing-pair
masses and `h=C(U+V)-E`. Summing disjoint center neighborhoods over each actual
leaf-leaf crossing gives `C e(U,V)<=Vx+Uy`, so with
`a=1-V/C`, `b=1-U/C` one has `a*x+b*y<=h`; also `h=delta-z^2`.

The pair theorem has overload `e_L=(C+L-K)_+` and smaller family mass `L` for
each leaf `L in {U,V}`. Its two branches imply `e_L<=sqrt(10)*sqrt(rho)` when
`e_L/L<=sqrt(20/29)`, and always imply
`e_L<=sqrt(29/2)*sqrt(rho)`. The cap proof gives `C<K`. For positive `L`,
`e_L/L` is increasing in `L`, and `L<=W-C`, so both leaves lie in the stronger
branch whenever

```text
z <= z_* = (K-(1-r/2)(2s+g))/r,   r=sqrt(20/29).
```

If a leaf has zero mass, `e_L=0` because `C<K`; its pair inequality is trivial,
so no division by zero is needed. This endpoint is explicit in this audit.

For either coefficient `lambda` valid for both leaves, set
`F_U=C+U-lambda*sqrt(x)` and `F_V=C+V-lambda*sqrt(y)`. The pair bounds give
`F_U,F_V<=K`. Their maximum dominates the nonnegative `(a,b)` weighted
average. Cauchy, `a*x+b*y<=h`, and `UV<=(U+V)^2/4` give

```text
max(F_U,F_V) >= 3W/4 + z/2
                 - lambda*sqrt(h*(W+2z)/(W+6z)).
```

Using `W>=W_0`, `h<=d_0-z^2`, and the branch-safe piecewise coefficient
`sqrt(10)` for `z<=z_*` and `sqrt(29/2)` otherwise, the exact interval
certificate places this lower bound strictly above `K` throughout the full
feasible `z` interval. This contradicts `F_U,F_V<=K`. The contradiction uses a
fresh `g=0.0071` setup; it does not inherit the separate `0.0050` Section-171
output.

The canonical exposed-hull comparison `A<=(T-q/2)/D` then transfers the atomic
floor to the all-train quantity. For the rhombic result, the argument must be
run on the strict-rhombus train graph itself: it is simple and triangle-free,
its edge mass is `R_4`, its crossings have limiting projective angle `pi/3`,
and the pair-payment input must apply to its selected phase families. This is
not a deletion of singleton trains from the all-train conclusion. Finally,
`sigma_R=2T_R-4*sqrt(R_4)` and `R_4/D^2->Delta_2`, so the `T_R` floor gives
`liminf sigma_R/D>=2g=0.0142`.

## Adversarial checks and limits

The decisive falsification checks are: both leaf ratios at the branch boundary;
all feasible positive and negative center imbalance; the phase-family cap
`C<K`; positivity of `W+6z` for the weighted denominator; intervals crossing
the switch `z_*`; and the strict-rhombus transfer independently of all-train
singleton deletion. The verifier's whole `[-0.083,0.083]` mesh strictly contains
`|z|<=sqrt(d_0)`, and uses the weaker coefficient on every interval touching
the branch threshold. This audit also checked the zero-mass leaf endpoint.

The conditional pair-payment candidate
`TARGET-C-ITERATIVE-PRUNING-PAIR-PAYMENT-20260914` is itself still `unreviewed`
in the destination. I did not independently audit its inversion-cover,
iterative-deletion, or global crossing-order proof; it is an explicit premise
here. The dominant three-phase/full-core framework and the strict-rhombus
application likewise remain scoped inputs. These dependencies make the result
**conditional**, rather than an unconditional destination PASS. The older
source hostile audit was inspected only after reconstructing this proof; its
PASS is not treated as destination lifecycle evidence.

No source-wide train-family extraction is proved here. The macroscopic-container
branch remains separate. The `0.0071` floor does not give a KKT diameter-weight
floor, a finite same-cardinality competitor, or a C-II/Level I closure. The
next concrete step is the exact-head independent review of the named pair
payment premise; separately, the candidate's next quantitative implication is
to rederive Section 171 and the outer-energy/complement-incidence chains from
`0.0071` without importing the `0.0050` endpoint.

## Provenance and reproducibility

The source candidate is from `1337isnot1337/e-99` main
`42f0296d1aca068c809f74cee5dcdb4ebdb27c73`, tree
`e061f039eac44c286a00eacdcaa9a4cbbb877891`; the destination source reports and
verifiers are byte-identical at the pins above. The originating agent/model is
not identified in the available candidate record. Reviewer: `homelab-15`,
GPT-6 Luna xhigh, independent research session; mathematical proof reconstruction
and scoped verifier review. AI assistance is disclosed; no human mathematical
review is claimed. The first-party project research is offered under the
repository's Apache-2.0 contribution terms.

Commands run, exact outputs, repository checks, base refresh, and PR details are
recorded in the focused PR body and controller result file. This note does not
change the manifest, accepted lifecycle, priority, or theorem state. A required
repository-wide theorem-certificate replay is deferred to the merging agent.
