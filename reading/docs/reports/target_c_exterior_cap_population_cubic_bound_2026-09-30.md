> Generated reading edition · [exact source](../../../docs/reports/target_c_exterior_cap_population_cubic_bound_2026-09-30.md) · source SHA-256 `0dde70fa8fe07714fffd5cafa7c6b831206501faf2379be3d92172797ffa5888`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-3F2D1FD883C7","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C: sharp cubic control of exterior cap population

**Date:** 2026-09-30<br>
**Base main:** `c00bb08090cf3a7a89fc195cbe3ab450983a5de0`<br>
**State version:** `2026-09-14.audit.51`<br>
**Classification:** proved candidate awaiting promotion; analytic regression.<br>
**Level I:** open. C-II remains open.

## 1. Full-source population theorem

Let $`A`$ be a finite unit-separated source of diameter $`D`$, and let
$`F`$ be its two-dimensional loaded hull. Assume every loaded hull side
has a common diameter partner. This includes the non-star $`d_H=0`$
branch by this run's exact V-cover candidate. Set
```math
B=\operatorname{per}F-|B_H|\ge0,
\qquad Z_{\rm ext}=|A\setminus F|.
```
Then the exact finite upper bound is
```math
\boxed{
Z_{\rm ext}\le
\frac{9+5\sqrt3}{12}\frac{B^3}{D}
+\frac{5+3\sqrt3}{4}B.
}
\tag{1.1}
```
In particular,
```math
B=o(D^{2/3})\quad\Longrightarrow\quad Z_{\rm ext}=o(D).
\tag{1.2}
```
The weaker $`B=o(D)`$ gives no such conclusion. An analytic family below
has $`d_H=0`$, a complete V-cover, a disk limit, and exactly one
unprotected side, but $`Z_{\rm ext}=\Theta(D^{5/4})`$.

## 2. Circular caps bound all exterior source points

For a covered side of length $`s`$, put its endpoints at
$`(\pm s/2,0)`$ and its partner at $`(0,H)`$, where
$`H=\sqrt{D^2-s^2/4}`$. Every source point below the side lies in the
convex cap $`C_s`$ of the radius-$`D`$ disk centered at that partner.
Writing $`u=s/(2D)\le1/2`$ and $`a=\arcsin u`$,
```math
\operatorname{area}C_s=D^2(a-\sin a\cos a),
\qquad \operatorname{per}C_s=s+2Da.
```
For $`0\le u\le1/2`$,
```math
\frac{d}{du}\bigl[\arcsin u-u\sqrt{1-u^2}\bigr]
=\frac{2u^2}{\sqrt{1-u^2}}\le\frac4{\sqrt3}u^2,
```
and $`\arcsin u\le2u/\sqrt3`$. Hence
```math
\operatorname{area}C_s\le\frac{s^3}{6\sqrt3D},
\qquad \operatorname{per}C_s\le(1+2/\sqrt3)s.
\tag{2.1}
```

Apply the Euclidean finite-packing inequality from canonical Section 68.1
to the exterior source points in this cap together with its two endpoint
guards. Their convex hull lies in $`C_s`$; convex perimeter and area
are monotone under containment. Thus the number $`z_s`$ of exterior
points beyond this side satisfies
```math
z_s\le\frac{2}{\sqrt3}\operatorname{area}C_s
       +\frac12\operatorname{per}C_s-1
\le\frac{s^3}{9D}+(1/2+1/\sqrt3)s-1.
\tag{2.2}
```
Endpoint guards are original source points and are included exactly once
in this application; the favorable $`-1`$ is not an assumed strict gap.

The protected-side theorem shows $`z_s=0`$ whenever
$`s^2\le4-D^{-2}`$. Every side possibly supporting an exterior point
therefore has $`s>\sqrt3`$. For those sides, writing
$`c=\sqrt3/(\sqrt3-1)=(3+\sqrt3)/2`$,
```math
\sum s\le c\sum(s-1)\le cB,
\qquad \sum s^3\le(\sum s)^3\le c^3B^3.
```
Every point outside the convex loaded hull violates at least one hull
support line. Sum (2.2) over the possible sides, allowing overcounting and
dropping the favorable $`-1`$'s. The coefficients are
$`c^3/9=(9+5\sqrt3)/12`$ and
$`c(1/2+1/\sqrt3)=(5+3\sqrt3)/4`$, proving (1.1).

