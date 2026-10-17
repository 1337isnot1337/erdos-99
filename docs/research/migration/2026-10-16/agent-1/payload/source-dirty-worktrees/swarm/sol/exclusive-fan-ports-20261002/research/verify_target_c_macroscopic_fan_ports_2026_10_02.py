#!/usr/bin/env python3
"""Exact finite reductions for macroscopic fan ports; scope in research/README.md.

No Euclidean source, global minimizer, nonlinear finite move, or theorem promotion
is certified by these finite graph/cyclic/arithmetic checks.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import isqrt


def matching_number(edges, n):
    neighbors = [0] * n
    for a, b in edges:
        neighbors[a] |= 1 << b
        neighbors[b] |= 1 << a

    @lru_cache(None)
    def solve(mask):
        if not mask:
            return 0
        bit = mask & -mask
        a = bit.bit_length() - 1
        rest = mask ^ bit
        value = solve(rest)
        possible = neighbors[a] & rest
        while possible:
            b = possible & -possible
            possible ^= b
            value = max(value, 1 + solve(rest ^ b))
        return value

    return solve((1 << n) - 1)


def graph_packets():
    for cyclic in (False, True):
        sizes = (1, 2, 3, 4, 5) if not cyclic else (3, 5, 7)
        for size in sizes:
            for leaves in product(range(3), repeat=size):
                if not cyclic:
                    if size == 1 and leaves[0] < 2:
                        continue
                    if size > 1 and (leaves[0] == 0 or leaves[-1] == 0):
                        continue
                n = size + sum(leaves)
                if n > 14:
                    continue
                edges = {(i, i + 1) for i in range(size - 1)}
                if cyclic:
                    edges.add((0, size - 1))
                index = size
                for a, count in enumerate(leaves):
                    for _ in range(count):
                        edges.add((a, index))
                        index += 1
                yield cyclic, leaves, edges, n


def atan_interval(z, terms=60):
    assert 0 < z < 1 and terms % 2 == 0
    total = sum(((-1) ** j * z ** (2 * j + 1) / (2 * j + 1)
                 for j in range(terms)), F(0))
    return total, total + z ** (2 * terms + 1) / (2 * terms + 1)


def sqrt_interval(q, scale=10**12):
    lo = F(isqrt(q.numerator * scale * scale // q.denominator), scale)
    hi = lo + F(1, scale)
    assert lo * lo <= q < hi * hi
    return lo, hi


def main():
    graph_cases = run_cases = 0
    for cyclic, leaves, edges, n in graph_packets():
        nu = matching_number(edges, n)
        h = len(edges)
        carrier_count = sum(x > 0 for x in leaves)
        same_carrier_adjacencies = sum(max(0, x - 1) for x in leaves)
        assert carrier_count <= nu
        assert same_carrier_adjacencies >= h - 3 * nu
        assert n - h <= nu
        graph_cases += 1
        for bits in product((False, True), repeat=same_carrier_adjacencies):
            cursor = internal = 0
            for count in leaves:
                block = bits[cursor:cursor + max(0, count - 1)]
                cursor += len(block)
                internal += sum(block[j] and block[j + 1] for j in range(len(block) - 1))
            bad = sum(not x for x in bits)
            assert internal >= h - 4 * nu - 2 * bad
            assert n - internal <= 5 * nu + 2 * bad
            run_cases += 1

    # Full cyclic compression enumeration. 0=A, 1=deleted exclusive ports,
    # 2=remaining nonattachment vertices. g counts A-gaps hit by deleted ports.
    compression_cases = bad_edge_cases = 0
    for q in range(3, 11):
        for labels in product(range(3), repeat=q):
            attachments = [i for i in range(q) if labels[i] == 0]
            if len(attachments) < 3:
                continue
            a = len(attachments)
            deleted = labels.count(1)
            retained = [x for x in labels if x != 1]
            actual_edges = sum(labels[i] == labels[(i + 1) % q] == 0 for i in range(q))
            compressed_edges = sum(retained[i] == retained[(i + 1) % len(retained)] == 0
                                   for i in range(len(retained)))
            g = 0
            for j, left in enumerate(attachments):
                right = attachments[(j + 1) % a]
                pos = (left + 1) % q
                hit = False
                while pos != right:
                    hit |= labels[pos] == 1
                    pos = (pos + 1) % q
                g += hit
            assert compressed_edges >= 2 * a - (q - deleted)
            assert compressed_edges - actual_edges <= g
            for missing in range(q + 1):
                good = max(0, actual_edges - missing)
                assert good >= 2 * a - (q - deleted) - g - missing
                bad_edge_cases += 1
            compression_cases += 1

    # Dropping actual noncrossing: two alternating triples violate g<=c-1.
    labels = (0, 1, 0, 1, 0, 1)
    assert sum(labels[i] == labels[(i + 1) % 6] == 0 for i in range(6)) == 0
    assert 2 * 3 - (6 - 3) - (2 - 1) == 2

    # Exact canonical mu_0 lower arithmetic and the safe 0.8896 coefficient.
    a_lo, a_hi = atan_interval(F(1, 5))
    b_lo, b_hi = atan_interval(F(1, 239))
    pi_lo, pi_hi = 16 * a_lo - 4 * b_hi, 16 * a_hi - 4 * b_lo
    t = F(1, 5)
    for _ in range(2):
        t = 2 * t / (1 - t * t)
    assert (t - F(1, 239)) / (1 + t * F(1, 239)) == 1
    assert 3 < pi_lo < pi_hi < F(22, 7)
    mu = F(556, 625)
    z_lo, z_hi = sqrt_interval((1 - mu * mu) / (mu * mu))
    az_lo, _ = atan_interval(z_lo)
    # mu/3 - 6 asin(mu) + 2pi = mu/3 - pi + 6 atan(z).
    assert mu / 3 - pi_hi + 6 * az_lo > 0
    assert mu / 5 == F(1112, 6250)  # 0.17792
    assert mu + pi_lo - F(93, 25) > F(3111, 10000)

    # Exact incidence-transfer identities, including multiple bad contacts.
    transfer_cases = 0
    for n in range(1, 16):
        for delta in range(n):
            for e in range(max(0, 2 * n - delta - 8), 2 * n - delta - 1):
                r = 2 * n - delta - 2 - e
                assert r >= 0
                for surplus in range(6):
                    contacts = 2 * n + 1 + surplus - e
                    assert contacts - delta - 3 == surplus + r
                    for bad_incidence in range(contacts + 1):
                        fan_incidence = contacts - bad_incidence
                        assert fan_incidence == delta + 3 + surplus + r - bad_incidence
                        transfer_cases += 1

    # Unit-disc strip count uses h=sqrt(3)/2<1, pi>3: 12(1+h)/pi<8.
    assert F(3, 4) < 1 and 24 / pi_lo < 8
    print(f"PASS: {graph_cases} Woodall graph packets; {run_cases} good/bad fan run packets; "
          f"{compression_cases} cyclic compressions and {bad_edge_cases} missing-side counts; "
          f"{transfer_cases} pinned-incidence identities; alternating-port regression; "
          "rational mu_0/Machin bounds and 0.17792 port coefficient; strip arithmetic.")


if __name__ == "__main__":
    main()
