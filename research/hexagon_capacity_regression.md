<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "b368acfb5800c44200db465bbca25e231b138a97", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/hexagon_capacity_regression.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "2377b7631d1e202adf1dd90aaedc7d790ac7f304d6bd8eb9f67b7240fd7683aa"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Exact caged singleton capacity regression

This is a deliberately small obstruction to a tempting Target A shortcut.  It is
not a counterexample to Erdős Problem #99; it is a certified finite test for any
argument that tries to perturb the first triangle-producing capacity insertion.

Let

\[
v_k=(\cos(k\pi/3),\sin(k\pi/3)),\qquad 0\le k<6,
\]

and set

\[
B=\{v_0,\ldots,v_5\},\qquad X=B\cup\{0\},qquad H=\operatorname{conv}B.
\]

The six vertices form a regular unit hexagon.  Their consecutive distances are
one, all other vertex distances are at least one, and the unit-contact graph of B is
the cycle \(C_6\).  Therefore B is triangle-free and \(\operatorname{diam}B=2\).
The center is at distance one from every vertex, so X is unit-separated, has diameter
two, and contains the six unit triangles

\[
\{0,v_k,v_{k+1}\}\quad (k\bmod 6).
\]

This is an exact capacity endpoint for H.  The known values

\[
D(7)=2,
\qquad
D(8)=\frac1{2\sin(\pi/14)}>2
\]

give \(\alpha_1(H)\ge7\) from X and \(\alpha_1(H)\le7\), since eight unit-separated
points in H would have diameter at most two.  Thus \(X\) has maximum possible
cardinality in its hull.  The seven-point endpoint is also the known global
minimizer for \(n=7\), although B itself is not a six-point global minimizer.

In the strict-conflict graph from X to B, the center has no conflict edge: all six
distances are exactly one.  Relative to the obvious matching of the six vertices,
the center is a singleton fundamental circuit, so the capacity flag inserts it with
net surplus one.  The inserted point immediately creates triangles.

The center is also one-point infinitesimally locked while B is held fixed.  The six
active separation vectors are \(-v_k\), whose sum is zero.  Hence no nonzero velocity
has positive dot product with all six vectors.  Equivalently, the six contact rays
are not contained in an open semicircle.  This is the exact finite model behind the
`center_has_strict_one_point_escape: false` line produced by
[`capacity_flag.py`](capacity_flag.py).

## Consequence

The source-capacity flag and global optimality do not imply that its first triangle
can be removed by moving only the newly inserted point.  Any successful first-
transition theorem must use motion of the whole configuration, source-specific
capacity information, or a different global invariant.  This regression is stronger
than an abstract graph example because its endpoint capacity and diameter optimality
are certified by the exact (D(7)) and (D(8)) values.
