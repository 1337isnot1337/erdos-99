> Generated reading edition · [exact source](../../../docs/reports/target_c_near_diameter_path_unloaded_core_2026-09-09.md) · source SHA-256 `cc03dc8b609ffab59227ada06562658eb9c7c4993b6eede2203da7dc821be609`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-82D214D1CBC9","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — diameter-lens exclusion and an unloaded near-chain core

**Date:** 2026-09-09

**Repository base:** `7838f6c0aabe0e3d63369bda804643c3c7833426`

**Run type:** proof / adversarial audit / partial campaign handoff

**Target:** Target C near-chain stability; C100–C102

**External search:** used to check the electrical/Kalmanson and Hoffman dependencies

**Computation:** exact standard-library regression script, linked below

## LEVEL I STATUS

**STILL OPEN.** This report does not certify exhaustion of all serious routes or
logical independence of any remaining theorem. Its first version was preserved and
pushed at the user's request; the continued run adds the sharp length-excess
constant, stress bounds, and a separate C-I dependency audit. It has not completed
the requested repository-wide campaign or a Level I proof/disproof.

The new result is an elementary diameter-lens theorem. It removes possible diameter
loading from every internal vertex of a sufficiently uniformly aligned diameter
contact path. A second version requires only small path-length excess and removes
loading from all but an explicitly bounded number of end vertices. Neither result
requires PSD, KKT, a rhombic disk, or global optimality.

These results are **unpromoted**. Their application to later C100–C102 statements
is explicitly dependent on those statements, whose indexing conflicts with the
older Target C route map. No canonical route map is changed by this report.

## 1. Starting endpoint and intended implication

C102's one-leaf near-chain branch has a diameter path with uniformly small angular
error, small total turning, and small length excess. Its frontier explicitly asks
whether enough internal vertices can be shown non-extreme to recover C97's strip.

The useful chain is:

```text
uniformly aligned diameter path
  -> all internal path vertices are non-diametral (new theorem)
  -> all those vertices are unloaded under every KKT stress
  -> in a contact-minimal source they are also non-extreme
  -> remaining obligation: transverse-contact/strip and prefix stability
  -> if that obligation produces a finite release or strict sub-D competitor,
     contradiction in this C-II subbranch.
```

The implication from non-diametrality to the strip is NOT proved. Section 5 gives
an exact counterexample to a local shortcut at precisely that step.

## 2. Diameter-lens exclusion theorem

Let A be a finite planar set of diameter D>0, and let z,a in A satisfy |z-a|=D.
Choose coordinates z=(0,0), a=(D,0). Write p=(t,h) in A, with p distinct from z,a,
and put m=min(t,D-t). Necessarily 0<t<D, hence m>0.

Set

```math
\kappa_*=2-\sqrt3=\tan(\pi/12).
```

### Theorem L1 — a universal non-diametral diamond

If |h|<κ_* m, then p is not an endpoint of any diameter pair of A.

More quantitatively, if |h|≤κm with 0≤κ<κ_*, then for every y in A,

```math
|p-y|^2\le D^2-A_\kappa Dm,
\qquad
A_\kappa=\frac{1-2\sqrt3\kappa-\kappa^2}{2}>0.
\tag{L1}
```

### Proof

Every y=(s,v) in A lies in the lens

```math
\overline B(z,D)\cap\overline B(a,D).
```

Consequently 0≤s≤D and

```math
v^2\le\min\{D^2-s^2,D^2-(D-s)^2\}\le3D^2/4.
```

For q=(t,0), the exact convex-combination identity gives

```math
|q-y|^2
=(1-t/D)|z-y|^2+(t/D)|a-y|^2-t(D-t)
\le D^2-t(D-t).
```

Therefore

```math
|p-y|^2\le D^2-t(D-t)+h^2+\sqrt3D|h|.
\tag{L2}
```

Use t(D-t)=m(D-m), |h|≤κm, and m≤D/2. The right side is at most

```math
D^2+m[-D+(1+\kappa^2)m+\sqrt3D\kappa]
\le D^2-\frac{1-2\sqrt3\kappa-\kappa^2}{2}Dm.
```

The coefficient is positive exactly when 0≤κ<2−√3. This proves (L1).
If |h|<κ_*m, choose κ between |h|/m and κ_* and apply (L1). Every distance from
p is strictly below D. □

