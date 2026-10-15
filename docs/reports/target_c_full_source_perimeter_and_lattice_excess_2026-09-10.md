<!-- theorem-state: {"artifact_id":"ART-0FE9461E394E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — full-source perimeter saturation and lattice-excess endpoint

**Date:** 2026-09-10  
**Repository state:** branch `research/2026-09-10-c2-capacity-closure` from `3f37ef0eab4407a411f9a6d51d016ba600302be7`  
**Run type:** closing proof / exact endpoint refinement  
**Target:** Target C, C-II with the full source population  
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md`, with the controlling September 9 update  
**External web search:** not used  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`.

This report adds two exact full-source consequences of the same Oler plus strict translated-lattice comparison used by the September 10 circumradius-response report.

First, the convex hull of **every** global minimizer has perimeter within an absolute constant of the maximum perimeter allowed by its diameter:

\[
0\le \pi D-P<\frac{\pi\sqrt3}{2}.
\]

Equivalently, the integrated width deficit is absolutely bounded, so every fixed relative width deficit occurs only in an `O(D^{-1})` set of directions.

Second, the proposed full-source capacity endpoint has an exact scalar form. If

\[
\Delta=\frac{\pi}{2\sqrt3},\qquad
g_A=n-1-\Delta D^2,
\]

then every global minimizer has `g_A>0` and

\[
\delta_K+\mathscr O_A=c_0P-a_0g_A.
\]

Thus the desired C-II inequality `delta_K+O_A>=c_0P` is **equivalent** to `g_A<=0`; there is no hidden hull term left in that endpoint. A closure through this inequality must therefore use triangle-freeness and the lexicographic/global structure to force

\[
n-1\le\Delta D^2,
\]

contradicting the strict translated-lattice comparison.

These are proved consequences, not a Level I solution.

## 1. Starting endpoint

For a hypothetical contact/diameter-lexicographically minimal triangle-free global source, the preceding full-source report reduces one exact C-II closure to

\[
\boxed{\delta_K+\mathscr O_A\ge c_0P,}
\tag{1.1}
\]

where

\[
K=\operatorname{conv}A,\quad P=\operatorname{per}K,
\quad a_0=\frac{\sqrt3}{2},\quad c_0=\frac{\sqrt3}{4},
\]

\[
\delta_K=\frac{\pi D^2}{4}-\operatorname{area}K,
\qquad
\mathscr O_A=\operatorname{area}K+c_0P-a_0(n-1).
\tag{1.2}
\]

The canonical global inputs are

\[
\operatorname{area}K+c_0P\ge a_0(n-1)
\tag{1.3}
\]

from Oler and

\[
D^2<\frac{2\sqrt3}{\pi}(n-1)
\tag{1.4}
\]

from the strict translated-triangular-lattice comparison. The latter is equivalent to

\[
a_0(n-1)>\frac{\pi D^2}{4}.
\tag{1.5}
\]

The implication attacked here is

```text
full-source Oler + strict global lattice comparison
    -> perimeter almost saturates Cauchy by an absolute amount
    -> almost every source-hull direction has width nearly D
    -> sharpen the geometry available to any later C-II population/face theorem.
```

A second exact calculation determines what (1.1) is actually asking:

```text
NC endpoint
    <-> nonpositive triangular-lattice population excess
    -> contradiction with strict global lattice comparison.
```

## 2. Strongest genuinely new audited theorem

### Theorem PW — absolute full-source perimeter saturation

Let `A` be any global `n`-point unit-separated minimum-diameter configuration in the plane, let `D=D(n)`, let `K=conv A`, and put `P=per K`. Then

\[
\boxed{
P>
\frac{\pi}{2}\left(\sqrt{4D^2+3}-\sqrt3\right).
}
\tag{PW.1}
\]

Together with Cauchy's perimeter-diameter inequality `P<=pi D`, this gives

\[
\boxed{
0\le \pi D-P
<\frac{\pi}{2}\left(2D-\sqrt{4D^2+3}+\sqrt3\right)
<\frac{\pi\sqrt3}{2}.
}
\tag{PW.2}
\]

In particular the source-hull perimeter deficit from its diameter-maximal value is `O(1)`, not merely `O(sqrt(D))` or `o(D)`.

#### Proof

By Oler and the strict translated-lattice comparison,

\[
\operatorname{area}K+c_0P
\ge a_0(n-1)
>\frac{\pi D^2}{4}.
\tag{PW.3}
\]

The planar isoperimetric inequality gives

\[
\operatorname{area}K\le\frac{P^2}{4\pi}.
\tag{PW.4}
\]

Hence

\[
\frac{P^2}{4\pi}+c_0P>\frac{\pi D^2}{4}.
\]

Multiplying by `4pi` and using `4c_0=sqrt(3)` gives

\[
P^2+\pi\sqrt3 P-\pi^2D^2>0.
\tag{PW.5}
\]

Since `P>0`, it lies above the positive root of the left side. This is exactly (PW.1).

Subtract (PW.1) from `pi D` to obtain the first strict bound in (PW.2). Since `sqrt(4D^2+3)>2D`, the parenthesis is strictly smaller than `sqrt(3)`, proving the final bound. `square`

### Corollary PW.1 — absolute integrated width deficit

Let `w_K(theta)` be the width of `K` in direction `theta`. Then

\[
\boxed{
\int_0^\pi\bigl(D-w_K(\theta)\bigr)\,d\theta
=\pi D-P
<\frac{\pi\sqrt3}{2}.
}
\tag{PW.6}
\]

Consequently, for every `tau>0`,

\[
\boxed{
\left|\{\theta\in[0,\pi):w_K(\theta)\le D-\tau\}\right|
<\frac{\pi\sqrt3}{2\tau}.
}
\tag{PW.7}
\]

In particular, for every fixed `rho>0`,

\[
\boxed{
\left|\{\theta:w_K(\theta)\le(1-\rho)D\}\right|
<\frac{\pi\sqrt3}{2\rho D}.
}
\tag{PW.8}
\]

#### Proof

Cauchy's width formula is

\[
P=\int_0^\pi w_K(\theta)\,d\theta.
\]

Every width is at most the diameter `D`; subtract from `pi D` and use (PW.2) to obtain (PW.6). On the set in (PW.7), the nonnegative integrand is at least `tau`; Markov's inequality gives (PW.7). Put `tau=rho D` for (PW.8). `square`

### Scope

PW and PW.1 concern **every global minimizer**, not only triangle-free sources, the force-visible core, a selected KKT support, a hull-saturated representative, or a jammed branch. All source points enter Oler through `K=conv A`, including contact-isolated points. No change of representative is used.

The theorem does not say that every direction has width `D-O(1)`, nor that the force hull itself has perimeter `pi D-O(1)`. The exceptional direction set may depend on the source, and the force hull may omit isolated source points.

### Dependencies

- `docs/theory/03-oler-shell.md`, Lemma 21.1: finite Oler inequality.
- `docs/targets/target-b/01-jammed-rhombic-branch.md`, Section 36.1: unconditional strict translated-lattice bound `D(n)^2<(2sqrt(3)/pi)(n-1)`.
- Cauchy's perimeter/width formula and the planar isoperimetric inequality, both already used in the canonical shared theory.

No Target B jammed/rhombic hypothesis is imported from the location of Section 36.1.

### Why it is new

The September 10 full-source report proves `R(K)=D/2+O(sqrt(D))` and transports this to every selected force hull, obtaining `P_*=2D-O(sqrt(D))` for the **reciprocal** force polygon. It does not record an absolute `O(1)` deficit for the **source hull perimeter** `P`, nor the resulting `O(D^{-1})` exceptional angular measure for a fixed relative width deficit.

The stronger perimeter conclusion comes from inserting the isoperimetric inequality between the same Oler/lattice inputs, rather than Bonnesen's radius-difference inequality.

## 3. Exact lattice-excess identity

Put

\[
\boxed{
\Delta=\frac{\pi}{2\sqrt3},
\qquad
g_A=n-1-\Delta D^2.
}
\tag{GE.1}
\]

### Theorem GE — NC is exactly a population-excess contradiction

For every global minimizer,

\[
\boxed{g_A>0}
\tag{GE.2}
\]

and the two full-source defects satisfy the exact identity

\[
\boxed{
\delta_K+\mathscr O_A=c_0P-a_0g_A.
}
\tag{GE.3}
\]

Therefore

\[
\boxed{
\delta_K+\mathscr O_A\ge c_0P
\quad\Longleftrightarrow\quad
g_A\le0
\quad\Longleftrightarrow\quad
n-1\le\Delta D^2.
}
\tag{GE.4}
\]

Thus (1.1), if proved for the triangle-free lexicographic C-II source, contradicts (GE.2) immediately.

#### Proof

The strict translated-lattice inequality (1.4) rearranges to

\[
n-1>\frac{\pi}{2\sqrt3}D^2=\Delta D^2,
\]

which is (GE.2).

Using the definitions (1.2), cancellation of `area K` gives

\[
\begin{aligned}
\delta_K+\mathscr O_A
&=\frac{\pi D^2}{4}+c_0P-a_0(n-1)\\
&=c_0P-a_0\left(n-1-\frac{\pi D^2}{4a_0}\right).
\end{aligned}
\]

Since `4a_0=2sqrt(3)`, the parenthesis is `g_A`. This proves (GE.3), and (GE.4) follows because `a_0>0`. `square`

### Corollary GE.1 — coupled isoperimetric/Oler budget

Since `mathscr O_A>=0` by Oler and `g_A>0`, (GE.3) yields

\[
\delta_K<c_0P.
\tag{GE.5}
\]

The isoperimetric inequality also gives

\[
\delta_K
\ge
\frac{\pi^2D^2-P^2}{4\pi}
=\frac{(\pi D-P)(\pi D+P)}{4\pi}.
\tag{GE.6}
\]

Together,

\[
\boxed{
\frac{(\pi D-P)(\pi D+P)}{4\pi}
+a_0g_A+\mathscr O_A
\le c_0P.
}
\tag{GE.7}
\]

Equation (GE.7) is a one-budget coupling between source width/perimeter deficit, triangular-lattice population excess, and Oler surplus. It is not a contradiction: all three nonnegative currencies can coexist within the right side.

## 4. Exact target implication

The full-source NC route can now be stated without the redundant hull defects. A sufficient C-II theorem is

> **Population-excess exclusion.** Every sufficiently large contact/diameter-lexicographically minimal triangle-free global source of diameter `D` satisfies
> \[
> n-1\le\frac{\pi}{2\sqrt3}D^2.
> \]

This contradicts the strict translated-lattice inequality for the same global source.

PW adds a new geometric restriction under which this theorem may be attacked: the full source hull has

\[
P=\pi D-O(1)
\]

with the explicit universal deficit (PW.2), and for every fixed `rho>0` only `O(D^{-1})` angular measure can have width below `(1-rho)D`.

The missing step is still source-specific. A density deficit for arbitrary triangle-free packings is impossible as a general principle: the repository contains near-triangular strict fillings and the fixed-cardinality triangle-free approximation theorem. The proof must use attainment/global optimality and the C-II structure, not triangle-freeness alone.

## 5. Exact remaining lemma

A direct closure through the full-source endpoint is now exactly:

\[
\boxed{
\textbf{PE:}\quad
A\text{ lexicographic, triangle-free, globally minimizing, sufficiently large}
\Longrightarrow
n-1\le\frac{\pi}{2\sqrt3}D^2.
}
\tag{5.1}
\]

It is enough to prove PE using the additional necessary conditions already available for that same source: C-I full actual support, FS.1-FS.4 after audit, PW/PW.1, and any separately audited post-ZF theorem whose hypotheses are satisfied.

A finite-rearrangement substitute remains equally valid: construct an `n`-point unit-separated configuration of diameter `<D` from the same hypotheses.

## 6. Audit classification of other claims

| Claim | Classification | Reason |
| --- | --- | --- |
| `P>(pi/2)(sqrt(4D^2+3)-sqrt(3))` | proved | Oler + strict lattice comparison + isoperimetric inequality |
| `pi D-P<pi sqrt(3)/2` | proved | exact positive-root algebra plus Cauchy `P<=pi D` |
| fixed relative width deficit occurs on `O(D^-1)` angular measure | proved | Cauchy width formula + Markov |
| `delta_K+O_A=c_0P-a_0g_A` | proved exact identity | direct cancellation of the hull area |
| NC is equivalent to `g_A<=0` | proved | `a_0>0` in the exact identity |
| source hull is Hausdorff `O(1)` from a disk | not proved | perimeter/mean-width control does not imply this rate |
| force hull has perimeter `pi D-O(1)` | not proved | isolates may enlarge the source hull without entering force support |
| PE / C-II / Level I | not proved | no theorem yet forces nonpositive lattice excess |

## 7. Regression tests

### Regular odd shells

The regular odd shell remains a valid regression to response-level shortcuts. Its source hull is itself a regular polygon of diameter `D`; its perimeter asymptotically approaches `pi D`, so PW is compatible with it. PW therefore does not mistakenly convert near-circularity into global optimality.

### Dense isolated shell fillings

Adding a dense strictly separated interior filling can preserve the shell stress/response and leading packing density while leaving those points force-invisible. PW is a full-source statement, so such a filling would have to satisfy the perimeter restriction if it were globally optimal. The known fillings have no global-optimality certificate, which is exactly the hypothesis used in (PW.3) through the strict `n-1` lattice comparison at the source diameter.

### Near-triangular triangle-free perturbations

Arbitrarily dense triangle-free perturbations block any claim that triangle-freeness alone forces a fixed density gap below `Delta`. PE is deliberately restricted to attained global minimizers with the lexicographic C-II structure.

### Hull-saturation normalization

No source point is moved in PW or GE. The proofs therefore do not combine the C1 hull-saturated representative with the C-I diameter-pair-minimal representative.

## 8. Failed routes and no-go results

1. `P=pi D-O(1) -> NC` is false as an inference from convex geometry alone. GE shows that NC is exactly the sign of `g_A`; perimeter terms cancel from the endpoint.
2. `near-maximal source perimeter -> near-matching diameter stress` is not asserted. The regular odd shell retains the matching obstruction from the FS report.
3. `near-maximal source perimeter -> small response trace` is not asserted. The shell has a quadratic response trace defect.
4. `triangle-free -> fixed density gap` remains false. Any PE proof must use global attainment/KKT/lexicographic structure.

## 9. Literature imported

None.

## 10. Computation and reproducibility

No computation is used. Every new statement is an algebraic consequence of canonical inequalities.

## 11. Canonical promotion recommendation

**Hold as report.** PW/PW.1 and GE are complete and have been checked against the active shell/filling regressions, but they should receive an independent dependency audit before route-map promotion. Do not promote PE: it is the remaining theorem, not a proved claim.

If PW/GE are promoted later, the natural locations are the Target C full-source C-II frontier and the exact population/area-gap endpoint; no change to Level I status is warranted.

## 12. Next run

The highest-value next theorem is PE itself, but PW suggests a more concrete attack: combine the `O(D^-1)` exceptional-direction width set with the post-ZF actual diameter graph and face/train ledger, and identify an exact use of global attainment that the regular shell lacks.

A second candidate is a right-plateau reduction: verify whether the canonical same-diameter extension theorem transports an arbitrary unbounded counterexample sequence to unbounded right endpoints `N` with `D(N+1)>D(N)`. At such endpoints the intrinsic insertion body is strictly open-unit-covered for **every** global minimizer. If the reduction preserves the Level I quantifiers, this supplies a genuinely global property absent from the filled-shell regressions.

## 13. Compact handoff

```text
LEVEL I STATUS: STILL OPEN

Strongest new theorem:
For every global minimizer with hull perimeter P and diameter D,
  P > (pi/2)(sqrt(4D^2+3)-sqrt(3)),
so
  0 <= pi D-P < pi sqrt(3)/2.
Equivalently the integrated width deficit is < pi sqrt(3)/2, and for fixed rho>0
directions of width <=(1-rho)D have measure O(1/D).

Exact endpoint identity:
Let Delta=pi/(2sqrt(3)) and g_A=n-1-Delta D^2>0. Then
  delta_K+O_A=c_0P-a_0g_A.
Thus NC >=c_0P is exactly g_A<=0, i.e. n-1<=Delta D^2.

Exact endpoint now:
Prove PE for every sufficiently large lexicographic triangle-free global source,
or construct a strict sub-D competitor.

Binding regressions/no-go results:
Odd shells still allow near-maximal perimeter with nonmatching diameter support and
quadratic response defect. Dense triangle-free perturbations rule out a generic
density gap. Neither family has the required global-attainment certificate.

Authoritative files:
docs/targets/target-c/56-ci-restored-frontier.md
docs/reports/target_c_full_source_circumradius_response_2026-09-10.md
docs/reports/campaign_zero_transfer_defect_review_2026-09-09.md
docs/reports/target_c_zf_boundary_surplus_collapse_2026-09-09.md
```
