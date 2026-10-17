> Generated reading edition · [exact source](../../../docs/reports/target_c_global_exceptional_face_return_quotas_2026-10-04.md) · source SHA-256 `098d8f5ef1e1236241fb93f5d4f3400f9458e26652fba836b196115e2eed5ae6`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-E3C3DD7BE585","canonical":true,"claim_ids":["C-GLOBAL-FACE-RETURN-QUOTAS"],"claim_statuses":{"C-GLOBAL-FACE-RETURN-QUOTAS":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C — global exceptional-face quotas for disjoint loaded returns

**Date:** 2026-10-04
**Starting commit:** `f539af073a691c13327a0a7fef3c746fb7704e5f`
**State version:** `2026-09-14.audit.51`
**Run:** closing-proof continuation after PR #699
**Classification:** canonical in `2026-10-05.audit.53` as `C-GLOBAL-FACE-RETURN-QUOTAS` after independent promotion audit
**LEVEL I STATUS: STILL OPEN. C-II REMAINS OPEN.**

## 1. Endpoint and dependencies

The new implication is

```text
mixed rigidity + positive unloaded equilibrium + minimum-separator exposure
  -> total selected exceptional-face defect <= twice separator cardinality - 4
  -> simultaneous actual contact returns with a separate quota for every face
  -> global returns from a persistent high-degree tail, including mesoscopic faces.
```

This closes the cross-face reuse issue for the **return-count demand defined
below**. It does not identify the length of a return with independent face,
train, or route-excess currency. It is not a second-depletion theorem or a
strict-diameter competitor.

Canonical inputs are `C-ZRF` ([Section 57](../targets/target-c/57-zr-zf-rigidity-audit.md)),
positive unloaded equilibrium and the loaded force hull, and
`C-ATTACH-CURRENCY`, `C-HARMONIC-CARRIER-QUAD`, and `C-HARMONIC-CELL-TILING`
([Sections 62](../targets/target-c/62-attachment-incidence-currency-audit.md),
[82](../targets/target-c/82-harmonic-cell-near-quadrangulation-audit.md), and
[83](../targets/target-c/83-attachment-cell-disjoint-tiling-audit.md)). The
full-core application also uses canonical `C-FULLCORE-LOADED-CHORD`.
No theorem of drafts #668 or #671 is a premise of the finite theorem. Their
current inspected tips are respectively `a2ccd6161519c7d27482a7c6e751cd44e595e1b6`
and `0e49b450cc4819cc2f4f205303cbb9a09b45d269`.

## 2. Exact finite source class

Let (P) be a canonical triangle-free C-II source with (D\ge9). Keep its
entire source, including contact-isolated points. Write (V) for its
nonisolated positive-contact core, (C) for the actual contact graph, and
(B) for the actual loaded diameter endpoints. We use:

1. (C) is a simple plane graph with no triangles;
2. every vertex of (B) is an extreme vertex of the force hull
   (F=\operatorname{conv}B), and (V\subset F);
3. the mixed contact/diameter framework on (V) has only Euclidean
   infinitesimal flexes;
4. at every vertex of (V\setminus B), all contact coefficients in its
   equilibrium equation are strictly positive;
5. at least two distinct vertices belong to (B).

Allow a set (E_0) of auxiliary straight edges between vertices of (B),
so that (G=C\cup E_0) is a simple plane graph. Keep an edge once if it is
already a contact, and then regard it as physical rather than auxiliary.
Auxiliary edges are bookkeeping edges, never packing constraints or paths.

Let $`\mathcal F`$ be a nonempty family of bounded faces of (G) with simple
boundary cycles and degrees (m_f\ge5). Define

```math
 Q_{\mathcal F}=\sum_{f\in\mathcal F}(m_f-4),\qquad
 X_{\mathcal F}=\bigcup_{f\in\mathcal F}V(\partial f).
 \tag{2.1}
```

A separator (S\subset V) removes vertices, including possible endpoints:
(C-S) has no path from (X_{\mathcal F}\setminus S) to (B\setminus S).
A path of length zero at (X_{\mathcal F}\cap B) is allowed in this full-boundary
convention. Unloaded-only starts are treated separately in Section 5.

## 3. Minimum-separator defect theorem

**Theorem GQ.1.** For a minimum-cardinality separator (S), put (k=|S|).
Let (U) be the union of the components of (C-S) meeting
(X_{\mathcal F}\setminus S), and let (c_U) be their number. Form (K)
from the induced physical contact graph on (U\cup S), together with all
auxiliary edges of (G) whose endpoints remain. Write (c_K) for the number
of components of (K). Then

```math
 \boxed{Q_{\mathcal F}\le 2k-2c_U-4c_K\le2k-4.}
 \tag{3.1}
```