### Sharpness of the constant under diameter alone

At diameter scale one, take

```math
z=(0,0),\quad a=(1,0),\quad
p=(1/2,1-\sqrt3/2),\quad y=(1/2,-\sqrt3/2).
```

Four squared pair distances are 1; the other two, |p-z|² and |p-a|², are
2−√3. In particular |p-y|=1 and |h|/m=2−√3. Thus replacing the strict
inequality by equality, or increasing κ_*, fails.

Multiplying the coordinates by √(2+√3) makes pz and pa unit contacts.
The diameter is √(2+√3), the contact graph is the path z–p–a plus isolated y,
and its two forward path directions make angles ±15° with za. This is an exact
unit-separated triangle-free regression. It is not globally optimal for four
points: the unit square has strictly smaller diameter √2. It also contains a
diameter equilateral triple z,a,y, excluded by the large-global-minimizer
anti-Reuleaux theorem. Sharpness here is asserted only under diameter alone.

## 3. Every internal vertex of a narrow diameter path is unloaded

### Theorem L3 — the 15-degree contact-path theorem

Let z=x_0,x_1,...,x_k=a be a unit-edge path in A, where |z-a|=diam(A)=D.
Let u=(a-z)/D. Suppose every forward unit vector e_j=x_j−x_{j−1} makes angle
at most θ with u, for a fixed 0≤θ<π/12. Then no internal x_i is a diameter
endpoint. In fact, with κ=tan θ, every y in A satisfies

```math
|x_i-y|^2\le D^2-A_\kappa D\cos\theta\min(i,k-i)
\qquad(1\le i<k).
\tag{L3}
```

### Proof

In the coordinates of Section 2, write x_i=(t_i,h_i). Forward projection gives

```math
t_i\ge i\cos\theta,\qquad D-t_i\ge(k-i)\cos\theta.
```

Summing transverse components from either endpoint gives

```math
|h_i|\le\sin\theta\min(i,k-i).
```

Thus, with m_i=min(t_i,D−t_i),

```math
|h_i|\le\tan\theta\,m_i,
\qquad m_i\ge\cos\theta\min(i,k-i)>0.
```

Apply (L1). Since tan θ<κ_*, the resulting deficit is strictly positive. □

### Exact Target C consequences

1. Every internal path vertex has no diameter reaction under **any** KKT stress,
   because no actual diameter pair uses it.
2. In a contact-minimal triangle-free global minimizer, Theorem 6.1 of
   [local structure](../theory/01-local-structure.md) implies that these nonisolated,
   non-diametral vertices are positively surrounded and are not convex-hull
   vertices. Their contact degrees are 3, 4, or 5, not automatically 4.
3. Under the later C100 uniform-cone theorem, put b=β_za and ρ=(1−b)/b.
   If

   
   ```math
   b>\frac1{1+\sin(\pi/12)},
   ```


   then θ=arcsin ρ<π/12. A shortest separator path has no internal diameter
   endpoint. Thus **every** internal vertex is unloaded eventually in the C98–C102
   one-leaf regime b→1. Neither C102's total-variation estimate nor an exact
   straight-chain endpoint is needed for this consequence.

## 4. A topology-independent length-excess version

The continued run sharpened the original end-piece constant. The following
angle bound yields the sharp constant, rather than the earlier estimate
1+1/(1−cos 15°).

### Theorem L2 — a 150-degree angle ceiling at another diameter endpoint

If p is another diameter endpoint of A, then

```math
\angle zpa\le5\pi/6.
\tag{AG}
```

### Proof

If p lies on za, with p distinct from its endpoints, the convex-combination
identity in Section 2 already gives |p−y|<D for every y in A, a contradiction.
Thus h≠0. Put θ=∠zpa. The dot product and unsigned cross product of z−p,a−p
give

```math
\cot\theta=\frac{t^2+h^2-Dt}{D|h|}.
```

If θ>5π/6, this is less than −√3. Equation (L2) would then give

```math
|p-y|^2\le D^2+D|h|(\cot\theta+\sqrt3)<D^2
```

for every y in A, again a contradiction. □

The four-point lens example attains equality: its angle at p is 150°.

### Theorem L4 — diameter endpoints are confined to short end pieces

