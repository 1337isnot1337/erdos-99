#!/usr/bin/env python3
from fractions import Fraction as F

def dec(s):
    neg=s.startswith('-')
    if neg:s=s[1:]
    if '.' in s:a,b=s.split('.',1)
    else:a,b=s,''
    x=F(int((a or '0')+b),10**len(b))
    return -x if neg else x
PI_LO=dec('3.14159265358979323846264338327950288419716939937510')
PI_HI=PI_LO+F(1,10**50)
SQ3_LO=dec('1.73205080756887729352744634150587236694280525381038')
SQ3_HI=SQ3_LO+F(1,10**50)
assert SQ3_LO*SQ3_LO<3<SQ3_HI*SQ3_HI
DELTA_LO=PI_LO/(2*SQ3_HI); DELTA_HI=PI_HI/(2*SQ3_LO)
S_LO=dec('0.9523128068639573458338104262565569008230510')
S_HI=dec('0.9523128068639573458338104262565569008230511')
assert S_LO*S_LO<DELTA_LO and S_HI*S_HI>DELTA_HI
G=dec('0.002123'); EPS=dec('0.0017327')
D0=(F(9,2)*EPS-G)/2
assert D0==dec('0.002837075')
C146_LO=F(4,9)*(PI_LO+S_LO); C146_HI=F(4,9)*(PI_HI+S_HI)
T0_LO=C146_LO+EPS; T0_HI=C146_HI+EPS
B_HI=10*T0_HI-5*PI_LO-5*D0
K_RAD_HI=81*(PI_HI+D0)**2*D0
K_HI=dec('1.31466'); assert K_HI**3>K_RAD_HI
RHS_LO=8*S_LO*S_LO/(2*S_LO+G)
MARGIN=RHS_LO-(B_HI+K_HI)
assert MARGIN>dec('0.00003')
C81_LO=dec('4.326'); ROOT_PI_D_HI=dec('1.466'); ROOT_D_HI=dec('0.143')
assert C81_LO**3<81 and ROOT_PI_D_HI**3>PI_HI+D0 and ROOT_D_HI**3>D0
KPRIME_LO=(C81_LO/3)*dec('3.1415')/ROOT_PI_D_HI/(ROOT_D_HI**2)
NEG_HI=16*dec('0.907')/(dec('1.906')**2)
DERIV_LO=KPRIME_LO-5-NEG_HI
assert DERIV_LO>dec('142')
print('PASS g=0.002123 -> Section 171 eps=0.0017327')
print('delta_endpoint=',float(D0))
print('t0_bracket=',float(T0_LO),float(T0_HI))
print('B_upper=',float(B_HI),'cube_upper=',float(K_HI),'response_lower=',float(RHS_LO))
print('endpoint_negativity_margin=',float(MARGIN))
print('delta_derivative_lower=',float(DERIV_LO))
