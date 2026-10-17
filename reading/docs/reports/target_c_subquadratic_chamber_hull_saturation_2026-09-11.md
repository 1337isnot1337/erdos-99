> Generated reading edition · [exact source](../../../docs/reports/target_c_subquadratic_chamber_hull_saturation_2026-09-11.md) · source SHA-256 `998c72f1706f137b4ddb44a3a42acaa61aeb6525b2146ec97642a12eb8ad9de6`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-4E2F880A796B","canonical":true,"claim_ids":["C-INACTIVE-HULL-STABILITY"],"claim_statuses":{"C-INACTIVE-HULL-STABILITY":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Erdős Problem #99 — convex-hull saturation inside the macroscopic inactive chamber

**Date:** 2026-09-11
**Repository commit:** `0b7294be0707f0f85f6f6b1a3d2cbcb69f2a7e0d`
**State version:** `2026-09-11.audit.31`
**Run type:** closing-proof continuation / convex-capacity stability
**Target:** Target C, C-II, subquadratic positive-contact-core branch
**Starting status:** canonical Sections 59, 67, and 77
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md`
**External literature search:** not used
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`.

This report records a source-specific convex-hull stability corollary of the canonical
Section-77 inactive-chamber statement. It does not claim a C-II closure.

The new implication is

```text
Canonical Section 77: one chamber has area Theta(D^2), perimeter O(D),
            and isolate population equal to its Oler area capacity up to O(D)
  + Oler applied to the convex hull of those isolates
  + an elementary cap lower bound from a macroscopic inball
  -> the convex hull of the chamber isolates is O(sqrt(D))-Hausdorff close
     to the entire chamber and contains a macroscopic inner disk
  -> the isolate-heavy branch contains a source hull, not merely a source count,
     that is asymptotically the chamber itself.
```

The remaining obstruction is still the absence of a finite source-preserving
diameter-decreasing move. Near-triangular strict packings remain a binding regression.

## 1. Starting canonical endpoint

Use the contact-minimal, then diameter-pair-minimal C-II representative, retaining all
source points. Let (D) be its diameter, (F) the full actual force hull, and (m) the
number of vertices of the nonisolated positive-contact core. Canonical Section 77
establishes, within its stated branch, a convex inactive chamber (C_*) with assigned
contact-isolated population (S_*) such that, along the branch, with
C_*\subseteq F\subseteq\operatorname{conv}A and \operatorname{diam}(C_*)\le D,

```math
A_*:=\operatorname{area}(C_*)=\Omega(D^2),
\qquad
z_*:=|S_*|={A_*\over a_0}+O(D),
\qquad
P_*:=\operatorname{per}(C_*)=O(D),
\tag{CH.1}
```

where (a_0=\sqrt3/2). Every point of (S_*) is an actual source point and is
contact-isolated in the full source. The chamber is either an exceptional bounded
contact face or an outer pocket; no point is deleted from the source.

The Section-77 theorem gives absolute constants (a_{\rm ch},P_{\rm ch},L_{\rm ch}>0)
such that, after passing to a sufficiently large member of the branch,

```math
A_*\ge a_{\rm ch}D^2,qquad P_*\le P_{\rm ch}D,qquad
a_0z_*\ge A_*-L_{\rm ch}D.
\tag{CH.2}
```

The exact proposed bridge is therefore

```math
\text{near-capacity isolated chamber}
\Longrightarrow
\text{source-specific geometric stability}
\Longrightarrow
\text{finite C-II release or contradiction}.
```

The first implication is proved here. The second remains open.

## 2. A convex cap lemma

We first isolate the geometric estimate used to turn an (O(D)) area deficit into an
(O(\sqrt D)) support deficit.

### Lemma CH.1 (macroscopic inball)

Let (C\subset\mathbb R^2) be a compact convex body with area (A_C>0), perimeter
(P_C), and inradius (r_C). Then

```math
\boxed{r_C\ge {A_C\over P_C}.}
\tag{CH.3}
```

### Proof

Let (r=r_C), and let (C_{-t}) be the inner parallel body at distance (t), for
(0\le t\le r). At the maximal inradius, (C_{-r}) has zero area; otherwise a
positive-area inner parallel body would allow a larger inscribed disk. The coarea
formula for the distance to the boundary gives

```math
A_C=\int_0^r \operatorname{per}(C_{-t})\,dt.
```

Perimeter is monotone under inclusion for convex bodies, so

```math
A_C\le rP_C.
```

Rearranging proves (CH.3). $`\square`$

### Lemma CH.2 (support-gap cap bound)

Let (C) be a convex body with diameter at most (D) and inradius (r_C). Let
(K\subseteq C) be a convex body. For a unit vector (u), put

```math
t(u):=h_C(u)-h_K(u)\ge0.
```

