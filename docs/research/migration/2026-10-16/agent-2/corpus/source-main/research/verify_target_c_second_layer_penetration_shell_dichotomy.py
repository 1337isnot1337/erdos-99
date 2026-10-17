#!/usr/bin/env python3
from decimal import Decimal as D, getcontext
getcontext().prec=80
Z=D('0.39484778853678284477696204486560321547013491766029891012046673705189129247516567')
s3=D(3).sqrt(); s59=D(59).sqrt(); lam=D(13)/D(25)
new_depth=s3/D(2)+lam
old_max=D(1)+s59/D(30)
margin=new_depth-old_max
floor=Z/D(4)
# 2 arccos(lambda) < 2pi/3 is equivalent, for lambda in (0,1), to lambda > 1/2.
assert lam>D(1)/D(2)
assert margin>D('0.129')
assert floor>D('0.09871194')
# Weak selected edge is within arcsin(lambda) of tangent; lambda=.52 gives <32 deg.
print('PASS second-layer penetration/internal-shell dichotomy')
print('lambda=',lam)
print('new_depth_floor=',new_depth)
print('old_layer_depth_ceiling=',old_max)
print('fixed_depth_margin=',margin)
print('uniform_second_layer_floor=',floor)
