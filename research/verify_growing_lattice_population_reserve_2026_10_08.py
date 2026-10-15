#!/usr/bin/env python3
"""Exact phase arithmetic and finite translated triangular-lattice disk patches.

The universal reserve uses the report's Fourier proof and checked NIST remainder.
Finite patches have no global-optimality certificate. Expanded patches are
triangle-free and nonglobal by the exact common-scaling competitor.
"""
from fractions import Fraction as F
from math import isqrt
import json
import verify_target_c_voronoi_spacing_debit_2026_10_08 as prior


def arithmetic():
    low5, high5 = prior.atan_bounds(F(1, 5), 20)
    low239, high239 = prior.atan_bounds(F(1, 239), 10)
    pi_low, pi_high = 16*low5-4*high239, 16*high5-4*low239
    assert 3 < pi_low < pi_high < F(22, 7)
    phase_first_case = F(1, 4)
    second_cosine_upper = 2*F(1, 4)**2-1
    second_sine_upper = 2*F(1, 4)
    assert second_cosine_upper == F(-7, 8)
    assert second_sine_upper == F(1, 2)
    phase_second_case = -(second_cosine_upper+second_sine_upper)/4
    assert phase_second_case == F(3, 32) < phase_first_case
    error_at_z8 = F(3, 8)/8
    assert error_at_z8 == F(3, 64)
    assert phase_second_case-error_at_z8 == F(3, 64)
    # The positive-part inequality loses a factor two. The amplitude's
    # sqrt(2) and R=D/2 conversion together give another factor two.
    assert F(3, 64)/4 == F(3, 256)
    assert F(22, 7)**4 < 3**5
    sqrt3_low = F(1732050807568877, 10**15)
    assert sqrt3_low*sqrt3_low < 3
    return pi_high, sqrt3_low, {
        "phase_lower_bound": "3/32",
        "normalized_error_at_z8": "3/64",
        "remaining_coefficient_lower_bound": "3/64",
        "conservative_diameter_reserve": "sqrt(D)/256",
        "pi_bounds_certified": True,
        "constant_inequality_certified": True,
    }


def ceil_div(a, b):
    assert b > 0
    return -((-a)//b)


def rows(radius, denominator, a, b):
    threshold = (denominator*radius)**2-1
    for i in range(-2*radius-2, 2*radius+3):
        d = denominator*i-a
        discriminant = 4*threshold-3*d*d
        if discriminant < 0:
            continue
        h = isqrt(discriminant)
        offset = d-2*b
        lo = ceil_div(-h-offset, 2*denominator)
        hi = (h-offset)//(2*denominator)
        if lo <= hi:
            yield i, lo, hi


def numerator(i, j, denominator, a, b):
    d, e = denominator*i-a, denominator*j-b
    return d*d+d*e+e*e


def patch_case(radius, pi_high, sqrt3_low, denominator=16):
    best = None
    for a in range(denominator):
        for b in range(denominator):
            count = sum(hi-lo+1 for _, lo, hi in rows(radius, denominator, a, b))
            if best is None or count > best[0]:
                best = count, a, b
    count, a, b = best
    threshold = (denominator*radius)**2-1
    total = 0
    maximum_radial_numerator = 0
    row_checks = 0
    for i, lo, hi in rows(radius, denominator, a, b):
        # The quadratic is convex in j; endpoint bounds cover every row point.
        for j in (lo, hi):
            value = numerator(i, j, denominator, a, b)
            assert value <= threshold
            maximum_radial_numerator = max(maximum_radial_numerator, value)
        assert numerator(i, lo-1, denominator, a, b) > threshold
        assert numerator(i, hi+1, denominator, a, b) > threshold
        total += hi-lo+1
        row_checks += 1
    assert total == count and maximum_radial_numerator <= threshold
    assert all(numerator(i, j, denominator, a, b) <= threshold
               for i, j in ((0, 0), (1, 0), (0, 1), (4, 0)))
    assert all(i*i+i*j+j*j == 1 for i, j in ((1, 0), (0, 1), (1, -1)))
    mean_upper = 2*pi_high*radius*radius/sqrt3_low
    root_denominator = 10**6
    root_upper = F(isqrt(2*radius*root_denominator**2)+1, root_denominator)
    assert root_upper*root_upper > 2*radius
    assert count-1 > mean_upper+root_upper/256
    radial2_upper = F(maximum_radial_numerator, denominator**2)
    lam = 1+F(1, 4*denominator**2*radius**2)
    assert lam > 1
    assert lam*lam*F(threshold, denominator**2) < radius**2
    assert lam*lam*radial2_upper < radius**2
    # All lattice differences have integer squared norm >=1. The common
    # expansion makes them >1 and scales the actual diameter by lam.
    return {
        "radius": radius, "translation_denominator": denominator,
        "translation_numerators": [a, b], "translations_tested": denominator**2,
        "strict_disk_lattice_points": count,
        "certified_rows": row_checks,
        "maximum_radial_squared": str(radial2_upper),
        "population_minus_one_exceeds_mean_and_reserve": True,
        "expanded_source_has_no_unit_contacts": True,
        "expanded_source_stays_strictly_in_disk": True,
        "exact_common_expansion": str(lam),
        "strict_competitor": "the unexpanded same-cardinality lattice patch",
    }


if __name__ == "__main__":
    pi_high, sqrt3_low, certificate = arithmetic()
    print(json.dumps({
        "status": "PASS",
        "arithmetic_certificate": certificate,
        "finite_patches": [
            patch_case(r, pi_high, sqrt3_low) for r in (10, 20, 50, 100, 200)
        ],
        "does_not_prove": [
            "the universal Fourier claim by finite sampling",
            "NIST special-function remainder without its cited theorem",
            "global optimality of any finite patch",
            "triangle forcing from population excess alone",
            "a source-preserving C-II replacement or Level I closure",
        ],
    }, indent=2))
