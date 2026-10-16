#!/usr/bin/env python3
"""Exact global endpoint search through finite planar placement palettes.

Arc consistency plus exhaustive branching certifies SAT/UNSAT of finite
independent-transversal systems. Negative geometric certificates use only
certainly forbidden pairs; positive certificates check all chosen pair bounds.
The fixtures concern nonglobal sources, never triangle-free global minimizers.
No floating-point calculation participates in a decision.
"""
from collections import deque
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations
from math import isqrt
from pathlib import Path
import json

from exact_trig_intervals_2026_10_12 import I, SCALE, sin_pi, cos_pi, check_exact_special_values

FIXTURE = Path(__file__).resolve().parent / "fixtures/global_palette_translation_2026_10_12"


def distance(x, y):
    return (x[0]-y[0]).square()+(x[1]-y[1]).square()


def build_system(options, diameter_squared, *, sufficient):
    """Sufficient graph proves SAT; permissive graph proves UNSAT.

    In a permissive graph an uncertain tuple remains allowed. Thus a genuine
    geometric assignment necessarily survives every encoded prohibition.
    """
    allowed = {}
    neighbours = [[] for _ in options]
    for i, j in combinations(range(len(options)), 2):
        bits = []
        for p in options[i]:
            mask = 0
            for c, q in enumerate(options[j]):
                d = distance(p, q)
                if sufficient:
                    permitted = d.lo >= SCALE and d.hi < diameter_squared.lo
                else:
                    permitted = not (d.hi < SCALE or d.lo >= diameter_squared.hi)
                if permitted:
                    mask |= 1 << c
            bits.append(mask)
        if bits == [(1 << len(options[j]))-1]*len(options[i]):
            continue
        allowed[i, j] = bits
        allowed[j, i] = [sum(1 << c for c, mask in enumerate(bits) if mask & (1 << d))
                          for d in range(len(options[j]))]
        neighbours[i].append(j)
        neighbours[j].append(i)
    return allowed, neighbours


def solve(allowed, neighbours, sizes):
    nodes = 0

    def visit(domains):
        nonlocal nodes
        nodes += 1
        queue = deque(allowed)
        while queue:
            i, j = queue.popleft()
            new = sum(1 << c for c in range(sizes[i])
                      if domains[i] & (1 << c) and allowed[i, j][c] & domains[j])
            if not new:
                return None
            if new == domains[i]:
                continue
            domains[i] = new
            queue.extend((k, i) for k in neighbours[i] if k != j)
        choices = [i for i, mask in enumerate(domains) if mask.bit_count() > 1]
        if not choices:
            return [mask.bit_length()-1 for mask in domains]
        i = min(choices, key=lambda k: (domains[k].bit_count(), -len(neighbours[k])))
        for c in range(sizes[i]):
            if domains[i] & (1 << c):
                branch = domains.copy()
                branch[i] = 1 << c
                result = visit(branch)
                if result is not None:
                    return result
        return None

    if any(size <= 0 for size in sizes):
        return None, 0
    result = visit([(1 << size)-1 for size in sizes])
    return result, nodes


def check_assignment(options, assignment, diameter_squared):
    assert len(assignment) == len(options)
    endpoint = [row[c] for row, c in zip(options, assignment)]
    norms = [distance(p, q) for p, q in combinations(endpoint, 2)]
    assert all(d.lo >= SCALE and d.hi < diameter_squared.lo for d in norms)
    return min(d.lo for d in norms), max(d.hi for d in norms), len(norms)


