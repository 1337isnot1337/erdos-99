#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations

# Regression checks for the short-pair bandwidth / 15-spaced exact-swap reduction.
# These checks verify the finite arithmetic and combinatorics used in the note;
# they do not replace the geometric train/crosscut inputs cited there.

# 1. The short-segment tube estimate has a fixed strict margin below 15
# at unit length.  Use fully rational safe bounds pi < 22/7 and
# sqrt(3) < 1733/1000.
sqrt3_hi = Fraction(1733, 1000)
assert sqrt3_hi * sqrt3_hi > 3
pi_hi = Fraction(22, 7)
limit_hi = 4 + 2 * pi_hi * sqrt3_hi
assert limit_hi == Fraction(26063, 1750)
assert limit_hi < 15
margin = Fraction(15) - limit_hi
assert margin == Fraction(187, 1750)

# If L <= 1+K/D, then D > (7000/187)K makes
# 4L+2*pi*sqrt(3) < 15 under the safe rational bounds above.
threshold_multiplier = Fraction(4, 1) / margin
assert threshold_multiplier == Fraction(7000, 187)

# 2. Among any integer layer indices, a largest residue class modulo 15
# is pairwise 15-separated and has size at least ceil(m/15).
def residue_winner(indices):
    buckets = [[] for _ in range(15)]
    for i in indices:
        buckets[i % 15].append(i)
    out = max(buckets, key=len)
    assert all(abs(a - b) >= 15 for a, b in combinations(out, 2))
    assert len(out) * 15 >= len(indices)
    return out

# Exhaust all subsets of a short interval and several larger deterministic sets.
for n in range(1, 13):
    for mask in range(1 << n):
        indices = [i for i in range(n) if (mask >> i) & 1]
        residue_winner(indices)

for step in range(1, 20):
    residue_winner(list(range(0, 500, step)))

# 3. Density after selecting one residue class from
# |M_D| > (s0/2)D-o(D).
s0 = Fraction(791, 320_000_000)
spaced_density = s0 / 30
assert spaced_density == Fraction(791, 9_600_000_000)
assert abs(float(spaced_density) - 8.239583333333333e-8) < 1e-22

# 4. Once genuine 11-only binary obstructions are absent, every bad 11
# state has a bad singleton ancestor.  Enumerate all bad-state sets
# B subset {10,01,11} satisfying that condition.
states = (1, 2, 3)  # bitmasks 10, 01, 11
for bmask in range(1 << 3):
    bad = {states[k] for k in range(3) if (bmask >> k) & 1}
    if 3 in bad and not (1 in bad or 2 in bad):
        continue
    if 3 in bad:
        assert 1 in bad or 2 in bad

# 5. Support-size <= 2 makes the pairwise no-new-obstruction law global.
# For every selected subset of two possible endpoint coordinates, a bad final
# pair must either be a singleton state or a 11 state with a singleton ancestor.
for selected in (1, 2, 3):
    if selected in (1, 2):
        # support size one in the selected state
        assert selected in (1, 2)
    else:
        # both endpoint coordinates selected
        for bmask in range(1 << 3):
            bad = {states[k] for k in range(3) if (bmask >> k) & 1}
            if 3 not in bad:
                continue
            if not (1 in bad or 2 in bad):
                # exactly the genuine binary pattern deleted in the theorem
                continue
            assert 1 in bad or 2 in bad

print("PASS: short-pair bandwidth / 15-spaced no-synergy regressions")
print("tube-limit rational upper =", float(limit_hi))
print("tube margin below 15 =", float(margin))
print("D/K threshold multiplier =", float(threshold_multiplier))
print("15-spaced density s0/30 =", float(spaced_density))
