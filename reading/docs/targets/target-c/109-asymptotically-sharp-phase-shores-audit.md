> Generated reading edition · [exact source](../../../../docs/targets/target-c/109-asymptotically-sharp-phase-shores-audit.md) · source SHA-256 `030adb56eceb6396b339b065550a3952774a84991c9ed2fded78fecd34bf631f`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target C — baseline inverse-phase shore extraction

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Status:** canonical from theorem-state `2026-09-12.audit.45`.

This module records the valid content of the former “asymptotically sharp” Section 109 and removes its false sharpness claim. The separate-shore counting proof below gives the baseline coefficient

$$
a<{r\over6C_T}.
$$

It does **not** prove that this coefficient is optimal. Canonical Section 111 uses the fact that the two selected phase-label shores are disjoint subsets of the same local train set and improves the threshold to

$$
a<{r\over3C_T}.
$$

The Section-109 numerical consequence remains valid as a historical quantitative waypoint; Section 111 and later sections supersede it.

---

# 109. Baseline shore extraction and the `5e-5` phase window

Consider one locally rhombus-saturated harmonic carrier. Let

- `R_D` be its number of strict unit rhombi;
- `T_D` be its number of full local train segments; and
- `Delta_D=sum_R delta_R` be the total acute-angle defect.

Assume fixed constants `r,C_T,C_phase>0` such that, for all sufficiently large `D`,

$$
R_D\ge rD^2,
\qquad
T_D\le C_TD,
\qquad
\Delta_D\le C_{phase}D.
\tag{109.1}
$$

## 109.1 Baseline shore lemma

### Lemma 109.1

For every fixed

$$
0<a<{r\over6C_T},
\tag{109.2}
$$

there are, for all sufficiently large `D`, two fixed distinct phase labels and two families `A_D,B_D` of full local train segments such that

$$
|A_D|,|B_D|\ge aD,
\tag{109.3}
$$

all their reduced phases lie in one interval of width `O(1/D)`. Their limiting projective directions therefore differ by `pi/3`.

### Proof

Apply the canonical Section-90 phase-circle cut. It deletes only `O(D)` crossing rhombi, so the retained crossing count is

$$
(r-o(1))D^2.
\tag{109.4}
$$

Fix a large constant `K`. Call a retained crossing `K`-good when its angular defect is at most `K/D`. Markov's inequality and (109.1) show that at most

$$
{C_{phase}\over K}D^2
$$

retained crossings are not `K`-good. One of the three unordered phase-label pairs therefore carries at least

$$
\left({r-C_{phase}/K\over3}-o(1)\right)D^2
\tag{109.5}
$$

`K`-good crossings.

Fix an integer `m>=2` and randomly shift reduced-phase bins of width

$$
W={mK\over D}.
\tag{109.6}
$$

A `K`-good crossing has endpoint phase difference at most `K/D`, so a random bin boundary separates its endpoints with probability at most `1/m`. Some shift therefore leaves at least

$$
\left(1-{1\over m}\right)
\left({r-C_{phase}/K\over3}-o(1)\right)D^2
\tag{109.7}
$$

crossings internal to common bins.

For bin `j`, let `a_j,b_j` be the two fixed-label shore sizes and `e_j` its internal crossing count. The train pseudosegment theorem makes the crossing graph simple, so

$$
e_j\le a_jb_j.
$$

Also

$$
\sum_j a_j\le C_TD,
\qquad
\sum_j b_j\le C_TD.
\tag{109.8}
$$

If every occupied bin had `a_j<aD` or `b_j<aD`, then bins small on the first shore carry at most `aC_TD^2` crossings, and the remaining bins that are small on the second shore carry at most another `aC_TD^2`. Thus all internal-bin crossings total at most

$$
2aC_TD^2.
\tag{109.9}
$$

Because `2aC_T<r/3`, choose `K` and then `m` sufficiently large that the leading coefficient in (109.7) exceeds `2aC_T`, and then take `D` large enough to absorb the `o(1)` term. Equation (109.9) is impossible. Hence one bin has both shores at least `aD`.

Its width is a fixed constant divided by `D`, so both reduced-phase families collapse to one limit. Distinct labels differ projectively by `pi/3`. `square`

The factor `1/6` is a **baseline produced by the separate-shore split in (109.9)**. It is not a sharp limit. Canonical Section 111 replaces (109.9) by a joint capacity estimate and reaches `a<r/(3C_T)`.

## 109.2 Explicit baseline on the Section-107 carrier

Canonical Section 107 gives, throughout its stated scalar window, the conservative finite mass bound

$$
R_D\ge0.472D^2.
\tag{109.10}
$$

Canonical Sections 68 and 89 give

$$
T_D\le6D,
\qquad
\Delta_D<5.317D.
\tag{109.11}
$$

Thus Lemma 109.1 permits every

$$
a<{0.472\over36}=0.013111\ldots .
$$

The historical choice

$$
a=0.0131
\tag{109.12}
$$

is therefore valid. Each selected train has two distinct physical boundary-end occurrences, so each phase family supplies at least `0.0262D` train endpoints.

Combining this endpoint supply with the already-audited Section-104/105 leakage geometry and the exact principal-route excess budget proves the historical Section-109 window

$$
\sigma(\theta)\le5\times10^{-5},
\qquad
\sigma(\theta)=3\theta-2\pi-\sin(\theta/2)-2\sin\theta,
\tag{109.13}
$$

and hence the carrier waypoint

$$
\operatorname{diam}(P_*)
\ge(0.9760419221833405\ldots-o(1))D.
\tag{109.14}
$$

This numerical conclusion is valid but superseded by later canonical sections.

## 109.3 Dependency and correction audit

- **Canonical Section 90 / `C-DENSE-PHASE-CORE`:** phase-circle cut, simple crossing graph, and reduced-phase relation.
- **Canonical Section 107 / `C-WRAP-AREA-RIGIDITY`:** local strict-rhombus mass `R_D>=0.472D^2` in the required window.
- **Canonical Section 89 / `C-HARMONIC-TRAIN-BUDGET`:** `T_D<=6D` at this stage.
- **Canonical Section 68 / `C-PUNCTURED-PHASE`:** total angular-defect budget.
- **Canonical Section 105 / `C-ROUTE-EXCESS-OPT`:** route-excess/leakage handoff for the historical `5e-5` consequence.
- **Canonical Section 111 / `C-JOINT-PHASE-SHORES`:** strict improvement of the shore coefficient; it is not a premise of Lemma 109.1.
- **Contact-isolated source points:** untouched.

**Binding correction:** every former statement that `r/(6C_T)` is “sharp”, “optimal”, or “the limit of the method” is withdrawn. The theorem proved here is only the baseline sufficient bound (109.2).

**Theorem state:** canonical as `C-PHASE-SHORE-BASELINE` from `2026-09-12.audit.45`. C-II remains open.
