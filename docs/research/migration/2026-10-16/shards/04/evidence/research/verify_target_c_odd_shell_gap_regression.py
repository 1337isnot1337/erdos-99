#!/usr/bin/env python3
"""Exact finite certificates for the odd-shell gap regression.

Report: docs/reports/target_c_odd_shell_gap_regression_2026-10-01.md.
For q=4s+1, encode the regular polygon's diameter graph by maximal cyclic
distance, and vertical-cut layers by right-half-plane x-coordinate order.
Check full support, one empty row, one-sided gaps, a full-rank gap basis,
common-star full-span witnesses, and internally/across-bundle disjoint CROSS
pairs. On selected q, work exactly in Q(zeta_q), with y multiplied by i,
to check transverse equilibrium, the positive-stress algebraic identity,
affine stress kernel, and mixed rigidity rank.

No floats are used. Trigonometric monotonicity/sign and PSD inequalities are
proved in the report, not decided numerically here. The chosen vertical cuts
are NOT actual exact-phase unit-contact train cuts. This certifies neither
global optimality nor a finite contact-preserving move.
"""

from __future__ import annotations

import argparse
from fractions import Fraction


def shell(s: int):
    q = 4 * s + 1
    step = 2 * s
    edges = sorted({tuple(sorted((j, (j + step) % q))) for j in range(q)})

    def signed(j: int) -> int:
        return j if j <= 2 * s else j - q

    def layer(j: int) -> int:
        a = abs(signed(j))
        if a == 0:
            return s + 1
        return s + 1 - a if a <= s else 0

    return q, step, edges, signed, layer


def discrete_certificate(s: int) -> tuple[int, int]:
    q, step, edges, signed, layer = shell(s)
    assert len(edges) == q
    degrees = [0] * q
    for a, b in edges:
        assert min((a - b) % q, (b - a) % q) == step
        degrees[a] += 1
        degrees[b] += 1
    assert set(degrees) == {2}
    # The step is coprime to q; the complete actual diameter graph is one cycle.
    assert len({(j * step) % q for j in range(q)}) == q

    empty = [(a, b) for a, b in edges if layer(a) == layer(b)]
    assert empty == [(s, q - s)]
    assert layer(s) == 1
    branch_counts = [0] * (s + 2)
    full_span = []
    supports = []
    for a, b in edges:
        la, lb = sorted((layer(a), layer(b)))
        if la == lb:
            continue
        assert la == 0
        branch_counts[lb] += 1
        supports.append((a, b, lb))
        if lb == s + 1:
            full_span.append((a, b))
    assert branch_counts[1] == 2
    assert branch_counts[s + 1] == 2
    assert all(branch_counts[i] == 4 for i in range(2, s + 1))
    assert full_span == [(0, 2 * s), (0, 2 * s + 1)]
    # Reflection exchanges the two signs and preserves support.
    reflected = {(min((-a) % q, (-b) % q),
                  max((-a) % q, (-b) % q), g) for a, b, g in supports}
    assert reflected == set(supports)
    for i in range(1, s + 1):
        middle = {j for e in edges for j in e if layer(j) == i}
        assert len(middle) == 2
        assert {signed(j) > 0 for j in middle} == {True, False}
        other = {layer(b if layer(a) == i else a)
                 for a, b in edges if (layer(a) == i) != (layer(b) == i)}
        assert other == {0}

    # Prefix indicators [1,g], g=1,...,s+1, form a triangular determinant-one
    # basis; every one is the support of an actual nonempty diameter row.
    assert {g for _, _, g in supports} == set(range(1, s + 2))
    common = set(range(1, s + 2))
    for _, _, g in supports:
        common.intersection_update(range(1, g + 1))
    assert common == {1}

    chosen = []
    used = set()
    for j in range(1, s):
        pair = [tuple(sorted((j, (j - step) % q))),
                tuple(sorted(((-j) % q, (-j + step) % q)))]
        assert all(e in edges for e in pair)
        vertices = set(pair[0]) | set(pair[1])
        assert len(vertices) == 4
        assert not vertices & used
        used |= vertices
        chosen.extend(pair)

    def crosses(e, f):
        a, b = e
        c, d = f
        return (a < c < b) != (a < d < b)

    for i, e in enumerate(chosen):
        for f in chosen[i + 1:]:
            assert not set(e) & set(f)
            assert crosses(e, f)
    return q, len(chosen) // 2


