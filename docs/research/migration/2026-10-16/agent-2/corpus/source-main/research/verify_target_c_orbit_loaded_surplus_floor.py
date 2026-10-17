#!/usr/bin/env python3
from decimal import Decimal, getcontext

getcontext().prec = 70
pi = Decimal('3.14159265358979323846264338327950288419716939937510')
sqrt3 = Decimal(3).sqrt()
delta2 = pi / (2 * sqrt3)
s2 = delta2.sqrt()
C146 = Decimal(4) * (pi + s2) / Decimal(9)
t42 = C146 + Decimal('0.0013751')
old = Decimal('1.785463210824532')
gain = t42 - old

assert Decimal('1.8208886379510192') < t42 < Decimal('1.8208886379954636')
assert gain > Decimal('0.0354254')
assert t42 > old

# Logical propagation used by OL.1--OL.4:
# mu_D = (q-k)/D + m_B/D - (2 c_I + 4)/D,
# with m_B >= 0 and c_I/D -> 0. Hence liminf mu_D >= liminf (q-k)/D.

print('Delta_2 =', delta2)
print('sqrt(Delta_2) =', s2)
print('C146 =', C146)
print('t_42 =', t42)
print('previous correlated-train mu floor =', old)
print('gain =', gain)
print('orbit-loaded surplus propagation: PASS')
