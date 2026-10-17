> Generated reading edition · [exact source](../../research/target_c_dominant_pentagon_through_splicing_2026-09-15.md) · source SHA-256 `b567c562312438782fbde9cc62788fc843eccf331c09c2fbe3a9f31b27603b16`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 17 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

# Target C-II — dominant pentagons force a quadratic train-crossing deficit by through-splicing

**Phase 2 preservation provenance:** PR #522, branch research/c2-pair14-g00522-sol-20260915, audited source head 2346fb9c3047f26525579df9aced37bc9759e7f6. Preserve the hostile-audit-passed through-splicing/Mantel-deficit lemma at its proof-only fully force-visible full-core Type-II scope. Its numerical floor is weaker than later current-main floors; no global minimizer, finite motion, C-II closure, or Level I conclusion is claimed.

**Date:** 2026-09-15<br>
**Status:** proof-only full-core Type-II structural theorem; theorem-state authority unchanged<br>
**Scope:** fully force-visible no-container/full-core Type-II train-measure branch<br>
**Dependencies:** bounded-face convexity C51; finite stopped-train geometry; no bounded train return / bounded singleton loop; atomic `pi/3` train-phase support; exact exceptional-face endpoint ledgers<br>
**LEVEL I STATUS:** `STILL OPEN`

The current direct dominant/complement energy theorem treats the dominant atomic
`pi/3` orbit only through its outer terminal population.  It does not use the other
terminal incidences.  Near the low-`t` scalar boundary this loses substantial
information: the bounded endpoint ledger is almost entirely pentagonal, and most of
those pentagon sides belong to the dominant orbit.

A pentagon whose **five** stopping-train incidences all lie in shrinking windows around
one exact triangular `pi/3` orbit has a forced local continuation.  In the lattice
limit its five oriented side directions are, up to rotation/reversal,

```math
a,\quad b,\quad c,\quad -b,\quad -b,
\qquad c=b-a,
\tag{DP.1}
```

so the repeated projective phase contains an opposite-sign pair.  Joining the
midpoints of the `+b` side and either `-b` side through the convex pentagon gives a
phase-preserving **through splice**.  The connector is asymptotically within `pi/6` of
the corresponding train normal.

Splicing one such pair at every all-dominant pentagon turns the dominant stopped trains
into longer phase-consistent monotone paths.  Those paths are still pseudosegments:
two of them meet at most once.  Contracting the splices therefore leaves a simple
intersection graph, while the singleton contracted vertices still induce the original
triangle-free train-crossing graph.  A finite extremal count then forces a quadratic
Mantel deficit.

The resulting new scalar constraint is

```math
\boxed{
K\ge
{8\Delta_2\over U}-2U+t-\kappa
-\sqrt{{U^2\over2}-2\Delta_2},
}
\tag{DP.2}
```

where

```math
\Delta_2={\pi\over2\sqrt3},
\qquad
U={9t\over2}-2\pi-2\delta-\kappa/2,
```

and `K` is the actual outer-terminal occurrence density of the frozen dominant atomic
orbit.  This is an allocation constraint absent from the current direct energy proof.

C-II remains open, but (DP.2) materially restricts the only scalar allocation that was
still minimizing the dominant/complement energy functional.

---

## 1. Bounded pentagons are genuine convex polygons

In the fully force-visible C-II core, C51 proves that every bounded contact face has a
simple strictly convex boundary cycle and every side is a unit contact.  In particular,
a degree-five exceptional face is a genuine strictly convex unit pentagon; no bridge or
repeated articulation occurrence appears on its boundary.

The audited no-bounded-return theorem excludes a nontrivial complete train whose two
terminal incidences lie on the same bounded face, and bounded singleton loops are also
excluded.  Thus the five train-terminal incidences of one pentagonal face belong to
five distinct complete trains.

These facts are essential below.  The theorem is not a statement about an arbitrary
occurrence-counted degree-five facial walk.

---

## 2. Exact lattice-limit classification of an all-dominant pentagon

Fix one exact atomic orbit

```math
[\phi],\quad[\phi+\pi/3],\quad[\phi+2\pi/3]
\pmod\pi.
```

Freeze projective phase windows of radius `rho` around these three atoms and then take
the source limit, followed by `rho->0`, in the standard train-measure order.

Call a pentagonal bounded face **all-dominant** if all five of its stopping-train side
incidences lie in those windows.

