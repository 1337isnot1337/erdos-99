#!/usr/bin/env python3
"""Exact common-host exclusions for newly certified chambers.

The companion interval-Newton verifier supplies ten further local collapsed chambers.
If all six parallel host trains end at one
outer host, their endpoints have a cyclic order.  Every alternating pair of
endpoint-disjoint internal trains must then cross, but a strict unit rhombus
crossing needs projective direction gap > pi/3.  All 720 endpoint orders are
rejected by rational interval arithmetic.
"""
from fractions import Fraction as Q
from itertools import combinations, permutations
from math import factorial
import contextlib
import importlib.util
import io
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "research" / "verify_target_c_support6_collapsed_additional_chambers_2026_09_18.py"
spec = importlib.util.spec_from_file_location("collapsed_additional", SOURCE)
assert spec is not None and spec.loader is not None
module = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(module)

EDGES = module.EDGES
RADIUS = module.R


def atan_inv_interval(n, terms):
    x = Q(1, n)
    s = Q(0)
    for k in range(terms):
        s += (-1 if k & 1 else 1) * x ** (2 * k + 1) / (2 * k + 1)
    nxt = (-1 if terms & 1 else 1) * x ** (2 * terms + 1) / (2 * terms + 1)
    return min(s, s + nxt), max(s, s + nxt)


a5 = atan_inv_interval(5, 40)
a239 = atan_inv_interval(239, 12)
PI = (16 * a5[0] - 4 * a239[1], 16 * a5[1] - 4 * a239[0])


def edge_interval(box, e):
    a = box[e]
    return a[0] - RADIUS, a[1] + RADIUS


def gap_upper(box, e, f):
    elo, ehi = edge_interval(box, e)
    flo, fhi = edge_interval(box, f)
    best = None
    for k in range(-5, 6):
        if k >= 0:
            lo, hi = elo - fhi - k * PI[1], ehi - flo - k * PI[0]
        else:
            lo, hi = elo - fhi - k * PI[0], ehi - flo - k * PI[1]
        # Choose the projective representative nearest zero.  The boxes in
        # these certificates do not straddle a nonzero half-period boundary.
        if lo <= 0 <= hi:
            upper = max(-lo, hi)
        elif hi < 0:
            upper = -lo
        else:
            upper = hi
        if best is None or upper < best:
            best = upper
    assert best is not None
    return best


def alternates(e, f, order):
    if set(e) & set(f):
        return False
    pos = {v: i for i, v in enumerate(order)}
    i, j = sorted((pos[e[0]], pos[e[1]]))
    k, ell = sorted((pos[f[0]], pos[f[1]]))
    return (i < k < j) != (i < ell < j)


for name in ("ch4", "ch5", "ch6", "ch7", "ch8", "ch9", "ch10", "ch11", "ch12", "ch13"):
    center = module.CASES[name]["center"]
    box = {e: (a, a) for e, a in zip(EDGES, center)}
    witnesses = []
    for order in permutations(range(6)):
        found = None
        for e, f in combinations(EDGES, 2):
            if not alternates(e, f, order):
                continue
            upper = gap_upper(box, e, f)
            if upper < PI[0] / 3:
                found = (e, f, upper)
                break
        assert found is not None, (name, order)
        witnesses.append(found)
    maximum = max(w[2] for w in witnesses)
    assert maximum < PI[0] / 3
    print(name, "orders_checked", factorial(6),
          "max_witness_projective_gap_upper", float(maximum),
          "pi_over_3_lower", float(PI[0] / 3),
          "strict_margin", float(PI[0] / 3 - maximum))

print("PASS: ch4, ch5, ch6, ch7, ch8, ch9, ch10, ch11, ch12, and ch13 cannot use a common all-outer host")
