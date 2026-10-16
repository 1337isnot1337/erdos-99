#!/usr/bin/env python3
"""Exact global endpoint search through finite planar placement palettes.

Arc consistency plus exhaustive branching certifies SAT/UNSAT of finite
independent-transversal systems. Negative geometric certificates use only
certainly forbidden pairs; positive certificates check all chosen pair bounds.
The fixtures concern nonglobal sources, never triangle-free global minimizers.
No floating-point calculation participates in a decision.
"""

if not __debug__:
    raise RuntimeError("Certificate assertions are required; run Python without -O.")
from collections import deque
from copy import deepcopy
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations
from math import isqrt
from pathlib import Path
import json

from exact_trig_intervals_2026_10_12 import I, SCALE, sin_pi, cos_pi, check_exact_special_values

PROVENANCE = Path(__file__).resolve().parent / "fixtures/global_palette_translation_2026_10_12/provenance.json"
FIXTURE_DATA_DIR: Path | None = None


def distance(x, y):
    return (x[0]-y[0]).square()+(x[1]-y[1]).square()


def build_system(options, diameter_squared, *, sufficient):
    """Sufficient graph proves SAT; permissive graph proves UNSAT.

    In a permissive graph an uncertain tuple remains allowed. Thus a genuine
    geometric assignment necessarily survives every encoded prohibition.
    """
    allowed = {}
    neighbours = [[] for _ in options]
    for i, j in combinations(range(len(options)), 2):
        bits = []
        for p in options[i]:
            mask = 0
            for c, q in enumerate(options[j]):
                d = distance(p, q)
                if sufficient:
                    permitted = d.lo >= SCALE and d.hi < diameter_squared.lo
                else:
                    permitted = not (d.hi < SCALE or d.lo >= diameter_squared.hi)
                if permitted:
                    mask |= 1 << c
            bits.append(mask)
        if bits == [(1 << len(options[j]))-1]*len(options[i]):
            continue
        allowed[i, j] = bits
        allowed[j, i] = [sum(1 << c for c, mask in enumerate(bits) if mask & (1 << d))
                          for d in range(len(options[j]))]
        neighbours[i].append(j)
        neighbours[j].append(i)
    return allowed, neighbours


def solve(allowed, neighbours, sizes, *, proof=None):
    nodes = 0

    def visit(domains, record=None):
        nonlocal nodes
        nodes += 1
        if record is not None:
            record["prunes"] = []
        queue = deque(allowed)
        while queue:
            i, j = queue.popleft()
            new = sum(1 << c for c in range(sizes[i])
                      if domains[i] & (1 << c) and allowed[i, j][c] & domains[j])
            if record is not None and new != domains[i]:
                record["prunes"].append([i, j, new])
            if not new:
                return None
            if new == domains[i]:
                continue
            domains[i] = new
            queue.extend((k, i) for k in neighbours[i] if k != j)
        choices = [i for i, mask in enumerate(domains) if mask.bit_count() > 1]
        if not choices:
            return [mask.bit_length()-1 for mask in domains]
        i = min(choices, key=lambda k: (domains[k].bit_count(), -len(neighbours[k])))
        if record is not None:
            record["split"] = i
            record["branches"] = []
        for c in range(sizes[i]):
            if domains[i] & (1 << c):
                branch = domains.copy()
                branch[i] = 1 << c
                child = {} if record is not None else None
                if record is not None:
                    record["branches"].append({"value": c, "proof": child})
                result = visit(branch, child)
                if result is not None:
                    return result
        return None

    if any(size <= 0 for size in sizes):
        return None, 0
    result = visit([(1 << size)-1 for size in sizes], proof)
    return result, nodes


def replay_unsat(allowed, sizes, proof, domains=None):
    """Check only supplied deductions and complete splits, without searching."""
    if domains is None:
        assert sizes and all(size > 0 for size in sizes)
        domains = [(1 << size)-1 for size in sizes]
    prunes = proof["prunes"]
    for step, (i, j, new) in enumerate(prunes):
        assert (i, j) in allowed
        supported = sum(1 << c for c in range(sizes[i])
                        if domains[i] & (1 << c) and allowed[i, j][c] & domains[j])
        assert new == supported and new != domains[i]
        domains[i] = new
        if not new:
            assert step == len(prunes)-1 and set(proof) == {"prunes"}
            return True
    i = proof["split"]
    assert 0 <= i < len(sizes) and domains[i].bit_count() > 1
    branches = proof["branches"]
    choices = [c for c in range(sizes[i]) if domains[i] & (1 << c)]
    assert [b["value"] for b in branches] == choices
    for branch in branches:
        child_domains = domains.copy()
        child_domains[i] = 1 << branch["value"]
        assert replay_unsat(allowed, sizes, branch["proof"], child_domains)
    return True


