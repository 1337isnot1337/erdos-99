# Target C-II — the linear high-`t` blocker fork contains a growing vertex-disjoint diameter staircase

**Date:** 2026-09-17  
**Status:** proof-only structural strengthening; no canonical promotion claimed  
**Scope:** the C65-normalized full-core/no-macroscopic-container Type-II high-`t` branch with `t=(q-k)/D<=1.8687`  
**Dependencies:** high-`t` exact-antipodal/strong-TB1 density fork; global one-sided switch-caterpillar theorem; canonical full-source hull circumradius estimate from Section 155; convex geometric-thrackle property of actual diameter edges  
**Certificate:** `research/verify_target_c_high_t_blocker_matching_star_collapse_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The current high-`t` endpoint leaves a linear-density alternative on one side of the common diameter-routing hub:

\[
|E_D|+|S_D|>c_*D-o(D),
\qquad
c_*={791\over160{,}000{,}000}=0.00000494375,
\tag{BM.1}
\]

where `E_D` consists of exact-antipodal interfaces carrying an opposite-transverse pair of switching diameter bars and `S_D` consists of strong one-bar interfaces. The global switch theorem puts every one of these bars into one ordered train-cut caterpillar forest.

A remaining apparent escape was that linearly many tagged blockers might reuse only a few caterpillar hubs of linear diameter degree. The full-source near-circular estimate rules this out. Every actual diameter vertex has degree only `O(D^(3/4))`. Consequently a linear blocker family contains an unbounded `Omega(D^(1/4))` vertex-disjoint subfamily.

More precisely, put

\[
c_1={c_*\over2}={791\over320{,}000{,}000}
=0.000002471875,
\qquad
\kappa=4\,3^{1/8}.
\tag{BM.2}
\]

Along every unbounded survivor sequence, at least one of the following occurs after passage to a subsequence.

### BM-S — strong-TB1 matching

There are

\[
\boxed{
\left({c_1\over\kappa}-o(1)\right)D^{1/4}
}
\tag{BM.3}

pairwise vertex-disjoint strong-TB1 switching diameter bars. They are pairwise crossing straight chords, belong to the same ordered hubward train-cut forest, have distinct switch-interface tags, and retain the uniform strong-TB1 first-order margin.

### BM-E — exact-antipodal dipole braid

There are

\[
\boxed{
\left({c_1\over4\kappa}-o(1)\right)D^{1/4}
}
\tag{BM.4}

exact-antipodal interfaces whose complete chosen opposite-transverse blocker pairs have pairwise disjoint endpoint sets. Hence every diameter bar in one selected pair crosses every diameter bar in every other selected pair. The two bars within each interface still have opposite transverse signs.

In both branches all extracted exact diameter chords have midpoint distance

\[
\boxed{
O(D^{3/4})
}
\tag{BM.5}

from one common source circumcenter. Thus after scaling by `D` they form an unbounded tagged family of pairwise crossing, asymptotically centrally-antipodal diameter chords. Their laminar interval supports retain the one-sided staircase: a blocker born at an interface crosses every selected row cut between that interface and the common hubward boundary.

This is a genuine strengthening of the current fork. A single high-degree star, or any bounded set of caterpillar hubs, cannot absorb the positive-density blocker population.

---

## 1. Full-source near-circularity gives a sublinear diameter-degree cap

Let `K` be the convex hull of the entire source and let `o` be a circumcenter. The canonical source-hull part of Section 155 gives, for

\[
\eta=3^{1/4}\sqrt D,
\tag{BM.6}
\]

\[
\boxed{
K\subset B(o,R),
\qquad
{D\over2}\le R<{D\over2}+\eta.
}
\tag{BM.7}

Take two distinct actual diameter partners `y,z` of one source point `b`. Write

\[
|b-y|=|b-z|=D,
\qquad
\theta=\angle ybz.
\]

Since the source diameter is `D`, `|y-z|<=D`, hence `theta<=pi/3`. The triangle `byz` is acute and has circumradius

\[
R_{byz}={D\over2\cos(\theta/2)}.
\]

Because its three vertices lie in `K`, its minimum enclosing circle has radius at most `R`. Therefore

\[
{D\over2\cos(\theta/2)}< {D\over2}+\eta,
\]

so

\[
\boxed{
\theta<\Theta_D:=2\arccos\left({D\over D+2\eta}\right).
}
\tag{BM.8}

Distinct diameter partners are unit-separated. If their angular separation at `b` is `theta'`, then

