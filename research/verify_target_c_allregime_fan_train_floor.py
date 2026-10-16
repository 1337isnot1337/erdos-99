"""Retained arithmetic provenance for the retracted all-regime fan/train floor.

The density-floor derivation was retracted because the finite fan term is O(D), not
O(D^2). This checks old endpoint arithmetic only; it does not certify a density floor,
the imported geometric theorems, or global optimality.
"""

from fractions import Fraction as F


def main() -> None:
    pi_lo = F(3141592653589793, 10**15)
    pi_hi = F(3141592653589794, 10**15)
    s3_lo = F(1732050807568877, 10**15)
    s3_hi = F(1732050807568878, 10**15)
    delta_lo = pi_lo / (2 * s3_hi)
    delta_hi = pi_hi / (2 * s3_lo)
    s_lo = F(9523128068, 10**10)
    s_hi = F(9523128069, 10**10)
    assert s_lo * s_lo < delta_lo < delta_hi < s_hi * s_hi

    # t_ar = sqrt(8s^2+160s+100)-4s-10.
    rad_lo = 8 * s_lo * s_lo + 160 * s_lo + 100
    rad_hi = 8 * s_hi * s_hi + 160 * s_hi + 100
    root_lo = F(1611289069, 10**8)
    root_hi = F(1611289070, 10**8)
    assert root_lo * root_lo < rad_lo < rad_hi < root_hi * root_hi
    t_lo = root_lo - 4 * s_hi - 10
    t_hi = root_hi - 4 * s_lo - 10
    assert F(2303639, 10**6) < t_lo < t_hi < F(2303640, 10**6)

    t0_lo = 4 * (s_lo + pi_lo) / 9
    t0_hi = 4 * (s_hi + pi_hi) / 9
    assert F(18195, 10**4) < t0_lo < t0_hi < t_lo

    # Lower endpoint H at t_ar is bounded above using positive upper endpoints
    # and negative lower endpoints.
    h_square_hi = t_hi / 2 + 2 * s_hi
    h_upper = (
        h_square_hi * h_square_hi
        - 20 * (s_lo - t_lo / 4)
        - 2 * delta_lo
    )
    assert h_upper < F(1, 1000)

    # J(t0) upper bound.
    j_a_hi = 5 * t0_hi - 2 * pi_lo
    j_b_lo = 2 * t0_lo - pi_hi
    j_upper = j_a_hi * j_a_hi - 20 * j_b_lo - 2 * delta_lo
    assert j_upper < F(-384, 100)

    # J(t_ar) upper bound.
    j2_a_hi = 5 * t_hi - 2 * pi_lo
    j2_b_lo = 2 * t_lo - pi_hi
    j2_upper = j2_a_hi * j2_a_hi - 20 * j2_b_lo - 2 * delta_lo
    assert j2_upper < F(-372, 100)

    # The lower endpoint is below the vertex of H throughout the admissible
    # kappa-range: pi/2+2s<5.
    assert pi_hi / 2 + 2 * s_hi < 5

    print(f"t_ar_interval=({float(t_lo):.13f},{float(t_hi):.13f})")
    print(f"t0_interval=({float(t0_lo):.13f},{float(t0_hi):.13f})")
    print(f"J(t0)_upper={float(j_upper):.6f}")
    print(f"J(t_ar)_upper={float(j2_upper):.6f}")
    print("all-regime fan/train scalar-floor arithmetic provenance: OK; density claim retracted")


if __name__ == "__main__":
    main()