For any unit-edge path z=x_0,...,x_k=a joining diameter endpoints, put δ=k−D≥0
and

```math
C_{\rm det}=\frac1{2-\sqrt{2+\sqrt3}}.
```

If an internal x_i is an endpoint of any diameter pair, then

```math
\min(i,k-i)\le C_{\rm det}\delta.
\tag{L4}
```

In particular there are at most 2⌊C_det δ⌋ such internal vertices (and of course
at most k−1). No angular, stress, train, or optimality assumption is required.
The coefficient C_det is sharp for the class of arbitrary unit-separated sets.

### Proof

Write r=min(|p-z|,|p-a|), s=max(|p-z|,|p-a|), and θ=∠zpa. By (AG) and
the cosine law,

```math
D^2=r^2+s^2-2rs\cos\theta\le r^2+s^2+\sqrt3rs.
```

For q=s/r≥1, the function

```math
f(q)=1+q-\sqrt{1+q^2+\sqrt3q}
```

is strictly increasing: its derivative is positive because
4(1+q²+√3q)−(2q+√3)²=1>0. Consequently, with
γ=2−√(2+√3)=f(1)>0,

```math
r+s-D\ge\gamma r,\qquad D\le s+(1-\gamma)r.
```

The path's length k=D+δ is at least r+s, so r≤δ/γ. Let j be the number of
path edges from the endpoint nearer p in Euclidean distance to p. The other
piece has length at least s, hence

```math
j\le k-s\le\delta+(1-\gamma)r\le\delta/\gamma.
```

Since min(i,k−i)≤j, (L4) follows. Count integer indices at the ends for the
cardinality bound. In the unit-scaled sharp lens example, k=2,
D=√(2+√3), δ=γ, and the internal diameter endpoint has i=1. Thus equality
holds in (L4), proving sharpness. □

For δ=o(D), the path has a consecutive D−o(D) internal core with no diameter
endpoints. Conditional on the later PSD/contact-distance bound k≤D/√b, the
number of possibly diameter-loaded internal vertices is at most

```math
2\left\lfloor C_{\rm det}D(b^{-1/2}-1)\right\rfloor.
```

This transfers the new unloading result beyond pure-rhombic topology.

### Total-turn corollary

If the sum of the unsigned turns between consecutive forward path edges is less
than π/6, no internal path vertex is diametral. Indeed choose continuous edge
angle lifts along the path. Their range is no greater than the total turn,
hence less than π/6. The vector sums of every nonempty prefix and suffix lie in
that same cone. Thus their directions differ by less than π/6, and the angle
z x_i a exceeds 5π/6, contradicting (AG) if x_i were diametral.

This offers an independent use of C102's total-variation conclusion, in addition
to L3's use of C100's uniform alignment. It does not make a bent path straight.

## 4A. Dominant diameter forces stress into unloaded-to-unloaded contacts

The next implication is a quantitative refinement of the one-leaf branch:

```text
dominant diameter weight b -> small weighted path excess
  -> few diameter-endpoint visits (L4)
  -> almost all contact stress joins two non-diametral vertices (L5)
  -> remaining obligation: turn this unloaded stress bulk into an exact
     transverse/terminal defect cost, not just a count of positive edges.
```

### Theorem L5 — an explicit diameter-boundary stress bound

Let A be a finite planar unit-separated set of diameter D, with a normalized
nonnegative KKT stress: contact weights α_e, actual diameter weights β_h,
Σ_h β_h=1, and equilibrium at every vertex. Zero weights are allowed. Fix a
diameter za of weight b≥1/2. Let B be the set of **all actual diameter endpoints**,
not merely endpoints with positive β. Let E' be the contact edges incident to
B\{z,a}, and E_B all contact edges incident to B. Then

```math
\sum_{e\in E'}\alpha_e\le 8C_{\rm det}(1-b)D^2,
\tag{LB1}
```

```math
\sum_{e\in E_B}\alpha_e
\le 2D(2b-1)+8C_{\rm det}(1-b)D^2.
\tag{LB2}
```

Thus, if D→∞ and b→1, contacts whose two endpoints are non-diametral carry
D²−o(D²) total stress. Neither PSD, full positive support, contact minimality,
nor global optimality is required for this theorem.

### Proof

