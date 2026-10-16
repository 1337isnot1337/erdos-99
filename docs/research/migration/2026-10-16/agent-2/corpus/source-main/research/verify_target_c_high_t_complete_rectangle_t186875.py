#!/usr/bin/env python3
"""Exact outward arithmetic for the high-t complete rectangle through t<=1.86875."""
from fractions import Fraction as Q

# Machin pi bounds, copied from the exact path verifier.
def atan_inv_bounds(q,n):
    s=Q(0)
    for k in range(n):
        term=Q(1,(2*k+1)*q**(2*k+1))
        s += term if k%2==0 else -term
    nxt=Q(1,(2*n+1)*q**(2*n+1))
    return (s,s+nxt) if n%2==0 else (s-nxt,s)

a5l,a5h=atan_inv_bounds(5,110)
a239l,a239h=atan_inv_bounds(239,35)
pil,pih=16*a5l-4*a239h,16*a5h-4*a239l

T=Q(299,160)
p=Q(1,20000)       # certified one-phase O-O path density
r=Q(6536,10000)     # safe crossing-degree density
n=9

# Total complete stopped trains: T_tr/D <= 5T-2pi.
ctr_hi=5*T-2*pil
assert ctr_hi<Q(30606,10000)

A=p/n
B=r-ctr_hi/n
assert A>Q(55,10_000_000)   # 0.0000055
assert B>Q(3135,10000)       # 0.3135

# After deleting O(1) orientation-ambiguous columns, one oriented side keeps half.
Bplus=B/2
assert Bplus>Q(1567,10000)

print('PASS complete high-t rectangle through t<=1.86875')
print('complete-train upper / D =',float(ctr_hi))
print('row-shore floor / D =',float(A))
print('column-shore floor / D =',float(B))
print('oriented column-shore floor / D =',float(Bplus))
