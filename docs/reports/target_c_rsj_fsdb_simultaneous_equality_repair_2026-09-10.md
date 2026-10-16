<!-- theorem-state: {"artifact_id":"ART-055DBD647A4E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — RSJ endpoint repaired by simultaneous FSDB equality rigidity

**Date:** 2026-09-10  
**Repository state:** branch `research/c2-circuit-attachment-20260910`, after `32f64249c7bfacefa4a288bdd855e7fcf2ac25fc`  
**Run type:** closing-implication repair / new convex-geometric stability theorem  
**Target:** Target C, C-II after ZF  
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md`  
**External web search:** used only for the preceding RSR provenance audit; no new external theorem is used here  
**Computation:** decimal values are diagnostic only; the proof is analytic

## LEVEL I STATUS

`STILL OPEN`.

The preceding dependency audit showed that Rogalski–Saint Raymond (1985) does not
prove the equality uniqueness invoked in Section 5 of
`target_c_symmetric_area_perimeter_joint_cavity_2026-09-10.md`.
This report repairs that endpoint **without** solving the RSR equality problem.

The key point is that approaching the RSJ optimizer forces equality not only in the
RSR area lower bound but also in the independent FSDB difference-body area lower
bound.  Equality in FSDB has a source-specific limiting shape: after normalization,
the force hull must coincide with the half diameter-direction polygon.  Near equality
in the elementary gap minimization then forces all projective diameter-direction gap
excess into one gap.  Its limiting perimeter is

\[
\boxed{
p_{FS}(y)=y+2\cos(y/2).}
\tag{RFS.1}
\]

At the unique RSJ optimizer, however,

\[
\boxed{p_R=2y_R.}
\tag{RFS.2}
\]

The parent report already proves

\[
y_R>\frac32>2\rho,
\qquad
\rho=\cos\rho,
\]

so

\[
2y_R>y_R+2\cos(y_R/2).
\tag{RFS.3}
\]

Thus the RSJ endpoint is impossible for a reason entirely internal to the Target C
geometry.  Consequently the uniform strict gap claimed as RSJ.6 is restored:

\[
\boxed{
\exists\epsilon_R>0\ \exists D_0<\infty\ \forall D\ge D_0,
\qquad
\frac{e_{BB}+2s_C}{D}
\ge
\lambda_R+\epsilon_R,
}
\tag{RFS.4}
\]

where

\[
\lambda_R=0.5921405436062881570\ldots .
\]

No classification of equality in the Rogalski–Saint Raymond inequality is used.

---

## 1. Exact implication to the C-II endpoint

Let

\[
y_D=\frac hD,
\qquad
p_D=\frac{\operatorname{per}F}{D},
\qquad
\lambda_D=\frac{e_{BB}+2s_C}{D}.
\]

The corrected RSJ argument through Sections 1–4 gives

\[
\liminf\lambda_D\ge\lambda_R,
\tag{1.1}
\]

with a unique parameter minimizer

\[
y_D\to y_R,
\qquad
p_D\to p_R=2y_R
\tag{1.2}
\]

whenever `lambda_D->lambda_R`.  Its Section 5 also proves from the unrelaxed GU/JC
upper chain that in this case

\[
\boxed{
\frac{\operatorname{area}F}{D^2}
\to
A_R:=\Phi(y_R)
=\frac{y_R+\sin y_R}{4}.
}
\tag{1.3}
\]

The new theorem proves that (1.2)–(1.3) are incompatible with FSDB.

The closing implication is therefore

```text
lambda_D -> lambda_R
  -> y_D -> y_R, p_D -> 2y_R, area(F_D)/D^2 -> Phi(y_R)
  + FSDB half-difference-body inclusion
  + equality stability of the diameter-direction gap problem
  -> p_D -> y_R + 2 cos(y_R/2)
  -> 2y_R = y_R + 2 cos(y_R/2)
  -> y_R = 2rho
  contradicts y_R > 3/2 > 2rho.
```

This is an exact contradiction with a fixed positive perimeter mismatch.

---

## 2. FSDB notation

For a post-ZF survivor let

\[
a_D=\arcsin\frac1{2D},
\qquad
\delta_D=2a_D.
\tag{2.1}
\]

Order the `h` projective directions of the actual diameter edges around the projective
circle and let

\[
g_{D,1},\ldots,g_{D,h}
\tag{2.2}
\]

be the gaps.  C67 and DB give

\[
g_{D,i}\ge\delta_D,
\qquad
\sum_i g_{D,i}=\pi.
\tag{2.3}
\]

Let

\[
P_D^{\rm dir}
:=D\operatorname{conv}\{\pm u_e:e\in E(H)\}
\tag{2.4}
\]

be DB's complete diameter-direction polygon.  Its exact area and perimeter are

\[
\operatorname{area}(P_D^{\rm dir})
=D^2\sum_i\sin g_{D,i},
\tag{2.5}
\]

and

\[
\operatorname{per}(P_D^{\rm dir})
=4D\sum_i\sin\frac{g_{D,i}}2.
\tag{2.6}
\]

FS.4 gives the full-source circumcenter `o_D` and FSDB proves, with
`L_D/D->0`,

\[
\boxed{
\frac12P_D^{\rm dir}
\subseteq
(F-o_D)+L_DB_2.
}
\tag{2.7}
\]

Define normalized convex bodies

\[
Q_D:=\frac1{2D}P_D^{\rm dir},
\qquad
\widehat F_D:=\frac1D(F-o_D),
\qquad
\epsilon_D:=\frac{L_D}{D}\to0.
\tag{2.8}
\]

Then

\[
\boxed{Q_D\subseteq\widehat F_D+\epsilon_DB_2.}
\tag{2.9}
\]

Also

\[
\operatorname{area}Q_D
=\frac14\sum_i\sin g_{D,i},
\tag{2.10}
\]

and

\[
\operatorname{per}Q_D
=2\sum_i\sin\frac{g_{D,i}}2.
\tag{2.11}
\]

---

## 3. New gap-stability lemma

### Lemma RFS.1 — asymptotic rigidity of the FSDB gap minimum

Let `D_j->infinity`, let `h_j/D_j->y` with `0<y<pi`, and let

\[
\delta_j=2\arcsin\frac1{2D_j}.
\]

Suppose angles

\[
g_{j,1},\ldots,g_{j,h_j}\ge\delta_j,
\qquad
\sum_i g_{j,i}=\pi
\]

satisfy the asymptotic FSDB area equality

\[
\sum_i\sin g_{j,i}
\longrightarrow
y+\sin y.
\tag{3.1}
\]

Then

\[
\boxed{
2\sum_i\sin\frac{g_{j,i}}2
\longrightarrow
y+2\cos\frac y2.
}
\tag{3.2}
\]

More precisely, after relabeling the gaps, if

\[
x_{j,i}:=g_{j,i}-\delta_j\ge0,
\qquad
X_j:=\sum_i x_{j,i}=\pi-h_j\delta_j,
\tag{3.3}
\]

then

\[
\boxed{
\sum_{i\ne i_j}x_{j,i}\to0
}
\tag{3.4}
\]

for an index `i_j` at which `x_{j,i}` is maximal.  Thus all asymptotic excess over the
C67 minimum gap is concentrated into one projective gap.

### Proof

Since `D_j delta_j->1` and `h_j/D_j->y`,

\[
X_j\to X:=\pi-y\in(0,\pi).
\tag{3.5}
\]

Write

\[
f_j(x):=\sin(\delta_j+x),
\qquad 0\le x\le X_j.
\]

For large `j`, `delta_j+x` lies in `(0,pi)` throughout this interval, so `f_j` is
strictly concave.  The standard concave-transfer argument gives the exact minimum

\[
\sum_i f_j(x_{j,i})
\ge
(h_j-1)f_j(0)+f_j(X_j).
\tag{3.6}
\]

The right side equals

\[
(h_j-1)\sin\delta_j
+
\sin\bigl(\pi-(h_j-1)\delta_j\bigr)
\to y+\sin y.
\tag{3.7}
\]

Hence (3.1) says that the deficit above the concave minimum in (3.6) tends to zero.

Let

\[
M_j:=\max_i x_{j,i},
\qquad
r_j:=X_j-M_j.
\tag{3.8}
\]

We show `r_j->0`.

First suppose along a subsequence that `M_j<=X_j/2`.  Among nonnegative vectors with
sum `X_j` and every coordinate at most `X_j/2`, concavity makes the minimum occur when
two coordinates equal `X_j/2` and all others vanish.  Therefore the deficit in (3.6)
is asymptotically at least

\[
2\sin(X/2)-\sin X>0,
\tag{3.9}
\]

because `0<X<pi`.  This contradicts the deficit tending to zero.  Thus eventually
`M_j>X_j/2`, so `0<=r_j<X_j/2`.

For such `j`, keep the largest coordinate `M_j=X_j-r_j`.  Concavity again minimizes
the contribution of all remaining coordinates, whose sum is `r_j`, by concentrating
that sum into one coordinate.  Hence the deficit in (3.6) is at least

\[
\begin{aligned}
\Delta_j(r_j):={}&
 f_j(X_j-r_j)+f_j(r_j)\\
&-f_j(X_j)-f_j(0).
\end{aligned}
\tag{3.10}
\]

If `r_j` failed to tend to zero, take a further subsequence with
`r_j->r in (0,X/2]`.  Then

\[
\Delta_j(r_j)
\to
\sin(X-r)+\sin r-\sin X.
\tag{3.11}
\]

Using the sum-to-product identity,

\[
\sin(X-r)+\sin r-\sin X
=2\sin(X/2)
\left[\cos(X/2-r)-\cos(X/2)\right]>0
\tag{3.12}
\]

for `0<r<=X/2`.  This again contradicts vanishing deficit.  Therefore `r_j->0`,
proving (3.4).

Now compare the half-angle sum with the one-excess-gap extremizer.  The function

\[
q_j(x):=\sin\frac{\delta_j+x}{2}
\]

is `1/2`-Lipschitz.  Moving all excess outside the maximal coordinate onto that
coordinate changes the excess vector in `l^1` distance exactly `2r_j`.  Hence

\[
\left|
\sum_i q_j(x_{j,i})
-
\left[(h_j-1)q_j(0)+q_j(X_j)\right]
\right|
\le r_j\to0.
\tag{3.13}
\]

Finally,

\[
(h_j-1)q_j(0)
=(h_j-1)\sin a_{D_j}
=\frac{h_j-1}{2D_j}
\to\frac y2,
\tag{3.14}
\]

and

\[
q_j(X_j)
=
\sin\frac{\pi-(h_j-1)\delta_j}{2}
=
\cos((h_j-1)a_{D_j})
\to\cos\frac y2.
\tag{3.15}
\]

Multiply (3.13) by two.  This proves (3.2). `square`

### Regression check

The exact one-large-gap configuration attains (3.6), so the lemma has the correct
limit.  Splitting a fixed positive amount of gap excess between two gaps produces the
strict positive defect (3.12), so no two-macroscopic-gap counterexample survives.
Distributing `o(1)` total excess over arbitrarily many gaps is allowed and changes the
half-angle sum by only `o(1)`, exactly as required.

---

## 4. New simultaneous-equality theorem

### Theorem RFS.2 — FSDB equality determines the limiting force-hull perimeter

Consider an unbounded post-ZF survivor sequence with

\[
\frac hD\to y\in(0,\pi)
\tag{4.1}
\]

and suppose

\[
\boxed{
\frac{\operatorname{area}F}{D^2}
\to\Phi(y)=\frac{y+\sin y}{4}.
}
\tag{4.2}
\]

Then

\[
\boxed{
\frac{\operatorname{per}F}{D}
\to y+2\cos(y/2).
}
\tag{4.3}
\]

### Proof

By FSDB's exact area formula and gap minimization,

\[
\operatorname{area}Q_D
=\frac14\sum_i\sin g_{D,i}
\ge
\frac14\left[
(h-1)\sin\delta_D+
\sin((h-1)\delta_D)
\right].
\tag{4.4}
\]

The right side tends to `Phi(y)`.  On the other hand, (2.9) and Steiner's formula give

\[
\operatorname{area}Q_D
\le
\operatorname{area}(\widehat F_D+\epsilon_DB_2)
=
\operatorname{area}\widehat F_D
+
\epsilon_D\operatorname{per}\widehat F_D
+
\pi\epsilon_D^2.
\tag{4.5}
\]

The normalized force hull has diameter one, so
`per(widehat F_D)<=pi`; hence the last two terms tend to zero.  By (4.2),

\[
\operatorname{area}Q_D\to\Phi(y).
\tag{4.6}
\]

Thus the lower bound (4.4) is asymptotically an equality, and Lemma RFS.1 gives

\[
\operatorname{per}Q_D
=2\sum_i\sin\frac{g_{D,i}}2
\to y+2\cos(y/2).
\tag{4.7}
\]

It remains to transfer this perimeter from `Q_D` to the force hull.  Both normalized
body sequences are uniformly bounded.  Indeed `Q_D` lies in the radius-`1/2` disk,
and FS's full-source circumradius bound places `widehat F_D` in a disk of radius
`1/2+o(1)` about the chosen source circumcenter.  Pass to a Hausdorff-convergent
subsequence

\[
Q_D\to Q_\infty,
\qquad
\widehat F_D\to F_\infty.
\tag{4.8}
\]

From (2.9),

\[
Q_\infty\subseteq F_\infty.
\tag{4.9}
\]

Equations (4.2) and (4.6) give

\[
\operatorname{area}Q_\infty
=
\operatorname{area}F_\infty
=
\Phi(y)>0.
\tag{4.10}
\]

Two planar compact convex bodies with positive area cannot be strictly nested while
having equal area: a point of `F_infty\Q_infty` together with an interior disk of
`Q_infty` would create a positive-area convex wedge outside `Q_infty`.  Hence

\[
Q_\infty=F_\infty.
\tag{4.11}
\]

Perimeter is continuous under Hausdorff convergence of planar convex bodies.  Therefore

\[
\lim\operatorname{per}\widehat F_D
=
\operatorname{per}F_\infty
=
\operatorname{per}Q_\infty
=
\lim\operatorname{per}Q_D.
\tag{4.12}
\]

Using (4.7) proves (4.3) on every convergent subsequence, hence on the original
sequence. `square`

### Geometric interpretation

RFS.1 says the limiting diameter directions fill one projective arc at the maximum
C67 density, leaving one macroscopic gap.  The normalized body `Q_D` converges to the
convex hull of two antipodal circular arcs on the radius-`1/2` circle.  Its two circular
arc pieces have total length `y` and its two closing chords have total length
`2 cos(y/2)`, which is exactly RFS.1.  This interpretation is not needed for the proof.

---

## 5. RSJ endpoint exclusion without RSR equality classification

### Theorem RFS.3 — repaired RSJ strict gap

Assume the report-level dependencies used in RSJ through Section 4, including FS.4,
FSDB, FD.1–FD.2, GU, and JC, and use only the **inequality** part of Rogalski–Saint
Raymond Theorem 1.  Then no unbounded post-ZF survivor sequence can satisfy

\[
\lambda_D\to\lambda_R.
\tag{5.1}
\]

Consequently RFS.4 holds for some absolute `epsilon_R>0`.

### Proof

Suppose (5.1).  The unique analytic minimization in RSJ Section 4 gives

\[
y_D\to y_R,
\qquad
p_D\to2y_R.
\tag{5.2}
\]

The GU/JC upper chain and the two area lower bounds, exactly as in RSJ (5.4)–(5.6),
give

\[
\frac{\operatorname{area}F}{D^2}
\to
A_R=\Phi(y_R).
\tag{5.3}
\]

Apply Theorem RFS.2 with `y=y_R`.  It forces

\[
p_D\to y_R+2\cos(y_R/2).
\tag{5.4}
\]

Comparing (5.2) and (5.4) yields

\[
y_R=2\cos(y_R/2).
\tag{5.5}
\]

Write `x=y_R/2`.  Then (5.5) is exactly

\[
x=\cos x.
\]

By uniqueness of the positive solution `rho` of `rho=cos rho`, this gives

\[
y_R=2\rho.
\tag{5.6}
\]

But the parent RSJ report proves `y_R>3/2`, while DB records `2rho<3/2`.  Contradiction.
Thus no endpoint sequence exists.

For the uniform gap, argue by diagonal sequence.  If no `epsilon_R>0,D_0` existed,
then for every integer `j` there would be a post-ZF survivor with

\[
D_j\ge j,
\qquad
\lambda_j<\lambda_R+1/j.
\]

The retained RSJ lower bound `liminf lambda>=lambda_R` would force
`lambda_j->lambda_R`, contradicting the endpoint exclusion just proved. `square`

### Fixed mismatch

For orientation only,

\[
y_R=1.51001714376294\ldots,
\]

so the two forced perimeter limits would be

\[
2y_R=3.02003428752588\ldots
\]

and

\[
y_R+2\cos(y_R/2)=2.96654848164832\ldots .
\]

Their difference is

\[
0.05348580587755\ldots>0.
\]

No decimal is needed for the sign: `y_R>3/2>2rho` proves it exactly.

---

## 6. Dependency audit

RFS uses the following inputs and no stronger forms:

1. **C67/DB:** distinct actual diameter directions have projective gap at least
   `delta_D=2 asin(1/(2D))`; all actual directions define `P_D^dir`.
2. **FS.4:** with the full-source circumcenter, the force hull is asymptotically
   centrally symmetric at Hausdorff scale `o(D)`.
3. **FSDB:** the resulting inclusion `(1/2)P_D^dir subset (F-o)+L_D B_2` and its exact
   area formula.
4. **Corrected RSJ Sections 1–4:** RSR is used only as an area inequality, not as an
   equality-classification theorem; the two-variable minimizer `(y_R,2y_R)` is unique.
5. **GU/JC:** the unrelaxed upper chain forces `area(F)/D^2->Phi(y_R)` when
   `lambda_D->lambda_R`.
6. Standard planar convex-body compactness and continuity of area/perimeter under
   Hausdorff convergence.

The proof retains contact-isolated source points because FS.4 obtains the center and
radius control from the entire source hull before transporting it to `F`.

---

## 7. Adversarial audit

### 7.1 Does area equality really force equality in the FSDB gap problem?

Yes.  Equation (4.4) is a lower bound for `area Q_D`; (4.5) is an upper bound tending
to the assumed limit `Phi(y)`.  Both squeeze `area Q_D` to `Phi(y)`.  Thus the exact
concave-gap lower bound has vanishing defect.

### 7.2 Could many tiny excess gaps alter the perimeter by order one?

No.  RFS.1 proves the **total** excess outside the largest gap tends to zero.  The
half-angle summand is `1/2`-Lipschitz, so the total perimeter error is bounded by this
total excess, not by the number of gaps.

### 7.3 Could `Q_infty` be a proper subset of `F_infty` with equal area?

No, because the common area `Phi(y)` is positive.  Proper inclusion of two compact
convex bodies when the smaller has interior adds positive area.

### 7.4 Is perimeter continuity legitimate?

Yes for planar compact convex bodies under Hausdorff convergence; equivalently use
Cauchy's perimeter formula and uniform convergence of support functions.

### 7.5 Does the proof assume the RSR equality body is the disk?

No.  The only RSR input is the inequality that participates in the RSJ parameter
optimization.  The endpoint contradiction is entirely between the RSJ forced
perimeter `2y_R` and the FSDB equality perimeter `y_R+2cos(y_R/2)`.

### 7.6 Odd-shell regression

The regular odd-shell family is not at FSDB equality for `y=y_R`; its normalized force
hull tends to the disk and its perimeter tends to `pi`, so RFS does not falsely exclude
it.  Dense isolated fillings likewise do not satisfy the global post-ZF/JC equality
chain needed to force (5.3).

### 7.7 Quantifiers

RFS.3 excludes **every** unbounded sequence of post-ZF survivors approaching the RSJ
endpoint.  The diagonal argument therefore yields a uniform nonexplicit positive gap
for all sufficiently large post-ZF survivors.  It does not yet exclude all such
survivors, because no contradictory upper bound on `e_BB+2s_C` is known.

---

## 8. Claim classification

| Claim | Classification | Reason |
| --- | --- | --- |
| RFS.1 gap-excess concentration | proved | strict concavity plus two-coordinate transfer |
| RFS.2 FSDB area equality fixes perimeter | proved | squeeze, Blaschke compactness, equal-area inclusion, perimeter continuity |
| RFS.3 RSJ endpoint impossible | proved | simultaneous equality forces two incompatible perimeter limits |
| uniform `epsilon_R>0` in RFS.4 | proved | diagonal-sequence compactness after endpoint exclusion |
| RSR equality uniqueness | not used / still unverified | preceding audit shows 1985 source leaves it open |
| explicit numerical value of `epsilon_R` | not proved | theorem is qualitative compactness separation |
| Level I | still open | no matching upper bound on pinned/contact currency |

---

## 9. Effect on the live endpoint

The provenance correction in
`target_c_rsr_equality_dependency_audit_2026-09-10.md` remains valid: the 1985 paper
must not be cited for equality uniqueness.  RFS.3 supplies a replacement proof of the
same **source-specific** strict endpoint exclusion that the parent RSJ report intended.

Thus the strongest justified report-level post-ZF statement is again

\[
\boxed{
\frac{e_{BB}+2s_C}{D}
\ge0.592140543606288\ldots+\epsilon_R
}
\]

for some absolute `epsilon_R>0` and all sufficiently large post-ZF survivors, but the
proof now uses simultaneous FSDB equality rigidity rather than an unsupported external
equality classification.

The new structural information is stronger than the scalar gap statement: any future
near-FSDB-equality sequence with `h/D->y` has force-hull perimeter pinned to
`y+2cos(y/2)` and its projective diameter directions have a single macroscopic gap.
This can be reused independently of RSJ.

---

## 10. Exact remaining implication

Level I still requires a contradiction for every post-ZF survivor.  After RFS, the
highest-value exact target remains an upper tradeoff on

\[
e_{BB}+2s_C
\]

that uses the retained `(y,p,lambda)` state.  A sufficient theorem is any uniform
upper bound

\[
\frac{e_{BB}+2s_C}{D}
\le\lambda_R+o(1),
\]

because RFS.4 would contradict it for large `D`.

The `s_Z=0` circuit phase is the cleanest place to seek such an upper bound: every
proper mixed edge set is independent, so the pinned row surplus can be bounded locally
by the size and internal mixed-edge content of each loaded attachment union.  The
next step should combine that exact circuit sparsity with the force-hull perimeter
parameter `p`, rather than discarding `p` into a scalar incidence count.

---

## 11. Promotion recommendation

**Promote after independent audit together with the RSR provenance correction.**

- Keep the RSR inequality in the RSJ dependency stack.
- Remove or correct every statement that attributes equality uniqueness to
  Rogalski–Saint Raymond (1985).
- Replace the parent Section 5 endpoint proof by RFS.1–RFS.3.
- The numerical `lambda_R` and the nonexplicit uniform strict gap then remain valid.

---

## 12. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

RSR provenance correction remains: 1985 does not prove disk uniqueness.

New repair RFS:
If h/D->y and FSDB's area lower bound is attained asymptotically,
    area(F)/D^2 -> Phi(y)=(y+sin y)/4,
then the projective diameter gap excess concentrates into one gap and
    per(F)/D -> y+2 cos(y/2).
Proof: squeeze Q=P_H/(2D) against F/D using FS.4; equal areas make their
Hausdorff limits equal; strict concavity of sin forces one-gap concentration;
perimeter continuity transfers the exact half-angle perimeter.

At the RSJ endpoint,
    y->y_R,
    p=per(F)/D->2y_R,
    area(F)/D^2->Phi(y_R).
RFS therefore also forces
    p->y_R+2cos(y_R/2).
These can agree only if y_R=2rho, rho=cos rho. But parent RSJ proves
    y_R>3/2>2rho.
Contradiction.

Hence no sequence reaches lambda_R and a diagonal argument restores
    (e_BB+2s_C)/D >= lambda_R+epsilon_R
for some absolute epsilon_R>0 and all sufficiently large post-ZF survivors,
without any RSR equality-classification assumption.

Next exact target: use s_Z=0 Laman-circuit sparsity plus retained (y,p,lambda)
to upper-bound e_BB+2s_C at or below lambda_R D+o(D).
```
