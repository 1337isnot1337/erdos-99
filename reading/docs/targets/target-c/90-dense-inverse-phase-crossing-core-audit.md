> Generated reading edition · [exact source](../../../../docs/targets/target-c/90-dense-inverse-phase-crossing-core-audit.md) · source SHA-256 `f2bd8ce7d24a4677e74e7a6126ef3b52417cba4d9f07d2758450bc3ceaeeecc0`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target C — dense inverse-diameter phase core without Fox--Pach

**Date:** 2026-09-12
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

Canonical `C-HARMONIC-WRAPPING` supplies, in the full-core near-disk Type-II branch, one macroscopic harmonic cell whose strict-rhombus population is quadratic and whose local rhombic filling tends to one. Canonical `C-HARMONIC-CARRIER-QUAD` gives only `O(D)` local train segments in that cell, while canonical `C-PUNCTURED-PHASE` gives only `O(D)` total angular defect over **all** strict rhombi.

Those three facts already force a much denser phase-collapsed train object than the current handoff records. No Fox--Pach biclique theorem is needed.

The output is not a complete grid. It is a bipartite train-crossing graph with

- linear-sized shores;
- quadratic many actual crossing rhombi;
- linear minimum degree; and
- all train reduced phases in one interval of width `O(1/D)`.

Thus a constant fraction of one macroscopic carrier can be retained at inverse-diameter phase scale before any complete-biclique extraction.

---

# 90. Dense inverse-diameter phase-collapsed crossing core

Work along a canonical Type-II survivor sequence and choose the harmonic cells `P_D` supplied by `C-HARMONIC-WRAPPING`. Let `mathcal R_D` be the full strict-rhombus complex carried by `P_D`, and let

$$
R_D:=|\mathcal R_D|,
\qquad
T_D:=\text{total number of local train segments in }\mathcal R_D.
$$

The canonical carrier conclusions imply that there are fixed constants

$$
r>0,
\qquad
C_T>0
\tag{90.1}
$$

such that, for all sufficiently large members of the selected sequence,

$$
\boxed{R_D\ge rD^2,\qquad T_D\le C_TD.}
\tag{90.2}
$$

One may take `C_T=10 pi` from the coarse canonical Section-82 estimate `P_R<=20a`, because `2T_D=P_R`, `a<=q`, and `q<=pi D`. No use of Section 89 is needed.

Canonical Section 68 gives a fixed constant `C_phase` such that the total acute-angle defect over the entire source satisfies

$$
\boxed{
\sum_R\delta_R\le C_{phase}D.
}
\tag{90.3}
$$

The sum over `mathcal R_D` is therefore bounded by the same quantity.

## 90.1 Remove only a fixed fraction of carrier crossings

Apply the canonical phase-circle cut. It deletes only `O(D)` crossing rhombi and assigns every remaining global train direction a real reduced phase

$$
x_\tau\in(s,s+\pi/3).
\tag{90.4}
$$

Every local train segment inherits the phase of its global train. Every retained oriented crossing edge `uv` satisfies

$$
x_v-x_u=\delta_e>0.
\tag{90.5}
$$

Also assign to each train the unique phase label

$$
\ell(\tau)\in\mathbb Z/3\mathbb Z
\tag{90.6}
$$

such that its projective direction is congruent to

$$
x_\tau+\ell(\tau){\pi\over3}\pmod\pi.
\tag{90.7}
$$

At every retained crossing the two labels are distinct. There are only three unordered label pairs.

Because the phase cut deletes only `O(D)` rhombi, after increasing the lower threshold on `D` we may retain at least

$$
{3r\over4}D^2
\tag{90.8}
$$

carrier crossings.

Fix a constant `K>0` and call a retained crossing **K-good** when

$$
\delta_e\le {K\over D}.
\tag{90.9}
$$

By (90.3), the number of retained crossings violating (90.9) is at most

