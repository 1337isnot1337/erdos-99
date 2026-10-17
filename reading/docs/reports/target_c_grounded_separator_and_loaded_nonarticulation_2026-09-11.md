> Generated reading edition · [exact source](../../../docs/reports/target_c_grounded_separator_and_loaded_nonarticulation_2026-09-11.md) · source SHA-256 `110c76aeefca79a2f718fdad8cf30f05d760fab7c8138074d43c881278ec51ea`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-78C8F978E61E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_grounded_separator_and_loaded_nonarticulation_2026-09-11.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=1022d5f21aeb972098aec032f0943ca1a1f63942; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — grounded separator obstruction and loaded non-articulation

**Date:** 2026-09-11
**Repository state:** the run began at `8a78616870368d8456892defe46be6c8e175666a`;
the shared checkout advanced to `b54e1e286f813e80a521681ad06200972d76dd60` during
the run. The controlling C-I/C-II route-map statements were unchanged.
**Run type:** closing-proof attempt / structural proof and regression audit
**Target:** C-II
**Active prompt:** [Target C continuation](../prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md)
**External search:** a search for a geometric thrackle transversal was made; no
external theorem from that search is used.
**Computation:** none in the proof
**Authority:** unpromoted report; no route-map or prompt promotion is made here.

## LEVEL I STATUS

**STILL OPEN.** This report does not solve Erdős Problem #99.

It proves two restrictions from the promoted selected-stress PSD theorem and the
fully force-visible source hypotheses:

1. Every positively diameter-loaded vertex is a non-articulation vertex of the
   full contact core.
2. In the contact/diameter-lexicographic representative, deleting any core vertex
   and contracting the remaining contact components gives a diameter interaction
   multigraph with **no bipartite connected component**, with loops retained.

In particular, if every diameter path passes through one contact vertex, that
vertex is unloaded. There are three to five contact components after its deletion,
and their diameter interaction graph is connected and contains a triangle or a
five-cycle. These are cycles of **contact components**, not necessarily cycles of
the actual diameter graph.

## 1. Starting endpoint and exact implication

The controlling endpoint is
[C-II after the C-I restoration](../targets/target-c/56-ci-restored-frontier.md):
exclude every sufficiently large contact/diameter-lexicographically minimal
triangle-free global minimizer, retaining all source points.

The specific implication attacked here is

```text
actual PSD stress + a contact separator
    -> grounded matrix with a forbidden sign pattern
    -> collinear contact component
    -> forbidden unloaded degree two, or a finite diameter-pair release.
```

The finite release, when needed, preserves every contact and removes exactly one
diameter pair. Thus it contradicts the actual secondary integer minimum; no
asymptotic loss or population estimate is substituted for this contradiction.

The loaded non-articulation theorem itself needs only contact minimality and full
contact support, not the secondary diameter-pair minimum.

## 2. Definitions and trusted inputs

Let $A$ be a triangle-free global minimizer with $D>1$. Let $V$ be its
nonisolated contact vertices and $G=(V,C)$ its contact core. In C-II choose a
relative-interior normalized KKT stress, with

$$
\alpha_e>0\quad(e\in C),\qquad
\beta_h>0\quad(h\in H_+),\qquad
B=V(H_+).
$$

The promoted inputs are:

- $G$ is connected and its unit-edge drawing is planar.
- Every vertex of $B$ is an extreme vertex of the full source hull.
- Every unloaded core vertex has full contact degree at least three; every loaded
  vertex has degree at most three; every core vertex has degree at most five.
- With the Laplacian convention of the
  [restoration audit, Section 4](target_c_c53_orientation_and_ci_restoration_2026-09-09.md),
  the actual stress matrix satisfies
  $$
  \Omega=L_C(\alpha)-L_{H_+}(\beta)\succeq0,
  \qquad \Omega\mathbf1=\Omega P_x=\Omega P_y=0.
  \tag{2.1}
  $$
- Distinct, vertex-disjoint source diameter chords have alternating hull endpoints.

