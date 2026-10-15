# Target C — hole-stable complete-grid order and diameter audit

**Date:** 2026-09-12
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This module removes the remaining topological defect in the complete-grid geometry
from canonical Section 73.  A complete phase-pure train grid inside a rhombic grain
with holes already has a common crossing order: no disk, crosscut tree, trimming, or
boundary-penetration hypothesis is needed.

The mechanism is metric rather than topological.  Canonical Section 68 gives an exact
oriented phase potential.  Once Section 73 purifies the two complete shores to fixed
distinct phase labels, every cross-shore crossing has the same orientation.  The
strict train displacement cones from canonical Theorem 10.6 then fit inside one common
open half-plane.  All selected train centerlines are therefore monotone in one common
linear coordinate, and their equal crossing sign forces a common order.

The resulting path argument globalizes the Target-B complete-grid diameter estimate
to arbitrary holes.  It also gives a finite defect-averaged inequality directly from
canonical Sections 68, 69, and 73.  The proof rederives the needed product-defect
identities; proof-only Section 74 is a compatible precursor but is **not** a dependency.

---

# 76. Complete phase-pure grids have common order even with holes

Put

\[
L={\pi\over3}.
\]

Fix one Section-69 physical grain and let `A,B` be the internally noncrossing,
distinct-phase, all-crossing train families supplied by canonical Section 73.  Write

\[
a=|A|,\qquad b=|B|.
\]

Every train in the grain has a reduced real phase potential `x_v` in one common
half-open bin of width `epsilon`, where

\[
0<\epsilon<L/2,
\tag{76.1}
\]

and a phase label `ell_v in Z/3`.  Thus a real argument of its projective unit-edge
direction can be written

\[
\phi_v\equiv x_v+L\ell_v\pmod\pi.
\tag{76.2}
\]

Canonical (68.16) says that every retained crossing has one orientation `u->v` for
which

\[
\ell_v-\ell_u\equiv1\pmod3,
\qquad
x_v-x_u=\delta_{uv}>0,
\tag{76.3}
\]

where `delta_uv` is the acute-angle excess of that rhombus above `pi/3`.

## 76.1 Phase purity makes every `A x B` crossing have the same orientation

The phase labels are constant on the two shores and are distinct.  Hence one of the
two label differences is `+1 mod 3` and the other is `-1 mod 3`.  Interchange the
names `A,B` if necessary so that

\[
\ell_B-\ell_A\equiv1\pmod3.
\tag{76.4}
\]

Then (76.3) forces **every** retained `A x B` crossing to be oriented from `A` to `B`.
Consequently

\[
\boxed{
\delta_{ab}=x_b-x_a>0
\qquad(a\in A,\ b\in B).
}
\tag{76.5}
\]

In particular

\[
\boxed{
\max_{a\in A}x_a<\min_{b\in B}x_b.
}
\tag{76.6}
\]

Choose integer representatives of the two labels with `ell_B=ell_A+1`, including
adding `pi=3L` to the `B` lift if the labels wrap around modulo three.  Define real
edge-direction arguments

\[
\alpha_a=x_a+L\ell_A,
\qquad
\beta_b=x_b+L\ell_B.
\tag{76.7}
\]

Because all potentials lie in one bin of width `epsilon`, (76.5) gives, for every
pair,

\[
\boxed{
L<\beta_b-\alpha_a=L+(x_b-x_a)<L+\epsilon<3L/2<2L.
}
\tag{76.8}
\]

Let `u_a` and `v_b` be the oriented unit edge vectors with arguments `alpha_a` and
`beta_b` respectively.  Then `det(u_a,v_b)>0` for every pair.

## 76.2 One common projection is strictly monotone on every selected train

Canonical Theorem 10.6 orients a train with unit edge direction `u` so that

\[
h_u(p)=\det(u,p)
\]

strictly increases along its centerline.  Every elementary centerline displacement
then has an argument in the strict cone

\[
(\arg u+L,\arg u+2L).
\tag{76.9}
\]

Indeed, in the crossed strict unit rhombus the other side direction has projective
separation strictly larger than `L`; choosing its sign by the positive determinant
puts its oriented separation in `(L,pi-L)=(L,2L)`.

Orient every `A` train in this canonical direction.  Orient every `B` train in the
**reverse** of its canonical direction.  Therefore the elementary displacements lie
in

\[
(\alpha_a+L,\alpha_a+2L)
\quad(a\in A),
\tag{76.10}
\]

and

\[
(\beta_b-2L,\beta_b-L)
\quad(b\in B).
\tag{76.11}
\]

Put

\[
\alpha_+=\max_{a\in A}\alpha_a,
\qquad
\beta_-=\min_{b\in B}\beta_b,
\qquad
\psi={\alpha_++\beta_-\over2},
\tag{76.12}
\]

