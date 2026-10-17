#!/usr/bin/env python3
"""Low-weight source filter layered onto the Profile B all-clean-fans audit.

The committed unstripped low-weight closure proves that a genuine Profile B
source has d1(P)>=4.  Hence it has no coefficient word of weight at most three
and all eight source coordinates are three-clean.  The global deletion bound
also gives d2(P)>=4.  This wrapper rejects every already-excluded source plane
before the expensive fixed-nine/all-clean-fans work and requires all eight
clean puncture fans for every retained source.
"""

from collections import Counter
from pathlib import Path
import contextlib
import importlib.util
import io

HERE = Path(__file__).resolve().parent
BASE = HERE / "verify_target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_profile_b_all_clean_fans_2026_09_22.py"
spec = importlib.util.spec_from_file_location("e99_profile_b_all_clean", BASE)
G = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(G)

ORIG_CLEAN_FAN_DATA = G.clean_fan_data
LOW_WEIGHT_COUNTS = Counter()


def coefficient_weight_profile(space8):
    """Return exact (d1,d2,zero columns, projective multiplicities)."""
    assert len(space8) == 2
    classes = Counter()
    zeros = []
    for i in range(8):
        a = space8[0][i]
        b = space8[1][i]
        if a == 0 and b == 0:
            zeros.append(i)
            continue
        if a != 0:
            key = (1, b / a)
        else:
            key = (0, 1)
        classes[key] += 1

    d2 = 8 - len(zeros)
    assert d2 > 0 and len(classes) >= 2
    d1 = d2 - max(classes.values())
    return d1, d2, tuple(zeros), tuple(sorted(classes.values()))


def low_weight_filtered_clean_fan_data(ext8, space8, rank_cache):
    d1, d2, zeros, multiplicities = coefficient_weight_profile(space8)
    LOW_WEIGHT_COUNTS[("source_weight_profile", d1, d2)] += 1
    LOW_WEIGHT_COUNTS[("source_projective_profile", len(zeros), multiplicities)] += 1

    if d2 < 4:
        # The all-depth seven-no-root theorem gives d2(P)>=4 for D=-1.
        LOW_WEIGHT_COUNTS["reject_d2_below_4"] += 1
        return ()
    if d1 < 4:
        # Weight two was excluded by the earlier low-weight reduction.  Weight
        # three is now excluded by the unstripped p=9 functional accounting:
        # the five-row rank-one child would need singleton-functional rank 6
        # at d=2 or rank 7 at d=3, while the exact committed maxima are 2 and
        # 6 respectively.
        LOW_WEIGHT_COUNTS[("reject_d1_below_4", d1)] += 1
        return ()

    # No source coefficient word has weight <=3.  Therefore every source
    # coordinate is three-clean, and the existing all-clean-fans routine must
    # return all eight first-deletion fans whenever the remaining canonical
    # state filters are satisfied.
    fans = ORIG_CLEAN_FAN_DATA(ext8, space8, rank_cache)
    if fans:
        assert len(fans) == 8
    LOW_WEIGHT_COUNTS["d1_ge_4_sources"] += 1
    return fans


G.clean_fan_data = low_weight_filtered_clean_fan_data


if __name__ == "__main__":
    try:
        G.F.L.B.main()
    finally:
        print("global_lift_counts", G.F.L.GLOBAL_LIFT_COUNTS)
        print("fixed_nine_counts", G.F.FIXED_NINE_COUNTS)
        print("actual_realization_counts", G.A.ACTUAL_COUNTS)
        print("all_clean_counts", G.ALL_CLEAN_COUNTS)
        print("low_weight_counts", LOW_WEIGHT_COUNTS)
        print("all_clean_examples", G.ALL_CLEAN_EXAMPLES)
