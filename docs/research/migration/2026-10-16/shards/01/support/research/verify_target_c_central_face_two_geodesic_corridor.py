#!/usr/bin/env python3
"""Exact Q(sqrt(147/212)) checks for the central-face corridor regression."""

from fractions import Fraction


class QS:
    """a + b*sqrt(147/212), with exact rational coefficients."""

    rad = Fraction(147, 212)

    def __init__(self, a=0, b=0):
        self.a = Fraction(a)
        self.b = Fraction(b)

    def __add__(self, other):
        other = as_qs(other)
        return QS(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return QS(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-as_qs(other))

    def __rsub__(self, other):
        return as_qs(other) - self

    def __mul__(self, other):
        other = as_qs(other)
        return QS(
            self.a * other.a + self.b * other.b * self.rad,
            self.a * other.b + self.b * other.a,
        )

    __rmul__ = __mul__

    def square(self):
        return self * self

    def sign(self):
        if self.a == 0:
            return 0 if self.b == 0 else (1 if self.b > 0 else -1)
        if self.b == 0:
            return 1 if self.a > 0 else -1
        if self.a > 0 and self.b > 0:
            return 1
        if self.a < 0 and self.b < 0:
            return -1
        lhs = self.a * self.a
        rhs = self.b * self.b * self.rad
        if lhs == rhs:
            return 0
        raw = 1 if lhs > rhs else -1
        return raw if self.a > 0 else -raw

    def __eq__(self, other):
        other = as_qs(other)
        return self.a == other.a and self.b == other.b

    def __repr__(self):
        return f"{self.a}+({self.b})*sqrt(147/212)"


def as_qs(x):
    return x if isinstance(x, QS) else QS(x, 0)


def qpoint(x, y):
    return (as_qs(x), as_qs(y))


def sub(p, q):
    return (p[0] - q[0], p[1] - q[1])


def dot(p, q):
    return p[0] * q[0] + p[1] * q[1]


def cross(p, q):
    return p[0] * q[1] - p[1] * q[0]


def norm2(p):
    return dot(p, p)


def make_points(m):
    r = QS(0, 1)
    h = Fraction(9, 10)
    s = Fraction(1, 2)
    alpha = QS(Fraction(1, 4), 0) + h * r
    beta = QS(Fraction(9, 20), 0) - Fraction(1, 2) * r
    pts = {}
    for i in range(m + 1):
        pts[f"A{i}"] = qpoint(i, 0)
        pts[f"B{i}"] = qpoint(i + s, h)
    pts["CL"] = qpoint(Fraction(1, 2) - alpha, h - beta)
    pts["CR"] = qpoint(m + alpha, beta)
    return pts, alpha, beta


def expected_edges(m):
    edges = set()

    def add(a, b):
        edges.add(tuple(sorted((a, b))))

    for i in range(m):
        add(f"A{i}", f"A{i+1}")
        add(f"B{i}", f"B{i+1}")
    for a, b in [("CL", "A0"), ("CL", "B0"),
                 ("CR", f"A{m}"), ("CR", f"B{m}")]:
        add(a, b)
    return edges


def run(m):
    pts, alpha, beta = make_points(m)
    expected = expected_edges(m)
    actual = set()
    names = list(pts)
    for i, name in enumerate(names):
        for other in names[i + 1:]:
            d2 = norm2(sub(pts[name], pts[other]))
            cmp = (d2 - 1).sign()
            if cmp < 0:
                raise AssertionError((m, name, other, d2))
            if cmp == 0:
                actual.add(tuple(sorted((name, other))))
    if actual != expected:
        raise AssertionError((m, "contacts", actual, expected))

    order = ["A0"] + [f"A{i}" for i in range(1, m + 1)]
    order += ["CR"] + [f"B{i}" for i in range(m, -1, -1)] + ["CL"]
    for i in range(len(order)):
        p = sub(pts[order[(i + 1) % len(order)]], pts[order[i]])
        q = sub(pts[order[(i + 2) % len(order)]], pts[order[(i + 1) % len(order)]])
        if cross(p, q).sign() < 0:
            raise AssertionError((m, "nonconvex turn", i, cross(p, q)))

    # The extreme pair is C_L,C_R. Their coordinate differences are
    # (m + 2*h*r, -r), so the formula is (m+2*h*r)^2+r^2.
    diameter2 = (QS(m, 0) + 2 * Fraction(9, 10) * QS(0, 1)).square() + QS(0, 1).square()
    hull_names = ["A0", f"A{m}", "CR", f"B{m}", "B0", "CL"]
    values = []
    for i, name in enumerate(hull_names):
        for other in hull_names[i + 1:]:
            values.append(norm2(sub(pts[name], pts[other])))
    if any((diameter2 - value).sign() < 0 for value in values):
        raise AssertionError((m, "diameter candidate", diameter2, values))
    if diameter2 != norm2(sub(pts["CL"], pts["CR"])):
        raise AssertionError((m, "diameter formula"))
    return len(pts), len(actual), diameter2


def main():
    for m in [2, 3, 4, 8, 16, 32]:
        n, contacts, diameter2 = run(m)
        print(f"PASS m={m} vertices={n} contacts={contacts} diameter^2={diameter2}")
    print("PASS: exact two-geodesic central-face corridor regression")
    print("Scope: explicit finite contact complex; no global-optimality claim")


if __name__ == "__main__":
    main()
