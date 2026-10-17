> Generated reading edition · [exact source](../../../docs/reports/target_c_force_hull_2026-08-30.md) · source SHA-256 `ab136d47fc53dc9662d10c46c823cee242abc01b8036e47b1acd45aa308b5ca7`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-CA389CA9D692","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C: diametral saturation, terminal covering, and the KKT force hull

**Date:** 2026-08-30  
**Repository state:** branch `research/target-c-force-hull-2026-08-30` from `0ecb0927d82b7a53c3c8133b821b5261c81b75f7`  
**Run type:** discovery / proof audit  
**Target:** Level I candidate route C  
**Active prompt:** `docs/prompts/erdos_problem_99_1.7.9_FINAL_CONTINUATION_PROMPT.md`  
**External web search:** used only for orientation; no external theorem is needed below  
**Computation:** exploratory sanity checks only; no computation is used in any proof

## LEVEL I STATUS

`STILL OPEN`

The purpose of this run was deliberately not to optimize the existing Target A Schur
inequality or Target B rhombic-shell inequality.  It looked instead for an exact
structure tied directly to global diameter optimality.

The strongest new outcome is a three-part normal form:

1. a contact-minimal triangle-free minimizer can be changed, at the same cardinality
   and with exactly the same unit-contact graph, until every point on its convex-hull
   boundary is a genuine diameter endpoint;
2. at a right endpoint of a diameter plateau, the entire one-point
   diameter-preserving insertion body is strictly covered by the open unit disks of
   the minimizer; and
3. the positive part of every KKT stress is globally contraction-rigid and is trapped
   in the convex hull of its positive diameter endpoints.  Maximizing support over the
   KKT multiplier polytope therefore defines a canonical same-diameter **force hull**.

These facts produce a route that is not the current source-to-scaffold Schur route and
is not the almost-rhombic shell route.  They do not yet give a Level I contradiction.

---

## 1. Starting endpoint

The canonical state still has two active endgames.

- Target A closes if the exact Schur saving
  
  ```math
  \operatorname{rank}S
  \le d_{\rm int}+|C^\partial|-\Delta_\Lambda
  ```

  is proved, or if a strict sub-`D` competitor is constructed.
- Target B closes by the exact shell/Oler surplus in its route map.

This run does not improve either displayed inequality.  It instead starts from the
shared KKT and contact-minimality theory in
`docs/theory/01-local-structure.md` and
`docs/theory/02-nonlinear-and-regressions.md`.

The intended Target C implication chain is

```text
fixed-cardinality diametral saturation
    + canonical KKT force hull
    + same-source/global insertion information
        -> force-free geometric sector or globally contractible replacement
        -> strict sub-D competitor
        -> contradiction.
```

The first two arrows now have exact theorems.  The last transport remains open.

---

## 2. Fixed-cardinality diametral hull saturation

Let
```math
Q(A)=\{p\in A:\exists q\in A,\ |p-q|=D\}
```
for a diameter-`D` configuration.

### Theorem C1 (contact-preserving diametral hull saturation)

Assume a triangle-free global `n`-point minimizer exists.  Choose a triangle-free
`n`-point minimizer `A` with the minimum possible number of unit contacts.  Then there
is another triangle-free global minimizer `A^\sharp` with the same cardinality and
same diameter `D=D(n)` such that

```math
\boxed{C(A^\sharp)=C(A)}
\tag{C1.1}
```

as an abstract unit-contact graph, every originally nonisolated point remains at the
same Euclidean position, and

```math
\boxed{
Q(A^\sharp)
=A^\sharp\cap\partial\operatorname{conv}A^\sharp
=\operatorname{Vert}(\operatorname{conv}A^\sharp).
}
\tag{C1.2}
```

In particular, no point of `A^\sharp` lies in the relative interior of a convex-hull
edge.

#### Proof

Work inductively, beginning with `A`.  Every intermediate configuration will have the
same contact graph, so it remains contact-minimal among triangle-free global
minimizers.

