# Target C — propagate the branch-aware atomic gap

## Question

Can the unreviewed full-core Type-II matched train-measure gap `0.0071` be
carried through the Section-171, outer-energy, complement-rhombus-incidence,
and low-`t` chains with all hypotheses and branch endpoints preserved, and
does the resulting quantitative margin close any remaining source-wide
diameter-bracing obligation?

## Starting evidence

Read the [iterative-pruning pair-payment and atomic-gap track](../docs/research/tracks/target-c-iterative-pruning-atomic-gap.md),
the [current Target C frontier](../docs/targets/target-c/CURRENT.md), the
[candidate registry](../docs/targets/target-c/candidate-registry.json), and
the authoritative [theorem-state manifest](../docs/state/theorem-state.yaml).
The `0.0071` all-train and strict-rhombus bounds are unreviewed in the
destination. The older `0.0050` Section-171 certificate remains valid only at
its stated input; the stronger gap has not been propagated through it.

## Work boundary

- Reconstruct the exact `0.0071` branch conditions and the downstream
  inequalities before substituting the stronger constant.
- Preserve the full-core Type-II scope, strict-rhombus transfer, all actual
  diameter pairs, contact isolates, and every hypothesis used by outer-energy
  and complement-incidence estimates.
- Produce an outward-rational certificate or proof for every new endpoint;
  update finite verifiers and negative controls where their checked domain
  changes.
- If a downstream implication fails, isolate the exact failed interval or
  hypothesis and keep the valid `0.0071` upstream result separate.

## Do not infer

- Do not transfer the `0.0050` Section-171 output by numerical monotonicity
  unless the proof's constants and endpoint functions are rederived.
- Do not promote source hostile-audit PASS labels to destination audit status.
- Do not infer C-II or Level I closure from a stronger asymptotic train bound.
- Do not omit a source label, inactive diameter upper pair, contact isolate,
  macroscopic-container branch, or finite-endpoint cardinality condition.

## Reproduction

```bash
python3 research/verify_target_c_iterative_minimax_atomic_gap_0050.py
python3 research/verify_target_c_g0050_global_propagation.py
python3 research/verify_target_c_branch_aware_atomic_gap_0071.py
python3 research/verify_target_c_branch_aware_atomic_gap_0071_pi_enclosure.py
python3 tools/task_context.py target-c-branch-aware-atomic-gap
```
