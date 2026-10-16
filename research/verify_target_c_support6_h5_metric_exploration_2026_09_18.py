#!/usr/bin/env python3
"""High-precision-discovery probe for the sixteen support-six H5 metrics.

Exploratory only: a small residual is neither an exclusion nor a realization.
"""

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from itertools import combinations
import numpy as np
from scipy.optimize import least_squares

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "verify_target_c_support6_h5_metric_normal_form_2026_09_18.py"
spec = spec_from_file_location("normal", SOURCE)
normal = module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(normal)


def reps():
    h5 = normal.h5
    uext = h5.enumerate_uniform_extensions()
    _, uniform = h5.uniform_survivors(uext)
    walls = h5.enumerate_simple_walls(uext)
    _, wall = h5.wall_survivors(uext, walls)
    u, w = normal.orbit_representatives(uniform, wall)
    return [("U", x) for x in u] + [("W", x) for x in w]


def residual_factory(edge_signs, missing):
    edges = sorted(edge_signs)
    sign = {e: (1.0 if edge_signs[e] else -1.0) for e in edges}
    present = [e for e in edges if e not in set(missing)]

    def residual(z):
        y = np.zeros((7, 2), dtype=float)
        y[1] = (1.0, 0.0)
        y[2:] = np.asarray(z).reshape(5, 2)
        out = []
        for i in range(1, 6):
            force = np.zeros(2)
            for a, b in present:
                d = y[a] - y[b]
                length = np.sqrt(float(d @ d) + 1e-24)
                if a == i:
                    force += sign[(a, b)] * d / length
                elif b == i:
                    force -= sign[(a, b)] * d / length
            out.extend(force)
        return np.asarray(out)

    return residual


def main():
    rng = np.random.default_rng(20260918)
    found = []
    for idx, (kind, data) in enumerate(reps()):
        if kind == "U":
            _sg, missing, edge_signs = data
        else:
            _target, _sg, missing, edge_signs = data
        fun = residual_factory(edge_signs, missing)
        best = float("inf")
        for trial in range(32):
            ang = np.linspace(0, 2 * np.pi, 7, endpoint=False)
            yy = np.c_[np.cos(ang), np.sin(ang)]
            yy[1:] += 0.5 * rng.normal(size=(6, 2))
            z0 = yy[2:].reshape(-1) if trial < 12 else rng.normal(scale=2.0, size=10)
            sol = least_squares(fun, z0, max_nfev=1200, ftol=1e-12,
                                xtol=1e-12, gtol=1e-12,
                                bounds=(-30.0, 30.0))
            norm = float(np.linalg.norm(fun(sol.x), ord=np.inf))
            best = min(best, norm)
            if norm < 1e-8:
                y = np.zeros((7, 2)); y[1] = (1.0, 0.0); y[2:] = sol.x.reshape(5, 2)
                mind = min(np.linalg.norm(y[a] - y[b])
                           for a, b in combinations(range(7), 2))
                if mind > 1e-5:
                    found.append((idx, kind, norm, mind))
                    break
        print(idx, kind, "best_inf_residual", f"{best:.3e}",
              "root_found", any(x[0] == idx for x in found), flush=True)
    print("candidate_roots", len(found))
    for x in found:
        print("ROOT", x)


if __name__ == "__main__":
    main()
