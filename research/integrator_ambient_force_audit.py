#!/usr/bin/env python3
"""Sanity checks for the September 9 ambient-force integrator reports.

Tests the finite midpoint/area/perimeter bounds for diameter endpoints in an
enclosing disk, the exact exterior-cap Oler bookkeeping, and the relaxed cavity
optimization. Geometry/root evaluation uses floating point; the coarse derivative
sign check uses exact rational arithmetic. No global optimality, KKT realizability,
or ZF hypothesis is encoded. A pass is finite consistency evidence, not a proof
of the general theorems or of Erdős #99. Proofs are in docs/reports/integrator_*.

Run: python3 research/integrator_ambient_force_audit.py
"""

import math
import random
from fractions import Fraction as Q


def cross(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points
    lower, upper = [], []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 1e-12:
            lower.pop()
        lower.append(p)
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 1e-12:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


def area(poly):
    return abs(sum(p[0] * q[1] - p[1] * q[0]
                   for p, q in zip(poly, poly[1:] + poly[:1]))) / 2


def perimeter(poly):
    return sum(math.dist(p, q) for p, q in zip(poly, poly[1:] + poly[:1]))


def inside(point, poly):
    return all(cross(p, q, point) >= -1e-9
               for p, q in zip(poly, poly[1:] + poly[:1]))


def close(a, b, scale=1.0):
    assert abs(a - b) <= 1e-8 * max(1.0, abs(a), abs(b), scale), (a, b)


def geometry_check(points):
    pairs = [(math.dist(p, q), i, j) for i, p in enumerate(points)
             for j, q in enumerate(points[:i])]
    diameter = max(item[0] for item in pairs)
    edges = [(i, j) for length, i, j in pairs if abs(length - diameter) < 1e-9]
    radius = max(math.hypot(*p) for p in points)
    mu = math.sqrt(max(0.0, radius * radius - diameter * diameter / 4))
    endpoint_ids = {i for edge in edges for i in edge}
    force = hull([points[i] for i in endpoint_ids])
    centered, directions = [], []
    for i, j in edges:
        p, q = points[i], points[j]
        midpoint = ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2)
        assert math.hypot(*midpoint) <= mu + 1e-7
        vector = ((p[0] - q[0]) / 2, (p[1] - q[1]) / 2)
        centered.extend([vector, (-vector[0], -vector[1])])
        directions.append(math.atan2(vector[1], vector[0]) % math.pi)
    directions.sort()
    gaps = [directions[(i + 1) % len(directions)] - directions[i]
            + (math.pi if i == len(directions) - 1 else 0)
            for i in range(len(directions))]
    model = hull(centered)
    close(perimeter(model), 2 * diameter * sum(math.sin(g / 2) for g in gaps))
    close(area(model), diameter * diameter / 4 * sum(math.sin(g) for g in gaps))
    assert abs(perimeter(force) - perimeter(model)) <= 2 * math.pi * mu + 1e-7
    assert abs(area(force) - area(model)) <= math.pi * diameter * mu + math.pi * mu**2 + 1e-7
    assert area(model) >= diameter * perimeter(model) - 3 * math.pi * diameter**2 / 4 - 1e-7


def regular_polygon(n):
    radius = 1 / (2 * math.sin(math.pi / n))
    return [(radius * math.cos(2 * math.pi * i / n),
             radius * math.sin(2 * math.pi * i / n)) for i in range(n)]


