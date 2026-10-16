#!/usr/bin/env python3
"""Exact aggregate census for the generic support-seven H6 complete-angle lift.

This verifier composes two already committed exact-checking layers:

  1. the 14,174 -> 6,308 ground-coupled affine reduction;
  2. the 85-variable complete-angle lift implemented by
     verify_target_c_support7_h6_complete_angle_chunk_2026_09_19.py.

The floating-point LP is used only to propose a dual support.  Every exclusion
counted below is accepted only after the complete-angle verifier checks the
Farkas identity coefficientwise over fractions.Fraction.
"""

from collections import Counter
from pathlib import Path
import contextlib
import importlib.util
import io

HERE = Path(__file__).resolve().parent


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    module = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    return module


G = load(
    "h6_ground",
    "verify_target_c_support7_h6_ground_coupled_affine_reduction_2026_09_19.py",
)
C = load(
    "h6_complete_angle",
    "verify_target_c_support7_h6_complete_angle_chunk_2026_09_19.py",
)

tri = G.tri

# The complete-angle build repeatedly reconstructs ray orders.  Cache only on
# the actual raw hull orders and chirotope from which those orders are derived.
_original_orders_for_state = C.orders_for_state
_order_cache = {}


def cached_orders_for_state(state):
    _, _, _, raws, chi, _, _ = state
    key = (
        tuple(tuple(raws[v]) for v in range(6)),
        repr(chi),
    )
    if key not in _order_cache:
        _order_cache[key] = _original_orders_for_state(state)
    return _order_cache[key]


C.orders_for_state = cached_orders_for_state


def ground_coupled_survivors(states):
    """Reproduce the committed exact 14,174 -> 6,308 endpoint."""
    previous = [tri.exact_system(state) for state in states]
    systems = [
        G.extended_system(state, old)
        for state, old in zip(states, previous)
    ]
    keys = [G.system_key(system) for system in systems]

    first = {}
    for i, key in enumerate(keys):
        first.setdefault(key, i)
    assert len(first) == 9038

    certified = set()
    for key, i in first.items():
        candidate = G.numerical_dual_candidate(systems[i])
        if candidate is None:
            continue
        if G.exactify_and_check(systems[i], candidate) is not None:
            certified.add(key)

    assert len(certified) == 5854
    remaining = [i for i, key in enumerate(keys) if key not in certified]
    assert len(remaining) == 6308
    assert Counter(states[i][1] for i in remaining) == Counter({
        "C7": 4936,
        "C3+C4": 1372,
    })
    return remaining


def main():
    states = tri.collect_survivors()
    assert len(states) == 14174
    remaining = ground_coupled_survivors(states)

    excluded = []
    exact_failures = []
    solver_failures = []
    forced_values = Counter()
    max_denominator = 1

    for i in remaining:
        system = C.build_system(states[i])
        margin, result = C.numerical_candidate(system)
        if margin is None:
            solver_failures.append(i)
            continue
        if margin > 1e-8:
            continue

        exact = C.exactify(system, result)
        if exact is None:
            exact_failures.append(i)
            continue

        forced, denominator = exact
        excluded.append(i)
        forced_values["zero" if forced == 0 else "negative"] += 1
        max_denominator = max(max_denominator, denominator)

    # Nothing numerical is promoted to an exclusion without exactification.
    assert solver_failures == []
    assert exact_failures == []
    assert len(excluded) == 616
    assert forced_values == Counter({"zero": 616})
    assert max_denominator == 102

    assert Counter(states[i][1] for i in excluded) == Counter({
        "C7": 472,
        "C3+C4": 144,
    })
    assert Counter(
        "".join(map(str, states[i][5])) for i in excluded
    ) == Counter({
        "145": 4,
        "235": 58,
        "236": 202,
        "245": 44,
        "256": 202,
        "346": 44,
        "347": 4,
        "356": 58,
    })

    excluded_set = set(excluded)
    final = [i for i in remaining if i not in excluded_set]
    assert len(final) == 5692
    assert Counter(states[i][1] for i in final) == Counter({
        "C7": 4464,
        "C3+C4": 1228,
    })
    assert Counter(
        "".join(map(str, states[i][5])) for i in final
    ) == Counter({
        "145": 8,
        "156": 16,
        "235": 772,
        "236": 1524,
        "237": 16,
        "245": 514,
        "256": 1524,
        "345": 24,
        "346": 514,
        "347": 8,
        "356": 772,
    })

    print("PASS")
    print("ground-coupled generic H6 input: 6308 = 4936 C7 + 1372 C3+C4")
    print("complete-angle exact exclusions: 616 = 472 C7 + 144 C3+C4")
    print("all 616 complete-angle certificates force the strict-facet average to 0")
    print("maximum exact complete-angle dual denominator: 102")
    print("remaining generic H6 cells: 5692 = 4464 C7 + 1228 C3+C4")


if __name__ == "__main__":
    main()
