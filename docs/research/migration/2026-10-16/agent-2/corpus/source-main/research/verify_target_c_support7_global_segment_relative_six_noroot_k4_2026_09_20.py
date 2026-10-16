#!/usr/bin/env python3
"""Exact closure of the synchronized t=6, k=4 Target-C density branch.

The deletion-shadow synchronization theorem leaves only

    (D,k,p)=(-2,4,4) or (-1,4,5)

in the six-no-root k=4 branch. Here the global coefficient-constraint space P
has rank two in six external coordinates. Every coordinate deletion P_i has
rank two because every five-no-root deletion shadow has k=3.

For fixed P define the virtual canonical state used in the repaired five-no-root
k=3 theorem: a touched root-0 block is empty iff its empty-state coefficient
constraint is contained in P, and complete otherwise. If C is the canonical
complete-block set and d=|C|-rank H(C), then every deletion canonical complete
set C_i is contained in C. The repaired five-row theorem gives d_i>=1, hence
row-nullity monotonicity gives d>=1. Its external-containment statement also
lifts through the deletion nullspaces, so the standard defect bound is

    D(A) >= 6 + p + 3*d - 3*q,

where q is the number of canonical-complete blocks made incomplete. Since
q<=p, every case is automatic except possibly d=1,p=5,q=5. Equality q=p=5
forces five singleton replacements.

If d=1 then every deletion shadow also has d_i=1. The repaired five-row k=3
census proves that there are exactly 86 such five-row virtual canonical states,
and all are in the empty-generated class. Therefore every six-row d=1 state
is S7-isomorphic to an extension of one of those 86 states by one no-root
cycle. This verifier exhausts those extensions.

For a fixed five-row parent plane P5 and an added sixth row, every realizable
rank-two P6 with projection P5 has a basis contributed either by one rank-two
local constraint space or by two rank-one local constraint spaces from distinct
blocks. Enumerating those possibilities is exact: one block has one local
state, empty states contribute rank at most two, singleton states rank at most
one, and pair/complete states contribute no coefficient constraint. A built-in
cross-check compares this basis enumeration against the full block-state DP on
100 extensions.

For the only dangerous q=5 case, deletion synchronization also requires every
nonempty incomplete block to be touched by at least two no-root cycles. The
exhaustive extension cover has 31 d=1 synchronized candidates. Their numbers
of canonical-complete blocks that both have support multiplicity at least two
and admit a compatible singleton are 0, 2, or 3, never five. Thus the last
six-no-root k=4 case is impossible.

Complete-block ranks are computed modulo MOD=2^127-1. The imported verifier
checks MOD prime by Lucas-Lehmer. Complete relation rows have squared norm at
most 12 and the directly checked dangerous-state external rows at most 36;
MOD^2>36^15, so Hadamard certifies every modular rank/containment decision over
Q. All coefficient-space row-space operations are exact rational operations.
"""

from argparse import ArgumentParser
from collections import Counter
from pathlib import Path
import contextlib
import importlib.util
import io

HERE = Path(__file__).resolve().parent
RESEARCH = HERE if HERE.name == "research" else HERE / "research"
BASE = RESEARCH / "verify_target_c_support7_global_segment_relative_five_noroot_k3_containment_2026_09_20.py"
spec = importlib.util.spec_from_file_location("relative_five_noroot_k3_for_t6_k4", BASE)
G = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(G)
P0 = G.P0
R = G.R
K = G.K
MOD = R.P

EXPECTED_DEFICIENCY = {1: 31, 2: 1877, 3: 2171, 4: 595, 5: 10}
EXPECTED_CAPACITY = {0: 1, 2: 6, 3: 24}


def touched_blocks(ext):
    return tuple(sorted(
        b for b in range(35)
        if any(R.QCOMP[e][b] != (0, 0) for e in ext)
    ))


def deficiency(complete, cache):
    complete = tuple(complete)
    basis = cache.get(complete)
    if basis is None:
        basis = G.rref_basis_mod([P0.COMPLETE_T[b] for b in complete])
        cache[complete] = basis
    return len(complete) - len(basis)


def project_space(space, drop):
    return R.rowspace_key(tuple(
        tuple(x for j, x in enumerate(row) if j != drop)
        for row in space
    ))


def canonical_complete_set(ext, space):
    touched = touched_blocks(ext)
    states = G.virtual_canonical(ext, touched, space)
    return touched, tuple(
        b for b, state in zip(touched, states) if state == 7
    )


