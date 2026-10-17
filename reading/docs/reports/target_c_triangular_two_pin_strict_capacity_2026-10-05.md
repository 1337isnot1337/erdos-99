> Generated reading edition · [exact source](../../../docs/reports/target_c_triangular_two_pin_strict_capacity_2026-10-05.md) · source SHA-256 `ac83868db308eefa21e107a2fb733c0803aa0c8dd849ae302e6a3d26d1642085`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-ACD3826933F8","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — two deleted triangular wall pins need not create an extra strict site

**Date:** 2026-10-05. **Checkpoint:** 03fda747.
**State:** 2026-10-05.audit.53.
**Classification:** rigorous regression and proved capacity candidate awaiting audit.
Unreviewed and noncanonical. **LEVEL I STATUS: STILL OPEN.**

## 1. Rejected activation step

The two-boundary-pin construction gives $K=(m-1)(n-1)$ strict interior
sites in a triangular rectangular frame. It is false, without further
size hypotheses, that the same two deleted pins always give $K+1$.

The statement fails at every $m=3,n\ge3$, including unbounded frame
length, and at the $4$-by-$4$ square. In these cases the strict capacity
is exactly $K$. This is a global arbitrary-point capacity bound in
the specified pinned container, stronger than a local motion obstruction.
It does not rule out an extra-site theorem with both side lengths large.
The pins contain unit triangles; they are not triangle-free global minimizers.

The desired but invalid implication was
$$
\text{two removed wall pins}
\ \Longrightarrow\ K+1\text{ strict interior sites}
\ \Longrightarrow\ \text{exclusion of one interior deficit near the triangular limit}.
$$
The one-pin positive-angle theorem remains valid; its angle-dependent
tolerance is not replaced by an angle-independent extra-site assertion.

## 2. A complete cover of every possible target

Let $u=(1,0)$, $v=(1/2,\sqrt3/2)$, and
$$
C=\{iu+jv:0\le i\le m,\ 0\le j\le n\}
$$
denote the parallelogram as a continuous region, not just its grid roster.
Keep every boundary lattice pin except $(1,0)$ and $(2,0)$.
A target packing $X\subset\operatorname{int}C$ must satisfy
$$
|x-y|>1\ (x\ne y),\qquad |x-w|>1\quad(w\text{ a retained pin}).
\tag{T.1}
$$

Triangulate $C$ into the elementary unit equilateral triangles
$$
\{(i,j),(i+1,j),(i,j+1)\},\qquad
\{(i+1,j),(i,j+1),(i+1,j+1)\}.
$$
Every point in a closed unit triangle is at distance at most one from
every vertex: distance is convex and its maximum over that triangle
occurs at a vertex. Thus a target cannot belong to any triangle containing
a retained pin. All targets are covered by the triangles whose vertices
are interior lattice sites or the two deleted pins. Boundary coincidences
are handled by closed triangles, not by ignoring measure-zero sets.

Assign each target to any containing admissible triangle. Two targets
cannot be assigned the same triangle, since its diameter is one.
Consequently the number of admissible triangles is a rigorous capacity
bound for arbitrary real-coordinate targets.

## 3. Every $3$-by-$n$ frame has strict capacity exactly $K$

For $m=3$, the nonfixed lattice vertices are precisely
$$
\{(1,j),(2,j):0\le j\le n-1\}.
$$
The admissible triangles triangulate the $1$-by-$(n-1)$ parallelogram
between those rows. Their number is
$$
2(n-1)=K.
$$
The assignment in Section 2 proves $|X|\le K$.
The exact all-size construction
[B.2](target_c_boundary_vacancy_funded_collective_refill_2026-10-05.md)
gives $K$ mutually strict interior points strictly clear of every retained
pin. Hence the bound is attained: strict capacity is exactly $K$ for
every integer $n\ge3$.

## 4. The $4$-by-$4$ square also has strict capacity exactly nine

There are ten admissible elementary triangles. Six form the complete
unit-triangle star around lattice vertex $(2,2)$. Each of those triangles
lies in the closed unit disk centered at that vertex, by convexity.

Six strictly unit-separated points cannot lie in a closed unit disk.
If one is at the center, it is within one of every other point.
Otherwise order the six polar angles. Some consecutive angular gap
is at most $\pi/3$. For radii $r,s\in[0,1]$ and such a gap,
$$
|x-y|^2\le r^2+s^2-rs\le1.
$$
The last quadratic is convex separately in each variable, and its four
corner values are $0,1,1,1$. This contradicts strict separation.

If ten targets existed, the triangle assignment would put exactly one in
each of the ten triangles. The six star targets would be in that one unit
disk, an impossibility. Therefore capacity is at most nine.
Construction B.2 supplies nine, so strict capacity equals $K=9$.

## 5. Certificate and precise surviving scope

    python3 research/verify_target_c_triangular_two_pin_capacity_2026_10_05.py

The checker enumerates the complete elementary triangulations, exact unit
edges, the retained wall and all admissible triangles. It verifies several
strip lengths and the six-triangle star. No sampled packing, optimizer
failure or rounded coordinate is used to prove an upper bound.

The exact failed activation is a two-pin $K+1$ theorem for all frames.
An asymptotic theorem with $\min(m,n)\to\infty$, a different funded
interface, or a positive-angle hypothesis remains a different proposition.
No canonical branch of E99 is eliminated by the regression itself.