Suppose the current configuration contains
```math
p\in A\cap\partial\operatorname{conv}A,
\qquad p\notin Q(A).
```
We first show that `p` is contact-isolated.  Choose an outward supporting vector
`w\ne0` at `p`, so
```math
(p-r)\cdot w\ge0
\qquad(r\in A).
\tag{C1.3}
```
If `p` had a unit contact, then for `t>0`
```math
|p+tw-r|^2
=|p-r|^2+2t(p-r)\cdot w+t^2|w|^2
>|p-r|^2
\tag{C1.4}
```
for every `r\ne p`.  Since `p\notin Q(A)`, all distances incident to `p` have strict
slack below `D`; for sufficiently small `t`, moving only `p` therefore preserves
unit separation and diameter `D` while breaking every unit contact incident to `p`.
No new contact, hence no new unit triangle, can appear because all distances from `p`
strictly increase.  This contradicts contact minimality.  Thus `p` is isolated.

Now continue the same outward motion until the first diameter event.  For each
`r\ne p`, the function
```math
f_r(t)=|p+tw-r|
```
is strictly increasing for `t>0`, starts below `D`, and tends to infinity.  Hence it
has a unique first time `\tau_r>0` at which it equals `D`.  Put
```math
t_*:=\min_{r\ne p}\tau_r>0.
\tag{C1.5}
```
For `0\le t\le t_*`, every distance incident to the moving point is at most `D` and
strictly larger than its initial value.  All other distances are unchanged.  An old
diameter pair avoids `p`, because `p\notin Q(A)`, so an old pair of length exactly
`D` remains fixed throughout.  Consequently every intermediate configuration is
again a global minimizer of diameter exactly `D`.  The moving point remains isolated,
and the complete contact graph is unchanged.

At `t=t_*`, the moving point has acquired a diameter partner and therefore joins
`Q`.  Every old member of `Q` stays in `Q`, because each of its old diameter pairs was
between fixed points.  Thus `|Q|` strictly increases while the contact graph does not
change.

Repeat whenever a boundary point outside `Q` exists.  Each step strictly increases
`|Q|`, so after at most `n` steps the process stops.  At the terminal configuration,
```math
A^\sharp\cap\partial\operatorname{conv}A^\sharp\subseteq Q(A^\sharp).
\tag{C1.6}
```
Canonical Lemma 5.1 gives the reverse structural fact that every diameter endpoint is
an extreme point of the convex hull.  Hence
```math
Q(A^\sharp)
\subseteq\operatorname{Vert}(\operatorname{conv}A^\sharp)
\subseteq A^\sharp\cap\partial\operatorname{conv}A^\sharp.
```
Together with (C1.6), this proves (C1.2).

Only contact-isolated points were moved, so every originally nonisolated point kept
its Euclidean coordinates.  This proves the theorem. `\square`

### Why C1 is not already the jammed identity `Q=Vert(conv A)`

Canonical Lemma 7.2 proves `Q=Vert(conv A)` in the zero pinned-expansive-cone branch.
Theorem C1 is different: it starts from the contact-minimal representative, whether
or not the full configuration is in that zero-cone branch, and moves only isolated
points.  The entire nonisolated mechanical core and its contact graph are preserved.
Thus one may impose genuine diametral hull saturation without replacing the core by a
different jammed representative.

### Corollary C1.1 (two genuine diameter pins per core component)

Let `A^\circ` be the nonisolated contact core of a contact-minimal representative, and
let `Q^\circ=Q\cap A^\circ`.  Every nontrivial contact component of `A^\circ` contains
at least two points of `Q^\circ`.

#### Proof

Canonical Theorem 12.2 gives zero pinned expansive cone for the core when `Q^\circ`
is fixed.  If a nontrivial component had no pin, translating that component would be
a nonzero pinned contact-preserving velocity.  If it had exactly one pin `q`, rotate
the entire component infinitesimally about `q`:
```math
v_i=J(p_i-q)
```
on that component and `v=0` elsewhere.  The pin is fixed and every internal contact
has first variation
```math
(p_i-p_j)\cdot J(p_i-p_j)=0.
```
The velocity is nonzero because the component is nontrivial, again contradicting the
zero cone. `\square`

### Corollary C1.2 (the fixed core already realizes the full diameter)

For every global minimizer, the nonisolated contact core contains a pair at distance
`D`.  In particular, in Theorem C1 the mechanically unchanged core already has
Euclidean diameter `D` before and after hull saturation.

#### Proof

