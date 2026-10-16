#!/usr/bin/env python3
"""Arithmetic checks for dense anchored Groemer triple extraction."""

from decimal import Decimal, getcontext

getcontext().prec = 60
pi = Decimal('3.14159265358979323846264338327950288419716939937510')
sqrt3 = Decimal(3).sqrt()
delta2 = pi / (2 * sqrt3)
f_star = delta2.sqrt() - pi / 4 + Decimal('0.00021')
triple = f_star / 13
type_split = f_star / 26

assert Decimal('0.1671245') < f_star < Decimal('0.1671248')
assert Decimal('0.0128556') < triple < Decimal('0.0128559')
assert Decimal('0.0064277') < type_split < Decimal('0.0064281')

# A triangle-free unit-contact vertex has degree <=5. If at most five selected
# face-triples can contain one boundary vertex, a selected 3-vertex triple conflicts
# with at most 3*(5-1)=12 other triples.
max_contact_degree = 5
max_triple_conflict = 3 * (max_contact_degree - 1)
assert max_triple_conflict == 12
assert max_triple_conflict + 1 == 13

# ell_K/13 increases monotonically to f_star/13.
prev = Decimal('-1')
for K in range(23, 10000):
    ell = f_star - pi / Decimal(K - 3)
    coeff = ell / 13
    assert coeff > prev
    assert coeff < triple
    prev = coeff

print('f_* =', f_star)
print('anchored triple coefficient =', triple)
print('one-type coefficient =', type_split)
print('max triple conflict degree =', max_triple_conflict)
print('anchored Groemer triple extraction: PASS')
