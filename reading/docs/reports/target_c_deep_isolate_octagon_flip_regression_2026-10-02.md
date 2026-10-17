> Generated reading edition · [exact source](../../../docs/reports/target_c_deep_isolate_octagon_flip_regression_2026-10-02.md) · source SHA-256 `4b4054db14e3525247f47e1fab42e80f9185872c3bb60f72530990547cdbce82`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-2D4BB03CBE46","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — deep diameter slack does not supply a strict isolate repair

candidate strict local isolate repair -> unchanged contact count and fewer
actual diameters -> lexicographic C-II contradiction.

**Date:** 2026-10-02.
**Starting branch HEAD:** d08fde2e0afcdca40e6e6f24f8aea6a907104c6e.
**Current main/state:** fbeae9b3fa18a63e07573676b4e2e512a91ca4d5;
2026-09-14.audit.51.
**Branch/mission:** swarm/sol/gap-stress-cycle-20261001; test strict lower-distance
repair for a deep isolate after a small finite core swap.
**Classification:** exact regression against a geometric repair lemma; full
proof for the parametric family below. No canonical source counterexample.
**Level I / C-II:** OPEN / OPEN.

## 1. Rejected lemma and repaired scope

The loaded-hull estimate gives a uniform upper-distance margin for deep interior
isolates. A possible next closing lemma was:

> If a small finite core move preserves old contacts, weakly shortens all old
> diameters, and strictly shortens one, every isolate with a fixed upper-distance
> margin has a small adjustment preserving all lower distances strictly above one.

This is false even with a connected unit-contact core, a two-dimensional loaded
hull, amplitude below 1/(2D), and complete upper-distance feasibility. A rational
13-point family has no strictly unit-separated isolate position in a fixed
half-unit neighborhood after the core move. Its only locally feasible positions
create three new contacts.

The family fails canonical local trapping at four nonloaded core vertices, and
the two changed contact edges face an inactive octagon. It therefore does not
disprove a repair theorem using full local trapping and actual global O-O cuts.
Those hypotheses, or a genuinely nonlocal relocation, are the repaired obligation.

## 2. Exact source

Choose any rational

```math
0<t\le1/40,\qquad
a={1-t^2\over1+t^2},\qquad b={2t\over1+t^2},\qquad
r=a+b,\qquad R=r+1.
```

Then a^2+b^2=1, a>0.99, 0<b<1/20, r>1, and R>2.
Take these thirteen points:

- four inner axial points ($`\pm r,0`$), ($`0,\pm r`$);
- four corners ($`\pm a,\pm a`$);
- four outer axial points ($`\pm R,0`$), ($`0,\pm R`$);
- the contact isolate z=(0,0).

The inner axial points and corners, in alternating cyclic order, form a convex
unit octagon. Add four radial unit spokes from each inner axial point to its
outer point. These are exactly the twelve old contacts.

An adjacent axial/corner vector has components a and b up to signs, so has
length one. Every other inner-ring distance is at least
min(2a,sqrt(2)r)>1. Every outer-ring distance other than its radial spoke is at
least sqrt(2+2b)>1; outer-outer distances are at least sqrt(2)R>1.
The isolate's inner-ring distances are r or sqrt(2)a, both strictly above one.
Thus the contact graph is a connected eight-cycle with four leaves, hence
bipartite and triangle-free.

The convex hull is the outer diamond F:

```math
|x|+|y|\le R.
```

The ring lies strictly in it because 2a<R. The full diameter is D=2R,
with exactly the two opposite outer pairs as actual diameters. Ring-ring and
outer-ring distances are less than D since the inner ring has norm at most
sqrt(2)a<R. All four loaded points are outer axial points. Thus q=4, h=2,
and d_H=2.

The isolate is deep in F: its boundary distance R/sqrt(2) exceeds sqrt(2),
in particular 1/2. Its largest original source distance is R=D/2.
Any adjustment of z by at most 1/2 retains a large upper margin even after
the core move below.

## 3. Small finite core move with no upper obstruction

Move only the right inner point (r,0) and its outer endpoint (R,0) by

```math
\Delta=(-2b,0),\qquad s=2b.
```

Their new positions are (a-b,0) and (a-b+1,0). The spoke stays unit.
The two ring contacts at the right inner point now have vectors (b,a) and
(b,-a), again unit. All other contacts are unchanged.

