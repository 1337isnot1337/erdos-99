#!/usr/bin/env python3
from collections import Counter
from itertools import combinations, permutations, product

# Third surviving support in the exact two-singleton support narrowing:
# [0123]^3 [0124]^2 [0134]^2 [0234]^2.
SUPPORT = {
    frozenset((0, 1, 2, 3)): 3,
    frozenset((0, 1, 2, 4)): 2,
    frozenset((0, 1, 3, 4)): 2,
    frozenset((0, 2, 3, 4)): 2,
}
VARYING = tuple(sorted((s for s, m in SUPPORT.items() if m < 3), key=lambda s: tuple(sorted(s))))
EXPECTED_AUTOS = {
    (0, 1, 2, 3, 4, 5, 6),
    (0, 1, 2, 3, 4, 6, 5),
    (0, 1, 3, 2, 4, 5, 6),
    (0, 1, 3, 2, 4, 6, 5),
    (0, 2, 1, 3, 4, 5, 6),
    (0, 2, 1, 3, 4, 6, 5),
    (0, 2, 3, 1, 4, 5, 6),
    (0, 2, 3, 1, 4, 6, 5),
    (0, 3, 1, 2, 4, 5, 6),
    (0, 3, 1, 2, 4, 6, 5),
    (0, 3, 2, 1, 4, 5, 6),
    (0, 3, 2, 1, 4, 6, 5),
}
EXPECTED_REPS_AND_SIZES = [
    ((0, 0, 0), 6),
    ((0, 0, 1), 3),
    ((0, 1, 0), 6),
    ((0, 1, 1), 6),
    ((0, 1, 2), 3),
    ((0, 2, 0), 2),
    ((1, 1, 1), 1),
]


def cycle_key(cycle):
    cycle = tuple(cycle)
    candidates = []
    for z in (cycle, tuple(reversed(cycle))):
        for i in range(4):
            candidates.append(z[i:] + z[:i])
    return min(candidates)


def cycles_on(support):
    support = tuple(sorted(support))
    first = support[0]
    out = {cycle_key((first,) + tail) for tail in permutations(support[1:])}
    assert len(out) == 3
    return tuple(sorted(out))


def state_options(support):
    cycles = cycles_on(support)
    # A multiplicity-two support uses two of the three possible unoriented
    # four-cycles. State 0,1,2 is the lexicographic two-subset below.
    return tuple(frozenset(x) for x in combinations(cycles, 2))


def automorphisms():
    out = []
    for p in permutations(range(7)):
        mapped = {frozenset(p[v] for v in s): m for s, m in SUPPORT.items()}
        if mapped == SUPPORT:
            out.append(p)
    assert set(out) == EXPECTED_AUTOS
    return tuple(out)


def mapped_cycle(cycle, p):
    return cycle_key(tuple(p[v] for v in cycle))


def action_on_assignments(p, assignments, assignment_index, options):
    action = []
    for assignment in assignments:
        target = [None] * len(VARYING)
        for i, support in enumerate(VARYING):
            mapped_support = frozenset(p[v] for v in support)
            j = VARYING.index(mapped_support)
            mapped_choice = frozenset(mapped_cycle(c, p) for c in options[support][assignment[i]])
            target[j] = options[mapped_support].index(mapped_choice)
        action.append(assignment_index[tuple(target)])
    assert sorted(action) == list(range(len(assignments)))
    return tuple(action)


def main():
    assert [tuple(sorted(s)) for s in VARYING] == [(0, 1, 2, 4), (0, 1, 3, 4), (0, 2, 3, 4)]
    options = {s: state_options(s) for s in VARYING}
    autos = automorphisms()
    assignments = tuple(product(range(3), repeat=3))
    assignment_index = {a: i for i, a in enumerate(assignments)}
    actions = tuple(action_on_assignments(p, assignments, assignment_index, options) for p in autos)

    fixed = Counter(sum(action[i] == i for i in range(len(assignments))) for action in actions)
    assert fixed == Counter({3: 10, 27: 2})
    assert sum(k * v for k, v in fixed.items()) // len(autos) == 7

    seen = set()
    orbits = []
    for i in range(len(assignments)):
        if i in seen:
            continue
        orbit = {i}
        stack = [i]
        while stack:
            j = stack.pop()
            for action in actions:
                k = action[j]
                if k not in orbit:
                    orbit.add(k)
                    stack.append(k)
        seen.update(orbit)
        orbits.append(tuple(sorted(orbit)))

    assert len(seen) == 27
    assert len(orbits) == 7
    assert Counter(map(len, orbits)) == Counter({6: 3, 3: 2, 2: 1, 1: 1})
    reps_and_sizes = [(assignments[orbit[0]], len(orbit)) for orbit in orbits]
    assert reps_and_sizes == EXPECTED_REPS_AND_SIZES

    print("automorphisms", len(autos))
    print("raw_assignments", len(assignments))
    print("fixed_count_census", dict(sorted(fixed.items())))
    print("orbit_size_census", dict(sorted(Counter(map(len, orbits)).items())))
    print("representatives", reps_and_sizes)
    print("PASS: support3 reduces from 27 raw orientations to exactly 7 support-automorphism classes")


if __name__ == "__main__":
    main()
