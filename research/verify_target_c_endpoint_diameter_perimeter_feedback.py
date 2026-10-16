"""Certified rational checks for the endpoint diameter/perimeter feedback note."""

from fractions import Fraction
import math

# Conservative rational lower bounds: S0<S_* and pi lies in this interval.
S0 = Fraction(27985, 10000)       # 2.7985
PI_LO = Fraction(314159, 100000)  # 3.14159
PI_HI = Fraction(314160, 100000)  # 3.14160

# y = pi/2 - S0/2 is positive.  sin(y)>=y-y^3/6 certifies a lower bound for
# cos(S0/2)=sin(y), using only pi>PI_LO.
y = PI_LO / 2 - S0 / 2
sin_y_lo = y - y**3 / 6
P_lo = S0 + 2 * sin_y_lo
assert P_lo > Fraction(31399, 10000)  # P_*>3.1399
assert PI_HI - P_lo < Fraction(18, 10000)  # slack <0.0018

# sin(S0)=sin(pi-S0), with z=pi-S0.  The alternating lower bound certifies
# sin(z)>=z-z^3/6 for 0<z<1.
z = PI_LO - S0
sin_z_lo = z - z**3 / 6
A_lo = (S0 + sin_z_lo) / 4
assert A_lo > Fraction(7836, 10000)  # area floor >0.7836
assert PI_HI / 4 - A_lo < Fraction(18, 10000)  # area slack <0.0018

# Diagnostic values only; the certified inequalities above are the check.
S = float(S0)
P = S + 2 * math.cos(S / 2)
A = (S + math.sin(S)) / 4
print("endpoint diameter/perimeter feedback: rational certificate OK")
print(f"P_star_diagnostic={P:.15f}")
print(f"perimeter_slack_diagnostic={math.pi-P:.15f}")
print(f"area_floor_diagnostic={A:.15f}")
print(f"area_slack_diagnostic={math.pi/4-A:.15f}")
