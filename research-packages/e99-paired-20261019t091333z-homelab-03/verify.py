"""Exact finite controls for the support-aware two-cut statement.

These are abstract stress/row records, not a planar source certificate.
"""
from fractions import Fraction as F


def require(condition, label):
    if not condition:
        raise RuntimeError(label)


def support_average(stresses):
    width = len(stresses[0])
    require(all(len(s) == width for s in stresses), "stress widths disagree")
    require(all(all(x >= 0 for x in s) and sum(s) == 1 for s in stresses),
            "stress is not normalized and nonnegative")
    support = {j for j in range(width) if any(s[j] > 0 for s in stresses)}
    average = tuple(sum((s[j] for s in stresses), F(0)) / len(stresses)
                    for j in range(width))
    require(all(average[j] > 0 for j in support),
            "average missed a stress-reachable row")
    require(all(average[j] == 0 for j in range(width) if j not in support),
            "average activated a structurally zero row")
    return support, average


def sign_table(t, contact_mass_sum, incoming, outgoing):
    require(t != 0 and contact_mass_sum > 0, "invalid phase or cut mass")
    require(incoming >= 0 and outgoing >= 0, "negative flow")
    require(outgoing - incoming == contact_mass_sum * t, "flux identity failed")
    if t > 0:
        require(outgoing > incoming, "positive phase has wrong net flow")
        if incoming > 0:
            require(outgoing > 0, "missing outgoing sign")
            return "supported-both-signs"
        require(incoming == 0 and outgoing > 0, "missing shortening flow")
        return "supported-shortening-only"
    require(incoming > outgoing, "negative phase has wrong net flow")
    if outgoing > 0:
        require(incoming > 0, "missing incoming sign")
        return "supported-both-signs"
    require(outgoing == 0 and incoming > 0, "missing shortening flow")
    return "supported-shortening-only"


def full_graph_class(t, support_case, zero_incoming, zero_outgoing):
    require(zero_incoming >= 0 and zero_outgoing >= 0, "negative zero-row flow")
    if support_case == "supported-both-signs":
        return "full-graph-both-signs"
    if t > 0 and zero_incoming > 0:
        return "full-graph-both-signs"
    if t < 0 and zero_outgoing > 0:
        return "full-graph-both-signs"
    return "full-graph-shortening-only"


def squared_distance_change(s, projection):
    # |r - s w|^2 - |r|^2, with projection r dot w.
    return -2 * s * projection + s * s


def main():
    # A row can be zero in one feasible stress and positive in another.
    stresses = (
        (F(1, 2), F(1, 2), F(0), F(0)),
        (F(1, 3), F(0), F(2, 3), F(0)),
        (F(0), F(1, 4), F(0), F(3, 4)),
    )
    support, average = support_average(stresses)
    require(support == {0, 1, 2, 3}, "finite support union is wrong")
    require(average == (F(5, 18), F(1, 4), F(2, 9), F(1, 4)),
            "finite average is wrong")

    # Rows 2 and 3 are structurally zero in this separate feasible stress set.
    structural = ((F(1), F(0), F(0), F(0)),
                  (F(0), F(1), F(0), F(0)))
    support_zero, average_zero = support_average(structural)
    require(support_zero == {0, 1}, "structural support is wrong")
    require(average_zero == (F(1, 2), F(1, 2), F(0), F(0)),
            "structural zeros were activated")

    # t > 0: positive support has only shortening flow, but a zero row can
    # still move in the lengthening direction. The stress table cannot rule it out.
    case = sign_table(F(1, 3), F(3), F(0), F(1))
    require(case == "supported-shortening-only", "positive phase table failed")
    require(full_graph_class(F(1, 3), case, F(1), F(0)) == "full-graph-both-signs",
            "adverse positive-phase zero row was hidden")
    require(full_graph_class(F(1, 3), case, F(0), F(0))
            == "full-graph-shortening-only",
            "favorable positive-phase zero row was misclassified")

    # t < 0: symmetric structural-zero control.
    case = sign_table(F(-1, 3), F(3), F(1), F(0))
    require(case == "supported-shortening-only", "negative phase table failed")
    require(full_graph_class(F(-1, 3), case, F(0), F(1)) == "full-graph-both-signs",
            "adverse negative-phase zero row was hidden")
    require(full_graph_class(F(-1, 3), case, F(0), F(0))
            == "full-graph-shortening-only",
            "favorable negative-phase zero row was misclassified")

    # Positive support can itself contain both signs.
    require(sign_table(F(1, 2), F(4), F(1), F(3)) == "supported-both-signs",
            "positive phase two-sign case failed")
    require(sign_table(F(-1, 2), F(4), F(3), F(1)) == "supported-both-signs",
            "negative phase two-sign case failed")

    # Exact finite sign: the non-grazing bound is D*s/2 = 5/4.
    D, s = F(10), F(1, 4)
    require(abs(F(2)) > D * s / 2, "non-grazing control failed")
    require(squared_distance_change(s, F(2)) == F(-15, 16)
            and squared_distance_change(s, F(2)) < 0,
            "shortening squared-distance control failed")
    require(squared_distance_change(s, F(-2)) == F(17, 16)
            and squared_distance_change(s, F(-2)) > 0,
            "lengthening squared-distance control failed")

    print("PASS: support-average lemma controls; both phase signs; supported and structural-zero rows; exact finite sign formula.")
    print("LIMIT: abstract finite algebra only; no planar source realization or all-pair endpoint is certified.")


main()
