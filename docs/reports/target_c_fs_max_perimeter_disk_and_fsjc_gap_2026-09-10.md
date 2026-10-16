<!-- migration-source: path=docs/reports/target_c_fs_max_perimeter_disk_and_fsjc_gap_2026-09-10.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=9ef927f3ad26257c539819c3faca18ec57275572; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — FS maximal-perimeter disk rigidity excludes the FSJC endpoint

**Date:** 2026-09-10  
**Repository state:** `1ea7a3c5970d614c9f860841eea5ad3718ca171f` at start  
**Run type:** structural compactness theorem / endpoint exclusion / adversarial audit  
**Target:** Target C, C-II after ZF and FSJC  
**External input:** none  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

The September 10 FSJC theorem gives the explicit post-ZF bound

\[
\liminf\frac{e_{BB}+2s_C}{D}
\ge\lambda_{FSJC}
=0.5882283437736394\ldots
\]

and proves that equality can be approached only if `h/D -> pi/2`.  This report proves
that the FSJC endpoint itself is impossible.

The new structural input is a direct consequence of FS.4:

\[
\boxed{
\frac{\operatorname{per}F}{D}\to\pi
\quad\Longrightarrow\quad
\frac{\operatorname{area}F}{D^2}\to\frac\pi4.
}
\tag{FD.1}
\]

Thus a post-ZF force hull with asymptotically maximal perimeter is asymptotically a
disk in area.  No Groemer stability theorem or Blaschke--Lebesgue theorem is needed;
FS.4 supplies the missing approximate central symmetry.

Combining FD.1 with the **unrelaxed actual-perimeter** JC cavity inequality shows that
no unbounded survivor sequence can satisfy

\[
\frac{e_{BB}+2s_C}{D}\to\lambda_{FSJC}.
\]

Consequently there exist absolute constants `epsilon_FS>0` and `D_0<infinity` such
that every post-ZF survivor with `D>=D_0` satisfies

\[
\boxed{
\frac{e_{BB}+2s_C}{D}
\ge\lambda_{FSJC}+\epsilon_{FS}.
}
\tag{FD.2}
\]

The gap is nonexplicit.  This is a structural endpoint exclusion, not another finite
iteration of the old scalar detour bootstrap.

---

## 1. The central symmetral of the force hull

Let `o` be the full-source circumcenter supplied by FS and translate

\[
F_0:=F-o.
\]

Define the central symmetral

\[
\boxed{
S:=\frac12(F_0-F_0).
}
\tag{1.1}
\]

Then `S` is centrally symmetric about the origin.

### Lemma FD.1 — exact diameter and perimeter of the symmetral

\[
\boxed{
\operatorname{diam}S=D,
\qquad
\operatorname{per}S=\operatorname{per}F.
}
\tag{1.2}
\]

#### Proof

Every element of `S` is `(a-b)/2` with `a,b in F`.  For two such elements,

\[
\left|\frac{a-b}{2}-\frac{c-d}{2}\right|
\le\frac{|a-c|+|b-d|}{2}
\le D,
\]

so `diam(S)<=D`.  Since `F` itself has diameter `D`, choose `a,b in F` with
`|a-b|=D`.  Then `(a-b)/2` and `(b-a)/2` both lie in `S` and are distance `D` apart.
Thus `diam(S)=D`.

For perimeter, Cauchy's width formula and width additivity under Minkowski addition
give

\[
\operatorname{per}(F_0-F_0)
=\operatorname{per}(F_0)+\operatorname{per}(-F_0)
=2\operatorname{per}F.
\]

Scaling by `1/2` proves `per(S)=per(F)`. `square`

### Lemma FD.2 — FS.4 makes `F` and `S` equal in normalized area

Let

\[
L_D=\sqrt{D\eta+\eta^2},
\qquad
\eta=3^{1/4}\sqrt D.
\]

Then

\[
\boxed{
0\le\operatorname{area}S-\operatorname{area}F
\le
L_D\operatorname{per}F+\pi L_D^2
=o(D^2).
}
\tag{1.3}
\]

#### Proof

Brunn--Minkowski gives

\[
\operatorname{area}(S)^{1/2}
\ge
\frac12\left(
\operatorname{area}(F_0)^{1/2}
+
\operatorname{area}(-F_0)^{1/2}
\right)
=
\operatorname{area}(F)^{1/2},
\]

