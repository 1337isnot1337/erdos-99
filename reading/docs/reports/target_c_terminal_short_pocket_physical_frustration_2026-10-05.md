> Generated reading edition · [exact source](../../../docs/reports/target_c_terminal_short_pocket_physical_frustration_2026-10-05.md) · source SHA-256 `63d1081a2cccd7eacc01a32483cac1c8a9cc471709cb81e46a9072fe1c0f7d96`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-24DA9008224B","canonical":true,"claim_ids":["C-TERMINAL-PHYSICAL-FRUSTRATION"],"claim_statuses":{"C-TERMINAL-PHYSICAL-FRUSTRATION":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C — terminal short pockets force physical unit-wall frustration

**Date:** 2026-10-05. **Starting main:** f539af073a691c13327a0a7fef3c746fb7704e5f.
**Preceding checkpoint:** 107aafc1380047b0e46bf756ac8e214fc042f1e4.
**State:** 2026-09-14.audit.51.
**Classification:** canonical in `2026-10-05.audit.53` as `C-TERMINAL-PHYSICAL-FRUSTRATION` at the exact branch scope `q/D->pi`, `u_B/D->0`. **LEVEL I STATUS: STILL OPEN. C-II REMAINS OPEN.**

## 1. Exact branch and changed quantity

Consider any sequence of canonical triangle-free full-core Type-II sources,
with every source point retained, diameter tending to infinity, and

```math
q/D\longrightarrow\pi,
\qquad u_B/D\longrightarrow0.
\tag{1.1}
```

Here `u_B=sum_P(ell_P-2)` is the total excess contact-path length of the
actual hull pockets. Nonunit hull-side count `m_B` need not be small;
the global outer walk can have linear excess through `m_B`.
There is no upper restriction on the live terminal parameter
`t_D=(q-k)/D`. In particular this is not the superseded low-terminal window.

Let `R_phys=sum_F r_F` over original bounded exceptional contact faces
only, excluding every new hull pocket. There is a universal, nonexplicit
constant `kappa_phys>0` such that every sequence (1.1) satisfies

```math
\boxed{\liminf R_{\rm phys}/D\ge\kappa_{\rm phys}.}
\tag{1.2}
```

More precisely, fixed degree and angular cutoffs force a linear family of
**original physical contact faces** with positive direction mismatch.
A linear subfamily has pairwise disjoint unit-contact wall vertices.
Thus no sequence (1.1) can have `R_phys=o(D)`, even if a few long hull
pockets carry linear or larger residual. This strengthens the
[total-residual exclusion](target_c_augmented_train_phase_rank_small_residual_exclusion_2026-10-05.md)
in this terminal scope by locating the compulsory bank on complete unit walls.

Independently of any residual hypothesis, all outer-ended stopped trains
in (1.1) carry only `o(D^2)` strict rhombi. Their second depletion gives
the physical bank inequality (5.2) below. Positive residual is still not
spare capacity or positive force activation.

The exact implication being proved is

`terminal hull-side saturation + negligible pocket-path excess`
`-> diffuse phases on almost all pocket ends`
`-> augmented rank forces physical direction-frustrated faces`
`-> no physical-small-residual survivor and full outer-train depletion`.

## 2. Inputs and source accounting

Use the contact-minimal, then diameter-pair-minimal triangle-free global
minimizer. Its positive-contact core and actual loaded force hull satisfy
the canonical mixed rigidity, convex augmented-face, stopped-train and
Type-II disk/rhombus theorems. No kernel is assigned to contact isolates.

The following inputs are canonical after audit.52/audit.53:

- the #699 actual hull-side normal-capacity bound, uniform in the phase-bin
  shift, and its good-unit-hull depletion theorem;
- the [augmented angular-column independence and phase bank](target_c_augmented_train_phase_rank_small_residual_exclusion_2026-10-05.md):
  internal augmented train columns are independent, and
  `N_j<=10|H|+4E_j`;
- the [outer angular restriction theorem](target_c_outer_train_rank_groemer_bank_synthesis_2026-10-05.md):
  the number `O` of outer-ended trains satisfies `O>=q-k+sigma_C`;
- [fixed-degree Groemer direction stability](target_c_outer_pocket_groemer_phase_depletion_2026-10-05.md),
  including the segment equality case;
- the [exact residual conservation](../../research/target_c_inactive_chamber_residual_conservation.md).

Write `a0=sqrt(3)/2`, `Delta_2=pi/(2sqrt(3))` and `s=sqrt(Delta_2)`.
Here `delta_F=pi D^2/4-A_F`, `E_4` is total strict-rhombus area excess
above `a0 R_4`, and `Z_ext` counts every source point outside the force hull.
All original exceptional faces have unit-boundary degree at least five,
`P_exc=4f+Q<=5pi D`, and `T<=3pi D`. Each new pocket has exactly one
added hull side and a contact path of length `ell_P>=2`. Consequently