Take any normalized KKT stress.  Since `\sum_H\beta=1`, some positive diameter edge
exists.  Canonical Lemma 5.2 says every endpoint of a positive diameter edge is
incident to a positive contact edge.  Both endpoints are therefore nonisolated and
belong to the contact core.  Their mutual distance is `D`. `\square`

This exposes a useful distinction: isolated hull points can be made genuine diameter
endpoints even though the unchanged nonisolated core already spans the entire global
diameter.

---

## 3. Strict covering of the full one-point insertion body

For a diameter-`D` finite set `A`, define its one-point diameter-preserving insertion
body
```math
\mathcal I_D(A)
:=\bigcap_{p\in A}\overline B(p,D).
\tag{C2.1}
```
A point `x` lies in `\mathcal I_D(A)` exactly when adjoining `x` cannot make the
diameter exceed `D`.

### Theorem C2 (right-plateau strict insertion cover)

Let `A` be any global `N`-point minimizer, with `D=D(N)`, and assume
```math
D(N+1)>D(N).
\tag{C2.2}
```
Then
```math
\boxed{
\mathcal I_D(A)
\subseteq
\bigcup_{p\in A}B^\circ(p,1).
}
\tag{C2.3}
```
Equivalently,
```math
\boxed{
R(A):=\max_{x\in\mathcal I_D(A)}\min_{p\in A}|x-p|<1.
}
\tag{C2.4}
```
Moreover,
```math
\operatorname{conv}A\subseteq\mathcal I_D(A),
\tag{C2.5}
```
so the convex hull itself is strictly open-unit-covered.

No triangle-free hypothesis is used.

#### Proof

If some `x\in\mathcal I_D(A)` satisfied
```math
|x-p|\ge1
\qquad(p\in A),
```
then `A\cup\{x\}` would be an `(N+1)`-point unit-separated set of diameter at most
`D`.  Since the original diameter-`D` pair in `A` remains present, its diameter is
exactly `D`, and therefore
```math
D(N+1)\le D,
```
contradicting (C2.2).  This proves (C2.3).

The insertion body is compact, and the function
`x\mapsto\min_{p\in A}|x-p|` is continuous, so the strict pointwise bound in (C2.3)
has a strict maximum below one.  This proves (C2.4).

Finally, if
```math
x=\sum_i\lambda_i p_i\in\operatorname{conv}A,
\qquad \lambda_i\ge0,\quad\sum_i\lambda_i=1,
```
then for every `p_j\in A`,
```math
|x-p_j|
\le\sum_i\lambda_i|p_i-p_j|
\le D.
```
Thus `x\in\mathcal I_D(A)`, proving (C2.5). `\square`

### Relation to canonical same-hull saturation

Canonical Theorem 63.1 constructs a same-diameter triangle-free extension whose
**fixed hull** is covered by closed unit disks.  That theorem works along a source
plateau and is already trusted.

Theorem C2 is different in two ways:

1. it covers the larger, intrinsic body `\mathcal I_D(A)`, not only
   `\operatorname{conv}A`; and
2. at a right plateau endpoint the cover is by **open** unit disks, so compactness
   supplies the positive margin `1-R(A)>0`.

The price is the right-endpoint hypothesis (C2.2).  A triangle-free minimizer at an
arbitrary point of a plateau cannot simply be replaced by an unrelated right-endpoint
minimizer; the canonical source warning remains binding.

---

## 4. Finite contraction rigidity of positive KKT support

Fix any normalized KKT stress `(\alpha,\beta)` from canonical Theorem 4.1.  Write
```math
C_+=\{ij\in C:\alpha_{ij}>0\},
\qquad
H_+=\{ij\in H:\beta_{ij}>0\},
```
and let `B_+` be the endpoint set of `H_+`.

### Theorem C3 (finite contraction rigidity)

Assign arbitrary points `y_i\in\mathbb R^2` to the vertices of `V(C_+)`, subject
only to
```math
y_b=p_b\qquad(b\in B_+)
\tag{C3.1}
```
and
```math
|y_i-y_j|\le1
\qquad(ij\in C_+).
\tag{C3.2}
```
Then
```math
\boxed{y_i=p_i\qquad(i\in V(C_+)).}
\tag{C3.3}
```

Thus the positive contact framework is globally, not merely infinitesimally,
rigid against contraction once the positive diameter-load vertices are fixed.

#### Proof