For every (0\le s\le\min\{t(u),r_C\}),

```math
\boxed{\operatorname{area}(C\setminus K)
\ge {r_C\over D}\,s^2.}
\tag{CH.4}
```

### Proof

Choose an inball (B(o,r_C)\subseteq C) and a support point (v\in C) with
(u\cdot v=h_C(u)). Put

```math
s_0=h_C(u)-u\cdot o.
```

The support inequality for the inball gives (s_0\ge r_C). Also
(s_0\le|v-o|\le D).
Let (w) be a unit vector perpendicular to (u), and set

```math
q_+=o+r_Cw,
\qquad
q_-=o-r_Cw.
```

The triangle (T=\operatorname{conv}\{v,q_+,q_-\}) lies in (C). Its cap cut off by
the line (u\cdot x=h_C(u)-s_1), for (0\le s_1\le r_C\le s_0), is a triangle of
height (s_1) and base (2r_Cs_1/s_0), where (s_0=h_C(u)-u\cdot o), hence has area

```math
{r_Cs_1^2\over s_0}\ge {r_C\over D}s_1^2.
```

Since (s_1\le t(u)), (K) lies in the half-plane (u\cdot x\le h_C(u)-s_1), so this
cap is contained in (C\setminus K), proving (CH.4). $`\square`$

## 3. Oler-saturated chamber hull

Let (K_*:=\operatorname{conv}(S_*)). Because (S_*) is a subset of the globally
unit-separated source, it is unit-separated. Oler applied to (S_*\subseteq K_*) gives

```math
a_0z_*
\le \operatorname{area}(K_*)+c_0\operatorname{per}(K_*)+a_0,
\qquad c_0={\sqrt3\over4}.
\tag{CH.6}
```

Since (K_*\subseteq C_*), convex perimeter monotonicity gives

```math
\operatorname{per}(K_*)\le P_*.
\tag{CH.7}
```

Combining (CH.2), (CH.6), and (CH.7),

```math
\operatorname{area}(C_*)-\operatorname{area}(K_*)
\le (L_{\rm ch}+c_0P_{\rm ch})D+a_0
=:M_{\rm ch}D.
\tag{CH.8}
```

Thus (K_*) misses only (O(D)) area from a chamber of area (Omega(D^2)).

By Lemma CH.1 and (CH.2),

```math
r(C_*)\ge {a_{\rm ch}\over P_{\rm ch}}D=:\kappa_{\rm ch}D.
\tag{CH.9}
```

For a support direction (u), let (t(u)=h_{C_*}(u)-h_{K_*}(u)). If
(t(u)>r(C_*)), apply Lemma CH.2 with (s_1=r(C_*)). This gives an area deficit at
least (r(C_*)^3/D)=\Omega(D^2), using (CH.9), contradicting (CH.8) for large
(D). Hence (t(u)\le r(C_*)) for every direction eventually. Applying (CH.4) with
(s_1=t(u)) and (CH.8) then gives

```math
t(u)^2
\le {D\over r(C_*)}\,M_{\rm ch}D
\le {M_{\rm ch}\over\kappa_{\rm ch}}D,
```

uniformly in (u). Therefore

```math
\boxed{
\sup_{u\in S^1}\bigl(h_{C_*}(u)-h_{K_*}(u)\bigr)
\le C_{\rm ch}\sqrt D,
\qquad
C_{\rm ch}:=\sqrt{M_{\rm ch}/\kappa_{\rm ch}}.
}
\tag{CH.10}
```

For nested convex bodies, the support-function supremum is their Hausdorff distance.
Consequently

```math
\boxed{d_H(C_*,K_*)\le C_{\rm ch}\sqrt D.}
\tag{CH.11}
```

This is a source-specific stability theorem: the actual isolated source points have a
convex hull filling the actual inactive chamber to sublinear geometric error.

## 4. A protected inner disk of the isolated-source hull

Let (o_*) be a center of an inball of (C_*). For every unit vector (u),

```math
h_{K_*}(u)
\ge h_{C_*}(u)-C_{\rm ch}\sqrt D
\ge u\cdot o_*+r(C_*)-C_{\rm ch}\sqrt D.
```

The support function of (B(o_*,r(C_*)-C_{\rm ch}\sqrt D)) is the right-hand side.
For sufficiently large (D), (CH.9) makes this radius positive, and the support
inequalities imply

```math
\boxed{
B\bigl(o_*,\kappa_{\rm ch}D-C_{\rm ch}\sqrt D\bigr)
\subseteq K_*\subseteq C_*.
}
\tag{CH.12}
```

Thus the convex hull of the contact-isolated source points contains a disk whose
radius is linear in (D), with an explicit (O(\sqrt D)) loss. Every vertex of this
inner hull is still one of the original contact-isolated source points; no KKT-positive
contact has been inferred.

