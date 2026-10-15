#!/usr/bin/env python3
"""Exact finite regressions for planar near-unit face/path reductions.

Encodes actual point distances and exact contact preservation, tiny unary
rhombus overlap, and a source matching that becomes cyclic after owner
identification. Omits global source KKT, actual nested train ownership,
ONE-SIGN diameter feasibility and global optimality of these regressions.
"""

from fractions import Fraction as F
from itertools import combinations


def sq(p, q):
    return sum((a - b) ** 2 for a, b in zip(p, q))


def unit(t):
    return ((1 - t * t) / (1 + t * t), 2 * t / (1 + t * t))


def add(p, q):
    return tuple(a + b for a, b in zip(p, q))


def sub(p, q):
    return tuple(a - b for a, b in zip(p, q))


def main():
    zero = (F(0), F(0))
    u = (F(1), F(0))
    v = unit(F(577351, 1000000))
    new_u = unit(F(1, 1000000))
    points = [zero, u, v, add(u, v)]
    delta = sub(new_u, u)
    old = {e: sq(points[e[0]], points[e[1]]) for e in combinations(range(4), 2)}
    contacts = {e for e, d in old.items() if d == 1}
    assert contacts == {(0, 1), (0, 2), (1, 3), (2, 3)}
    assert all(d >= 1 for d in old.values())
    assert old[(1, 2)] > 1 and old[(0, 3)] > 1
    assert sq(delta, zero) < F(1, 100000) ** 2
    moved = [add(p, delta) if i in (1, 3) else p for i, p in enumerate(points)]
    assert all(sq(moved[i], moved[j]) == 1 for i, j in contacts)
    assert sq(moved[1], moved[2]) < 1

    # Cyclic order 0,u,u+v,v: excluded binary patterns have an isolated
    # ownership bit whose two-contact preservation needs displacement >1.
    cyclic = [points[i] for i in (0, 1, 3, 2)]
    allowed = set()
    for mask in range(16):
        bits = [(mask >> i) & 1 for i in range(4)]
        isolated = [i for i in range(4) if bits[(i - 1) % 4] == bits[(i + 1) % 4] != bits[i]]
        if isolated:
            i = isolated[0]
            a = sub(cyclic[i], cyclic[(i - 1) % 4])
            b = sub(cyclic[i], cyclic[(i + 1) % 4])
            necessary_delta = tuple(-x for x in add(a, b))
            assert sq(necessary_delta, zero) > 1
            assert sq(add(a, necessary_delta), zero) == 1
            assert sq(add(b, necessary_delta), zero) == 1
        else:
            allowed.add(mask)
    assert allowed == {0, 3, 6, 9, 12, 15}

    square = [zero, u, (F(1), F(1)), (F(0), F(1))]
    assert all(sq(square[i], square[j]) >= 1 for i, j in combinations(range(4), 2))
    assert sq(square[0], square[2]) == sq(square[1], square[3]) == 2
    # Both equal-threshold diagonals meet at their common midpoint.
    assert add(square[0], square[2]) == add(square[1], square[3])

    lengths = [F(3, 10000), F(2, 10000), F(1, 10000)]
    owners, source, conflicts = [], [], []
    for packet_index, (i, j) in enumerate(((0, 1), (1, 2), (2, 0))):
        a, b = lengths[i], lengths[j]
        e = min(a, b, abs(a - b)) ** 2 / 16
        horizontal = 1 - e
        pair_vector = (horizontal, -(a - b))
        base = (F(0), F(10 * packet_index))
        source.extend([add(base, pair_vector), base])
        owners.extend([i, j])
        dis_i, dis_j = (F(0), a), (F(0), b)
        f00 = sq(pair_vector, zero) - 1
        f10 = sq(add(pair_vector, dis_i), zero) - 1
        f01 = sq(sub(pair_vector, dis_j), zero) - 1
        f11 = sq(add(pair_vector, sub(dis_i, dis_j)), zero) - 1
        assert f00 > 0 and f10 > 0 and f01 > 0 and f11 < 0
        assert sq(pair_vector, zero) <= F(5, 4) ** 2
        assert abs(pair_vector[1]) <= F(1, 8)
        conflicts.append((2 * packet_index, 2 * packet_index + 1))
    distances = {e: sq(source[e[0]], source[e[1]]) for e in combinations(range(6), 2)}
    assert min(distances.values()) > 1
    assert {e for e, d in distances.items() if d <= F(5, 4) ** 2} == set(conflicts)
    assert max(sum(v in edge for edge in conflicts) for v in range(6)) == 1
    owner_edges = {tuple(sorted((owners[i], owners[j]))) for i, j in conflicts}
    assert owner_edges == {(0, 1), (1, 2), (0, 2)}

    t = F(1, 1000)
    core = sorted({(F(x), F(y)) for x in range(5) for y in range(5) if x in (0, 4) or y in (0, 4) or x == 3})
    isolate = (F(1), F(2) - t)
    original = core + [isolate]
    old = {e: sq(original[e[0]], original[e[1]]) for e in combinations(range(len(original)), 2)}
    assert min(old.values()) >= 1 and max(old.values()) == 32
    contacts = {e for e, d in old.items() if d == 1}
    iz = len(core)
    assert all(iz not in e for e in contacts)
    cut = {e for e in contacts if (core[e[0]][0] <= 3) != (core[e[1]][0] <= 3)}
    assert len(cut) == 5
    assert all({core[i][0] for i in e} == {3, 4} and core[e[0]][1] == core[e[1]][1] for e in cut)
    delta = sub(u, unit(t))
    fixed_isolate = [add(p, delta) if p[0] <= 3 else p for p in core] + [isolate]
    face_isolate = fixed_isolate[:-1] + [add(isolate, delta)]
    assert all(sq(fixed_isolate[i], fixed_isolate[j]) == 1 for i, j in contacts)
    assert all(sq(face_isolate[i], face_isolate[j]) == 1 for i, j in contacts)
    left_vertex = core.index((F(0), F(2)))
    assert sq(fixed_isolate[left_vertex], fixed_isolate[iz]) < 1
    assert sq(face_isolate[left_vertex], face_isolate[iz]) == old[(left_vertex, iz)] > 1
    assert all(sq(face_isolate[i], face_isolate[j]) >= 1 for i, j in old)
    assert all(old[(i, iz)] <= 31 for i in range(iz))
    assert all(sq(face_isolate[i], face_isolate[iz]) < 32 for i in range(iz))
    # Exact sufficient cloud margin: |delta| <1/100 and gamma_D >1/(2D)>1/12.
    assert sq(delta, zero) < F(1, 100) ** 2

    a, b = F(1, 1000), F(2, 1000)
    contact_gain = [(F(1), b - a), (F(1), 1 + b - a), zero, (F(0), F(-1))]
    old = {e: sq(contact_gain[e[0]], contact_gain[e[1]]) for e in combinations(range(4), 2)}
    old_c = {e for e, d in old.items() if d == 1}
    assert old_c == {(0, 1), (2, 3)}
    new_c = None
    for bit_i in (0, 1):
        for bit_j in (0, 1):
            moved = [add(p, (F(0), a * bit_i if i < 2 else b * bit_j)) for i, p in enumerate(contact_gain)]
            distances = {e: sq(moved[e[0]], moved[e[1]]) for e in old}
            assert min(distances.values()) >= 1
            assert all(distances[e] == 1 for e in old_c)
            assert (distances[(0, 2)] == 1) == (bit_i == bit_j == 1)
            if bit_i == bit_j == 1:
                assert max(distances.values()) == 5 < max(old.values())
                new_c = {e for e, d in distances.items() if d == 1}
    assert new_c == {(0, 1), (0, 2), (2, 3)}
    assert not any(all(tuple(sorted(e)) in new_c for e in combinations(triple, 2)) for triple in combinations(range(4), 3))
    print("PASS: square threshold; 16 rhombus patterns; tiny unary blocker; matching/owner-cycle regression; actual O–O isolate extension; triangle-free pure joint equality with strict diameter decrease")


if __name__ == "__main__":
    main()
