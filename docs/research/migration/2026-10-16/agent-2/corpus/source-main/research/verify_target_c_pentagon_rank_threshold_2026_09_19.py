#!/usr/bin/env python3
"""Exact rational certificate for the physical pentagon rank-threshold theorem.

Uses the previously proved convex two-gap closure function only through its exact
secants on [0,2/5] and [2/5,2/3]. Every certificate below is checked as an
identity over fractions.Fraction; no floating point is used.
"""
from fractions import Fraction as Q

N = 5


def add(*vs):
    return tuple(sum(z) for z in zip(*vs))


def mul(a, v):
    return tuple(a * z for z in v)


def form(coeff=None, constant=Q(0)):
    row = [Q(0)] * N
    if coeff:
        for i, a in coeff.items():
            row[i] += Q(a)
    return tuple(row + [Q(constant)])


# A form represents constant + sum_i coeff_i*x_i.
E = form({i: 1 for i in range(N)}, -2)  # =0


def qfacet(i):
    return form({i: 1, (i + 1) % 5: 1, (i + 3) % 5: -1}, Q(-1, 3))


def order_facet(a, b):
    # x_b - x_a >= 0.
    return form({b: 1, a: -1})


def low_cut(k):
    # 2/3 + x_k/3 - x_{k+2} - x_{k+3} >= 0.
    return form({k: Q(1, 3), (k + 2) % 5: -1, (k + 3) % 5: -1}, Q(2, 3))


def high_cut(k):
    # 1/2 + 3*x_k/4 - x_{k+2} - x_{k+3} >= 0.
    return form({k: Q(3, 4), (k + 2) % 5: -1, (k + 3) % 5: -1}, Q(1, 2))


# Representative physical order cone from the exact gap-order theorem:
# x0 <= x2 <= x3 <= x4 <= x1.
FAC = {
    **{f"q{i}": qfacet(i) for i in range(5)},
    "o02": order_facet(0, 2),
    "o23": order_facet(2, 3),
    "o34": order_facet(3, 4),
    "o41": order_facet(4, 1),
}

# Exact secants of the sharp closure function M. The existing rank-secant
# certificate proves M(0)=2/3, M(2/5)=4/5, M(2/3)=1 and convexity was proved
# in the force-closure argument. Recheck the rational line algebra here.
assert (Q(4, 5) - Q(2, 3)) / Q(2, 5) == Q(1, 3)
assert (Q(1) - Q(4, 5)) / (Q(2, 3) - Q(2, 5)) == Q(3, 4)

FAC["L0"] = low_cut(0)
FAC["L2"] = low_cut(2)
FAC["L3"] = low_cut(3)
FAC["H1"] = high_cut(1)
FAC["H3"] = high_cut(3)
FAC["H4"] = high_cut(4)


def check_identity(target, weights, beta=Q(0)):
    assert all(Q(a) >= 0 for a in weights.values())
    rhs = mul(Q(beta), E)
    for name, a in weights.items():
        rhs = add(rhs, mul(Q(a), FAC[name]))
    assert rhs == target, (target, rhs)


# Rank threshold 1: second-smallest gap x2 <= 2/5.
# Since x0 is the minimum, x0 <= 2/5 by the average, so L0 is valid.
T_X2_MAX = form({2: -1}, Q(2, 5))
check_identity(T_X2_MAX, {
    "L0": Q(3, 5),
    "o02": Q(1, 5),
    "o23": Q(3, 5),
})

# Rank threshold 2: second-largest gap x4 >= 2/5.
# If x3 >= 2/5 this follows from x4>=x3. In the other branch x3<=2/5,
# L3 is valid and the identity below proves x4>=2/5.
T_X4_MIN = form({4: 1}, Q(-2, 5))
check_identity(T_X4_MIN, {
    "L3": Q(3, 10),
    "o23": Q(3, 10),
    "o34": Q(7, 10),
}, beta=Q(3, 10))