In particular there are at least

```math
 \boxed{\left\lceil\frac{Q_{\mathcal F}+4}{2}\right\rceil}
 \tag{3.2}
```

simultaneously vertex-disjoint actual contact paths from the selected face
boundaries to distinct actual loaded vertices.

### 3.1 Pinned rank and positive left nullity

Every component (U_j) of (U) is unloaded. Every physical contact neighbor
outside (U_j) lies in (S). Let (n_j,e_j,t_j) count its vertices, internal
contacts, and contacts to (S).

The contact rigidity matrix on its (2n_j) columns has full column rank.
A kernel vector extended by zero to (V\setminus U_j) would be a mixed
infinitesimal flex: no actual diameter is incident to (U_j). Mixed rigidity
makes it Euclidean. It vanishes at the two distinct loaded vertices, hence
is zero.

Positive equilibrium on (U_j) supplies a nonzero dependence of the same
rows. Thus (e_j+t_j\ge2n_j+1). Summing over the disjoint components,

```math
 e_U+t_U\ge2|U|+c_U. \tag{3.3}
```

Let (e_S) count physical contacts internal to (S), and (a) count retained
auxiliary edges. Auxiliary edges have both endpoints in (S), because
(U\cap B=\varnothing). Therefore

```math
 e(K)=e_U+t_U+e_S+a\ge2|U|+c_U+e_S+a.
 \tag{3.4}
```

### 3.2 Every separator vertex is exposed on an outer walk

Minimum cardinality implies inclusion minimality. Restoring one (s\in S)
creates an (X_{\mathcal F})-to-(B) path avoiding (S\setminus\{s\}).

If (s\notin B), follow the suffix from (s) to its first loaded vertex.
After leaving (s), this suffix lies in a component of (C-S) meeting
(B\setminus S). Such a component is disjoint from (U\cup S). Its loaded
endpoint (b\notin K) is outside (\operatorname{conv}V(K)): loaded extremality
implies (b\notin\operatorname{conv}(V\setminus\{b\})).
The suffix cannot cross (K), since (G) is plane. It must therefore leave
(s) through the unbounded face of the component of (K) containing (s).
Thus (s) has an occurrence on that component's outer walk. If (s\in B),
loaded extremality gives the same exposure directly.

Every (s) is incident to an edge of (K). Indeed, the restoring path either
has a prefix from (X_{\mathcal F}\setminus S) through a component of (U) to
(s), supplying an incident physical edge of (K), or starts at (s\in X_{\mathcal F}).
In the latter case its selected face cycle is wholly retained in (K).
Consequently no separator vertex is a singleton component of (K).

Choose one outer occurrence of each separator vertex. Let (b_K) be the sum
of the occurrence lengths of all component outer walks, and (a_{\rm out})
the number of auxiliary outer occurrences. Between consecutive chosen
occurrences an interval has length at least two unless it is one edge with
both endpoints in (S). Such one-step intervals use at most (2e_S) physical
occurrences and at most (a_{\rm out}) auxiliary occurrences. Hence

```math
 b_K\ge2k-2e_S-a_{\rm out}. \tag{3.5}
```

A bridge may contribute both orientations. This is why the physical term is
(2e_S), not (e_S). A component with one chosen occurrence contributes its
entire nonzero outer walk as one interval, of length at least two.

### 3.3 Euler and triangular-face cancellation

For each component of (K), apply Euler with its own outer facial walk.
Let (F_3(K)) count bounded degree-three faces and let
(Q^+(K)=\sum_{\deg g\ge5}(\deg g-4)). The graph is simple; bounded face walks
have degree at least three. Exact occurrence counting gives

```math
 b_K-F_3(K)+Q^+(K)=4|V(K)|-2e(K)-4c_K.
 \tag{3.6}
```

Every bounded triangular face uses an auxiliary edge, since the physical
contact graph is triangle-free. An auxiliary edge has two side occurrences;
(a_{\rm out}) of the total (2a) occurrences are outer. Charging a triangle
to one auxiliary bounded-side occurrence gives

```math
 F_3(K)\le2a-a_{\rm out}. \tag{3.7}
```

All vertices and edges of each selected simple face cycle are in (K).
Its interior was empty in (G), so it remains a bounded face of its component
of (K). Thus (Q_{\mathcal F}\le Q^+(K)). Combining (3.4)--(3.7),

```math
\begin{aligned}
 Q_{\mathcal F}
 &\le4k-2c_U-2e_S-2a-4c_K-b_K+F_3(K)\\
 &\le2k-2c_U-4c_K.
\end{aligned}
```

The family is nonempty, so (c_K\ge1). This proves (3.1). This argument
allows two triangular faces on opposite sides of one virtual chord; it does
not incorrectly assert one triangular face per auxiliary edge.

