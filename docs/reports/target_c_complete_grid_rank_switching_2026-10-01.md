<!-- theorem-state: {"artifact_id":"ART-34ADF52D063F","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II -- rank forces distributed diameter support on the complete O-O grid

Date: 2026-10-01  
Base main: d42d85b0d1d4a27617fabcff834ce7330d7f91fd  
Status: proof-only; C-II remains open.

## Theorem

Let \(\tau_1,\ldots,\tau_m\) be non-singleton global outer-to-outer stopped trains,
ordered on one simple complement-dual path. Assume at least one complete stopped train
is not selected. Orient the selected cuts as nested shores.

For an actual diameter edge \(h=xy\), let
\(\varepsilon_{hi}\in\{-1,0,1\}\) be its signed incidence with cut \(i\), and let
\(r_h=p_y-p_x\). Exact laminar interval support gives

\[
(\varepsilon_{h1},\ldots,\varepsilon_{hm})
=0,\ldots,0,\sigma_h,\ldots,\sigma_h,0,\ldots,0
\]

with one constant nonzero sign \(\sigma_h\) on a possibly empty or full interval.

If \(u_i\) is the oriented unit train direction, define the actual-diameter derivative
matrix

\[
M_{hi}=\varepsilon_{hi}(r_h\cdot Ju_i).
\]

Then:

\[
\boxed{\operatorname{rank}M=m.}
\tag{1}
\]

If \(N_{\rm prop}\) is the number of actual diameter edges with nonempty proper
support on the selected path, then

\[
\boxed{N_{\rm prop}\ge m-2.}
\tag{2}
\]

If \(s\) is the number of adjacent selected positions \(i,i+1\) at which some
diameter incidence changes, then

\[
\boxed{s\ge\left\lceil\frac m2\right\rceil-1.}
\tag{3}
\]

Moreover the \(s\) changes can be charged to \(s\) distinct actual diameter endpoints
whose complement-dual projections lie in distinct coarse slabs between consecutive
selected cuts.

If all selected trains have one exact projective direction, then after consistent
orientation

\[
\boxed{N_{\rm prop}\ge m-1,\qquad s\ge m-1.}
\tag{4}
\]

## Proof

Superpose the exact one-train O-O infinitesimal shears with coefficients
\(\theta_1,\ldots,\theta_m\). If \(M\theta=0\), every positive contact and every actual
diameter has zero first length variation. Canonical mixed infinitesimal rigidity makes
the flex Euclidean. Selected train angular rates are \(\theta_i\), while every
unselected complete train has angular rate zero. A Euclidean rotation has one common
rate on all trains, so the unselected train kills the rotation. Only translation
remains, hence every \(\theta_i=0\). This proves (1).

For a full-span diameter edge the incidence sign is constant, so its row is

\[
\pm(r_h\cdot Ju_1,\ldots,r_h\cdot Ju_m).
\]

As \(r_h\in\mathbb R^2\) varies, all full-span rows lie in a fixed space of dimension
at most two. Empty-support rows vanish. Each proper-support edge contributes at most
one row dimension. Thus

\[
m=\operatorname{rank}M\le2+N_{\rm prop},
\]

which proves (2).

The \(s\) incidence-change positions partition the selected columns into \(s+1\)
consecutive blocks. On each block every \(\varepsilon_{hi}\) is constant. Therefore
the restriction of the complete row space to one block has dimension at most two:
it is spanned by the two coordinate sequences of \(Ju_i\). Hence

\[
m=\operatorname{rank}M\le2(s+1),
\]

which proves (3).

A start or stop between two consecutive selected cuts means that one endpoint of the
corresponding diameter edge projects to the unique coarse dual-path slab between
those cuts. Distinct selected boundaries give disjoint slabs, so choosing one witness
endpoint per switching boundary gives distinct actual diameter endpoints.

If all \(u_i\) are the same after reorientation, full-span rows have rank at most one
and each constant-incidence block has rank at most one. The same two arguments give
(4).

## Current fixed-star rectangle

Current main gives, after the local witness-cell extraction, a complete O-O rectangle
\(A'\times B'\) with

\[
|A'|,|B'|\ge(c_*-o(1))D,
\qquad
c_*=
\frac{\kappa^4}{16\pi^3C_KM_K},
\]

where \(C_K=\lfloor4K\rfloor+2\) and
\(M_K=2\lfloor4K\rfloor+3\).

Apply the theorem separately to the two shores. The opposite shore supplies an
unselected train. Therefore

\[
N_{\rm prop}^A,N_{\rm prop}^B\ge(c_*-o(1))D
\]

and

\[
s_A,s_B\ge\left(\frac{c_*}{2}-o(1)\right)D.
\]

The two common witness edges on either shore are full-span, so they are not among
that shore's proper-support rows. Thus the fixed-star branch contains, on each shore,

\[
\boxed{
\text{two fixed full-span witness rows}
+
\Omega(D)\text{ proper-support actual diameter rows}
+
\Omega(D)\text{ support-switch positions}.
}
\]

In the threshold witness-cell case, where the retained shore has one exact projective
direction, the switching bound improves to \(s\ge(c_*-o(1))D\).

## Remaining target

The previous focus on the four common witness rows was incomplete: those rows certify
two-sided bracing but cannot carry the mixed-rigidity rank of the linear train grid.
The fixed-star branch must now reconcile two gap-local witness cells with linearly
distributed support changes on both transverse shores. The next useful obstruction is
a convex-thrackle order theorem coupling those two switching systems.

The split-star and inactive-interface branches remain open.

No computation, verifier, numerical experiment, or CI output is used.
