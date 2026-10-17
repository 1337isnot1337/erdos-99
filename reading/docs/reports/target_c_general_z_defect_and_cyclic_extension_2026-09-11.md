> Generated reading edition · [exact source](../../../docs/reports/target_c_general_z_defect_and_cyclic_extension_2026-09-11.md) · source SHA-256 `531c265465c2925e458c718f5bbe5c3fa60628fcf6b1fe1be6ab92ec3630bdc8`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-0DAB470B5E73","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_general_z_defect_and_cyclic_extension_2026-09-11.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=57266ee5b5f05d3e2697a65c0f73e40553786294; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — retaining positive `s_Z` in the detour and cyclic bounds

**Date:** 2026-09-11  
**Repository state:** `053e1e1b85643b738b4cde306838d150ea325783`  
**Run type:** closing-proof extension / branch audit  
**Target:** Target C, C-II after the report-level ZF chain  
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md`  
**External web search:** not used  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`.

This report does not promote any theorem or change the route map. It records two
extensions of the September 10 circuit/cyclic arguments. Both are conditional on the
report-level ZF/ZE/ZK/PC stack; the promoted C53/C63 stack alone does not establish
that stack.

The first extension retains positive `s_Z` in the exact detour identity and proves the
same explicit low-surplus exclusion in every post-ZF branch. The second extends the
cyclic atomic-endpoint argument from `s_Z=0` to arbitrary `s_Z>=0`.

The forest branch with `d_H>0` and arbitrary `s_Z` remains open.

## 1. Starting endpoint

For a report-level post-ZF C-II survivor write

```math
\Lambda_D=e_{BB}+2s_C,
\qquad
\nu_D={\Lambda_D-3d_H\over D},
\qquad
z_D={s_Z\over D}.
```

The September 10 explicit circuit report proved, under `s_Z=0`,

```math
\liminf\nu_D>{597\over1000}.
```

The exact general identity already recorded in the September 9 detour ledger is

```math
E_{out}+Q=P_F-h+e_{BB}-3d_H-2s_Z-c_B.\tag{1.1}
```

The candidate closing implication is therefore

```text
positive s_Z consumes the same detour budget
  -> the explicit 0.597 exclusion holds without s_Z=0
  -> only the high-surplus forest/cyclic branches remain.
```

## 2. General post-ZF low-surplus exclusion

### Theorem GZ — uniform `0.597` floor with positive `s_Z`

Assume the report-level ZF, ZE, ZK, PC, FSDB, RSJ, DD, and ZG inputs used by the
September 10 `0.597` report. Then there are absolute constants
`epsilon_597>0` and `D_0` such that every sufficiently large survivor, with no
assumption `s_Z=0`, satisfies

```math
\boxed{
{e_{BB}+2s_C-3d_H\over D}
\ge0.597+\epsilon_{597}.}
\tag{GZ.1}
```

Consequently

```math
\boxed{
{e_{BB}+2s_C\over D}
\ge0.597+\epsilon_{597}+3{d_H\over D}.}
\tag{GZ.2}
```

### Proof

Suppose GZ.1 fails. Choose an unbounded sequence with

```math
\nu_D\le0.597+o(1).
\tag{2.1}
```

Pass to a subsequence on which all normalized quantities used below converge. Put

```math
y={h\over D},\quad p={P_F\over D},\quad
\delta=2y-p,
\quad \xi={Q\over D},\quad z={s_Z\over D}.
```

The exact perimeter identity is

```math
b+Q=2h-2s_Z.
\tag{2.2}
```

Since `P_F<=b`,

```math
0\le b-P_F=D(\delta_D-2z_D-\xi_D),
\tag{2.3}
```
where `delta_D=(2h-P_F)/D`. In particular `p<=2y` and `p>=y` because
`q=h+d_H` is a set of force-hull vertices and `q<=P_F`. Thus the RSJ/FSDB feasibility
inequality used in the September 10 report remains valid with

```math
\max\{\Phi(y),\Psi(p)\}
\le
J_{\nu}(p-y),
\tag{2.4}
```

where

```math
\Phi(y)={y+\sin y\over4},\qquad
\Psi(p)={\pi\over(\pi-2)^2}\left({p\over2}-1\right)^2,
```

and

```math
J_u(m)={\pi\over4}u^2+{(u+m)^2\over4\pi}.
```

Equation (2.4) is no weaker than the `s_Z=0` inequality: the cavity expression before
relaxation is `nu+p-y-2z-c_B/D`, and the omitted terms are nonnegative. The attachment
area expression uses `6+e_BB+2s_C-3d_H`, so it also depends on `nu`, not on a
specialization of `s_Z`.