Use the equilibrium convention
Σ_j α_ij(p_i−p_j)=Σ_j β_ij(p_i−p_j). Dot each equation with p_i and sum.
Every contact contributes α_e and every diameter contributes β_h D², giving
Σ_e α_e=D².

For any z–a vertex cut, the diameter za contributes a vector of length bD to
the summed equilibrium, while all other crossing diameter reactions have total
length at most (1−b)D. Unit contact forces across that cut therefore have total
capacity at least F=D(2b−1). Max-flow/min-cut supplies a contact flow of value
exactly F. Cancel cycles and decompose the resulting directed flow into simple
z–a paths P with weights x_P≥0. Write k_P for the unit-edge length of P and
f_e=Σ_{P containing e}x_P for the resulting nonnegative edge usage. The
decomposition has no opposite-direction cancellation, and 0≤f_e≤α_e.

Set

```math
M=\sum_e f_e=\sum_P x_P k_P,
\qquad E=\sum_Px_P(k_P-D)=M-DF.
```

Then DF≤M≤D², and the total unused contact capacity is U=D²−M.
These facts also reprove the geodesic-flow input used here; they do not import
any of its downstream C65/C98 assumptions.

By L4, P visits B\{z,a} at no more than 2C_det(k_P−D) internal indices.
Each such visit accounts for at most two path edges incident to that set.
Consequently

```math
\sum_{e\in E'}f_e\le4C_{\rm det}E.
```

Adding unused capacity, and using 4C_det>1, gives

```math
\begin{aligned}
\sum_{e\in E'}\alpha_e
&\le4C_{\rm det}(M-DF)+D^2-M\\
&\le4C_{\rm det}(D^2-DF)
=8C_{\rm det}(1-b)D^2.
\end{aligned}
```

A simple path has at most two additional edges incident to z or a (one at each
end). Its E_B edge count is therefore at most two plus its preceding bound.
Sum with weights x_P, using Σ_P x_P=F, and repeat the unused-capacity estimate
to obtain (LB2). Subtract (LB2) from Σ_e α_e=D² for the final conclusion. □

### Adversarial scope check

The bound counts **stress**, not edges, vertices, faces, or Oler surplus.
Arbitrarily many tiny positive transverse stresses remain allowed. It gives no
uniform lower bound on a strict response minor or on a terminal-twist cost.
The local star in Section 5 illustrates the small-weight issue but is not a
counterexample to L5, because it lacks global equilibrium. Regular stressed
shells have no diameter weight approaching one; inactive isolated points carry
no α and do not invalidate the estimate. No claim about their number is made.
In particular L5 does not repair the force-bulk transport failure recorded by
the heptagon-plus-center regression.

### Theorem L6 — direct support and tensor bounds improve the constants

A subsequent adversarial simplification improves L5 without using a path at all.
Under the same KKT hypotheses, now for any 0≤b≤1, write η=1−b. Then

```math
\sum_{e\in E'}\alpha_e\le4\eta D^2,
\qquad
\sum_{e\in E_B}\alpha_e\le D(1+b)+5\eta D^2.
\tag{LB3}
```

These are the preferred numerical bounds. L5's path-visit estimate remains valid
but its constant is not competitive; its value is the geometric control of
individual paths, not a claim of a best stress estimate.

**Proof.** For any actual diameter endpoint p choose an actual partner q.
For every unit-contact neighbor x, the bound |q−x|≤D gives

```math
(p-q)\cdot(p-x)\ge\tfrac12.
```

Put s_p=Σ_{h incident to p}β_h and g_p=Σ_h β_h(p−p_h). Equilibrium and
|g_p|≤Ds_p therefore give

```math
\tfrac12\sum_{e\ni p}\alpha_e
\le(p-q)\cdot g_p\le D^2s_p.
```

Since Σ_{p∈B\{z,a}}s_p≤2η, summing proves the first bound. It also shows
directly that an actual diameter endpoint with s_p=0 has no positive contact
stress; weak diameter endpoints have not been silently omitted.

For the second bound put u=(a−z)/D and let w be a perpendicular unit vector.
The KKT tensor identity, obtained by multiplying equilibrium by the coordinate
p·w and summing, is

```math
\sum_{e\in C}\alpha_e(e\cdot w)^2
=\sum_{h\in H}\beta_h(h\cdot w)^2\le\eta D^2,
```

