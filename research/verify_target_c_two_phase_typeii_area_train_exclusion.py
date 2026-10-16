"""Exact arithmetic check for the retracted Type-II area/train note.

The reviewed draft incorrectly divided an O(D^2) face-area bound by D.  This
certificate checks the corrected scale distinction only; it does not certify any
geometric hypothesis or C-II consequence.
"""

from fractions import Fraction as F


def main() -> None:
    # A representative linear defect has a nonzero D-scale ratio but vanishing
    # D^2-scale ratio.  This is exactly why the corrected area inequality cannot
    # control f/D or Q/D.
    D = F(1000)
    f = F(30)
    Q = F(40)
    linear_scale = (2 * f + Q) / D
    area_scale = (2 * f + Q) / (D * D)
    assert linear_scale > 0
    assert area_scale < F(1, 100)
    assert area_scale < linear_scale

    print("two-phase Type-II area/train normalization retraction: PASS")
    print(f"linear_defect_scale={float(linear_scale):.6f}")
    print(f"area_defect_scale={float(area_scale):.9f}")


if __name__ == "__main__":
    main()
