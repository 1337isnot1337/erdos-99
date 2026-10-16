#!/usr/bin/env python3
from math import pi, sqrt
from fractions import Fraction as F
from random import Random

rng=Random(749)
for _ in range(20000):
    t=F(rng.randrange(0,100),rng.randrange(1,9))
    f=F(rng.randrange(0,80),rng.randrange(1,9))
    PF=F(rng.randrange(0,200),rng.randrange(1,9))
    J=2*(t+2*f)-PF
    H=J-2*f
    assert H == J/2+t-PF/2

D2=pi/(2*sqrt(3)); s=sqrt(D2)
C146=4*(pi+s)/9
t=C146+0.0013751
C=2*s+0.00042
j=t+2*C-pi
h=j/2+t-pi/2
c0=sqrt(3)/4
print('PASS: exact H identity on 20,000 rational trials')
print(f'h_42={h:.15f}')
print(f'chamber coefficient={c0*h:.15f}')
print(f'rhombus deficit coefficient={h/2:.15f}')
