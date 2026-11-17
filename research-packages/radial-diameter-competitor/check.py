"""Exact finite checks for the radial replacement note. Run without -O."""

from fractions import Fraction as F
from itertools import combinations
from math import factorial, isqrt

if not __debug__:
    raise SystemExit("run without -O")

PI_LO, PI_HI = F(333, 106), F(355, 113)


def sine_polynomial(x, terms):
    return sum((-1) ** i * x ** (2 * i + 1) / factorial(2 * i + 1)
               for i in range(terms))


def sine_bounds(k, q):
    # sin(k*pi/q) on [0, pi/2]. At k=q/2 avoid evaluating beyond pi/2.
    if 2 * k == q:
        return F(1), F(1)
    assert 0 <= 2 * k < q and k * PI_HI / q < PI_LO / 2
    return sine_polynomial(k * PI_LO / q, 8), sine_polynomial(k * PI_HI / q, 9)


def check_rim(q):
    # Work in squared distances divided by R^2, so unit length squared is u.
    s_lo, s_hi = sine_bounds(1, q)
    u_lo, u_hi = 4 * s_lo ** 2, 4 * s_hi ** 2
    diameter_lo = 4 * sine_bounds(q // 2, q)[0] ** 2
    offsets = [0] + [1 if i % 2 else 3 for i in range(1, q)]
    classes = set()
    for i, j in combinations(range(q), 2):
        a, b = sorted((offsets[i], offsets[j]))
        classes.add((a, b, min(j - i, q + i - j)))
    for a, b, k in classes:
        chord_lo, chord_hi = sine_bounds(k, q)
        lower = (a-b)**2 * u_lo**2 + 4*(1-a*u_hi)*(1-b*u_hi)*chord_lo**2
        upper = (a-b)**2 * u_hi**2 + 4*(1-a*u_lo)*(1-b*u_lo)*chord_hi**2
        if k == 1:
            # Keep the equality at (0,1) exact; independent intervals overlap.
            assert a != b and (a-b)**2 >= a+b and a*b >= 0
        else:
            assert lower > u_hi
        assert upper < diameter_lo
    return q * (q - 1) // 2


def squared(p, q):
    return sum((x-y)**2 for x, y in zip(p, q))


def check_occupied_source():
    R = 1_000_000
    D = 2*R
    lo = F(-499, 1000)
    inner = R-1-F(1, 64*D)
    points = [(R, lo), (-R, lo), (inner, lo), (inner, lo+1), (inner-1, lo+1),
              (0, 3), (0, -3)]
    origin = (0, 0)
    eps = F(1, 2)
    rad2 = [squared(p, origin) for p in points]
    bins = [isqrt(int(v*(32*D)**2)) for v in rad2]
    assert bins[2] == bins[3] and rad2[2] < rad2[3]
    order = sorted(range(len(points)), key=lambda i: (-bins[i], i))
    depth = [0]*len(points)
    depth[0] = 1
    for pos, i in enumerate(order):
        if depth[i]:
            for j in order[pos+1:]:
                if squared(points[i], points[j]) <= (1+eps)**2:
                    depth[j] = max(depth[j], depth[i]+1)
    assert depth == [1, 0, 2, 3, 4, 0, 0]
    assert max(depth) <= isqrt(int(D*eps))//64
    r = F(D, 16)
    new = []
    for p, k in zip(points, depth):
        scale = 1-k*(k+1)/r**2
        new.append(tuple(scale*x for x in p))
    old_d2 = [squared(p,q) for p,q in combinations(points,2)]
    new_d2 = [squared(p,q) for p,q in combinations(new,2)]
    assert min(old_d2) == 1 and max(old_d2) == D**2
    assert min(new_d2) > 1 and max(new_d2) < D**2
    return len(new_d2)


def check_refilled_cut():
    seeds = {(5, -1), (5, 1)}
    cut = {(3, 0)}
    fixed = {(-5, 0), (-4, 0), (0, -3), (0, 3)}
    moved = {(x-2, y) for x, y in seeds}
    for x in moved:
        assert squared(x, (3, 0)) == 1
        assert all(squared(x, y) > 1 for y in fixed | seeds)
    old = fixed | seeds | cut
    enlarged = moved | fixed | seeds
    trimmed = enlarged - {(-5, 0)}
    before = [squared(p, q) for p, q in combinations(old, 2)]
    after = [squared(p, q) for p, q in combinations(trimmed, 2)]
    assert len(trimmed) == len(old) and min(before) == 1 < min(after)
    assert max(after) < max(before)
    return len(after)


if __name__ == "__main__":
    for n in (33, 65, 129, 257):
        print(f"q={n}, all {check_rim(n)} rim pairs covered")
    print(f"Occupied-source fixture: all {check_occupied_source()} pairs passed")
    print(f"Refilled-cut fixture: all {check_refilled_cut()} trimmed pairs passed")
