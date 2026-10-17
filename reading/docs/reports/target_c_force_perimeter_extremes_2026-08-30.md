> Generated reading edition · [exact source](../../../docs/reports/target_c_force_perimeter_extremes_2026-08-30.md) · source SHA-256 `211cb421b7cf42ef474711952329dfda5688f27d5940869913fd7d40b926a5f3`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-67D2A308C86E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_force_perimeter_extremes_2026-08-30.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=b7ca61a9788d9f6bb09ee7193bcc5e4ab137b1d9; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — Target C addendum: exact force-perimeter extremes

**Date:** 2026-08-30  
**Repository state:** `research/target-c-force-hull-v2-2026-08-30`  
**Run type:** proof / convex-diameter classification  
**Target:** Level I candidate route C  
**Depends on:** Target C Theorem C10  
**External theorem used:** the classical planar diameter-graph fact of Hopf--Pannwitz / Sutherland / Erdős that every cycle in a planar diameter graph is odd; equivalently the straight-line diameter graph is a special thrackle.  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

Target C Theorem C10 proved for the reciprocal force polygon `F^*`

$$
\sqrt3D\le\operatorname{per}(F^*)\le2D.
$$

The upper equality case was already classified: it occurs exactly when the positive
diameter graph is a matching.  This note gives an elementary local proof of the lower
bound and completely classifies its equality case.

The two endpoints are therefore rigidly different:

$$
\boxed{
P_*=2D
\iff
H_+\text{ is a matching},
}
$$

whereas

$$
\boxed{
P_*=\sqrt3D
\iff
H_+=K_3\text{ on an equilateral diameter triangle and }\beta\equiv1/3.
}
$$

Thus the force-perimeter parameter continuously measures how far the positive diameter
reactions lie between a two-ended matching regime and a maximally cancelling
three-direction equilateral regime.

---

## 1. Diameter reactions at one vertex occupy at most sixty degrees

Fix a normalized KKT stress `(\alpha,\beta)`.  At a positive diameter endpoint
`b\in B_+`, write

$$
s_b:=\sum_{bk\in H_+}\beta_{bk}>0
\tag{C14.1}
$$

and

$$
g_b=\sum_{bk\in H_+}\beta_{bk}(b-k).
\tag{C14.2}
$$

Every vector `b-k` occurring here has length `D`.

### Lemma C14.1 (sixty-degree diameter cone)

If `bk,bl\in H` are two diameter pairs incident to the same point `b`, then the angle
between `b-k` and `b-l` is at most `\pi/3`.

#### Proof

Let the angle be `\theta`.  Since the entire configuration has diameter `D`,

$$
|k-l|\le D.
$$

But

$$
|k-l|^2
=|(b-k)-(b-l)|^2
=2D^2(1-\cos\theta).
$$

Hence

$$
2(1-\cos\theta)\le1,
\qquad
\cos\theta\ge\frac12,
$$

so `\theta\le\pi/3`. `\square`

Because all pairwise angular distances are at most `\pi/3<\pi`, the incident diameter
directions lie in one closed angular interval of width at most `\pi/3`.  Let `u_b` be
the unit vector along the bisector of a shortest such interval.  Then every incident
diameter vector has projection at least `D\cos(\pi/6)=\sqrt3D/2` onto `u_b`.

### Corollary C14.2 (local reaction lower bound)

$$
\boxed{
|g_b|
\ge
\frac{\sqrt3}{2}D s_b.
}
\tag{C14.3}
$$

#### Proof

Project (C14.2) onto `u_b`:

$$
g_b\cdot u_b
\ge
\frac{\sqrt3}{2}D\sum_{bk}\beta_{bk}
=
\frac{\sqrt3}{2}Ds_b.
$$

Since `|g_b|\ge g_b\cdot u_b`, the result follows. `\square`

Summing over `b` and using

$$
\sum_{b\in B_+}s_b=2\sum_{h\in H_+}\beta_h=2
\tag{C14.4}
$$

immediately recovers

