# Target C-II — high-t pentagon sea forces residual or a linear hidden near-contact matching

**Date:** 2026-09-15
**Status:** proof-only source-level structural strengthening
**Scope:** canonical full-core Type-II branch at any fixed endpoint `t=(q-k)/D <= T < 2.0215`
**Dependencies:** uniform `g=0.007707` pentagon-sea theorem; degree-`>=7` isolate-host theorem; exact inactive-chamber residual conservation; Wegner/Groemer low-degree face stability; canonical contact-degree bound `deg_C<=5`
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The modern all-train ledger forces a linear population of source-empty pentagonal contact faces far beyond the O--O path endpoint. The older Wegner theorem says that an individual pentagon can have vanishing Oler slack only by developing a hidden nonboundary distance tending to one. The exact chamber residual conservation law lets those two statements be combined globally without double-counting face slack.

Let `R_F` be the punctured force-hull residual from the exact chamber conservation theorem. For a bounded pentagonal contact face `P`, let

\[
 h(P):=\min\{|x-y|-1: x,y\in V(P),\ xy\notin E(\partial P)\}.
\]

Every such pair is a nonedge of the contact graph, hence has strictly positive gap in the canonical face representation.

For every fixed endpoint `T<2.0215`, write

\[
 p_5(T):=C_{707}+\pi-\frac52T,
 \qquad
 C_{707}=2\sqrt{\frac{\pi}{2\sqrt3}}+0.007707.
\]

Then the following fork holds along every unbounded survivor sequence with `t<=T`:

1. either `limsup R_F/D>0`; or
2. `R_F=o(D)`, and there is an endpoint-disjoint matching `M_D` of source nonedges such that
   \[
   |M_D|\ge \left(\frac{p_5(T)}{21}-o(1)\right)D,
   \qquad
   \max_{xy\in M_D}(|x-y|-1)\longrightarrow0.
   \]

Thus a sublinear-residual high-`t` survivor cannot merely contain linearly many abstract pentagonal defects. It contains linearly many vertex-disjoint actual source pairs poised at first contact.

## 1. A source-empty pentagon residual is exactly normalized Oler slack

The isolate-host theorem says that every bounded pentagonal contact face contains no assigned contact-isolated source point. For such an internal chamber,

- the assigned inactive count is `z_P=0`;
- the fixed graph-boundary count is `k_P=5`;
- the boundary perimeter is `P_P=5`;
- the chamber area is the Euclidean pentagon area `A_P`.

The exact residual-conservation theorem defines

\[
 r_P=\frac{A_P}{a_0}+\frac{P_P}{2}+1-z_P-k_P,
 \qquad a_0=\frac{\sqrt3}{2}.
\]

Therefore

\[
 \boxed{
 r_P
 =\frac{A_P}{a_0}-\frac32
 =\frac{A_P-3\sqrt3/4}{a_0}.
 }
 \tag{RN.1}
\]

The scaled Wegner inequality gives `A_P>=3sqrt(3)/4`, so `r_P>=0`, and equality is exactly the zero-Oler-slack situation.

Residual conservation is occurrence-safe and gives

\[
 \boxed{
 \sum_{P\in\mathcal P_5} r_P\le \sum_{j\in ch}r_j=R_F.
 }
 \tag{RN.2}
\]

No chamber residual is counted twice.

## 2. Quantitative Wegner stability converts residual into hidden-distance margin

Fix `eta>0`. The low-degree Wegner stability theorem supplies a constant

\[
 \sigma_5(\eta)>0
\]

such that every convex equilateral unit-separated pentagon whose nonconsecutive distances are all at least `1+eta` has

\[
 A_P\ge\frac{3\sqrt3}{4}+\sigma_5(\eta).
\]

Put

\[
 c_5(\eta):=\frac{\sigma_5(\eta)}{a_0}>0.
\]

By (RN.1), every pentagon with `h(P)>=eta` has `r_P>=c_5(eta)`. Hence (RN.2) gives the finite bound