The rational barriers in the September 10 proof of E597 therefore apply unchanged to
(2.4). They give

```math
y<1.523,
\qquad
\delta<0.024.
\tag{2.5}
```

Returning to the finite identity (2.3),

```math
{Q\over D}+2{s_Z\over D}<0.024+o(1).
\tag{2.6}
```

The exact terminal identity gives
`x_B=b-q=h-d_H-2s_Z-Q<=h`; together with `a<=x_B` and (2.5), the DD outer-pocket
estimate gives

```math
\limsup {H_{out}\over D^2}<0.33715464282.
\tag{2.7}
```

Exceptional-face isoperimetry and (2.6) give

```math
\limsup {A_{exc}\over D^2}< {2\over25}(0.024)^2=0.00004608.
\tag{2.8}
```

Therefore ZG gives

```math
\limsup {G\over D^2}<0.33720072282.
\tag{2.9}
```

On the other hand, FSDB and the ZK attachment estimate give, with
`A_FS>0.617804` and `nu<=0.597+o(1)`,

```math
\liminf {G\over D^2}
>
0.617804-0.2799236286
=0.3378803714.
\tag{2.10}
```

The gap `0.00067964858` is positive. This contradicts (2.9). The usual subsequence
argument upgrades the contradiction to a uniform positive `epsilon_597`, proving
GZ.1. Equation GZ.2 is its definition rearranged. `square`

### Scope

The theorem includes the `s_Z>0` branch, but it is not a theorem from the promoted
C53/C63 stack alone. It is report-level until the ZF dependency chain is promoted.
It retains contact-isolated source points because the FSDB source-area term and the
cap/lattice estimates count the full source population.

## 3. General cyclic extension

### Theorem GC — cyclic atomic floor for arbitrary `s_Z>=0`

Assume the same report-level inputs and the Woodall cyclic branch `d_H=0`. Then there
is an absolute `epsilon_A>0` such that every sufficiently large cyclic survivor with
arbitrary `s_Z>=0` satisfies

```math
\boxed{
{e_{BB}+2s_C\over D}
\ge
\lambda_A+\epsilon_A,
\qquad
\lambda_A={\pi\over
\sqrt{\pi^2+(\frac54-\sqrt{\pi/(2\sqrt3)})^2}}.}
\tag{GC.1}
```

In particular, the cyclic `s_Z>0` branch is reduced to a high-surplus phase; the
bound remains below `1` and is not a Level I contradiction.

### Proof

The cyclic Reuleaux/cap argument is independent of `s_Z`. Woodall gives one odd
diameter cycle, C17 puts the entire source in its width-`D` Reuleaux polygon, and the
shared-endpoint angle bound gives a partition of the boundary into force-hull subarcs
with angles `phi_j` satisfying

```math
\sum_j\phi_j=\pi,
\qquad
\max_j\phi_j=O(D^{-1/4}).
```

Thus

```math
P_F=\pi D-O(\sqrt D),
\qquad
b-P_F=O(\sqrt D),
\tag{3.1}
```

and the FSDB/RSJ equality input gives

```math
{\operatorname{area}F\over D^2}\longrightarrow {\pi\over4}.
\tag{3.2}
```

Write normalized subsequential limits

```math
\nu={e_{BB}+2s_C\over D},\quad
\xi={Q\over D},\quad \varphi={f\over D},\quad
w=\xi-\varphi.
```

Here `f` is the number of bounded exceptional faces. From PC.2 with `d_H=0`,

```math
e_{BB}=Q+2s_Z+d_P+c_B,
\tag{3.3}
```

so

```math
0\le w\le\xi\le\nu,
\tag{3.4}
```

and `Q,f=O(D)`. The refined exceptional-face square bound and ZG give

```math
{A_{exc}\over D^2}\le {w^2\over4\pi}+o(1).
\tag{3.5}
```

The exact ZK attachment estimate, with `d_H=0`, gives

```math
\limsup {\sum_r\operatorname{area}(P_r)\over D^2}
\le {\pi\over4}\nu^2.
\tag{3.6}
```

If `nu>=1`, (GC.1) is automatic after decreasing `epsilon_A` if necessary. Assume
`nu<1`. Since the outer-pocket area is `o(D^2)`, (3.2), (3.5), and ZG imply

```math
w\ge\pi\sqrt{1-\nu^2}.
\tag{3.7}
```

The `s_Z` term cancels from the full-source Oler ledger rather than being silently
set to zero. Indeed, Euler/face incidence gives

