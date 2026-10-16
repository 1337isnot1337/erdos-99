#!/usr/bin/env python3
"""Exact finite/constant checks for the twelve-arc population competitor.

The all-real-radius averaging theorem is analytic, in the accompanying report.
This script proves its constant comparisons and checks complete finite packet
geometry against every potentially close retained lattice label. It does not
certify global packing optimality or any Level I implication. No floats are
used for predicates, square-root brackets, enumeration, or distance checks.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction as F
import json
from math import isqrt
from pathlib import Path


def need(ok, message):
    if not ok:
        raise ValueError(message)


@dataclass(frozen=True)
class Q:
    """Canonical a+b sqrt(3), with exact order and rational-compatible hash."""

    a: F = F(0)
    b: F = F(0)

    def __post_init__(self):
        object.__setattr__(self, "a", F(self.a))
        object.__setattr__(self, "b", F(self.b))

    @staticmethod
    def of(x):
        return x if isinstance(x, Q) else Q(x)

    def __add__(self, x):
        x = Q.of(x)
        return Q(self.a + x.a, self.b + x.b)

    __radd__ = __add__

    def __neg__(self):
        return Q(-self.a, -self.b)

    def __sub__(self, x):
        return self + -Q.of(x)

    def __rsub__(self, x):
        return Q.of(x) + -self

    def __mul__(self, x):
        x = Q.of(x)
        return Q(self.a*x.a + 3*self.b*x.b, self.a*x.b + self.b*x.a)

    __rmul__ = __mul__

    def __truediv__(self, x):
        x = Q.of(x)
        den = x.a*x.a - 3*x.b*x.b
        need(den != 0, "division by zero")
        return self * Q(x.a/den, -x.b/den)

    def __rtruediv__(self, x):
        return Q.of(x) / self

    def sign(self):
        a, b = self.a, self.b
        if not b:
            return (a > 0) - (a < 0)
        if not a:
            return (b > 0) - (b < 0)
        if a > 0 and b > 0:
            return 1
        if a < 0 and b < 0:
            return -1
        d = a*a - 3*b*b
        return ((d > 0) - (d < 0)) * (1 if a > 0 else -1)

    def __eq__(self, x):
        if not isinstance(x, (Q, int, F)):
            return NotImplemented
        x = Q.of(x)
        return self.a == x.a and self.b == x.b

    def __hash__(self):
        return hash(self.a) if not self.b else hash((self.a, self.b))

    def __lt__(self, x):
        return (self - x).sign() < 0

    def __le__(self, x):
        return (self - x).sign() <= 0

    def __gt__(self, x):
        return (self - x).sign() > 0

    def __ge__(self, x):
        return (self - x).sign() >= 0

    def bounds(self):
        scale = 10**40
        lo = F(isqrt(3*scale*scale), scale)
        hi = lo + F(1, scale)
        return ((self.a+self.b*lo, self.a+self.b*hi) if self.b >= 0
                else (self.a+self.b*hi, self.a+self.b*lo))

    def floor(self):
        lo, hi = self.bounds()
        n = lo.numerator // lo.denominator
        while self >= n+1:
            n += 1
        need(self >= n and self < n+1, "invalid floor")
        return n

    def ceil(self):
        return -(-self).floor()

    def approximate(self):
        lo, hi = self.bounds()
        return float((lo+hi)/2)


ROOT3 = Q(0, 1)
A = ROOT3/2
H = F(56, 65)
P = 1-A
TOP = F(98, 65)-A
B = A-TOP
K = F(9, 56)
C = F(65, 28)
S = F(256, 16385)
BETA = F(16383, 16385)
GAMMA = 6/A*(K*B*S-C*(1-BETA))


def square(x):
    return x*x


def norm2(point):
    x, y = point
    return x*x+y*y


def dist2(p, q):
    return norm2((p[0]-q[0], p[1]-q[1]))


def rotate(point, turns):
    x, y = point
    for _ in range(turns % 6):
        x, y = x/2-A*y, A*x+y/2
    return x, y


def rotate_indices(point, turns):
    x, y = point
    for _ in range(turns % 6):
        x, y = -y, x+y
    return x, y


def lattice_point(m, n, translation):
    r, s = translation
    return Q(m+r+(n+s)/2), A*(n+s)


def sqrt_bracket(value, upper, scale=2**24):
    """Exact inward-rounding inputs; bracket in rationals, not machine sqrt."""
    value = Q.of(value)
    need(value >= 0, "negative square-root input")
    lo, hi = 0, int(upper)*scale+1
    need(square(F(hi, scale)) > value, "invalid square-root upper bracket")
    while hi-lo > 1:
        mid = (lo+hi)//2
        if square(F(mid, scale)) <= value:
            lo = mid
        else:
            hi = mid
    lower, higher = F(lo, scale), F(hi, scale)
    need(square(lower) <= value and value < square(higher), "bad sqrt bracket")
    return lower, higher


def constants():
    need(S*S+BETA*BETA == 1, "Pythagorean arc identity")
    need(H*H+F(33, 65)**2 == 1, "packet contact identity")
    need(0 < P < TOP < A, "height order")
    need(A+P == 1 and TOP-P == F(33, 65), "row safety")
    need(B*BETA/S > 14, "minimum packet length")
    need(BETA*8192+A < 8192, "all-radius onset")
    need(BETA*(BETA-ROOT3*S) > F(1, 2), "cross-frame clearance")
    need(GAMMA == 3*(576*B-65)/(114695*A), "gamma identity")
    need(F(193, 100000) < GAMMA < F(194, 100000), "gamma bounds")
    need(GAMMA > 620*F(1, 320000), "strict prior coefficient comparison")
    # A_root^2=(128/a^2)k^2 b^3; A_root is positive.
    root_error_squared = 128*K*K*B*B*B/(A*A)
    need(0 < root_error_squared < F(1, 16), "square-root error < 1/4")
    constant_error = 12/A*K*B*(2*BETA*A/S+A*A/(8192*S))
    need(0 < constant_error < 60, "constant error < 60")
    # Effective D>=10^6 reduction, expressed as a polynomial in sqrt(D).
    x = F(1000)
    gap = F(193, 100000)-F(1, 600)
    need(gap*x*x-x/5-60 == F(10, 3), "effective threshold value")
    need(2*gap*x-F(1, 5) > 0, "effective threshold monotonicity")
    # kappa0^3=243*pi^3/(32000*a). pi<22/7 proves kappa0<2/3.
    need(243*F(22, 7)**3/(32000*A) < F(8, 27), "kappa0 < 2/3")
    # Sign oracle controls use rational bounds on sqrt(3), independently of sign().
    checks = 0
    for da in range(-6, 7):
        for db in range(-6, 7):
            z = Q(F(da, 7), F(db, 11))
            lo, hi = z.bounds()
            expected = 0 if da == db == 0 else (1 if lo > 0 else -1)
            need(expected == 0 or lo > 0 or hi < 0, "ambiguous sign control")
            need(z.sign() == expected, "sign oracle disagreement")
            need(z.floor() <= z < z.floor()+1, "floor control")
            checks += 1
    need(Q(2) == 2 and hash(Q(2)) == hash(F(2)), "rational hash identity")
    for u in range(-2, 3):
        for v in range(-2, 3):
            point = lattice_point(u, v, (F(0), F(0)))
            for turn in range(6):
                rotated = rotate(point, turn)
                need(norm2(rotated) == norm2(point), "rotation isometry")
                m, n = rotate_indices((u, v), turn)
                need(rotated == lattice_point(m, n, (F(0), F(0))), "index rotation")
    return {"gamma_interval": [str(t) for t in GAMMA.bounds()],
            "gamma_decimal_illustration": GAMMA.approximate(),
            "constant_error_upper_illustration": constant_error.approximate(),
            "sign_controls": checks, "rotation_identities": 150}


def construct(radius, translation):
    """Finite rounded-inward variant of the analytic packet construction."""
    deleted, inserted, packet_count = set(), [], 0
    for turn in range(6):
        tr, ts = rotate_indices(translation, -turn)
        first = (Q(BETA*radius)/A-ts).ceil()
        last = (Q(radius)/A-1-ts).floor()
        for row in range(first, last+1):
            y = A*(row+ts)
            need(BETA*radius <= y <= radius-A, "row range")
            _, u = sqrt_bracket(radius*radius-square(y+A), radius)
            v, _ = sqrt_bracket(radius*radius-square(y+TOP), radius)
            length = v-u
            need(length > 2, "rounded interval too short")
            count = ((length-2)/H).numerator//((length-2)/H).denominator+1
            for side in [-1, 1]:
                left, right = (u, v) if side == 1 else (-v, -u)
                phase = tr+(row+ts)/2
                j_min = Q(left-phase).ceil()
                j_max = Q(right-phase).floor()
                for j in range(j_min, j_max+1):
                    mr, nr = rotate_indices((j+tr, row+ts), turn)
                    m, n = mr-translation[0], nr-translation[1]
                    need(m.denominator == n.denominator == 1, "nonintegral old label")
                    label = (int(m), int(n))
                    need(norm2(lattice_point(*label, translation)) <= radius*radius,
                         "deleted label outside disk")
                    deleted.add(label)
                for i in range(count):
                    x = side*(u+1+i*H)
                    need(u+1 <= abs(x) <= v-1, "packet guards")
                    point = rotate((Q(x), y+(P if i % 2 == 0 else TOP)), turn)
                    inserted.append(point)
                packet_count += 1
    return deleted, inserted, packet_count


def validate(radius, translation, deleted, inserted):
    grid = {}
    retained_checks = new_checks = equalities = 0
    for point in inserted:
        need(norm2(point) <= radius*radius, "inserted label outside disk")
        x, y = point
        cell = x.floor(), y.floor()
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                for old in grid.get((cell[0]+dx, cell[1]+dy), []):
                    distance = dist2(point, old)
                    need(distance >= 1, "new/new collision")
                    equalities += distance == 1
                    new_checks += 1
        grid.setdefault(cell, []).append(point)
        r, s = translation
        low = (y/A-s-1/A).ceil()
        high = (y/A-s+1/A).floor()
        for n in range(low, high+1):
            off = r+(n+s)/2
            for m in range((x-off-1).ceil(), (x-off+1).floor()+1):
                if (m, n) in deleted:
                    continue
                old = lattice_point(m, n, translation)
                if norm2(old) > radius*radius:
                    continue
                need(dist2(point, old) >= 1, "new/retained collision")
                retained_checks += 1
    return {"retained_neighbor_checks": retained_checks,
            "new_neighbor_checks": new_checks, "new_unit_equalities": equalities}


def headline_ties():
    """Independent finite strictness check, including nonempty exact-D shells."""
    result = []
    for diameter in [8, 16, 32]:
        radius = F(diameter, 2)+F(1, 8)
        sites = []
        bound = diameter+2
        for m in range(-bound, bound+1):
            for n in range(-bound, bound+1):
                if m*m+m*n+n*n < radius*radius:
                    sites.append((m, n))
        removed, edges, ties = set(), 0, 0
        for i, (m, n) in enumerate(sites):
            for j in range(i):
                u, v = m-sites[j][0], n-sites[j][1]
                value = u*u+u*v+v*v
                if value >= diameter*diameter:
                    edges += 1
                    ties += value == diameter*diameter
                    removed.add(i)
        kept = [x for i, x in enumerate(sites) if i not in removed]
        maximum = max((m-u)**2+(m-u)*(n-v)+(n-v)**2
                      for i, (m, n) in enumerate(kept) for u, v in kept[:i])
        need(ties > 0, "test did not exercise exact-D ties")
        need(len(kept) >= len(sites)-edges, "edge-deletion count")
        need(maximum < diameter*diameter, "strict diameter failed")
        result.append({"D": diameter, "input": len(sites), "edges": edges,
                       "distance_D_ties": ties, "kept": len(kept),
                       "maximum_squared_diameter": maximum})
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--extended", action="store_true")
    args = parser.parse_args()
    summary = {"scope": "exact constants and finite packet geometry; analytic theorem in report",
               "constants": constants(), "headline_ties": headline_ties(), "cases": []}
    cases = [(8192, (F(0), F(0))), (16385, (F(1, 3), F(1, 5))),
             (65540, (F(0), F(0))), (65540, (F(1, 7), F(2, 5)))]
    if args.extended:
        cases.append((500000, (F(2, 7), F(3, 11))))
    for radius, translation in cases:
        deleted, inserted, packets = construct(radius, translation)
        case = {"R": radius, "translation_basis": [str(x) for x in translation],
                "packets": packets, "deleted": len(deleted), "inserted": len(inserted),
                "net_gain": len(inserted)-len(deleted)}
        case.update(validate(radius, translation, deleted, inserted))
        summary["cases"].append(case)
        print(json.dumps(case), flush=True)
    # Negative controls exercise actual geometric validators, not solver status.
    translation = (F(0), F(0))
    controls = [({(0, 0)}, [(Q(0), Q(0)), (Q(F(1, 2)), Q(0))], "new/new collision"),
                (set(), [(Q(0), Q(0))], "new/retained collision")]
    for removed, bad, expected_error in controls:
        try:
            validate(10, translation, removed, bad)
        except ValueError as error:
            need(str(error) == expected_error, "wrong negative-control rejection")
        else:
            raise ValueError("negative geometric control was accepted")
    summary["rejected_negative_controls"] = 2
    if args.output:
        args.output.write_text(json.dumps(summary, indent=2)+"\n")
    print(json.dumps({"result": "PASS", "cases": len(cases),
                      "gamma_decimal_illustration": GAMMA.approximate(),
                      "negative_controls_rejected": 2}), flush=True)


if __name__ == "__main__":
    if not __debug__:
        raise SystemExit("Refusing optimized Python; run without -O.")
    main()
