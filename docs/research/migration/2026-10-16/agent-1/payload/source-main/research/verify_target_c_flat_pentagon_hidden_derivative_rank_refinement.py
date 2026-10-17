#!/usr/bin/env python3
from decimal import Decimal, getcontext
getcontext().prec=80
D=Decimal
pi=D('3.14159265358979323846264338327950288419716939937510')
s=(pi/(D(2)*D(3).sqrt())).sqrt()
g=D('0.002123'); C0=D(2)*s+g
C146=D(4)/D(9)*(pi+s); t=C146+D('0.0017327')
P=pi+C0-D(5)*t/D(2)
X=D(9)*t/D(4)-pi-C0/D(2)
Rnew=P/D(3)-D(2)*X
expanded=D(7)*pi/D(3)+D(4)*C0/D(3)-D(16)*t/D(3)
Rold=D(7)*P/D(3)-D(2)*(D(2)*t-pi)
root=(D(7)*pi+D(4)*C0)/D(16)
assert abs(Rnew-expanded)<D('1e-70')
assert D('0.15940107')<Rnew<D('0.15940108')
assert abs((Rnew-Rold)-D(2)*X)<D('1e-70')
assert D('0.00567414')<Rnew-Rold<D('0.00567416')
assert D('1.85113')<root<D('1.85114')
print('PASS refined hidden-derivative rank')
print('p_floor=',P,'X_cap=',X)
print('old_rank=',Rold,'new_rank=',Rnew,'gain=',Rnew-Rold)
print('positive_until=',root)
