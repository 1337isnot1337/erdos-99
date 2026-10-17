> Generated reading edition · [exact source](../../../docs/reports/target_c_fs_cyclic_area_perimeter_2026-09-10.md) · source SHA-256 `0976f8438bdac9c46684239eae6548a1887989679b28b114a16f8eff86efa2cf`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-B801CCF87A83","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_fs_cyclic_area_perimeter_2026-09-10.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=48ca95324b34a6ab29bd74b03b6e8363979daccd; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — FS cyclic force-hull area/perimeter inequality

**Date:** 2026-09-10  
**Repository state:** branch `research/c-ii-cyclic-gap-2026-09-10`, based on `a64364e1a3a79370e8c2b342a1fdd6b1f86b66e4`  
**Run type:** closing-proof continuation / convex-geometric transport  
**Target:** Target C, C-II after ZF/FS/FSDB/FSJC/FDJ  
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md`  
**External web search:** not used  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

FS.4 gives more than the central symmetry used in the maximal-perimeter disk theorem.
Every force-hull vertex is `o(D)` from the common radius-`D/2` circle about the
full-source circumcenter. Combining this radial fact with FS.4 reflection symmetry
produces an asymptotically cyclic, centrally symmetric force hull. The resulting
circle-gap algebra gives a new joint area/perimeter constraint:

```math
\boxed{
\liminf_{D\to\infty}
\left(
\frac{\operatorname{area}F}{D^2}
-
\frac{\operatorname{per}F}{D}
+
\frac{3\pi}{4}
\right)\ge0.
}
\tag{CAP.1}
```

Equivalently, if along a subsequence

```math
\frac{\operatorname{per}F}{D}\to p,
\qquad
\frac{\operatorname{area}F}{D^2}\to a,
```

then

```math
\boxed{a\ge p-\frac{3\pi}{4}.}
\tag{CAP.2}
```

The inequality is sharp at the disk and requires no stability theorem.

---

## 1. Exact cyclic lemma

### Lemma CAP.1

Let `Q` be a centrally symmetric convex polygon whose vertices lie on the circle of
radius `1/2` centered at the origin. Then

```math
\boxed{
\operatorname{area}Q
\ge
\operatorname{per}Q-\frac{3\pi}{4}.
}
\tag{1.1}
```

Equality can occur only in the limiting disk case; every finite nondegenerate polygon
has strict inequality.

### Proof

List one representative from each antipodal pair of consecutive circular gaps. Let

```math
\alpha_1,\ldots,\alpha_m>0,
\qquad
\sum_{i=1}^m\alpha_i=\pi.
\tag{1.2}
```

Because the polygon is centrally symmetric, this gap list occurs twice around the
full circle. A chord subtending angle `alpha` on the radius-`1/2` circle has length
`sin(alpha/2)`, while the corresponding oriented triangle from the origin has area
`sin(alpha)/8`. Hence

```math
\operatorname{per}Q
=2\sum_i\sin\frac{\alpha_i}{2},
\tag{1.3}
```

and

```math
\operatorname{area}Q
=\frac14\sum_i\sin\alpha_i.
\tag{1.4}
```

Using (1.2),

```math
\begin{aligned}
4\left(
\operatorname{area}Q-\operatorname{per}Q+\frac{3\pi}{4}
\right)
&=
\sum_i
\left(
3\alpha_i+\sin\alpha_i-8\sin\frac{\alpha_i}{2}
\right).
\end{aligned}
\tag{1.5}
```

Define

```math
f(\alpha)=3\alpha+\sin\alpha-8\sin(\alpha/2).
```

Then `f(0)=0` and

```math
\begin{aligned}
f'(\alpha)
&=3+\cos\alpha-4\cos(\alpha/2)\\
&=2\left(\cos(\alpha/2)-1\right)^2\ge0.
\end{aligned}
\tag{1.6}
```

Thus `f(alpha)>=0` on `[0,pi]`, and it is strictly positive for every `alpha>0`.
Summing (1.5) proves (1.1) and the strict finite-polygon statement. `square`

### Corollary CAP.2 — cyclic compact limits

Let `Q` be a compact convex body which is centrally symmetric about the origin and is
the convex hull of a subset of the radius-`1/2` circle. Then (1.1) still holds.

Indeed the extreme points of `Q` occur in antipodal pairs on the circle. Finite
antipodal subsets of the extreme-point set give centrally symmetric inscribed polygons
converging to `Q` in Hausdorff distance. Planar convex area and perimeter are continuous
under this convergence, so Lemma CAP.1 passes to the limit. `square`

---

## 2. Transport from FS.4 to the actual force hull

Let `F` be the force hull of the relative-interior stress of a post-ZF survivor and let
`o` be the full-source circumcenter from FS.1/FS.4. Put

```math
\eta=3^{1/4}\sqrt D,
\qquad
L_D=\sqrt{D\eta+\eta^2}=o(D).
\tag{2.1}
```

FS.1/FS.4 give, for every force-hull vertex `b`,

```math
\frac D2-\eta
<|p_b-o|<
\frac D2+\eta,
\tag{2.2}
```

and

```math
d_{Haus}(F-o,-(F-o))\le2L_D=o(D).
\tag{2.3}
```

Radially project every force-hull vertex onto the radius-`D/2` circle:

```math
q_b:=\frac D2\frac{p_b-o}{|p_b-o|},
\qquad
Q_D:=\operatorname{conv}\{q_b:b\in B_+\}.
\tag{2.4}
```

Equation (2.2) gives

```math
d_{Haus}(F-o,Q_D)\le\eta=o(D).
\tag{2.5}
```

Consequently

```math
d_{Haus}(Q_D,-Q_D)
\le2\eta+2L_D=o(D).
\tag{2.6}
```

Normalize

```math
\widetilde Q_D=D^{-1}Q_D.
```

Every `widetilde Q_D` lies in the radius-`1/2` disk and is the convex hull of points on
its boundary circle. Take an arbitrary unbounded survivor subsequence and then a
Hausdorff-convergent subsubsequence

```math
\widetilde Q_D\to Q_\infty.
\tag{2.7}
```

Equation (2.6) makes `Q_infty` centrally symmetric. Moreover every exposed extreme
point of `Q_infty` is a limit of support vertices of `widetilde Q_D`, hence lies on the
radius-`1/2` circle. Thus `Q_infty` is the convex hull of a centrally symmetric subset
of that circle, and Corollary CAP.2 gives

```math
\operatorname{area}Q_\infty
\ge
\operatorname{per}Q_\infty-\frac{3\pi}{4}.
\tag{2.8}
```

It remains only to return from the radial projection to `F`. Hausdorff distance
`eta/D->0` gives

```math
\frac{\operatorname{per}F}{D}
-
\operatorname{per}\widetilde Q_D
\to0
\tag{2.9}
```

by Cauchy's support/width formula. The two inclusions associated with (2.5), followed
by Steiner's formula and `per(F),per(Q_D)<=pi D+o(D)`, give

```math
\frac{\operatorname{area}F}{D^2}
-
\operatorname{area}\widetilde Q_D
\to0.
\tag{2.10}
```

Area and perimeter are continuous in (2.7), so (2.8)--(2.10) prove CAP.1 on the
chosen subsequence. Since the original subsequence was arbitrary, CAP.1 holds for every
unbounded post-ZF survivor sequence. `square`

---

## 3. Scope and dependencies

CAP uses only:

1. `docs/reports/target_c_full_source_circumradius_response_2026-09-10.md`, FS.1 and
   FS.4: common full-source circumcenter, force-hull vertex radial bounds, and
   `o(D)` reflection symmetry;
2. elementary circle chord/area formulas;
3. Cauchy's perimeter formula, Steiner's outer parallel-body formula, and standard
   Hausdorff compactness/continuity for planar convex bodies.

It does **not** use:

- a small-isolate assumption;
- a force-bulk population theorem;
- response-operator control beyond FS.4's geometric conclusion;
- a matching or conductance floor;
- Target B shell topology.

The full source population enters exactly through the FS circumcenter/radius theorem.

---

## 4. Exact target implication

FSDB already gives, if

```math
y=\lim h/D,
```

then

```math
\liminf\frac{\operatorname{area}F}{D^2}
\ge
\Phi(y):=\frac{y+\sin y}{4}.
\tag{4.1}
```

CAP adds the independent perimeter-sensitive floor. Therefore, if also

```math
p=\lim\operatorname{per}(F)/D,
```

then

```math
\boxed{
\liminf\frac{\operatorname{area}F}{D^2}
\ge
\max\left\{
\Phi(y),
p-\frac{3\pi}{4}
\right\}.
}
\tag{4.2}
```

This is designed to be inserted into JC **before** replacing the actual perimeter by
`pi D`. The current FSJC scalar optimization discards `p`; CAP makes that discarded
variable carry a matching area cost.

---

## 5. Regression audit

| Regression | Passed? | Exact reason |
| --- | --- | --- |
| regular odd shell | yes | its normalized force hull tends to the radius-`1/2` disk, where CAP is sharp |
| dense isolated shell filling | yes | the radial transport comes from the full source via FS; no core-population saturation is used |
| Reuleaux constant-width limit | yes | FS reflection symmetry makes the cyclic limit centrally symmetric; a non-symmetric constant-width body is outside CAP's derived limit class |
| strict rhombic bulk | yes | CAP uses only force-hull vertex radii and symmetry, not local face angles |
| shell response trace defect | yes | no arbitrary boundary-data response estimate appears |

---

## 6. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| exact cyclic inequality (1.1) | proved | one-variable derivative identity (1.6) |
| extension to cyclic compact limits | proved | antipodal polygon approximation plus area/perimeter continuity |
| actual force-hull CAP.1 | proved under FS.1/FS.4 | radial projection has `o(D)` Hausdorff error and asymptotic reflection symmetry |
| explicit improvement of the `0.588228...` floor | not yet included in this commit | requires the two-variable `y,p` JC optimization using (4.2) |
| Level I | still open | CAP alone does not upper-bound the pinned/contact currency |

---

## 7. Canonical promotion recommendation

**Hold as report pending joint FS-chain promotion.** CAP is proof-complete relative to
FS.1/FS.4. It should be promoted together with the full-source geometric chain if the
subsequent JC optimization materially raises the post-ZF floor.

---

## 8. Next step

Insert (4.2) into the actual-perimeter JC inequality

```math
\frac GD^2
\le
\frac{(t+\min\{y,p-y\})^2}{4\pi}+o(1),
```

retain `p in [y,pi]`, and minimize the resulting exact quadratic threshold in
`lambda=(e_BB+2s_C)/D`. The crossover

```math
\Phi(y)+\frac{3\pi}{4}=2y
```

is the natural candidate minimizer because it is where the CAP area branch and the
maximum two-sided cavity-perimeter branch change simultaneously.
