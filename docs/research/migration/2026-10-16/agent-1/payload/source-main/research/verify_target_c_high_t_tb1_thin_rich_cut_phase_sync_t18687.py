from fractions import Fraction
from math import ceil, floor, pi, sqrt

s0 = Fraction(791, 320_000_000)
gamma = s0 / 30
upper_owned_density = gamma / 8
thin_density = upper_owned_density / 2  # gamma/16
rich_cut_density = 3 * thin_density
rich_blocker_density = thin_density / 5

assert gamma == Fraction(791, 9_600_000_000)
assert thin_density == Fraction(791, 153_600_000_000)
assert rich_cut_density == Fraction(791, 51_200_000_000)
assert rich_blocker_density == Fraction(791, 768_000_000_000)
assert 5.1497e-9 < float(thin_density) < 5.1498e-9
assert 1.5449e-8 < float(rich_cut_density) < 1.5450e-8
assert 1.0299e-9 < float(rich_blocker_density) < 1.0300e-9

# Packing lemma behind the rich-cut extraction.
# N distinct owners are 15-spaced and all endpoint-region intervals share a
# common integer region interval [A,B] of width w=B-A.
# If w >= 3N, there are already 3N cuts supported by all N blockers.
# If w < 3N, at most floor(w/15)+1 owners lie in [A,B]. One exterior side
# contains M owners. Taking the farther half of that side gives a block of
# 1+15*floor(M/2) cuts, each supported by at least ceil(M/2) blockers.
# The uniform asymptotic bounds are Q >= 3N-O(1), H >= N/5-O(1).
for N in range(1, 1500):
    for w in range(0, 3 * N):
        inside = min(N, w // 15 + 1)
        outside = N - inside
        M = ceil(outside / 2)
        H = ceil(M / 2)
        Q = 1 + 15 * floor(M / 2)
        assert Q >= 3 * N - 30, (N, w, inside, M, Q)
        assert H >= N / 5 - 1, (N, w, inside, M, H)

C_phase = pi**2 * sqrt(3) * (2 + sqrt(3)) / 12
H_phase = C_phase / float(rich_cut_density)
sigma = 0.01
K_phase = H_phase / sigma
r = 0.6536
mu = 0.01
flank_density = r - sigma - (1 + 2 * mu) / sqrt(3)

assert 3.4412e8 < H_phase < 3.4414e8
assert 3.4412e10 < K_phase < 3.4414e10
assert 0.05470 < flank_density < 0.05471

print("PASS: THIN rich-cut synchronization regressions")
print("thin_density=", float(thin_density))
print("rich_cut_density=", float(rich_cut_density))
print("rich_blocker_density=", float(rich_blocker_density))
print("phase_charge_bound=", H_phase)
print("phase_pointwise_constant=", K_phase)
print("flank_density=", flank_density)
