from fractions import Fraction
from math import sqrt

s0 = Fraction(791, 320_000_000)
gamma = s0 / 30
delta0 = gamma / 8
Tstar = Fraction(6121, 2000)
vartheta = delta0 / (3 * Tstar)
class_coeff = vartheta / 2

assert gamma == Fraction(791, 9_600_000_000)
assert delta0 == Fraction(791, 76_800_000_000)
assert class_coeff == Fraction(791, 1_410_278_400_000)
assert 5.6088e-10 < float(class_coeff) < 5.6089e-10

# The rich-threshold bookkeeping is exact in normalized units:
# one length class has >= delta0/2 density; poor cuts/windows have total
# capacity at most delta0/3, leaving delta0/6 rich mass.
assert vartheta * Tstar == delta0 / 3
assert delta0 / 2 - delta0 / 3 == delta0 / 6

# Short interval assignment: if a<b and b-a<L, assigning by the block of a
# puts both endpoints in that block plus the next block.
for L in range(2, 20):
    for m in range(1, 80):
        for a in range(m + 1):
            for b in range(a + 1, m + 1):
                if b - a >= L:
                    continue
                r = a // L
                lo = r * L
                hi = (r + 2) * L - 1
                assert lo <= a <= hi
                assert lo <= b <= hi

# Every region index belongs to at most two consecutive two-block windows.
for L in range(2, 20):
    for x in range(200):
        hits = 0
        for r in range(100):
            if r * L <= x <= (r + 2) * L - 1:
                hits += 1
        assert hits <= 2

# The asymptotic common-flank density at mu=.01 after o(D) column deletion.
flank_density = 0.6536 - 1.02 / sqrt(3)
assert 0.06470 < flank_density < 0.06471

# Superdiameter threshold used by the THIN split.
for D in (2, 3, 10, 100, 10_000):
    assert D - 1 / (4 * D) > sqrt(D * D - 1)

print("PASS: Horn upper-blocker dense-grid localization regressions")
print("gamma=", float(gamma))
print("delta0_upper=", float(delta0))
print("rich_threshold_coeff=", float(vartheta))
print("same_type_D_over_logD_coeff=", float(class_coeff))
print("flank_density=", flank_density)
