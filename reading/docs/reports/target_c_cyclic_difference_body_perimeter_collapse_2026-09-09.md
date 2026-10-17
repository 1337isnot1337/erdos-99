> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_difference_body_perimeter_collapse_2026-09-09.md) · source SHA-256 `6c540f9214506104c3b68a4ce6c3107d571fe44ff7a86c612fdcb67553f05221`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Presentation repairs: 9 exact-source-bound TeX/escape correction(s); [reviewed repair ledger](../../../docs/publication/reading-tex-repairs.json). Frozen source bytes are unchanged.

> Source formatting note: 30 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-FD509000488C","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic endpoint: difference-body perimeter collapse

**Date:** 2026-09-09  
**Repository base:** PR #118 reconciled with main `6ed9d78ae146b68fd9b14c3c3486b048f3d59074`  
**Run type:** exact difference-body / perimeter bootstrap  
**Target:** Target C cyclic primitive endpoint  
**Depends on:** CY cyclic shell `per(F)=q`, `h=q-d_H` with `d_H<=2`; main-branch DA diameter-direction polygon and gap lower bound; Cauchy/Minkowski perimeter additivity and planar isoperimetry  
**External web search:** not used in the proof  
**Computation:** only numerical sanity checks; no computation enters the theorem

## LEVEL I STATUS

`STILL OPEN`

The cyclic primitive endpoint has enough extra structure to use the new DA diameter-direction polygon much more strongly than the generic Rogers--Shephard argument.

DA constructs

```math
P_H
:=D\operatorname{conv}\{\pm u_h:h\in H\}
\subseteq F-F,
```

where the `u_h` are the `h` projective diameter directions. In a cyclic survivor

```math
\operatorname{per}(F)=q,
\qquad
h=q-d_H,
\qquad
0\le d_H\le2.
```

The key observation is that the difference body itself has perimeter exactly `2q`. Isoperimetry on `F-F`, rather than Rogers--Shephard back to `F`, forces the cyclic perimeter ratio to the **maximum possible value**:

```math
\boxed{
\frac qD\longrightarrow\pi,
\qquad
\frac hD\longrightarrow\pi.}
\tag{DP.1}
```

In fact the perimeter deficit is second-order small:

```math
\boxed{
0\le \pi D-q
\le
\frac{\pi}{12D}+O(D^{-2}).}
\tag{DP.2}
```

Thus the cyclic force hull is not merely a long equilateral polygon. It asymptotically saturates the Rosenthal--Szasz perimeter-diameter inequality at rate `O(1/D)`.

---

## 1. Exact finite difference-body inequality

Let

```math
\delta_D:=2\arcsin\frac1{2D}.
```

DA/C67 gives pairwise projective separation at least `delta_D` between actual diameter directions. If the `h` projective gaps are `g_i`, then

```math
g_i\ge\delta_D,
\qquad
\sum_i g_i=\pi,
```

and

```math
\operatorname{area}(P_H)
=D^2\sum_i\sin g_i.
\tag{1.1}
```

Concavity of sine gives the exact DA lower bound

```math
\boxed{
\operatorname{area}(P_H)
\ge
D^2\left[
(h-1)\sin\delta_D
+
\sin((h-1)\delta_D)
\right].}
\tag{DP.3}
```

Here the final sine uses

```math
\sin(\pi-(h-1)\delta_D)
=\sin((h-1)\delta_D).
```

Now use

```math
P_H\subseteq F-F.
\tag{1.2}
```

For planar convex bodies perimeter is Minkowski additive. Since `per(-F)=per(F)`,

```math
\boxed{
\operatorname{per}(F-F)
=2\operatorname{per}(F)
=2q.}
\tag{1.3}
```

Equivalently, Cauchy's perimeter formula gives this immediately from

```math
w_{F-F}(\theta)=w_F(\theta)+w_F(\theta+\pi)=2w_F(\theta)
```

after integration over one projective period.

Planar isoperimetry applied to the centrally symmetric convex body `F-F` gives

```math
\boxed{
\operatorname{area}(F-F)
\le
\frac{(2q)^2}{4\pi}
=\frac{q^2}{\pi}.}
\tag{1.4}
```

Combining DP.3, (1.2), and (1.4):

### Theorem DP.1 — exact cyclic difference-body inequality

Every cyclic primitive survivor satisfies