where e and h are their geometric edge vectors. At z, take outward axis −u,
and at a take outward axis u. Each incident unit-contact direction has projection
c≥1/(2D)>0 onto its outward axis. Thus 1−c≤1−c²=(e·w)². Summing at z and a,
the total incident contact weight is at most

```math
g_z\cdot(-u)+g_a\cdot u
+\sum_{e\text{ incident to }\{z,a\}}\alpha_e(e\cdot w)^2
\le D(1+b)+\eta D^2.
```

Here za contributes 2bD to the projected reactions; each other diameter is
incident to at most one of z,a and the sum of its possible contributions is at
most ηD. No transverse term is double-counted: the only edge that could join
z and a is parallel to u and has zero transverse term (it is a contact only when
D=1). The incident weight may double-count that edge, which only strengthens
the upper bound for its union. Add the already proved 4ηD² bound for E'. □

This simplification is important for the campaign: contact-stress concentration
does not in itself require the new near-path geometry. Its still-missing
conversion to an exact finite escape must not be mistaken for a path-counting
problem already solved by L4.

### Sharp endpoint term and an exact failure of stress-only closure

For every integer k≥2, the k+1 points p_j=(j,0), 0≤j≤k, have D=k,
unit-contact path edges of weight α=k, and the sole diameter of weight β=1.
All vertex equilibrium equations hold, including the endpoint equations, and
Σα=k². Exactly two contact edges meet a diameter endpoint. Hence their total
stress is 2k, attaining (LB2) at b=1, while unloaded-to-unloaded edges carry
k²−2k. Even the signed stress matrix is PSD: for any scalar f,

```math
k\sum_{j=0}^{k-1}(f_{j+1}-f_j)^2-(f_k-f_0)^2\ge0
```

by Cauchy–Schwarz. Thus full positive support, PSD and perfect dominant-flow
concentration alone do not exclude arbitrarily long triangle-free chains.

**Exact missing source hypothesis:** these are neither contact-minimal global
sources nor global optima. The k+1 integer points
{(0,0)}∪{(1,j):0≤j≤k−1} are unit separated, triangle free, and have squared
diameter 1+(k−1)²<k². This is a strict smaller-diameter competitor for every
member of the family. The canonical one-dimensional exclusion already removes
this family; it is recorded here only to certify the limits and sharp endpoint
term of the new stress bound, not to reopen that canonical branch.

## 5. Exact failure of the next local shortcut

The stronger claim

> positive equilibrium at an unloaded vertex on an arbitrarily nearly straight
> diameter contact path forces degree four and off-path contacts on both sides

is false under these local hypotheses.

For rational 0<t≤1/10, set c=(1−t²)/(1+t²), s=2t/(1+t²), and take

```math
L=(-c,-s),\quad p=(0,0),\quad R=(c,-s),\quad U=(0,1).
```

The contacts are exactly Lp, pR, pU. All three have length one;
|L−R|²=4c² and |L−U|²=|R−U|²=2+2s. Since 0<s<1/2,
4c²>2+2s>1. Thus LR is the unique diameter and p is nondiametral.
At p there is strictly positive equilibrium

```math
1(L-p)+1(R-p)+2s(U-p)=0.
```

The two forward path directions are (c,s),(c,−s), tending to the common diameter
direction as t→0. Nevertheless p has degree three and only one off-path contact.
The off-path stress 2s tends to zero.

**Missing global hypotheses:** U is unloaded with contact degree one, so this
configuration has no full positive global KKT contact equilibrium. It is not a
pure rhombic disk, and a unit square beats its diameter. It does not disprove a
global C-II strip theorem. It proves that L3 plus local positive equilibrium alone
cannot supply that theorem, and illustrates why small turning does not quantize
small positive transverse forces into zero forces.

## 6. Repository drift and closure audit: findings, not promotion

### Target A

The active prompt is version 1.7.10, through Section 167. The route map explicitly
indexes Sections 168–174. Section 174 therefore supplies the current tube-shield
endpoint, not the prompt's earlier source-labeling task. The top-level map's
Section-167 description is also stale relative to the detailed route map.

The September 5 sink-surplus report gives the exact algebraic reformulation

```math
s=|C^\partial|-|O|+j_*,\qquad
\zeta-s=|O|-\operatorname{rank}S-j_*.
```

