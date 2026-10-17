#!/usr/bin/env python3
from decimal import Decimal, getcontext

getcontext().prec = 100

pi = Decimal('3.14159265358979323846264338327950288419716939937510')
sqrt2 = Decimal(2).sqrt()
sqrt3 = Decimal(3).sqrt()
sqrt6 = Decimal(6).sqrt()

Delta2 = pi / (Decimal(2) * sqrt3)
s = Delta2.sqrt()
C146 = Decimal(4) * (pi + s) / Decimal(9)
t = C146 + Decimal('0.0013751')
R = Decimal('0.00576795')

c15 = Decimal(1) - (sqrt6 + sqrt2) / Decimal(4)
A = Decimal(1) / c15 - Decimal(1)
S15 = pi - t - A * R / Decimal(2)

outer_repetition = Decimal('0.0459365399110338116')
Vsimple = S15 - outer_repetition

Tmax = Decimal(5) * t - Decimal(2) * pi
TRmin = Decimal(2) * s + Decimal('0.0004')
Ssingleton = Tmax - TRmin

ER = S15 - Ssingleton
ERsimple = Vsimple - Ssingleton
Mall = S15 / Decimal(2)
MR = ER / Decimal(2)
MRsimple = ERsimple / Decimal(2)
terminal_or_internal = ERsimple / Decimal(2)
terminal_train_floor = ERsimple / Decimal(4)
edge_floor_low_cubic = Decimal('1.5') * S15

assert A > Decimal(4)
assert S15 > Decimal('1.2389498413')
assert Vsimple > Decimal('1.1930133014')
assert Mall > Decimal('0.6194749206')
assert ER > Decimal('0.3227175723')
assert ERsimple > Decimal('0.2767810324')
assert MR > Decimal('0.1613587861')
assert MRsimple > Decimal('0.1383905162')
assert terminal_train_floor > Decimal('0.0691952581')
assert edge_floor_low_cubic > Decimal('1.8584247620')

print('t42 =', t)
print('R(t42) =', R)
print('c15 =', c15)
print('A = 1/c15 - 1 =', A)
print('convex S15/D >=', S15)
print('simple-outer S15/D >=', Vsimple)
print('singleton trains/D <=', Ssingleton)
print('rhombic-train penetration edges/D >=', ER)
print('simple rhombic-train penetration edges/D >=', ERsimple)
print('all penetration matching/D >=', Mall)
print('rhombic-train penetration matching/D >=', MR)
print('simple rhombic-train penetration matching/D >=', MRsimple)
print('terminal/internal edge floor/D >=', terminal_or_internal)
print('terminal-hit distinct train floor/D >=', terminal_train_floor)
print('edge floor in low-cubic half split/D >=', edge_floor_low_cubic)
print('PASS: convex-route degree/matching/train propagation constants')