Extend the assignment to arbitrary vectors `y_i` on all remaining vertices, for
example by setting `y_i=p_i` there.  Apply the exact virtual-work identity (11.7) with
`\xi_i=y_i`.

For every edge in `H_+`, both endpoints lie in `B_+` and are fixed, so
```math
(p_i-p_j)\cdot(y_i-y_j)=D^2.
```
Since `\sum_H\beta=1`, the right side of virtual work is exactly `D^2`.

For a positive contact `ij`, put `u_{ij}=p_i-p_j`, so `|u_{ij}|=1`.  By Cauchy and
(C3.2),
```math
u_{ij}\cdot(y_i-y_j)
\le |y_i-y_j|
\le1.
\tag{C3.4}
```
Therefore the left side of virtual work is at most
```math
\sum_C\alpha_{ij}=D^2.
```
Equality with the right side forces equality in (C3.4) on every edge carrying
positive `\alpha`.  Hence
```math
y_i-y_j=p_i-p_j
\qquad(ij\in C_+).
\tag{C3.5}
```
So the displacement `y_i-p_i` is constant on every connected component of `C_+`.
Canonical Proposition 5.4 says every nontrivial positive-contact component contains
at least two vertices of `B_+` (one would already suffice here).  Since those vertices
are fixed, the constant displacement on each component is zero.  This gives (C3.3).
`\square`

This theorem is stronger than the first-order rank statement: no nonlinear finite
contraction satisfying (C3.2) exists at all.

### Corollary C3.1 (positive support lies in the positive diameter hull)

For every normalized KKT stress,
```math
\boxed{
V(C_+)\subseteq\operatorname{conv}B_+.
}
\tag{C3.6}
```
Consequently,
```math
\boxed{
\operatorname{conv}V(C_+)=\operatorname{conv}B_+.
}
\tag{C3.7}
```

#### Proof

Let `L=\operatorname{conv}B_+` and let `P_L` be Euclidean metric projection onto
`L`.  Projection onto a closed convex set is nonexpansive:
```math
|P_Lx-P_Ly|\le|x-y|.
```
For completeness, if `x'=P_Lx` and `y'=P_Ly`, the projection variational
inequalities give
```math
(x-x')\cdot(y'-x')\le0,
\qquad
(y-y')\cdot(x'-y')\le0.
```
Adding them yields
```math
|x'-y'|^2\le(x-y)\cdot(x'-y')
\le|x-y|\,|x'-y'|.
```

Apply Theorem C3 to `y_i=P_Lp_i`.  Every `b\in B_+` is fixed by projection, and
every positive unit contact is contracted to length at most one.  Hence
`P_Lp_i=p_i` for every `i\in V(C_+)`, proving (C3.6).

Canonical Lemma 5.2 gives `B_+\subseteq V(C_+)`, so taking convex hulls gives
(C3.7). `\square`

The same conclusion can also be viewed as a discrete maximum principle, but C3 gives
the stronger finite cable-rigidity statement.

---

## 5. The canonical maximal-support force hull

The KKT multiplier set at a fixed minimizer is a compact convex polytope: it is cut
out by the linear equilibrium equations, nonnegativity, and `\sum_H\beta=1`; the
identity `\sum_C\alpha=D^2` makes the contact multipliers bounded.

Define
```math
C_*:=\{e\in C:\alpha_e>0\text{ for some normalized KKT multiplier}\},
\tag{C4.1}
```
```math
H_*:=\{h\in H:\beta_h>0\text{ for some normalized KKT multiplier}\},
\tag{C4.2}
```
and let `B_*` be the endpoint set of `H_*`.

Because there are only finitely many active constraints, averaging one witness
multiplier for each coordinate that can be positive produces a single normalized KKT
multiplier whose positive supports are exactly `C_*` and `H_*`.

### Theorem C4 (canonical force hull)

Put
```math
\boxed{F(A):=\operatorname{conv}B_*.}
\tag{C4.3}
```
Then
```math
\boxed{
F(A)=\operatorname{conv}V(C_*),
\qquad
\operatorname{diam}F(A)=D.
}
\tag{C4.4}
```
Moreover,
```math
\boxed{
B_*=\operatorname{Vert}F(A).
}
\tag{C4.5}
```
Every point of `A\setminus F(A)` is incident only to active contact and diameter
constraints whose KKT multiplier is zero in **every** normalized KKT stress.

