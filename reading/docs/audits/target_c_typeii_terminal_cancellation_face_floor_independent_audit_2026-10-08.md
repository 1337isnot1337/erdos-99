> Generated reading edition · [exact source](../../../docs/audits/target_c_typeii_terminal_cancellation_face_floor_independent_audit_2026-10-08.md) · source SHA-256 `2abaff04ce431afe7c2857f4a843f1525bafb2a61c4dc38978e2af6629715682`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-AF6484C9929B","canonical":true,"claim_ids":["C-TYPEII-ATOMIC-SEPARATE-FACE-FLOOR"],"claim_statuses":{"C-TYPEII-ATOMIC-SEPARATE-FACE-FLOOR":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C Audit.174 — terminal cancellation face floor

Date: 2026-10-08  
Audit base: `origin/main=f62282f4f7909c8036038c1a9422d80268a7ed67`, state `2026-10-08.audit.169`  
Frozen source: `origin/research/level-i-closure-20261007` at `12f6833725f281ce39a6d04ebcb45630b3a6768f`  
Classification: independently reconstructed; **PASS — promote the strongest exact face-floor statement**.

Frozen source hashes:

- Candidate report, introduced at `55efb7a23c7ed114b5de25bc2627a5120da3b5ce`: `44504166b3f11e978f972cfbd5bbf237247a92eac1f5d1299406045719dd6b19`.
- Separate-face refinement, introduced at `ba6edaa8f5791bd02c9459e83ed7993f884f1ec2`.
- Exact finite checker: `ec287768485076f01b49ea361e7ae08e71206cc1f46a04658c123db883b5cb9e`.
- Imported finite helper: `50160bb3c3d68185a401a6fbeed3d39f5b80aa16d74af43efafd814714300e88`.

The source tip and all three hashes were rechecked after the proof audit. The discovery branch was not modified.

## Exact theorem promoted

Take any unbounded canonical contact-minimal, then diameter-pair-minimal, triangle-free global-source sequence in the full-core Type-II near-disk branch, with diameter (D\to\infty). Retain every source point, including all contact isolates. Use the canonical loaded hull and actual positive-contact rhombus trains. Let (f) be the number of bounded nonquadrilateral contact faces, (Q=\sum_F(\deg F-4)) their total excess, (q) the number of loaded hull vertices, (k=d_H+s_Z\ge0), (p) the loaded-hull perimeter, and (z=b-p\ge0) the excess of the occurrence-counted outer contact walk over the perimeter. Put

```math
s_2=\sqrt{\frac{\pi}{2\sqrt3}}.
```

Then

```math
\boxed{\liminf\frac{f-k}{D}\ge\frac{6s_2}{5}},\qquad
\boxed{\liminf\frac{2(q-k)-k-z}{D}\ge\pi+\frac{6s_2}{5}}.
```

In particular,

```math
\boxed{\liminf\frac{q-k}{D}\ge\frac\pi2+\frac{3s_2}{5}
      =2.1421840109\ldots>\frac{2\pi}{3}}.
```

Thus the positive one-cell collar range (4\pi-6(q-k)/D>0) is empty in this Type-II branch. The bound is a new scoped asymptotic exclusion; it gives no face-width or area lower bound, source move, C-II closure, or Level I result.

## Canonical inputs

- `C-FULLCORE-NEAR-DISK` supplies the circular full-core regime and (p/D\to\pi). Its macroscopic-container alternative is not included in this theorem's scope.
- `C-LOADED-HULL` supplies (b+Q=2(q-k)), (b=p+z), (q\le p), and the cyclic loaded-chain decomposition with every chain chord of length at least one.
- `C-RHOMBUS-POP` and `C-PUNCTURED-PHASE` give disjoint actual strict rhombi and (E_4=o(D^2)) in the near-disk Type-II regime.
- `C-ATOMIC-TRACK-BOUNDARY-COST` gives atomic mass at least (A=2s_2) in every fixed joint weak limit of normalized actual rhombus-track direction measures.
- `C-ATOMIC-ONE-END-TRAIN-BOUNDARY` gives the exact complete-train count (T_D=q-k+2f), including singleton contact edges, and the two-end boundary handshake.
- Theory 01, Theorem 10.6 supplies actual track simplicity, at most one crossing per pair, opposite terminal vectors, and the terminal-midpoint displacement bound by the number of crossed rhombi.

