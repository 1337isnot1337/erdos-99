> Generated reading edition · [exact source](../../../docs/reports/target_c_interface_fragmentation_stability_2026-09-09.md) · source SHA-256 `98e78c90bcaa256e1aa36e6d086705de59d4d44ee085a906c2e73c14771478a6`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 21 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-F0EFD35FD40A","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_interface_fragmentation_stability_2026-09-09.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=2554eaff58ea0bd3eb43f628c129e75e87d1f4a6; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — minimal loaded-interface defect forces two individual half-disk harmonic carriers

**Date:** 2026-09-09  
**Repository branch:** `research/fullcore-interface-perimeter-2026-09-09`  
**Run type:** asymptotic equality/stability classification  
**Target:** full-core near-circle endpoint after GP  
**Depends on:** GP group-perimeter theorem, HG two-semicircle groups, C49 interior-disjoint attachment cells, HBd, NC, NBd, ZU, ZT, groupwise Oler  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

GP removes cap minimality from the loaded-interface defect theorem and proves

```math
Q_B\ge(2-o(1))D
```

through a lower bound on the total attachment-cell perimeter. The same argument contains a sharper structural inequality:

```math
\boxed{
Q_B\ge P_A-q-o(D),
\qquad
P_A:=\sum_r\operatorname{per}(P_r).
}
\tag{FS.1}
```

Since HG gives `q=(pi+o(1))D` and `P_A>=(pi+2-o(1))D`, FS.1 recovers GP.2.

The new point is its equality case. If

```math
\frac{Q_B}{D}\to2,
\tag{FS.2}
```

then

```math
\boxed{
\frac{P_A}{D}\to\pi+2.
}
\tag{FS.3}
```

Thus the two dominant semicircle groups have asymptotically no perimeter available for macroscopic fragmentation. A relative-isoperimetric compactness argument forces one attachment cell in each group to occupy asymptotically the whole half-disk. Consequently each group contains one harmonic component with

```math
\boxed{
|I_i|=(\Delta/2+o(1))D^2,
\qquad
\delta_i\ge(1-o(1))D,
\qquad i=1,2.
}
\tag{FS.4}
```

The graph-diameter statement in the first version of this report incorrectly wrote equality `delta_i=(1-o(1))D`. The proof supplies only the displayed lower bound from the attachment diameter. An upper bound `delta_i<=D+o(D)` requires an additional theorem and is **not** a consequence of minimal interface defect alone. This correction also removes the first version's attempted direct use of DS.3, whose semicircle-carrier form assumes `delta_i/D->1` from the separate cap-minimal branch.

Thus minimal loaded-interface defect recovers two individual **half-density, diameter-scale** carriers, but does not yet recover cap minimality of their internal graph metric.

More generally, for every fixed positive population-fragmentation threshold there is a fixed positive interface-defect gap above `2D`.

---

## 1. A direct perimeter-to-interface inequality

Retain the notation of GP. Let

```math
Q_{\rm int}:=\sum_rQ_r,
\qquad
P_A:=\sum_r\operatorname{per}(P_r).
```

GP.3 gives componentwise

```math
k_r\ge\operatorname{per}(P_r)-2\pi.
```

Summing and using `c_I=o(D)` from HBd,

```math
\sum_rk_r\ge P_A-o(D).
\tag{1.1}
```

The exact local face identity gives

```math
R_I
=\frac12\sum_rk_r+\frac12Q_{\rm int}-S,
```

hence

```math
R_I\ge\frac12P_A+\frac12Q_{\rm int}-S-o(D).
\tag{1.2}
```

Insert this into NBd:

```math
S+R_I+s_B+2E_{BB}+3c_I+s_C=q+2x_B.
```

NC/HBd and the near-circle hypothesis give

```math
E_{BB}=o(D),\qquad c_I=o(D),\qquad x_B=o(D).
```

Therefore

```math
\frac12P_A+\frac12Q_{\rm int}+s_C
\le q+o(D),
\tag{1.3}
```

where `s_B>=0` was discarded.

HBd gives

```math
d_H+s_Z=s_C+o(D),
```

and ZT gives

```math
q=x_B+Q+2(d_H+s_Z).
```

Thus

```math
Q=q-2s_C+o(D).
\tag{1.4}
```

Subtract `Q_int` and use (1.3):

```math
\begin{aligned}
Q_B
&=Q-Q_{\rm int}\\
&=q-2s_C-Q_{\rm int}+o(D)\\
&\ge q-2\left(q-\frac12P_A-\frac12Q_{\rm int}\right)-Q_{\rm int}-o(D)\\
&=P_A-q-o(D).
\end{aligned}
```

This proves FS.1.

The estimate is stronger than the scalar `Q_B>=2D-o(D)` because it retains the actual fragmentation perimeter.

---

## 2. Equality in interface defect forces equality in group perimeter