### 3.4 Paths are finite and integral

Split each physical graph vertex into an input and output with a unit-capacity
arc. Replace each physical contact by two directed arcs of capacity
(M>|V|); connect a supersource to the inputs of (X_{\mathcal F}) and the
outputs of (B) to a supersink with capacity (M). Integral augmenting paths
give an integral maximum flow. A minimum cut of value at most (|V|) cannot
use an (M)-arc, so its cut vertex arcs are exactly an endpoint-inclusive
separator. Flow decomposition gives the same number of vertex-disjoint
actual contact paths. The minimum-separator bound therefore proves (3.2).

Auxiliary edges are absent from this flow network.

## 4. Stronger single-face corollary

For one degree-(m\ge5) face, its full-boundary minimum separator satisfies

```math
 \boxed{k\ge\left\lceil\frac{m+2}{2}\right\rceil.} \tag{4.1}
```

If (U\ne\varnothing), use (c_U\ge1) and (c_K\ge1) in (3.1), with
(Q=m-4). If (U=\varnothing), all (m) boundary vertices are in (S), so
(k\ge m\ge(m+2)/2). These alternatives are exhaustive.

If the face has $`\ell`$ loaded boundary vertices, there are at least

```math
 \boxed{\max\left\{0,\left\lceil\frac{m+2}{2}\right\rceil-\ell\right\}}
 \tag{4.2}
```

vertex-disjoint contact returns with unloaded starts and distinct loaded ends.
For an unloaded-start separator, adding those $`\ell`$ loaded boundary vertices
gives a full-boundary separator. Thus its size plus $`\ell`$ is at least (4.1).

This strengthens the face-local ((m-2\ell)/(4\pi+2)) return floor of draft
#671 under the explicit plane-augmentation/source hypotheses above. It does
not import its cap extraction or claim any positive route-length currency.

## 5. Simultaneous quotas for every face

Let $`\ell_f=|V(\partial f)\cap B|`$, and define the integer demand

```math
 r_f=\max\left\{0,\left\lfloor\frac{m_f-4}{2}\right\rfloor-\ell_f\right\}.
 \tag{5.1}
```

**Theorem GQ.2.** All demands can be realized simultaneously: for every (f)
there are (r_f) physical contact paths starting at distinct unloaded vertices
of $`\partial f`$ and ending at distinct actual loaded vertices. Paths for
different faces are also vertex-disjoint. Each path can stop at its first
loaded vertex. A shared boundary vertex can serve only one demand.

### Proof

Discard zero-demand faces. For every subfamily $`\mathcal E`$, adding the union
of its loaded boundary vertices to any unloaded-start separator makes a
full-boundary separator. By (3.1), its unloaded-start minimum separator has
size at least

```math
 \frac{Q_{\mathcal E}}2+2
 -\left|\bigcup_{f\in\mathcal E}(V(\partial f)\cap B)\right|
 \ \ge\sum_{f\in\mathcal E}r_f. \tag{5.2}
```

The union is bounded by $`\sum\ell_f`$; hence repeated loaded occurrences do
not supply extra capacity.

In the vertex-split physical network, add one node per face, an arc of
capacity (r_f) from the supersource to that node, and arcs of capacity
(M>|V|+\sum r_f) from it to the inputs of its unloaded boundary vertices.
Keep the unit vertex arcs and the physical-contact and sink arcs.

For any cut of capacity below $`\sum r_f`$, no (M)-arc is cut. Let
$`\mathcal E`$ be the face nodes on its source side. The cut pays
$`\sum_{f\notin\mathcal E}r_f`$ on the source arcs. Its cut vertex arcs form
a separator between the unloaded starts of $`\mathcal E`$ and (B), and
by (5.2) pay at least $`\sum_{f\in\mathcal E}r_f`$. Contradiction. Integral
flow therefore saturates every face demand. Flow decomposition and stopping
at the first loaded vertex prove the theorem. □

The result allocates face defect before constructing the paths. It does not
add independently chosen path families after the fact.

## 6. Full-core high-degree tail and mesoscopic faces

In the sufficiently large canonical full-core branch, all physical loaded-
loaded contacts are force-hull sides. Add every harmonic attachment-polygon
side to the full core, retaining coincident edges once. This is a plane
augmentation: canonical Section 83 gives disjoint cell interiors, and
harmonic trapping places each unloaded component inside its own polygon.
Physical contacts between different unloaded components do not exist; all
remaining physical loaded-loaded contacts lie on the force hull.
Bounded augmented-cell faces remain faces in this global augmentation.

For a family of such faces with (m_f>M\ge5), put