so `area(S)>=area(F)`.

FS.4 gives

\[
d_H(F_0,-F_0)\le2L_D,
\]

hence

\[
-F_0\subseteq F_0+2L_DB_2.
\]

By convexity,

\[
S=\frac12(F_0+(-F_0))
\subseteq F_0+L_DB_2.
\]

Steiner's formula therefore yields

\[
\operatorname{area}S
\le
\operatorname{area}F
+L_D\operatorname{per}F
+\pi L_D^2.
\]

Since `per(F)<=pi D` and `L_D=O(D^{3/4})`, the error is `O(D^{7/4})=o(D^2)`.
This proves (1.3). `square`

---

## 2. Maximal perimeter forces the disk

### Theorem FD — force-hull disk rigidity at maximal perimeter

For every unbounded post-ZF survivor sequence,

\[
\frac{\operatorname{per}F}{D}\to\pi
\]

implies

\[
\frac{\operatorname{area}F}{D^2}\to\frac\pi4.
\]

In fact the normalized central symmetrals `D^{-1}S` converge in Hausdorff distance to
the radius-`1/2` disk after passage to any subsequence.

#### Proof

Normalize

\[
\widetilde S:=D^{-1}S.
\]

By Lemma FD.1, `widetilde S` is centrally symmetric, has diameter one, and

\[
\operatorname{per}(\widetilde S)	o\pi.
\tag{2.1}
\]

A centrally symmetric diameter-one body is contained in the radius-`1/2` disk centered
at its symmetry center: if `x in widetilde S`, then `-x in widetilde S`, so
`2|x|=|x-(-x)|<=1`.  Hence the family is uniformly bounded.  Blaschke selection gives
Hausdorff convergence along a subsequence to a compact convex centrally symmetric body
`S_infty`.

Planar convex perimeter is continuous under Hausdorff convergence.  Thus

\[
\operatorname{per}(S_\infty)=\pi.
\tag{2.2}
\]

Its diameter is at most one.  Cauchy's width formula gives for every diameter-at-most-
one convex body

\[
\operatorname{per}(K)
=
\int_0^\pi w_K(\theta)\,d\theta
\le\pi,
\]

because `w_K(theta)<=1` pointwise.  Equality in (2.2), together with continuity of the
width function, forces

\[
w_{S_\infty}(\theta)=1
\qquad\text{for every }\theta.
\tag{2.3}
\]

Thus `S_infty` has constant width one.  Central symmetry says its support function
satisfies

\[
h(-u)=h(u).
\]

Constant width gives

\[
h(u)+h(-u)=1.
\]

Therefore `h(u)=1/2` for every unit direction `u`, so `S_infty` is exactly the closed
radius-`1/2` disk.

Every convergent subsequence has the same limit; hence the normalized symmetrals tend
to that disk.  In particular

\[
\frac{\operatorname{area}S}{D^2}\to\frac\pi4.
\]

Lemma FD.2 now gives

\[
\frac{\operatorname{area}F}{D^2}\to\frac\pi4.
\]

This proves FD. `square`

### Why FS.4 is decisive

Without approximate central symmetry, perimeter `pi D-o(D)` only forces a
constant-width limit.  A Reuleaux-type limit is not a disk.  FS.4 converts the actual
force hull to its central symmetral with `o(D^2)` area loss, and central symmetry turns
constant width into the disk.

---

## 3. The FSJC endpoint forces maximal perimeter

Write along a hypothetical endpoint sequence

\[
\lambda_D:=\frac{e_{BB}+2s_C}{D},
\qquad
 t_D:=\frac{e_{BB}}D,
\qquad
 y_D:=\frac hD,
\qquad
 p_D:=\frac{\operatorname{per}F}{D}.
\tag{3.1}
\]

Assume

\[
\lambda_D\to\lambda_*:=\lambda_{FSJC}.
\tag{3.2}
\]

FSJC proves

\[
y_D\to\frac\pi2.
\tag{3.3}
\]

Let

\[
A_D:=\frac{\operatorname{area}F}{D^2},
\qquad
C_D:=\frac{1}{D^2}\sum_r\operatorname{area}(P_r),
\qquad
G_D:=A_D-C_D.
\]

