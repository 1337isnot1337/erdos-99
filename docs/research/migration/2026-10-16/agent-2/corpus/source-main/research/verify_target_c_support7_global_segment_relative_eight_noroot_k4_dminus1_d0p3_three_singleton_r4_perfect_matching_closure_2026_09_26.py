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
        mask = 0
        for i, si in enumerate(ms):
            if set(tri).issubset(SUP[si]):
                mask |= 1 << i
        if not mask:
            continue
        occurring = tuple(i for i in range(8) if (mask >> i) & 1)
        dim = 2 if any(mult[ms[i]] >= 2 for i in occurring) else 1
        data[b] = (mask, dim, mask.bit_count())
    return data


def perfect_matchings(items=tuple(range(8))):
    if not items:
        yield ()
        return
    a = items[0]
    for k in range(1, len(items)):
        b = items[k]
        rest = items[1:k] + items[k + 1 :]
        for matching in perfect_matchings(rest):
            yield ((a, b),) + matching


MATCHINGS = tuple(perfect_matchings())
assert len(MATCHINGS) == 105


def matching_tables():
    tables = []
    for matching in MATCHINGS:
        pair_masks = tuple((1 << a) | (1 << b) for a, b in matching)
        empty = [[False] * 3 for _ in range(256)]
        singleton = [[False] * 3 for _ in range(256)]
        for mask in range(1, 256):
            union_of_pairs = all((mask & p) in (0, p) for p in pair_masks)
            met_pairs = sum(bool(mask & p) for p in pair_masks)
            for dim in (1, 2):
                empty[mask][dim] = (
                    union_of_pairs
                    and mask.bit_count() >= (2 if dim == 1 else 4)
                )
                singleton[mask][dim] = (
                    met_pairs >= 3
                    and (
                        dim == 1
                        or any((mask & p) == p for p in pair_masks)
                    )
                )
        tables.append((pair_masks, empty, singleton))
    return tuple(tables)


MATCHING_TABLES = matching_tables()


def virtual_survivor(ms, data, matching_index):
    T = tuple(sorted(data))
    rank_T = tri_rank(T)
    _, empty_lookup, singleton_lookup = MATCHING_TABLES[matching_index]

    E = {
        b
        for b in T
        if empty_lookup[data[b][0]][data[b][1]]
    }
    S = {
        b
        for b in T
        if singleton_lookup[data[b][0]][data[b][1]]
    }
    if len(S) < 3:
        return None

    N = set(T) - E
    min_singletons_from_N = max(0, len(N) - (rank_T - 4))
    if min_singletons_from_N > 3:
        return None

    S_in_N = sorted(S & N)
    S_in_E = sorted(S & E)

    for x in range(min_singletons_from_N, min(3, len(S_in_N)) + 1):
        y = 3 - x
        if y > len(S_in_E):
            continue
        for X in combinations(S_in_N, x):
            forced_complete = tuple(sorted(N - set(X)))
            if tri_rank(forced_complete) != len(forced_complete):
                continue
            if rank_T - len(forced_complete) < 4:
                continue

            for Y in combinations(S_in_E, y):
                singletons = set(X) | set(Y)

                nominal_dim = sum(
                    data[b][1] for b in E if b not in singletons
                )
                nominal_dim += sum(
                    1 for b in singletons if data[b][1] == 2
                )
                if nominal_dim < 4:
                    continue

                generator_support = 0
                for b in E:
                    if b not in singletons:
                        generator_support |= data[b][0]
                for b in singletons:
                    if data[b][1] == 2:
                        generator_support |= data[b][0]
                if generator_support != 0xFF:
                    continue

                return (
                    matching_index,
                    tuple(sorted(E)),
                    tuple(sorted(singletons)),
                    forced_complete,
                    rank_T,
                    nominal_dim,
                )
    return None


def lucas_lehmer_31():
    s = 4
    for _ in range(29):
        s = (s * s - 2) % MOD
    return s == 0


def main():
    assert lucas_lehmer_31()
    assert MOD * MOD > 3**15

    reps = support_multiset_orbits()
    census = Counter()
    survivors = []

    for ms in reps:
        data = block_data(ms)
        h = len(data)
        census["all"] += 1
        if h > 20:
            continue
        census["h_le_20"] += 1

        for matching_index in range(len(MATCHINGS)):
            census["support_matching_pairs"] += 1
            witness = virtual_survivor(ms, data, matching_index)
            if witness is not None:
                survivors.append((ms, h, witness))

    assert census["all"] == 27763, census
    assert census["h_le_20"] == 13574, census
    assert census["support_matching_pairs"] == 13574 * 105, census
    assert not survivors, survivors[:3]

    print(
        "PASS: eight-no-root k=4 D=-1 d_root=0 p=3 "
        "three-singleton r=4 perfect-matching closure"
    )
    print("orbit_counts_size_0_through_8", EXPECTED_ORBIT_COUNTS)
    print("support_multiset_orbits_size_8", census["all"])
    print("touch_at_most_20", census["h_le_20"])
    print("perfect_matchings", len(MATCHINGS))
    print("support_matching_pairs_tested", census["support_matching_pairs"])
    print("virtual_survivors", len(survivors))
    print("hadamard_exact_rank_bound", MOD * MOD > 3**15)


if __name__ == "__main__":
    main()