The degree statements are
[C26](target_c_fully_visible_no_neutral_vertices_2026-08-31.md) and
[C35](target_c_loaded_boundary_attachment_2026-08-31.md). The relevant connectivity,
planarity, and diameter-path inputs are recorded in
[the force-hull module, Sections 6 and 8](../targets/target-c/01-force-hull-and-shear.md).
None of these uses the unpromoted ZR/ZF maximal-rank conclusions.

For Theorem GS below, additionally choose the promoted lexicographic
representative, so $H_+=H$ is the **entire actual diameter graph**.

All matrices below are on $V$. Contact-isolated points remain in $A$; they have
zero stress rows. Any finite motion below fixes them and checks their inactive
distance constraints by strict slack.

## 3. Elementary grounded-matrix lemma

### Lemma GM

Let $M$ be a real symmetric positive semidefinite matrix with nonpositive
off-diagonal entries. Suppose the graph of its strictly negative off-diagonal
entries is connected. Then

$$
\dim\ker M\le1.
\tag{3.1}
$$

If the kernel is nonzero, every nonzero kernel vector has no zero entries and has
one strict sign, up to multiplying the whole vector by $-1$.

**Proof.** If $Mx=0$, the off-diagonal signs give

$$
|x|^{\mathsf T}M|x|\le x^{\mathsf T}Mx=0.
$$

PSD therefore gives $M|x|=0$. If $|x|_i=0$, the $i$-th equation is a sum of
nonpositive terms. It forces every neighbor in the negative-entry graph also to
have zero coordinate. Connectedness would give $x=0$. Thus a nonzero kernel
vector has no zero entry. Equality in the displayed quadratic inequality then
forces equal signs across every negative-entry edge, hence throughout the graph.
Two independent kernel vectors would have a nonzero linear combination with one
zero coordinate, which has just been excluded. This proves the lemma. $\square$

### Grounding convention

Fix $z\in V$, translate $p_z=0$, and let $V_1,\ldots,V_k$ be the vertex sets
of the contact components of $G-z$. Deleting the $z$-row and column of
$\Omega$ gives a PSD principal matrix. On these remaining coordinates, both
coordinate vectors are still in its kernel: the deleted coordinate at $z$ is zero.

More generally, if $U$ is a union of the $V_i$ with no positive diameter edge
from $U$ to $V\setminus(U\cup\{z\})$, then

$$
\Omega_{UU}P_{U,x}=\Omega_{UU}P_{U,y}=0.
\tag{3.2}
$$

Diameter edges to $z$ are retained in the diagonal entries. They are not
discarded from the stress.

## 4. The loaded non-articulation theorem

### Theorem LN

In the contact-minimal fully force-visible branch with $D>1$,

$$
\boxed{G-z\text{ is connected for every }z\in B.}
\tag{LN}
$$

### Proof

Fix $z\in B$ and translate it to zero. Since it is a strict extreme vertex of
the finite source hull, choose a linear functional $\ell$ such that

$$
f_i:=\ell(p_i)>0\qquad(i\in V\setminus\{z\}).
$$

Set $M=\Omega_{V\setminus\{z\},V\setminus\{z\}}$. By grounding, $Mf=0$.
For arbitrary constants $a_1,\ldots,a_k$, put $w_i=a_r f_i$ on $V_r$.
The matrix $\operatorname{diag}(f)M\operatorname{diag}(f)$ has zero row sums.
Its quadratic-form identity gives

$$
w^{\mathsf T}Mw
=-\sum_{i<j}M_{ij}f_if_j(a_{r(i)}-a_{r(j)})^2
=-\sum_{\substack{ij\in H_+\\r(i)\ne r(j)}}
\beta_{ij}f_if_j(a_{r(i)}-a_{r(j)})^2.
\tag{4.1}
$$

There are no contact edges between distinct $V_r$. All other terms vanish
because the two component constants agree. PSD and the strict positivity of
$\beta_{ij},f_i,f_j$ show that **no positive diameter edge joins different
contact components of $G-z$**.