```math
\boxed{
D^2\left[
(h-1)\sin\delta_D
+
\sin((h-1)\delta_D)
\right]
\le
\frac{q^2}{\pi}.}
\tag{DP.5}
```

No population asymptotic, Favard theorem, or contact-stress coefficient enters DP.5.

---

## 2. The only possible perimeter-density limit is `pi`

Take any unbounded cyclic survivor sequence. Put

```math
y_j:=\frac{h_j}{D_j}.
```

Since `h<=q<=pi D`, the sequence is bounded. Pass to any convergent subsequence

```math
y_j\to y.
```

CY gives

```math
0\le q_j-h_j=d_H\le2,
```

so

```math
\frac{q_j}{D_j}\to y.
\tag{2.1}
```

Also

```math
D\delta_D
=2D\arcsin\frac1{2D}
\longrightarrow1,
```

and

```math
D\sin\delta_D
=
\sqrt{1-\frac1{4D^2}}
\longrightarrow1.
```

Therefore DP.5 divided by `D^2` gives in the limit

```math
\boxed{
y+\sin y\le\frac{y^2}{\pi}.}
\tag{2.2}
```

Define

```math
\Phi(y):=\pi(y+\sin y)-y^2.
```

For `0<y<pi`,

```math
\Phi''(y)
=-\pi\sin y-2<0.
\tag{2.3}
```

Thus `Phi` is strictly concave on `[0,pi]`. Moreover

```math
\Phi(0)=0,
\qquad
\Phi(\pi)=0.
```

Strict concavity therefore gives

```math
\boxed{\Phi(y)>0\quad(0<y<\pi).}
\tag{2.4}
```

Inequality (2.2) is equivalent to `Phi(y)<=0`. The post-ZF lower bounds exclude `y=0`, so the only possible subsequential limit is

```math
y=\pi.
```

Every convergent subsequence has that limit, proving DP.1. `square`

This supersedes the cyclic Favard threshold `2.6189005...`: the actual limit is the maximal perimeter ratio `pi`.

---

## 3. Quantitative perimeter-deficit rate

Put

```math
\boxed{t_D:=\pi D-q\ge0.}
\tag{3.1}
```

DP.1 first gives

```math
t_D=o(D).
\tag{3.2}
```

Fix one of the three possible values `d=d_H in {0,1,2}` along a subsequence, and write

```math
n:=h-1=q-d-1
=\pi D-t_D-d-1.
\tag{3.3}
```

Use the standard expansions

```math
\boxed{
\delta_D
=
\frac1D+\frac1{24D^3}+O(D^{-5}),}
\tag{3.4}
```

and, exactly before expansion,

```math
\sin\delta_D
=
\frac1D\sqrt{1-\frac1{4D^2}}
=
\frac1D-\frac1{8D^3}+O(D^{-5}).
\tag{3.5}
```

Since `t_D=o(D)`, (3.3)--(3.5) give

```math
\begin{aligned}
n\sin\delta_D
&=
\pi-
\frac{t_D+d+1}{D}
-
\frac\pi{8D^2}
+O\left(\frac{t_D+1}{D^3}\right),
\end{aligned}
\tag{3.6}
```

and

```math
n\delta_D
=
\pi-
\frac{t_D+d+1}{D}
+
\frac\pi{24D^2}
+O\left(\frac{t_D+1}{D^3}+D^{-4}\right).
\tag{3.7}
```

Let

```math
u_D
:=
\pi-n\delta_D.
```

Then `u_D=o(1)`, and

```math
\sin(n\delta_D)=\sin u_D
=u_D+O(u_D^3).
\tag{3.8}
```

Combining (3.6)--(3.8), the two linear terms in `t_D+d+1` cancel:

```math
\boxed{
 n\sin\delta_D+\sin(n\delta_D)
=
\pi-\frac\pi{6D^2}
+O\left(
\frac{t_D+1}{D^3}
+
\left(\frac{t_D+1}{D}\right)^3
\right).}
\tag{3.9}
```

The right side of DP.5 is

```math
\frac{q^2}{\pi D^2}
=
\pi-\frac{2t_D}{D}
+
\frac{t_D^2}{\pi D^2}.
\tag{3.10}
```

