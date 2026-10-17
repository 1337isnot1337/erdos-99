> Generated reading edition · [exact source](../../../docs/reports/target_c_typeii_aggregate_payment_and_exchange_2026-09-14.md) · source SHA-256 `21dd59a9ca86b88cba2137c462796df6eabba9e2a4ef48a1016bb9c1d57f2b61`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-966C604F8050","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Type-II aggregate payment and inactive-exchange audit

Date: 2026-09-14
Repository commit: ef941ab2b44aa393bdc461926769247b45754202
State version at start: 2026-09-12.audit.46
Run type: closing proof / adversarial audit
Target: C-II / Level I
Starting status: canonical Sections 122–123; Type-II and macroscopic-container branches open
Active prompt: docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md
External literature search: used; no imported theorem
Computation: used; see Section 7

## LEVEL I STATUS

STILL OPEN

This report supplies a finite Type-II aggregate inequality and an exact
inactive-exchange obstruction. Neither produces a strict source-preserving sub-D(n)
competitor, an exact unit equilateral triangle, or a global-optimality disproof.

## 1. Starting canonical endpoint

The selected route was the full-core C-II branch. The canonical endpoint was

```math
 \liminf_{D\to\infty}\frac1D\sum_r
 (L_r+P_{{\rm exc},r}-2d_r)
 \ge c_{\rm det},\qquad
 c_{\rm det}:=\frac\pi2(2-\sqrt3),
 \tag{1.1}
```

from C-AGGREGATE-TWO-ARC-DETOUR, together with

```math
 \sum_rP_{{\rm exc},r}\le10(e_{BB}-k),
 \qquad k=d_H+s_Z,
 \tag{1.2}
```

from C-AUGMENTED-CELL-DEFECT-BUDGET. The exact residual was
$`\sum_r(L_r-2d_r)`$.

The attempted chain was

    near-disk loaded-side localization
        -> correlated aggregate payment
        -> contradiction or a source-level strict deformation
        -> Level I

The last implication remains unavailable.

## 2. Strongest genuinely new result

Classification: audited-working; not admitted as a canonical premise in this run.

The proof below repairs a broader proof-only aggregate-payment formulation by making
explicit the hypothesis it needs: absence of loaded-loaded interior chords. The
near-disk lemma proves that hypothesis in the canonical Type-II branch. All local
walks count edge occurrences with multiplicity, and all source points, including
contact-isolated points, remain in the global source.

### Theorem 2.1 — Type-II correlated aggregate payment

Let A be a contact-minimal, then diameter-pair-minimal, triangle-free global
minimizer in the canonical post-ZF C-II normal form. Assume it is in the full-core
near-disk Type-II branch and D=diam(A) is sufficiently large. For every unloaded
positive-contact component I_r define:

- A_r subset B, a_r=|A_r|, P_r=conv(A_r), and d_r=diam(P_r);
- L_r as the occurrence-counted outer-face walk length of the induced graph on
  I_r union A_r;
- P_exc,r as the total degree of bounded nonquadrilateral faces;
- T_r and Q_r^+ as the Section-123 triangular count and augmented degree excess;
- d_tile >= 0 as the Section-123 polygon-dissection deficit;
- C_partial as the total number of actual loaded-loaded contacts that are sides of
  attachment polygons; and
- M_miss >= 0 as the missing-side route defect defined in (2.8).

Then

```math
\boxed{\sum_r(L_r+P_{{\rm exc},r}-2a_r)
\le 10(e_{BB}-k-d_{\rm tile})
-4M_{\rm miss}-6C_\partial.}
\tag{2.1}
```

Consequently,

```math
\boxed{\sum_r(L_r+P_{{\rm exc},r}-2d_r)
\le 10(e_{BB}-k-d_{\rm tile})
\;+\;2\sum_r(a_r-d_r)-4M_{\rm miss}-6C_\partial.}
\tag{2.2}
```

Thus the canonical lower bound (1.1) implies only the necessary condition

```math
\boxed{\liminf_{D\to\infty}\frac1D
\left[10(e_{BB}-k-d_{\rm tile})
\;+\;2\sum_r(a_r-d_r)-4M_{\rm miss}-6C_\partial\right]
\ge c_{\rm det}.}
\tag{2.3}
```

No sign or smallness statement for the residual
$`\sum_r(a_r-d_r)`$ has been proved.

### 2.1 Near-disk localization of loaded contacts

Let F=conv(B) be the loaded force hull. Canonical C-FULLCORE-NEAR-DISK gives
$`d_H(F,B(o_D,D/2))=o(D)`$. After translating, put R=D/2, choose
$`\delta=o(D)`$, $`r=R-\delta`$, and $`R_+=R+\delta`$. Support functions give

