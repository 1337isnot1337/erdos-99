<!-- theorem-state: {"artifact_id":"ART-2109751E4F53","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_full_source_cell_slack_and_inward_pockets_2026-09-11.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=528b3bbf2f799d6a6dbb7b23fa135342f7ace283; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — full-source cell slack and the inward-pocket obstruction

**Date:** 2026-09-11

**Repository state:** local `8a78616870368d8456892defe46be6c8e175666a`; remote main inspected at `053e1e1b85643b738b4cde306838d150ea325783`

**Run type:** closing-proof attempt with a dependency repair

**Target:** Target C C-II and Level I

**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md`, subordinated to the current user instructions

**External access:** authenticated read-only GitHub reads; no new literature imported

**Computation:** none

## LEVEL I STATUS

`STILL OPEN`.

The new result is an exact extension of the local Oler-slack decomposition to
the full C-II source, with arbitrary contact isolates, repeated outer walks,
both diameter topologies, and unrestricted mixed surplus. In particular the
rhombic area excess satisfies `E=O(D)` in **every** C-II branch, without ZR/ZF
or the cyclic cap-detour claim.

A concrete issue arose when trying to use the newest cyclic results to close
the high-surplus branch. CRC Section 3 puts an OP pocket on the wrong side of
its force-hull chord. The OP pocket is inside the force hull; the Reuleaux
minor cap is outside it. Thus the proof of `ell <= D phi` does not apply to
that pocket. The exact six-point pentagon-and-center global minimizer already
violates this purported local inequality. This does not disprove the proposed
sufficiently-large detour theorem, but its supplied containment proof does
not establish it. The later atomic conclusions retain this dependency issue.

No authoritative theorem status is changed by this report.

## 1. Exact closing endpoint

Write

\[
a_0=\frac{\sqrt3}{2},\qquad c_0=\frac{\sqrt3}{4},\qquad
K=\operatorname{conv}A,\quad P_K=\operatorname{per}K,
\]

\[
\delta_K=\frac{\pi D^2}{4}-\operatorname{area}K,
\qquad
\mathcal O_A=\operatorname{area}K+c_0P_K-a_0(n-1).
\]

The strict global lattice comparison gives

\[
\delta_K+\mathcal O_A<c_0P_K.                 \tag{1.1}
\]

The attempted closure was to prove the opposite inequality from actual
source cell slacks and the C-II geometry. It must recover the entire boundary
term in (1.1); a positive or linear lower bound with an unspecified coefficient
does not suffice.

The response alternative was to turn the common contact block into a strict
mixed-row deficit. The common-bridge proof does not itself supply that
extension. Neither attempted closing step is asserted below.

## 2. The full-source slack theorem

Work with the representative supplied by the promoted C-I restoration:
contacts are minimized first and diameter pairs second, with `C=C_*` and
`H=H_*`. Retain every source point. Let `G` be the connected nonisolated
contact core, `v=|V(G)|`, `e=|E(G)|`, and

\[
F=\operatorname{conv}V(G),\qquad P_F=\operatorname{per}F,
\qquad q=|\operatorname{Vert}F|.
\]

The promoted force-hull/C26 inputs identify these hull vertices with the
loaded vertices. They are also extreme vertices of `K`. Every other core
vertex is a positive weighted barycenter of its contact neighbors and has
degree at least three. The force hull is two-dimensional.

Add all missing sides of `F` to `G`, obtaining a plane graph `Ghat`. Let
`mathcal T` be its bounded faces. For each `T in mathcal T`, let `k_T` be its
number of graph-boundary vertices and let `z_T` count the assigned source
isolates in that cell. Points on an added hull side are assigned to its
unique bounded cell. Define

\[
\sigma_T=\frac{\operatorname{area}T}{a_0}
          +\frac{\operatorname{per}T}{2}+1-k_T-z_T.       \tag{2.1}
\]

For every side of `F` that is not a common side of `K`, let `K_i` be the
convex exterior cap between that side and the corresponding source-hull arc.
Let `k` count these nondegenerate caps, `P_com` be the total common-side
length, and `z_i=|A cap (K_i setminus F)|`. Set

\[
\sigma_i=\frac{\operatorname{area}K_i}{a_0}
          +\frac{\operatorname{per}K_i}{2}-1-z_i,
\qquad L=P_F-P_{\rm com}-k.                         \tag{2.2}
\]

If `F=K`, set `k=0`, `P_com=P_F`, and `L=0`.

### Theorem FSCS

All the slacks in (2.1)--(2.2) are nonnegative, and

\[
\boxed{
W:=a_0\left(\sum_{T\in\mathcal T}\sigma_T+\sum_i\sigma_i\right)
  =\mathcal O_A+a_0L.
}                                                        \tag{2.3}
\]

Let `mathcal R` consist of the original bounded quadrilateral contact faces,
and put

\[
E=\sum_{R\in\mathcal R}(\operatorname{area}R-a_0).
\]

Then

\[
\boxed{
0\le E\le W,\qquad
\delta_K+E<c_0P_K+a_0L
\le c_0P_K+a_0(P_F-q).
}                                                        \tag{2.4}
\]

In particular,

\[
\boxed{E<3\pi c_0D-a_0q=O(D).}                           \tag{2.5}
\]

No circuit identity, diameter-topology classification, small-isolate bound,
or simultaneous hull saturation is assumed.

### Proof: convexity and the subdivision

First, every component `S` of `G-x` contains a loaded vertex. Otherwise all
coordinates on `S` are harmonic for positive contact conductances with their
only possible boundary value at `x`. The discrete maximum principle makes
every vertex of `S` equal to `x`, contradicting distinct source points.

After adding the hull cycle, deletion of any vertex leaves the augmented
graph connected: if the deleted vertex is a hull vertex, the surviving hull
path connects all other hull vertices; otherwise the hull cycle survives.
Each component of the original deleted graph meets that path or cycle by
the preceding paragraph. Thus `Ghat` is 2-connected, so every bounded face
has a simple boundary cycle.

At a nonloaded vertex, an empty face sector of angle greater than `pi`
would place all positive contact directions in an open half-plane, contrary
to equilibrium. An angle equal to `pi` would force all contact directions
onto its boundary line. Unit separation permits only two unit neighbors on
that line, contrary to the degree bound. At a loaded vertex, a bounded face
sector lies in the strictly smaller-than-`pi` tangent cone of `F`. Every
bounded augmented face is therefore strictly convex.

Oler applies to its `k_T` boundary source vertices and `z_T` assigned
isolates, proving `sigma_T>=0`. No isolate lies on a unit contact segment.
Consequently all source points in `F` are counted as graph vertices or as
exactly one assigned cell population.

### Proof: exact interior cancellation

Let `a` be the number of added hull sides and `L_add` their total length.
Let `fhat=e+a-v+1` be the number of bounded augmented faces. Euler and
edge incidence, retaining repeated original outer-walk occurrences, give

\[
\sum_T k_T=2(e+a)-q,
\qquad
\sum_T\operatorname{per}T=2(e+L_{\rm add})-P_F.          \tag{2.6}
\]

The `q-a` existing hull sides are unit contacts, so

\[
P_F=q-a+L_{\rm add}.                                    \tag{2.7}
\]

Write `N_F=|A cap F|=v+sum_T z_T`. Summing (2.1) and using
(2.6)--(2.7) yields exactly

\[
\begin{aligned}
\sum_T\sigma_T
&=\frac{\operatorname{area}F}{a_0}
  +e+L_{\rm add}-\frac{P_F}{2}
  +(e+a-v+1)-[2(e+a)-q]-(N_F-v)\\
&=\frac{\operatorname{area}F}{a_0}+\frac{P_F}{2}+1-N_F.
\end{aligned}                                           \tag{2.8}
\]

This is an identity of actual source slacks, not a replacement packing.

### Proof: exterior population and cap cancellation

Because the hull vertices of `F` are extreme vertices of `K`, the exterior
caps are convex, have disjoint interiors, and partition `K setminus F`
apart from their closing chords. Each cap contains its two chord endpoints
and `z_i` external source points. Oler proves `sigma_i>=0`. The exact sums
are

\[
\sum_i\operatorname{area}K_i=\operatorname{area}K-\operatorname{area}F,
\qquad
\sum_i\operatorname{per}K_i=P_K+P_F-2P_{\rm com},
\qquad
\sum_i z_i=n-N_F.                                       \tag{2.9}
\]

Combining (2.8)--(2.9) proves

\[
\sum_T\sigma_T+\sum_i\sigma_i
=\frac{\operatorname{area}K}{a_0}+\frac{P_K}{2}+1-n
 +P_F-P_{\rm com}-k,
\]

which is (2.3).

### Proof: recovering the rhombic excess

An original quadrilateral contact face is a strict unit rhombus with angle
in `(pi/3,2pi/3)`, because both diagonals have length greater than one.
It contains no additional unit-separated source point. To see this directly,
write its points as `tu+sv`, `0<=t,s<=1`, for unit side vectors `u,v`.
Round `t,s` to `i,j in {0,1}`. The residual coefficients lie in
`[-1/2,1/2]`; convexity of the norm bounds the distance to the corner
`iu+jv` by half the longer diagonal, which is less than `sqrt(3)/2<1`.

Thus its slack is exactly

\[
a_0\sigma_R=\operatorname{area}R-a_0.
\]

Every other summand of `W` is nonnegative, giving `E<=W`. Combine this
with (1.1) and (2.3) to obtain the strict bound in (2.4). There are `q-k`
common sides, all of length at least one; hence `P_com>=q-k` and
`L<=P_F-q`. Finally `P_K,P_F<=pi D` proves (2.5). QED.

### The strict comparison used above

For clarity, the `n-1` comparison can be proved without a new literature
input. A triangular lattice of covolume `a_0` has, on average over its
translations, `n-1` points in the open disk of area `a_0(n-1)`. Its counting
function is not almost everywhere constant: locally finitely many translated
boundary circles occur, and a point of one circle away from their finitely
many intersections has neighborhoods on opposite sides where the count
differs by one. An integer-valued nonconstant counting function of integer
mean `n-1` takes a value at least `n`. Those `n` points lie in the open disk
and therefore have diameter strictly less than its diameter. Consequently
`pi D(n)^2/4<a_0(n-1)` for `n>=2`, proving (1.1).

### Dependencies and novelty

The inputs are the promoted C-II normal form and force-hull/C26 properties,
the shared Oler inequality, Euler counting, and elementary convex geometry.
The argument checks the needed OP/C51 geometry directly, so it does not
depend on a later unpromoted rigidity or circuit theorem.

The cancellation method is inherited from shared theory Section 21.3, C52,
OP, and the exterior-cap slack identity. The new extension is its exact
application to the entire C-II source with isolates and arbitrary outer-walk
topology, and hence the unrestricted `E=O(D)` conclusion. It is not a new
Oler inequality and not a closure by itself.

## 3. Concrete failure of the cyclic cap containment

The remote [CRC report, Section 3](https://github.com/1337isnot1337/e-99/blob/053e1e1b85643b738b4cde306838d150ea325783/docs/reports/target_c_cyclic_reuleaux_cap_detour_2026-09-10.md)
asserts for an OP pocket behind a missing hull side `AB` that

\[
P\subset K\cap H_{AB}^{\rm out}.                         \tag{3.1}
\]

But an OP pocket is a bounded face of `G union partial F`, obtained by
cutting the original outer contact face **inside** `F`. Thus it is on the
interior side of `AB`. Its nonempty interior is disjoint from the exterior
half-plane in (3.1). The Reuleaux minor circular segment is on that exterior
side. It cannot contain the OP pocket.

The fact that `K` lies in the Reuleaux container proves containment of the
external source cap. It does not identify that cap with the internal contact
pocket. In particular the following claimed implication fails:

\[
\text{Reuleaux arc above }AB\quad\Longrightarrow\quad
\ell_{\rm contact}(A,B)\le D\phi.                         \tag{3.2}
\]

### Exact force-visible circuit regression

Let

\[
p_j=(\cos(2\pi j/5),\sin(2\pi j/5)),\quad 0\le j<5,
\qquad o=(0,0).
\]

The configuration `A={o,p_0,...,p_4}` is unit-separated and triangle-free.
Its contacts are the five spokes `op_j`. Its diameter is
`D=2 sin(2pi/5)`, and its five diameter pairs join `p_j` to `p_{j+2}`.
The supplied literature baseline records this as an exact six-point global
minimizer. Moreover `e+h=10=2v-2`, so its mixed surplus is zero.

There is a normalized fully positive KKT stress

\[
\beta_h=\frac15,\qquad \alpha_{op_j}=\frac{D^2}{5}.
\]

Indeed
`(p_j-p_{j+2})+(p_j-p_{j-2})=D^2 p_j`, and the five radial vectors sum to
zero. Thus this regression also has the relevant actual force-hull and
positive-equilibrium geometry.

For consecutive outer vertices `A=p_0`, `B=p_1`, the OP pocket is the
triangle `AoB` and its contact-chain length is `ell=2`. The corresponding
Reuleaux arc is centered at `p_3` and has angle `phi=pi/5`. But

\[
 D\phi=\frac{2\pi}{5}\sin\frac{2\pi}{5}<2=\ell.        \tag{3.3}
\]

Thus the purported local inequality is false even on this actual global
minimizer. The example is finite, so it does not disprove a theorem with a
new sufficiently-large hypothesis. It does disprove the universal local
containment/monotonicity step used in its supplied proof.

### Vanishing arc angle does not repair the geometric inference

For any `D>=2`, set

\[
A=(-1/\sqrt2,0),\quad B=(1/\sqrt2,0),\quad
x=(0,-1/\sqrt2),\quad c=(0,-\sqrt{D^2-1/2}).
\]

Then `|A-x|=|B-x|=1`, `|A-B|=sqrt(2)`, and
`|A-c|=|B-c|=D`. The convex triangle `AxB` lies in the radius-`D` disk
centered at `c`, but on the opposite side of `AB` from its minor cap.
Here

\[
\phi_D=2\arcsin\frac{1}{\sqrt2D}\longrightarrow0,
\qquad D\phi_D\longrightarrow\sqrt2<2=\ell.
\]

This is a regression for the proposed geometric inference only. It is not a
large C-II realization or a global-optimality certificate.

### Consequences for the dependency chain

The cycle-skeleton perimeter estimate `P_F=pi D-O(sqrt D)` and the placement
of loaded vertices on the Reuleaux boundary are not refuted here. They do
not use (3.1). The external Reuleaux-cap population calculation also uses
the correct side of the chord and survives.

The supplied proofs of sublinear **internal** contact detour, vanishing
internal outer-pocket area, outer-walk direction equidistribution, and the
atomic surplus bound use the failed step. Without another proof of the
detour statement they cannot be used unconditionally in this run. The
endpoint contradiction remains a valid implication if its listed geometric
and measure hypotheses are independently established. FSCS separately
recovers the rhombic defect estimate, in stronger all-branch scope.

## 4. Closing attempts and the surviving obstruction

### 4.1 High-surplus closure from cyclic direction measures

The intended contradiction was to force actual exceptional-face endpoint
directions into a finite atomic set while their macroscopic area required
a diffuse boundary-direction measure. In the reported endpoint argument
these conclusions depend on saturation; outside that endpoint neither a
giant face nor one direction orbit is forced. In addition, deriving uniform
outer-walk directions currently needs the unproved detour repair above.
No unrestricted high-surplus contradiction was obtained.

### 4.2 Full-source slack closure

FSCS gives the exact new expression

\[
\delta_K+\mathcal O_A=\delta_K+W-a_0L.
\]

To contradict global optimality it would suffice to prove

\[
\boxed{\delta_K+W\ge c_0P_K+a_0L}                       \tag{4.1}
\]

for every sufficiently large C-II source. This is the exact surviving
obligation for the new ledger. Nonnegativity of all local slacks only gives
`W>=0`; strict rhombi give `W>=E>0` when present. Neither pays the right
side of (4.1). Near-equilateral rhombi can have arbitrarily small positive
slack. Retaining isolates in cell populations prevents counting their area
as unused capacity.

No simultaneous packing rearrangement attaining (4.1) or a smaller diameter
was proved. Independent improvements in separate cells do not supply such
a rearrangement because their shared boundaries are actual source points.

### 4.3 Common-block response closure

The common-bridge audit is sound at the exact passage used: a unique bridge
forces every cross-cut unit current through the same resistor, giving a
positive transfer drop. A block or a multi-edge cut has no such obligatory
single-resistor drop. The unit square already has zero transfer between its
two diameter diagonals although both cross the same two-edge contact cut.
Thus substituting total cut conductance for the bridge conductance cannot
prove the required strictly positive transfer entries. No source-specific
replacement theorem coupling the common block to the forest charge was
obtained.

### 4.4 Positive mixed surplus

An extreme normalized stress can omit actual rows supported by another
stress. Omission is not weakness in the fixed-diameter critical cone and
does not authorize releasing those rows. FSCS applies without eliminating
this branch; it does not convert stress sparsification into a finite motion.

## 5. Complete branch and regression ledger

- `s_Z=0`, cyclic diameter graph: still unresolved. The disk-like force-hull
  geometry survives, but the supplied internal-pocket detour proof needs
  repair. FSCS gives `E=O(D)` without that repair.
- `s_Z=0`, forest diameter graph: still unresolved, including fixed and
  sublinear component counts. FSCS does not discard or replace the `3d_H`
  term in the inherited circuit ledger.
- `s_Z>0`: still unresolved; FSCS now supplies the same defect estimate
  without a circuit reduction.
- Regular odd shells are retained. Their `s_Z=2` does not enter the proof,
  and FSCS supplies no large-shell global-optimality certificate.
- All isolates are included in one cell or exterior cap, or as source-hull
  chord points assigned to the interior cell. None is declared diametral.
- Bridges and repeated outer walks are handled by augmented-graph incidence
  identities; no simple original outer-boundary hypothesis is imposed.
- Shared diameter endpoints, exceptional faces, attachment overlaps, and the
  whole-circuit exception create no omitted terms: the theorem uses no
  attachment sparsity sum.
- High pinned surplus is unrestricted. No necessary lower surplus bound is
  interpreted as an upper bound or as a contradiction.

## 6. Promotion and handoff

**Hold as report.** The exact proof and regression are supplied for audit;
no route map or prompt is changed. Existing untracked research files were
preserved. The CRC dependency issue should be resolved before further use
of its downstream conclusions, not by silently treating them as promoted.

```text
LEVEL I STATUS: STILL OPEN.

New extension: for the entire C-II source, let W be the sum of dimensional
Oler slacks of all hull-augmented contact cells and external source caps.
Then W=O_A+a0(P_F-P_com-k), W>=E, and
    delta_K+E<c0 P_K+a0(P_F-P_com-k).
Hence E=O(D) in every branch, without ZR/ZF, circuit identities, or small
isolate assumptions.

Concrete failed implication: CRC places internal OP pockets in external
Reuleaux minor caps. These lie on opposite sides of the force-hull chord.
The six-point regular pentagon plus center has ell=2>D*pi/5 and refutes
the claimed local contact-chain bound. No sufficiently-large C-II
counterexample is claimed.

Exact new-ledger closing obligation:
    delta_K+W >= c0 P_K+a0(P_F-P_com-k).
No proof of this reverse inequality or a compatible strict sub-D competitor
was obtained. All three C-II branches remain unresolved.
```
