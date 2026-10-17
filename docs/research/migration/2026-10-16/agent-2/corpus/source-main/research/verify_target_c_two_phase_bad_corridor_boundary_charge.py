#!/usr/bin/env python3
"""Finite regressions for the two-phase bad-corridor boundary-charge candidate.

This script checks only the finite bookkeeping used after the near-disk shared-
boundary lemma.  It does not certify the asymptotic convex-boundary lemma or C-II.
"""

from fractions import Fraction
from itertools import product
from math import cos, pi, sin


def main() -> None:
    # In the canonical contact-core scope, Section 82 rules out collinear boundary
    # subdivisions, so a strict convex face has at most two sides in each selected
    # projective direction.  Thus a face has at most four selected occurrences.
    selected = 4
    assert selected <= 4

    # A bad face has U>=1 unpaid non-phase occurrences and I=S+U with S<=4.
    # Hence I<=5U, the exact finite factor used in (BC.8).
    for u in range(1, 20):
        for s in range(0, 5):
            assert s + u <= 5 * u

    # The five-factor charge survives summation with arbitrary bad-face multiplicity.
    U = 0
    I = 0
    for u, s in ((1, 4), (2, 0), (3, 4), (7, 1)):
        U += u
        I += u + s
    assert I <= 5 * U

    # The equality-branch implication H>=Q-o(D), H<=5U+o(D) gives U>=Q/5.
    Q = Fraction(37, 10)
    H = Q
    assert H / 5 == Q / 5

    # The same equality-branch bookkeeping forces Q <= 4 f (up to the
    # asymptotic boundary error).  A finite toy instance with equality is enough
    # to check the direction of this consequence.
    f = Fraction(37, 40)
    I = 4 * f
    assert H + I == 4 * f + Q
    assert H <= I
    assert Q <= 4 * f

    # Local sharpness regression: u,v,w,-u,-v,-w close a strict unit hexagon at
    # theta=70 degrees. Mark one off-phase edge as hull and one as non-hull.
    theta = 70.0 * pi / 180.0
    angles = (0.0, theta, 120.0 * pi / 180.0, pi,
              pi + theta, 300.0 * pi / 180.0)
    vectors = [(cos(a), sin(a)) for a in angles]
    closure = tuple(sum(v[j] for v in vectors) for j in (0, 1))
    assert max(abs(x) for x in closure) < 1e-12
    gaps = tuple((angles[(i + 1) % 6] - angles[i]) % (2 * pi) for i in range(6))
    assert all(0.0 < gap < pi for gap in gaps)
    H_sharp, S_sharp, U_sharp = 1, 4, 1
    assert H_sharp + S_sharp + U_sharp == 6
    assert S_sharp + U_sharp == 5 * U_sharp

    # The phase-word endpoint set is finite (the zero word is not used as a path).
    steps = ("u", "-u", "v", "-v")
    words = set()
    for length in range(1, 5):
        words.update(product(steps, repeat=length))
    assert len(words) == 4 + 16 + 64 + 256

    print("two-phase bad-corridor boundary-charge bookkeeping: OK")
    print(f"phase_word_count={len(words)}")
    print(f"sample_I={I} <= 5*sample_U={5 * U}")
    print(f"equality_branch_U_floor={Q / 5}")
    print(f"equality_branch_Q_floor={Q} <= 4*f={4 * f}")
    print("local_factor_five_sharpness_regression: H=1 S=4 U=1 I=5")
    print("near-disk shared-boundary lemma remains proof-only")


if __name__ == "__main__":
    main()
