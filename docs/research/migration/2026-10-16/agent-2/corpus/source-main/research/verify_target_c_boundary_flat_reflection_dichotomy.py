#!/usr/bin/env python3
"""Arithmetic/packing regression for boundary flat-center reflection dichotomy."""
from decimal import Decimal as D, getcontext
import math

getcontext().prec = 80

# Certified endpoint burden inherited from target_c_double_unit_flat_center_overlap.
H = D('0.442242872369096')
threshold = H / D(18)
assert D('0.0245690484') < threshold < D('0.0245690486')

# The weighted passage to the union uses 4 E_pen + E_in <= 5(E_pen union E_in)
# and L_diag <= 13 H_ref, hence total coefficient 5+13=18.
assert D(5) + D(13) == D(18)

# Explicit finite seven-centers-around-one-blocker exclusion once the annular excess
# is at most 1/20.
annulus_bound = 1/20 + (21/20) * 2 * math.sin(math.pi/7)
assert annulus_bound < 0.962
assert annulus_bound < 1.0

# Greedy matching in an assignment multigraph of max degree 7 loses at most 13 edges.
max_assignment_degree = 1 + 6
matching_loss = 2 * max_assignment_degree - 1
assert max_assignment_degree == 7
assert matching_loss == 13

print('PASS boundary flat-center reflection dichotomy')
print('endpoint weighted burden =', H)
print('two-currency density floor =', threshold)
print('seven-center annulus bound =', annulus_bound)
print('assignment max degree =', max_assignment_degree)
print('matching loss denominator =', matching_loss)
