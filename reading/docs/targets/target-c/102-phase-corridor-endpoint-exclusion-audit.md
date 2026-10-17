> Generated reading edition · [exact source](../../../../docs/targets/target-c/102-phase-corridor-endpoint-exclusion-audit.md) · source SHA-256 `b0df36244445c8454b6a1c69f414f6af0107438eee6b511680d972b281895aa9`.
> [Current theorem state](../../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 9 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

# Target C — phase/corridor endpoint exclusion audit

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Status:** canonical after independent hostile audit and theorem-state audit.42 promotion.

Canonical Section 101 raises the wrapping threshold to

```math
\mu_8=0.976040765267052\ldots
```

by combining the sharp Section-100 circle-support ceiling with the outer-contact
currency forced by the full support complement.  The scalar endpoint itself has a
very rigid equality model: one positive-length support arc, two isolated support
points, and three complementary gaps of lengths

```math
(\theta_8,\phi_8,\phi_8),
\qquad
\phi_8=2\pi-2\theta_8.
```

This module couples that equality model to the canonical Section-90 inverse-diameter
phase core.  The two linear train families supplied by Section 90 have projective
edge directions separated by `pi/3`.  At the Section-101 endpoint, however, almost all
physical train endpoints must occur on the three near-geodesic complement corridors,
and a corridor carrying linearly many endpoints of one inverse-phase family must have
its chord parallel to that family.  The three corridor chord directions have pairwise
projective separations

```math
\pi-\theta_8,
\qquad
{\theta_8\over2},
\qquad
{\theta_8\over2},
```

none of which equals `pi/3`.  This is impossible.

Hence the Section-101 scalar endpoint cannot be approached by a macroscopic
locally-rhombic Type-II wrapping carrier.  Compactness plus the canonical cap-family
capacity then gives a **strict, though not numerically optimized, improvement**:
there are absolute constants

```math
\boxed{\epsilon_*>0,\qquad c_*>0}
```

such that every sufficiently large Type-II survivor contains a locally
rhombus-saturated harmonic cell `P_*` with

```math
\boxed{
\operatorname{diam}(P_*)
\ge(\mu_8+\epsilon_*)D,
\qquad
\operatorname{area}(P_*)\ge c_*D^2.
}
```

No lower bound for `epsilon_*` is claimed here.  The point is qualitative endpoint
exclusion: the scalar `0.9760407652...` barrier is not sharp once the canonical train
phase structure is used.

---

# 102. The Section-101 wrapping endpoint is incompatible with the phase core

## 102.1 Hypothetical endpoint sequence

Assume for contradiction that there is a Type-II sequence with source diameters
`D->infinity` and macroscopic locally rhombus-saturated harmonic cells

```math
P_D=\operatorname{conv}(A_D)
```

such that

```math
\operatorname{area}(P_D)\ge cD^2
\tag{102.1}
```

for one fixed `c>0`,

```math
{A_{4,D}\over\operatorname{area}(P_D)}\to1,
\tag{102.2}
```

and

```math
{\operatorname{diam}(P_D)\over D}\to\mu_8.
\tag{102.3}
```

Assume the normalized attachment sets converge in Hausdorff distance to a wrapping
compact set `S` on the radius-`1/2` circle.  Put

```math
\theta:=\theta_8=2\arcsin\mu_8,
\qquad
\phi:=2\pi-2\theta,
\qquad
U:=3\theta-2\pi.
\tag{102.4}
```

After a further subsequence write

```math
{a_D\over D}\to\alpha,
\qquad a_D:=|A_D|.
\tag{102.5}
```

Proof-only Section 101 gives the chain

```math
2\alpha
\le |S|
\le U,
\tag{102.6}
```

and, if `g_j` are the connected complementary angular gaps of `S`,

```math
2\alpha
\ge\sum_j\sin(g_j/2)
\ge \sin(\theta/2)+2\sin\theta.
\tag{102.7}
```

The defining scalar equation for `theta_8` is

```math
\sin(\theta/2)+2\sin\theta=U.
\tag{102.8}
```

Therefore every inequality in (102.6)--(102.7) is equality:

```math
\boxed{
2\alpha=|S|=U,
\qquad
\sum_j\sin(g_j/2)=U.
}
\tag{102.9}
```

## 102.2 Equality fixes the support as one arc plus two points

Section 101 proves its complement-chord lower bound by majorization.  The function

```math
f(x)=\sin(x/2)
```

is strictly concave on `(0,pi)`.  Equality in (102.7), together with the three
Section-94 gaps of size at least `phi`, the upper bound `g_j<=theta`, and total
complement measure at least `theta+2phi`, therefore forces, after cyclic relabeling,

```math
\boxed{
(g_1,g_2,g_3)=(\theta,\phi,\phi)
}
\tag{102.10}
```

and no other complementary gap of positive length.  Also

```math
|S|=U.
```

A gap of length exactly `theta` has both endpoints in `S`.  Neither support component
adjacent to that gap can contain a nontrivial arc.  Indeed, moving any positive
angular amount from either endpoint into the adjacent support component produces two
points of `S` whose minor separation is strictly larger than `theta` (for a sufficiently
small move it remains below `pi`), contradicting the angular-diameter condition.
Thus the two support components adjacent to the `theta`-gap are singletons.

The remaining support component has no internal complementary gap and total angular
measure `U`; it is therefore one closed circular arc of length `U`.  Up to rotation,

```math
\boxed{
S=\{0\}\cup\{\theta\}\cup[\theta+\phi,\,2\pi-\phi].
}
\tag{102.11}
```

The last interval has length

```math
2\pi-\phi-(\theta+\phi)=U.
```

Let

```math
K:=\operatorname{conv}(S).
\tag{102.12}
```

Then `D^{-1}P_D -> K`, and the positive-length support component in (102.11) is a
strictly curved radius-`1/2` arc of `partial K`.  In particular no positive-length
subarc of that component is a line segment of `partial K`.

## 102.3 Endpoint saturation gives one dense tooth arc and three geodesic corridors

Use the canonical local notation `L_D,s_D,c_D,c_D^partial,Q_D`.  Section 82 gives

```math
L_D+Q_D=4a_D-6-2s_D-2c_D.
\tag{102.13}
```

Apply the Section-101 outer-route lower bound to the three positive complement gaps.
Their chord contribution tends to

```math
D\left(\sin(\theta/2)+2\sin\theta\right)=UD.
```

All other attachment intervals cost at least two outer-walk edges, except for
`c_D^partial` direct loaded-loaded sides.  Therefore

```math
L_D
\ge UD+2a_D-c_D^partial-o(D).
\tag{102.14}
```

Since `2a_D=UD+o(D)`, (102.13)--(102.14) force

```math
\boxed{
Q_D=o(D),
\qquad
s_D=o(D),
\qquad
c_D=o(D),
\qquad
L_D=2UD+o(D).
}
\tag{102.15}
```

The same nonnegative-slack argument gives the following endpoint stability facts.

1. The three complement-gap outer routes have lengths equal to their endpoint chords
   up to `o(D)`.  Thus their lengths are
   
   ```math
   \mu_8D+o(D),
   \qquad
   \sin\theta_8D+o(D),
   \qquad
   \sin\theta_8D+o(D).
   \tag{102.16}
   ```

2. Their path excesses above the corresponding chord lengths are individually
   `o(D)`.
3. Only `o(D)` ordinary attachment intervals have outer-route length other than two,
   after discarding the `o(D)` direct loaded-loaded sides.
4. Only `o(D)` of those two-edge routes have a loaded middle vertex, because each such
   route uses loaded-loaded contact edges and `c_D=o(D)`.

The equality `2alpha=|S|` also saturates unit-spacing capacity on the positive-length
support arc.  The two isolated support points have `o(D)` attachment vertices in every
shrinking angular neighborhood.  Hence, after discarding `o(D)` intervals, the
remaining ordinary intervals lie along the one support arc in (102.11), their polygon
side lengths have total excess `o(D)` over one per side, and their two-edge routes have
an unloaded middle vertex.

Exactly as in the corrected Section-97 argument, after a further `o(D)` discard there
are

```math
\boxed{(\alpha-o(1))D}
\tag{102.17}
```

near-equilateral unit-unit teeth

```math
p_k-x_k-p_{k+1},
\qquad
|p_k-x_k|=|x_k-p_{k+1}|=1,
\tag{102.18}
```

with

```math
1<|p_k-p_{k+1}|=1+o(1)
\tag{102.19}
```

uniformly over the retained family.  The apex `x_k` lies on the interior side of the
polygon side `[p_k,p_{k+1}]`, because harmonic trapping puts unloaded vertices in
`int(P_D)`.

All outer-edge occurrences not belonging to these retained teeth or to the three
macroscopic corridors have total count `o(D)`.

## 102.4 Nonquadrilateral rhombus boundary is sublinear

Let `mathcal R_D` be the full strict-rhombus complex of the carrier.  Every physical
boundary edge occurrence of `mathcal R_D` faces either

- the outer face of the induced harmonic contact graph, or
- one bounded nonquadrilateral face.

If `f_exc,D` is the number of bounded nonquadrilateral faces, canonical Section 82
has

```math
f_{exc,D}\le Q_D,
\qquad
\sum_{f\ nonquad}\deg f\le5Q_D=o(D).
\tag{102.20}
```

Hence only `o(D)` physical rhombus-boundary edge occurrences face nonquadrilateral
bounded faces.  Every remaining endpoint of a local train segment is an outer-face
edge occurrence lying either on a retained tooth or on one of the three macroscopic
corridors, up to `o(D)` exceptions.

## 102.5 A fixed inverse-phase family has only `o(D)` endpoints on the curved tooth arc

We need one geometric lemma.

### Lemma 102.1 — curved tooth phase dispersion

Let `mathcal E_D` be any family of physical rhombus-boundary edges chosen from the
retained teeth in (102.17)--(102.19).  Suppose their projective edge directions all
lie in an angular interval of width `o(1)`.  Then

```math
\boxed{|\mathcal E_D|=o(D).}
\tag{102.21}
```

### Proof

Assume instead that, along a subsequence,

```math
|\mathcal E_D|\ge\beta D
```

for some `beta>0`.  Each tooth contributes at most two selected legs.  Split by which
leg of the oriented boundary tooth is selected; one class contains at least
`beta D/2` occurrences.

For a retained near-equilateral tooth, the projective direction of either leg differs
from the projective direction of its polygon base `[p_k,p_{k+1}]` by

```math
\pi/3+o(1)
```

uniformly.  Thus at least `beta D/2` polygon bases have projective directions in one
interval of width `o(1)`. Their lengths are `1+o(1)` uniformly.

At this point we must choose the oriented lift. All retained bases lie on the single
positive support arc from (102.11), whose angular length is
`U_8=3theta_8-2pi<pi`. Along a convex polygon converging to that arc, the total
variation of the oriented boundary-side direction over the retained arc is
`U_8+o(1)<pi`. Therefore two retained bases that are `o(1)`-close in `RP^1` cannot use
opposite oriented lifts separated by `pi-o(1)`; after splitting by tooth leg, all the
selected bases lie in one oriented `o(1)` direction cone.

Along the convex polygon boundary the oriented side direction is monotone.  Therefore
all sides between the first and last of these selected bases also have direction in
that same `o(1)` interval.  The corresponding convex-boundary subchain has total
length at least `(beta/3)D` for large `D`, and because all of its edge directions lie
in an `o(1)` cone, its endpoint displacement has length at least `(beta/4)D`.

After scaling by `D` and passing to a subsequence, the two subchain endpoints converge
to two distinct points of the positive-length circular support arc in (102.11), while
the whole subchain converges to their straight segment.  Hausdorff convergence of the
convex polygons to `K` puts that positive-length segment in `partial K`.

But both endpoints lie on the same radius-`1/2` circular arc contained in `S`; the
intermediate circle arc is also contained in `partial K` and lies strictly outside its
chord.  Their chord therefore cannot be a boundary segment of `K`.  Contradiction.
`\square`

The lemma uses only strict curvature of the limiting support arc.  It does not assume
that the finite force hull is uniformly `C^1` or that individual finite boundary
edges are tangent to a circle.

## 102.6 The canonical dense phase core forces two linear endpoint families

The proof of canonical Section 90 is local once three estimates are available on one
harmonic carrier:

```math
R_D\ge rD^2,
\qquad
T_D\le C_TD,
\qquad
\sum_{R\subset P_D}\delta_R\le C_{phase}D.
\tag{102.22}
```

They hold uniformly here.  Indeed, (102.1)--(102.2) and `area(R)<=1` give
`R_D>=rD^2` for some `r=r(c)>0`; canonical Section 89 gives `T_D=O(D)`; and the last
bound is the global canonical phase-defect budget restricted to this cell.

Apply the Section-90 binning argument verbatim.  We obtain two fixed, distinct phase
labels and two families `mathcal A_D,mathcal B_D` of local train segments with

```math
\boxed{
|\mathcal A_D|\ge\kappa D,
\qquad
|\mathcal B_D|\ge\kappa D
}
\tag{102.23}
```

for one `kappa>0`, while all reduced phases of all selected trains lie in one interval
of width

```math
O(1/D).
\tag{102.24}
```

Thus there are limiting projective train directions `u_A,u_B` such that

```math
\operatorname{dist}_{RP^1}(\operatorname{dir}\tau,u_A)=O(1/D)
\quad(\tau\in\mathcal A_D),
\tag{102.25}
```

and similarly for `mathcal B_D`.  Distinct phase labels in one reduced-phase bin give

```math
\boxed{
\operatorname{dist}_{RP^1}(u_A,u_B)=\pi/3.
}
\tag{102.26}
```

Each local train segment has exactly two physical boundary ends.  A physical
rhombus-boundary edge is the end of only the train using that edge direction, so
(102.23) supplies at least `2kappa D` distinct endpoint occurrences for each family.

By (102.20), only `o(D)` of those endpoints can lie against bounded
nonquadrilateral faces.  By Lemma 102.1, only `o(D)` endpoints from either inverse-phase
family can lie on the retained curved tooth arc.  The remaining outer-face exceptions
from §102.3 also total `o(D)`.

Consequently, for each of the two families, linearly many train endpoints lie on the
three macroscopic complement corridors.  Pigeonholing the three corridors gives
indices `i_A,i_B in {1,2,3}` and a constant `kappa'>0` such that corridor `i_A`
contains at least `kappa'D` endpoints of `mathcal A_D`, while corridor `i_B` contains
at least `kappa'D` endpoints of `mathcal B_D`.

## 102.7 A near-geodesic corridor can host only its own limiting phase

Let one macroscopic corridor have endpoint chord unit direction `q_D` and route edge
vectors `z_1,...,z_m`, oriented from one corridor endpoint to the other.  Let

```math
d_D=\text{endpoint chord length},
\qquad
\ell_D=m.
```

Endpoint stability from §102.3 gives

```math
\ell_D-d_D=o(D).
\tag{102.27}
```

Write `q_D` for the oriented chord unit vector.  Projection along `q_D` gives the exact
identity

```math
\sum_{j=1}^m\bigl(1-q_D\cdot z_j\bigr)=\ell_D-d_D=o(D).
\tag{102.28}
```

Suppose the corridor contains at least `kappa'D` train-end edges from one selected
phase family with limiting projective direction `u`.  Their undirected edge directions
are `u+o(1)` in `RP^1`.

If the limiting projective corridor direction `q` differed from `u` by some
`delta>0`, then, for all sufficiently large `D`, every one of those `kappa'D`
occurrences would satisfy

```math
1-q_D\cdot z_j\ge c(delta)>0.
```

(Choosing the opposite orientation of an undirected phase edge only makes the
projection loss larger.)  Their contribution to (102.28) would be `Omega(D)`, a
contradiction.  Therefore

```math
\boxed{u=q\quad\text{in }RP^1.}
\tag{102.29}
```

In particular corridors `i_A` and `i_B` are distinct, because otherwise (102.29) would
make `u_A=u_B`, contradicting (102.26).  Moreover their limiting chord directions must
satisfy

```math
\boxed{
\operatorname{dist}_{RP^1}(q_{i_A},q_{i_B})=\pi/3.
}
\tag{102.30}
```

## 102.8 The three endpoint corridor directions never differ by `pi/3`

Use the explicit support normalization (102.11).  The three complementary gaps are

```math
(0,\theta),
\qquad
(\theta,\theta+\phi),
\qquad
(2\pi-\phi,2\pi).
\tag{102.31}
```

Their angular midpoints are

```math
m_1={\theta\over2},
\qquad
m_2=\theta+{\phi\over2},
\qquad
m_3=2\pi-{\phi\over2}.
\tag{102.32}
```

A circle chord spanning a gap centered at `m` has projective direction `m+pi/2`; thus
projective separations between corridor chord directions equal projective separations
between these midpoints.  Direct calculation using `phi=2pi-2theta` gives

```math
\boxed{
\left\{
\operatorname{dist}_{RP^1}(q_i,q_j):i<j
\right\}
=
\left\{
{\theta\over2},
{\theta\over2},
\pi-\theta
\right\}.
}
\tag{102.33}
```

Because

```math
\theta=\theta_8>{2\pi\over3},
```

we have

```math
{\theta\over2}>{\pi\over3},
\qquad
\pi-\theta<{\pi\over3}.
\tag{102.34}
```

Hence no pair of endpoint corridors has projective separation `pi/3`, contradicting
(102.30).

Numerically the smaller angular margin is

```math
{\theta_8\over2}-{\pi\over3}
=0.304256\ldots\text{ radians}
=17.43\ldots^\circ,
\tag{102.35}
```

so the contradiction is separated from equality by a fixed angle; it is not a
zero-margin coincidence.

We have proved:

> **Endpoint exclusion theorem.** No macroscopic locally rhombus-saturated wrapping
> Type-II harmonic-cell sequence can have normalized diameter tending to `mu_8`.

## 102.9 Compactness upgrades endpoint exclusion to a strict carrier gap

We finally transfer the endpoint exclusion back to the global Type-II selection.
Canonical Section 83/88 gives

```math
\sum_r\sqrt{\operatorname{area}(P_r)}=O(D).
\tag{102.36}
```

Let

```math
\Gamma_8:={\pi\over4}-\mathcal C(\mu_8)>0
\tag{102.37}
```

be the positive Section-88 cap-family area gap recorded in Section 101.  Choose a fixed
`eta>0` so small that cells of area below `eta D^2` carry at most
`Gamma_8D^2/4` total area for all sufficiently large `D`; this is possible by
(102.36).

Suppose no strict diameter improvement existed.  Then for every integer `n` there
would be arbitrarily large Type-II survivors in which every harmonic cell of area at
least `eta D^2` had

```math
\operatorname{diam}(P_r)<(\mu_8+1/n)D.
\tag{102.38}
```

Choose a diagonal sequence with `n->infinity`.  There are uniformly only finitely many
`eta`-macroscopic cells.  Pass to a subsequence on which all their normalized cells and
attachment supports converge.  Every limiting cell has diameter at most `mu_8`.

Global local-rhombic deficit is `o(D^2)`, so every `eta`-macroscopic cell in this
finite family is locally rhombus-saturated.  A wrapping limit of diameter below
`mu_8` contradicts Section 101.  A wrapping limit of diameter exactly `mu_8`
contradicts the endpoint exclusion theorem above.  Therefore every macroscopic limit
is cap type.

The Section-88 laminar cap-family theorem, now with support-arc lengths at most
`theta_8=2 asin(mu_8)`, bounds the total limiting area of these macroscopic cells by

```math
\mathcal C(\mu_8).
\tag{102.39}
```

Adding the small-cell contribution gives at most

```math
\mathcal C(\mu_8)+{\Gamma_8\over4}
<{\pi\over4},
```

contradicting the Type-II area identity

```math
\sum_r\operatorname{area}(P_r)
={\pi\over4}D^2-o(D^2).
```

Thus there is an absolute `epsilon_*>0` such that, for every sufficiently large Type-II
survivor, one harmonic cell satisfies

```math
\operatorname{diam}(P_*)\ge(\mu_8+\epsilon_*)D
\tag{102.40}
```

and has area at least `eta D^2`.  Its individual rhombic deficit is `o(D^2)`, so it is
locally rhombus-saturated.  Taking `c_*=eta` proves the claimed strict carrier gap.

## 102.10 Dependency and regression audit

- **Canonical Section 100 / `C-WRAP-ANGULAR-MEASURE`:** sharp wrapping support-measure
  ceiling and attachment-density transfer.  Section 100 is canonical from theorem
  state audit.40.
- **Canonical Section 101 / `C-WRAP-COMPLEMENT-CHORD`:** complement-chord density floor, fixed-support-measure strengthening, scalar endpoint `mu_8`, and endpoint complement profile.
- **Canonical Sections 62 and 82:** consecutive-attachment outer routes, exact local
  face ledger, and quadrilateral-face classification.
- **Canonical Sections 89 and 90:** linear local train count and the cell-local
  inverse-diameter two-phase crossing core.
- **Canonical Sections 83 and 88:** cell area additivity, small-cell control, cap-family
  capacity, and global propagation.
- **Sections 97--98:** not premises.  Their corrected endpoint arguments motivate the
  route-excess and bridge-safe bookkeeping, but §§102.3--102.8 rederive everything
  needed at the new endpoint.
- **Bridges:** never counted as rhombus train endpoints.  The proof uses only physical
  boundary edges of the strict-rhombus complex, so a bridge-rich corridor is allowed;
  it simply cannot supply train endpoints on its bridge occurrences.
- **Finite force-hull smoothness:** not assumed.  Lemma 102.1 uses convex side-order
  and the strictly curved Hausdorff limit, not a `C^1` estimate on finite hulls.
- **Contact-isolated source points:** untouched.
- **No Cauchy perimeter inequality, KKT coefficient floor, rejected Reuleaux-cap
  theorem, or external pseudosegment theorem is used.**

**Theorem state:** canonical from `2026-09-12.audit.42`. C-II remains open.
