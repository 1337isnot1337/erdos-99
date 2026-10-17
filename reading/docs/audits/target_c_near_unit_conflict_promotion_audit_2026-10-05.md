> Generated reading edition · [exact source](../../../docs/audits/target_c_near_unit_conflict_promotion_audit_2026-10-05.md) · source SHA-256 `5ff83bf2948e2d705ea4e6b6c73ab7d0327ee6d29cd75731ea8efc5860c40560`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-1D4A6FA9E1B6","canonical":true,"claim_ids":["C-NEAR-UNIT-CONFLICT-GEOMETRY","C-OO-LOWER-BLOCKER-LOCALIZATION","C-OWNER-CONTRACTION-CYCLE-REGRESSION","C-UNARY-RHOMBUS-BLOCKER-REGRESSION"],"claim_statuses":{"C-NEAR-UNIT-CONFLICT-GEOMETRY":"canonical","C-OO-LOWER-BLOCKER-LOCALIZATION":"canonical","C-OWNER-CONTRACTION-CYCLE-REGRESSION":"regression","C-UNARY-RHOMBUS-BLOCKER-REGRESSION":"regression"},"index":"docs/state/artifact-index.jsonl","status":"mixed","target":"target-c"} -->
# Independent promotion audit — Target C near-unit conflict geometry and O–O blocker localization

