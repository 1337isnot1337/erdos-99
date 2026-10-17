from itertools import permutations, product
from math import log, sqrt

# Asymmetric exponents and displayed constants.
c = 1 / (2 * log(5))
assert abs(c - 0.31066746727980593) < 1e-15
assert abs(c / 3 - 1 / (6 * log(5))) < 1e-15
assert abs(c / 12 - 1 / (24 * log(5))) < 1e-15
assert 0.0258 < 1 / (24 * log(5)) < 0.0260
assert 0.321 < sqrt(1 / (6 * log(5))) < 0.323

q0 = 0.05470272542658
T = 3.0605
subexp = 2 * log(T / q0)
assert 8.04 < subexp < 8.06


# Finite guard-rank model. Guards 1..m have compatible endpoint order.
# A chord with endpoint gap ranks (a,b) properly crosses exactly the guards
# between its two ranks.
def incidence(m, a, b):
    lo, hi = sorted((a, b))
    return frozenset(range(lo + 1, hi + 1))


for m in range(1, 8):
    for a, b in product(range(m + 1), repeat=2):
        I = incidence(m, a, b)
        assert len(I) == abs(a - b)
        if I:
            assert max(I) - min(I) + 1 == len(I)


# Pairwise-crossing rank families have a nondecreasing alpha sequence and a
# nonincreasing beta sequence. Within either orientation class, incidence
# intervals are nested.
for m in range(1, 6):
    pairs = [(a, b) for a in range(m + 1) for b in range(m + 1)]
    for n in range(1, 5):
        def rec(prefix):
            if len(prefix) == n:
                seq = prefix
                for orient in (0, 1):
                    cls = []
                    for a, b in seq:
                        if (orient == 0 and a <= b) or (orient == 1 and a > b):
                            cls.append(incidence(m, a, b))
                    for X, Y in zip(cls, cls[1:]):
                        if orient == 0:
                            assert Y <= X
                        else:
                            assert X <= Y
                    assert len(set(cls)) <= m + 1
                return
            for p in pairs:
                if prefix and not (
                    prefix[-1][0] <= p[0] and prefix[-1][1] >= p[1]
                ):
                    continue
                rec(prefix + [p])

        rec([])


# A sequence of row permutations in which each unordered chord pair flips at
# most once can change its full permutation in at most C(n,2) gaps.
def inversion_bits(p):
    pos = {v: i for i, v in enumerate(p)}
    n = len(p)
    return tuple(pos[i] > pos[j] for i in range(n) for j in range(i + 1, n))


for n in range(2, 6):
    ps = list(permutations(range(n)))
    bits = [inversion_bits(p) for p in ps]
    max_states = n * (n - 1) // 2 + 1
    vecs = {b for b in bits}
    ordered = sorted(vecs, key=sum)
    dp = {}
    for b in ordered:
        best = 1
        for a in ordered:
            if sum(a) >= sum(b):
                break
            if all((not x) or y for x, y in zip(a, b)):
                best = max(best, dp.get(a, 1) + 1)
        dp[b] = best
    assert max(dp.values()) <= max_states


# Erdos-Szekeres finite lower bound: every permutation of n entries has an
# increasing or decreasing subsequence of length at least ceil(sqrt(n)).
def lis_len(p):
    d = []
    for i, x in enumerate(p):
        d.append(1 + max([d[j] for j in range(i) if p[j] < x] or [0]))
    return max(d)


def lds_len(p):
    return lis_len(tuple(-x for x in p))


for n in range(1, 9):
    need = int(sqrt(n))
    if need * need < n:
        need += 1
    for p in permutations(range(n)):
        assert max(lis_len(p), lds_len(p)) >= need


print("PASS: asymmetric THIN unique-grid regressions")
print("braid coefficient =", c)
print("sector braid coefficient =", c / 3)
print("balanced GUARD homogeneous coefficient =", 1 / (24 * log(5)))
print("train subexponential exponent coefficient =", subexp)