Suppose one component $V_r$ has no internal positive diameter edge. Its grounded
principal block has nonpositive off-diagonal entries, with connected negative-entry
graph given by its contacts. Equation (3.2) and Lemma GM force all its coordinates
to lie on one line through $z$.

The unit-contact graph on $V_r\cup\{z\}$ is then a straight consecutive unit
chain on one side of $z$. To see this explicitly, start from a contact neighbor
of $z$; connectivity makes every coordinate an integer multiple of its unit
direction. A path avoiding $z$ cannot pass from positive to negative multiples.
Every intermediate integer is present by connectivity.

If the chain has two or more vertices other than $z$, its first vertex has full
contact degree two and lies strictly between two source points. It is not a
diameter endpoint, contrary to C26. Thus $V_r$ is a single contact neighbor
of $z$. Its only possible positive diameter partner is $z$, because there
are no internal or cross-component positive diameters. Their distance is one,
whereas $D>1$. This contradicts equilibrium at that contact leaf.

Therefore **every** $V_r$ contains an internal positive diameter edge. If there
were two different components, choose one such edge in each. Their four endpoints
alternate on the source hull. Connectedness supplies two vertex-disjoint contact
paths joining the two respective endpoint pairs, one inside each component. Such
paths cannot both be drawn in the hull disk without intersecting. This contradicts
the planar contact embedding.

Hence $k=1$, proving (LN). $\square$

### Consequence for bridges

If a loaded vertex is incident to a contact bridge, it has contact degree one.
Indeed, a bridge incident to a vertex of degree at least two makes that vertex an
articulation point. Thus every other endpoint of a contact bridge is unloaded,
and has degree at least three.

This does not exclude bridges between unloaded vertices or bridges ending at
loaded contact leaves.

## 5. The general diameter interaction obstruction

For a fixed $z$, define the multigraph $J_z$ as follows:

- Its vertices are the contact components $V_1,\ldots,V_k$ of $G-z$.
- Every actual diameter edge with neither endpoint $z$ gives an edge between
  the components containing its endpoints.
- An internal diameter edge gives a loop. Parallel edges are retained.
- Diameter edges incident to $z$ are not edges of $J_z$; their stress
  contributions remain in the grounded matrix.

Here a graph with a loop is nonbipartite.

### Theorem GS

For the lexicographically normalized C-II source with $D>1$,

$$
\boxed{\text{Every connected component of }J_z\text{ is nonbipartite, for every }z\in V.}
\tag{GS}
$$

### Proof

Suppose a connected component $T$ of $J_z$ is bipartite. Let $U$ be the union
of its contact components, and give each such component a sign $\varepsilon_r\in
\{-1,1\}$ from a bipartition. Let $E$ be the diagonal matrix with that sign
on its component's vertices.

There is no internal diameter edge in any component belonging to $T$, since that
would be a loop. Contacts have negative off-diagonal stress entries and connect
vertices of the same sign. Diameter edges within $U$ have positive entries and
connect opposite signs. Consequently

$$
\widetilde M=E\Omega_{UU}E\succeq0
$$

has nonpositive off-diagonal entries. Its negative-entry graph is connected: each
contact component is connected, and the diameter edges of the connected graph
$T$ connect these components. Equation (3.2), conjugation by $E$, and Lemma GM
imply that the two coordinate columns on $U$ have rank at most one. Thus all
points of $U$ lie on one line through $z$.

As in the proof of LN, every contact component in $U$ is a straight unit chain
attached to $z$, and C26 makes it a single unit-distance neighbor. There are at
most two such positions on the line. A single position cannot balance its positive
contact force: a positive diameter partner would have to be $z$, at distance one.
Therefore there are exactly two points

$$
u=z+a,\qquad v=z-a,\qquad |a|=1,
$$

whose only contact is to $z$. Their only possible positive diameter edge is
$uv$, so $D=2$. Full actual diameter support means neither $u$ nor $v$ has
any other actual diameter partner.

Rotate $u$ about $z$ by a sufficiently small nonzero angle $t$, fixing every
other source point, including all isolates. The contact $uz$ remains exactly one
and

