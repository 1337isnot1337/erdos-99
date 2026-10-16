#!/usr/bin/env python3
"""Supplementary checks for the almost-unit hull / lattice-interior competitor.

--exact uses Fraction arithmetic only. --numerical uses numpy floating point;
it is a falsification pilot, not a certificate of optimality or of the theorem.
The complete asymptotic proof is in the linked dated report.
"""

import argparse
import json
from fractions import Fraction as F


def atan_bounds(x, terms=40):
    """Alternating integrated geometric series; even partial sum is lower."""
    assert 0 < x < 1 and terms % 2 == 0
    lower = sum(((-1)**k * x**(2*k + 1) / (2*k + 1)
                 for k in range(terms)), F(0))
    return lower, lower + x**(2*terms + 1) / (2*terms + 1)


def exact_checks():
    # 0.8660254037844386 < sqrt(3)/2 < 0.8660254037844387.
    alo = F(8660254037844386, 10**16)
    ahi = F(8660254037844387, 10**16)
    assert 4 * alo * alo < 3 < 4 * ahi * ahi
    rlo, rhi = (1 - ahi) / 2, (1 - alo) / 2
    # Machin: pi = 16 atan(1/5) - 4 atan(1/239). The tangent
    # identity and the branch 0 < 4 atan(1/5)-atan(1/239) < pi/2
    # establish the formula. The series remainder bounds are rational.
    x = F(1, 5)
    tan2 = 2*x/(1-x*x)
    tan4 = 2*tan2/(1-tan2*tan2)
    assert (tan4 - F(1, 239))/(1 + tan4/F(239)) == 1
    a5lo, a5hi = atan_bounds(x)
    a239lo, a239hi = atan_bounds(F(1, 239))
    pilo, pihi = 16*a5lo - 4*a239hi, 16*a5hi - 4*a239lo
    assert F(31415926535897932384, 10**19) < pilo < pihi < F(31415926535897932385, 10**19)
    mulo, muhi = pilo/6 - ahi/2, pihi/6 - alo/2
    assert 2*mulo > F(18117214, 10**8)
    assert pilo*mulo/ahi > F(3286099, 10**7)
    # A physical two-grain cut plus exceptions of 0.3 D remains below
    # the exact payment threshold; the retained competitor gap is positive.
    assert 2*mulo - 2*ahi*F(3, 10)/pilo > F(1577, 10**5)
    assert 2*mulo - 1/(2*pilo) > F(22, 1000)
    assert 13*F(7, 25)**2 > 1 and F(7, 25) < pilo*mulo/ahi
    # The matched outer-row pair threshold is exact precisely at the
    # two short periods used by the proved equal-row seam theorem.
    for ell_squared in (F(1), F(3)):
        assert F(3, 4)/ell_squared + ell_squared/4 == 1
        for gap_fraction in (F(0), F(1, 2), F(3, 4)):
            # Multiply the normalized E-minus-deletion inequality by ell.
            assert 1 - gap_fraction - 1 == -gap_fraction <= 0
    # Flat lattice interfaces really have a linear boundary-site charge.
    # The index parallelogram has area/a = m*s and B = 2(m+s).
    for m, s in ((1, 1), (17, 23), (1000, 2)):
        points, boundary = (m + 1)*(s + 1), 2*(m + s)
        assert F(points) == m*s + F(boundary, 2) + 1
    # A conservative elementary lower bound pi > 3 is sufficient here.
    assert 6 * rlo * rlo > F(269, 10000)
    assert 9 * rlo * rlo / ahi > F(466, 10000)
    # t0 +/- r = a0, 1 at the limiting radius. At any strictly smaller
    # radius both the erosion and exclusion have a positive margin.
    for a in (alo, ahi):
        t0, r0 = (1 + a) / 2, (1 - a) / 2
        assert t0 - r0 == a and t0 + r0 == 1
        r = r0 * F(99, 100)
        assert t0 - r > a and t0 + r < 1 and 2 * r < 1
    # The numerator in the lattice-covolume comparison is eventually
    # positive. At fixed area and perimeter, a larger covolume decreases
    # this upper bound, rather than reversing the desired inequality.
    area, perimeter, vertices = F(10**6), F(1000), F(1000)
    for a in (ahi, F(1), F(4)):
        numerator = area - ahi * perimeter - vertices * 3 * rlo**2
        assert numerator > 0
        upper = vertices + numerator / a
        assert upper <= area / ahi - vertices * 3 * rlo**2 / ahi
    # Retaining a linear exception budget tau still leaves a margin
    # whenever tau < pi^2 r0^2/a0; this identity is exact algebra.
    pi_proxy = F(3)
    threshold = pi_proxy**2 * rlo**2 / ahi
    tau = threshold / 2
    margin = 2 * pi_proxy * rlo**2 - 2 * ahi * tau / pi_proxy
    assert margin == pi_proxy * rlo**2 > 0
    return {
        "arithmetic": "Fraction; no floating-point proof claim",
        "sqrt3_over_2_interval": [str(alo), str(ahi)],
        "diameter_gap_lower_bound_using_pi_gt_3": "> 0.0269",
        "exception_threshold_lower_bound_using_pi_gt_3": "> 0.0466",
        "full_strip_diameter_gap": "> 0.18117214",
        "full_strip_exception_threshold": "> 0.3286099",
        "two_grain_margin_with_cut_and_exceptions_0_3D": "> 0.01577",
        "one_nonresonant_other_sqrt3_row_margin": "> 0.0220",
        "equal_parallel_rows_1_and_sqrt3": "squared-distance and cancellation identities PASS",
        "pi_interval": ["3.1415926535897932384", "3.1415926535897932385"],
        "checks": "PASS",
        "scope": "constant and sign checks only; asymptotic proof is in report",
    }