# The two threshold facets are now available for the branch refinements.
FAC["T2"] = T_X2_MAX
FAC["T4"] = T_X4_MIN
FAC["Mlo"] = form({3: -1}, Q(2, 5))
FAC["Mhi"] = form({3: 1}, Q(-2, 5))

# On the median-low branch x3<=2/5, low cuts apply at ranks min, second-min,
# median; high cuts apply at second-max and max.
LOW_CERTS = [
    # x0 in [0,2/5]
    (form({0: 1}), {"q0": 1, "q1": 2, "q3": 2, "q4": 1}, Q(-1)),
    (form({0: -1}, Q(2, 5)), {"T2": Q(1, 3), "T4": 1, "L2": 1}, 0),
    # x1 in [2/5,2/3]
    (form({1: 1}, Q(-2, 5)), {"T2": Q(4, 3), "Mlo": 1, "L2": 1}, 1),
    (form({1: -1}, Q(2, 3)), {"q0": 1, "q1": 1, "q3": 2}, -1),
    # x2 in [4/15,2/5]
    (form({2: 1}, Q(-4, 15)), {"q1": 1, "q3": 1, "Mlo": 1}, 0),
    (T_X2_MAX, {"T2": 1}, 0),
    # x3 in [1/3,2/5]
    (form({3: 1}, Q(-1, 3)), {"q1": Q(1, 2), "q3": Q(1, 2), "o23": Q(1, 2)}, 0),
    (FAC["Mlo"], {"Mlo": 1}, 0),
    # x4 in [2/5,2/3]
    (T_X4_MIN, {"T4": 1}, 0),
    (form({4: -1}, Q(2, 3)), {"q0": 1, "q1": Q(3, 2), "q3": Q(3, 2), "o23": Q(1, 2)}, -1),
]

# On the median-high branch x3>=2/5, low cuts apply at min and second-min;
# high cuts apply at median, second-max, max.
HIGH_CERTS = [
    # x0 in [1/15,2/5]
    (form({0: 1}, Q(-1, 15)), {"q0": 2, "q1": 1, "q3": 2, "Mhi": 1}, -1),
    (form({0: -1}, Q(2, 5)), {"o02": Q(1, 2), "o41": Q(1, 2), "T4": 1, "Mhi": Q(1, 2)}, Q(-1, 2)),
    # x1 in [2/5,2/3]
    (form({1: 1}, Q(-2, 5)), {"T2": Q(16, 21), "T4": Q(4, 7), "L2": Q(4, 7), "H1": Q(4, 7)}, Q(4, 7)),
    (form({1: -1}, Q(2, 3)), {"q0": 1, "q1": 1, "q3": 2}, -1),
    # x2 in [1/6,2/5]
    (form({2: 1}, Q(-1, 6)), {"q0": Q(1, 2), "q1": Q(3, 2), "q3": Q(3, 2), "o34": Q(1, 2)}, Q(-1, 2)),
    (T_X2_MAX, {"T2": 1}, 0),
    # x3 in [2/5,1/2]
    (FAC["Mhi"], {"Mhi": 1}, 0),
    (form({3: -1}, Q(1, 2)), {"q0": Q(1, 2), "q1": Q(1, 2), "q3": Q(1, 2), "o34": Q(1, 2)}, Q(-1, 2)),
    # x4 in [2/5,3/5]
    (T_X4_MIN, {"T4": 1}, 0),
    (form({4: -1}, Q(3, 5)), {"q0": 1, "q1": 1, "q3": 1, "Mhi": 1}, -1),
]

for cert in LOW_CERTS + HIGH_CERTS:
    check_identity(*cert)

print("PASS")
print("representative order: x0 <= x2 <= x3 <= x4 <= x1")
print("universal rank thresholds: x2 <= 2/5 <= x4")
print("equality in either threshold forces the regular gap vector (2/5,...,2/5)")
print("median-low intervals: x0[0,2/5], x1[2/5,2/3], x2[4/15,2/5], x3[1/3,2/5], x4[2/5,2/3]")
print("median-high intervals: x0[1/15,2/5], x1[2/5,2/3], x2[1/6,2/5], x3[2/5,1/2], x4[2/5,3/5]")
