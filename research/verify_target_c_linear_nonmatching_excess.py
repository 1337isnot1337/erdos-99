#!/usr/bin/env python3
from fractions import Fraction as F

# Section 61 defines c_* by c = cos(3c/2).  The function
# G(c)=c-cos(3c/2) is strictly increasing on (0,1).
# We certify 6099/10000 < c_* < 61/100 with exact rational
# alternating-series bounds for cos x, where x<1 in both tests.

def cos_lower_10(x: F) -> F:
    # Alternating cosine series truncated after the negative x^10 term.
    return (
        F(1)
        - x**2 / F(2)
        + x**4 / F(24)
        - x**6 / F(720)
        + x**8 / F(40320)
        - x**10 / F(3628800)
    )


def cos_upper_8(x: F) -> F:
    # Alternating cosine series truncated after the positive x^8 term.
    return (
        F(1)
        - x**2 / F(2)
        + x**4 / F(24)
        - x**6 / F(720)
        + x**8 / F(40320)
    )


lo = F(6099, 10000)
hi = F(61, 100)
x_lo = F(3, 2) * lo
x_hi = F(3, 2) * hi

assert 0 < x_lo < 1
assert 0 < x_hi < 1

# cos(3 lo/2) > lo, hence G(lo)<0 and lo<c_*.
lo_margin = cos_lower_10(x_lo) - lo
assert lo_margin > 0

# cos(3 hi/2) < hi, hence G(hi)>0 and c_*<hi.
hi_margin = hi - cos_upper_8(x_hi)
assert hi_margin > 0

print("certified lower endpoint:", lo)
print("lower sign margin cos(3c/2)-c:", lo_margin)
print("certified upper endpoint:", hi)
print("upper sign margin c-cos(3c/2):", hi_margin)
print("therefore 0.6099 < c_* < 0.61")