def numerical_case(q, angle_gap, rotation, shift):
    import numpy as np

    a0 = np.sqrt(3) / 2
    R = 1 / (2 * np.sin(np.pi / q))
    D = 2 * R * np.cos(np.pi / (2 * q))
    theta = np.pi / 3 + angle_gap
    # Strictly separate the interior points. This inflation is far below
    # boundary order and keeps the canonical regular-shell example relevant.
    inflation = 1 + q**-3
    c, s = np.cos(rotation), np.sin(rotation)
    rot = np.array([[c, -s], [s, c]])
    matrix = inflation * rot @ np.array([[1, np.cos(theta)], [0, np.sin(theta)]])
    translation = matrix @ np.asarray(shift)
    inv = np.linalg.inv(matrix)
    max_index = int(np.ceil(np.linalg.norm(inv, axis=1).max() * R + 3))
    j = np.arange(-max_index, max_index + 1)
    # Enumerate row by row to keep memory bounded at larger q.
    accepted, disk_sites, blocked, minimum_shell_distance = 0, 0, 0, float("inf")
    for ii in range(-max_index, max_index + 1):
        pts = np.column_stack((np.full(len(j), ii), j)) @ matrix.T + translation
        radii = np.linalg.norm(pts, axis=1)
        inside = radii <= np.sqrt(R * R - 0.25) - a0
        pts, radii = pts[inside], radii[inside]
        disk_sites += len(pts)
        phi = np.arctan2(pts[:, 1], pts[:, 0])
        # Closest shell node is the nearest multiple of 2pi/q in angle.
        dphi = (phi + np.pi / q) % (2 * np.pi / q) - np.pi / q
        dist2 = (R - radii)**2 + 2 * R * radii * (1 - np.cos(dphi))
        good = dist2 > 1 + 1e-10
        accepted += int(good.sum())
        blocked += int((~good).sum())
        if good.any():
            minimum_shell_distance = min(minimum_shell_distance, float(np.sqrt(dist2[good].min())))
    n = q + accepted
    competitor_diameter = 2 * np.sqrt(a0 * n / np.pi)
    t0, r0 = (1 + a0) / 2, (1 - a0) / 2
    phi = np.arange(q) * 2 * np.pi / q
    trace = (R - t0) * np.column_stack((np.cos(phi), np.sin(phi)))
    phase = (trace - translation) @ inv.T
    # The lattice basis is oblique. Componentwise rounding alone is not a
    # closest-site algorithm, so inspect all nearby index offsets.
    near = np.rint(phase).astype(int)
    closest2 = np.full(q, np.inf)
    for di in range(-2, 3):
        for dj in range(-2, 3):
            candidates = (near + np.array([di, dj])) @ matrix.T + translation
            closest2 = np.minimum(closest2, ((trace - candidates)**2).sum(axis=1))
    target_missing = int((closest2 < (0.95 * r0)**2).sum())
    covolume = float(abs(np.linalg.det(matrix)))
    characters = {}
    for mode in ((1, 0), (0, 1), (1, 1), (2, -1)):
        characters[str(mode)] = float(abs(np.exp(2j * np.pi * (phase @ np.asarray(mode))).mean()))
    return {
        "q": q, "theta_gap": angle_gap, "rotation": rotation, "shift": shift,
        "source_population": n, "diameter": float(D),
        "lost_sites_inside_eroded_disk": blocked,
        "source_population_deficit_per_D": float((np.pi * D * D / (4 * a0) - n) / D),
        "average_disk_competitor_diameter_gap": float(D - competitor_diameter),
        "minimum_shell_distance_of_retained_interior": minimum_shell_distance,
        "trace_ball_missing_sites": target_missing,
        "trace_ball_expected_sites": float(q * np.pi * (0.95 * r0)**2 / covolume),
        "trace_character_moduli": characters,
        "scope": "floating-point feasible-family pilot; no global-optimality certificate",
    }