```math
\#\{P:\ell_P\ge3\}\le u_B,
\qquad \sum_{\ell_P\ge3}\ell_P\le3u_B.
\tag{2.1}
```

The added sides impose zero vector displacement only in the linear rank
proof. Four-sided pockets keep their closure rows; they are not strict
unit rhombi. Original stopped trains are used throughout.

Type-II disk convergence and (1.1) give

```math
g_B:=P_F-q=o(D),\qquad
g_B=\sum_{e\ {\rm nonunit}}(|e|-1)\ge0.
\tag{2.2}
```

Every source isolate remains in its uniquely assigned chamber or exterior
cap. This includes isolates assigned on an added hull chord. Physical
unit-wall faces have their assigned isolates strictly in their interiors.

## 3. Two-step pockets have the hull phase

Suppose a pocket path is `a-x-b` with both contacts of length one, and
its added chord has length `c>1`. The two oriented path unit vectors are
symmetric about the chord direction, with angle

```math
\rho=\arccos(c/2).
```

At `c=1`, `rho=pi/3`; both path directions therefore equal the chord
phase modulo `pi/3`. For `1<c<=3/2`,

```math
0<\pi/3-\rho
=\int_1^c\frac{dt}{\sqrt{4-t^2}}
<c-1.
\tag{3.1}
```

Thus a two-step pocket with `c<=1+eta`, `0<eta<1/2`, has **both**
terminal phases within `eta` of its actual hull chord. This uses no
Groemer threshold, isolate count or stress activation.

The number of two-step pockets failing `c<=1+eta` is at most `g_B/eta`.
All longer pockets have node count at most `u_B` and total terminal
mass at most `3u_B`. For fixed `eta`, both exceptional counts are `o(D)`
under (1.1).

### 3.1 Unconditional outer-train depletion in this branch

Assign to each outer-ended train one actual outer terminal occurrence.
An occurrence belongs either to a unit hull side, a two-step pocket, or
a longer pocket. The last class has total mass `o(D)` by (2.1).
For fixed `eta`, the chord-bad two-step class also has total mass `o(D)`.
Every remaining occurrence is anchored to its actual hull side, with at
most two occurrences per side, and phase error at most `eta`.

For a fixed narrow phase window, actual hull-side normal dispersion bounds
its anchored terminal count by `O((epsilon+eta)D)+o(D)`, uniformly in its
position. Choose one end per train; multiplicity two is retained. As
`D->infinity`, then `eta->0`, then `epsilon->0`, the normalized maximum
window mass tends to zero. Canonical phase coarea, or the #699 incident
crossing count, now gives

```math
\boxed{R_{\mathcal O}=o(D^2),}
\tag{3.2}
```

where `mathcal O` is **all** outer-ended trains. Bad-train crossings are
at most their count times `T=O(D)`. Far-phase crossings are `O_epsilon(D)`.
Simple crossings handle the remaining window count. All statements are
about graph deletion for counting; no source point is removed.

## 4. Rank locates the bank on physical faces

Fix a physical degree cutoff `M`, tolerance `eta<1/2`, and equal-circle
bin width `epsilon=pi/(3n)>2eta`. Choose one unit edge as the reference
phase of each physical exceptional face.

Let `B=B_{M,eta}` count physical faces of degree at most `M` with some
incident train phase at distance at least `eta` from their reference.
Declare bad nodes:

1. physical faces of degree greater than `M`, at most `5pi D/M`;
2. these `B` direction-frustrated physical faces;
3. every pocket of path length at least three, at most `u_B`;
4. two-step pockets with chord longer than `1+eta`, at most `g_B/eta`;
5. remaining nodes whose reference is within `eta` of a shifted bin boundary.

The total bounded-node count is at most `2pi D`. A random shift gives
some choice with the fifth count at most `4pi eta D/epsilon`. All good
nodes have every incident train in one bin. Good pockets have valence two
and distinct nonunit hull anchors. Outside terminals have distinct unit
hull anchors. Hence the actual hull-side estimate gives

```math
\max_j E_j\le(6\epsilon+o_\epsilon(1))D.
\tag{4.1}
```

The finite phase bank, the two-bin comparison with canonical coarea,
and `T<=3pi D` imply, on a subsequence attaining the liminf,

```math
\Delta_2\le60\pi\liminf \frac{B}{D}
+\frac{300\pi^2}{M}
+\frac{240\pi^2\eta}{\epsilon}
+144\pi\epsilon.
\tag{4.2}
```

Here (1.1) removes `60pi(u_B+g_B/eta)/D` **after all cutoffs are fixed**.
No residual estimate for the long pockets is needed. High-degree physical
terminal mass is charged by augmented rank, not discarded.

For example choose the same constants for all sequences:

```math
M=100000,\quad
n=\lceil2000\pi^2/\Delta_2\rceil,\quad
\epsilon=\pi/(3n),\quad
\eta=\Delta_2\epsilon/(3000\pi^2).
\tag{4.3}
```