FSDB and GU give

\[
\liminf G_D
\ge
\Phi(\pi/2)-\frac\pi4\lambda_*^2,
\qquad
\Phi(y)=\frac{y+\sin y}{4}.
\tag{3.4}
\]

By the defining equation for `lambda_*`, the right side equals

\[
\boxed{
U_*:=\frac{(\lambda_*+\pi/2)^2}{4\pi}.
}
\tag{3.5}
\]

Now retain JC's actual-perimeter form rather than replacing `p_D` by `pi`:

\[
G_D
\le
\frac{
\left(t_D+\min\{y_D,p_D-y_D\}\right)^2
}{4\pi}
+o(1).
\tag{3.6}
\]

Here `t_D<=lambda_D`, `p_D<=pi`, and (3.3) gives

\[
\limsup\min\{y_D,p_D-y_D\}\le\frac\pi2.
\]

Therefore (3.6) gives

\[
\limsup G_D\le U_*.
\tag{3.7}
\]

Together with (3.4),

\[
G_D\to U_*.
\tag{3.8}
\]

Every inequality in the upper chain must therefore asymptotically saturate.  In
particular

\[
t_D\to\lambda_*
\tag{3.9}
\]

and

\[
\min\{y_D,p_D-y_D\}\to\frac\pi2.
\tag{3.10}
\]

Since `y_D->pi/2`, (3.10) forces

\[
\boxed{p_D\to\pi.}
\tag{3.11}
\]

Thus every FSJC endpoint sequence lies in the maximal-perimeter regime of Theorem FD.

---

## 4. Disk rigidity contradicts the FSJC cavity equality

Theorem FD and (3.11) give

\[
A_D\to\frac\pi4.
\tag{4.1}
\]

GU still gives

\[
\limsup C_D\le\frac\pi4\lambda_*^2.
\tag{4.2}
\]

Hence

\[
\liminf G_D
\ge
\frac\pi4-\frac\pi4\lambda_*^2.
\tag{4.3}
\]

But (3.8) gives `G_D->U_*`.  Subtract the FSJC defining equality (3.5), equivalently

\[
U_*=\Phi(\pi/2)-\frac\pi4\lambda_*^2,
\]

from (4.3).  The excess is exactly

\[
\begin{aligned}
\frac\pi4-\Phi(\pi/2)
&=
\frac\pi4-\frac{\pi/2+1}{4}\\
&=
\boxed{\frac{\pi-2}{8}>0.}
\end{aligned}
\tag{4.4}
\]

Thus (4.3) is larger than the forced limit `U_*` by a fixed positive amount,
contradiction.

Therefore:

### Theorem FDJ — FSJC endpoint exclusion

There is no unbounded post-ZF survivor sequence with

\[
\frac{e_{BB}+2s_C}{D}\to\lambda_{FSJC}.
\tag{4.5}
\]

---

## 5. Uniform nonexplicit gap above the FSJC floor

### Corollary FDJ.1

There exist `epsilon_FS>0` and `D_0<infinity` such that every post-ZF survivor with
`D>=D_0` satisfies FD.2:

\[
\frac{e_{BB}+2s_C}{D}
\ge\lambda_{FSJC}+\epsilon_{FS}.
\]

#### Proof

If no such constants existed, then for every integer `j` there would be a post-ZF
survivor with `D_j>=j` and

\[
\frac{e_{BB}+2s_C}{D_j}<\lambda_{FSJC}+\frac1j.
\]

FSJC already says every unbounded sequence has liminf at least `lambda_FSJC`.  Hence,
after choosing one such survivor for each `j`, the ratios would converge to
`lambda_FSJC`, contradicting FDJ. `square`

No numerical value for `epsilon_FS` is claimed.

---

## 6. Exact target implication

The report-level statement

\[
\liminf\frac{e_{BB}+2s_C}{D}\ge0.5882283437\ldots
\]

is now strengthened in two ways:

1. the endpoint is structurally impossible;
2. there is a uniform, although nonexplicit, positive gap above it for all sufficiently
   large post-ZF survivors.

This is stronger than running another finite DD/PI scalar iteration.  The contradiction
uses the global-source circumcenter through FS.4 and the equality geometry of the
actual force hull.

