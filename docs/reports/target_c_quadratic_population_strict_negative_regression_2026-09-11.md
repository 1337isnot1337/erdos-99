<!-- theorem-state: {"artifact_id":"ART-CDDA6C6EB20F","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C: quadratic-population strict-negative response regression

**Date:** 2026-09-11  
**Status:** STILL OPEN; regression report  
**Target:** C-II strict-negative transfer and isolated-source population  

## Statement

There is a sequence of triangle-free, unit-separated configurations \(A_D\) with

\[
\operatorname{diam}(A_D)=D,\qquad
|A_D|=\frac{\pi}{2\sqrt3}D^2-O(D),
\]

whose only unit contacts are a regular polygon boundary cycle and whose positive
KKT stress has a strict-negative C53 transfer. Thus even quadratic population at
the asymptotically optimal density does not by itself exclude the strict-negative
response phase when contact-isolated source points are retained.

No global-optimality claim is made.

## Construction

Let \(k\to\infty\), let \(R=1/(2\sin(\pi/(2k)))\), and take the regular \(2k\)-gon
on the circle of radius \(R\). Its side length is one and its diameter is
\(D=2R\). Let \(s=1+D^{-1}\), and let \(\Lambda_s\) be a triangular lattice with
nearest-neighbor spacing \(s\). Add all lattice points in the disk
\(B(0,R-2)\), after deleting any duplicate points (there are none for large \(D\)).

The lattice cloud has

\[
\frac{2}{\sqrt3s^2}\pi(R-2)^2+O(R)
=\frac{\pi}{2\sqrt3}D^2-O(D)
\]

points. Every cloud point is at distance at least \(2\) from every polygon vertex,
and distinct cloud points are at distance at least \(s>1\). The only unit contacts
are the consecutive polygon vertices. All points lie in \(B(0,R)\), while the
antipodal polygon vertices are \(D\) apart, so the diameter is exactly \(D\).

The unit-contact graph is \(C_{2k}\), and the cloud contributes no unit edges.
Hence the whole configuration is triangle-free.

## Strict-negative KKT response

Give the polygon contact edges coefficient

\[
\alpha=\frac1{2k\sin^2(\pi/(2k))}
\]

and its antipodal diameter edges coefficient \(\beta=1/k\); give every cloud point
zero coefficients. The same calculation as in the regular-polygon report gives

\[
\sum_C\alpha=D^2,\qquad \sum_H\beta=1,\qquad
L_C(\alpha)P=L_H(\beta)P.
\]

The cloud points have zero rows in both weighted Laplacians, so they do not alter
equilibrium or the response on the polygon boundary. The response is the cycle
response, and for the oriented antipodal incidence columns
\(q_i=e_{i+k}-e_i\),

\[
\boxed{
q_{k-1}^{\mathsf T}\Lambda^+q_0
=\frac1\alpha\left(1-\frac k2\right)<0.
}
\]

Thus the strict-negative transfer persists with \(n\asymp D^2\), not merely in a
linear-size boundary cycle.

## Exact scope

The construction is not a counterexample to Erdős Problem #99. Its interior cloud
is deliberately inactive and no proof says that the displayed \(D\) is minimal
for its cardinality. It proves a narrower no-go statement:

\[
\text{quadratic population}+\text{triangle-free packing}
\]

does not force a nonnegative C53 transfer or a dense contact core. A closing proof
must use the same-cardinality global minimum-diameter condition to rule out this
inactive-cloud mechanism. This is exactly the population/optimality input missing
from the strict-negative C-II branch.