Orient the pentagon boundary counterclockwise.  In the `rho->0` limit every oriented
unit side tends to one of the six triangular-lattice rays.  After rotation write three
representatives

```math
a=(1,0),
\qquad
b=(1/2,\sqrt3/2),
\qquad
c=b-a=(-1/2,\sqrt3/2).
```

Let

```math
r_a=n_a^+-n_a^-,
\qquad
r_b=n_b^+-n_b^-,
\qquad
r_c=n_c^+-n_c^-
```

be the signed ray imbalances in the three projective phases.  Polygon closure gives

```math
r_a a+r_b b+r_c c=0.
```

Since `c=b-a`, linear independence of `a,b` gives

```math
\boxed{
r_a=r_c=-r_b=:r.}
\tag{DP.3}
```

For each phase, its total number of sides is at least `|r|` and has the same parity as
`r`.  The three phase totals sum to five.  If `r=0` their sum would be even.  If
`|r|>=2` their sum would be at least six.  Hence

```math
|r|=1.
```

All three phase totals are therefore positive odd integers summing to five, so they are
exactly

```math
\boxed{3,1,1.}
\tag{DP.4}
```

In the phase occurring three times, the two ray signs occur with multiplicities `2`
and `1`.  Thus there is an opposite-sign same-phase pair.

Strict convexity fixes the cyclic lattice-limit pattern up to rotation and reversal.
One representative is precisely (DP.1):

```math
a,b,c,-b,-b.
```

This six-ray classification is also checked exhaustively by the companion verifier.

---

## 3. The opposite-sign pair is a geometric through pair

Consider the representative pattern (DP.1).  Let the vertices start at the origin and
write `m_e` for a side midpoint.  The `+b` side has midpoint

```math
m_+=a+{b\over2}.
```

The two `-b` sides have midpoints

```math
m_-^{(1)}={3b\over2},
\qquad
m_-^{(2)}={b\over2}.
```

Hence

```math
m_-^{(1)}-m_+=b-a=c,
\qquad
m_-^{(2)}-m_+=-a.
\tag{DP.5}
```

Let

```math
n_b=Jb
```

be the positive train-normal direction.  Both `c` and `-a` make angle exactly `pi/6`
with `n_b` and have positive `n_b` projection `sqrt(3)/2`.

Because the face is convex, either midpoint segment lies entirely in the closed face,
with interior disjoint from the contact graph.  By compactness, uniformly for
all-dominant pentagons in sufficiently small phase windows, one may choose an
opposite-sign pair whose midpoint connector has

```math
\boxed{
\angle(v_{conn},n_b)\le\pi/6+o_\rho(1),
\qquad
v_{conn}\cdot n_b\ge\sqrt3/2-o_\rho(1)>0.
}
\tag{DP.6}
```

The rotated/reversed lattice patterns give the same statement for their repeated
phase.

There is also an orientation interpretation.  The pentagon interior lies to the left
of each counterclockwise boundary edge.  For a `+b` terminal edge the adjacent
rhombic train approaches the face when oriented with positive `n_b` projection; for a
`-b` edge it leaves the face in that orientation.  Thus the connector in (DP.6)
continues an arriving positive-normal train into a leaving positive-normal train.  It
is a genuine **through** splice, not a U-turn.

---

## 4. Simultaneous through-splicing gives phase-monotone paths

Choose one through pair at every all-dominant pentagon.  Make a graph whose vertices
are dominant-orbit complete trains and whose splice edges are the chosen pentagons.

For one phase `j`, orient every train midpoint path in the positive normal direction

```math
n_j=J\phi_j.
```

The finite stopped-train theorem says every rhombic midpoint step lies within angle
strictly less than `pi/6` of the normal to that train's contact direction.  Since the
train direction lies in a shrinking window around `phi_j`, every oriented train step
has positive `n_j` projection.  Equation (DP.6) gives the same property for every
splice connector.

At a bounded endpoint, the boundary sign determines whether the positive-normal train
orientation enters or leaves the face.  Each selected splice joins one entering end to
one leaving end.  Therefore every train vertex in the directed splice graph has
indegree at most one and outdegree at most one.

A directed splice cycle is impossible: traversing it would produce a closed polygonal
curve every segment of which has strictly positive `n_j` projection.  Hence every
splice component is a directed path.

If `M_D` is the number of dominant-window trains and `P_D` the number of selected
all-dominant pentagons, then the splice forest has exactly

```math
\boxed{N_D=M_D-P_D}
\tag{DP.7}
```