```math
m=R+f+q-s_Z+1,
```

for the nonisolated contact-core population `m`, while (2.2) gives
`b+Q=2q-2s_Z`. Adding the bounded-face Oler estimate to the outer-face isolate
estimate therefore yields exactly

```math
a_0N_F\le \operatorname{area}F+c_0P_F+a_0-E,
\qquad a_0={\sqrt3\over2},\quad c_0={\sqrt3\over4}.
\tag{3.8a}
```

The capwise Oler estimate outside `F` and the strict translated-lattice comparison
then give

```math
E+\delta_{\mathcal R}
<c_0(2P_F+\pi D-2q),
```

so `E=O(D)` uniformly. The exact cyclic Oler cancellation therefore gives `E=O(D)`
for the total area excess of the strict unit-rhombic bounded faces. If `R` is their
number, then

```math
{R\over D^2}\ge r_{min}(w)-o(1),
\qquad
r_{min}(w)={\pi^2-w^2\over2\pi\sqrt3}.
\tag{3.8}
```

The stopped-train theorem applies to the actual contact core, including exceptional
faces and bridges. Its exact identities are

```math
T={b+Q\over2}+2f,
\qquad
{T\over D}\longrightarrow
\tau={\pi+\xi\over2}+2\varphi.
\tag{3.9}
```

The diameter-cycle source geometry gives a uniform outer-walk direction measure. The
train Mantel theorem then gives, for `s` equal to the atomic mass of the limiting train
direction measure,

```math
s\tau\ge2\sqrt{r_{min}(w)}.
\tag{3.10}
```

Atomic trains have `o(D)` outer endpoint incidences because the outer direction measure
is uniform. Their remaining endpoints fit in the exceptional-face incidence capacity
`Q+4f`, so

```math
2s\tau\le\xi+4\varphi.
\tag{3.11}
```

Combining (3.10)--(3.11), with `xi=w+varphi`, gives

```math
4\sqrt{r_{min}(w)}\le w+5\varphi.
\tag{3.12}
```

Since `nu>=xi=w+varphi`,

```math
\nu\ge {4\over5}\left(w+\sqrt{r_{min}(w)}\right).
\tag{3.13}
```

The function in parentheses is increasing for `0<=w<=1`. Insert the lower bound
(3.7). With `Delta=pi/(2sqrt(3))`, this gives

```math
\left({5\over4}-\sqrt\Delta\right)\nu
\ge\pi\sqrt{1-\nu^2},
```

and hence `nu>=lambda_A`.

It remains to exclude equality. Suppose `nu_D->lambda_A`. Equality in the preceding
chain forces

```math
\xi\to\nu,\quad {Q-f\over D}\to
\pi\sqrt{1-\nu^2}>0,
\quad {R\over D^2}\to\Delta\nu^2,
\tag{3.14}
```

and equality in (3.10)--(3.11). The first relation also forces
`s_Z/D->0` through (3.3), so the endpoint specializes asymptotically to the
September 10 atomic endpoint profile.

Equality in the refined exceptional-face square bound produces one bounded
exceptional face with perimeter `(Q-f)+o(D)` and area
`(Q-f)^2/(4pi)+o(D^2)`. Its normalized edge-direction measure is uniform by equality
in the isoperimetric inequality.

On the train side, equality in the angular-defect and Mantel steps forces all atomic
train directions into one projective three-point orbit

```math
\{\theta_0,\theta_0+\pi/3,\theta_0+2\pi/3\}.
```

Equality in (3.11) says these atomic trains exhaust all exceptional-face endpoint
incidences up to `o(D)`; outer incidences are `o(D)`. Therefore all but `o(D)` edges
of the macroscopic exceptional face have directions in three shrinking windows,
contradicting its uniform limiting direction measure. Thus equality is impossible,
and compactness yields a uniform `epsilon_A>0`. `square`

### Scope audit

- No hull saturation is added to the secondary diameter-pair minimization.
- Contact-isolated source points are retained in the Reuleaux cap and Oler accounting.
- The proof uses actual stopped-train endpoints, not hypothetical continuations through
  exceptional faces.
- The regular odd shell has `s_Z=2`, but it is not a global minimizer in this branch;
  its role remains a regression against any claim that `s_Z>0` is locally impossible.
- The endpoint exclusion is qualitative. It does not produce a gap known to cross `1`.

## 4. Exact effect on the branch ledger

The report-level branch ledger becomes:

