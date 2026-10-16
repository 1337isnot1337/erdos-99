#!/usr/bin/env python3
"""Reproducible full-source exchange reconnaissance, not a Level I proof.

Sources are circular subsets of an exact rational unit-rhombus lattice. A bank
combines three rotated/translated near-triangular rational clouds; the bank
need not itself be feasible. Every successful output is separately certified.
"""

import argparse
from fractions import Fraction as Q
import json
from pathlib import Path

from global_cloud_exchange_2026_10_12 import distance2, search


def grid(radius, basis, offset=(Q(0), Q(0)), rotation=Q(0)):
    cosine = (1 - rotation * rotation) / (1 + rotation * rotation)
    sine = 2 * rotation / (1 + rotation * rotation)
    points = []
    bound = int(radius) * 2 + 3
    for i in range(-bound, bound + 1):
        for j in range(-bound, bound + 1):
            x, y = Q(i) + j * basis[0], j * basis[1]
            p = (cosine * x - sine * y + offset[0],
                 sine * x + cosine * y + offset[1])
            if distance2(p, (Q(0), Q(0))) <= radius * radius:
                points.append(p)
    return points


def instance(radius):
    t = Q(577351, 1000000)
    v = ((1 - t * t) / (1 + t * t), 2 * t / (1 + t * t))
    source = grid(Q(radius), v)
    basis = (Q(1, 2), Q(866025404, 1000000000))
    cloud = []
    for offset, rotation in (
        ((Q(1, 2), Q(0)), Q(0)),
        ((Q(1, 3), Q(1, 7)), Q(1, 5)),
        ((Q(-1, 5), Q(1, 4)), Q(2, 5)),
    ):
        cloud.extend(grid(Q(radius) + Q(1, 5), basis, offset, rotation))
    return source, cloud


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--radii", type=int, nargs="+", default=[4, 6, 8])
    parser.add_argument("--seconds", type=float, default=30)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    for radius in args.radii:
        source, cloud = instance(radius)
        print(json.dumps({"radius": radius, "source_labels": len(source),
                          "cloud_labels": len(cloud), "phase": "exact graph construction"}),
              flush=True)
        summary, certificate = search(source, cloud, args.seconds,
                                      f"full circular unit-rhombus source R={radius}")
        summary["radius"] = radius
        if certificate is not None:
            path = args.output_dir / f"radius_{radius}_certificate.json"
            path.write_text(json.dumps(certificate, sort_keys=True, indent=2) + "\n")
            summary["certificate"] = str(path)
        (args.output_dir / f"radius_{radius}_summary.json").write_text(
            json.dumps(summary, sort_keys=True, indent=2) + "\n")
        print(json.dumps(summary, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
