#!/usr/bin/env python3
from decimal import Decimal as D, getcontext
getcontext().prec=90
pi=D('3.14159265358979323846264338327950288419716939937510')
s2=D(2).sqrt(); s3=D(3).sqrt(); s6=D(6).sqrt()
s=(pi/(D(2)*s3)).sqrt()
C146=D(4)/D(9)*(pi+s)
g=D('0.0050'); eps=D('0.0023374'); t=C146+eps
Cg=D(2)*s+g
# Use the algebraically exact cancellation form for the Section-171 remainder.
R=D('4.5')*eps-g
eta=D(17)/D(250)
Csrc=D(13)*pi+D(7)*Cg-D(29)*t+D('0.5')*(D(11)-D(1)/eta)*R
union=Csrc/D(4); branch=Csrc/D(5)
# Fixed-threshold compatibility.
eta_max=D(2)-(s6+s2)/D(2)
assert eta < D(1)/D(11)
assert eta < eta_max
assert R==D('0.00551830')
assert D('1.36418150') < Csrc < D('1.36418151')
assert union>D('0.34104537')
assert branch>D('0.27283630')
print('PASS matched loaded-slack externalization with penetration matching')
print('eta=',eta)
print('eta_locality_max=',eta_max)
print('t50=',t)
print('R50=',R)
print('Csrc=',Csrc)
print('disjoint_union_floor=',union)
print('two_way_branch_floor=',branch)
