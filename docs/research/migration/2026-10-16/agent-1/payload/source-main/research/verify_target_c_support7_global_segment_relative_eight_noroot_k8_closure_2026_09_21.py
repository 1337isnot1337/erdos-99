from math import comb, ceil

# Eight-no-root k=8 residual arithmetic.
branches = [(-2, 14), (-1, 15)]
for D, p in branches:
    D6 = D + 4
    assert D6 in (2, 3)
    # Deleting a pair preserves k=6 and changes p only by the selected
    # incomplete-row cost supported entirely on that pair. Congruence forces
    # every pair loss to be a multiple of 3.
    for loss in (0, 3):
        p6 = p - loss
        assert (D6 - (6 + p6)) % 3 == 0

# Triple shadows in the committed reduction lose either 0 or 3 rows.
for D, p in branches:
    D5 = D + 6
    allowed = {p, p - 3}
    for p5 in allowed:
        assert (D5 - (5 + p5)) % 3 == 0

# After the singleton- and pair-support eliminations, every pair of the eight
# external coordinates must lie in a positive exact-support triple. A triple
# covers exactly three unordered pairs.
pairs = comb(8, 2)
pairs_per_triple = comb(3, 2)
cover_lb = ceil(pairs / pairs_per_triple)
assert pairs == 28
assert pairs_per_triple == 3
assert cover_lb == 10

# Each positive exact-support triple has cost exactly 3, while the total
# incomplete-row budgets are only 14 and 15.
max_edges = {14: 14 // 3, 15: 15 // 3}
assert max_edges == {14: 4, 15: 5}
for p in (14, 15):
    assert max_edges[p] < cover_lb

print("PASS: eight-no-root k=8 low-support hypergraph closure")
print("pair_cover_lower_bound", cover_lb)
print("max_positive_triples", max_edges)
print("remaining_k8_branches", 0)
