#!/usr/bin/env python3
from fractions import Fraction as F

# Audited parent constants.
A = F(1851, 2500)       # 0.7404 weighted center-degree average
W = F(53, 625)          # 0.0848 retained leaf-pair weight density
N = F(1063, 1000)       # center-train count cap

# New exact selection parameters.
lam = F(6403, 10000)    # 0.6403
d_low = F(1, 100000)    # 1e-5
x = lam - d_low         # x = r*N
r = x / N

d_top = lam - (1-r) * N
g = (A-lam) * W / (N-lam)
p = d_top * g / (r*N)

assert x == F(64029, 100000)
assert r == F(64029, 106300)
assert d_top == F(21759, 100000)
assert d_low == F(1, 100000)
assert g == F(53053, 2641875)
assert p == F(54970487, 8055076875)

# Same outward enclosures used by the parent certificate stack.
pi_up = F(355, 113)
Cphase_up = F(3258689123681, 612912000000)

# Pareto thresholds. n<921 plus integrality gives N_i<=920 eventually.
n = F(3683, 4)          # 920.75
b = F(10**12, 1)
a = F(10**13, 1)

count_bad = 2*pi_up/n
beta_bad = F(2, 1)/b
phase_bad = 2*Cphase_up/(d_low*a)
total_bad = count_bad + beta_bad + phase_bad
gap = p-total_bad

assert total_bad < p
assert gap > F(2, 10**7)  # exact margin > 2e-7
assert n < 921

print('lambda =', lam, float(lam))
print('rN =', x, float(x))
print('r =', r, float(r))
print('d_top =', d_top, float(d_top))
print('d_low =', d_low, float(d_low))
print('good-leaf density g =', g, float(g))
print('path density p =', p, float(p))
print('count-bad density =', count_bad, float(count_bad))
print('multiplier-bad density =', beta_bad, float(beta_bad))
print('phase-bad density =', phase_bad, float(phase_bad))
print('total bad density =', total_bad, float(total_bad))
print('exact gap =', gap, float(gap))
print('PASS: one boundary has N_i<920.75+o(1), hence N_i<=920 for large D')
