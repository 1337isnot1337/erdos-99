from math import log2
import random


def admissible_s(k: int, n: int) -> int:
    """Largest s with 4s <= k and 16^s s <= n."""
    s = 0
    while 4 * (s + 1) <= k and (16 ** (s + 1)) * (s + 1) <= n:
        s += 1
    return s


# Exact arithmetic behind the two pigeonhole steps.
for s in range(1, 9):
    n = (16**s) * s
    k = 4 * s
    assert n // (2 ** (4 * s)) >= s
    assert n // (2 ** (2 * s)) >= s
    assert 4 * s <= k


# The maximal s satisfies s ~ (1/4) log_2 n.  Powers of two let us
# inspect the ratio without floating-point ambiguity in n itself.
ratios = []
for L in range(20, 241, 10):
    n = 1 << L
    k = 2 * n
    s = admissible_s(k, n)
    ratios.append(s / L)
assert ratios[-1] > 0.24
assert ratios[-1] > ratios[0]


def extract(matrix_left, matrix_right):
    """Implement the constructive proof of Lemma IP.1.

    Matrices are train-by-braid binary incidence matrices.  The routine
    returns braid coordinates F, left rows IL, right rows IR and the two
    homogeneous incidence bits.
    """
    n_left = len(matrix_left)
    n_right = len(matrix_right)
    k = len(matrix_left[0])
    assert all(len(row) == k for row in matrix_left)
    assert all(len(row) == k for row in matrix_right)

    n = min(n_left, n_right)
    s = admissible_s(k, n)
    if s == 0:
        return [], [], [], None, None

    # First pigeonhole on 4s braid coordinates against the left fence.
    F0 = list(range(4 * s))
    classes = {}
    for i, row in enumerate(matrix_left):
        pattern = tuple(row[j] for j in F0)
        classes.setdefault(pattern, []).append(i)
    pattern_left, indices_left = max(classes.items(), key=lambda kv: len(kv[1]))
    assert len(indices_left) >= s

    bit_left = 1 if sum(pattern_left) >= 2 * s else 0
    F1 = [F0[j] for j, bit in enumerate(pattern_left) if bit == bit_left][: 2 * s]
    assert len(F1) == 2 * s
    indices_left = indices_left[:s]

    # Second pigeonhole on the surviving 2s coordinates against the right
    # fence, followed by one more majority-coordinate selection.
    classes = {}
    for i, row in enumerate(matrix_right):
        pattern = tuple(row[j] for j in F1)
        classes.setdefault(pattern, []).append(i)
    pattern_right, indices_right = max(classes.items(), key=lambda kv: len(kv[1]))
    assert len(indices_right) >= s

    bit_right = 1 if sum(pattern_right) >= s else 0
    F = [F1[j] for j, bit in enumerate(pattern_right) if bit == bit_right][:s]
    assert len(F) == s
    indices_right = indices_right[:s]

    for i in indices_left:
        for j in F:
            assert matrix_left[i][j] == bit_left
    for i in indices_right:
        for j in F:
            assert matrix_right[i][j] == bit_right

    return F, indices_left, indices_right, bit_left, bit_right


# Deterministic randomized regression for the constructive extraction.
rng = random.Random(20260917)
for s_target in (1, 2):
    n = (16**s_target) * s_target
    k = max(4 * s_target, 2 * n)
    for _ in range(4):
        left = [[rng.randrange(2) for _ in range(k)] for _ in range(n)]
        right = [[rng.randrange(2) for _ in range(k)] for _ in range(n)]
        F, IL, IR, bit_left, bit_right = extract(left, right)
        assert len(F) >= s_target
        assert len(IL) >= s_target
        assert len(IR) >= s_target
        assert bit_left in (0, 1)
        assert bit_right in (0, 1)


# Explicit asymptotic lower witness: the maximal integer is within the
# expected (1/4) log_2 n scale.  This checks the logarithmic bookkeeping
# used in IP.17--IP.19, independently of the geometric parent theorem.
for log2D in (10**3, 10**4, 10**5, 10**6):
    n = max(1, log2D // 40)
    k = 2 * n
    s = admissible_s(k, n)
    if s:
        target = 0.25 * log2(max(n, 2))
        assert s < target + 1


print("PASS: two-sided THIN braid/fence incidence purification")
print("last s/log2(n)=", ratios[-1])