Its shield sufficient condition becomes

```math
\sum_i\max(0,|O_i|-|C_i|)+|O_{\rm iso}|
\ge j_*+|\widehat W_\Sigma\setminus O|.
```

This reformulation does not prove the inequality. Nor does the boundary-order
inner-source defect bound identify that defect with Schur demand.

The subsequently fetched [September 8 tube-only cut report](target_a_tube_only_cut_2026-09-08.md)
sharpens the shield charge using the actual alternating orientation. Its bound is
ζ≥t_Σ+δ_Σ−|T_Σ|, where t_Σ counts shield terminals and δ_Σ is the sum of
positive sector surpluses. Its proof only charges a linkage path when it visits
a right-shore tube vertex; every visit to the basis-closed shield entails such
a visit. The exact new sufficient population condition is
t_Σ+δ_Σ≥s+|T_Σ|. This focused check finds no gap in that combinatorial
refinement, but supplies no stress-generated shield satisfying the condition.

### Target B

The later coherent-phase work is conditional on its dense-core/coherence and
near-saturation hypotheses. The September 5 dual-tree correction rejects a false
global linear ordering of disjoint crosscuts: their complement dual is a tree.
Dense crossing pairs yield an almost-spanning path in that tree and thereby repair
the grid-extraction step. This does not supply the missing global deficit transfer
or the topology-correct shell inequality. It is not a Level I closure.

### Target C

The route map and foundational module still leave universal PSD and C-I open.
Later C52–C54/C63 files claim universal PSD and C-I closure. Higher numbering and
the branch-consolidation report alone do not authorize promotion.

The C52.R algebra and C63 correction mechanism survived the focused checks in this
run. Here is a shorter independent verification of C52.R. Let L have zero row sums,
L_ij=−γ_iγ_j s_ij off the diagonal, γ_i>0, Robinson similarities s, and Lt=0 for
strictly increasing t. Set A=Γ⁻¹L, let D_f be first differences, and let T be
cumulative summation with D_f T=I. Then H=D_f A T has nonpositive off-diagonal
entries by the Robinson inequalities and H(D_f t)=0, where D_f t>0.
The similar matrix diag(D_f t)⁻¹H diag(D_f t) has zero row sums, nonpositive
off-diagonal entries and nonnegative diagonal entries. Its Gershgorin disks lie
in the closed right half-plane. The spectrum of H is that of A on the quotient
by constants; A is similar to the real symmetric Γ⁻¹/²LΓ⁻¹/². Thus all those
eigenvalues are real and nonnegative, and L is PSD.

C53's finite chord-sign check was independently reproduced exactly: all triples
of pairwise intersecting chords on convex-parabola polygons with three through
six vertices, all projective cuts, and all circular intervals give the nineteen
listed signed triples. This checks the finite sign table; it is not by itself a
new universal packing theorem or a substitute for checking the geometric reduction.

For C63, the essential hypothesis is PSD of **every** normalized stress on
**arbitrary** displacement fields. Under it, every fixed-base correction system
A_* y≥−g_*(x) is Farkas-feasible. A fixed-matrix Hoffman bound controls y by the
negative residual; the quadratic remainder contracts for sufficiently small x.
The resulting correction to tv is O(t²), preserving weak first-order release.
No uniform-in-n Hoffman constant is needed. This supports, rather than refutes,
the later proof mechanism; it does not justify declaring all downstream modules
audited. Canonical promotion is deferred to a dedicated dependency-complete audit.

### Remote-state reconciliation before publication

