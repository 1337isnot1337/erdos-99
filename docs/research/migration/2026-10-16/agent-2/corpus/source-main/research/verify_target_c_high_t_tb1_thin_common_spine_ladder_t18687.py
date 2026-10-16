#!/usr/bin/env python3
"""Regression checks for the THIN common-spine ladder theorem."""

from __future__ import annotations

import itertools
import math
from fractions import Fraction


def check_constants() -> None:
    gamma = Fraction(791, 9_600_000_000)
    p0 = Fraction(1609, 2500)
    tstar = Fraction(6121, 2000)

    kappa = 3 * p0 / (10 * tstar)
    assert kappa == Fraction(9654, 153025)
    assert abs(float(kappa) - 0.06308773076294723) < 1e-16

    dcoef_before_phase = kappa * gamma / 16
    assert dcoef_before_phase == Fraction(1_272_719, 3_917_440_000_000_000)
    assert abs(float(dcoef_before_phase) - 3.248853843326254e-10) < 1e-24

    dcoef_after_phase = kappa * gamma / 32
    assert dcoef_after_phase == Fraction(1_272_719, 7_834_880_000_000_000)
    assert abs(float(dcoef_after_phase) - 1.624426921663127e-10) < 1e-24


def check_defect_threshold() -> None:
    gamma = 791.0 / 9_600_000_000.0
    cphase = math.pi**2 * math.sqrt(3.0) * (2.0 + math.sqrt(3.0)) / 12.0
    hthin = 16.0 * cphase / (3.0 * gamma)
    h0 = 32.0 * cphase / (3.0 * gamma) + 1.0
    assert abs(hthin - 344128111.92503613) < 1e-5
    assert h0 > 2.0 * hthin

    # With F_a <= H0, deleting defects >100 H0/D removes at most 0.01 D columns.
    for D in [1e3, 1e6, 1e9]:
        threshold = 100.0 * h0 / D
        max_bad = h0 / threshold
        assert max_bad <= 0.01 * D * (1.0 + 1e-14)


def check_markov_half() -> None:
    # Finite integer sanity: at least half the entries are <= 2 times the average.
    for q in range(1, 7):
        for vals in itertools.product(range(5), repeat=q):
            avg = sum(vals) / q
            good = sum(v <= 2.0 * avg + 1e-15 for v in vals)
            assert good >= math.ceil(q / 2)


def check_triple_pigeonhole() -> None:
    # Exhaust a small incidence model. Rows choose blockers and columns independently.
    # The max blocker-column codegree is at least ceil(total triples/(N*T)).
    n_blockers = 3
    n_cols = 4
    n_rows = 4
    blocker_choices = list(itertools.combinations(range(n_blockers), 1))
    col_choices = list(itertools.combinations(range(n_cols), 2))
    row_types = [(bs, cs) for bs in blocker_choices for cs in col_choices]

    for rows in itertools.product(row_types, repeat=n_rows):
        counts = [[0 for _ in range(n_cols)] for _ in range(n_blockers)]
        triples = 0
        for bs, cs in rows:
            triples += len(bs) * len(cs)
            for e in bs:
                for b in cs:
                    counts[e][b] += 1
        max_codeg = max(max(r) for r in counts)
        assert max_codeg >= math.ceil(triples / (n_blockers * n_cols))


def check_two_phase_split() -> None:
    for n in range(1, 20):
        for k in range(n + 1):
            assert max(k, n - k) >= math.ceil(n / 2)


def main() -> None:
    check_constants()
    check_defect_threshold()
    check_markov_half()
    check_triple_pigeonhole()
    check_two_phase_split()
    print("PASS: THIN common-spine ladder certificate")


if __name__ == "__main__":
    main()
