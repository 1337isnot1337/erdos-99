#!/usr/bin/env python3
"""Exact certificate: the optimized t<=1.844 three-cut kernel has <1086 exceptional rows."""
from fractions import Fraction as Q
from math import factorial, isqrt


def atan_inv_bounds(q, n):
    s = Q(0)
    for k in range(n):
        term = Q(1, (2 * k + 1) * q ** (2 * k + 1))
        s += term if k % 2 == 0 else -term
    nxt = Q(1, (2 * n + 1) * q ** (2 * n + 1))
    return (s, s + nxt) if n % 2 == 0 else (s - nxt, s)


def sqrt_bounds(lo, hi, S):
    a = isqrt((lo.numerator * S * S) // lo.denominator)
    b = isqrt((hi.numerator * S * S) // hi.denominator) + 1
    return Q(a, S), Q(b, S)


def sin_bounds(x, n=30):
    s = Q(0)
    for k in range(n):
        term = x ** (2 * k + 1) / factorial(2 * k + 1)
        s += term if k % 2 == 0 else -term
    nxt = x ** (2 * n + 1) / factorial(2 * n + 1)
    return (s, s + nxt) if n % 2 == 0 else (s - nxt, s)


def F_lower(z):
    _, shi = sin_bounds(z / 6)
    return z - 6 * shi


# Standard exact outward constants.
S = 10 ** 100
a5l, a5h = atan_inv_bounds(5, 100)
a239l, a239h = atan_inv_bounds(239, 30)
pi_lo = 16 * a5l - 4 * a239h
pi_hi = 16 * a5h - 4 * a239l
n3 = isqrt(3 * S * S)
s3lo, s3hi = Q(n3, S), Q(n3 + 1, S)
Dlo, Dhi = pi_lo / (2 * s3hi), pi_hi / (2 * s3lo)
slo, shi = sqrt_bounds(Dlo, Dhi, S)
C707_lo = 2 * slo + Q(7707, 1_000_000)

# Current all-t<=1.844 defect ledger on main.
T = Q(461, 250)
Rt_hi = Q(9, 2) * T - 2 * pi_lo - C707_lo
Z = Q(22069, 10000)
delta_lo = F_lower(Z)
kappa_hi = 2 * (Rt_hi - 2 * delta_lo)
hdiam_hi = T + kappa_hi
switch_budget = 2 * hdiam_hi

assert kappa_hi < Q(73, 10000)
assert hdiam_hi < Q(18513, 10000)

# Count-optimized high-center path.
fan_avg = Q(1851, 2500)       # 0.7404
pair_weight = Q(53, 625)      # 0.0848
center_ceiling = Q(1063, 1000)
lam = Q(1601, 2500)           # 0.6404
d_low = Q(1, 10000)           # positive phase-charge reserve
r = (lam - d_low) / center_ceiling
d_top = lam - (1 - r) * center_ceiling
good = (fan_avg - lam) * pair_weight / (center_ceiling - lam)
path = d_top * good / (r * center_ceiling)

assert r > 0 and r < 1
assert d_top == Q(2177, 10000)
assert d_low > 0 and good > 0 and path > 0

# Two-boundary Pareto extraction.
N = Q(1086)
L = Q(100_000_000_000_000)
Cphase = Q(3258689123681, 612912000000)

# sum_i (N_i+N_{i+1}) <= 2 sum_i N_i
bad_count = 2 * switch_budget / N
# sum_i D(B_i+B_{i+1}) <= 4D
bad_beta = Q(4) / L
# sum_i D[(q_i+q_{i+1})+(q_{i+1}+q_{i+2})]
# <= 4 Cphase/d_low D
bad_phase = (4 * Cphase / d_low) / L
margin = path - bad_count - bad_beta - bad_phase

assert switch_budget / path < Q(543)
assert 2 * switch_budget / path < Q(1086)
assert margin > Q(3, 1_000_000)

print("PASS three-cut kernel exceptional count <1086+o(1)")
print("kappa upper =", float(kappa_hi))
print("diameter-edge density upper =", float(hdiam_hi))
print("single-boundary switch budget density =", float(switch_budget))
print("r =", float(r))
print("d_top =", float(d_top), "d_low =", float(d_low))
print("good leaf density =", float(good))
print("optimized path density =", float(path))
print("two-boundary count-only average =", float(2 * switch_budget / path))
print("bad count density at N=1086 =", float(bad_count))
print("bad beta density =", float(bad_beta))
print("bad phase density =", float(bad_phase))
print("Pareto density margin =", float(margin))
print(
    "CONCLUSION: eventually |H_exc|<=1085 and beta(H_exc), total adjacent "
    "phase variation <1e14/D+o(1/D)."
)
