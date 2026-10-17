> Generated reading edition · [exact source](../../../docs/reports/erdos_problem_99_complete_working_report_SYNTHESIZED.md) · source SHA-256 `ca9fe28ff239dd485e8af885b1f1087694c30985668b7fe3c7c305cf38f5df17`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "d9dd602abec9573b286732c169c2156e22c1dcf2", "source_canonical": false, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "unreviewed", "source_path": "docs/reports/erdos_problem_99_complete_working_report_SYNTHESIZED.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "5bd000f7dfac62b57d6b59d2b0fc92f21482d1d2ecc97810e7c19b16c0f20103"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle was `unreviewed`; it is retained as provenance only. Destination status remains unreviewed/noncanonical.

# Erdős Problem #99

## Audited research record: stress, boundary anchoring, rhombic structure, and the exact remaining obstruction

**Status:** No Level I proof or disproof has been obtained. This document records the strongest unconditional results established during the investigation, audits the supplied and imported arguments, and states precisely what remains unproved.

**Scope:** The seven supplied papers are the only external literature sources used in the main investigation. No internet search was used. The continuation addenda below also give self-contained derivations of the additional finite-packing and boundary lemmas they use, including the finite Oler inequality. Numerical experiments are explicitly separated from proofs.

**Latest audit:** The structural theorem stack through Section 20 is unchanged: every surviving flexible representative has a pointwise fixed contact-minimal core plus a bridge forest, while every jammed survivor has an almost-spanning strict-rhombus core with at least $`2\sqrt n-O(1)`$ train-track ends entering a defect network. Two independent continuation runs now sharpen the boundary-scale endgame in complementary ways. First, an exact Oler-surplus decomposition incorporates area, convex-hull perimeter, topology, holes, rhombic components, and vertices outside the core into one capacity window; it proves convex contact-face and pocket area inequalities and gives explicit $`\Theta(\sqrt n)`$ shell-area charges, but shows that plain area accounting assigns forest vertices the same bulk allowance as core vertices. Second, every bounded defect-face train end has a sharp transverse cost $`\sqrt3/2`$, while every non-hull train end on the unbounded face has an exact positive depth $`\rho_e`$; summing gives a defect-extended train-span inequality. The synthesis sharpens this further to a per-track inequality with the actual hull width $`w_K(\nu_\tau)`$, directly linking the train geometry to Cauchy perimeter/support-function methods. Target B is therefore reduced to a joint Oler/isodiametric/outer-depth stability theorem converting the compulsory outer-shell depths and pocket geometry into enough global surplus. Target A remains the super-boundary bridge-forest capacity problem. No Level I proof or disproof is yet obtained.

---

## Contents

