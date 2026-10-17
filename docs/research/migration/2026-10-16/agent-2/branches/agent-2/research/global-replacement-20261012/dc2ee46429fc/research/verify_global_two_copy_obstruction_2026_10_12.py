#!/usr/bin/env python3
"""Exact finite certificates for an infinite, nonglobal two-copy obstruction.

The associated report proves the infinite family analytically. This script
checks its Boolean obstructions and explicit full-cardinality lattice
competitors, using integers and fractions only. It certifies no optimum.
"""

from fractions import Fraction as F
from math import gcd, isqrt
import json


def atan_bounds(inverse, terms):
    total = sum((F((-1) ** j, (2 * j + 1) * inverse ** (2 * j + 1))
                 for j in range(terms)), F(0))
    next_term = F((-1) ** terms, (2 * terms + 1) * inverse ** (2 * terms + 1))
    return min(total, total + next_term), max(total, total + next_term)


def pi_bounds(q):
    """Machin's identity and alternating-series remainder, width < q^-3."""
    terms = 1
    while True:
        a_lo, a_hi = atan_bounds(5, terms)
        b_lo, b_hi = atan_bounds(239, terms)
        lower, upper = 16 * a_lo - 4 * b_hi, 16 * a_hi - 4 * b_lo
        if upper - lower < F(1, q ** 3):
            assert 3 < lower < upper < F(22, 7)
            return lower, upper
        terms += 1


def lattice_packet(radius, spacing=F(1)):
    """Sites (m+n/2, sqrt(3)n/2)*spacing inside the closed radius disk."""
    threshold = radius ** 2 / spacing ** 2
    # Q(m,n) >= (m^2+n^2)/2, so this integer box contains every site.
    bound = isqrt((2 * threshold.numerator) // threshold.denominator) + 1
    return [(m, n) for m in range(-bound, bound + 1)
            for n in range(-bound, bound + 1)
            if m * m + m * n + n * n <= threshold]


def graph_cycles(q):
    contact = [(i, (i + 1) % q) for i in range(q)]
    step = (q - 1) // 2
    assert gcd(step, q) == 1
    diameter = [(i, (i + step) % q) for i in range(q)]
    return contact, diameter


def unsat_certificate(q, strict):
    """Implication-cycle certificate using only within-copy constraints.

    Literal 2*i+b means label i selects copy b. Each strict copy forbids
    both ends of a contact selecting that copy; each noncontracting copy forbids
    both ends of a diameter selecting that copy. This includes expansion.
    Return paths from one
    literal to its negation and back, hence a checkable UNSAT certificate.
    """
    contact, diameter = graph_cycles(q)
    graph = [[] for _ in range(2 * q)]
    for bit in (0, 1):
        for i, j in contact if strict[bit] else diameter:
            graph[2 * i + bit].append(2 * j + 1 - bit)
            graph[2 * j + bit].append(2 * i + 1 - bit)

    def path(start, finish):
        queue = [start]
        parent = {start: None}
        for vertex in queue:
            for neighbor in graph[vertex]:
                if neighbor not in parent:
                    parent[neighbor] = vertex
                    queue.append(neighbor)
            if finish in parent:
                answer = [finish]
                while answer[-1] != start:
                    answer.append(parent[answer[-1]])
                answer.reverse()
                assert all(v in graph[u] for u, v in zip(answer, answer[1:]))
                return answer
        return None

    forward, backward = path(0, 1), path(1, 0)
    assert forward is not None and backward is not None, (q, strict)
    return [len(forward) - 1, len(backward) - 1]


def fixture(q):
    assert q >= 33 and q % 2 == 1
    pi_lower, pi_upper = pi_bounds(q)
    a = F(q, 2) / pi_upper
    assert a >= F(7 * q, 44) >= F(21, 4)
    interior_radius = a.numerator // a.denominator - 4
    interior_spacing = F(q + 1, q)
    interior = lattice_packet(F(interior_radius), interior_spacing)
    packet_radius = a - 1
    packet = lattice_packet(packet_radius)
    source_n = q + len(interior)
    assert len(packet) > source_n

    # Actual source D = cos(pi/(2q))/sin(pi/q). Elementary sine/cosine
    # inequalities give this rational lower bound. The packet's complete
    # pairwise diameter bound follows from its common disk, not a sample.
    source_diameter_lower = F(q) / pi_upper - pi_upper / (8 * q)
    competitor_diameter_upper = 2 * packet_radius
    assert source_diameter_lower - competitor_diameter_upper == 2 - pi_upper / (8 * q)
    assert competitor_diameter_upper < source_diameter_lower
    strict_spacing = 1 + F(1, 10 * q)
    assert strict_spacing * competitor_diameter_upper < source_diameter_lower

    # Uniform analytic population proof: using pi>3, 1/sqrt(3)<3/5,
    # and 1/a0>8/7, the lattice count gap exceeds this rational quantity.
    count_gap_lower = (212 * a - 1080) / 35
    assert count_gap_lower > 0
    modes = {}
    for strict in ((False, False), (False, True), (True, False), (True, True)):
        modes[str(strict)] = unsat_certificate(q, strict)
    return {
        "q": q,
        "source_n": source_n,
        "interior_isolates": len(interior),
        "competitor_available": len(packet),
        "competitor_retained": source_n,
        "certified_diameter_gap_lower": str(source_diameter_lower - competitor_diameter_upper),
        "strictly_separated_competitor_gap_lower": str(source_diameter_lower - strict_spacing * competitor_diameter_upper),
        "rim_anchor_height_upper": str(pi_upper / q),
        "two_copy_unsat_path_lengths": modes,
        "pi_interval_width": str(pi_upper - pi_lower),
    }


def main():
    # Check Machin's angle identity exactly, including its branch.
    tangent_twice = F(2, 5) / (1 - F(1, 25))
    tangent_four = 2 * tangent_twice / (1 - tangent_twice ** 2)
    assert (tangent_four - F(1, 239)) / (1 + tangent_four / 239) == 1
    assert 4 * (F(1, 5) - F(1, 375)) - F(1, 239) > 0
    assert F(4, 5) < F(3, 2)  # angle < 4/5 < pi/2
    assert F(3, 4) < F(49, 64)  # sqrt(3)/2 < 7/8
    assert F(1, 3) < F(9, 25)   # 1/sqrt(3) < 3/5
    for m in (5, 16, 64, 256):
        diameter, amplitude = F(m ** 2), F(m, 4)
        assert diameter / 2 - 8 * amplitude > 0
        assert diameter * amplitude - 16 * amplitude ** 2 > 0
        assert 4 * amplitude ** 2 == diameter / 4
    # Check the exact graph obstruction beyond the geometric fixtures too.
    for q in (5, 7, 9, 11, 17, 31, 33, 65, 129, 257, 1025):
        for strict in ((False, False), (False, True), (True, False), (True, True)):
            unsat_certificate(q, strict)
    print(json.dumps({
        "status": "regression; no global optimality or Level I claim",
        "arithmetic": "integer and Fraction only",
        "roundness_coefficient_fixtures": [5, 16, 64, 256],
        "fixtures": [fixture(q) for q in (33, 65, 129, 257)],
    }, indent=2))


if __name__ == "__main__":
    main()
