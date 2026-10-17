#!/usr/bin/env python3
import math
from decimal import Decimal, getcontext

getcontext().prec = 100

pi_d = Decimal('3.14159265358979323846264338327950288419716939937510')
sqrt3_d = Decimal(3).sqrt()
Delta2 = pi_d / (Decimal(2) * sqrt3_d)
s = Delta2.sqrt()
C146 = Decimal(4) * (pi_d + s) / Decimal(9)
t = C146 + Decimal('0.0013751')
R = Decimal('0.00576795')

# Transcendental window constants are evaluated in double precision only for the
# displayed numerical certificate. The theorem uses the exact fixed beta=pi/6-0.003.
eps = 0.003
beta = math.pi / 6 - eps
c = 1 - math.cos(beta)
A = 1 / c - 1
Socc = float(pi_d - t) - A * float(R) / 2

rep = 0.0459365399110338116
V = Socc - rep
Vsimple = Socc - 2 * rep

signed = math.sin(math.pi / 6 + eps)
route = math.sin(beta)
theta0 = 2 * math.asin(0.002883975 / 2)
cone_width = 2 * (math.pi / 3 - eps + theta0)

Ssingleton = 0.9162322689897223521
ER = V - Ssingleton
ERsimple = Vsimple - Ssingleton

assert A > 4
assert Socc > 1.3018186084
assert V > 1.2558820685
assert Vsimple > 1.2099455286
assert signed - route > theta0
assert eps > theta0
assert cone_width < 2 * math.pi / 3
assert V / 2 > 0.6279410342
assert ER > 0.3396497995
assert ER / 2 > 0.1698248997
assert ERsimple > 0.2937132596
assert ERsimple / 2 > 0.1468566298

print('beta =', beta, 'rad =', beta * 180 / math.pi, 'deg')
print('1/(1-cos beta)-1 =', A)
print('straight occurrences/D >=', Socc)
print('distinct straight tails/D >=', V)
print('simple-outer straight tails/D >=', Vsimple)
print('signed inward threshold >', signed)
print('route normal component <', route)
print('signed-route gap =', signed - route)
print('nearby-normal angle <=', theta0)
print('epsilon-normal margin =', eps - theta0)
print('endpoint cone width <=', cone_width)
print('2pi/3 =', 2 * math.pi / 3)
print('physical matching/D >=', V / 2)
print('train-supported edges/D >=', ER)
print('train-supported matching/D >=', ER / 2)
print('simple train-supported edges/D >=', ERsimple)
print('simple train-supported matching/D >=', ERsimple / 2)
print('PASS: near-30 convex-route penetration matching constants')
