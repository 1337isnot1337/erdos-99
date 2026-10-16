#!/usr/bin/env python3
from decimal import Decimal, getcontext
getcontext().prec = 70
D=Decimal
PI=D('3.141592653589793238462643383279502884197169399375105820974944')
S=D('0.9523128068639573458338104262565569008230510550118582389446084732508783')
EPS=D('0.0017279'); ETA=D('0.005')
T0=D(4)/D(9)*(PI+S)+EPS
Q0=2*T0-PI
V=Q0-2*ETA
E=D('1.5')*Q0-9*ETA
D3=Q0-14*ETA
CYC=Q0/2-9*ETA
assert D('0.4908901') < V < D('0.4908903')
assert D('0.7063352') < E < D('0.7063355')
assert D('0.4308901') < D3 < D('0.4308903')
assert D('0.2054450') < CYC < D('0.2054452')
assert 2*E <= 3*Q0
print('PASS exact-two face-network arithmetic')
print('t21=',T0); print('q0=',Q0); print('eta=',ETA); print('exact_two_vertices_floor=',V); print('internal_edges_floor=',E); print('internal_degree_three_vertices_floor=',D3); print('cycle_rank_floor=',CYC)