#### Proof

Apply Corollary C3.1 to a maximal-support multiplier.  It gives
```math
\operatorname{conv}V(C_*)=\operatorname{conv}B_*=F(A).
```
The set `H_*` is nonempty because every normalized KKT multiplier has
`\sum_H\beta=1`.  Hence `F(A)` contains the two endpoints of at least one diameter
edge and has diameter at least `D`.  Since `F(A)\subseteq\operatorname{conv}A`, its
diameter is at most `D`; therefore it is exactly `D`.

Every `b\in B_*` is a diameter endpoint and hence an extreme vertex of
`\operatorname{conv}A` by canonical Lemma 5.1.  It cannot be a convex combination of
other points of `B_*\subset A`, so every point of `B_*` is a vertex of `F(A)`.  The
reverse inclusion `\operatorname{Vert}F(A)\subseteq B_*` follows from
`F(A)=\operatorname{conv}B_*`.  This proves (C4.5).

Finally, if a point `p\notin F(A)` were incident to a contact that is positive in some
KKT multiplier, that contact would belong to `C_*`, placing `p` in
`V(C_*)\subset F(A)`, a contradiction.  The same argument with a positive diameter
edge would put `p` in `B_*\subset F(A)`.  Thus every active constraint incident to
`p` is universally zero-multiplier. `\square`

The force hull is therefore a canonical same-diameter subpolygon carrying every
active constraint that can participate in first-order KKT force transmission.
Geometric hull points outside it are not merely zero-stressed for one convenient
certificate; they are invisible to the entire normalized KKT multiplier polytope.

### Corollary C4.1 (one-dimensional force hull is an exact unit chain)

If `F(A)` is one-dimensional, then `D` is an integer and, after a rigid motion,
```math
\boxed{
A\cap F(A)
=V(C_*)
=\{0,1,\ldots,D\}\times\{0\},
}
\tag{C4.6}
```
with
```math
\boxed{
C_*=\{\{k,k+1\}:0\le k<D\}.
}
\tag{C4.7}
```
All remaining points of `A` lie outside this segment and are incident only to
universally zero-KKT active constraints.

#### Proof

By (C4.4), the force hull is a segment `[a,b]` with `|a-b|=D`.  By (C4.5),
`B_*=\{a,b\}`.  Canonical Proposition 5.4 says every nontrivial component of `C_*`
contains at least two vertices of `B_*`; hence `C_*` has exactly one component and it
contains both `a` and `b`.

All of its vertices lie on `[a,b]`, and every positive contact has length one.  Sort
the component vertices along the segment.  Any gap between consecutive sorted
vertices larger than one would disconnect the contact graph, while unit separation
forbids a gap smaller than one.  Therefore every consecutive gap is exactly one.
Thus `D` is an integer and the component is the complete unit-step chain from `a` to
`b`.  No additional point of `A` can lie in an open unit interval between consecutive
chain vertices because of unit separation, proving (C4.6)-(C4.7). `\square`

This gives an exact degenerate Target C branch: either the canonical force hull is
2-dimensional, or the entire KKT-positive part of the configuration is a single
straight unit chain spanning the diameter and every other active constraint is
universally KKT-invisible.

---

## 6. A useful diametral support inequality

The following elementary inequality is included because it links actual diameter
chords to supporting geometry without any rhombic-shell assumptions.

### Lemma C5 (quadratic inward support from a diameter chord)

If `p,q\in A` satisfy `|p-q|=D`, put
```math
u=(p-q)/D.
```
Then every `x\in\operatorname{conv}A` satisfies
```math
\boxed{
u\cdot(p-x)\ge\frac{|p-x|^2}{2D}.}
\tag{C5.1}
```
In particular, the line through `p` perpendicular to `u` supports the convex hull,
and every unit contact `px` satisfies
```math
\boxed{
u\cdot(p-x)\ge\frac1{2D}.}
\tag{C5.2}
```

#### Proof

Since `x\in\operatorname{conv}A` and distance to a fixed point is convex,
`|x-q|\le D`.  Write `x-p=s`.  Then
```math
D^2\ge|x-q|^2=|Du+s|^2
=D^2+2D\,u\cdot s+|s|^2.
```
Rearrangement gives (C5.1), and (C5.2) is the case `|p-x|=1`. `\square`