components.  Each component is a simple phase-consistent polygonal **supertrain**.

Singleton stopped trains cause no problem.  They contribute zero-length midpoint
pieces, while every selected connector still has strictly positive normal projection;
bounded singleton loops are already excluded.

---

## 5. Two supertrains meet at most once

Take supertrains from two distinct orbit phases.  Their central normal directions are
separated projectively by `pi/3`.  Choose the common projection direction halfway
between those normals.

Every train midpoint segment lies within `pi/6+o_\rho(1)` of its phase normal, and the
same is true of every through connector by (DP.6).  Hence, for sufficiently small
`rho`, every segment of both supertrains has strictly positive projection on this one
common direction.  Both supertrains are therefore graphs over the same linear
coordinate.

Different pentagon connectors have disjoint interiors.  At a pentagon carrying a
selected connector, every other train midpoint path terminates at the boundary and does
not enter the face interior.  Thus intersections between two distinct supertrains can
occur only at original strict-rhombus crossings of their constituent trains.

For any fixed ordered pair of orbit phase labels, the train-phase crossing law gives
one sign to every actual strict-rhombus crossing: the reduced phase on the forward
label is strictly larger than the reduced phase on the backward label.  Consequently
all intersections of the two common-coordinate graphs have the same transverse
crossing sign.

Two graphs over one coordinate cannot have two transverse intersections with the same
sign: their vertical order would have to alternate.  Therefore

```math
\boxed{
\text{any two distinct supertrains intersect at most once.}
}
\tag{DP.8}
```

Same-phase supertrains do not intersect because their constituent train directions are
within one sufficiently small phase window, whereas a strict-rhombus train crossing
requires projective direction separation greater than `pi/3`.

Hence the supertrain intersection graph is simple.

---

## 6. Splices force a quadratic Mantel deficit

Let `E_D` be the number of strict-rhombus crossings among the `M_D` dominant-window
trains.  Splicing does not remove or create any such crossing, and by (DP.8) distinct
original crossings map to distinct edges of the simple supertrain intersection graph.
Thus that graph has exactly `E_D` edges.

Let `r_D` be the number of nonsingleton supertrains.  Every nonsingleton component uses
at least one splice, so

```math
r_D\le P_D.
\tag{DP.9}
```

The remaining

```math
s_D=N_D-r_D
```

supertrains are singleton components, hence original unspliced stopped trains.  Their
induced crossing graph is a subgraph of the original stopped-train crossing graph,
which is triangle-free.  Mantel therefore gives at most `s_D^2/4` edges among them.

Because the whole supertrain graph is simple, the number of edges having at least one
nonsingleton endpoint is at most

```math
r_Ds_D+{r_D(r_D-1)\over2}.
```

Consequently

```math
E_D
\le
{s_D^2\over4}
+r_Ds_D
+{r_D(r_D-1)\over2}.
\tag{DP.10}
```

With `N_D=M_D-P_D`, the right side is increasing in `r_D` throughout the asymptotic
linear regime up to `r_D=P_D`.  Inserting `r_D<=P_D` gives

```math
\boxed{
E_D
\le {M_D^2\over4}-{P_D^2\over2}+O(D).
}
\tag{DP.11
}
```

Thus if

```math
m=\lim {M_D\over D},
\qquad
p=\liminf {P_D\over D},
\qquad
e=\limsup {E_D\over D^2},
```

then the dominant-orbit Mantel deficit

```math
d:={m^2\over4}-e
```

obeys the new structural lower bound

```math
\boxed{d\ge {p^2\over2}.}
\tag{DP.12}
```

No diameter estimate is used in (DP.12); it is a consequence of pentagonal endpoint
closure plus planar train geometry.

---

## 7. Count all-dominant pentagons from the exact endpoint ledgers

Let

- `f` be the number of bounded exceptional faces;
- `Q=sum_F(deg F-4)` over them;
- `f_5` be the number of pentagonal exceptional faces;
- `B_D=Q+4f` be the total bounded train-terminal incidence count;
- `K_D` be the dominant-window outer-terminal occurrence count.

Every exceptional face has degree at least five, so

```math
f_5\ge2f-Q.
\tag{DP.13}
```

The `M_D` dominant trains have exactly `2M_D-K_D` bounded terminal incidences.  Hence
the number of bounded **non-dominant** terminal incidences is

```math
B_D-(2M_D-K_D).
```

Every pentagon which is not all-dominant consumes at least one such non-dominant
incidence.  Therefore the number `H_D` of all-dominant pentagons satisfies