def five_row_d1_parents(rank_cache):
    """Return the exact 86 repaired-k3 deficiency-one parent states."""
    keys, orbits, orbit_sizes, augmentation_candidates = K.five_no_root_orbits()
    assert len(orbits) == 20451
    assert sum(orbit_sizes) == 96560646
    assert augmentation_candidates == 20475
    key_to_global = {K.cycle_key(R.DESC[e]): e for e in R.NO_ROOT}

    parents = []
    for local_five in orbits:
        ext = tuple(key_to_global[keys[i]] for i in local_five)
        touched = touched_blocks(ext)

        # The repaired theorem proves every d=1 plane is empty-generated, so
        # the older empty-generated candidate list is exhaustive for d=1.
        for space in P0.candidate_rank2_constraint_spaces(ext, touched):
            states = P0.canonical_minimal_state(ext, touched, space)
            assert states is not None
            complete = tuple(
                b for b, state in zip(touched, states) if state == 7
            )
            if deficiency(complete, rank_cache) == 1:
                parents.append((ext, space))

    assert len(parents) == 86
    assert len({ext for ext, _ in parents}) == 70
    return tuple(parents)


def local_basis_options(ext6, touched, parent_space):
    """Nonzero local spaces whose sixth-coordinate projection lies in P5."""
    out = {}
    for block in touched:
        spaces = set()
        for state in (0, 1, 2, 4):
            space = R.local_constraint_key(ext6, block, state)
            if not space or len(space) > 2:
                continue
            if R.is_subspace(project_space(space, 5), parent_space):
                spaces.add(space)
        if spaces:
            out[block] = tuple(spaces)
    return out


def candidate_six_planes(ext6, touched, parent_space):
    """Enumerate every realizable rank-two P6 projecting to parent_space."""
    options = local_basis_options(ext6, touched, parent_space)
    candidates = set()
    rank_one = []

    for block, spaces in options.items():
        for space in spaces:
            if len(space) == 2:
                if project_space(space, 5) == parent_space:
                    candidates.add(space)
            else:
                assert len(space) == 1
                rank_one.append((block, space))

    for i, (block_i, space_i) in enumerate(rank_one):
        for block_j, space_j in rank_one[i + 1:]:
            if block_i == block_j:
                continue
            space = R.union_key(space_i, space_j)
            if len(space) == 2 and project_space(space, 5) == parent_space:
                candidates.add(space)

    return tuple(candidates)


def relation_rows_six(ext6, touched, states, space):
    """Canonical complete rows followed by the four six-row external lifts."""
    rows = [
        P0.COMPLETE_T[block]
        for block, state in zip(touched, states)
        if state == 7
    ]
    alphas = R.nullspace_int(space, 6)
    assert len(alphas) == 4
    for alpha in alphas:
        tv = [
            sum(alpha[i] * R.MCOORD[e][70 + j] for i, e in enumerate(ext6))
            for j in range(15)
        ]
        for block, state in zip(touched, states):
            vx = sum(alpha[i] * R.QCOMP[e][block][0] for i, e in enumerate(ext6))
            vy = sum(alpha[i] * R.QCOMP[e][block][1] for i, e in enumerate(ext6))
            beta = R.solve_local_coeffs_int(R.STATES[state][0], (-vx, -vy))
            ids = R.BLOCKS[block]
            for local_index, q in enumerate(beta):
                if q:
                    for j in range(15):
                        tv[j] += q * R.MCOORD[ids[local_index]][70 + j]
        rows.append(tuple(tv))
    return rows


def compatible_shared_singleton_blocks(ext6, space, complete):
    """Canonical-complete blocks eligible for a counterexample singleton."""
    good = []
    for block in complete:
        support = sum(R.QCOMP[e][block] != (0, 0) for e in ext6)
        if support < 2:
            continue
        if any(
            R.is_subspace(R.local_constraint_key(ext6, block, state), space)
            for state in (1, 2, 4)
        ):
            good.append(block)
    return tuple(good)


def crosscheck_candidate_enumerator(parents, instances=100):
    """Compare fast basis enumeration with the full repaired block-state DP."""
    checked = 0
    for ext5, parent_space in parents:
        for extra in R.NO_ROOT:
            if extra in ext5:
                continue
            ext6 = ext5 + (extra,)
            touched = touched_blocks(ext6)
            fast = set(candidate_six_planes(ext6, touched, parent_space))
            full = {
                space
                for space, _ in G.candidate_spaces(ext6, touched)
                if project_space(space, 5) == parent_space
            }
            assert fast == full, (ext5, extra, len(fast), len(full))
            checked += 1
            if checked == instances:
                return checked
    return checked