1. [The problem and its quantifiers](#1-the-problem-and-its-quantifiers)
2. [What the supplied literature proves](#2-what-the-supplied-literature-proves)
3. [Audit of the imported GPT arguments](#3-audit-of-the-imported-gpt-arguments)
4. [Exact first-order KKT stress for every minimizer](#4-exact-first-order-kkt-stress-for-every-minimizer)
5. [Consequences for the positive stress support](#5-consequences-for-the-positive-stress-support)
6. [A contact-minimal normal form](#6-a-contact-minimal-normal-form)
7. [The pinned expansive-cone dichotomy](#7-the-pinned-expansive-cone-dichotomy)
8. [Strict pinned stress and interior trapping](#8-strict-pinned-stress-and-interior-trapping)
9. [The forest exclusion and boundary anchoring](#9-the-forest-exclusion-and-boundary-anchoring)
10. [The almost-rhombic structure theorem](#10-the-almost-rhombic-structure-theorem)
11. [Second-order and nonlinear stress identities](#11-second-order-and-nonlinear-stress-identities)
12. [Rattlers and canonical representatives](#12-rattlers-and-canonical-representatives)
13. [Arbitrarily large triangle-free local minima](#13-arbitrarily-large-triangle-free-local-minima)
14. [The regular-shell obstruction](#14-the-regular-shell-obstruction)
15. [Computational exploration](#15-computational-exploration)
16. [Routes that were tested and why they do not close the problem](#16-routes-that-were-tested-and-why-they-do-not-close-the-problem)
17. [Strongest consolidated unconditional theorem](#17-strongest-consolidated-unconditional-theorem)
18. [Exact remaining Level I target](#18-exact-remaining-level-i-target)
19. [Final adversarial audit](#19-final-adversarial-audit)
20. [References](#20-references)
21. [Oler-surplus decomposition for the defect shell](#21-addendum-an-exact-oler-surplus-decomposition-for-the-defect-shell)
22. [Exact track-end depth and defect-extended span](#22-exact-track-end-depth-and-defect-extended-span)
23. [Combined continuation frontier](#23-combined-continuation-frontier)

---

## 1. The problem and its quantifiers

For $`n\ge 2`$, define

```math
D(n)=\min\left\{\operatorname{diam}(A):
A\subset\mathbb R^2,\ |A|=n,\ |x-y|\ge1\text{ for }x\ne y\right\}.
```

A minimizing configuration is an $`n`$-point set $`A`$ with minimum pairwise distance (1) and diameter $`D(n)`$. Its **unit-contact graph** $`G(A)`$ has vertex set $`A`$ and edge set

```math
C(A)=\{xy:|x-y|=1\}.
```

A unit equilateral triangle is exactly a triangle in $`G(A)`$, or equivalently three mutually tangent radius-$`1/2`$ disks in the associated equal-disk packing.

Erdős asks whether

```math
\exists n_0\ \forall n\ge n_0\ \forall A,
\quad A\text{ minimizing}\Longrightarrow G(A)\text{ contains a triangle}.
```

The negation requires triangle-free global minimizers for arbitrarily large $`n`$. One finite counterexample, even a very large one, does not disprove the conjecture. Conversely, constructing one triangle-containing minimizer for every $`n`$ does not prove it, because the conjecture concerns **every** minimizer.

The disk formulation will be used throughout: the radius-$`1/2`$ disks centered at the points of $`A`$ have disjoint interiors, and

```math
\operatorname{diam}\left(\bigcup_{p\in A}B(p,1/2)\right)=D(n)+1.
```

---

## 2. What the supplied literature proves

### 2.1 Exact small cases

Bateman and Erdős [2] establish

```math
D(2)=D(3)=1,\qquad D(4)=\sqrt2,
```

```math
D(5)=\frac{1+\sqrt5}{2},\qquad D(6)=2\sin72^\circ,
```

and prove

```math
D(7)=2,
```

with the unique $`n=7`$ minimizer equal to a regular unit hexagon together with its center.

Bezdek and Fodor [3, Theorem 1.1] prove

```math
D(8)=\frac1{2\sin(\pi/14)},
```

and show that every minimizer has a regular unit heptagon as its convex hull; the eighth point is not uniquely determined.

The exact contact structures show nonmonotonicity:

- $`n=4`$: the unit square is triangle-free.
- $`n=5`$: the regular unit pentagon is triangle-free.
- $`n=6`$: the regular pentagon has circumradius (1), so the center-to-vertex contacts form $`K_{1,5}`$; the configuration is triangle-free.
- $`n=7`$: the center and every pair of adjacent hexagon vertices form a unit equilateral triangle.
- $`n=8`$: taking the eighth point at the heptagon center gives contact graph $`C_7`$ plus an isolated vertex, hence a triangle-free minimizer.

These cases disprove every naive monotonicity principle.

### 2.2 Diameter bounds and normalization

Bondarenko, Hardin, and Saff [5] define

```math
D_2(n)=\min
\frac{\max_{i\ne j}|p_i-p_j|}{\min_{i\ne j}|p_i-p_j|},
```

which is exactly the present $`D(n)`$ after normalizing the minimum distance to (1). With

```math
\Delta_2=\frac{\pi}{\sqrt{12}}=\frac{\pi}{2\sqrt3},
```

their general Theorem 2 yields

```math
\sqrt{\frac n{\Delta_2}}-2\le D(n)\le\sqrt{\frac n{\Delta_2}}.
\tag{2.1}
```

For the plane, however, Bezdek and Fodor give the sharper lower estimate in the introduction to [3]:

```math
\boxed{
\sqrt{\frac n{\Delta_2}}-1\le D(n)<\sqrt{\frac n{\Delta_2}}.
}
\tag{2.2}
```

Indeed, Fejes Tóth's finite packing inequality gives

```math
\operatorname{area}\bigl(\operatorname{conv}A+B(0,1/2)\bigr)
\ge \frac{\sqrt3}{2}n.
```

The parallel body has diameter $`D(n)+1`$, and the isodiametric inequality gives the lower half of (2.2). For the strict upper half, average the number of points of the unit triangular lattice in an open disk of radius $`\frac12\sqrt{n/\Delta_2}`$. The average over lattice translations is exactly $`n`$, so some translate contains at least $`n`$ lattice points; any finite subset of that open disk has diameter strictly smaller than its diameter. The same argument is recorded in Theorem 10.9.

This correction matters: several imported drafts used the weaker (-2) bound even when working specifically in the plane.

### 2.3 Nonlattice optimality

Schürmann [4, Theorem 9] includes the minimum-diameter packing function and proves that, for all sufficiently large $`n`$, extremal packings are nonlattice. His proof uses loose boundary edges and sequential movements of disks in a lattice packing.

This rules out an eventual classification by finite triangular-lattice patches. It does **not** imply that large minimizers are triangle-free, nor does it exclude a nonlattice configuration with a large triangular contact core.

### 2.4 Triangle-free penny graphs

Eppstein [6] proves:

1. Every triangle-free penny graph is (2)-degenerate [6, Theorem 1].
2. Every connected triangle-free penny graph containing a cycle has at least four non-articulation vertices of degree at most (2) [6, Lemma 2].
3. If $`G`$ is connected with graph diameter $`d_G`$, then

   ```math
   |E(G)|\le2|V(G)|-d_G-2
   \tag{2.3}
   
   ```

   [6, Theorem 2].
4. For arbitrary $`n`$-vertex triangle-free penny graphs,

   ```math
   |E(G)|
   \le
   2n-\frac12\sqrt{2\pi\sqrt3\,n}+O(1)
   \tag{2.4}
   
   ```

   [6, Theorem 4].

These results are exact graph-theoretic restrictions, but they do not alone imply geometric flexibility of a cable-strut framework.

### 2.5 Rigidity terminology

Bezdek, Bezdek, and Connelly [7] define tensegrity stresses with nonnegative coefficients on cables and nonpositive coefficients on struts. Their paper develops stability and infinitesimal-rigidity ideas for sphere packings.

One imported argument relied on an all-strut characterization quoted in Section 4 of [7] from another paper. Because the present project permits results actually proved in the supplied sources, the consolidated arguments below do not rely on that quotation. The needed pinned result is instead proved directly by elementary finite-dimensional cone duality.

---

## 3. Audit of the imported GPT arguments

The imported work contains several valuable results, but also some statements that require repair.

| Imported claim | Audit result | Treatment here |
|---|---|---|
| Regular unit $`p`$-gons are triangle-free strict local diameter minima for odd primes $`p`$ | Correct, modulo Euclidean congruence | Included as Proposition 13.1 |
| Pinned rigidity provides a stress strictly positive on every contact | The cited justification was unsafe for pinned frameworks and relied on a theorem merely quoted in [7] | Reproved directly from the zero expansive cone using cone duality |
| In the jammed branch every hull vertex is diametral | Correct; there is also a direct outward-flex proof | Included as Lemma 7.2 and Theorem 8.2 |
| A rigid triangle-free minimizer with forest contact graph has $`n\le43`$ | Correct after replacing “rigid” by the precisely defined zero-cone branch | Included as Corollary 9.2 |
| BHS gives the operative planar lower bound with (-2) | True but not sharp | Replaced by Bezdek-Fodor's planar (-1) bound |
| Every minimizer has an ordinary KKT stress | Correct; MFCQ has an explicit strict direction | Included with full proof |
| Positive contact-stress components must be boundary loaded | Correct | Included in Section 5 |
| A contact-minimal triangle-free minimizer has all non-diameter nonisolated vertices trapped by (3)-(5) contacts | Correct | Included in Section 6 |
| In the pinned zero-cone branch almost all faces are near-equilateral unit rhombi | Correct after direct rank proof | Included in Section 10 |
| One fixed KKT multiplier is nonnegative on the whole second-order critical cone | Not justified by MFCQ | Replaced by a direction-dependent multiplier theorem |
| An affine shear produces a negative second-order stress energy | False | The tensor identity makes the quadratic energy exactly zero |
| The pinned rank count may omit contacts joining two fixed vertices | Correct | Strengthened to $`e^\circ\ge2(n-q)`$ in Theorem 7.1 |
| The total rhombus angular excess is $`O(\sqrt n)`$ | Correct by the concavity chord bound | Included as Corollary 10.4 |
| The midpoint, quartic, annular-mass, and high-moment stress identities | Correct after direct algebraic verification | Included as Theorems 11.3--11.5 |
| A maximal-contact representative has every contact component diameter-anchored | Correct after handling coincident boundary circles | Included as Theorem 12.3 |
| The minimum- and maximum-contact normal forms can be partly combined | Correct only after freezing the original core and all original diameter endpoints | Included as Theorems 12.4--12.5; the remaining bridge forest is not silently declared jammed |
| Rhombus tracks are pseudolines and satisfy $`R\le B^2/16`$ | Correct after replacing an informal crossing-sign argument by the strict displacement-cone proof | Included as Theorem 10.6 |
| A two-direction rhombic core needs $`\Omega(\sqrt R)`$ non-hull supports | Correct with explicit simple-boundary and no-pinch hypotheses | Included as Theorem 10.12, with the one-rhombus and five-rhombus-cross classification at zero support |
| Boundary-pinned almost-equilateral rhombus meshes must contain a $`60^\circ`$ face | False | Proposition 10.10 gives total positive defect $`8/s\to0`$ with zero boundary-pinned cone |
| A triangle-free packing has a uniform density gap | False as a proposed principle | Explicit near-triangular perturbations and shell fillings disprove such a gap |
| Schürmann implies an eventual triangular or rhombic lattice structure | False | His theorem only excludes lattice extremizers |

The imported reports were therefore used as sources of candidate lemmas, not as authorities. Every theorem retained below is either quoted with its exact hypotheses from a supplied paper or reproved in this document.

### 3.1 Disposition of the latest strengthening

The outward hull-vertex flex, the degree-$`\le2`$ local motions, the effective row count $`e^\circ`$, the $`n-O(\sqrt n)`$ cyclomatic bound, the component estimates, and the angular-defect conversion are correct as stated after replacing the informal word “rigid” by the exact condition $`\mathcal E_Q(A)=\{0\}`$.

The virtual-work, midpoint, quartic, dispersion, annular-mass, and high-moment radius formulas are also correct; their constants were recomputed directly. Two proof repairs were made:

1. Full pinned rank follows directly from the zero expansive cone, so no rigidity theorem merely quoted in [7] is invoked.
2. A regular boundary translation can activate several coincident constraints. They need not be unique, but the corresponding new unit edges form a matching and therefore cannot create a triangle. This is the form proved in Theorem 12.3.

### 3.2 Audit of the bridge-forest and train-track strengthening

The later imported investigation was also treated as candidate mathematics rather than authority. Its main claims were checked against the definitions and retained in the following precise forms.

1. The proposed representative combination is valid after freezing the contact-minimal core and every original diameter endpoint throughout the construction. New unit contacts can be made one at a time and always join distinct current components, so they remain bridges. This gives Theorem 12.4, not the stronger and still unproved assertion that the entire final representative is pinned-jammed.
2. Contracting the frozen core leaves a forest. A direct row count, allowing several fixed roots in one component, gives the lower bound $`u-r+c`$ in Theorem 12.5. Thus the residual obstruction is quantitatively high-dimensional whenever more than boundary-order many vertices lie outside the core.
3. The train-track monotonicity, at-most-one-crossing theorem, triangle-free crossing graph, width inequality, and Cartesian determinant inequality all survive without a disk assumption; the disk hypothesis is used only for the Euler relation in Theorem 10.8 and related boundary classifications.
4. The fixed-two-direction support theorem is valid with the regularity hypotheses stated in Theorem 10.12. In particular, hole-boundary incidences and pinched boundaries cannot be silently ignored.
5. The apparent five-direction escape is geometrically real. Proposition 10.10 realizes the balanced $`C_5`$ blow-up by a unit-separated rhombic disk, so no large Cartesian block follows merely from a dense triangle-free track-crossing graph.

These audits narrow the two branches but do not close either one. The five-sector construction is not certified globally optimal. The 11-point sun following Proposition 10.10 is stronger as a local regression test but is proved not globally optimal by an explicit smaller-diameter lattice competitor.

---

## 4. Exact first-order KKT stress for every minimizer

Let

```math
A=\{p_1,\ldots,p_n\}
```

be any minimizer, and put

```math
T=D(n)^2.
```

Define the active contact and diameter sets

```math
C=\{ij:|p_i-p_j|=1\},\qquad
H=\{ij:|p_i-p_j|^2=T\}.
```

### Theorem 4.1: normalized signed equilibrium stress

There exist multipliers

```math
\alpha_{ij}\ge0\quad(ij\in C),\qquad
\beta_{ij}\ge0\quad(ij\in H)
```

such that

```math
\sum_{ij\in H}\beta_{ij}=1,
\tag{4.1}
```

```math
\sum_{j:ij\in C}\alpha_{ij}(p_i-p_j)
=
\sum_{j:ij\in H}\beta_{ij}(p_i-p_j)
\qquad(i=1,\ldots,n),
\tag{4.2}
```

```math
\sum_{ij\in C}\alpha_{ij}=T,
\tag{4.3}
```

and

```math
\sum_{ij\in C}\alpha_{ij}
(p_i-p_j)(p_i-p_j)^{\mathsf T}
=
\sum_{ij\in H}\beta_{ij}
(p_i-p_j)(p_i-p_j)^{\mathsf T}.
\tag{4.4}
```

Equivalently, if

```math
u_{ij}=p_i-p_j\quad(ij\in C),\qquad
w_{ij}=\frac{p_i-p_j}{D}\quad(ij\in H),
```

then

```math
\boxed{
\sum_{ij\in C}\frac{\alpha_{ij}}{D^2}u_{ij}u_{ij}^{\mathsf T}
=
\sum_{ij\in H}\beta_{ij}w_{ij}w_{ij}^{\mathsf T}.
}
\tag{4.5}
```

Both sides of (4.5) are convex combinations of rank-one projections.

#### Proof

Minimize $`T`$ in the variables $`(p_1,\ldots,p_n,T)`$ subject to

```math
g_{ij}=1-|p_i-p_j|^2\le0,
\qquad
h_{ij}=|p_i-p_j|^2-T\le0.
```

MFCQ holds explicitly. At any feasible point take

```math
v_i=p_i,\qquad \tau=3T.
```

For every active contact,

```math
Dg_{ij}(v)=-2|p_i-p_j|^2=-2<0,
```

and for every active diameter constraint,

```math
Dh_{ij}(v,\tau)=2T-3T=-T<0.
```

Thus ordinary KKT applies. The Lagrangian is

```math
L=T+
\sum_{ij}\alpha_{ij}(1-|p_i-p_j|^2)
+\sum_{ij}\beta_{ij}(|p_i-p_j|^2-T).
```

Stationarity in $`T`$ gives (4.1), while stationarity in every $`p_i`$ gives (4.2).

Multiply (4.2) by $`p_i^{\mathsf T}S`$, sum over $`i`$, and let $`S`$ range over all symmetric $`2\times2`$ matrices. The two endpoint contributions of each edge combine, yielding (4.4). Taking $`S=I`$, using the active lengths, and then using (4.1) gives (4.3). Dividing (4.4) by $`D^2`$ gives (4.5). ∎

With the sign convention of [7], the coefficients

```math
\omega_{ij}=-\alpha_{ij}\quad(ij\in C),\qquad
\omega_{ij}=+\beta_{ij}\quad(ij\in H)
```

form a proper mixed cable-strut equilibrium stress.

---

## 5. Consequences for the positive stress support

Let

```math
C_+=\{ij\in C:\alpha_{ij}>0\},\qquad
H_+=\{ij\in H:\beta_{ij}>0\},
```

and let $`B_+`$ be the vertex set of $`H_+`$.

### Lemma 5.1: diameter endpoints are extreme

Every endpoint of a diameter pair is a vertex of $`\operatorname{conv}A`$.

#### Proof

If $`p_i=\sum_k\lambda_kx_k`$ were a nontrivial convex combination and $`|p_i-p_j|=D`$, then

```math
D=|p_i-p_j|
\le\sum_k\lambda_k|x_k-p_j|
\le D.
```

Equality in the Euclidean triangle inequality would force all vectors $`x_k-p_j`$ occurring with positive coefficient to be the same length-$`D`$ vector, contradicting nontriviality. ∎

### Lemma 5.2: positive diameter load requires positive contact load

Every vertex in $`B_+`$ is incident to an edge of $`C_+`$.

#### Proof

Otherwise (4.2) would express the extreme point $`p_i`$ as a convex combination of its diameter partners. ∎

### Lemma 5.3: unloaded stress vertices are contact barycenters

If $`p_i\notin B_+`$ but is incident to positive contact stress, then

```math
p_i=
\frac{\sum_j\alpha_{ij}p_j}{\sum_j\alpha_{ij}}.
\tag{5.1}
```

Consequently, its $`C_+`$-degree cannot be (1). If its $`C_+`$-degree is (2), its two neighbors are exactly opposite unit contacts, the two stresses agree, and the neighbors are distance (2) apart.

### Proposition 5.4: every stressed contact component is boundary loaded twice

Every nontrivial connected component of $`C_+`$ contains at least two vertices incident to $`H_+`$.

#### Proof

If a component had no $`H_+`$-loaded vertex, choose a direction in which one of its vertices is uniquely extreme. The positive contact forces there all have strictly positive projection in that direction, contradicting equilibrium.

If a component had exactly one loaded vertex $`p_i`$, sum equilibrium over the component. Internal contact forces cancel, leaving

```math
\sum_j\beta_{ij}(p_i-p_j)=0.
```

For any two diameter partners $`p_j,p_k`$,

```math
(p_i-p_j)\cdot(p_i-p_k)
=D^2-\frac{|p_j-p_k|^2}{2}
\ge\frac{D^2}{2}>0.
```

A positive combination of these vectors cannot vanish. ∎

### Proposition 5.5: forest-supported stress

Let $`m=|V(C_+)|`$, let $`c_+`$ be the number of components of $`C_+`$, and let $`L`$ be the unloaded $`C_+`$-degree-(2) vertices. If $`C_+`$ is a forest, then

```math
m-|L|\le2|B_+|-2c_+\le2\pi D-2c_+.
\tag{5.2}
```

Indeed, vertices in $`B_+`$ have degree at least (1), vertices in $`L`$ have degree (2), and all other vertices have degree at least (3). The forest degree sum gives the first inequality. Lemma 5.1, unit-separated hull sides, and Cauchy's perimeter-diameter inequality give

```math
|B_+|\le |V(\operatorname{conv}A)|
\le\operatorname{per}(\operatorname{conv}A)
\le\pi D.
```

In particular, if $`V(C_+)=A`$, $`L=\varnothing`$, and $`C_+`$ is a forest, then

```math
n\le2\pi\sqrt{\frac n{\Delta_2}}-2c_+,
```

which is impossible for $`n\ge40`$.

### Proposition 5.6: cyclic stress components

If the full contact graph is triangle-free, every cyclic component of $`C_+`$ has at least four vertices in $`B_+\cup L`$.

This follows by applying Eppstein's Lemma 2 to that component and then using Lemma 5.3 at every low-degree vertex.

### Exact warning example: the unit square

For the unit square, put weight $`\alpha=1/2`$ on each of the four contact sides and weight $`\beta=1/2`$ on each of the two diameter diagonals. Then

```math
\sum\beta=1,
\qquad
\sum\alpha=2=D(4)^2,
```

and equilibrium holds at every vertex. Thus triangle-free (2)-degeneracy, a normalized positive mixed stress, and exact global optimality are mutually compatible. Any argument asserting that a contact-degree-(2) vertex is automatically movable is already false at $`n=4`$: the diameter cables can supply the missing reactions.

These propositions explain the precise limitation of stress plus (2)-degeneracy: stress may travel through exact straight unit chains, and sparse boundary diameter forces may support a large interior network.

---

## 6. A contact-minimal normal form

Assume that, for a fixed $`n`$, at least one triangle-free minimizer exists. Among all triangle-free minimizers choose $`A^*`$ with the minimum number of unit contacts. Let

```math
Q=\{p_i:\exists j,\ |p_i-p_j|=D(n)\}
```

be the full set of diameter endpoints.

### Theorem 6.1: local trapping after contact minimization

For $`A^*`$:

1. Every non-diameter, nonisolated vertex is strictly surrounded by its unit contacts: its contact vectors positively span $`\mathbb R^2`$.
2. Every such vertex has contact degree (3), (4), or (5).
3. Every nonisolated contact vertex of degree (1) or (2) belongs to $`Q`$.

#### Proof

Let $`p_i\notin Q`$ have at least one contact. If its contact vectors do not positively span the plane, finite-dimensional separation gives a nonzero vector $`w`$ satisfying

```math
(p_i-p_j)\cdot w\ge0
```

for every contact $`ij`$. Move only $`p_i`$:

```math
p_i(t)=p_i+tw.
```

For every old contact,

```math
|p_i(t)-p_j|^2
=1+2t(p_i-p_j)\cdot w+t^2|w|^2>1.
\tag{6.1}
```

The quadratic term handles two exactly opposite contacts: a perpendicular motion has zero first derivative but strictly increases both lengths.

All noncontacts involving $`p_i`$ have positive slack above (1), and because $`p_i\notin Q`$, all its distances have positive slack below $`D`$. Hence, for sufficiently small $`t>0`$, feasibility and diameter $`D`$ are preserved while every contact at $`p_i`$ is broken.

If another contact remains elsewhere, this contradicts contact minimality. If no contact remains, the new minimum distance is $`>1`$, and rescaling produces diameter $`<D(n)`$, contradicting global optimality. Thus the contact vectors positively span the plane.

Positive spanning requires at least three directions. Triangle-freeness gives at most five unit neighbors, because equality in a $`60^\circ`$ angular gap would make a unit triangle, while six gaps strictly larger than $`60^\circ`$ cannot fit around $`360^\circ`$. ∎

### Corollary 6.2: boundary count

Every diameter endpoint is a convex-hull vertex, and

```math
|Q|\le\pi D(n)
\le
\sqrt{2\pi\sqrt3}\,\sqrt n.
\tag{6.2}
```

Write

```math
C_0:=\sqrt{2\pi\sqrt3}=3.298908\ldots.
```

Then $`|Q|\le C_0\sqrt n`$.

### Corollary 6.3: tree components

If $`T`$ is a nontrivial tree contact component and

```math
b_T=|Q\cap V(T)|,
```

then

```math
|V(T)|\le2b_T-2.
\tag{6.3}
```

Therefore all nontrivial tree components together contain $`O(\sqrt n)`$ vertices.

### Corollary 6.4: cyclic components

Every cyclic contact component contains at least four vertices of $`Q`$. Thus there are at most $`|Q|/4=O(\sqrt n)`$ cyclic components.

### Corollary 6.5: cyclomatic number

Let $`z`$ be the number of contact-isolated vertices, $`m=n-z`$, $`e`$ the number of contact edges, and $`c_*`$ the number of nontrivial contact components. Then

```math
e\ge\frac32m-|Q|,
```

and the cyclomatic number

```math
\kappa=e-m+c_*
```

satisfies

```math
\boxed{
\kappa\ge\frac{n-z}{2}-C_0\sqrt n+c_*.
}
\tag{6.4}
```

Thus a contact-minimal triangle-free counterexample is either rattler dominated or has a linear number of independent contact cycles anchored to only $`O(\sqrt n)`$ diameter vertices.

---

## 7. The pinned expansive-cone dichotomy

The strongest framework statement can be proved without invoking any external rigidity theorem.

For a triangle-free minimizer $`A`$, let $`Q`$ be all diameter endpoints and define

```math
\mathcal E_Q(A)=
\left\{
v=(v_i):
v_i=0\ (p_i\in Q),\quad
(p_i-p_j)\cdot(v_i-v_j)\ge0\ (ij\in C)
\right\}.
\tag{7.1}
```

### Theorem 7.1: exact dichotomy

Exactly one of the following holds.

#### Flexible branch

If $`\mathcal E_Q(A)\ne\{0\}`$, then $`A`$ belongs to a nonconstant continuous family of noncongruent triangle-free global minimizers of diameter $`D(n)`$, with all points in $`Q`$ fixed.

#### First-order-jammed branch

If $`\mathcal E_Q(A)=\{0\}`$, let $`e^\circ`$ denote the number of contact edges that do not have both endpoints in $`Q`$. Then the reduced contact rigidity matrix has full column rank and

```math
\boxed{e^\circ\ge2(n-q).}
\tag{7.2}
```

In particular, $`e\ge2(n-q)`$, where $`q=|Q|`$.

#### Proof

If $`v\in\mathcal E_Q(A)\setminus\{0\}`$, take the straight motion

```math
p_i(t)=p_i+tv_i.
```

For each contact,

```math
|p_i(t)-p_j(t)|^2
=1+2t(p_i-p_j)\cdot(v_i-v_j)
+t^2|v_i-v_j|^2\ge1.
```

Every active diameter pair has both endpoints fixed. All initially noncontact and nondiameter pairs have strict slack, so sufficiently small $`t`$ preserves feasibility, diameter $`D`$, and triangle-freeness. Because two distinct diameter endpoints are fixed, a nonzero continuous motion cannot be a nontrivial Euclidean congruence.

If the cone is zero, any vector in the kernel of the reduced contact rigidity matrix would belong to the cone together with its negative. Hence the kernel is zero and the matrix has rank $`2(n-q)`$. A contact joining two pinned vertices gives a zero row, so only the $`e^\circ`$ remaining rows can contribute to this rank. This proves (7.2). ∎

### Lemma 7.2: direct local witnesses for the flexible branch

The following statements hold for every minimizer $`A`$.

1. If a convex-hull vertex $`p`$ is not in $`Q`$, then $`\mathcal E_Q(A)\ne\{0\}`$.
2. If a vertex $`p\notin Q`$ has contact degree at most $`2`$, then $`\mathcal E_Q(A)\ne\{0\}`$.

Consequently, in the first-order-jammed triangle-free branch,

```math
\boxed{Q=V(\operatorname{conv}A)}
\tag{7.3}
```

and every vertex outside $`Q`$ has contact degree $`3`$, $`4`$, or $`5`$. In particular, every contact-isolated vertex belongs to $`Q`$.

#### Proof

For the first statement, choose a strict supporting normal $`u`$ at the hull vertex $`p`$, so

```math
u\cdot(p-x)>0\qquad(x\in A\setminus\{p\}).
```

Moving only $`p`$ with velocity $`u`$ strictly expands every incident contact. Because $`p\notin Q`$, all distances from $`p`$ have strict slack below $`D`$, while a diameter pair not using $`p`$ remains fixed. Thus this velocity lies in the pinned expansive cone and produces the same-diameter flex of Theorem 7.1. Lemma 5.1 gives the reverse inclusion $`Q\subseteq V(\operatorname{conv}A)`$, proving (7.3) in the zero-cone branch.

For the second statement, degree $`0`$ is immediate. At degree $`1`$, move $`p`$ perpendicular to its unique contact direction; that contact expands quadratically. At degree $`2`$, let $`a,b`$ be the two unit vectors from the neighbors toward $`p`$. If $`a\ne-b`$, the velocity $`w=a+b`$ satisfies

```math
a\cdot w=b\cdot w=1+a\cdot b>0.
```

If $`a=-b`$, move perpendicular to them and both contacts expand quadratically. Since $`p\notin Q`$, all upper constraints incident to it have slack. Triangle-freeness supplies the upper degree bound $`5`$. ∎

### Corollary 7.3: cycle count and size of the diameter boundary

Let $`c`$ be the number of contact-graph components and

```math
\kappa=e-n+c
```

its cyclomatic number. In the first-order-jammed branch,

```math
\boxed{
\kappa\ge n-2q+c
\ge n-2\sqrt{2\pi\sqrt3}\,\sqrt n+1.
}
\tag{7.4}
```

Thus

```math
\kappa\ge n-6.597816\ldots\sqrt n+1,
```

and in particular $`\kappa=n-O(\sqrt n)`$.

Eppstein's bound (2.4) and (7.2) imply

```math
q\ge\frac14\sqrt{2\pi\sqrt3\,n}-O(1)
=0.824727\ldots\sqrt n-O(1).
\tag{7.5}
```

Together with (6.2),

```math
q=\Theta(\sqrt n),\qquad e=2n-\Theta(\sqrt n).
\tag{7.6}
```

If the contact graph is connected, (2.3) yields

```math
q\ge\frac{d_G+2}{2}
\ge\frac{D(n)+2}{2}
\ge\frac12\left(\sqrt{\frac n{\Delta_2}}+1\right),
\tag{7.7}
```

where the last step uses the sharper planar lower bound (2.2).

---

## 8. Strict pinned stress and interior trapping

Lemma 7.2 already identifies the hull geometrically. Cone duality gives additional exact information: every unpinned vertex is strictly trapped by a positive stress on every incident contact. This replaces the imported reliance on an all-strut theorem that is only quoted, not proved, in [7].

### Lemma 8.1: strict positive dependence from a zero expansive cone

Let $`R`$ be a real matrix. If

```math
\{x:Rx\ge0\}=\{0\},
\tag{8.1}
```

then $`R`$ has full column rank and there exists a vector $`c`$ with every coordinate strictly positive such that

```math
R^{\mathsf T}c=0.
\tag{8.2}
```

#### Proof

The kernel is zero because both $`x`$ and $`-x`$ satisfy $`Rx=0`$. Let $`r_1,\ldots,r_e`$ be the rows. Condition (8.1) says that the dual cone of $`\operatorname{pos}\{r_1,\ldots,r_e\}`$ is $`{0}`$, hence the positive hull of the rows is the full column space.

For every nonzero row $`r_i`$, express $`-r_i`$ as a nonnegative combination of the rows. This produces a nonnegative linear dependence with a positive coefficient on $`r_i`$. Summing these dependences over $`i`$, and assigning arbitrary positive coefficients to any zero rows, gives (8.2) with $`c_i>0`$ for every $`i`$. ∎

### Theorem 8.2: strict positive pinned stress and local trapping

Assume $`\mathcal E_Q(A)=\{0\}`$. Then:

1. Every contact edge admits a strictly positive pinned equilibrium stress.
2. At every unpinned vertex $`p_i\notin Q`$,

   ```math
   \sum_{j\sim i}c_{ij}(p_j-p_i)=0,
   \qquad c_{ij}>0.
   \tag{8.3}
   
   ```

3. The contact neighbors of every unpinned vertex affinely span the plane.
4. Every unpinned vertex lies in the strict interior of the convex hull of its contact neighbors and has contact degree at least (3).
5. The diameter endpoints are exactly the convex-hull vertices:

   ```math
   \boxed{Q=V(\operatorname{conv}A).}
   \tag{8.4}
   
   ```

#### Proof

Apply Lemma 8.1 to the reduced contact rigidity matrix whose columns correspond to unpinned coordinates. Equation (8.2) is exactly (8.3). It first places $`p_i`$ in the affine hull of its contact neighbors. If those neighbors failed to span the plane, they and $`p_i`$ would lie on one line, and moving only $`p_i`$ perpendicular to that line would give a nonzero vector in the kernel of the reduced matrix, contrary to full column rank. Thus the neighbors affinely span the plane, and the positive equilibrium relation makes $`p_i`$ a strict convex combination of them.

No equilibrium equation is asserted at a pinned vertex; the missing force there is the pin reaction. Contacts joining two pinned vertices give zero rows in the reduced matrix and may be assigned arbitrary positive coefficients without affecting the unpinned equations.

An unpinned point therefore cannot be extreme in $`\operatorname{conv}A`$. Hence every hull vertex lies in $`Q`$. Lemma 5.1 gives the reverse inclusion, consistently with the direct proof in Lemma 7.2. ∎

Under the triangle-free hypothesis, every unpinned vertex consequently has degree (3), (4), or (5).

This theorem is stronger than the earlier estimate $`Q\subseteq V(\operatorname{conv}A)`$: in the first-order-jammed branch, **all** hull vertices are diameter endpoints.

---

## 9. The forest exclusion and boundary anchoring

### Proposition 9.1: component anchoring in every jammed counterexample

In the first-order-jammed triangle-free branch:

1. If $`T`$ is a nontrivial tree contact component with $`n_T`$ vertices and $`q_T=|Q\cap V(T)|`$, then

   ```math
   \boxed{n_T\le2q_T-2.}
   \tag{9.1}
   
   ```

2. All nontrivial tree components together contain at most $`2q=O(\sqrt n)`$ vertices.
3. Every cyclic contact component contains at least four diameter endpoints.
4. Every isolated contact vertex is a diameter endpoint.

#### Proof

Every non-$`Q`$ vertex has degree at least $`3`$ by Lemma 7.2, while every vertex of a nontrivial tree has degree at least $`1`$. Therefore

```math
2(n_T-1)
=\sum_{v\in T}\deg v
\ge3(n_T-q_T)+q_T,
```

which gives (9.1). Sum over the tree components. For a cyclic component, Eppstein's Lemma 2 supplies four non-articulation vertices of degree at most $`2`$; Lemma 7.2 puts all four in $`Q`$. Its degree-$`0`$ case also proves the last assertion. ∎

### Corollary 9.2: no forest for $`n\ge44`$

If $`A`$ is a triangle-free minimizer in the first-order-jammed branch and $`n\ge44`$, then its contact graph is not a forest.

#### Proof

Let $`h=|Q|`$, which equals the number of hull vertices by (8.4). Let $`U`$ be the unpinned vertices, $`Q'\subseteq Q`$ the nonisolated pinned vertices, and $`c`$ the number of nontrivial forest components.

Every vertex in $`U`$ has degree at least (3), and every vertex in $`Q'`$ has degree at least (1). Since a forest on $`|U|+|Q'|`$ nonisolated vertices with $`c`$ components has $`|U|+|Q'|-c`$ edges,

```math
2(|U|+|Q'|-c)
\ge3|U|+|Q'|.
```

Thus

```math
|U|\le|Q'|-2c,
```

and therefore

```math
n=|U|+h\le2h.
\tag{9.2}
```

Every hull side has length at least (1), while Cauchy's inequality gives

```math
h\le\operatorname{per}(\operatorname{conv}A)
\le\pi D(n).
```

Using the upper bound in (2.2),

```math
n\le2\pi\sqrt{\frac n{\Delta_2}},
```

so

```math
n\le\frac{4\pi^2}{\Delta_2}=8\pi\sqrt3=43.531\ldots.
```

Hence $`n\ge44`$ is impossible. ∎

### Corollary 9.3: four low-degree diametral hull vertices

For $`n\ge44`$, every triangle-free minimizer in the first-order-jammed branch has a cyclic contact component. Eppstein's Lemma 2 supplies at least four non-articulation vertices of contact degree at most (2) in that component. Lemma 7.2 forces all four to be diameter endpoints on the convex hull.

Thus a hypothetical large jammed counterexample must simultaneously have:

- every hull vertex diametral;
- every interior vertex strictly surrounded by at least three contacts;
- at least four hull vertices of contact degree at most (2); and
- $`\Theta(\sqrt n)`$ hull/diameter vertices in total.

---

## 10. The almost-rhombic structure theorem

Continue in the triangle-free first-order-jammed branch. Let $`e`$ be the number of contact edges, $`c`$ the number of contact-graph components, and $`k`$ the number of edge incidences with the unbounded face.

Euler's formula gives the number of bounded faces:

```math
f_b=e-n+c.
\tag{10.1}
```

Every bounded face has length at least (4). Define its total excess over quadrilateral length by

```math
X=\sum_{F\text{ bounded}}(|\partial F|-4).
```

Counting edge-face incidences gives

```math
X=2e-k-4f_b=4n-2e-k-4c.
\tag{10.2}
```

Using $`e\ge2(n-q)`$,

```math
0\le X\le4q-k-4c\le4q.
\tag{10.3}
```

Let $`F_4`$ be the number of bounded faces of length (4). Since every other bounded face contributes at least (1) to $`X`$,

```math
F_4\ge f_b-X
=3e-5n+k+5c
\ge n-6q+k+5c.
\tag{10.4}
```

In particular,

```math
F_4=n-O(\sqrt n).
\tag{10.5}
```

### Lemma 10.1: geometry of a four-face

Every bounded four-face is a simple unit rhombus. If $`\theta_F\in(0,\pi/2]`$ is its acute angle, then

```math
\boxed{
\frac\pi3<\theta_F\le\frac\pi2.
}
\tag{10.6}
```

Indeed, the short diagonal has length $`2\sin(\theta_F/2)\ge1`$. Equality would add the short diagonal as a unit contact and form unit equilateral triangles. Therefore equality is forbidden in a triangle-free contact graph.

The face area is

```math
\operatorname{area}(F)=\sin\theta_F>\frac{\sqrt3}{2}.
\tag{10.7}
```

### Theorem 10.2: total rhombus defect

Define

```math
\eta_F=\sin\theta_F-\frac{\sqrt3}{2}>0.
```

Then

```math
\boxed{
\sum_{F\in\mathcal F_4}\eta_F
\le
\frac{\sqrt3}{2}(n-F_4)
\le
\frac{\sqrt3}{2}(6q-k-5c).
}
\tag{10.8}
```

#### Proof

The bounded contact faces have disjoint interiors and lie in $`\operatorname{conv}A`$. Therefore

```math
\sum_{F\in\mathcal F_4}\operatorname{area}(F)
\le\operatorname{area}(\operatorname{conv}A).
```

The isodiametric inequality and the BHS upper bound give

```math
\operatorname{area}(\operatorname{conv}A)
\le\frac{\pi D^2}{4}
\le\frac\pi4\frac n{\Delta_2}
=\frac{\sqrt3}{2}n.
```

Substitute (10.7) and then use (10.4). ∎

### Corollary 10.3: almost every rhombus is nearly equilateral

For fixed $`0<\varepsilon\le\pi/6`$, the number $`N_\varepsilon`$ of four-faces satisfying

```math
\theta_F\ge\frac\pi3+\varepsilon
```

obeys

```math
N_\varepsilon
\le
\frac{(\sqrt3/2)(6q-k-5c)}
{\sin(\pi/3+\varepsilon)-\sqrt3/2}
=O_\varepsilon(\sqrt n).
\tag{10.9}
```

Hence all but $`O_\varepsilon(\sqrt n)`$ bounded faces have acute angle in

```math
60^\circ<\theta_F<60^\circ+\varepsilon.
```

### Corollary 10.4: total angular excess is boundary order

Put

```math
\delta_F=\theta_F-\frac\pi3\in(0,\pi/6].
```

The concave function

```math
f(\delta)=\sin\left(\frac\pi3+\delta\right)-\frac{\sqrt3}{2}
```

lies above the chord joining its endpoint values on $`[0,\pi/6]`$. Hence

```math
f(\delta)
\ge
\frac6\pi\left(1-\frac{\sqrt3}{2}\right)\delta.
```

Together with (10.8), this gives the explicit estimate

```math
\boxed{
\sum_{F\in\mathcal F_4}
\left(\theta_F-\frac\pi3\right)
\le
\frac{\pi\sqrt3}{12(1-\sqrt3/2)}(6q-k-5c)
=O(\sqrt n).
}
\tag{10.10}
```

Since $`F_4=n-O(\sqrt n)`$, the mean angular excess is $`O(n^{-1/2})`$.

### Corollary 10.5: almost every vertex has degree four

Only $`O(q)`$ vertices are isolated, lie on the unbounded contact face, or are incident to a nonquadrilateral bounded face. Every other vertex is surrounded by rhombi whose angles lie strictly between $`60^\circ`$ and $`120^\circ`$, so its degree is (4) or (5).

Moreover,

```math
0\le\sum_v(4-\deg v)=4n-2e\le4q.
```

The left inequality follows, for example, from Eppstein's (2)-degeneracy bound $`e\le2n-3`$ on every nonempty graph with at least two vertices. Let $`E_0`$ be the exceptional vertex set and let $`N_5`$ count the nonexceptional degree-(5) vertices. The nonexceptional vertices have degree (4) or (5), while triangle-freeness gives degree at most (5) everywhere. Hence

```math
0\le \sum_{v\in E_0}(4-\deg v)-N_5
\le 4|E_0|-N_5,
```

so $`N_5\le4|E_0|=O(q)`$. Consequently,

```math
\boxed{
\text{all but }O(\sqrt n)\text{ vertices have degree }4
\text{ and are incident only with unit-rhombus faces.}
}
\tag{10.11}
```

For each fixed $`\varepsilon>0`$, excluding also the vertices incident to the $`O_\varepsilon(\sqrt n)`$ exceptional rhombi in Corollary 10.3 shows that all but $`O_\varepsilon(\sqrt n)`$ vertices are surrounded by rhombi whose acute angles lie between $`60^\circ`$ and $`60^\circ+\varepsilon`$.

The estimate remains asymptotic. It does not force any exact equality $`\theta_F=60^\circ`$.

### Theorem 10.6: exact train-track bounds

Let $`\mathcal R`$ be any finite collection of the bounded four-faces from Lemma 10.1, regarded as an edge-to-edge rhombic complex. It may be disconnected and may have holes. Write

```math
R=|\mathcal R|
```

and let $`B_{\mathcal R}`$ be the number of contact edges incident to exactly one face of $`\mathcal R`$.

Declare opposite edges of a rhombus equivalent and take the transitive closure. The resulting equivalence classes are the **train tracks** of $`\mathcal R`$. If $`T`$ is their number, then

```math
\boxed{
B_{\mathcal R}=2T,
\qquad
R\le \frac{T^2}{4}=\frac{B_{\mathcal R}^2}{16}.
}
\tag{10.12}
```

Consequently,

```math
\boxed{B_{\mathcal R}\ge4\sqrt R.}
\tag{10.13}
```

#### Proof

All edges belonging to one track are parallel. Orient a unit vector $`u`$ along them and draw the track centerline by joining midpoints of opposite track edges across each rhombus. Orient this centerline so that

```math
h_u(x)=\det(u,x)
```

increases. It increases strictly across every rhombus. At a shared edge the next rhombus lies on the other side, so the same orientation continues. A track therefore cannot close or self-intersect. Since the complex is finite, it is a path with two boundary edges. Conversely, every boundary edge ends exactly one track. Hence $`B_{\mathcal R}=2T`$.

Two tracks can cross only in a rhombus, and they cross at most once. Here the strict angle bound is essential. Every directed segment of the $`u`$-track has angle from $`u`$ in

```math
\left(\frac\pi3,\frac{2\pi}3\right).
\tag{10.14}
```

Therefore every forward displacement along it belongs to the open convex cone $`C_u`$ with that angular interval. If a $`v`$-track crosses it, orient $`v`$ so that its direction at the crossing belongs to $`C_u`$, and write $`\phi=\arg_u v`$. Then

```math
\frac\pi3<\phi<\frac{2\pi}3,
```

while the forward-displacement cone of the $`v`$-track has angular interval

```math
\left(\phi+\frac\pi3,\phi+\frac{2\pi}3\right).
```

This interval is disjoint from both $`C_u`$ and $`-C_u`$. If the tracks crossed at two points $`P,Q`$, label them so that $`Q-P`$ is a forward displacement on the $`v`$-track. According to their order on the $`u`$-track, the same vector would lie in $`C_u`$ or $`-C_u`$, a contradiction. This argument does not use simple connectedness.

Form the graph whose vertices are tracks and whose edges are their crossings. It is simple by the preceding paragraph. It is triangle-free: three pairwise crossing tracks would give three points on the projective direction circle, of circumference $`\pi`$, whose three pairwise circular separations were all strictly greater than $`\pi/3`$. The three circular gaps cannot then sum to $`\pi`$.

Mantel's inequality gives at most $`T^2/4`$ crossing pairs. Every rhombus is one crossing, proving (10.12) and (10.13). ∎

### Corollary 10.7: almost every track enters the defect network

Return to the jammed hypotheses, and take $`\mathcal R=\mathcal F_4`$. Let $`h_{\mathcal R}`$ count its boundary edges lying on $`\partial\operatorname{conv}A`$, and put

```math
b_{\mathcal R}=B_{\mathcal R}-h_{\mathcal R}.
```

At most two train tracks have both end edges on the convex hull. Therefore

```math
\boxed{
b_{\mathcal R}
\ge \frac{B_{\mathcal R}}2-2
\ge2\sqrt{F_4}-2
=2\sqrt n-O(1).
}
\tag{10.15}
```

Also $`h_{\mathcal R}\le q`$, and hence

```math
b_{\mathcal R}\ge4\sqrt{F_4}-q.
\tag{10.16}
```

Every edge counted by $`b_{\mathcal R}`$ either borders a bounded nonquadrilateral face or lies on a non-hull boundary component or indentation of the rhombic complex.

#### Proof

Theorem 8.2 makes every point of $`A`$ on the convex hull an extreme vertex, so directed hull-edge angles turn strictly. A directed track centerline enters the rhombic complex through one end edge and leaves through the other; the two parallel end edges consequently have opposite induced boundary orientations. Strict turning also means that two different hull-to-hull tracks cannot use the same unoriented direction. Thus the end edges of any two such tracks alternate in the cyclic hull order. Their centerlines are arcs in the convex disk with alternating endpoints and must cross. The crossing graph induced by hull-to-hull tracks is therefore complete; Theorem 10.6 makes it triangle-free, so it has at most two vertices.

Every remaining track supplies at least one non-hull end edge. This proves (10.15). A hull contact edge joins consecutive hull vertices, so there are at most $`q`$ such edges; (10.13) now gives (10.16). ∎

There is also an exact convex exception theorem. If the closed strict rhombi tile a convex polygon and every boundary vertex is extreme, then every track is hull-to-hull, so the preceding proof leaves two tracks and one crossing: the complex is one rhombus. Under the jammed hypotheses, if the rhombi tile all of $`\operatorname{conv}A`$, all four vertices of that rhombus belong to $`Q`$. A nonsquare rhombus has only the endpoints of its longer diagonal in $`Q`$, so the rhombus must be the unit square.

For comparison with the planar excess variables, if $`s`$ is the number of bounded nonquadrilateral faces, then

```math
B_{\mathcal R}
\le k+\sum_{F\notin\mathcal R}|\partial F|
=k+4s+X
\le k+5X
\le20q-4k-20c.
\tag{10.17}
```

Thus (10.15) is a real boundary-order demand, but the existing face-excess budget is still large enough to absorb it.

### Theorem 10.8: track width and exact angular-defect charge

Let

```math
D_{\mathcal R}=\operatorname{diam}V(\mathcal R),
\qquad
\chi_*=\frac{6-3\sqrt3}{\pi}.
```

Then, with no connectedness or disk assumption,

```math
\boxed{
B_{\mathcal R}D_{\mathcal R}
\ge4\sum_{F\in\mathcal R}\sin\theta_F
\ge2\sqrt3R+4\chi_*\sum_{F\in\mathcal R}\delta_F.
}
\tag{10.18}
```

If $`\mathcal R`$ is a topological disk and $`v=|V(\mathcal R)|`$, then

```math
v=R+\frac{B_{\mathcal R}}2+1
```

and

```math
\boxed{
v\ge R+2\sqrt R+1=(\sqrt R+1)^2,
\qquad
R\le(\sqrt v-1)^2.
}
\tag{10.19}
```

#### Proof

Across a rhombus $`F`$, the increase of the track coordinate $`h_u`$ in the proof of Theorem 10.6 is exactly $`\sin\theta_F`$. The two endpoint midpoints lie in $`\operatorname{conv}V(\mathcal R)`$, so every track $`\tau`$ satisfies

```math
\sum_{F\in\tau}\sin\theta_F\le D_{\mathcal R}.
```

There are $`B_{\mathcal R}/2`$ tracks and every rhombus belongs to two of them. This proves the first inequality in (10.18). Concavity of sine on $`[\pi/3,\pi/2]`$ gives the chord estimate

```math
\sin\left(\frac\pi3+\delta\right)
\ge\frac{\sqrt3}{2}+\chi_*\delta,
```

which proves the second.

For a disk quadrangulation, Euler and edge-face incidence counting give

```math
v-e+R=1,
\qquad
4R=2e-B_{\mathcal R}.
```

Eliminate $`e`$ and use (10.13) to obtain (10.19). ∎

### Theorem 10.9: a global restriction on Cartesian train grids

Suppose a rhombic complex contains an additive $`a\times b`$ train-grid block with vertices

```math
p_{ij}=p+x_i+y_j,
\qquad
0\le i\le a,\qquad 0\le j\le b,
```

where

```math
u_i=x_i-x_{i-1},\quad |u_i|=1,
\qquad
v_j=y_j-y_{j-1},\quad |v_j|=1,
```

and all cell orientations are consistent:

```math
\det(u_i,v_j)=\sin\theta_{ij}>0.
```

Then

```math
\boxed{
D_{\mathcal R}^2
\ge2\sum_{i=1}^a\sum_{j=1}^b\sin\theta_{ij}
\ge\sqrt3ab+2\chi_*\Delta_{a,b},
}
\tag{10.20}
```

where $`\Delta_{a,b}=\sum_{i,j}(\theta_{ij}-\pi/3)`$. Moreover, for every $`n`$,

```math
\boxed{D(n)^2<\frac{2\sqrt3}{\pi}n.}
\tag{10.21}
```

Consequently every such block in an $`n`$-point global minimizer obeys

```math
\boxed{
ab+\frac{4\sqrt3-6}{\pi}\Delta_{a,b}
<\frac2\pi n.
}
\tag{10.22}
```

In particular $`ab<2n/\pi`$.

#### Proof

Put $`U=\sum_i u_i`$ and $`V=\sum_jv_j`$. The block contains

```math
p,\qquad p+U,\qquad p+V,\qquad p+U+V,
```

and

```math
\det(U,V)=\sum_{i,j}\sin\theta_{ij}.
```

Both $`U+V`$ and $`U-V`$ are differences of block vertices. Hence

```math
2|\det(U,V)|
=|\det(U+V,U-V)|
\le|U+V|\,|U-V|
\le D_{\mathcal R}^2.
```

This proves (10.20).

For (10.21), average the number of points of the unit triangular lattice in an **open** radius-$`r`$ disk over translations modulo a fundamental cell. The average is

```math
\frac{\pi r^2}{\sqrt3/2}.
```

Choose $`r`$ so that this average is $`n`$. Some translate contains at least $`n`$ lattice points. Any chosen $`n`$ of them form a finite subset of the open disk and therefore have diameter strictly less than $`2r`$. This proves (10.21). Combining it with (10.20), and using

```math
\frac{2\chi_*}{\sqrt3}=\frac{4\sqrt3-6}{\pi},
```

gives (10.22). ∎

The additive block hypothesis is substantive. A dense triangle-free train-crossing graph need not contain a Cartesian block holding a comparable fraction of all its crossings.

### Proposition 10.10: a five-sector boundary-pinned countermodel

The local train-track, defect, stress, and pinned-jamming conclusions still do not use the decisive diametral-hull condition.

Fix $`s\ge2`$ and $`0<\varepsilon<\pi/24`$. Choose unit vectors $`w_0,\ldots,w_4`$ in counterclockwise order with successive oriented gaps

```math
\gamma_0=\gamma_1=\gamma_2=\gamma_3
=\frac\pi3+\varepsilon,
\qquad
\gamma_4=\frac{2\pi}3-4\varepsilon,
```

where $`w_5=w_0`$. Define

```math
S_{s,\varepsilon}
=\bigcup_{i\in\mathbb Z/5\mathbb Z}
\left\{aw_i+bw_{i+1}:0\le a,b\le s, a,b\in\mathbb Z\right\}.
\tag{10.23}
```

The five sector grids meet along their radial sides. Their union is an edge-to-edge disk complex with

```math
\boxed{
n=5s^2+5s+1,
\qquad
R=5s^2,
\qquad
B_{\mathcal R}=10s.
}
\tag{10.24}
```

Its $`T=5s`$ tracks fall into five classes of size $`s`$, one for each direction $`w_i`$. Every track crosses precisely the tracks in the two adjacent direction classes. Thus the crossing graph is the balanced blow-up of $`C_5`$. Its largest complete bipartite subgraph contains only

```math
2s^2=\frac{2R}{5}
```

crossings.

Four sectors have rhombus defect $`\varepsilon`$ and the fifth has defect $`4\varepsilon`$, so

```math
\boxed{
\sum_F\delta_F=8\varepsilon s^2.
}
\tag{10.25}
```

The vertex set is unit-separated, its contact graph consists exactly of the grid edges, and it is triangle-free. All but $`O(s)`$ vertices have degree four, and its diameter is $`O(s)=O(\sqrt n)`$.

If every vertex on the boundary of this five-sector complex is pinned, its expansive cone is zero and it admits a stress positive on every contact edge. In particular, choosing

```math
\varepsilon_s=s^{-3}
```

gives arbitrarily large, triangle-free, boundary-pinned jammed complexes with

```math
R=n-O(\sqrt n),
\qquad
\sum_F\delta_F=\frac8s=o(1).
\tag{10.26}
```

#### Proof

Within one sector, the difference of two vertices is $`aw_i+bw_{i+1}`$ with integers $`a,b`$. Let $`\gamma\in(\pi/3,2\pi/3)`$ be the oriented angle between the two generators. If $`ab\ge0`$ and both coefficients are nonzero, the shortest case is their unit sum and has squared length $`2+2\cos\gamma>1`$. If $`ab<0`$ and $`\cos\gamma>0`$, writing $`r=|a|`$ and $`t=|b|`$ gives

```math
r^2+t^2-2rt\cos\gamma
=(r-t)^2+2rt(1-\cos\gamma)>1.
```

The case $`\cos\gamma\le0`$ is immediate. Equality therefore occurs only for a coordinate unit vector.

For adjacent sectors, points off their shared radial ray lie on opposite sides of it, each at perpendicular distance at least $`\sin(\pi/3)`$; if one point lies on the ray, the same two-generator calculation applies. Two nonadjacent sector cones are separated by an angle $`\alpha>\pi/3`$. Their nonzero lattice points have norms $`r,t\ge1`$, and

```math
|x-y|^2=(r-t)^2+2rt(1-\cos\alpha)>1.
```

This proves unit separation and identifies all contacts. The five sector cones have disjoint interiors, so their rhombi do not overlap. Gluing five $`(s+1)\times(s+1)`$ grids along their radial chains gives (10.24), and (10.25) is immediate.

Across a radial seam, the $`s`$ half-tracks of direction $`w_i`$ in its two adjacent sectors join pairwise. Hence there are exactly $`s`$ complete tracks in each of the five direction classes. A class-$`i`$ track crosses all $`s`$ tracks in classes $`i-1`$ and $`i+1`$ and no others. This proves the asserted balanced $`C_5`$ crossing graph. In a $`C_5`$ blow-up, a complete bipartite subgraph is maximized by taking one full class on one side and its two neighboring classes on the other, giving $`2s^2`$ crossings.

To see full rank after the outer boundary is pinned, first consider a contact-preserving infinitesimal motion. In each sector the vertex $`(s-1)w_i+(s-1)w_{i+1}`$ has two nonparallel contacts to pinned outer-side vertices, so its velocity is zero. The same two-direction argument fixes the rest of the layer $`\max\{a,b\}=s-1`$. Induction on the layers fixes the whole complex.

It remains to construct a positive pinned equilibrium stress. At the radial seam in direction $`w_i`$, the vector $`w_i`$ lies strictly inside the cone generated by $`w_{i-1}`$ and $`w_{i+1}`$, because

```math
\gamma_{i-1}+\gamma_i<\pi.
```

Choose positive $`a_i^-,a_i^+,\lambda_i`$ such that

```math
a_i^-w_{i-1}+a_i^+w_{i+1}=\lambda_iw_i.
\tag{10.27}
```

Give every off-seam grid line ending at that seam its corresponding weight $`a_i^-`$ or $`a_i^+`$. Opposite edges then cancel at every ordinary grid vertex. Give the radial edge from $`rw_i`$ to $`(r+1)w_i`$ weight $`\rho_{i,r}`$. At an internal seam vertex equilibrium is exactly

```math
\rho_{i,r-1}=\rho_{i,r}+\lambda_i.
\tag{10.28}
```

Because the five rays surround the origin with every gap less than $`\pi`$, there are $`d_i>0`$ with $`\sum_i d_iw_i=0`$. Scale them until $`d_i>s\lambda_i`$, put $`\rho_{i,0}=d_i`$, and define $`\rho_{i,r}=d_i-r\lambda_i`$. All weights are positive, (10.28) holds, and the center is in equilibrium.

For an expansive velocity pinned on the boundary, multiply every contact inequality by this positive stress and sum. Interior equilibrium makes the sum zero, so every contact derivative is zero. The full-rank argument in the preceding paragraph then makes the velocity zero. ∎

There is also a useful exact finite regression test in which the pins really are the diameter endpoints. Let $`w_0,\ldots,w_4`$ be the five unit vectors at successive angles $`2\pi/5`$ and take

```math
S=\{0\}\cup\{w_i:0\le i<5\}
\cup\{w_i+w_{i+1}:0\le i<5\}.
\tag{10.27a}
```

This is an 11-point, triangle-free union of five $`72^\circ`$ unit rhombi. Its five outer points $`w_i+w_{i+1}`$ form a regular pentagon, are exactly the convex-hull vertices, and every one is a diameter endpoint. Pinning only these five points gives zero expansive cone. Indeed, at each radial point $`w_i`$, its two contacts to the pinned hull have directions $`w_{i-1}`$ and $`w_{i+1}`$; a positive stress with weight (1) on those edges and weight $`2\cos(2\pi/5)`$ on the edge to the center is in equilibrium. The five center-edge forces sum to zero. Positivity turns every expansive derivative into an equality, the two nonparallel pinned contacts fix each $`w_i`$, and the radial contacts then fix the center.

For an exact distance check, put $`\varphi=(1+\sqrt5)/2`$ and $`z_i=w_i+w_{i+1}`$. Then $`|z_i|=\varphi`$, the inner pentagon has side length $`2\sin(\pi/5)>1`$, and every outer-pentagon side is also longer than (1). Rotational symmetry reduces the mixed distances to

```math
|z_j-w_i|^2=
\begin{cases}
1,&j-i\equiv0,-1\pmod5,\\[2mm]
(7+\sqrt5)/2,&j-i\equiv1,3\pmod5,\\[2mm]
(7+3\sqrt5)/2,&j-i\equiv2\pmod5.
\end{cases}
```

Thus the displayed edges are exactly all unit contacts. The outer pentagon has inradius $`\varphi^2/2>1`$, so it contains the five $`w_i`$ strictly. Its diagonals are the unique longest distance class and have squared length $`5+2\sqrt5`$. This verifies the hull and diameter assertions.

Thus even the exact conditions $`Q=V(\operatorname{conv}A)`$, positive pinned stress, zero pinned cone, and strict rhombic faces do not force a $`60^\circ`$ face at finite size. Its diameter is

```math
\sqrt{5+2\sqrt5}>3,
```

whereas the unit triangular lattice contains the following 12-point set of diameter (3):

```math
\{(a,b):
(a,b)\in
\{(0,1),(0,2),(0,3),(1,0),(1,1),(1,2),(1,3),
(2,0),(2,1),(2,2),(3,0),(3,1)\}\},
\tag{10.27b}
```

where $`(a,b)`$ denotes $`a(1,0)+b(1/2,\sqrt3/2)`$. For every nonzero integer difference, $`a^2+ab+b^2\ge1`$, while a direct check of the finitely many displayed differences gives $`a^2+ab+b^2\le9`$, with equality for $`(0,1)`$ and $`(3,1)`$. Thus the set is unit-separated and has diameter (3). Any 11 of these points beat the sun. The sun is therefore an exact adversarial test of local arguments, not a candidate for Target C.

The large five-sector family is an exact warning. It defeats any proposed quantization of positive rhombus defect, any maximum principle based only on a pinned boundary, and any argument using only positive equilibrium stress. What that large family does **not** satisfy is Theorem 8.2: most pinned boundary points are nonextreme and nondiametral. The 11-point sun shows in turn that the diametral-hull condition alone is not a finite local contradiction. Global capacity, or an equivalent large-scale extremality input, remains indispensable.

### Corollary 10.11: the exact ideal-disk boundary budget

Suppose an $`n`$-point global minimizer is exactly the vertex set of a topological-disk rhombic complex $`\mathcal R`$. Put

```math
G=\operatorname{area}(\operatorname{conv}A)
-\sum_{F\in\mathcal R}\operatorname{area}(F),
\qquad
\Delta=\sum_F\delta_F.
```

Then

```math
\boxed{
4G+4\chi_*\Delta
<\sqrt3B_{\mathcal R}+2\sqrt3.
}
\tag{10.29}
```

Indeed, Theorem 10.8 gives $`n=R+B_{\mathcal R}/2+1`$, while (10.21), the isodiametric inequality, and the sine chord estimate give

```math
\frac{\sqrt3}{2}R+\chi_*\Delta+G
\le\operatorname{area}(\operatorname{conv}A)
<\frac{\sqrt3}{2}n.
```

Thus a reverse boundary-shell inequality, with exact correction terms for exceptional faces, holes, components, and vertices outside the rhombic core, would eliminate the jammed branch. Proposition 10.10 proves that no such reverse inequality follows from strict defects, positive stress, and boundary-pinned jamming alone.

### Theorem 10.12: support cost and classification for two fixed directions

Let $`\mathcal R`$ be a connected finite unit-rhombus complex whose cell union has a simple outer boundary, with holes allowed but no pinched boundary vertices. Assume all edges use two fixed unoriented directions. Let $`K_\partial`$ consist of all hole-boundary incidences together with selected outer-boundary incidences only at vertices that are not vertices of $`\operatorname{conv}V(\mathcal R)`$, chosen so that:

1. every incidence on a hole boundary belongs to $`K_\partial`$; and
2. every outer-boundary vertex that is not a vertex of $`\operatorname{conv}V(\mathcal R)`$ and is uncharged admits a strictly positive equilibrium using only the incident edges of $`\mathcal R`$.

Thus any non-hull vertex that needs a contact outside $`\mathcal R`$ or another external reaction must be charged to $`K_\partial`$. Put $`k=|K_\partial|`$. Then

```math
\boxed{
R\le(k+3)^2,\qquad k\ge\sqrt R-3.
}
\tag{10.30}
```

If $`k=0`$, there is a complete classification:

```math
\boxed{
\mathcal R\text{ is either one rhombus or the five-rhombus cross.}
}
\tag{10.31}
```

#### Proof

Apply an invertible affine map carrying the two unit edge vectors to the coordinate vectors. The complex becomes a finite union of unit squares. Positive linear equilibrium and convexity are preserved.

At a locally convex outer-boundary vertex, all incident internal edge vectors lie in a closed half-plane and at least one points strictly inward, so no strictly positive combination can vanish. At a straight boundary vertex, the two tangent directions may cancel but every remaining internal edge points strictly inward. Hence every outer-boundary vertex outside $`K_\partial`$ is either a convex-hull vertex or a reflex vertex with all four coordinate edge directions present.

Consider the boundary path between two consecutive convex-hull vertices. If its interior contains no incidence from $`K_\partial`$, every internal turn is reflex. There can be at most two such turns: three consecutive right-angle reflex turns produce four successive unit coordinate vectors whose sum is zero, returning to the initial vertex before reaching the next hull vertex. The hull chord is therefore a sum of one, two, or three successive coordinate unit vectors. Its direction is one of

```math
\pm e_1,\quad\pm e_2,\quad
\pm(e_1+e_2),\quad\pm(e_1-e_2).
\tag{10.32}
```

A convex polygon has at most one side in each of these eight oriented directions. If $`q`$ is its number of vertices and $`k_{\rm out}`$ is the number of charged outer-boundary incidences, at most eight of the $`q`$ gaps between consecutive hull vertices are uncharged. Therefore

```math
q\le k_{\rm out}+8.
\tag{10.33}
```

Let $`C,L,Z`$ denote the numbers of convex, reflex, and straight incidences of the outer orthogonal boundary. Then

```math
C-L=4,\qquad
B_{\rm out}=C+L+Z=2C+Z-4.
```

Write $`C=q+C_K`$, where $`C_K`$ counts the charged non-hull convex incidences. Since every straight incidence is also charged, (10.33) gives

```math
B_{\rm out}
\le12+2k_{\rm out}+2C_K+Z
\le12+4k_{\rm out}.
```

All inner-boundary incidences are charged, and a simple orthogonal inner boundary has the same number of edge and vertex incidences. Consequently

```math
B_{\mathcal R}\le12+4k.
\tag{10.34}
```

The tracks split into two straight families of sizes $`m`$ and $`r`$. Tracks in one family do not cross, and an opposite-family pair crosses at most once. Hence

```math
R\le mr
\le\frac{(m+r)^2}{4}
=\frac{B_{\mathcal R}^2}{16}
\le(k+3)^2,
```

proving (10.30).

It remains to classify equality-free support, $`k=0`$. There are no holes or straight boundary vertices; every convex boundary vertex is a hull vertex and every other boundary vertex is reflex. Between consecutive convex turns let $`r_i\in\{0,1,2\}`$ be the number of reflex turns. Total turning and (10.33) give

```math
\sum_{i=1}^{C}(1-r_i)=4,\qquad 4\le C\le8.
\tag{10.35}
```

This leaves a finite exact closure check. Start with $`d_1=e_1`$, let $`J`$ be a positive quarter-turn, and set

```math
d_{i+1}=J^{1-r_i}d_i,\qquad
s_i=\sum_{j=0}^{r_i}J^{-j}d_i.
\tag{10.36}
```

Here $`s_i`$ is the hull chord between consecutive convex turns. Impose $`\sum_i s_i=0`$, no repeated proper partial sum of the individual unit steps, and strict consistent turning of the hull chords. Direct substitution of $`r_i\in\{0,1,2\}`$ gives, up to cyclic shift and reversal,

```math
\begin{array}{c|c|c}
C&\text{closed words}&\text{simple word with strict hull}\\ \hline
4&0000&0000\\
5&-&-\\
6&001001&-\\
7&-&-\\
8&00020002,\ 00101002,\ 00110011,\ 01010101
&01010101.
\end{array}
```

The word $`0000`$ bounds one square. The alternating word bounds the plus-shaped union of a central square and its four edge-neighbors. Applying the inverse affine map proves (10.31). ∎

Thus a large two-direction oblique-lattice core cannot be supported only at its diametral hull vertices. An $`R`$-face core needs at least $`\sqrt R-3`$ non-hull interface supports. The general $`O(\sqrt n)`$ defect shell can pay this cost, so the theorem sharply constrains but does not eliminate the jammed branch.

---

## 11. Second-order and nonlinear stress identities

The ordinary KKT stress is not automatically a universal prestress-stability certificate. The correct necessary statement is direction dependent.

Let $`v=(v_1,\ldots,v_n)`$ satisfy the first-order critical inequalities with no first-order change in $`T`$:

```math
(p_i-p_j)\cdot(v_i-v_j)\ge0\quad(ij\in C),
\tag{11.1}
```

```math
(p_i-p_j)\cdot(v_i-v_j)\le0\quad(ij\in H).
\tag{11.2}
```

Let $`C_0(v)`$ and $`H_0(v)`$ be the active edges on which equality holds.

### Theorem 11.1: second-order normal stress for each critical direction

There exist multipliers

```math
\alpha_{ij}\ge0\quad(ij\in C_0(v)),\qquad
\beta_{ij}\ge0\quad(ij\in H_0(v))
```

satisfying the equilibrium, scalar, and tensor identities (4.1)-(4.5), supported on the zero-derivative edges, and additionally

```math
\boxed{
\sum_{H_0(v)}\beta_{ij}|v_i-v_j|^2
-
\sum_{C_0(v)}\alpha_{ij}|v_i-v_j|^2
\ge0.
}
\tag{11.3}
```

#### Proof

Suppose there were accelerations $`a_i`$ and $`s<0`$ such that

```math
p_i(t)=p_i+tv_i+\frac{t^2}{2}a_i,
\qquad
T(t)=T+\frac{t^2}{2}s
```

strictly satisfy every second-order condition on the zero-derivative active edges. Those conditions are

```math
-2(p_i-p_j)\cdot(a_i-a_j)-2|v_i-v_j|^2<0
\quad(ij\in C_0(v)),
\tag{11.4}
```

```math
2(p_i-p_j)\cdot(a_i-a_j)-s+2|v_i-v_j|^2<0
\quad(ij\in H_0(v)).
\tag{11.5}
```

Edges with strict first-order slack remain feasible automatically for sufficiently small $`t>0`$, as do inactive constraints. Thus (11.4)-(11.5) with $`s<0`$ would produce a feasible configuration of smaller diameter, contradicting optimality.

The strict linear system in the variables $`(a,s)`$ is therefore infeasible. Apply the strict Farkas alternative also to the row $`s<0`$. It gives nonnegative multipliers $`\alpha,\beta,\lambda`$, not all zero, with stationarity in $`(a,s)`$, where stationarity in $`s`$ says

```math
\lambda=\sum\beta.
```

If $`\lambda=0`$, then $`\beta=0`$ and the remaining equations would be a nonzero nonnegative equilibrium stress supported only on contacts. That is impossible for a finite free framework: choose a vertex uniquely extreme in a generic direction among the vertices incident to positive stress; every positive incident contact force has strictly positive projection there. Thus $`\lambda>0`$. Normalize it to (1), obtaining $`\sum\beta=1`$. The constant term in the Farkas alternative is precisely (11.3), and the scalar and tensor identities follow as in Theorem 4.1. ∎

### Corollary 11.2: affine second-order neutrality

For an affine velocity field

```math
v_i=Mp_i+b,
```

write $`r_{ij}=p_i-p_j`$ on contacts and $`R_{ij}=p_i-p_j`$ on diameter edges. Then the quadratic stress expression is identically zero:

```math
\begin{aligned}
&\sum_H\beta_{ij}|M(p_i-p_j)|^2
-\sum_C\alpha_{ij}|M(p_i-p_j)|^2\\
&\qquad=
\operatorname{tr}\!\left(
M^{\mathsf T}M
\left[
\sum_H\beta_{ij}R_{ij}R_{ij}^{\mathsf T}
-\sum_C\alpha_{ij}r_{ij}r_{ij}^{\mathsf T}
\right]
\right)=0.
\end{aligned}
\tag{11.6}
```

Thus the tensor identity blocks the hoped-for contradiction from a global affine shear. Also, the multiplier in Theorem 11.1 may depend on $`v`$; MFCQ alone does not justify one stress with nonnegative quadratic energy on the entire critical cone.

### Theorem 11.3: virtual work and the common stress midpoint

Fix any KKT stress from Theorem 4.1. For arbitrary vectors $`\xi_i\in\mathbb R^2`$, equilibrium gives the exact virtual-work identity

```math
\boxed{
\sum_{ij\in C}\alpha_{ij}(p_i-p_j)\cdot(\xi_i-\xi_j)
=
\sum_{ij\in H}\beta_{ij}(p_i-p_j)\cdot(\xi_i-\xi_j).
}
\tag{11.7}
```

Let

```math
m_{ij}=\frac{p_i+p_j}{2},
\qquad
a_{ij}=\frac{\alpha_{ij}}{D^2}\quad(ij\in C).
```

Both $`(a_{ij})_{C}`$ and $`(\beta_{ij})_{H}`$ are probability weights. Their midpoint barycenters agree:

```math
\boxed{
\sum_C a_{ij}m_{ij}
=
\sum_H\beta_{ij}m_{ij}
=:\mu.
}
\tag{11.8}
```

In particular, $`\mu\in\operatorname{conv}A`$.

#### Proof

Dot the vertex equilibrium equation (4.2) with $`\xi_i`$ and sum over $`i`$; the two endpoint terms of every edge combine to give (11.7).

For a fixed vector $`b`$, choose

```math
\xi(x)=|x|^2b-2(b\cdot x)x.
```

A direct calculation, with $`d=x-y`$, gives

```math
d\cdot\bigl(\xi(x)-\xi(y)\bigr)
=-|d|^2b\cdot(x+y).
```

Use this field in (11.7), substitute the active lengths $`1`$ and $`D`$, and divide by $`2D^2`$. Since $`b`$ is arbitrary, (11.8) follows. ∎

### Theorem 11.4: quartic identity and macroscopic contact-stress mass

Write

```math
\bar m_{ij}=m_{ij}-\mu,
\qquad
u_{ij}=p_i-p_j\quad(ij\in C),
\qquad
w_{ij}=\frac{p_i-p_j}{D}\quad(ij\in H).
```

Then

```math
\boxed{
\begin{aligned}
&\sum_C a_{ij}
\left[|\bar m_{ij}|^2+2(\bar m_{ij}\cdot u_{ij})^2\right]\\
&\quad-
\sum_H\beta_{ij}
\left[|\bar m_{ij}|^2+2(\bar m_{ij}\cdot w_{ij})^2\right]
=\frac{D^2-1}{4}.
\end{aligned}
}
\tag{11.9}
```

Consequently,

```math
\boxed{
\sum_C a_{ij}|m_{ij}-\mu|^2
\ge\frac{D^2-1}{12}.
}
\tag{11.10}
```

For $`D>2`$, the normalized contact-stress mass whose midpoint lies at distance at least $`D/4`$ from $`\mu`$ satisfies

```math
\boxed{
\sum_{\substack{ij\in C\\|m_{ij}-\mu|\ge D/4}}a_{ij}
\ge\frac{D^2-4}{45D^2}.
}
\tag{11.11}
```

Equivalently, the corresponding unnormalized $`\alpha`$-mass is at least $`(D^2-4)/45`$, which is $`\Theta(n)`$ along any sequence with $`n\to\infty`$ by (2.2).

#### Proof

Translate the origin to $`\mu`$ and use $`\xi(x)=|x|^2x`$ in (11.7). For $`d=x-y`$ and $`m=(x+y)/2`$,

```math
d\cdot\bigl(|x|^2x-|y|^2y\bigr)
=|m|^2|d|^2+\frac{|d|^4}{4}+2(m\cdot d)^2.
```

Insert the contact and diameter lengths, divide by $`D^2`$, and use $`\sum_Ca=\sum_H\beta=1`$ to obtain (11.9). The diameter sum in (11.9) is nonnegative, while

```math
|m|^2+2(m\cdot u)^2\le3|m|^2,
```

which proves (11.10).

Every midpoint and $`\mu`$ lie in $`\operatorname{conv}A`$, whose diameter is $`D`$, so $`|m_{ij}-\mu|\le D`$. If $`s`$ denotes the left side of (11.11), then

```math
\sum_Ca_{ij}|m_{ij}-\mu|^2
\le (1-s)\frac{D^2}{16}+sD^2.
```

Combine this with (11.10) and solve for $`s`$ to get (11.11). ∎

### Theorem 11.5: positive contact stress reaches radius $`(D-1)/2`$

For every normalized KKT certificate,

```math
\boxed{
\max_{\alpha_{ij}>0}|m_{ij}-\mu|
\ge\frac{D-1}{2}.
}
\tag{11.12}
```

#### Proof

Translate again so $`\mu=0`$. For an integer $`k\ge1`$, put

```math
\xi_k(x)=|x|^{2k}x
=\nabla\left(\frac{|x|^{2k+2}}{2k+2}\right).
```

Its Jacobian, equivalently the Hessian of the displayed convex function, is

```math
H_k(x)=|x|^{2k}I+2k|x|^{2k-2}xx^{\mathsf T}.
```

For a segment $`[x,y]`$ of length $`L`$, unit direction $`u`$, and midpoint $`m`$, define its normalized work

```math
W_k(x,y)
=\frac{(x-y)\cdot(\xi_k(x)-\xi_k(y))}{L^2}
=\frac1L\int_{-L/2}^{L/2}u^{\mathsf T}H_k(m+tu)u\,dt.
```

For a diameter segment, write $`m\cdot u=s_0`$. Since

```math
u^{\mathsf T}H_k(z)u
\ge(2k+1)|z\cdot u|^{2k},
```

and the integral of $`|s_0+t|^{2k}`$ over an interval of fixed length is minimized when $`s_0=0`$,

```math
W_k(x,y)\ge\left(\frac D2\right)^{2k}
\qquad(ij\in H).
\tag{11.13}
```

Let

```math
R=\max_{\alpha_{ij}>0}|m_{ij}|.
```

Every point on a positively stressed unit contact lies within distance $`R+1/2`$ of the origin. The largest eigenvalue of $`H_k(z)`$ is $`(2k+1)|z|^{2k}`$, so

```math
W_k(x,y)\le(2k+1)(R+1/2)^{2k}
\qquad(ij\in C,\ \alpha_{ij}>0).
\tag{11.14}
```

Apply (11.7) with $`\xi_i=\xi_k(p_i)`$ and divide by $`D^2`$. It becomes

```math
\sum_Ca_{ij}W_k(p_i,p_j)
=\sum_H\beta_{ij}W_k(p_i,p_j).
```

Equations (11.13)--(11.14) give

```math
(2k+1)(R+1/2)^{2k}
\ge(D/2)^{2k}.
```

Let $`k\to\infty`$ to obtain $`R+1/2\ge D/2`$, proving (11.12). ∎

---

## 12. Rattlers and canonical representatives

### Theorem 12.1: every isolated point can be attached

Let $`A`$ be a triangle-free minimizer and let $`p\in A`$ be contact-isolated. Then $`p`$ can be moved, without increasing the diameter or creating a unit triangle, until it has exactly one unit contact. Repeating this process gives a triangle-free minimizer with the same $`n`$ and $`D(n)`$ and no contact-isolated points.

#### Proof

For $`n\ge4`$, a diameter minimizer is noncollinear: a collinear feasible $`n`$-point set has diameter at least $`n-1`$, whereas the regular unit $`n`$-gon has strictly smaller diameter. The smaller cases have no isolated point. Thus the convex hull below has nonempty interior.

Work inside the convex polygon $`K=\operatorname{conv}A`$. Every point $`y\in K`$ satisfies

```math
|y-x|\le D\qquad(x\in A\setminus\{p\})
```

by convexity of the distance function. Starting from $`p`$, choose a path in $`K`$ toward one of the existing points. It must meet the boundary of the forbidden union

```math
\bigcup_{x\in A\setminus\{p\}}B(x,1).
```

The finitely many points at which two of the boundary circles meet can be avoided by a generic small perturbation of the path. Stop at its first boundary point. Exactly one distance is then (1), every other lower-distance constraint is still strict, and every upper-distance constraint is at most $`D`$. Thus no unit triangle is created.

The resulting diameter is at most $`D`$. If it were smaller than $`D(n)`$, global optimality would be contradicted. Hence it remains exactly $`D(n)`$. ∎

This theorem does **not** imply that a no-isolate representative can simultaneously be chosen contact-minimal or first-order jammed. The exact $`n=8`$ family warns against such a simultaneous normalization.

### Theorem 12.2: structure of a minimum-contact core

Choose a triangle-free minimizer with the minimum possible number of contacts. Delete its isolated vertices, leaving a nonisolated core with $`m`$ vertices. Let $`Q^\circ`$ be the diameter endpoints belonging to that core.

Then:

1. Every nontrivial contact component meets $`Q^\circ`$.
2. Fixing $`Q^\circ`$, the expansive cone of the core is zero.
3. If the core has $`e`$ contact edges, then

   ```math
   e\ge2(m-|Q^\circ|).
   \tag{12.1}
   
   ```

4. Under triangle-freeness,

   ```math
   |Q^\circ|
   \ge\frac14\sqrt{2\pi\sqrt3\,m}-O(1).
   \tag{12.2}
   
   ```

#### Proof

If a nontrivial contact component contains no diameter endpoint, give every vertex $`p_i`$ in that component the velocity

```math
v_i=J(p_i-c),
```

where $`J`$ is a quarter-turn and $`c`$ is fixed. Along the straight path, every internal contact vector $`r`$ changes by $`tJr`$, so its squared length becomes

```math
|r+tJr|^2=|r|^2+t^2|r|^2>1.
```

Cross-component pairs and diameter constraints have strict slack. This breaks contacts without increasing the diameter, contradicting contact minimality. Hence every component meets $`Q^\circ`$.

Now suppose the core has a nonzero pinned expansive velocity. Along the straight motion, every contact with positive first derivative breaks immediately; a zero-derivative contact with nonzero relative velocity breaks at second order. If every contact has zero relative velocity, the velocity is constant on each component, and the pinned vertex in that component forces the constant to be zero. Thus every nonzero expansive velocity would reduce the contact count, a contradiction. The cone is zero, and the rank and Eppstein arguments give (12.1)-(12.2). ∎

If the number $`z=n-m`$ of isolated vertices in this contact-minimal representative is $`O(\sqrt n)`$, the face-counting argument applied to the core again yields $`m-O(\sqrt n)`$ near-equilateral rhombi. If $`z`$ is large, that representative is genuinely rattler dominated; Theorem 12.3 controls a different, maximal-contact representative.

### Theorem 12.3: a maximal-contact representative has no unanchored component

Assume that a triangle-free minimizer exists for a fixed $`n`$. Among all such minimizers, choose $`A_{\max}`$ with the maximum number of unit contacts; subject to that choice, maximize the number $`q`$ of diameter endpoints. Then every contact component contains a diameter endpoint. Consequently, if $`z`$ is the number of isolated contact vertices and $`c`$ the number of contact components,

```math
\boxed{
z\le q\le C_0\sqrt n,
\qquad
c\le q\le C_0\sqrt n.
}
\tag{12.3}
```

#### Proof

Suppose a contact component $`K`$ contains no diameter endpoint. Translate every point of $`K`$ by the same vector $`t`$. Internal distances remain unchanged. For every $`p\in K`$ and $`x\notin K`$, the original cross-distance is strictly between $`1`$ and $`D`$. Define the feasible translation set

```math
\mathcal T=
\left\{
t\in\mathbb R^2:
1\le|p+t-x|\le D
\text{ for all }p\in K, x\notin K
\right\}.
```

It is closed and bounded, and $`0`$ lies in its interior. Boundedness follows already from any one upper constraint $`|p+t-x|\le D`$; a point outside $`K`$ exists because every diameter edge lies outside $`K`$.

The boundary lies in finitely many unit or diameter circles in the translation plane. Choose a ray from $`0`$ that avoids every intersection point of two noncoincident circles, and move along it until the first boundary point of $`\mathcal T`$. All newly active cross-constraints then belong to one geometric circle. Distinct constraints defining the same circle have the same center $`x-p`$ and radius. For unit constraints, the resulting new contact edges form a matching: two distinct such pairs cannot share $`p`$ or share $`x`$. A matching of new intercomponent edges cannot create a triangle, because any triangle using the old components would require two new edges sharing a vertex.

If the active circle is a unit circle, at least one contact is added and none is lost, contradicting maximality of the contact count. If it is a diameter circle, the contact graph is unchanged but a vertex of $`K`$ becomes a new diameter endpoint, contradicting the secondary maximization. Existing diameter edges lie outside $`K`$ and remain fixed, so every translated configuration still has diameter exactly $`D`$. This proves the anchoring assertion.

Each component contains a distinct vertex of $`Q`$, proving $`c\le q`$; an isolated vertex is itself a component, proving $`z\le q`$. Corollary 6.2 supplies the remaining bounds. ∎

The minimum-contact and maximum-contact representatives serve different purposes. The former has a jammed nonisolated core; the latter eliminates an arbitrarily large collection of unanchored rattlers or components. They need not be the same minimizer.

### Theorem 12.4: a hybrid representative with a fixed jammed backbone

Assume that a triangle-free minimizer exists for a fixed $`n`$. There is a triangle-free minimizer $`\widehat A`$ with the same $`n`$ and $`D(n)`$, together with a distinguished contact subgraph $`K`$, such that:

1. $`K`$ is the unchanged nonisolated core of a contact-minimal triangle-free minimizer. If $`Q_K`$ denotes its original diameter endpoints, then the expansive cone of $`K`$ pinned at $`Q_K`$ is zero.
2. Every contact component of $`\widehat A`$ contains a diameter endpoint, and

   ```math
   \#\{\text{contact components}\},
   \quad
   \#\{\text{contact-isolated vertices}\}
   \le C_0\sqrt n.
   \tag{12.4}
   
   ```

3. Every contact edge of $`\widehat A`$ outside $`K`$ is a bridge. Thus every contact cycle and every nonbridge contact edge lies in $`K`$.
4. If $`\widehat Q`$ is the full diameter-endpoint set of $`\widehat A`$, every velocity in $`\mathcal E_{\widehat Q}(\widehat A)`$ vanishes on $`V(K)`$. All surviving pinned flexibility is confined to the forest left after the fixed vertices $`V(K)\cup\widehat Q`$ are deleted.

#### Proof

Start with a contact-minimal triangle-free minimizer $`A_0`$. Let $`K`$ be its nonisolated core and $`Q_0`$ its full diameter-endpoint set. By Theorem 12.2, every component of $`K`$ meets

```math
Q_K=Q_0\cap V(K),
```

and the expansive cone of $`K`$ pinned at $`Q_K`$ is zero.

Keep every point of $`K`$ and every point of $`Q_0`$ fixed from now on. In particular, an original diameter pair remains fixed, so every configuration constructed below has diameter exactly $`D(n)`$, not merely at most $`D(n)`$.

First treat the isolated points. Whenever a currently isolated point $`p\notin Q_0`$ remains, apply the path construction from Theorem 12.1 while all other points stay fixed, choosing the path generically so that its first lower-distance boundary point creates exactly one contact. That edge joins two previously distinct contact components, so it is a bridge and cannot create a triangle. Repeat until every remaining isolated point belongs to $`Q_0`$. There are at most $`|Q_0|=O(\sqrt n)`$ such points.

Next take a contact component $`L`$ containing no current diameter endpoint. Every cross-distance between $`L`$ and its complement is strictly between (1) and $`D`$. Make an arbitrarily small generic rigid rotation of $`L`$, preserving all its internal distances and all strict cross-inequalities. After that rotation, parameterize a translation by $`t`$. Each cross-constraint has boundary circle

```math
|Rp+t-x|=r,
\qquad r\in\{1,D\},\qquad p\in L,\qquad x\notin L.
\tag{12.5}
```

Two distinct constraints of the same radius have coincident circles only if

```math
x-y=R(p-q).
\tag{12.6}
```

For each pair this excludes at most finitely many rotation angles unless the constraints are identical. The two radii are distinct in every nontrivial case. Thus the preliminary rotation can make all distinct boundary circles noncoincident.

The feasible translation set

```math
\mathcal T_L=
\left\{t:
1\le|Rp+t-x|\le D
\text{ for all }p\in L, x\notin L
\right\}
```

is closed and bounded and contains the current translation in its interior. Choose a ray avoiding the finitely many intersection points of distinct boundary circles and stop at its first boundary point. Exactly one cross-constraint becomes active.

If it is a unit constraint, one new bridge joins two contact components and their number decreases. If it is a diameter constraint, the contact graph stays unchanged and $`L`$ acquires a diameter endpoint. In either case the number of components without a diameter endpoint decreases by at least one. Never move a component after it has acquired a diameter endpoint. Repetition terminates with every component anchored.

Every added unit edge joined two distinct current components. The quotient graph of these mergers is therefore a forest, so every added contact remains a bridge. Since every final component contains a distinct point of $`\widehat Q`$,

```math
\#\{\text{components}\},
\quad
\#\{\text{isolates}\}
\le|\widehat Q|
\le C_0\sqrt n.
```

Finally let $`v\in\mathcal E_{\widehat Q}(\widehat A)`$. Every point of $`Q_K`$ remains an endpoint of its fixed original diameter pair, so $`Q_K\subseteq\widehat Q`$. Restrict $`v`$ to the unchanged contacts of $`K`$. This is an element of the expansive cone of $`K`$ pinned at $`Q_K`$, hence it vanishes throughout $`K`$. Every edge outside $`K`$ is a bridge, proving the last assertion. A remaining forest piece may have several fixed attachments; no one-root assertion is being made. ∎

### Theorem 12.5: quantitative size of the bridge-forest obstruction

Use $`\widehat A,K,\widehat Q`$ from Theorem 12.4 and put

```math
U=V(\widehat A)\setminus\bigl(V(K)\cup\widehat Q\bigr),
\qquad u=|U|.
```

Contract each component of $`K`$ to one fixed root, retain each point of $`\widehat Q\setminus V(K)`$ as a fixed root, and retain all contact edges incident with $`U`$. Let $`r`$ be the number of incident fixed roots and $`c`$ the number of nonempty connected components of this quotient forest. Define the pinned contact-preserving lineality space

```math
\mathcal L_{\widehat Q}(\widehat A)=
\left\{v:
v_i=0\ (i\in\widehat Q),
\quad
(p_i-p_j)\cdot(v_i-v_j)=0\ (ij\in C)
\right\}.
\tag{12.7}
```

Then

```math
\boxed{
\dim\mathcal L_{\widehat Q}(\widehat A)
\ge u-r+c
\ge u-|\widehat Q|+c.
}
\tag{12.8}
```

In particular, if the full pinned expansive cone is zero, then

```math
\boxed{
u\le r-c\le|\widehat Q|-c.
}
\tag{12.9}
```

Writing $`\ell=\dim\mathcal L_{\widehat Q}(\widehat A)`$, one has

```math
\boxed{
|V(\widehat A)\setminus V(K)|
\le \ell+2|\widehat Q|.
}
\tag{12.10}
```

Consequently, if $`\ell=O(\sqrt n)`$, then $`K`$ contains $`n-O(\sqrt n)`$ vertices and itself has

```math
n-O(\sqrt n)
```

strict unit-rhombus faces with total angular defect $`O(\sqrt n)`$.

#### Proof

Every contact edge outside $`K`$ is a bridge. After the components of $`K`$ are contracted, a cycle or a pair of parallel quotient edges would put its uncontracted edges on a contact cycle in the original graph, contradicting that bridge property. The quotient is therefore a forest.

A forest on $`u+r`$ vertices with $`c`$ components has $`u+r-c`$ edges. Its contact-equality matrix has $`2u`$ columns and at most $`u+r-c`$ nonzero rows, so its kernel has dimension at least

```math
2u-(u+r-c)=u-r+c.
```

Extend a kernel vector by zero on $`V(K)\cup\widehat Q`$. Every contact derivative is zero, so the extension belongs to (12.7). Every component of $`K`$ contains an original diameter endpoint, and all other roots are in $`\widehat Q\setminus V(K)`$; hence $`r\le|\widehat Q|`$. This proves (12.8).

The lineality space lies inside the pinned expansive cone. If that cone is zero, its lineality is zero, and (12.9) follows from (12.8). In general, $`u\le\ell+|\widehat Q|-c`$. Adding the at most $`|\widehat Q|`$ pinned vertices outside $`K`$ gives (12.10). If $`\ell=O(\sqrt n)`$, (12.10) and Corollary 6.2 give $`|V(K)|=n-O(\sqrt n)`$. The core is triangle-free and has zero expansive cone after $`Q_K`$ is pinned. Applying the rank and Euler counts to $`K`$, and using the ambient area bound

```math
\operatorname{area}(\operatorname{conv}A)
<\frac{\sqrt3}{2}n,
```

gives the stated almost-rhombic conclusions exactly as in Sections 8--10. ∎

Thus Target A has an exact scale dichotomy. Either one representative already has an almost-spanning jammed rhombic backbone, or its bridge forest carries more than boundary-order many independent contact-preserving motions. Eliminating only the latter, super-boundary-dimensional alternative would reduce all sufficiently large counterexamples to the boundary-capacity problem of Target B.

---

## 13. Arbitrarily large triangle-free local minima

The local-rigidity route cannot prove Erdős #99.

### Proposition 13.1: regular prime polygons

For every odd prime $`p\ge5`$, the regular unit $`p`$-gon is a triangle-free strict local minimum of diameter among feasible $`p`$-point configurations, modulo Euclidean congruence.

#### Proof

In a regular unit $`p`$-gon, a diagonal spanning $`k`$ boundary steps has length

```math
\frac{\sin(k\pi/p)}{\sin(\pi/p)}>1
\qquad
\left(2\le k\le\frac{p-1}{2}\right).
```

Thus its only contacts are its sides, and the contact graph is $`C_p`$.

Bezdek and Fodor [3, Theorem 1.2] prove that, for odd prime $`p`$, every convex $`p`$-gon with sides at least (1) has diameter at least

```math
d_p=\frac1{2\sin(\pi/(2p))},
```

with equality only for the regular unit $`p`$-gon.

Convexity and cyclic order persist under sufficiently small perturbations. Every nearby feasible configuration is therefore a convex $`p`$-gon with consecutive side lengths at least (1), so the theorem applies. Equality forces congruence. ∎

There are arbitrarily large odd primes, so there are arbitrarily large triangle-free strict local minima. Consequently, no proof can rely on the assertion that every sufficiently large triangle-free feasible configuration is locally diameter-improvable.

The proposition does not produce global minimizers for the full $`p`$-point problem: other configurations may have fewer hull vertices and smaller diameter, as already happens at $`p=7`$.

---

## 14. The regular-shell obstruction

The exact stress identities also cannot distinguish global minimizers from large, dense triangle-free local minima.

Let $`h=2k+1\ge5`$ be odd and let $`P_h`$ be a regular unit $`h`$-gon. Its diameter is

```math
D_h=\frac1{2\sin(\pi/(2h))}.
\tag{14.1}
```

Its contact graph is the boundary cycle. Its diameter graph joins each vertex to the two vertices $`k`$ steps away and is another $`h`$-cycle.

### Proposition 14.1: exact shell stress

Assign

```math
\alpha_e=\frac{D_h^2}{h}
```

to every contact edge and

```math
\beta_e=\frac1h
```

to every diameter edge. These coefficients satisfy all equations (4.1)-(4.5).

#### Verification

At a vertex, the sum of its two contact edge vectors is radial with factor $`2(1-\cos(2\pi/h))`$, while the sum of its two diameter vectors is radial with factor $`2(1+\cos(\pi/h))`$. The identity

```math
D_h^2\bigl(1-\cos(2\pi/h)\bigr)
=1+\cos(\pi/h)
```

gives equilibrium. Rotational symmetry gives the tensor identity; both sides equal $`D_h^2I/2`$.

### Proposition 14.2: dense triangle-free shell fillings

For arbitrarily large odd $`h`$, one can place

```math
n_h=\Delta_2D_h^2+o(D_h^2)
\tag{14.2}
```

points in $`P_h`$, including its vertices, so that the configuration is unit-separated, has diameter $`D_h`$, and has no unit equilateral triangle.

#### Construction

Retain the unit polygon vertices. Inside $`P_h`$, exclude the unit neighborhoods of those vertices and place a generically translated and rotated triangular lattice of spacing $`1+\varepsilon_h`$, where $`\varepsilon_h\downarrow0`$. All interior-interior distances are at least $`1+\varepsilon_h`$, and all shell-interior distances are strictly greater than (1). A generic placement avoids accidental equalities. Thus the only unit contacts are the shell sides.

The excluded boundary area is $`O(h)`$, while

```math
\operatorname{area}(P_h)\sim\frac{h^2}{4\pi}
\quad\text{and}\quad
D_h\sim\frac h\pi.
```

For completeness, if $`\Lambda`$ is a lattice with fundamental-cell area $`a`$, averaging over a fundamental cell of translations gives

```math
\frac1a\int_{\mathbb R^2/\Lambda}|(K+t)\cap\Lambda|\,dt
=\frac{\operatorname{area}(K)}a
```

for every measurable bounded region $`K`$. Hence some translate contains at least the average number of lattice points. Apply this to the polygon after deleting the forbidden shell neighborhoods. Its area is $`\operatorname{area}(P_h)-O(h)`$, and the spacing-$`1+\varepsilon_h`$ triangular lattice has cell area $`\frac{\sqrt3}{2}(1+\varepsilon_h)^2`$. Choosing $`\varepsilon_h\downarrow0`$ slowly gives (14.2); a further generic translation or rotation avoids the finitely many unwanted equality conditions without changing the asymptotic count.

For prime $`h`$, Proposition 13.1 makes the shell locally diameter minimizing. The interior points may move, so the filled configuration need not be a strict local minimum, but no sufficiently small feasible perturbation can lower its diameter because the shell subset cannot be improved locally.

These configurations are **not certified global minimizers**. They prove instead that all of the following may coexist at arbitrarily large scale:

- triangle-freeness;
- asymptotically hexagonal density;
- exact KKT scalar and tensor identities;
- a boundary-supported proper stress;
- a flexible or completely unstressed interior; and
- local diameter minimality.

Therefore any Level I proof must use a sharp global finite-capacity comparison, not merely local rigidity, stress, or leading density.

---

## 15. Computational exploration

Numerical optimization was used only for conjecture formation and falsification of local lemmas.

### 15.1 Moderate-$`n`$ nonlinear searches

SLSQP searches were run for $`9\le n\le13`$, minimizing a diameter variable subject to all squared-distance lower and upper constraints. Multiple perturbed triangular-patch starts were used.

For $`n=9`$, one run produced an apparent triangle-free local optimum with

```math
D\approx2.56923698,
```

with (11) apparent unit contacts and (5) apparent diameter pairs. Its hull had seven vertices. This is consistent with the Vincze-type upper-bound discussion in [3], but it is **not** an exact configuration and no global lower bound was obtained.

For $`n=10,11,12,13`$, the best runs found in the limited search included apparent unit triangles in several active sets. These computations are neither exhaustive nor exact.

No numerical equality was treated as a unit contact. The experiment supplies no proof for or against Erdős #99.

### 15.2 Polygon-area experiment

A separate constrained numerical experiment minimized the area of convex equilateral $`m`$-gons with all vertex distances at least (1), for $`4\le m\le8`$. It repeatedly found the value

```math
(m-2)\frac{\sqrt3}{4}
```

at degenerate triangular-lattice-type limits. A complete proof for the general face class was not established, and even such a face inequality would not control the possibly winding outer contact face. It was therefore not used as a theorem.

### 15.3 Train-track and boundary-word falsification

The balanced $`C_5`$ crossing pattern was first tested by explicit coordinate generation for small sector sizes. Those tests detected no unintended unit distances or edge crossings and led to Proposition 10.10. The proposition's final statement does not rely on those computations: its unit separation, planarity, track graph, positive stress, and pinned rank are proved exactly.

The $`k=0`$ case of Theorem 10.12 was independently checked by enumerating the words $`r_i\in\{0,1,2\}`$ for $`4\le C\le8`$. Before simplicity is imposed, the canonical closed words are exactly those displayed after (10.36); all except $`0000`$ and $`01010101`$ repeat a boundary vertex. Again the theorem uses the explicit finite recurrence (10.36), not floating-point evidence.

Finally, the pairwise distances in the 11-point sun and the 12-point triangular-lattice competitor were enumerated during discovery and then replaced by the exact cyclotomic and quadratic-form calculations in Proposition 10.10.

---

## 16. Routes that were tested and why they do not close the problem

### 16.1 Leading density

A triangular lattice can be perturbed by an arbitrarily small amount so that no exact unit triangle remains, then rescaled to minimum distance (1). Thus triangle-free configurations can approach $`\Delta_2`$ arbitrarily closely. There is no uniform density gap based only on the absence of exact contacts.

### 16.2 Raw edge counts and Laman-style counting

Eppstein gives a contact deficit of order $`\sqrt n`$, but the diameter graph also lives on $`\Theta(\sqrt n)`$ boundary vertices. Those cable constraints can compensate for the missing contact rows. The square is the smallest exact example.

### 16.3 Recursive use of (2)-degeneracy

A low-degree contact vertex need not be removable. It may be a diameter-loaded polygon corner, as in the square and every regular odd shell. Deleting it also destroys the equilibrium equations at its neighbors. A degeneracy ordering is not a recursively valid stress ordering.

### 16.4 First-order flexibility

The zero-cone branch is possible, and Proposition 13.1 gives arbitrarily large triangle-free local minima. In the nonzero-cone branch, the result is only a family of same-diameter minimizers, not a diameter improvement.

### 16.5 Second-order prestress

The correct multiplier may depend on the critical direction. Furthermore, the tensor identity makes every affine critical shear quadratic-neutral. A fixed-stress negative-curvature claim is unjustified.

### 16.6 Exact rhombus equality

The total defect

```math
\sum_F\left(\sin\theta_F-\frac{\sqrt3}{2}\right)
```

is only $`O(\sqrt n)`$. This permits $`n-O(\sqrt n)`$ strictly positive defects of size $`O(1/n)`$, or smaller. No exact $`60^\circ`$ angle follows.

### 16.7 Lattice classification

Schürmann rules out eventual lattice extremizers. Nonlattice does not mean triangle-free, and a nonlattice rhombic mesh is not excluded.

### 16.8 Simultaneous normalizations

The full normalization $`\mathcal E_Q(A)=\{0\}`$ still cannot be imposed by selection. Theorem 12.4 does combine the two useful partial normalizations in one representative: it has only $`O(\sqrt n)`$ components and isolates, and every pinned motion vanishes on a fixed contact-minimal core. The residue is exactly a bridge forest. Theorem 12.5 quantifies it: if its contact-preserving lineality is only $`O(\sqrt n)`$, the fixed core already contains $`n-O(\sqrt n)`$ vertices. What remains is a genuinely high-dimensional forest-flex alternative, not the old arbitrary-representative gap.

### 16.9 Regular shells as counterexamples

Regular prime shells certify local polygonal optimality and carry exact stresses. What is missing for a disproof is an infinite sequence of $`n`$ for which a filled shell has diameter exactly $`D(n)`$. Bezdek-Fodor's polygon theorem does not compare against configurations with fewer hull vertices and many interior points.

### 16.10 Nonlinear stress moments

The identities (11.7)--(11.14) are exact and substantially restrict where positive stress can live. They are nevertheless necessary conditions, not global certificates. The regular-shell stress satisfies every virtual-work identity automatically, including the midpoint and high-moment consequences. Their remaining promise lies in combining them with the degree-four rhombic bulk, not in using them alone.

### 16.11 Train tracks without diametral boundary control

The crossing graph of the rhombus tracks is simple and triangle-free, giving

```math
F_4\le B_{\mathcal R}^2/16.
```

At most two tracks can have both ends on the strictly turning convex hull, so at least

```math
2\sqrt n-O(1)
```

track ends enter the non-hull or non-rhombic defect network. The exact width inequality also charges every angular defect. These facts eliminate an exception-free convex rhombic crystal but do not control the compulsory boundary shell sharply enough.

Proposition 10.10 is the exact limitation. Its five-sector complexes have zero expansive cone when their full boundary is pinned, a positive stress on every edge, $`n-O(\sqrt n)`$ strict rhombi, diameter $`O(\sqrt n)`$, and total defect tending to zero. They fail precisely because most boundary pins are neither extreme nor diametral. Thus a local curvature maximum principle, positive stress, or ordinary boundary-pinned rigidity cannot replace $`Q=V(\operatorname{conv}A)`$.

Theorem 10.12 sharpens the opposite side of this picture. A two-fixed-direction $`R`$-face core needs at least $`\sqrt R-3`$ non-hull interface supports, apart from the one-rhombus and five-rhombus-cross exceptions. This proves that the $`\Theta(\sqrt n)`$ support shell is genuinely necessary for an ordinary oblique grid, but the general theorem stack still permits a shell of exactly that order.

### 16.12 Why the Cartesian estimate does not automatically globalize

Theorem 10.9 is a genuine global-capacity exclusion: an additive $`a\times b`$ block occupying at least $`2n/\pi`$ cells cannot occur in a minimizer. A dense track-crossing graph need not supply such a block. Five projective direction classes can have crossing graph a balanced blow-up of $`C_5`$; Proposition 10.10 realizes the corresponding five-sector geometry with $`R=5s^2`$ crossings. Its largest complete bipartite subgraph has only $`2s^2=2R/5`$ crossings, below the $`2R/\pi`$ scale needed for the Cartesian estimate to contradict global optimality when $`R\sim n`$. No extraction of a sufficiently large Cartesian block follows from triangle-freeness, quadratic track density, unit separation, or even total defect $`o(1)`$ alone.

### 16.13 Schürmann's deformation mechanism

Schürmann's proof was rechecked at the level of its actual sequential motion. It uses missing neighbors in one fixed four- or six-neighbor packing lattice, frees sites one at a time, and propagates the free sites to the boundary. An almost-rhombic mesh has varying track directions and may devote $`\Theta(\sqrt n)`$ exceptional vertices to blocking exactly this propagation. The lattice deformation remains a useful model, but its hypotheses do not extend to the surviving defect shell without a new boundary-peeling theorem.

---

## 17. Strongest consolidated unconditional theorem

### Theorem 17.1: audited triangle-free minimizer alternatives

Let $`A`$ be a triangle-free diameter-minimizing $`n`$-point configuration with minimum distance (1), and let $`Q`$ be its diameter endpoints.

Then:

1. **Exact stress and moments.** $`A`$ carries a normalized proper mixed contact/diameter KKT stress satisfying (4.1)-(4.5) and the virtual-work identity (11.7). The two normalized edge-stress measures have the same midpoint barycenter $`\mu`$, satisfy the quartic identity (11.9), and obey

   ```math
   \sum_C\frac{\alpha_{ij}}{D^2}|m_{ij}-\mu|^2
   \ge\frac{D^2-1}{12},
   \qquad
   \max_{\alpha_{ij}>0}|m_{ij}-\mu|
   \ge\frac{D-1}{2}.
   
   ```

2. **Second-order normality.** Every critical first-order direction has a direction-dependent normalized stress supported on its zero-derivative active edges and satisfying (11.3).

3. **Pinned dichotomy.** Exactly one of the following occurs:

   - $`A`$ belongs to a nontrivial continuous family of triangle-free global minimizers with all diameter endpoints fixed; or
   - the pinned expansive cone is zero.

4. **Jammed branch.** In the zero-cone branch:

   ```math
   Q=V(\operatorname{conv}A),
   
   ```

   every non-hull vertex is a strict convex combination of at least three unit-contact neighbors,

   ```math
   |Q|=\Theta(\sqrt n),\qquad
   e^\circ\ge2(n-|Q|),\qquad
   |E(G(A))|=2n-\Theta(\sqrt n),
   
   ```

   and its cyclomatic number is at least $`n-2|Q|+c=n-O(\sqrt n)`$. All nontrivial tree components together contain $`O(\sqrt n)`$ vertices, every cyclic component contains at least four diameter endpoints, and for $`n\ge44`$ at least one cyclic component exists.

5. **Rhombic bulk.** In the zero-cone branch there are $`n-O(\sqrt n)`$ bounded unit-rhombus faces and

   ```math
   \sum_{F\in\mathcal F_4}\left(\theta_F-\frac\pi3\right)=O(\sqrt n).
   
   ```

   All but $`O(\sqrt n)`$ vertices have contact degree (4) and are incident only with these rhombi. For every fixed $`\varepsilon>0`$, all but $`O_\varepsilon(\sqrt n)`$ vertices are surrounded by rhombi with acute angles in

   ```math
   60^\circ<\theta<60^\circ+\varepsilon.
   
   ```

   If $`B_{\mathcal R}`$ is the boundary-edge count of the full rhombic face complex, then

   ```math
   F_4\le\frac{B_{\mathcal R}^2}{16},
   \qquad
   B_{\mathcal R}D_{\mathcal R}
   \ge4\sum_F\sin\theta_F
   \ge2\sqrt3F_4+4\chi_*\sum_F\left(\theta_F-\frac\pi3\right).
   
   ```

   At most two tracks have both ends on the convex hull, so at least $`2\sqrt n-O(1)`$ track ends enter the defect network. If the rhombi tile the whole convex hull, the configuration is the unit square.

   If a connected $`R`$-face subcomplex uses only two fixed edge directions, has regular boundary topology as in Theorem 10.12, and needs external support at only $`k`$ non-hull boundary incidences, then

   ```math
   R\le(k+3)^2.
   
   ```

   With no such incidences it is either one rhombus or the five-rhombus cross.

6. **Existential normal forms.** If any triangle-free minimizer exists for a given $`n`$, there is a contact-minimal one for the same $`n,D(n)`$ in which every non-diameter nonisolated vertex is surrounded by (3)-(5) contacts, every contact vertex of degree (1) or (2) is diametral, all nontrivial tree components together contain $`O(\sqrt n)`$ vertices, and

   ```math
   \kappa\ge\frac{n-z}{2}-C_0\sqrt n+c_*
   
   ```

   for the cyclomatic number of the nonisolated contact graph.

   More strongly, one hybrid representative has only $`O(\sqrt n)`$ components and isolates and contains the unchanged contact-minimal core $`K`$, pointwise fixed under every pinned expansive motion. Every contact edge outside $`K`$ is a bridge. If $`u`$ unpinned vertices lie outside $`K`$ and the contracted bridge forest has $`r`$ fixed roots and $`c`$ components, then

   ```math
   \dim\mathcal L_{\widehat Q}\ge u-r+c\ge u-|\widehat Q|+c.
   
   ```

   Hence lineality $`O(\sqrt n)`$ already forces $`|V(K)|=n-O(\sqrt n)`$ and puts that core in the almost-rhombic regime.

7. **Exact global block restriction.** Every additive Cartesian $`a\times b`$ rhombic train block in a global minimizer satisfies

   ```math
   ab+\frac{4\sqrt3-6}{\pi}\Delta_{a,b}<\frac2\pi n.
   
   ```

8. **Exact limitations.** There are arbitrarily large triangle-free strict local diameter minima, arbitrarily large asymptotically dense triangle-free shell configurations carrying the full exact KKT stress, and arbitrarily large boundary-pinned jammed rhombic complexes with positive stress and total positive angular defect tending to zero. The 11-point sun additionally has a diametral convex hull, positive stress, zero hull-pinned cone, and five strict rhombi, yet no $`60^\circ`$ face. It is provably not global: a 12-point triangular-lattice set of diameter (3) is already smaller than its diameter $`\sqrt{5+2\sqrt5}`$.

Every statement above is unconditional. None implies that a hypothetical triangle-free configuration is globally nonoptimal.

---

## 18. Exact remaining Level I target

The investigation reduces the affirmative problem to eliminating two sharply defined possibilities.

### 18.1 Flexible anchored-component obstruction

One must prove that, for sufficiently large $`n`$, no triangle-free global minimizer can have a nonzero pinned expansive cone. Equivalently, one must rule out a same-diameter triangle-free minimizer family supported by a diametral shell.

Theorems 12.4 and 12.5 reduce this to an exact scale question. In one representative, all nonbridge structure lies in a fixed pinned-jammed core $`K`$, and the remaining contact graph is a bridge forest. If its pinned contact-preserving lineality has dimension $`\ell`$, then

```math
|V(A)\setminus V(K)|\le\ell+2|Q|.
```

Thus $`\ell=O(\sqrt n)`$ already puts $`n-O(\sqrt n)`$ vertices into the almost-rhombic core. The genuinely separate flexible obstruction is now:

> **Super-boundary forest-capacity lemma.** No sufficiently large triangle-free global minimizer in the hybrid normal form has $`\ell=\omega(\sqrt n)`$.

This lemma would not by itself finish Level I, but it would reduce every counterexample to the same boundary-order rhombic problem. The $`n=8`$ family and the regular-shell fillings show why it requires global capacity, not another local rigidity count.

### 18.2 First-order-jammed almost-rhombic obstruction

One must prove that a global minimizer cannot satisfy all of the following for arbitrarily large $`n`$:

```math
Q=V(\operatorname{conv}A),\qquad |Q|=\Theta(\sqrt n),
```

```math
e^\circ\ge2(n-|Q|),\qquad
e=2n-\Theta(\sqrt n),\qquad
F_4=n-O(\sqrt n),
```

```math
\theta_F>60^\circ\text{ for every rhombus},
```

```math
\sum_F\left(\theta_F-\frac\pi3\right)=O(\sqrt n),
```

together with cyclomatic number $`n-O(\sqrt n)`$, the first- and second-order stress identities, the common midpoint barycenter, the quartic identity, and positive contact stress reaching radius at least $`(D-1)/2`$ from that barycenter.

In addition, the surviving rhombic complex must satisfy

```math
F_4\le\frac{B_{\mathcal R}^2}{16},
\qquad
b_{\mathcal R}\ge2\sqrt{F_4}-2,
```

where $`b_{\mathcal R}`$ counts non-hull boundary edges, as well as

```math
B_{\mathcal R}D_{\mathcal R}
\ge2\sqrt3F_4+4\chi_*\sum_F\delta_F.
```

For an ideal disk rhombic minimizer, its exact permitted shell budget is

```math
4G+4\chi_*\Delta
<\sqrt3B_{\mathcal R}+2\sqrt3.
\tag{18.1}
```

Theorem 10.12 eliminates one important model case: a large two-direction core cannot be held only by its diametral hull vertices. It must use at least $`\sqrt R-3`$ non-hull support incidences. This does not yet contradict the general $`O(\sqrt n)`$ exceptional budget; it identifies the exact boundary scale that a sharp capacity theorem must charge.

The required conclusion is an exact equality

```math
\theta_F=60^\circ
```

for at least one face, not merely $`\theta_F=60^\circ+o(1)`$.

### 18.3 A sufficient missing global theorem

One sufficient theorem would be:

> **Sharp boundary-capacity theorem.** For all sufficiently large $`n`$, every unit-separated triangle-free $`n`$-point set satisfying either branch of Theorem 17.1 has diameter strictly larger than an explicitly constructed $`n`$-point competitor.

Such a theorem must include a boundary-order term and an exact equality analysis. The leading Thue density constant, an $`O(\sqrt n)`$ contact deficit, or an $`O(1)`$ diameter estimate is insufficient unless its constants and equality cases actually separate the two configurations.

After the new train-track theorem, a focused jammed-branch version is:

> **Diametral-shell cost lemma.** In a sufficiently large jammed triangle-free minimizer, the non-hull interfaces forced by at least $`2\sqrt n-O(1)`$ bad track ends have a strict area/diameter cost exceeding the right side of (18.1), with the exact exceptional-face, hole, component, and outside-vertex corrections.

Proposition 10.10 shows that “pinned boundary” cannot replace “diametral convex hull” in this statement. The five-sector examples satisfy all the local premises, even with total defect $`o(1)`$, and fail only at the hull condition.

For a disproof, the exact missing theorem is the opposite:

> **Globally optimal shell theorem.** There are arbitrarily large $`n`$ for which a triangle-free shell or rhombic configuration can be proved to have diameter $`D(n)`$.

No such global certificate was obtained.

---

## 19. Final adversarial audit

The following checks were applied to every consolidated claim.

### Quantifiers

- No result replaces “every minimizer” by “some minimizer” except the explicitly labeled contact-minimal normal-form theorem, which is used only under an existential contradiction hypothesis.
- No finite counterexample is presented as a disproof.
- No infinite family of local minima is presented as an infinite family of global minimizers.

### Exact distances

- Every asserted unit triangle consists of three exact unit edges.
- Near-equilateral rhombi are never counted as exact unit triangles.
- Numerical distances are not used as equality evidence.

### Optimization

- Ordinary KKT is justified by an explicit MFCQ direction.
- The second-order multiplier is allowed to depend on the critical direction.
- The nonlinear midpoint and moment formulas are derived from the vertex equilibrium equations by exact virtual work, not by an asymptotic approximation.
- The high-moment radius estimate uses the explicit Hessian of $`|x|^{2k+2}/(2k+2)`$ and then takes $`k\to\infty`$ only after a valid inequality for every integer $`k\ge1`$.
- Global and local optimality are kept distinct.
- Same-diameter flexes are not called diameter improvements.

### Rigidity

- No Laman theorem is applied to the cable-strut problem.
- The pinned positive stress is obtained by a direct cone-duality proof, not by an unchecked transfer of an unpinned theorem.
- Contacts joining two pinned vertices are removed from the effective row count, giving $`e^\circ\ge2(n-q)`$.
- First-order zero-cone rigidity is not silently upgraded to global rigidity.

### Boundary and packing

- The planar lower bound uses Bezdek-Fodor's sharper (-1) constant.
- The triangular-lattice averaging argument uses an open disk, so the upper bound in (2.2) is strict.
- Cauchy's perimeter-diameter inequality is used only for convex hulls.
- The enclosing-circle problem is never substituted for the diameter problem.
- Schürmann's theorem is used only to exclude large lattice extremizers.
- Train monotonicity and the two-crossing exclusion do not assume simple connectedness; the latter uses disjoint open $`60^\circ`$ displacement cones.
- The Cartesian determinant bound is invoked only for an actual additive block, not for an abstract biclique or a dense crossing graph.
- The two-direction support theorem assumes a connected cell complex, a simple outer boundary, and no pinched boundary vertices. Every hole-boundary incidence is explicitly charged; none disappears in the affine square-complex reduction.
- The zero-support classification in Theorem 10.12 is an exact finite turn-word check. The closed but rejected words repeat a boundary vertex; numerical polyomino enumeration is not being used as proof.

### Rattlers and disconnected graphs

- Contact-isolated vertices are retained as a genuine possibility.
- Theorem 12.4 does not conflate minimum- and maximum-contact representatives. It freezes the original contact-minimal core and every original diameter endpoint, then creates only bridge contacts while anchoring the other components.
- An original diameter pair remains fixed throughout the hybrid construction, so its diameter never silently falls below $`D(n)`$.
- The generic preliminary rotation separates coincident equal-radius translation circles; the subsequent ray avoids their intersections, so each new contact is unique.
- The bridge-forest count permits several fixed roots in one forest component; no false one-root or freely hinged-leaf assertion is used.
- In the maximal-contact representative, coincident active translation circles are handled explicitly: their new unit edges form a matching and cannot create a triangle.
- Euler formulas use the correct component term.

### Regression against the exact small minimizers

- The unit square lies in the zero-cone branch because every vertex is diametral; its single bounded contact face is the allowed $`90^\circ`$ rhombus.
- The five-rhombus cross is the exact nontrivial $`k=0`$ exception in Theorem 10.12. It blocks the stronger but false assertion that an internally equilibrated two-direction core must be a single rhombus.
- The regular unit pentagon also has every hull vertex diametral and supplies an arbitrarily extensible model for polygonal local rigidity.
- For $`n=6`$, the five hull vertices are diametral and the center is trapped by its five radial contacts; the contact graph is a tree, consistent with the threshold $`n<44`$.
- The $`n=7`$ hexagon-plus-center configuration is excluded by the triangle-free hypothesis exactly because its six center-side triples are unit triangles.
- For $`n=8`$, the regular unit heptagon plus its center lies in the flexible branch: all seven hull vertices are fixed diameter endpoints and the contact-isolated center can move. The attachment or maximum-contact selection moves it to a representative with additional anchoring, whereas contact minimization prefers the isolated representative. This confirms why the normalizations must not be conflated.
- The 11-point five-rhombus sun is triangle-free, has a regular-pentagon diametral hull, and has zero cone after exactly those hull vertices are pinned. Its contact distances and diameter $`\sqrt{5+2\sqrt5}`$ are checked exactly. The explicit 12-point triangular-lattice set of diameter (3) proves that the sun is not globally minimizing.
- The five-sector family has exactly $`5s^2+5s+1`$ vertices, $`5s^2`$ rhombi, $`10s`$ rhombic boundary edges, and a balanced $`C_5`$ blow-up on $`5s`$ tracks. With $`\varepsilon=s^{-3}`$ its positive total defect is $`8/s`$, while its boundary-pinned cone is still zero. It is not a jammed-branch counterexample because most of those pins are nonextreme and nondiametral.

### Conclusion

The Level I problem remains unresolved in this record. Target A is reduced to a super-boundary-dimensional bridge-forest capacity question; Target B is reduced to charging at least $`2\sqrt n-O(1)`$ forced bad track ends against the exact diametral shell budget. Both remaining statements are global finite-capacity comparisons, not omitted routine rigidity or train-track calculations.

---

## 20. References

1. P. Erdős, “Some problems in number theory, combinatorics and combinatorial geometry,” *Mathematica Pannonica* **5** (1994), 261-269. [Supplied PDF](../BIBLIOGRAPHY.md)
2. P. Bateman and P. Erdős, “Geometrical Extrema Suggested by a Lemma of Besicovitch,” *American Mathematical Monthly* **58** (1951), 306-314. [Supplied PDF](../BIBLIOGRAPHY.md)
3. A. Bezdek and F. Fodor, “Minimal Diameter of Certain Sets in the Plane,” *Journal of Combinatorial Theory, Series A* **85** (1999), 105-111. [Supplied PDF](../BIBLIOGRAPHY.md)
4. A. Schürmann, “On Extremal Finite Packings,” *Discrete & Computational Geometry* **28** (2002), 389-403. [Supplied PDF](../BIBLIOGRAPHY.md)
5. A. V. Bondarenko, D. P. Hardin, and E. B. Saff, “Minimal $`N`$-Point Diameters and $`f`$-Best-Packing Constants in $`\mathbb R^d`$,” *Proceedings of the American Mathematical Society* **142** (2014), 981-988. [Supplied PDF](../BIBLIOGRAPHY.md)
6. D. Eppstein, “Edge Bounds and Degeneracy of Triangle-Free Penny Graphs and Squaregraphs,” *Journal of Graph Algorithms and Applications* **22** (2018), 483-499. [Supplied PDF](../BIBLIOGRAPHY.md)
7. A. Bezdek, K. Bezdek, and R. Connelly, “Finite and Uniform Stability of Sphere Packings,” *Discrete & Computational Geometry* **20** (1998), 111-130. [Supplied PDF](../BIBLIOGRAPHY.md)

---

## 21. Addendum: an exact Oler-surplus decomposition for the defect shell

This addendum records the strongest new boundary-capacity result obtained in the
subsequent investigation.  It does not close Level I.  Its point is that the area,
perimeter, topology, holes, rhombic components, and vertices outside the rhombic
complex can be placed in one exact inequality with no unspecified boundary-order
constant.

Put

```math
a_0=\frac{\sqrt3}{2},\qquad c_0=\frac{\sqrt3}{4},\qquad
c=\frac{2\sqrt3}{\pi},\qquad
C_0=\pi\sqrt c=\sqrt{2\pi\sqrt3}.
```

### 21.1 The finite Oler inequality and an improved universal diameter bound

The following finite packing inequality is the unsummed cell inequality relevant to
the present boundary problem.

**Lemma 21.1 (Oler inequality).**  If $`X\subset K\subset\mathbb R^2`$, where
$`K`$ is convex, $`|X|=N`$, and the mutual distances in $`X`$ are at least $`1`$,
then

```math
\boxed{
N\le \frac{2}{\sqrt3}\operatorname{area}(K)
       +\frac12\operatorname{per}(K)+1.
}
\tag{21.1}
```

Equivalently,

```math
\boxed{
\operatorname{area}(K)+c_0\operatorname{per}(K)
\ge a_0(N-1).
}
\tag{21.2}
```

For completeness, the standard proof is the Dirichlet-cell proof of the finite
hexagonal packing inequality before its boundary terms are discarded.  Intersect the
Voronoi cells of $`X`$ with a polygonal approximation to $`K`$, and join each cell
center to the consecutive vertices of its clipped cell.  Every internal Voronoi side
is at distance at least $`1/2`$ from each of its two centers.  On the resulting
triangles, symmetrization about the side and

```math
\tan u+\tan v\ge2\tan\frac{u+v}{2}
```

give the regular circumscribed-hexagon value $`a_0`$ for each full cell after the
cell angles are summed.  Internal side terms cancel in pairs.  The uncancelled
boundary triangles contribute at worst $`c_0`$ times their total base length, and the
outer-face term in Euler's formula contributes one further $`a_0`$.  Thus

```math
a_0N\le \operatorname{area}(K)+c_0\operatorname{per}(K)+a_0.
```

Passing from polygonal approximations to an arbitrary convex $`K`$ proves (21.2).
This is also sharp: collinear unit chains and convex triangular-lattice patches give
equality.

Applying (21.2), the isodiametric inequality, and Cauchy's perimeter inequality gives
a universal improvement of (2.2):

```math
a_0(n-1)
\le \frac{\pi D(n)^2}{4}+c_0\pi D(n).
```

Consequently,

```math
\boxed{
D(n)\ge
\sqrt{\frac{2\sqrt3}{\pi}(n-1)+\frac34}
-\frac{\sqrt3}{2}.
}
\tag{21.3}
```

Thus the additive loss in the universal planar lower bound improves from $`1`$ to
$`\sqrt3/2=0.8660254037\ldots`$.  The constant check is important: this remains a
positive constant below the strict lattice-averaging upper bound
$`D(n)<\sqrt{cn}`$, so (21.3) alone cannot prove Erdős #99.

### 21.2 Exact topology-corrected shell window

Let $`A`$ be an $`n`$-point unit-separated set and put
$`K=\operatorname{conv}A`$, $`P=\operatorname{per}K`$.  Let $`\mathcal R`$ be
any finite edge-to-edge complex of strict unit-rhombus faces whose vertices belong to
$`A`$.  Write

```math
R=|\mathcal R|,
\qquad B=B_{\mathcal R},
\qquad v=|V(\mathcal R)|,
\qquad t=n-v,
```

and let $`\chi=\chi(\mathcal R)`$ be its Euler characteristic.  For a regular
planar complex with $`r`$ components and $`h`$ holes, $`\chi=r-h`$.  Define

```math
E_{\mathcal R}
=\sum_{F\in\mathcal R}
\left(\sin\theta_F-a_0\right),
\qquad
G_{\mathcal R}
=\operatorname{area}(K)-\sum_{F\in\mathcal R}\sin\theta_F.
\tag{21.4}
```

The edge-face incidence count and Euler's formula give the exact identity

```math
4R=2e-B,
\qquad
v-e+R=\chi,
\qquad
\boxed{v=R+\frac B2+\chi.}
\tag{21.5}
```

**Theorem 21.2 (Oler shell window).**  For every such complex,

```math
\boxed{
G_{\mathcal R}+E_{\mathcal R}
\ge
c_0(B-P)+a_0(t+\chi-1).
}
\tag{21.6}
```

If $`A`$ is a global diameter minimizer, then additionally

```math
\boxed{
G_{\mathcal R}+E_{\mathcal R}
<
c_0B+a_0(t+\chi).
}
\tag{21.7}
```

The difference between the right sides of (21.7) and (21.6) is exactly

```math
\boxed{c_0P+a_0.}
\tag{21.8}
```

In particular, all component, hole, and outside-vertex corrections cancel from the
remaining capacity window.

**Proof.**  Since the rhombi have disjoint interiors,

```math
\operatorname{area}(K)
=a_0R+E_{\mathcal R}+G_{\mathcal R}.
```

Insert this expression into (21.2), use $`n=v+t`$, and then use (21.5):

```math
\begin{aligned}
G_{\mathcal R}+E_{\mathcal R}
&\ge a_0(n-R-1)-c_0P\\
&=c_0(B-P)+a_0(t+\chi-1).
\end{aligned}
```

This proves (21.6).  For a global minimizer, Theorem 10.9 gives
$`D(n)^2<cn`$, and hence the isodiametric inequality gives
$`\operatorname{area}(K)<a_0n`$.  Therefore

```math
G_{\mathcal R}+E_{\mathcal R}
<a_0(n-R)
=c_0B+a_0(t+\chi),
```

which is (21.7).  Subtraction gives (21.8). $`\square`$

The theorem incorporates, with exact signs, all of the following quantities requested
in Target B: holes, multiple rhombic components, vertices outside the rhombic core,
and the full convex-hull perimeter.  A bridge forest outside the core is counted in
$`t`$.  The cancellation in (21.8) also shows why area accounting alone cannot prove
the super-boundary forest-capacity theorem: each outside vertex receives exactly one
bulk allowance $`a_0`$ on both sides.

For an ideal rhombic disk, $`t=0`$ and $`\chi=1`$, so (21.6)-(21.7) reduce to

```math
c_0(B-P)
\le G+\sum_F(\sin\theta_F-a_0)
<c_0B+a_0.
\tag{21.9}
```

This is the exact perimeter-refined version of the ideal budget (10.29).

### 21.3 Convex defect faces, pockets, and a local surplus decomposition

There is a useful local form of Theorem 21.2 in the jammed branch.

**Lemma 21.3 (convexity of simple contact faces).**  In the zero pinned-cone
branch, every simple bounded contact face is a strictly convex equilateral polygon.

Indeed, at a non-hull vertex the positive spanning relation in Theorem 8.2 makes every
angular gap between consecutive contact rays strictly smaller than $`\pi`$.  At a hull
vertex, every bounded face angle is contained in the strictly smaller-than-$`\pi`$
interior angle of the convex hull.  Thus every face angle is smaller than $`\pi`$.

Two immediate specializations of (21.1) are:

1. If $`F`$ is a convex equilateral $`m`$-gon whose vertices are unit-separated, then

   ```math
   \boxed{
   \operatorname{area}(F)\ge c_0(m-2).
   }
   \tag{21.10}
   
   ```

2. If $`C`$ is a convex pocket bounded by a chain of $`r`$ unit edges and its
   closing hull chord of length $`L`$, then

   ```math
   \boxed{
   \operatorname{area}(C)\ge c_0(r-L).
   }
   \tag{21.11}
   
   ```

For (21.10), use $`N=m`$ and perimeter $`m`$ in (21.1).  For (21.11), use
$`N=r+1`$ and perimeter $`r+L`$.  The vertices of a pocket are a subset of
$`A`$, so the separation hypothesis is automatic.

Suppose now that the full contact graph is connected, has a simple outer boundary,
and its bounded faces form a topological disk.  Its non-hull outer-boundary vertices
are reflex for the bounded region, because their outer-face angular gaps are smaller
than $`\pi`$.  Hence the indentation between consecutive hull vertices, together with
the hull chord, is a convex pocket to which (21.11) applies.

If the bounded contact faces have lengths $`m_F`$, the outer boundary has $`k`$
unit edges, and there are $`f`$ bounded faces, Euler and incidence counting give

```math
\sum_F(m_F-2)=2n-k-2.
\tag{21.12}
```

Writing

```math
s_F=\operatorname{area}(F)-c_0(m_F-2)\ge0,
\qquad
s_C=\operatorname{area}(C)-c_0(r_C-L_C)\ge0,
```

and noting that $`\sum_C(r_C-L_C)=k-P`$, one obtains the exact local identity

```math
\boxed{
\operatorname{area}(K)+c_0P-a_0(n-1)
=\sum_Fs_F+\sum_Cs_C.
}
\tag{21.13}
```

For a rhombus, its summand is exactly
$`s_F=\sin\theta_F-a_0`$.  Thus the global Oler surplus is literally the sum
of the strict-rhombus, exceptional-face, and indentation-pocket slacks.  This is the
local-cell decomposition that is lost when the finite packing inequality is used only
in its already-summed form.

A nonquadrilateral contact face has $`m\ge5`$, so (21.10) gives the sharp uniform
track-end charge

```math
\operatorname{area}(F)
\ge \frac{3c_0}{5}m
\ge \frac{3c_0}{5}\,r_F,
\qquad
\boxed{\frac{3c_0}{5}=\frac{3\sqrt3}{20}
=0.2598076211\ldots,}
\tag{21.14}
```

where $`r_F`$ is the number of rhombic boundary edges incident with $`F`$.
The constant is forced by pentagons and cannot be improved using only (21.10).

Let $`B`$ now denote the boundary-edge count of all rhombic faces in this regular
contact disk, and let

```math
G=\operatorname{area}(K)-\sum_{F\in\mathcal R}\operatorname{area}(F).
```

Partition the rhombic boundary edges into those incident with bounded
nonquadrilateral faces and those incident with the outer face.  Apply (21.14) to the
first class and (21.11) to the outer pockets.  A two-case comparison according as the
number of outer rhombic edges is at least $`P`$ gives

```math
\boxed{
G\ge\frac{3\sqrt3}{20}(B-P).
}
\tag{21.15}
```

If every bounded face is a rhombus, the sharper coefficient $`c_0`$ holds:

```math
\boxed{G\ge c_0(B-P).}
\tag{21.16}
```

Finally, in the jammed almost-rhombic regime,

```math
B\ge4\sqrt R=4\sqrt n-O(1),
\qquad
P\le\pi D<C_0\sqrt n.
```

Therefore

```math
\boxed{
B-P\ge(4-C_0)\sqrt n-O(1)
=0.7010916676\ldots\sqrt n-O(1).
}
\tag{21.17}
```

Under the regular contact-disk hypotheses, (21.15) yields the unconditional shell
area charge

```math
\boxed{
G\ge0.1821489584\ldots\sqrt n-O(1).
}
\tag{21.18}
```

In the pure rhombic-disk case, (21.16) improves this to

```math
\boxed{
G\ge0.3035815973\ldots\sqrt n-O(1).
}
\tag{21.19}
```

These are genuine boundary-order lower bounds.  The five-sector examples escape for
the correct global reason: their boundary perimeter is too large to satisfy
$`P<C_0\sqrt n`$.  The 11-point sun is below the asymptotic range and remains a
valid finite local regression example.

### 21.4 Constant audit and exact remaining lemma

The new estimates do not close Target B.  Define the Oler surplus

```math
\mathscr O(A)
=\operatorname{area}(K)+c_0P-a_0(n-1).
\tag{21.20}
```

Equation (21.13) decomposes it into nonnegative local face and pocket slacks.  For a
global minimizer,

```math
\mathscr O(A)
<c_0\pi D+a_0
<c_0C_0\sqrt n+a_0,
```

where

```math
\boxed{
c_0C_0
=\frac{\sqrt3}{4}\sqrt{2\pi\sqrt3}
=1.4284692103\ldots.
}
\tag{21.21}
```

Thus an affirmative closure by this route requires the genuinely new large-scale
stability estimate

```math
\boxed{
\mathscr O(A)\ge c_0\pi D+a_0
}
\tag{21.22}
```

for every sufficiently large triangle-free minimizer in the normalized rhombic/forest
regime, with the forest contribution included.  Equation (21.22) would imply

```math
\operatorname{area}(K)\ge a_0n+c_0(\pi D-P)\ge a_0n,
```

contradicting $`D^2<cn`$.

The bad train-track count by itself cannot prove (21.22).  The local constants
$`3\sqrt3/20`$, (21.18), and (21.19) are all below the required coefficient
(21.21), and the face and pocket inequalities can be approached arbitrarily closely
by near-triangular geometry.  What remains is a quantitative *simultaneous stability*
theorem: near equality in the local Oler cells must be incompatible, at large scale,
with both the diametral-hull condition and near equality in the isodiametric bound.

This addendum therefore narrows Target B and supplies its exact topology-corrected
bookkeeping, but it closes neither Target A nor Target B.  The most promising next
step is to prove a joint Oler/isodiametric stability inequality in which shallow
pockets with near-unit hidden diagonals are charged either to a definite support-width
loss or to a feasible diameter-decreasing boundary motion.  Target A must enter that
same inequality, since (21.8) proves that plain area accounting assigns a forest vertex
exactly the same bulk allowance as a core vertex.

---

## 22. Exact track-end depth and defect-extended span

This section incorporates the second continuation run. It does not solve Level I, but it removes one previously unquantified class of train-track terminations from Target B and complements the Oler-surplus bookkeeping of Section 21. Its first lemma strengthens Lemma 21.3 by proving that every bounded contact face has a single simple boundary cycle, rather than assuming simplicity.

Continue in the triangle-free first-order-jammed branch and let
$`\mathcal R=\mathcal F_4`$ be the full strict-rhombus face complex.  A boundary
edge of $`\mathcal R`$ is called **face-terminated** if the contact face on its
non-rhombic side is bounded.  Let $`b_F`$ be the number of face-terminated
rhombic boundary edges.

If a rhombic boundary edge $`e`$ instead borders the unbounded contact face,
orient its unit normal $`\nu_e`$ away from its incident rhombus and put

```math
 \rho_e=
 \max_{x\in A}\nu_e\cdot(x-m_e),
```

where $`m_e`$ is the midpoint of $`e`$.  Thus $`\rho_e=0`$ for a hull edge,
whereas $`\rho_e>0`$ for a non-hull edge on the unbounded contact face.  Put

```math
 H_\infty=\sum_{e\text{ bordering the unbounded face}}\rho_e.
```

### Lemma 22.1: bounded contact faces are strictly convex

Every bounded face of the contact graph has one simple boundary cycle and is a
strictly convex unit-sided polygon.

#### Proof

The straight unit-contact graph is plane.  At a vertex $`v\notin Q`$, Theorem
8.2 says that the contact directions positively span the plane.  Equivalently,
every angular gap between consecutive contact rays is strictly smaller than
$`\pi`$.  Every face angle at $`v`$ is one of these gaps and is therefore less
than $`\pi`$.

At a vertex $`v\in Q=V(\operatorname{conv}A)`$, the tangent cone of the convex
hull has angle strictly smaller than $`\pi`$, because $`v`$ is an extreme
polygon vertex.  A bounded face lies locally inside the convex hull, so its
face angle at $`v`$ is again smaller than $`\pi`$.

A bounded plane-graph face with an inner boundary component, a bridge slit, or
a repeated boundary vertex necessarily has a reflex corner on one of its
boundary walks.  The preceding paragraph excludes this.  Hence the boundary
is one simple cycle, and all its interior angles are smaller than $`\pi`$.
The face is therefore strictly convex.  Every one of its boundary edges is a
unit contact. $`\square`$

### Lemma 22.2: sharp width of a convex contact face

Let $`P`$ be a convex unit-sided polygon whose distinct vertices are mutually
at distance at least $`1`$.  Then

```math
 \boxed{\operatorname{width}(P)\ge\frac{\sqrt3}{2}.}
 \tag{22.1}
```

In particular, measured normally from any side of $`P`$, the opposite support
line is at distance at least $`\sqrt3/2`$.

#### Proof

A minimum-width direction of a convex polygon is normal to one of its sides.
Put that unit side at

```math
 A=(0,0),\qquad B=(1,0),
```

and suppose that the polygon lies in the strip $`0\le y\le w`$.  If
$`w<\sqrt3/2`$, set

```math
 a=\sqrt{1-w^2}>\frac12.
```

For any two vertices, their vertical separation is at most $`w`$, while their
Euclidean separation is at least $`1`$.  Their horizontal coordinates are
therefore separated by at least $`a`$.  No third vertex can have horizontal
coordinate strictly between those of $`A`$ and $`B`$, since it would be within
horizontal distance at most $`1/2<a`$ of one of them.  Thus $`A,B`$ are
consecutive in the ordering of all vertex coordinates by $`x`$.

If the polygon has $`m`$ vertices and horizontal span $`L`$, the one gap from
$`A`$ to $`B`$ has length $`1`$, and the other $`m-2`$ gaps have length at
least $`a`$.  Hence

```math
 L\ge1+(m-2)a.
```

The two boundary arcs between a leftmost and a rightmost vertex each have
length at least $`L`$.  Since the perimeter is $`m`$,

```math
 m\ge2L\ge2+2(m-2)a.
```

As $`m\ge3`$, this implies $`a\le1/2`$, a contradiction.  This proves
(22.1).  The constant is sharp, already for the unit equilateral triangle and
as a limiting constant for admissible equilateral polygons. $`\square`$

### Theorem 22.3: exact defect-extended train-span inequality

For each train track $`\tau`$, let

```math
 L_\tau=\sum_{F\in\tau}\sin\theta_F.
```

If $`s_F(\tau)\in\{0,1,2\}`$ is the number of its end edges that are
face-terminated, then

```math
 \boxed{
 L_\tau+\frac{\sqrt3}{2}s_F(\tau)
 +\sum_{e\in\partial\tau,\ e\text{ on the unbounded face}}\rho_e
 \le D.
 }
 \tag{22.2}
```

Consequently, since there are $`T=B_{\mathcal R}/2`$ tracks and every rhombus
belongs to two tracks,

```math
 \boxed{
 \frac{B_{\mathcal R}}2D
 \ge
 2\sum_{F\in\mathcal R}\sin\theta_F
 +\frac{\sqrt3}{2}b_F+H_\infty,
 }
 \tag{22.3}
```

or equivalently

```math
 \boxed{
 B_{\mathcal R}D
 \ge
 4\sum_{F\in\mathcal R}\sin\theta_F
 +\sqrt3\,b_F+2H_\infty.
 }
 \tag{22.4}
```

This strictly refines (10.18).

#### Proof

Orient the transverse coordinate of a train as in Theorem 10.6.  Crossing a
rhombus increases that coordinate by exactly $`\sin\theta_F`$, so the two end
edge midpoints differ in transverse coordinate by $`L_\tau`$.

At a face-terminated end, Lemmas 22.1 and 22.2 provide a vertex of the bounded
contact face at transverse distance at least $`\sqrt3/2`$ beyond the end-edge
line.  At an end bordering the unbounded contact face, the definition of
$`\rho_e`$ provides a vertex of $`A`$ at transverse distance $`\rho_e`$ beyond
that line.  Choosing such a vertex at each end gives two points of $`A`$ whose
transverse separation is at least the left side of (22.2).  Their Euclidean
distance is at most $`D`$, proving (22.2).

Sum over all tracks.  Each rhombus is counted on its two tracks, every
face-terminated edge is one track end, and every unbounded-face end contributes
its $`\rho_e`$ once.  This gives (22.3) and (22.4). $`\square`$

### Exact consequence and limitation

Every bad track end now has an explicit disposition:

1. a bounded-face end costs at least $`\sqrt3/2`$ of additional transverse
   span;
2. a non-hull end on the unbounded contact face costs its exact positive depth
   $`\rho_e`$;
3. a hull end has zero additional depth.

Thus bounded nonquadrilateral faces and bounded holes are no longer merely
combinatorial defect objects: they carry the sharp metric charge
$`\sqrt3/2`$ per incident train end.  The five-sector complexes and the
11-point sun evade this conclusion in precisely the correct way: their hard
train ends lie on the nonconvex unbounded boundary, rather than in bounded
defect faces.

The new term is boundary order and does not by itself finish Target B.  With
$`B_{\mathcal R}\ge4\sqrt{F_4}`$, the old product bound has order-$`n`$ slack,
whereas the new contribution in (22.4) is only order $`\sqrt n`$.  A closing
argument must therefore combine $`H_\infty`$ and the bounded-face term with
actual convex-hull perimeter or parallel-body area; substituting only
$`\operatorname{span}(\tau)\le D`$ still loses too much.

The exact remaining metric lemma after this continuation is an aggregate
outer-shell inequality that charges the compulsory non-hull unbounded-face
edges through their depths $`\rho_e`$, their convexification area, and the
actual perimeter of $`\operatorname{conv}A`$, with a coefficient strong enough
to beat the finite packing boundary slack.  Target A, the super-boundary
bridge-forest alternative, is unchanged.

---

## 23. Combined continuation frontier

Sections 21 and 22 attack the same boundary-scale obstruction from complementary sides. This section records the exact synthesis that should be treated as the current research frontier. It is a reduction and bookkeeping statement, not a Level I solution.

### 23.1 The bad train ends now have only two nontrivial dispositions

Continue in the triangle-free first-order-jammed branch and take the full strict-rhombus complex $`\mathcal R=\mathcal F_4`$. Let $`b_F`$ be the number of rhombic boundary edges whose non-rhombic side is a bounded contact face, and let $`b_\infty`$ be the number of non-hull rhombic boundary edges on the unbounded contact face. Then

```math
 b_F+b_\infty=b_{\mathcal R}\ge2\sqrt{F_4}-2=2\sqrt n-O(1).
\tag{23.1}
```

A bounded-face end has a universal metric charge $`\sqrt3/2`$ in the transverse train-span inequality. An unbounded non-hull end has an exact positive depth $`\rho_e`$, and their aggregate is

```math
H_\infty=\sum_{e\text{ on the unbounded face}}\rho_e.
\tag{23.2}
```

Thus the defect network can no longer hide a train end in an unquantified bounded face. The only soft escape is through many shallow non-hull ends on the unbounded face.

### 23.2 Directional train-width refinement

The proof of Theorem 22.3 yields a strictly stronger per-track inequality than the displayed diameter bound. Let $`\nu_\tau`$ be the oriented transverse unit normal of a train track and let

```math
w_K(\nu)=\max_{x\in K}\nu\cdot x-\min_{x\in K}\nu\cdot x
```

be the width of $`K=\operatorname{conv}A`$ in direction $`\nu`$. The two witness points used in the proof of Theorem 22.2 belong to $`A\subset K`$, so their transverse separation is at most $`w_K(\nu_\tau)`$. Hence

```math
\boxed{
L_\tau+\frac{\sqrt3}{2}s_F(\tau)
+\sum_{e\in\partial\tau,\ e\text{ on the unbounded face}}\rho_e
\le w_K(\nu_\tau)\le D.
}
\tag{23.3}
```

Summing over tracks gives the exact directional form

```math
\boxed{
\sum_\tau w_K(\nu_\tau)
\ge
2\sum_{F\in\mathcal R}\sin\theta_F
+\frac{\sqrt3}{2}b_F+H_\infty.
}
\tag{23.4}
```

This is the most direct bridge between the two continuation runs. Cauchy's formula

```math
P=\int_0^\pi w_K(\phi)\,d\phi
\tag{23.5}
```

controls the integral of the same width function, while the train geometry supplies a highly structured discrete multiset of directions. A closing argument may therefore be formulated as a sharp discrete-to-continuous width inequality rather than as another estimate involving only $`D`$.

### 23.3 Exact simultaneous inequalities for a surviving jammed counterexample

Such a counterexample must satisfy the Oler shell window

```math
G_{\mathcal R}+E_{\mathcal R}
\ge c_0(B-P)+a_0(t+\chi-1),
\tag{23.6}
```

```math
G_{\mathcal R}+E_{\mathcal R}
<c_0B+a_0(t+\chi),
\tag{23.7}
```

whose remaining allowance is exactly $`c_0P+a_0`$, together with the refined train inequality

```math
BD
\ge
4\sum_{F\in\mathcal R}\sin\theta_F
+\sqrt3\,b_F+2H_\infty.
\tag{23.8}
```

For regular contact disks, the Oler surplus

```math
\mathscr O(A)=\operatorname{area}(K)+c_0P-a_0(n-1)
\tag{23.9}
```

has the exact local decomposition

```math
\mathscr O(A)=\sum_F s_F+\sum_C s_C,
\tag{23.10}
```

where the summands are nonnegative face and indentation-pocket slacks. For global minimizers,

```math
\mathscr O(A)<c_0\pi D+a_0,
\tag{23.11}
```

and proving the reverse inequality for every sufficiently large triangle-free survivor would close the jammed branch.

### 23.4 The precise missing Target B theorem

The current Target B is no longer merely a generic ``sharp boundary-capacity theorem.'' A sufficient focused statement is:

> **Joint outer-shell stability theorem.** For every sufficiently large triangle-free global minimizer in the normalized jammed/almost-rhombic regime, the compulsory train-end data satisfy a quantitative inequality coupling $`b_F`$, $`H_\infty`$, the indentation-pocket slacks, the convexification area, and the actual hull perimeter strongly enough to force
> 

```math
> \mathscr O(A)\ge c_0\pi D+a_0.
> 
```

Equivalently, near equality in the local Oler cells must be incompatible at large scale with both the diametral-hull condition $`Q=V(\operatorname{conv}A)`$ and near equality in the isodiametric/perimeter bounds.

A particularly promising route is to replace the final use of $`\operatorname{span}(\tau)\le D`$ by the actual hull width in the train's transverse direction and then aggregate those directional widths through the support function or Cauchy perimeter formula. The unbounded-face depth $`\rho_e`$ is already a support-function deficit:

```math
\rho_e=h_K(\nu_e)-\nu_e\cdot m_e
```

for a non-hull outer train end. The missing step is therefore to convert the sum of these support deficits, together with the bounded-face charges, into the Oler/pocket surplus with a sharp enough coefficient.

### 23.5 Target A is now cleanly separated from plain area bookkeeping

The bridge-forest alternative remains:

```math
\ell=\dim\mathcal L_{\widehat Q}=\omega(\sqrt n).
\tag{23.12}
```

Section 21 shows why simply adding forest vertices to the Oler area count cannot eliminate this branch: the topology/outside-vertex terms cancel from the global shell window. A successful Target A argument must therefore exploit information not visible to plain area alone, for example the configuration-space dimension of the forest, free volume, saturation by new constraints, or a coupling between forest occupancy and the same outer-shell support resources charged in Target B.

The most attractive unified endpoint would prove that every forest degree of freedom or every forest vertex consumes a definite amount of the same support-function/pocket budget appearing in the joint outer-shell stability theorem. Such a theorem would simultaneously force $`\ell=O(\sqrt n)`$ and close Target B on the resulting $`n-O(\sqrt n)`$ jammed core.

### 23.6 Current exact status

No Level I proof or disproof is established. The two remaining tasks are now:

1. **Target A:** rule out super-boundary-dimensional bridge-forest lineality, preferably by charging forest freedom to finite shell capacity;
2. **Target B:** prove the joint Oler/isodiametric/track-depth stability theorem above, with constants strong enough to exceed the global-minimizer allowance.

Sections 21--23 supersede the less quantitative formulation of the Target B endpoint in Sections 18--19. The older statements remain valid, but the present formulation is the sharper continuation state.
