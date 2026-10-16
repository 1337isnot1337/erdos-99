#!/usr/bin/env python3
"""Finite regression checks for the proof-only interval-biclique sharpening.

The theorem under test is:

    e + a >= k(a+b-k+1)

for a bipartite graph with |A|=a, |B|=b and interval neighborhoods on the
ordered B shore implies a K_{k,k} whose B shore is a consecutive k-block.

This script exhausts all interval-row graphs in a bounded small range and also
checks the simpler k=floor(e/(a+b)) corollary.
"""

from __future__ import annotations

from itertools import product


def interval_masks(b: int) -> list[int]:
    masks = [0]
    for left in range(b):
        mask = 0
        for right in range(left, b):
            mask |= 1 << right
            masks.append(mask)
    return masks


def has_consecutive_k_by_k(rows: tuple[int, ...], b: int, k: int) -> bool:
    if k <= 0:
        return True
    for start in range(b - k + 1):
        block = ((1 << k) - 1) << start
        if sum((row & block) == block for row in rows) >= k:
            return True
    return False


def run() -> None:
    checked = 0
    for b in range(1, 7):
        masks = interval_masks(b)
        for a in range(1, 6):
            total = len(masks) ** a
            if total > 2_000_000:
                continue
            for rows in product(masks, repeat=a):
                e = sum(row.bit_count() for row in rows)

                k0 = e // (a + b)
                assert has_consecutive_k_by_k(rows, b, k0)

                for k in range(1, min(a, b) + 1):
                    if e + a >= k * (a + b - k + 1):
                        assert has_consecutive_k_by_k(rows, b, k)

                checked += 1

    print("Target C interval-biclique regression: PASS")
    print(f"exhaustive interval-row graphs checked: {checked}")


if __name__ == "__main__":
    run()
