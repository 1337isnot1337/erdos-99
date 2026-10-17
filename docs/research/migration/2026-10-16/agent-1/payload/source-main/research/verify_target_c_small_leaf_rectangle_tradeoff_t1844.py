#!/usr/bin/env python3
"""Exact rational checks for the t<=1.844 small-leaf rectangle tradeoff."""
from fractions import Fraction as F

P = F(53, 625)       # 0.0848
A = F(73, 100)       # 0.73
C = F(1063, 1000)    # 1.063


def tradeoff(L: F, alpha: F):
    assert 0 < L < A
    G = (A - L) * P / (C - L)
    S = L * G / C
    assert 0 < alpha < S
    beta = L - alpha * C / S
    return G, S, beta


checks = [
    (F(301, 500), F(31, 10000), F(7, 20)),
    (F(23, 40), F(51, 10000), F(1, 5)),
    (F(281, 500), F(13, 2000), F(1, 10)),
    (F(591, 1000), F(19, 5000), F(3, 10)),
]

for L, alpha, beta_safe in checks:
    G, S, beta = tradeoff(L, alpha)
    assert beta > beta_safe
    print("L =", L, "=", float(L))
    print("  good density G >", G, "=", float(G))
    print("  backbone density S >", S, "=", float(S))
    print("  block alpha =", alpha, "=", float(alpha))
    print("  common beta >", beta, "=", float(beta))
    print("  safe beta =", beta_safe, "margin =", beta - beta_safe,
          "=", float(beta - beta_safe))

L = F(591, 1000)
G = (A - L) * P / (C - L)
S = L * G / C
alpha_star = L * S / (2 * C)
beta_star = L / 2
assert alpha_star * beta_star > F(114, 100000)
print("product diagnostic at L=.591:", float(alpha_star), "x", float(beta_star),
      "=", float(alpha_star * beta_star))
print("PASS: exact small-leaf complete-rectangle tradeoff")
