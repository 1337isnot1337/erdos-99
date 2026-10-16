#!/usr/bin/env python3
"""Exact projection-potential exclusion of the ten simple-wall H5 cases.

This is the zero-aware companion to
verify_target_c_support6_h5_uniform_infinity_extension_2026_09_18.py.
The simple-wall reciprocal chirotope has one prescribed zero triple.  A
generic projection order is again represented by a formal point U at infinity,
but the rank-three Grassmann--Pluecker test must allow an all-zero product
triple.  A nonzero product triple with no signs of both polarities is rejected.
"""

from itertools import combinations, permutations
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "verify_target_c_support6_h5_uniform_infinity_extension_2026_09_18.py"
spec = spec_from_file_location("h5_uniform_infinity", SOURCE)
uniform = module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(uniform)
h5 = uniform.h5


U = 7
ELEMENTS = tuple(range(8))


def weak_grassmann_pluecker_ok(table):
    """Check the realizable rank-three chirotope sign condition with zeros."""
    for subset in combinations(ELEMENTS, 5):
        for a in subset:
            rest = [x for x in subset if x != a]
            b, c, d, e = rest
            values = (
                uniform.chi(table, a, b, c) * uniform.chi(table, a, d, e),
                -uniform.chi(table, a, b, d) * uniform.chi(table, a, c, e),
                uniform.chi(table, a, b, e) * uniform.chi(table, a, c, d),
            )
            # The Pluecker relation can vanish identically.  Otherwise its
            # nonzero products must include both signs.
            if any(values) and not (
                any(value > 0 for value in values)
                and any(value < 0 for value in values)
            ):
                return False
    return True


def main():
    base = h5.enumerate_uniform_extensions()
    walls = h5.enumerate_simple_walls(base)
    _, full = h5.wall_survivors(base, walls)
    representatives = {}
    for target, signs, missing, edge_signs in full:
        representatives[h5.canonical_candidate(signs, missing, edge_signs)] = (
            target, signs, missing, edge_signs
        )
    representatives = list(representatives.values())
    assert len(representatives) == 10

    rows = []
    for _target, signs, _missing, edge_signs in representatives:
        valid = []
        for order in permutations(range(7)):
            table = uniform.extension_signs(signs, order)
            if weak_grassmann_pluecker_ok(table):
                valid.append(order)
        acyclic = [order for order in valid if uniform.is_acyclic(order, edge_signs)]
        assert not acyclic
        rows.append((len(valid), len(acyclic)))

    print("simple_wall_metric_orbits", len(representatives))
    print("weak_rank3_infinity_extensions_by_orbit", [n for n, _ in rows])
    print("acyclic_extensions_by_orbit", [n for _, n in rows])
    print("PASS: no simple-wall H5 projection extension admits a signed potential")


if __name__ == "__main__":
    main()
