#!/usr/bin/env python3
"""Finite arithmetic/direction regression for the empty-pentagon trapezoid endpoint."""
from decimal import Decimal, getcontext
from itertools import product
getcontext().prec=70
pi=Decimal('3.141592653589793238462643383279502884197169399375105820974944592307816')
sqrt3=Decimal(3).sqrt()
Delta2=pi/(Decimal(2)*sqrt3)
f_star=Delta2.sqrt()-pi/Decimal(4)+Decimal('0.00021')
whole=f_star/Decimal(21)
kappa=Decimal(1)/sqrt3-Decimal(1)/Decimal(2)
sol=[]
for n in product(range(6), repeat=6):
    if sum(n)!=5:
        continue
    a=n[0]-n[3]; b=n[1]-n[4]; c=n[2]-n[5]
    if a==c and b==-c:
        sol.append(n)
base=(2,0,1,1,1,0)
rotations={tuple(base[(j-r)%6] for j in range(6)) for r in range(6)}
assert len(sol)==6 and set(sol)==rotations
for n in sol:
    assert sorted(n)==[0,0,1,1,1,2]
pts=[(Decimal(0),Decimal(0)),(Decimal(1),Decimal(0)),(Decimal(2),Decimal(0)),
     (Decimal(3)/2,sqrt3/2),(Decimal(1)/2,sqrt3/2)]
def d2(i,j):
    x=pts[i][0]-pts[j][0]; y=pts[i][1]-pts[j][1]
    return x*x+y*y
for i in range(5):
    assert abs(d2(i,(i+1)%5)-Decimal(1))<Decimal('1e-60')
assert abs(d2(1,3)-Decimal(1))<Decimal('1e-60')
assert abs(d2(1,4)-Decimal(1))<Decimal('1e-60')
assert d2(0,2)==Decimal(4)
assert Decimal('0.16712')<f_star<Decimal('0.16713')
assert Decimal('0.00795')<whole<Decimal('0.00797')
assert Decimal('0.0773')<kappa<Decimal('0.0774')
print('PASS empty-pentagon trapezoid endpoint regression')
print('direction_count_solutions=',sol)
print('f_star=',f_star)
print('vertex_disjoint_whole_pentagon_coefficient=',whole)
print('wegner_first_jump=',kappa)