Every distance to the moving outer point strictly decreases, since every fixed
point has x-coordinate at most a<a-b+1. Every distance from the moving inner
point either stays unchanged (its corner contacts and moving spoke) or
decreases: all its other fixed neighbors have x-coordinate at most zero.
Its distances to the top and bottom inner points become sqrt(2), and to
the left inner point 2a>1. The moving outer point's distances to the right
corners become sqrt(2-2b)>1. All remaining noncontacts stay above one.
Hence the core remains unit-separated with exactly its twelve old contacts.

The horizontal outer diameter strictly shortens; the vertical diameter stays
at D. No inactive pair becomes a diameter. This is an actual finite
old-contact-preserving upper-feasible move, with one actual diameter removed.

It is inside the ultrasmall regime:

```math
s<0.1,\qquad D<4.1,\qquad 2sD<0.82<1,
```

so s<1/(2D)<D-sqrt(D^2-1). These are strict finite bounds for the stated
parameter interval, not numerical approximations to feasibility.

## 4. Complete local lower-obstruction certificate

Write c=a-b>0. The four post-move inner axial points are

```math
L=(-r,0),\quad U=(0,r),\quad P=(c,0),\quad V=(0,-r).
```

Their quadrilateral contains the closed radius-1/2 disk about the origin.
The distances from the origin to its four sides are r/sqrt(2) and

```math
{cr\over\sqrt{c^2+r^2}}
={a^2-b^2\over\sqrt2}
={1-2b^2\over\sqrt2},
```

both strictly greater than 1/2.

The upper triangle LUP has circumcenter z_+=(-b,b) and circumradius exactly
one. Its lower reflection LVP has circumcenter z_-=(-b,-b), also of radius
one. All three squared circumcenter-vertex distances equal a^2+b^2=1.

Every point p in either triangle is within one of a vertex. Explicitly,
if p=sum_i lambda_i v_i is a convex combination of its vertices, then

```math
\sum_i\lambda_i|p-v_i|^2
=\sum_i\lambda_i|v_i-z_\pm|^2-|p-z_\pm|^2
=1-|p-z_\pm|^2\le1.
```

If all three distances were at least one, this forces p=z_\pm.
Conversely z_\pm lie in their triangles (b<a) and are unit from all three
vertices. The two triangles cover the post-move axial quadrilateral.

**No isolate position within distance 1/2 of its original location is strictly
more than one from every core point.** The only weakly unit-separated positions
there are z_+ and z_-.

Both positions are feasible against every remaining point. Their minimum
corner distance is sqrt(2)(a-b)>1; their outer-point distances are at least
R-sqrt(2)b>1. Each creates exactly three new contacts with inner axial vertices
and no unit triangle. Thus in these full-source endpoints,

```math
|C_{\rm old}|=12,\quad |H_{\rm old}|=2,\qquad
|C_{\rm new}|=15,\quad |H_{\rm new}|=1.
```

Reducing diameter-pair count after increasing contact count does not contradict
the canonical lexicographic normalization. A new equality at one is a blocking
event for the required strict extension, even without overlap or a new triangle.

## 5. Canonical hypotheses omitted

Every corner is nonloaded with contact degree two and nonparallel incident
vectors. It fails canonical Theorem 6.1 local trapping. Two positive contact
forces cannot sum to zero there, so the source has no full positive KKT stress.
The cardinal midpoints themselves can be trapped by their two ring contacts
and outward spoke; this does not repair the corner failure.

The changed ring edges are incident to the bounded inactive eight-face.
They cannot belong to a global O-O train, whose allowed incident faces are
strict rhombi and the exterior. In the actual global O-O setting the previous
bounded-face transport theorem supplies one constant label around a bounded
inactive face, explicitly excluding this flip.

The source is not a global-minimizer certificate. D remains bounded as t tends
to zero; there is no quadratic packing population. This packet rejects only
the uniform-small-repair inference from deep upper slack and core connectivity.
It also shows why the inactive-interface branch cannot be silently imported
into the fixed-star global O-O proof. An isolate may be relocatable farther than
1/2 in this sparse source; no global relocation impossibility is asserted.

## 6. Verification and next obligation

Run:

    python3 research/verify_target_c_deep_isolate_octagon_flip_2026_10_02.py

The verifier uses Fraction for coordinates and squared distances. It checks
old/new contacts and diameters, every separation, the small-amplitude threshold,
the loaded hull, the two unit circumcircles, half-unit containment bounds,
and three-contact endpoint repairs. The universal local-covering argument is
proved above; sampling does not replace it.

