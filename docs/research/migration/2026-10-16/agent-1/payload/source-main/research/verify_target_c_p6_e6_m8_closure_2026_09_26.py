#!/usr/bin/env python3
"""Exact closure of the e=6,m=8 slice in the final p=6 branch.

Inputs already proved in the repository:
  * rank(P)=3 and generalized weights (d1,d2,d3)>=(2,4,5);
  * six touched singleton replacements and no selected pair;
  * e=6 touched actual-empty blocks;
  * nu(T)<=e+1=7;
  * all e=6 slices with m<=7 are already closed.

For m=8 the eight no-root cycles have eight distinct four-supports, hence
multiplicity profile (1,1,1,1,1,1,1,1). This verifier enumerates the exact S7
support quotient with nu(T)<=7, applies the phase-independent generalized-weight
conditions to the six actual-empty blocks, then scans every retained phase.
A mod-2 rank greater than three is a rigorous obstruction because the local
constraint rows are integral and rank_F2(U)<=rank_Q(U).
"""
from collections import Counter
from pathlib import Path
import contextlib
import importlib.util
import io

HERE = Path(__file__).resolve().parent
BASE = HERE / "verify_target_c_p6_e6_m7_closure_2026_09_26.py"
spec = importlib.util.spec_from_file_location("p6_e6_m8_parent", BASE)
M7 = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(M7)

B = M7.B
E5 = M7.E5


def support_orbits_m8():
    cands = set()
    for ss in M7.support_orbits_m7():
        for j in range(35):
            if j in ss:
                continue
            u = tuple(sorted(ss + (j,)))
            if B.support_nullity(u) <= 7:
                cands.add(B.canonical_support(u))
    out = tuple(sorted(cands))
    nullities = dict(sorted(Counter(B.support_nullity(s) for s in out).items()))
    assert len(out) == 39 and nullities == {7: 39}, (len(out), nullities)
    return out


def main():
    profile = (1, 1, 1, 1, 1, 1, 1, 1)
    supports = support_orbits_m8()

    kept = []
    for ss in supports:
        qs = M7.strong_empty_sextuples(ss, profile)
        if qs:
            kept.append((ss, profile, qs))

    assert len(kept) == 7, len(kept)
    assert sum(len(qs) for _, _, qs in kept) == 65
    assert Counter(len(qs) for _, _, qs in kept) == Counter({6: 3, 7: 1, 8: 1, 14: 1, 18: 1})

    counts = Counter()
    ranks = Counter()
    for ss, a, qs in kept:
        blocks = set(b for q in qs for b in q)
        for ext in B.phase_exts(ss, a):
            counts["phases"] += 1
            mm = E5.masks(ext, blocks)
            for q in qs:
                counts["pairs"] += 1
                r = E5.rank2(tuple(z for b in q for z in mm[b]))
                ranks[r] += 1
                assert r > 3, (ss, ext, q, r)

    assert counts["phases"] == 45927, counts
    assert counts["pairs"] == 426465, counts
    assert dict(ranks) == {5: 22, 6: 1831, 7: 59660, 8: 364952}, ranks

    print("PASS: p=6 e=6 m=8 closure")
    print("support_orbits", len(supports))
    print("prefilter_support_orbits", len(kept))
    print("prefilter_empty_sextuples", sum(len(qs) for _, _, qs in kept))
    print("phase_configs", counts["phases"])
    print("phase_empty_sextuple_pairs", counts["pairs"])
    print("rank_F2_census", dict(sorted(ranks.items())))


if __name__ == "__main__":
    main()
