<!-- theorem-state: {"artifact_id":"ART-B47C0DDAB20B","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — nested-disk boundary rigidity excludes the exact RSR/DD endpoint

**Date:** 2026-09-10  
**Branch base:** `a4f0705047cfb1c0825e920e8573a722061c39b7`  
**Depends on:** RX and AC on this branch; C36/C49 force-hull attachment geometry  
**Run type:** compactness / convex-boundary rigidity / endpoint exclusion  
**Target:** Target C, C-II after ZF

## LEVEL I STATUS

`STILL OPEN`.

RX gives the exact generic post-ZF scalar lower endpoint

\[
\lambda_{RD}=0.5981536184601480\ldots .
\]

AC proves that any sequence attaining this endpoint would contain one macroscopic
unloaded component whose attachment hull is asymptotically a disk of diameter
`lambda_RD D`.  Every vertex of that attachment hull is simultaneously a loaded
vertex on the boundary of the full force hull, whose diameter is `D`.

Those two facts are incompatible.

### Theorem ND — RD endpoint exclusion

No unbounded post-ZF survivor sequence can satisfy

\[
\boxed{
\frac{e_{BB}+2s_C}{D}\to\lambda_{RD}.
}
\tag{ND.1}
\]

Consequently there exist absolute constants

\[
\boxed{
\epsilon_{ND}>0,
\qquad D_0<\infty,
}
\]

such that every sufficiently large post-ZF survivor satisfies

\[
\boxed{
\frac{e_{BB}+2s_C}{D}
\ge\lambda_{RD}+\epsilon_{ND}.
}
\tag{ND.2}
\]

The gap is currently nonexplicit.  The explicit certified generic floor remains
`>0.598`, but the exact variational value `lambda_RD` is now known not to be the true
asymptotic endpoint.

---

## 1. Endpoint attachment hull from AC

Assume for contradiction that a sequence satisfies ND.1.  Let `I_*` be the
macroscopic unloaded component selected by AC and put

\[
K_D:=\operatorname{conv}A_*,
\]

where `A_*` is its set of distinct loaded attachment vertices.

AC proves

\[
\boxed{
\frac{\operatorname{diam}K_D}{D}\to\lambda_{RD},
}
\tag{1.1}
\]

and

\[
\boxed{
\frac{\operatorname{area}K_D}{D^2}
\to\frac\pi4\lambda_{RD}^2.
}
\tag{1.2}
\]

Also

\[
K_D\subseteq F_D,
\tag{1.3}
\]

where `F_D` is the full force hull, and every point of `A_*` is a loaded force-hull
boundary vertex.  Thus

\[
\boxed{A_*\subseteq\partial F_D.}
\tag{1.4}
\]

Finally the force hull contains the endpoints of every loaded diameter edge, so

\[
\boxed{\operatorname{diam}F_D=D.}
\tag{1.5}
\]

---

## 2. Simultaneous Hausdorff limits

Scale by `D` and translate both bodies by the same point of `K_D`.  Write

\[
\widehat K_D:=D^{-1}(K_D-x_D),
\qquad
\widehat F_D:=D^{-1}(F_D-x_D).
\tag{2.1}
\]

Both families lie in a fixed bounded disk because `diam(F_D)=D`.  By Blaschke
selection, pass to a subsequence on which

\[
\widehat K_D\to K_\infty,
\qquad
\widehat F_D\to F_\infty
\tag{2.2}
\]

in Hausdorff distance.

Inclusion is closed under Hausdorff convergence, so

\[
K_\infty\subseteq F_\infty.
\tag{2.3}
\]

Diameter and planar convex area are continuous under Hausdorff convergence.  Equations
(1.1)--(1.2) therefore give

\[
\operatorname{diam}K_\infty=\lambda_{RD},
\qquad
\operatorname{area}K_\infty=rac\pi4\lambda_{RD}^2.
\tag{2.4}
\]

By equality in the planar isodiametric inequality,

\[
\boxed{K_\infty\text{ is a Euclidean disk of diameter }\lambda_{RD}.}
\tag{2.5}
\]

Meanwhile (1.5) gives

\[
\boxed{\operatorname{diam}F_\infty=1.}
\tag{2.6}

---

## 3. Vertices of the attachment hull become dense on the limit circle

Let `V_D` be the vertex set of the polygon `K_D`.  Since

\[
K_D=\operatorname{conv}A_*,
\]

every vertex of `K_D` belongs to `A_*`.  Hence by (1.4)

\[
\boxed{V_D\subseteq\partial F_D.}
\tag{3.1}
\]

After normalization the same holds for `widehat V_D`.

We claim that the normalized polygon vertices become dense on the circle
`partial K_infty`.  Suppose not.  Then along a subsequence there is an arc of the
limit circle of some fixed positive chord length whose nearby portion of
`partial widehat K_D` contains no polygon vertex.  The corresponding portion of the
polygon boundary is therefore contained in one straight edge joining vertices on
opposite sides of that arc.  A chord spanning a fixed positive arc of a fixed-radius
circle has a fixed positive sagitta.  Hence that straight edge stays a fixed positive
Hausdorff distance inside the circular arc, contradicting

\[
\widehat K_D\to K_\infty.
\]

Thus:

### Lemma ND.1 — vertex density

For every `x in partial K_infty`, there are vertices

\[
v_D\in V_D
\]

along a subsequence such that

\[
\boxed{v_D/D-x_D/D\to x.}
\tag{3.2}

Equivalently, the Hausdorff distance from the normalized vertex set to the limit circle
tends to zero.

No lower bound on `|A_*|` is needed; disk convergence itself forces the polygon mesh
to vanish.

---

## 4. Boundary points remain boundary points in a convex Hausdorff limit

We use a standard elementary support-function observation.

### Lemma ND.2 — boundary closedness for convex Hausdorff limits

Let compact convex bodies `C_j` converge in Hausdorff distance to `C`.  If

\[
x_j\in\partial C_j,
\qquad
x_j\to x,
\]

then

\[
\boxed{x\in\partial C.}
\]

### Proof

For each `j`, choose a unit supporting normal `u_j` at `x_j`:

\[
x_j\cdot u_j=h_{C_j}(u_j).
\]

Pass to a subsequence with `u_j->u`.  Hausdorff convergence of convex bodies is
equivalent to uniform convergence of support functions on the unit circle.  Therefore

\[
x\cdot u=h_C(u),
\]

so `x` lies on a supporting line of `C`, hence on `partial C`. `square`

Apply ND.2 to the vertices supplied by ND.1 and use (3.1).  Every point of the limit
circle is a limit of points on `partial widehat F_D`.  Hence

\[
\boxed{
\partial K_\infty\subseteq\partial F_\infty.
}
\tag{4.1}

---

## 5. A convex body cannot strictly contain a disk while preserving its entire boundary

### Lemma ND.3 — nested disk boundary rigidity

Let `B` be a nondegenerate closed Euclidean disk and `C` a compact convex set.  If

\[
B\subseteq C
\]

and

\[
\partial B\subseteq\partial C,
\]

then

\[
\boxed{C=B.}
\]

### Proof

Translate so the disk center is the origin and write its radius as `r>0`.  Suppose
there were a point `y in C\setminus B`.  Then `|y|>r`.  Put

\[
x:=r\frac y{|y|}\in\partial B.
\]

Since `0` is an interior point of `B`, it is an interior point of `C`.  Also

\[
x=t y+(1-t)0,
\qquad
 t=\frac r{|y|}\in(0,1).
\]

Any strict convex combination of a point of `C` with an interior point of `C` is
interior to `C`: if `B(0,eta) subset C`, then

\[
t y+(1-t)B(0,\eta)
=B(x,(1-t)\eta)\subseteq C.
\]

Thus `x in int(C)`, contradicting `x in partial C`.  Hence no such `y` exists and
`C=B`. `square`

Apply ND.3 to (2.3), (2.5), and (4.1).  We obtain

\[
\boxed{F_\infty=K_\infty.}
\tag{5.1}

But then

\[
\operatorname{diam}F_\infty
=\operatorname{diam}K_\infty
=\lambda_{RD}<1,
\]

contradicting (2.6).  This proves ND.1.

---

## 6. Uniform nonattainment gap

RX already proves the asymptotic lower bound

\[
\liminf\lambda_D\ge\lambda_{RD}.
\]

If ND.2 were false, then for every integer `j` there would be arbitrarily large
post-ZF survivors with

\[
\lambda_D<\lambda_{RD}+1/j.
\]

Choose a diagonal sequence with `D_j->infinity`.  RX supplies the matching lower
bound, so after passage to a subsequence

\[
\lambda_{D_j}\to\lambda_{RD},
\]

contradicting ND.1.  Therefore some absolute `epsilon_ND>0` and `D_0` exist, proving
ND.2.

---

## 7. Why this closes the exact RD geometry

The contradiction does not use the detailed geometry of the outer pockets or the
Woodall classification after AC has concentrated the attachment area.  It uses only
four facts:

1. one attachment hull is asymptotically isodiametric;
2. its diameter is a strict fraction `lambda_RD<1` of the force-hull diameter;
3. every attachment-hull polygon vertex lies on the force-hull boundary;
4. an isodiametric planar limit is a disk, whose boundary cannot remain entirely on
   the boundary of a strictly larger convex body.

This is a stronger endpoint mechanism than the initial singleton-pocket plan.  The
linear singleton layer remains useful for quantitative stability, but is not needed
for qualitative exclusion.

---

## 8. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| simultaneous `K_D,F_D` Hausdorff limit | proved | common diameter-one bounded container + Blaschke |
| `K_infty` is disk of diameter `lambda_RD` | proved | AC area/diameter equality + isodiametric equality |
| attachment-hull vertices dense on disk boundary | proved | otherwise fixed chord sagitta violates Hausdorff convergence |
| limits of convex-body boundary points remain boundary points | proved | supporting normals + support-function convergence |
| nested disk boundary rigidity | proved | interior-point convex combination |
| exact RD endpoint impossible | proved | would force force hull limit equal smaller disk |
| positive uniform gap above `lambda_RD` | proved nonconstructively | diagonal sequence + RX lower bound |
| Level I | still open | high-surplus survivors above the gap remain possible |

---

## 9. Next run

Quantify ND.  A near-isodiametric attachment hull has small Hausdorff distance from a
disk by an elementary planar stability argument.  Because its vertices lie on the
force-hull boundary, sufficiently dense approximate circle contact should bound how
far the force hull can extend beyond that disk.  Any explicit relation

\[
\operatorname{diam}F/D-\operatorname{diam}K_*/D
\le
\omega(\text{attachment-area deficit})
\]

with `omega(t)->0` would turn the fixed diameter gap

\[
1-\lambda_{RD}=0.4018463815\ldots
\]

into a quantitative endpoint exclusion and raise the certified generic surplus floor
above `0.5981536184...`.