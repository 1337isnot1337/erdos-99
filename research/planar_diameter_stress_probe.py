"""Falsification probe for a strengthened C53 response-PSD statement.

Run: python3 research/planar_diameter_stress_probe.py
Model: regular odd-polygon boundary, interior points, straight planar Delaunay
network, nonnegative edge conductances, actual diameter loads, exact-form
vertex equilibrium and sum(beta)=1 imposed by a floating-point LP.
OMITTED: equal/unit contact lengths, global minimum diameter, contact minimality.
Arithmetic: floating point, deterministic seeds. Output is exploratory evidence
only; any negative eigenvalue requires an exact follow-up certificate. A pass
is not a proof of PSD, not a C-I closure, and not a packing optimality certificate.
"""

import numpy as np
from scipy.optimize import linprog
from scipy.spatial import Delaunay


def probe(sides, interior, seed):
    rng = np.random.default_rng(seed)
    angle = 2 * np.pi * np.arange(sides) / sides
    boundary = np.column_stack((np.cos(angle), np.sin(angle)))
    weights = rng.dirichlet(np.ones(sides), size=interior)
    points = np.vstack((boundary, weights @ boundary))
    triangles = Delaunay(points).simplices
    contacts = sorted({tuple(sorted((int(t[i]), int(t[j]))))
                       for t in triangles for i in range(3) for j in range(i)})
    diameters = sorted({tuple(sorted((i, (i + sides // 2) % sides)))
                        for i in range(sides)})
    edges = contacts + diameters
    signs = np.array([1.] * len(contacts) + [-1.] * len(diameters))
    count = len(points)
    matrix = np.zeros((2 * count + 1, len(edges)))
    for e, (i, j) in enumerate(edges):
        d = signs[e] * (points[i] - points[j])
        matrix[2*i:2*i+2, e] = d
        matrix[2*j:2*j+2, e] = -d
    matrix[-1, len(contacts):] = 1
    rhs = np.zeros(2 * count + 1)
    rhs[-1] = 1
    worst = 0.
    for attempt in range(30):
        if attempt % 3:
            field = rng.normal(size=count)
            objective = np.array([s * (field[i]-field[j])**2
                                  for s, (i, j) in zip(signs, edges)])
        else:
            objective = rng.normal(size=len(edges))
        result = linprog(objective, A_eq=matrix, b_eq=rhs,
                         bounds=(0, None), method="highs")
        if not result.success:
            raise RuntimeError(result.message)
        lap = np.zeros((count, count))
        for weight, sign, (i, j) in zip(result.x, signs, edges):
            value = weight * sign
            lap[i, i] += value
            lap[j, j] += value
            lap[i, j] -= value
            lap[j, i] -= value
        eigenvalue, vectors = np.linalg.eigh(lap)
        worst = min(worst, float(eigenvalue[0]))
        if eigenvalue[0] < -1e-7:
            print("CANDIDATE", sides, interior, seed, attempt,
                  "eigenvalue", eigenvalue[0],
                  "equilibrium residual", np.max(np.abs(matrix @ result.x-rhs)))
            print("points", points.tolist())
            print("signed edges", [(i,j,float(sign*w)) for (i,j),sign,w
                                   in zip(edges,signs,result.x) if w>1e-10])
            print("negative field", vectors[:,0].tolist())
            return False
    print("tested", sides, interior, seed, "minimum numerical eigenvalue", worst)
    return True


def main():
    for sides in (5, 7, 9, 11):
        for seed in range(5):
            if not probe(sides, sides, seed):
                return
    print("No candidate found in 600 sampled LP stresses. This is not a PSD proof.")


if __name__ == "__main__":
    main()