HG gives two dominant maximal-cap groups `G_1,G_2`. GP proves separately

```math
P_i:=\sum_{r\in G_i}\operatorname{per}(P_r)
\ge\left(1+\frac\pi2-o(1)\right)D,
\qquad i=1,2.
\tag{2.1}
```

All other cells have nonnegative perimeter. Hence

```math
P_A\ge(\pi+2-o(1))D.
\tag{2.2}
```

Also

```math
q=(\pi+o(1))D.
\tag{2.3}
```

Suppose FS.2 holds. FS.1 gives

```math
P_A\le Q_B+q+o(D)=(\pi+2+o(1))D.
```

Together with (2.2),

```math
P_A=(\pi+2+o(1))D.
```

Because each `P_i` already has the lower bound (2.1), we necessarily have

```math
\boxed{
P_i=\left(1+\frac\pi2+o(1)\right)D,
\qquad i=1,2,
}
\tag{2.4}
```

and the total perimeter of all cells outside the two dominant groups is `o(D)`.

Thus each dominant group attains the smallest perimeter sum compatible with filling its limiting half-disk.

---

## 3. Relative-perimeter lemma for an asymptotically filled half-disk

Let `H` be the fixed diameter-one closed semicircle. Consider finite families of compact convex polygons

```math
C_{j,1},\ldots,C_{j,m_j}\subset H+o_H(1)
```

with pairwise disjoint interiors, such that their union `E_j` satisfies

```math
|E_j\triangle H|\to0.
\tag{3.1}
```

Assume

```math
\sum_a\operatorname{per}(C_{j,a})
\to\operatorname{per}(H).
\tag{3.2}
```

### Lemma FS.1 — vanishing fragmentation

Then

```math
\boxed{
\max_a|C_{j,a}|\to|H|.
}
\tag{3.3}
```

Equivalently, one cell contains all but `o(1)` of the half-disk area.

### Proof

Suppose not. After a subsequence there is an `eta>0` such that every cell has area at most `|H|-eta`.

Choose a subfamily `U_j` as follows. If one cell has area in `[eta/4,|H|-eta/4]`, take that cell. Otherwise every cell has area below `eta/4`; greedily add cells until the selected area first exceeds `eta/4`. The overshoot is less than `eta/4`, so the selected union has area in `[eta/4,eta/2]`. Since `E_j` fills `H` in measure, its complement inside the family has area bounded below by a positive constant depending only on `eta`.

Thus, in either case, after passing to a further subsequence there is a union `U_j` of whole cells such that both `U_j` and `E_j\setminus U_j` carry a fixed positive area fraction of `H`.

The relative isoperimetric inequality in the fixed Lipschitz domain `H` now gives a constant `c_eta>0` such that the relative perimeter separating these two macroscopic pieces is at least `c_eta`, up to `o(1)` from the vanishing symmetric-difference error in (3.1).

For a finite polygonal partition, every interface edge between selected and unselected cells is counted twice in the sum of cell perimeters but not in the perimeter of the full union. Boundaries facing a gap are also counted in the sum and can only increase the excess. Therefore

```math
\sum_a\operatorname{per}(C_{j,a})
\ge
\operatorname{per}(E_j)+2c_eta-o(1).
\tag{3.4}
```

Perimeter lower semicontinuity under (3.1) gives

```math
\liminf_j\operatorname{per}(E_j)
\ge\operatorname{per}(H).
```

Hence (3.4) contradicts (3.2). This proves the lemma. `square`

The proof also gives the qualitative stability statement: for every `eta>0` there is `epsilon(eta)>0` such that if no cell has area at least `|H|-eta`, then the sum of cell perimeters exceeds `per(H)` by at least `epsilon(eta)` for all sufficiently close half-disk fillings.

---

## 4. Apply the lemma to the two dominant groups

Scale by `D`. HG gives, for each dominant group `G_i`,

```math
E_{i,D}:=D^{-1}\bigcup_{r\in G_i}P_r
\to H_i
\quad\text{in }L^1,
\tag{4.1}
```

where `H_i` is a diameter-one semicircle. Equation (2.4) says

```math
\sum_{r\in G_i}\operatorname{per}(D^{-1}P_r)
\to\operatorname{per}(H_i).
```

Lemma FS.1 therefore gives one component index `r_i(D)` with

```math
\boxed{
\operatorname{area}(P_{r_i})
=\left(\frac\pi8+o(1)\right)D^2.
}
\tag{4.2}
```

All other attachment cells in that group have total area `o(D^2)`.

The dominant cell is contained in the group's limiting semicircle and has asymptotically full semicircle area. Consequently its normalized convex hull itself converges in measure, and by convexity in Hausdorff distance, to that semicircle. In particular its attachment diameter is

```math
(1-o(1))D.
```

C44 gives only

```math
\boxed{
\delta_{r_i}\ge(1-o(1))D.
}
\tag{4.3}
```

