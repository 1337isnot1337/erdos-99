# Hostile audit — terminal saturation or fixed-aperture vanishing-mass corridor

**Date:** 2026-09-17  
**Reviewed:** `research/target_c_high_t_terminal_or_fixed_aperture_corridor_t18687_2026-09-17.md`  
**Certificate:** `research/verify_target_c_high_t_terminal_or_fixed_aperture_corridor_t18687.py`  
**Disposition:** **PASS at proof-only high-`t` scope, with the construction-level interpretation of the near-full survivor set made explicit below.**  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The candidate synchronizes three facts that were previously proved on related but not identical subfamilies:

1. the near-full paired population has the full-parent non-TT aperture `nu-o(1)`, where
   \[
   \nu={113\over10{,}000{,}000};
   \]
2. a one-sided shore has total switching KKT mass at most one; and
3. a long consecutive exact-phase low-complexity block inherits the coercive cancellation kernel and almost-full common train grid.

The only genuinely delicate point is whether the near-full paired center set has `o(D)` **physical holes**, rather than merely cardinality `(nu-o(1))D`. Cardinality alone would not imply a long consecutive run. The parent construction does provide the stronger hole statement because its survivor set is obtained by explicit deletion from a consecutive shore. With that point fixed, the rest of the synchronization is valid.

---

## 1. The one-sided shore is consecutive

The deep bilateral-force theorem explicitly starts from the **selected consecutive one-sided shore** `I_D` and records

\[
|I_D|>{c\over2}D-o(D),
\qquad
c={113\over5{,}000{,}000}.
\]

Thus physical interface adjacency inside `I_D` is meaningful. No inference from an unordered positive-density set is being made.

**Verdict:** PASS.

---

## 2. The near-full diagonal may be taken as the full deletion survivor set

For fixed diagonal parameter `n`, the full-shore deep-force proof does not obtain its center set by an arbitrary existential selection. It starts from `I_D` and deletes explicit bad sets. With the concrete schedule

\[
r_n=n,
\qquad
m_n=2n+1,
\]

\[
T_{0,n}=41n,
\qquad
T_{r,n}=41m_nn,
\]

and

\[
\rho_n={c\over80n m_n},
\]

the leading deletion bounds are

\[
{c\over T_{0,n}}D={c\over41n}D,
\]

for center-cost failures,

\[
{m_nc\over T_{r,n}}D={c\over41n}D,
\]

for radius-`r_n` separator neighborhoods, and

\[
2m_n\rho_nD={c\over40n}D
\]

for radius-`r_n` neighborhoods meeting a narrow force pair.

There is additionally an `O(r_n)` shore-end loss, at most six unilateral-force centers after gap-free bilateralization, and fixed-`n` `o(D)` remainders from the separator classification. In the diagonal extraction `D_n` is chosen so large that every such fixed-`n` remainder is at most `D_n/n` (or any smaller prescribed diagonal error).

Therefore one may define `Q_n` to be the **entire survivor set after these deletions**, rather than an arbitrary subset satisfying the parent lower bound. Then

\[
|I_{D_n}\setminus Q_n|
\le
\left(
{c\over41n}+{c\over41n}+{c\over40n}
\right)D_n
+o(D_n)
+O(n),
\]

so

\[
\boxed{|I_{D_n}\setminus Q_n|=o(D_n).}
\]

Deleting the at most six remaining unilateral centers to obtain the paired population does not change this conclusion.

This is the construction-level justification for equation (FC.3). If `Q_D` were treated only as an arbitrary existential subset of the cardinality asserted by the parent theorem, (FC.3) would not follow. The candidate uses the actual deletion survivor set, so the stronger statement is valid.

**Verdict:** PASS, with this interpretation required.

---

## 3. A positive-density non-TT suffix contains arbitrarily long physical runs

Terminal membership is a prefix in each paired lane, hence TT membership is a prefix in paired-center order. If the non-TT suffix has

\[
L\ge\varepsilon D,
\]

then the physical interface interval from the first non-TT paired center to the last paired center contains at least `L` good non-TT indices and at most

\[
H_D=o(D)
\]

holes.

Choose `m_D` with

\[
m_D\to\infty,
\qquad
{m_D(H_D+1)\over D}\to0.
\]

