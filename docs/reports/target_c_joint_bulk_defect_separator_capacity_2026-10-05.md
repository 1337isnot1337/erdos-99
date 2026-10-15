<!-- theorem-state: {"artifact_id":"ART-BB90A4B2C5DE","canonical":true,"claim_ids":["C-JOINT-BULK-FACE-SEPARATOR"],"claim_statuses":{"C-JOINT-BULK-FACE-SEPARATOR":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C — joint bulk/face separator capacity and spatial tail exclusion

Date: 2026-10-05.
Run base: `f539af073a691c13327a0a7fef3c746fb7704e5f`; first checkpoint
`b2f82ebfbb3980f0ed037da7114f9e7e7df3fb49`.
State: `2026-09-14.audit.51`.
Classification: canonical in `2026-10-05.audit.53` as `C-JOINT-BULK-FACE-SEPARATOR` after independent promotion audit.
LEVEL I STATUS: STILL OPEN. C-II REMAINS OPEN.

## 1. New implication and source class

This continues the [global face-quota theorem](target_c_global_exceptional_face_return_quotas_2026-10-04.md).
The two new consequences are:

```text
pinned positive equilibrium + unit outer perimeter
  -> a joint rhombus-area/exceptional-face charge behind one separator
  -> simultaneous face and bulk demands paid by one loaded endpoint bank;

global face quota + unit packing across a circular cut
  -> exceptional-face defect is at most a constant times cluster radius
  -> a linear high-degree tail cannot be confined to submacroscopic clusters.
```

Use the same canonical core (V), physical contact graph (C), loaded set
(B), and source hypotheses as the preceding report. All source points,
including isolates, stay in the full source. Graph punctures are analyses,
never source deletions. Put (a_0=\sqrt3/2).

## 2. Joint finite capacity for physical faces and rhombi

Select a family \(\mathcal F\) of bounded **physical contact faces** of degrees
at least five, and a family \(\mathcal R\) of (R) strict-rhombus faces all
of whose vertices are unloaded. Let (Q_{\mathcal F}=\sum(m_f-4)), and let
(X) be the union of their boundary vertices. Empty \(\mathcal F\) or
\(\mathcal R\) is allowed, but (X\ne\varnothing).

Let (S\subset V) be any physical-contact separator from (X) to (B),
with endpoint removal allowed. Put (k=|S|), (k_I=|S\setminus B|).
Let (U) be the union of the components of (C-S) meeting (X\setminus S),
let (c_U) count them, and form the **physical** induced graph
(K=C[U\cup S]). Let (c_K) count its components and (e_S) its contacts
with both ends in (S).

**Theorem JB.1.** For every such separator,

\[
 \boxed{
 2\sqrt{\pi a_0(R-5k_I)_+}+Q_{\mathcal F}
 \le4k-2c_U-4c_K-2e_S\le4k-4.
 }
 \tag{2.1}
\]

If (R>5k_I), the final upper bound improves to (4k-6).
The theorem does not allow nonunit auxiliary edges in (K): their metric
length would invalidate the perimeter step.

### Proof

The pinned-rank and positive-row-dependence argument from GQ.1 gives
(e_U+t_U\ge2|U|+c_U). Since every edge of (K) is a physical unit contact,
Euler and occurrence counting give

\[
 b_K+Q(K)=4|V(K)|-2e(K)-4c_K
 \le4k-2c_U-4c_K-2e_S, \tag{2.2}
\]

where (b_K) sums the unit lengths of the component outer walks and
(Q(K)\ge0) is their total bounded-face defect. Every selected physical face
cycle is retained, so (Q(K)\ge Q_{\mathcal F}).

A source vertex has contact degree at most five, hence is incident with at
most five strict-rhombus faces. Remove from the selected family only rhombi
incident with (S); at most (5k_I) are lost. Every remaining selected
rhombus has all four vertices in one component of (U), hence lies in one
component hull of (K). Write (R_0\ge(R-5k_I)_+) for their number.

If the component outer lengths are (b_j), its convex hull has perimeter at
most (b_j). Isoperimetry and disjoint rhombus interiors imply

\[
 a_0R_0\le\sum_j\operatorname{area}(\operatorname{conv}V(K_j))
 \le\frac1{4\pi}\sum_jb_j^2
 \le\frac{b_K^2}{4\pi}. \tag{2.3}
\]

Nested component hulls are harmless: this is an upper bound by a sum, not
an injectivity claim about hull interiors. Rhombus area is counted once.
Thus (b_K\ge2\sqrt{\pi a_0(R-5k_I)_+}). Substitute into (2.2).
The nonempty starting set gives (c_K\ge1). If (R>5k_I), a retained
rhombus gives (c_U\ge1). This proves (2.1). □

The pure-bulk corollary is

\[
 \boxed{R\le5k_I+\frac{(4k-6)_+^2}{2\pi\sqrt3}.} \tag{2.4}
\]

If no selected rhombus remains, the deletion term suffices; otherwise use
the strengthened right side of (2.1). This is valid for arbitrary separators.
It uses metric perimeter instead of graph diameter in draft #671's
isodiametric capacity argument.

## 3. Asymptotic joint endpoint budget

Let an unbounded Type-II sequence have an unloaded rhombus family

\[
 R_D=(\Delta_2-o(1))D^2,
 \qquad\Delta_2=\pi/(2\sqrt3).
\]

For any selected physical exceptional faces, a minimum separator has
(k\le q\le\pi D), since deleting all loaded endpoints separates the starts.
The loss (5k_I=O(D)) is negligible in the square root in (2.1). Consequently
the maximum simultaneous full-boundary return count satisfies

\[
 \boxed{
 p_D\ge\frac\pi4D+\frac14Q_{\mathcal F_D}-o(D).
 } \tag{3.1}
\]

Here the paths start in the **union** of the bulk and selected face boundaries.
One cannot count them twice as independently chosen path families.

There is a stronger assignment statement. For each selected face put

\[
 r_f=\max\{0,\lfloor(m_f-4)/4\rfloor-\ell_f\}.
\]

For every fixed \(\varepsilon>0\), and all sufficiently large sources, one
may simultaneously realize every face demand (r_f) and at least
(\lfloor(\pi/4-\varepsilon)D\rfloor) additional paths from the unloaded
rhombus vertex set to distinct loaded endpoints, with **all paths mutually
vertex-disjoint**.

### Proof of the assignment statement

Use the face-node flow construction of GQ.2 and one additional source group
for the bulk. For a group subfamily not containing bulk, GQ.1 gives rank at
least (Q/2+2-|\bigcup_f(V(\partial f)\cap B)|\ge\sum r_f) after restricting
to positive-demand faces.
For a group subfamily containing bulk, adding its loaded boundary vertices
to an unloaded-start separator and applying (2.1) gives rank at least

\[
 (\pi/4-o(1))D+Q/4-
 \left|\bigcup_f(V(\partial f)\cap B)\right|\ge
 \lfloor(\pi/4-\varepsilon)D\rfloor+\sum r_f.
\]

The union of loaded boundary vertices has size at most \(\sum_f\ell_f\),
which is already debited in each positive face demand. The (o(D)) error
is uniform over face subfamilies: its only losses are (5q=O(D)) and the
fixed rhombus asymptotic. No small-loaded-incidence hypothesis is required.
The same integral min-cut proof therefore saturates all source-group demands.
Auxiliary chords never enter the network. □

This is a joint assignment result. It still does not turn path length into
new exceptional-face or train currency.

## 4. Spatial exclusion for a selected face cluster

Now permit the plane loaded-to-loaded augmentation of GQ.1. Suppose every
boundary vertex of a selected face family lies in \(\overline B(x,r)).
No restriction is imposed on isolates inside that disk.

**Theorem SC.1.** Uniformly over every finite canonical source and such family,

\[
 \boxed{Q_{\mathcal F}\le(32+4\pi)r+18.} \tag{4.1}
\]

### Proof

Take as a physical separator all source-core vertices in the annulus
(r<|p-x|\le r+1), together with the loaded vertices in the closed radius-
(r) disk. Every actual contact edge has length one. A path starting inside
the disk and ending outside radius (r+1) therefore meets the annulus;
loaded ends inside radius (r) are removed explicitly. This is an actual
contact separator, including the endpoint convention.

Disjoint open radius-(1/2) disks about the annulus vertices lie in the
annulus with radii \((r-1/2)_+\) and (r+3/2). Thus their number is at most

\[
 4[(r+3/2)^2-(r-1/2)_+^2]\le16r+9. \tag{4.2}
\]

Every loaded subset is in convex position and is unit-separated. If at least
three loaded points lie in a radius-(r) disk, their convex hull has perimeter
at most (2\pi r), whereas its consecutive side lengths sum to at least their
number. Including the one/two-point cases, the loaded count is at most
(2\pi r+2).

Hence the displayed separator has size at most ((16+2\pi)r+11). Its size
is at least the minimum separator size. Applying the scalar consequence
(Q_{\mathcal F}\le2k_{\min}-4) of GQ.1 proves (4.1). □

## 5. Exact eliminated localization regimes

For every canonical source sequence with (D\to\infty), if selected face
boundaries all lie in one disk of radius (r_D=o(D)), then

\[
 Q_{\mathcal F_D}=o(D). \tag{5.1}
\]

More generally, assign each selected face to one of (N_D) disks containing
its entire boundary, and denote their radii by (r_{D,j}). Summing (4.1) for
the disjointly assigned subfamilies gives

\[
 Q_{\mathcal F_D}
 \le(32+4\pi)\sum_jr_{D,j}+18N_D. \tag{5.2}
\]

Therefore a persistent (\Omega(D)) face-defect tail cannot be supported by
(N_D=o(D)) clusters with \(\sum_jr_{D,j}=o(D)). This excludes both a single
submacroscopic concentration and any such sublinear cluster cover, including
families made entirely of mesoscopic faces. It does not exclude tails spread
across a macroscopic amount of the source.

This is an actual source exclusion using global-optimality consequences
(mixed rigidity and positive equilibrium). Convexity or small total hole area
alone would not give it.

## 6. Exact remaining bridge

The post-#699 weighted inequality still requires either a strict source
replacement or additional second depletion. SC.1 forces a persistent tail
to have macroscopic spatial spread; GQ.2 prevents global endpoint reuse;
JB.1 pays joint bulk/face demands with one separator and one endpoint bank.
None proves that the corresponding stopped trains have (o(D^2)) incident
rhombi. Adding a return-count bonus to the weighted inequality remains invalid.

No full-core branch is closed. The spatially concentrated tail regimes in
Section 5 are excluded. Macroscopic-container collective repacking remains
separate. The registered separator/spatial-exclusion claim is canonical in audit.53.

## 7. Audit and computation scope

The analytic argument checks every physical cut edge, loaded endpoint inside
the geometric cut, and outer walk occurrence. It counts at most five lost
rhombi per unloaded separator vertex and counts no loss at a loaded vertex
for an unloaded-only rhombus family. It does not apply a nonunit virtual-edge
count as metric perimeter.

The global face-quota certificate verifies its finite algebra and flow
ingredients. The [joint-capacity certificate](../../research/verify_target_c_joint_bulk_separator_2026_10_05.py)
passes twelve exact pinned-unit-grid separator packets (largest selected bulk:
729 rhombi), 1,001 rational annular bounds, and interval perimeter-capacity
checks using rational enclosures of pi and sqrt(3). Boundary pins are not all
actual diameter endpoints; these are finite proof-ingredient checks, not
canonical-source examples. No computation is a premise of the analytic
perimeter/isoperimetric or disk-packing arguments. No external literature
result is imported beyond elementary planar isoperimetry and the convex
perimeter bound.

Promotion status: the joint group assignment, metric separator argument, and spatial endpoint handling were independently audited and promoted in `2026-10-05.audit.53`.