$$
|u(t)-v|=2|\cos(t/2)|<2.
\tag{5.1}
$$

Every other pair involving $u$ was strictly between one and two, so retains both
inequalities for sufficiently small $t$. Thus the full contact graph is unchanged
and the diameter graph loses exactly $uv$, with no new diameter pair. If another
diameter pair remains, this contradicts the secondary diameter-count minimum. If
none remains, it gives a strict smaller-diameter competitor. Both alternatives
contradict the chosen global source. $\square$

## 6. Exact consequence for a common vertex hub

Say $z$ is a common vertex hub if no actual diameter edge has both endpoints
in one component of $G-z$. Equivalently, every contact path between the endpoints
of any actual diameter pair passes through $z$, allowing $z$ itself to be an
endpoint. This is precisely the condition that $J_z$ has no loops.

### Corollary VH

For such a hub in the lexicographic C-II source,

$$
\boxed{z\notin B,\qquad 3\le c(G-z)\le\deg_C(z)\le5.}
\tag{6.1}
$$

Moreover $J_z$ is connected and has an odd cycle of length three or five. In
particular,

$$
|H|-\deg_H(z)\ge c(G-z).
\tag{6.2}
$$

**Proof.** GS makes each loopless connected component of $J_z$ nonbipartite, hence
it contains at least three vertices. Each contact component needs a distinct contact
at $z$, and triangle-freeness bounds that degree by five. There can therefore be
only one connected component of $J_z$, and its vertex count is between three and
five. It has an odd cycle of length three or five and at least as many edges as
vertices. This proves the count and (6.2). Since $z$ is an articulation point,
LN makes it unloaded. $\square$

If the C24 common bridge-block hub is a singleton vertex, it satisfies this
corollary. Thus that case is reduced to an unloaded junction with a three- or
five-cycle of diameter interactions. A nontrivial common block remains possible.

## 7. Regression and scope audit

| Regression or scope issue | Disposition |
| --- | --- |
| Unit square, regular pentagon, heptagon plus center | Loaded vertices lie on a contact cycle or are contact leaves; LN does not exclude them. The heptagon's isolated center remains part of the source. |
| Opposite unit leaves at a central vertex | Exactly the collinear $D=2$ exception identified inside the GS proof; finite rotation, not PSD alone, excludes it in the lexicographic global source. |
| Odd shell with an inactive cloud | Deleting one cycle vertex leaves a connected contact path with internal diameter edges, hence a loop in $J_z$. GS makes no population or global-optimality claim about the cloud. |
| Near-star networks with small conductances | No conductance lower bound is used. Abstract networks also lack the required source geometry and actual KKT identity. |
| One selected stress with omitted contacts | LN and GS cannot silently be applied to its support as if it were the full contact graph. The full-degree C26 input is essential. |
| Unweighted actual diameter at a moving leaf | GS uses $H=H_*$ to exclude it. This is why its finite-release argument uses the promoted lexicographic representative. |
| A loop or odd cycle in $J_z$ | Not excluded. Dropping loops would make the theorem false. |
| Odd cycle of contact components | Does not imply an actual diameter cycle or a Reuleaux triple; its edges may have different endpoints within each component. |

Two exact models clarify the remaining odd-cycle cases.

### Three-arm star

Take $z=0$ and three unit vectors $p_i$ at angles $0,2\pi/3,4\pi/3$.
The contacts are the three spokes and the diameters are the three leaf pairs,
of length $\sqrt3$. Put $\alpha=1$ on each spoke and $\beta=1/3$ on each
diameter. In the order center, leaves,

$$
\Omega=\frac13(-3,1,1,1)^{\mathsf T}(-3,1,1,1)\succeq0.
$$

The quotient at the center is a triangle. This model is not a global four-point
minimizer, since $D(4)=\sqrt2$, but it rules out excluding the quotient triangle
from PSD, unit contacts, and equilibrium alone.

### Five-arm star: an actual small global minimizer

