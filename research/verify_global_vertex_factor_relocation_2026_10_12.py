#!/usr/bin/env python3
"""Exact finite certificates; no global-optimality or Level I certificate.

All source labels and all unordered source pairs are retained. See the associated
report and research/README.md for the hypotheses of the general theorems.
"""

if not __debug__:
    raise SystemExit("Run without -O: this exact checker requires assertions")

from fractions import Fraction as Q
from itertools import combinations
import json


def certify_balance(n, contacts, diameters, contact_weights, diameter_weights):
    assert len(contacts) == len(contact_weights)
    assert len(diameters) == len(diameter_weights)
    assert all(x >= 0 for x in contact_weights + diameter_weights)
    assert sum(contact_weights) == sum(diameter_weights) == 1
    left = [Q(0) for _ in range(n)]
    right = [Q(0) for _ in range(n)]
    for (i, j), weight in zip(contacts, contact_weights):
        assert i != j
        left[i] += weight
        left[j] += weight
    for (i, j), weight in zip(diameters, diameter_weights):
        assert i != j
        right[i] += weight
        right[j] += weight
    assert left == right
    return {"labels": n, "weighted_vertices": sum(x > 0 for x in left)}


def check_emitted_certificate(n, contacts, diameters, certificate):
    """Replay the serialized walk and weights without rerunning the DFS."""
    cycle = certificate["state_cycle"]
    length = certificate["alternating_walk_length"]
    assert length > 0 and length % 2 == 0 and length <= 2*n
    assert len(cycle) == length+1 and cycle[0] == cycle[-1]
    assert len(set(cycle[:-1])) == length
    assert all(type(v) is int and 0 <= v < 2*n for v in cycle)
    occurrence = ({}, {})
    allowed = ({tuple(sorted(e)) for e in contacts},
               {tuple(sorted(e)) for e in diameters})
    for a, b in zip(cycle, cycle[1:]):
        kind = a % 2
        assert b % 2 == 1-kind
        edge = tuple(sorted((a//2, b//2)))
        assert edge in allowed[kind]
        occurrence[kind][edge] = occurrence[kind].get(edge, 0)+1
    decoded = []
    for kind, key in enumerate(("contact_weights", "diameter_weights")):
        weights = {}
        for row in certificate[key]:
            edge, weight = tuple(row["edge"]), Q(row["weight"])
            assert edge in allowed[kind] and edge not in weights and weight > 0
            weights[edge] = weight
        assert weights == {e: Q(count, length//2) for e, count in occurrence[kind].items()}
        decoded.append(weights)
    certify_balance(n, list(decoded[0]), list(decoded[1]),
                    list(decoded[0].values()), list(decoded[1].values()))


def alternating_certificate(n, contacts, diameters):
    """Return a short rational degree certificate, or None, by a directed DFS."""
    adjacent = [[] for _ in range(2 * n)]
    for kind, edges in enumerate((contacts, diameters)):
        for i, j in edges:
            adjacent[2 * i + kind].append(2 * j + 1 - kind)
            adjacent[2 * j + kind].append(2 * i + 1 - kind)
    visited = set()
    for start in range(2 * n):
        if start in visited:
            continue
        stack = [(start, iter(adjacent[start]))]
        active = {start: 0}
        visited.add(start)
        while stack:
            node, outgoing = stack[-1]
            successor = next(outgoing, None)
            if successor is None:
                active.pop(node)
                stack.pop()
            elif successor in active:
                cycle = [entry[0] for entry in stack[active[successor]:]]
                cycle.append(successor)
                assert (len(cycle) - 1) % 2 == 0
                assert len(cycle) - 1 <= 2 * n
                counts = ({}, {})
                m = (len(cycle) - 1) // 2
                for a, b in zip(cycle, cycle[1:]):
                    kind = a % 2
                    assert b % 2 == 1 - kind
                    edge = tuple(sorted((a // 2, b // 2)))
                    counts[kind][edge] = counts[kind].get(edge, Q(0)) + Q(1, m)
                certify_balance(n, list(counts[0]), list(counts[1]),
                                list(counts[0].values()), list(counts[1].values()))
                certificate = {
                    "alternating_walk_length": 2*m, "state_cycle": cycle,
                    "contact_weights": [{"edge": list(e), "weight": str(w)}
                                        for e, w in counts[0].items()],
                    "diameter_weights": [{"edge": list(e), "weight": str(w)}
                                         for e, w in counts[1].items()],
                }
                # Check the actual JSON representation, not just in-memory weights.
                certificate = json.loads(json.dumps(certificate))
                check_emitted_certificate(n, contacts, diameters, certificate)
                return certificate
            elif successor not in visited:
                active[successor] = len(stack)
                visited.add(successor)
                stack.append((successor, iter(adjacent[successor])))
    return None


def cycle_certificates():
    output = []
    for q in [5, 7, 43, 101]:
        k = (q - 1) // 2
        contacts = [tuple(sorted((i, (i + 1) % q))) for i in range(q)]
        diameters = [tuple(sorted((i, (i + k) % q))) for i in range(q)]
        assert len(set(contacts)) == len(set(diameters)) == q
        # Extra vertices represent arbitrary isolates; they contribute zero.
        result = certify_balance(q + 132, contacts, diameters,
                                 [Q(1, q)] * q, [Q(1, q)] * q)
        certificate = alternating_certificate(q + 132, contacts, diameters)
        assert certificate is not None
        result["uniform_certificate_weighted_vertices"] = result.pop("weighted_vertices")
        result["weighted_vertices"] = len({i for row in certificate["contact_weights"] for i in row["edge"]})
        result.update(certificate)
        output.append(result)
    contacts = [(0, 1), (1, 2), (2, 3), (0, 3)]
    diameters = [(0, 2), (1, 3)]
    result = certify_balance(4, contacts, diameters, [Q(1, 4)] * 4,
                             [Q(1, 2)] * 2)
    certificate = alternating_certificate(4, contacts, diameters)
    result["uniform_certificate_weighted_vertices"] = result.pop("weighted_vertices")
    result["weighted_vertices"] = len({i for row in certificate["contact_weights"] for i in row["edge"]})
    result.update(certificate)
    output.append(result)
    return output


def square_grid_relaxation():
    points = [(Q(x), Q(y)) for x in range(3) for y in range(3)]
    factors = [Q(9, 10) if (x + y) % 2 == 0 else Q(10, 9)
               for x, y in points]
    old = {}
    new = {}
    for i, j in combinations(range(len(points)), 2):
        old[i, j] = sum((a - b) ** 2 for a, b in zip(points[i], points[j]))
        new[i, j] = old[i, j] * factors[i] ** 2 * factors[j] ** 2
    assert len(old) == len(new) == 36
    assert min(old.values()) == min(new.values()) == 1
    assert max(old.values()) == 8
    assert max(new.values()) == Q(40000, 6561) < 8
    # The two opposite edge midpoints are linked through the center by two
    # unit distances, but their prescribed distance is 200/81 > 2.
    i, k, j = points.index((0, 1)), points.index((1, 1)), points.index((2, 1))
    assert new[min(i, k), max(i, k)] == new[min(k, j), max(k, j)] == 1
    assert new[min(i, j), max(i, j)] == Q(200, 81) ** 2 > 4
    assert alternating_certificate(9, [e for e, d in old.items() if d == 1],
                                   [e for e, d in old.items() if d == 8]) is None
    return {"pairs": len(new), "diameter_squared": str(max(new.values())),
            "triangle_inequality_excess": str(Q(200, 81) - 2)}


def rhombus_dimension_regression():
    # Original vertices: A=0, B=u, C=u+v, D=v, |u|=|v|=1,
    # u dot v=3/7. All six original squared distances are rational.
    old = {(0, 1): Q(1), (0, 2): Q(20, 7), (0, 3): Q(1),
           (1, 2): Q(1), (1, 3): Q(8, 7), (2, 3): Q(1)}
    r = Q(19, 20)
    factors = [r, 1 / r, r, 1 / r]
    new = {pair: value * factors[pair[0]] ** 2 * factors[pair[1]] ** 2
           for pair, value in old.items()}
    assert len(new) == 6
    assert min(old.values()) == min(new.values()) == 1
    assert max(new.values()) == new[0, 2] == Q(130321, 56000)
    assert max(new.values()) < max(old.values()) == Q(20, 7)
    length2, width2 = new[0, 2], new[1, 3]
    assert width2 == Q(1280000, 912247)
    height2 = 1 - (length2 + width2) / 4
    assert height2 > 0
    # 3D realization: A=(-L/2,0,0), C=(L/2,0,0),
    # B=(0,S/2,h), D=(0,-S/2,h). Hence every metric inequality holds.
    assert length2 / 4 + width2 / 4 + height2 == 1
    # Any four distinct planar vertices with the same four unit cycle edges
    # form a rhombus. Their diagonal squared lengths must sum to four.
    planar_defect = 4 - length2 - width2
    assert planar_defect > 0
    # A signed vertex potential separates contact from diameter incidence.
    z = [-1, 1, -1, 1]
    assert all(z[i] + z[j] == 0 for (i, j), d2 in old.items() if d2 == 1)
    assert z[0] + z[2] == -2
    assert alternating_certificate(4, [e for e, d in old.items() if d == 1],
                                   [(0, 2)]) is None
    return {"pairs": len(new), "diameter_squared": str(max(new.values())),
            "embedding_dimension": 3, "height_squared": str(height2),
            "planar_diagonal_defect": str(planar_defect)}


def difference(a, b):
    return a[0] - b[0], a[1] - b[1]


def complex_product(a, b):
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def norm2(a):
    return a[0] ** 2 + a[1] ** 2


def complex_divide(a, b):
    assert norm2(b) > 0
    numerator = complex_product(a, (b[0], -b[1]))
    return tuple(x / norm2(b) for x in numerator)


def normalized(points):
    a, b, c = points[:3]
    k = complex_divide(difference(b, c), difference(b, a))
    return [complex_product(k, complex_divide(difference(z, a), difference(z, c)))
            for z in points if z != c]


def mobius_cross_ratios():
    points = [(Q(x), Q(y)) for x, y in
              [(0, 0), (1, 0), (1, 1), (0, 1), (3, 0), (4, 2)]]
    a, b, c, d = (Q(2), Q(1)), (Q(1), Q(-2)), (Q(1), Q(1)), (Q(3), Q(2))
    determinant = difference(complex_product(a, d), complex_product(b, c))
    determinant2 = norm2(determinant)
    images = []
    pole_denominators = []
    for z in points:
        az, cz = complex_product(a, z), complex_product(c, z)
        numerator = (az[0] + b[0], az[1] + b[1])
        denominator = (cz[0] + d[0], cz[1] + d[1])
        pole_denominators.append(norm2(denominator))
        images.append(complex_divide(numerator, denominator))
    for i, j in combinations(range(len(points)), 2):
        old2, new2 = norm2(difference(points[i], points[j])), norm2(difference(images[i], images[j]))
        assert new2 == old2 * determinant2 / (pole_denominators[i] * pole_denominators[j])
    original_normalized = normalized(points)
    image_normalized = normalized(images)
    assert original_normalized == image_normalized
    reflected_images = [(x, -y) for x, y in images]
    assert normalized(reflected_images) == [(x, -y) for x, y in original_normalized]
    for i, j in combinations(range(len(original_normalized)), 2):
        assert norm2(difference(original_normalized[i], original_normalized[j])) == norm2(
            difference(image_normalized[i], image_normalized[j]))
    return {"labels": 6, "pairs": 15, "reflection_checked": True,
            "determinant_squared_norm": str(determinant2)}


def full_source_inversion_competitor():
    points = [(Q(x), Q(0)) for x in range(-2, 3)] + [(Q(0), Q(7, 5)), (Q(0), Q(-7, 5))]
    pole = Q(0), Q(10)
    old = {e: norm2(difference(points[e[0]], points[e[1]]))
           for e in combinations(range(len(points)), 2)}
    assert min(old.values()) == 1 and max(old.values()) == 16
    contacts = [e for e, d2 in old.items() if d2 == 1]
    assert contacts == [(0, 1), (1, 2), (2, 3), (3, 4)]
    assert [e for e, d2 in old.items() if d2 == 16] == [(0, 4)]
    images = []
    denominators = []
    for p in points:
        v = difference(p, pole)
        g = norm2(v)
        denominators.append(g)
        images.append(tuple(x / g for x in v))
    unscaled = {e: norm2(difference(images[e[0]], images[e[1]])) for e in old}
    assert all(unscaled[i, j] == old[i, j] / (denominators[i] * denominators[j]) for i, j in old)
    scale_squared = 1 / min(unscaled.values())
    assert scale_squared == 104 * 101
    final = {e: d2 * scale_squared for e, d2 in unscaled.items()}
    assert min(final.values()) == 1
    assert max(final.values()) == Q(202, 13) < 16
    assert all(final[i, j] > 1 for i, j in final if i >= 5 or j >= 5)
    return {"labels_retained": 7, "isolates_retained": 2, "pairs": 21,
            "old_diameter_squared": "16", "new_diameter_squared": str(max(final.values())),
            "squared_diameter_improvement": str(16 - max(final.values()))}


def certificate_controls():
    contacts = [(0, 1), (1, 2), (2, 3), (0, 3)]
    diameters = [(0, 2), (1, 3)]
    original = alternating_certificate(4, contacts, diameters)
    check_emitted_certificate(4, [e[::-1] for e in contacts],
                             [e[::-1] for e in diameters], original)
    rejected = 0
    for fault in ("weight", "walk", "edge"):
        candidate = json.loads(json.dumps(original))
        if fault == "weight":
            candidate["contact_weights"][0]["weight"] = "0"
        elif fault == "walk":
            candidate["state_cycle"][1] = 8
        else:
            candidate["contact_weights"][0]["edge"] = [0, 2]
        try:
            check_emitted_certificate(4, contacts, diameters, candidate)
        except AssertionError:
            rejected += 1
        else:
            raise AssertionError("corrupted serialized certificate accepted: "+fault)
    assert rejected == 3
    return rejected


def main():
    print(json.dumps({"status": "PASS", "arithmetic": "exact rational",
                      "degree_certificates": cycle_certificates(),
                      "certificate_negative_controls": certificate_controls(),
                      "square_grid": square_grid_relaxation(),
                      "rhombus": rhombus_dimension_regression(),
                      "mobius_cross_ratio_identities": mobius_cross_ratios(),
                      "full_source_inversion_competitor": full_source_inversion_competitor(),
                      "global_optimality_certified": False,
                      "level_i_resolved": False}, indent=2))


if __name__ == "__main__":
    main()