No source/scaffold identification, positive stress-weight lower bound, prescribed route endpoint, or deletion of contact isolates is used.

## Independent reconstruction

### 1. Atomic direction selection controls the omitted train mass

For each sequence member, place mass (1/D) at the projective direction of every complete physical train: each strict-rhombus track and each unit contact edge incident to no rhombus as a singleton. The number of trains is (O(D)), since (q\le p=O(D)), (b+Q=2(q-k)\le2q), (f\le Q), and (T_D=q-k+2f). Pass jointly to weak limits of this train measure and the actual-track measure. The latter is dominated by the former, so the full train limit has atomic mass (a\ge A).

The ordered physical crossing measure, with mass (D^{-2}) on each orientation of each crossing, is dominated in the limit by the product of the train measure with itself: the physical crossing graph is simple, and singleton trains have no crossings. Disjointness of rhombus interiors and the near-disk population equality give (E_4=o(D^2)). On the allowed rhombus-angle interval, the sine area excess controls the angular deviation from (\pi/3); hence the limiting crossing measure is supported on the projective (60^\circ) relation. A product measure charges that relation only on pairs of atoms.

Choose finite neighborhoods exhausting the atoms and shrink them with null boundary so that their excess limiting mass tends to zero. A diagonal choice gives selected complete trains $`\mathcal A_D`$ with

```math
\frac{|\mathcal A_D|}{D}\to a,\qquad
\sum_{\tau\notin\mathcal A_D}d_\tau=o(D^2),
```

where (d_\tau) is the number of actual rhombi crossed by train $`\tau`$. This is a compactness/diagonal argument and assumes no convergence rate. Markov's inequality then leaves only (o(D)) complementary trains with terminal-midpoint separation larger than $`\epsilon_DD`$ for some $`\epsilon_D\to0`$; singleton trains have coincident midpoints.

### 2. Separate-face recipient graph and boundary cancellation

Make one recipient vertex for each actual outer chain (W_i) between consecutive loaded hull vertices and one separate recipient for each bounded nonquadrilateral face. Each complementary train gives an edge between its two actual terminal recipients. Keep loops and parallel edges. This graph records facial occurrences only; its edges are not source paths or proposed motions.

Let (c_\partial) be the number of components meeting an outer-chain recipient, and let (f_\partial) count the exceptional faces in those components. For fixed recipient cutoff (M) and boundary-walk cutoff (L), components with too many recipients number at most ((q+f)/(M+1)); components containing a recipient with more than (L) edge occurrences number at most ((b+4f+Q)/(L+1)); components containing a long complementary train number (o(D)). Both numerators are (O(D)).

In each remaining boundary component, short train edges and bounded recipient walks put all its outer-chain bases and face boundary occurrences within (o(D)) of one another. Its outer hull chords have length at least one and share a limiting tangent direction. Every bounded facial boundary sums to zero, and the two terminal vectors of every complementary train edge in the component cancel. Therefore

```math
\sum_{W_i\text{ in }C}(b_{i+1}-b_i)
=\sum_{\text{selected atomic terminal occurrences in }C}e.
\tag{1}
```

The left side is nonzero and has the common limiting hull-tangent direction.

### 3. Atomless hull normals force few boundary components

For fixed (M,L), mark each retained boundary component by one chosen hull-side normal and the ordered list of its selected atomic terminal vectors. There are at most (ML) vectors in each list. Normalize the record measures by (1/D) and pass to subsequential limits for every list length.

Each vector-coordinate marginal is dominated by the selected train terminal-vector measure. Its limit is supported on the countable signed directions of the atoms of the train measure. The chosen-normal marginal is dominated by the perimeter-weighted loaded-hull side-direction measure: distinct components choose distinct hull sides, and every side has length at least one. Since the scaled loaded hull converges to a disk, that limiting side measure is atomless.

