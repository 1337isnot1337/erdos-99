> Generated reading edition · [exact source](../../research/target_c_open_cell_host_cap_harmonic_localization_2026-10-04.md) · source SHA-256 `307e8acdf0ca444ac1c000c90df2920d1b2b2f658cc7e979c97962716eb15a4f`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target C: strong open-cell host cap contains a macroscopic harmonic grain

Date: 2026-10-04
Base main: 014932e601c89d66424d4e53f3c9d4afcb351248
Status: proof-only Target C-II candidate; theorem-state authority unchanged.
LEVEL I STATUS: STILL OPEN. C-II REMAINS OPEN.

This note continues only the strong nonconstant open-witness-cell Target C route.

Current main proves that the strong-SCC staircase forces one complete-grid host to
contain linearly many distinct actual diameter endpoints. If $Q_*$ is that endpoint
set and $C_*=\operatorname{conv}Q_*$, then for some fixed $\alpha_*>0$,

$$
\operatorname{area}(C_*)\ge(\alpha_*-o(1))D^2.
\tag{1}
$$

The open point was that $C_*$ was not identified with any canonical contact or
harmonic object. The theorem below supplies that connection in the Type-II branch.

No computation, verifier, numerical experiment, or CI result is used.

## 1. Loaded vertices avoid the cap interior

Canonical full diameter visibility gives positive KKT weight to every actual diameter
edge. Every actual diameter endpoint is an extreme source-hull vertex, hence every
point of $Q_*$ is a loaded extreme vertex of the force hull $F$. In the canonical
Section-78 notation,

$$
Q_*\subseteq B\subseteq F,\qquad C_*\subseteq F.
\tag{2}
$$

Moreover

$$
\boxed{B\cap\operatorname{int}C_*=\varnothing.}
\tag{3}
$$

Indeed each $b\in B$ is a vertex of the convex polygon $F$. A point of
$B\setminus Q_*$ in the interior of $\operatorname{conv}Q_*$ would be a nontrivial
convex combination of other points of $F$, contradicting its extremality. Points of
$Q_*$ lie on $\partial C_*$.

## 2. Type II puts quadratic coherent-rhombus area in the cap

Compose with the canonical Section-80 dichotomy. Type I already supplies an actual
macroscopic inactive chamber or exterior cap, so assume Type II.

For every fixed $0<\epsilon<\pi/6$, canonical Sections 69 and 80 give
$\epsilon$-coherent strict-rhombus grains with union $U_\epsilon$ such that

$$
\operatorname{area}(F\setminus U_\epsilon)=o(D^2),
\qquad
P(U_\epsilon)=O_\epsilon(D),
\tag{4}
$$

where $P(U_\epsilon)$ is the sum of physical grain perimeters. Since
$C_*\subseteq F$, (1) and (4) give

$$
\operatorname{area}(C_*\cap U_\epsilon)
\ge(\alpha_*-o(1))D^2.
\tag{5}
$$

It remains to discard the boundary-crossing rhombi.

Every strict unit rhombus has diameter less than $2$, area at least

$$
a_0={\sqrt3\over2},
\tag{6}
$$

and distinct rhombus interiors are disjoint. A retained rhombus meeting
$\partial C_*$ lies in the closed two-neighborhood of that boundary.

For a planar convex body $C$ of perimeter $P$, that two-neighborhood has area at
most

$$
4P+4\pi.
\tag{7}
$$

The outer width-two strip has area $2P+4\pi$ by Steiner's formula; the inner
width-two strip has area at most $2P$ by inner-parallel coarea and perimeter
monotonicity. Also $\operatorname{per}(C_*)\le\pi D$. Therefore, if
$\mathcal R_\partial$ is the set of retained rhombi meeting $\partial C_*$,

$$
\boxed{
|\mathcal R_\partial|
\le {4\pi(D+1)\over a_0}
=O(D).
}
\tag{8}
$$

Each unit rhombus has area at most one. After omitting $\mathcal R_\partial$, the
retained rhombi wholly inside $\operatorname{int}C_*$ still have total area
$(\alpha_*-o(1))D^2$, hence their number satisfies

$$
\boxed{R_{\rm in}=\Omega(D^2).}
\tag{9}
$$

## 3. One inside component is quadratic

Split the retained grains, after omitting the boundary-crossing rhombi, into
edge-connected rhombic components. Omitting one rhombus can expose at most four new
unit boundary edges, so the sum of component perimeters is

$$
P_{\rm comp}
\le P(U_\epsilon)+4|\mathcal R_\partial|
=O_\epsilon(D).
\tag{10}
$$

Restrict to the components contained in $\operatorname{int}C_*$, with rhombus
counts $R_j$ and physical perimeters $P_j$. Then