If only some sides are covered, the same sum bounds points beyond covered
sides. Exterior points supported solely by uncovered sides remain a separate
population term; a small number of such sides does not control it.

## 3. Exact family realizing the cubic scale

Use the analytic regular-Reuleaux shell in
`target_c_contiguous_star_incidence_concentration_regression_2026-09-30.md`.
Let $`p\ge9`$ be odd, and take $`D=p^L`$ with fixed $`L\ge3`$.
Its $`p`$ radius-$`D`$ boundary arcs have angle $`\pi/p`$. On every
arc sample $`r`$ equal steps, with
```math
r=\lfloor\pi/(p\delta_D)\rfloor,
\qquad \delta_D=2\arcsin(1/(2D)).
```
Omit **all interior samples of one arc**, retaining its two endpoints and
every corner. The loaded graph remains an odd cycle with pendant leaves:
```math
q=(p-1)r+1=h,\qquad d_H=0.
```
Its hull has $`(p-1)r`$ near-unit sides and one long covered side of
length $`s_p=2D\sin(\pi/(2p))`$. Thus
```math
B=\Theta(D/p),\qquad q/D\to\pi,
\qquad D^{-1}F\to B(0,1/2).
\tag{3.1}
```
The small sides tend to one, so they are protected for large $`p`$.
The long side is the single unprotected side.

### Place genuinely contact-isolated points in the omitted cap

Use coordinates in which that long side is horizontal and the loaded hull
is above it. For $`|a|\le s_p/4`$, the outward depth of the circular
cap is at least
```math
\sqrt{D^2-s_p^2/16}-\sqrt{D^2-s_p^2/4}
\ge g:=\frac{3s_p^2}{32D}.
```
The rectangle
```math
|a|\le s_p/4,\qquad 2\le b\le g-2,
\qquad z=(a,-b),
```
lies strictly inside the Reuleaux body and outside $`F`$. Put a
spacing-two rectangular grid in it. This gives
```math
\Theta(s_pg)=\Theta(D^2/p^3)=\Theta(B^3/D)
\tag{3.2}
```
new source points. They have distance at least two from the old source,
which lies above the side, and mutual distance at least two. They are
therefore contact-isolated.

The Reuleaux body has diameter $`D`$, so source separation and diameter
remain valid. A diameter pair involving one of its interior points would
uniquely expose that point on the **entire Reuleaux body** in the chord
direction, a contradiction. Consequently
the full diameter graph, loaded hull, and complete V-cover are unchanged.

For $`L=3`$, (3.1)--(3.2) give
$`B=\Theta(D^{2/3})`$, $`Z_{\rm ext}=\Theta(D)`$.
For $`L=4`$, they give
```math
\boxed{B=\Theta(D^{3/4})=o(D),\qquad
Z_{\rm ext}=\Theta(D^{5/4}),}
```
behind just one exceptional side. The old unit contacts, if any, join only
consecutive arc samples; the other pairwise distances exceed one. The new
points have no unit contacts. Thus the source is also triangle-free.
This proves that the cubic population
currency and the rate in (1.2) cannot be discarded under the shell hypotheses.
The source has no certified quadratic harmonic core or global optimality.

## 4. Certificates, scope, and exact next obligation

`research/verify_exterior_cap_population.py` checks the coefficient identities,
gives rational lower bounds for the rectangle dimensions, and counts certified
spacing-two sites for bounded
choices of $`p,L`$. It uses rational Machin bounds and a sine remainder
bound; it never enumerates or claims to optimize the complete source. The
universal containment, separation, diameter, and scaling arguments are analytic.

The new upper bound uses the canonical Euclidean packing theorem, the
candidate protected-side theorem, and actual source endpoint guards.
The regression uses the earlier analytic shell candidate. Equality-case
loading, exterior isolate multiplicity, cap area, and the threshold
$`D^{2/3}`$ are retained explicitly.

For the complete-V branch, the exterior contribution to a source refill
argument can now be controlled by $`B+B^3/D`$. The rooted ledger gives
only $`B=O(\Delta D)+o(D)`$, so it does not furnish the rate (1.2).
Nor does an exterior-population bound supply interior vacant sites.
The missing theorem still must turn the actual source defects into a
simultaneous replacement, retaining the full population.