Take the center and the vertices of a regular pentagon of circumradius one. The
contact graph consists of its five spokes; its diameter graph is the pentagram
cycle, with $D=2\sin(2\pi/5)$. This is the six-point global minimizer recorded in
the [supplied literature baseline](../problem/literature_baseline.md).

Set $\beta=1/5$ on its five diameters and $\alpha=D^2/5$ on each spoke.
The leaf diameter Laplacian has eigenvalues

$$
0,\quad \frac{5+\sqrt5}{10}\ (\text{twice}),\quad
\frac{5-\sqrt5}{10}\ (\text{twice}).
$$

The middle value equals $\alpha$. On the leaf mean-zero subspace the grounded
stress is $\alpha I-L_H$, with two zero and two positive eigenvalues; the
center/leaf-mean energy is $5\alpha(f_z-\bar f)^2$. Thus the full stress is PSD.
Deleting the center gives the allowed five-cycle quotient. Any proposed exclusion
of this case must genuinely use sufficiently large global cardinality.

For comparison, the center and the four points $(\pm1,0),(0,\pm1)$, with spoke
weights one and opposite-diameter weights $1/2$, have PSD energy

$$
\frac12(f_E+f_W-2f_z)^2+
\frac12(f_N+f_S-2f_z)^2.
$$

Their quotient consists of two bipartite edges. This is the exact $D=2$
collinear-pair exception, not a global C-II counterexample; the rotation in (5.1)
releases one diameter while preserving the other.

## 8. Classification and exact remaining obligation

| Claim | Classification |
| --- | --- |
| LN: loaded vertices are not contact articulation points | Proved from promoted inputs; no secondary normalization or maximal stress rank used. |
| GS: no bipartite diameter-interaction component after grounding one core vertex | Proved from promoted inputs, including full actual support and lexicographic minimality. |
| VH: singleton hub is an unloaded three-to-five-branch junction with an odd interaction cycle | Proved consequence of LN and GS. |
| Every articulation point is impossible | Not proved. |
| A quotient triangle violates the actual Reuleaux-triple theorem | Rejected inference: the three components need not supply three mutually diametral source points. |
| LN/GS control isolates, source area, or density | Not claimed. |
| C-II or Level I is closed | Not proved. |

These statements add a restriction on the actual source separator, rather than an
abstract signed minor obtained after arbitrary contractions. They do not recover
literal diameter endpoints along the quotient's odd cycle.

The exact next obligation for the singleton-hub case is:

> Exclude, for all sufficiently large lexicographic triangle-free global sources,
> an unloaded contact vertex $z$ for which $G-z$ has three to five components,
> every diameter joins different components, and the connected diameter interaction
> graph has a three- or five-cycle; count every source point, including isolates.

Resolving that obligation would force the common bridge-block hub to be a
nontrivial block. The separate nontrivial-block and full-source packing problems
would still have to be closed to solve C-II.

## 9. Promotion recommendation and handoff

**Hold as report.** The proofs above have an explicit local audit and exact
regressions, but this run makes no coordinated route-map/prompt promotion and no
claim that the overall C-II endpoint has been reached. Existing concurrent reports
were left untouched.

```text
LEVEL I STATUS: STILL OPEN.

New proved results:
LN: a positively loaded vertex cannot be an articulation of the full contact core.
GS: after grounding a core vertex and contracting contact components, no connected
component of the actual diameter interaction multigraph is bipartite; keep loops.

Mechanism:
actual PSD stress + affine equilibrium -> grounded sign-matrix kernel restriction;
collinearity -> C26 contradiction or exact one-diameter finite release.

Singleton common hub:
unloaded, three to five contact components, connected quotient with a 3- or 5-cycle.
Quotient cycles are not actual diameter cycles.

Still missing:
large-global exclusion of that odd-interaction junction and of the nontrivial hub
block, with the full isolated-point population retained.

Authority:
the September 9 restoration and existing Target C route map remain controlling.
No ZR/ZF maximal-rank theorem or unpromoted population estimate was used.
```
