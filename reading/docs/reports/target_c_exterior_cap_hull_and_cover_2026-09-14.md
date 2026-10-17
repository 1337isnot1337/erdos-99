> Generated reading edition · [exact source](../../../docs/reports/target_c_exterior_cap_hull_and_cover_2026-09-14.md) · source SHA-256 `819776a9132762e4d1fecbfef0b02e5f052babb11d1cd92d6e94703ac59995f1`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-7A36875D1E94","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — exterior-cap source-hull stability and covering

**Date:** 2026-09-14
**Repository commit:** `ef941ab2b44aa393bdc461926769247b45754202`
**State version:** `2026-09-12.audit.46`
**Run type:** closing proof / adversarial audit
**Target:** C-II / macroscopic-container branch
**Starting status:** canonical global container/full-core dichotomy; proof-only internal
chamber hull stability
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md`
**External literature search:** used earlier in this run; no imported theorem
**Computation:** used earlier in this run; no script is logically required here

## LEVEL I STATUS

`STILL OPEN`

This report extends the source-specific convex-hull stability argument from an internal
inactive chamber to an actual exterior cap. It also records the exact finite covering
consequence of contact minimality. Neither result produces a unit equilateral triangle
or a strict same-cardinality sub-diameter competitor.

## 1. Starting canonical endpoint

Canonical `C-FULLCORE-NEAR-DISK` and `C-INACTIVE-DICHOTOMY` give the following
macroscopic exterior-cap alternative. Along a survivor sequence there may be a convex
cap (C_*subset K\setminus\operatorname{int}F), where (K=\operatorname{conv}A) is
the full source hull and (F) is the positive-contact force hull, with its assigned
external source set

```math
S_*:=A\cap(C_*\setminus F),
\qquad z_*:=|S_*|,
```

satisfying, for fixed constants (alpha,P_0,L_0>0),

```math
\operatorname{area}C_*\ge\alpha D^2,
\qquad
\operatorname{per}C_*\le P_0D,
\qquad
a_0z_*\ge\operatorname{area}C_*-L_0D,
\tag{EC.1}
```

where (a_0=\sqrt3/2). The cap has diameter at most (D), and every point in
(S_*) is a retained contact-isolated source point. The chord boundary in (F) is
not treated as an additional source population.

The intended chain was

```text
quadratic exterior cap + boundary-order Oler slack
    -> source-specific cap filling and protected source population
    -> finite exchange or exact triangle
    -> C-II / Level I