Canonical dependencies used to reject a source-level upgrade are Theorem 6.1
local trapping and C-I lexicographic normalization in module 56. The O-O
application uses explicitly unpromoted stopped-train/cutset hypotheses.

The repaired attack is precise: for an actual global O-O swap, classify
exterior-face near-unit constraints using local trapping and moving/fixed
labels, or relocate isolates beyond their local feasible cells while retaining
source cardinality and every upper constraint. Deep upper slack supplies
neither conclusion. Forest upper exceptions, bounded rhombus blockers,
exact phase, TWO-SIGN/few-phase, split-star, inactive interfaces, macroscopic
containers, and uncovered full-core sources remain open.

## 7. The repaired degree-five attack transmits the slack to actual contact stars

Now restore one canonical local hypothesis rather than asserting a uniform
repair. Suppose p has five actual unit-contact neighbors in a triangle-free
unit-separated source, and another source point z satisfies

```math
1<|p-z|\le1+s,\qquad 0<s\le1/4.
```

There are exactly four consecutive contact-neighbor pairs whose angular gaps
at p do not contain the ray pz. Call those gaps g_1,...,g_4. They satisfy

```math
g_i>\pi/3,\qquad
\sum_{i=1}^4(g_i-\pi/3)
\le\eta(s):=2\left({\pi\over3}
-\arccos{1+s\over2}\right)
\le{4s\over3}.                                      \tag{1}
```

Consequently the four corresponding strict source-pair lengths l_i obey

```math
1<l_i,\qquad \sum_{i=1}^4(l_i-1)\le{4s\over3}.       \tag{2}
```

This is an actual contact-star conclusion: each pair in (2) is joined to p
by two original unit contacts. No near pair is assigned a KKT multiplier.

To prove it, insert pz in the cyclic order of the five unit rays. Unit separation
from each of the two neighboring unit-contact endpoints gives an inserted
angular gap at least arccos(|p-z|/2), hence at least arccos((1+s)/2).
The other four angular gaps exceed pi/3; equality would be a forbidden unit
triangle at p. Summing the six gaps to 2pi proves the first bound. The derivative
of eta is 2/sqrt(4-(1+s)^2), at most 8/sqrt(39)<4/3 on [0,1/4], proving the
linear bound. Since l_i=2sin(g_i/2), whose derivative is at most one, (2) follows.

Thus a degree-five near-unit blocker on an O(D^-2) swap forces four old
two-contact near-triangles with total excess O(D^-2). This is more structured
than an arbitrary near-unit source pair, but still does not force equality.

### Exact regression against the next equality shortcut

A positive equilibrium at p does not change this last limit into an exact
triangle. For rational 0<h<=1/1000 put epsilon=2arctan(h), r_*=1+10h, and choose
five unit vectors at the angles

```math
\pi/3-2\epsilon,\quad 2\pi/3-\epsilon,\quad \pi,\quad
4\pi/3+\epsilon,\quad 5\pi/3+2\epsilon.
```

Add p=0 and z=(r_*,0). All four ordinary contact gaps are pi/3+epsilon.
The remaining gap is 2pi/3-4epsilon. All source pairs are unit-separated;
exactly the five p-neighbor pairs are unit. In particular there is no unit
triangle, and z is contact-isolated.

For the nearest contact vector u, its x-coordinate satisfies
2u_x<=1+4sqrt(3)h<1+10h=r_*, so z stays strictly more than one from that
contact and its reflection. The other contacts are farther away. Taking weights
2 on u and its reflection, 1 on the next contact vector v and its reflection,
and 4u_x+2v_x>0 on (-1,0), gives an exact positive equilibrium at p.

Coordinates are in Q(sqrt(3)): use rational cos(epsilon), sin(epsilon) and
rotate the usual pi/3 and 2pi/3 unit vectors. The verifier checks three exact
members. This local star has no full-source KKT or global-optimality certificate;
it only rejects degree-five crowding plus local positive equilibrium as an
exact-equality argument.

The next obligation for this degree-five subcase is to use the original
contact-star phase labels, actual rhombus incidence, and global source stress
to repair the four small-slack pairs or force a strict competitor. Degree-three
and degree-four blockers, and the exterior-face global O-O embedding, are not
removed by (1)--(2).
