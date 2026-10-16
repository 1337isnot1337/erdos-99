#!/usr/bin/env python3
"""Exact finite certificate for excluding every simple-ground-wall H5 survivor.

This script imports the existing exact support-six H5 enumerator, reconstructs its
80 simple-wall survivors, collapses each duplicated ground ray to a signed
multiplicity, and checks that only two coefficient words occur. Summation by
parts then converts those two words into the two impossible forward-chord
identities recorded in the accompanying proof note.

Only integer signs, exact finite enumeration, and tuple ordering are used here.
No floating point or metric coordinates are used.
"""

from collections import Counter
from functools import cmp_to_key
import importlib.util
from pathlib import Path

BASE_PATH = Path(__file__).with_name(
    "verify_target_c_support6_reciprocal_h5_reduction_2026_09_18.py"
)
spec = importlib.util.spec_from_file_location("h5_base", BASE_PATH)
H = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(H)


def ray_class_order(signs, target):
    """Increasing raw ground-ray order after merging the unique tied pair."""
    _, u, v = target
    classes = [frozenset((u, v))]
    classes.extend(frozenset((j,)) for j in H.NONGROUND if j not in (u, v))

    def representative(cls):
        return min(cls)

    def cmp(a, b):
        aa, bb = representative(a), representative(b)
        c = H.chi(signs, 0, aa, bb)
        # Distinct ray classes on a simple wall cannot be collinear.
        assert c in (-1, 1)
        return -1 if c > 0 else 1

    return sorted(classes, key=cmp_to_key(cmp))


def signed_multiplicity_word(target, signs, edge_signs):
    order = ray_class_order(signs, target)
    coeff = []
    for cls in order:
        value = sum(1 if edge_signs[H.edge(0, j)] else -1 for j in cls)
        assert value != 0
        coeff.append(value)

    # Global reciprocal sign reversal is immaterial. Normalize the first entry.
    if coeff[0] < 0:
        coeff = [-x for x in coeff]
    assert sum(coeff) == 0
    return tuple(coeff)


def prefix_sums(word):
    out = []
    s = 0
    for x in word[:-1]:
        s += x
        out.append(s)
    return tuple(out)


def main():
    uniform = H.enumerate_uniform_extensions()
    assert len(uniform) == 370
    walls = H.enumerate_simple_walls(uniform)
    assert len(walls) == 316
    wall_result = H.wall_survivors(uniform, walls)
    wall_full = wall_result[1] if isinstance(wall_result, tuple) else wall_result
    assert len(wall_full) == 80

    words = Counter(
        signed_multiplicity_word(target, signs, edge_signs)
        for target, signs, _missing, edge_signs in wall_full
    )

    A = (1, -2, 1, -1, 1)
    B = (1, -1, 1, -2, 1)
    assert words == Counter({A: 40, B: 40})
    assert prefix_sums(A) == (1, -1, 0, -1)
    assert prefix_sums(B) == (1, 0, 1, -1)

    # If v_1,...,v_5 are the five distinct ground unit rays in increasing
    # angle and Delta_k=v_{k+1}-v_k, summation by parts gives
    #   sum c_j v_j = -sum_{k=1}^4 S_k Delta_k.
    # Hence ground equilibrium would require:
    # A: Delta_1 = Delta_2 + Delta_4;
    # B: Delta_4 = Delta_1 + Delta_3.
    # Forward chord arguments strictly increase inside one open halfplane, so
    # either positive-sum identity is impossible.

    print("simple_wall_survivors", len(wall_full))
    print("normalized_ground_words", dict(words))
    print("A_prefix", prefix_sums(A), "requires Delta_1 = Delta_2 + Delta_4")
    print("B_prefix", prefix_sums(B), "requires Delta_4 = Delta_1 + Delta_3")
    print("PASS: every simple-ground-wall H5 survivor violates ground unit-force equilibrium")


if __name__ == "__main__":
    main()
