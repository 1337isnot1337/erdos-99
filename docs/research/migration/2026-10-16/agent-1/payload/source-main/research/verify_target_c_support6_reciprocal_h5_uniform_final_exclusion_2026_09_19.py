#!/usr/bin/env python3
"""Exact certificate excluding the final three uniform noncollapsed H5 orbits.

This imports the already certified affine raw-triangle-angle machinery, then proves
three sparse coefficient identities forcing the same normalized turn functional D=2.
The audited adjacent-turn theorem gives each of three physical adjacent pairs >2/3,
while strict ground convexity gives the remaining contribution >0, so D>2.

All coefficient checks and evaluations below use integer arithmetic only.
"""

import importlib.util
from pathlib import Path

BASE_PATH = Path(__file__).with_name(
    "verify_target_c_support6_reciprocal_h5_triangle_angle_signature_collapse_2026_09_18.py"
)
spec = importlib.util.spec_from_file_location("h5_angle", BASE_PATH)
H = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(H)

# D = x00+x01 +(x13+x14) +(x24+x20) +(x30+x31).
D_VARS = (
    (0, 0), (0, 1),
    (1, 3), (1, 4),
    (2, 4), (2, 0),
    (3, 0), (3, 1),
)

# Sparse combinations C of full affine F_i and T_ijk functionals.
# In every case the exact coefficient identity is C = -D + const.
COMBOS = {
    1: [
        (-1, "F2"), (+2, "F3"), (-1, "F6"),
        (-1, "T013"), (-1, "T023"), (-1, "T026"),
        (+1, "T036"), (-1, "T124"), (+1, "T135"),
        (-1, "T145"), (+1, "T246"), (-1, "T356"),
        (-1, "T456"),
    ],
    2: [
        (-1, "F1"), (-1, "F2"),
        (-1, "T012"), (-1, "T023"),
    ],
    3: [
        (+1, "F0"), (-1, "F3"), (-1, "F4"), (+2, "F5"),
        (-1, "T015"), (-1, "T036"), (+1, "T056"),
        (-1, "T124"), (+1, "T145"), (-1, "T236"),
        (+1, "T246"), (-1, "T456"),
    ],
}

for case in (1, 2, 3):
    face_cycles = {0: H.GROUND_FORCE, **H.CASES[case]}

    funcs = {f"F{i}": H.face_affine(face_cycles, i) for i in range(7)}
    for a in range(7):
        for b in range(a + 1, 7):
            for c in range(b + 1, 7):
                if any(
                    H.edge(*e) in H.MISSING
                    for e in ((a, b), (a, c), (b, c))
                ):
                    continue
                funcs[f"T{a}{b}{c}"] = H.triangle_affine(
                    case, face_cycles, a, b, c
                )

    D_row = {v: 1 for v in D_VARS}
    combo_row = {}
    combo_const = 0
    combo_exact_value = 0

    for coeff, name in COMBOS[case]:
        row, const = funcs[name]
        combo_row = H.add(combo_row, row, coeff)
        combo_const += coeff * const
        combo_exact_value += coeff * (2 if name.startswith("F") else 1)

    # Exact affine identity: C = -D + combo_const.
    assert combo_row == H.scaled(D_row, -1), (
        case,
        "coefficient identity failed",
    )

    # On every candidate realization F_i=2 and T_ijk=1, so
    # combo_exact_value = -D + combo_const.
    forced_D = combo_const - combo_exact_value
    assert forced_D == 2, (
        case,
        combo_const,
        combo_exact_value,
        forced_D,
    )

    print(f"P{case}: exact face/triangle identities force D={forced_D}")

# The remaining contradiction is exact and strict:
#   x00+x01 > 0                         (strict convex ground hexagon)
#   x13+x14 > 2/3
#   x24+x20 > 2/3
#   x30+x31 > 2/3                       (audited adjacent-turn theorem)
# Hence D > 2, contradicting the exact D=2 above.
print("strict source inequalities force D > 0 + 3*(2/3) = 2")
print(
    "PASS: all three remaining uniform noncollapsed H5 support-six orbits "
    "are excluded."
)
