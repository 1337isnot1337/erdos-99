<!-- theorem-state: {"artifact_id":"ART-C0B8427ADD8C","canonical":true,"claim_ids":["C-LOADED-HULL-CAP-BUDGET","C-LOADED-NEAR-UNIT-ADJACENCY"],"claim_statuses":{"C-LOADED-HULL-CAP-BUDGET":"canonical","C-LOADED-NEAR-UNIT-ADJACENCY":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent promotion audit — loaded near-unit adjacency and loaded-hull cap budget

**Date:** 2026-10-05  
**Audit base:** \`0351c2c3aecd34c0427d0ad081afae563468d401\`  
**Starting theorem state:** \`2026-10-05.audit.61\`  
**Target:** C-II / outer-face near-unit blocker geometry  
**Verdict:** **PASS for the two exact claims below.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This audit promotes:

1. \`C-LOADED-NEAR-UNIT-ADJACENCY\`;
2. \`C-LOADED-HULL-CAP-BUDGET\`.

These are finite source-geometry theorems. Their canonical asymptotic consequences are stated separately and use only already-canonical audit.61 inputs.

## 1. Loaded near-unit pairs lie on the loaded hull cycle

Audited source:
\`docs/reports/target_c_loaded_near_unit_hull_adjacency_2026-10-01.md\`.

Let \(A\) be any finite unit-separated planar source of diameter \(D\). Let \(B\) be the set of all endpoints of actual diameter pairs and assume \(\operatorname{conv}B\) has positive area.

Define
\[
\tau_D
=
\frac{3D}{\sqrt{3D^2+4}+1}.
\]

The promoted theorem is:

\[
\boxed{
a,b\in B,\ a,b\text{ nonconsecutive on }\partial\operatorname{conv}B,\ |ab|<D
\Longrightarrow
|ab|\ge\tau_D.
}
\]

In particular, for \(D\ge6\),
\[
\tau_D>\frac32>\frac{13}{12},
\]
so every loaded pair of length at most \(13/12\) is a side of the loaded hull. Therefore the graph on \(B\) with edge set
\[
\{ab:\ |ab|\le13/12\}
\]
is a subgraph of the hull cycle and has maximum degree at most two.

### 1.1 Cap threshold

Suppose \(a,b\) have distance \(\ell<D\), diameter partners \(c,d\) lie on one side of line \(ab\), and a source point \(z\) lies strictly on the other side.

Writing the two diameter vectors by their angles \(\alpha,\beta\) from the perpendicular to \(ab\), with \(\theta=\alpha+\beta\), the diameter constraints give
\[
2D\sin(\theta/2)\le D+\ell.
\]

The point \(z\) lies in the wedge cut out by the two diameter disks. Since \(|za|,|zb|\ge1\), the angle at \(z\) gives
\[
\ell^2\ge4\cos^2(\theta/2).
\]

Combining,
\[
\ell^2\ge4-\left(1+\frac{\ell}{D}\right)^2,
\]
equivalently
\[
(1+D^{-2})\ell^2+\frac{2\ell}{D}\ge3.
\]
Solving the positive quadratic root gives \(\ell\ge\tau_D\).

No KKT or source optimality is used here.

### 1.2 Why nonconsecutive loaded endpoints satisfy the cap hypothesis

Take nonconsecutive \(a,b\in B\). Diameter edges in a planar point set form a geometric thrackle: any two distinct actual diameter edges meet.

If a diameter partner of \(a\) and a diameter partner of \(b\) lay on opposite open hull arcs between \(a,b\), the two corresponding diameter chords would be disjoint, contradicting the thrackle property. Hence all partners of \(a,b\) lie on one hull arc.

Because \(a,b\) are nonconsecutive, the opposite arc contains another loaded hull vertex \(z\). Convexity places \(z\) on the opposite side of line \(ab\) from all selected partners, so the cap threshold applies.

This proof works uniformly for stars, matchings, and odd-unicyclic diameter graphs. No Euler-trail assumption is used.

### 1.3 Sharpness boundary

The source report gives an explicit five-point family whose nonadjacent loaded-pair distance approaches \(\sqrt3\) from below while all diameter identities and unit-separation inequalities hold. Thus the asymptotic nonadjacent threshold cannot be raised universally above \(\sqrt3\).

That family is not a canonical minimizer and is used only as a sharpness regression.

### 1.4 Certificate

The exact certificate
\`research/verify_loaded_near_unit_hull_adjacency_2026_10_01.py\`
was rerun during this audit and passed:

- 1,607 rational/quadratic-field loaded-hull packets;
- 624 loaded pairs at distance at most \(13/12\), all hull-adjacent;
- 44,166 nonadjacent loaded pairs satisfying the exact cap polynomial;
- seven sharpness packets approaching \(\sqrt3\) from below.

**Verdict:** canonical-ready.

## 2. Loaded-hull cap and attachment budget

Audited source:
\`docs/reports/target_c_loaded_hull_cap_attachment_budget_2026-10-01.md\`.

Let \(A\) be a finite unit-separated planar set of diameter \(D\), let
\[
K=\operatorname{conv}A,
\]
and let \(B\) be a cyclic subset of vertices of \(K\), with \(q=|B|\ge3\), such that
\[
F=\operatorname{conv}B
\]
has positive area and the positive-contact core lies in \(F\).

Put
\[
W=\operatorname{per}K-q.
\]

For every side \(ab\) of \(F\), let \(Q_{ab}\) be the cap of \(K\) outside \(F\), \(L_{ab}\) the corresponding \(K\)-boundary arc length, and \(\ell_{ab}=|ab|\).

The promoted finite theorem is:

\[
\boxed{
\#\{\text{occupied caps}\}\le W,
\qquad
\sum_{\rm occupied}L_{ab}\le2W,
\qquad
\sum_{\rm occupied}\ell_{ab}\le2W.
}
\]

Let \(P\) be the set of core points \(p\in F\) for which some source point \(z\notin F\) satisfies \(|p-z|<\sqrt2\). Then
\[
\boxed{|P|\le68W.}
\]

Let \(X\) be the nonloaded source points in \(F\) whose distance to \(\partial F\) is at most \(1/2\). Then
\[
\boxed{|X|\le12W.}
\]

Every source point \(p\in F\) at boundary distance at least \(1/2\) has
\[
\boxed{|p-y|\le D-\frac12\qquad\text{for every }y\in K.}
\]

Finally, the number of extreme source vertices of \(K\) outside \(B\) is at most
\[
\boxed{W.}
\]

### 2.1 Exact cap ledger

The consecutive \(B\)-chords partition \(K\) into \(F\) and the cap regions. Since
\[
W=\sum_{ab}(L_{ab}-1),
\]
and every occupied cap contains a source point unit-separated from both endpoints, convex perimeter monotonicity gives
\[
L_{ab}\ge2
\]
for every occupied cap.

Thus each occupied cap spends at least one unit of \(W\), and
\[
L_{ab}\le2(L_{ab}-1).
\]
Summing gives the three cap bounds.

### 2.2 Short core-to-exterior attachments

For an exterior source point \(z\) in cap \(Q_{ab}\), its nearest point in \(F\) lies on the base segment \(ab\).

If \(p\in P\), then
\[
\operatorname{dist}(p,ab)<2\sqrt2.
\]
The radius-\(1/2\) disks around points of \(P\) are interior-disjoint and lie in radius-\(7/2\) tubes about occupied base segments.

The total tube area is at most
\[
\sum_{\rm occupied}\left(7\ell_{ab}+\frac{49\pi}{4}\right).
\]
Using the cap ledger,
\[
|P|\frac{\pi}{4}
\le
\left(14+\frac{49\pi}{4}\right)W.
\]
Since \(\pi>3\),
\[
\frac{56}{\pi}+49<68,
\]
hence \(|P|\le68W\).

### 2.3 Shallow loaded-hull boundary layer

If a nonloaded source point \(x\in F\) lies within \(1/2\) of \(\partial F\), its closest boundary point lies in the relative interior of a side \(ab\). Unit separation from both endpoints forces
\[
|ab|\ge\sqrt3.
\]

Writing
\[
U=\operatorname{per}F-q\le W,
\]
the number and total length of such long sides are controlled by \(U/(\sqrt3-1)\). Radius-\(1/2\) disks around shallow points lie in radius-one tubes around those long sides, yielding
\[
|X|
\le
\frac{4(2\sqrt3+\pi)}{\pi(\sqrt3-1)}U
<12W.
\]

### 2.4 Deep interior upper margin

If \(p\in F\) has distance at least \(1/2\) from \(\partial F\), the radius-\(1/2\) disk about \(p\) lies in \(F\subset K\).

For any \(y\in K\), move from \(p\) exactly \(1/2\) directly away from \(y\) to \(p'\in K\). Since \(\operatorname{diam}K=D\),
\[
|p-y|+\frac12=|p'-y|\le D.
\]
Thus
\[
|p-y|\le D-\frac12.
\]

This is an exact inactive-upper margin, not merely asymptotic slack.

### 2.5 Canonical C-II applicability

In the canonical post-ZF source, every actual diameter endpoint is a source-hull extreme point. Every nonloaded nonisolated core vertex is a positive weighted barycenter of its contact neighbors, so the connected positive-contact core lies in the loaded hull
\[
F=\operatorname{conv}B.
\]

Therefore the finite theorem applies with \(B\) equal to the full loaded endpoint set.

Canonical full-source geometry gives
\[
\operatorname{per}K<\pi D.
\]
Hence
\[
0\le W=\operatorname{per}K-q<\pi D-q.
\]

Consequently, on every canonical subsequence with
\[
\frac qD\to\pi,
\]
one has
\[
W=o(D).
\]

The finite theorem then gives the canonical asymptotic consequences
\[
\boxed{|P|=o(D),\qquad |X|=o(D),\qquad
\#(\operatorname{ext}K\setminus B)=o(D).}
\]

Thus in the terminal \(q/D\to\pi\) regime, hull-cap geometry contributes only a sublinear number of:

- exterior extreme contact isolates;
- core vertices with source points outside the loaded hull within distance \(<\sqrt2\);
- nonloaded shallow loaded-hull boundary-layer points.

Deep core points enjoy the exact \(D-1/2\) upper margin.

No claim is made that the population inside one cap is \(O(W)\), nor that the entire outer contact face lies outside \(F\).

### 2.6 Certificate

The new exact ledger certificate
\`research/verify_target_c_loaded_hull_cap_budget_2026_10_05.py\`
passed:

- 254 occupied-cap charging ledgers;
- the three constant inequalities used above;
- 720 extreme-vertex perimeter ledgers.

It checks arithmetic and charging only; the convex geometry is proved analytically above.

**Verdict:** canonical-ready.

## 3. Effect on the audit.61 outer-face blocker frontier

Audit.61 reduces a small O–O finite motion to:

\[
\text{outer-face near-unit owner/implication structure}
+\text{unary rhombus blockers}
+\text{at most }d_H\text{ upper exceptions}.
\]

Audit.62 adds two exact restrictions on that remaining lower-blocker geometry.

First, any near-unit clause whose two endpoints are loaded and whose old length is at most \(13/12\) lies on the loaded hull cycle. Therefore loaded-loaded near-unit blocker degree is at most two per loaded vertex, with the cyclic hull order explicit.

Second, along any terminal subsequence \(q/D\to\pi\), cap/exterior geometry is sublinear:
\[
|P|+|X|+\#(\operatorname{ext}K\setminus B)=o(D).
\]

Thus a linear obstruction family cannot be supported predominantly by:

- loaded-hull caps;
- exterior extreme isolates;
- short core-to-exterior attachments through those caps;
- shallow nonloaded loaded-hull boundary-layer sites.

The remaining possible linear obstruction must therefore concentrate on actual outer-contact-face geometry inside the loaded hull, on loaded hull-cycle vertices, or on the already-explicit unary-rhombus / inactive-upper exceptions.

This still does not prove owner-level acyclicity or satisfiability. It sharpens the object on which the next outer-order theorem must act.

**Promotion recommendation:** advance theorem state to \`2026-10-05.audit.62\` and register both claims as canonical.
