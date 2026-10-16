<!-- theorem-state: {"artifact_id":"ART-6B6923EDF6F6","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Rogalski–Saint Raymond equality dependency audit

**Date:** 2026-09-10  
**Repository state:** `f0e565d92d331c74f672f32b2e2e6c81b587f61e` at branch start  
**Run type:** dependency audit / literature audit  
**Target:** Target C, C-II after ZF / FSDB / RSJ  
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md`  
**External web search:** used; primary Rogalski–Saint Raymond paper checked directly  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`.

The explicit Rogalski–Saint Raymond area lower bound used in
`target_c_symmetric_area_perimeter_joint_cavity_2026-09-10.md` survives this audit.
The subsequent endpoint-exclusion step does not follow from the cited 1985 paper.
That paper proves the sharp constant and notes that the Euclidean disk attains equality,
but explicitly leaves uniqueness of the equality case as an open problem.

Consequently the currently justified conclusion from the RSJ optimization is

\[
\boxed{
\liminf_{D\to\infty}\frac{e_{BB}+2s_C}{D}
\ge \lambda_R
=0.5921405436062881570\ldots,
}
\]

with `lambda_R` defined exactly in the RSJ report.  The stronger assertion

\[
\frac{e_{BB}+2s_C}{D}\ge\lambda_R+\epsilon_R
\]

for some absolute `epsilon_R>0` is not established by the cited equality theorem.
It becomes valid if one supplies the missing equality classification or another
source-specific theorem excluding all equality bodies at the RSJ perimeter.

This correction does not roll back FS, FSDB, GU, JC, or the two-variable RSJ
optimization.  It removes only the unsupported uniqueness-based strict-gap step.

---

## 1. Starting endpoint

The parent report combines the central symmetral

\[
S=\frac12\bigl((F-o)-(F-o)\bigr)
\]

with Rogalski–Saint Raymond's inequality

\[
\operatorname{area}S
\ge
c_R\left(\frac{\operatorname{per}S}{2}-D\right)^2,
\qquad
c_R=\frac{\pi}{(\pi-2)^2}.
\tag{1.1}
\]

Together with FSDB and the unrelaxed joint-cavity inequality, the parent report
minimizes the limiting feasible region and obtains the unique parameter point

\[
p_R=2y_R<\pi,
\qquad
\lambda_R=0.5921405436062881570\ldots .
\tag{1.2}
\]

Its Section 5 then attempts the implication

```text
lambda_D -> lambda_R
  -> normalized central symmetral S_D reaches equality in (1.1)
  -> S_infty is the Euclidean disk
  -> per(S_infty)=pi, contradicting p_R<pi
  -> uniform epsilon_R gap above lambda_R.
```

The first arrow is the compactness/equality-chain argument in the parent report.
The second displayed implication, equality in (1.1) forcing the disk, is the
specific dependency audited here.

---

## 2. Primary-source audit

The cited source is:

M. Rogalski and J. Saint Raymond, *Inequalities about Symmetric Compact Convex Sets
in the Plane*, American Mathematical Monthly 92 (1985), 466–480, Theorem 1.
Author-hosted scan:
`https://webusers.imj-prg.fr/~jean.saint-raymond/preprints/IneqR2.pdf`.

Theorem 1 proves the sharp inequality corresponding to (1.1) and states that the
Euclidean ball gives equality.  It does **not** state that the disk is the unique
equality body.

The decisive provenance check is the paper's concluding Section 10.  Its Problem 2
asks whether a symmetric compact convex set satisfying equality in the same inequality
must be the Euclidean ball.  Thus equality uniqueness was explicitly left open in the
cited source.

The paper does prove a narrower strictness statement in Remark 2: the inequality is
strict for symmetric polygons.  That is insufficient for the RSJ compactness argument,
because a Hausdorff limit of polygonal force hulls can be a nonpolygonal convex body.
No uniform polygonal strictness modulus is supplied there.

Therefore the parent report's sentence

> equality only for the disk

is stronger than the cited theorem and cannot presently be used as a dependency.

---

## 3. Strongest audited consequence retained

### Proposition RA.1 — the explicit RSJ floor does not use equality uniqueness

Assume the report-level FS.4, FD.1–FD.2, FSDB, GU, and JC inputs used by the parent
RSJ report.  Then every unbounded post-ZF survivor sequence satisfies

\[
\boxed{
\liminf_{D\to\infty}\frac{e_{BB}+2s_C}{D}
\ge\lambda_R,
}
\tag{RA.1}
\]

where `lambda_R` is the positive root specified by RSJ.2 and RSJ.5.

#### Proof

The proof through Sections 1–4 of the parent report uses only the inequality (1.1),
not its equality classification.  For every convergent parameter subsequence with

\[
y=\lim h/D,
\qquad
p=\lim \operatorname{per}(F)/D,
\qquad
\lambda=\lim (e_{BB}+2s_C)/D,
\]

that proof establishes

\[
\max\left\{
\frac{y+\sin y}{4},
\frac{\pi}{(\pi-2)^2}\left(\frac p2-1\right)^2
\right\}
-\frac\pi4\lambda^2
\le
\frac{(\lambda+\min\{y,p-y\})^2}{4\pi}.
\tag{RA.2}
\]

The analytic minimization in parent Sections 3–4 proves that the least nonnegative
`lambda` compatible with (RA.2) is `lambda_R`, attained in parameter space only at
`p=2y`, `y=y_R`.  Hence every subsequential limit of the normalized pinned/contact
currency is at least `lambda_R`, which is exactly (RA.1).  No statement about the
shape of an equality body is used. `square`

### Scope

RA.1 is an asymptotic theorem for the same post-ZF global-source class as the parent
report.  It retains every contact-isolated source point through the FS full-source
input.  It does not assert a positive gap above `lambda_R`.

---

## 4. The strict-gap step is conditional

### Proposition RA.2 — exact missing hypothesis for the parent endpoint exclusion

The parent Section 5 argument becomes valid under either of the following statements:

1. **global RSR equality uniqueness:** every centrally symmetric compact convex planar
   set satisfying equality in (1.1) is a disk; or
2. **source-specific equality exclusion:** no Hausdorff limit of normalized post-ZF
   central symmetrals can satisfy equality in (1.1) at perimeter `p_R`.

Under either statement there exists an absolute `epsilon_R>0` and `D_0` such that

\[
D\ge D_0
\Longrightarrow
\frac{e_{BB}+2s_C}{D}\ge\lambda_R+\epsilon_R.
\tag{RA.3}
\]

#### Proof

Assume no such uniform gap exists.  Choose survivors with `D_j>=j` and normalized
currency below `lambda_R+1/j`.  RA.1 forces convergence to `lambda_R`.  The unique
parameter minimization in the parent report gives

\[
y_j\to y_R,
\qquad
p_j\to p_R.
\]

The equality chain then forces the normalized central symmetrals to converge along a
subsequence to a centrally symmetric diameter-one body `S_infty` with perimeter
`p_R` and equality in (1.1).  Statement 1 would force `S_infty` to be the disk and
therefore to have perimeter `pi`, contradicting `p_R<pi`.  Statement 2 contradicts
the existence of `S_infty` directly. `square`

RA.2 isolates the exact missing input; it is conditional and is not a new Level I
result.

---

## 5. Later-literature search

A focused search found the later line of work by M. A. Hernández Cifre, G. Salinas,
and S. Segura Gomis on complete systems of inequalities for centrally symmetric planar
convex sets:

- *Complete systems of inequalities*, J. Inequal. Pure Appl. Math. 2 (2001), Art. 10;
- *Complete systems of inequalities for centrally symmetric planar convex sets*,
  Intern. Math. J. 2 (2002), 39–49;
- M. A. Hernández Cifre, G. Salinas, J. A. Pastor, S. Segura,
  *Complete systems of inequalities for centrally symmetric convex sets in the
  n-dimensional space*, Arch. Inequal. Appl. 1 (2003), 155–167.

The 2001 survey says that, because central symmetry gives `omega=2r` and `d=2R`,
the four three-parameter complete-system cases for centrally symmetric planar convex
sets had been solved in the cited 2000 preprint that became the 2002 paper.

This is directly relevant because the RSJ central symmetral has fixed
`(area, perimeter, diameter)` and `D=2R`.  However, this audit did not obtain a
primary-text theorem from the 2002 paper that states the lower `(A,p,D)` boundary or
an equality classification strong enough to replace the missing RSR uniqueness.
It is therefore recorded as a targeted literature lead, not imported as a theorem.

A general Santaló-diagram summary gives the classical lower bound

\[
16A^2\ge p(p-2D)^2(4D-p)
\]

only on `2D<=p<=3D`.  The RSJ optimizer has

\[
p_R=3.0200342875\ldots D>3D,
\]

so that classical branch does not reach the required endpoint.

---

## 6. Exact target implication

The justified frontier after this audit is

\[
\boxed{
\lambda:=\liminf\frac{e_{BB}+2s_C}{D}\ge\lambda_R,
\qquad
\lambda_R=0.5921405436062881570\ldots .
}
\tag{6.1}
\]

The claim `lambda>=lambda_R+epsilon_R` should not be treated as proved unless a later
source supplies the missing equality theorem.

This changes the next useful target.  A valid strengthening must do one of:

- solve or bypass the RSR equality case at `p=p_R`;
- obtain a strictly stronger centrally symmetric area lower bound at or near `p_R`;
- use the source-specific post-ZF geometry to exclude RSR equality bodies at `p_R`;
- derive a direct upper bound on `(e_BB+2s_C)/D` below `lambda_R`.

The final item would close C-II immediately against RA.1.

---

## 7. Regression and claim audit

| Claim | Classification | Decisive reason |
| --- | --- | --- |
| RSR sharp inequality (1.1) | literature import survives | Theorem 1 of the cited 1985 paper. |
| disk attains equality | literature import survives | Explicitly stated in Theorem 1. |
| disk is the only equality body | not proved by cited source | Section 10, Problem 2 asks exactly this uniqueness question. |
| strictness for symmetric polygons | literature import survives | Remark 2. |
| RSJ parameter minimum `lambda_R` | survives this dependency audit | Parent Sections 1–4 use only the inequality. |
| endpoint exclusion at `lambda_R` | unsupported as written | It invokes the missing equality uniqueness. |
| uniform `epsilon_R` gap | conditional | Follows from RA.2 only after equality exclusion. |
| regular odd shell regression | retained | Its normalized force hull approaches the disk and its currency is above the floor; no conflict. |
| contact-isolated population | retained | FS transports the full source circumradius before passing to the force hull. |

---

## 8. Failed route recorded

The implication

```text
sharp inequality + one known equality example
  -> unique equality example
  -> compactness gives a uniform strict gap
```

is invalid.  Sharpness determines the best constant, not the full equality set.
The cited source explicitly distinguishes those questions.

Likewise, Remark 2's strictness for every finite symmetric polygon does not provide a
uniform gap after Hausdorff passage.  A sequence of strict polygons can converge to an
equality body.

---

## 9. Canonical promotion recommendation

**Promote regression/correction only.**

The parent RSJ report is itself report-level.  It should receive a visible dependency
correction: retain RSJ.1–RSJ.5 and the explicit `lambda_R` floor; mark its Section 5
endpoint exclusion and RSJ.6 conditional pending an equality theorem.  No canonical
Target C module should promote the `epsilon_R` statement in its present form.

---

## 10. Next run

The highest-value immediate theorem is the centrally symmetric fixed
`(perimeter,diameter)` area lower boundary in the narrow range containing

\[
p/D=p_R=3.0200342875\ldots .
\]

First extract the exact 2002 centrally symmetric complete-system theorem and its
equality cases.  If it improves (1.1) at `p_R`, feed it into the retained RSJ
three-variable cavity optimization.  If it coincides with (1.1), check whether its
equality classification resolves the 1985 Problem 2.  If neither happens, return to
the source-specific `s_Z=0` circuit/attachment geometry rather than iterating another
uncontrolled scalar constant.

---

## 11. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Primary-source correction:
Rogalski-Saint Raymond (1985), Theorem 1 proves the sharp symmetric
area/perimeter/diameter inequality and says the disk attains equality, but Section 10
Problem 2 asks whether equality forces the disk. Therefore equality uniqueness is not
a theorem of the cited source.

What survives from RSJ:
    liminf (e_BB+2s_C)/D >= lambda_R
with
    lambda_R=0.5921405436062881570...
and the unique parameter optimizer
    y_R=1.51001714376294...,
    p_R=2y_R=3.02003428752589....

What does not currently survive:
    endpoint exclusion at lambda_R,
    existence of a uniform epsilon_R>0 above lambda_R.
Those become valid if RSR equality uniqueness, or a source-specific equality
exclusion at perimeter p_R, is proved.

Next:
extract the 2002 complete system for centrally symmetric planar convex sets in the
(A,p,D=2R) variables and its equality cases; feed any stronger boundary directly into
the RSJ cavity optimization.
```
