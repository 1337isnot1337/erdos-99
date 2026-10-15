#!/usr/bin/env python3
"""Reproduce the strict q=13 cyclic-S1 shell regression.

This is a regression/probe, not a proof of the source-level Target C statement.
It reconstructs the palindromic RSQ shell, checks its active contact/diameter
sets, finds a strictly positive equilibrium stress by linear programming, and
checks the scalar stress spectrum.

Requires numpy, scipy, sympy.
"""

from __future__ import annotations

import cmath
import math

import numpy as np
import sympy as sp
from scipy.optimize import brentq, linprog


Q = 13
M = 11
BITS = (-1, 1, -1, -1, 1, 1, 1, -1, -1, 1, -1)
EPS = (1, -1) + BITS

EXPECTED_CONTACTS = [
    (0, 1), (0, 12), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6),
    (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12),
]
EXPECTED_DIAMETERS = [
    (0, 6), (0, 7), (1, 7), (1, 8), (1, 9), (2, 9),
    (3, 9), (4, 9), (4, 10), (4, 11), (5, 11), (5, 12),
]
EXPECTED_SIDE_ORDER = [3, 6, 7, 8, 11, 1, 2, 4, 5, 9, 10, 12, 0]


def p13_float(t: float) -> float:
    return (
        t**10 - 2*t**9 - 8*t**8 + 18*t**7 + 17*t**6 - 52*t**5
        + t**4 + 51*t**3 - 22*t**2 - 13*t + 11
    )


def p1_boundary_delta() -> float:
    zero = math.pi / Q

    def equation(delta: float) -> float:
        return M * delta + 2 * math.asin(2 * math.sin(delta / 2)) - math.pi

    return brentq(equation, 1.0e-12, zero)


def reconstruct() -> tuple[np.ndarray, float, float, float, list[int]]:
    # The physical algebraic root is isolated well inside this interval.
    trace = brentq(p13_float, 1.94199, 1.941995, xtol=1.0e-14)
    delta = math.acos(trace / 2)
    x = delta / 2
    diameter = 1 / (2 * math.sin(x))
    gap = math.pi - M * delta
    eta = math.asin(diameter * math.sin(gap / 2))
    tau = math.pi - 2 * eta

    assert p1_boundary_delta() < delta < math.pi / Q
    assert tau > 0

    theta = [-tau / 2, tau / 2]
    theta.extend(
        math.pi / 2 + (2 * j - Q - 1) * x
        for j in range(2, Q)
    )

    primal_sides = [
        EPS[j] * complex(math.cos(theta[j]), math.sin(theta[j]))
        for j in range(Q)
    ]
    side_order = sorted(
        range(Q), key=lambda j: cmath.phase(primal_sides[j]) % (2 * math.pi)
    )
    assert side_order == EXPECTED_SIDE_ORDER

    points_complex = [0j]
    for j in side_order:
        points_complex.append(points_complex[-1] + primal_sides[j])

    closure = abs(points_complex[-1])
    assert closure < 1.0e-10

    points = np.array([[z.real, z.imag] for z in points_complex[:-1]])
    points -= points.mean(axis=0)
    return points, diameter, delta, tau, side_order


def active_sets(points: np.ndarray, diameter: float):
    distances = np.linalg.norm(points[:, None, :] - points[None, :, :], axis=2)
    contacts = []
    diameters = []
    for i in range(Q):
        for j in range(i + 1, Q):
            d = distances[i, j]
            if abs(d - 1) < 1.0e-8:
                contacts.append((i, j))
            if abs(d - diameter) < 1.0e-8:
                diameters.append((i, j))

    assert contacts == EXPECTED_CONTACTS
    assert diameters == EXPECTED_DIAMETERS

    inactive_contact_slack = min(
        distances[i, j] - 1
        for i in range(Q) for j in range(i + 1, Q)
        if (i, j) not in contacts
    )
    inactive_diameter_slack = min(
        diameter - distances[i, j]
        for i in range(Q) for j in range(i + 1, Q)
        if (i, j) not in diameters
    )
    return distances, contacts, diameters, inactive_contact_slack, inactive_diameter_slack


def positive_stress(points: np.ndarray, contacts, diameters):
    edges = contacts + diameters
    signs = [1] * len(contacts) + [-1] * len(diameters)
    equilibrium = np.zeros((2 * Q, len(edges)))

    for col, ((i, j), sign) in enumerate(zip(edges, signs)):
        delta = points[i] - points[j]
        equilibrium[2 * i:2 * i + 2, col] = sign * delta
        equilibrium[2 * j:2 * j + 2, col] = -sign * delta

    n = len(edges)
    # Variables are all stress coefficients followed by t=min coefficient.
    objective = np.zeros(n + 1)
    objective[-1] = -1

    inequalities = np.zeros((n, n + 1))
    for i in range(n):
        inequalities[i, i] = -1
        inequalities[i, -1] = 1

    equalities = np.zeros((2 * Q + 1, n + 1))
    equalities[:2 * Q, :n] = equilibrium
    equalities[-1, len(contacts):n] = 1  # sum beta = 1
    rhs = np.zeros(2 * Q + 1)
    rhs[-1] = 1

    result = linprog(
        objective,
        A_ub=inequalities,
        b_ub=np.zeros(n),
        A_eq=equalities,
        b_eq=rhs,
        bounds=[(None, None)] * (n + 1),
        method="highs",
    )
    assert result.success

    weights = result.x[:n]
    residual = np.linalg.norm(equilibrium @ weights)
    assert weights.min() > 0.05
    assert residual < 1.0e-10
    return weights[:len(contacts)], weights[len(contacts):], residual


def laplacian(edges, weights):
    matrix = np.zeros((Q, Q))
    for (i, j), weight in zip(edges, weights):
        matrix[i, i] += weight
        matrix[j, j] += weight
        matrix[i, j] -= weight
        matrix[j, i] -= weight
    return matrix


def main() -> None:
    # Exact symbolic consistency check for the palindromic amplitude polynomial.
    t = sp.symbols("t")
    p13 = (
        t**10 - 2*t**9 - 8*t**8 + 18*t**7 + 17*t**6 - 52*t**5
        + t**4 + 51*t**3 - 22*t**2 - 13*t + 11
    )
    assert sp.Poly(p13, t).degree() == 10

    points, diameter, delta, tau, side_order = reconstruct()
    distances, contacts, diameters, contact_slack, diameter_slack = active_sets(
        points, diameter
    )
    alpha, beta, equilibrium_residual = positive_stress(points, contacts, diameters)

    omega = laplacian(contacts, alpha) - laplacian(diameters, beta)
    eigenvalues = np.linalg.eigvalsh(omega)
    assert np.max(np.abs(eigenvalues[:3])) < 1.0e-10
    assert eigenvalues[3] > 1.10

    print(f"q={Q}, m={M}")
    print(f"delta={delta:.16f}")
    print(f"D={diameter:.16f}")
    print(f"tau={tau:.16f}")
    print(f"side_order={side_order}")
    print(f"contacts={contacts}")
    print(f"diameters={diameters}")
    print(f"min inactive contact slack={contact_slack:.12f}")
    print(f"min inactive diameter slack={diameter_slack:.12f}")
    print(f"min stress coefficient={min(alpha.min(), beta.min()):.12f}")
    print(f"equilibrium residual={equilibrium_residual:.3e}")
    print("stress eigenvalues=" + np.array2string(eigenvalues, precision=10))
    print(f"canonical short 05={distances[0, 5]:.12f}")


if __name__ == "__main__":
    main()