$$
\boxed{
P_*:=\sum_b|g_b|\ge\sqrt3D.
}
\tag{C14.5}
$$

This proof is local and does not use Jung's circumradius theorem.

---

## 2. Equality at one vertex

### Lemma C14.3 (local equality classification)

Equality holds in (C14.3) at `b` if and only if exactly two positive diameter edges
are incident to `b`, their two diameter vectors make angle exactly `\pi/3`, and their
`\beta` weights are equal.

#### Proof

If only one positive diameter vector is present, then

$$
|g_b|=Ds_b>\frac{\sqrt3}{2}Ds_b,
$$

so equality is impossible.

For at least two vectors, let `I` be a shortest containing angular interval of width
`\theta\le\pi/3`, with bisector direction `u_b`.  Every vector in the interior of `I`
has projection strictly larger than `D\cos(\theta/2)` onto `u_b`, while the two endpoint
directions have projection exactly that value.  Therefore equality in

$$
|g_b|
\ge g_b\cdot u_b
\ge D\cos(\theta/2)s_b
\ge\frac{\sqrt3}{2}Ds_b
\tag{C14.6}
$$

forces all three inequalities to be equalities.

The last equality forces `\theta=\pi/3`.  The middle equality forces all positive
weight to lie on the two endpoint directions; a ray from `b` contains at most one
point at distance `D`, so there are exactly two incident positive diameter edges.
Finally equality in the first inequality says the component of `g_b` perpendicular to
`u_b` vanishes.  The two endpoint directions are symmetric at angles `\pm\pi/6` from
`u_b`, so their positive weights must be equal.

Conversely, two equal-weight length-`D` vectors at angle `\pi/3` have resultant
magnitude `\sqrt3/2` times the sum of their magnitudes, giving equality. `\square`

---

## 3. Global lower equality

### Theorem C14 (lower force-perimeter equality)

For a normalized KKT stress,

$$
\boxed{
P_*=\sqrt3D
}
\tag{C14.7}
$$

if and only if `B_+` consists of three points forming an equilateral triangle of side
`D`,

$$
\boxed{H_+=K_3,}
\tag{C14.8}
$$

and

$$
\boxed{\beta_h=\frac13\qquad(h\in H_+).}
\tag{C14.9}
$$

#### Proof

Suppose first that `P_*=\sqrt3D`.  Since (C14.3) is summed with positive quantities,
local equality must hold at every `b\in B_+`.  Lemma C14.3 therefore says every vertex
of `H_+` has degree exactly two.  Hence `H_+` is a disjoint union of cycles.  The
classical planar diameter-graph theorem says every such cycle is odd.  The straight-line
diameter graph is a thrackle, so two vertex-disjoint odd cycles cannot occur.  Thus
`H_+` is one odd cycle

$$
v_0v_1\cdots v_{q-1}v_0.
\tag{C14.10}
$$

At each vertex, the two incident positive diameter edges meet at angle exactly
`\pi/3`.  In particular, at `v_0` the two neighbors `v_1,v_{q-1}` satisfy

$$
|v_1-v_{q-1}|^2
=D^2+D^2-2D^2\cos(\pi/3)
=D^2.
\tag{C14.11}
$$

So `v_1v_{q-1}` is also an edge of the full diameter graph `H`, whether or not it
carries positive `\beta`.

If `q>3`, this chord together with the path

$$
v_1v_2\cdots v_{q-1}
$$

forms a cycle of length `q-1`.  The positive cycle `q` is odd, so `q-1` is even.  This
contradicts the same classical theorem that every planar diameter-graph cycle is odd.
Therefore

$$
q=3,
$$

and `H_+=K_3`.  All three distances are `D`, so the three points form an equilateral
triangle of side `D`.

Lemma C14.3 also says the two incident edge weights agree at every vertex.  Around the
connected triangle all three `\beta` weights are therefore equal.  Since they sum to
one, each equals `1/3`.

Conversely, if `H_+=K_3` on an equilateral diameter triangle with all three weights
`1/3`, then at each of the three vertices the two reaction vectors have length `D/3`
and angle `\pi/3`.  Their resultant has magnitude

