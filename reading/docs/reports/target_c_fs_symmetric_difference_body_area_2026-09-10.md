> Generated reading edition · [exact source](../../../docs/reports/target_c_fs_symmetric_difference_body_area_2026-09-10.md) · source SHA-256 `37534b37bdcb8ee81ee49bce0cdaaf20c0d9854addc88cb5b40eeb21f2ca3bf9`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-0E3494E82B46","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_fs_symmetric_difference_body_area_2026-09-10.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=4dfe22b7c6b2ad3657bed736353e3bc27d1065b0; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — FS symmetry upgrades the post-ZF force-hull area floor

**Date:** 2026-09-10  
**Repository state:** `3f37ef0eab4407a411f9a6d51d016ba600302be7` at start  
**Run type:** closing proof / dependency synthesis / adversarial audit  
**Target:** Target C, C-II after ZF  
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md`  
**External web search:** not used in this theorem  
**Computation:** decimal evaluation only; no computation is a proof dependency

## LEVEL I STATUS

`STILL OPEN`

The September 10 full-source theorem FS.4 gives a fact that was not available to the
September 9 difference-body argument: the actual relative-interior force hull is
Hausdorff-close to its reflection through the **full-source circumcenter**.  This turns
the difference-body polygon back into the force hull with asymptotic factor `1/4`,
rather than the general Rogers--Shephard factor `1/6`.

For every unbounded post-ZF survivor sequence,

```math
\boxed{
\liminf_{D\to\infty}\frac{\operatorname{area}F}{D^2}
\ge
A_{FS}:=
\frac{2\rho+\sin(2\rho)}4
=0.6184708847696858\ldots,
}
\tag{FSDB.1}
```

where `rho` is the positive solution of

```math
\rho=\cos\rho
\qquad
(\rho=0.7390851332151606\ldots).
\tag{FSDB.2}
```

The previous best universal post-ZF force-hull area floor in the report stack was

```math
\frac12\sin(2\rho)=0.497856636324211\ldots
```

from the projective-circle theorem PI.  The new bound is strictly stronger.  It does
not itself settle Level I; regular odd shells satisfy an even larger normalized area.

---

## 1. Starting endpoint

Let the hypothetical triangle-free global source be chosen first to minimize unit
contacts and then diameter pairs, as in the promoted C-I restoration.  In the audited
post-ZF branch let

- `F` be the force hull of the relative-interior normalized KKT stress;
- `H` be the full actual diameter graph;
- `h=|E(H)|`;
- `D` be the source diameter.

The September 9 difference-body theorem DB defines

```math
P_H:=D\,\operatorname{conv}\{\pm u_e:e\in E(H)\},
\tag{1.1}
```

where `u_e` is a unit vector along the projective direction of diameter edge `e`, and
proves `P_H\subseteq F-F`.  Using only the planar Rogers--Shephard inequality gives a
factor `1/6` in area.  PI instead used a single well-separated pair of diameter chords
and obtained the stronger constant `0.497856...`.

The new implication is

```text
FS.4 approximate central symmetry of F
    + complete diameter-direction polygon P_H subset F-F
    -> (1/2) P_H lies within o(D) of F
    -> area(F) >= area(P_H)/4-o(D^2)
    + DB h/D >= 2 rho
    -> area(F)/D^2 >= (2 rho+sin(2 rho))/4-o(1).
