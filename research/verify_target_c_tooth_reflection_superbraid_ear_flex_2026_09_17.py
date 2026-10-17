import math

h = math.sqrt(303.0) / 52.0
c = 1.0 / math.sqrt(1.0 + h / 2.0)
endpoint_coeff = 2.0 * c
near_unit_coeff = c / 102.0
flex_coeff = c / 2.0

assert abs(c - 0.925539574680581) < 1e-15
assert abs(endpoint_coeff - 1.851079149361162) < 2e-15
assert abs(near_unit_coeff - 0.009073917398829225) < 2e-15
assert abs(flex_coeff - 0.4627697873402905) < 2e-15

# Guard graph: lambda<=1 gives incoming packing count <=25, hence Delta<=26.
for lam in (0.0, 0.1, 0.5, 1.0):
    incoming = (3.0 + 2.0 * lam) ** 2
    assert incoming <= 25.0 + 1e-12

# If g_g >= g/2, distinct guard edges >= g_g/2 and greedy matching
# >= E/(2*26-1), hence >= g/204.
for g in (204, 1000, 10000):
    gg = g / 2.0
    distinct_edges = gg / 2.0
    matching = distinct_edges / 51.0
    assert matching >= g / 204.0 - 1e-12

# Movable side: if maximum conflict matching is < |G_m|/4, unmatched
# vertices are > |G_m|/2, hence > g/4 whenever |G_m|>g/2.
for g in (100.0, 1000.0):
    gm = 0.5001 * g
    r = 0.2499 * gm
    unmatched = gm - 2.0 * r
    assert unmatched > gm / 2.0
    assert unmatched > g / 4.0

# Sublinear-terminal normalization: bad shallow ears are o(sqrt(D)) for
# lambda=sqrt(t/D), leaving endpoint_coeff*sqrt(D)+o(sqrt(D)). The
# conservative common near-unit coefficient is endpoint_coeff/204=c/102.
assert abs(endpoint_coeff / 204.0 - near_unit_coeff) < 1e-15
assert abs(endpoint_coeff / 4.0 - flex_coeff) < 1e-15

print("PASS: superbraid ear-flex combinatorial arithmetic")
print(f"c_blk={c:.15f}")
print(f"near-unit coefficient={near_unit_coeff:.15f}")
print(f"simultaneous-flex coefficient={flex_coeff:.15f}")
