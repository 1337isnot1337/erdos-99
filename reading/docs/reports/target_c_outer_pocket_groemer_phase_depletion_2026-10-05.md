> Generated reading edition · [exact source](../../../docs/reports/target_c_outer_pocket_groemer_phase_depletion_2026-10-05.md) · source SHA-256 `f72078b55ebc5d9f35a74922e1e1149321eeab9abf71e2e70e628463c92e601e`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-CDB4A193FF43","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — Groemer phase depletion of every outer-ended train

**Date:** 2026-10-05
**Starting main:** `f539af073a691c13327a0a7fef3c746fb7704e5f`
**Preceding run checkpoint:** `76a673d2981ef4fa12985be7652786a4c4a87d66`
**State:** `2026-09-14.audit.51`
**Classification:** conditional theorem candidate awaiting independent audit;
artifact unreviewed. No canonical promotion.
**LEVEL I STATUS: STILL OPEN. C-II REMAINS OPEN.**

## 1. Exact implication and remaining hypotheses

```text
small fixed-boundary Oler residual + uniformly integrable outer-pocket lengths
  -> every outer-pocket contact edge has the phase of its hull side, modulo pi/3,
     except an asymptotically negligible family of terminal occurrences
  -> all outer-ended stopped trains carry o(D^2) rhombi
  -> the quadratic bulk lives on trains with two bounded exceptional-face ends
  -> an additional, explicit second-depletion charge in the current synthesis.
```

The first arrow is an aggregate statement: it does not assert that each pocket
has small residual. Nor does it activate a near-contact. Its geometric input
is Groemer equality, including the segment equality case.

The two hypotheses are not canonical conclusions. The theorem eliminates the
subbranch in which the resulting internal train bank is too small, and the
subbranch in which the bounded exceptional-face perimeter is too small. It
leaves positive residual and persistent outer-pocket length tails live.

## 2. Source class, exact objects, and dependencies

Consider any sequence of canonical triangle-free full-core Type-II sources
with diameters (D\to\infty). Use the actual contact-minimal, then
diameter-pair-minimal source. Every contact-isolated source point is retained.
Write (F) for the actual loaded force hull and use the current synthesis's

$$
q,m_B,u_B,b,Q,f,k,R_4,T,S,\sigma_R,
\qquad s=\sqrt{\pi/(2\sqrt3)}.
$$

In particular, (b=q+m_B+u_B), (h_B=q-m_B) is the number of unit
loaded-hull sides, (P_{\rm exc}=4f+Q), and

$$
2T=b+P_{\rm exc},\qquad T=q-k+2f\le3\pi D.
\tag{2.1}
$$

Dependencies personally used are canonical [Section 67](../targets/target-c/67-rhombus-population-transport-audit.md)
(hull augmentation, convex pockets, source assignment),
[Section 69](../targets/target-c/69-coherent-grain-interface-audit.md)
(fixed-width train-phase bins), and the audited proof-only
[hull phase-capacity/depletion theorem](target_c_fullcore_hull_train_depletion_floor_2026-10-04.md)
and [finite synthesis](../../research/target_c_hull_depletion_post_endpoint_synthesis_2026-10-04.md).
The exact residual identity is independently reconstructed in
[the residual conservation note](../../research/target_c_inactive_chamber_residual_conservation.md).
None of drafts #663, #668, #671, or #677 is a premise of this theorem.

Add every missing loaded-hull side to the contact graph. Its new pockets are
convex simple faces. Each pocket has exactly one added side: there are (m_B)
new pockets by Euler, each uses an added side, and each added hull side has
exactly one bounded-side occurrence. Therefore their incidences are bijective.

For pocket (j), let (\ell_j\ge2) be the number of actual unit contact
edges in its remaining boundary path, (c_j) its added hull side, (z_j)
its assigned isolated population, and

$$
r_j=\frac{A_j}{a_0}+\frac{\ell_j+|c_j|}{2}+1-(\ell_j+1)-z_j\ge0,
\qquad a_0=\sqrt3/2.
\tag{2.2}
$$

An isolated point on the added side is assigned to its unique interior
pocket, as in Section 67. It remains included in (z_j). The conservation
identity gives (\sum_j r_j\le R_F), where

$$
R_F=\frac{A_F}{a_0}+\frac{P_F}{2}+1-N_F-\frac{E_4}{a_0}\ge0.
\tag{2.3}
$$

The hypotheses of the new theorem are