Equation (1) determines each chosen normal as a right rotation of the normalized sum of its finite vector list. There are only countably many possible lists of limiting atomic vectors, so the normal marginal is countably supported. It is also atomless, hence zero. Thus, for each fixed (M,L), the retained boundary components number (o(D)). The discarded-component bounds imply

```math
\limsup\frac{c_\partial}{D}
\le \frac{\limsup(q+f)/D}{M+1}
 +\frac{\limsup(b+4f+Q)/D}{L+1}.
```

Letting (M,L\to\infty) gives (c_\partial=o(D)). This argument bounds only components meeting the outer boundary; interior-only face components are not discarded.

### 4. Exact incidence algebra yields the stronger floor

Let (N_\partial) be the number of complementary-train edges in boundary components, (N_\circ) their number in interior-only components, and (Q_\circ) the face excess in interior-only components. The component edge bound and exact terminal-occurrence handshake give

```math
N_\partial\ge q+f_\partial-c_\partial,
\qquad
a_\partial=b+4f_\partial+Q-Q_\circ-2N_\partial,
```

where (a_\partial\ge0) counts selected atomic terminal occurrences on boundary components. Using (b+Q=2(q-k)),

```math
0\le a_\partial\le 2f_\partial-Q_\circ-2k+2c_\partial.
```

Every interior-only exceptional face contributes at least one to (Q_\circ), so (Q_\circ\ge f-f_\partial). Hence

```math
3f_\partial\ge f+2k-2c_\partial.\tag{2}
```

The interior-only atomic terminal count is exactly (4(f-f_\partial)+Q_\circ-2N_\circ). Adding both atomic-end populations and dividing by two gives

```math
|\mathcal A_D|+N_\circ\le 2f-f_\partial-k+c_\partial.
```

Combining with (2),

```math
3(|\mathcal A_D|+N_\circ)\le5(f-k+c_\partial).
```

Divide by (D), use (|\mathcal A_D|/D\to a\ge2s_2), (N_\circ\ge0), and (c_\partial=o(D)). This proves (liminf(f-k)/D\ge6s_2/5) along every subsequential limit, hence for the full sequence.

Finally, (Q-k=2(q-k)-k-p-z\ge f-k). Since (p/D\to\pi), this gives the second boxed bound. Nonnegativity of (k,z) yields the (q-k) floor. The strict collar exclusion is exact: (3s_2/5>\pi/6) is equivalent to (162>25\pi\sqrt3), which follows from (\pi<22/7), (\sqrt3<7/4), and (137.5<162).

## Adversarial review and checker scope

- The auxiliary graph uses actual facial terminal occurrences, including repeated outer bridge occurrences and each separate exceptional face. Its components do not become physical contact paths.
- The proof does not discard interior-only components; it retains their train edges and face excess in the exact incidence count.
- The hull-normal argument uses distinct side choices and the atomless tangent-direction measure of the actual near-disk loaded hull. It does not infer a finite-position lattice cover.
- The theorem gives linearly many exceptional faces only in count. It does not give positive width, area, vacancy capacity, or a finite source move.
- Contact isolates remain in the source and all global canonical hypotheses.
- The frozen exact checker was inspected and rerun. It uses `Fraction` arithmetic and passes 7,252 source lower-pair checks, 108 terminal-pair checks, 620 component identities, and 886 separate-face cancellation checks across eight nonglobal fixtures. It checks finite facial identities and inequalities only; it does not certify Type-II limits, atom selection, the marked-measure argument, global optimality, or Level I.

## Verdict and frontier effect

**PASS — promote `C-TYPEII-ATOMIC-SEPARATE-FACE-FLOOR`.** This strongest face-by-face theorem subsumes the report's weaker (2f-k) floor and its lower metric consequences. It removes the positive one-cell collar range from the full-core Type-II near-disk branch. Higher-((q-k)/D) Type-II sequences and the macroscopic-container alternative remain open. The current finite-move obligation is narrowed to the surviving high-((q-k)/D) Type-II train/face system plus the separate macroscopic-container branch. No discovery-worker branch was changed.
