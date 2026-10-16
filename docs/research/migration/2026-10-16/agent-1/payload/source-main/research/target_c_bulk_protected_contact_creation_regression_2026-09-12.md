# Target C — bulk protected contact creation still leaves the old KKT system unchanged

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Status:** proof-only regression / no-go theorem; theorem authority unchanged.

Canonical Sections 81 and 87 plus proof-only Section 95 already show that a
macroscopic inactive chamber contains linearly many inverse-diameter almost-contact
pairs, and that linearly many of them can be closed simultaneously without changing
the old KKT polytope.  The inverse-diameter scale is not essential to that obstruction.
At any fixed small gap scale there are **quadratically many** deep disjoint pairs.
After a constant-factor separation thinning, quadratically many simultaneous
first-contact motions are feasible, and all of the new contacts still have zero KKT
weight.

Thus the proposed chamber mechanism

```text
sufficiently many protected isolate motions
    -> the active diameter/KKT structure must change
```

is false even when "sufficiently many" means `Theta(D^2)`.
A successful macroscopic-container closure must move/reconfigure the old
positive-contact/diameter core itself, or compare the full source to a strict
sub-`D` competitor.  Bulk contact creation inside a protected inactive chamber is
not enough.

---

## 1. Setup

Let `C` be the canonical macroscopic inactive chamber.  Retain the constants from
canonical Sections 77, 81, and 87:

\[
\operatorname{area}(C)=A\ge \alpha D^2,
\qquad
\operatorname{per}(C)=P\le P_0D,
\tag{1.1}
\]

and let `Z` be its contact-isolated source population with isolate-only Oler slack

\[
\sigma={A\over a_0}+{P\over2}+1-|Z|
\le S_0D,
\qquad a_0={\sqrt3\over2}.
\tag{1.2}
\]

Fix constants

\[
0<\varepsilon\le {1\over4},
\qquad
w>1.
\tag{1.3}
\]

Write

\[
U_w=\{x\in C:\operatorname{dist}(x,\partial C)<w\}.
\]

Canonical Lemma 87.1 gives

\[
|Z\cap U_w|
\le {4(w+1)P\over\pi}+1
\le C_wD+1,
\qquad
C_w={4(w+1)P_0\over\pi}.
\tag{1.4}
\]

---

## 2. A fixed gap scale gives a quadratic deep matching

Let `G_epsilon` be the graph on `Z` joining pairs at distance at most
`1+epsilon`, and let `nu_epsilon` be its matching number.
Canonical Theorem 81.1 gives

\[
2\nu_\varepsilon
\ge
{A\over a_0}
\left(1-{1\over(1+\varepsilon)^2}\right)
+{P\over2}
\left(1-{1\over1+\varepsilon}\right)
-\sigma.
\tag{2.1}
\]

Discard the nonnegative perimeter term and use (1.1)--(1.2).  Put

\[
\eta_\varepsilon
:={\alpha\over2a_0}
\left(1-{1\over(1+\varepsilon)^2}\right)>0.
\tag{2.2}
\]

Then

\[
\nu_\varepsilon
\ge \eta_\varepsilon D^2-{S_0\over2}D.
\tag{2.3}
\]

Take a maximum matching `M`.  Because its edges are vertex-disjoint, at most
`|Z cap U_w|` matching edges have an endpoint in `U_w`: assign to each such edge one
boundary-strip endpoint.  Therefore the submatching

\[
M_{deep}:=\{xy\in M:x,y\in C_{-w}\}
\tag{2.4}
\]

satisfies

\[
|M_{deep}|
\ge \eta_\varepsilon D^2-O_{w}(D).
\tag{2.5}
\]

In particular, for all sufficiently large `D`,

\[
\boxed{|M_{deep}|\ge {\eta_\varepsilon\over2}D^2.}
\tag{2.6}
\]

Every edge of this matching is an actual strict almost-contact:

\[
1<|x-y|\le1+\varepsilon,
\qquad x,y\in C_{-w}.
\tag{2.7}
\]

No inverse-diameter threshold is used.

---

## 3. Constant-factor spatial thinning

Orient every edge of `M_deep` and call one endpoint `x_i` the moving center and the
other `y_i` its mate.

A radius-3 disk contains at most 49 unit-separated moving centers: the open
radius-`1/2` disks around such centers are disjoint and lie in the concentric
radius-`7/2` disk.  Hence the greedy thinning in Section 95 gives an index set `J`
with