No matching upper bound is proved here.

---

## 5. Population concentrates in the same two components

HG gives total unloaded population in group `G_i`

```math
N_i=(\Delta/2+o(1))D^2.
\tag{5.1}
```

Apply the componentwise Oler lower-area estimate and sum it only over the nondominant cells in `G_i`. Their total attachment-cell area is `o(D^2)`. The total component-diameter correction is at most the global `S=O(D)`, and HBd gives `c_I=o(D)`. Therefore the nondominant components contain only

```math
o(D^2)
```

vertices.

Hence the dominant component itself contains

```math
\boxed{
|I_{r_i}|=(\Delta/2+o(1))D^2.
}
\tag{5.2}
```

Together with (4.3), this proves the corrected FS.4.

Thus minimal loaded-interface defect produces two individual positive-density half-disk carriers, but their internal contact-graph diameters may still exceed the Euclidean diameter by a positive linear factor.

---

## 6. Quantitative fragmentation alternative

The relative-isoperimetric proof gives the following useful qualitative dichotomy.

Fix `eta>0`. Then there exists `epsilon_eta>0` such that every sufficiently large full-core near-circle survivor satisfies at least one of:

1. in each dominant semicircle group there is an attachment cell of area at least
   ```math
   \left(\frac\pi8-\eta\right)D^2;
   
   ```
2. the loaded-interface defect satisfies
   ```math
   \boxed{
   Q_B\ge(2+\epsilon_eta-o(1))D.
   }
   \tag{6.1}
   ```

Indeed, failure of the first alternative in either group raises `P_A` by a fixed multiple of `D`; FS.1 transfers that perimeter excess one-for-one into `Q_B`.

No explicit formula for `epsilon_eta` is needed here. A future quantitative version can use the explicit relative isoperimetric constant of a half-disk if a numerical optimization becomes useful.

---

## 7. Correct relation to the stopped-train bound

The first version of this section claimed that DS.3 automatically applies to the two FS carriers. That was incorrect.

DS.3 was proved for the cap-minimal TS/SI carriers and explicitly uses

```math
\delta_i/D\to1
```

when converting the exact identity

```math
r_i=(k_i+Q_i)/2-\delta_i
```

into its first affine lower branch and when converting the stopped-train lower bound into the second branch.

FS supplies

```math
|I_i|=(\Delta/2+o(1))D^2,
\qquad
P_i/D\to H_i,
\qquad
\delta_i/D\ge1-o(1),
```

but does not prove `delta_i/D<=1+o(1)`. Therefore the numerical DS conclusion

```math
Q_B\ge(2.245502\ldots-o(1))D
```

is valid only when the additional cap-minimal graph-diameter hypothesis is available; it cannot currently be imported into FS solely from `Q_B/D->2`.

The corrected equality model therefore retains a new live variable:

```math
\boxed{
\lambda_i:=\limsup\delta_i/D\ge1.
}
```

Controlling these graph-metric stretch factors is a legitimate next target. A theorem forcing `lambda_i=1` would reactivate the full DS envelope in the minimal-interface branch. A construction with `lambda_i>1` would identify a different binding half-disk regression.

---

## 8. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| `Q_B >= P_A-q-o(D)` | proved | GP3 + local Euler + NBd/NC/HBd/ZU/ZT |
| `Q_B/D->2` implies `P_A/D->pi+2` | proved | HG/GP perimeter lower bound + FS.1 |
| minimal group perimeter forces one full-area cell | proved | relative isoperimetric fragmentation lemma |
| dominant component has `(Delta/2+o(1))D^2` vertices | proved | group population + Oler on vanishing-area remainder |
| dominant component has graph diameter at least `(1-o(1))D` | proved | attachment diameter + C44 |
| dominant component has graph diameter `(1+o(1))D` | **not proved** | first-version overclaim corrected |
| DS.3 applies from FS alone | **false/not claimed** | DS.3 needs the extra `delta_i/D->1` hypothesis |
| explicit `epsilon_eta` | not computed | qualitative relative isoperimetric constant suffices |
| Level I | still open | graph-metric stretch and central-corridor capacity remain |

---

## 9. Next target

FS converts the full-core near-circle endpoint into a useful strict alternative:

- **fragmented half-disk group:** pay a fixed positive linear gap above `2D` in `Q_B`;
- **near-minimal interface defect:** two individual half-density harmonic carriers exist, but their graph-metric stretch `delta_i/D` remains uncontrolled above one.

The next theorem should either

1. show that the annular/central-face equality geometry forces `delta_i/D->1`, reactivating DS and the train-defect envelope; or
2. exploit `delta_i/D>1+epsilon` directly as extra component path length / attachment incidence cost.

This graph-metric fork is sharper and correctly dependency-scoped; no DS conclusion is used without its cap-minimal hypothesis.
