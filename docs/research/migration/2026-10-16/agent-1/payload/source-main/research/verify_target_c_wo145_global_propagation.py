#!/usr/bin/env python3
"""Outward rational certificate for WO145 propagation through audited Section 171."""
from fractions import Fraction as F


def dec(s: str) -> F:
    neg=s.startswith('-')
    if neg:
        s=s[1:]
    if '.' in s:
        a,b=s.split('.',1)
    else:
        a,b=s,''
    x=F(int((a or '0')+b),10**len(b))
    return -x if neg else x

PI_LO=dec('3.14159265358979323846264338327950288419716939937510')
PI_HI=PI_LO+F(1,10**50)
SQ3_LO=dec('1.73205080756887729352744634150587236694280525381038')
SQ3_HI=SQ3_LO+F(1,10**50)
assert SQ3_LO*SQ3_LO<3<SQ3_HI*SQ3_HI
DELTA_LO=PI_LO/(2*SQ3_HI)
DELTA_HI=PI_HI/(2*SQ3_LO)
S_LO=dec('0.9523128068')
S_HI=dec('0.9523128069')
assert S_LO*S_LO<DELTA_LO
assert S_HI*S_HI>DELTA_HI

G=dec('0.00145')
EPS=dec('0.0015914')
D0=(F(9,2)*EPS-G)/2
assert D0==dec('0.00285565')

C146_LO=F(4,9)*(PI_LO+S_LO)
C146_HI=F(4,9)*(PI_HI+S_HI)
T0_LO=C146_LO+EPS
T0_HI=C146_HI+EPS
B_HI=10*T0_HI-5*PI_LO-5*D0

K_RAD_HI=81*(PI_HI+D0)**2*D0
K_HI=dec('1.31753')
assert K_HI**3>K_RAD_HI

# At the right endpoint, the Section-171 denominator is exactly 2*s_2+g.
RHS_LO=8*S_LO*S_LO/(2*S_LO+G)
MARGIN=RHS_LO-(B_HI+K_HI)
assert MARGIN>dec('0.000015')

# Uniform positive delta derivative on the feasible interval.
C81_LO=dec('4.326')
ROOT_PI_D_HI=dec('1.466')
ROOT_D_HI=dec('0.143')
assert C81_LO**3<81
assert ROOT_PI_D_HI**3>PI_HI+D0
assert ROOT_D_HI**3>D0
KPRIME_LO=(C81_LO/3)*dec('3.1415')/ROOT_PI_D_HI/(ROOT_D_HI**2)
NEG_HI=16*dec('0.907')/(dec('1.905')**2)
DERIV_LO=KPRIME_LO-5-NEG_HI
assert DERIV_LO>dec('142')

print('PASS: WO145 -> Section 171 exact endpoint certificate')
print('delta145 =',float(D0))
print('t145 bracket =',float(T0_LO),float(T0_HI))
print('endpoint negativity margin >',float(MARGIN))
print('delta derivative lower >',float(DERIV_LO))
print('safe q-k floor >',float(T0_LO))
