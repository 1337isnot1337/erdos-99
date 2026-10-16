#!/usr/bin/env python3
"""Finite exact-coordinate replay of report index 599's diagnostic range.

This checks m=5..24 only. The all-m attachment/diameter formulas are proved in
its imported report; this script is not a substitute for those formulas.
"""
from __future__ import annotations


def cross(o: tuple[int, int], a: tuple[int, int], b: tuple[int, int]) -> int:
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def inside_convex(point: tuple[int, int], polygon: list[tuple[int, int]]) -> bool:
    signs = {1 if cross(polygon[i], polygon[(i + 1) % len(polygon)], point) > 0 else -1
             for i in range(len(polygon))
             if cross(polygon[i], polygon[(i + 1) % len(polygon)], point) != 0}
    return len(signs) <= 1


def run() -> dict[str, int]:
    checked = 0
    for m in range(5, 25):
        interior = {(i, j) for i in range(1, m) for j in range(1, m)}
        boundary = {
            (i, j)
            for i in range(m + 1)
            for j in range(m + 1)
            if i in (0, m) or j in (0, m)
        } - {(0, 0), (0, m), (m, 0), (m, m)}
        points = interior | boundary
        assert len(boundary) == 4 * m - 4
        assert len(points) == (m - 1) ** 2 + 4 * m - 4

        point_list = sorted(points)
        contacts: dict[tuple[int, int], set[tuple[int, int]]] = {p: set() for p in points}
        for i, p in enumerate(point_list):
            for q in point_list[i + 1:]:
                d2 = (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2
                assert d2 >= 1
                if d2 == 1:
                    contacts[p].add(q)
                    contacts[q].add(p)
        for p, neighbors in contacts.items():
            assert all((p[0] + p[1]) % 2 != (q[0] + q[1]) % 2 for q in neighbors)
        for p in points:
            for q in contacts[p]:
                assert p in contacts[q]  # symmetric adjacency
                for r in contacts[p] & contacts[q]:
                    assert False, (m, p, q, r)  # no unit-contact triangle

        for i, j in interior:
            expected = {(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)}
            assert expected <= points
            assert contacts[(i, j)] == expected
            assert sum(q[0] - i for q in expected) == 0
            assert sum(q[1] - j for q in expected) == 0

        hull = [
            (1, 0), (m - 1, 0), (m, 1), (m, m - 1),
            (m - 1, m), (1, m), (0, m - 1), (0, 1),
        ]
        assert all(inside_convex(p, hull) for p in interior | boundary)
        diameter2 = max(
            (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2
            for i, p in enumerate(hull) for q in hull[i + 1:]
        )
        assert diameter2 == m * m + (m - 2) ** 2
        attachment_count = 4 * m - 4
        assert attachment_count * attachment_count > diameter2
        checked += 1
    return {'m_values_checked': checked, 'first_m': 5, 'last_m': 24}


if __name__ == '__main__':
    print(run())