```

---

## 2. Strongest genuinely new audited theorem

Put

```math
\eta=3^{1/4}\sqrt D,
\qquad
L_D=\sqrt{D\eta+\eta^2},
\tag{2.1}
```

as in FS.4, and put

```math
\delta_D=2\arcsin\frac1{2D}.
\tag{2.2}
```

### Theorem FSDB — finite symmetric difference-body area bound

Every post-ZF survivor for which the September 10 FS.4 theorem and the audited C67
diameter-direction separation apply satisfies

```math
\boxed{
\begin{aligned}
\operatorname{area}F
\ge{}&
\frac{D^2}{4}
\left[
(h-1)\sin\delta_D
+
\sin\bigl((h-1)\delta_D\bigr)
\right]\\
&-\pi D L_D-\pi L_D^2.
\end{aligned}
}
\tag{FSDB.3}
```

Consequently, after inserting DB's

```math
\liminf h/D\ge2\rho,
\tag{2.3}
```

one obtains FSDB.1.

### Scope

FSDB concerns the force hull of the relative-interior stress of the lexicographically
normalized C-II source.  It retains every contact-isolated source point.  The isolates
enter indirectly through FS.4, because the common circumcenter and its radius estimate
come from the full source hull.  No small-isolate or force-bulk hypothesis is used.

The theorem is asymptotic only in its constant form FSDB.1.  The finite statement
FSDB.3 is exact under the cited finite inputs.

### Proof

Translate by the full-source circumcenter `o` from FS.4 and write

```math
F_0:=F-o.
```

FS.4 gives

```math
d_{\rm Haus}(F_0,-F_0)\le2L_D.
\tag{2.4}
```

Hence

```math
-F_0\subseteq F_0+2L_DB_2,
\tag{2.5}
```

where `B_2` is the closed unit Euclidean disk.  Therefore

```math
\begin{aligned}
\frac12(F_0-F_0)
&=\frac12(F_0+(-F_0))\\
&\subseteq
\frac12(F_0+F_0+2L_DB_2)\\
&=F_0+L_DB_2,
\end{aligned}
\tag{2.6}
```

using convexity of `F_0`, so `F_0+F_0=2F_0`.

Every diameter vector `\pm Du_e` is a difference of two force-hull vertices.  Thus DB's
polygon satisfies

```math
P_H\subseteq F_0-F_0.
\tag{2.7}
```

Combining (2.6) and (2.7),

```math
\boxed{\frac12P_H\subseteq F_0+L_DB_2.}
\tag{2.8}
```

Area monotonicity and Steiner's formula now give

```math
\frac14\operatorname{area}(P_H)
\le
\operatorname{area}(F+L_DB_2)
=
\operatorname{area}F+L_D\operatorname{per}F+\pi L_D^2.
\tag{2.9}
```

Since `diam(F)=D`, Cauchy's perimeter--diameter inequality gives

```math
\operatorname{per}F\le\pi D.
\tag{2.10}
```

It remains to evaluate `area(P_H)`.  Order the `h` projective diameter directions
cyclically on the projective circle of circumference `pi`, and let their gaps be

```math
g_1,\ldots,g_h,
\qquad
\sum_i g_i=\pi.
\tag{2.11}
```

C67 gives

```math
g_i\ge\delta_D.
\tag{2.12}
```

The vertices of `P_H` are the `2h` points `\pm Du_e` on the circle of radius `D`.
The projective gap list occurs twice around the Euclidean circle.  The signed area
formula for an inscribed polygon therefore gives the exact identity

```math
\boxed{
\operatorname{area}(P_H)
=D^2\sum_{i=1}^h\sin g_i.
}
\tag{2.13}
```

The function `sin` is concave on `[0,pi]`.  Under `g_i>=delta_D` and fixed sum `pi`,
its sum is minimized at an extreme point of the feasible simplex: all but one gaps
are equal to `delta_D`.  Equivalently one may transfer mass between any two gaps
until one reaches the lower bound; concavity never increases the sum.  Hence

```math
\begin{aligned}
\sum_i\sin g_i
&\ge
(h-1)\sin\delta_D
+
\sin\bigl(\pi-(h-1)\delta_D\bigr)\\
&=
(h-1)\sin\delta_D
+
\sin\bigl((h-1)\delta_D\bigr).
\end{aligned}
\tag{2.14}
```

Substitute (2.13)--(2.14) into (2.9) and use (2.10).  This proves FSDB.3.

For the asymptotic conclusion, the convex diameter-graph bound and
`per(F)<=pi D` give `h=O(D)`.  From any unbounded sequence take a subsequence with

```math
\frac hD\to y.
```

DB gives `y>=2rho`; the projective packing gives `y<=pi`.  Also

```math
D\delta_D\to1,
\qquad
\sin\delta_D\sim\delta_D,
\qquad
\frac{L_D}{D}=O(D^{-1/4}).
\tag{2.15}
```

Divide FSDB.3 by `D^2` and pass to the limit:

```math
\liminf\frac{\operatorname{area}F}{D^2}
\ge
\frac{y+\sin y}{4}.
\tag{2.16}
```

On `[0,pi]`,

```math
\frac d{dy}(y+\sin y)=1+\cos y\ge0.
```

Thus the right side of (2.16) is minimized at `y=2rho`, giving

```math
\liminf\frac{\operatorname{area}F}{D^2}
\ge
\frac{2\rho+\sin(2\rho)}4.
```

This is FSDB.1. `square`

### Dependencies

- `docs/reports/target_c_full_source_circumradius_response_2026-09-10.md`, FS.4,
  specifically `d_Haus(F-o,-(F-o))<=2L_D`.
- `docs/reports/target_c_post_zf_difference_body_perimeter_2026-09-09.md`, the
  complete actual diameter-direction polygon and DB.4.
- the C67 diameter-direction separation used in DB:
  `delta_D=2 asin(1/(2D))`.
- Cauchy's perimeter formula / perimeter--diameter inequality and Steiner's outer
  parallel-body formula.

No external theorem beyond those already present in the repository is imported.

### Why it is new

The September 9 difference-body area route uses only

```math
P_H\subseteq F-F
```

and the general planar Rogers--Shephard inequality

```math
\operatorname{area}(F-F)\le6\operatorname{area}F,
```

which loses a factor `6`.  PI bypasses the difference body and uses one pair of
well-separated diameter chords.  FS.4, committed on September 10, supplies the missing
near-central-symmetry needed to convert **the entire** difference body back to `F`:

```math
\tfrac12(F-F)\subseteq F-o+o(D)B_2.
```

That is the new step.  A repository search at the starting commit found no prior use
of this `1/4` conversion or the constant `0.6184708847...`.

---

## 3. Exact target implication

The universal post-ZF force-hull area floor improves from PI's

```math
0.4978566363\ldots D^2
```

to

```math
0.6184708847\ldots D^2.
```

Therefore the maximum source-hull area lying outside the force hull is asymptotically
at most

```math
\boxed{
\left(
\frac\pi4-A_{FS}
\right)D^2+o(D^2)
=0.1669272786277625\ldots D^2+o(D^2).
}
\tag{3.1}
```

This is especially relevant to MB's perfect-matching branch, where every non-core
source point is already known to lie outside `F` and MB requires a quadratic external
population.  Converting (3.1) into a population upper bound requires a finite packing
estimate for the nonconvex annular region `K\setminus F`; that is deliberately not
smuggled into this report.

---

## 4. Exact remaining lemma

For the perfect-matching subbranch, the immediate sufficient theorem is:

> **Annular finite-packing theorem.** If `F subset K` are convex planar bodies with
> `per(F)+per(K)=O(D)`, and `S subset K\setminus F` is unit-separated, then
> 

```math
> |S|\le\frac2{\sqrt3}
> \bigl(\operatorname{area}K-\operatorname{area}F\bigr)+o(D^2).
> 
```

Combined with (3.1), this would give

```math
|S|\le0.1927510185\ldots D^2+o(D^2),
```

whereas MB requires

```math
|S|\ge0.2900494070\ldots D^2-o(D^2).
```

The margin is about `0.0972983885 D^2`, so a boundary error of order `O(D)` is more
than sufficient.

---

## 5. Audit classification of other claims

| Claim | Classification | Reason |
| --- | --- | --- |
| FS.4 implies `(F-F)/2 subset F-o+L_DB_2` after translation | proved | direct Hausdorff inclusion and convexity |
| `area(P_H)=D^2 sum sin g_i` | proved | exact inscribed-polygon area formula; projective gaps repeat twice |
| gap-concentrated lower bound (2.14) | proved | concavity of sine with lower-bounded gaps |
| asymptotic constant `A_FS` | proved under FS.4 + DB | subsequence limit and monotonicity of `y+sin y` |
| matching branch is excluded | not proved in this report | needs annular population bound |
| Level I | still open | high-surplus/general topology remains even if matching is later removed |

---

## 6. Regression tests

| Regression | Passed? | Exact reason |
| --- | --- | --- |
| regular odd unit shell | yes | its force hull approaches the radius-`D/2` disk, so `area(F)/D^2 -> pi/4 > A_FS` |
| shell with dense strict isolated filling | yes | isolates do not enter `F`; FS.4 is a full-source theorem and the shell force hull still has area near `pi D^2/4` |
| unit square | yes | FSDB.3 is finite with a negative parallel-body error; no false asymptotic exclusion is asserted |
| low diameter-direction count | yes | the `A_FS` constant uses DB; FSDB.3 itself retains explicit `h` |

The shell regressions lack large-cardinality global optimality; FSDB does not use them
as a contradiction.

---

## 7. Failed routes and no-go results

This run rejects two shortcuts.

1. `FS near symmetry -> F is nearly a disk` is false.  Approximate central symmetry
   alone permits many centrally symmetric noncircular convex bodies.
2. `large area(F) -> Level I` is false without population localization.  The source
   may still contain contact-isolated points outside `F`; the matching branch makes
   this obstruction explicit.

The valid use of FS symmetry is the quantitative difference-body conversion (2.8).

---

## 8. Literature imported

None.

---

## 9. Computation and reproducibility

Only decimal evaluation of the closed-form constant was used:

```math
\rho=0.7390851332151606\ldots,
\quad
A_{FS}=0.6184708847696858\ldots .
```

The proof depends only on the defining equation `rho=cos rho`, not on the decimals.

---

## 10. Canonical promotion recommendation

**Hold as report** until an independent dependency audit checks FS.4, DB, and the
one-line convex-body inclusion (2.6).  If that audit passes, promote the force-hull
area floor into the post-ZF Target C frontier and supersede PI only as the best
universal area constant; PI's projective-circle and downstream structural statements
remain independently useful.

---

## 11. Next run

Prove the annular finite-packing theorem in Section 4 with an explicit `O(D)` boundary
term, then combine it with MB.  A local Voronoi-cell proof is the natural route because
it can localize packing density to `K\setminus F` without convexifying across `F`.

---

## 12. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Strongest new theorem FSDB:
For the post-ZF relative-interior force hull F, FS.4 gives
    d_Haus(F-o,-(F-o)) <= 2 L_D,  L_D=O(D^(3/4)).
If P_H=D conv{+-u_e : e in H}, then P_H subset F-F and therefore
    (1/2)P_H subset F-o+L_D B.
Hence
    area(F) >= area(P_H)/4 - pi D L_D-pi L_D^2.
For projective gaps g_i>=delta_D=2 asin(1/(2D)), sum g_i=pi,
    area(P_H)=D^2 sum sin g_i
             >=D^2[(h-1)sin delta_D+sin((h-1)delta_D)].
DB gives liminf h/D>=2rho, rho=cos rho, so
    liminf area(F)/D^2 >= (2rho+sin(2rho))/4
                       = 0.6184708847696858...

This improves PI's 0.4978566363... area floor.
Immediate next target: localize planar packing density to the annulus K\F with only
O(per K+per F) boundary loss; combined with MB this should exclude the perfect-matching
branch by a quadratic margin.
```