$$
{C_{phase}D\over K/D}
={C_{phase}\over K}D^2.
\tag{90.10}
$$

Choose once and for all

$$
K\ge {4C_{phase}\over r}.
\tag{90.11}
$$

Then at least

$$
\boxed{{r\over2}D^2}
\tag{90.12}
$$

carrier crossings are K-good for all sufficiently large `D`.

One unordered phase-label pair therefore supports at least

$$
\boxed{E_0\ge {r\over6}D^2}
\tag{90.13}
$$

K-good crossings. Denote the two corresponding train shores by `A` and `B`, and retain only those K-good crossing edges.

Canonical train pseudosegment geometry implies that two train segments cross at most once, so this is a simple bipartite graph.

## 90.2 Random phase bins retain a fixed fraction of those crossings

Put

$$
h:={K\over D},
\qquad
W:=4h={4K\over D}.
\tag{90.14}
$$

For a shift `t in [0,W)`, partition the real reduced-phase axis into half-open bins

$$
I_j(t)=[t+jW,t+(j+1)W).
\tag{90.15}
$$

For one K-good edge `ab`, equation (90.5) gives

$$
|x_a-x_b|\le h.
$$

As `t` is uniform in `[0,W)`, a bin boundary separates the two endpoint phases with probability exactly `|x_a-x_b|/W`, hence at most `1/4`. Therefore the expected number of K-good edges whose endpoints lie in one common bin is at least `3E_0/4`.

Choose a shift attaining at least this expectation. Then the total number of **internal-bin** edges satisfies

$$
\boxed{
E_{bin}\ge {r\over8}D^2.
}
\tag{90.16}
$$

For each occupied bin `I_j`, let

$$
a_j:=|A\cap I_j|,
\qquad
b_j:=|B\cap I_j|,
\qquad
e_j:=\#\{K\text{-good edges internal to }I_j\}.
\tag{90.17}
$$

The total number of local train segments is at most `C_TD`, so

$$
\sum_j a_j\le C_TD,
\qquad
\sum_j b_j\le C_TD.
\tag{90.18}
$$

## 90.3 One inverse-diameter phase bin has linear shores and quadratic crossing mass

Set

$$
\gamma:={r\over8},
\qquad
\alpha:={\gamma\over4C_T}={r\over32C_T}.
\tag{90.19}
$$

Call a bin **large on both shores** when

$$
a_j\ge\alpha D,
\qquad
b_j\ge\alpha D.
\tag{90.20}
$$

The edges in bins with `a_j<alpha D` satisfy

$$
\sum_{a_j<\alpha D}e_j
\le
\sum_{a_j<\alpha D}a_jb_j
\le
\alpha D\sum_jb_j
\le
\alpha C_TD^2.
\tag{90.21}
$$

Among the remaining bins, those with `b_j<alpha D` similarly carry at most

$$
\alpha C_TD^2.
\tag{90.22}
$$

By the definition of `alpha`, the two small-shore classes together carry at most

$$
2\alpha C_TD^2={\gamma\over2}D^2.
\tag{90.23}
$$

Equation (90.16) therefore implies that bins large on both shores carry at least

$$
{\gamma\over2}D^2
\tag{90.24}
$$

K-good edges in total.

There are at most

$$
{C_TD\over\alpha D}={C_T\over\alpha}
={4C_T^2\over\gamma}
\tag{90.25}
$$

such bins. Hence one bin `I_*` satisfies simultaneously

$$
\boxed{|A_*|,|B_*|\ge\alpha D}
\tag{90.26}
$$

and

$$
\boxed{
e(A_*,B_*)\ge\eta D^2,}
\qquad
\eta:={\gamma^2\over8C_T^2}>0.
\tag{90.27}
$$

Every train in `A_* union B_*` has reduced phase in the same interval `I_*` of length

$$
\boxed{|I_*|={4K\over D}.}
\tag{90.28}
$$