def scan_extensions(parents, start, stop, rank_cache):
    counts = Counter()
    deficiency_census = Counter()
    capacity_census = Counter()
    first_capacity_five = None
    max_external_norm2 = 0

    for parent_index in range(start, stop):
        ext5, parent_space = parents[parent_index]
        for extra in R.NO_ROOT:
            if extra in ext5:
                continue
            ext6 = ext5 + (extra,)
            touched = touched_blocks(ext6)
            counts["extensions"] += 1

            for space in candidate_six_planes(ext6, touched, parent_space):
                counts["candidate_P6"] += 1
                projections = tuple(project_space(space, i) for i in range(6))
                if any(len(projected) != 2 for projected in projections):
                    continue
                counts["all_projection_rank2"] += 1

                states = G.virtual_canonical(ext6, touched, space)
                complete = tuple(
                    b for b, state in zip(touched, states) if state == 7
                )
                d = deficiency(complete, rank_cache)
                deficiency_census[d] += 1
                if d != 1:
                    continue

                counts["six_d1"] += 1

                # Independent direct check of the lifted-containment theorem
                # on every dangerous d=1 canonical state.
                basis = G.rref_basis_mod([P0.COMPLETE_T[b] for b in complete])
                relation_rows = relation_rows_six(ext6, touched, states, space)
                external_rows = relation_rows[len(complete):]
                assert len(external_rows) == 4
                for row in external_rows:
                    max_external_norm2 = max(
                        max_external_norm2, sum(x * x for x in row)
                    )
                    assert G.contained_mod(row, basis), (ext6, space, complete, row)

                for i, projected in enumerate(projections):
                    ext_i = ext6[:i] + ext6[i + 1:]
                    touched_i, complete_i = canonical_complete_set(ext_i, projected)
                    assert deficiency(complete_i, rank_cache) == 1
                    assert projected in set(
                        P0.candidate_rank2_constraint_spaces(ext_i, touched_i)
                    )

                good = compatible_shared_singleton_blocks(ext6, space, complete)
                capacity_census[len(good)] += 1
                if len(good) >= 5 and first_capacity_five is None:
                    first_capacity_five = (ext6, space, complete, good)

    return {
        "counts": counts,
        "deficiency_census": deficiency_census,
        "capacity_census": capacity_census,
        "first_capacity_five": first_capacity_five,
        "max_external_norm2": max_external_norm2,
    }


def main():
    parser = ArgumentParser()
    parser.add_argument("--parent-start", type=int, default=0)
    parser.add_argument("--parent-end", type=int)
    parser.add_argument("--crosscheck", type=int, default=100)
    args = parser.parse_args()

    assert R.lucas_lehmer_127()
    max_complete_norm2 = max(sum(x * x for x in row) for row in P0.COMPLETE_T)
    assert max_complete_norm2 == 12
    assert MOD * MOD > max_complete_norm2 ** 15

    rank_cache = {}
    parents = five_row_d1_parents(rank_cache)
    end = len(parents) if args.parent_end is None else args.parent_end
    assert 0 <= args.parent_start <= end <= len(parents)

    crosschecked = crosscheck_candidate_enumerator(parents, args.crosscheck)
    assert crosschecked == min(args.crosscheck, 8600)

    result = scan_extensions(parents, args.parent_start, end, rank_cache)
    assert result["first_capacity_five"] is None, result["first_capacity_five"]

    if args.parent_start == 0 and end == len(parents):
        assert result["counts"]["extensions"] == 8600
        assert result["counts"]["candidate_P6"] == 16781
        assert result["counts"]["all_projection_rank2"] == 4684
        assert result["counts"]["six_d1"] == 31
        assert dict(sorted(result["deficiency_census"].items())) == EXPECTED_DEFICIENCY
        assert dict(sorted(result["capacity_census"].items())) == EXPECTED_CAPACITY
        assert max(result["capacity_census"]) == 3
        assert result["max_external_norm2"] == 36

    bound_norm2 = max(max_complete_norm2, result["max_external_norm2"])
    assert MOD * MOD > max(1, bound_norm2) ** 15

    print("PASS: six-no-root k=4 synchronized boundary closure")
    print("five_row_d1_parent_states", len(parents))
    print("five_row_d1_parent_cycle_sets", len({ext for ext, _ in parents}))
    print("candidate_enumerator_crosschecks", crosschecked)
    print("parent_range", args.parent_start, end)
    print("extension_cover_counts", dict(result["counts"]))
    print("synchronized_deficiency_census", dict(sorted(result["deficiency_census"].items())))
    print("d1_shared_singleton_capacity_census", dict(sorted(result["capacity_census"].items())))
    print("max_d1_shared_singleton_capacity", max(result["capacity_census"], default=-1))
    print("max_complete_row_norm_squared", max_complete_norm2)
    print("max_d1_external_row_norm_squared", result["max_external_norm2"])
    print("hadamard_exact_rank_bound", MOD * MOD > max(1, bound_norm2) ** 15)
    print("complete_rank_cache_size", len(rank_cache))


if __name__ == "__main__":
    main()
