#!/usr/bin/env python3
"""Arithmetic regression for the global flat-center stress trichotomy."""
from decimal import Decimal, getcontext
from math import pi, sin

getcontext().prec = 70
D = Decimal
piD = D('3.14159265358979323846264338327950288419716939937510')
sqrt3 = D(3).sqrt()
Delta2 = piD / (D(2) * sqrt3)
r = Delta2.sqrt()
C0 = D(2) * r + D('0.00042')
C146 = D(4) / D(9) * (piD + r)
t42 = C146 + D('0.0013751')

def P(t):
    return piD + C0 - D(5) * t / D(2)

p42 = P(t42)
p18585 = P(D('1.8585'))
vals = {
    'p42': p42,
    'loaded42': p42 / D(3),
    'hidden42': D(2) * p42 / D(27),
    'stress_edges42': p42 / D(6),
    'p18585': p18585,
    'loaded18585': p18585 / D(3),
    'hidden18585': D(2) * p18585 / D(27),
    'stress_edges18585': p18585 / D(6),
}

assert D('0.1648055574') < vals['loaded42'] < D('0.1648055575')
assert D('0.0366234572') < vals['hidden42'] < D('0.0366234573')
assert D('0.0824027787') < vals['stress_edges42'] < D('0.0824027788')
assert D('0.1334627557') < vals['loaded18585'] < D('0.1334627559')
assert D('0.0296583901') < vals['hidden18585'] < D('0.0296583903')
assert D('0.0667313778') < vals['stress_edges18585'] < D('0.0667313780')

# Local loaded-center obstruction: once the face sector occupies pi-epsilon
# inside an extreme-vertex hull wedge of width <pi, any third contact would
# lie within epsilon of one boundary ray, contradicting >pi/3 separation.
for eps in (1e-6, 1e-4, 1e-2, 0.1):
    assert eps < pi / 3
    hull_width_upper = pi
    face_width_lower = pi - eps
    leftover_upper = hull_width_upper - face_width_lower
    # Algebraically this quantity is exactly eps. Avoid a brittle <= check after
    # subtracting two nearly equal binary floats.
    assert abs(leftover_upper - eps) < 1e-12
    assert leftover_upper < pi / 3

    # Degree-three stress ratio tends to zero.
    ratio = sin(eps) / sin(pi / 3 - eps)
    assert ratio > 0
    assert ratio < 2 * eps

print('PASS global flat-center stress trichotomy arithmetic')
for key, value in vals.items():
    print(f'{key}={value}')
