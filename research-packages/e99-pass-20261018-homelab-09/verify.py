#!/usr/bin/env python3
"""Independent small-graph audit of PR #957's supplied-packet identity.

This checks the finite graph identity on every 3-by-3 diameter/cross-conflict
pattern, then gives an exact rational counterexample if the candidate summary's
word "contain" is read as allowing extra cross edges. It proves no global
packet-existence statement.
"""

from fractions import Fraction
from itertools import combinations


N = M = 3
H_EDGES = ((0, 1), (0, 2), (1, 2))


def popcount(mask):
    return mask.bit_count()


def is_cover(mask, h_mask):
    return all(
        not (h_mask & (1 << edge_id))
        or (mask & (1 << i))
        or (mask & (1 << j))
        for edge_id, (i, j) in enumerate(H_EDGES)
    )


def max_matching(cross_mask, available_source_mask):
    """Maximum matching by a direct packet-label recursion."""

    def visit(packet, used_source):
        if packet == M:
            return 0
        best = visit(packet + 1, used_source)
        for source in range(N):
            edge = 1 << (packet * N + source)
            if (cross_mask & edge and available_source_mask & (1 << source)
                    and not used_source & (1 << source)):
                best = max(best, 1 + visit(packet + 1,
                                           used_source | (1 << source)))
        return best

    return visit(0, 0)


def direct_independent_set_size(h_mask, cross_mask):
    best = 0
    for source_subset in range(1 << N):
        if any(h_mask & (1 << edge_id)
               and source_subset & (1 << i)
               and source_subset & (1 << j)
               for edge_id, (i, j) in enumerate(H_EDGES)):
            continue
        for packet_subset in range(1 << M):
            if any(cross_mask & (1 << (packet * N + source))
                   and packet_subset & (1 << packet)
                   and source_subset & (1 << source)
                   for packet in range(M) for source in range(N)):
                continue
            best = max(best, popcount(source_subset) + popcount(packet_subset))
    return best


def formula_size(h_mask, cross_mask):
    costs = []
    for cover in range(1 << N):
        if is_cover(cover, h_mask):
            nu = max_matching(cross_mask, ((1 << N) - 1) ^ cover)
            costs.append(popcount(cover) + nu)
    return N + M - min(costs)


def check_all_small_graphs():
    cases = 0
    for h_mask in range(1 << len(H_EDGES)):
        for cross_mask in range(1 << (N * M)):
            direct = direct_independent_set_size(h_mask, cross_mask)
            stated = formula_size(h_mask, cross_mask)
            if direct != stated:
                raise AssertionError((h_mask, cross_mask, direct, stated))
            cases += 1
    if cases != 4096:
        raise AssertionError(f"unexpected case count: {cases}")
    print(f"PASS: formula equals direct independent-set enumeration in {cases} "
          "all 3-source/3-packet H/G graph patterns")


def max_matching_small(cross_edges, available_source):
    # The counterexample has one packet label, so its matching is direct.
    return int(any((source, 0) in cross_edges for source in available_source))


def small_formula(n, m, diameter_edges, cross_edges):
    covers = []
    for cover in range(1 << n):
        if all((cover & (1 << i)) or (cover & (1 << j))
               for i, j in diameter_edges):
            available = {i for i in range(n) if not cover & (1 << i)}
            nu = max_matching_small(cross_edges, available)
            covers.append(cover.bit_count() + nu)
    return n + m - min(covers)


def check_exact_graph_hypothesis():
    # A={0,2} has D=2; B={1} is unit-separated with diam(B)=0<D.
    # Cross distances are exactly one, so neither <1 nor >=D: the exact G is
    # empty. The best strict-D subset has size two, e.g. {0,1}.
    a = (Fraction(0), Fraction(2))
    b = (Fraction(1),)
    diameter = max(abs(x - y) for x, y in combinations(a, 2))
    lower_cross = {(i, j) for i, x in enumerate(a) for j, y in enumerate(b)
                   if abs(x - y) < 1}
    upper_cross = {(i, j) for i, x in enumerate(a) for j, y in enumerate(b)
                   if abs(x - y) >= diameter}
    exact_cross = lower_cross | upper_cross
    if diameter != 2 or exact_cross:
        raise AssertionError("rational control does not have empty exact G")

    diameter_edges = {(0, 1)}
    exact_prediction = small_formula(2, 1, diameter_edges, exact_cross)
    # An arbitrary supergraph is still a graph that "contains every" true
    # conflict, but its matching cost is wrong for geometric feasibility.
    enlarged = {(0, 0), (1, 0)}
    enlarged_prediction = small_formula(2, 1, diameter_edges, enlarged)
    direct_geometric_maximum = 2
    if exact_prediction != direct_geometric_maximum:
        raise AssertionError((exact_prediction, direct_geometric_maximum))
    if enlarged_prediction == direct_geometric_maximum:
        raise AssertionError("extra false conflicts did not falsify the formula")
    print("PASS: exact iff conflict definition predicts 2; adding two false "
          f"cross edges predicts {enlarged_prediction} for a true maximum of 2")


def main():
    check_all_small_graphs()
    check_exact_graph_hypothesis()


main()