def algebraic_certificate(s: int) -> dict[str, int]:
    from sympy import Poly, QQ, Symbol, cyclotomic_poly
    from sympy.polys.matrices import DomainMatrix

    q, step, edges, signed, layer = shell(s)
    z = Symbol("z")
    field = QQ.alg_field_from_poly(Poly(cyclotomic_poly(q, z), z), alias="zeta")
    zeta = field.unit
    assert zeta ** q == field.one
    half = field.convert(Fraction(1, 2))
    # Y=i*y. Multiplication of one coordinate column family by i preserves
    # the rank of the actual real rigidity matrix after complexification.
    x = [(zeta ** j + zeta ** ((-j) % q)) * half for j in range(q)]
    yy = [(zeta ** j - zeta ** ((-j) % q)) * half for j in range(q)]
    contacts = sorted({tuple(sorted((j, (j + 1) % q))) for j in range(q)})
    alpha = ((2 - zeta ** step - zeta ** ((-step) % q)) /
             (2 - zeta - zeta ** (q - 1)))
    assert alpha * (2 - zeta - zeta ** (q - 1)) == (
        2 - zeta ** step - zeta ** ((-step) % q))
    omega = [[field.zero for _ in range(q)] for _ in range(q)]
    rigidity = []
    for weight, rows in ((alpha, contacts), (-field.one, edges)):
        for a, b in rows:
            omega[a][a] += weight
            omega[b][b] += weight
            omega[a][b] -= weight
            omega[b][a] -= weight
            row = [field.zero] * (2 * q)
            for coord, vals in enumerate((x, yy)):
                row[2 * a + coord] = vals[a] - vals[b]
                row[2 * b + coord] = vals[b] - vals[a]
            rigidity.append(row)
    for vals in ([field.one] * q, x, yy):
        assert all(sum((omega[i][j] * vals[j] for j in range(q)), field.zero)
                   == field.zero for i in range(q))
    stress_rank = DomainMatrix(omega, (q, q), field).rank()
    mixed_rank = DomainMatrix(rigidity, (2 * q, 2 * q), field).rank()
    assert stress_rank == q - 3
    assert mixed_rank == 2 * q - 3

    matrix = []
    transverse_divergence = [field.zero] * (s + 2)
    for a, b in edges:
        if layer(a) > layer(b):
            a, b = b, a
        p, g = layer(a), layer(b)
        if p == g:
            matrix.append([field.zero] * (s + 1))
            continue
        coeff = yy[b] - yy[a]
        assert coeff != field.zero
        transverse_divergence[p] += coeff
        transverse_divergence[g] -= coeff
        matrix.append([coeff if p <= j < g else field.zero
                       for j in range(s + 1)])
    assert all(c == field.zero for c in transverse_divergence)
    gap_rank = DomainMatrix(matrix, (q, s + 1), field).rank()
    assert gap_rank == s + 1
    return {"q": q, "stress_rank": stress_rank,
            "mixed_rank": mixed_rank, "gap_rank": gap_rank}


def two_shore_certificate(t: int) -> int:
    """Discrete part of the analytic two-axis crosscut rectangle.

    q=12t+1; second axis goes through vertex 2t+1. First floor(q/100)
    crosscuts on each shore have positive projections less than R/8. The
    report proves that every geometric crosscut pair intersects in F.
    """
    s = 3 * t
    q, _, edges, _, full_layer = shell(s)
    count = q // 100
    assert count >= 1
    axis = 2 * t + 1
    # phi in (pi/3,pi/2), with phi-pi/3=5pi/(3q), exactly.
    assert 6 * axis - q == 5
    assert 4 * axis < q
    labels = [[min(full_layer((j - offset) % q), count) for j in range(q)]
              for offset in (0, axis)]
    for shore in labels:
        supports = set()
        for a, b in edges:
            p, g = sorted((shore[a], shore[b]))
            if p != g:
                assert p == 0
                supports.add(g)
        assert supports == set(range(1, count + 1))
        assert min(supports) == 1  # common pivot also survives on both shores
        for gap in range(1, count):
            neighbors = {shore[b if shore[a] == gap else a]
                         for a, b in edges if (shore[a] == gap) != (shore[b] == gap)}
            assert neighbors == {0}
    # A diameter row switches at each internal endpoint label. This also
    # checks the joint per-edge two-shore budget, without assuming it.
    for a, b in edges:
        switches = sum(int(0 < shore[a] < count) + int(0 < shore[b] < count)
                       for shore in labels)
        assert switches <= 2
    return count


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-s", type=int, default=64)
    parser.add_argument("--algebraic-s", type=int, nargs="+", default=[1, 2, 3, 4, 5])
    args = parser.parse_args()
    assert args.max_s >= 1 and all(s >= 1 for s in args.algebraic_s)
    total_q = total_bundles = 0
    for s in range(1, args.max_s + 1):
        q, bundles = discrete_certificate(s)
        total_q += q
        total_bundles += bundles
    print(f"PASS integer certificates: {args.max_s} shells, "
          f"{total_q} vertices, {total_bundles} disjoint CROSS bundles")
    for s in args.algebraic_s:
        row = algebraic_certificate(s)
        print("PASS cyclotomic certificate: " + ", ".join(f"{k}={v}" for k, v in row.items()))
    counts = [two_shore_certificate(t) for t in range(9, 65)]
    print(f"PASS two-shore certificates: {len(counts)} shells; "
          "full prefix rank, one-sided internal gaps, joint switch budget <=2")
    print("Omitted: actual exact-phase unit-train cuts, quadratic core, "
          "global optimality, finite release.")


if __name__ == "__main__":
    main()
