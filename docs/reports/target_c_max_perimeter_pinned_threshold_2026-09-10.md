<!-- migration-source: path=docs/reports/target_c_max_perimeter_pinned_threshold_2026-09-10.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=135ee64e62c349eda096383be60936b84d524f72; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — maximal force-hull perimeter forces a 0.693 pinned/contact threshold

**Date:** 2026-09-10  
**Repository state:** `f977f2d0d25f5022c2a587e59cab38375d85caee` at start  
**Run type:** closing-proof continuation / dependency audit / structural branch exclusion  
**Target:** Target C, C-II after ZF and the September 10 full-source symmetry reports  
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md` with the promoted September 9 C-I correction  
**External web search:** used only to look for sharper fixed-diameter convex inequalities; no external theorem is imported here  
**Computation:** decimal evaluation only; no computation is a proof dependency

## LEVEL I STATUS

`STILL OPEN`

The September 10 FDJ report excludes only the single FSJC endpoint

\[
\frac{e_{BB}+2s_C}{D}\to0.5882283437\ldots
\]

when its equality chain drives the force-hull perimeter to `pi D`.  The same disk-limit
mechanism is substantially stronger.  It excludes the entire maximal-perimeter regime
below an explicit larger threshold.

Put

\[
\ell_D:=\frac{e_{BB}+2s_C}{D},
\qquad
p_D:=\frac{\operatorname{per}F}{D}.
\]

Define

\[
\boxed{
\lambda_{\rm disk}:=
\frac{\pi\bigl(\sqrt{3\pi^2+4}-1\bigr)}{2(\pi^2+1)}
=0.693272542288314\ldots .
}
\tag{MP.1}
\]

Then every unbounded post-ZF survivor sequence with

\[
p_D\to\pi
\]

satisfies

\[
\boxed{
\liminf\ell_D\ge\lambda_{\rm disk}.
}
\tag{MP.2}
\]

Equivalently, for every fixed `lambda_0<lambda_disk` there are
`epsilon(lambda_0)>0` and `D_0(lambda_0)<infinity` such that every post-ZF survivor
with `D>=D_0` and `ell_D<=lambda_0` obeys

\[
\boxed{
p_D\le\pi-\epsilon(\lambda_0).}
\tag{MP.3}
\]

This is a branch elimination, not another unconditional scalar iteration: a low- or
medium-pinned-surplus survivor must now lose a fixed fraction of the maximum possible
force-hull perimeter.

---

## 1. Starting endpoint and exact implication chain

The current report-level C-II stack supplies two complementary facts.

First, FS.4 and FD show that the relative-interior force hull is asymptotically
centrally symmetric about the full-source circumcenter, and that maximal normalized
perimeter forces a disk limit:

\[
p_D\to\pi
\quad\Longrightarrow\quad
\frac{\operatorname{area}F}{D^2}\to\frac\pi4.
\tag{1.1}
\]

Second, ZK/GU and JC compare the force-hull area not occupied by the unloaded attachment
hulls with the total pinned/contact currency and the actual perimeter available to
outer pockets and exceptional faces.

The new implication is

```text
per(F)/D -> pi
    -> FS central symmetral tends to the radius-1/2 disk
    -> area(F)/D^2 -> pi/4
    -> attachment-cell gap >= (pi/4)(1-lambda^2)
JC actual-perimeter cavity capacity
    -> attachment-cell gap <= (lambda+pi/2)^2/(4pi)
    -> lambda >= lambda_disk = 0.6932725422...
