#!/usr/bin/env python3
"""Exact certificate: t<=1.8436 forces both leaf phases below .513D.

Together with the already-certified phasewise retained outer mass z_U,z_V>.616D,
this gives retained O-O pair weights P_U,P_V>.103D in both leaf phases.
"""

from fractions import Fraction as Q
from math import factorial, isqrt


def atan_inv_bounds(q, n):
    s = Q(0)
    for k in range(n):
        term = Q(1, (2 * k + 1) * q ** (2 * k + 1))
        s += term if k % 2 == 0 else -term
    nxt = Q(1, (2 * n + 1) * q ** (2 * n + 1))
    return (s, s + nxt) if n % 2 == 0 else (s - nxt, s)


def sqrt_bounds(lo, hi, scale):
    a = isqrt((lo.numerator * scale * scale) // lo.denominator)
    b = isqrt((hi.numerator * scale * scale) // hi.denominator) + 1
    return Q(a, scale), Q(b, scale)


def sin_bounds(x, n=26):
    s = Q(0)
    for k in range(n):
        term = x ** (2 * k + 1) / factorial(2 * k + 1)
        s += term if k % 2 == 0 else -term
    nxt = x ** (2 * n + 1) / factorial(2 * n + 1)
    return (s, s + nxt) if n % 2 == 0 else (s - nxt, s)


def F_lower(x):
    _, shi = sin_bounds(x / 6)
    return x - 6 * shi


SCALE = 10**100
a5_lo, a5_hi = atan_inv_bounds(5, 100)
a239_lo, a239_hi = atan_inv_bounds(239, 30)
pi_lo = 16 * a5_lo - 4 * a239_hi
pi_hi = 16 * a5_hi - 4 * a239_lo

n3 = isqrt(3 * SCALE * SCALE)
sqrt3_lo = Q(n3, SCALE)
sqrt3_hi = Q(n3 + 1, SCALE)
K_lo = Q(2) / sqrt3_hi
K_hi = Q(2) / sqrt3_lo
Delta_lo = pi_lo / (2 * sqrt3_hi)
Delta_hi = pi_hi / (2 * sqrt3_lo)
s_lo, s_hi = sqrt_bounds(Delta_lo, Delta_hi, SCALE)
C77_lo = 2 * s_lo + Q(77, 10000)
C77_hi = 2 * s_hi + Q(77, 10000)

# 1. Localize residual slack h=U_net-C77 at t<=1.8436.
T = Q(4609, 2500)  # 1.8436
c = Q(21, 20)
h0 = Q(13, 100000)  # .00013
Rt_hi = Q(9, 2) * T - 2 * pi_lo - C77_lo
delta_hi = (Rt_hi - h0) / 2
assert 0 < delta_hi < Q(51, 1000)
B_hi = c * c * h0 * h0 / (2 * (1 - delta_hi))
A_lo = pi_lo - T / 2 - c * h0 - B_hi
localization_margin = F_lower(A_lo) - delta_hi
assert localization_margin > Q(4, 1_000_000)

# The parent residual-coupled survivor capacity decreases in both h and x=kappa/2.
Fprime_cap = Q(67, 500)
Qh_upper = -1 / (2 * Fprime_cap) + c + c * c * Q(101, 1000) / (1 - Q(51, 1000))
Qx_upper = -1 / (2 * Fprime_cap) + 1
assert Qh_upper < Q(-5, 2)
assert Qx_upper < Q(-27, 10)

# 2. Consequent dominant-orbit mass/crossing box.
WBAR = Q(239057, 125000)  # 1.912456
assert C77_hi + h0 < WBAR
RMAX = c * h0
E0 = Q(90689967, 100000000)
assert Delta_lo - RMAX * RMAX / 4 > E0

# Existing t<=1.844 phase theorem: z_V>.616 and z_V<=2V, hence V>.308.
VMIN = Q(77, 250)  # .308
U0 = Q(513, 1000)
CLOW = WBAR - 2 * U0  # .886456
CHI = Q(261, 250)  # 1.044
alpha = Q(1, 10)
rcrit_lo, _ = sqrt_bounds(Q(20, 29), Q(20, 29), SCALE)

# C>=1.044 is already impossible by generic center capacity.
assert CHI * (WBAR - CHI) < E0

# C<=CLOW is impossible by the strong aggregate phase-star capacity.
def phi(C):
    q = 3 - WBAR / C
    r = (WBAR + C) / 2 - K_hi
    return C * (WBAR - C) - alpha * q * r * r


def phi_prime(C):
    r = (WBAR + C) / 2 - K_hi
    q = 3 - WBAR / C
    return WBAR - 2 * C - alpha * (WBAR * r * r / (C * C) + q * r)


assert phi_prime(CLOW) > 0
assert phi(CLOW) < E0 - Q(2, 1000)

# On [CLOW,CHI], the strong 1/10 branch is valid for U=.513;
# since C<K and V<=U, it is valid for the smaller leaf too.
ratio_hi = (CHI + U0 - K_lo) / U0
assert ratio_hi < rcrit_lo

# For fixed W,C the correlated strong capacity increases with W and decreases
# with the larger leaf U. Therefore the adverse point is W=WBAR,U=U0.
def cap(C):
    V = WBAR - C - U0
    A = 1 - V / C
    B = 1 - U0 / C
    x = alpha * (C + U0 - K_hi) ** 2
    y = alpha * (C + V - K_hi) ** 2
    return C * (U0 + V) - A * x - B * y


def cap_prime(C):
    V = WBAR - C - U0
    A = 1 - V / C
    B = 1 - U0 / C
    eU = C + U0 - K_hi
    eV = C + V - K_hi
    x = alpha * eU * eU
    y = alpha * eV * eV
    Ap = (WBAR - U0) / (C * C)
    Bp = U0 / (C * C)
    return WBAR - 2 * C - Ap * x - A * (2 * alpha * eU) - Bp * y


# cap''<-2 throughout. This gives a tangent upper bound for its unique maximum.
Dconst = (
    K_hi * K_hi * WBAR
    + 4 * K_hi * U0 * U0
    - 4 * K_hi * U0 * WBAR
    - U0 * U0 * WBAR
    + U0 * WBAR * WBAR
)
for C in (CLOW, Q(933067, 1000000), CHI):
    assert (1 + 2 * alpha) * C**3 - alpha * Dconst > C**3

c0 = Q(933067, 1000000)
assert CLOW < c0 < CHI
f0 = cap(c0)
fp0 = cap_prime(c0)
cap_upper = f0 + fp0 * fp0 / 4
assert cap_upper < E0 - Q(7, 1_000_000)

print("PASS t<=1.8436 two-leaf O-O localization")
print("h localization margin =", float(localization_margin))
print("W upper =", float(WBAR))
print("dominant crossing lower =", float(E0))
print("strong ratio upper =", float(ratio_hi))
print("rcrit lower =", float(rcrit_lo))
print("low-C aggregate margin =", float(E0 - phi(CLOW)))
print("cap(c0) =", float(f0))
print("cap'(c0) =", float(fp0))
print("capacity upper =", float(cap_upper))
print("capacity margin =", float(E0 - cap_upper))
print("CONCLUSION: U<0.513, V<=U; z_U,z_V>0.616 imply P_U,P_V>0.103")
