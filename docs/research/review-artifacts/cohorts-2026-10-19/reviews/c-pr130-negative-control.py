#!/usr/bin/env python3
"""Exact rational rectangle control for normalized versus unnormalized lifts."""
from fractions import Fraction as F
from itertools import combinations
import json
from pathlib import Path

p = [(F(0), F(0)), (F(1), F(0)), (F(0), F(2)), (F(1), F(2))]
colors = [0, 1, 0, 1]
t2 = F(1, 4)
pairs = []
for i, j in combinations(range(4), 2):
    d2 = sum((a - b) ** 2 for a, b in zip(p[i], p[j]))
    same = colors[i] == colors[j]
    normalized = d2 / (1 + t2) if same else (d2 + t2) / (1 + t2)
    unnormalized = d2 if same else d2 + t2
    pairs.append({"pair": [i, j], "source_d2": str(d2), "same_color": same,
                  "normalized_d2": str(normalized), "unnormalized_d2": str(unnormalized)})
old_d2 = max(F(x["source_d2"]) for x in pairs)
normalized = [F(x["normalized_d2"]) for x in pairs]
unnormalized = [F(x["unnormalized_d2"]) for x in pairs]
result = {
    "source_vertices": [[str(a), str(b)] for a, b in p],
    "colors": colors,
    "unit_edge_simplex_coordinates": {"color0": "-1/2", "color1": "1/2"},
    "t": "1/2", "t_squared": str(t2), "source_diameter_squared": str(old_d2),
    "same_color_separation_slack_min": str(F(4) - 1),
    "pairs": pairs,
    "normalized_minimum_squared_distance": str(min(normalized)),
    "normalized_diameter_squared": str(max(normalized)),
    "normalized_strict_diameter_drop": max(normalized) < old_d2,
    "normalized_all_pairs_unit_separated": min(normalized) >= 1,
    "unnormalized_minimum_squared_distance": str(min(unnormalized)),
    "unnormalized_diameter_squared": str(max(unnormalized)),
    "unnormalized_unit_contact_preservation": all(
        (F(x["source_d2"]) == 1) == (F(x["unnormalized_d2"]) == 1) for x in pairs),
    "unnormalized_diameter_improved": max(unnormalized) < old_d2,
    "affine_flattening": {
        "reason": "z=x-1/2, so the added coordinate t*z is affine in x",
        "affine_rank": 2,
    },
}
assert t2 < 3
assert result["normalized_minimum_squared_distance"] == "1"
assert result["normalized_diameter_squared"] == "21/5"
assert result["normalized_strict_diameter_drop"]
assert result["normalized_all_pairs_unit_separated"]
assert result["unnormalized_minimum_squared_distance"] == "5/4"
assert result["unnormalized_diameter_squared"] == "21/4"
assert not result["unnormalized_unit_contact_preservation"]
assert not result["unnormalized_diameter_improved"]
print(json.dumps(result, indent=2))