The same argument also gives

```math
\operatorname{diam}(K_*)\ge\operatorname{diam}(C_*)-2C_{\rm ch}\sqrt D,
\qquad
\operatorname{area}(K_*)=A_*+O(D).
\tag{CH.13}
```

The diameter statement is only $`\Omega(D)`$, not a claim that (K_*) contains an
actual diameter pair of the full source.

## 5. Exact frontier effect on C-II

Section 77 reduces (m=o(D^2)) to one macroscopic chamber with a near-capacity
population. The present corollary upgrades that endpoint to

```text
m=o(D^2)
  -> C_* has area Omega(D^2), perimeter O(D), and z_*=area(C_*)/a0+O(D)
  -> K_*=conv(isolates in C_*) has area(C_*)-area(K_*)=O(D)
     and d_H(C_*,K_*)=O(sqrt(D))
  -> K_* contains a disk of radius kappa D-O(sqrt(D))
     and is made entirely from contact-isolated source points.
```

This removes a second possible escape from the chamber theorem: the isolated points
cannot be near-capacity only because of a thin boundary cloud while leaving the
macroscopic chamber's convex geometry empty. Their own source hull fills the chamber
at sublinear geometric resolution.

The exact remaining closure lemma can now be stated source-geometrically:

> **Protected inactive-hull release (PIHR).** Suppose a contact-minimal,
> diameter-pair-minimal C-II source contains a convex set (K_*) of contact-isolated
> source points satisfying (CH.12), with (K_*) at (O(\sqrt D)) Hausdorff distance
> from a chamber whose boundary is made of the positive-contact core and/or actual
> force-hull sides. Prove either a same-cardinality unit-separated competitor of
> diameter (<D), or a contradiction with the exact post-ZF face/response ledger
> (for example, a strict violation of one of its nonnegative inequalities).

PIHR is not proved here. The strict near-equilateral rhombic regression shows why
`d_H=O(\sqrt D)` and contact-isolation alone do not supply a fixed density gap or an
automatic unit equilateral triangle. A successful PIHR proof must use the global
minimum-diameter coupling or the exact response/face ledger.

## 6. Dependencies and claim audit

| Claim | Status | Dependencies | Reason |
| --- | --- | --- | --- |
| CH.1 inradius bound | unreviewed candidate | elementary convex coarea | (A\le rP) for inner parallel bodies |
| CH.2 cap lower bound | unreviewed candidate | elementary convex geometry | inball/support-point triangle |
| CH.8 chamber area deficit (O(D)) | unreviewed candidate | Section 77, Oler | isolate population saturates chamber area |
| CH.10–CH.11 Hausdorff (O(\sqrt D)) hull stability | unreviewed candidate | CH.1–CH.8 | support gaps create quadratic caps |
| CH.12 protected inner disk | unreviewed candidate | CH.11, convex support functions | support inequalities contain the eroded inball |
| PIHR release/contradiction | open | global minimum and C-II ledger | no finite move is proved |
| C-II / Level I | open | all current dependencies | the protected-hull release remains missing |

## 7. Regression and scope audit

- **Contact-isolated points:** all points in (S_*) are retained source points. The
  report never extends the Section-57 affine-kernel theorem to them and never calls
  their hull a KKT force hull.
- **Near-equilateral strict rhombi:** compatible. A strict oblique triangular lattice
  can have no unit contacts while its convex hull is close to a filled chamber; this is
  why PIHR is left open.
- **Global optimality:** used only through the contact-minimal/diameter-pair-minimal
  setup, the canonical Section-77 chamber statement, and Oler. No standalone
  feasible packing is promoted to a minimizer.
- **Exceptional face versus outer pocket:** both are covered; only convexity, area,
  perimeter, and the Section-77 capacity relation are used.
- **Diameter:** (CH.13) does not infer that chamber isolates are diameter endpoints.
- **Response/KKT weights:** no coefficient floor or new positive multiplier is claimed.
- **Rejected routes:** no inward Reuleaux-cap containment, no deletion of isolates, no
  full-source ZR/ZF extension, and no Eppstein equality uniqueness is used.

## 8. Promotion recommendation

**Canonical after the independent promotion audit** at
docs/audits/target_c_inactive_chamber_hull_stability_promotion_2026-09-12.md.
The result is a canonical geometric dependency, while the PIHR release and C-II
remain open.

## 9. Handoff

1. Read Section 77 and this report together in the (m=o(D^2)) branch.
2. The next exact target is PIHR: turn the protected all-isolate hull into a
   source-preserving diameter reduction or a contradiction in the exact post-ZF
   face/response ledger.
3. Keep the quadratic-core Section-76 complete-grid branch separate; no cross-branch
   assumption is used here.
4. Do not treat the report as a promotion or as a C-II closure.
