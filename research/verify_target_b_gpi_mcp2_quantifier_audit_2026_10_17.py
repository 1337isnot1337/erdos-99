#!/usr/bin/env python3
"""Replay arithmetic margins for the Target B GPI/MCP2 scope audit.

This checks numerical inequalities and the example rational exponents only.
It does not verify any geometric or asymptotic theorem.
"""

from decimal import Decimal, getcontext
from fractions import Fraction


getcontext().prec = 60
D = Decimal


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


sqrt3 = D(3).sqrt()
pi = D("3.14159265358979323846264338327950288419716939937510")
mu0 = D("8e-5")
gamma0 = D(3) / 4 - sqrt3 / pi
missing_pair_loss = 4 * sqrt3 * (3 * mu0.sqrt() + mu0)
require(missing_pair_loss < D("0.1865"), "uniform missing-pair loss margin")
require(gamma0 > D("0.1986"), "uniform phase margin")
require(gamma0 - missing_pair_loss > D("0.0121"), "residual unique-max margin")

# Under Delta < 4e-17 tau^2, tau <= 1, these are the displayed safe bounds.
delta = D("4e-17")
tau = D(1)
eps_bal_bound = delta / (mu0 * tau * tau) + delta / tau
require(eps_bal_bound < D("6e-13"), "balanced restriction deficit bound")
eps_bal_safe = D("1e-12")
l_grid = 6 * eps_bal_safe ** (D(1) / 4) + 4 * eps_bal_safe.sqrt()
require(l_grid < D("0.00601"), "balanced grid omission bound")

# Eventually 1-s <= 1e-12; then this safe restoration error is valid.
gap = D("1e-12")
l_del = 2 * gap / (1 - gap)
require(l_del < D("3e-12"), "restored-train error bound")
d2_lower = 3 - 4 * sqrt3 * D("0.00601") - 2 * sqrt3 * D("3e-12")
d2_upper = 4 * sqrt3 / pi
require(d2_lower > D("2.95"), "GPI lower diameter margin")
require(d2_upper < D("2.21"), "GPI dominant-core upper diameter margin")

# Fixed-lambda conversion: 4e-17 * (lambda/(2 C_T))^2
# equals 1e-17 * lambda^2/C_T^2 exactly.
lhs = Fraction(4, 10**17) * Fraction(1, 4)
rhs = Fraction(1, 10**17)
require(lhs == rhs, "fixed-lambda GPI coefficient")

eta = Fraction(1, 3)
kappa = Fraction(1, 4)
require(kappa < 1 - eta, "zero-gain-cycle condition in example")
require(2 * kappa + eta < 1, "summed coherence error is o(D^2)")
require(1 - eta > 0 and kappa > 0, "positive pruning exponents")
require(1 + 2 * kappa + eta == Fraction(11, 6), "example total coherence exponent")
require(2 * kappa + eta - 1 == Fraction(-1, 6), "example normalized coherence exponent")
require(min(eta, kappa) == Fraction(1, 4), "example deletion rate")

print("PASS: GPI decimal margins and fixed-lambda coefficient")
print("PASS: eta=1/3, kappa=1/4 gives normalized coherence O(D^-1/6)")
print("PASS: diagonal deletion exponents are eta=1/3 and kappa=1/4")
print("LIMIT: arithmetic only; geometric and source hypotheses are not checked")
