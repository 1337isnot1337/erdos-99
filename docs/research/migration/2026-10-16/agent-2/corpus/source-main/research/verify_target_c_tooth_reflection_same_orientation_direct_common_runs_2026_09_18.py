#!/usr/bin/env python3
"""Regression checks for same-orientation far-pair direct common runs."""

from __future__ import annotations

import math
import random


def check_majority_far_pair() -> None:
    random.seed(12345)
    for threshold in (3, 4, 10, 101):
        for _ in range(1000):
            # threshold+1 distinct participating module indices in normal order.
            indices = sorted(
                random.sample(range(0, 10 * (threshold + 1)), threshold + 1)
            )
            labels = [random.randrange(2) for _ in indices]
            count0 = labels.count(0)
            count1 = len(labels) - count0
            majority = 0 if count0 >= count1 else 1
            cls = [idx for idx, label in zip(indices, labels) if label == majority]

            assert len(cls) >= math.ceil((threshold + 1) / 2)
            assert cls[-1] - cls[0] >= len(cls) - 1
            assert cls[-1] - cls[0] >= (threshold - 1) / 2


def check_tuned_scaling() -> None:
    # S=sqrt(D)/(Z+1). With m~omega^2, H~omega, gamma~omega^-2,
    # the direct common-run matching has q~S^2/omega^4 and the normal
    # gap has theta~omega^-1. The optimized currency is S/omega^(5/2).
    for s_scale in (1e8, 1e16, 1e32, 1e64):
        omega = math.log(math.log(s_scale + math.e**math.e))
        module_count = omega**2
        threshold = module_count / omega
        q = s_scale**2 / module_count**2
        theta = 1.0 / omega
        a = theta  # asymptotic stand-in for 2 sin(theta/2)
        target = math.sqrt(a * q)
        expected = s_scale / omega**2.5

        assert math.isclose(threshold, omega, rel_tol=1e-12)
        assert math.isclose(target, expected, rel_tol=1e-12)
        assert q > 1.0
        assert target > 1.0
        assert omega**2 < s_scale
        assert omega**2.5 < s_scale


def check_abstract_minimax() -> None:
    for q in (100.0, 1e4, 1e8):
        for a in (0.001, 0.01, 0.1, 1.0):
            threshold = math.sqrt(q / a)
            target = math.sqrt(a * q)
            trunk = a * threshold - a / 2.0
            cycle = q / threshold - 1.0

            assert math.isclose(a * threshold, target, rel_tol=1e-12)
            assert math.isclose(cycle + 1.0, target, rel_tol=1e-12, abs_tol=1e-12)
            assert trunk >= target - max(1.0, a)


def check_run_pair_pigeonhole() -> None:
    # M common matching edges are distributed among at most (Z+1)^2 run pairs.
    for matching_size in (100, 1000, 10_000):
        for external_count in (0, 1, 4, 9):
            cells = (external_count + 1) ** 2
            lower = math.ceil(matching_size / cells)
            assert lower >= matching_size / cells


def main() -> None:
    check_majority_far_pair()
    check_tuned_scaling()
    check_abstract_minimax()
    check_run_pair_pigeonhole()
    print("PASS: same-orientation far-pair direct common-run certificate")


if __name__ == "__main__":
    main()
