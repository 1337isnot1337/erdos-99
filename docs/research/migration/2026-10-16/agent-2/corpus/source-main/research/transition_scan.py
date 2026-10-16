#!/usr/bin/env python3
"""Scan small triangular-lattice capacity flags for first bad transitions.

The scan is deliberately finite and diagnostic. A capacity shore X is a finite
triangular-lattice patch, and B ranges over its triangle-free subshores. For each
B the exact strict-conflict exchange flag is built. At the first flag member
containing a unit triangle, the script tests whether every newly inserted point
appearing in that triangle is locally caged when all other points are held fixed.

The one-point test uses the exact closed-semicircle criterion for the active unit
contacts. This matters on the boundary case: when the contact directions fit in a
closed but not open semicircle, there is no strict first-order escape, but a
nontrivial finite motion still exists because first-order-neutral contacts open
quadratically. Diameter constraints are omitted, so an ``escapable`` label does
not certify feasibility in the full Target A configuration.
"""

from __future__ import annotations

import argparse
import itertools
import json
import sys
from collections import Counter
from pathlib import Path


if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parent))

from capacity_flag import (  # noqa: E402
    Point,
    assert_flag_invariants,
    exchange_flag,
    triangular_points_in_box,
    unit_separated,
    unit_triangles,
)
from escape_cone import fits_closed_semicircle  # noqa: E402


def configuration_labels(record: dict) -> list[tuple[str, int]]:
    """Return labels in the order used by ``exchange_flag`` triangle indices."""
    return [("B", i) for i in record["right_indices"]] + [
        ("X", i) for i in record["left_indices"]
    ]


def first_transition_report(
    basis_points: list[Point],
    capacity_points: list[Point],
    flag: dict,
) -> dict | None:
    """Summarize the first flag record containing a unit triangle."""
    previous_left: set[int] = set()
    for record in flag["flags"]:
        current_left = set(record["left_indices"])
        triangles = record["unit_triangles"]
        labels = configuration_labels(record)
        new_left = current_left - previous_left
        if triangles:
            configurations = [
                basis_points[i] for i in record["right_indices"]
            ] + [capacity_points[i] for i in record["left_indices"]]
            triangle_details = []
            for triangle in triangles:
                triangle_labels = [labels[i] for i in triangle]
                inserted = [
                    label for label in triangle_labels
                    if label[0] == "X" and label[1] in new_left
                ]
                escape = {}
                for shore, index in inserted:
                    point_index = labels.index((shore, index))
                    vectors = [
                        (
                            configurations[point_index][0] - point[0],
                            configurations[point_index][1] - point[1],
                        )
                        for other_index, point in enumerate(configurations)
                        if other_index != point_index
                        and abs(
                            (configurations[point_index][0] - point[0]) ** 2
                            + (configurations[point_index][1] - point[1]) ** 2
                            - 1.0
                        )
                        <= 1e-8
                    ]
                    escape[str(index)] = fits_closed_semicircle(vectors)
                triangle_details.append(
                    {
                        "labels": triangle_labels,
                        "new_insertions": inserted,
                        "one_point_escape": escape,
                        "locally_caged": bool(inserted)
                        and all(not value for value in escape.values()),
                    }
                )
            return {
                "step": record["step"],
                "new_left_count": len(new_left),
                "triangle_count": len(triangles),
                "triangles": triangle_details,
                "locally_caged_triangle_count": sum(
                    item["locally_caged"] for item in triangle_details
                ),
            }
        previous_left = current_left
    return None


def scan(width: float, height: float) -> dict:
    capacity = triangular_points_in_box(width, height)
    first_steps: Counter[int] = Counter()
    insertion_sizes: Counter[int] = Counter()
    status: Counter[str] = Counter()
    source_count = 0
    bad_source_count = 0
    bad_triangle_count = 0
    caged_triangle_count = 0
    examples: list[dict] = []

    for size in range(1, len(capacity) + 1):
        for indices in itertools.combinations(range(len(capacity)), size):
            basis = [capacity[i] for i in indices]
            if not unit_separated(basis) or unit_triangles(basis):
                continue
            source_count += 1
            flag = exchange_flag(basis, capacity)
            assert_flag_invariants(basis, capacity, flag)
            report = first_transition_report(basis, capacity, flag)
            if report is None:
                continue
            bad_source_count += 1
            bad_triangle_count += report["triangle_count"]
            caged_triangle_count += report["locally_caged_triangle_count"]
            first_steps[report["step"]] += 1
            insertion_sizes[report["new_left_count"]] += 1
            for item in report["triangles"]:
                status["caged" if item["locally_caged"] else "escapable"] += 1
            if len(examples) < 12:
                examples.append(
                    {
                        "basis_indices": list(indices),
                        "first_transition": report,
                    }
                )

    return {
        "capacity_width": width,
        "capacity_height": height,
        "capacity_points": len(capacity),
        "triangle_free_subshores": source_count,
        "subshores_with_first_triangle": bad_source_count,
        "first_triangle_count": bad_triangle_count,
        "locally_caged_first_triangle_count": caged_triangle_count,
        "triangle_status": dict(sorted(status.items())),
        "first_step_histogram": dict(sorted(first_steps.items())),
        "new_insertion_count_histogram": dict(sorted(insertion_sizes.items())),
        "examples": examples,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--width", type=float, default=2.0)
    parser.add_argument("--height", type=float, default=2.0)
    args = parser.parse_args()
    print(json.dumps(scan(args.width, args.height), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
