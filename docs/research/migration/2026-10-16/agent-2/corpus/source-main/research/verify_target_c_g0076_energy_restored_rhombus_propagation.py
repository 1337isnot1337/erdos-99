#!/usr/bin/env python3
"""High-precision certificate for g=0.0076 restored-rhombus propagation."""

from decimal import Decimal, getcontext

getcontext().prec = 110
D = Decimal

pi = D(
    "3.141592653589793238462643383279502884197169399375105820974944"
    "5923078164062862089986280348253421170679"
)


def sin_decimal(x: D) -> D:
    term = x
    total = x
    n = 1
    sign = -1
    while True:
        term = term * x * x / D((2 * n) * (2 * n + 1))
        old = total
        total = total - term if sign < 0 else total + term
        if total == old:
            return total
        sign *= -1
        n += 1
        assert n < 500


def cos_decimal(x: D) -> D:
    term = D(1)
    total = D(1)
    n = 1
    sign = -1
    while True:
        term = term * x * x / D((2 * n - 1) * (2 * n))
        old = total
        total = total - term if sign < 0 else total + term
        if total == old:
            return total
        sign *= -1
        n += 1
        assert n < 500


sqrt3 = D(3).sqrt()
Delta2 = pi / (D(2) * sqrt3)
s = Delta2.sqrt()
gap = D("0.0076")
C0 = D(2) * s + gap


def m2(U: D) -> D:
    return (U + (D(8) * Delta2 - U * U).sqrt()) / D(2)


def mprime(U: D) -> D:
    return (D(1) - U / (D(8) * Delta2 - U * U).sqrt()) / D(2)


def rfun(U: D) -> D:
    return U - m2(U)


def F(z: D) -> D:
    return z - D(6) * sin_decimal(z / D(6))


def Fprime(z: D) -> D:
    return D(1) - cos_decimal(z / D(6))


M0 = m2(C0)
r0 = rfun(C0)


def delta0(t: D) -> D:
    return (D("4.5") * t - D(2) * pi - C0) / D(2)


def S0(t: D) -> D:
    return pi - t / D(2) - r0


def zstar(t: D) -> D:
    d = delta0(t)
    s0 = S0(t)

    def equation(z: D) -> D:
        return z + (d - F(z) + r0 * r0) / (D(2) * (D(1) - d)) - s0

    lo = D(0)
    hi = pi
    assert equation(lo) < 0 < equation(hi)
    for _ in range(500):
        mid = (lo + hi) / D(2)
        if equation(mid) >= 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / D(2)


def margin(t: D) -> D:
    z = zstar(t)
    return F(z) - delta0(t)


# Uniform feasible-region bounds on 1.84323 <= t <= 1.84334.
t_max = D("1.84334")
U_max = D("4.5") * t_max - D(2) * pi
delta_max = (U_max - C0) / D(2)
r_max = rfun(U_max)
mp_min = mprime(U_max)

assert C0 < U_max < D("2.012")
assert D(0) < delta_max < D("0.050")
assert D("0.007") < r0 <= r_max < D("0.111")
assert D("-0.062") < mp_min < mprime(C0) < D(0)

GU_max = D("0.111") * D("1.062") / D("0.95")
Gz_min = D(1) - D("0.134") / (D(2) * D("0.95"))
Zdelta_max = (D(2) * D("1.062") + D(2) * GU_max) / Gz_min
Hdelta_upper = D("0.134") * Zdelta_max - D(1)

assert GU_max < D("0.125")
assert Gz_min > D("0.929")
assert Zdelta_max < D("2.56")
assert Hdelta_upper < D("-0.65")

safe_t = D("1.84332")
upper_t = D("1.84334")
safe_margin = margin(safe_t)
upper_margin = margin(upper_t)
assert safe_margin > D("0.000023")
assert upper_margin < D("-0.000023")

root_lo = D("1.84332993800832")
root_hi = D("1.84332993800833")
assert margin(root_lo) > 0
assert margin(root_hi) < 0

print("C0 =", C0)
print("M0 =", M0)
print("r0 =", r0)
print("U_max =", U_max)
print("delta_max =", delta_max)
print("r_max =", r_max)
print("mprime_min =", mp_min)
print("GU_max =", GU_max)
print("Gz_min =", Gz_min)
print("Zdelta_max =", Zdelta_max)
print("Hdelta_upper =", Hdelta_upper)
print("H(1.84332) =", safe_margin)
print("H(1.84334) =", upper_margin)
print("root bracket =", root_lo, root_hi)
print("H(root_lo) =", margin(root_lo))
print("H(root_hi) =", margin(root_hi))
print("PASS: g=0.0076 restored-rhombus propagation t >= 1.84332")