**Date:** 2026-10-05  
**Audit base:** \`f4cdcd21e5a3480ccaa61f25cba19d5decfbdf99\`  
**Starting theorem state:** \`2026-10-05.audit.60\`  
**Target:** C-II / lower-blocker geometry for finite source motions  
**Verdict:** **PASS for two canonical finite theorems and two binding regressions.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This audit promotes:

1. \`C-NEAR-UNIT-CONFLICT-GEOMETRY\`;
2. \`C-OO-LOWER-BLOCKER-LOCALIZATION\`;

and registers:

3. \`C-UNARY-RHOMBUS-BLOCKER-REGRESSION\`;
4. \`C-OWNER-CONTRACTION-CYCLE-REGRESSION\`.

The promotion is deliberately limited to finite source geometry and explicit O–O motion hypotheses. The historical joint-swap/TB1 asymptotic applications remain unreviewed unless separately promoted.

## 1. Near-unit source pairs form a planar graph below $\sqrt2$

Audited source:
\`docs/reports/target_c_near_unit_faces_and_pure_conflict_paths_2026-10-01.md\`.

Let $A$ be any finite unit-separated planar source. For
$$
1<t<\sqrt2,
$$
join every source pair of length at most $t$.

Then the resulting straight-line graph $N_t$ is plane:

- two edges with four distinct endpoints cannot cross;
- no source vertex lies in the interior of an edge;
- distinct collinear edges cannot overlap improperly.

### Proof audit

If two $N_t$-edges cross, their four endpoints form a strictly convex quadrilateral. Some interior angle is at least $\pi/2$. The two source sides incident with that angle have lengths at least one, so the opposite diagonal has squared length at least two. One crossing edge is that diagonal, contradicting $t<\sqrt2$.

A source vertex in an $N_t$-edge would split a segment of length $<2$ into two source distances each at least one. Collinear overlap reduces to the same contradiction or places two same-ray neighbors at mutual distance $<1$.

Therefore every old near-unit pair with length $<\sqrt2$ lies entirely in the closure of one face of the old contact graph.

### Unit-contact crossing threshold

There is also a sharp asymmetric fact useful for lower blockers.

If a source segment crosses a unit contact, its length is at least
$$
\boxed{\sqrt3}.
$$

Indeed, at each endpoint of the crossing segment the unit contact subtends angle at most $\pi/3$, since the other two source distances in that triangle are at least one. The remaining two quadrilateral angles therefore sum to at least $4\pi/3$, so one is at least $2\pi/3$. The opposite segment then has length at least $\sqrt3$.

In a unit-triangle-free source the inequality is strict: equality forces the adjacent source sides and the unit diagonal into the equality geometry producing a unit equilateral triangle.

Thus every blocker with old length below $\sqrt3$ is cofacial with the contact graph.

## 2. Contact-preserving small translation owners cannot interleave inside a strict rhombus

Let the source points be partitioned among disjoint moving owners and fixed points. Give owner $i$ translation $\Delta_i$. Assume:

- every old unit contact remains exactly unit under **every** binary selection of owners;
- every nonzero $\Delta_i$ has norm $<1$;
- distinct nonzero translation vectors are mutually acute:
  $$
  \Delta_i\cdot\Delta_j>0.
  $$

### 2.1 A contact edge cannot join two distinct moving owners

If an old unit contact joins owners $i,j$, the four binary states require all of
$$
r,\quad r+\Delta_i,\quad r-\Delta_j,\quad r+\Delta_i-\Delta_j
$$
to have unit norm. Taking the mixed second difference of squared norms gives
$$
-2\Delta_i\cdot\Delta_j=0,
$$
contradicting mutual acuteness.

### 2.2 Strict-rhombus ownership patterns

A bounded four-face in the triangle-free contact graph is a strict unit rhombus.

Suppose one rhombus vertex moves while its two adjacent vertices are fixed. If the two old unit vectors to those neighbors are $a,b$, contact preservation gives
$$
a\cdot\Delta=b\cdot\Delta=-\frac{|\Delta|^2}{2}
$$
up to the consistent orientation convention. Hence $\Delta$ is parallel to $a+b$, and the nonzero solution has length
$$
|\Delta|=|a+b|=2\cos(\theta/2).
$$

For a strict unit rhombus in a triangle-free source,
$$
\pi/3<\theta<2\pi/3,
$$
so
$$
|\Delta|>1,
$$
contradicting the small-move hypothesis.

The same two-contact calculation excludes the one-, three-, and opposite-two-vertex moving patterns. The mixed-difference calculation excludes two adjacent distinct owners.

Therefore the only possible binary ownership patterns on a strict rhombus are:

- all four vertices fixed;
- all four vertices in one owner;
- two adjacent vertices in one owner and the other two fixed.

A unit-separated source has no additional source point in the interior of a strict unit rhombus. In affine rhombus coordinates, rounding both coefficients to a nearest corner gives a corner at distance strictly below one.

Consequently:

$$
\boxed{\text{a lower clause joining two distinct moving owners cannot be a strict-rhombus diagonal}.}
$$

Unary rhombus-diagonal clauses are not excluded; the regression below shows this distinction is essential.

## 3. A sharply defined pure-conflict graph is a path forest

Fix orthonormal directions $u,v$. Let $P$ be the graph on actual source vertices whose selected edges satisfy
$$
1<|r|\le\frac54,
\qquad
|r\cdot v|\le\frac18.
$$

Then every connected component of $P$ is a path or isolated vertex.

Indeed,
$$
|r\cdot u|
>
\sqrt{1-\frac1{64}}
>
\frac78.
$$

Two neighbors of one vertex on the same $u$-side would differ in $u$-coordinate by at most $3/8$ and in $v$-coordinate by at most $1/4$, so their mutual squared distance would be at most
$$
\left(\frac38\right)^2+\left(\frac14\right)^2
=
\frac{13}{64}
<1,
$$
contradicting unit separation.

Hence every vertex has at most one neighbor on each longitudinal side. A finite cycle would have a vertex of maximal $u$-coordinate with two neighbors on the same side, impossible.

Thus
$$
\boxed{P\text{ is a linear forest}.}
$$

This is a theorem on actual source vertices, not on owner labels. Owner identification may destroy the forest property; that overreach is registered separately below.

**Verdict for Sections 1--4 of the source report:** canonical-ready as \`C-NEAR-UNIT-CONFLICT-GEOMETRY\`.

## 4. Global stopped O–O cuts localize full-source lower blockers

Now impose explicit finite-motion hypotheses.

Assume the positive contact core is connected. Select actual global stopped O–O trains: every selected train has both terminal occurrences on the outer face, every interior train edge has a strict rhombus on both sides, and no selected train edge is incident with a bounded nonquadrilateral face.

The selected train cuts induce layer/owner translations on the core.

### 4.1 Every bounded nonquadrilateral face has one core owner

No boundary edge of a bounded nonquadrilateral face lies on a selected O–O cut. Consecutive face-boundary vertices therefore have equal shore indicators. Following the full occurrence-counted face walk, including bridges and repeated vertices, shows that the entire boundary belongs to one core owner.

Together with the rhombus ownership theorem above, this implies:

$$
\boxed{\text{every core-to-core intergroup lower clause lies in the outer contact face}.}
$$

The only bounded core-to-core lower obstruction left is a **unary** strict-rhombus diagonal.

### 4.2 Bounded-face isolate reassignment

Let the translation cloud, including zero, have diameter
$$
s<
\min\left\{
D-\sqrt{D^2-1},
\sqrt2-1
\right\}.
$$

Use canonical \`C-LONG-PAIR-ISOLATE-DISPATCH\` for exterior/long-pair isolates. Reassign every contact isolate lying inside a bounded nonquadrilateral face to that face's common core owner.

Then every such bounded-face isolate creates **no** new lower or upper obstruction.

#### Upper constraints

An isolate $z$ in an open bounded contact face lies strictly inside the convex hull of that face's boundary vertices. Write
$$
z=\sum_i\lambda_ip_i.
$$
Every boundary vertex is a source point at distance at least one from $z$, so for any source point $q$,
$$
|z-q|^2
=
\sum_i\lambda_i|p_i-q|^2
-
\sum_i\lambda_i|p_i-z|^2
\le D^2-1.
$$
Thus no strict-long pair is incident with $z$. Relative displacement at most $s<D-\sqrt{D^2-1}$ keeps every upper pair strict.

#### Lower constraints

If reassignment created a lower equality/violation with $x$, then originally
$$
1<|z-x|\le1+s<\sqrt2.
$$
Near-unit planarity makes the open segment $zx$ stay in the same old contact face. Hence $x$ is either a boundary core point of that face or another isolate in it. Both receive the same translation as $z$, so the distance is unchanged, contradiction.

There are no hidden four-face isolates by the strict-rhombus interior argument above.

Therefore after bounded-face isolate reassignment:

$$
\boxed{\text{every intergroup full-source lower clause lies in the outer contact face, except unary rhombus diagonals}.}
$$

### 4.3 Conditional outer-face capacity corollary

Under the additional explicit assumptions that

- every unary rhombus-diagonal state remains strict;
- all upper constraints/old diameters have already been handled;
- every nonzero singleton owner pattern strictly shortens an old diameter;

canonical minimality implies that every surviving owner must contain or be charged to an outer-face source vertex.

After bounded-face isolate reassignment,
$$
\boxed{k\le b+Z_{\rm out},}
$$
where $Z_{\rm out}$ counts contact isolates lying in the outer contact face.

Using the audit.60 upper-exception budget across an original family of $r$ proposals gives
$$
\boxed{r\le b+Z_{\rm out}+2d_H.}
$$

This is an exact conditional capacity statement, not a global asymptotic contradiction.

### 4.4 General small O–O multishear reduction

The same finite reduction does not require binary swaps.

Suppose selected global stopped O–O train vectors $u_i$ are replaced by unit vectors $u_i'$, inducing layer translations
$$
X_0=0,
\qquad
X_j=\sum_{i=1}^j(u_i'-u_i),
$$
and the translation cloud has diameter below the same small threshold.

Assign bounded-face isolates to their common layer owner and exterior isolates by \`C-LONG-PAIR-ISOLATE-DISPATCH\`.

A strict rhombus meets at most one selected train whenever the selected projective directions lie in an interval of width $<\pi/3$. If that train changes from $u_i$ to $u_i'$ and the transverse unit side is $w$, its two noncontact diagonals remain strict exactly when
$$
\boxed{|u_i'\cdot w|<\frac12.}
$$

After checking these local unary rhombus inequalities, the entire full-source feasibility problem reduces to:

$$
\boxed{
\begin{array}{c}
\text{actual old diameter constraints},\\
|J|\le d_H\text{ inactive upper exceptions},\\
\text{explicit unary rhombus inequalities},\\
\text{outer-face near-unit lower pairs only}.
\end{array}
}
$$

This theorem is promoted only at the explicit finite-motion scope stated above. It does not assert that every C-II survivor supplies such an O–O multishear.

**Verdict:** canonical-ready as \`C-OO-LOWER-BLOCKER-LOCALIZATION\`.

## 5. Regression: unary rhombus diagonals can fail under arbitrarily small contact-preserving motion

The source report gives an exact rational strict rhombus.

An adjacent pair of rhombus vertices is translated by a vector of norm below
$$
10^{-5},
$$
all four old unit contacts remain exactly unit, yet one formerly strict rhombus diagonal becomes **shorter than one**.

Therefore:

$$
\boxed{\text{contact preservation + arbitrarily small motion does not imply unary rhombus-diagonal immunity}.}
$$

Any finite O–O motion theorem must check the explicit rhombus inequality; it cannot infer it merely from small amplitude.

**Verdict:** register as \`C-UNARY-RHOMBUS-BLOCKER-REGRESSION\`.

## 6. Regression: a source path forest may become an owner cycle

The report also gives an exact rational packet of three well-separated near-unit source pairs.

As an actual source graph those three conflict edges form a matching, hence a forest. Assign endpoint owners
$$
(A,B),\quad(B,C),\quad(C,A).
$$
The resulting owner conflict graph is a triangle.

Thus:

$$
\boxed{\text{source-level path/forest structure does not imply the owner implication/conflict graph is acyclic}.}
$$

A future 2-SAT closure theorem must use actual owner/train/KKT structure, not just the source-pair forest theorem.

**Verdict:** register as \`C-OWNER-CONTRACTION-CYCLE-REGRESSION\`.

## 7. Verification

The exact verifier
$$
\texttt{research/verify\_near\_unit\_face\_conflicts\_2026\_10\_01.py}
$$
was rerun independently and passed:

- the $\sqrt2$ square threshold;
- all 16 rational strict-rhombus binary ownership patterns;
- the arbitrarily-small unary rhombus blocker;
- the matching-to-owner-cycle regression;
- the actual O–O bounded-face isolate extension packet;
- the triangle-free pure-joint equality packet with strict diameter decrease.

The analytic planarity, face-localization, path-forest, and bounded-face transport arguments above do not depend on the verifier.

## 8. Effect on the live audit.60 frontier

Audit.60 reduces sufficiently small finite-motion failure to near-active implication/weighted paths plus at most $d_H$ upper exceptions.

Audit.61 sharpens the geometry of those lower paths:

- near-unit blocker edges below $\sqrt2$ are planar and cofacial;
- a selected quantitative pure-conflict band forms a path forest on actual source vertices;
- distinct moving owners cannot interleave through a strict rhombus under the stated contact-preserving acute-translation hypotheses;
- for genuine global O–O motions, bounded nonquadrilateral faces and all their isolates can be transported rigidly with one owner;
- after explicit unary-rhombus checks, every remaining lower blocker lies in the **outer contact face**.

The remaining obstruction is therefore more specific:

$$
\boxed{\text{outer-face near-unit implication structure}+\text{unary rhombus blockers}+\text{at most }d_H\text{ upper exceptions}.}
$$

The next high-value theorem should exploit outer-face order, loaded-hull occurrence structure, audit.53 loaded returns, and audit.56 diameter coordinates to rule out the implication paths/cycles required by canonical 2-SAT unsatisfiability—or build a satisfying shortening assignment.

**Promotion recommendation:** advance theorem state to \`2026-10-05.audit.61\`, promote the two finite theorems, and register the two regressions.
