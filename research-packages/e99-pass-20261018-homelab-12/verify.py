"""Exact exponent check for the supplied slow-chart count composition.

This checks arithmetic only. It does not check any geometric theorem or premise.
"""
from fractions import Fraction


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def near_boundary_exponent(rho_decay):
    # The canonical near-boundary estimate is D^(4/5) + D*rho_D.
    return max(Fraction(4, 5), Fraction(1) - rho_decay)


r = Fraction(4, 5)
canonical_anchor_decay = Fraction(1, 2)
proposed_stronger_decay = Fraction(2, 3)

require(Fraction(1, 2) <= r <= 1, "patch radius is outside the local-capacity range")
require(near_boundary_exponent(canonical_anchor_decay) == r,
        "canonical O(D^(-1/2)) anchor error does not fit the D^(4/5) target")
require(near_boundary_exponent(proposed_stronger_decay) == r,
        "the stronger candidate rate should also fit the same target")

# Negative control: a fixed-width boundary error costs order D and cannot be hidden.
require(near_boundary_exponent(Fraction(0)) == 1,
        "nondecaying boundary error must remain visible as a linear term")
require(near_boundary_exponent(Fraction(0)) > r,
        "negative control failed to reject absorption into D^(4/5)")

# Patch count is D/r. Local terms are r*(r/D), r*D^(-1/2), (D*r)^(1/3), and 1.
patch_count = 1 - r
chart_drift_local = r + r - 1
square_root_local = r - Fraction(1, 2)
curvature_local = (1 + r) / 3
constant_local = Fraction(0)

chart_drift_total = patch_count + chart_drift_local
square_root_total = patch_count + square_root_local
curvature_total = patch_count + curvature_local
constant_total = patch_count + constant_local

require(chart_drift_total == r, "chart drift exponent is not D^(4/5)")
require(square_root_total == Fraction(1, 2), "tangency error exponent changed")
require(curvature_total == r, "curved-boundary term is not D^(4/5)")
require(constant_total <= r, "patch-count constant term exceeds D^(4/5)")
require(max(chart_drift_total, square_root_total, curvature_total, constant_total) == r,
        "double-port patch sum does not have exponent 4/5")
require(r < 1, "the covered endpoint error must be sublinear")

print("PASS: exact exponent arithmetic only; geometric premises and proofs are not checked")
