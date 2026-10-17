from collections import Counter
from functools import lru_cache
from itertools import combinations, permutations, product

MOD = 2147483647
V = tuple(range(7))
SUP = tuple(combinations(V, 4))
SI = {s: i for i, s in enumerate(SUP)}
TRI = tuple(combinations(V, 3))
TI = {t: i for i, t in enumerate(TRI)}
EDGES = tuple(combinations(V, 2))
EI = {e: i for i, e in enumerate(EDGES)}
EXPECTED_ORBIT_COUNTS = (1, 1, 4, 14, 61, 268, 1283, 6032, 27763)

TRIROW = []
for a, b, c in TRI:
    row = [0] * 21
    row[EI[(b, c)]] = 1
    row[EI[(a, c)]] = -1
    row[EI[(a, b)]] = 1
    TRIROW.append(tuple(row))


def rank_mod(rows):
    if not rows:
        return 0
    A = [[x % MOD for x in row] for row in rows]
    m = len(A)
    n = len(A[0])
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if A[i][c]), None)
        if pivot is None:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        inv = pow(A[r][c], MOD - 2, MOD)
        A[r] = [(x * inv) % MOD for x in A[r]]
        for i in range(m):
            if i != r and A[i][c]:
                q = A[i][c]
                A[i] = [(x - q * y) % MOD for x, y in zip(A[i], A[r])]
        r += 1
        if r == m:
            break
    return r


@lru_cache(None)
def tri_rank(blocks):
    return rank_mod([TRIROW[b] for b in blocks])


@lru_cache(None)
def canonical(ms):
    degree = [0] * 7
    for si in ms:
        for v in SUP[si]:
            degree[v] += 1

    values = sorted(set(degree), reverse=True)
    groups = []
    positions = []
    offset = 0
    for value in values:
        group = tuple(v for v in V if degree[v] == value)
        groups.append(group)
        positions.append(tuple(range(offset, offset + len(group))))
        offset += len(group)

    best = None
    for choices in product(*(permutations(group) for group in groups)):
        relabel = [None] * 7
        for old_order, new_positions in zip(choices, positions):
            for old, new in zip(old_order, new_positions):
                relabel[old] = new
        image = tuple(
            sorted(
                SI[tuple(sorted(relabel[v] for v in SUP[si]))]
                for si in ms
            )
        )
        if best is None or image < best:
            best = image
    return best


def support_multiset_orbits():
    reps = {()}
    counts = [1]
    for _ in range(8):
        out = set()
        for ms in reps:
            mult = Counter(ms)
            for si in range(35):
                if mult[si] < 3:
                    out.add(canonical(tuple(sorted(ms + (si,)))))
        reps = out
        counts.append(len(reps))
    assert tuple(counts) == EXPECTED_ORBIT_COUNTS, counts
    return tuple(sorted(reps))


def block_data(ms):
    mult = Counter(ms)
    data = {}
    for b, tri in enumerate(TRI):
        occurrences = frozenset(
            i for i, si in enumerate(ms) if set(tri).issubset(SUP[si])
        )
        if not occurrences:
            continue
        # Committed local-block rule: a touched empty block has local rank two
        # iff one containing tetrahedral support is repeated; otherwise rank one.
        dim = 2 if any(mult[ms[i]] >= 2 for i in occurrences) else 1
        data[b] = (occurrences, dim, len(occurrences))
    return data


def individually_eligible(x):
    _, dim, incidence = x
    return incidence >= (4 if dim == 2 else 2)


def compatible(x, y):
    Ix, dx, nx = x
    Iy, dy, ny = y
    inter = len(Ix & Iy)
    union = nx + ny - inter

    # Necessary consequences of (d1,d2,d3,d4) >= (2,4,5,7).
    if dx == dy == 1:
        return inter >= 2 or union >= 4
    if dx != dy:
        return inter >= 2 or union >= 5
    return inter >= 4 or (inter >= 2 and union >= 5) or union >= 7


def occurrence_union_size(blocks, data):
    support = set()
    for b in blocks:
        support.update(data[b][0])
    return len(support)


def search_empty_sets(ms, data, census):
    h = len(data)
    if h > 24:
        return

    census["touch_at_most_24"] += 1
    eligible = sorted(b for b in data if individually_eligible(data[b]))
    later = {
        b: {w for w in eligible if w > b and compatible(data[b], data[w])}
        for b in eligible
    }

    # Root deficiency one means the full complete-block family has nullity one
    # in the 15-dimensional triangle-row space. Therefore at most 16 complete
    # blocks are present, so at least h-16 touched blocks must be empty.
    min_empty = max(0, h - 16)

    def test(E, dim_sum):
        if len(E) < min_empty or dim_sum < 4:
            return
        if occurrence_union_size(E, data) < 7:
            return

        census["weight_compatible_empty_sets"] += 1

        T = tuple(sorted(data))
        Eset = set(E)
        C = tuple(b for b in T if b not in Eset)
        nullity_C = len(C) - tri_rank(C)

        # Any subset of a complete family of nullity one has nullity at most one.
        if nullity_C > 1:
            return
        census["touched_complete_nullity_at_most_1"] += 1

        # All four external relation directions must survive modulo the complete
        # root span. Every external lift is face-local, hence lies in H(T).
        # Replacing the full complete span by the smaller touched-complete span
        # only enlarges the available quotient, so this is a necessary condition.
        capacity = tri_rank(T) - tri_rank(C)
        if capacity >= 4:
            census["capacity_survivors"] += 1

    def rec(E, candidates, dim_sum):
        if len(E) + len(candidates) < min_empty:
            return
        if dim_sum + sum(data[b][1] for b in candidates) < 4:
            return

        test(E, dim_sum)
        ordered = sorted(candidates)
        for i, b in enumerate(ordered):
            rec(
                E + [b],
                set(ordered[i + 1 :]) & later[b],
                dim_sum + data[b][1],
            )

    rec([], set(eligible), 0)


def lucas_lehmer_31():
    s = 4
    for _ in range(29):
        s = (s * s - 2) % MOD
    return s == 0


def main():
    assert lucas_lehmer_31()
    # Triangle rows have squared Euclidean norm 3 and rank at most 15.
    # Hadamard therefore gives |det|^2 <= 3^15 for every relevant nonzero
    # integer minor. This makes mod-MOD rank identical to rational rank.
    assert MOD * MOD > 3**15

    reps = support_multiset_orbits()
    census = Counter()
    census["support_multiset_orbits_size_8"] = len(reps)

    for ms in reps:
        search_empty_sets(ms, block_data(ms), census)

    expected = {
        "support_multiset_orbits_size_8": 27763,
        "touch_at_most_24": 26580,
        "weight_compatible_empty_sets": 32060,
        "touched_complete_nullity_at_most_1": 908,
        "capacity_survivors": 0,
    }
    for key, value in expected.items():
        assert census[key] == value, (key, census[key], value)

    print("PASS: eight-no-root k=4 D=-1 d_root=1 p=0 support closure")
    print("orbit_counts_size_0_through_8", EXPECTED_ORBIT_COUNTS)
    for key in expected:
        print(key, census[key])
    print("hadamard_exact_rank_bound", MOD * MOD > 3**15)


if __name__ == "__main__":
    main()