\[
 \boxed{
 \#\{P\in\mathcal P_5:h(P)\ge\eta\}
 \le \frac{R_F}{c_5(\eta)}.
 }
 \tag{RN.3}
\]

This is the exact global payment missing from the old face-by-face compactness argument.

## 3. Insert the modern high-t pentagon floor

The uniform all-train theorem gives, for fixed `t<=T`,

\[
 |\mathcal P_5|\ge(p_5(T)-o(1))D.
 \tag{RN.4}
\]

Suppose now that `R_F=o(D)`. For every fixed `eta>0`, (RN.3) and (RN.4) imply

\[
 \#\{P:h(P)<\eta\}\ge(p_5(T)-o(1))D.
 \tag{RN.5}
\]

A standard diagonal choice of `eta_D\downarrow0` yields a family `\mathcal G_D` of pentagons satisfying

\[
 |\mathcal G_D|\ge(p_5(T)-o(1))D,
 \qquad
 \max_{P\in\mathcal G_D}h(P)\to0.
 \tag{RN.6}
\]

For each `P in G_D`, choose one nonconsecutive pair `e_P` attaining `h(P)`. Then

\[
 1<|e_P|=1+o(1)
\]

uniformly over the chosen family.

## 4. Extract a vertex-disjoint matching with only a factor 21 loss

Canonical C-II contact degrees satisfy `deg_C(v)<=5`. A vertex of the plane contact graph can therefore lie on at most five distinct bounded face boundaries. In particular, a fixed vertex belongs to at most five pentagons.

One pentagon has five vertices. For each of those vertices there are at most four *other* pentagons containing it. Thus a pentagon conflicts, by vertex intersection, with at most

\[
 5\cdot4=20
\]

other pentagons.

The intersection graph of `G_D` consequently has maximum degree at most 20. A greedy independent-set extraction gives a vertex-disjoint subfamily `G_D'` with

\[
 |\mathcal G_D'|\ge\frac{|\mathcal G_D|}{21}.
 \tag{RN.7}
\]

The selected hidden pairs `e_P`, `P in G_D'`, have pairwise disjoint endpoint sets. Therefore they form a matching `M_D` in the complete source graph, and (RN.6)--(RN.7) give

\[
 \boxed{
 |M_D|\ge\left(\frac{p_5(T)}{21}-o(1)\right)D,
 \qquad
 \max_{e\in M_D}(|e|-1)\to0.
 }
 \tag{RN.8}
\]

Every member of `M_D` is an inactive unit-separation constraint approaching activation from above.

## 5. Representative densities

Using the certified modern pentagon floors already on `main`, the sublinear-residual branch forces endpoint-disjoint hidden near-contact matchings with safe asymptotic density at least

\[
\begin{array}{c|c}
T & |M_D|/D\\ \hline
1.88 & 0.0168\\
1.90 & 0.0144\\
1.92 & 0.0120\\
1.96 & 0.0073\\
2.00 & 0.0025\\
2.01 & 0.0013\\
2.02 & 0.00018
\end{array}
\]

(the displayed rows are deliberately rounded down).

## 6. What this changes and what remains

The modern high-`t` branch now has a source-level fork in a currency that the repacking program already identified as load-bearing:

```text
linear R_F
    -> the only scalar currently available to pay globally pooled fixed-boundary repacking;

or R_F=o(D)
    -> linear endpoint-disjoint hidden nonedge matching
       with lengths 1+o(1).
```

The second branch is materially narrower than a generic pentagon sea. Its next obligation is an activation theorem for a matching of almost-active unit constraints in the lexicographically normalized diameter minimizer, preferably using the additional rhombic bracing available in Branch R/full-flower subfamilies.

No claim is made that `1+o(1)` equals one at finite `D`, that the hidden pairs can all be activated simultaneously, or that `R_F` itself is realized as packing capacity.

**Disposition:** proved proof-only residual/near-contact matching fork through every fixed `T<2.0215`. C-II and Level I remain open.