The last three terms of (4.2) sum to less than `Delta_2/2`: the first
is below `0.048`, the second is `0.08Delta_2`, and the third is at most
`0.024Delta_2`; `Delta_2>3/4` suffices. Therefore

```math
\liminf B/D\ge\frac1{240\sqrt3}.
\tag{4.4}
```

Fixed-degree Groemer compactness assigns every such physical face a
residual at least `sigma_M(eta)>0`. Consequently (1.2) holds with

```math
\kappa_{\rm phys}
=\frac{\sigma_{100000}(\eta)}{240\sqrt3}>0.
\tag{4.5}
```

No effective estimate for this compactness threshold or `D_0` is claimed.
Each wall has at most `M` vertices; a contact vertex meets at most five
physical faces. Greedy selection from the eventual half of (4.4) gives
at least `D/(2400sqrt(3)M)` pairwise boundary-vertex-disjoint physical
direction-frustrated faces. Their assigned isolate populations also have
disjoint interiors. All walls are complete unit-contact cycles, so the
existing contact-wall shield applies to any actually certified interior
replacement. Existence of that replacement is not proved here.

## 5. Immediate composition with the strongest train ledger

Let `S_U` be singleton trains not in `mathcal O`, and let

```math
U=T-|\mathcal O|-S_U.
```

Deleting `mathcal O` and these singletons leaves all but `o(D^2)` rhombi
by (3.2). Mantel and outer angular determination give

```math
U\ge(2s-o(1))D,\qquad
U\le2f-\max\{\sigma_C,k-m_B-d_D\}-S_U.
```

The second bound retains both `|mathcal O|>=q-k+sigma_C` and the earlier
good-hull count `|G|=q-m_B-d_D`, with `0<=d_D<=2`. Put
`rho_B=max(sigma_C,k-m_B)`. Thus the compulsory bank is

```math
\boxed{2f\ge2sD+\rho_B+S_U-o(D).}
\tag{5.1}
```

With `sigma_R=2(T-S)-4sqrt(R_4)`, the exact finite identity is

```math
4S+2\sigma_R
=2b-8\sqrt{R_4}+5U+5\sigma_C+2(Q-f)+5S_U
+5\bigl(|\mathcal O|-(q-k+\sigma_C)\bigr).
\tag{5.2}
```

Its last term is nonnegative and at least
`5 max(0,k-m_B-d_D-sigma_C)`. Substitution gives the second-depletion
form of the physical frontier:

```math
\boxed{4S+2\sigma_R
\ge2(\pi+s)D+5(\rho_B+S_U)+2(Q-f)+2(b-P_F)-o(D).}
\tag{5.3}
```

The `5m_B` escape on the left of (S) is canceled in this branch by spending
all additional outer-ended trains. Equations (5.1) and (5.3) are two
forms of the same scalar identity, not independent currencies. Combining
`f<=Q=q-m_B-u_B-2k` with (5.1) also gives

```math
m_B+u_B+2k+\frac{\rho_B+S_U}{2}
\le(\pi-s)D+o(D).
\tag{5.4}
```

Finally, the actual population comparison spends (1.2):

```math
\limsup\frac{\delta_F+E_4-a_0Z_{\rm ext}}D
\le c_0\pi-a_0\kappa_{\rm phys},\qquad c_0=a_0/2.
\tag{5.5}
```

This is a necessary budget. Neither it nor the complete unit-wall matching
implies a strict competitor. The general positive-residual full-core
branch, terminal sources with `u_B=Omega(D)`, and the macroscopic-container
branch remain open.
The total-residual and physical-residual floors can overlap; they are not
added as independent payments.

## 6. Hostile checks and computation

- Long pockets may carry large residual or area while having `o(D)` nodes.
  They are handled by rank and (2.1), not declared geometrically negligible.
- Two-step phase alignment uses actual unit lower edges and a near-unit
  hull chord. It never invokes near-diameter upper pairs or PR #664.
- Unit hull occurrences and two-step pocket terminals use separate actual
  side anchors, with multiplicity two kept explicitly.
- All fixed tolerances precede the source limit. There is no division of
  an `o(D^2)` local area error by `D`.
- Actual bridges and repeated outer occurrences remain train incidences;
  no incident diameter sequence is treated as an Euler path.
- Global optimality enters through canonical mixed rigidity and the
  loaded/Type-II reductions. It supplies no new force activation theorem.
- The finite loaded-pentagon wall regression still blocks a generic
  fixed-wall capacity inference. The new physical bank requires the
  additional large-source coupling that regression lacks.

The [exact verifier](../../../research/verify_target_c_terminal_short_pocket_physical_frustration_2026_10_05.py)
checks rational two-step pockets approaching chord length one, unit
separation and positive vanishing pocket residual, long-pocket count and
terminal-mass inequalities, the finite cancellation (5.2), and the
outer-train bank implications. Scalar ledgers are not source embeddings.
It does not certify global optimality, asymptotic hull convergence,
Groemer compactness, activation or closure.
