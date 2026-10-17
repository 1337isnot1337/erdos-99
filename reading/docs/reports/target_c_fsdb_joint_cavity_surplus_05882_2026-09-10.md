> Generated reading edition · [exact source](../../../docs/reports/target_c_fsdb_joint_cavity_surplus_05882_2026-09-10.md) · source SHA-256 `d9206c50e452e4dff789067d5d6c9fe68ae12f3e9119706fc11088348f23faf6`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-0FECCD139BF5","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_fsdb_joint_cavity_surplus_05882_2026-09-10.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=47512228a77ec399ab97a8d0fa8785b95305c339; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — FSDB raises the post-ZF pinned/contact floor to 0.588228

**Date:** 2026-09-10  
**Repository state:** `406800d59c56289626e28cae947340ab2a0b3499` at start  
**Run type:** exact asymptotic inequality synthesis / branch narrowing  
**Target:** Target C, C-II after ZF  
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md`  
**External web search:** not used  
**Computation:** decimal root evaluation only; proof is analytic

## LEVEL I STATUS

`STILL OPEN`

The September 9 joint-cavity theorem JC used PI's force-hull area floor and obtained

```math
\liminf\frac{e_{BB}+2s_C}{D}\ge0.4633168953\ldots,
```

later sharpened by detour arguments to `0.4702`.  The September 10 FSDB theorem gives a
substantially stronger area lower bound that depends on the actual normalized diameter
edge count

```math
y:=\lim\frac hD.
```

Feeding that functional lower bound into the **unrelaxed diameter-density-sensitive
JC inequality** gives

```math
\boxed{
\liminf_{D\to\infty}\frac{e_{BB}+2s_C}{D}
\ge
\lambda_{FSJC}
=0.5882283437736394387\ldots,
}
\tag{FSJC.1}
```

where `lambda_FSJC` is the unique positive root of

```math
\boxed{
(\pi^2+1)\lambda^2+\pi\lambda-\frac{\pi^2}{4}-\pi=0.
}
\tag{FSJC.2}
```

Equivalently,

```math
\lambda_{FSJC}
=
\frac{-\pi+
\sqrt{\pi^2+4(\pi^2+1)(\pi^2/4+\pi)}}
{2(\pi^2+1)}.
\tag{FSJC.3}
```

The minimizing diameter density is exactly

```math
\boxed{y=\pi/2.}
\tag{FSJC.4}
```

Thus any sequence whose pinned/contact currency approaches the new lower endpoint must
also satisfy `h/D -> pi/2`.  This extremal localization is part of the theorem, not a
numerical observation.

---

## 1. Starting endpoint

Pass to an arbitrary convergent post-ZF survivor subsequence and write

```math
\lambda:=\lim\frac{e_{BB}+2s_C}{D},
\qquad
t:=\lim\frac{e_{BB}}D,
\qquad
y:=\lim\frac hD.
\tag{1.1}
```

Then

```math
0\le t\le\lambda.
\tag{1.2}
```

DB gives

```math
\boxed{2\rho\le y\le\pi,}
\qquad
\rho=\cos\rho=0.7390851332\ldots,
\tag{1.3}
```

where the upper bound follows from `h<=q<=per(F)<=pi D`.

FSDB proves the diameter-density-sensitive force-hull area estimate

```math
\boxed{
\liminf\frac{\operatorname{area}F}{D^2}
\ge
\Phi(y):=\frac{y+\sin y}{4}.
}
\tag{1.4}
```

The GU attachment-cell estimate used in JC is unchanged and gives

```math
\limsup
\frac{\sum_r\operatorname{area}(P_r)}{D^2}
\le\frac\pi4\lambda^2.
\tag{1.5}
```

Hence the attachment-cell gap `G` obeys

```math
\boxed{
\liminf\frac G{D^2}
\ge
\Phi(y)-\frac\pi4\lambda^2.
}
\tag{1.6}
```

JC's unrelaxed diameter-density-sensitive cavity bound is

```math
\boxed{
\limsup\frac G{D^2}
\le
\frac{(t+m(y))^2}{4\pi},
\qquad
m(y):=\min\{y,\pi-y\}.
}
\tag{1.7}
```

The `O(D)` charging remainder vanishes after division by `D^2`.  Since `t<=lambda`,
(1.6)--(1.7) imply the necessary condition

```math
\boxed{
\Phi(y)-\frac\pi4\lambda^2
\le
\frac{(\lambda+m(y))^2}{4\pi}.
}
\tag{1.8}
```

Unlike the old scalar JC step, no replacement `m(y)<=pi/2` has yet been made.

---

## 2. Convert the feasible-region inequality to a quadratic

Multiply (1.8) by `4pi` and use `4pi Phi(y)=pi(y+sin y)`:

```math
\boxed{
F(y,\lambda):=
(\pi^2+1)\lambda^2
+2m(y)\lambda
+m(y)^2
-\pi(y+\sin y)
\ge0.
}
\tag{2.1}
```

For fixed `y`, `F(y,lambda)` is strictly increasing on `lambda>=0`, because

```math
\partial_\lambda F
=2(\pi^2+1)\lambda+2m(y)>0
```

except at the irrelevant simultaneous zero endpoint.  Thus every `y` has a unique
nonnegative threshold root whenever `F(y,0)<0`; any survivor must lie at or above that
root.

We now show the smallest threshold over the entire DB interval `y in [2rho,pi]` occurs
at `y=pi/2`.

---

## 3. Exact minimization at `y=pi/2`

Let `lambda_*` be the positive root of FSJC.2.  By construction,

```math
F(\pi/2,\lambda_*)=0,
\tag{3.1}
```

because `m(pi/2)=pi/2` and

```math
\pi\left(\frac\pi2+\sin\frac\pi2\right)
=\frac{\pi^2}{2}+\pi.
```

It suffices to prove

```math
F(y,\lambda_*)\le0
\qquad(2\rho\le y\le\pi),
\tag{3.2}
```

because `F` is increasing in `lambda`.  Then the threshold root at every `y` is at
least `lambda_*`.

### Left side: `2rho <= y <= pi/2`

Here `m(y)=y`, so

```math
F(y,\lambda_*)
=(\pi^2+1)\lambda_*^2
+2y\lambda_*+y^2
-\pi y-\pi\sin y.
```

Differentiate in `y`:

```math
\boxed{
\partial_yF
=2\lambda_*+2y-\pi(1+\cos y).
}
\tag{3.3}
```

A second derivative gives

```math
\partial_y^2F=2+\pi\sin y>0,
```

so (3.3) is increasing in `y`.  It is enough to check positivity at `y=2rho`.

The exact constant audit already gives

```math
\frac{739}{1000}<\rho<\frac{37}{50},
\qquad
\pi<\frac{22}{7}.
\tag{3.4}
```

Also `lambda_*>1/2`: substituting `lambda=1/2` into FSJC.2's left side gives

```math
\frac14-\frac\pi2<0,
```

and the quadratic is increasing for positive `lambda` after its positive root.

Because `cos(2rho)=2rho^2-1` and `rho<37/50`,

```math
\cos(2\rho)
<2\left(\frac{37}{50}\right)^2-1
=\frac{119}{1250}.
\tag{3.5}
```

Therefore

```math
\begin{aligned}
\partial_yF(2\rho,\lambda_*)
&=2\lambda_*+4\rho-\pi(1+\cos2\rho)\\
&>
1+4\frac{739}{1000}
-\frac{22}{7}\left(1+\frac{119}{1250}\right)\\
&=
\frac{4497}{8750}>0.
\end{aligned}
\tag{3.6}
```

Hence `F(y,lambda_*)` is strictly increasing on `[2rho,pi/2]`.  Since its value at
`pi/2` is zero,

```math
F(y,\lambda_*)<0
\qquad(2\rho\le y<\pi/2).
\tag{3.7}
```

### Right side: `pi/2 <= y <= pi`

Here `m(y)=pi-y`.  Differentiation gives

```math
\boxed{
\partial_yF
=-2\lambda_*-2(\pi-y)-\pi(1+\cos y)<0
}
\tag{3.8}
```

for every `y in [pi/2,pi]`.  Thus `F(y,lambda_*)` is strictly decreasing to the right
of `pi/2`, and again

```math
F(y,\lambda_*)<0
\qquad(\pi/2<y\le\pi).
\tag{3.9}
```

Equations (3.7), (3.9), and (3.1) prove (3.2), with equality only at `y=pi/2`.

Therefore every post-ZF subsequential limit satisfies

```math
\boxed{\lambda\ge\lambda_*.}
```

This proves FSJC.1.

---

## 4. Endpoint localization

The preceding proof is strict away from `y=pi/2`.  More precisely, for every
`epsilon>0`, compactness of

```math
[2\rho,\pi]\setminus(\pi/2-\epsilon,\pi/2+\epsilon)
```

and continuity give a positive threshold gap above `lambda_*` on that set.

Hence if a survivor sequence satisfies

```math
\frac{e_{BB}+2s_C}{D}\to\lambda_*,
```

then necessarily

```math
\boxed{\frac hD\to\frac\pi2.}
\tag{4.1}
```

This is the structural part of FSJC: a near-minimum pinned/contact survivor must also
be asymptotically at the midpoint of the two JC perimeter branches.

The exact JC proof then shows that any sequence approaching simultaneous equality must
also drive its actual force-hull perimeter toward `pi D` and exhaust the pocket/face
joint perimeter budget.  Those stronger equality consequences require a separate
stability audit before being promoted; they are not silently claimed here.

---

## 5. Exact target implication

The best explicit report-level post-ZF pinned/contact floor increases from

```math
0.4702
```

to

```math
\boxed{0.5882283437736394\ldots}.
```

This is not a closing upper/lower contradiction by itself.  The repository currently
contains no proved universal upper bound on `(e_BB+2s_C)/D` below this value.

The more useful change is the endpoint localization `h/D -> pi/2`: future work near the
new floor may use both sides of JC at equality rather than carry the entire DB interval
`[2rho,pi]`.

---

## 6. Exact remaining lemma

A closing continuation should not merely iterate this scalar floor.  The shortest
useful next theorem is one of the following equivalent types:

1. prove a universal upper bound
   ```math
   \limsup\frac{e_{BB}+2s_C}{D}<\lambda_{FSJC};
   
   ```
2. prove that the FSJC near-equality normal form `h/D -> pi/2` is incompatible with
   the post-ZF exact ledgers, mixed redundant rigidity, or FS.4 common-center geometry;
3. strengthen the cavity upper bound in a way that excludes every
   `lambda>=lambda_FSJC` allowed by current topology, rather than only raising the
   threshold again.

---

## 7. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| FSDB functional area floor `Phi(y)` | already proved | September 10 FSDB report |
| JC density-sensitive cavity bound | already proved | JC.16/JC.22 |
| necessary quadratic FSJC.2.1 | proved | direct substitution, only `t<=lambda` relaxed |
| minimizing density `y=pi/2` | proved exactly | piecewise derivative argument |
| floor `lambda_FSJC` | proved asymptotically | unique positive root at the exact minimizer |
| endpoint localization `h/D->pi/2` | proved | strict compact minimum away from midpoint |
| universal upper bound below new floor | not proved | remains a structural gap |
| Level I | still open | high pinned/contact surplus remains feasible under current inequalities |

---

## 8. Regression tests

| Regression | Passed? | Exact reason |
| --- | --- | --- |
| regular odd shell | yes | it has large loaded-loaded contact currency and is not excluded by the new lower bound |
| perfect matching | already excluded | MFS closes it independently by the FSDB/Mantel area gap |
| low `y=2rho` DB endpoint | yes | FSJC forces a strictly larger lambda threshold there than at `pi/2` |
| high `y` near `pi` | yes | `m(y)=pi-y` collapses cavity perimeter capacity and raises the required lambda |
| dense isolated fillings | yes | FSDB's full-source input retains isolates; FSJC does not assume core population saturation |

---

## 9. Failed routes and no-go results

The existing DD/DP detour inequality does not automatically close the new endpoint.
Once `lambda` rises above the FSJC threshold, the near-equality detour budget can grow
quickly; merely replacing `A_PI` by a larger constant in DP and repeating finite scalar
iterations is not a proof of incompatibility.  Any further use of DD should retain the
actual `y` and exact defect currencies rather than report another isolated decimal.

---

## 10. Computation and reproducibility

The proof is analytic.  The only numerical evaluation is the positive root of FSJC.2:

```math
\lambda_{FSJC}
=0.5882283437736394387149516348687232919\ldots .
```

The theorem and minimizer are defined exactly by FSJC.2 and `y=pi/2`; the decimal is
not a proof dependency.

---

## 11. Canonical promotion recommendation

**Hold as report pending independent audit.**  If FSDB and JC remain accepted, FSJC
should replace `0.4702` as the best explicit post-ZF pinned/contact floor and should add
the `h/D -> pi/2` endpoint localization to the Target C frontier.

---

## 12. Next run

Attack the near-FSJC endpoint structurally.  At `lambda=lambda_FSJC`, equality in the
relaxed proof requires `t=lambda`, `y=pi/2`, and simultaneous saturation of the JC
joint cavity capacity.  Audit the exact JC identities to determine whether those
conditions force `d_H=s_Z=c_B=0` and `per(F)/D->pi`; if so, combine FS.4 central
symmetry with the resulting constant-width limit and the exact contact/diameter
ledgers.  This has a concrete chance to produce a contradiction rather than another
scalar increment.

---

## 13. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

FSJC theorem:
Pass to a post-ZF subsequence with
    lambda=(e_BB+2s_C)/D -> lambda,
    t=e_BB/D -> t,
    y=h/D -> y.
DB: 2rho<=y<=pi. FSDB gives
    area(F)/D^2 >= Phi(y):=(y+sin y)/4-o(1).
GU gives attachment-cell area <=(pi/4)lambda^2D^2+o(D^2).
JC gives joint cavity capacity
    G/D^2 <=(t+min(y,pi-y))^2/(4pi)+o(1).
Using t<=lambda:
    (pi^2+1)lambda^2+2m(y)lambda+m(y)^2-pi(y+sin y)>=0,
    m(y)=min(y,pi-y).
The required positive root is minimized exactly at y=pi/2. Therefore
    liminf (e_BB+2s_C)/D >= lambda_FSJC,
where
    (pi^2+1)lambda_FSJC^2+pi lambda_FSJC-pi^2/4-pi=0,
    lambda_FSJC=0.5882283437736394387...
If the ratio tends to this endpoint, necessarily h/D->pi/2.

Perfect matching is already closed by MFS. Remaining target: exploit the FSJC equality
normal form or prove a structural upper bound below lambda_FSJC; do not merely iterate
scalar constants.
```