and let `e` be the unit vector with argument `psi`.  Equation (76.8) is exactly the
strict angular hypothesis needed for the standard projection cone estimate.  In
particular, for every `a,b`,

\[
\alpha_a+{L\over2}<\psi<\alpha_a+{5L\over2},
\tag{76.13}
\]

\[
\beta_b-{5L\over2}<\psi<\beta_b-{L\over2}.
\tag{76.14}
\]

For example, the lower bound in (76.13) follows from
`beta_- - alpha_+>L`; the remaining bounds follow from the pairwise upper bound
`beta_b-alpha_a<2L` exactly as in the Target-B complete-grid projection argument.
Equations (76.10)--(76.14) imply that every elementary displacement in every selected
oriented train has **strictly positive** projection onto `e`.

Hence the common scalar coordinate

\[
X(p):=e\cdot p
\tag{76.15}
\]

strictly increases along every selected oriented train centerline.  Each selected
centerline is therefore the graph of a continuous piecewise-linear function

\[
Y=f(X)
\]

over one interval, where `Y=(Je)\cdot p`.

No simple-connectedness or boundary information has entered.

## 76.3 Every cross-shore crossing has one graph sign

At an `A`--`B` crossing rhombus, the local forward centerline displacement on the
oriented `A` train is `v_b`.  For the canonical `B` orientation it would be `-u_a`,
because `det(v_b,u_a)<0`; after reversing the `B` train as above, its local forward
displacement is `u_a`.

Thus, at every cross-shore crossing,

\[
\det(v_b,u_a)<0.
\tag{76.16}
\]

Both vectors have positive `X` component.  In `(X,Y)` coordinates, (76.16) says that
the slope of the `A` centerline is larger than the slope of the `B` centerline.
Therefore, as `X` increases through their unique crossing,

\[
\boxed{
A\text{ passes from below }B\text{ to above }B.
}
\tag{76.17}
\]

The sign is the same for every pair in the complete product.

## 76.4 Signed monotone-grid order lemma

We isolate the topology used below.

### Lemma 76.1 — common order for signed `X`-monotone complete grids

Let `A_1,...,A_a` and `B_1,...,B_b` be two finite families of simple arcs in the
plane such that

1. every arc is strictly `X`-monotone and hence a graph over an interval;
2. arcs in the same family are pairwise disjoint;
3. every `A` arc meets every `B` arc exactly once, at an interior proper crossing;
4. at every such crossing, as `X` increases, the `A` graph passes from below the `B`
   graph to above it.

Then all `A` arcs meet the `B` arcs in one common order, and all `B` arcs meet the `A`
arcs in one common order.

### Proof

Fix two `B` arcs, call them `B_1,B_2`, with `X`-domain intervals `I_1,I_2`.

If the interiors of `I_1,I_2` are disjoint, their left-to-right interval order fixes
which crossing occurs first on every `A` arc.

Suppose instead that their interiors overlap.  On the open overlap the two graphs are
disjoint, so their vertical order is constant.  Relabel for this paragraph so that

\[
B_1(X)>B_2(X)
\tag{76.18}
\]

throughout the overlap.  Let one `A` arc cross `B_i` at `X=x_i`.  We claim

\[
x_2<x_1.
\tag{76.19}
\]

If instead `x_1<x_2`, the open interval `(x_1,x_2)` meets the common domain of
`B_1,B_2`.  To see this, write `J=int(I_1) cap int(I_2)`, which is nonempty.  If
`J` lay entirely at or to the left of `x_1`, then `int(I_2)` still extends to the
later interior point `x_2`; consequently the right endpoint of `int(I_1)` would have
to be at most `x_1`, contradicting `x_1 in int(I_1)`.  If `J` lay entirely at or to
the right of `x_2`, the symmetric argument would force the left endpoint of
`int(I_2)` to be at least `x_2`, contradicting `x_2 in int(I_2)`.  Hence choose
`X_0 in J cap (x_1,x_2)`.

By the uniform crossing sign, after crossing `B_1` the `A` graph is above `B_1` at
`X_0`, while before crossing `B_2` it is below `B_2` there.  This would give

\[
A(X_0)>B_1(X_0)>B_2(X_0)>A(X_0),
\]

an impossibility.  Thus (76.19) holds for every `A` arc.

Hence each pair of `B` arcs has one relative crossing order independent of the chosen
`A` arc.  Taking the order seen on any one `A` arc gives a total order that every `A`
arc shares.  The same argument with the roles of the two families interchanged (the
`B` graph passes from above `A` to below it) gives one common order of the `A` arcs
along every `B` arc.  `square`

Apply Lemma 76.1 using (76.15)--(76.17).  We obtain common orders

