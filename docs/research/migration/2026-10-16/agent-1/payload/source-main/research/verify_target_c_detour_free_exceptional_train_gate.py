#!/usr/bin/env python3
from decimal import Decimal, getcontext

getcontext().prec = 70
D = Decimal
PI = D('3.141592653589793238462643383279502884197169399375105820974944')
SQ = D('0.9523128068639573458338104262565569008230510550118582389446084732508783')
GRID = D('0.00042')
CSTAR = 2*SQ + GRID
CDF = CSTAR/2 + D('0.00084') - PI/4
THREE = CDF / D(32)
SIGMA_SPLIT = CDF / 2
SE_SPLIT = CDF / 4
MANTEL = CDF/8 * (4*SQ + CDF/2)

assert CDF > D('0.16796464346650')
assert CDF < D('0.16796464346652')
assert THREE > D('0.00524889510832')
assert SIGMA_SPLIT > D('0.08398232173325')
assert SE_SPLIT > D('0.04199116086662')
assert MANTEL > D('0.08174069812767')

# Symbolic coefficient checks for the retained kappa term.
# AG42 face floor: phi >= C*/2 - t/4 + kappa/4.
# Exact outer ledger with X=Q-f: delta <= 9t/4 - p - C*/2 - kappa/4 - X/D.
# Train/bridge floor: sigma+2SE >= t+kappa+0.00084-delta, hence one +X/D survives.
# Hence before q<=p: coefficients are -5t/4 +5kappa/4.
assert D(1) - D(9)/4 == -D(5)/4
assert D(1) + D(1)/4 == D(5)/4
# Replacing t by p-kappa contributes another +5kappa/4.
assert D(5)/4 + D(5)/4 == D(5)/2
assert D(1) - D(5)/4 == -D(1)/4
assert -(-D(1)) == D(1)

print('PASS detour-free exceptional-train gate arithmetic')
print('C_star=', CSTAR)
print('c_DF=', CDF)
print('sigma_split=', SIGMA_SPLIT)
print('S_E_split=', SE_SPLIT)
print('three_currency_threshold_cDF_over_32=', THREE)
print('degree_excess_bonus_coefficient=', D(1))
print('Mantel_if_sigma_carries_c_DF=', MANTEL)