```math
 T_M=\sum_{m_f>M}(m_f-4),\quad N_M=\#\{f:m_f>M\},\quad
 L_M=\sum_{m_f>M}\ell_f.
```

The unconditional quota consequence is

```math
 \boxed{p_M\ge\sum r_f\ge\frac12T_M-\frac12N_M-L_M.} \tag{6.1}
```

The first bound is nonnegative; a negative last expression is harmless.
This handles any number and any degrees of the faces, including degrees
(o(D)). No individual face needs macroscopic perimeter.

If each selected face has at most two loaded vertices, then

```math
 \boxed{p_M\ge\left(\frac12-\frac{5}{2(M-3)}\right)T_M.} \tag{6.2}
```

Indeed (N_M\le T_M/(M-3)), because degrees are integer and (m_f>M).
For the augmented graph built from internal and attachment contacts only,
the at-most-two-loaded-vertices assertion follows from the face crosscut
argument independently stated in draft #668. Using (6.2) requires that extra
topological statement; (6.1) requires no bound on loaded incidence. In the
full-core graph a restored physical loaded-loaded polygon side simply
reclassifies the corresponding auxiliary edge and changes no face.

For a sequence with $`T_M=\Theta(D)`$, and then (M\to\infty), (6.2) gives
asymptotically one globally disjoint loaded return per two tail-defect units.
More precisely, fix (M) first and use the displayed coefficient at every
finite source. If $`\liminf T_M/D\ge\tau_M`$, then

```math
 \liminf p_M/D\ge
 \left(\frac12-\frac{5}{2(M-3)}\right)\tau_M
```

whenever the coefficient is nonnegative. No unsupported diagonal choice of
(M=M_D) is needed.

## 7. Substitution into the post-#699 frontier

The trusted proof-only #699 identity remains

```math
5m_B+4S+2\sigma_R
\ge2(\pi+s)D+5k+2(Q-f)+2(b-P_F)-o(D),
\quad s=\sqrt{\pi/(2\sqrt3)}.
```

The new theorem supplies **independent face-indexed return counts**. It does
not prove that these paths are stopped trains, that incident rhombi can be
deleted at (o(D^2)) cost, or that the sum of path lengths is new (Q-f)
currency. Adding (5p_M) to this inequality would be unjustified.

The exact remaining bridge for these returns is to spend their face labels
and distinct loaded ends in a source-preserving finite replacement, or prove
that their associated exceptional-terminal train family has only (o(D^2))
incident strict rhombi. Only the latter would earn a second-depletion term.
No full-core branch or macroscopic-container branch is closed by GQ.1--GQ.2.

## 8. Hostile audit obligations and scope

* **Isolates:** all graph operations are analyses of (V). Every source isolate
  stays in (P); no packing or deformation is constructed.
* **Bridges/repeated walks:** (3.5) uses oriented occurrences and allows two
  copies of a physical bridge. Using (e_S) would fail on a two-vertex tree.
* **Virtual triangles:** (3.7) counts bounded side occurrences; an auxiliary
  chord may border two triangles. Auxiliary edges never enter the path network.
* **Minimum separator:** exposure and the refined component-count bound use
  inclusion minimality. The scalar (Q_{\mathcal F}\le2|S|-4) holds for every
  separator by comparison with the minimum size; the refined component
  correction is not claimed for arbitrary unnecessary punctures.
* **KKT signs:** (3.3) uses the positive *contact* equilibrium on unloaded
  vertices, and no positive force activation from contact creation.
* **Source class:** this is not a theorem for arbitrary dense packings. Pinned
  rank is load-bearing, supplied by canonical mixed rigidity.
* **Endpoint identity:** all return ends are actual members of (B); no
  near-unit pair is converted to a near-diameter pair.
* **Independent currency:** face labels and quotas are independent; route
  lengths have not been made independent.

No literature theorem is imported. The integral network argument is proved
above rather than invoked with an unchecked endpoint convention.

## 9. Exact finite checks

The [standard-library verifier](../../../research/verify_target_c_global_face_return_quotas_2026_10_04.py)
passes 153,600 integer cancellation ledgers, ten rational pinned-framework
face-family/separator packets, fourteen simultaneous face demands, and
three packets in which every auxiliary chord borders two bounded triangles.
It also checks the physical-bridge counterexample to the false one-occurrence
discount. The rational frameworks have exact positive equilibrium and full
pinned bar rank; their bars have arbitrary lengths, so they are not claimed
to be unit-separated sources or globally optimal configurations. No
computation is a premise of the universal theorem above.

**Promotion status:** minimum-separator exposure, virtual-triangle cancellation, endpoint-inclusive flow, and simultaneous quotas were independently audited and promoted in `2026-10-05.audit.53`.
