#!/usr/bin/env python3
"""Exact rational interval certificate for the AG47 chain-cover constants."""
from fractions import Fraction as F
from math import isqrt

SCALE=10**36
PI= (F(3141592653589793238462643383279502884, SCALE),
     F(3141592653589793238462643383279502885, SCALE))

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
        o=iv(o)
        assert o.lo>0
        return self*I(1/o.hi,1/o.lo)
    def __rtruediv__(self,o): return iv(o).__truediv__(self)

def iv(x): return x if isinstance(x,I) else I(x)

def sqrt_frac(x, digits=42):
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

def dec(x,n=15): return float(x)

pi=I(*PI)
s3=sqrt_i(I(3)); rt2=sqrt_i(I(2))
Delta=pi/(2*s3); s=sqrt_i(Delta)
eta=I(F(47,100000))
A=2*s+eta
M=4*s*s/A
R=A-M
d=A*A/4-s*s+R*R/4
assert d.lo>0
S0=M/2-sqrt_i(d)-sqrt_i(6*d)
p0=sqrt_i(2*d)
coeff=F(3,2)*S0-(4+rt2)*p0
proj=s3*coeff/2
margin=S0/2-(4+rt2)*p0

assert proj.lo>1
assert margin.lo>F(277,1000)

print('PASS: AG47 exact interval certificate')
print('projection lower =', float(proj.lo))
print('common-neighbor margin lower =', float(margin.lo))
print('M0 interval =', float(M.lo), float(M.hi))
print('d0 interval =', float(d.lo), float(d.hi))
print('S0 interval =', float(S0.lo), float(S0.hi))
print('p0 interval =', float(p0.lo), float(p0.hi))