```

The first arrow is proved below. The second remains open.

## 2. Exterior-cap source-hull stability

### Theorem EC.1

Let (C) be a compact convex planar body with

```math
\operatorname{diam}C\le D,
\qquad
\operatorname{area}C\ge\alpha D^2,
\qquad
\operatorname{per}C\le P_0D,
\tag{EC.2}
```

for fixed (alpha,P_0>0). Let (S\subset C) be unit-separated and suppose

```math
a_0|S|\ge\operatorname{area}C-L_0D
\tag{EC.3}
```

for fixed (L_0\ge0). Put (H=\operatorname{conv}S). Then there are constants

```math
\kappa=\alpha/P_0>0,
\qquad
M=L_0+\frac{\sqrt3}{4}P_0+a_0,
\qquad
C_0=\sqrt{M/\kappa},
\tag{EC.4}
```

such that, for all sufficiently large (D),

```math
\boxed{\operatorname{area}C-\operatorname{area}H\le MD,}
\tag{EC.5}
```

```math
\boxed{d_H(C,H)\le C_0\sqrt D,}
\tag{EC.6}
```

and, if (o) is a center of an inball of (C),

```math
\boxed{B(o,\kappa D-C_0\sqrt D)\subset H\subset C.}
\tag{EC.7}
```

### Proof

Let (r(C)) be the inradius. For a convex body, inner-parallel coarea and perimeter
monotonicity give

```math
\operatorname{area}C
=\int_0^{r(C)}\operatorname{per}(C_{-t})\,dt
\le r(C)\operatorname{per}C.
```

Thus (r(C)\ge\operatorname{area}C/\operatorname{per}C\ge\kappa D).

Apply Oler’s finite inequality to (S\subset H):

```math
a_0|S|\le\operatorname{area}H+\frac{\sqrt3}{4}\operatorname{per}H+a_0.
```

Since (H\subset C) and convex perimeter is monotone,

```math
\operatorname{area}C-\operatorname{area}H
\le (L_0+\tfrac{\sqrt3}{4}P_0)D+a_0
\le MD
\tag{EC.8}
```

for (D\ge1).

Fix a unit vector (u), and write (t=h_C(u)-h_H(u)). Choose an inball
(B(o,r)\subset C), a support point (v\in C), and a unit vector (w\perp u).
The triangle with vertices (v,o+rw,o-rw) lies in (C). If

```math
0\le s\le\min\{t,r\},
```

its support cap of depth (s) has area at least (rs^2/D): the altitude from
(o) to the support line is at most (|v-o|\le D). The cap is disjoint from (H),
so

```math
\operatorname{area}(C\setminus H)\ge (r/D)s^2.
\tag{EC.9}
```

For large (D), (t>r) would give an (Omega(D^2)) lower bound in (EC.9),
contradicting (EC.8). Hence (t\le r), and choosing (s=t) gives

```math
t^2\le (D/r)MD\le (M/\kappa)D.
```

Taking the supremum over (u) gives (EC.6). The support inequality

```math
h_H(u)\ge u\cdot o+r-C_0\sqrt D
```

for every (u) is exactly the inclusion (EC.7). This proves the theorem. $`\square`$

The proof is finite once (D) is beyond the explicit contradiction threshold

```math
D> M/\kappa^3,
```

and uses no limiting subsequence or unstated equality case.

## 3. Application to a macroscopic exterior cap

Apply Theorem EC.1 to the cap (C_*) and actual external source set (S_*) in
(EC.1). Then its external-isolate hull (H_*:=\operatorname{conv}S_*) satisfies

```math
\boxed{
\operatorname{area}C_*-\operatorname{area}H_*=O(D),
\qquad
d_H(C_*,H_*)=O(\sqrt D),
}
\tag{EC.10}
```

and (H_*) contains a disk of radius (kappa D-O(\sqrt D)). Every extreme point
of (H_*) is an actual source point from (S_*), hence remains contact-isolated in
the canonical representative. No point of the full source is removed or reclassified.

This is the exterior analogue of proof-only Section 86’s internal-chamber conclusion.
The cap population cannot be a boundary arc or a spatially diffuse cloud while retaining
the Section-80 (O(D)) capacity deficit.

## 4. Exact cap covering from contact minimality

The hull-stability theorem is not the only source-level consequence. The same finite
exchange argument used for an internal chamber gives a covering statement for a cap.

### Theorem EC.2

Let (A) be a contact-minimal triangle-free global (n)-point minimizer with a
nonempty nonisolated contact graph. Let (Csubset\operatorname{conv}A) be convex, and
let (S=A\cap\operatorname{int}C). Assume every nonisolated source vertex lies outside
(\operatorname{int}C). Then

```math
\boxed{
C_{-1}\subseteq\bigcup_{s\in S}\overline B(s,1).
}
\tag{EC.11}
```

Here (C_{-1}=\{x\in C:\operatorname{dist}(x,\partial C)>1\}). The statement allows
source points on (\partial C), and it retains all source points in the comparison.

### Proof

Choose a nonisolated source vertex (v). Suppose (x\in C_{-1}) is farther than one
from every (s\in S). Every source (a\notin\operatorname{int}C) lies on the other
side of the boundary from the interior point (x), or on (\partial C). The segment
([x,a]) meets (\partial C), so

```math
|x-a|\ge\operatorname{dist}(x,\partial C)>1.
```

In particular (x) is strictly farther than one from every source point other than
possibly (v); but (v\notin\operatorname{int}C) by hypothesis, so it too is farther
than one. Delete (v) and insert (x). The resulting source has the same cardinality,
is unit-separated, lies in the old source hull, and has diameter at most (D(n)). It
therefore has diameter exactly (D(n)), while it creates no unit contact and deletes
at least one. It is triangle-free, contradicting contact minimality. Hence (EC.11).
$`\square`$

For the canonical exterior cap, all positive-core vertices and all source points outside
the cap lie outside its interior. Therefore EC.2 applies to every actual cap, with
(S=S_*) (up to assigning any source point on a closing chord to the force hull).

## 5. Exact obstruction: the conclusions are jointly compatible with strict packing

The two conclusions do not force a spare strict site. Here is an exact family that
also supplies a hostile check on any attempted cap closure from EC.10--EC.11.

For (m\ge2), choose two vectors (u,v) of equal length

```math
s_m=1+1/m
```

meeting at (60^\circ). Let

```math
C_m=\operatorname{conv}\{iu+jv:0\le i,j\le m\},
\qquad
S_m=\{iu+jv:0\le i,j\le m\}.
```

The index cells split into equilateral triangles of side (s_m). Every nonzero
lattice difference has length at least (s_m>1), so (S_m) is strictly unit-separated,
contact-free, and triangle-free. The circumradius of every cell is

```math
\frac{s_m}{\sqrt3}<1
```

for (m\ge2), so the closed parallelogram (C_m) is covered by the open unit disks
centered at (S_m). In particular no point of (C_m) is strictly farther than one
from all members of (S_m), even before taking the one-unit erosion.

The exact population and capacity data are

```math
|S_m|=(m+1)^2,
\qquad
\frac{\operatorname{area}C_m}{a_0}=m^2s_m^2=(m+1)^2,
\tag{EC.12}
```

```math
\operatorname{per}C_m=4ms_m=4(m+1),
\qquad
\operatorname{diam}C_m=\sqrt3\,ms_m=\sqrt3(m+1),
\tag{EC.13}
```

and hence the isolate-only Oler slack is exactly

```math
\frac{\operatorname{area}C_m}{a_0}
 +\frac{\operatorname{per}C_m}{2}+1-|S_m|
