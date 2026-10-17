# Target C — vacancy and collective refill capacity

**Investigation:** `target-c-capacity-collective-refill-current-20261017`. **Status:** open. Source: `e396ea07887dd0528b817ce4e656ff0e6b01f8fb`.

Downstream use: Name the downstream claim or decision this result can change, the exact quantity it controls, and the remaining hypothesis before extending the investigation.

## Question

Can any fixed-frame vacancy/refill theorem be extracted at sufficient scale
from every canonical C-II source to give a same-cardinality competitor or an
admissible strict endpoint, after accounting for the exact capacity barriers
and every lower and upper pair constraint?

## Starting evidence

Begin with the [full research track](../docs/research/tracks/target-c-capacity-collective-refill.md)
and its [candidate registry entries](../docs/targets/target-c/candidate-registry.json).
The track connects eight proof candidates and their exact verifiers:

- One-vacancy strictification, actual unit-wall activation, and two-boundary-pin refill.
- One-pin oblique and two-side polynomial refill, with their distinct frame hypotheses and explicit margins.
- Triangular two-pin capacity and universal convex unit-pentagon capacity, which block overstrong refill claims.
- Exact multishear traffic domination, which controls a weighted mean but not the maximum diameter.

Read the destination [current Target C frontier](../docs/targets/target-c/CURRENT.md),
the canonical [theorem-state manifest](../docs/state/theorem-state.yaml), and
the full-source finite-endpoint rule before using any candidate. These eight
reports remain unreviewed unless the destination manifest says otherwise.

## Next proof obligation

Find a source-wide extraction theorem for a qualifying actual wall, vacancy,
population deficit, or common feasible multishear cell. Preserve the full
source population, all unit lower bounds, all actual and inactive diameter
upper bounds, and (at diameter `D`) triangle-freeness plus a strict decrease
in the contact/actual-diameter-pair lexicographic objective. If the proposed
extraction fails, give an exact source-compatible obstruction under the same
hypotheses.

## Stop conditions

- Do not infer a source wall or vacancy from an exact fixed-frame packet.
- Do not use interior capacity as a cardinality payment without identifying
  the deleted and restored labels.
- Do not apply the one-pin estimate at the triangular endpoint.
- Do not infer a `K+1` strict capacity from two-pin constructions that reach
  only `K`.
- Do not sum individual pentagon interiors as if each supplied one spare
  site; the universal capacity theorem rules that out.
- Do not turn a mean-diameter-square decrease into a maximum-diameter
  decrease, and check inactive upper pairs in any proposed shear.
- Do not change C-II or Level I status from these unreviewed results.

## Reproduction

```bash
python3 research/verify_target_c_boundary_vacancy_funded_collective_refill_2026_10_05.py
python3 research/verify_target_c_multishear_traffic_domination_2026_10_05.py
python3 research/verify_target_c_one_boundary_pin_oblique_refill_2026_10_05.py
python3 research/verify_target_c_one_vacancy_collective_strictification_2026_10_05.py
python3 research/verify_target_c_triangular_two_pin_capacity_2026_10_05.py
python3 research/verify_target_c_two_side_polynomial_refill_2026_10_05.py
python3 research/verify_target_c_unit_pentagon_capacity_2026_10_05.py
python3 research/verify_target_c_vacancy_funded_unit_wall_activation_2026_10_05.py
python3 tools/task_context.py target-c-capacity-collective-refill
```