```math
B(0,r)\subset F\subset B(0,R_+). \tag{2.4}
```

For a boundary point x and outward unit normal u,
$`u\cdot x=h_F(u)\ge r`$ and $`|x|\le R_+`$. Therefore the normal and radial
directions differ by at most
$`\beta=\arccos(r/R_+)=o(1)`$.

If boundary vertices p,q satisfy $`|p-q|=1`$, their smaller radial angular
separation satisfies

```math
1\ge2r\sin(\gamma/2),\qquad
\gamma\le2\arcsin(1/(2r))=o(1). \tag{2.5}
```

Indeed, writing $`p=a e`$, $`q=b f`$, with $`a,b\ge r`$, the case
$`e\cdot f<0`$ already gives $`|p-q|^2\ge2r^2>1`$ for large D. In the
remaining case,
```math
|p-q|^2=(a-b)^2+2ab(1-e\cdot f)
\ge4r^2\sin^2(\gamma/2).
```

Along the short polar arc from p to q, every side direction lies in an interval
of width
$`\tau=2\beta+2\arcsin(1/(2r))=o(1)`$. If p and q were nonconsecutive, the
arc would contain at least two side vectors $`v_i`$. Let
$`w=(q-p)/|q-p|`$. Since the sum of vectors in a cone of width $`\tau<\pi/2`$
stays in that cone, every $`v_i`$ makes angle at most $`\tau`$ with $`w`$.
Projection onto $`w`$ gives

```math
1=|q-p|=w\cdot(q-p)
\ge \sum_i |v_i|\cos(\tau)
\ge2\cos(\tau)>1,
\tag{2.6}
```

a contradiction. Hence every unit chord between loaded hull vertices is a hull side,
and the Section-63 slack satisfies

```math
\boxed{c_B=0,\qquad e_{BB}=q-m.} \tag{2.7}
```

In particular, any loaded-loaded unit contact inside A_r is a side of P_r: the
global hull side has no loaded vertex, and therefore no attachment vertex, between
its endpoints.

### 2.2 Cellwise augmented ledger

Fix r. Form J_r^+ from the internal and attachment contacts on I_r union A_r by
omitting loaded-loaded contacts and adding all sides of P_r. Let c_r^partial be
the number of actual loaded contacts that are sides of P_r, and set
$`h_r=a_r-c_r^\partial`$. By (2.7), J_r^+ has no loaded-loaded interior chords.

Partition its bounded degree excess as

```math
Q_r^+=Q_{M,r}+Q_{C,r}+Q_{I,r}, \tag{2.8}
```

according as a face is side-adjacent to a missing polygon side, side-adjacent to an
actual contact side, or is any other bounded face. Define

```math
M_r:=h_r-T_r+Q_{M,r}\ge0. \tag{2.9}
```

Every bounded triangular face uses a polygon side because the source is
triangle-free. A triangle using two polygon sides would require the third edge
to be a loaded interior chord, unless the attachment polygon itself is a
triangle; in the latter case the three polygon sides bound the outer face, not
a bounded face. The former possibility is excluded by (2.7). A contact polygon
side cannot bound a triangle using one polygon side, since its two other unit
edges would form an exact unit equilateral triangle. Thus every bounded triangle
is on a missing side, so $`T_r\le h_r`$, proving the inequality in (2.9).

A missing-side face of degree m has old route length m-1. Its contribution to
$`L_r-2a_r`$ is m-3, namely 0 for a triangle, 1 for a quadrilateral, and
1+(m-4) for m at least 5. A contact side contributes -1. Therefore

```math
L_r-2a_r=M_r-c_r^\partial. \tag{2.10}
```

There are no loaded interior chords. On deleting missing polygon sides, precisely
the missing-side faces leave the bounded-face set, so the actual bounded
nonquadrilateral excess is

```math
Q_r=Q_{C,r}+Q_{I,r}. \tag{2.11}
```

If f_r is the number of actual bounded nonquadrilateral faces, then
$`P_{{\rm exc},r}=4f_r+Q_r`$, $`f_r\le Q_r`$, and

```math
P_{{\rm exc},r}\le5(Q_{C,r}+Q_{I,r}). \tag{2.12}
```

The exact Section-123 defect is $`X_r=a_r-T_r+Q_r^+`$, and (2.8)–(2.9) give
$`X_r=M_r+c_r^\partial+Q_{C,r}+Q_{I,r}`$. Consequently