def read_packing(n):
    provenance = json.loads((FIXTURE/"provenance.json").read_text())
    record = next(row for row in provenance["sources"] if row["cardinality"] == n)
    raw = (FIXTURE/f"cci{n}.txt").read_bytes()
    assert sha256(raw).hexdigest() == record["sha256"]
    integer_scale = 10**30
    points = []
    for expected, line in enumerate(raw.decode().splitlines(), 1):
        label, x, y = line.split()
        assert int(label) == expected
        x, y = F(x)*integer_scale, F(y)*integer_scale
        assert x.denominator == y.denominator == 1
        points.append((int(x), int(y)))
    assert len(points) == n
    norms = [(x-u)**2+(y-v)**2 for (x, y), (u, v) in combinations(points, 2)]
    normalizer_den = 10**12
    normalizer_num = isqrt(integer_scale**2*normalizer_den**2//min(norms))+1
    factor = F(normalizer_num*1000001, integer_scale*normalizer_den*1000000)
    assert min(norms)*factor**2 > 1
    radius_sq = max(x*x+y*y for x, y in points)*factor**2
    return [(I.rational(x*factor), I.rational(y*factor)) for x, y in points], radius_sq


def options_for(source, alpha, palette):
    return [[(alpha*x+u, alpha*y+v) for u, v in palette] for x, y in source]


def verify_boolean_kernel():
    def test(sizes, restrictions):
        neighbours = [[] for _ in sizes]
        for i, j in restrictions:
            neighbours[i].append(j)
        result, _ = solve(restrictions, neighbours, sizes)
        # Independent direct enumeration is used only for these small logic fixtures.
        from itertools import product
        witnesses = [a for a in product(*(range(s) for s in sizes))
                     if all(mask[a[i]] & (1 << a[j]) for (i, j), mask in restrictions.items())]
        assert (result is None) == (not witnesses)
        if result is not None:
            assert tuple(result) in witnesses
    test([3, 3], {})
    test([3, 3], {(0, 1): [0, 0, 0], (1, 0): [0, 0, 0]})
    # Odd cycle is not 2-colourable, but is 3-colourable.
    for q in (2, 3):
        restrictions = {}
        for i, j in [(0, 1), (1, 2), (2, 0)]:
            bits = [((1 << q)-1) ^ (1 << c) for c in range(q)]
            restrictions[i, j] = bits
            restrictions[j, i] = bits
        test([q]*3, restrictions)
    print("PASS Boolean propagation/branching against independent small enumeration")


def verify_hybrid_cloud(source, diameter_squared):
    """An unlabeled 349-site cloud has packing capacity exactly 174.

    One forbidden triangle plus 173 disjoint forbidden edges partitions
    every cloud vertex. This proves the upper bound without assuming a
    label assignment or a chosen source contact cover.
    """
    cert = json.loads((FIXTURE/"hybrid_clique_matching.json").read_text())
    alpha = F(cert["alpha"])
    phase_a, phase_b = map(F, cert["phase"])
    assert alpha == F(99999999, 100000000)
    assert phase_a == phase_b == F(1, 3)
    old = [(alpha*x, alpha*y) for x, y in source]
    labels = [tuple(row) for row in cert["lattice_labels"]]
    assert len(labels) == len(set(labels)) == 174
    root3 = I.rational(3).sqrt()
    lattice = [(I.rational(i+phase_a+(j+phase_b)/2),
                root3*I.rational((j+phase_b)/2)) for i, j in labels]
    assert all((x.square()+y.square()).hi < (diameter_squared/4).lo
               for x, y in lattice)
    # Unit separation within this grain is an exact integer norm identity.
    max_norm = 0
    for (i, j), (k, ell) in combinations(labels, 2):
        a, b = i-k, j-ell
        norm = a*a+a*b+b*b
        assert norm >= 1
        max_norm = max(max_norm, norm)
    assert max_norm == 181 and I.rational(max_norm).hi < diameter_squared.lo
    i, j = cert["triangle_old"]
    k = cert["triangle_new"]
    assert (i, j) == (0, 1)  # Analytic old side length is exactly alpha < 1.
    assert distance(old[i], lattice[k]).hi < SCALE
    assert distance(old[j], lattice[k]).hi < SCALE
    used_old, used_new = {i, j}, {k}
    for a, b in cert["matching"]:
        assert a not in used_old and b not in used_new
        assert distance(old[a], lattice[b]).hi < SCALE
        used_old.add(a)
        used_new.add(b)
    assert len(cert["matching"]) == 173
    assert used_old == set(range(175)) and used_new == set(range(174))
    print("PASS unlabeled hybrid cloud: 349 sites partitioned into one forbidden triangle and 173 edges")
    print("PASS exact hybrid capacity = 174; no 175-site unit-separated subset, even without a diameter bound")


def main():
    check_exact_special_values()
    verify_boolean_kernel()
    q = 43
    radius = I.rational(1)/(2*sin_pi(F(1, q)))
    diameter_squared = I.rational(1)/(4*sin_pi(F(1, 2*q)).square())
    core = [(radius*cos_pi(F(2*i, q)), radius*sin_pi(F(2*i, q))) for i in range(q)]
    inner, inner_r2 = read_packing(132)
    assert (radius-I.rational(inner_r2).sqrt()).lo > SCALE
    assert (radius+I.rational(inner_r2).sqrt()).hi < diameter_squared.sqrt().lo
    assert all(distance(p, r).lo > SCALE and distance(p, r).hi < diameter_squared.lo
               for p, r in combinations(inner, 2))
    # Exact sine chord identities give C=H=43 on the rim. All other rim pairs
    # have step 2,...,20 and are strictly between the two bounds.
    for step in range(2, 21):
        chord = sin_pi(F(step, q)).square()/sin_pi(F(1, q)).square()
        assert chord.lo > SCALE and chord.hi < diameter_squared.lo
    source = core+inner
    assert len(source) == 175
    assert diameter_squared.lo > I.rational(F(1874262, 10000)).hi
    palette = [(I.rational(1), I.rational(0)),
               (I.rational(F(-1, 2)), I.rational(3).sqrt()/2),
               (I.rational(F(-1, 2)), -I.rational(3).sqrt()/2)]
    alpha = F(17, 20)
    core_options = options_for(core, alpha, palette)
    system, neighbours = build_system(core_options, diameter_squared, sufficient=True)
    assignment, nodes = solve(system, neighbours, [3]*q)
    assert assignment is not None
    lower, upper, pair_count = check_assignment(core_options, assignment, diameter_squared)
    assert lower > I.rational(F(101, 100)).hi
    assert upper < I.rational(185).lo
    print("PASS core palette endpoint: 43 labels,", pair_count, "pairs,", nodes, "search nodes")
    print("PASS core endpoint min squared distance > 1.01; squared diameter < 185 < old D^2")
    full_options = options_for(source, alpha, palette)
    system, neighbours = build_system(full_options, diameter_squared, sufficient=False)
    result, nodes = solve(system, neighbours, [3]*len(source))
    assert result is None
    print("PASS full-source palette UNSAT: 175 labels,", len(system)//2,
          "constrained label pairs,", nodes, "exhaustive search nodes")
    winner, _ = read_packing(175)
    norms = [distance(p, r) for p, r in combinations(winner, 2)]
    assert len(norms) == 15225
    assert all(d.lo > SCALE and d.hi < diameter_squared.lo for d in norms)
    assert max(d.hi for d in norms) < I.rational(F(1832352, 10000)).lo
    print("PASS independent full-source winner: all 15225 pairs > 1, D^2 < 183.2352")
    verify_hybrid_cloud(source, diameter_squared)
    print("SCOPE: certified failure of one finite palette on a nonglobal source; Level I remains open")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