Every edge counted in (90.27) is an actual strict-rhombus crossing inside the same harmonic cell and has individual angular defect at most `K/D`.

This is already an explicit dense inverse-diameter phase core. It does not use a complete-biclique theorem.

## 90.4 Robustify to linear minimum degree

The core can be made robust. Let

$$
N_*:=|A_*|+|B_*|\le 2C_TD.
\tag{90.29}
$$

Starting from the graph in (90.27), repeatedly delete any vertex whose current degree is smaller than

$$
\kappa D,
\qquad
\kappa:={\eta\over2C_T}>0.
\tag{90.30}
$$

If every vertex were deleted, the total number of deleted edges would be strictly less than

$$
N_*\kappa D
\le 2C_TD\,{\eta\over2C_T}D
=\eta D^2,
$$

contradicting (90.27). Thus a nonempty bipartite subgraph `G_*` survives and obeys

$$
\boxed{\delta(G_*)\ge\kappa D.}
\tag{90.31}
$$

Consequently both surviving shores have at least `kappa D` vertices, and

$$
\boxed{e(G_*)\ge\kappa^2D^2.}
\tag{90.32}
$$

All surviving train reduced phases remain in the same interval of width `4K/D`, and every retained edge remains K-good.

We have therefore proved:

> **Dense inverse-phase core theorem.** In every sufficiently large canonical Type-II survivor, one Section-88 macroscopic harmonic cell contains two fixed phase-label families of local trains and a bipartite crossing subgraph with linear minimum degree, quadratic edge count, and total reduced-phase spread `O(1/D)`. Every retained edge is an actual carrier rhombus of defect `O(1/D)`.

## 90.5 Relation to the existing complete-grid route

Canonical Section 73 plus Fox--Pach extracts a linear-by-linear **complete** crossing grid, but its numerical shore coefficient contains the external constant `c_PS`. Section 90 proves a different statement:

- no complete bipartite structure is asserted;
- the retained edge count is a fixed positive fraction of `D^2`;
- both shores and every vertex degree are linear in `D`;
- the entire vertex phase set, not merely the crossing edges, lies in one inverse-diameter phase interval.

Thus the remaining Type-II obstruction can be restated without the unknown Fox--Pach constant:

```text
one >=0.8896708101D harmonic carrier
+ one dense bipartite pseudosegment crossing core
+ minimum degree Omega(D)
+ Theta(D^2) actual crossing rhombi
+ all train phases in one O(1/D) interval
+ local train/area budget from Section 89
 -> missing: convert dense near-triangular crossing coverage into
    a diameter contradiction, a large ordered near-Cartesian block,
    or a source-preserving strict competitor.
```

A dense graph need not contain a complete bipartite graph with a useful explicit linear coefficient, so Section 90 does not claim that the Section-76 complete-grid diameter inequality applies to all retained edges at once.

## 90.6 Dependency audit

- **Canonical `C-HARMONIC-WRAPPING` / Section 88:** supplies one harmonic cell with `R_D=Omega(D^2)` strict rhombi and local filling fraction `1-o(1)`.
- **Canonical `C-HARMONIC-CARRIER-QUAD` / Section 82:** supplies `T_D=O(D)` local train segments; the coarse canonical `P_R<=20a` is sufficient.
- **Canonical `C-PUNCTURED-PHASE` / Section 68:** supplies the `O(D)` phase-cut deletion, real reduced phase potential, phase labels, and total angular-defect budget `sum delta_R=O(D)`.
- **Canonical train pseudosegment theorem:** two train segments cross at most once, so every phase-pair crossing graph used above is simple.
- **Section 89 is not required.** Its sharper `T_R<=6a+O(1)` estimate can improve the constants `C_T,alpha,eta,kappa`, but is not part of this proof.
- **Sections 84–85 are not used.**

**Status:** canonical; promoted by the independent Sections-90–94 audit.
**Theorem state:** `2026-09-11.audit.36`.
