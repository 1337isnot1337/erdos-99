#!/usr/bin/env python3
"""Exact certificate for the modern high-t full-core chamber-surplus floor.

Inputs:
  * hostile-audited full-core exclusion of t=(q-k)/D <= 1.844;
  * scope-safe matched all-train gap g=0.007707:
      liminf (T-q/2)/D >= 2*sqrt(Delta_2)+g;
  * canonical difference-body terminal floor q/D >= 2*rho-o(1),
    where rho is the positive root rho=cos(rho);
  * canonical R4/D^2 -> Delta_2=pi/(2*sqrt(3));
  * exact tau_D=T-2*sqrt(R4);
  * exact Section-85 chamber identity/inequality
      H=(b-p)+(Q+2f)=(q-k)+tau_D-p+2*sqrt(R4),
      A_ch-a0*Z_ch >= (sqrt(3)/4)*H.

The script proves the safe coefficient 0.586223 using only Fraction arithmetic,
rational pi/sqrt(3) enclosures, an integer-square-root enclosure, and an alternating
cosine-series lower bound for rho.
"""
from fractions import Fraction as Q
from math import factorial, isqrt

T0 = Q(461, 250)          # 1.844
g = Q(7707, 10**6)       # modern scope-safe matched all-train gap

# Rational enclosures for pi and sqrt(3).
pi_lo = Q(103993, 33102)
pi_up = Q(104348, 33215)
s3_lo = Q(1732050807, 10**9)
s3_up = Q(1732050808, 10**9)
assert s3_lo * s3_lo < 3 < s3_up * s3_up

# Lower bound Delta_2=pi/(2sqrt(3)), then lower bound sqrt(Delta_2).
Delta_lo = pi_lo / (2 * s3_up)
S = 10**12
root = isqrt((Delta_lo.numerator * S * S) // Delta_lo.denominator)
sqrtDelta_lo = Q(root, S)
assert sqrtDelta_lo * sqrtDelta_lo <= Delta_lo

# rho is the positive fixed point rho=cos(rho).  Prove rho>0.7390851.
rho_lo = Q(7390851, 10**7)
cos_lo = sum(
    (-1) ** k * rho_lo ** (2 * k) / factorial(2 * k)
    for k in range(8)
)
# The k=7 term is negative, so this alternating partial sum is below cos(rho_lo).
assert cos_lo > rho_lo
# x -> cos(x)-x is strictly decreasing on x>=0, hence its zero rho exceeds rho_lo.

# tau_D/D >= rho+g-o(1).
tau_lo = rho_lo + g
assert tau_lo > Q(746792, 10**6)

# H_D/D >= 1.844 + tau_floor - pi + 2*sqrt(Delta_2).
# Round every term in the adverse direction.
H_lo = T0 + tau_lo - pi_up + 2 * sqrtDelta_lo
assert H_lo > Q(1353825, 10**6)

# A_ch-a0 Z_ch >= c0 H with c0=sqrt(3)/4.
chamber_lo = (s3_lo / 4) * H_lo
SAFE = Q(586223, 10**6)
assert chamber_lo > SAFE
assert chamber_lo - SAFE > Q(4, 10**7)

# Consequent positive-core second-order floor:
# m-R4=(p+H)/2+1=(q-k+tau_D+2sqrt(R4))/2+1.
pop_lo = (T0 + tau_lo + 2 * sqrtDelta_lo) / 2
assert pop_lo > Q(2247708, 10**6)

print("PASS modern high-t chamber-surplus certificate")
print("rho lower =", float(rho_lo))
print("cos lower - rho lower =", float(cos_lo - rho_lo))
print("tau/D lower =", float(tau_lo))
print("Delta2 lower =", float(Delta_lo))
print("sqrt(Delta2) lower =", float(sqrtDelta_lo))
print("H_D/D lower =", float(H_lo))
print("chamber-surplus coefficient lower =", float(chamber_lo))
print("safe chamber coefficient =", float(SAFE))
print("chamber margin =", float(chamber_lo - SAFE))
print("(m-R4)/D lower =", float(pop_lo))
print("CONCLUSION: remaining full-core Type-II survivors force")
print("  tau_D/D >= 0.7467921-o(1),")
print("  H_D/D >= 1.353825-o(1),")
print("  (A_ch-a0 Z_ch)/D >= 0.586223-o(1).")
