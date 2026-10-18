#!/usr/bin/env python3
"""Fresh review controls for pinned Erdős99 PR86/88/93/94.

No submitted proof or checker is imported. The finite tests are adversarial
controls; the accompanying review receipt contains the mathematical audit.
"""

from fractions import Fraction as F
from itertools import combinations, product
import json


def require(value, message):
    if not value:
        raise ValueError(message)


def arctan_bounds(x, pairs):
    """Integrate alternating geometric sums; return exact even/odd brackets."""
    power = x
    partial = F(0)
    for k in range(2 * pairs):
        partial += power / (2 * k + 1)
        power *= -x * x
    return partial, partial + power / (4 * pairs + 1)


def gpi_margins():
    a8, a9 = arctan_bounds(F(1, 5), 4)
    b2, b3 = arctan_bounds(F(1, 239), 1)
    b4, _ = arctan_bounds(F(1, 239), 2)
    a6, a7 = arctan_bounds(F(1, 5), 3)
    submitted_pi_lower = 16 * a7 - 4 * b2
    corrected_pi_lower = 16 * a8 - 4 * b3
    rigorous_pi_upper = 16 * a9 - 4 * b4
    require(submitted_pi_lower > rigorous_pi_upper,
            "PR93 parity counterexample was not detected")
    require(corrected_pi_lower < rigorous_pi_upper,
            "independent pi bracket is inverted")
    require(corrected_pi_lower > F(314159, 100000),
            "corrected pi lower bound too small")
    r3 = F(1732051, 1000000)
    rmu = F(89443, 10000000)
    mu = F(8, 100000)
    require(r3 * r3 > 3 and rmu * rmu > mu, "root upper bounds")
    cupper = 2 * r3 / corrected_pi_lower
    gamma = F(3, 4) - cupper / 2
    loss = 4 * r3 * (3 * rmu + mu)
    require(loss < F(1865, 10000) < gamma, "missing-pair margin")
    imbalance = F(5, 10**13)
    require(F(4, 10**17) / mu == imbalance, "imbalance coefficient")
    require(imbalance + F(4, 10**17) < F(6, 10**13), "balanced deficit")
    restore = 2 * imbalance / (1 - imbalance)
    require(restore < F(3, 10**12), "restored-train error")
    grid = F(601, 100000)
    lower = 3 - 4 * r3 * grid - 2 * r3 * F(3, 10**12) - F(1, 10**10)
    # Include the original size imbalance, unlike the baseline-only PR94 check.
    upper = 2 * cupper / (1 - imbalance)**2
    require(lower > F(295, 100) and upper < F(221, 100), "GPI diameter gap")
    eta, kappa = F(1, 3), F(1, 4)
    require(kappa + eta < 1 and 2 * kappa + eta < 1, "diagonal conditions")
    require(1 + 2*kappa + eta == F(11, 6), "total diagonal exponent")
    return {
        "submitted_PR93_pi_bound_is_above_a_rigorous_upper_bound": True,
        "minimum_excess_above_pi": str(submitted_pi_lower-rigorous_pi_upper),
        "corrected_pi_lower": str(corrected_pi_lower),
        "corrected_all_GPI_margins_pass": True,
        "diameter_lower_approx": float(lower),
        "diameter_upper_including_imbalance_approx": float(upper),
        "diagonal_total_exponent": "11/6",
        "diagonal_normalized_exponent": "-1/6",
    }


def interface_physical_subsets():
    """Optimize over physical presence before assigning charges.

    This model differs from the submission's five-state charge histogram.
    A lower demand is feasible exactly when enough incident edges are present.
    """
    configurations = physical_sets = demands = 0
    for shared, private_a, private_b in product(range(6), range(4), range(4)):
        bins = set()
        for present in product((0, 1), repeat=shared+private_a+private_b):
            i = sum(present[:shared])
            ca = sum(present[shared:shared+private_a])
            cb = sum(present[shared+private_a:])
            bins.add((i+ca+cb, i+ca, i+cb, i))
            physical_sets += 1
        for p, q, cap in product(range(shared+private_a+1),
                                 range(shared+private_b+1), range(shared+1)):
            admissible = [cost for cost, pa, pb, i in bins
                          if i == cap and pa >= p and pb >= q]
            oracle = min(admissible) if admissible else None
            expected = (cap+max(0,p-cap)+max(0,q-cap)
                        if p <= cap+private_a and q <= cap+private_b else None)
            require(oracle == expected, "exact shared-count optimum")
            admissible = [cost for cost, pa, pb, i in bins
                          if i <= cap and pa >= p and pb >= q]
            oracle = min(admissible) if admissible else None
            expected = (max(p,q,p+q-cap)
                        if p <= cap+private_a and q <= cap+private_b else None)
            require(oracle == expected, "upper shared-cap optimum")
            demands += 1
        configurations += 1
    require(max(1,0,0,-1) > 0, "cap-is-actual counterexample")
    return {"inventories": configurations, "physical_subsets": physical_sets,
            "exact_and_cap_demand_cases_each": demands,
            "includes_zero_inventory_and_zero_demand": True}