```

Thus the maximal-perimeter branch is unavailable throughout the entire interval
`lambda<lambda_disk`.

---

## 2. Dependency audit

The proof below uses four report-level inputs.  They were rechecked for the specific
statements used here.

### 2.1 FS.4 and FD

`target_c_full_source_circumradius_response_2026-09-10.md`, FS.4, gives for the
full-source circumcenter `o`

\[
d_{\rm Haus}(F-o,-(F-o))=o(D).
\tag{2.1}
\]

More explicitly the right side is `2L_D` with `L_D=O(D^{3/4})`.

`target_c_fs_max_perimeter_disk_and_fsjc_gap_2026-09-10.md`, FD, forms the central
symmetral

\[
S=\frac12\bigl((F-o)-(F-o)\bigr).
\]

The two facts needed here are exact:

\[
\operatorname{diam}S=D,
\qquad
\operatorname{per}S=\operatorname{per}F,
\tag{2.2}
\]

and FS.4 gives

\[
0\le\operatorname{area}S-\operatorname{area}F=o(D^2).
\tag{2.3}
\]

For a centrally symmetric diameter-`D` body, symmetry about the origin places it
inside the radius-`D/2` disk.  If its perimeter divided by `D` tends to `pi`, Cauchy's
width formula forces every Hausdorff limit to have width one in every direction after
normalization.  Central symmetry then forces support function `1/2`, hence the disk.
This verifies (1.1).  No generic claim that a nearly maximal-perimeter nonsymmetric
body is near a disk is used.

### 2.2 ZK/GU attachment-cell capacity

Let the unloaded contact components have harmonic attachment hulls `P_r`, with
pairwise disjoint interiors, and put

\[
C_D:=\frac1{D^2}\sum_r\operatorname{area}(P_r).
\]

ZK gives

\[
L_2=6-3(d_H+s_Z)+e_{BB}+2s_C
\le6+e_{BB}+2s_C
\tag{2.4}
\]

and the attachment-hull estimate

\[
\sum_r\operatorname{area}(P_r)
\le\frac\pi4L_2^2+\pi L_2+\pi^2D.
\tag{2.5}
\]

Therefore, on any subsequence with `ell_D->lambda`,

\[
\boxed{\limsup C_D\le\frac\pi4\lambda^2.}
\tag{2.6}
\]

This is the only GU/ZK consequence used below.

### 2.3 JC with actual perimeter retained

Let

\[
G_D:=\frac1{D^2}
\left(
\operatorname{area}F-
\sum_r\operatorname{area}(P_r)
\right).
\tag{2.7}
\]

Write

\[
t_D:=\frac{e_{BB}}D,
\qquad
y_D:=\frac hD.
\]

The proof of JC.10--JC.16 gives, before replacing `per(F)` by `pi D`,

\[
E_{out}+Q
\le
 e_{BB}+
 \min\{h,\operatorname{per}F-h\}.
\tag{2.8}
\]

The same isoperimetric squaring and the `O(D)` charging remainder therefore give

\[
\boxed{
G_D
\le
\frac{\left(
 t_D+\min\{y_D,p_D-y_D\}
\right)^2}{4\pi}
+o(1).
}
\tag{2.9}
\]

This is exactly the actual-perimeter form already used in the FDJ report.  It is not a
new cavity estimate.

No assertion from the withdrawn force-bulk localization is used.  Contact-isolated
source points remain present through the full-source FS.4 input.

---

## 3. Theorem MP — maximal-perimeter pinned/contact threshold

### Theorem MP.1

Let `(A_j)` be any unbounded sequence of triangle-free, contact-then-diameter
lexicographically normalized post-ZF global minimizers, with diameters `D_j->infinity`.
Let `F_j` be their relative-interior force hulls.  If

\[
\frac{\operatorname{per}F_j}{D_j}\to\pi,
\tag{3.1}
\]

then

\[
\liminf_{j\to\infty}
\frac{e_{BB,j}+2s_{C,j}}{D_j}
\ge\lambda_{\rm disk}.
\tag{3.2}
\]

More sharply, if along a subsequence

\[
\frac{h_j}{D_j}\to y,
\]

then, with

\[
m(y):=\min\{y,\pi-y\},
\]

its pinned/contact limit `lambda` obeys

\[
\boxed{
(\pi^2+1)\lambda^2
+2m(y)\lambda
+m(y)^2-\pi^2
\ge0.
}
\tag{MP.4}
\]

Equivalently,

\[
\boxed{
\lambda\ge
\Lambda_{\rm disk}(y):=
\frac{-m(y)+
\pi\sqrt{\pi^2+1-m(y)^2}}
{\pi^2+1}.
}
\tag{MP.5}
\]

The minimum of `Lambda_disk(y)` over all admissible `y` occurs at `m(y)=pi/2`,
and equals `lambda_disk` in MP.1.

### Scope

This is an asymptotic theorem about the post-ZF C-II class only.  It uses global
minimum-diameter information through the full-source FS circumradius theorem and the
lexicographically normalized post-ZF stack.  It does not apply to arbitrary saturated
unit-distance frameworks or dense isolated shell fillings.

### Proof

Assume (3.1).  Put

\[
\ell_j:=\frac{e_{BB,j}+2s_{C,j}}{D_j}.
\]

If `liminf ell_j>=lambda_disk` there is nothing to prove.  Otherwise choose a
subsequence realizing a finite limit

\[
\ell_j\to\lambda<\lambda_{\rm disk}<1.
\tag{3.3}
\]

The exact ZT/ZU ledgers and `q<=pi D` make all normalized defect currencies bounded,
so after a further subsequence we may also assume

\[
t_j:=\frac{e_{BB,j}}{D_j}\to t,
\qquad
 y_j:=\frac{h_j}{D_j}\to y.
\tag{3.4}
\]

Since `e_BB<=e_BB+2s_C`,

\[
0\le t\le\lambda.
\tag{3.5}
\]

By FD and (3.1),

\[
\frac{\operatorname{area}F_j}{D_j^2}
\to\frac\pi4.
\tag{3.6}
\]

By (2.6),

\[
\limsup C_j\le\frac\pi4\lambda^2.
\]

Hence the normalized attachment-cell gap satisfies

\[
\boxed{
\liminf G_j
\ge\frac\pi4(1-\lambda^2).
}
\tag{3.7}
\]

On the other hand, (2.9), `p_j->pi`, and (3.4) give

\[
\limsup G_j
\le
\frac{(t+m(y))^2}{4\pi}
\le
\frac{(\lambda+m(y))^2}{4\pi}.
\tag{3.8}
\]

Combining (3.7) and (3.8),

\[
\pi^2(1-\lambda^2)
\le(\lambda+m(y))^2.
\tag{3.9}
\]

Rearranging proves MP.4.  The left side of MP.4, viewed as a quadratic in nonnegative
`lambda`, is strictly increasing above its unique positive root.  Solving for that
root gives MP.5.

For `0<=m<=pi/2`, the threshold root decreases as `m` increases: at fixed `lambda`
the expression

\[
(\pi^2+1)\lambda^2+2m\lambda+m^2-\pi^2
\]

is increasing in `m`.  Thus the weakest threshold occurs at the largest possible
`m`, namely `pi/2`.  Substituting `m=pi/2` gives

\[
(\pi^2+1)\lambda^2
+\pi\lambda
-\frac{3\pi^2}{4}=0.
\tag{3.10}
\]

Its positive root is exactly

\[
\lambda_{\rm disk}
=
\frac{\pi(\sqrt{3\pi^2+4}-1)}{2(\pi^2+1)}.
\]

This contradicts (3.3), proving MP.2. `square`

### Corollary MP.2 — uniform perimeter loss below the disk threshold

Fix any `lambda_0<lambda_disk`.  Then there exist constants
`epsilon(lambda_0)>0` and `D_0(lambda_0)<infinity` such that every post-ZF survivor
with `D>=D_0` and

\[
\frac{e_{BB}+2s_C}{D}\le\lambda_0
\]

satisfies

\[
\frac{\operatorname{per}F}{D}
\le\pi-\epsilon(\lambda_0).
\]

#### Proof

If not, for each positive integer `j` one could choose a survivor with `D_j>=j`,
`ell_j<=lambda_0`, and

\[
p_j>\pi-\frac1j.
\]

Then `p_j->pi` while `liminf ell_j<=lambda_0<lambda_disk`, contradicting MP.1.
`square`

### Why this is new

FDJ proves only that the FSJC endpoint `lambda_FSJC=0.588228...` cannot coexist with
the maximal-perimeter equality forced by that endpoint.  MP retains the disk area in
the cavity comparison for an arbitrary pinned/contact limit.  The resulting threshold
is `0.693272...`, so it excludes a full open interval of normalized surplus values
from the maximal-perimeter branch.  A repository search at the starting commit found
neither the constant nor this general threshold statement.

---

## 4. Exact target implication

The current low-surplus C-II feasible region splits rigorously as follows.

For every fixed

\[
\lambda_0<0.693272542288314\ldots,
\]

a sufficiently large post-ZF survivor with

\[
\frac{e_{BB}+2s_C}{D}\le\lambda_0
\]

must have a **uniform force-hull perimeter deficit**

\[
\pi D-\operatorname{per}F\ge\epsilon(\lambda_0)D.
\tag{4.1}
\]

Thus the low-surplus branch can no longer approach the constant-width/disk endpoint.
In particular FDJ is recovered immediately because

\[
\lambda_{FSJC}=0.5882283437\ldots<\lambda_{\rm disk}.
\]

The theorem does not yet contradict the exact C-II face inequality.  A survivor may
pay (4.1) while retaining enough outer-pocket/exceptional-face capacity to satisfy the
current JC bound.

---

## 5. Exact remaining lemma

The shortest new bridge to the C-II endpoint is now a perimeter-defect transfer, not
another endpoint compactness argument.

> **PD — perimeter-defect transfer.**  For every fixed `lambda_0<lambda_disk`, prove
> that a post-ZF survivor satisfying
> \[
> e_{BB}+2s_C\le\lambda_0D,
> \qquad
> \pi D-\operatorname{per}F\ge\epsilon D
> \]
> for some fixed `epsilon>0` either obeys
> \[
> b+Q>2h
> \]
> or admits an `n`-point unit-separated competitor of diameter `<D`.

Because ZF gives `b+Q=2h-2s_Z<=2h`, either conclusion closes that low-surplus
subbranch.  A valid proof must use information absent from the regular-shell and dense
isolated-fill regressions, namely global minimum-diameter finite capacity or the full
post-ZF mixed/contact topology.  Pure convex perimeter deficit alone is insufficient.

---

## 6. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| FD maximal-perimeter disk limit | audited dependency | direct central-symmetral/width proof checked |
| attachment-cell upper `limsup C_D<=pi lambda^2/4` | audited dependency | ZK finite bound with `L_2<=6+e_BB+2s_C` |
| JC actual-perimeter form MP.2.9 | audited dependency | retain `per(F)` in JC.5 before its Cauchy relaxation |
| MP.4 refined disk-cavity inequality | proved | direct lower/upper comparison |
| `lambda_disk=0.6932725422...` | proved exactly | positive root of MP.3.10 |
| uniform perimeter loss MP.3 | proved | contradiction/compactness from MP.1 |
| universal `ell_D>=lambda_disk` | not proved | perimeter-deficient branch remains |
| Level I | still open | high-surplus and perimeter-deficient branches survive |

---

## 7. Regression tests

| Regression | Passed? | Exact reason |
| --- | --- | --- |
| regular odd unit shell | yes | `per(F)/D->pi`, but `e_BB/D->pi`, far above `lambda_disk` |
| dense isolated filling of an odd shell | yes | isolates do not change the shell stress/currency; it remains above the threshold and lacks global optimality |
| FS exact odd-shell response regression | yes | MP uses no matching approximation and no response-trace bound |
| perfect matching | yes | already excluded independently by NB; MP makes no new matching assertion |
| Reuleaux/constant-width limit | yes | FS.4 central symmetrization is the step that rules out a nonsymmetric constant-width limit in FD |
| finite small sources | yes | MP is asymptotic and asserts a nonexplicit large-`D` threshold only |

The decisive use of global optimality beyond the shell regressions is inherited from
FS.4: its common circumcenter estimate comes from Oler on the **entire global source**
combined with the strict translated-lattice comparison at `D(n)`.  The shell fillings
have no certificate that their cardinality realizes `D(n)`.

---

## 8. Failed routes and no-go results

1. `per(F)/D->pi` by itself does not force a disk for a general convex force hull;
   constant-width nonsymmetric limits exist.  The FS.4 approximate central symmetry is
   essential.
2. MP does not imply the unconditional bound `ell_D>=lambda_disk`.  A sequence with a
   fixed normalized perimeter deficit is outside MP's hypothesis.
3. Replacing PD by a generic convex area-perimeter inequality is not enough.  The odd
   shell is asymptotically disk-like while remaining triangle-free, and dense isolated
   fillings retain the same force geometry without global optimality.

---

## 9. Literature search

A search was made for sharp minimum-area inequalities at fixed diameter and perimeter,
including Kubota/Kripfganz-type results.  No external theorem is used in MP.  Any such
inequality would still require a separate source-specific transfer to the exact C-II
face or competitor endpoint, so it is not imported merely to improve another decimal
constant.

---

## 10. Computation and reproducibility

No computation is logically required.  The displayed decimal is the evaluation of the
closed form MP.1.  The theorem is defined exactly by

\[
(\pi^2+1)\lambda_{\rm disk}^2
+\pi\lambda_{\rm disk}
-3\pi^2/4=0.
\]

---

## 11. Canonical promotion recommendation

**Hold as report pending independent audit.**

The proof depends on the September 10 FS/FD report chain, which is itself currently
report-level.  If those inputs are promoted, MP should be added as a post-ZF structural
branch theorem rather than merely as a numerical lower-bound update.

---

## 12. Next run

Attack PD using the exact outer-walk identity and mixed bridge topology.  In the
low-surplus range MP gives a linear gap between `pi D` and `per(F)`; JC currently treats
that gap only as reduced cavity perimeter.  The next useful theorem must charge a
linear fraction of this missing convex perimeter to `x_B`, `Q`, `s_Z`, or to a finite
rearrangement with preserved source cardinality.  The bridge-cut theorem and mixed
redundant rigidity are the first structural inputs to test because repeated outer-walk
bridge traversals are invisible to `per(F)` but are constrained by independent actual
diameter bypasses.

---

## 13. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

New theorem MP:
For any unbounded post-ZF survivor sequence, if
    per(F)/D -> pi,
then
    liminf (e_BB+2s_C)/D >= lambda_disk,
where
    lambda_disk = pi(sqrt(3pi^2+4)-1)/(2(pi^2+1))
                = 0.693272542288314...
More generally, if h/D->y, lambda obeys
    (pi^2+1)lambda^2 + 2m lambda + m^2 - pi^2 >= 0,
    m=min(y,pi-y).

Uniform consequence:
For every lambda_0<lambda_disk, sufficiently large survivors with
    (e_BB+2s_C)/D <= lambda_0
have
    per(F)/D <= pi-epsilon(lambda_0)
for some epsilon(lambda_0)>0.

Exact endpoint now:
Use that forced perimeter deficit to prove b+Q>2h or construct a strict sub-D
n-point competitor.  Pure convexity is insufficient; the transfer must use global
finite capacity or post-ZF mixed/contact topology.

Binding regressions:
regular odd shells; dense isolated shell fillings; no matching/trace shortcut.
```
