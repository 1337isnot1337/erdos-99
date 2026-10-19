"""Exact-rational arithmetic controls for the PR #103 inequality audit.

This verifies algebraic bounds and scale controls only. It does not model a
rhombic disk, establish the defect budget, or certify the geometric proof.
"""

from fractions import Fraction as F


def virtual_lower_bound(population_pairs: int, angular_gap: F, high_edge_budget: F) -> F:
    return population_pairs * angular_gap - high_edge_budget


def check_pair_partition() -> None:
    """Exhaust the finite algebra V >= qN - E for crossing count c <= E."""
    gaps = (F(0), F(1, 7), F(1, 2), F(1))
    for total_pairs in range(1, 25):
        for edge_budget in range(total_pairs + 1):
            for gap in gaps:
                bound = virtual_lower_bound(total_pairs, gap, F(edge_budget))
                for crossing_pairs in range(min(total_pairs, edge_budget) + 1):
                    worst_virtual_mass = (total_pairs - crossing_pairs) * gap
                    assert worst_virtual_mass >= bound


def check_high_defect_count() -> None:
    """Use D=100^2 and eta=1/2 so the high-edge threshold is rational."""
    diameter = 10_000
    eta = F(1, 2)
    threshold = F(1, 100)
    defect_budget = F(1, 100) * diameter
    high_edge_bound = F(1, 100) * 100**3
    assert threshold == F(1, 1) / 100
    assert 9_999 * threshold < defect_budget
    assert 10_000 * threshold == defect_budget
    assert high_edge_bound == 10_000


def check_positive_and_failure_controls() -> None:
    diameter = 10_000
    eta = F(1, 2)
    error = F(1, 100) * 100**3

    # Fixed macroscopic populations and fixed positive angular gap.
    alpha, beta, gap = F(1, 4), F(1, 5), F(1, 2)
    pairs = int(alpha * diameter) * int(beta * diameter)
    lower = virtual_lower_bound(pairs, gap, error)
    assert lower == 2_490_000
    assert lower >= alpha * beta * gap * diameter**2 / 2

    # Aligned directions have no positive quadratic term.
    assert virtual_lower_bound(pairs, F(0), error) <= 0

    # Near-threshold gap q_D = D^(-eta)/2 can be swallowed by the error.
    small_alpha_beta = F(1, 100)
    near_gap = F(1, 200)
    assert small_alpha_beta * near_gap * diameter**2 - error < 0

    # With |A|=|B|=D^(3/4), the product has the same D^(2-eta) order
    # when eta=1/2, so constants can leave no positive conclusion.
    sublinear_pairs = 1_000 * 1_000
    assert virtual_lower_bound(sublinear_pairs, F(1, 2), F(100**3)) < 0

    # Incorrectly charging a fixed quadratic pruning budget can erase the gain.
    pruning_loss = F(3, 100) * diameter**2
    assert alpha * beta * gap * diameter**2 - error - pruning_loss < 0


def main() -> None:
    check_pair_partition()
    check_high_defect_count()
    check_positive_and_failure_controls()
    print("PASS: exact-rational algebra and scale controls; geometry not certified")


main()