\[
B_1,\ldots,B_b
\quad\text{along every oriented }A,
\tag{76.20}
\]

and, in the fixed increasing-`X` orientation of every `B`,

\[
A_1,\ldots,A_a
\quad\text{along every oriented }B.
\tag{76.21}
\]

This is the order conclusion that the older Target-B proof obtained from proper
crosscuts of a topological disk.  Here it follows without a disk and without deleting
any additional train.

## 76.5 Hole-stable complete-grid diameter bound

Let `p_00` be the center of the crossing rhombus `A_1 cap B_1`.  Follow oriented
`A_1` through the common order (76.20) to the center of `A_1 cap B_b`, then follow
oriented `B_b` through the common order (76.21) to the center `p_11` of
`A_a cap B_b`.

Both endpoints are centers of source rhombi, hence belong to the convex hull of the
source.  The convex hull has diameter `D`, so

\[
|p_{11}-p_{00}|\le D.
\tag{76.22}
\]

Every intervening centerline displacement on both legs has nonnegative, in fact
positive, projection on `e`.  The selected `B` crossings on the first leg contribute

\[
{v_1\over2}+v_2+\cdots+v_{b-1}+{v_b\over2}
\]

when `b>=2`; for `b=1` that leg is empty.  Thus, uniformly in `b>=1`, its selected
contribution is at least

\[
e\cdot\sum_{j=1}^b v_j-1.
\tag{76.23}
\]

Likewise the selected `A` crossings on the second leg contribute at least

\[
e\cdot\sum_{i=1}^a u_i-1.
\tag{76.24}
\]

Projecting the endpoint displacement and using (76.22) gives the hole-stable analogue
of the Target-B CR estimate:

\[
\boxed{
D\ge
 e\cdot\left(\sum_{a\in A}u_a+\sum_{b\in B}v_b\right)-2.
}
\tag{76.25}
\]

The proof used neither an outer-boundary crosscut nor a penetration-to-boundary
argument.  Hole boundaries may terminate other trains arbitrarily; they do not affect
(76.25).

## 76.6 A finite defect-averaged near-triangular bound

The complete product carries more quantitative information than (76.25) alone.  Define

\[
S_{AB}:=\sum_{a\in A}\sum_{b\in B}\delta_{ab}
       =\sum_{a,b}(x_b-x_a).
\tag{76.26}
\]

Every pair corresponds to a distinct retained rhombus, so `S_AB` is a sub-sum of the
global train angular defect.  Canonical (68.14), `c_0=sqrt(3)/4`, and
`per(K)<=pi D` give

\[
\boxed{
S_{AB}<C_{phase}D,
\qquad
C_{phase}:={\pi^2\sqrt3(2+\sqrt3)\over12}.
}
\tag{76.27}
\]

Put

\[
x_A^+=\max_Ax_a,
\qquad
x_B^-=\min_Bx_b,
\qquad
g=x_B^--x_A^+>0,
\tag{76.28}
\]

and

\[
r_a=x_A^+-x_a\ge0,
\qquad
q_b=x_b-x_B^-\ge0.
\tag{76.29}
\]

Then every product defect is exactly

\[
\delta_{ab}=g+r_a+q_b,
\tag{76.30}
\]

so

\[
S_{AB}=abg+b\sum_ar_a+a\sum_bq_b.
\tag{76.31}
\]

The direction `e` from (76.12) satisfies the exact angle identities

\[
\psi-\alpha_a={L\over2}+{g\over2}+r_a,
\tag{76.32}
\]

\[
\beta_b-\psi={L\over2}+{g\over2}+q_b.
\tag{76.33}
\]

Since `cos(L/2)=sqrt(3)/2` and `|cos'|<=1`,

\[
e\cdot u_a
\ge {\sqrt3\over2}-{g\over2}-r_a,
\tag{76.34}
\]

\[
e\cdot v_b
\ge {\sqrt3\over2}-{g\over2}-q_b.
\tag{76.35}
\]

Let

\[
m_0=\min\{a,b\}.
\]

Equation (76.31) implies

\[
{a+b\over2}g+\sum_ar_a+\sum_bq_b
\le {S_{AB}\over m_0}.
\tag{76.36}
\]

Indeed, if `a>=b`, then

\[
{S_{AB}\over b}=ag+\sum_ar_a+{a\over b}\sum_bq_b
\]

dominates the left side because `a>=(a+b)/2`; the case `b>=a` is symmetric.

Summing (76.34)--(76.35), inserting (76.36) into (76.25), gives the finite inequality

\[
\boxed{
D\ge
{\sqrt3\over2}(a+b)
-{S_{AB}\over\min\{a,b\}}
-2.
}
\tag{76.37}
\]

This is the useful form because it charges angular defect only once per train-scale
shore, not once per crossing.

If

