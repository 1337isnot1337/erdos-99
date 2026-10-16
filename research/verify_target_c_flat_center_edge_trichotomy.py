#!/usr/bin/env python3
from decimal import Decimal, getcontext
getcontext().prec = 70
D = Decimal

V9 = D('0.494644672369096')
V42 = D('0.494416672369096169800871114085883591376359893413306676731324799299913')
V18585 = D('0.400388267317707930130264235792616685843271509398822298864161538809573')

for V in (V9, V42, V18585):
    assert V / D(6) > 0
    assert V / D(2) == D(3) * (V / D(6))

assert D('0.0824407') < V9 / D(6) < D('0.0824409')
assert D('0.2473222') < V9 / D(2) < D('0.2473224')
assert D('0.0667313') < V18585 / D(6) < D('0.0667315')
assert D('0.2001940') < V18585 / D(2) < D('0.2001943')

# 3 hidden-pair occurrences per degree-4 center, at most two centers per fixed pair.
for v4 in (D(1), D(17), D(1000)):
    assert D(3) * v4 / D(2) >= v4

print('PASS flat-center edge-level trichotomy arithmetic')
print('current V_flat/D >=', V9)
print('positive-diameter / weak-contact edge alternative >=', V9 / D(6))
print('degree-4 distinct hidden-pair alternative >=', V9 / D(2))
print('old g=.00042 V_flat/D =', V42)
print('t<=1.8585 edge alternative >=', V18585 / D(6))
print('t<=1.8585 hidden-pair alternative >=', V18585 / D(2))