The holes divide the good positions into at most `H_D+1` runs. If the run lengths are `q_j`, the number of disjoint length-`m_D` blocks is

\[
K_D=\sum_j\left\lfloor{q_j\over m_D}\right\rfloor.
\]

Since `floor(x)>=x-1`,

\[
K_Dm_D
\ge
\sum_jq_j-(H_D+1)(m_D-1)
\ge
L-(H_D+1)(m_D-1).
\]

Hence

\[
\boxed{
K_D\ge(\varepsilon-o(1)){D\over m_D}\to\infty.
}
\]

The repository certificate exhaustively checks this finite packing inequality for all binary words through length 12 and every admissible block length. The proof itself is the floor inequality above and is exact for all lengths.

**Verdict:** PASS.

---

## 4. The slow block schedule can satisfy both hole and complexity requirements

Let `T_D` denote the fixed constant `C` times the neighborhood threshold on the current diagonal source, so

\[
{T_D\over D}\to0.
\]

Because also `(H_D+1)/D->0`, the choice

\[
m_D=
\left\lfloor
\min\left\{
\sqrt{D\over H_D+1},
\sqrt{D\over T_D+1}
\right\}
\right\rfloor
\]

on a sufficiently large tail satisfies

\[
m_D\to\infty,
\]

\[
{m_D(H_D+1)\over D}
\le
\sqrt{{H_D+1}\over D}
\to0,
\]

and

\[
{m_DT_D\over D}
\le
\sqrt{{T_D+1}\over D}
\to0.
\]

It also gives `m_D/D->0`. Thus the block can grow while both the physical-hole loss and the cumulative crossing-family drift are negligible.

**Verdict:** PASS.

---

## 5. Global KKT mass selects a vanishing-mass block

On one fixed side of the common hub, switching sets at distinct interfaces are pairwise edge-disjoint, and the normalized full-diameter KKT stress satisfies

\[
\sum_iB_i\le1.
\]

The `K_D` physical blocks are interface-disjoint. Therefore one block `J_D` has

\[
\sum_{i\in J_D}B_i\le{1\over K_D}
=O\left({m_D\over D}\right)
\to0.
\]

Using `|G_i|<=DB_i` gives

\[
{1\over D}\sum_{i\in J_D}|G_i|\to0.
\]

No individual multiplier lower bound or probabilistic averaging is used.

**Verdict:** PASS.

---

## 6. The full-parent aperture remains valid after physical block extraction

Every interface retained in `J_D` is itself one of the paired centers in the original ordered population. The full-parent aperture theorem is pointwise over **all** non-TT paired centers:

\[
\eta_i\ge N\delta_D-o(1)
\ge\nu-o(1).
\]

Extracting a physical consecutive subblock does not reset the forward C67 count and does not replace `N` by the block length. Thus the fixed aperture is still the full parent scale `nu`, not `m_D/D`.

For force-coefficient estimates it is legitimate to freeze the smaller fixed value

\[
\rho_*={\nu\over2}
\]

for all sufficiently large sources. Then

\[
\sum_{i\in J_D}(\lambda_i^-+\lambda_i^+)
\le
{2\over\sin(\nu/2)}
\sum_{i\in J_D}B_i
\to0.
\]

**Verdict:** PASS.

---

## 7. Fixed aperture gives a common macroscopic central diamond at every separator

The wide-dipole central-diamond theorem is stated for every fixed `rho>0`. Since

\[
\eta_i\ge\nu-o(1)
\]

uniformly on `J_D`, for each fixed `rho<nu` all sufficiently large sources satisfy `eta_i>=rho` at every interface in the block. Therefore every force quadrilateral contains

\[
B\left(o,{D\over2}\sin{\rho\over2}-L_D\right).
\]

Letting the fixed `rho` approach `nu` after the source limit gives the asymptotic shorthand

\[
\boxed{
B\left(o,\left({1\over2}\sin{\nu\over2}-o(1)\right)D\right)
}
\]

uniformly over the block. This is not an illicit use of the fixed-`rho` theorem with a source-dependent parameter.

The radius coefficient is

\[
{1\over2}\sin{\nu\over2}
=2.82499999998\ldots\times10^{-6}.
\]

The same theorem gives cross-chord endpoint separation