def verify_unsat_corruptions(allowed, sizes, proof):
    def alter(record, kind):
        if kind == "prune" and record["prunes"]:
            i = record["prunes"][0][0]
            record["prunes"][0][2] = (1 << sizes[i])-1
            return True
        if kind == "branch" and record.get("branches"):
            record["branches"].pop()
            return True
        return any(alter(b["proof"], kind) for b in record.get("branches", []))
    for kind in ("prune", "branch"):
        bad = deepcopy(proof)
        assert alter(bad, kind)
        try:
            replay_unsat(allowed, sizes, bad)
        except (AssertionError, KeyError):
            continue
        raise AssertionError("Corrupted exhaustive proof accepted")
    print("PASS corrupted pruning and incomplete branch cover rejected")


def check_assignment(options, assignment, diameter_squared):
    assert len(assignment) == len(options)
    assert all(isinstance(c, int) and 0 <= c < len(row)
               for row, c in zip(options, assignment))
    endpoint = [row[c] for row, c in zip(options, assignment)]
    norms = [distance(p, q) for p, q in combinations(endpoint, 2)]
    assert all(d.lo >= SCALE and d.hi < diameter_squared.lo for d in norms)
    return min(d.lo for d in norms), max(d.hi for d in norms), len(norms)


def read_packing(n):
    if FIXTURE_DATA_DIR is None:
        raise RuntimeError("Pass --fixture-dir with locally obtained, licensed cci132.txt and cci175.txt files.")
    provenance = json.loads(PROVENANCE.read_text())
    record = next(row for row in provenance["sources"] if row["cardinality"] == n)
    raw = (FIXTURE_DATA_DIR/f"cci{n}.txt").read_bytes()
    assert sha256(raw).hexdigest() == record["sha256"]
    integer_scale = 10**30
    points = []
    for expected, line in enumerate(raw.decode().splitlines(), 1):
        label, x, y = line.split()
        assert int(label) == expected
        x, y = F(x)*integer_scale, F(y)*integer_scale
        assert x.denominator == y.denominator == 1
        points.append((int(x), int(y)))
    assert len(points) == n
    norms = [(x-u)**2+(y-v)**2 for (x, y), (u, v) in combinations(points, 2)]
    normalizer_den = 10**12
    normalizer_num = isqrt(integer_scale**2*normalizer_den**2//min(norms))+1
    factor = F(normalizer_num*1000001, integer_scale*normalizer_den*1000000)
    assert min(norms)*factor**2 > 1
    radius_sq = max(x*x+y*y for x, y in points)*factor**2
    return [(I.rational(x*factor), I.rational(y*factor)) for x, y in points], radius_sq


def options_for(source, alpha, palette):
    return [[(alpha*x+u, alpha*y+v) for u, v in palette] for x, y in source]


def verify_boolean_kernel():
    def test(sizes, restrictions):
        neighbours = [[] for _ in sizes]
        for i, j in restrictions:
            neighbours[i].append(j)
        proof = {}
        result, _ = solve(restrictions, neighbours, sizes, proof=proof)
        # Independent direct enumeration is used only for these small logic fixtures.
        from itertools import product
        witnesses = [a for a in product(*(range(s) for s in sizes))
                     if all(mask[a[i]] & (1 << a[j]) for (i, j), mask in restrictions.items())]
        assert (result is None) == (not witnesses)
        if result is not None:
            assert tuple(result) in witnesses
        else:
            assert replay_unsat(restrictions, sizes, json.loads(json.dumps(proof)))
    test([3, 3], {})
    test([3, 3], {(0, 1): [0, 0, 0], (1, 0): [0, 0, 0]})
    # Odd cycle is not 2-colourable, but is 3-colourable.
    for q in (2, 3):
        restrictions = {}
        for i, j in [(0, 1), (1, 2), (2, 0)]:
            bits = [((1 << q)-1) ^ (1 << c) for c in range(q)]
            restrictions[i, j] = bits
            restrictions[j, i] = bits
        test([q]*3, restrictions)
    # All 16 possible binary relations on each of three unordered label pairs.
    from itertools import product
    for relations in product(range(16), repeat=3):
        restrictions = {}
        for (i, j), relation in zip([(0, 1), (0, 2), (1, 2)], relations):
            rows = [relation & 3, (relation >> 2) & 3]
            restrictions[i, j] = rows
            restrictions[j, i] = [sum(1 << c for c, mask in enumerate(rows)
                                      if mask & (1 << d)) for d in range(2)]
        test([2]*3, restrictions)
    print("PASS Boolean propagation/branching and UNSAT proof replay: 4100 cases "
          "against independent enumeration, including all 4096 binary-relation systems")


def main():
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixture-dir", type=Path,
                        help="directory containing locally obtained cci132.txt and cci175.txt; expected URLs and SHA-256 values are in the adjacent provenance.json")
    parser.add_argument("--core-only", action="store_true",
                        help="run the self-contained 43-gon palette check without external coordinate tables")
    parser.add_argument("--certificate-json", type=Path)
    parser.add_argument("--replay-certificate-json", type=Path)
    args = parser.parse_args()
    global FIXTURE_DATA_DIR
    FIXTURE_DATA_DIR = args.fixture_dir.resolve() if args.fixture_dir else None
    saved = json.loads(args.replay_certificate_json.read_text()) if args.replay_certificate_json else None
    if args.core_only and (args.fixture_dir or args.certificate_json or args.replay_certificate_json):
        parser.error("--core-only cannot be combined with fixture or whole-source certificate options")
    if not args.core_only and FIXTURE_DATA_DIR is None:
        parser.error("provide --fixture-dir for the 132/175 checks, or use --core-only for the self-contained 43-gon check")
    if FIXTURE_DATA_DIR is not None:
        if not FIXTURE_DATA_DIR.is_dir():
            parser.error("--fixture-dir must name a local directory containing the two external coordinate files")
        missing = [f"cci{n}.txt" for n in (132, 175) if not (FIXTURE_DATA_DIR/f"cci{n}.txt").is_file()]
        if missing:
            parser.error("external coordinate files are not bundled; missing " + ", ".join(missing) + "; see " + str(PROVENANCE))
    if args.core_only and saved is not None:
        parser.error("--core-only does not replay a whole-source certificate")
    if saved is None:
        verify_boolean_kernel()
    check_exact_special_values()
    q = 43
    radius = I.rational(1)/(2*sin_pi(F(1, q)))
    diameter_squared = I.rational(1)/(4*sin_pi(F(1, 2*q)).square())
    core = [(radius*cos_pi(F(2*i, q)), radius*sin_pi(F(2*i, q))) for i in range(q)]
    palette = [(I.rational(1), I.rational(0)),
               (I.rational(F(-1, 2)), I.rational(3).sqrt()/2),
               (I.rational(F(-1, 2)), -I.rational(3).sqrt()/2)]
    alpha = F(17, 20)
    # Exact sine chord identities give C=H=43 on the rim. All other rim
    # pairs have step 2,...,20 and are strictly between the two bounds.
    for step in range(2, 21):
        chord = sin_pi(F(step, q)).square()/sin_pi(F(1, q)).square()
        assert chord.lo > SCALE and chord.hi < diameter_squared.lo
    core_options = options_for(core, alpha, palette)
    system, neighbours = build_system(core_options, diameter_squared, sufficient=True)
    if saved is None:
        assignment, nodes = solve(system, neighbours, [3]*q)
    else:
        assert saved["source_labels"] == 175 and saved["rim_labels"] == q
        assert saved["alpha"] == str(alpha) and saved["interval_scale"] == str(SCALE)
        assignment, nodes = saved["rim_assignment"], "replayed"
    assert assignment is not None
    lower, upper, pair_count = check_assignment(core_options, assignment, diameter_squared)
    assert lower > I.rational(F(101, 100)).hi
    assert upper < I.rational(185).lo
    print("PASS core palette endpoint: 43 labels,", pair_count, "pairs,", nodes, "search nodes")
    print("PASS core endpoint min squared distance > 1.01; squared diameter < 185 < old D^2")
    if args.core_only:
        print("SCOPE: exact finite 43-gon palette success only; no global-minimizer conclusion")
        return 0

    inner, inner_r2 = read_packing(132)
    assert (radius-I.rational(inner_r2).sqrt()).lo > SCALE
    assert (radius+I.rational(inner_r2).sqrt()).hi < diameter_squared.sqrt().lo
    assert all(distance(p, r).lo > SCALE and distance(p, r).hi < diameter_squared.lo
               for p, r in combinations(inner, 2))
    source = core+inner
    assert len(source) == 175
    fixture_hashes = {str(n): sha256((FIXTURE_DATA_DIR/f"cci{n}.txt").read_bytes()).hexdigest()
                      for n in (132, 175)}
    if saved is not None:
        assert saved["fixture_sha256"] == fixture_hashes
    full_options = options_for(source, alpha, palette)
    system, neighbours = build_system(full_options, diameter_squared, sufficient=False)
    proof = {}
    sizes = [3]*len(source)
    if saved is None:
        result, nodes = solve(system, neighbours, sizes, proof=proof)
    else:
        result, nodes, proof = None, "replayed", saved["full_source_unsat"]
    assert result is None
    proof = json.loads(json.dumps(proof))
    assert replay_unsat(system, sizes, proof)
    verify_unsat_corruptions(system, sizes, proof)
    print("PASS full-source palette UNSAT: 175 labels,", len(system)//2,
          "constrained label pairs,", nodes, "exhaustive search nodes")
    winner, _ = read_packing(175)
    norms = [distance(p, r) for p, r in combinations(winner, 2)]
    assert len(norms) == 15225
    assert all(d.lo > SCALE and d.hi < diameter_squared.lo for d in norms)
    assert max(d.hi for d in norms) < I.rational(F(1832352, 10000)).lo
    print("PASS independent full-source winner: all 15225 pairs > 1, D^2 < 183.2352")
    certificate = {"source_labels": len(source), "rim_labels": q,
                   "alpha": str(alpha), "interval_scale": str(SCALE),
                   "fixture_sha256": fixture_hashes,
                   "rim_assignment": assignment, "full_source_unsat": proof}
    if args.certificate_json:
        args.certificate_json.write_text(json.dumps(certificate, indent=2)+"\n")
    print("PASS full-source JSON UNSAT proof replay without search")
    print("SCOPE: certified failure of one finite palette on a nonglobal source; Level I remains open")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