Suppose first that `D t_D` were unbounded along a subsequence. Divide the inequality obtained from (3.9)--(3.10) by `t_D/D`. Because `t_D=o(D)`, every error term and the quadratic term are `o(1)` relative to `t_D/D`, while the term `pi/(6D^2)` is also `o(t_D/D)` when `Dt_D->infinity`. The inequality would reduce to

```math
0\le -2+o(1),
```

a contradiction.

Therefore

```math
\boxed{t_D=O(D^{-1}).}
\tag{3.11}
```

Insert this improved scale back into (3.9). The error is now `O(D^{-3})`, while the final quadratic term in (3.10) is `O(D^{-4})`. DP.5 yields

```math
\pi-\frac\pi{6D^2}+O(D^{-3})
\le
\pi-\frac{2t_D}{D}+O(D^{-4}).
```

Hence

```math
\boxed{
 t_D
\le
\frac\pi{12D}+O(D^{-2}).}
\tag{3.12}
```

This proves DP.2. `square`

The argument is uniform over the three bounded values of `d_H`, so no subsequence restriction remains in the final estimate.

---

## 4. The `d_H=0` phase also has a lower perimeter-deficit scale

If `d_H=0`, then

```math
h=q.
```

The projective separation gaps themselves must fit on the projective circle:

```math
h\delta_D\le\pi.
\tag{4.1}
```

Using

```math
q=\pi D-t_D
```

and (3.4),

```math
q\delta_D
=
\pi-\frac{t_D}{D}+\frac\pi{24D^2}+O(D^{-3}).
```

Thus (4.1) gives

```math
\boxed{
 t_D
\ge
\frac\pi{24D}+O(D^{-2})
\qquad(d_H=0).}
\tag{DP.6}
```

Together with DP.2,

```math
\boxed{
\frac\pi{24D}+O(D^{-2})
\le
\pi D-q
\le
\frac\pi{12D}+O(D^{-2})
\qquad(d_H=0).}
\tag{DP.7}
```

The regular odd unit shell has

```math
D=\frac1{2\sin(\pi/(2q))}
```

and asymptotically attains the lower scale

```math
D(\pi D-q)\to\frac\pi{24}.
```

Thus DP.6 is consistent with, and sharp at leading order for, the regular-shell regression.

---

## 5. Near equality of the difference body

DP.1-DP.2 force

```math
\frac{\operatorname{per}(F-F)}D
=
\frac{2q}{D}
\longrightarrow2\pi.
```

The diameter of `F-F` is at most `2D`. Rosenthal--Szasz/Cauchy perimeter-diameter inequality therefore also becomes asymptotically sharp.

Moreover DP.5 and the exact upper bound show

```math
\frac{\operatorname{area}(F-F)}{D^2}
\longrightarrow\pi,
\tag{5.1}
```

and

```math
\frac{\operatorname{area}(P_H)}{D^2}
\longrightarrow\pi.
\tag{5.2}
```

Indeed the DA lower tends to `pi+sin pi=pi`, while the isoperimetric upper `q^2/(pi D^2)` also tends to `pi`.

Thus the centrally symmetric bodies

```math
D^{-1}(F-F)
```

asymptotically saturate planar isoperimetry with perimeter `2pi`. Quantitative isoperimetric compactness therefore forces them, after translation (unnecessary here because difference bodies are centrally centered), toward the unit disk in the usual Hausdorff/measure senses available from standard stability theorems.

At the purely support-function level, if an actual subsequential Hausdorff limit exists, perimeter and diameter equality imply it has constant width `2` as a difference body; central symmetry then makes the limit the unit-radius disk.

Hence the cyclic branch has an asymptotically disk-like difference body even though the primal force hull need not itself approach a disk; constant-width primal limits remain possible.

---

## 6. Projective diameter directions asymptotically fill the circle

Let the projective gaps be `g_i>=delta_D`. Their total excess above the minimum is

```math
E_{dir}
:=
\sum_i(g_i-\delta_D)
=
\pi-h\delta_D.
\tag{6.1}
```

Since

```math
h=q-d_H=\pi D-t_D-d_H
```

and DP.2 gives `t_D=O(1/D)`, expansion of `delta_D` gives

```math
\boxed{
E_{dir}
=
\frac{d_H}{D}+O(D^{-2}).}
\tag{DP.8}
```

In particular:

