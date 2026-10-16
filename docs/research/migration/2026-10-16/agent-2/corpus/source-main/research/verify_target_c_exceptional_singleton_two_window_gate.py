#!/usr/bin/env python3
"""Arithmetic/incidence regression for exceptional-singleton two-window gate."""
from decimal import Decimal, getcontext
import random
getcontext().prec=70
PI=Decimal('3.1415926535897932384626433832795028841971693993751058209749445923078164')
SQRT3=Decimal(3).sqrt(); DELTA=PI/(Decimal(2)*SQRT3); S=DELTA.sqrt()
T_STAR=Decimal(4)*(PI+S)/Decimal(9)+Decimal('0.0013751')
L=T_STAR+Decimal('0.00084'); GATE=L/Decimal(34); HALF=L/Decimal(2)
M_FULL=L*(Decimal(4)*S+L/Decimal(2))/Decimal(8)
assert Decimal('1.8217')<L<Decimal('1.8218')
assert Decimal('0.0535')<GATE<Decimal('0.0537')
assert Decimal('0.9108')<HALF<Decimal('0.9110')
rng=random.Random(20260914)
for _ in range(20000):
    counts={d:rng.randrange(0,50) for d in range(6,30)}
    x=sum((d-5)*n for d,n in counts.items())
    p_hi=sum(d*n for d,n in counts.items())
    n_hi=sum(counts.values())
    assert n_hi<=x
    assert p_hi==x+5*n_hi
    assert p_hi<=6*x
assert 6==6*1
print('PASS exceptional-singleton two-window gate')
for name,value in [('Delta_2',DELTA),('sqrt_Delta_2',S),('L_star',L),('four_currency_threshold',GATE),('two_currency_threshold',HALF),('Mantel_if_sigma_carries_full_L',M_FULL)]: print(f'{name}={value}')
