#!/usr/bin/env python3
from decimal import Decimal as D, getcontext
getcontext().prec=80
pi=D('3.14159265358979323846264338327950288419716939937510')
s3=D(3).sqrt()
s=(pi/(D(2)*s3)).sqrt()
C146=D(4)/D(9)*(pi+s)
g=D('0.0050')
eps=D('0.0023374')
t=C146+eps
R=D('4.5')*eps-g
delta=R/D(2)
C0=D(2)*s+g
M=D(5)*pi+D(2)*C0-D(10)*t
B=M/D(3)
assert R==D('0.00551830')
assert delta==D('0.00275915')
assert D('0.4362350')<B<D('0.4362351')

eta15=D(1)/D(15)
E15=(B-delta/eta15)/D(2)
Y15=(D(29)*s3-D(59).sqrt())/D(60)
assert E15>D('0.19742389')
assert Y15>D('0.70913879')

eta=D('0.06')
Epen=(B-delta/eta)/D(2)
Y=s3/D(2)*(D(1)-eta/D(2))-D(1)/D(2)*(eta-eta*eta/D(4)).sqrt()
flux_pen=Epen*Y
assert Epen>D('0.19512460')
assert Y>D('0.71849218')
assert flux_pen>D('0.14019550')

bad=delta/(D(1)-s3/D(2))
Etan=(B-bad)/D(2)
flux_tan=Etan*s3/D(2)
assert Etan>D('0.20782023')
assert flux_tan>D('0.1799')

print('PASS g=0.0050 physical boundary propagation')
for k,v in [('t50',t),('R50',R),('delta50',delta),('B50',B),('Epen_1_15',E15),('Y_1_15',Y15),('Epen_0_06',Epen),('Y_0_06',Y),('inward_flux',flux_pen),('Etan_pi_6',Etan),('tangent_flux',flux_tan)]: print(k,'=',v)
