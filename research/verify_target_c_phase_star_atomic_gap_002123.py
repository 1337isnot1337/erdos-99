#!/usr/bin/env python3
from fractions import Fraction as F
from math import isqrt

def dec(s):
    neg=s.startswith('-')
    if neg:s=s[1:]
    if '.' in s:a,b=s.split('.',1)
    else:a,b=s,''
    x=F(int((a or '0')+b),10**len(b))
    return -x if neg else x

def sqrt_bounds(lo,hi,digits=45):
    scale=10**digits
    q=(lo.numerator*scale*scale)//lo.denominator
    r=isqrt(q); slo=F(r,scale)
    assert slo*slo<=lo
    num=hi.numerator*scale*scale
    q=(num+hi.denominator-1)//hi.denominator
    r=isqrt(q)
    if r*r*hi.denominator<num:r+=1
    shi=F(r,scale); assert shi*shi>=hi
    return slo,shi

def sqrt_upper(x,digits=40):
    scale=10**digits
    num=x.numerator*scale*scale
    q=(num+x.denominator-1)//x.denominator
    r=isqrt(q)
    if r*r*x.denominator<num:r+=1
    out=F(r,scale); assert out*out>=x
    return out

PI_LO=dec('3.141592653589793238462643383279502884197169399375105820974944')
PI_HI=PI_LO+F(1,10**60)
SQ3_LO=dec('1.732050807568877293527446341505872366942805253810380628055806')
SQ3_HI=SQ3_LO+F(1,10**60)
assert SQ3_LO*SQ3_LO<3<SQ3_HI*SQ3_HI
DELTA_LO=PI_LO/(2*SQ3_HI); DELTA_HI=PI_HI/(2*SQ3_LO)
S_LO,S_HI=sqrt_bounds(DELTA_LO,DELTA_HI)
G=dec('0.002123')
W_LO=4*S_LO*S_LO/(2*S_LO+G)
A_HI=2*S_HI+G
d_HI=S_HI*G+G*G/4
CAP_HI=2/SQ3_LO; CAP_LO=2/SQ3_HI
Z=dec('0.045'); STEP=dec('0.000005')
assert Z*Z>d_HI
C_MIN=W_LO/2-Z; C_MAX=A_HI/2+Z
assert C_MAX<CAP_LO
P_MAX=(A_HI-CAP_LO)/6
assert C_MIN>5*P_MAX
best=None;arg=None;count=0;x=-Z
while x<Z:
    y=min(x+STEP,Z)
    raw=3*W_LO/4+x/2
    if x<=0<=y:h=d_HI
    elif y<0:h=d_HI-y*y
    else:h=d_HI-x*x
    if h<0:h=F(0)
    if x<0:
        den=W_LO+6*x; assert den>0
        R=(W_LO+2*x)/den
        if R<1:R=F(1)
    else:R=F(1)
    loss=6*sqrt_upper(h*R)
    lb=raw-loss
    if best is None or lb<best:best=lb;arg=(x,y,h,R,loss)
    count+=1;x=y
margin=best-CAP_HI
assert margin>dec('0.000010')
print('PASS minimax phase-star atomic gap g=0.002123')
print('intervals=',count)
print('s bracket=',float(S_LO),float(S_HI))
print('W_lower=',float(W_LO),'d_upper=',float(d_HI))
print('C_min=',float(C_MIN),'C_max=',float(C_MAX),'selected_p_upper=',float(P_MAX))
print('best_leaf_lower=',float(best),'cap_upper=',float(CAP_HI))
print('margin_lower=',float(margin),'worst=',tuple(float(v) for v in arg))