\[
|J|\ge {|M_{deep}|\over49},
\qquad
|x_i-x_j|>3\quad(i\ne j\in J).
\tag{3.1}
\]

Together with (2.6),

\[
\boxed{
|J|\ge c_{\varepsilon}D^2,
\qquad
c_{\varepsilon}:={\eta_\varepsilon\over98}>0
}
\tag{3.2}
\]

for all sufficiently large `D`.

---

## 4. Quadratically many simultaneous first-contact motions are feasible

For each `i in J`, hold every other source point fixed and move `x_i` along the
segment toward `y_i`.  Because `x_i` is initially contact-isolated, there is a first
contact after a displacement

\[
0<t_i\le |x_i-y_i|-1\le\varepsilon.
\tag{4.1}
\]

Run all selected stopped motions on the common parameter `s in [0,1]`, moving `x_i`
through displacement `s t_i`.

The inner parallel body `C_{-w}` is convex, so every moving point remains in
`C_{-w}`.  Moving-versus-fixed distances stay at least one by the individual
first-contact definitions.

For two moving centers,

\[
|x_i(s)-x_j(s)|
>3-2\varepsilon
\ge {5\over2}>1.
\tag{4.2}
\]

Thus all pairwise lower-distance constraints remain feasible throughout the
simultaneous motion.

The full-source diameter remains exactly `D`.  Every moved point remains in the old
source convex hull, so convex-hull diameter safety gives distance at most `D` to every
fixed source point.  All old diameter endpoints are fixed, and one old core diameter
pair remains at distance `D`.

Likewise every old contact remains unchanged because only originally contact-isolated
points move.

---

## 5. The terminal new contacts are quadratically many disjoint zero-stress stars

At `s=1`, every selected moving center has at least one new unit contact.
No fixed source point can be touched by two selected moving centers.  Indeed, if a
fixed point `z` were a unit contact of both terminal centers, then

\[
|x_i-x_j|
\le t_i+1+1+t_j
\le2+2\varepsilon
\le {5\over2},
\]

contradicting (3.1).  Moving centers never touch each other by (4.2).

Every point touched by a moving center was originally contact-isolated.  All selected
motions remain in `C_{-w}`, so no new contact reaches the old positive contact core.
Consequently the newly created contact graph is a disjoint union of nonempty stars on
formerly isolated vertices, disjoint from the old core.  Because all fixed leaves
were mutually nonadjacent before the motion, these stars create no unit triangle.

There are at least `|J|` distinct new unit-contact edges, hence

\[
\boxed{
E_{new}\ge c_\varepsilon D^2.
}
\tag{5.1}
\]

Now apply the Section-95 virial argument to each new contact component `S`.  It has no
external contact to the old core and no diameter edge.  If `alpha_e>=0` are its
contact multipliers in any normalized nonnegative equilibrium stress, summing the
vertex equilibrium equations after dotting with positions gives

\[
\sum_{e\subset S}\alpha_e=0.
\tag{5.2}
\]

Hence every new multiplier is zero.  Restriction to the old rows and zero extension
across the new rows are inverse maps, so

\[
\boxed{
\mathcal K_{terminal}
=\mathcal K_{old}\times\{0\}_{E_{new}}.
}
\tag{5.3}
\]

In particular the old positive contact core, old diameter graph, normalized KKT
polytope, source cardinality, and global diameter are all unchanged.

---

## 6. Consequence for the macroscopic-container route

For every fixed `epsilon in (0,1/4]`, every sufficiently large survivor in the
macroscopic inactive-chamber branch has another same-cardinality, same-diameter,
triangle-free global-minimizer representative with

\[
\Theta_\varepsilon(D^2)
\]

additional actual unit contacts, all of which remain invisible to every normalized
KKT stress.

Therefore none of the following implications is valid without a separate mechanism
that moves or replaces the old diameter-carrying core:

```text
many protected near contacts
 -> many created contacts
 -> positive force transfer;

quadratically many simultaneous contact events
 -> change of the active diameter graph;

bulk contact creation
 -> strict diameter decrease.
```

This is stronger than the inverse-diameter-scale obstruction in Section 95.  The
remaining chamber problem is genuinely **core-coupled**: one must either deform the
old positive core/diameter support while carrying the inactive population, or build a
new same-cardinality unit-separated source of diameter strictly below `D`.

No source point is deleted and no affine-kernel statement is applied to the protected
isolates.

**Disposition:** rigorous proof-only regression.  C-II remains open.