<!-- theorem-state: {"artifact_id":"ART-68C644B7C160","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_near_density_shell_global_competitor_2026-09-12.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=5f57f3fd6191b878b120c3d6655d3ef6683acddb; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Target C — near-density triangle-free shell families have a strict global competitor

**Date:** 2026-09-12  
**Run type:** hostile source-level regression / inactive-container branch  
**Target:** C-II  
**Classification:** proved candidate; noncanonical  
**Certificate:** `research/verify_target_c_near_density_shell_global_competitor.py`

## Status and exact implication

This note removes a more demanding shell regression than the earlier buffered-cloud
examples.  The source cardinalities satisfy

\[
\frac{|A_q|}{\operatorname{diam}(A_q)^2}
\longrightarrow
\Delta_2:=\frac{\pi}{2\sqrt3},
\]

the global minimum-diameter density, while the unit-contact graph is a triangle-free
cycle and the quadratic interior population is contact-isolated.  Nevertheless the
family has an explicit same-cardinality unit-separated competitor of strictly smaller
diameter.

The result does **not** close the arbitrary inactive-chamber branch.  Its value is
source-level: even a near-density regular shell plus an almost-unit triangular cloud
cannot be a global minimizer.  The surviving obstruction is therefore not explained
by the shell's density deficit; it is the absence of a comparison theorem for an
arbitrary canonical inactive chamber and its actual positive-contact boundary.

## 1. Construction

Let (q\ge 8) be even and let (B_q) be the vertices of a regular (q)-gon with
side length one.  Put

\[
R_q=\frac1{2\sin(\pi/q)},
\qquad
D_q=2R_q=\frac1{\sin(\pi/q)}.
\]

The polygon has diameter (D_q), and its consecutive vertices form a unit cycle.
Nonconsecutive polygon chords are strictly longer than one, so this cycle is
triangle-free.

Fix a constant (a>1), restrict to even orders with (R_q>a), and set

\[
s_q=1+D_q^{-2}.
\]

Let (Λ_{s_q}) be a triangular lattice with nearest-neighbor spacing (s_q).  By
averaging translates over one fundamental cell, some translate contains at least

\[
z_q:=\left\lfloor
\frac{2\pi}{\sqrt3\,s_q^2}(R_q-a)^2
\right\rfloor
\tag{ND.1}
\]

lattice points in the disk (B(0,R_q-a)).  Select exactly (z_q) of them and call
the set (I_q).  Define

\[
A_q:=B_q\cup I_q.
\tag{ND.2}
\]

The shell and the cloud are disjoint in the strongest useful sense: for (b\in B_q)
and (x\in I_q),

\[
|b-x|\ge |b|-|x|\ge a>1.
\tag{ND.3}
\]

All nonzero lattice differences in (I_q) have length at least (s_q>1).  Thus the
only unit contacts in (A_q) are the shell edges.  In particular (A_q) contains
no unit equilateral triangle, and

\[
\operatorname{diam}(A_q)=D_q.
\tag{ND.4b}
\]

The source is triangle-free at every finite (q), not only asymptotically.

The shell also carries a strictly positive mixed KKT stress.  Write

\[
\phi_q=\frac\pi q,
\qquad D_q=\frac1{\sin\phi_q}.
\]

Give every one of the (q) shell edges the contact multiplier

\[
\alpha_q=\frac1{q\sin^2\phi_q},
\]

and every one of the (q/2) antipodal diameter pairs the multiplier

\[
\beta_q=\frac2q.
\]

At a shell vertex, the two contact vectors have radial sum
(4R_q\sin^2\phi_q), while its antipodal diameter vector has length (2R_q).
Thus

\[
\alpha_q\,4R_q\sin^2\phi_q
=\beta_q\,2R_q=\frac{4R_q}{q}.
\]

The equilibrium equation holds at every shell vertex, all displayed multipliers are
strictly positive, and

\[
\sum_H\beta_q=1,
\qquad
\sum_C\alpha_q=q\alpha_q=D_q^2.
\tag{ND.4a}
\]

The interior points have no active constraints and contribute no equilibrium rows.
Consequently this family has the full positive shell stress and still has the strict
same-cardinality competitor below.  The stress is a first-order certificate only; it
does not assert global minimality and it does not assign affine-kernel control to the
contact-isolated interior points.

## 2. The family has global leading density

Write (Delta=2/\sqrt3).  Since (q=\pi D_q+O(D_q^{-1})),

\[
s_q^{-2}=1+O(D_q^{-2}),
\qquad
(R_q-a)^2=\frac{D_q^2}{4}-aD_q+O(1).
\]

Equation (ND.1) therefore gives

\[
z_q=\frac{\Delta\pi}{4}D_q^2+O(D_q),
\qquad
q=O(D_q),
\]

and hence

\[
\boxed{
\frac{|A_q|}{D_q^2}
\longrightarrow
\frac{\Delta\pi}{4}=\frac{\pi}{2\sqrt3}.
}
\tag{ND.5}
\]

This is the same leading density as global minimum-diameter sources.  The shell is
not being dismissed merely because it has too few points.

## 3. Strict same-cardinality competitor

Choose a constant (c) with

\[
0<c<a-\frac{\sqrt3}{2}.
\tag{ND.6}
\]

The unit triangular lattice has density (Delta).  Translation averaging gives a
translate containing at least

\[
w_q:=\left\lfloor\Delta\pi(R_q-c)^2\right\rfloor
\tag{ND.7}
\]

points in (B(0,R_q-c)).  We claim (w_q>|A_q|) for all sufficiently large even
(q).

Indeed, the upper bound in (ND.1), together with (q=\pi D_q+O(D_q^{-1})), gives

\[
|A_q|
\le
\frac{\Delta\pi}{4}D_q^2
+\bigl(\pi-\Delta\pi a\bigr)D_q+O(1).
\tag{ND.8}
\]

On the other hand (ND.7) gives

\[
w_q
\ge
\frac{\Delta\pi}{4}D_q^2-\Delta\pi cD_q+O(1).
\tag{ND.9}
\]

Subtracting, the coefficient of (D_q) in (w_q-|A_q|) is

\[
\Delta\pi\left(a-c-\frac1\Delta\right)
=\Delta\pi\left(a-c-\frac{\sqrt3}{2}\right)>0
\tag{ND.10}
\]

by (ND.6).  Therefore (w_q>|A_q|) eventually.  Select (|A_q|) of the (w_q)
lattice points.  The selected competitor is unit-separated and has diameter at most

\[
2(R_q-c)=D_q-2c<D_q.
\tag{ND.11}
\]

Consequently

\[
\boxed{D(|A_q|)\le D_q-2c<D_q=\operatorname{diam}(A_q)}
\]

for all sufficiently large even (q).  The competitor is allowed to contain unit
equilateral triangles, as every valid global comparison permits.

The proof uses only translation averaging and the elementary expansion of the regular
polygon radius.  It is therefore a finite global-minimality comparison, not a
heuristic density argument.

## 4. What this regression rules out

The following proposed explanation for the inactive branch is false:

```text
triangle-free unit shell + quadratic isolated interior
    may survive global minimality because its n/D^2 density is asymptotically optimal.
```

Even after reducing the cloud spacing excess to (D_q^{-2}), so that its loss from
the triangular density is only (O(1)), the one-unit-plus radial separation from the
shell leaves a positive linear source-count margin.  A global lattice competitor uses
that margin to reduce the diameter by a fixed amount.

This does not prove the same statement for an arbitrary inactive chamber.  A canonical
chamber need not be a concentric regular shell, its boundary may have non-unit outer
arcs, and its source population is known only up to an (O(D)) Oler slack.  The exact
remaining bridge is still one of:

1. a general source-capacity inequality replacing the regular-shell expansion in
   (ND.8); or
2. a source-preserving strict competitor that changes the actual diameter-carrying
   core while retaining every source point.

No contact-isolated point is deleted in the construction or in the comparison, and no
full-source affine-kernel statement is used.

## 5. Classification

The finite construction and the asymptotic competitor comparison are **proved
candidate / noncanonical**.  The theorem-state manifest remains unchanged:
C-II and Level I are open, and the canonical inactive-chamber theorem remains only a
structural reduction.  The companion script is an arithmetic sanity certificate; the
translation-averaging and (O(D)) estimates above are the proof.

### Arithmetic self-audit correction

The original sanity script multiplied the leading-margin lower bound by an extra
factor of pi. That asserted lower bound was invalid, although its positive sign
and the analytic comparison (ND.10) were unaffected. The corrected check uses
exact rational arithmetic and the deliberately weaker bound pi > 3; the certified
coefficient is at least 6/13. The missing addition sign in (ND.8) is also restored.
