#!/usr/bin/env python3
"""Exact two-grain incidence audit of the MCP1/MCP2 accounting interface.

Five labelled trains form two fixed 1-by-1 grids and one pruned train. Each
non-grid pair in distinct directions is absent (virtual) or a deleted physical
crossing; each physical pair may be charged by either/both eligible endpoint
grids. Same-direction pairs cannot cross. Exhaust all 2,025 states. Directions
are u,v,u,v,w in the triangular frame: determinant areas are
integer multiples of sqrt(3)/2. No planar realization, coherence, penetration
depth, jammed packing, or global minimizer is asserted. This is unreviewed finite
evidence, not a new theorem or an implementation of the Target B shell bound.

Source: docs/reports/target_b_multicomponent_penetration_budget_2026-09-05.md,
Sections 2-3. Run from the public repository root with assertions enabled:
    python3 research/onboarding_two_grain_audit.py
"""
from itertools import combinations, product
import json


def audit():
    # H_0={0,1}, H_1={2,3}; vertex 4 was pruned. G_j has one edge.
    grains = ({0, 1}, {2, 3})
    internal = {(0, 1), (2, 3)}
    pairs = set(combinations(range(5), 2))
    external = sorted(pairs - internal)
    directions = (0, 1, 0, 1, 2)
    options = []
    for edge in external:
        if directions[edge[0]] == directions[edge[1]]:
            options.append([None])
            continue
        eligible = [j for j, grain in enumerate(grains) if len(set(edge) & grain) == 1]
        # None=absent. Empty tuple=physical but not charged. A tuple names the
        # grids actually charging this physical edge in X_j.
        options.append([None] + [tuple(j for j, bit in zip(eligible, bits) if bit)
                                 for bits in product((False, True), repeat=len(eligible))])
    checked = 0
    best_failure = None
    double_interface = False
    cross_virtual_witness = None
    for state in product(*options):
        physical = set(internal)
        charges = [set(), set()]
        for edge, selected in zip(external, state):
            if selected is not None:
                physical.add(edge)
                for j in selected:
                    charges[j].add(edge)
        deleted = physical - internal
        virtual = pairs - physical
        r = len(physical)
        total_grid_and_penetration = len(internal) + sum(map(len, charges))
        assert total_grid_and_penetration <= 2 * r
        incidences = [sum(len(set(edge) & grain) == 1 for edge in deleted) for grain in grains]
        assert sum(incidences) <= 2 * len(deleted)
        double_interface |= bool(deleted) and sum(incidences) == 2 * len(deleted)
        # Partition the determinant ledger before summing any grain estimates.
        area_units = lambda edges: sum(directions[a] != directions[b] for a, b in edges)
        assert area_units(pairs) == (area_units(internal) + area_units(deleted) + area_units(virtual))
        cross_virtual = {edge for edge in virtual
                         if any(edge[0] in g and edge[1] in h for g, h in (grains, grains[::-1]))}
        if cross_virtual_witness is None and area_units(cross_virtual):
            cross_virtual_witness = {"cross_grain_virtual_pairs": sorted(cross_virtual),
                                     "determinant_area_units": area_units(cross_virtual)}
        if total_grid_and_penetration > r:
            witness = {"physical_crossings": sorted(physical),
                       "grid_crossings": sorted(internal),
                       "penetration_sets": [sorted(x) for x in charges],
                       "R": r, "sum_grid_plus_penetration": total_grid_and_penetration,
                       "deleted_interface_edges": sorted(deleted),
                       "sum_deleted_endpoint_incidences": sum(incidences)}
            if best_failure is None or (r, sorted(physical)) < (best_failure["R"], best_failure["physical_crossings"]):
                best_failure = witness
        checked += 1
    assert checked == 2025
    assert best_failure is not None and best_failure["R"] == 3
    assert double_interface and cross_virtual_witness is not None
    return {
        "status": "finite model passed",
        "arithmetic": "integer incidence; determinant areas in units sqrt(3)/2",
        "domain": "two fixed disjoint one-edge grids, one pruned train, six optional distinct-direction pairs and all eligible penetration assignments; two parallel pairs always absent",
        "states": checked,
        "naive_single_charge_counterexample": best_failure,
        "cross_grain_virtual_mass_omitted_by_grain_internal_ledgers": cross_virtual_witness,
        "checks": ["MCP1 factor-two budget", "MCP2 deleted-edge multiplicity at most two", "retained/deleted/virtual pair partition"],
        "does_not_establish": "Geometric realization, PC penetration lower bounds, GPI additivity, topology correction, shell stability or Level I.",
    }


if __name__ == "__main__":
    print(json.dumps(audit(), indent=2, sort_keys=True))
