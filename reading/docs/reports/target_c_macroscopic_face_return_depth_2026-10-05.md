> Generated reading edition · [exact source](../../../docs/reports/target_c_macroscopic_face_return_depth_2026-10-05.md) · source SHA-256 `364a03dcbf95893cbad5e223a2a418bc1fe25e3bec38bb01bfd07415deb3e75a`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-AA632E4F0858","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — deep macroscopic physical faces force a quadratic contact core

Date: 2026-10-05. Base main: `3c94a1a93641a5f8fa24d43068d487594d3e38cd`.
State: `2026-10-05.audit.57`. Classification: **proved candidate awaiting
independent audit**; artifact lifecycle remains **unreviewed**.
C-II and Level I remain open.

## 1. Exact implication

```
macroscopic actual contact face with more than half its boundary
macroscopically distant from actual loaded vertices
-> canonical disjoint return quota forces linearly many long contact paths
-> quadratic nonisolated core population
-> contradict subquadratic-core subsequence.
```

This eliminates a genuine geometric subcase of the inactive-container
route. It does not eliminate a boundary-attached face, an outer pocket,
an exterior cap, or a macrochamber subsequence with quadratic core.
The finite statement also gives a depth profile valid outside the
subquadratic-core regime. It assigns no packing sites to return lengths.

The sole nontrivial input is canonical `C-GLOBAL-FACE-RETURN-QUOTAS`,
[Theorem GQ.1 and its single-face corollary](target_c_global_exceptional_face_return_quotas_2026-10-04.md).
Use the full-boundary convention, including length-zero paths at loaded
boundary vertices. No independent path families are added together.

## 2. Finite source-depth theorem

Let V be the canonical positive-contact core and B its actual loaded
vertices. Let C be a bounded actual physical contact face with a simple
boundary cycle of m>=5 vertices. For x on its boundary put

    d(x)=min_{b in B}|x-b|.

Sort these depths as d_1<=...<=d_m and set

    k=ceil((m+2)/2).

Then

    |V|>=k+sum_{i=1}^k ceil(d_i).                 (2.1)

In particular, if t boundary vertices have d(x)>=rho, where rho>0,

    |V|>=k+ceil(rho)*max(0,k-m+t).               (2.2)

**Proof.** The canonical single-face theorem gives k simultaneously
vertex-disjoint actual contact paths from distinct boundary vertices
to distinct actual loaded vertices. Stop them at the first loaded
vertex. A path starting at x has at least ceil(d(x)) edges, because
each physical contact edge has Euclidean length one. It therefore
contains at least 1+ceil(d(x)) core vertices. Vertex disjointness
permits summation in the core population, giving at least k plus the
sum of the chosen k rounded depths. Among all choices of k boundary
vertices the k smallest depths minimize this sum, proving (2.1).
At most m-t chosen starts can be shallow, so at least k-m+t of the
paths, if positive, have depth at least rho. This proves (2.2). QED.

Path length zero is consistent with ceil(0)=0 and contributes its one
loaded vertex. Contact isolates are not path vertices and are not
counted in |V|. They remain in the full source; no full-source population
is substituted for |V| and no isolate rigidity is asserted.

## 3. Exact asymptotic exclusion

Consider a canonical sequence with D tending to infinity and
|V|=o(D^2). Suppose the chosen actual physical face has area at least
a D^2 for a fixed a>0. Its perimeter equals m, since every boundary
edge is an actual unit contact. The isoperimetric inequality implies

    m>=2sqrt(pi*a)*D.

The canonical chamber-perimeter budget gives m=O(D). For fixed
eta>0 let t_eta count its boundary vertices at distance at least
eta D from B. Rearranging (2.2) gives

    t_eta<=m-k+(|V|-k)/ceil(eta D)
          <=m/2+o(D).                          (3.1)

Consequently at least m/2-o(D) boundary vertices lie within eta D of
actual loaded vertices, for every fixed eta>0. No common rate for
eta tending to zero is asserted.

If for some fixed eta,epsilon>0 the face has

    t_eta>=m/2+epsilon D,

then (2.2) gives |V|>=eta*epsilon D^2 up to lower-order terms,
a contradiction. In particular a physical macroface whose entire
boundary stays a fixed fraction of D away from B is impossible on a
subquadratic-core subsequence.

This is a statement about actual source contact paths and actual loaded
endpoints, not an abstract separator ledger or a nonconsecutive grid.

## 4. Composition with the live container route

Canonical Section 77's inactive chambers can be physical faces or outer
pockets. The physical-face case has an actual unit-contact wall, so its
wall-safe region has the canonical shield. Its old interior population
consists of contact isolates. An equal-cardinality strict refill of only
those isolates removes no contact; one extra guarded site is still
needed for the contact-minimality contradiction. Theorem (3.1) does not
provide that extra site.

In the subquadratic-core case, an argument producing a deeply internal
macroface is now contradictory. Any surviving physical macroface must
instead have at least half its wall population close to actual loaded
vertices at each fixed macroscopic scale. Its original capacity problem
therefore includes this boundary attachment, rather than a freely
isolated interior chamber.

For outer pockets, a closing hull chord need not be a unit contact and
can be macroscopically long. This proof cannot treat that chord as a
physical return path or invoke a unit-wall shield across it. Exterior
caps likewise require their own actual protected-wall extraction.
The finite contact-manifold and residual-cage theorem is valid on the
canonical core in the container branch, as stated by the manifest, but
it supplies neither these walls nor their packing surplus.

The general Type-I/macroscopic-container branch also permits quadratic
core population. In that case (2.1) is a population lower bound, not a
contradiction. No exhaustive branch or Level I lifecycle is changed.

## 5. Validation scope

The finite counting proof is analytic and uses an already canonical
integral disjoint-path theorem. There is no new arithmetic search or
verifier. State and artifact checks certify repository consistency only;
independent audit of this new composition is still required.
