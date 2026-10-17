> Generated reading edition · [exact source](../../../../docs/targets/target-c/quantitative-phase-gap-technical-audit-2026-09-12.md) · source SHA-256 `f61e9e102ee38b8d5fa2cdc754bd6b1d387724a4dbc0d2ab9bb14802eea24550`.
> [Current theorem state](../../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

# Target C — Section 104 technical audit: micro bases and direction windows

**Date:** 2026-09-12  
**Scope:** proof-only support for Section 104.  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This note supplies the two finite geometric estimates in Section 104 that are easiest
to overstate if one argues only from Hausdorff pictures:

1. the micro-base excess bound
   
   ```math
   \limsup {1\over D}\sum_{\rm micro\ bases}(|p_k-p_{k+1}|-1)
   \le {|S|\over2}-\alpha;
   ```

2. the tangent-window length bound used to count good-base tooth legs.

No smoothness of the finite force hull or attachment polygon is assumed.

## A. Fixed open covers give the base-excess estimate

Let `A_D` be the attachment set of the wrapping carrier and assume, after scaling,
its polar-angle sets converge in Hausdorff distance to the compact support `S`. Let
`a_D/D -> alpha`.

Fix `epsilon>0`. By outer regularity and compactness choose a finite disjoint union of
open angular intervals

```math
U=I_1\cup\cdots\cup I_m,
\qquad
S\subset U,
\qquad
|U|\le |S|+\epsilon.
\tag{A.1}
```

For all sufficiently large `D`, every attachment angle lies in `U`. On each interval
`I_j`, list the carrier attachments in force-hull cyclic order. The force-hull boundary
arcs between successive listed attachments are pairwise disjoint and remain over
`I_j`. Each attachment-polygon side is a chord of the corresponding force-hull
boundary arc, so

```math
\sum_{\substack{\text{successive attachments}\\\text{inside one component of }U}}
|p_k-p_{k+1}|
\le
\operatorname{len}(\partial F_D\text{ over }U).
\tag{A.2}
```

Canonical Type-II annular geometry gives

```math
\operatorname{len}(\partial F_D\text{ over }U)
\le
\left({D\over2}+o(D)\right)|U|.
\tag{A.3}
```

At most `m` cyclic attachment-polygon sides cross between components of `U`. Thus the
number of sides counted in (A.2) is `a_D-O_U(1)=alpha D+o(D)`. Every such side joins
distinct source points and has length at least one. Subtracting one per counted side,
dividing by `D`, and using (A.1) gives

```math
\limsup {1\over D}
\sum_{\text{within-}U\text{ bases}}
(|p_k-p_{k+1}|-1)
\le {|S|+\epsilon\over2}-\alpha.
\tag{A.4}
```

Let `epsilon` decrease to zero through nested finite covers and take a diagonal
subsequence. The omitted inter-component sides are the finitely resolved macroscopic
complement gaps at that scale. Exhausting the complement components leaves the micro
bases. Monotone nonnegativity gives

```math
\boxed{
\limsup {1\over D}
\sum_{\rm micro\ bases}(|p_k-p_{k+1}|-1)
\le {|S|\over2}-\alpha.
}
\tag{A.5}
```

In the Section-104 slack regime, `|S|-2alpha<=sigma`, so the right side is at most
`sigma/2`.

## B. The macro/micro split is an ordered finite limit

Fix `epsilon>0`. There are only finitely many complement components of `S` with
angular length at least `epsilon`. Hausdorff convergence pins both endpoints of each
such gap, so for large `D` they determine distinct finite consecutive-attachment
intervals. Call these the `epsilon`-macro intervals; call every other finite attachment
interval `epsilon`-micro.

All Section-101 outer-ledger inequalities are finite before passing to the limit.
Apply them with the `epsilon`-macro family selected. After `D->infinity`, let
`epsilon->0`. The omitted positive complement gaps have total chord sum controlled by

```math
C_{tail}=\sum_{j\ge4}\sin(g_j/2),
```

and total angular mass controlled by the tail mass `tau`. Thus every use of “macro”
and “micro” in Section 104 means

```text
fix epsilon > 0 -> D -> infinity -> epsilon -> 0.
```

No classification of a growing family of finite gaps is assumed.

## C. Convex tangent-window length bound

Let `K=conv(S)` be the normalized carrier limit. Remove the three principal complement
gaps and the two tiny support spans adjacent to the largest principal gap. The
remaining main region has angular extent strictly below `pi`; oriented tangent
direction therefore has one lift there.

The boundary of `K` in the main region consists of radius-`1/2` circular support arcs
and straight chords spanning tail complement gaps. Let `I` be an oriented
tangent-direction interval of width `w<pi`.

On a radius-`1/2` circle arc, tangent angle and polar angle advance at the same rate,
so the total circular boundary length whose tangent direction lies in `I` is at most
`w/2`. A tail gap of angular length `g` contributes a chord of length `sin(g/2)`.
Even if every tail chord lies in `I`, their total length is at most `C_tail`. Hence

```math
\boxed{
\operatorname{len}(\partial K\text{ in the main region and direction window }I)
\le {w\over2}+C_{tail}.
}
\tag{C.1}
```

Transfer this to finite attachment polygons without a smoothness assumption. Along a
convex polygon boundary, oriented side direction is monotone. Thus sides whose
directions lie in a fixed interval `I` form one contiguous boundary subchain, except
for endpoint ties. Enlarge `I` to `I_eta` by `eta` at both ends. Hausdorff convergence
of the normalized convex polygons to `K`, together with planar convex perimeter
continuity applied after cutting by support lines at the endpoint directions of
`I_eta`, gives

```math
\limsup_{D\to\infty}{1\over D}
\operatorname{len}(\text{finite sides in }I)
\le
\operatorname{len}(\partial K\text{ in }I_eta).
\tag{C.2}
```

Let `eta->0` and use (C.1):

```math
\boxed{
\limsup_{D\to\infty}{1\over D}
\operatorname{len}(\text{main-region bases with direction in }I)
\le {w\over2}+C_{tail}.
}
\tag{C.3}
```

Every attachment-polygon base has length at least one, so the same right side bounds
the normalized number of bases in the window.

## D. Application to good-base teeth

Fix a base cutoff `h>0`. A regular unit-unit tooth with base `1<=b<=1+h` has either
leg at projective angle

```math
\beta(b)=\arccos(b/2)
```

from its base. Thus

```math
\arccos((1+h)/2)\le\beta(b)\le\pi/3.
```

For one inverse-phase family whose train-end directions lie in an `o(1)` projective
window, split selected tooth legs into the two possible leg choices. Because the main
support region has oriented tangent variation below `pi`, each class lifts to one
oriented base-direction window of asymptotic width at most

```math
w_h:=\pi/3-\arccos((1+h)/2).
\tag{D.1}
```

Apply (C.3) to each class. Each contributes base-count density at most
`w_h/2+C_tail`. Therefore the total number of good-base tooth endpoints from one
inverse-phase family has density at most

```math
\boxed{w_h+2C_{tail}.}
\tag{D.2}
```

This is Section 104 equation (104.59). The two-class bound already allows both leg
choices, so a single tooth creates no hidden multiplicity.

## E. Projective lift

The same `main region < pi` observation removes the orientation issue found during the
Section-102 audit. Over this region, finite oriented attachment-polygon side directions
vary in an interval of length `<pi+o(1)`. Hence an `o(1)` projective direction window
has one oriented lift; occurrences separated by `pi-o(1)` cannot both lie in the main
region.

## F. Disposition

The micro-base excess estimate and good-tooth tangent-window estimate used in Section
104 are valid with the ordered finite-cover limits above. They do not assume finite
boundary differentiability, uniform curvature, or that individual attachment-polygon
sides are tangent to the limiting circle.

**Status:** proof-only technical audit; theorem state unchanged.