\[
D\sin(\nu/2)-o(D)
=(5.64999999997\ldots\times10^{-6}-o(1))D.
\]

**Verdict:** PASS.

---

## 8. Exact phase and cancellation-kernel coercivity survive the extraction

Every interface in the physical block is exact-antipodal. Adjacent row phases are therefore equal at every separator, so equality propagates through the consecutive block. Its `m_D+1` rows have one common oriented phase.

The switching supports remain disjoint. The existing direct-sum argument applies without any density hypothesis and yields on the entire zero-sum cancellation kernel

\[
\left\|D^{-1}L_D(c)\right\|_2
\ge
(\sqrt2c_H-o(1))\|c\|_2,
\]

with

\[
\sqrt2c_H=0.64179823755\ldots .
\]

The dimension is `m_D->infinity`, while Section 5 gives total KKT mass on the derivative-active switching rows tending to zero.

**Verdict:** PASS.

---

## 9. The almost-full common train family also survives

At every interface in the block the parent diagonal gives

\[
L_i<T_D,
\qquad
S_i+S_{i+1}<T_D.
\]

Let `Gamma_j` be the complete-train crossing family of row `j`. The adjacent-family estimate gives

\[
|\Gamma_j\triangle\Gamma_{j+1}|<T_D.
\]

Across `m_D` interfaces the running intersection therefore loses at most `m_DT_D=o(D)` columns. Starting from the audited row floor `0.6536D-o(D)`, the common family has

\[
(0.6536-o(1))D
\]

columns.

Exact co-phase makes the angular defect of a fixed common column identical on every row. On one row the total defect is below `T_D`; with

\[
\sigma_D=\sqrt{T_D/D}=o(1),
\]

Markov deletes at most

\[
{T_D\over\sigma_D}=\sigma_DD=o(D)
\]

columns. Thus the same `(0.6536-o(1))D` family has uniform `o(1)` defect on every row. The exact train-step/circumdisk argument then gives the common flank density

\[
0.6536-{1.02\over\sqrt3}
=0.0647027254265\ldots
\]

on both sides of the circumcenter coordinate.

No assumption that the original paired centers were consecutive is used here beyond the block-packing step that explicitly creates the physical consecutive block.

**Verdict:** PASS.

---

## 10. Terminal-dominant branch

If the non-TT suffix is `o(D)`, then

\[
M>(\nu-o(1))D.
\]

The established TT-prefix inequality

\[
\operatorname{normalspan}(T_m)
\ge
2\gamma_H+2(M-1)\delta_D-o(1)
\]

and `delta_D>=1/D` give

\[
\boxed{
\operatorname{normalspan}(T_m)
\ge2\gamma_H+2\nu-o(1).
}
\]

The value is

\[
0.9421174460385\ldots\text{ radians}
=53.97935346\ldots^\circ.
\]

Uniform Type-II near-disk convergence transfers the support-normal span to central radial angular span up to `o(1)`, so the corresponding terminal chord lower bound is

\[
\boxed{
\operatorname{diam}(T_m\cap S)
\ge
(\sin(\gamma_H+\nu)-o(1))D
=(0.45382995525\ldots-o(1))D.
}
\]

**Verdict:** PASS.

---

## 11. Scope and remaining seam

The theorem does **not** prove C-II. It does not infer a diameter decrease from small KKT mass, and it does not infer that actual diameter chords cross a selected row near the train-grid crossing centers.

The return-positive branch now has a stronger simultaneous normal form:

```text
unbounded consecutive exact-phase row stack
+ fixed pair aperture >= 1.13e-5-o(1) at every separator
+ one common macroscopic central disk inside every force quadrilateral
+ vanishing total switching KKT mass
+ vanishing total compressed force mass
+ dimension-free cancellation-kernel coercivity
+ (0.6536-o(1))D common near-60-degree columns
+ common positive-density circumcenter flanks.
```

The immediate missing statement is geometric localization: relate the intersection of a switching diameter chord with each train row to the metric crossing-center order of the common columns. The alternative route is an independent upper bound on the far terminal normal span, which would contradict or quantitatively restrict the terminal-dominant branch.

**Final verdict:** PASS at the stated proof-only scope. The construction-level `o(D)` hole property is valid because the near-full center set is taken to be the full survivor set of explicit deletions from the consecutive shore. C-II remains open.