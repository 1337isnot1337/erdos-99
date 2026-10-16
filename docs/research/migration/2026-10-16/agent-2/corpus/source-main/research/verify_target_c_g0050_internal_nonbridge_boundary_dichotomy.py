#!/usr/bin/env python3
from decimal import Decimal as D, getcontext
getcontext().prec=80
pi=D('3.14159265358979323846264338327950288419716939937510')
s2=D(2).sqrt(); s3=D(3).sqrt(); s=(pi/(D(2)*s3)).sqrt()
C146=D(4)/D(9)*(pi+s); g=D('0.005'); eps=D('0.0023374'); t=C146+eps
R=D('4.5')*eps-g; delta=R/D(2); C0=D(2)*s+g
B=(D(5)*pi+D(2)*C0-D(10)*t)/D(3)
assert R==D('0.00551830') and delta==D('0.00275915')

eta15=D(1)/D(15)
Eint15=B-delta/eta15
assert Eint15>D('0.39484778')
Y15=(D(29)*s3-D(59).sqrt())/D(60)
assert Y15>D('0.70913879')
eta=D('0.06')
Eint06=B-delta/eta
Y06=s3/D(2)*(D(1)-eta/D(2))-D(1)/D(2)*(eta-eta*eta/D(4)).sqrt()
flux=Eint06*Y06
assert Eint06>D('0.39024920') and flux>D('0.28039100')

cos8=(D(2)+s2).sqrt()/D(2)
Enb8=B-delta/(D(1)-cos8)-delta
assert Enb8>D('0.39722873')
cos6=s3/D(2)
Enb6=B-delta/(D(1)-cos6)-delta
assert Enb6>D('0.41288131')
assert min(Eint15,Enb8)==Eint15

print('PASS g=0.0050 internal/nonbridge boundary dichotomy')
for k,v in [('B50',B),('delta50',delta),('Eint_1_15',Eint15),('Eint_0_06',Eint06),('inward_flux_0_06',flux),('Enb_pi_8',Enb8),('Enb_pi_6',Enb6),('uniform_floor',min(Eint15,Enb8))]: print(k,'=',v)