```math
\begin{aligned}
L_r+P_{{\rm exc},r}-2a_r
&\le M_r-c_r^\partial+5(Q_{C,r}+Q_{I,r})\\
&=5X_r-4M_r-6c_r^\partial.
\end{aligned}
\tag{2.13}
```

This finite inequality does not identify outer-walk occurrences from different cells.

### 2.3 Globalization and obstruction

Canonical Section 123 gives the exact identity

```math
e_{BB}-k=\frac12\sum_rX_r+d_{\rm tile}. \tag{2.14}
```

Summing (2.13), putting $`M_{\rm miss}=\sum_rM_r`$ and
$`C_\partial=\sum_rc_r^\partial`$, proves (2.1). Adding
$`2\sum_r(a_r-d_r)`$ proves (2.2), and (1.1) proves (2.3).

This does not close C-II. Current area saturation does not bound
$`\sum_r(a_r-d_r)`$ with a sufficiently small coefficient; the loaded-hull scalar
and the three negative credits have no proved joint sign that contradicts (2.3).
No source-preserving deformation follows from this accounting.

## 3. Exact inactive-chamber exchange obstruction

This is a separate finite result for the macroscopic-container branch.

### Theorem 3.1 — strict finite exchange saturation

Let A be a triangle-free contact-minimal global n-point minimizer, let
K=conv(A), let Z be contact-isolated source points, and let v not in Z be
nonisolated. If $`Y\subset K`$ obeys

```math
|Y|=|Z|+1,\qquad |y-y'|>1\ (y\ne y'),\qquad
|y-x|>1\quad
(y\in Y,\ x\in A\setminus(Z\cup\{v\})), \tag{3.1}
```

then such a Y cannot exist.

Proof. Replace $`Z\cup\{v\}`$ by Y. The cardinality is unchanged, retained old
pairs stay separated, and (3.1) handles every new pair. All points remain in K,
so the new diameter is at most D(n); the definition of D(n) forces equality.
The deleted isolates remove no contact, v removes at least one, and Y creates none.
The new contact graph remains triangle-free, so contact minimality is contradicted.
$`\square`$

### Theorem 3.2 — loaded lexicographic companion

Assume in Theorem 3.1 that K has nonempty interior, v is incident to a diameter
pair, and $`Y\subset\operatorname{int}K`$ has the same cardinality as
$`Z\cup\{v\}`$. Suppose the replacement is unit-separated and triangle-free, and
let c_new be the number of new unit contacts incident to Y. If

```math
c_{\rm new}\le d_C(v), \tag{3.2}
```

then the replacement is impossible.

Proof. If the inequality is strict, contact minimality is contradicted. At equality,
contact count is unchanged. For $`y\in\operatorname{int}K`$ and $`x\in K`$, one has
$`|y-x|<D(n)`$: otherwise y lies on the boundary circle of the disk
$`\overline B(x,D(n))`$, while a neighborhood of y lies in
$`K\subset\overline B(x,D(n))`$. Thus new points create no diameter pairs, while
deleting v removes a diameter pair. Diameter-pair minimality is contradicted.
$`\square`$

For an actual internal convex inactive chamber C, write
$`C_{-1}=\{x\in C:\operatorname{dist}(x,\partial C)>1\}`$.
Every point of $`C_{-1}`$ is more than unit distance from source points outside the
chamber's assigned isolate set. Hence Theorem 3.1 gives the exact finite no-go: no
protected strict k to k+1 exchange exists entirely in $`C_{-1}`$. The loaded
companion gives the contact-budget analogue after deleting a loaded point. Both
statements preserve source cardinality and retain all isolates; neither constructs
a replacement.

## 4. Frontier effect and remaining obligations

The repaired Type-II theorem reduces the aggregate route target to the exact positive
currencies $`e_{BB}-k`$ and $`\sum_r(a_r-d_r)`$, after explicit dissection, missing-side,
and attachment-contact credits. It is a bookkeeping advance, not a Level-I closure.

The remaining obligations are:

1. Prove an upper bound for (2.3) below $`c_{\rm det}`$, or turn its residual into a
   finite source-preserving strict diameter decrease, or force an exact unit triangle.
2. In the macroscopic internal chamber or exterior-cap branch, construct a protected
   finite exchange with the exact deleted-core contact budget, or prove a global
   contradiction. The exterior cap is not covered by the inner-body no-go.

No asymptotic conclusion here supplies a uniform threshold for every n and every
global minimizer.

## 5. Compact proof-obligation ledger