def tripartite_graphs():
    """Exhaust small unequal graphs and balance by actual vertex subsets."""
    records = []
    for M,b,a in ((2,2,2),(3,2,1),(3,2,2)):
        shores = [range(M), range(M,M+b), range(M+b,M+b+a)]
        pairs = [list(product(shores[i], shores[j])) for i,j in ((0,1),(0,2),(1,2))]
        edges = [edge for family in pairs for edge in family]
        triangle_free = 0
        for mask in range(1 << len(edges)):
            chosen = {edge for bit, edge in enumerate(edges) if mask >> bit & 1}
            if any((aa,bb) in chosen and (aa,cc) in chosen and (bb,cc) in chosen
                   for aa,bb,cc in product(*shores)):
                continue
            counts = [sum(e in chosen for e in family) for family in pairs]
            x,y,z = M*b-counts[0],M*a-counts[1],counts[2]
            require(M*z <= a*x+b*y, "transversal triple charge inequality")
            balanced_counts = []
            for AA,BB in product(combinations(shores[0],a),combinations(shores[1],a)):
                kept = set(AA)|set(BB)|set(shores[2])
                balanced_counts.append(sum(u in kept and v in kept for u,v in chosen))
            require(max(balanced_counts)*M*b >= a*a*sum(counts),
                    "random-balanced-restriction bound")
            if M==b==a:
                epsilon_numerator = 2*a*a-sum(counts)
                missing = min(a*a-e for e in counts)
                require(missing*missing <= 16*epsilon_numerator*a*a,
                        "balanced 4 sqrt(epsilon) stability control")
            triangle_free += 1
        records.append({"shape":[M,b,a],"all_graphs":1 << len(edges),
                        "triangle_free_graphs":triangle_free})
    return records


def separable_controls():
    # Cutoff identity in Q(sqrt(3)): multiply by the squared denominator.
    # (24+14r)*4*(1-r/2)^2 = 2r for r^2=3.
    constant = 7*24 - 4*14*3
    radical = 7*14 - 4*24
    require((constant,radical)==(0,2), "exact cutoff rationalization")
    cutoff = F(22,7)*(24+14*F(26,15))
    require(cutoff == F(15928,105) < 152, "integer cutoff")
    # For all integer offsets, q-(1-c)(a^2+b^2)=c(a+b)^2.
    # Check the identity on non-submitted sizes and mixed-sign large offsets.
    checks = 0
    for m in (2,3,17,127,1024):
        c = F(m*m-1,2*m*m)
        for a,b in product((-m,-2,-1,0,1,2,m), repeat=2):
            q = a*a+b*b+2*c*a*b
            require(q-(1-c)*(a*a+b*b)==c*(a+b)**2, "pair lower identity")
            if a and b:
                require(q >= 2*(1-c) > 1, "mixed offset separation")
            elif a or b:
                require(q >= 1, "axis separation")
            checks += 1
        require(2*m*m*(1+c)==3*m*m-1>2*m*m, "strict square competitor")
        require(F(1,2)-c==F(1,2*m*m)<F(1,2), "third disk cuts unique separator")
    return {"cutoff_upper": str(cutoff), "algebraic_identity_checks": checks,
            "all_size_proof_is_in_review_receipt": True}


if __name__ == "__main__":
    print(json.dumps({"PR86": interface_physical_subsets(),
                      "PR88": separable_controls(),
                      "PR93_PR94_graphs": tripartite_graphs(),
                      "PR93_PR94_constants": gpi_margins()}, indent=2))
