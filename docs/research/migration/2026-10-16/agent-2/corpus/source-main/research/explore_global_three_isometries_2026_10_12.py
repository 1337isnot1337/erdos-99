#!/usr/bin/env python3
"""Numerical discovery only. A successful endpoint needs a separate certificate."""
from itertools import combinations, product
import argparse
import json
import math
from pathlib import Path

import numpy as np
from scipy.optimize import minimize


def search(n, attempts, seed, rotations=False):
    if n < 5 or n % 2 == 0 or attempts < 1:
        raise ValueError("Use an odd rim size n>=5 and a positive attempt budget")
    rng = np.random.default_rng(seed)
    angles = np.arange(n) * (2 * math.pi / n)
    radius = 1 / (2 * math.sin(math.pi / n))
    points = radius * np.column_stack((np.cos(angles), np.sin(angles)))
    pairs = np.array(list(combinations(range(n), 2)))
    original = points[pairs[:, 0]] - points[pairs[:, 1]]
    old_d2 = float(np.max(np.sum(original**2, axis=1)))
    diameter_pairs = [tuple(pair) for pair, d2 in zip(pairs, np.sum(original**2, axis=1))
                      if abs(d2 - old_d2) < 1e-9]
    patterns = []
    # Restricted growth removes only permutations of the same three groups.
    for tail in product(range(3), repeat=n-1):
        state = (0,) + tail
        if max(state) != 2 or any(state[k] > 1 + max(state[:k]) for k in range(1, n)):
            continue
        if any(state[i] == state[j] for i, j in diameter_pairs):
            continue
        patterns.append(np.array(state))
    rng.shuffle(patterns)
    best = old_d2
    for trial in range(attempts):
        state = patterns[trial % len(patterns)]
        mixed = state[pairs[:, 0]] != state[pairs[:, 1]]
        width = 3 if rotations else 2
        size = 2*width + 1
        def transformed(z):
            result = points.copy()
            derivatives = np.zeros((n, 2, size))
            for group in (1, 2):
                offset = width*(group-1)
                selected = state == group
                if rotations:
                    theta = z[offset]
                    c, s = math.cos(theta), math.sin(theta)
                    matrix = np.array([[c,-s],[s,c]])
                    rotated = points[selected] @ matrix.T
                    result[selected] = rotated + z[offset+1:offset+3]
                    derivatives[selected,:,offset] = rotated @ np.array([[0,1],[-1,0]])
                    derivatives[selected,:,offset+1] = [1,0]
                    derivatives[selected,:,offset+2] = [0,1]
                else:
                    result[selected] += z[offset:offset+2]
                    derivatives[selected,:,offset] = [1,0]
                    derivatives[selected,:,offset+1] = [0,1]
            return result, derivatives
        def deltas(z):
            moved, _ = transformed(z)
            return moved[pairs[:,0]] - moved[pairs[:,1]]
        def d2(z):
            delta = deltas(z)
            return np.sum(delta**2, axis=1)
        def jac_d2(z):
            delta = deltas(z)
            _, derivatives = transformed(z)
            delta_derivatives = derivatives[pairs[:,0]] - derivatives[pairs[:,1]]
            return 2*np.einsum('pi,pij->pj', delta, delta_derivatives)
        def constraints(z):
            distances = d2(z)
            return np.concatenate((distances[mixed] - 1.00001, z[-1] - distances))
        def jac_constraints(z):
            jac = jac_d2(z)
            upper = -jac
            upper[:, -1] = 1
            return np.vstack((jac[mixed], upper))
        initial = np.r_[rng.uniform(-2*radius, 2*radius, size-1), old_d2]
        gradient = np.zeros(size)
        gradient[-1] = 1
        result = minimize(lambda z: z[-1], initial, jac=lambda z: gradient,
                          bounds=[(-4*radius,4*radius)]*(size-1) + [(1.,old_d2)],
                          constraints={"type":"ineq", "fun":constraints,"jac":jac_constraints},
                          method="SLSQP", options={"maxiter":300,"ftol":1e-11})
        distances = d2(result.x)
        if np.min(distances[mixed]) >= 1.000009 and np.max(distances) < best:
            best = float(np.max(distances))
        if np.min(distances[mixed]) >= 1.000009 and np.max(distances) < old_d2 - .001:
            return {"status":"numerical candidate only", "n":n, "seed":seed,
                    "trial":trial, "patterns":len(patterns), "state":state.tolist(),
                    "rotations":rotations,"parameters":result.x[:-1].tolist(),
                    "old_diameter_squared":old_d2,
                    "endpoint_diameter_squared":float(np.max(distances)),
                    "minimum_mixed_distance_squared":float(np.min(distances[mixed]))}
        if trial % 50 == 0:
            print(json.dumps({"n":n,"trial":trial,"patterns":len(patterns),"best":best}), flush=True)
    return {"status":"no certified conclusion; numerical search exhausted", "n":n,
            "seed":seed,"attempts":attempts,"patterns":len(patterns),"best":best}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=7)
    parser.add_argument("--attempts", type=int, default=500)
    parser.add_argument("--seed", type=int, default=20261012)
    parser.add_argument("--rotations", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = search(args.n, args.attempts, args.seed, args.rotations)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result), flush=True)
