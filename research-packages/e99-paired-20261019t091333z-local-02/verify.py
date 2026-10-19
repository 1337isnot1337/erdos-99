"""Exact arithmetic for the PR147 conditional PC3/payment obstruction."""

import json
from fractions import Fraction as F
from math import isqrt


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def sign_rational(x):
    return (x > 0) - (x < 0)


def sign_sqrt3(a, b):
    """Sign of a + b*sqrt(3), for rational a,b, without floats."""
    if a == 0:
        return sign_rational(b)
    if b == 0:
        return sign_rational(a)
    if a > 0 and b > 0:
        return 1
    if a < 0 and b < 0:
        return -1
    compare = sign_rational(a * a - 3 * b * b)
    return compare if a > 0 else -compare


def add_surd(x, y):
    return x[0] + y[0], x[1] + y[1]


def sub_surd(x, y):
    return x[0] - y[0], x[1] - y[1]


def scale_surd(x, q):
    return x[0] * q, x[1] * q


def floor_q_over_sqrt3(q):
    r = isqrt((q * q) // 3)
    require(3 * r * r <= q * q < 3 * (r + 1) * (r + 1),
            "integer square root does not give floor(q/sqrt(3))")
    return r


def family_parameters(m):
    if m < 12 or m % 4:
        raise ValueError("m must be a multiple of four and at least twelve")
    q = m * m
    p = floor_q_over_sqrt3(q) + 1
    t = F(p, q)
    c = (1 - t * t) / (1 + t * t)
    s = 2 * t / (1 + t * t)
    require(3 * p * p > q * q, "parameter t is not above 1/sqrt(3)")
    require(t < F(117, 200), "parameter t exceeds the all-m rational cap")
    require(c > 0 and s > 0 and t < 1, "invalid acute-grid parameters")
    return p, q, t, c, s


def residual_surd(m, c, s):
    # Q = 2(c-2s)m^2 - 2 + (2m^2-4m+1)*sqrt(3).
    return 2 * (c - 2 * s) * m * m - 2, 2 * m * m - 4 * m + 1


def verify_case(m):
    p, q, t, c, s = family_parameters(m)
    m2 = m * m

    # These two listed hull points differ by (1-c+s,-1-c-s)*m.
    dx = 1 - c + s
    dy = -1 - c - s
    require(dx * dx + dy * dy == 4 * (1 + s),
            "listed hull points do not give the claimed diameter")
    # Thus D^2 is at least 4*(1+s)*m^2.
    diameter_squared_lower = 4 * (1 + s) * m2
    require(diameter_squared_lower > 4 * m2 > 3 * m2,
            "diameter does not clear the PC3 threshold")
    require(F(4, 1) > 3, "4/sqrt(3) is not greater than 2")
    # Hence 2D/sqrt(3) > 4m/sqrt(3) > 2m >= M' + b'
    # for every trim. The canonical PC3 positive-part term is zero
    # eventually, since its o(D) error cannot erase this linear margin.

    trim = m // 4
    depth = trim - 2
    trimmed_shore_sum = 2 * (m - 2 * trim)
    require(depth > 0, "the displayed PR147 trim has nonpositive depth")
    require(trimmed_shore_sum == m, "the displayed trim sizes changed")
    require(trimmed_shore_sum <= 2 * m, "trimmed shore sum exceeds full grid")

    v12 = 2 * (1 + c) * m2 - 1
    q12 = 2 * (1 + c) * m2
    p12 = F(1)
    physical_determinant_mass = 2 * s * m2 + 1
    total_determinant_mass = 2 * (s + 1 + c) * m2
    require(v12 == q12 - p12, "cross virtual/deleted ledger changed")
    require(physical_determinant_mass + v12 == total_determinant_mass,
            "global physical/virtual determinant ledger changed")
    g = m2 - 1
    e = (2 * m2 * s + 1, -m2 - F(1, 2))
    h = ((4 + 2 * c) * m2 - 2, F(0))
    j = (2 * (1 + c) * m2, F(0))
    net = sub_surd(add_surd(scale_surd(e, 2), h), j)
    expected_net = (2 * (1 + 2 * s) * m2, -2 * m2 - 1)
    require(net == expected_net, "support-corrected shell identity changed")
    require(j[0] == v12 + 1, "support turning differs from cross determinant")
    require(h[0] - j[0] == 2 * g, "support-depth cancellation changed")

    boundary_allowance = (F(0), 4 * m)
    candidate_rhs = add_surd((p12, F(0)), add_surd(net, boundary_allowance))
    q_actual = sub_surd((v12, F(0)), candidate_rhs)
    require(q_actual == residual_surd(m, c, s), "payment residual formula changed")
    require(sign_sqrt3(*q_actual) > 0, "payment residual is not positive")
    raw_h_rhs = add_surd(candidate_rhs, j)
    raw_h_residual = sub_surd((v12, F(0)), raw_h_rhs)
    require(sign_sqrt3(*raw_h_residual) < 0,
            "raw H control no longer demonstrates the turning subtraction")

    # The pure-disk global-minimizer window excludes this family:
    # G+E-c0*B = (1+2s)m^2 + (-m^2-1/2-2m)*sqrt(3).
    source_gap = ((1 + 2 * s) * m2, -m2 - F(1, 2) - 2 * m)
    require(sign_sqrt3(*source_gap) > 0,
            "family does not violate the canonical global-minimizer upper window")

    return {
        "m": m,
        "p": p,
        "t": str(t),
        "c": str(c),
        "s": str(s),
        "D_squared_lower": str(diameter_squared_lower),
        "trim_depth": depth,
        "trimmed_shore_sum": trimmed_shore_sum,
        "PC3_positive_part": "zero eventually; the o(D) remainder is smaller than the linear gap",
        "internal_physical_crossings": 2 * m2,
        "deleted_interface_crossings": 1,
        "V12": str(v12),
        "Q12": str(q12),
        "P12": "1",
        "global_M": str(v12),
        "physical_determinant_mass_S": str(physical_determinant_mass),
        "total_determinant_mass_S_plus_M": str(total_determinant_mass),
        "rhombi_R": 2 * m2 + 1,
        "G": str(g),
        "H": str(h[0]),
        "J": str(j[0]),
        "2E_plus_H_minus_J": [str(net[0]), str(net[1])],
        "payment_residual_Q": [str(q_actual[0]), str(q_actual[1])],
        "Q_positive": True,
        "raw_H_payment_residual": [
            str(raw_h_residual[0]),
            str(raw_h_residual[1]),
        ],
        "raw_H_would_appear_to_pay": True,
        "global_minimizer_upper_violated": True,
    }


def verify_all_m_bound():
    # For m>=12, 1/sqrt(3)<t<1/sqrt(3)+1/m^2<0.585.
    # c decreases and s increases on this interval. These rational bounds
    # give 2(c-2s+sqrt(3)) > f_lower.
    require(F(578, 1000) ** 2 > F(1, 3),
            "rational upper bound for 1/sqrt(3) failed")
    require(F(578, 1000) + F(1, 144) < F(117, 200),
            "all-m upper bound for t is not below 0.585")
    require(F(1732, 1000) ** 2 < 3 < F(1733, 1000) ** 2,
            "rational bounds for sqrt(3) failed")
    tmax = F(117, 200)
    cmin = (1 - tmax * tmax) / (1 + tmax * tmax)
    smax = 2 * tmax / (1 + tmax * tmax)
    f_lower = 2 * (cmin - 2 * smax + F(1732, 1000))
    require(f_lower == F(6425087, 6711125),
            "coefficient lower bound calculation changed")
    require(f_lower > F(95, 100), "coefficient lower bound is too small")

    # Q(m) > g(m); g is increasing for m>=12 and starts strictly positive.
    def g_bound(m):
        return f_lower * m * m - F(1733, 1000) * (4 * m - 1) - 2

    start = g_bound(12)
    first_difference = f_lower * 25 - F(4 * 1733, 1000)
    require(start == F(584259897, 10737800) and start > 0,
            "all-m payment lower bound is not positive at m=12")
    require(first_difference == F(228211313, 13422250) and first_difference > 0,
            "all-m payment lower bound is not increasing")

    # The canonical global-minimizer upper window also excludes the family:
    # s>sqrt(3)/2 implies G+E-c0*B > m^2-sqrt(3)/2-2sqrt(3)m.
    source_lower_at_12 = 12 * 12 - F(1733, 2000) - F(3466, 1000) * 12
    source_first_difference = 25 - F(3466, 1000)
    require(source_lower_at_12 == F(203083, 2000) and source_lower_at_12 > 0,
            "all-m globality-exclusion lower bound failed at m=12")
    require(source_first_difference == F(10767, 500) and source_first_difference > 0,
            "all-m globality-exclusion lower bound is not increasing")
    return {
        "all_m_domain": "integers m >= 12; construction uses multiples of four",
        "coefficient_lower_bound": str(f_lower),
        "Q_lower_bound_at_12": str(start),
        "discrete_increment_lower_bound": str(first_difference),
        "globality_exclusion_lower_bound_at_12": str(source_lower_at_12),
        "globality_exclusion_increment_lower_bound": str(source_first_difference),
    }


def main():
    result = {
        "status": "PASS: exact PR147 PC3-threshold and scalar-payment arithmetic",
        "all_m_proof": verify_all_m_bound(),
        "cases": [verify_case(m) for m in (12, 16, 20, 24, 40, 100)],
        "scope": (
            "Conditional on PR147's displayed geometric ledger; does not replay "
            "its unit-separation/topology verifier or prove global-source extraction."
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


main()
