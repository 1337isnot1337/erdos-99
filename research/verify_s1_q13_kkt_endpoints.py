#!/usr/bin/env python3
"""Independent numerical check of the q=13 S1 KKT-segment endpoints.

This supplements target_c_s1_q13_shell_regression.py. It is a regression, not an
interval-arithmetic theorem or a global-minimizer certificate.

The constrained null direction recovered from an SVD is defined only up to sign.
Accordingly, the two endpoint edges are checked as an unordered pair rather than
being attached to the sign of the arbitrary numerical direction.
"""

from __future__ import annotations

import numpy as np

from target_c_s1_q13_shell_regression import (
    Q,
    active_sets,
    laplacian,
    positive_stress,
    reconstruct,
)


def equilibrium_matrix(points, contacts, diameters):
    edges = contacts + diameters
    signs = [1] * len(contacts) + [-1] * len(diameters)
    matrix = np.zeros((2 * Q, len(edges)))
    for col, ((i, j), sign) in enumerate(zip(edges, signs)):
        delta = points[i] - points[j]
        matrix[2 * i : 2 * i + 2, col] = sign * delta
        matrix[2 * j : 2 * j + 2, col] = -sign * delta
    return matrix


def main() -> None:
    points, diameter, _, _, _ = reconstruct()
    _, contacts, diameters, _, _ = active_sets(points, diameter)
    alpha, beta, _ = positive_stress(points, contacts, diameters)
    midpoint = np.concatenate([alpha, beta])

    equilibrium = equilibrium_matrix(points, contacts, diameters)
    _, singular, vh = np.linalg.svd(equilibrium)
    rank = int(np.sum(singular > 1.0e-10))
    assert rank == 2 * Q - 3
    nullspace = vh[rank:].T
    assert nullspace.shape == (len(midpoint), 2)

    beta_total = np.zeros(len(midpoint))
    beta_total[len(contacts) :] = 1
    coordinates = beta_total @ nullspace
    direction_coeff = np.array([coordinates[1], -coordinates[0]])
    direction = nullspace @ direction_coeff
    direction /= np.linalg.norm(direction)

    assert np.linalg.norm(equilibrium @ direction) < 1.0e-10
    assert abs(beta_total @ direction) < 1.0e-10

    lower = -np.inf
    upper = np.inf
    for weight, velocity in zip(midpoint, direction):
        if velocity > 1.0e-14:
            lower = max(lower, -weight / velocity)
        elif velocity < -1.0e-14:
            upper = min(upper, -weight / velocity)

    assert -0.470 < lower < -0.468
    assert 0.468 < upper < 0.470

    endpoint_edges = []
    for label, parameter in (("lower", lower), ("upper", upper)):
        weights = midpoint + parameter * direction
        assert weights.min() > -1.0e-10

        zero_indices = np.flatnonzero(np.abs(weights) < 1.0e-9)
        assert len(zero_indices) == 1
        zero_index = int(zero_indices[0])
        assert zero_index >= len(contacts)
        zero_edge = diameters[zero_index - len(contacts)]
        endpoint_edges.append(zero_edge)

        alpha_e = weights[: len(contacts)]
        beta_e = weights[len(contacts) :]
        omega = laplacian(contacts, alpha_e) - laplacian(diameters, beta_e)
        eigenvalues = np.linalg.eigvalsh(omega)
        assert np.max(np.abs(eigenvalues[:3])) < 1.0e-10
        assert eigenvalues[3] > 1.05

        print(label, "endpoint parameter =", parameter)
        print("  zero diameter edge =", zero_edge)
        print("  first positive stress eigenvalue =", eigenvalues[3])

    assert set(endpoint_edges) == {(1, 7), (4, 11)}
    print("PASS: q=13 S1 normalized KKT endpoints remain numerically PSD")


if __name__ == "__main__":
    main()
