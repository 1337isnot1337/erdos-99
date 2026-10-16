#!/usr/bin/env python3
"""Exact algebra check for the two rational rank-conditioned M secants."""
from fractions import Fraction as Q

# Work in Q(sqrt(5)): pairs (a,b) represent a+b*sqrt(5).
def sub(x, y):
    return (x[0] - y[0], x[1] - y[1])


# Standard regular-pentagon cosine values.
COS_PI_5 = (Q(1, 4), Q(1, 4))
COS_3PI_5 = (Q(1, 4), Q(-1, 4))
assert COS_3PI_5 == sub((Q(1, 2), Q(0)), COS_PI_5)

# Therefore, for
#   M(x)=2[1-arccos(1/2-cos(pi*x/2))/pi],
# the middle exact value is M(2/5)=4/5. Together with the endpoint
# values this gives three exact rational knots.
KNOTS = (
    (Q(0), Q(2, 3)),
    (Q(2, 5), Q(4, 5)),
    (Q(2, 3), Q(1)),
)
(x0, y0), (xm, ym), (x1, y1) = KNOTS

low_slope = (ym - y0) / (xm - x0)
low_intercept = y0 - low_slope * x0
high_slope = (y1 - ym) / (x1 - xm)
high_intercept = ym - high_slope * xm

assert (low_slope, low_intercept) == (Q(1, 3), Q(2, 3))
assert (high_slope, high_intercept) == (Q(3, 4), Q(1, 2))

# Compare to the full-domain chord 2/3+x/2.
# On (0,2/5), its excess above the low secant is x/6.
assert Q(1, 2) - low_slope == Q(1, 6)
# On (2/5,2/3), its excess above the high secant is 1/6-x/4.
assert Q(2, 3) - high_intercept == Q(1, 6)
assert high_slope - Q(1, 2) == Q(1, 4)

print("PASS")
print("M(0)=2/3, M(2/5)=4/5, M(2/3)=1")
print("low-rank secant: M(x) <= 2/3 + x/3 on [0,2/5]")
print("high-rank secant: M(x) <= 1/2 + 3x/4 on [2/5,2/3]")
