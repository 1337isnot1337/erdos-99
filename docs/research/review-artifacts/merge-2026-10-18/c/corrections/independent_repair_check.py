#!/usr/bin/env python3
"""Independent exact arithmetic review of PR93 repair and PR89 scope comparison.
No submitted module is imported. This does not audit GPI geometry.
"""
from fractions import Fraction as F
from decimal import Decimal, localcontext
import json


def demand(condition, message):
    if not condition: raise AssertionError(message)


def series(x,n):
    total=F(0)
    power=x
    for k in range(n):
        total += power/(2*k+1)
        power *= -x*x
    return total


def dec(x):
    with localcontext() as c:
        c.prec=50
        return str(Decimal(x.numerator)/Decimal(x.denominator))


def main():
    a,b=F(1,5),F(1,239)
    tan2a=2*a/(1-a*a)
    tan4a=2*tan2a/(1-tan2a*tan2a)
    demand((tan4a-b)/(1+tan4a*b)==1,"Machin exact tangent identity")
    # The integral remainder is (-1)^n integral_0^x t^(2n)/(1+t^2) dt.
    # Even n lower, odd n upper, strictly for x>0.
    lower=16*series(a,8)-4*series(b,3)
    upper=16*series(a,9)-4*series(b,4)
    tight_lower=16*series(a,16)-4*series(b,15)
    tight_upper=16*series(a,17)-4*series(b,16)
    old_false_lower=16*series(a,7)-4*series(b,2)
    demand(lower<tight_lower<tight_upper<upper<old_false_lower,"independent interval enclosure and old error")
    demand(upper-lower==16*a**17/17+4*b**7/7,"exact interval width")
    sqrt3u=F(1732051,10**6)
    sqrtmu=F(89443,10**7)
    mu=F(8,10**5)
    c=2*sqrt3u/lower
    gamma=F(3,4)-c/2
    loss=4*sqrt3u*(3*sqrtmu+mu)
    u=F(5,10**13);delta=F(4,10**17)
    deletion=2*u/(1-u)
    grid=6*F(1,1000)+4*F(1,10**6)
    diameter=3-4*sqrt3u*F(601,100000)-2*sqrt3u*F(3,10**12)-F(1,10**10)
    lattice=2*c/(1-u)**2
    margins={
      "pi_lower_minus_3.14159":lower-F(314159,100000),
      "sqrt3_upper_squared_minus_3":sqrt3u**2-3,
      "sqrt_mu0_upper_squared_minus_mu0":sqrtmu**2-mu,
      "0.1865_minus_unique_max_loss_upper":F(1865,10000)-loss,
      "gamma0_lower_minus_0.1865":gamma-F(1865,10000),
      "gamma0_lower_minus_0.198":gamma-F(198,1000),
      "6e-13_minus_u_plus_delta":F(6,10**13)-(u+delta),
      "1e-12_minus_balanced_deficit_cap":F(1,10**12)-(u+delta),
      "3e-12_minus_deletion_bound":F(3,10**12)-deletion,
      "0.00601_minus_grid_loss_cap":F(601,100000)-grid,
      "diameter_lower_minus_2.95":diameter-F(295,100),
      "2.21_minus_lattice_upper":F(221,100)-lattice,
    }
    demand(delta/mu==u,"contradiction coefficient quotient")
    demand(all(x>0 for x in margins.values()),"all rational margins strictly positive")
    # Distinct triangular-basis classes in the already merged package.
    for M in (5,6,20,32,100):
        deep={(i,j) for i in range(1,M) for j in range(1,M) if i+j<=M-1}
        omitted={(2,1)}|{(1,j) for j in range(2,M-1)}
        demand(omitted<=deep and len(omitted)==M-2,"relaxed witness omits required incidence-deep columns")
        raw_relaxed=(3*M+3)-(2*M+1)-3
        raw_admissible=raw_relaxed-(M+1-3)
        demand(raw_relaxed==M-1 and raw_admissible==1,"distinct basis-class optima ledger")
    for m in (2,3,10,32,100):
        demand((9*m+4)-(9*m-8)-9==3,"independent hexagonal disjoint partition cap")
        demand((6*m+3)-3==6*m,"deficiency gap arithmetic")
    print(json.dumps({"status":"PASS","Machin_interval":{"lower_fraction":str(lower),"upper_fraction":str(upper),"lower_decimal":dec(lower),"upper_decimal":dec(upper),"width_fraction":str(upper-lower),"width_decimal":dec(upper-lower),"old_false_lower_above_tight_upper":str(old_false_lower-tight_upper)},"strict_margin_decimal_displays":{k:dec(v) for k,v in margins.items()},"strict_margin_exact_fractions":{k:str(v) for k,v in margins.items()},"PR89_scope_check":"Section-102 optimum1; relaxed Z-perfect optimumM-1, missingM-2 deep columns; hexagonal bound<=3 is independent and not claimed sharp","scope":"PR93 repaired arithmetic only; PR89 part4 integration correction only"},indent=2))

if __name__=="__main__":main()
