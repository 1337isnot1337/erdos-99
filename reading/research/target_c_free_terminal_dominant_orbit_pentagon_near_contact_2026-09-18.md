> Generated reading edition · [exact source](../../research/target_c_free_terminal_dominant_orbit_pentagon_near_contact_2026-09-18.md) · source SHA-256 `756e4786e462e9d25731e9dd9c904b6cbb57794c6730c6ea6016df966c0dd043`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "8e3dda633c83025b4ed3c557db6a53d87ca83c25", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_free_terminal_dominant_orbit_pentagon_near_contact_2026-09-18.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "016b2a5622fc4115f177989f6c32f0726f40b1a0d4b0113267b340c20228db0d"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — terminal FREE dominant-orbit pentagon near-contact ears

**Date:** 2026-09-18  
**Status:** proof-only endpoint refinement; theorem-state authority unchanged  
**Scope:** terminal full-core Type-II FREE survivor sequences with `pi D-q=o(D)` and all-phase surplus `mu_D -> mu_*`  
**Depends on:** terminal FREE surplus-endpoint stability; audited outer-geodesic atomic endpoint theorem; audited atomic stopped-train orbit decomposition; terminal FREE transport fan ladder; global contact-degree cap five  
**Certificate:** `research/verify_target_c_free_terminal_dominant_orbit_pentagon_near_contact_2026_09_18.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The local pentagon regression has so far been an obstruction: an empty unit pentagon,
even with rhombi on every side, can approach the three triangular-lattice projective
directions without paying a uniform angular defect. At the exact terminal FREE surplus
endpoint that regression can instead be used as a source-level constraint.

The endpoint identities and the atomless outer walk force almost all atomic stopped-train
mass into one exact `pi/3` phase orbit. Consequently almost every endpoint pentagon has
all five edge directions close to that one orbit. Closure of five unit edge vectors near
one triangular-lattice orbit is discrete: the nearest sixth-root labels must have the
unique five-root zero-sum pattern. That pattern contains two disjoint `120 degree`
ears, and each ear spans a noncontact diagonal whose length tends to one.

Quantitatively, at exact surplus saturation at least

```math
\boxed{
(0.734167166325767\ldots-6\eta-o(1))D
}
\tag{NC.1}
```

bounded pentagons have all five projective edge directions within `eta` of one dominant
three-line orbit. Every such pentagon contains two disjoint diagonals with

```math
\boxed{
1<d\le 2\cos(\pi/3-\eta).
}
\tag{NC.2}
```

Combining this with the four-spoke row of the terminal transport-fan ladder gives a
sharper alternative. Either there are at least

```math
0.105849189639537\ldots D-o(D)
```

singleton trains, or that many outer-to-outer trains, or for every sufficiently small
fixed `eta` there are at least

```math
\boxed{
(0.075083310474139\ldots-6\eta-o(1))D
}
\tag{NC.3}
```

empty fully-rhombic pentagons that simultaneously

1. have at least four rhombic stopped trains running to the actual outer face;
2. have an ear diagonal satisfying (NC.2); and
3. can choose that ear so both of its boundary sides belong to outer-reaching trains.

From these pentagons one can extract a vertex-disjoint matching of such ear diagonals
of size

```math
\boxed{
\left(
0.008342590052682\ldots-\frac23\eta-o(1)
\right)D.
}
\tag{NC.4}
```

The supporting outer-reaching trains are distinct across the matching. Thus the third
branch also contains at least twice the matching size in distinct outer-reaching
rhombic train corridors attached directly to pairwise vertex-disjoint near-contact
ears.

No diameter-decreasing deformation is claimed. The new point is that exact surplus
saturation cannot remain a purely combinatorial pentagon/flower endpoint: it creates a
linear family of core-core nonedges with slack tending to zero, and a positive-density
subfamily of those near-active inequalities is attached on both sides to audited
outer-reaching train corridors.

---

## 1. Endpoint constants

Put

```math
\Delta_2=\frac{\pi}{2\sqrt3},
\qquad
s_2=\sqrt{\Delta_2},
\qquad
g=0.007707,
```

and

```math
C_{707}=2s_2+g
=1.912332613727915\ldots .
\tag{1.1}
```

At the terminal surplus endpoint the preceding stability theorem gives

```math
\frac{b-P_F}{D}\to0,
\qquad
\frac{Q-f}{D}\to0,
\qquad
\frac{\tau_D}{D}\to\frac\pi2+g,
\tag{1.2}
```

and

```math
\frac{Q+4f}{D}\to M_*:=4s_2+2g
=3.824665227455829\ldots ,
\tag{1.3}
```

```math
\frac{P_5}{D}\to p_*:=\frac{M_*}{5}
=0.764933045491166\ldots .
\tag{1.4}
```

The outer walk is asymptotically geodesic, so the audited outer-geodesic theorem applies:
its normalized occurrence-counted projective direction measure converges to Lebesgue
measure on the projective circle.

---

## 2. One exact phase orbit carries almost all atomic train mass

Pass to a subsequence on which the normalized stopped-train direction measures
converge. Let the atomic train masses in absolute `D` normalization be `a_i`, and write

```math
A:=\sum_i a_i.
\tag{2.1}
```

Group the atoms into exact projective `pi/3` orbits. If `M_j` is the total atomic train
mass of orbit `j` and `E_j` its limiting strict-rhombus crossing mass, the audited
atomic orbit decomposition gives

```math
E_j\le\frac{M_j^2}{4},
\qquad
\sum_jE_j=\Delta_2.
\tag{2.2}
```

Let

```math
W:=\max_jM_j.
\tag{2.3}
```

Then

```math
4\Delta_2
\le
\sum_jM_j^2
\le
WA.
\tag{2.4}
```

At zero outer detour, the audited endpoint-incidence theorem sends every atomic train
endpoint to bounded exceptional-face capacity asymptotically. Hence

```math
2A\le
\lim\frac{Q+4f}{D}
=M_*,
\tag{2.5}
```

so

```math
A\le C_{707}.
\tag{2.6}
```

Equations (2.4)--(2.6) force one dominant exact orbit with

```math
\boxed{
W\ge W_0:=
\frac{4\Delta_2}{C_{707}}
=
1.896949674145215\ldots .
}
\tag{2.7}
```

The entire bounded endpoint capacity left after paying the two terminal occurrences of
that orbit is only

```math
\boxed{
M_*-2W_0
=
0.0307658791653984\ldots .
}
\tag{2.8}
```

This is the concentration input used below.

---

## 3. Bounded pentagons inherit the dominant orbit

Fix an `eta` with

```math
0<\eta<\frac{\pi}{6},
\tag{3.1}
```

chosen so the boundaries of the three phase neighborhoods are null for the limiting
train measure. Let `U_eta` be the union of the three projective intervals of radius
`eta` around the dominant orbit.

Because the limiting outer occurrence measure is Lebesgue,

```math
\frac{N_{\rm out}(U_\eta)}D
\to 6\eta.
\tag{3.2}
```

The dominant orbit supplies `(W-o(1))D` stopped trains in `U_eta`, hence
`(2W-o(1))D` terminal face-side occurrences there. At most `(6 eta+o(1))D` of these
can terminate on the outer face. Therefore the bounded exceptional faces contain at
least

```math
(2W-6\eta-o(1))D
\tag{3.3}
```

occurrences whose directions lie in `U_eta`.

The total bounded exceptional-face occurrence count is

```math
Q+4f=(M_*+o(1))D.
\tag{3.4}
```

Thus the number of bounded occurrences outside `U_eta` is at most

```math
(M_*-2W+6\eta+o(1))D
\le
(M_*-2W_0+6\eta+o(1))D.
\tag{3.5}
```

Every bounded pentagon having at least one side direction outside `U_eta` consumes a
distinct occurrence counted in (3.5). Since `P_5=(p_*+o(1))D`, the number
`P_5^{near}(eta)` whose five sides all lie in `U_eta` satisfies

```math
\boxed{
\frac{P_5^{near}(\eta)}D
\ge
c_{\rm near}-6\eta-o(1),
}
\tag{3.6}
```

where

```math
\begin{aligned}
c_{\rm near}
&:=p_*-M_*+2W_0\\
&=0.734167166325767\ldots .
\end{aligned}
\tag{3.7}
```

The boundary-null restriction on `eta` is harmless: only countably many radii fail it,
and the sets `U_eta` are monotone in `eta`.

---

## 4. Five near-lattice unit vectors force two near-unit ears

The next lemma is finite and independent of the asymptotic train machinery.

### Lemma 4.1 — five-root closure

Let `P=(v_0,...,v_4)` be a strict convex unit pentagon. Suppose every projective edge
direction is within `eta` of one fixed three-line `pi/3` orbit, where

```math
10\sin(\eta/2)<1.
\tag{4.1}
```

Then `P` has two disjoint adjacent edge pairs whose turning angles lie in

```math
\left[
\frac{2\pi}{3}-2\eta,\,
\frac{2\pi}{3}+2\eta
\right].
\tag{4.2}
```

Consequently each pair spans a pentagon diagonal `d` satisfying

```math
\boxed{
1<d\le2\cos(\pi/3-\eta).
}
\tag{4.3}
```

#### Proof

Rotate the orbit so its six oriented directions are

```math
r_j=e^{ij\pi/3},
\qquad 0\le j<6.
\tag{4.4}
```

Orient the pentagon edges cyclically and write `u_i=v_{i+1}-v_i`. For each `u_i`
choose the nearest oriented root `r_{j_i}`. Then

```math
|u_i-r_{j_i}|\le2\sin(\eta/2).
\tag{4.5}
```

Pentagon closure gives

```math
\left|\sum_{i=0}^4r_{j_i}\right|
=
\left|\sum_{i=0}^4(r_{j_i}-u_i)\right|
\le10\sin(\eta/2)<1.
\tag{4.6}
```

Every sum of sixth roots is a vector of the triangular lattice
`Z + Z exp(i pi/3)`. Every nonzero vector of that lattice has norm at least one.
Therefore

```math
\sum_{i=0}^4r_{j_i}=0.
\tag{4.7}
```

Let `c_j` count the occurrences of `r_j`. The nonnegative integer system

```math
\sum_jc_j=5,
\qquad
\sum_jc_jr_j=0
\tag{4.8}
```

has exactly the six rotations of

```math
\boxed{(2,0,1,1,1,0).}
\tag{4.9}
```

This is a six-variable finite lattice calculation; the companion certificate exhausts
all `252` weak compositions of five into six parts.

For `eta<pi/6`, strict convexity preserves the cyclic order of the nearest root labels.
The cyclic gap pattern corresponding to (4.9) is therefore

```math
0,2,1,1,2
\tag{4.10}
```

up to cyclic shift. The two gap-`2` positions use disjoint adjacent edge pairs. Their
actual turning angles differ from `2pi/3` by at most `2 eta`, proving (4.2).

If one such pair has edge vectors `u,v` and turning angle `theta<pi`, its ear diagonal
has length

```math
|u+v|=2\cos(\theta/2)
\le2\cos(\pi/3-\eta).
\tag{4.11}
```

The diagonal joins nonconsecutive vertices of a contact face. Equality `d=1` would make
it a unit contact chord inside the strict convex pentagon, contradicting facehood.
Unit separation therefore gives `d>1`. This proves (4.3). `square`

A safe local range is

```math
0<\eta<\eta_{\rm lat}:=2\arcsin(0.1)
=0.200334842323120\ldots ,
\tag{4.12}
```

which also lies below `pi/6`.

Combining Lemma 4.1 with (3.6) proves (NC.1)--(NC.2).

---

## 5. Intersect with the four-spoke outer-fan branch

Use the `k=4` row of the terminal transport-fan ladder. At exact surplus saturation,
put

```math
C_4
=
\frac{\pi-3p_*}{8}
=
0.105849189639537\ldots .
\tag{5.1}
```

That theorem says at least one of the following holds:

```math
S\ge(C_4-o(1))D,
\tag{5.2}
```

```math
L_O\ge(C_4-o(1))D,
\tag{5.3}
```

or the number `F_{5,\ge4O}^{full}` of fully-rhombic pentagons incident to at least four
pentagon-to-outer stopped trains satisfies

```math
F_{5,\ge4O}^{full}\ge(C_4-o(1))D.
\tag{5.4}
```

Assume the third branch. Both `P_5^{near}(eta)` and
`F_{5,\ge4O}^{full}` are subsets of the `P_5` bounded pentagons. Inclusion-exclusion,
(1.4), and (3.6) give

```math
\begin{aligned}
\frac{|P_5^{near}(\eta)\cap F_{5,\ge4O}^{full}|}{D}
&\ge c_{\rm near}-6\eta+C_4-p_*-o(1)\\
&=
c_{4,\rm ear}-6\eta-o(1),
\end{aligned}
\tag{5.5}
```

where

```math
\boxed{
c_{4,\rm ear}
=
C_4-(M_*-2W_0)
=
0.075083310474139\ldots .
}
\tag{5.6}
```

Each pentagon in this intersection has two disjoint near-unit ears from Lemma 4.1.
At most one of its five side trains fails to run to the outer face. Because the two
ears use disjoint pairs of sides, at least one ear has both side trains running to the
outer face.

Thus every pentagon counted in (5.5) supplies a near-unit noncontact diagonal flanked
by two distinct pentagon-to-outer non-singleton rhombic trains. The two supporting
trains are noncrossing because they terminate on the same bounded face.

This proves (NC.3).

---

## 6. A vertex-disjoint matching of outer-braced near contacts

Choose one outer-braced ear diagonal from each pentagon counted in (5.5), and make an
auxiliary graph `H_eta` whose vertices are contact-core source points and whose edges
are these selected diagonals.

The selected diagonals are distinct. The interior of each lies in the open interior of
its own strict convex pentagonal face, and distinct bounded face interiors are
disjoint.

Moreover,

```math
\Delta(H_\eta)\le5.
\tag{6.1}
```

Indeed a selected diagonal can use a core vertex only through a bounded pentagon
incident to that vertex. The number of bounded face sectors at a vertex is at most its
contact degree, and the triangle-free unit-distance neighbor-angle bound gives global
contact degree at most five.

A greedy matching in a graph of maximum degree five has size at least one ninth of its
edge count: after selecting one edge, deleting it and all edges sharing either endpoint
removes at most

```math
1+4+4=9
\tag{6.2}
```

edges. Therefore (5.5) yields a vertex-disjoint matching `M_eta` with

```math
\boxed{
\frac{|M_\eta|}{D}
\ge
\frac{c_{4,\rm ear}-6\eta}{9}-o(1)
=
0.008342590052682\ldots
-\frac23\eta-o(1).
}
\tag{6.3}
```

Every matching edge has length in

```math
\left(1,\ 2\cos(\pi/3-\eta)\right].
\tag{6.4}
```

The two supporting outer-reaching trains for different matching pentagons are also
distinct: a pentagon-to-outer complete train has exactly one bounded terminal face.
Hence the matching of size `m` comes with `2m` distinct outer-reaching rhombic train
corridors.

Equivalently, for every constants

```math
0<\kappa<0.008342590052682\ldots,
\qquad
\varepsilon>0,
\tag{6.5}
```

the exact-endpoint outer-fan branch contains, after passage to that branch subsequence
and for all sufficiently large sources on it, at least `kappa D` pairwise
vertex-disjoint pentagon diagonals of length in `(1,1+epsilon)`, each flanked by two
distinct rhombic stopped trains that reach the actual outer face. Choose a sufficiently
small admissible `eta`, then use (6.3)--(6.4).

---

## 7. What this removes from the endpoint

The known pentagon phase regression remains real. It cannot support a theorem assigning
a fixed positive angular defect to every fully-rhombic pentagon. What changes at exact
terminal FREE surplus saturation is that the regression becomes global and abundant:
the bounded-face endpoint measure has so little room outside one exact atomic orbit that
a linear population of pentagons is forced into the regression regime simultaneously.

The resulting endpoint split is now:

```text
singleton:
  S >= 0.105849189639537 D - o(D);

or outer-loop:
  L_O >= 0.105849189639537 D - o(D);

or outer-braced near-contact:
  for every kappa < 0.008342590052682 and every epsilon > 0,
  at least kappa D pairwise vertex-disjoint core-core nonedges have
  length in (1,1+epsilon),
  each lies as an ear diagonal of an empty fully-rhombic pentagon,
  and each ear is flanked by two distinct noncrossing rhombic trains
  reaching the actual outer face.
```

This is not a C-II contradiction. Existing one-train shears are contact-framework
motions and need not be diameter-nonincreasing for the full source. The new closing
target is more specific: use the two outer-reaching train coordinates adjacent to a
near-active ear inequality, together with active diameter rows, to obtain either a
simultaneous feasible descent on a positive-density matching or a rigidity/stress
payment proportional to the number of near-active ears.

No theorem-state file is changed.