- if `d_H=0`, the total projective gap excess is `O(D^{-2})`;
- if `d_H=1`, it is `D^{-1}+O(D^{-2})`;
- if `d_H=2`, it is `2D^{-1}+O(D^{-2})`.

Since every individual excess is nonnegative, **every** projective diameter-direction gap satisfies

```math
\boxed{
0\le g_i-\delta_D
\le
\frac{d_H}{D}+O(D^{-2}).}
\tag{DP.9}
```

Thus the actual diameter directions become asymptotically uniformly spaced around the complete projective circle, with total defect controlled only by the constant `d_H`.

For `d_H=0`, the uniformity is one order sharper: all `h=q` direction gaps equal the minimum `1/D+O(D^{-2})` up to a total `O(D^{-2})` budget.

---

## 7. What this does to the cyclic endpoint

The exact primitive cycle has now collapsed to a near-equality geometry:

1. `q=pi D+O(1/D)` loaded unit hull sides;
2. `h=q-d_H` actual diameter edges with `d_H<=2`;
3. projective diameter directions filling the circle almost uniformly;
4. `F-F` asymptotically the radius-`D` disk;
5. the source still contains `Delta D^2-O(D)` contact-isolated points by CY.

The remaining cyclic problem is therefore a stability/classification problem near constant width, not a general convex-shell problem.

---

## 8. Relation to Favard and PI

The preceding Favard bootstrap proved only

```math
\liminf q/D\ge2.6189005\ldots .
```

DP supersedes that constant completely:

```math
q/D\to\pi.
```

PI likewise becomes asymptotically saturated in direction spread; it remains useful for interpreting the nearly perpendicular diameter pairs but is no longer the best cyclic scalar bound.

The Favard report remains useful as an independent convex-envelope derivation and as a possible stability tool, but not as the current cyclic perimeter endpoint.

---

## 9. Next theorem

The cyclic branch is now extremely narrow. Two high-value routes remain:

### DP-A — constant-width/equilateral stability

Classify convex equilateral polygons with

```math
q=\pi D+O(D^{-1})
```

and `q-O(1)` actual diameter pairs whose projective directions have total spacing defect `O(1/D)`. Show that they must be quantitatively close to the regular odd-shell geometry, or exclude the `d_H=1,2` topologies.

### DP-B — rattler replacement in an almost constant-width carrier

Use the `Delta D^2-O(D)` contact-isolated population together with the fact that `F-F` is disk-like and the shell has only `O(D)` points. A force-free replacement theorem only needs to perturb this near-constant-width boundary while retaining the quadratic interior cloud.

Either route is substantially more rigid than the pre-DP cyclic endpoint.

---

## 10. Promotion recommendation

**Hold as report pending independent audit.**

DP.5 and DP.1 use only exact main-branch DA inputs plus elementary Minkowski perimeter/isoperimetric facts. DP.2 is an asymptotic expansion consequence. No canonical route map is changed.

---

## 11. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Cyclic endpoint:
  per(F)=q,
  h=q-d_H, 0<=d_H<=2.
DA gives a diameter-direction polygon P_H subset F-F with
  area(P_H) >= D^2[(h-1)sin(delta_D)+sin((h-1)delta_D)],
  delta_D=2asin(1/(2D)).

But
  per(F-F)=2q,
so isoperimetry gives
  area(F-F)<=q^2/pi.
Hence exactly
  D^2[(h-1)sin(delta_D)+sin((h-1)delta_D)] <= q^2/pi.

If h/D->y, then q/D->y and the inequality tends to
  y+sin y <= y^2/pi.
For Phi(y)=pi(y+sin y)-y^2,
  Phi''=-pi sin y-2<0,
  Phi(0)=Phi(pi)=0,
so Phi>0 on (0,pi). Therefore
  q/D -> pi,
  h/D -> pi.

Let t_D=pi D-q. Expanding the exact inequality after first obtaining t_D=o(D):
  t_D <= pi/(12D)+O(D^-2).
If d_H=0, projective-circle packing also gives
  t_D >= pi/(24D)+O(D^-2),
sharp at leading order for regular odd shells.

Direction-gap excess:
  sum_i(g_i-delta_D)=pi-h delta_D=d_H/D+O(D^-2).
Thus F-F is asymptotically disk-like and actual diameter directions asymptotically
uniformly fill the projective circle.

Next: constant-width/equilateral stability or rattler replacement.
```
