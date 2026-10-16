#!/usr/bin/env python3
"""Exact rational interval certificate for the LB154 atomic-gap constants."""
from fractions import Fraction as F
from math import isqrt

SCALE=10**36
PI=(F(3141592653589793238462643383279502884,SCALE),
    F(3141592653589793238462643383279502885,SCALE))

class I:
    def __init__(self,lo,hi=None):
        self.lo=F(lo); self.hi=F(lo if hi is None else hi)
    def __add__(self,o):
        o=iv(o); return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __sub__(self,o):
        o=iv(o); return I(self.lo-o.hi,self.hi-o.lo)
    def __rsub__(self,o): return iv(o).__sub__(self)
    def __mul__(self,o):
        o=iv(o)
        vals=[self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi]
        return I(min(vals),max(vals))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=iv(o); assert o.lo>0
        return self*I(1/o.hi,1/o.lo)
    def __rtruediv__(self,o): return iv(o).__truediv__(self)

def iv(x): return x if isinstance(x,I) else I(x)

def sqrt_frac(x,digits=42):
    assert x>=0
    S=10**digits
    m=isqrt((x.numerator*S*S)//x.denominator)
    while F((m+1)*(m+1),S*S)<=x: m+=1
    while F(m*m,S*S)>x: m-=1
    return F(m,S),F(m+1,S)

def sqrt_i(x):
    lo,_=sqrt_frac(x.lo)
    _,hi=sqrt_frac(x.hi)
    return I(lo,hi)

pi=I(*PI)
s3=sqrt_i(I(3))
rt2=sqrt_i(I(2))
Delta=pi/(2*s3)
s=sqrt_i(Delta)
eta=I(F(154,100000))
Abar=2*s+eta
M0=4*s*s/Abar
R0=Abar-M0
d0=Abar*Abar/4-s*s+R0*R0/4
assert d0.lo>0
s0=M0/2-sqrt_i(d0)
K=2/s3
L=4+rt2
B=F(3,2)*s0-K
payment=2*B*B/(L*L+2)
budget=2*d0
margin=payment-budget
qmax=F(3,2)*sqrt_i(2*d0)
empty_cost=s0*s0/3

assert B.lo>0
assert s0.hi<K.lo
assert qmax.hi<s0.lo/3
assert empty_cost.lo>budget.hi
assert payment.lo>budget.hi
assert margin.lo>F(16,10**6)

print('PASS: LB154 exact interval certificate')
print('Abar interval =',float(Abar.lo),float(Abar.hi))
print('M0 interval =',float(M0.lo),float(M0.hi))
print('R0 interval =',float(R0.lo),float(R0.hi))
print('d0 interval =',float(d0.lo),float(d0.hi))
print('s0 interval =',float(s0.lo),float(s0.hi))
print('B interval =',float(B.lo),float(B.hi))
print('payment interval =',float(payment.lo),float(payment.hi))
print('budget interval =',float(budget.lo),float(budget.hi))
print('payment-budget lower =',float(margin.lo))
print('qmax interval =',float(qmax.lo),float(qmax.hi))
print('s0/3 interval =',float((s0/3).lo),float((s0/3).hi))