$$
\frac{R_F}{D}\longrightarrow0,
\tag{H1}
$$

and uniform integrability of the *occurrence lengths* of the pockets:

$$
\boxed{\lim_{K\to\infty}\limsup_{D\to\infty}
 \frac1D\sum_{j:\ell_j>K}\ell_j=0.}
\tag{H2}
$$

A fixed bound on all (\ell_j) is sufficient for (H2); it is not required.
No bound on physical exceptional-face degrees is part of (H2).

## 3. Fixed-length Groemer direction stability

For projective directions define reduced phase distance by

$$
\operatorname{dist}_{60}(\phi,\psi)
=\min_{n\in\mathbb Z}|\phi-\psi-n\pi/3|.
$$

**Lemma OP.1.** Fix (K\ge2) and (\eta>0). There is

$$
\sigma_K(\eta)>0
$$

such that any convex polygon with (2\le\ell\le K), a unit-contact
boundary path, a distinguished straight boundary chord of length at least one, and any
unit-separated assigned source population satisfies

$$
r<\sigma_K(\eta)
\quad\Longrightarrow\quad
\operatorname{dist}_{60}(\arg e,\arg c)<\eta
\quad\hbox{for every contact edge }e\hbox{ of the path}.
\tag{3.1}
$$

The chord may be an added pocket side or an actual unit hull side of a
bounded contact face. This is a statement about directions, not contact
activation or KKT support.

### Proof

Suppose the conclusion fails along a sequence with residual tending to zero.
Pass to a fixed path length (\ell\). Since the contact path has length
(\ell), its chord length lies in ([1,\ell]), its diameter is at most
(\ell), and its area is bounded in terms of (K). Oler therefore bounds
the assigned population uniformly. Pass to a fixed population and normalize
one chord endpoint to the origin and its direction to the positive real axis.
All source coordinates lie in a fixed compact set. Unit separation keeps the
labelled points distinct in every limit.

The pocket is the convex hull of its path vertices; adding its assigned
points does not change that hull. Area and convex perimeter are continuous,
also at a segment limit. The limiting set thus attains equality in

$$
N\le A/a_0+P/2+1.
\tag{3.2}
$$