---

## 7. What Target C now is

The new object is the nested geometry
```math
F(A)=\operatorname{conv}B_*
=\operatorname{conv}V(C_*)
\subseteq\operatorname{conv}A
\subseteq\mathcal I_D(A).
\tag{C6.1}
```
The first set has diameter exactly `D` and carries every KKT-active force.  At a right
plateau endpoint, the last set is strictly covered by the open unit disks centered at
**all** points of `A`.

The difference between these two structures is the Target C resource:

- the **force hull** records where global diameter optimality is visible to first-order
  KKT force;
- the **insertion body cover** records where global cardinality optimality prevents an
  extra point;
- points and constraints outside the force hull can still be geometrically essential
  to the insertion cover while being universally invisible to KKT.

This is not a relabeling of Target A.  No independent smaller optimum, triangular
lattice scaffold, Hall matrix, or Schur response occurs in C1-C5.  It is also not a
relabeling of Target B: no rhombus, train, shell face count, or Oler surplus is used.

The exact obstruction exposed by this run is the coexistence of

```math
\boxed{
\text{a same-diameter KKT force hull}
\quad\text{and}\quad
\text{a larger packing/covering geometry supported by universally force-free constraints}.
}
\tag{C6.2}
```

A proof must convert that coexistence into a strict sub-`D` replacement, or prove that
for a large global minimizer the force-free part cannot exist at the required scale.

---

## 8. Exact next lemma

The highest-value next statement is not “all hull vertices have positive KKT load.”
Theorem C1 shows why that is too strong: a moved isolated hull point is a genuine
diameter endpoint but, by canonical Lemma 5.2, cannot carry positive diameter load.

The precise next target is instead:

> **Target C1 (force-free replacement theorem).**  Let `A` be a contact-minimal,
> diametrally saturated triangle-free global minimizer as in Theorem C1, and let
> `F(A)` be its canonical force hull.  If the active constraints outside `F(A)` are
> universally zero-KKT, construct either
> 
> 1. an `n`-point unit-separated configuration of diameter strictly below `D`; or
> 2. a same-`D` triangle-free global minimizer for which the canonical force hull
>    strictly enlarges.
> 
> Iteration of alternative 2 must terminate after finitely many active vertices, so a
> proof of this dichotomy would yield alternative 1 unless `F(A)=conv A` and every
> remaining active obstruction is force-supported.

A second, plateau-specific target is sharper:

> **Target C2 (force-cover incompatibility).**  At a right plateau endpoint, use the
> strict cover
> `\mathcal I_D(A)\subset\bigcup B^\circ(p,1)` together with the universal zero-KKT
> exterior of `F(A)` to produce a same-cardinality strict sub-`D` replacement whenever
> `A` is triangle-free and sufficiently large.

Neither statement is proved here.  They identify the missing global step exactly:
KKT-invisible geometry must be charged to finite insertion capacity rather than to a
Schur terminal or a rhombic shell.

A possible intermediate theorem, worth attacking before either full statement, is:

> **Weak-contact release theorem.**  In a contact-minimal diametrally saturated global
> minimizer, every universally zero-KKT contact can be released by a same-`D`
> deformation unless it belongs to a finite boundary-rooted obstruction whose total
> rank is `O(D)`.

The activation/deactivation results in Target A prove such release for a special
monotone activation class, not for arbitrary weak contacts.  A general proof would
make the canonical force hull capture the full nonisolated bulk after only
boundary-order loss.

---

## 9. Audit classification of other claims

