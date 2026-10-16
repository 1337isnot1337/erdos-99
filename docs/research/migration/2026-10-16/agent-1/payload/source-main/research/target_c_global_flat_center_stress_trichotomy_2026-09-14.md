# Erdős Problem #99 — global flat-center stress trichotomy

**Date:** 2026-09-14
**Target:** C-II, canonical contact-minimal full-core Type-II branch
**Dependencies:** low-`t` flat-center amplification; flat-center contact-degree trichotomy; degree-four activation dichotomy; C26 full-support virial identity; C35 extreme loaded vertices
**Claim class:** proof-only structural refinement awaiting independent audit
**External literature:** no new import

## LEVEL I STATUS

`STILL OPEN`

The low-`t`, small-residual branch now contains a linear population of **distinct**
flat pentagon centers. Existing local work classifies an unloaded center as degree
three or degree four, but leaves the loaded branch coarse. The convex-hull geometry
closes that local gap: a sufficiently flat loaded center has exactly the two face
contacts and no third contact.

Combining that observation with the degree-four hidden-contact theorem and the
full-support virial identity gives a quantitative global trichotomy.

Let

\[
\Delta_2={\pi\over2\sqrt3},\qquad
C_0:=2\sqrt{\Delta_2}+0.00042,
\]

and on a convergent Type-II subsequence write

\[
t:=\lim {q-k\over D},\qquad
\delta:=\lim {b-P_F\over D},\qquad
\kappa:=\lim {k\over D}.
\]

Put

\[
P(t,\delta,\kappa)
:=\pi+C_0-{5t\over2}+\delta+{\kappa\over2}.
\tag{ST.1}
\]

Assume the true force-hull residual satisfies

\[
R_F=o(D).
\tag{ST.2}
\]

The low-`t` flat-center theorem supplies a scale `epsilon_D->0` and a set `V_flat` of
distinct actual source vertices such that

\[
|V_{flat}|\ge (P(t,\delta,\kappa)-o(1))D,
\tag{ST.3}
\]

and every `m in V_flat` is the middle of two consecutive unit contacts

\[
l-m-r,
\qquad |l-m|=|m-r|=1,
\qquad \angle lmr\ge\pi-\epsilon_D.
\tag{ST.4}
\]

For all sufficiently large `D`, these centers split into exactly three classes:

- `L`: positively diameter-loaded centers, each of contact degree **two**;
- `U_3`: unloaded centers of contact degree three;
- `U_4`: unloaded centers of contact degree four.

Thus

\[
|L|+|U_3|+|U_4|=|V_{flat}|.
\tag{ST.5}
\]

Consequently at least one of the following three alternatives holds:

### (A) Loaded degree-two sea

\[
\boxed{
|L|\ge {P(t,\delta,\kappa)\over3}D-o(D).
}
\tag{ST.6}
\]

Every such center contributes one unit to the loaded contact-degree slack

\[
s_B:=\sum_{v\in B_+}(3-\deg_C v),
\]

so

\[
\boxed{
s_B\ge {P(t,\delta,\kappa)\over3}D-o(D).
}
\tag{ST.7}
\]

### (B) Degree-four activation sea

There is a family `H_4` of pairwise endpoint-disjoint inactive source pairs with a
common unit-contact center and length `1+o(1)` such that

\[
\boxed{
|H_4|\ge {2P(t,\delta,\kappa)\over27}D-o(D),
}
\tag{ST.8}
\]

and, on the same diagonal flatness scale,

\[
\boxed{
\sum_{xy\in H_4}(|x-y|-1)=o(D).
}
\tag{ST.9}
\]

### (C) Degree-three stress degeneration

There is a set `E_3` of distinct positive contact edges such that

\[
\boxed{
|E_3|\ge {P(t,\delta,\kappa)\over6}D-o(D),
}
\tag{ST.10}
\]

and, for the normalized relative-interior KKT stress,

\[
\boxed{
\sum_{e\in E_3}\alpha_e
\le R(\epsilon_D)D^2=o(D^2),
\qquad
R(\epsilon):={\sin\epsilon\over\sin(\pi/3-\epsilon)}.
}
\tag{ST.11}
\]

Thus a linear family of actual positive contact edges carries a vanishing fraction of
the total contact virial.

At the present low-`t` endpoint profile

