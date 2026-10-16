#!/usr/bin/env python3
"""Exact S7 orbit count for six no-root K8 four-cycles.

A no-root four-cycle is a simple 4-cycle on vertices {1,...,7}; there are
C(7,4)*3 = 105.  S7 relabels these 105 objects.  Burnside's lemma counts
orbits of unordered six-subsets exactly.  For each vertex permutation, the
number of invariant t-subsets is the coefficient of x^t in

    product_C (1 + x^{|C|}),

where C ranges over cycles of the induced permutation on the 105 four-cycles.
All arithmetic is integral.  As a cross-check, t=5 reproduces the independently
committed 20,451 S7 orbit count used by the five-no-root verifiers.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations
from math import comb, factorial

VERTICES = tuple(range(1, 8))


def edge(a, b):
    return (a, b) if a < b else (b, a)


def cycle_key(order):
    return tuple(sorted(edge(order[i], order[(i + 1) % 4]) for i in range(4)))


def four_cycles():
    out = set()
    for quad in combinations(VERTICES, 4):
        a, b, c, d = quad
        # Exactly the three unoriented Hamiltonian cycles of K4.
        out.add(cycle_key((a, b, c, d)))
        out.add(cycle_key((a, b, d, c)))
        out.add(cycle_key((a, c, b, d)))
    result = tuple(sorted(out))
    assert len(result) == comb(7, 4) * 3 == 105
    return result


CYCLES = four_cycles()
INDEX = {c: i for i, c in enumerate(CYCLES)}


def vertex_cycle_type(perm):
    mapping = {VERTICES[i]: perm[i] for i in range(7)}
    seen = set()
    lengths = []
    for v in VERTICES:
        if v in seen:
            continue
        cur = v
        length = 0
        while cur not in seen:
            seen.add(cur)
            cur = mapping[cur]
            length += 1
        lengths.append(length)
    return tuple(sorted(lengths, reverse=True))


def induced_permutation(perm):
    mapping = {VERTICES[i]: perm[i] for i in range(7)}
    image = []
    for c in CYCLES:
        mapped = tuple(sorted(edge(mapping[a], mapping[b]) for a, b in c))
        image.append(INDEX[mapped])
    assert sorted(image) == list(range(105))
    return tuple(image)


def induced_cycle_lengths(image):
    seen = [False] * len(image)
    lengths = []
    for start in range(len(image)):
        if seen[start]:
            continue
        cur = start
        length = 0
        while not seen[cur]:
            seen[cur] = True
            cur = image[cur]
            length += 1
        lengths.append(length)
    assert sum(lengths) == 105
    return tuple(sorted(lengths))


def fixed_subset_count(induced_lengths, t):
    coeff = [0] * (t + 1)
    coeff[0] = 1
    for length in induced_lengths:
        for j in range(t, length - 1, -1):
            coeff[j] += coeff[j - length]
    return coeff[t]


def class_size(cycle_type):
    counts = Counter(cycle_type)
    denominator = 1
    for length, multiplicity in counts.items():
        denominator *= (length ** multiplicity) * factorial(multiplicity)
    return factorial(7) // denominator


def main():
    by_type = defaultdict(list)
    burnside5 = 0
    burnside6 = 0

    for perm in permutations(VERTICES):
        ctype = vertex_cycle_type(perm)
        lengths = induced_cycle_lengths(induced_permutation(perm))
        fixed5 = fixed_subset_count(lengths, 5)
        fixed6 = fixed_subset_count(lengths, 6)
        by_type[ctype].append((lengths, fixed5, fixed6))
        burnside5 += fixed5
        burnside6 += fixed6

    assert sum(len(v) for v in by_type.values()) == factorial(7) == 5040

    expected_fixed6 = {
        (1, 1, 1, 1, 1, 1, 1): 1609344100,
        (2, 1, 1, 1, 1, 1): 926980,
        (2, 2, 1, 1, 1): 64036,
        (2, 2, 2, 1): 64036,
        (3, 1, 1, 1, 1): 595,
        (3, 2, 1, 1): 49,
        (3, 2, 2): 19,
        (3, 3, 1): 595,
        (4, 1, 1, 1): 100,
        (4, 2, 1): 100,
        (4, 3): 1,
        (5, 1, 1): 0,
        (5, 2): 0,
        (6, 1): 19,
        (7,): 0,
    }

    rows = []
    for ctype in sorted(by_type, reverse=True):
        records = by_type[ctype]
        size = len(records)
        assert size == class_size(ctype)
        fixed5_values = {r[1] for r in records}
        fixed6_values = {r[2] for r in records}
        assert len(fixed5_values) == 1
        assert len(fixed6_values) == 1
        fixed5 = fixed5_values.pop()
        fixed6 = fixed6_values.pop()
        assert expected_fixed6[ctype] == fixed6
        rows.append((ctype, size, fixed5, fixed6))

    assert len(rows) == 15
    assert burnside5 % factorial(7) == 0
    assert burnside6 % factorial(7) == 0
    orbits5 = burnside5 // factorial(7)
    orbits6 = burnside6 // factorial(7)

    assert comb(105, 5) == 96560646
    assert comb(105, 6) == 1609344100
    assert orbits5 == 20451
    assert burnside5 == 103073040
    assert orbits6 == 325911
    assert burnside6 == 1642591440

    print("PASS: exact S7 orbit count for six no-root four-cycle subsets")
    print("no_root_four_cycles", len(CYCLES))
    print("six_subsets", comb(105, 6))
    print("S7_orbits_six_subsets", orbits6)
    print("burnside_sum_six", burnside6)
    print("crosscheck_S7_orbits_five_subsets", orbits5)
    print("crosscheck_burnside_sum_five", burnside5)
    print("cycle_type class_size fixed_5_subsets fixed_6_subsets")
    for ctype, size, fixed5, fixed6 in rows:
        print(ctype, size, fixed5, fixed6)


if __name__ == "__main__":
    main()