| Claim | Classification | Reason |
| --- | --- | --- |
| Contact-preserving diametral hull saturation C1 | **proved** | Direct finite outward-motion argument; only isolated points move. |
| Two genuine pins per contact-minimal core component | **proved** | A one-pin component has a nonzero infinitesimal rotation about its sole pin. |
| Contact-minimal core already has diameter `D` | **proved** | Any positive KKT diameter edge has two positively contact-loaded endpoints. |
| Right-plateau insertion-body open cover C2 | **proved** | Otherwise one more unit-separated point can be adjoined at diameter `D`. |
| Finite contraction rigidity C3 | **proved** | Exact virtual work plus equality in Cauchy on every positive contact. |
| Positive support convex-hull identity C3.7 | **proved** | Apply C3 to metric projection onto `conv B_+`. |
| Canonical maximal-support force hull C4 | **proved** | Finite averaging in the KKT polytope plus C3.7. |
| One-dimensional force hull is a full unit chain | **proved** | `B_*` has two endpoints and positive-contact component anchoring forces a connected collinear unit path. |
| Every diametrally saturated hull vertex has positive KKT diameter load | **rejected** | Isolated diameter endpoints cannot have positive diameter load by Lemma 5.2. |
| Contact minimality implies strict KKT complementarity on every contact | **not proved** | Universal zero multipliers need not by themselves give a finite same-`D` release. |
| Constant-width completion alone closes the problem | **rejected as a closure route** | It gives a useful container language but no exact boundary-order gain; no such theorem is needed for C1-C5. |
| Pure density gap for triangle-free configurations | **already rejected canonically** | Near-triangular and shell regressions can approach triangular density. |

---

## 10. Regression tests

| Regression | Passed? | Exact reason |
| --- | --- | --- |
| Unit square (`n=4`) | yes | Already diametrally saturated; its symmetric KKT stress has force hull equal to the square. |
| Regular unit pentagon | yes | Every hull vertex is diametral; C1 makes no false large-`n` claim. |
| `n=8` regular heptagon plus center | yes | The heptagon realizes the diameter and the center can remain KKT-invisible inside the force hull; C4 does not claim all invisible points lie outside `F`. |
| Regular odd-prime shell local minima | yes | C1 and C5 are compatible with the shell; global KKT/plateau conclusions are not inferred from local optimality. |
| Five-sector boundary-pinned rhombic regression | yes | Arbitrary pins are not positive diameter-load vertices.  C3 specifically uses a genuine global KKT stress. |
| 11-point sun | yes | True diametral pinning alone is not enough; the example is globally suboptimal and does not satisfy the full global premises. |
| Near-extremal same-hull saturated activation regression | yes | It has closed unit coverage of its own hull but is deliberately not certified as a right-plateau global optimum; C2 covers the larger insertion body and needs exact plateau optimality. |
| Activation constraints with universal zero KKT load | yes | C4 explicitly retains a universally force-free class instead of treating zero multiplier as automatic removability. |
| Dense near-triangular shell fillings | yes | No uniform angular or density gap is asserted. |

The `n=8` regression is particularly important: the force hull can equal the entire
geometric hull while a KKT-invisible rattler lies strictly inside it.  Therefore a
future Target C theorem must control universal KKT invisibility itself, not merely the
set difference `A\setminus F(A)`.

---

## 11. Failed routes and no-go results from this run

### 11.1 Hull saturation is not strict complementarity

Moving an isolated boundary point outward can make it a genuine diameter endpoint,
but Lemma 5.2 forces its KKT diameter multiplier to remain zero in every stress as
long as it stays contact-isolated.  Thus
```math
Q=\operatorname{Vert}(\operatorname{conv}A)
```
does not imply `B_+=Q` for any KKT stress.

### 11.2 Same-hull unit coverage is not the new discriminator

Canonical Theorem 63.1 already gives fixed-hull saturation, and the current
near-extremal activation regression can imitate that geometry without global
optimality.  The genuinely stronger global object is the one-point insertion body
`\mathcal I_D(A)` together with strict coverage at a right plateau endpoint.

### 11.3 A source cannot be replaced by an unrelated plateau endpoint

Theorem C2 is exact at a right plateau endpoint, but the canonical warning remains:
a triangle-free minimizer at the left or middle of the same `D(n)` plateau cannot be
replaced by an unrelated endpoint configuration.  Any Level I use of C2 must either
preserve the source through the plateau or work at fixed cardinality.

### 11.4 Force-hull localization is not a density theorem

The force hull has diameter `D`, but it need not contain every point and it need not
have a known uniform area deficit.  Oler/isodiametric estimates on `F(A)` alone retain
boundary-order slack.  No contradiction follows merely from `diam F=D`.

### 11.5 The pin-reaction realization shortcut is not automatic

The strict positive pinned stress of canonical Theorem 8.2 has arbitrary pin
reactions.  A weak diameter pin may have no positively loadable diameter chord in any
KKT stress.  Hence one cannot simply identify the strict pinned stress with a KKT
stress positive on every core contact.  The gap between those two stress cones is one
form of the Target C obstruction.

