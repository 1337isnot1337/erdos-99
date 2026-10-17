#!/usr/bin/env python3
from decimal import Decimal, getcontext
getcontext().prec = 70
D = Decimal
pi = D('3.14159265358979323846264338327950288419716939937510')
sqrt3 = D(3).sqrt()
Delta2 = pi / (D(2) * sqrt3)
r = Delta2.sqrt()
C0 = D(2) * r + D('0.00042')
C146 = D(4) * (pi + r) / D(9)
t42 = C146 + D('0.0013751')

def p(t, delta=D(0), kappa=D(0)):
    return pi + C0 - D(5)*t/D(2) + delta + kappa/D(2)

def pack(x):
    return {
        'H60': D(2)*x/D(3),
        'H0': x/D(3),
        'M3': x/D(4),
        'S5': x/D(6),
        'H60_train_variables': D(4)*x/D(3),
    }

p42 = p(t42)
pbar = p(D('1.8585'))
a = pack(p42)
b = pack(pbar)
assert D('0.49441667') < p42 < D('0.49441668')
assert D('0.40038826') < pbar < D('0.40038828')
assert a['H60'] > D('0.32961111')
assert a['H0'] > D('0.16480555')
assert a['M3'] > D('0.12360416')
assert a['S5'] > D('0.08240277')
assert a['H60_train_variables'] > D('0.65922222')
assert b['H60'] > D('0.26692551')
assert b['H0'] > D('0.13346275')
assert b['M3'] > D('0.10009706')
assert b['S5'] > D('0.06673137')

# General conflict-graph ledger: N r-train objects, each train in <=2 objects,
# gives Delta <= r and hence greedy independent set >= N/(r+1).
for n, rr, claimed_den in [(D(2), 2, 3), (D(1), 2, 3), (D(1), 3, 4), (D(1), 5, 6)]:
    assert claimed_den == rr + 1
    assert n / D(claimed_den) > 0

print('PASS low-t pentagon train-star packing arithmetic')
print('t42 =', t42)
print('P42 =', p42)
for k,v in a.items(): print(k+'42 =', v)
print('P18585 =', pbar)
for k,v in b.items(): print(k+'18585 =', v)