\[
a,b\ge\gamma D
\tag{76.38}
\]

for one fixed `gamma>0`, then (76.27) gives

\[
\boxed{
D\ge {\sqrt3\over2}(a+b)-{C_{phase}\over\gamma}-2.
}
\tag{76.39}
\]

Equivalently,

\[
\boxed{
 a+b
\le {2\over\sqrt3}
\left(D+{C_{phase}\over\gamma}+2\right).
}
\tag{76.40}
\]

By AM--GM,

\[
\boxed{
 ab
\le {1\over3}
\left(D+{C_{phase}\over\gamma}+2\right)^2
={D^2\over3}+O_\gamma(D).
}
\tag{76.41}
\]

Thus every linear complete phase-pure grid, even in an arbitrarily holed physical
grain, obeys the same leading triangular-grid diameter economy as a common-order disk
grid.

## 76.7 What is actually left in the quadratic-core branch

Section 73 made grid extraction hole-stable.  Section 76 makes **common order and the
complete-grid diameter bound hole-stable as well**.  Therefore the quadratic-core
obstruction is no longer topological penetration of a complete grid.

The remaining issue is quantitative coverage.  The Fox--Pach theorem gives

\[
a,b\ge\gamma D
\]

for some fixed positive coefficient inherited from the coherent-grain density and the
absolute pseudosegment constant, but current canonical inputs do not make that
coefficient large enough to contradict (76.40), nor do they prove that one extracted
complete grid carries a sufficiently large fraction of all quadratic rhombi.

The next theorem should therefore attack one of the following genuinely quantitative
statements:

1. force a complete phase-pure grid with `a+b>(2/sqrt(3)+c)D` for some `c>0`;
2. cover enough of the quadratic coherent grain by complete grids so that (76.37) can
   be aggregated without losing the defect budget;
3. combine (76.37) with the exact total train/perimeter ledgers to force a source-wide
   area or population contradiction.

Do **not** spend another run proving a disk/common-order reduction for a complete grid:
(76.20)--(76.25) already remove that requirement.

The complementary branch `m=o(D^2)` is unchanged: asymptotically almost all source
points lie outside the positive KKT core.

## 76.8 Dependency and regression audit

The proof depends only on canonical material:

- **Section 68:** oriented phase law (68.16) and the global angular-defect bound
  (68.14);
- **Section 69:** one endpoint-safe real phase bin of width `epsilon<pi/6` on the
  selected grain;
- **Section 73:** internally noncrossing, distinct-phase, all-crossing shores `A,B`;
- **Theorem 10.6:** strict train displacement cones and at-most-one crossing.

Proof-only Section 74 independently derives inverse-`D` phase collapse from the same
inputs.  It is consistent with (76.37) but is not used as a premise.

Regression checks:

- **holes:** completely retained; no complementary region is assumed simply connected;
- **train endpoints:** arbitrary; the order lemma uses only `X`-domain intervals and
  the fact that selected crossings are interior;
- **same-shore crossings:** excluded by canonical Section 73;
- **right-angle rhombi:** cannot occur in this phase-pure retained grid because all
  potentials are in one bin of width `<pi/6`, so (76.8) is strict;
- **additive Cartesian array:** never asserted; (76.25) follows from a two-leg path,
  not from Theorem 10.9;
- **boundary penetration:** unused;
- **contact-isolated source points:** retained in the source; only rhombus centers are
  used for the path endpoints, and they lie in the full source convex hull.

## 76.9 Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Canonical Section 73:
    phase-pure complete A x B grid,
    A and B internally noncrossing,
    a,b=Omega(D) in the quadratic-core branch.

Canonical Section 68 phase law + fixed labels:
    all A x B crossings have one orientation,
    delta_ab=x_b-x_a>0,
    L < beta_b-alpha_a < L+epsilon < 3L/2.

Theorem 10.6 displacement cones:
    orient A canonically and B oppositely;
    one common projection X=e.p strictly increases on every selected train;
    every A crosses every B from below to above.

Signed X-monotone grid lemma:
    pairwise disjoint same-shore graphs + complete equal-sign crossings
      -> one common B order along every A,
         one common A order along every B,
    with no disk hypothesis.

Two-leg path through the common order:
    D >= e.(sum_A u_a + sum_B v_b) - 2.

Let S_AB=sum delta_ab. Then
    D >= (sqrt(3)/2)(a+b) - S_AB/min(a,b) - 2.
Since S_AB < C_phase D and min(a,b)>=gamma D,
    a+b <= (2/sqrt(3))(D+C_phase/gamma+2),
    ab <= D^2/3 + O_gamma(D).

Quadratic-core frontier after Section 76:
    not holes, not grid extraction, not common order;
    force quantitatively enough complete-grid coverage to violate the diameter/global
    packing budget.
```