```math
\begin{aligned}
H_D
&\ge f_5-\left[B_D-(2M_D-K_D)\right]\\
&\ge 2M_D-K_D-2Q-2f.
\end{aligned}
\tag{DP.14
}
```

We selected one splice from every all-dominant pentagon, so `P_D=H_D`.  After dividing
by `D`,

```math
\boxed{
p\ge
\left[2m-K-2\chi-2\varphi\right]_+,
}
\tag{DP.15}
```

where

```math
K=\lim {K_D\over D},
\qquad
\chi=\lim {Q\over D},
\qquad
\varphi=\lim {f\over D}.
```

---

## 8. Eliminate the hidden orbit and face variables

Let

```math
A=x\sigma
```

be total absolute atomic train mass and let

```math
C={T-q/2\over D}.
```

The exposed-hull theorem gives `A<=C`.  For the dominant orbit,

```math
\boxed{m\ge{4\Delta_2\over C}.}
\tag{DP.16}
```

Also, if `d=m^2/4-e` is its Mantel deficit, the standard orbit decomposition gives

```math
d\le {A^2\over4}-\Delta_2
\le {C^2\over4}-\Delta_2.
\tag{DP.17}
```

Indeed, writing `R=A-m` and using the orbitwise Mantel bound outside the dominant
orbit,

```math
{A^2\over4}-\Delta_2-d
\ge {Rm\over2}\ge0.
```

Normalize as usual:

```math
t={q-k\over D},
\qquad
\kappa={k\over D},
\qquad
\delta={d_{out}\over D},
```

```math
U={9t\over2}-2\pi-2\delta-\kappa/2,
\qquad C\le U.
```

The exact ledgers give

```math
\chi=2t-\pi-\delta,
\qquad
2\varphi=C-{t\over2}+{\kappa\over2}.
\tag{DP.18}
```

Insert (DP.16) and (DP.18) into (DP.15).  Using the definition of `U`, this becomes

```math
p\ge
{8\Delta_2\over C}-K-C+t-U-\kappa.
\tag{DP.19}
```

The function `8Delta2/C-C` is strictly decreasing, so `C<=U` implies

```math
\boxed{
p\ge
\left[
{8\Delta_2\over U}-K-2U+t-\kappa
\right]_+.
}
\tag{DP.20}
```

On the other hand, (DP.12) and (DP.17) give

```math
p\le\sqrt{2d}
\le
\sqrt{{U^2\over2}-2\Delta_2}.
\tag{DP.21}
```

If `K` were smaller than the right side of (DP.2), equations (DP.20)--(DP.21) would be
incompatible.  Therefore every survivor obeys the promised allocation constraint

```math
\boxed{
K\ge K_{sp}(t,\delta,\kappa):=
{8\Delta_2\over U}-2U+t-\kappa
-\sqrt{{U^2\over2}-2\Delta_2}.
}
\tag{DP.22
}
```

This is the main scalar output of the theorem.

---

## 9. Numerical scale at the current frontier

For the stronger matched atomic input on this branch,

```math
C_{22}=2\sqrt{\Delta_2}+0.00522,
```

the current direct-energy weakest point at `t=1.83240` has

```math
U=C_{22},
\qquad
\delta=0.0263845395\ldots,
\qquad
\kappa=0.
```

There (DP.22) gives approximately

```math
\boxed{K\ge1.71177,}
```

whereas the unconstrained direct-energy allocation minimizes near

```math
K\approx1.64394.
```

Thus the new constraint is active by a macroscopic margin; it is not a vanishing
endpoint refinement.  The companion scalar note propagates it through the direct
energy functional.

---

## 10. Scope and non-implications

- The pentagon splice is performed only inside bounded faces whose five train endpoints
  all lie in the frozen dominant-orbit windows.
- Exactly one connector is selected per such pentagon, so connector interiors are
  pairwise disjoint.
- The splice is a topological/counting device.  It does **not** assert a new physical
  contact, a bar-preserving deformation, or a valid source motion through the pentagon.
- The proof uses the strict convexity of bounded faces and the no-bounded-return
  endpoint theorem; it does not apply to an arbitrary plane graph facial walk.
- The `rho->0` compactness step is essential: the connector cone statement is
  asymptotic, not an exact finite `pi/6` inequality for every pentagon.
- Contact-isolated source points play no role and remain in the full source.

**Disposition:** proof-only structural strengthening.  C-II and Level I remain open.