$$
\sum_jR_j=\Omega(D^2),\qquad \sum_jP_j=O_\epsilon(D).
\tag{11}
$$

Every component has area at least $a_0R_j$, so isoperimetry gives

$$
P_j\ge2\sqrt{\pi a_0R_j}.
\tag{12}
$$

Thus $\sum_j\sqrt{R_j}=O_\epsilon(D)$. If
$R_{\max}=\max_jR_j$, then

$$
\sum_jR_j\le\sqrt{R_{\max}}\sum_j\sqrt{R_j},
$$

and consequently

$$
\boxed{R_{\max}=\Omega_\epsilon(D^2).}
\tag{13}
$$

Choose a maximizing component $G_{\cap}$. It inherits the phase coherence of its
parent grain and satisfies

$$
\boxed{
G_{\cap}\subset\operatorname{int}C_*,
\quad
R(G_{\cap})=\Omega_\epsilon(D^2),
\quad
P(G_{\cap})=O_\epsilon(D).
}
\tag{14}
$$

## 4. The component is trapped in one actual harmonic cell

By (3), $G_{\cap}$ contains no loaded vertex. Its vertices are positive-contact-core
vertices, and its unit edges connect them, so all its vertices belong to one component
$I_{\cap}$ of the unloaded graph $C[V\setminus B]$.

Let $A_{\cap}\subset B$ be that component's canonical attachment set and put

$$
P_{\cap}:=\operatorname{conv}A_{\cap}.
$$

Canonical harmonic trapping gives $I_{\cap}\subseteq P_{\cap}$. Convexity then
contains every rhombus of $G_{\cap}$, so

$$
\boxed{
G_{\cap}\subset\operatorname{int}C_*\cap P_{\cap}.
}
\tag{15}
$$

Furthermore,

$$
\operatorname{area}(P_{\cap})
\ge a_0R(G_{\cap})
=\Omega_\epsilon(D^2),
$$

and the isodiametric inequality yields

$$
\boxed{\operatorname{diam}(P_{\cap})=\Omega_\epsilon(D).}
\tag{16}
$$

Thus, in Type II, the macroscopic one-host cap forced by the strong open-cell
staircase necessarily contains a quadratic coherent positive-contact grain trapped in
one actual macroscopic harmonic attachment cell.

## 5. Cap-local grid corollary

The canonical Section-78.3 extraction applies to $G_{\cap}$: its train count obeys
$2T_{\cap}=P(G_{\cap})=O_\epsilon(D)$, while its rhombus count is
$\Omega_\epsilon(D^2)$. Hence it contains two all-crossing coherent train families
$\mathcal A_{\cap},\mathcal B_{\cap}$ with

$$
\boxed{
|\mathcal A_{\cap}|,|\mathcal B_{\cap}|=\Omega_\epsilon(D).
}
\tag{17}
$$

All product-grid rhombi lie in $G_{\cap}\subset C_*\cap P_{\cap}$. Therefore the
Section-76 endpoint projection localizes to either containing convex set. If
$S_{\cap}$ is the acute-angle defect sum,

$$
\operatorname{diam}(C_*)
\ge
{\sqrt3\over2}
\bigl(|\mathcal A_{\cap}|+|\mathcal B_{\cap}|\bigr)
-
{S_{\cap}\over\min(|\mathcal A_{\cap}|,|\mathcal B_{\cap}|)}
-2,
\tag{18}
$$

and the same inequality holds with $\operatorname{diam}(P_{\cap})$ on the left.
The canonical angular-defect bound gives $S_{\cap}=O(D)$, so (17) makes the error
term $O_\epsilon(1)$.

## 6. Frontier effect

Every unbounded strong open-cell survivor subsequence therefore has the following
Target C fork.

1. Type I: an actual inactive chamber or exterior cap already has quadratic area and
   quadratic contact-isolated population.

2. Type II: the staircase-forced host cap $C_*$ contains a quadratic coherent
   strict-rhombus grain $G_{\cap}$ in one macroscopic harmonic attachment cell, and
   a secondary $\Omega(D)$-by-$\Omega(D)$ complete train grid lies inside the same
   $C_*\cap P_{\cap}$.

This does not close C-II. It removes the previous strong-branch gap of connecting the
one-host cap to canonical contact/harmonic structure. The remaining Type-II task is
to use the co-location of the original staircase diameter endpoints, the quadratic
grain, the harmonic cell, and the secondary complete grid to force a source-preserving
strict diameter move or a contradiction in the local train/diameter currency.

The separate non-strong branch remains the inverse-$D$ inactive near-unit or
near-diameter witness.

Disposition: proof-only Target C candidate. C-II and Level I remain open.
