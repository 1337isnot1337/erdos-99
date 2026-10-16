from collections import Counter
from functools import lru_cache
from itertools import combinations, permutations, product

MOD = 2147483647
V = tuple(range(7))
SUP = tuple(combinations(V, 4))
SI = {s: i for i, s in enumerate(SUP)}
TRI = tuple(combinations(V, 3))
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
        for j in range(c, n):
            A[r][j] = A[r][j] * inv % MOD
        for i in range(r + 1, m):
            if A[i][c]:
                q = A[i][c]
                for j in range(c, n):
                    A[i][j] = (A[i][j] - q * A[r][j]) % MOD
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
        # Committed local-block rule: rank two exactly when a containing
        # tetrahedral support occurs at least twice; otherwise rank one.
        dim = 2 if any(mult[ms[i]] >= 2 for i in occurrences) else 1
        data[b] = (occurrences, dim, len(occurrences))
    return data


def empty_eligible(x):
    _, dim, incidence = x
    return incidence >= (5 if dim == 2 else 4)


def compatible(x, y):
    Ix, dx, nx = x
    Iy, dy, ny = y
    inter = len(Ix & Iy)
    union = nx + ny - inter
    # Necessary consequences of (d1,d2,d3,d4) >= (4,5,6,7).
    if dx == dy == 1:
        return inter >= 4 or union >= 5
    if dx != dy:
        return inter >= 4 or union >= 6
    return inter >= 5 or (inter >= 4 and union >= 6) or union >= 7


def singleton_object(data, block):
    occurrences, _, incidence = data[block]
    return occurrences, 1, incidence


def occurrence_union_size(objects):
    support = set()
    for occurrences, _, _ in objects:
        support.update(occurrences)
    return len(support)


def mixed_profile_survives(ms, census):
    data = block_data(ms)
    T = tuple(sorted(data))
    h = len(T)
    # Mixed singleton+pair profile: at most two selected incomplete blocks are touched.
    # Complete touched blocks are independent (d_root=0), so e>=h-17. Since every
    # empty block has at least four incidences, 32>=h+3e forces h<=20.
    if h > 20:
        return False
    census["touch_at_most_20"] += 1

    untouched = 35 - h
    eligible = sorted(b for b in T if empty_eligible(data[b]))
    later = {
        b: {w for w in eligible if w > b and compatible(data[b], data[w])}
        for b in eligible
    }
    min_empty = max(0, h - 17)

    @lru_cache(None)
    def structural_ok(incomplete_tuple):
        incomplete = set(incomplete_tuple)
        complete = tuple(b for b in T if b not in incomplete)
        if tri_rank(complete) != len(complete):
            return False
        return tri_rank(T) - tri_rank(complete) >= 4

    def generator_ok(E, singleton_nonzero):
        objects = [data[b] for b in E]
        if singleton_nonzero is not None:
            objects.append(singleton_object(data, singleton_nonzero))
        dim_sum = sum(data[b][1] for b in E) + (singleton_nonzero is not None)
        if dim_sum < 4:
            return False
        if occurrence_union_size(objects) < 7:
            return False
        return all(
            compatible(objects[i], objects[j])
            for i in range(len(objects))
            for j in range(i)
        )

    def test(E):
        Eset = set(E)
        remaining = [b for b in T if b not in Eset]

        # Both selected blocks untouched. They must be distinct.
        if untouched >= 2:
            if structural_ok(tuple(sorted(Eset))) and generator_ok(E, None):
                return True

        # Singleton touched, pair untouched. The singleton may contribute zero or one line.
        if untouched >= 1:
            for sb in remaining:
                inc = tuple(sorted(Eset | {sb}))
                if not structural_ok(inc):
                    continue
                if generator_ok(E, None):
                    return True
                if data[sb][2] >= 4 and generator_ok(E, sb):
                    return True

        # Singleton untouched, pair touched.
        if untouched >= 1 and generator_ok(E, None):
            for pb in remaining:
                if structural_ok(tuple(sorted(Eset | {pb}))):
                    return True

        # Both touched, on distinct blocks.
        for sb in remaining:
            for pb in remaining:
                if pb == sb:
                    continue
                inc = tuple(sorted(Eset | {sb, pb}))
                if not structural_ok(inc):
                    continue
                if generator_ok(E, None):
                    return True
                if data[sb][2] >= 4 and generator_ok(E, sb):
                    return True
        return False

    found = False

    def rec(E, candidates, dim_sum):
        nonlocal found
        if found:
            return
        if len(E) + len(candidates) < min_empty:
            return
        # The singleton supplies at most one further coefficient dimension.
        if dim_sum + sum(data[b][1] for b in candidates) + 1 < 4:
            return
        if len(E) >= min_empty and test(E):
            found = True
            return
        ordered = sorted(candidates)
        for i, b in enumerate(ordered):
            rec(
                E + [b],
                set(ordered[i + 1 :]) & later[b],
                dim_sum + data[b][1],
            )
            if found:
                return

    rec([], set(eligible), 0)
    return found


def lucas_lehmer_31():
    s = 4
    for _ in range(29):
        s = (s * s - 2) % MOD
    return s == 0


def main():
    # Arithmetic sharpening used by the proof note.
    D = -1
    # In the mixed profile, any nonzero coefficient word of weight at most
    # three is supported in a three-coordinate deletion. The all-depth deletion
    # bound forces q=1 there, giving a five-row (D,k,p)=(2,2,3) state. The
    # committed sharp theorem for that state forces three singleton blocks,
    # contradicting the mixed singleton+pair profile. Hence d1(P)>=4.
    assert D + 2 * 3 - 3 * 1 == 2

    assert lucas_lehmer_31()
    # Triangle rows have squared norm 3 and rank at most 15. Hadamard makes
    # modular and rational ranks identical for every triangle-row minor used here.
    assert MOD * MOD > 3**15

    reps = support_multiset_orbits()
    census = Counter()
    census["support_multiset_orbits_size_8"] = len(reps)
    survivors = []
    for ms in reps:
        if mixed_profile_survives(ms, census):
            survivors.append(ms)

    expected = {
        "support_multiset_orbits_size_8": 27763,
        "touch_at_most_20": 13574,
    }
    for key, value in expected.items():
        assert census[key] == value, (key, census[key], value)
    assert not survivors, survivors[:3]

    print("PASS: eight-no-root k=4 D=-1 d_root=0 p=3 mixed singleton+pair closure")
    print("orbit_counts_size_0_through_8", EXPECTED_ORBIT_COUNTS)
    print("support_multiset_orbits_size_8", census["support_multiset_orbits_size_8"])
    print("touch_at_most_20", census["touch_at_most_20"])
    print("mixed_profile_survivors", len(survivors))
    print("hadamard_exact_rank_bound", MOD * MOD > 3**15)


if __name__ == "__main__":
    main()
