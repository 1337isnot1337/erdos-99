> Generated reading edition · [exact source](../../../docs/reports/target_c_d6_symmetric_affine_window_comparison_2026-09-14.md) · source SHA-256 `095f555118a87d1b30ef8a8224d05dabd7a7d3cc5b299c9ff7b583a3ad34b656`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 1 paragraph(s) with malformed inline math are preserved as explicit source excerpts rather than guessed equations.

<!-- theorem-state: {"artifact_id":"ART-C5D0BDEC5BA5","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — exact (D_6)-symmetric affine-window comparison

**Date:** 2026-09-14
**Repository commit:** `ef941ab2b44aa393bdc461926769247b45754202`
**State version:** `2026-09-12.audit.46`
**Run type:** closing proof / exact comparison / adversarial audit
**Target:** C-II / Level I
**Starting status:** canonical C-II frontier through normalized Sections 122–123; both C-II branches open
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md`
**External literature search:** used for status only; no theorem imported
**Computation:** used — `research/verify_target_c_d6_affine_window_comparison.py`

## LEVEL I STATUS

`STILL OPEN`

This report proves an exact global-minimality exclusion for a broad but explicitly
restricted affine-lattice class. It does not prove that every triangle-free global
minimizer belongs to that class, and it does not construct a disproof family.

## 1. Starting canonical endpoint

The active C-II route still requires a source-level implication from the full-core
or macroscopic-container branch to either an exact unit equilateral triangle or a
same-cardinality configuration of diameter strictly below (D(n)). In the full-core
branch, the preferred unresolved quantity is the aggregate outer-walk detour

```math
\sum_r(L_r-2d_r),
```

after the canonical Sections 122–123 detour/payment bookkeeping.

The exact candidate chain for the result below is

```text
D6-invariant affine index window with a non-equilateral unit basis
    -> same-cardinality equilateralized affine source
    -> strict diameter decrease
    -> exclusion of that restricted source from global minimizers.
```

This chain is source-level and exact, but its first hypothesis is not supplied by
the current C-II theorem stack.

## 2. Strongest genuinely new result

**Classification:** proved candidate awaiting promotion; not canonical.

### Theorem — rotationally symmetric affine windows are not optimal when sheared

Let (S\subset\mathbb Z^2) be finite with (|S|\ge2), and suppose its difference
set (Delta=S-S) is invariant under

```math
 r(i,j)=(-j,i+j).
```

Let (c\in(-1/2,1/2)), and let (u,v_c\in\mathbb R^2) be unit vectors with

```math
u\cdot v_c=c.
```

Define

```math
A_c(S)=\{iu+jv_c:(i,j)\in S\},
\qquad
q_c(i,j)=i^2+j^2+2cij.
```

Then:

1. (A_c(S)) is unit-separated. If the four basis differences occur, its
   unit-contact graph is a subgraph of the square grid and is triangle-free.
2. If (D_c=\operatorname{diam}A_c(S)) and (D_{\rm eq}) is the diameter of
   the same index set under the equilateral metric (q_{1/2}), then
   
   ```math
   \boxed{
   D_c^2\ge {4-2c\over3}\,D_{\rm eq}^2.
   }
   ```

3. Since (c<1/2), the factor is (>1), and hence
   
   ```math
   \boxed{D_{\rm eq}<D_c.}
   ```

   The equilateralized source has the same cardinality and remains unit-separated.

Therefore no non-equilateral (D_6)-difference-symmetric affine source in this
range is a global minimum-diameter configuration for its cardinality. The strict
comparison is valid for every finite (S) in the stated class; no asymptotic
argument is used.

Here “(D_6)-difference-symmetric” means invariance under the six rotations generated
by (r). Full dihedral symmetry of (S) is a sufficient stronger hypothesis.

### Proof

The matrix of (q_c) is

```math
G_c=\begin{pmatrix}1&c\\c&1\end{pmatrix}.
```

First consider unit separation. For a nonzero integer pair ((i,j)), put
(a=|i|), (b=|j|). Since (|2c|<1),

```math
q_c(i,j)\ge a^2+b^2-ab=(a-b)^2+ab\ge1.
```

If (a,b>0), the inequality is strict in the only potentially dangerous case
(a=b=1), because (c\in(-1/2,1/2)); if one coordinate vanishes, the
value is an integer square. In fact, every pair with both coordinates nonzero has
length strictly greater than one. Thus (A_c(S)) is unit-separated, and its only
possible unit differences are ((\pm1,0)) and ((0,\pm1)). The parity of (i+j)
therefore gives a bipartite contact graph, so no unit equilateral triangle can occur.

The rotation (r) has order six, and its orbit on (z=(i,j)) is

```math
(i,j),\ (-j,i+j),\ (-i-j,i),\ (-i,-j),\ (j,-i-j),\ (i+j,-i).
```

A direct expansion gives

```math
\begin{aligned}
\sum_{k=0}^{5}q_c(r^kz)
 &=8i^2+8j^2+(8-4c)ij\\
 &=6\,{4-2c\over3}\,q_{1/2}(z).
\end{aligned}
\tag{D6.1}
```

Let (Delta=S-S). By hypothesis, every (r^kz) belongs to (Delta) whenever
(z\inDelta). Choose (z_0\inDelta) maximizing (q_{1/2}); it is nonzero
because (|S|\ge2). Then

```math
\begin{aligned}
 D_c^2
 &=\max_{z\in\Delta}q_c(z)\\
 &\ge\max_{0\le k<6}q_c(r^kz_0)\\
 &\ge {1\over6}\sum_{k=0}^{5}q_c(r^kz_0)\\
 &={4-2c\over3}q_{1/2}(z_0)\\
 &={4-2c\over3}D_{\rm eq}^2.
\end{aligned}
```



**Source formatting excerpt (unbalanced inline math in the original):**

```text
Because (c<1/2), ((4-2c)/3>1). Also (D_{\rm eq}>0), so
(D_{\rm eq}<D_c). The equilateralized set is unit-separated because
(q_{1/2}(i,j)\ge1) for every nonzero integer pair. It has exactly (|S|) points,
which proves the theorem. \(\square)
```



## 3. Scope and exact global-minimality consequence

The theorem is genuinely stronger than a density comparison:

- the two sources have exactly the same finite cardinality;
- both satisfy all pairwise unit-separation constraints;
- the diameter inequality is strict and certified algebraically;
- the comparison does not assume that either source is locally jammed or globally
  optimal;
- no contact-isolated points are deleted because the theorem compares the entire
  affine source (A_c(S)) to its equilateralized copy.

If (A_c(S)) were a triangle-free global minimizer, the equilateralized copy would
be a feasible (|S|)-point source with diameter (<\operatorname{diam}A_c(S)), a
direct contradiction. This use of global optimality is exact.

The theorem includes the usual axial hexagonal window as a special case, and also
applies to arbitrary finite windows whose difference set has the required sixfold
rotational symmetry. It can therefore be used whenever a future source-level
rigidity theorem supplies an affine coordinate chart and sixfold difference symmetry.

## 4. Why this does not close C-II

The current canonical C-II modules do not prove any of the following:

1. every locally rhombus-saturated coherent grain is an affine lattice patch;
2. its finite index difference set has sixfold rotational symmetry;
3. holes, phase interfaces, loaded attachments, and contact-isolated source points
   can be reflected/rotated while preserving the complete source cardinality;
4. an arbitrary source can be replaced by an equilateralized affine copy without
   changing its index set.

The strongest canonical full-core result instead gives a quadratic coherent grain
with a boundary-order interface, and the current regressions explicitly allow
vanishing shear, non-hexagonal windows, holes, and asymmetric boundaries. The
square-grid attachment regression also shows that local harmonic equilibrium and
triangle-freeness do not supply the needed window symmetry.

Thus the theorem eliminates a restricted affine-symmetric subbranch, not the full
Type-II branch. It has no implication for the macroscopic inactive chamber/exterior
cap branch.

## 5. Claim audit table

| Claim | Status | Dependencies | Reason |
|---|---|---|---|
| Unit separation for (c\in(-1/2,1/2)) | proved candidate | elementary quadratic form | (q_c(i,j)\ge(a-b)^2+ab\ge1) |
| Bipartite contact graph | proved candidate | preceding exact contact classification | parity of (i+j) |
| Six-orbit averaging identity | proved candidate | direct expansion | equation (D6.1) |
| Strict same-cardinality diameter reduction | proved candidate | difference-set invariance; averaging | factor ((4-2c)/3>1) |
| Exclusion from global minimizers in the stated class | proved candidate | definition of (D(n)) | equilateralized source is feasible and strictly smaller |
| Every C-II full-core source has this form | unresolved | none | current theorem stack permits holes/asymmetric windows/interfaces |
| Level I | open | original quantifiers | restricted affine theorem is insufficient |

## 6. Regression checks

| Regression/correction | Result | Exact hypothesis or failure |
|---|---|---|
| Near-equilateral triangle-free shear | pass | (c\uparrow1/2) remains in the strict unit-separated range and the factor tends to (1) from above; no fixed gap is claimed |
| Existing oblique-hexagon comparison | subsumed | the axial hex window has sixfold difference symmetry; its sharper formula is compatible with (D6.1) |
| Non-hexagonal affine windows | retained | the theorem assumes difference-set symmetry and makes no claim outside it |
| Local/jammed versus global optimality | pass | the proof uses an explicit same-cardinality feasible competitor, not local rigidity |
| Contact-isolated source points | pass | the comparison is between full finite affine sources; no source coordinates are dropped |
| Boundary/interface/holes | retained | none are silently treated as symmetric or absent |
| Source/scaffold distinction | pass | (A_c(S)) is an actual source in the theorem, not a carrier or response scaffold |
| Full-source ZR/ZF scope | pass | no stress matrix or affine-kernel statement is extended to isolated points |
| Exact source cardinality | pass | both sources have (|S|) points |
| Strict diameter condition | pass | (D_{\rm eq}\le D_c/\sqrt{(4-2c)/3}<D_c) |

The exact certificate also tests negative, zero, and positive rational shears inside
the full strict range. No floating-point arithmetic is used.

## 7. Literature imports

No theorem is imported. A targeted status check of the official Problem #99 entry
still lists the problem as open and identifies Thue’s triangular-lattice construction
as an asymptotic benchmark, not an every-minimizer theorem. The cited status source
is [Erdős Problems #99](https://www.erdosproblems.com/99). The external source is not
used in the proof.

## 8. Computation

The command is:

```text
python3 research/verify_target_c_d6_affine_window_comparison.py
```

It checks:

- the six-orbit identity (D6.1) for all integer pairs in a finite box and three
  exact rational values of (c);
- exact difference-set rotational symmetry for several finite orbit-closed windows;
- exact unit separation in each sheared metric;
- the averaged diameter inequality and strict diameter decrease.

Arithmetic is `fractions.Fraction`; no optimizer or numerical approximation is used.
The script certifies only the displayed finite instances and algebraic identity. It
does not search over arbitrary source configurations, prove global optimality for a
cardinality, or settle the original Level I quantifiers.

## 9. Corrections / supersessions

This report does not correct a canonical theorem. It strengthens the existing
restricted oblique-hexagon comparison by replacing one prescribed axial window with
any finite index set whose difference set is invariant under the six triangular
rotations. It does not supersede the vanishing-shear regression or the residual
non-hexagonal-window obstruction.

## 10. Promotion recommendation

**unreviewed / proved candidate awaiting independent audit.**

No `state_version`, route map, active prompt, or canonical theorem module should be
changed from this report alone. If independently audited and promoted, the theorem
should be registered as a restricted C-II global-minimality exclusion with no claim
about arbitrary full-core sources or the macroscopic-container branch.

## 11. Handoff

1. **Strongest new theorem:** every finite non-equilateral affine source with
   sixfold rotationally symmetric index difference set is beaten, at the same
   cardinality, by its equilateralized source; the exact factor is
   ((4-2c)/3).
2. **Canonical dependency chain:** elementary quadratic-form and six-orbit averaging;
   the canonical C-II stack is motivation only, not a premise of the proof.
3. **Exact remaining lemma:** prove an affine-chart plus sixfold difference-symmetry
   theorem for every triangle-free global minimizer in the full-core branch, or
   replace it with a source-preserving deformation that handles asymmetric windows,
   holes, interfaces, and the macroscopic inactive branch.
4. **Binding dead routes:** density-only angle gaps, local harmonic equilibrium,
   one-point cap covering, and arbitrary-window equilateralization are all
   insufficient; the theorem uses its symmetry hypothesis explicitly.
5. **Files to read next:** `docs/targets/target-c/CURRENT.md`,
   `docs/targets/target-c/122-aggregate-two-arc-detour-audit.md`,
   `docs/targets/target-c/123-augmented-cell-defect-budget-audit.md`, and the
   Target A current endpoint if attempting a source/response transfer.

## 12. Final verification

The final repository checks for this run were:

```text
python3 tools/build_artifact_index.py --write --write-headers
python3 tools/check_theorem_state.py
python3 research/verify_target_c_d6_affine_window_comparison.py
```

The artifact index was regenerated with 905 records, the theorem-state checker
returned `theorem-state: OK`, and the exact D6 certificate passed. The relevant
existing exact regression scripts for the oblique hexagon, scalar ledger,
saturated chamber, multigrain endpoint, and co-embedded protected cover also
returned `PASS`.

The aggregate certificate runner was attempted separately. Its first certificate
passed, but the runner stopped at the historical `q=13` shell regression because
this environment has no `sympy` module. That dependency failure does not affect the
elementary proof above; the unavailable regression was not treated as a theorem or
as evidence for Level I.
