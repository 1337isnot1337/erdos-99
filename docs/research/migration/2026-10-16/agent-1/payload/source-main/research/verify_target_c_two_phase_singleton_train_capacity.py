"""Certified scalar checks for the two-phase singleton-train capacity note.

The script checks only the displayed constants and a surviving normalized scalar
witness.  It does not certify phase concentration, the geometric variation theorem,
or global optimality.
"""

from fractions import Fraction as F


def main() -> None:
    pi_lo = F(3141592653589793, 10**15)
    pi_hi = F(3141592653589794, 10**15)
    sqrt3_lo = F(1732050807568877, 10**15)
    sqrt3_hi = F(1732050807568878, 10**15)

    delta_lo = pi_lo / (2 * sqrt3_hi)
    delta_hi = pi_hi / (2 * sqrt3_lo)
    sqrt_delta_lo = F(9523128, 10**7)
    sqrt_delta_hi = F(9523129, 10**7)
    assert sqrt_delta_lo * sqrt_delta_lo < delta_lo < delta_hi < sqrt_delta_hi * sqrt_delta_hi

    off_occ_lo = 4 - pi_hi
    train_floor_lo = 2 * sqrt_delta_lo + off_occ_lo / 2
    assert train_floor_lo > F(2333, 1000)

    defect_floor_lo = 4 * sqrt_delta_lo + 4 - 2 * pi_hi
    assert defect_floor_lo > F(1525, 1000)
    assert defect_floor_lo / 10 > F(152, 1000)

    # The slack-aware form is minimized at s=1 when x=b/D >= pi.
    # At x=pi+delta it loses exactly 2*delta.
    delta = F(1, 100)
    slack_floor = 4 * sqrt_delta_lo + 4 - 2 * (pi_hi + delta)
    assert slack_floor == defect_floor_lo - 2 * delta
    assert slack_floor > F(1325, 1000)

    # A current scalar witness survives this added conditional defect floor.
    t = F(29, 10)
    kappa = F(0)
    q = t + kappa
    Q = 2 * t - pi_lo
    f = F(2, 5)
    B = Q + 4 * f
    assert B > defect_floor_lo
    assert q < pi_lo
    assert Q > 0 and f < Q

    print("two-phase singleton-train capacity arithmetic: OK")
    print(f"defect_floor_lower_bound={float(defect_floor_lo):.12f}")
    print(f"surviving_witness_B_lower_bound={float(B):.12f}")


if __name__ == "__main__":
    main()
