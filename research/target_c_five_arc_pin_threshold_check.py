from fractions import Fraction as F
from math import isqrt, pi, asin

# Exact rational sign checks for the delayed five-component attachment threshold.
# The adjacent report supplies the geometric proof. All asserted signs here use
# Fraction/integer arithmetic; floating-point values are diagnostic only.

PI_LO = F(6283, 2000)
PI_HI = F(3927, 1250)
SQRT3_HI = F(97, 56)
DEN = 10**12


def floor_sqrt_fraction(x: F, den: int = DEN) -> F:
    target = (x.numerator * den * den) // x.denominator
    k = isqrt(target)
    while F(k + 1, den) ** 2 <= x:
        k += 1
    while F(k, den) ** 2 > x:
        k -= 1
    return F(k, den)


def ceil_sqrt_fraction(x: F, den: int = DEN) -> F:
    lo = floor_sqrt_fraction(x, den)
    if lo * lo == x:
        return lo
    return lo + F(1, den)


def atan_lower(t: F, pairs: int = 10) -> F:
    out = F(0)
    for k in range(2 * pairs):
        term = t ** (2 * k + 1) / F(2 * k + 1)
        out += term if k % 2 == 0 else -term
    return out


def atan_upper(t: F, pairs: int = 10) -> F:
    out = F(0)
    for k in range(2 * pairs + 1):
        term = t ** (2 * k + 1) / F(2 * k + 1)
        out += term if k % 2 == 0 else -term
    return out


def pin_function_upper(z: F) -> F:
    # F5(z)=10 asin(z)-4pi-z/3 = pi-10 atan(sqrt(1-z^2)/z)-z/3.
    s_lo = floor_sqrt_fraction(1 - z * z)
    t_lo = s_lo / z
    return PI_HI - 10 * atan_lower(t_lo) - z / 3


def pin_function_lower(z: F) -> F:
    s_hi = ceil_sqrt_fraction(1 - z * z)
    t_hi = s_hi / z
    return PI_LO - 10 * atan_upper(t_hi) - z / 3


Z_LO = F(2401, 2500)  # 0.9604
Z_HI = F(961, 1000)   # 0.961

assert pin_function_upper(Z_LO) < 0
assert pin_function_lower(Z_HI) > 0

# At mu<z5*<0.961, JS gives C<=(2mu+pi)/4<17727/14000<51/40.
c_max = (2 * Z_HI + F(22, 7)) / 4
assert c_max == F(17727, 14000)
assert c_max < F(51, 40)

# For C<=51/40, prove the JS side-cost difference is minimized at C=0.
# With x=C^2/4<41/100,
#   (1-x)^(-1/2) <= 1+x/2+3x^2/5.
# Squaring reduces to -x^2(36x^3+24x^2+85x-45)/100 >=0;
# the cubic is increasing and negative at x=41/100.
x = F(41, 100)
poly = 36 * x**3 + 24 * x**2 + 85 * x - 45
assert poly == -F(908611, 250000)
assert poly < 0

C = F(51, 40)
phi_over_c2_upper = C / 6 + C**3 / 80 + 3 * C**5 / 1120
assert phi_over_c2_upper == F(28377658153, 114688000000)
assert F(49, 198) - phi_over_c2_upper == F(467842853, 11354112000000)
assert phi_over_c2_upper < F(49, 198)
assert F(49, 198) < F(7, 1) / (9 * PI_HI)

# Finally certify that even the relaxed three-arc + side/perimeter inequality
# is still contradictory at mu=0.961.  Write
# g=4pi/3-2asin(z)=pi/3+2atan(t).
z = Z_HI
s_lo = floor_sqrt_fraction(1 - z * z)
s_hi = ceil_sqrt_fraction(1 - z * z)
t_lo = s_lo / z
g_lo = PI_LO / 3 + 2 * atan_lower(t_lo)

# sin g=(sqrt(3)/2)(2z^2-1)+z sqrt(1-z^2).
sin_g_hi = SQRT3_HI / 2 * (2 * z * z - 1) + z * s_hi
w3_deficit_lo = F(3, 8) * (g_lo - sin_g_hi)
cavity_hi = (2 * z + PI_HI) ** 2 / (36 * PI_LO)
h0_lower = w3_deficit_lo - cavity_hi
assert h0_lower > 0

print("PASS: delayed five-arc pin threshold exact checks")
print("F5(0.9604) upper =", float(pin_function_upper(Z_LO)))
print("F5(0.961) lower =", float(pin_function_lower(Z_HI)))
print("side-cost C upper =", float(c_max))
print("three-arc/side contradiction margin at 0.961 =", float(h0_lower))

# Diagnostics only.
def f5_diag(z: float) -> float:
    return 10 * asin(z) - 4 * pi - z / 3

lo, hi = 0.9604, 0.961
for _ in range(100):
    mid = (lo + hi) / 2
    if f5_diag(mid) < 0:
        lo = mid
    else:
        hi = mid
print("diagnostic z5* =", (lo + hi) / 2)
