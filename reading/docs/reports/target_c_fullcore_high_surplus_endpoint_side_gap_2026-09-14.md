> Generated reading edition · [exact source](../../../docs/reports/target_c_fullcore_high_surplus_endpoint_side_gap_2026-09-14.md) · source SHA-256 `d51f1ff5d8010a2879e2f826bcc7a21d814e2c7a87f55cd2c457022d435f5c0a`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 4 paragraph(s) with malformed inline math are preserved as explicit source excerpts rather than guessed equations.

<!-- theorem-state: {"artifact_id":"ART-F2AD63C9D248","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_fullcore_high_surplus_endpoint_side_gap_2026-09-14.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=208ba46b481174908244ebe0ddf22092ddcfa3be; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — full-core high-surplus endpoint and loaded-side gap audit

**Date:** 2026-09-14
**Repository commit:** `ef941ab2b44aa393bdc461926769247b45754202`
**State version:** `2026-09-14.audit.49`
**Run type:** closing proof / exact asymptotic endpoint audit
**Target:** Target C-II / Level I
**Starting status:** canonical full-core near-disk branch with promoted loaded-chord and train-coupled surplus floors
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md`
**External literature search:** used for a near-miss scope check; no external theorem imported into the proof
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

This report does not claim a solution. It sharpens the equality structure of the
current canonical full-core surplus floor and adds an exact geometric bound on the
number of nonunit sides of the loaded force hull. The remaining high-surplus branch
still has no source-preserving descent or exact unit-triangle implication.

## 1. Starting canonical endpoint

In the canonical full-core, no-macroscopic-container Type-II branch, let $`F`$ be the
actual loaded force hull, $`B=\operatorname{Vert}(F)`$, $`q=|B|`$, $`p=\operatorname{per}F`$,
and let $`m_B`$ be the number of nonunit sides of $`F`$. Put


```math
k=d_H+s_Z,
\qquad
\mu_D=\frac{e_{BB}+2s_C-3k}{D}.
```

The promoted loaded-chord theorem gives, for all sufficiently large members of the
sequence,

```math
c_B=0,
\qquad e_{BB}=q-m_B,
\qquad
\mu_DD=q+m_B-k-2c_I-4.
\tag{1.1}
```

The promoted train-coupled surplus theorem gives

```math
\liminf\mu_D\ge
\mu_{\rm TC}:=
\frac{2\pi+2\sqrt{\pi/(2\sqrt3)}}5
=1.6375621841815\ldots.
\tag{1.2}
```

Its proof uses the exact inequalities

```math
u_D:=\frac{q-k}{D}
\ge \frac{p}{2D}+\frac{Q}{2D},
\qquad
u_D+2\frac fD\ge2\sqrt{\frac{R_4}{D^2}},
\qquad Q\ge f,
\tag{1.3}
```

where $`Q`$ is bounded-face degree excess, $`f`$ is the number of bounded
nonquadrilateral faces, and (R_4) is the strict-rhombus face count. In the full-core
near-disk branch,

```math
\frac pD\to\pi,
\qquad
\frac{R_4}{D^2}\to
\Delta_2:=\frac{\pi}{2\sqrt3}.
\tag{1.4}
```

The candidate chain for this report is

```text
near-disk inner/outer radius sandwich
    -> exact upper bound on every loaded-hull side
    -> endpoint equality in (1.3)
    -> explicit high-mu endpoint side/face/outer-walk restrictions
    -> test whether the remaining endpoint is contradictory
```

## 2. Strongest genuinely new result

**Classification:** unreviewed candidate; complete proof of the stated conditional
endpoint theorem, with no promotion requested.

### 2.1 Exact loaded-side chord bound

Let $`F`$ be a convex body satisfying

```math
B(0,r_D)\subset F\subset B(0,R_D),
\qquad 0<r_D\le R_D.
\tag{2.1}
```

Every side of $`F`$ has length at most

```math
\boxed{\;s_D^{\max}:=2\sqrt{R_D^2-r_D^2}.\;}
\tag{2.2}
```

#### Proof

Let a side lie on a supporting line (n\cdot x=t), with (|n|=1), and orient (n)
outward. Since (B(0,r_D)subset F), (t\ge r_D). Both side endpoints lie in
(B(0,R_D)). The intersection of the line (n\cdot x=t) with that outer disk is a
chord of length

```math
2\sqrt{R_D^2-t^2}
\le2\sqrt{R_D^2-r_D^2}.
```



**Source formatting excerpt (unbalanced inline math in the original):**

```text
The side is contained in this chord, proving (2.2). \(\square)
```



### 2.2 Exact count bound for nonunit loaded-hull sides


**Source formatting excerpt (unbalanced inline math in the original):**

```text

Let \(m_B\) be the number of sides of $`F`$ whose length exceeds one. Since every
loaded-loaded unit contact is a hull side and every other hull side is nonunit, the
side lengths (s_1,ldots,s_q) satisfy
```



```math
p-q=\sum_{i:s_i>1}(s_i-1).
\tag{2.3}
```

Applying (2.2) to each nonunit side gives the finite inequality

```math
\boxed{
m_B\ge
\frac{p-q}{2\sqrt{R_D^2-r_D^2}-1}
}
\tag{2.4}
```

whenever (2\sqrt{R_D^2-r_D^2}>1). The numerator is nonnegative because source
unit-separation gives every loaded-hull side length at least one.

This is an actual loaded-hull statement. It does not count repeated contact-walk
occurrences, does not replace $`F`$ by a scaffold, and does not remove any
contact-isolated source point.

### 2.3 Equality package at the train-coupled floor

Let $`A_D`$ be any unbounded canonical full-core sequence satisfying

```math
\mu_D\longrightarrow\mu_{\rm TC}.
\tag{2.5}
```

Then the following limits hold:

```math
\boxed{
\frac{q-k}{D}\longrightarrow\mu_{\rm TC},
\qquad
\frac{m_B}{D}\longrightarrow0,
\qquad
\frac{Q-f}{D}\longrightarrow0,
}
\tag{2.6}
```

```math
\boxed{
\frac{b-p}{D}\longrightarrow0,
\qquad
\frac fD\longrightarrow
f_{\rm TC}:=\frac{4\sqrt{\Delta_2}-\pi}{5},
}
\tag{2.7}
```

and, using canonical component deatomization,

```math
\boxed{\frac{c_I}{D}\longrightarrow0.}
\tag{2.8}
```

Here $`b`$ is the occurrence-counted outer contact-face walk length. In particular,
the endpoint has only asymptotically pentagonal exceptional-face degree excess,
asymptotically no outer-walk detour beyond the loaded-hull perimeter, and no linear
loaded-side count. The theorem does not assert that (q/D\to\pi): a sublinear number
of nonunit sides may still carry a linear perimeter deficit because the near-disk side
bound (2.2) is only (o(D)) per side.

#### Proof

Canonical component deatomization gives (c_I=O(D^{2/3})), so (1.1) implies

```math
\mu_D-u_D=\frac{m_B-2c_I-4}{D}.
\tag{2.9}
```

Since (m_B\ge0), the train-coupled proof first establishes

```math
u_D\ge
\frac45\left(\frac{p}{2D}+\frac{Q}{2D}\right)
+\frac15\left(2\sqrt{\frac{R_4}{D^2}}-2\frac fD\right)
\ge
\frac{2p}{5D}+\frac{2\sqrt{R_4/D^2}}5
+\frac{2(Q-f)}{5D}.
\tag{2.10}
```

The last expression tends to $`\mu_{\rm TC}`$ from below only through the two
vanishing geometric limits in (1.4) and the nonnegative term (2(Q-f)/(5D)).
More explicitly, set

```math
A_D=\frac{p+Q}{2D},
\qquad
B_D=2\sqrt{R_4/D^2}-2\frac fD.
```

The two canonical inequalities say $`A_D\le u_D`$ and $`B_D\le u_D`$, while
(2.10) is $`\frac45A_D+\frac15B_D\le u_D`$. Since the weighted average tends to
$`\mu_{\rm TC}`$, and $`\mu_D\to\mu_{\rm TC}`$ together with (2.9) gives
$`u_D\le\mu_{\rm TC}+o(1)`$, both nonnegative gaps $`u_D-A_D`$ and
$`u_D-B_D`$ tend to zero. Consequently (2.9) forces

```math
\frac{m_B}{D}\to0,
\qquad
\frac{Q-f}{D}\to0,
\qquad
\frac{q-k}{D}\to\mu_{\rm TC}.
```

Now the first inequality in (1.3) is the exact identity

```math
u_D-\left(\frac{p}{2D}+\frac{Q}{2D}\right)
=\frac{b-p}{2D},
\tag{2.11}
```

so $`b-p=o(D)`$. The second inequality in (1.3), together with $`Q-f=o(D)`$, is
asymptotically an equality:

```math
\mu_{\rm TC}=\frac{\pi}{2}+\frac{f_{\rm TC}}2
=2\sqrt{\Delta_2}-2f_{\rm TC}.
\tag{2.12}
```



**Source formatting excerpt (unbalanced inline math in the original):**

```text
Solving gives (2.7). Equation (2.8) is canonical. \(\square)
```



### 2.4 Endpoint side-gap consequence

The exact side inequality (2.4) and (2.6) imply the following subsequential
dichotomy for any sequence satisfying (2.5):

```math
\boxed{
\text{after passing to a subsequence, either }\frac{p-q}{D}\to0,
\quad\text{or}\quad
m_B\to\infty\text{ while }m_B/D\to0.
}
\tag{2.13}
```

More quantitatively, if (p-q\ge\eta D) along a subsequence for some fixed
(eta>0), then

```math
m_B\ge
\frac{\eta D}{2\sqrt{R_D^2-r_D^2}-1}
=\omega(1),
\qquad m_B=o(D).
\tag{2.14}
```



**Source formatting excerpt (unbalanced inline math in the original):**

```text
The \(m_B=o(D)\) conclusion is from (2.6); the $`\omega(1)`$ conclusion follows from
the near-disk limit
```



```math
\frac{2\sqrt{R_D^2-r_D^2}-1}{D}\longrightarrow0.
\tag{2.15}
```

Thus, on any subsequence with a linear loaded-hull perimeter deficit, the floor
endpoint cannot have only finitely many nonunit loaded sides. It may still have a
sublinear but diverging
number of increasingly long sides. This is the exact remaining side-gap obstruction.

### 2.5 Exact scalar freedom at the endpoint

The preceding endpoint package does not merely fail to determine $`q/D`$; the
remaining freedom can be written exactly. Pass to a further subsequence on which

```math
\frac qD\longrightarrow \xi.
\tag{2.16}
```

The endpoint relations (2.6)--(2.8), the definitions

```math
x_B=b-q,
\qquad u_B=x_B-m_B,
\qquad k=d_H+s_Z,
\tag{2.17}
```

and the exact loaded-hull split (63.3), with $`c_B=0`$, give

```math
q-m_B=Q+2k+u_B.
\tag{2.18}
```

Since $`Q/D\to f_{\rm TC}`$, $`(q-k)/D\to\mu_{\rm TC}`$, and
$`m_B/D\to0`$, (2.18) yields

```math
\boxed{
\frac{u_B}{D}\longrightarrow
2\mu_{\rm TC}-\xi-f_{\rm TC}.}
\tag{2.19}
```

On the other hand, $`b-p=o(D)`$ and $`p/D\to\pi`$, so (2.17) gives

```math
\boxed{
\frac{u_B}{D}\longrightarrow\pi-\xi.}
\tag{2.20}
```

The two formulae agree identically, because (2.12) is equivalent to

```math
\boxed{2\mu_{\rm TC}-f_{\rm TC}=\pi.}
\tag{2.21}
```

Thus the endpoint scalar package imposes only

```math
\boxed{
\frac{k}{D}\longrightarrow\xi-\mu_{\rm TC},
\qquad
\frac{u_B}{D}\longrightarrow\pi-\xi,
\qquad
\mu_{\rm TC}\le\xi\le\pi,}
\tag{2.22}
```

where the interval follows from $`k,u_B\ge0`$. Every value in this interval is
algebraically compatible with the endpoint identities; no value of $`\xi`$ is
selected by the train-floor equality. In particular, the endpoint may store the
complementary linear currency either in the loaded-hull deficit $`k`$, or in the
outer-walk excess $`u_B`$, or in both.

This is an exact no-go for a scalar closure based only on (2.6)--(2.8) and the
loaded-hull identity: it leaves a continuum of normalized assignments. It is not a
geometric counterexample. The missing theorem must constrain how a linear $`u_B`$
is realized by actual unit-contact paths with unloaded vertices and positive
equilibrium, or must use the source-preserving global diameter comparison.

## 3. Scope

The endpoint theorem concerns only sequences already in the canonical full-core
near-disk branch. The source is the original full configuration; all source points,
including contact-isolated points, remain present. $`F`$, $`B`$, $`b`$, $`Q`$, and
$`m_B`$ concern the actual loaded positive-contact core and its occurrence-counted
outer walk. No claim is made about Type-I macroscopic chambers or exterior caps.

The result is asymptotic and conditional on the existence of a sequence with
$`\mu_D\to\mu_{\rm TC}`$. It is not a finite threshold theorem and does not assert
that the floor is attained.

## 4. Exact frontier effect

This report does not change the canonical state. It removes one informal endpoint
possibility—finitely many nonunit loaded-hull sides carrying a linear $`p-q`$ deficit—
but leaves the following actual alternatives:

```text
full-core high-surplus floor endpoint
    -> m_B=o(D), Q-f=o(D), b-p=o(D), c_I=o(D)
    -> either p-q=o(D), or a diverging sublinear family of long nonunit sides
    -> unresolved source-level deformation / exact-triangle implication
```

The scalar endpoint remains compatible with the current ledgers. In particular,
(2.13) is not a contradiction: $`m_B\to\infty`$ and $`m_B=o(D)`$ is allowed by every
promoted theorem listed below. No strict same-cardinality sub-(D) source is
constructed.

## 5. Exact remaining lemma

A genuine closure would need one of the following new source-level statements:

1. **Long-side elimination:** in a full-core global minimizer, a sublinear family of
   nonunit loaded-hull sides cannot carry (\Theta(D)) of (p-q) without forcing a
   unit equilateral triangle or a strict source-preserving diameter decrease;
2. **Pentagon-interface elimination:** the endpoint rates
   (Q-f=o(D)), (b-p=o(D)), and (f/D\to f_{\rm TC}) are incompatible with the
   actual loaded/exceptional-face geometry; or
3. **High-surplus deformation:** every full-core sequence with the endpoint package
   (2.6)--(2.8), whether or not (p-q=o(D)), admits an explicit same-cardinality
   feasible deformation with diameter (<D(n)).

No one of these statements follows from the current scalar ledgers.

## 6. Claim audit table

| Claim | Status | Dependencies | Reason |
| --- | --- | --- | --- |
| Near-disk annulus (B(0,r_D)\subset F\subset B(0,R_D)) | canonical | `C-FULLCORE-NEAR-DISK` | exact promoted full-core scope |
| Every loaded-loaded unit chord is a hull side | canonical | `C-FULLCORE-LOADED-CHORD` | promoted near-disk chord theorem |
| Loaded side bound (2.2) | proved here | convexity and annulus | supporting-line chord calculation |
| Count bound (2.4) | proved here | (2.2), unit side lengths | exact side-length sum |
| Endpoint package (2.6)--(2.8) | proved here | `C-FULLCORE-TRAIN-SURPLUS-FLOOR`, `C-COMP-DEATOMIZATION` | equality in two positive lower bounds |
| (p-q=o(D)) at the endpoint | not proved | side bound only gives (2.13) | long sublinear side family remains possible |
| High-surplus endpoint is impossible | not proved | missing long-side/interface theorem | no source-level contradiction |
| Level I | still open | Type-I and high-surplus branches remain | quantifiers not discharged |

## 7. Regression checks

| Regression/correction | Result | Exact hypothesis or failure |
| --- | --- | --- |
| Near-disk vanishing-shear lattice | pass | its loaded boundary can have small angular defects; no global-optimality claim is made |
| Regular odd shell | pass | it is a finite/local-shell regression, not a full-core floor sequence; no side theorem is applied beyond its hypotheses |
| Loaded nonconsecutive chord | pass | excluded only by the promoted near-disk loaded-chord theorem; arbitrary convex polygons are outside scope |
| Contact-isolated source points | pass | never enter the side count or the core stress extension; they remain in the full source |
| Repeated outer-walk occurrences | pass | (b-p) is the occurrence-counted difference and is not silently set to zero |
| Low-slack/saturated exterior caps | pass | Type-I cap branch is explicitly outside the theorem |
| Global minimality versus local deformation | pass | no local side equality is converted into a finite release |

## 8. Literature imports and near miss

No external theorem is used in the proof. A scope check was made against
Connelly--Dickinson, *Periodic Planar Disk Packings*, especially their results on
collectively jammed triangular-torus packings by equilateral triangles and rhombi.
Those results concern periodic torus packings and jammed/tiling hypotheses; they do
not provide a theorem for a free-boundary finite (D(n)) minimizer, do not retain the
same-cardinality global source comparison, and do not bridge the long-side alternative
(2.13). The primary source checked was the authors' PDF:

<https://pi.math.cornell.edu/~connelly/Connelly-Dickinson-V3.pdf>

No conclusion from that paper is imported into (2.1)--(2.15).

## 9. Computation

No computation was logically required. The constants in (1.2) and (2.12) are carried
symbolically; the displayed decimal is orientation only. The side bound is exact
Euclidean geometry.

## 10. Corrections / supersessions

No canonical claim is superseded. The report refines the equality discussion in
`docs/reports/target_c_fullcore_train_coupled_surplus_floor_2026-09-14.md` by making
the exact (m_B=o(D)), (Q-f=o(D)), and (b-p=o(D)) consequences explicit and by
adding the finite side inequality (2.4). It does not alter that report's conclusion
that the high-surplus branch remains open.

## 11. Promotion recommendation

**unreviewed**. The finite side lemma and endpoint algebra are complete, but the
result is an equality audit with no branch elimination. Do not change theorem-state,
route maps, or prompts.

## 12. Handoff

1. **Strongest new theorem:** the exact loaded-side bound (2.4) and its endpoint
   consequence (2.13), together with the explicit pentagon/interface equality package.
2. **Canonical dependency chain:** `C-FULLCORE-NEAR-DISK` +
   `C-FULLCORE-LOADED-CHORD` + `C-FULLCORE-TRAIN-SURPLUS-FLOOR` +
   `C-COMP-DEATOMIZATION`.
3. **Exact remaining lemma:** eliminate a sublinear family of long nonunit loaded
   sides, or eliminate the endpoint's pentagon/interface rates by a source-preserving
   deformation or exact-triangle theorem.
4. **Binding dead routes:** scalar upper-bound optimization, finite local KKT-force
   release, arbitrary affine-window equilateralization, and cap covering without a
   source-preserving exchange.
5. **Files to read next:** `docs/targets/target-c/CURRENT.md`,
   `docs/reports/target_c_typeii_aggregate_payment_and_exchange_2026-09-14.md`,
   `docs/reports/target_c_zr_holed_train_angle_flex_dimension_2026-09-09.md`, and
   Target A Sections 175--177.