It still does not supply a universal upper bound on the pinned/contact currency, so
C-II remains open.

---

## 7. Regression audit

- **Regular odd shells:** their force hull tends to the disk and their loaded/contact
  currency is well above the excluded endpoint.  FD is compatible with them.
- **Reuleaux constant-width bodies:** excluded only after central symmetrization.  This
  is why FS.4 is essential; perimeter saturation alone would not imply a disk.
- **Dense isolated fillings:** retained.  FD applies to the actual force hull through
  the full-source FS.4 theorem and does not assume a small isolated population.
- **Perfect matching:** already closed independently by MFS; FDJ does not reuse that
  branch result.
- **Near-radial response is not an operator bound:** unused.  FDJ uses only the
  Hausdorff symmetry conclusion of FS.4, not arbitrary response boundary data.

---

## 8. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| `diam S=D`, `per S=per F` | proved exactly | difference body + Cauchy width additivity |
| `0<=areaS-areaF=o(D^2)` | proved | Brunn--Minkowski + FS.4 + Steiner |
| maximal-perimeter central symmetral tends to disk | proved | Blaschke compactness + Cauchy width equality + central symmetry |
| FD force-hull disk rigidity | proved | preceding two results |
| FSJC endpoint forces `p_D->pi` | proved | equality in actual-perimeter JC upper chain |
| endpoint cavity contradiction | proved | disk area exceeds FSDB endpoint area by `(pi-2)/8` |
| nonexplicit uniform gap | proved | diagonal sequence contradiction |
| explicit value of the new gap | not claimed | requires quantitative stability, unnecessary here |
| Level I | still open | no contradictory upper bound for all high-surplus sources |

---

## 9. Computation and reproducibility

No computation is used.  Every strict sign is exact; the final contradiction margin is
`(pi-2)/8>0`.

---

## 10. Canonical promotion recommendation

**Promote after review.**  FD is a short reusable structural consequence of FS.4, and
FDJ removes the exact equality regime left by FSJC.  Recommended canonical changes
after audit:

1. add maximal-perimeter disk rigidity to the post-FS Target C frontier;
2. record the pinned/contact lower bound as `lambda_FSJC + epsilon_FS` for some
   absolute `epsilon_FS>0`, not merely the printed `0.588228...` endpoint;
3. keep the gap nonexplicit unless a quantitative stability theorem is independently
   useful for a later branch.

---

## 11. Next run

Use the new disk-rigidity dichotomy away from the endpoint rather than optimize a
single number.  Split post-ZF survivors by normalized force-hull perimeter.  A
perimeter bounded away from `pi` reduces JC cavity capacity; a perimeter near `pi`
forces force-hull area near `pi/4` by FD.  The next useful result is a quantitative or
compactness-based two-parameter exclusion covering a whole interval of
`(p,lambda)`, ideally until it intersects a proved structural upper bound or forces a
new exact topology.

---

## 12. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Let S=(F-F)/2 after translating by the FS circumcenter.
Exactly:
    diam S=D,
    per S=per F.
FS.4 and Brunn-Minkowski give
    0 <= area(S)-area(F)
       <= L_D per(F)+pi L_D^2=o(D^2).
If per(F)/D->pi, then normalized S is centrally symmetric, diameter one, perimeter
pi. Cauchy width equality forces constant width one; central symmetry then forces
support h=1/2, so S is the radius-1/2 disk. Hence area(F)/D^2->pi/4.

If lambda=(e_BB+2s_C)/D->lambda_FSJC, FSJC gives h/D->pi/2. The actual-perimeter JC
bound and equality of the FSJC lower/upper gap force
    e_BB/D->lambda_FSJC,
    per(F)/D->pi.
FD then gives area(F)/D^2->pi/4. But GU bounds attachment-cell area by
(pi/4)lambda_FSJC^2D^2, so the attachment gap exceeds the JC endpoint upper bound by
exactly (pi-2)D^2/8. Contradiction.
Therefore the FSJC endpoint is impossible, and by a diagonal argument there exists an
absolute epsilon_FS>0 such that sufficiently large post-ZF survivors satisfy
    (e_BB+2s_C)/D >= lambda_FSJC+epsilon_FS.
```
