<!-- theorem-state: {"artifact_id":"ART-70C13C7CCB86","canonical":true,"claim_ids":["C-FULLCORE-TRAIN-SURPLUS-FLOOR"],"claim_statuses":{"C-FULLCORE-TRAIN-SURPLUS-FLOOR":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Erdős Problem #99 — full-core train-coupled surplus floor

**Date:** 2026-09-14
**Repository commit:** ef941ab2b44aa393bdc461926769247b45754202
**State version:** 2026-09-14.audit.49
**Run type:** closing proof / exact asymptotic synthesis
**Target:** Target C-II / Level I
**Starting status:** canonical full-core near-disk branch; canonical Sections 63, 75, 80, and 85; loaded-chord and train-coupled surplus claims are now promoted in audit.49
**Active prompt:** docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md
**External literature search:** not used for the result
**Computation:** not used

## LEVEL I STATUS

STILL OPEN

This report proves a stronger full-core surplus floor by coupling a new
near-disk loaded-hull chord lemma to the canonical train-boundary currency.
It does not close the aggregate detour, the source-preserving deformation, or the
macroscopic-container branch.

## 1. Exact candidate chain

    full-core near-disk hull
        -> every loaded-loaded unit chord is a hull side
        -> c_B=0 and e_BB=q-m_B
        -> mu_D D = q+m_B-k-2c_I-4
        -> Section 63 gives q-k >= (P_F+Q)/2
        -> Section 85 gives q-k+2f >= 2 sqrt(R_4)
        -> explicit full-core floor for mu_D

The only new geometric step is the loaded-chord lemma. The remaining inequalities
are exact canonical ledgers with their stated scopes.

## 2. Near-disk loaded-chord lemma

Let \(F\) be the actual loaded force hull and \(B=\operatorname{Vert}(F)\) in a
full-core near-disk Type-II survivor. For all sufficiently large \(D\), every
unit-distance pair of vertices of \(F\) is a side of \(F\).

The canonical C-FULLCORE-NEAR-DISK statement gives, after the canonical
translation,

\[
B(0,r_D)\subset F\subset B(0,R_D),
\qquad r_D/D\to1/2,\quad R_D/D\to1/2.
\tag{TC.1}
\]

Suppose a unit chord \(pq\) has a loaded vertex between \(p\) and \(q\) on the
short boundary arc. Since \(|p-q|=1\) and \(|p|,|q|\ge r_D\), the polar angular
span of that arc is \(O(D^{-1})\). At any point \(x\) on it, an outward normal \(n\)
satisfies \(n\cdot x\ge r_D\), while \(|x|\le R_D\). Consequently the tangent
directions of all hull sides on the arc lie in one cone of width
\(\tau_D=2\arccos(r_D/R_D)+O(D^{-1})=o(1)\). Orient the sides from \(p\) toward \(q\),
write them as \(v_j=\ell_jt_j\), and choose a unit axis \(t_0\) through the middle of
that cone. Unit separation makes \(\ell_j\ge1\), and therefore

\[
 t_0\cdot(q-p)=\sum_j\ell_j(t_0\cdot t_j)
\ge N\cos(\tau_D)\ge2\cos(\tau_D)>1,
\]

where \(N\ge2\) because the arc contains an intervening vertex. Since
\(t_0\cdot(q-p)\le|q-p|=1\), this is a contradiction. A nonsmooth hull causes no
problem: support normals are taken one side at a time, and the inner/outer disk
sandwich controls every limiting normal on the short arc.

Therefore, with Section-63 notation,

\[
\boxed{c_B=0,\qquad e_{BB}=q-m_B.}
\tag{TC.2}
\]

The proof concerns only loaded vertices; contact-isolated source points remain in
the full source.

## 3. Exact surplus reduction

Canonical Section 63 gives

\[
e_{BB}=q-m_B+c_B,
\qquad
c_I+s_C+c_B=m_B+k-2,
\qquad k=d_H+s_Z.
\tag{TC.3}
\]

Using (TC.2),

\[
s_C=m_B+k-c_I-2.
\tag{TC.4}
\]

Substitution into \(\mu_DD=e_{BB}+2s_C-3k\) gives the exact finite identity

\[
\boxed{\mu_DD=q+m_B-k-2c_I-4.}
\tag{TC.5}
\]

Canonical Section 75 supplies \(c_I=O(D^{2/3})\), so \(m_B\ge0\) and (TC.5) imply

\[
\mu_D\ge {q-k\over D}-o(1).
\tag{TC.6}
\]

The exact Section-63 identity

\[
b+Q=2h-2s_Z=2q-2k
\tag{TC.7}
\]

holds with occurrence-counted outer walk \(b\), degree defect \(Q\), and
\(k=d_H+s_Z\). Since \(b\ge P_F\), where \(P_F=\operatorname{per}(F)\),

\[
\boxed{q-k={b+Q\over2}\ge {P_F+Q\over2}.}
\tag{TC.8}
\]

No outer-walk occurrence is discarded and no simple-boundary assumption is made.

## 4. Coupling to canonical train-boundary currency

Let \(f\) be the number of bounded nonquadrilateral contact faces and \(R_4\) the
number of bounded strict-rhombus contact faces. Canonical Section 85 gives

\[
\boxed{q-k+2f\ge2\sqrt{R_4}.}
\tag{TC.9}
\]

Every nonquadrilateral face has degree at least five, so \(Q\ge f\). Divide by
\(D\) and put

\[
u_D={q-k\over D},\quad x_D={f\over D},\quad
p_D={P_F\over D},\quad r_D={R_4\over D^2}.
\]

Equations (TC.8) and (TC.9) give

\[
u_D\ge {p_D\over2}+{x_D\over2},
\qquad
u_D\ge2\sqrt{r_D}-2x_D.
\tag{TC.10}
\]

For any nonnegative \(x_D\), the convex combination with weights \(4/5\) and
\(1/5\) cancels \(x_D\), yielding

\[
u_D\ge {4\over5}\left({p_D\over2}+{x_D\over2}\right)
+{1\over5}\left(2\sqrt{r_D}-2x_D\right)
={2p_D+2\sqrt{r_D}\over5}.
\tag{TC.11}
\]

Canonical C-FULLCORE-NEAR-DISK gives \(p_D\to\pi\), and canonical
C-HARMONIC-CELL-TILING / C-TRAIN-INTERFACE-CURRENCY gives

\[
r_D\to{\pi\over2\sqrt3}.
\tag{TC.12}
\]

Combining (TC.6), (TC.11), and (TC.12) proves

\[
\boxed{
\liminf_{D\to\infty}\mu_D
\ge
\mu_{\mathrm{TC}}
:={2\pi+2\sqrt{\pi/(2\sqrt3)}\over5}.
}
\tag{TC.13}
\]

Numerically,

\[
\boxed{\mu_{\mathrm{TC}}=1.6375621841815\ldots.}
\tag{TC.14}
\]

The decimal is only an orientation value; the exact expression (TC.13) is the
theorem.

## 5. Equality audit and exact remaining branch

A sequence approaching (TC.13) must make the loaded-chord elimination, the
component error \(c_I/D\), the perimeter inequality \(b\ge P_F\), the degree
inequality \(Q\ge f\), and the train-boundary inequality all asymptotically tight.

If the two lower bounds in (TC.10) meet exactly, then

\[
{f\over D}\to
{4\sqrt{\pi/(2\sqrt3)}-\pi\over5}
=0.1335317\ldots.
\tag{TC.15}
\]

This is a boundary/interface endpoint, not a bulk low-surplus endpoint.

The stronger floor removes the earlier \(\mu_D=1\) equality analysis entirely.
The live full-core obstruction is now

\[
\mu_D\ge1.637562\ldots
\quad\Longrightarrow\quad
\text{exclude the high-surplus detour/interface branch}.
\tag{TC.16}
\]

Sections 122--123 still leave the exact source-level residual
\[
\sum_r(L_r-2d_r)
\]
coupled to \(e_{BB}-k\). The present floor does not upper-bound that residual, force
an exact unit equilateral triangle, or construct a strict same-cardinality
sub-\(D(n)\) competitor.

## 6. Scope and dependency audit

| Claim | Status | Dependencies | Scope |
| --- | --- | --- | --- |
| Full-core force hull tends to a radius-\(D/2\) disk | canonical | C-FULLCORE-NEAR-DISK | full source retained |
| Loaded-loaded unit chord is a hull side | proved in this report | convexity, unit separation, (TC.1) | full-core near-disk only |
| \(c_B=0,\ e_{BB}=q-m_B\) | proved in this report | Section 63 definitions | loaded hull only |
| \(c_I=O(D^{2/3})\) | canonical | C-COMP-DEATOMIZATION / Section 75 | nonisolated positive-contact components |
| \(q-k\ge(P_F+Q)/2\) | canonical exact algebra | Section 63 | occurrence-counted outer walk |
| \(q-k+2f\ge2\sqrt{R_4}\) | canonical | C-TRAIN-INTERFACE-CURRENCY / Section 85 | all strict rhombi, holes/components allowed |
| Full-core floor (TC.13) | proved candidate | preceding rows | asymptotic Type-II full-core branch |
| Level-I/C-II closure | not proved | missing detour/deformation/triangle bridge | both branches remain open |

No ZR/ZF affine-kernel extension to contact isolates is used.

## 7. Regression checks

* Perfect-matching diameter graph: the canonical exclusion of the exact perfect
  matching remains intact. The new floor does not infer perfect matching from a
  scalar limit.
* Near-disk vanishing-shear lattice: it can satisfy the local chord geometry but
  is not a global minimizer and supplies no source-level competitor.
* Loaded interior chords: these are precisely the case eliminated by the near-disk
  lemma; away from the full-core disk limit the lemma is not claimed.
* Contact-isolated source points: none are deleted, counted as loaded, or put into
  the affine kernel.
* Repeated vertices and bridges: \(b\) is the occurrence-counted canonical outer
  walk; only \(b\ge P_F\) is used.
* Boundary-order loss: constants \(4\), \(c_I\), and all finite terms are retained
  before division by \(D\).
* Global optimality: the new result is a necessary inequality for canonical
  global-minimizer representatives; it is not itself a strict competitor theorem.

## 8. Literature and computation

No external theorem or computation is load-bearing. The only imported inputs are
canonical repository theorem IDs listed in Section 6 and elementary convex
perimeter/isodiametric facts.

## 9. Corrections / supersessions

This report supersedes the weaker unreviewed endpoint description in
target_c_fullcore_loaded_chord_elimination_2026-09-14.md: the \(\mu_D=1\) endpoint
is already excluded by (TC.13). The earlier loaded-chord proof remains the
geometric ingredient, while its endpoint discussion should be read as provenance
for the pre-coupling state, not as the current best floor.

The claim is now registered as `C-FULLCORE-TRAIN-SURPLUS-FLOOR` in the audit.49
state manifest. The report itself remains a proof artifact; the manifest and route
map control its theorem authority.

## 10. Promotion recommendation

canonical in the audit.49 manifest; the surrounding report is not a Level-I closure.

The algebraic coupling is short and exact, but the near-disk loaded-chord lemma
should receive an independent hostile audit before promotion. Promotion would
advance the full-core scalar frontier but would not close C-II or Level I.

## 11. Handoff

1. Strongest new theorem: \(\liminf\mu_D\ge\mu_{\mathrm{TC}}=1.637562184\ldots\)
   in the canonical full-core branch.
2. Dependency chain: C-FULLCORE-NEAR-DISK + Section 63 + C-COMP-DEATOMIZATION +
   C-TRAIN-INTERFACE-CURRENCY.
3. Exact remaining lemma: couple the high-surplus train/interface currency to the
   occurrence-counted aggregate detour, an exact triangle, or a strict
   source-preserving diameter decrease.
4. Binding dead routes: scalar optimization without embedding, density-only affine
   comparisons, contact creation without force transfer, and full-source affine-kernel
   extension.
5. Read next: docs/targets/target-c/122-aggregate-two-arc-detour-audit.md,
   docs/targets/target-c/123-augmented-cell-defect-budget-audit.md,
   docs/targets/target-c/85-train-boundary-interface-currency-audit.md, and
   docs/reports/target_c_isolate_paid_aggregate_detour_2026-09-14.md.