| Claim | Status | Dependencies | Decisive reason |
| --- | --- | --- | --- |
| Near-disk unit loaded chord is a hull side | audited-working | C-FULLCORE-NEAR-DISK; convex support geometry | finite angular-width argument (2.4)–(2.6) |
| Type-II c_B=0 and no attachment-cell interior loaded chord | audited-working | preceding claim; C-LOADED-HULL | all loaded unit contacts are global hull sides |
| Local identities (2.10)–(2.13) | audited-working | C-AUGMENTED-CELL-DEFECT-BUDGET; no interior chord | exact face/route occurrence count |
| Global payment (2.1)–(2.3) | audited-working | preceding line; Section-123 identity | exact summation, no cross-cell occurrence injection |
| Strict finite exchange obstruction | audited-working | global and contact minimality | same cardinality, unit separation, diameter, contact count |
| Loaded lexicographic companion | audited-working | contact-/diameter-pair-minimal normal form | interior replacements create no diameter pairs |
| Type-II closure from (2.3) | rejected | none | no proved sign for loaded and attachment currencies |
| Near-unit pair creation implies positive KKT support | rejected | C-INACTIVE-DEEP-MATCHING only | protected contact creation can be zero-stress |

Canonical trusted inputs are C-FULLCORE-NEAR-DISK, C-LOADED-HULL,
C-HARMONIC-CELL-TILING, and C-AUGMENTED-CELL-DEFECT-BUDGET, with exactly the
hypotheses stated in their manifest entries. Theorems 2.1, 3.1, and 3.2 are not
canonical because this run did not mutate the manifest.

## 6. Regression checks and computation

The following exact checks were run:

    python3 research/verify_target_c_anisotropic_two_arc_return_120.py
    python3 research/verify_target_c_local_return_oler_121.py
    python3 research/verify_target_c_protected_contact_creation.py
    python3 research/verify_target_c_scalar_ledger_compatibility.py

Certified relevant output:

    universal_constant=0.5358983848622456
    uniform_direction_average=1.4535209105296745
    withdrawn implication G=o(D^2) => G/d=o(1): FALSE
    Exact finite motion checks passed. No global-optimality claim.
    PASS: exact pinned, loaded-hull, and outerplanar scalar ledgers
    PASS: local and aggregate Section-122 demands hold with rational margins

The scalar script is an abstract ledger witness, not a planar packing or global
minimizer. The finite-motion script is a protected-contact regression, not a strict
diameter decrease. The pre-existing 2026-09-14 vanishing-shear report and its
nearchain computation were preserved and audited as regressions, not used as
global-minimizer evidence.

The mandatory regressions also pass at the scope used here: bridges and repeated
outer-walk vertices are retained by occurrence counting; contact-isolated points are
never silently removed; the rejected Euler-path, FB4, C53, RSR uniqueness, five-host,
Reuleaux-cap, withdrawn sharpness, full-source-ZRF, PR #191, and finite-S1 claims are
not used as premises.

## 7. Literature imports

No external theorem is used in the proof. A targeted search found the problem still
listed as open and related distance-multiplicity work, but no theorem with the
required “every sufficiently large n, every global minimizer” bridge. These are
near misses and are not dependencies.

## 8. Corrections and disposition

The proof-only all-regime aggregate-payment proposal was not adopted in its broad
form. Without the Type-II no-interior-chord hypothesis, an interior loaded chord can
split a missing-side augmented face, so its degree excess cannot automatically be
discarded from the actual bounded-face ledger. The repaired theorem above is
restricted to Type II, where the near-disk lemma proves c_B=0.

Promotion recommendation: audited-working for Theorems 2.1, 3.1, and 3.2; no
canonical manifest mutation in this run. The existing local artifact-index change,
vanishing-shear report, and scalar verification script were preserved.

## 9. Handoff

1. Strongest result: the repaired Type-II payment (2.1)–(2.3), with exact credits.
2. Dependency chain: C-FULLCORE-NEAR-DISK + C-LOADED-HULL +
   C-HARMONIC-CELL-TILING + C-AUGMENTED-CELL-DEFECT-BUDGET -> Theorem 2.1;
   global lexicographic minimality -> Theorems 3.1–3.2.
3. Exact remaining lemma: bound $`e_{BB}-k+\sum_r(a_r-d_r)`$ below the Section-122
   demand after credits, or construct a strict source-preserving competitor; also
   close the internal/exterior macroscopic-container branch.
4. Binding dead routes: density-only loss, scalar ledger elimination, local KKT
   activation, whole outer-walk geodesicity, and full-source ZR/ZF extension.
5. Next files: docs/targets/target-c/CURRENT.md, canonical Sections 122–123, and
   research/target_c_section122_finite_exchange_saturation.md.