=2(m+1)+1=O(\operatorname{diam}C_m).
\tag{EC.14}
```

Moreover (H_m=\operatorname{conv}S_m=C_m), so the Hausdorff error in EC.10 is
zero while the inradius is linear in the diameter. Nevertheless there is no strict
(S_m\to S_m+1) insertion anywhere in (C_m).

This is a fixed-container regression, not a global-minimality counterexample. It shows
that source-hull stability, exact erosion covering, near-unit matching, and (O(D))
Oler slack do not by themselves supply the protected exchange required by the C-II
branch. The missing hypothesis must couple the external cap to the actual diameter
minimization problem, not merely to its local capacity data.

## 6. Exact frontier effect

The macroscopic-container branch is sharpened as follows:

```text
quadratic cap population + O(D) cap perimeter/slack
    -> actual isolate hull fills the cap to O(sqrt(D)) support error
    -> cap one-unit erosion is exactly covered by actual isolates
    -> no diffuse-cap or simple-hole escape remains
    -> protected strict exchange / core reconfiguration is still missing.
```

This does not alter `docs/state/theorem-state.yaml`. No canonical promotion is claimed
in this run.

## 7. Claim audit table

| Claim | Status | Dependencies | Reason |
| --- | --- | --- | --- |
| EC.1 exterior-cap hypotheses | canonical | `C-INACTIVE-DICHOTOMY`, `C-FULLCORE-NEAR-DISK` | exact cap area/perimeter/population scope |
| EC.1 hull stability | audited-working candidate | Oler and elementary convex geometry | finite support-cap proof |
| EC.2 erosion covering | audited-working candidate | contact-minimal global representative | exact one-point exchange |
| EC.10 source-specific cap filling | conditional on EC.1 hypotheses | EC.1 | applies to actual cap isolates |
| EC.12--EC.14 regression | exact regression | elementary triangular geometry | no global-optimality claim |
| cap conclusions imply C-II closure | rejected | EC.1--EC.2 plus regression | strict insertion can be absent |

## 8. Regressions and hostile checks

- Contact-isolated points are retained in (S_*); none are deleted in EC.1 or EC.2.
- The cap closing chord is not counted as an external source point.
- EC.2 uses strict distance (>1), as required by the contact-minimal exchange; closed
  unit covering alone is insufficient for a contradiction.
- The cap source set can have zero unit contacts, so no KKT positivity or force transfer
  is inferred.
- The exact strained triangular patch in Section 5 has a strict covering margin and
  therefore defeats any purported spare-site lemma based only on capacity and filling.
- The internal-frame activation regression remains a stronger co-embedded check when a
  unit-contact boundary and a fixed diameter-carrying core are required.

## 9. Exact remaining implication

For an actual macroscopic exterior cap, prove at least one of:

1. a strict source-preserving exchange that moves or replaces part of the old
   diameter-carrying core;
2. a global diameter comparison showing that a cap-filling strained triangular patch
   cannot be optimal at the source cardinality; or
3. an exact unit triangle forced by the cap/core diameter geometry.

The current theorem does not establish any of these.

## 10. Promotion recommendation

**audited-working** for the two finite statements after an independent check; do not
promote without adding explicit theorem IDs and a route-map entry. Theorem-state remains
unchanged because the final global-minimality bridge is absent.

## 11. Handoff

1. Strongest new result: EC.1--EC.2, actual exterior-isolate hull stability plus exact
   one-unit-erosion covering.
2. Canonical chain: `C-INACTIVE-DICHOTOMY` + `C-FULLCORE-NEAR-DISK` -> EC.1/EC.2.
3. Exact remaining lemma: a cap/core source-preserving strict exchange or global
   diameter comparison.
4. Binding dead route: density/filling/activation alone, defeated by EC.12--EC.14 and
   the co-embedded frame regression.
5. Next files: `docs/targets/target-c/CURRENT.md`, Sections 120--123, and the Target-A
   current endpoint if route switching is attempted.
