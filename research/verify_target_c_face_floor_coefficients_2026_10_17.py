#!/usr/bin/env python3
"""Exact algebra and rational-constant replay for the Target C face floor.

This checks identities used in the proof reconstruction and the strict collar
coefficient comparison. It does not certify the geometric or limiting lemmas.
"""

from fractions import Fraction
from math import pi, sqrt


def linear(**terms):
    return {name: Fraction(value) for name, value in terms.items() if value}


def add(*forms):
    result = {}
    for form in forms:
        for name, value in form.items():
            result[name] = result.get(name, Fraction(0)) + value
    return {name: value for name, value in result.items() if value}


def scale(value, form):
    value = Fraction(value)
    return {name: value * coefficient for name, coefficient in form.items()
            if value * coefficient}


def require(condition, message):
    if not condition:
        raise SystemExit("FAIL: " + message)


q, k, z, p, f, Q = (linear(**{name: 1}) for name in ("q", "k", "z", "p", "f", "Q"))
q_minus_k = add(q, scale(-1, k))

# Theorem-state identities: b+Q=2(q-k), b=p+z, and T=q-k+2f.
Q_from_loaded_hull = add(scale(2, q_minus_k), scale(-1, p), scale(-1, z))
T = add(q_minus_k, scale(2, f))
require(scale(2, T) == add(scale(2, q_minus_k), scale(4, f)),
        "complete-train terminal count")

# Q>=f gives the face-floor conversion with no dropped k, z, or perimeter term.
face_numerator = add(scale(2, q_minus_k), scale(-1, k), scale(-1, z))
face_decomposition = add(p, f, scale(-1, k), Q_from_loaded_hull, scale(-1, f))
require(face_numerator == face_decomposition,
        "2(q-k)-k-z = p+(f-k)+(Q-f)")

# Exact incidence algebra. Let r>=0 be boundary-component edge surplus over
# vertices-minus-one, and s>=0 the excess of interior face degree excess over
# one per interior exceptional face. The boundary atomic-end count is a>=0.
fp, c, r, s = (linear(**{name: 1}) for name in ("f_boundary", "c_boundary", "r", "s"))
A_plus_Ni = add(scale(2, f), scale(-1, fp), scale(-1, k), c, scale(-1, r))
a_boundary = add(scale(3, fp), scale(-1, f), scale(-2, k),
                 scale(2, c), scale(-1, s), scale(-2, r))
slack_identity = add(scale(5, add(f, scale(-1, k), c)),
                     scale(-3, A_plus_Ni))
require(slack_identity == add(a_boundary, s, scale(5, r)),
        "3(A+N_interior) <= 5(f-k+c_boundary) slack identity")

# Exact strict comparison: pi<22/7 and sqrt(3)<7/4 imply
# 25*pi*sqrt(3)<275/2<162, equivalent to 3*s2/5>pi/6.
pi_upper = Fraction(22, 7)
sqrt3_upper = Fraction(7, 4)
product_upper = 25 * pi_upper * sqrt3_upper
require(product_upper == Fraction(275, 2), "rational upper-bound product")
require(product_upper < 162, "strict collar comparison")

value = pi / 2 + 3 * sqrt(pi / (2 * sqrt(3))) / 5
print("PASS: train-count, coefficient, and incidence identities are exact")
print(f"PASS: 25*(22/7)*(7/4) = {product_upper} < 162")
print(f"PASS: pi/2 + 3*s2/5 = {value:.12f} > 2*pi/3")
print("LIMIT: geometric compactness and asymptotic source hypotheses are not checked")