\[
2D\sin(\theta'/2)\ge1,
\]

and hence

\[
\boxed{
\theta'\ge\delta_D:=2\arcsin{1\over2D}.
}
\tag{BM.9}

All diameter-partner rays at one vertex lie in one angular interval of width at most

\[
\theta_{cap,D}:=\min\{\pi/3,\Theta_D\}.
\]

Ordering them in that interval gives the exact degree bound

\[
\boxed{
\Delta(H)
\le
\Delta_D:=1+\left\lfloor{\theta_{cap,D}\over\delta_D}\right\rfloor.
}
\tag{BM.10}

As `D->infinity`,

\[
\Theta_D=(4\,3^{1/8}+o(1))D^{-1/4},
\qquad
\delta_D=(1+o(1))D^{-1},
\]

and consequently

\[
\boxed{
\Delta(H)\le(\kappa+o(1))D^{3/4},
\qquad
\kappa=4\,3^{1/8}.
}
\tag{BM.11}

This estimate is source-wide. It applies to every blocker bar below, independently of its KKT multiplier.

---

## 2. The positive-density fork has a dominant mechanism

The strong blocker theorem gives (BM.1). Therefore

\[
\boxed{
\max\{|E_D|,|S_D|\}
>c_1D-o(D),
\qquad
c_1={791\over320{,}000{,}000}.
}
\tag{BM.12}

Pass to a subsequence on which the same side of the fork is dominant.

The switching sets of distinct interfaces on the chosen hub side are pairwise edge-disjoint. The global switch theorem also puts their union `X` inside one common train-cut diameter graph and proves that `X` is a caterpillar forest. In particular every selected blocker subgraph is a forest of maximum degree at most `Delta_D`.

---

## 3. Strong-TB1 density forces a growing matching

Assume the `S_D` side of (BM.12). Choose the certified strong TB1 bar `h_i` at each `i in S_D`, and let `Y_D` be the graph formed by those bars.

The bars are distinct because different interfaces have disjoint switching supports. Also `Y_D` is a subgraph of the forest `X`; hence it is a forest and

\[
\Delta(Y_D)\le\Delta_D.
\tag{BM.13}

A finite forest of maximum degree `Delta` has an edge coloring with `Delta` colors. One elementary proof removes a leaf edge, colors the smaller forest inductively, and uses at the nonleaf endpoint one of the `Delta` colors not already present there. Therefore the largest color class is a matching containing at least `|E(Y_D)|/Delta_D` edges.

Using (BM.11)--(BM.12),

\[
\nu(Y_D)
\ge{|S_D|\over\Delta_D}
>
\left({c_1\over\kappa}-o(1)\right)D^{1/4}.
\tag{BM.14}

This proves (BM.3).

Every two edges in this matching are vertex-disjoint actual diameter edges. The actual diameter graph is a convex straight-line geometric thrackle, so every two of them cross. Each edge remains tagged by a distinct strong-TB1 interface and retains the strong local inequality

\[
n_i\cdot w\ge D\sin\gamma
\]

for every unit local opening direction `w`, with the fixed `gamma=113/640,000,000` from the parent theorem.

---

## 4. Exact-antipodal density forces many vertex-disjoint dipole bundles

Assume instead the `E_D` side of (BM.12). At each exact-antipodal interface `i`, choose the parent theorem's two switching diameter bars

\[
P_i=\{h_i^+,h_i^-\}
\tag{BM.15}

with opposite transverse signs. Different `P_i` are edge-disjoint because the switching supports are disjoint.

Call two interface bundles `P_i,P_j` **conflicting** when their endpoint sets intersect. Each bundle uses at most four source vertices. Fix one endpoint `v` of `P_i`. At most `Delta_D` actual diameter bars are incident with `v`. Since selected blocker bars belonging to distinct interfaces are distinct, at most `Delta_D` other bundles can meet `P_i` through this particular endpoint. Summing over the at most four endpoints, the bundle-conflict graph has maximum degree at most

\[
4\Delta_D.
\tag{BM.16}

A greedy independent-set selection therefore retains at least

\[
{|E_D|\over4\Delta_D+1}
>
\left({c_1\over4\kappa}-o(1)\right)D^{1/4}
\tag{BM.17}

bundles with pairwise disjoint endpoint sets. This proves (BM.4).

For two retained distinct interfaces `i,j`, every edge of `P_i` is vertex-disjoint from every edge of `P_j`. Hence the convex diameter-thrackle property forces all four cross-interface edge pairs to cross geometrically. Within each retained bundle the two bars still have the opposite transverse signs supplied by exact antipodality.

This rules out the possibility that the linear exact-antipodal obstruction is supported by a bounded collection of repeatedly reused diameter vertices.

---

## 5. All extracted chords are almost centrally antipodal

The same source circumcenter in (BM.7) controls every actual diameter edge `xy`. Let

\[
m={x+y\over2}.
\]

The parallelogram identity gives

\[
|m-o|^2
={|x-o|^2+|y-o|^2\over2}-{D^2\over4}
\le R^2-{D^2\over4}
<D\eta+\eta^2.
\tag{BM.18}

Therefore

\[
\boxed{
|m-o|<L_D:=\sqrt{D\eta+\eta^2}
=(3^{1/8}+o(1))D^{3/4}.
}
\tag{BM.19}

If `d=(x-y)/D` is the oriented unit diameter direction, then

\[
x-o=(m-o)+{D\over2}d,
\qquad
y-o=(m-o)-{D\over2}d.
\tag{BM.20}

Thus every extracted matching edge or dipole-bundle edge has normalized endpoints within `O(D^{-1/4})` of an antipodal pair on the radius-`1/2` circle about `o/D`.

This central localization is simultaneous for the entire extracted family; it is not an interface-by-interface choice of center.

---

## 6. The extracted family retains the laminar staircase tags

Work on the pre-hub side; the post-hub side is the reversed statement. In the interval coordinates of the common-hub theorem, every switching diameter edge born at interface `i` has

\[
a_h=i,
\qquad b_h\ge k,
\tag{BM.21}

where `k` is the common hub index. Hence its cut-support interval is

\[
I_h=\{i+1,\ldots,b_h\},
\tag{BM.22}

and it crosses every selected hubward row cut after its birth interface and before the hubward edge of the selected shore.

The matching extraction in BM-S and the bundle extraction in BM-E delete interfaces but do not alter these support intervals. Consequently the retained blockers have distinct ordered birth tags and one-sided nested incidence with all later selected cuts toward the hub.

Together with the common-cut ordered-thrackle theorem, this produces an unbounded exact object:

```text
Omega(D^(1/4)) vertex-disjoint tagged blocker objects
+ exact diameter length D
+ pairwise geometric crossing across distinct objects
+ one common train-cut bipartition and caterpillar order
+ one-sided laminar staircase support toward the common hub
+ one common O(D^(3/4)) midpoint disk
+ either strong-TB1 first-order margins
  or complete opposite-transverse exact-antipodal pairs.
```

---

## 7. What this removes and what remains

The previous positive-density fork still allowed a conceptual star escape: linearly many interface tags might have been absorbed by a bounded number of very high-degree diameter vertices. BM.10--BM.17 exclude that. Actual diameter degree is `o(D)`, so positive-density blockers force an unbounded vertex-disjoint geometric braid.

This does **not** close C-II. Regular-shell-type diameter geometry shows that many almost centrally antipodal crossing chords are possible in finite unit-separated sources. The new obligation is narrower and source-specific: combine the extracted tagged staircase with the common near-triangular train rectangle and either

1. the opposite-transverse pairing at every retained exact-antipodal tag, or
2. the fixed strong-TB1 opening margin at every retained one-bar tag,

in order to force a forbidden hull endpoint order, an exact unit triangle, or a source-preserving strict diameter decrease.

No individual KKT multiplier lower bound is used. No canonical promotion is claimed.

**Disposition:** proved that the linear high-`t` exact-antipodal/strong-TB1 fork necessarily contains a growing `Omega(D^(1/4))` vertex-disjoint tagged diameter staircase; in the exact-antipodal branch one can retain complete opposite-transverse two-edge bundles with pairwise disjoint endpoint sets. C-II and Level I remain open.
