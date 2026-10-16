from fractions import Fraction
from itertools import product

# Density bookkeeping.
gamma = Fraction(791, 9_600_000_000)
rich_blocker_density = gamma / 80
final_rail_density = rich_blocker_density / 8

assert rich_blocker_density == Fraction(791, 768_000_000_000)
assert final_rail_density == Fraction(791, 6_144_000_000_000)
assert 1.0299e-9 < float(rich_blocker_density) < 1.0300e-9
assert 1.2874e-10 < float(final_rail_density) < 1.2875e-10

# A weakly unimodal sequence has a weakly monotone prefix or suffix of at least
# half the entries. Exhaust all small one-turn words by choosing an extremal
# position and weak steps on either side.
def is_nondecreasing(a):
    return all(a[i] <= a[i + 1] for i in range(len(a) - 1))


def is_nonincreasing(a):
    return all(a[i] >= a[i + 1] for i in range(len(a) - 1))


def longest_monotone_prefix_or_suffix(a):
    n = len(a)
    best = 1
    for k in range(1, n + 1):
        if is_nondecreasing(a[:k]) or is_nonincreasing(a[:k]):
            best = max(best, k)
        if is_nondecreasing(a[n-k:]) or is_nonincreasing(a[n-k:]):
            best = max(best, k)
    return best

# Generate weakly increasing then weakly decreasing sequences (and reversals).
for n in range(1, 9):
    vals = range(4)
    for a in product(vals, repeat=n):
        one_turn = False
        for p in range(n):
            if is_nondecreasing(a[:p+1]) and is_nonincreasing(a[p:]):
                one_turn = True
                break
            if is_nonincreasing(a[:p+1]) and is_nondecreasing(a[p:]):
                one_turn = True
                break
        if not one_turn:
            continue
        assert longest_monotone_prefix_or_suffix(a) >= (n + 1) // 2

# Support-order check: strictly increasing owner indices and a weakly monotone
# partner sequence give exactly staircase or strict nesting.
for n in range(1, 8):
    owners = [2 + 15 * i for i in range(n)]
    k = owners[-1] + 20
    # Small weakly monotone partner-label samples on the far side of k.
    for partners in product(range(k, k + 4), repeat=n):
        if is_nondecreasing(partners):
            supports = [(owners[i] + 1, partners[i]) for i in range(n)]
            for i in range(n - 1):
                assert supports[i][0] < supports[i + 1][0]
                assert supports[i][1] <= supports[i + 1][1]
                assert supports[i][0] <= k <= supports[i][1]
        if is_nonincreasing(partners):
            supports = [(owners[i] + 1, partners[i]) for i in range(n)]
            for i in range(n - 1):
                # [l_{i+1},r_{i+1}] is a strict subset of [l_i,r_i].
                assert supports[i][0] < supports[i + 1][0]
                assert supports[i][1] >= supports[i + 1][1]
                assert supports[i][0] <= k <= supports[i][1]
                assert supports[i + 1][0] <= supports[i + 1][1]

print("PASS: linear THIN weak-rail extraction regressions")
print("rich_blocker_density=", float(rich_blocker_density))
print("final_rail_density=", float(final_rail_density))