---

## 12. Literature and computation

No external theorem is logically used in C1-C5.  Web search was used only to check
that standard terminology around diametric completion/constant-width bodies did not
supply an immediate missing bridge.  That avenue was not promoted because the
constant-width completion by itself does not remove the exact boundary-order slack.

A small floating-point angle search was used privately to test a possible Delaunay
area lemma.  The lemma was not needed and is not claimed here.  No script or numerical
output is part of the proof.

---

## 13. Canonical promotion recommendation

**Hold as report pending independent audit.**

Theorems C1-C5 have complete elementary proofs and survive the named regression suite,
but they open a genuinely new route rather than merely extending the currently
indexed Target A/B endpoint.  The safest repository action is therefore to review the
report first.

If the report survives audit, promote the shared pieces as follows:

1. put C3-C5 in a new shared theory addendum, because they apply to arbitrary global
   minimizers and are not branch-specific;
2. put C1 and its core corollaries in the canonical representative/normal-form theory;
3. create `docs/targets/target-c/README.md` only after deciding to make the force-hull
   route an active third endgame;
4. update `docs/README.md`, `docs/KNOWLEDGE_MAP.md`, and the active prompt only after
   that decision.

No current Target A or Target B theorem should be deleted.

---

## 14. Next run

The highest-value next theorem is the **weak-contact release theorem** from Section 8.
It is the shortest bridge from the newly canonical force hull to a bulk statement:
prove that universally zero-KKT contacts in a contact-minimal, diametrally saturated
source either release along a same-`D` family or are confined to a boundary-order
obstruction.

Two concrete approaches remain live:

1. use the full KKT multiplier polytope and a strict Farkas alternative on the
   fixed-`D` tangent/second-order cone, rather than one selected multiplier; or
2. use finite contraction rigidity C3 contrapositively: remove one weak constraint,
   project/contract the remaining positive-support framework, and analyze the first
   lower-distance event in the force-free region.  The event must be converted into a
   replacement, not merely another contact.

A separate plateau run should test the **force-cover incompatibility** C2 against the
near-extremal activation regressions, because those regressions match fixed-hull
coverage but have not been shown to cover their full one-point insertion bodies.

---

## 15. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

New Target C theorem stack:

C1. Any contact-minimal triangle-free global minimizer can be modified at fixed n and
fixed D, moving only isolated points and preserving the entire contact graph/core,
until
    Q = A cap boundary(conv A) = Vert(conv A).
Every nontrivial contact-minimal core component has at least two genuine diameter pins,
and the unchanged core already has diameter D.

C2. If D(N+1)>D(N)=D, then for every N-point global minimizer A,
    I_D(A) = intersection_{p in A} closed B(p,D)
is strictly covered by the open unit disks centered at A.  Hence its covering radius
is some R(A)<1.  This is stronger than fixed-hull closed saturation, but only at a
right plateau endpoint.

C3. For any normalized KKT stress, the positive contact support is finitely
contraction-rigid once the positive diameter endpoints are fixed.  Therefore
    V(C_+) subset conv(B_+)
and
    conv V(C_+) = conv B_+.

C4. Taking maximal support over the whole KKT polytope defines the canonical force hull
    F(A)=conv B_* = conv V(C_*),
with diam F(A)=D and Vert F(A)=B_*.  Every active constraint incident to a point
outside F(A) has zero multiplier in every KKT stress.  If F is one-dimensional, the
entire positive KKT support is exactly a straight unit chain of integer length D.

New obstruction:
global packing/covering geometry can be essential while remaining universally
KKT-invisible.  Hull saturation does not imply strict complementarity.

Highest-value next lemma:
Weak-contact release theorem: in a contact-minimal diametrally saturated source,
universally zero-KKT contacts either admit a same-D release or are confined to a
boundary-order obstruction.  A plateau-specific alternative is to combine the strict
insertion-body cover with the force hull to obtain a same-cardinality strict sub-D
replacement.

Authoritative dependencies:
docs/theory/01-local-structure.md
docs/theory/02-nonlinear-and-regressions.md
docs/targets/target-a/01-forest-and-kinematics.md (Theorem 63.1 comparison only)
docs/prompts/erdos_problem_99_1.7.9_FINAL_CONTINUATION_PROMPT.md
```
