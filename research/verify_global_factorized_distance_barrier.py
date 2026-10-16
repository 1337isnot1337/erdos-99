#!/usr/bin/env python3
"""Exact finite checks; the report supplies the general analytic theorem."""

if not __debug__:
    raise RuntimeError("Certificate assertions are required; run Python without -O.")

from fractions import Fraction as F
from math import prod


def regular_graphs(n):
    contacts = sorted({tuple(sorted((i, (i + 1) % n))) for i in range(n)})
    step = n // 2
    diameters = sorted({tuple(sorted((i, (i + step) % n))) for i in range(n)})
    return contacts, diameters


def squared_distance(p, q):
    return sum((a - b) ** 2 for a, b in zip(p, q))


def invert(p, pole):
    offset = tuple(a - b for a, b in zip(p, pole))
    denominator = sum(a * a for a in offset)
    assert denominator > 0
    return tuple(b + a / denominator for a, b in zip(offset, pole))


def verify_regular_incidence():
    for n in range(4, 102):
        contacts, diameters = regular_graphs(n)
        a, b = F(1, len(contacts)), F(1, len(diameters))
        contact_incidence = [sum(a for edge in contacts if i in edge) for i in range(n)]
        diameter_incidence = [sum(b for edge in diameters if i in edge) for i in range(n)]
        assert contact_incidence == diameter_incidence == [F(2, n)] * n
        # Clear the weighted-product denominators by duplicating even diameters.
        repeated_diameters = diameters * (2 if n % 2 == 0 else 1)
        factors = [F((i + 2) ** 2 + 1, i + 3) for i in range(n)]
        contact_product = prod(factors[i] * factors[j] for i, j in contacts)
        diameter_product = prod(factors[i] * factors[j] for i, j in repeated_diameters)
        assert contact_product == diameter_product
    return 98


def verify_actual_square():
    points = [(F(0), F(0)), (F(1), F(0)), (F(1), F(1)), (F(0), F(1))]
    pairs = [(i, j) for i in range(4) for j in range(i + 1, 4)]
    contacts = [(i, j) for i, j in pairs if squared_distance(points[i], points[j]) == 1]
    diameters = [(i, j) for i, j in pairs if squared_distance(points[i], points[j]) == 2]
    assert len(contacts) == 4 and len(diameters) == 2
    assert all(not all(tuple(sorted(edge)) in contacts for edge in ((i, j), (j, k), (i, k)))
               for i in range(4) for j in range(i + 1, 4) for k in range(j + 1, 4))
    poles = [(F(2), F(3)), (F(1, 2), F(1, 2)), (F(-1, 7), F(5, 13)),
             (F(1000), F(-17)), (F(1, 100), F(0))]
    for pole in poles:
        image = [invert(p, pole) for p in points]
        radii_squared = [squared_distance(p, pole) for p in points]
        new_distances = {(i, j): squared_distance(image[i], image[j]) for i, j in pairs}
        for i, j in pairs:
            assert new_distances[i, j] == squared_distance(points[i], points[j]) / (
                radii_squared[i] * radii_squared[j])
        assert max(new_distances.values()) / min(new_distances.values()) >= 2
        # Squared product invariant: two copies of each diameter, one of each contact.
        quotient = prod(new_distances[e] ** 2 for e in diameters) / prod(
            new_distances[e] for e in contacts)
        assert quotient == 16
    return len(poles), len(pairs)


def main():
    rim_count = verify_regular_incidence()
    poles, pairs = verify_actual_square()
    print(f"PASS: {rim_count} regular-rim incidence/product checks; "
          f"{poles} rational square inversions with all {pairs} pairs checked each")
    print("Scope: exact finite identities, not global optimality or Level I closure.")


if __name__ == "__main__":
    main()
