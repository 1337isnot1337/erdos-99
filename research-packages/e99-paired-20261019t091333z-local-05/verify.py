"""Exact finite scale checks; this does not verify the geometric theorem."""

from fractions import Fraction


def main() -> None:
    d0, a0 = 216, 24

    # 6 D^(2/3) <= D is equivalent, for D>0, to D >= 6^3.
    assert 216 == 6**3
    assert 216 > 215

    # The support energy coefficient is 8 + 1/2 = 17/2, with eta^2=sqrt(3)D.
    assert Fraction(8, 1) + Fraction(1, 2) == Fraction(17, 2)

    # For D>=216, eta>1, so a>=eta implies a+1<=2a.
    assert 216 > 1
    assert Fraction(216, 1) + 1 <= 2 * 216

    # Band midpoints: eta<=a gives sqrt(4a^2+eta^2)<=sqrt(5)a<3a.
    assert 4 + 1 < 3**2

    # Scaled windows: w=a/(2D)<=1/2 whenever a<=D. The two per-band
    # window-count coefficients from 2D*Lambda/a and Nc, with
    # Lambda<=4E/a^2 and Nc<=8DE/a^3, combine to 32 DE/a^2 after
    # multiplying by 2a points/window.
    assert a0 <= d0
    assert Fraction(a0, 2 * d0) <= Fraction(1, 2)
    assert 2 * (8 + 8) == 32

    # With fixed width 1/2, the component-start cost D*Nc divided by the
    # desired DE/a^2 scale carries the extra factor 8D/a. At D=216,a=24,
    # a>=eta and this factor is 72. The factor D/a is unbounded along a=eta.
    assert a0**4 >= 3 * d0**2  # a0^2 >= sqrt(3)*d0, hence a0 >= eta
    assert Fraction(d0, a0) == 9
    assert 8 * Fraction(d0, a0) == 72

    # For s>=4eta, s^2-eta^2 >= (15/16)s^2 >= s^2/4.
    assert Fraction(15, 16) >= Fraction(1, 4)

    # The integration upper radius exceeds 4eta at D=216; the ratio then
    # increases as D^(1/6). Raise positive terms to the fourth power.
    assert 7**4 * 6**2 > 4**4 * 3
    assert Fraction(2, 3) - Fraction(1, 2) == Fraction(1, 6)

    print("PASS: exact scale and coefficient controls only")
    print("LIMIT: no finite configuration or code checks the universal geometry")


main()
