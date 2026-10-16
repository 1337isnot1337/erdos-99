<!-- theorem-state: {"artifact_id":"ART-D7DFF2201291","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — quantitative stability makes the ST gap constructive

**Date:** 2026-09-10  
**Branch base:** `f977f2d0d25f5022c2a587e59cab38375d85caee`  
**Depends on:** DB, FSDB, FD/JC, SJ, and QS on this branch  
**Run type:** exact compact variational improvement  
**Target:** Target C, C-II after ZF  
**External input:** none  
**Computation:** exploratory decimal evaluation only; no decimal is a theorem claim

## LEVEL I STATUS

`STILL OPEN`.

ST proves a nonconstructive positive gap above

\[
\lambda_{SA}=0.5906428373093669\ldots .
\]

QS replaces that compactness-only gap by an explicit finite-dimensional variational
constant.  Define

\[
\mathcal R:=
\left\{(y,p):
2\rho\le y\le\pi,
\quad
g(y):=y+2\cos(y/2)\le p\le\pi
\right\}.
\tag{QV.1}
\]

Let

\[
A_{QS}(y,p):=\max\{\Phi(y),\mathcal Z(p)\},
\qquad
\Phi(y)=\frac{y+\sin y}{4},
\tag{QV.2}
\]

and

\[
m(y,p):=\min\{y,p-y\}.
\tag{QV.3}
\]

For `A>=0,m>=0`, put

\[
R(A,m):=
\frac{
\sqrt{4\pi(\pi^2+1)A-\pi^2m^2}-m
}{\pi^2+1}.
\tag{QV.4}
\]

Finally define

\[
\boxed{
\lambda_{QS}:=
\min_{(y,p)\in\mathcal R}
R(A_{QS}(y,p),m(y,p)).
}
\tag{QV.5}
\]

Then

\[
\boxed{
\liminf_{D\to\infty}
\frac{e_{BB}+2s_C}{D}
\ge\lambda_{QS}
>
\lambda_{SA}.
}
\tag{QV.6}

Thus the post-ST positive gap is now represented by a concrete compact optimization
whose inner stability term `mathcal Z(p)` is itself the unique root of the monotone
one-dimensional equation QS.3.11.  No unspecified compactness constant remains in the
statement of the improved threshold.

---

## 1. Extension and continuity of the stability envelope

QS defines `mathcal Z(p)` for `2<p<pi` by

\[
\mathcal Z(p)
=\frac{p a_s(p)}4,
\tag{1.1}
\]

where `a_s(p)` is the unique root in `(alpha(p),1)` of

\[
\frac{ap}{4}
=
\tau(a)
-p\sqrt{\frac{f(a)-p}{2}}
-\frac\pi2(f(a)-p).
\tag{1.2}
\]

The feasible post-ZF perimeter range is bounded below by `4rho>2`, so only the upper
endpoint needs to be added.  Set

\[
\boxed{\mathcal Z(\pi):=\pi/4.}
\tag{1.3}

As `p->pi`, both `alpha(p)` and the unique crossing `a_s(p)` tend to one; otherwise a
subsequence bounded below one would leave `f(a_s)-p` negative for large `p`, contrary
to its definition.  Hence

\[
\mathcal Z(p)=\frac{p a_s(p)}4\to\frac\pi4.
\tag{1.4}
\]

The implicit crossing is unique and transversal because the increasing branch
`ap/4` and decreasing branch `B(a,p)` have opposite `a` derivatives.  Standard
one-variable root continuity therefore gives continuity of `a_s(p)`, and hence of
`mathcal Z(p)`, on `[4rho,pi]` after the extension (1.3).

Thus the objective in QV.5 is continuous on the compact feasible region `mathcal R`,
and its minimum exists.

---

## 2. Every survivor lies above the variational constant

Take any post-ZF unbounded sequence and pass to a subsequence on which

\[
\frac hD\to y,
\qquad
\frac{\operatorname{per}F}{D}\to p,
\qquad
\frac{e_{BB}+2s_C}{D}\to\lambda.
\tag{2.1}
\]

DB gives `(y,p) in mathcal R`.  FSDB and QS give

\[
\liminf\frac{\operatorname{area}F}{D^2}
\ge
A_{QS}(y,p).
\tag{2.2}
\]

The actual-perimeter JC inequality gives

\[
A_{QS}(y,p)-\frac\pi4\lambda^2
\le
\frac{(\lambda+m(y,p))^2}{4\pi}.
\tag{2.3}
\]

The left side decreases in `lambda` and the right side increases; equivalently the
associated quadratic is increasing at and above its positive root.  Therefore

\[
\lambda
\ge
R(A_{QS}(y,p),m(y,p))
\ge
\lambda_{QS}.
\tag{2.4}
\]

Since the original sequence was arbitrary, QV.6's first inequality follows.

---

## 3. The improvement over SJ is strictly positive

Define the SJ objective

\[
J_{SA}(y,p)
:=
R\left(
\max\{\Phi(y),\Xi(p)\},
 m(y,p)
\right).
\tag{3.1}
\]

SJ proves that `J_SA` has a unique global minimum on `mathcal R`, at

\[
\boxed{
(y_*,p_*)=(y_*,2y_*),
}
\tag{3.2}
\]

where

\[
\Xi(p_*)=\Phi(y_*),
\qquad
p_*<\pi,
\tag{3.3}
\]

and

\[
J_{SA}(y_*,p_*)=\lambda_{SA}.
\tag{3.4}
\]

QS proves pointwise

\[
\mathcal Z(p)\ge\Xi(p)
\qquad(4\rho\le p\le\pi),
\tag{3.5}
\]

with strict inequality for every `p<pi`.  Since `R` is increasing in its area
argument,

\[
J_{QS}(y,p)
:=R(A_{QS}(y,p),m(y,p))
\ge
J_{SA}(y,p)
\tag{3.6}
\]

throughout `mathcal R`.

Suppose for contradiction that

\[
\lambda_{QS}=\lambda_{SA}.
\tag{3.7}
\]

Let `(y_0,p_0)` minimize `J_QS`.  Then

\[
\lambda_{SA}
=J_{QS}(y_0,p_0)
\ge J_{SA}(y_0,p_0)
\ge\lambda_{SA}.
\]

Thus `(y_0,p_0)` also minimizes `J_SA`.  By SJ uniqueness,

\[
(y_0,p_0)=(y_*,p_*).
\tag{3.8}
\]

But `p_*<pi`, so QS gives

\[
\mathcal Z(p_*)>\Xi(p_*)=\Phi(y_*).
\tag{3.9}
\]

Therefore the area argument in `J_QS(y_*,p_*)` is strictly larger than that in
`J_SA(y_*,p_*)`, while `m` is unchanged.  Since `R` is strictly increasing in area,

\[
J_{QS}(y_*,p_*)
>
J_{SA}(y_*,p_*)
=\lambda_{SA},
\]

contradicting (3.7).  Hence

\[
\boxed{\lambda_{QS}>\lambda_{SA}.}
\tag{3.10}
\]

This proves the second inequality in QV.6 exactly.

---

## 4. Constructive character of the new constant

`lambda_QS` is not an abstract existential epsilon.  It is determined by the following
nested compact/monotone computation:

1. for each `p`, solve the single monotone crossing equation (1.2) for `a_s(p)`;
2. set `mathcal Z(p)=p a_s(p)/4`;
3. evaluate the explicit JC root `R` in QV.4;
4. minimize that continuous function on the explicit compact region QV.1.

Every function involved is elementary.  A directed-rounding interval implementation
can therefore certify a rational lower bound for `lambda_QS` without any new
mathematics.

Exploratory high-precision floating-point optimization places the minimizer near

\[
y\approx1.53478422,
\qquad
p\approx3.06956844,
\]

and gives

\[
\lambda_{QS}\approx0.5906857323.
\tag{4.1}
\]

Equation (4.1) is **not** promoted as a certified bound in this report.  The theorem is
the exact variational inequality QV.6 and the strict comparison (3.10).

---

## 5. Why this is stronger than ST

ST already proves

\[
\lambda\ge\lambda_{SA}+\epsilon_{ST}
\]

for some unspecified `epsilon_ST>0`.  QV does not merely repeat that conclusion.  It
provides an explicit mathematical definition of a stronger constant `lambda_QS` that
can be evaluated and independently certified.  In particular the gap is now reduced
to finite elementary interval arithmetic rather than another geometric stability
lemma.

The exact relation is

\[
\boxed{
0<\lambda_{QS}-\lambda_{SA}
\le\text{the true post-ZF surplus gap above }\lambda_{SA}.
}
\tag{5.1}
\]

---

## 6. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| continuity/attainment of `lambda_QS` | proved | unique root continuity + compact feasible region |
| survivor lower bound `lambda>=lambda_QS` | proved asymptotically | DB + FSDB + QS + actual-perimeter JC |
| strict `lambda_QS>lambda_SA` | proved | pointwise domination + uniqueness of SJ minimizer + strict QS gain there |
| approximate `0.5906857323` | exploratory only | not interval-certified here |
| Level I | still open | no upper contradiction for all high-surplus survivors |

---

## 7. Next run

Certify a concrete decimal or rational bound below `lambda_QS` by interval arithmetic,
or prove enough monotonicity of `mathcal Z` to reduce QV.5 analytically to one scalar
transition equation.  The latter is preferable because it would localize the next
endpoint geometrically as well as numerically.