The equality classification, checked in the authors' original
[Böröczky–Ruzsa manuscript, page 2](https://users.renyi.hu/~carlos/wegner.pdf),
is: a segment, or a convex hull triangulated by unit equilateral triangles
using its source points. In the latter case its boundary sides have three
projective directions separated by (\pi/3). In particular every unit
path edge and the nonzero chord have the same reduced phase. In the segment
case they are collinear, with the same conclusion. Neither case permits the
fixed phase error at least (\eta). This contradiction proves (3.1).

The external normalization divides the manuscript's disk-center coordinates
by two. The inequality and equality theorem are the same ones used by the
[all-degree Groemer stability report](target_c_all_degree_groemer_face_stability_2026-09-14.md);
its separate bootstrap constants are not used here. □

## 4. Depletion of the full outer-end family

Let (\mathcal O_D) be every stopped actual train having at least one
outer-contact-walk terminal occurrence. A physical bridge may have two outer
occurrences; count both. Every such occurrence is either a unit hull side or
a contact edge on exactly one pocket boundary. Indeed hull augmentation
puts every other old outer-side occurrence on a new bounded pocket. Thus

$$
b=h_B+\sum_j\ell_j.
\tag{4.1}
$$

**Theorem OP.2.** Under (H1)--(H2), the number of actual strict rhombi
incident with at least one train of (\mathcal O_D) is (o(D^2)).

### Proof with order of limits

Fix (K), then fix (0<\epsilon<\pi/6). Use Lemma OP.1 with
(\eta=\epsilon). Call a length-at-most-(K) pocket bad when its
residual is at least (\sigma_K(\epsilon)). Nonnegativity and (H1)
give at most (R_F/\sigma_K(\epsilon)=o_{K,\epsilon}(D)) bad pockets,
and at most (K R_F/\sigma_K(\epsilon)=o_{K,\epsilon}(D)) bad
contact terminal occurrences.

For a good pocket, an edge in one reduced phase bin of width (\epsilon)
has its chord's reduced phase in the same interval enlarged by
(\epsilon) at each end. This enlarged interval has width
(3\epsilon). Each pocket has its own distinct hull-side anchor and
at most (K) contact occurrences.

The #699 near-disk normal-capacity proof applies to **all** hull sides here.
Every side has length at least one, so their count is at most their total
length. Uniformly in the shifted reduced interval, the side count in a
width-(w) bin is ((3w+o_w(1))D). Consequently each width-(\epsilon)
train bin contains at most

$$
g_j\le (3+9K)\epsilon D+o_{K,\epsilon}(D)
       +\sum_{\ell_i>K}\ell_i
\tag{4.2}
$$

members of (\mathcal O_D). Associate each train with one of its outer
terminal occurrences to obtain this upper bound; distinct trains cannot
use the same terminal occurrence.

Section 69 deletes (O_\epsilon(D)) rhombus crossing edges to put every
remaining edge into a common real phase bin. The train graph is simple, so
the number of retained crossings touching (\mathcal O_D) is at most

$$
\sum_j g_jT_j\le(\max_j g_j)T\le3\pi D\max_j g_j.
\tag{4.3}
$$

Writing (\beta_K=\limsup_D D^{-1}\sum_{\ell_i>K}\ell_i), (4.2)--(4.3)
and the deleted edges give

$$
\limsup_D\frac{R_{\mathcal O}}{D^2}
\le3\pi[(3+9K)\epsilon+\beta_K].
\tag{4.4}
$$

First take the source sequence limit with (K,\epsilon) fixed. Then let
(\epsilon\downarrow0), still with (K) fixed. Finally let
(K\to\infty) and use (H2). The result is zero. Neither a uniform
rate of Groemer stability nor a uniform rate in the disk limit is assumed. □

Only an auxiliary train-graph family is removed. All source points, actual
contacts, unselected contacts, diameter constraints, and isolates remain.

## 5. The actual internal bank and branch elimination

Let (T_{\rm int}=T-|\mathcal O_D|). These are exactly the trains with
two terminal occurrences on bounded nonquadrilateral faces. Let
(T_{\rm mix}) count trains with one outer end and one such bounded end.
Exact terminal counting gives

$$
\boxed{P_{\rm exc}=2T_{\rm int}+T_{\rm mix}.}
\tag{5.1}
$$

After OP.2, the induced crossing graph on the internal bank retains
((\Delta_2-o(1))D^2) rhombi. Mantel yields

$$
\boxed{T_{\rm int}\ge(2s-o(1))D,\qquad
 P_{\rm exc}\ge(4s-o(1))D+T_{\rm mix}.}
\tag{5.2}
$$

Thus no sequence satisfying (H1)--(H2) has
(\limsup T_{\rm int}/D<2s), or
(\limsup(P_{\rm exc}-T_{\rm mix})/D<4s).
These alternatives are excluded for every such sequence, not just generic
ones. The constant is (4s=3.809251ldots); its exact expression controls.
This is a conditional branch elimination, not full-core closure.

It follows that a sequence violating (5.2) must have either a positive
normalized residual along a subsequence, or a persistent normalized
outer-pocket occurrence tail along a subsequence. The tail is not silently
replaced by a fixed-degree or single macroscopic face alternative.

## 6. Substitution into the strongest physical synthesis

Let (G_D) be #699's good-hull train family. It is contained in
(\mathcal O_D), and (|G_D|=h_B-d_D), with (0\le d_D\le2).
Therefore deleting the additional family
(\mathcal O_D\setminus G_D) is a valid second depletion. Its exact
cardinality is (z_O=|\mathcal O_D|-|G_D|\ge0).

Substituting it immediately into (S) gives

$$
\boxed{
5m_B+4S+2\sigma_R\ge2(\pi+s)D
 +5z_O+5k+2(Q-f)+2(b-P_F)-o(D).
}
\tag{6.1}
$$

Every train has at most two outer ends, so (|\mathcal O_D|\ge b/2).
Since (b=q+m_B+u_B),

$$
\boxed{z_O\ge\max\{0,(3m_B+u_B-q)/2+d_D\}.}
\tag{6.2}
$$

In particular a live large-(m_B) branch satisfying
(3m_B+u_B-q\ge cD) pays an additional (5cD/2) in (S).
The former nonunit-hull currency then cannot be treated as a free escape.
This is a second-depletion payment, rather than a conversion of near-unit
lower constraints into near-diameter upper constraints.

Singleton trains with no outer end can also be removed at no rhombus cost;
their count adds to (z_O) in (6.1). Do not count outer singletons again.

### 6.1 Spend bounded-degree boundary exceptional faces as well

Fix an integer (K\ge5). Let (\mathcal B_{K,D}) be **all** bounded
nonquadrilateral physical contact faces of degree at most (K) having an
actual unit loaded-hull side. Put

$$
P_{B,K}=\sum_{f\in\mathcal B_{K,D}}\deg f,
\qquad P_{U,K}=P_{\rm exc}-P_{B,K}.
\tag{6.3}
$$

Choose one unit hull side as an anchor for each selected face. These anchors
are distinct: an actual hull side has only one inside face. They are also
distinct from the added-side anchors of the pockets. A face may touch more
than one hull side; no one-side-per-physical-face assumption is made.

Its Oler residual is (A/a_0-m/2+1-z). Lemma OP.1 applies with the chosen
unit edge as chord and the other (m-1) contact edges as path. The face
residuals sum to at most (R_F=o(D)), so all but (o(D)) selected faces
have every boundary edge's reduced phase close to their anchor's phase.
The same uniform hull-bin estimate and Section-69 argument therefore prove
that every train having an end on one of these selected faces carries only
(o(D^2)) aggregate rhombus incidence. The fixed cutoff (K) is taken
before the source sequence limit; there is no claim about a growing cutoff.

**Theorem OP.3.** Under (H1)--(H2), let (\mathcal D_{K,D}) be the union
of the outer-ended trains and trains with a selected-face end. It is a
valid subquadratic-incidence deletion family. The retained bank consists
exactly of trains whose two ends lie on unselected exceptional faces.
If its size is (T_{U,K}), and (T_{\rm mix,K}) counts trains with one
unselected-face end and one marked end, then

$$
\boxed{T_{U,K}\ge(2s-o(1))D,\qquad
P_{U,K}=2T_{U,K}+T_{\rm mix,K}
\ge(4s-o(1))D+T_{\rm mix,K}.}
\tag{6.4}
$$

Thus boundary Groemer faces cannot supply the surviving quadratic bank.
For every fixed (K), a sequence with (H1)--(H2) and
(\limsup P_{U,K}/D<4s) is excluded. In particular the branch with all
exceptional faces of degree at most (K) touching a unit hull side is
excluded, since then (P_{U,K}=0). No source point is deleted by this
conditional branch elimination.

There are (b+P_{B,K}) marked terminal occurrences, and each train has at
most two. Hence the extra deletion beyond (G_D), denoted (z_K), obeys

$$
\boxed{z_K=|\mathcal D_{K,D}|-|G_D|
\ge\max\{0,(3m_B+u_B-q+P_{B,K})/2+d_D\}.}
\tag{6.5}
$$

Replace (z_O) by this stronger (z_K) in (6.1). This is the requested
phase second depletion on a concrete family of bounded-degree exceptional
faces. It spends their geometry without falsely activating a hidden pair.
The large unselected-face perimeter in (6.4) still needs a contradiction
or finite source replacement.

## 7. Hostile checks and exact surviving gap

- A pocket has one added side by the finite incidence argument, not by an
  assumed source path being Eulerian. Bridges retain both occurrences.
- Both Groemer equality cases are included. No RSR uniqueness is imported.
- Assigned isolates occur in the residual and compactness point set. No
  affine-kernel statement is used on them.
- The direction limit creates no actual contact and transfers no force.
- Large pockets may contribute many ends at one anchored phase. (H2) is
  essential to this proof; residual alone does not control their multiplicity.
- A mere count of anchors cannot replace the occurrence tail. A train with
  two outer ends is removed once and consumes two counted occurrences.
- The phase argument uses the (D\) limit before shrinking the bin and then
  removes the degree cutoff. It never divides an (o(D^2)) area statement
  by a possibly small carrier diameter.
- Actual source global optimality supplies the canonical Type-II/phase/force
  hull inputs. This result is not an all-constraints deformation theorem.

The companion [exact verifier](../../../research/verify_target_c_outer_pocket_phase_depletion_2026_10_05.py)
checks rational triangular pockets approaching Groemer equality, an explicit
positive-residual direction mismatch, terminal counts, and the finite second
payment. It does not certify compactness, phase coarea, source optimality,
the two asymptotic hypotheses, or a strict competitor.

The surviving obligations are positive residual activation, persistent
outer-pocket/exceptional-face tails, and the internal-to-internal bulk bank.
The earlier global face quotas apply to simple augmented high-degree pocket
faces, but their paths are not automatically independent trains. The
macroscopic-container branch remains separate and open.
