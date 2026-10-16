"""Retained arithmetic provenance for the retracted fan/train/hull scalar floor.

The density-floor derivation was retracted because the finite fan term is O(D), not
O(D^2). This checks old rational enclosures only; it does not certify a density floor,
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

    # C = 2 sqrt(2 Delta_2).
    c_lo = F(2693547, 10**6)
    c_hi = F(2693548, 10**6)
    assert c_lo * c_lo < 8 * delta_lo < 8 * delta_hi < c_hi * c_hi

    # The discriminant for the larger root of J is 1600-400*pi+200*Delta_2.
    disc_lo = 1600 - 400 * pi_hi + 200 * delta_lo
    disc_hi = 1600 - 400 * pi_lo + 200 * delta_hi
    sd_lo = F(22907266, 10**6)
    sd_hi = F(22907267, 10**6)
    assert sd_lo * sd_lo < disc_lo < disc_hi < sd_hi * sd_hi

    tstar_lo = (20 * pi_lo + 40 + sd_lo) / 50
    tstar_hi = (20 * pi_hi + 40 + sd_hi) / 50
    assert F(2514782, 10**6) < tstar_lo < tstar_hi < F(2514783, 10**6)

    t0_lo = (2 * c_lo + 4 * pi_lo) / 9
    t0_hi = (2 * c_hi + 4 * pi_hi) / 9
    assert F(19948, 10**4) < t0_lo < t0_hi < tstar_lo

    # J(t0) = (5*t0-2*pi)^2 - 20*(2*t0-pi) - 2*Delta.
    j_a_hi = 5 * t0_hi - 2 * pi_lo
    j_b_lo = 2 * t0_lo - pi_hi
    j_upper = j_a_hi * j_a_hi - 20 * j_b_lo - 2 * delta_lo
    assert j_upper < F(-515, 100)

    # H_{t*}(a(t*)) is bounded above by replacing positive terms by upper
    # endpoints and negative terms by lower endpoints.
    h_square_hi = tstar_hi / 2 + c_hi
    h_upper = (
        h_square_hi * h_square_hi
        - 10 * c_lo
        + 5 * tstar_hi
        - 2 * delta_lo
    )
    assert h_upper < F(-56, 100)

    print(f"tstar_interval=({float(tstar_lo):.13f},{float(tstar_hi):.13f})")
    print(f"t0_interval=({float(t0_lo):.13f},{float(t0_hi):.13f})")
    print(f"J(t0)_upper={float(j_upper):.6f}")
    print(f"H_tstar_a_upper={float(h_upper):.6f}")
    print("fan/train/hull scalar-floor arithmetic provenance: OK; density claim retracted")


if __name__ == "__main__":
    main()