\[
t_{42}={4\over9}\left(\pi+\sqrt{\Delta_2}\right)+0.0013751
=1.8208886379794447\ldots,
\]

with the conservative `delta=kappa=0`,

\[
P(t_{42},0,0)=0.4944166723690961\ldots .
\]

Therefore at least one of

\[
\boxed{|L|/D\ge0.164805557456365\ldots-o(1),}
\tag{ST.12}
\]

\[
\boxed{|H_4|/D\ge0.0366234572125256\ldots-o(1),}
\tag{ST.13}
\]

or

\[
\boxed{|E_3|/D\ge0.0824027787281827\ldots-o(1)}
\tag{ST.14}
\]

holds, with (ST.7), (ST.9), or (ST.11), respectively.

Throughout the broader conditional band `t<=1.8585`, after dropping the nonnegative
`delta,kappa` bonuses, the corresponding coefficients are

\[
0.133462755772569\ldots,
\qquad
0.0296583901716821\ldots,
\qquad
0.0667313778862847\ldots .
\tag{ST.15}
\]

This theorem does not close C-II. It replaces the generic “loaded / degree-3 / degree-4”
flat-center split by three concrete global currencies: linear loaded degree slack,
linear near-contact activation capacity, or linear **low-stress positive contact
support**.

---

## 1. A loaded flat center has contact degree exactly two

Let `m` be loaded and let `l,m,r` be the consecutive face contacts from (ST.4). A
positively diameter-loaded contact vertex is an extreme point of the full source convex
hull. Therefore all source rays from `m` lie in a convex-hull wedge `W_m` whose opening
angle satisfies

\[
\omega_m<\pi.
\tag{ST.16}
\]

The bounded pentagonal face lies inside the source hull. Its sector at `m` is exactly
the sector between the consecutive contact rays `ml,mr`, and by (ST.4) has angle

\[
\theta_m\ge\pi-\epsilon_D.
\tag{ST.17}
\]

No additional contact ray can lie in the interior of this face sector: such an edge
would split the contact face. Hence any third contact ray must lie in the part of the
hull wedge outside that sector. The total angular room there is strictly less than

\[
\omega_m-\theta_m
<\pi-(\pi-\epsilon_D)
=\epsilon_D.
\tag{ST.18}
\]

So a third contact ray would lie within angular distance `<epsilon_D` of one of the
boundary rays `ml` or `mr`.

For two distinct unit-contact neighbors of one source vertex, unit separation forces
the smaller angular separation to be at least `pi/3`; equality would create a forbidden
unit equilateral triangle, so the separation is in fact strictly greater than `pi/3`.
For sufficiently large `D`, `epsilon_D<pi/3`, contradicting (ST.18).

Thus a loaded flat center has no third contact. It already has the two face contacts,
so

\[
\boxed{\deg_C(m)=2\qquad(m\in L).}
\tag{ST.19}
\]

This is stronger than the general loaded bound `deg_C<=3`.

---

## 2. The three classes exhaust all flat centers

The local flat-center contact-degree theorem gives

\[
\deg_C(m)\le4
\tag{ST.20}
\]

for all sufficiently flat centers. C26 gives

\[
3\le\deg_C(m)\le5
\tag{ST.21}
\]

at every unloaded positive-contact vertex. Hence an unloaded flat center has degree
three or four. Section 1 shows a loaded flat center has degree two. Therefore (ST.5)
is an exact partition for all sufficiently large sources.

By the pigeonhole principle, one of `L,U_3,U_4` has size at least `|V_flat|/3`.
Combining with (ST.3) gives the population floor `P D/3-o(D)` for the active branch.

For the loaded class, (ST.19) gives `3-deg_C(m)=1` at every member. Summing inside the
definition of `s_B` proves (ST.7).

---

## 3. The degree-four class gives a stronger activation matching

The degree-four activation theorem already proves that from `V_4` flat centers of
degree four one can select a pairwise endpoint-disjoint hidden-pair family with

\[
|H_4|\ge {2V_4\over9}
\tag{ST.22}
\]

and total hidden-side excess `o(D)` on the diagonal flatness scale. Every degree-four
flat center is unloaded, so `V_4=|U_4|`.

If the degree-four class is the pigeonhole-large class, then

\[
|U_4|\ge {P\over3}D-o(D).
\]

Substitution into (ST.22) gives

\[
|H_4|
\ge {2P\over27}D-o(D),
\]

