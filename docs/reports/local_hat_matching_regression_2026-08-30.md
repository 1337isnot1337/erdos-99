<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "90ff88cb59e4220d6e38b99325275880dc3cce49", "source_canonical": false, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "unreviewed", "source_path": "docs/reports/local_hat_matching_regression_2026-08-30.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "2eae21e5629d0c085918014d76dab21e0be370fd396a90ec48f63e8179e43485"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle was `unreviewed`; it is retained as provenance only. Destination status remains unreviewed/noncanonical.

# Local barycentric-hat matching regression

This note records an exact obstruction to a tempting shortcut in the triangular
lattice scaffold.  Let (u_0,u_2,u_4) be three unit lattice directions separated
by (120^circ), and choose

\[
r=\frac35.
\]

The three points (p_i=r u_i) are pairwise at distance

\[
\sqrt3r=\frac{3\sqrt3}{5}>1.
\]

Thus this is a unit-separated, triangle-free three-point set.  Each point lies on
an alternating lattice ray.  If one assigns to it the ordinary barycentric
weights in a chosen incident elementary triangle, its weight at the central
lattice vertex is (1-r=2/5).  The total central weight is therefore

\[
3(1-r)=\frac65>1.
\]

So the standard continuous piecewise-linear hat functions of the triangular
triangulation do **not** furnish a fractional matching from arbitrary
unit-separated, triangle-free points to lattice vertices.

This is not a Hall obstruction.  Each point is in a four-neighbor dimer region on
the corresponding lattice ray, and the three cells have distinct outer vertices
available for an integral matching.  The failure is specifically the choice of a
single-triangle barycentric rule, which ignores the extra dimer vertex on the
shared edge.

The exact regression is executable with:

```text
python -m unittest discover -s research -p 'test_local_hat_regression.py' -v
```

The lesson for Target A is narrow but binding: any fractional source-to-lattice
transport must use the full monomer--dimer conflict cell, or an equivalent
phase-aware rule.  A central-vertex mass estimate based only on one elementary
triangle is invalid even in a triangle-free configuration.
