#!/usr/bin/env python3
"""Certify a dense triangle-free local trap and a global source replacement.

The old source is a regular unit 43-gon with 132 strict interior isolates.
All imported decimal coordinates are treated as exact rational input.
Source minimality is refuted, not asserted. The analytic radius-multiset
obstruction and core stress/rank statements are in the associated report.
"""

from decimal import Decimal, localcontext
from fractions import Fraction as Q
from hashlib import sha256
from itertools import combinations
from math import isqrt
from pathlib import Path
import json

from exact_trig_intervals_2026_10_11 import I, PI, SCALE, sin_pi, cos_pi, check_exact_special_values


FIXTURE = Path(__file__).resolve().parent / "fixtures/global_odd_shell_reassignment_2026_10_11"
INPUT_SCALE = 10**30


def decimal_interval(value, digits=12):
    with localcontext() as ctx:
        ctx.prec = 80
        lo, hi = Decimal(value.lo) / Decimal(SCALE), Decimal(value.hi) / Decimal(SCALE)
        # Display only; every decision above/below uses integers.
        return f"[{lo:.{digits}f}, {hi:.{digits}f}] (display rounded)"


def read_packing(n):
    provenance = json.loads((FIXTURE / "provenance.json").read_text())
    record = next(row for row in provenance["sources"] if row["cardinality"] == n)
    raw = (FIXTURE / f"cci{n}.txt").read_bytes()
    assert sha256(raw).hexdigest() == record["sha256"]
    points = []
    for expected, line in enumerate(raw.decode().splitlines(), 1):
        label, x, y = line.split()
        assert int(label) == expected
        x, y = Q(x) * INPUT_SCALE, Q(y) * INPUT_SCALE
        assert x.denominator == y.denominator == 1
        points.append((int(x), int(y)))
    assert len(points) == n
    pair_norms = [(x-u)**2 + (y-v)**2 for (x, y), (u, v) in combinations(points, 2)]
    minimum, maximum = min(pair_norms), max(pair_norms)
    scale_den = 10**12
    target = INPUT_SCALE**2 * scale_den**2
    scale_num = isqrt(target // minimum) + 1
    assert scale_num**2 * minimum > target
    # An explicit strict inflation prevents any use of approximate equality.
    num, den = scale_num * 1000001, INPUT_SCALE * scale_den * 1000000
    scaled = [(x * num, y * num) for x, y in points]
    assert minimum * num**2 > den**2
    pair_min = Q(minimum * num**2, den**2)
    pair_max = Q(maximum * num**2, den**2)
    radius_sq = Q(max(x*x+y*y for x, y in scaled), den**2)
    return scaled, den, pair_min, pair_max, radius_sq, Q(num, den // INPUT_SCALE)


def main():
    check_exact_special_values()
    q, n = 43, 175
    inner, inner_den, inner_min, inner_max, inner_r2, scale_old = read_packing(132)
    winner, winner_den, winner_min, winner_max, winner_r2, scale_new = read_packing(n)
    s = sin_pi(Q(1, q))
    radius = I.rational(1) / (2 * s)
    diameter_sq = I.rational(1) / (4 * sin_pi(Q(1, 2*q)).square())
    inner_radius = I.rational(inner_r2).sqrt()
    assert (radius - inner_radius).lo > SCALE
    assert (radius + inner_radius).hi < diameter_sq.sqrt().lo
    assert I.rational(inner_max).hi < diameter_sq.lo
    core = [(radius * cos_pi(Q(2*i, q)), radius * sin_pi(Q(2*i, q))) for i in range(q)]
    core_contacts = core_diameters = strict_core_pairs = 0
    chord_sq = {step: sin_pi(Q(step, q)).square() / s.square()
                for step in range(2, (q-1)//2)}
    for i, j in combinations(range(q), 2):
        step = min(j-i, q-(j-i))
        if step == 1:
            # Exact unit identity is analytic, not inferred from an interval.
            core_contacts += 1
        elif step == (q-1)//2:
            # Exact diameter identity is analytic, not inferred from an interval.
            core_diameters += 1
        else:
            assert chord_sq[step].lo > SCALE
            assert chord_sq[step].hi < diameter_sq.lo
            strict_core_pairs += 1
    assert core_contacts == core_diameters == q
    for _, _, bound in [(inner, inner_den, inner_min), (winner, winner_den, winner_min)]:
        assert bound > 1
    cross_count = 0
    for x, y in core:
        for u, v in inner:
            distance_sq = (x-I.rational(Q(u, inner_den))).square() + (y-I.rational(Q(v, inner_den))).square()
            assert distance_sq.lo > SCALE
            assert distance_sq.hi < diameter_sq.lo
            cross_count += 1
    assert cross_count == q * 132
    total_pairs = q*(q-1)//2 + cross_count + 132*131//2
    assert total_pairs == n*(n-1)//2
    # Certify the full-core stress's nontrivial Fourier eigenvalues strictly.
    m = (q-1)//2
    eigen_lower = None
    for k in range(2, q-1):
        value = 4 * (diameter_sq * sin_pi(Q(k, q)).square()
                     - sin_pi(Q(m*k, q)).square()) / q
        assert value.lo > 0
        eigen_lower = value.lo if eigen_lower is None else min(eigen_lower, value.lo)
    # The null modes 0,+1,-1 and equilibrium are exact analytic identities.
    assert I.rational(winner_max).hi < diameter_sq.lo
    population_excess = I.rational(n-1) - PI * diameter_sq / (2 * I.rational(3).sqrt())
    assert population_excess.lo > 0
    assert (population_excess.square() * population_excess).lo > (I.rational(Q(7, 10)**3) * diameter_sq).hi
    # Canonical kappa0^3=243*pi^3/(32000*a0); elementary envelopes give kappa0<0.7.
    assert Q(243) * Q(22, 7)**3 / (32000 * Q(17, 20)) < Q(7, 10)**3
    diameter_gain = diameter_sq - I.rational(winner_max)
    assert diameter_gain.lo > 0
    assert diameter_sq.lo > I.rational(Q(1874262, 10000)).hi
    assert winner_max < Q(1832352, 10000)
    assert diameter_gain.lo > I.rational(Q(41910, 10000)).hi
    assert population_excess.lo > I.rational(Q(40232, 10000)).hi
    assert population_excess.hi < I.rational(Q(40233, 10000)).lo
    print(f"PASS old source: labels={n}, all {total_pairs} full-source pairs, C={q}, H={q}, isolates=132")
    print("PASS core PSD: null modes analytically 0,+1,-1; all other Fourier eigenvalues positive")
    print("PASS population: n-1-Delta*D^2 > (7/10)*D^(2/3), with 7/10>kappa0")
    print(f"PASS winner: all {n*(n-1)//2} rational pairs strictly above one; diameter squared strictly smaller")
    print("old D^2:", decimal_interval(diameter_sq))
    print("winner D^2:", decimal_interval(I.rational(winner_max)))
    print("strict squared-diameter gain:", decimal_interval(diameter_gain))
    print("population excess:", decimal_interval(population_excess))
    print("exact coordinate scales:", str(scale_old), str(scale_new))
    print("Scope: finite nonglobal regression and analytic radial barrier; no Level I disproof")


if __name__ == "__main__":
    main()
