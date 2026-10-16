<!-- theorem-state: {"artifact_id":"ART-D78808D86644","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_fsdb_low_defect_branch_2026-09-11.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=b5ff0ec76e123ca9c579ccd322a207049731c6d8; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — FSDB closes the sublinear outer/exceptional-defect phase

**Date:** 2026-09-11  
**Repository state:** local `8a78616`; FSDB read from `origin/main` at `053e1e1`  
**Run type:** exact branch closure / area-capacity synthesis  
**Target:** Target C C-II after ZF  
**External access:** read-only repository inspection; no new literature  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`.

This report proves a valid subbranch exclusion without using the withdrawn cyclic
Reuleaux detour. It is conditional only on the audited September 10 FSDB theorem,
whose route-map status remains unpromoted.

The excluded subbranch is

\[
s_Z=0,
\qquad x_B+Q=o(D),
\tag{1.1}
\]

where `x_B=b-q` is outer-walk excess and `Q` is bounded-face defect. The proof gives

\[
\operatorname{area}F\le
\left(\frac{\pi^2}{16}+o(1)\right)D^2,
\tag{1.2}
\]

while FSDB gives

\[
\liminf\frac{\operatorname{area}F}{D^2}
\ge
A_{FS}:=\frac{2\rho+\sin(2\rho)}4
>\frac{\pi^2}{16}.
\tag{1.3}
\]

The strict constant gap is exact, not numerical.

## 2. Theorem LFD — low-defect area contradiction

Assume a sequence of C-II post-ZF sources satisfies (1.1), with `s_Z=0`, and let
`F` be the selected force hull. Then no such sequence can be unbounded.

### Proof

Write `h=|H|`, `q=|B_+|`, and `b` for the outer contact-face walk length. The exact
post-ZF circuit identity is

\[
b+Q=2h.
\tag{2.1}
\]

By definition `b=q+x_B`, hence

\[
2h=q+x_B+Q.
\tag{2.2}
\]

The loaded vertices are consecutive vertices of the convex force hull and are
unit-separated. Therefore

\[
q\le\operatorname{per}F\le\pi D.
\tag{2.3}
\]

From (1.1)--(2.3),

\[
\frac hD\le\frac\pi2+o(1).
\tag{2.4}
\]

Let `f` be the number of bounded nonquadrilateral faces. Since every such face
contributes at least one to `Q`,

\[
f\le Q=o(D).
\tag{2.5}
\]

The stopped-train count in the actual contact complex is

\[
T=\frac{b+Q}{2}+2f=h+2f.
\tag{2.6}
\]

Thus

\[
T\le\frac\pi2D+o(D).
\tag{2.7}
\]

The train-crossing graph is triangle-free. In the strict-rhombus part, each bounded
quadrilateral face is the crossing of two train tracks, so if `R` is the number of
bounded quadrilateral faces, Mantel's theorem gives

\[
R\le\frac{T^2}{4}
\le\left(\frac{\pi^2}{16}+o(1)\right)D^2.
\tag{2.8}
\]

Every strict unit rhombus has area at most one, so the total quadrilateral area is at
most `R`.

It remains to bound the area of the outer pockets and exceptional faces.

For the outer pockets, OP adds each missing force-hull side and obtains `a` convex
pockets, where `a\le x_B`. If `k_P` is the number of original unit-contact edges on
the boundary chain of a pocket `P`, OP's exact incidence identity gives

\[
\sum_P k_P=x_B+2a=o(D).
\tag{2.9}
\]

The closing force-hull chord has length at most `k_P`, by the triangle inequality
along the unit contact chain. Hence

\[
\operatorname{per}P\le2k_P,
\qquad
\operatorname{area}P\le\frac{\operatorname{per}(P)^2}{4\pi}
\le\frac{k_P^2}{\pi}.
\tag{2.10}
\]

Summing and using (2.9),

\[
\sum_P\operatorname{area}P
\le\frac1\pi\left(\sum_P k_P\right)^2
=o(D^2).
\tag{2.11}
\]

For exceptional bounded faces, let their boundary lengths be `\ell_i`. The finite
face-defect budget gives

\[
\sum_i(\ell_i-4)=Q=o(D),
\tag{2.12}
\]

so the number of exceptional faces and their total boundary length are `o(D)`. Each
exceptional face has area at most `\ell_i^2/(4\pi)`, and therefore

\[
\sum_i\operatorname{area}F_i
\le\frac1{4\pi}\left(\sum_i\ell_i\right)^2
=o(D^2).
\tag{2.13}
\]

The augmented contact subdivision partitions `F` into its bounded quadrilateral
faces, bounded exceptional faces, and outer pockets. Combining (2.8), (2.11), and
(2.13) gives (1.2).

FSDB supplies (1.3). Since

\[
\frac{2\rho+\sin(2\rho)}4-rac{\pi^2}{16}>0,
\tag{2.14}
\]

the two asymptotic bounds contradict each other. `square`

## 3. Exact constant verification

The FSDB reports provide a rational certificate. The Dottie root satisfies

\[
\frac{739}{1000}<\rho<\frac{37}{50},
\]

which implies

\[
A_{FS}>\frac{154451}{250000}.
\]

Also `\pi<22/7`, hence

\[
\frac{\pi^2}{16}<\frac{121}{196}.
\]

Finally

\[
154451\cdot196=30272396>30250000=121\cdot250000.
\]

Therefore (2.14) is proved without decimal evaluation.

## 4. Scope and dependency audit

The proof uses:

1. the exact `s_Z=0` circuit identity `b+Q=2h`;
2. the OP convex-pocket augmentation and incidence identity;
3. the triangle-free stopped-train crossing graph and Mantel's theorem;
4. the finite C42 face-defect budget; and
5. FSDB.3/FSDB.1 from
   `docs/reports/target_c_fs_symmetric_difference_body_area_2026-09-10.md`.

The first four inputs are the established C-II/report stack. FSDB is an unpromoted
September 10 report; its proof was checked directly: FS.4 gives approximate central
symmetry of the actual force hull, DB gives the inscribed diameter-direction polygon,
and Steiner's formula gives the finite area estimate.

No cyclic Reuleaux cap-detour estimate is used. No hull saturation is imposed, and
contact-isolated source points are not discarded; they are irrelevant to the area
partition because `F` is the convex hull of the nonisolated core.

## 5. Exact target implication

The low-defect circuit subbranch is excluded:

\[
\boxed{s_Z=0\quad\Longrightarrow\quad x_B+Q\not=o(D).}
\tag{5.1}
\]

This is independent of the previously known near-matching stability bound. It uses a
global force-hull area contradiction rather than a train-end count.

The theorem does **not** exclude the mandatory linear-defect regime. The live branches
are still:

- `s_Z=0`, cyclic or forest, with `x_B+Q=Omega(D)`;
- `s_Z>0`, where the same area argument has no circuit identity or train count;
- giant exceptional faces and high pinned/mixed surplus.

## 6. Regression audit

| Regression | Result | Reason |
|---|---|---|
| perfect matching | covered | it has `x_B=Q=s_Z=0`; the theorem recovers its area contradiction |
| regular odd shell | outside scope | it has `s_Z=2`, not `s_Z=0` |
| repeated outer-walk edges | retained | OP counts their pocket chains in (2.9) |
| exceptional faces | retained | their total defect is explicitly bounded in (2.12)--(2.13) |
| contact-isolated source points | retained | the force-hull area partition is geometric and does not assume they are absent |
| near-equilateral rhombi | retained | only `area(rhombus)\le1` is used |
| inward Reuleaux-pocket containment | not used | the withdrawn cyclic detour is irrelevant here |

## 7. Exact remaining lemma

The next useful inequality would be a quantitative upper bound on force-hull area in
the remaining linear-defect phase, for example one coupling

\[
x_B+Q+2s_Z\ge(2\rho/3-o(1))D
\]

to a strict area loss below `A_FS`, while retaining the exceptional-face and isolate
terms. No such upper tradeoff is currently proved.

## 8. Promotion recommendation

**Hold as report.** FSDB is not promoted, and this corollary should not be promoted
until FSDB and the train/OP dependencies receive the required audit and route-map
indexing.

## 9. Compact handoff

```text
STILL OPEN.

Conditional theorem LFD (using unpromoted FSDB):
  In s_Z=0, x_B+Q=o(D) is impossible.
  Exact identity b+Q=2h gives h<=pi D/2+o(D).
  Train count T=h+2f=pi D/2+o(D); Mantel gives at most pi^2 D^2/16+o(D^2)
  strict-rhombus area. OP pockets and exceptional faces have o(D^2) total area
  because x_B,Q=o(D). Hence area(F)<=pi^2 D^2/16+o(D^2).
  FSDB gives area(F)>=(A_FS-o(1))D^2 with A_FS>pi^2/16, contradiction.

Remaining: s_Z=0 with linear x_B/Q, and all s_Z>0 branches.
```
