#!/usr/bin/env python3
"""Independent exact checks for the through-splice audit's finite algebra."""

def quotient_edge_bound_times_four(M: int, P: int, r: int) -> int:
    """Mantel bound on singleton edges plus all possible other simple edges."""
    N = M - P
    s = N - r
    return s * s + 4 * r * s + 2 * r * (r - 1)

checked = 0
for M in range(1, 351):
    # Five distinct terminal occurrences per selected face; at most two ends
    # per dominant train, so 5P <= 2M (the K_D term only strengthens this).
    for P in range(0, 2 * M // 5 + 1):
        N = M - P
        assert P <= N
        target_times_four = M * M - 2 * P * P - 2 * P
        values = []
        for r in range(P + 1):
            value_times_four = quotient_edge_bound_times_four(M, P, r)
            assert value_times_four <= target_times_four, (
                M, P, r, value_times_four, target_times_four
            )
            values.append(value_times_four)
            checked += 1
        assert values[-1] == target_times_four
        assert values == sorted(values)

# Negative control: without the endpoint-incidence cap, substituting r=P can
# fail. Here P=3>M*2/5, N=2, r=2 is admissible as a quotient forest count.
bad_M, bad_P, bad_r = 5, 3, 2
bad_actual_times_four = quotient_edge_bound_times_four(bad_M, bad_P, bad_r)
bad_target_times_four = bad_M * bad_M - 2 * bad_P * bad_P - 2 * bad_P
assert bad_actual_times_four == 4 and bad_target_times_four == 1
assert bad_actual_times_four > bad_target_times_four

# Exact integer cross-multiplication controls for g(C)=8*delta/C-C.
for delta in (1, 3, 5):
    for C, U in ((2, 3), (4, 7), (9, 11)):
        assert C < U
        assert (U - C) * (8 * delta + C * U) > 0
        assert C * C < U * U

print("PASS independent through-splice finite audit")
print("admissible integer (M,P,r) triples checked =", checked)
print("without endpoint cap: M=5, P=3, r=2 gives 1 > 1/4 (excluded by 5P<=2M)")
print("positive-integer scalar monotonicity controls = 9")