| branch | new consequence | status |
|---|---|---|
| cyclic `d_H=0`, `s_Z=0` | `Lambda_D/D>=lambda_A+epsilon_A` | high-surplus cyclic branch remains |
| cyclic `d_H=0`, `s_Z>0` | same bound; endpoint forces `s_Z/D->0` | high-surplus cyclic branch remains |
| forest `d_H>0`, `s_Z=0` | `Lambda_D/D>=0.597+epsilon_597+3d_H/D`; common universal bridge excluded | open |
| forest `d_H>0`, `s_Z>0` | same general `0.597` floor; common universal bridge excluded | open |

The common-bridge transfer theorem applies independently of the new extension, so in
both forest rows the common intersection of all diameter routes is one bridgeless
contact block. Woodall still makes the full diameter graph a caterpillar forest.

## 5. Exact remaining lemma

The shortest unresolved statement is now a forest-hub or high-surplus cyclic theorem,
not another low-surplus estimate:

> **Forest-hub closure.** Exclude a triangle-free report-level C-II source with
> `d_H>0`, all diameter routes meeting one common bridgeless positive-contact block,
> and
> `Lambda_D/D>=0.597+epsilon_597+3d_H/D`, for arbitrary `s_Z>=0`.

An independent cyclic closure would have to raise the nonexplicit gap above `lambda_A`
to a known contradiction or produce a strict sub-`D` competitor. The current proof
does neither.

## 6. Failed implications and binding regressions

| proposed implication | classification | exact failure |
|---|---|---|
| positive `s_Z` is impossible from the circuit ledger | rejected | regular odd shells have `s_Z=2`; the exact ledger permits them |
| `nu>0.597` closes C-II | false as a logical endpoint | no opposing upper bound is proved |
| `lambda_A+epsilon_A` closes the cyclic branch | false as a logical endpoint | the gap is nonexplicit and not known to exceed `1` |
| outer direction uniformity gives a quantitative gap by itself | insufficient | endpoint contradiction is qualitative; near-endpoint sequences are not quantitatively separated |
| contact-isolated points can be discarded | rejected | the Reuleaux/cap and full-source Oler terms explicitly retain them |

## 7. Dependencies and promotion recommendation

The proof uses the following existing inputs.

- `docs/reports/target_c_exact_detour_defect_surplus_04673_2026-09-09.md`, equation
  (ED.12), for the general `-2s_Z` detour term.
- `docs/reports/target_c_sz0_explicit_0597_detour_gap_2026-09-10.md`, Sections 2--6,
  for the rational `1.523`, `0.024`, and fixed cavity-gap certificate.
- `docs/reports/target_c_outer_pocket_internal_chord_ledger_2026-09-09.md`, PC.2.
- `docs/reports/target_c_component_slack_cancellation_2026-09-09.md`, ZK.3.
- `docs/reports/target_c_cyclic_reuleaux_cap_detour_2026-09-10.md`, for the cyclic
  cap/perimeter and `O(D^2)` outer-pocket statements.
- `docs/reports/target_c_cyclic_rhombus_excess_transport_2026-09-10.md`, for the
  full-source Oler cancellation and `E=O(D)`.
- `docs/reports/target_c_cyclic_atomic_endpoint_incidence_2026-09-10.md` and
  `target_c_cyclic_atomic_endpoint_exclusion_2026-09-10.md`, with the proof changes
  in Section 3 above.

These are dated reports, not promoted theorem modules. **Hold as report.** Do not edit
the Target C route map or active theorem status from this file.

## 8. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

New extension, conditional on the report-level ZF/ZE/ZK/PC stack:
  nu_D=(e_BB+2s_C-3d_H)/D >= 0.597+epsilon_597
  for every sufficiently large post-ZF survivor, with arbitrary s_Z>=0.
The reason is exact:
  E_out+Q=P_F-h+e_BB-3d_H-2s_Z-c_B,
so positive s_Z only reduces the available cavity detour. The old rational barriers
  y<1.523, delta=2h/D-P_F/D<0.024 remain valid, and then Q/D+2s_Z/D<0.024.
The fixed cavity gap 0.00067964858 survives unchanged.

New cyclic extension, under the same report-level inputs:
  for d_H=0 and arbitrary s_Z>=0,
    (e_BB+2s_C)/D >= lambda_A+epsilon_A,
  lambda_A=pi/sqrt(pi^2+(5/4-sqrt(pi/(2sqrt3)))^2).
The cyclic endpoint equality forces s_Z/D->0 and then the existing giant-face versus
three-direction endpoint contradiction applies. This still does not cross 1.

Surviving obstruction:
  forest d_H>0 with arbitrary s_Z>=0, all diameter routes through one common
  bridgeless contact block, and no opposing upper bound on the surplus currency.
```