During the push preparation, `origin/main` advanced to `d4c46e6`, adding the
[September 8 force-bulk/correction audit](target_c_force_bulk_and_correction_audit_2026-09-08.md)
and [campaign ledger](../publication/provenance.md#historical-navigation). Its exact heptagon-center
regression reinforces the need to retain interior isolates. Its quadratic-program
regression also reinforces the all-displacement premise in C63.

That report additionally says a September 5 pentagon regression already rejected
C53.T. The referenced witness/correction was not found in the fetched tree, and
the fetched C53 module still contains the original claimed proof. The remote
report describes pre-existing working-tree corrections in another workspace;
those corrections may account for the provenance mismatch. Its specific claim
of prior rejection is therefore unresolved here, not silently adopted or dismissed.
The 27,252 checks above test the stated finite chord lemma and pass, but cannot
resolve a missing witness without knowing its exact statement and coordinates.
No universal PSD or C-I theorem is promoted. L1–L4 do not depend on this conflict.

### Continued audit superseding the preceding provisional assessment

The separate [C53 sign and C-I dependency audit](target_c_c53_sign_and_ci_dependency_audit_2026-09-09.md)
now supplies a convexity-preserving deformation to justify the finite sign
reduction for every strictly convex polygon. It proves the checked-in C53.T
signature, rather than merely testing sample geometries, and gives complete
Robinson/response and Farkas–Hoffman derivations of universal PSD and C-I closure
from the listed canonical inputs. This is a focused audited result, not yet a
route-map promotion and not an audit of every downstream numbered module.

The next remote update, `c26d6ab`, delivered the pentagon witness. Section 1A
of the separate audit now rejects it exactly: the reported order `f,g,e` uses
the cut `[0,pi)`, but its chosen x-positive orientation requires order `e,f,g`.
The consistent signed triples are `(1,0,-1)` and `(1,1,0)`, respectively, and
both obey C53.T. This resolves the missing-witness provenance. The route map
promotes that rejection only, pending coordinated promotion of the full C-I audit.

The same update delivered a near-chain report with an exact degree-five
rhombic-star regression, including a positive local stress floor and vanishing
area excess. This strengthens the warning in Section 5: imposing a local stress
floor still does not recover degree four. Its path endpoints are not the full
patch diameter endpoints, and global KKT/optimality is not established, so it
does not refute L3/L4 or a source-level strip theorem.

## 7. Branch ledger after continuation

This is a ledger of the branches inspected or reached, not a claim that every
serious mathematical route was exhausted. “Reduced” records an exact obligation,
not independence from the theorem library.

| Branch / hypotheses | Available inputs and target quantity | Attempt / status | Regression or exact remaining attack |
| --- | --- | --- | --- |
| A, fixed source hull | Exact hull capacity | Over-capacity Hall shortcut rejected | Capacity flag attains the ceiling; need new global information |
| A, Section-174 locked shield | Sector locality, basis balance; ζ≥s | Reduced to displayed sink surplus | Full-rank/annular/SDR regressions prevent local-count closure |
| A, zero slack | Actual source labels; inner defect r≤12d+9 | Reduced | No proved transport from r to ζ or s |
| A, vanishing strain | Five-block finite rearrangement and quartic barriers | No new closure | Exterior compatibility and strain/support regime still required |
| B, coherent near-saturated core | Promoted PC/PW/CR/PS/IS/TS/NE; phase cuts and coherent crossing families | Conditional phase-star and near-extremal-core exclusions retained | Must derive NE's coherence/coverage/near-extremality hypotheses globally |
| B, positive phase deficits | Virtual missing area and support depth | Reduced | Transfer deficits/interface population to actual shell currency |
| B, general topology | Exact Section-36 Oler shell window; HA for edge-aligned rhombic holes | Reduced | Prove Oler surplus ≥(√3/4)P, equivalently G+E≥(√3/4)B+(√3/2)(t+χ−1), with all corrections |
| C-I | Strong/weak duality; arbitrary-stress circular response | **Closed by contact-minimality contradiction in the separate dependency audit**, not yet canonically promoted | Convex-deformation finite sign proof plus all-displacement PSD; not ordinary KKT alone |
| C-II, absolute response gap | ε=tr(Λ−L_H)/2 | Reduced | No contradiction from ε bounded below has been supplied |
| C-II, bridges | Macroscopic reciprocal cut and loaded-block cost | Reduced | Exclude bridge stress α_e≥cD with crossing diameter mass ≥c |
| C-II, inactive rattlers | Fully inactive points outside positive core under C65 | Reduced | Force-bulk transport or a source-preserving competitor |
| C-II, Dε→0, multi-port | C66–C71 mechanical/electrical star concentration | Reduced | Force nonvanishing off-star response mass from a return component |
| C-II, Dε→0, single port | C98 gives b→1; C100 gives uniform path alignment | **Advanced by L3:** every internal path vertex is nondiametral | Transverse-contact and variable-prefix stability remain |
| C-II, arbitrary near-geodesic topology | k=D+o(D) | **Advanced by L4:** D−o(D) consecutive unloaded core | Control defects and tiny side stresses, not merely loaded vertices |
| C-II, any normalized stress with b→1 | Cut flow, tensor identity, diameter support inequality | **Advanced by L5/L6:** D²−o(D²) stress joins two non-diametral vertices; L6 improves the constants without paths | Need an exact transverse/terminal defect lower bound; no stress-to-population conversion proved |
| C-II, exact pure chain | Later C97 / no-geodesic report | Existing subcase exclusion, not new | Exact equality cannot be substituted for near equality |
| Local near-chain degree-four shortcut | Unloaded p; positive local equilibrium | **Disproved exactly**, Section 5 | Global KKT / rhombic compatibility must enter |
| Bare regular odd shells | D_h≥h/π; D(h)<√((2√3/π)h) | Strictly beaten for odd h≥11 | Filled shells have different cardinalities and are not covered |
| Filled-shell disproof | Feasible asymptotically dense triangle-free sets | No global certificate | Need infinitely many cardinalities with a proved sharp lower bound |

After the focused C-I dependency audit, the shortest currently identified single
all-branch C-route obligation remains the fully force-visible contradiction theorem:
exclude sufficiently large contact/diameter-lexicographically minimal triangle-free
global minimizers with full positive KKT support on every actual contact and diameter
pair, while retaining any fully inactive rattlers. L3 does not replace that theorem
by a one-branch near-chain claim.

## 8. Literature and computation

- Stefan Forcey, [Circular planar electrical networks, Split systems, and
  Phylogenetic networks](https://arxiv.org/pdf/2108.00550), Theorems 3.7 and 4.2:
  connected circular-planar positive networks have a Kalmanson boundary resistance
  metric, and such a metric has a circular split representation. This matches the
  C52/C53 electrical input, not the unit-contact/global-optimality conclusion.
  The resistance metric is unchanged by the paper's opposite Laplacian sign
  convention. No converse electrical-realization assertion is imported.
- Peña, Vera and Zuluaga, [New characterizations of Hoffman constants for systems
  of linear constraints](https://arxiv.org/abs/1905.02894): the fixed-matrix error
  bound is uniform over feasible right-hand sides. C63 needs precisely this
  finite-dimensional statement, not a constant uniform across configurations.
- No external theorem is used in L1–L4 or the local-star regression. L5 uses finite
  max-flow/min-cut; L6 uses only geometry and the KKT scalar/tensor identities.
- Exact reproduction:

  ```sh
  python3 research/near_diameter_path_audit.py
  ```

  [The script](../../../research/near_diameter_path_audit.py) checks five rational
  local stars, the sharp lens example in Q(√3), five exact full-KKT chains and their
  strict L-shaped competitors, and 27,252 chord/interval cases.
  All assertions pass. No floating-point equality or global-optimality certificate
  is claimed. SymPy was unavailable and is not a dependency.

## 9. Promotion recommendation and compact handoff

**Hold as report.** Consider promoting L1/L3/L4 after an independent audit, with
L1/L4 in shared geometry and the C100 application in Target C. Retain the
degree-three local-star regression with the exact missing-global-hypothesis warning.
Do not modify the canonical C-I status on the strength of this partial campaign.

```text
LEVEL I STATUS: STILL OPEN.
New: a diameter contact path whose forward directions lie within <15 degrees of
its diameter has no internal diameter endpoint; an explicit squared-distance
clearance is proved. With only excess length delta=k-D, all diameter-loaded
internal vertices lie within delta/[2-sqrt(2+sqrt(3))] edges of the path ends.
Effect: the later C100/C102 one-leaf path is entirely unloaded internally;
arbitrary D+o(D) paths have a consecutive D-o(D) unloaded core.
Direct support/tensor simplification: other diameter endpoints have incident
contact stress <=4(1-b)D^2, and the entire diameter boundary has incident stress
<=D(1+b)+5(1-b)D^2. Small positive transverse forces remain uncontrolled.
Binding new regression: an arbitrarily nearly straight rational degree-three
unit-contact star has positive local equilibrium and one-sided tiny transverse
stress. It lacks full global KKT equilibrium and is not globally optimal.
Remaining: source-level transverse/strip and variable-prefix stability, plus the
other C-II branches. No Level I result or exhaustive-independence claim.
```