which is (ST.8). The inherited `L^1` gap statement is (ST.9).

---

## 4. The degree-three class has vanishing total exterior stress

Let `m in U_3`. Besides the two flat-face contacts `ml,mr`, it has one additional
contact edge `mx`; call this the exterior edge `e_m`.

The local degree-three KKT estimate gives, uniformly at flatness scale `epsilon_D`,

\[
\alpha_{e_m}
\le
R(\epsilon_D)\min\{\alpha_{ml},\alpha_{mr}\}
\le
{R(\epsilon_D)\over2}
(\alpha_{ml}+\alpha_{mr}).
\tag{ST.23}
\]

The normalized full-support virial identity is

\[
\sum_{e\in C}\alpha_e=D^2.
\tag{ST.24}
\]

When (ST.23) is summed over the distinct centers `m in U_3`, an actual contact edge can
occur among the two selected face-edge terms at most twice, once from each endpoint.
Therefore

\[
\sum_{m\in U_3}
(\alpha_{ml}+
\alpha_{mr})
\le2D^2.
\tag{ST.25}
\]

Equations (ST.23)--(ST.25) yield

\[
\boxed{
\sum_{m\in U_3}\alpha_{e_m}
\le R(\epsilon_D)D^2.
}
\tag{ST.26}
\]

Let `E_3` be the set of distinct edges among the `e_m`. One contact edge has only two
endpoints, so it can be the designated exterior edge for at most two centers. Thus

\[
|E_3|\ge {|U_3|\over2}.
\tag{ST.27}
\]

If the degree-three class is pigeonhole-large,

\[
|E_3|
\ge {P\over6}D-o(D),
\]

which proves (ST.10). Since the weights are nonnegative, deduplicating the multiset of
`e_m` cannot increase the total weight; (ST.26) therefore proves (ST.11).

Because `epsilon_D->0`,

\[
R(\epsilon_D)\to0.
\]

So this linear positive-contact family carries `o(D^2)` total KKT weight even though
the whole contact graph carries exactly `D^2`.

---

## 5. Numerical certificate

At the current endpoint profile,

\[
P=0.4944166723690961698\ldots .
\]

The three relevant divisions are

\[
{P\over3}=0.1648055574563653899\ldots,
\]

\[
{2P\over27}=0.0366234572125256422\ldots,
\]

\[
{P\over6}=0.0824027787281826950\ldots .
\]

For `t<=1.8585`, the conservative floor

\[
P\ge0.4003882673177079301\ldots
\]

gives the constants displayed in (ST.15).

The companion script checks these constants and the finite angular inequalities. The
stress estimate itself is exact algebra after the already-proved local KKT ratio and
virial identity.

---

## 6. Frontier effect

The low-`t`, small-residual survivor is now forced into one of three sharply different
failure modes:

```text
(A) Omega(D) loaded degree-2 flat centers
    -> Omega(D) loaded degree slack;

(B) Omega(D) endpoint-disjoint hidden near-contacts
    -> o(D) aggregate activation gap;

(C) Omega(D) actual positive contact edges
    -> o(D^2) aggregate KKT stress.
```

Branch (B) is aligned with the separate pentagon activation-budget theorem. Branch (C)
is a new stress-degeneration target: a future rigidity argument can try to delete or
soften a linear family whose total stress is negligible compared with the `D^2` virial.
Branch (A) directly couples the pentagon sea to the near-extremal Woodall diameter
vertices and to the exact loaded-slack ledger.

No branch is eliminated here. No individual positive KKT multiplier is given a
uniform lower bound, and no same-cardinality strict sub-`D` competitor is constructed.
C-II and Level I remain open.

## 7. Scope audit

- The theorem uses the contact-minimal fully force-visible C-II branch and its
  relative-interior positive KKT stress.
- The low-`t` population constants inherit proof-only AG42 `0.00042`.
- The flat centers are distinct actual source vertices by the low-`t` flat-center
  amplification theorem.
- The loaded degree-two proof uses only extremality, convex-hull wedge geometry,
  face consecutiveness, and the triangle-free `>pi/3` contact-ray separation.
- The degree-four matching and its `o(D)` gap budget are inherited from the current
  degree-four activation theorem.
- The degree-three stress sum uses no lower bound on any KKT multiplier.
- Contact-isolated source points remain in the source.
- No exact hidden contact, unit triangle, or strict smaller-diameter source is claimed.