def cap_check(boundary, selected):
    source = boundary + [(0.0, 0.0)]
    force = hull([boundary[i] for i in selected])
    external = [p for p in source if not inside(p, force)]
    caps, common = [], 0.0
    for pos, i in enumerate(selected):
        j = selected[(pos + 1) % len(selected)]
        arc = [boundary[i]]
        cur = (i + 1) % len(boundary)
        while cur != j:
            arc.append(boundary[cur])
            cur = (cur + 1) % len(boundary)
        arc.append(boundary[j])
        if len(arc) == 2:
            common += math.dist(*arc)
        else:
            caps.append(hull(arc))
    counts = [sum(inside(p, cap) for p in external) for cap in caps]
    assert sum(counts) == len(external)
    close(sum(area(cap) for cap in caps), area(boundary) - area(force))
    close(sum(perimeter(cap) for cap in caps), perimeter(boundary) + perimeter(force) - 2 * common)
    a0 = math.sqrt(3) / 2
    slack_k = area(boundary) / a0 + perimeter(boundary) / 2 + 1 - len(source)
    slack_f = area(force) / a0 + perimeter(force) / 2 + 1 - (len(source) - len(external))
    slacks = [area(cap) / a0 + perimeter(cap) / 2 - 1 - count
              for cap, count in zip(caps, counts)]
    assert min([slack_k, slack_f] + slacks) >= -1e-7
    close(slack_f + sum(slacks), slack_k + perimeter(force) - common - len(caps))
    upper = (area(boundary) - area(force)) / a0 + (perimeter(boundary) + perimeter(force)) / 2 - common - len(caps)
    assert len(external) <= upper + 1e-7


def bisect(function, low, high):
    assert function(low) < 0 < function(high)
    for _ in range(80):
        mid = (low + high) / 2
        if function(mid) > 0:
            high = mid
        else:
            low = mid
    return (low + high) / 2


def scalar_check(rng):
    pi = math.pi
    rho = bisect(lambda r: r - math.cos(r), 0, 1)
    y_star = bisect(lambda y: 7 * y - math.sin(y) - 3 * pi, 1.48, 1.5)
    f = lambda y: (y + math.sin(y)) / 4
    lambda_star = bisect(lambda x: pi * x*x / 4 + (x + y_star)**2 / (4*pi) - f(y_star), 0.5, 1)
    # Exact rational check of the deliberately coarse derivative margin.
    cos_upper = 1 - Q(7, 5)**2 / 2 + Q(7, 5)**4 / 24
    assert Q(19, 10) / (2 * Q(22, 7)) > (1 + cos_upper) / 4
    max_slack = -math.inf
    for _ in range(20000):
        y = rng.uniform(2 * rho, pi)
        p = rng.uniform(y, min(2 * y, pi))
        slack = pi * lambda_star**2 / 4 + (lambda_star + p - y)**2 / (4*pi) - max(f(y), p - 3*pi/4)
        assert slack <= 1e-10, (y, p, slack)
        max_slack = max(max_slack, slack)
    close(pi * lambda_star**2 / 4 + (lambda_star + y_star)**2 / (4*pi), f(y_star))
    a_int = f(2 * rho)
    print(f"rho={rho:.12f}; integrated area floor={a_int:.12f}")
    print(f"y_star={y_star:.12f}; lambda_star={lambda_star:.12f}")
    print(f"external fraction ceiling={1-4*a_int/pi:.12f}")
    print(f"20000 relaxed scalar samples passed; largest sampled slack={max_slack:.6g}")


def main():
    rng = random.Random(20260909)
    geom_count = cap_count = 0
    for n in range(7, 52):
        polygon = regular_polygon(n)
        geometry_check(polygon)
        geom_count += 1
        for _ in range(15):
            selected = sorted(rng.sample(range(n), rng.randint(3, n)))
            cap_check(polygon, selected)
            cap_count += 1
    # The finite, noncentrally-symmetric equilateral matching regression from MB.
    for a in [math.pi / 5, math.pi / 4, 2 * math.pi / 5]:
        x = y = 0.0
        polygon = []
        for direction in [0, a, 2*math.pi/3, 2*math.pi/3+a, 4*math.pi/3, 4*math.pi/3+a]:
            polygon.append((x, y))
            x += math.cos(direction)
            y += math.sin(direction)
        center = tuple(sum(p[i] for p in polygon) / 6 for i in range(2))
        polygon = [(p[0]-center[0], p[1]-center[1]) for p in polygon]
        geometry_check(polygon)
        geom_count += 1
    print(f"{geom_count} enclosing-disk geometry cases; {cap_count} cap partitions passed")
    scalar_check(rng)
    print("Finite sanity checks only: no global-optimality or post-ZF certificate.")


if __name__ == "__main__":
    main()
