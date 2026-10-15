# Target C — Section 120: anisotropic two-arc signed return

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Status:** proof-only structural candidate pending independent hostile audit.

Section 116 proves an exact two-arc signed-return inequality by cutting the occurrence-counted outer walk at a diameter pair and replacing every strict rhombus by the worst possible `60 degree` local return constant. That last replacement loses essentially all directional information in the rhombic core.

This section keeps that information.

Let one harmonic carrier have

- convex attachment-cell diameter `d`;
- occurrence-counted outer-face walk length `L`;
- bounded-nonquadrilateral total perimeter `P_exc`;
- strict unit-rhombus set `R_4` and total strict-rhombus area `A_4`.

For each strict rhombus `R`, let `u_R,v_R` be unit representatives of its two projective train directions. Choose **any two distinct attachment vertices** `p_-,p_+` occurring on the outer-face walk, put

\[
r:=|p_+-p_-|>0,
\qquad
q:={p_+-p_-\over r}.
\]

Then

\[
\boxed{
 d\bigl(L+P_{\rm exc}-2r\bigr)
 \ge
 \sum_{R\in\mathcal R_4}
 \operatorname{area}(R)
 \Bigl[
 4-2\bigl(|q\cdot u_R|+|q\cdot v_R|\bigr)
 \Bigr].
}
\tag{120.1}
\]

Equivalently, if

\[
M(q):=
\sum_{R\in\mathcal R_4}
\operatorname{area}(R)
\bigl(|q\cdot u_R|+|q\cdot v_R|\bigr),
\]

then

\[
\boxed{
 d\bigl(L+P_{\rm exc}-2r\bigr)
 \ge 4A_4-2M(q).
}
\tag{120.2}
\]

The Section-116 universal two-arc theorem is the immediate pointwise corollary

\[
 d(L+P_{\rm exc}-2r)
 \ge (4-2\sqrt3)A_4,
\tag{120.3}
\]

because a strict unit rhombus has projective train angle `phi_R>pi/3` and

\[
|q\cdot u_R|+|q\cdot v_R|
\le2\cos(\phi_R/2)<\sqrt3.
\]

For a diameter pair `r=d`, (120.3) is exactly the Section-116 companion inequality.

The gain in (120.1) is structural rather than another carrier-decimal optimization. It turns the remaining outer-detour problem into an explicit competition between

1. available long attachment chords, and
2. the area-weighted angular distribution of complete train directions.

No phase extraction, near-endpoint assumption, or asymptotic limit is used.

---

## 120.1 Two arbitrary outer cuts give hosts `{q,-q,0}`

Use the same physical boundary orientation convention as the hostile-audited Section-117 signed-return theorem: every physical strict-rhombus boundary edge is oriented with its incident retained rhombus on the left.

Cut the occurrence-counted outer-face walk at the two chosen attachment vertices `p_-` and `p_+`. Orient the outer walk with its bounded side on the left. The two resulting directed arcs have displacements

\[
z=p_+-p_-=rq,
\qquad
-z,
\]

and therefore unit chord hosts `q` and `-q`.

For every bounded nonquadrilateral face, orient its complete boundary cycle clockwise. Whenever one of its edge occurrences is a physical strict-rhombus boundary edge, the incident rhombus lies on the left, exactly as in Section 116. The cycle has displacement zero and therefore receives the common host `0`.

Every physical terminal edge of every complete train is thus assigned injectively to either

- one occurrence on one of the two outer arcs, or
- one occurrence on one bounded defect-face cycle.

All complete train ends are good.

The total exact route excess of the designated walks is

\[
\boxed{
E=L+P_{\rm exc}-2r.
}
\tag{120.4}
\]

Indeed the two outer arcs have total length `L` and total displacement norm `2r`, while every bounded defect-face cycle has zero displacement and contributes its full length to `P_exc`.

## 120.2 Exact train return cost for the chosen chord direction

For the host set

\[
Q=\{q,-q,0\},
\]

the support width in a unit train direction `u` is

\[
\begin{aligned}
w_Q(u)
&=\max\{q\cdot u,-q\cdot u,0\}
  -\min\{q\cdot u,-q\cdot u,0\}\\
&=2|q\cdot u|.
\end{aligned}
\tag{120.5}
\]

Hence the exact signed-return cost assigned to a complete train `tau` with projective direction `u_tau` is

\[
\boxed{
\delta_\tau(q)
:=2-w_Q(u_\tau)
=2-2|q\cdot u_\tau|.
}
\tag{120.6}
\]

Because every train has two good ends, the finite signed-return projection identity gives

\[
\boxed{
E\ge\sum_\tau\delta_\tau(q).
}
\tag{120.7}
\]

There is no orientation ambiguity in (120.6): replacing `u_tau` by `-u_tau` leaves the absolute scalar product unchanged.

## 120.3 Reweight the return cost by the exact train transverse span

Let `R` be a strict unit rhombus. Its two crossing complete trains have projective directions `u_R,v_R`. Therefore

\[
\delta_{u_R}(q)+\delta_{v_R}(q)
=
4-2\bigl(|q\cdot u_R|+|q\cdot v_R|\bigr).
\tag{120.8}
\]

Multiply (120.8) by `area(R)` and sum over all strict rhombi. Reorganizing by complete trains gives the exact identity

\[
\begin{aligned}
&\sum_R \operatorname{area}(R)
\Bigl[4-2\bigl(|q\cdot u_R|+|q\cdot v_R|\bigr)\Bigr]\\
&\qquad=
\sum_\tau \delta_\tau(q)
\sum_{R\in\tau}\operatorname{area}(R).
\end{aligned}
\tag{120.9}
\]

For one complete train, the sum of the areas of the rhombi along it equals the transverse displacement between its two physical terminal-edge midpoints. Both terminal midpoints lie in the same carrier of diameter `d`, so

