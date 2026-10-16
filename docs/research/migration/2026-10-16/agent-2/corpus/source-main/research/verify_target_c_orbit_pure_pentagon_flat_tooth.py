#!/usr/bin/env python3
from itertools import product
from decimal import Decimal, getcontext

getcontext().prec = 60
D = Decimal

# Exact integer classification.  With omega^2=omega-1, closure is equivalent to
# (n0-n3,n1-n4,n2-n5)=(a,-a,a).  Enumerate only as a regression check.
solutions = []
for n in product(range(6), repeat=6):
    if sum(n) != 5:
        continue
    a0 = n[0] - n[3]
    a1 = n[1] - n[4]
    a2 = n[2] - n[5]
    if a0 == a2 and a1 == -a2:
        solutions.append(n)

expected = {
    (2, 0, 1, 1, 1, 0),
    (0, 2, 0, 1, 1, 1),
    (1, 0, 2, 0, 1, 1),
    (1, 1, 0, 2, 0, 1),
    (1, 1, 1, 0, 2, 0),
    (0, 1, 1, 1, 0, 2),
}
assert set(solutions) == expected

# Current structural population arithmetic, copied from the independently certified
# bounded-endpoint theorem with conservative outward rounding.
pure_floor = D('0.4106157004282432')
face_matching_floor = pure_floor / D(21)
hidden_pair_floor = D(2) * face_matching_floor

assert face_matching_floor > D('0.0195531')
assert hidden_pair_floor > D('0.0391062')

print('directed count solutions =', sorted(solutions))
print('vertex-disjoint pentagon floor =', face_matching_floor)
print('endpoint-disjoint hidden-pair floor =', hidden_pair_floor)
print('PASS: orbit-pure pentagon flat-tooth classification')