$$
\frac{\sqrt3}{3}D.
$$

Summing over the three vertices gives `P_*=\sqrt3D`. `\square`

---

## 4. The two exact endpoint geometries

Combining Theorem C14 with Target C Theorem C10.3 gives

$$
\boxed{
\sqrt3D\le P_*\le2D,
}
\tag{C14.12}
$$

with exact endpoint classifications

$$
\boxed{
P_*=\sqrt3D
\iff
\text{equal-weight equilateral diameter }K_3,
}
\tag{C14.13}
$$

$$
\boxed{
P_*=2D
\iff
H_+\text{ is a matching}.
}
\tag{C14.14}
$$

These are opposite cancellation regimes.

- At the lower endpoint, every positive diameter endpoint receives two equal reactions
  separated by the largest geometrically possible angle `60` degrees.  Reaction
  cancellation is maximal, and the entire positive diameter system is the three-edge
  equilateral cycle.
- At the upper endpoint, no positive diameter endpoint receives two reactions at all.
  There is zero local reaction cancellation.

The unit square sits at the matching endpoint.  The lower endpoint is not excluded by
triangle-freeness because the equilateral triangle has side `D`, not side one.

---

## 5. Weighted leaf refinement

The same local proof gives a useful strictness parameter.  Let

$$
B_1:=\{b\in B_+:\deg_{H_+}(b)=1\}
$$

and put

$$
S_1:=\sum_{b\in B_1}s_b.
\tag{C14.15}
$$

At a leaf `b`, there is no cancellation:

$$
|g_b|=Ds_b.
$$

At every other vertex use (C14.3).  Since `\sum_bs_b=2`,

$$
\boxed{
P_*
\ge
\sqrt3D
+
\left(1-\frac{\sqrt3}{2}\right)D S_1.
}
\tag{C14.16}
$$

Thus any positive `\beta` mass carried by leaf edges of the diameter graph pushes the
force perimeter quantitatively away from the equilateral endpoint.

No uniform positive lower bound for `S_1` is currently known; edge weights can in
principle be highly nonuniform.  Equation (C14.16) should therefore be treated as an
exact weighted refinement, not yet as an asymptotic gap.

---

## 6. Literature audit

The only external graph-theoretic fact used in the equality classification is the
classical planar diameter-graph theorem that every cycle is odd.  It goes back to
Hopf--Pannwitz (1934), Sutherland (1935), and is discussed by Erdős in *On sets of
distances of n points*, American Mathematical Monthly 53 (1946), 248--250.  The same
geometry is often phrased by saying that straight diameter segments form a geometric
thrackle; in particular two vertex-disjoint odd cycles cannot occur.

The proof does not import any quantitative result about arbitrary topological
thrackles.  Only the special planar diameter-graph properties above are used.

---

## 7. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

New local fact:
At a positive diameter endpoint b, any two diameter vectors make angle <=60 degrees.
If s_b is total incident beta weight, then
    |g_b| >= (sqrt(3)/2) D s_b.
Summing gives P_force >= sqrt(3)D without Jung.

Exact local equality:
Exactly two positive diameter edges meet at b, their angle is 60 degrees, and their
beta weights are equal.

Global equality C14:
    P_force = sqrt(3)D
iff H_+ is exactly an equilateral diameter triangle K3 with beta=1/3 on each edge.
Proof: local equality makes H_+ 2-regular; planar diameter cycles are odd and two
disjoint odd cycles cannot occur, so H_+ is one odd cycle.  A 60-degree pair of
consecutive diameter edges makes the two next-nearest vertices another diameter pair;
if the cycle length exceeded 3 this creates an even diameter cycle.  Hence length 3.

Together with C10.3:
    sqrt(3)D endpoint = equal-weight diameter triangle;
    2D endpoint       = positive diameter matching.

Weighted refinement:
If S_1 is total endpoint beta-incidence mass at degree-1 vertices of H_+,
    P_force >= sqrt(3)D + (1-sqrt(3)/2)D S_1.
```
