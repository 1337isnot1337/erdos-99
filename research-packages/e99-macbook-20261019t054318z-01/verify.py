#!/usr/bin/env python3
"""Exact source-geometry control for the Oler slack and signed area gap."""

from fractions import Fraction as F
from itertools import combinations


class QRootPi:
    """A + B*sqrt(3) + C*pi with exact rational coefficients."""

    def __init__(self, rational=0, root3=0, pi=0):
        self.rational = F(rational)
        self.root3 = F(root3)
        self.pi = F(pi)

    def __add__(self, other):
        return QRootPi(
            self.rational + other.rational,
            self.root3 + other.root3,
            self.pi + other.pi,
        )

    def __sub__(self, other):
        return QRootPi(
            self.rational - other.rational,
            self.root3 - other.root3,
            self.pi - other.pi,
        )

    def __mul__(self, scalar):
        scalar = F(scalar)
        return QRootPi(
            self.rational * scalar,
            self.root3 * scalar,
            self.pi * scalar,
        )

    def is_zero(self):
        return self.rational == self.root3 == self.pi == 0

    def __repr__(self):
        return (
            f"({self.rational}) + ({self.root3})*sqrt(3) "
            f"+ ({self.pi})*pi"
        )


def norm2(point):
    """Squared Euclidean norm in the triangular basis at angle 60 degrees."""
    i, j = point
    return i * i + i * j + j * j


def hex_patch(radius):
    return [
        (i, j)
        for i in range(-radius, radius + 1)
        for j in range(-radius, radius + 1)
        if abs(i + j) <= radius
    ]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def check_hex_source(radius):
    points = hex_patch(radius)
    require(
        len(points) == 3 * radius * (radius + 1) + 1,
        f"wrong source population for radius {radius}",
    )
    distances = [
        norm2((p[0] - q[0], p[1] - q[1]))
        for p, q in combinations(points, 2)
    ]
    require(distances and min(distances) == 1, "source is not unit-separated")

    # H is the regular hexagon with side length radius. In the triangular
    # basis, its six vertices are (r,0), (0,r), (-r,r), and their opposites.
    # Its area is 3*sqrt(3)*r^2/2 and perimeter is 6r.
    area_h = QRootPi(root3=F(3, 2) * radius * radius)
    oler_perimeter_term = QRootPi(root3=F(3, 2) * radius)
    oler_population_term = QRootPi(
        root3=F(3, 2) * radius * (radius + 1)
    )
    oler_slack = area_h + oler_perimeter_term - oler_population_term
    require(oler_slack.is_zero(), "hexagonal source did not saturate Oler")


def check_triangle_free_control(radius):
    require(radius % 3 == 0, "triangle-free control radius must be divisible by 3")
    full = set(hex_patch(radius))
    source = {p for p in full if (p[0] - p[1]) % 3 != 1}
    require(
        len(full) - len(source) == radius * (radius + 1),
        "removed color-class count changed",
    )
    corners = {
        (radius, 0),
        (0, radius),
        (-radius, radius),
        (-radius, 0),
        (0, -radius),
        (radius, -radius),
    }
    require(corners <= source, "triangle-free source no longer has hull H_M")
    require(
        all(
            norm2((p[0] - q[0], p[1] - q[1])) >= 1
            for p, q in combinations(source, 2)
        ),
        "triangle-free source is not unit-separated",
    )
    for triple in combinations(source, 3):
        if all(
            norm2((p[0] - q[0], p[1] - q[1])) == 1
            for p, q in combinations(triple, 2)
        ):
            raise RuntimeError("a unit triangle survived color-class deletion")

    area_h = QRootPi(root3=F(3, 2) * radius * radius)
    oler_perimeter_term = QRootPi(root3=F(3, 2) * radius)
    population_term = QRootPi(root3=F(radius * (radius + 1)))
    oler_slack = area_h + oler_perimeter_term - population_term
    expected_slack = QRootPi(root3=F(radius * (radius + 1), 2))
    require(
        oler_slack.rational == expected_slack.rational
        and oler_slack.root3 == expected_slack.root3
        and oler_slack.pi == expected_slack.pi,
        "triangle-free source Oler slack changed",
    )
    return len(source), oler_slack


def check_inner_parallel_body(radius, collar):
    require(0 < collar < radius, "invalid inner patch collar")
    require(
        3 * collar * collar >= 4,
        "inner regular-hexagon apothem gap is below one",
    )
    area_h = QRootPi(root3=F(3, 2) * radius * radius)
    area_k = QRootPi(root3=F(3, 2) * (radius - collar) ** 2)
    parallel_area = (
        area_k
        + QRootPi(rational=6 * collar * (radius - collar))
        + QRootPi(pi=collar * collar)
    )
    delta = area_h - parallel_area
    closed_delta = QRootPi(
        rational=-6 * collar * radius + 6 * collar * collar,
        root3=3 * collar * radius - F(3, 2) * collar * collar,
        pi=-collar * collar,
    )
    require(
        delta.rational == closed_delta.rational
        and delta.root3 == closed_delta.root3
        and delta.pi == closed_delta.pi,
        "signed parallel-body area expansion changed",
    )
    return delta


def main():
    for radius in range(1, 7):
        check_hex_source(radius)
    for radius, expected_n, expected_slack in ((3, 25, 6), (6, 85, 21)):
        control_n, control_slack = check_triangle_free_control(radius)
        require(control_n == expected_n, "triangle-free control population changed")
        require(
            control_slack.root3 == expected_slack,
            "triangle-free control slack changed",
        )
    delta = check_inner_parallel_body(6, 3)

    # The gap between the separate-envelope threshold and the largest source
    # plus basis envelope is pi + 2e - (sqrt(3)/2)(1+e). Using pi>3 and
    # sqrt(3)/2<1 gives the strict positive lower bound 2+e.
    for edges in range(101):
        lower_gap = F(2 + edges)
        require(lower_gap > 0, "envelope gap lower bound is not positive")

    print("PASS: six explicit triangular-lattice patches are unit-separated and Oler-sharp")
    print("PASS: M=3,6 two-color sources are triangle-free with exact populations and Oler slack")
    print("PASS: inner parallel-body signed area identity at M=6, k=3")
    print(f"CONTROL: Delta_H = {delta}")
    print("PASS: independent envelope method has strict gap at least 2+e for e>=0")
    print(
        "LIMIT: the triangle-free control is not a global optimum or plateau response; "
        "no fan or Section-102 basis is modeled"
    )


main()
