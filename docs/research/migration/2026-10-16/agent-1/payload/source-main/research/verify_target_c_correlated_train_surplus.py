#!/usr/bin/env python3
"""Arithmetic/bookkeeping regression for correlated stopped-train surplus."""
import math, random
from decimal import Decimal, getcontext
getcontext().prec=60
rho=Decimal('0.73908513321516064165531208767387340401341175890076')
pi=Decimal('3.14159265358979323846264338327950288419716939937510')
sqrt3=Decimal(3).sqrt(); delta2=pi/(2*sqrt3); s2=delta2.sqrt()
eta=Decimal('0.00042')
mu_tc=(2*pi+2*s2)/5
corr=2*rho+2*eta
branch=rho+eta
mu_floor=mu_tc+corr/10
large_mantel=branch*(4*s2+branch/2)/8
endpoint_defect=2*rho+(4*s2-pi)+2*eta
assert abs(Decimal(str(math.cos(float(rho))))-rho)<Decimal('1e-15')
assert Decimal('1.4790102')<corr<Decimal('1.4790104')
assert Decimal('1.7854631')<mu_floor<Decimal('1.7854634')
assert Decimal('0.38')<large_mantel<Decimal('0.40')
assert Decimal('2.1466687')<endpoint_defect<Decimal('2.1466690')
rng=random.Random(20260914)
for _ in range(20000):
    tr=rng.randint(1,1000); s=rng.randint(0,1000)
    r=rng.randint(1,max(1,tr*tr//4)); sr=Decimal(r).sqrt()
    rho_rec=Decimal(2*s); sigma=Decimal(2*tr)-4*sr
    tau=Decimal(tr+s)-2*sr
    assert abs(2*tau-rho_rec-sigma)<Decimal('1e-50')
print('rho =',rho)
print('Delta_2 =',delta2)
print('mu_TC =',mu_tc)
print('correlated currency / D =',corr)
print('max branch currency / D =',branch)
print('singleton count / D on singleton branch =',branch/2)
print('new mu floor =',mu_floor)
print('large-sigma Mantel deficit / D^2 =',large_mantel)
print('endpoint defect / D =',endpoint_defect)
print('correlated stopped-train surplus: PASS')
