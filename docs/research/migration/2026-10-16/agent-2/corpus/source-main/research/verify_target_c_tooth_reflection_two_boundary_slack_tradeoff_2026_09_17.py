import math
import random

h = math.sqrt(303.0) / 52.0
two_h = 2.0 * h

assert abs(h - 0.33474798433710024) < 1e-15
assert abs(two_h - 0.6694959686742005) < 1e-15

# Reverse-triangle upper-gate regression:
# if |d|=D and the original edge is r=d+Delta*N, then
# D-|r| <= Delta whenever |r|<D.
for D in (100.0, 1e4, 1e8):
    for Delta in (1e-6, 0.01, 0.2, h):
        for cosang in (-1.0, -0.7, -0.1):
            # N=(1,0), d has the selected cosine to N.
            dx = D * cosang
            dy = D * math.sqrt(max(0.0, 1.0 - cosang * cosang))
            # The squared diameter deficit has the exact stable form
            # D^2-|d+Delta*N|^2 = -2*D*Delta*cosang-Delta^2.
            # Use it instead of subtracting two numbers of size D^2.
            gap2 = -2.0 * D * Delta * cosang - Delta * Delta
            if gap2 > 0.0:
                r = math.sqrt(D * D - gap2)
                rho = gap2 / (D + r)
                assert 0.0 < rho <= Delta + 1e-12

# Exact support/backtracking identity regression on synthetic gate ancestries.
rng = random.Random(99)
for _ in range(1000):
    lower_cs = [rng.random() for _ in range(rng.randrange(1, 20))]
    upper_bs = [5.0 * rng.random() for _ in range(rng.randrange(0, 10))]
    deltas = [0.3 * rng.random() for _ in range(len(lower_cs) + len(upper_bs))]
    S = sum(deltas)
    L = len(lower_cs)
    E = sum(1.0 - c for c in lower_cs)
    B = sum(upper_bs)
    A = sum(lower_cs) - sum(upper_bs) + S
    assert abs((E + B) - (L - A + S)) < 1e-12

# The Markov-plus-parity extraction used in both metric-boundary cases.
def check_markov_parity(slacks):
    n = len(slacks)
    if n == 0:
        return
    total = sum(slacks)
    threshold = 2.0 * total / n
    good = [i for i, s in enumerate(slacks) if s <= threshold + 1e-15]
    assert len(good) >= n / 2.0
    even = sum((i % 2) == 0 for i in good)
    odd = len(good) - even
    assert max(even, odd) >= len(good) / 2.0

for n in range(1, 100):
    for _ in range(20):
        slacks = [rng.random() ** 4 for _ in range(n)]
        check_markov_parity(slacks)

# Scale regressions.  Ignore the already-proved O(sqrt(D)) lower-edge count
# loss here; these checks only verify the new leading scales and constants.
for D in (1e8, 1e12, 1e16):
    t = h + D ** (-1.0 / 3.0)

    M = math.sqrt(D)
    upper_count = M / 4.0
    upper_deficit = 2.0 * t / M
    lower_count = D / (4.0 * M)
    lower_excess = 2.0 * t * M / D
    assert abs(upper_count / math.sqrt(D) - 0.25) < 1e-12
    assert abs(lower_count / math.sqrt(D) - 0.25) < 1e-12
    assert upper_deficit * math.sqrt(D) < two_h + 2.1 * D ** (-1.0 / 3.0)
    assert lower_excess * math.sqrt(D) < two_h + 2.1 * D ** (-1.0 / 3.0)

    M = D ** 0.25
    upper_count = M / 4.0
    upper_deficit = 2.0 * t / M
    lower_count = D / (4.0 * M)
    lower_excess = 2.0 * t * M / D
    assert abs(upper_count / D ** 0.25 - 0.25) < 1e-12
    assert abs(lower_count / D ** 0.75 - 0.25) < 1e-12
    assert upper_deficit * D ** 0.25 < two_h + 2.1 * D ** (-1.0 / 3.0)
    assert lower_excess * D ** 0.75 < two_h + 2.1 * D ** (-1.0 / 3.0)

print('PASS: two-boundary FREE ancestry slack/tradeoff arithmetic')
print(f'h_*={h:.15f}')
print(f'2h_*={two_h:.15f}')