\[
\sum_{R\in\tau}\operatorname{area}(R)\le d.
\tag{120.10}
\]

Every `delta_tau(q)` is nonnegative. Thus (120.9), (120.10), and (120.7) give

\[
\begin{aligned}
&\sum_R \operatorname{area}(R)
\Bigl[4-2\bigl(|q\cdot u_R|+|q\cdot v_R|\bigr)\Bigr]\\
&\qquad\le
 d\sum_\tau\delta_\tau(q)
\le dE.
\end{aligned}
\]

Using (120.4) proves (120.1).

This proof is finite. Holes, bridges, repeated outer-face vertices, and disconnected strict-rhombus components are handled by the same physical occurrence convention as Sections 89, 116, and 117.

## 120.4 Recovery of the Section-116 universal constant

Let `phi_R in (pi/3,pi/2]` be the projective angle between the two train directions of one strict unit rhombus. For any unit `q`, choose signs of `u_R,v_R` so their oriented angle is `phi_R`. Then

\[
|q\cdot u_R|+|q\cdot v_R|
\le
\max\{|u_R+v_R|,|u_R-v_R|\}
=2\cos(\phi_R/2)
<\sqrt3.
\tag{120.11}
\]

Consequently each local bracket in (120.1) is strictly larger than

\[
4-2\sqrt3.
\]

The weak uniform estimate gives

\[
 d(L+P_{\rm exc}-2r)
 \ge(4-2\sqrt3)A_4.
\tag{120.12}
\]

Taking a diameter pair `r=d` recovers the existing Section-116 two-arc theorem exactly at its uniform constant. Thus Section 120 is a genuine refinement, not a competing proof with a different convention.

## 120.5 Averaged admissible-chord form

The anisotropic statement can be averaged without changing any finite geometry.

Let `nu` be any probability distribution on admissible ordered cut pairs `(p_-,p_+)` of distinct attachment vertices on the outer walk. For a sampled pair write `r(q)` for its chord length and `q` for its unit chord direction. Averaging (120.2) gives

\[
\boxed{
 d\left(
 L+P_{\rm exc}-2\mathbb E_\nu r
 \right)
 \ge
 \sum_R\operatorname{area}(R)
 \left[
 4-2\left(
 \mathbb E_\nu|q\cdot u_R|
 +\mathbb E_\nu|q\cdot v_R|
 \right)
 \right].
}
\tag{120.13}
\]

In particular, suppose an admissible cut-pair distribution satisfies, for every train direction `u` occurring in the strict-rhombus complex,

\[
\mathbb E_\nu|q\cdot u|
\le {2\over\pi}+\eta
\tag{120.14}
\]

and

\[
\mathbb E_\nu r\ge\rho d.
\tag{120.15}
\]

Then

\[
\boxed{
L+P_{\rm exc}
\ge
2\rho d
+\left(4-{8\over\pi}-4\eta\right){A_4\over d}.
}
\tag{120.16}
\]

The constant

\[
4-{8\over\pi}=1.4535209\ldots
\]

is much larger than the universal worst-case constant

\[
4-2\sqrt3=0.5358983\ldots .
\]

Equation (120.16) is a **conditional corollary only**. This section does not assert that the required admissible cut-pair distribution exists. Its purpose is to isolate the exact next geometric obligation: produce many sufficiently long attachment chords whose directions are diffuse relative to the area-weighted train-direction measure.

## 120.6 Why this is relevant to the live C-II frontier

The reconciled Target-C state identifies the Section-116 outer-walk detour

\[
L+P_{\rm exc}-2d
\]

as one of the two main source-level full-core obstructions. The universal Section-116 theorem forces a linear detour but ignores essentially all phase information in the rhombic core.

Section 120 shows exactly what additional information would strengthen that obstruction:

- a long admissible chord gives the favorable subtraction `2r`;
- train directions transverse to that chord contribute much more than the worst-case `4-2sqrt3` local return constant;
- the entire improvement is area-weighted, so it uses the quadratic rhombic core rather than only boundary-order endpoint counts.

In the Type-II near-disk regime, the force hull is asymptotically circular and coherent train grains occupy all but `o(D^2)` area. A future closure can therefore target a **long-chord directional sampling theorem** rather than another scalar carrier threshold.

A sufficient structural statement would be any uniform pair `(rho,eta)` for the actual harmonic carrier making the lower bound in (120.16) incompatible with the canonical Oler/interface/global-minimality upper currencies. A stronger source-preserving conclusion would turn failure of such directional sampling into a strict diameter-decreasing deformation.

Section 120 does not supply either final implication.

## 120.7 Scope and audit checklist

This theorem uses only:

1. the physical complete-train decomposition and occurrence convention of Sections 89/116/117;
2. the zero-displacement defect-face assignment of Section 116;
3. the exact signed-return projection identity;
4. the exact transverse-span/area identity along a complete train.

It does **not** use:

- deletion of contact-isolated source points;
- a full-source extension of the ZR/ZF affine-kernel theorem;
- phase-bin extraction;
- near-endpoint wrapping stability;
- smoothness of the carrier boundary;
- a claim that all chord directions are available.

The hostile-audit points are:

- verify that arbitrary attachment cut vertices really produce the two host vectors `q,-q` with exact excess `L-2r`;
- verify the defect-face zero-host assignment remains injective and occurrence-counted;
- verify the train transverse area sum is bounded by the same carrier diameter `d`;
- verify no sign/orientation information is lost in passing to `|q dot u_tau|`;
- treat (120.14)--(120.16) strictly as a conditional sampling corollary.

**Theorem state:** unchanged. Independent hostile audit is required before any promotion or use as an authoritative C-II premise.