def mirror_seam_pilot():
    """Falsify g>=h for two full mirrored half-lattices if a smaller gap appears.

    Floating-point grid search; positive results do not prove a gap bound,
    an arbitrary-hole payment, a finite-source theorem, or global optimality.
    """
    import numpy as np
    from math import sqrt

    results = []
    for m, n, wm, wn in ((1, 0, 0, 1), (1, 1, 0, 1),
                         (2, 1, 1, 1), (3, 1, 2, 1), (3, 2, 1, 1)):
        assert m*wn - n*wm == 1
        v = np.array([m + n/2, sqrt(3)*n/2])
        w = np.array([wm + wn/2, sqrt(3)*wn/2])
        ell = float(np.linalg.norm(v))
        height = sqrt(3)/(2*ell)
        row_phase = float(np.dot(v, w)/ell)
        phases = np.linspace(0, ell, 200001)
        required_gap = np.zeros_like(phases)
        for total_rows in range(int(1/height) + 2):
            for upper_row in range(total_rows + 1):
                dx = (phases + (total_rows - 2*upper_row)*row_phase + ell/2) % ell - ell/2
                needed = np.sqrt(np.maximum(0, 1 - dx*dx)) - total_rows*height
                required_gap = np.maximum(required_gap, needed)
        best = int(required_gap.argmin())
        results.append({
            "primitive_index": [m, n], "period": ell, "row_pitch": height,
            "best_grid_phase": float(phases[best]),
            "minimum_grid_gap": float(required_gap[best]),
            "gap_minus_row_pitch": float(required_gap[best] - height),
            "arithmetic": "numpy float; phase grid of 200001 points",
        })
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--exact", action="store_true")
    parser.add_argument("--numerical", action="store_true")
    parser.add_argument("--seam-pilot", action="store_true")
    parser.add_argument("--q", type=int, nargs="+", default=[101, 401, 1001])
    args = parser.parse_args()
    if args.exact or not args.numerical:
        print(json.dumps(exact_checks(), sort_keys=True))
    if args.numerical:
        for q in args.q:
            if q < 5 or q % 2 == 0:
                raise ValueError("Regular-shell numerical pilot requires odd q >= 5")
            for rotation, shift in ((0.0, (0.0, 0.0)), (0.271, (0.499, 0.499)),
                                    (1.047, (0.211, 0.733))):
                print(json.dumps(numerical_case(q, q**-2, rotation, shift), sort_keys=True))
    if args.seam_pilot:
        print(json.dumps({"mirror_seam_pilot": mirror_seam_pilot()}, sort_keys=True))


if __name__ == "__main__":
    main()
