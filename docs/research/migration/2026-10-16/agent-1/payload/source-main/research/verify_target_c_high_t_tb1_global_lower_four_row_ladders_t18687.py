from fractions import Fraction
from math import sqrt

s0 = Fraction(791, 320_000_000)
# Current sharp all-residue Horn budget: 2 N_L + N_U > (s0/8-o(1)) D.
# Thus a LOWER metric winner has density s0/24.
delta = s0 / 24
good = delta / 2
pure = Fraction(1609, 2500)  # 0.6436
Tstar = Fraction(6121, 2000)  # 3.0605
thread = good * pure / Tstar
disjoint_thread = thread / 8

assert delta == Fraction(791, 7_680_000_000)
assert good == Fraction(791, 15_360_000_000)
assert thread == Fraction(1_272_719, 117_523_200_000_000)
assert disjoint_thread == Fraction(1_272_719, 940_185_600_000_000)
assert 1.0829e-8 < float(thread) < 1.0830e-8
assert 1.3536e-9 < float(disjoint_thread) < 1.3538e-9


def support(owner, other):
    a, b = sorted((owner, other))
    return set(range(a + 1, b + 1))


# For support depth <= 4, a fixed cut can be covered only by blockers whose
# injective owner is in one of eight positions. An internal adjacent-row
# transition has only six possible owner positions.
records = []
for owner in range(-30, 31):
    for d in range(-4, 5):
        if d:
            records.append((owner, support(owner, owner + d)))

max_row_overlap = 0
max_adj_overlap = 0
for k in range(-20, 21):
    row_owners = {owner for owner, I in records if k in I}
    adj_owners = {owner for owner, I in records if k in I and k + 1 in I}
    max_row_overlap = max(max_row_overlap, len(row_owners))
    max_adj_overlap = max(max_adj_overlap, len(adj_owners))

assert max_row_overlap == 8
assert max_adj_overlap == 6

# Interval graphs are perfect, so maximum overlap <= 8 gives an 8-coloring
# and a pairwise-disjoint subfamily of size at least one eighth.
assert max_row_overlap == 8

flank_density = 0.6436 - 1.02 / sqrt(3)
assert 0.05470 < flank_density < 0.05471

print("global four-row LOWER synchronization certificate: PASS")
print("lower_winner_density =", float(delta))
print("good_window_density =", float(good))
print("max_row_overlap =", max_row_overlap)
print("max_adjacent_overlap =", max_adj_overlap)
print("fixed_train_density =", float(thread))
print("disjoint_fixed_train_density =", float(disjoint_thread))
print("flank_density =", flank_density)
