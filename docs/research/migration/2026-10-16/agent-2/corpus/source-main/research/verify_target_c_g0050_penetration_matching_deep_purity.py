#!/usr/bin/env python3
from decimal import Decimal as D, getcontext
getcontext().prec=80
pi=D('3.14159265358979323846264338327950288419716939937510')
s3=D(3).sqrt(); s=(pi/(D(2)*s3)).sqrt()
C146=D(4)/D(9)*(pi+s); g=D('0.0050'); eps=D('0.0023374')
t=C146+eps; C=D(2)*s+g
R=D('4.5')*eps-g; delta=R/D(2)
B=(D(5)*pi+D(2)*C-D(10)*t)/D(3)
Z=B-D(15)*delta
assert R==D('0.00551830')
assert delta==D('0.00275915')
assert Z>D('0.39484778')
assert D(2)*Z>D('0.78969557')
assert D(4)*Z>D('1.57939115')
print('PASS matched g=0.0050 penetration matching')
print('matching=',Z)
print('endpoint_union=',D(2)*Z)
print('internal_edges_floor=',D(2)*Z)
print('attachment_edges_floor=',D(2)*Z)
print('combined_edge_floor=',D(4)*Z)
