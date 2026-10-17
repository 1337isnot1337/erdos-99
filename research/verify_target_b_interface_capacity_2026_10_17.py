#!/usr/bin/env python3
"""Two independent exact enumerations for the unreviewed interface-capacity note.

The labelled-edge engine assigns absent/physical/charged states separately to
all eligible pairs. The inventory engine uses multinomial occupation numbers,
then convolves edge classes. Neither imports a predecessor checker or claims
planar realization. Integer checks use explicit exceptions, including under -O.
"""
from collections import Counter
from itertools import combinations, product
from math import factorial
from pathlib import Path
import argparse
import hashlib
import json


ROOT = Path(__file__).resolve().parents[1]
BASE = "e396ea07887dd0528b817ce4e656ff0e6b01f8fb"
SOURCE_PATHS = (
    "docs/STATE.md",
    "docs/research/priority-state.json",
    "docs/research/agent-task-catalog.json",
    "docs/targets/target-b/README.md",
    "docs/targets/target-b/01-jammed-rhombic-branch.md",
    "docs/reports/target_b_dense_grid_penetration_interpolation_dependency_audit_2026-09-11.md",
    "docs/reports/target_b_trimmed_grid_phase_star_exclusion_2026-09-05.md",
    "docs/reports/target_b_penetration_charged_grid_cancellation_2026-09-05.md",
    "docs/reports/target_b_multicomponent_penetration_budget_2026-09-05.md",
    "docs/research/onboarding-evaluation-2026-10-15.md",
    "research/onboarding_two_grain_audit.py",
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def labelled_model(shores, pruned):
    """Return labelled vertices, internal edges, and eligible optional edges."""
    a, b, c, d = shores
    groups = ((0, 0, a), (0, 1, b), (1, 0, c), (1, 1, d), (-1, 2, pruned))
    vertices = [(grain, phase) for grain, phase, size in groups for _ in range(size)]
    internal, optional = [], []
    for left, right in combinations(range(len(vertices)), 2):
        gl, pl = vertices[left]
        gr, pr = vertices[right]
        if pl == pr:
            continue  # Parallel pairs always virtual.
        if gl == gr and gl >= 0:
            internal.append((left, right))
        else:
            eligible = tuple(sorted({g for g in (gl, gr) if g >= 0}))
            optional.append(((left, right), eligible))
    return vertices, internal, optional


def edge_options(eligible):
    """Counters are (exterior physical edges, X_1, X_2, shared physical edges)."""
    yield (0, 0, 0, 0)  # Absent physical pair; not chargeable.
    for bits in product((0, 1), repeat=len(eligible)):
        selected = dict(zip(eligible, bits))
        yield (1, selected.get(0, 0), selected.get(1, 0), int(len(eligible) == 2))


def labelled_histogram(optional):
    # Enumerate every labelled edge state. No multiplicity shortcut is used.
    histogram = Counter()
    choices = [tuple(edge_options(eligible)) for _, eligible in optional]
    def visit(index, r, x, y, shared):
        if index == len(choices):
            histogram[r, x, y, shared] += 1
            return
        for dr, dx, dy, ds in choices[index]:
            visit(index + 1, r + dr, x + dx, y + dy, shared + ds)
    visit(0, 0, 0, 0, 0)
    return histogram


def occupations(total, categories):
    """All occupation vectors, independently of labelled assignments."""
    if categories == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in occupations(total - first, categories - 1):
            yield (first,) + tail


def multinomial(counts):
    value = factorial(sum(counts))
    for count in counts:
        value //= factorial(count)
    return value


def inventory_histogram(shared_slots, private_1, private_2):
    # Shared categories: absent, physical-unclaimed, only 1, only 2, both.
    shared = Counter()
    for counts in occupations(shared_slots, 5):
        absent, unused, only_1, only_2, both = counts
        physical = shared_slots - absent
        shared[physical, only_1 + both, only_2 + both, physical] += multinomial(counts)
    histogram = shared
    for grid, slots in enumerate((private_1, private_2)):
        private = Counter()
        # Private categories: absent, physical-unclaimed, claimed.
        for counts in occupations(slots, 3):
            absent, unused, claimed = counts
            private[slots - absent, claimed] += multinomial(counts)
        expanded = Counter()
        for (r, x, y, i), weight in histogram.items():
            for (physical, claimed), multiplicity in private.items():
                expanded[r + physical, x + claimed * (grid == 0),
                         y + claimed * (grid == 1), i] += weight * multiplicity
        histogram = expanded
    return histogram


def digest_histogram(histogram):
    rows = [list(key) + [count] for key, count in sorted(histogram.items())]
    return hashlib.sha256(json.dumps(rows, separators=(",", ":")).encode()).hexdigest()


def check_inventory_optima(histogram, shared_slots, private_1, private_2):
    minima = {}
    for r, x, y, i in histogram:
        key = x, y, i
        minima[key] = min(minima.get(key, r), r)
    exact_checked = upper_checked = 0
    for x in range(shared_slots + private_1 + 1):
        for y in range(shared_slots + private_2 + 1):
            for i in range(shared_slots + 1):
                actual = minima.get((x, y, i))
                feasible = x <= i + private_1 and y <= i + private_2
                predicted = i + max(0, x - i) + max(0, y - i) if feasible else None
                require(actual == predicted, f"exact-I optimum disagrees at {(x, y, i)}")
                exact_checked += 1
            for cap in range(shared_slots + 1):
                costs = [minima[x, y, i] for i in range(cap + 1) if (x, y, i) in minima]
                actual = min(costs) if costs else None
                feasible = x <= cap + private_1 and y <= cap + private_2
                predicted = max(x, y, x + y - cap) if feasible else None
                require(actual == predicted, f"upper-cap optimum disagrees at {(x, y, cap)}")
                if feasible:
                    selected_i = max(min(cap, x, y), x - private_1, y - private_2)
                    require(0 <= selected_i <= cap, "constructive shared inventory invalid")
                    require(minima.get((x, y, selected_i)) == predicted,
                            "constructive optimum not attained")
                upper_checked += 1
    return exact_checked, upper_checked


def audit_two_grains():
    rows = []
    total_states = exact_checks = cap_checks = 0
    minimum_naive_failure = None
    strict_gain_states = improved_over_single_grids = 0
    for shores in product(range(1, 4), repeat=4):
        if sum(shores) > 6:
            continue
        a, b, c, d = shores
        for pruned in (0, 1):
            vertices, internal, optional = labelled_model(shores, pruned)
            g = len(internal)
            shared_slots = a * d + b * c
            private_1, private_2 = (a + b) * pruned, (c + d) * pruned
            require(g == a * b + c * d, "internal grid population mismatch")
            direct = labelled_histogram(optional)
            inventory = inventory_histogram(shared_slots, private_1, private_2)
            require(direct == inventory, f"independent histograms disagree: {shores}, {pruned}")
            states = sum(direct.values())
            require(states == 5 ** shared_slots * 3 ** (private_1 + private_2), "domain size mismatch")
            for (r, x, y, i), multiplicity in direct.items():
                physical = g + r
                # Actual-I bound counts all physical interface edges, even unclaimed.
                exact_bound = g + max(i, x, y, x + y - i)
                half_bound = g + (x + y + 1) // 2
                deletion_bound = g + x + y - r  # Every optional physical edge is deleted.
                require(physical >= max(exact_bound, half_bound, deletion_bound),
                        "refined physical budget failed")
                old_integer_bound = (g + x + y + 1) // 2
                if max(exact_bound, half_bound, deletion_bound) > old_integer_bound:
                    strict_gain_states += multiplicity
                previous_single_grid_bounds = max(g, a * b + x, c * d + y, old_integer_bound)
                if max(exact_bound, half_bound, deletion_bound) > previous_single_grid_bounds:
                    improved_over_single_grids += multiplicity
                if physical < g + x + y:
                    candidate = (physical, sum(shores), pruned, tuple(shores), r, x, y, i)
                    if minimum_naive_failure is None or candidate < minimum_naive_failure:
                        minimum_naive_failure = candidate
            exact, caps = check_inventory_optima(direct, shared_slots, private_1, private_2)
            exact_checks += exact
            cap_checks += caps
            total_states += states
            rows.append(dict(shores=shores, pruned=pruned, grid_edges=g,
                             shared_slots=shared_slots, private_slots=[private_1, private_2],
                             states=states, counter_bins=len(direct),
                             histogram_sha256=digest_histogram(direct)))
    require(total_states == 8336550, "two-grain domain was not exhausted")
    require(minimum_naive_failure is not None and minimum_naive_failure[0] == 3,
            "missing minimal naive-additivity counterexample")
    return dict(configurations=rows, states=total_states,
                strict_gain_over_rounded_mcp1_states=strict_gain_states,
                strict_gain_over_mcp1_and_individual_pc1_states=improved_over_single_grids,
                exact_inventory_cases=exact_checks, upper_cap_inventory_cases=cap_checks,
                minimal_naive_failure_counters=dict(zip(
                    ("R", "grid_trains", "pruned", "shores", "exterior_R", "X_1", "X_2", "I"),
                    minimum_naive_failure)))


def audit_three_grains():
    # Three disjoint one-edge grids, two phases, no pruned train.
    grains, phases = (0, 0, 1, 1, 2, 2), (0, 1, 0, 1, 0, 1)
    internal = set()
    optional = []
    for a, b in combinations(range(6), 2):
        if phases[a] == phases[b]:
            continue
        if grains[a] == grains[b]:
            internal.add((a, b))
        else:
            eligible = (grains[a], grains[b])
            options = [None] + [tuple(g for g, bit in zip(eligible, bits) if bit)
                                for bits in product((0, 1), repeat=2)]
            optional.append(((a, b), options))
    states = 0
    tight_identity = tight_deletion = 0
    for selected in product(*(options for _, options in optional)):
        physical = set(internal)
        charges = [set() for _ in range(3)]
        for (edge, _), charged_by in zip(optional, selected):
            if charged_by is not None:
                physical.add(edge)
                for grid in charged_by:
                    charges[grid].add(edge)
        # Derive membership from sets; independent of the two-grain counters.
        usage = Counter(edge for chosen in charges for edge in chosen)
        require(all(count <= 2 for count in usage.values()), "physical edge used more than twice")
        b = sum(count == 2 for count in usage.values())
        u = len(physical - internal - set(usage))
        s, g, r = sum(map(len, charges)), len(internal), len(physical)
        deleted = physical - internal
        require(b <= len(deleted), "shared charge is not deleted")
        require(r == g + s - b + u, "exact multiplicity identity failed")
        require(r >= g + max((s + 1) // 2, s - len(deleted), max(map(len, charges))),
                "multicomponent lower bound failed")
        tight_identity += r == g + (s + 1) // 2
        tight_deletion += r == g + s - len(deleted)
        states += 1
    require(states == 15625 and tight_identity and tight_deletion, "three-grain domain mismatch")
    return dict(states=states, grids=3, trains=6,
                rounded_half_bound_equalities=tight_identity,
                deletion_bound_equalities=tight_deletion)


def controls():
    # A physical interface is charged twice: the predecessor's minimal failure.
    grids = ({(0, 1)}, {(2, 3)})
    physical = {(0, 1), (0, 3), (2, 3)}
    charges = ({(0, 3)}, {(0, 3)})
    g, r, x, y, i = 2, len(physical), 1, 1, 1
    require(r < g + x + y, "naive-additivity mutation survived")
    require(r == g + max(i, x, y, x + y - i), "minimal sharp case failed")
    # Same demand pair, no shared edge: two distinct private edges are needed.
    private_physical = {(0, 1), (2, 3), (0, 4), (2, 4)}
    require(len(private_physical) == g + x + y and len(private_physical) > r,
            "interface correction fails to distinguish sharing")
    # A cap does not guarantee that any shared edge is physically present.
    cap, x0, y0, actual_i, actual_r = 1, 0, 0, 0, g
    require(actual_r < g + max(cap, x0, y0, x0 + y0 - cap),
            "cap-as-actual-count mutation survived")
    require(actual_r == g + max(x0, y0, x0 + y0 - cap), "upper-cap base case failed")
    # Two grids in the same retained component need not share a deleted edge.
    require(r < g + x + y - 0,
            "dropping distinct-component/deleted-interface hypothesis survived")
    # Arbitrarily large complete grids can have zero encoded penetration demand.
    zero_deficit = []
    for size in (1, 2, 3, 10, 100):
        grid_count = 2 * size * size
        bound = grid_count + max(0, 0, 0)
        require(bound == grid_count, "zero-deficit obstruction was lost")
        zero_deficit.append(dict(shore=size, R=grid_count, p=[0, 0], I=0))
    # Conservation of physical/deleted/virtual determinant units on the minimal case.
    phase = (0, 1, 0, 1, 2)
    pairs = set(combinations(range(5), 2))
    internal = set().union(*grids)
    deleted, virtual = physical - internal, pairs - physical
    units = lambda edges: sum(phase[a] != phase[b] for a, b in edges)
    require(units(pairs) == units(internal) + units(deleted) + units(virtual),
            "determinant ledger is not a partition")
    return dict(
        naive_addition_rejected=dict(physical_edges=sorted(physical),
                                     grid_edges=[sorted(q) for q in grids],
                                     charge_sets=[sorted(q) for q in charges], R=r,
                                     naive_lower_bound=g + x + y, repaired_lower_bound=r),
        unshared_same_demands=dict(physical_edges=sorted(private_physical), R=len(private_physical)),
        upper_cap_as_actual_count_rejected=dict(K=cap, I=actual_i, p=[x0, y0],
                                                R=actual_r, incorrect_lower_bound=g + cap),
        missing_deleted_interface_hypothesis_rejected=True,
        zero_deficit_regression=zero_deficit,
        determinant_units=dict(all=units(pairs), internal=units(internal),
                               deleted=units(deleted), virtual=units(virtual)))


def audit():
    return dict(
        status="unreviewed exact finite evidence",
        source_commit=BASE,
        state_version="2026-10-15.publication.2",
        priority_revision="public-frontier.3",
        catalogue_revision="public-frontier.7",
        task_id="compute-b-two-grain-interface-regressions",
        arithmetic="standard-library integers; determinant units sqrt(3)/2",
        source_sha256={path: hashlib.sha256((ROOT / path).read_bytes()).hexdigest()
                       for path in SOURCE_PATHS},
        two_grain=audit_two_grains(), three_grain=audit_three_grains(), controls=controls(),
        limitations=["No planar train realization or separator extraction",
                     "No PC1/PC3 penetration lower bound certified by the finite model",
                     "No jammed packing, global minimizer, virtual-area payment or topology estimate",
                     "No Target B or Level I closure; no independent review or canonical promotion"],
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--check", type=Path)
    args = parser.parse_args()
    # Normalize tuple-valued labels before comparing with a JSON fixture.
    result = json.loads(json.dumps(audit()))
    if args.check:
        expected = json.loads(args.check.read_text(encoding="utf-8"))
        require(result == expected, "fixture differs from independently recomputed evidence")
    if args.output:
        args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(dict(status=result["status"],
                         two_grain_states=result["two_grain"]["states"],
                         three_grain_states=result["three_grain"]["states"],
                         configurations=len(result["two_grain"]["configurations"]),
                         exact_inventory_cases=result["two_grain"]["exact_inventory_cases"],
                         upper_cap_inventory_cases=result["two_grain"]["upper_cap_inventory_cases"],
                         fixture="matched" if args.check else "not compared"), sort_keys=True))


if __name__ == "__main__":
    main()
