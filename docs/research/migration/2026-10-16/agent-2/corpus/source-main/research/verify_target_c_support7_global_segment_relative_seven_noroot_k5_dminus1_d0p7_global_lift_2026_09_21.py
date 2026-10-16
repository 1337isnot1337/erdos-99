#!/usr/bin/env python3
"""Arithmetic certificate for the final seven-no-root k=5 closure.

This file checks the numerical endpoint of the global virtual-canonical lift
proved in the companion note.  The structural inputs are established by the
committed exact six-row k=4 containment theorem and the preceding all-pair
synchronization note:

* every one-row deletion is a synchronized six-row rank-two state;
* only root patterns B and C remain;
* B has (p,q_i,d_i)=(7,6,2) for every deletion i;
* C has (p,q_i,d_i)=(7,7,3) for every deletion i.

The lift proves C_i subset C_7, hence d_7 >= d_i, and proves that all seven-row
external canonical relations lie in H(C_7).  Every incomplete block counted by
q_i in all deletions is globally virtual-complete, so q_7 is respectively 6
or 7.  The standard containment accounting then gives

    D_7 >= 7 + p + 3*d_7 - 3*q_7.

Both patterns have lower bound 2, contradicting the target D_7=-1.
"""

TARGET_D = -1
T = 7
PATTERNS = {
    "B_five_singletons_one_pair": {
        "p": 7,
        "global_q": 6,
        "deletion_deficiency": 2,
    },
    "C_seven_singletons": {
        "p": 7,
        "global_q": 7,
        "deletion_deficiency": 3,
    },
}


def containment_lower_bound(t, p, deficiency, q):
    return t + p + 3 * deficiency - 3 * q


def main():
    bounds = {}
    for name, data in PATTERNS.items():
        # Row-nullity monotonicity under C_i subset C_7 gives this global
        # deficiency lower bound.
        d7_min = data["deletion_deficiency"]
        bound = containment_lower_bound(
            T, data["p"], d7_min, data["global_q"]
        )
        bounds[name] = bound
        assert bound == 2, (name, bound)
        assert bound > TARGET_D, (name, bound, TARGET_D)

    assert set(bounds.values()) == {2}
    print("PASS: final seven-no-root k=5 global-lift arithmetic")
    print("target_defect", TARGET_D)
    print("pattern_bounds", bounds)
    print("surviving_patterns", 0)


if __name__ == "__main__":
    main()
