> Generated reading edition · [exact source](../../../docs/reports/target_c_fullcore_contact_walk_anisotropic_regression_2026-09-14.md) · source SHA-256 `f2179c71da31e861160f7d5851f3a719140ea8f9452eac873d768f6b56bdbad9`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 4 paragraph(s) with malformed inline math are preserved as explicit source excerpts rather than guessed equations.

<!-- theorem-state: {"artifact_id":"ART-02DE33235967","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_fullcore_contact_walk_anisotropic_regression_2026-09-14.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=6334ebc2f126f5828e2f7a9568f832d1b59595cc; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — anisotropic contact-walk detour regression

**Date:** 2026-09-14
**Repository commit:** `ef941ab2b44aa393bdc461926769247b45754202`
**State version:** `2026-09-14.audit.49`
**Run type:** closing proof / exact regression
**Target:** Target C-II / Level I
**Starting status:** canonical full-core frontier through Sections 122–123 and the
promoted loaded-chord/train-surplus floor
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md`
**External literature search:** not used for the result
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

This report proves a finite, source-level regression against any proposed
near-disk/density-only upper bound on an occurrence-counted contact outer walk.
The family is not asserted to be a global minimum-diameter source, and its source
hull is not identified with the C-II positive-force hull. It therefore neither
solves nor disproves Problem #99.

## 1. Starting canonical endpoint

The live full-core C-II endpoint is the occurrence-counted aggregate inequality

```math
 \liminf_{D\to\infty}{1\over D}
 \sum_r(L_r+P_{{\rm exc},r}-2d_r)
 \ge {\pi\over2}(2-\sqrt3),
```

together with

```math
 \sum_rP_{{\rm exc},r}\le10(e_{BB}-k),
 \qquad k=d_H+s_Z.
```

The promoted near-disk loaded-chord/train coupling additionally gives, in the
canonical Type-II force-hull branch,

```math
 \liminf {e_{BB}+2s_C-3k\over D}
 \ge {2\pi+2\sqrt{\pi/(2\sqrt3)}\over5}.
```

The missing source-level implication is still an upper bound on the same outer
detour, an exact unit triangle, or a finite same-cardinality strict sub-$`D`$
competitor.

The candidate chain tested here was

```text
near-disk + triangle-free + near-optimal density
    -> outer contact walk is close to Euclidean hull perimeter
    -> Section 122/123 closes the full-core branch
```

The first implication is false without a force/global-optimality hypothesis.

## 2. Strongest genuinely new result

**Classification:** regression / proved finite obstruction; unreviewed and
noncanonical.

### Theorem — a near-disk triangle-free source can have linear anisotropic detour

For every sufficiently large integer (R), put

```math
 \varepsilon_R=R^{-2},
 \qquad \theta_R={\pi\over3}+\varepsilon_R,
 \qquad u=(1,0),
 \qquad v=(\cos\theta_R,\sin\theta_R),
```

and let

```math
 \Lambda_R=\{iu+jv:i,j\in\mathbb Z\},
 \qquad A_R=\Lambda_R\cap B(0,R).
```

Let (G_R) be the straight-line graph on (A_R) whose edges are the unit
contacts, let (F_R=\operatorname{conv}(A_R)), let (b_R) be the length of the
outer-face boundary walk of (G_R), with edge occurrences counted, and let

```math
 D_R=\operatorname{diam}(A_R),
 \qquad P_R=\operatorname{per}(F_R).
```

Then, for all sufficiently large (R):

1. (A_R) is unit-separated and contains no unit equilateral triangle;
2. (G_R) is connected and its edges are exactly the differences
   $`\pm u,\pm v`$, so it is bipartite;
3. (D_R=2R+O(1)), (F_R) is within bounded Hausdorff distance of (B(0,R)), and
   ```math
   |A_R|={\pi\over2\sqrt3}D_R^2+O(D_R);
   
   ```
4. the outer contact walk has the explicit lower bound
   ```math
   b_R\ge {8(R-3)\over\sin\theta_R};
   
   ```
5. consequently,
   ```math
   b_R-P_R\ge
   {8(R-3)\over\sin\theta_R}-2\pi R,
   
   ```
   and therefore
   ```math
   \boxed{
   \liminf_{R\to\infty}{b_R-P_R\over D_R}
   \ge {8\over\sqrt3}-\pi
   =1.4772094999272136\ldots .
   }
   
   ```

Thus near-disk geometry, asymptotically optimal triangular-packing density, and
triangle-free two-direction contact structure do not imply
$`b_R-P_R=o(D_R)`$. The obstruction is a genuine linear detour, not a boundary
rounding error.

### Scope

This is an actual finite source family. It retains every point of (A_R), has no
contact-isolated cloud, and uses no scaffold. It is nevertheless only a feasible
packing family:

- no claim of global minimum-diameter optimality is made;
- no KKT stress with a positive diameter-force hull is supplied;
- (F_R) is the source hull, not the C-II loaded positive-force hull (F);
- the family is not a canonical post-ZF representative;
- the outer walk is the contact graph's walk, not one of the attachment-cell walks
  (L_r) in Sections 122–123.

Accordingly the theorem is a regression against a proposed geometric bridge. It is
not a counterexample to the C-II theorem itself.

### Proof

Write (c_R=\cos\theta_R) and (s_R=\sin\theta_R). For sufficiently large
(R),

```math
0<c_R<\frac12.
```



**Source formatting excerpt (unbalanced inline math in the original):**

```text
For a lattice difference (iu+jv\), if (ij\ge0), then
```



```math
 |iu+jv|^2=i^2+j^2+2c_Rij\ge1
```

for every nonzero integer pair. If (ij<0), put (a=|i|), (d=|j|). Then

```math
 |iu+jv|^2=(a-d)^2+2ad(1-c_R).
```

For (a=d=1), this is (2(1-c_R)>1), and for (a\ne d) the first term is at
least one and the second is positive. Hence all distinct points are at distance at
least one. Equality occurs only for
$`±u,±v`$. Coloring (iu+jv) by (i+j\pmod 2) makes every contact edge
bichromatic, so (G_R) is triangle-free.

It remains to check that the induced contact graph is connected. In the coordinate
form

```math
 Q(i,j)=i^2+j^2+2c_Rij,
```

consider a nonzero pair ((i,j)). If (ij\ge0), moving one nonzero coordinate
one unit toward zero changes (Q) by

```math
 -2(|i|+c_R|j|)+1
 \quad\text{or}\quad
 -2(|j|+c_R|i|)+1,
```

which is negative. If (ij<0), write (I=|i|), (J=|j|). When (I\ge J),
moving (i) toward zero has dot-product term (I-c_RJ\ge1-c_R>1/2); when
(J\ge I), move (j) toward zero instead. In every case one permitted contact
step strictly decreases (Q), and therefore remains inside the disk (Q\le R^2).
Iterating reaches the origin, proving connectivity.

For the diameter and density estimates, use the fundamental parallelogram

```math
 Q_0=\{su+tv:0\le s,t<1\}.
```

It tiles the plane, has area (s_R), and every point of (Q_0) is within distance
at most two of one of its lattice vertices. Thus, for an absolute constant (C),

```math
 {\pi(R-C)^2\over s_R}
 \le |A_R|\le
 {\pi(R+C)^2\over s_R}.
\tag{2.1}
```



**Source formatting excerpt (unbalanced inline math in the original):**

```text
More directly, rounding the two real lattice coordinates independently gives a
lattice point within distance at most one. Applying this to
\((R-2)e) and \(-(R-2)e), for any unit vector (e), gives
```



```math
 2R-6\le D_R\le2R.
\tag{2.2}
```

The same rounding argument gives a support point of (F_R) at distance at least
(R-3) in every direction. Hence

```math
 B(0,R-3)\subseteq F_R\subseteq B(0,R).
\tag{2.3}
```

Since (s_R=\sqrt3/2+O(R^{-2})), (2.1)–(2.2) give the stated density estimate,
and (2.3) gives bounded Hausdorff error.

Now use lattice coordinates. Every contact edge changes exactly one of the two
coordinates (\alpha,β) in

```math
 x=\alpha u+\beta v
```

by (+1) or (-1). The graph's outer boundary walk is a closed polygonal walk
whose image has convex hull (F_R): every extreme vertex of a straight-line
connected planar graph lies on its outer face. Consequently its number of edge
occurrences is its total coordinate variation,

```math
 b_R=\operatorname{Var}_{\partial G_R}(\alpha)
     +\operatorname{Var}_{\partial G_R}(\beta).
\tag{2.4}
```

For any closed walk whose image has coordinate range of width (w), the total
variation in that coordinate is at least (2w). The coordinate functionals are

```math
 \alpha(x,y)=x-\cot\theta_R\,y,
 \qquad
 \beta(x,y)=\csc\theta_R\,y.
```



**Source formatting excerpt (unbalanced inline math in the original):**

```text
Each has Euclidean gradient norm \(\csc\theta_R\), so (2.3) gives
```



```math
 \operatorname{width}_{F_R}(\alpha)
 \ge {2(R-3)\over\sin\theta_R},
 \qquad
 \operatorname{width}_{F_R}(\beta)
 \ge {2(R-3)\over\sin\theta_R}.
\tag{2.5}
```

Combining (2.4)–(2.5) gives

```math
 b_R\ge {8(R-3)\over\sin\theta_R}.
\tag{2.6}
```

Finally, (F_R\subseteq B(0,R)), and Euclidean perimeter is monotone for convex
bodies, so

```math
 P_R\le2\pi R.
\tag{2.7}
```

Equations (2.6)–(2.7), (D_R=2R+O(1)), and
$`\sin\theta_R\to\sqrt3/2`$ yield

```math
 {b_R-P_R\over D_R}
 \ge
 {8(R-3)/\sin\theta_R-2\pi R\over 2R+O(1)}
 \longrightarrow {8\over\sqrt3}-\pi.
```

This proves the theorem. $`\square`$

## 3. Exact frontier effect

The result rejects the following implication unless it gains an additional
force/global-minimality hypothesis:

```text
near-disk source hull
    + density Delta_2 + o(1)
    + triangle-free two-direction local contacts
    -> b-P_F=o(D).
```

The regression is stronger than a density-only example because the detour is
quantified by a finite outer-face walk and has a fixed positive normalized limit.
It also explains why replacing (b) by Euclidean perimeter in a source-level
version of Sections 122–123 is invalid.

It does not change the theorem-state manifest. The C-II residual remains the
aggregate attachment-cell detour coupled to (e_{BB}-k), and the Type-I
macroscopic-container branch remains open.

## 4. Exact remaining lemma

The relevant closing target is now more sharply delimited:

> Prove an upper bound on the occurrence-counted attachment-cell detour using
> information that the regression lacks—namely the actual positive-force hull,
> the mixed KKT stress/diameter graph, global minimum-diameter optimality, or an
> exact source-preserving deformation. A bound based only on near-disk source
> geometry, density, and local two-direction contacts is impossible.

The bound must be on the actual $`\sum_r(L_r-2d_r)`$, retain repeated boundary
occurrences and bridges, and include every source point in any subsequent
source-preserving competitor.

## 5. Proof-obligation ledger and claim audit

| Claim | Status | Exact scope and reason |
|---|---|---|
| Unit separation of (A_R) | proved finite | Exact quadratic-form calculation; (0<\cos\theta_R<1/2) |
| Triangle-freeness | proved finite | The only unit differences are (\pm u,\pm v), so the contact graph is bipartite |
| Connectivity of (G_R) | proved finite | A contact step strictly decreases (Q(i,j)) |
| (D_R=2R+O(1)), bounded source-hull error | proved finite | Fundamental-cell rounding |
| ( |A_R|=\Delta_2D_R^2+O(D_R)) | proved finite | Fundamental parallelogram area and (\sin\theta_R=\sqrt3/2+O(R^{-2})) |
| (b_R-P_R\ge(8/\sqrt3-\pi-o(1))D_R) | proved finite/asymptotic | Coordinate variation of the actual contact outer walk |
| Source hull equals C-II force hull | not claimed | The regression has no KKT force construction |
| (A_R) is globally diameter-minimal | not claimed | The family is only a feasible source |
| Regression closes C-II | rejected | It identifies a missing hypothesis, not a contradiction |
| Level I | open | No statement about all cardinalities or all global minimizers |

## 6. Regression checks

| Regression/correction | Result | Exact hypothesis or failure |
|---|---|---|
| Vanishing-shear near-density family | pass | This is a finite realization with angle gap (R^{-2}) and density (Δ_2+O(R^{-1})) |
| Near-equilateral triangle-free configurations | pass | (θ_R>π/3) removes the third unit direction while the contact graph remains bipartite |
| Boundary-order loss | pass | The fixed detour constant (8/\sqrt3-\pi) is positive |
| Repeated outer-walk occurrences | pass | (b_R) is total edge-occurrence variation; no simple-cycle reduction is used |
| Source/scaffold distinction | pass | (A_R) is an actual source, but it is never promoted to a C-II source |
| Contact-isolated points | pass | The family has none; no point is deleted from a claimed global source |
| Local jammed versus global optimality | pass | No local-jamming or global-optimality conclusion is drawn |
| Loaded-force-hull scope | pass | The report explicitly uses (F_R=\operatorname{conv}(A_R)), not the C-II force hull |

The regular odd shell and near-chain regressions remain compatible: this family is
used only to disprove a detour upper bound, not to claim a diameter-graph structure
or a KKT stress. The exact affine-window comparisons remain compatible as well; they
can beat this family in restricted symmetric windows, but do not apply to arbitrary
global sources.

## 7. Literature imports

None. The proof uses elementary lattice coordinates, convex support widths, and
perimeter monotonicity for convex bodies. No external theorem is imported.

## 8. Computation

No computation is logically required. Every displayed constant follows from the
exact limit

```math
\sin\theta_R\to{\sqrt3\over2},
\qquad D_R=2R+O(1).
```

The finite construction could be enumerated directly, but no numerical enumeration
is used as evidence for the theorem.

## 9. Corrections / supersessions

This report does not supersede a canonical claim. It sharpens the earlier
vanishing-shear regression by adding an explicit linear lower bound on the actual
contact outer-walk detour of the finite lattice cut. It does not alter the canonical
Sections 122–123, whose walks are attachment-cell walks and whose force-hull
hypotheses are different.

## 10. Promotion recommendation

**regression/rejection only — do not promote.**

No state-version, route-map, prompt, or canonical theorem change is justified by
this report. The artifact should remain available as a mandatory regression against
any future source-level claim that turns near-disk density into a vanishing outer
detour.

## 11. Handoff


**Source formatting excerpt (unbalanced inline math in the original):**

```text

1. **Strongest new theorem:** the explicit finite family (A_R) has
   \(b_R-P_R\ge(8/\sqrt3-\pi-o(1))D_R) while remaining triangle-free and
   asymptotically density-optimal.
2. **Canonical dependency chain:** elementary quadratic-form/unit-separation and
   convex-width arguments; canonical Sections 122–123 are the endpoint being tested,
   not premises of the construction.
3. **Exact remaining lemma:** an upper detour/deformation theorem using the actual
   force hull and global optimality, or an exact triangle/source-preserving competitor.
4. **Binding dead route:** near-disk source geometry plus density cannot control the
   contact outer walk.
5. **Files to read next:** `docs/targets/target-c/CURRENT.md`, canonical Sections
   122–123, the promoted train-surplus report, and the active Target A/B endpoints.
```
