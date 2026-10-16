<!-- theorem-state: {"artifact_id":"ART-AE704DD03CD5","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_fs_quantitative_perimeter_area_tradeoff_2026-09-10.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=3b2f812139b1eae8f59a10637bec916e7c563cfa; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — quantitative FS perimeter/area tradeoff

**Date:** 2026-09-10  
**Repository state:** `f977f2d0d25f5022c2a587e59cab38375d85caee` at start  
**Run type:** convex-geometric stability / post-FD quantitative refinement  
**Target:** Target C, C-II after ZF  
**External input:** none  
**Computation:** none in the theorem

## LEVEL I STATUS

`STILL OPEN`.

The FD theorem proves qualitatively that a post-ZF force hull whose normalized
perimeter tends to `pi` has normalized area tending to `pi/4`.  This report makes the
perimeter-to-area implication explicit at every perimeter scale.

Let

\[
f(a):=2\left(\arcsin a+\sqrt{1-a^2}\right),\qquad 0\le a\le1.
\tag{QPA.1}
\]

Then `f` increases continuously from `2` to `pi`.  Let

\[
\alpha:[2,\pi]\to[0,1]
\]

be its inverse and define

\[
\boxed{
\Psi(p):=\frac\pi4\alpha(p)^2.
}
\tag{QPA.2}
\]

For the actual force hull `F`, put `P=per(F)`.  With the FS.4 error

\[
\eta=3^{1/4}\sqrt D,
\qquad
L_D=\sqrt{D\eta+\eta^2},
\tag{QPA.3}
\]

one has the finite estimate

\[
\boxed{
\operatorname{area}F
\ge
\frac{\pi D^2}{4}\,
\alpha\!\left(\frac PD\right)^2
-L_DP-\pi L_D^2.
}
\tag{QPA.4}
\]

Consequently, along every unbounded post-ZF sequence on which

\[
\frac{P}{D}\to p,
\]

\[
\boxed{
\liminf\frac{\operatorname{area}F}{D^2}\ge\Psi(p).
}
\tag{QPA.5}
\]

This is useful precisely where the qualitative FD theorem was not: it gives an
explicit area gain before `P/D` reaches `pi`.

---

## 1. Central symmetral reduction

Translate by the full-source circumcenter `o` from FS.4 and write

\[
F_0:=F-o,
\qquad
S:=\frac12(F_0-F_0).
\tag{1.1}
\]

FD already proves the exact identities

\[
\operatorname{diam}S=D,
\qquad
\operatorname{per}S=P,
\tag{1.2}
\]

and the finite area comparison

\[
0\le
\operatorname{area}S-\operatorname{area}F
\le L_DP+\pi L_D^2.
\tag{1.3}
\]

Thus it remains only to lower-bound the area of a centrally symmetric
`diameter-D` convex body from its perimeter.

The point of using `S` rather than `F` directly is essential.  Without central
symmetry, perimeter close to `pi D` permits noncircular constant-width bodies.  For
`S`, central symmetry fixes the circumcenter and converts a support deficit into a
symmetric strip constraint.

---

## 2. A sharp strip envelope for the centered inradius

Let `K` be any compact centrally symmetric convex body with center `0` and diameter
`D`.  Put

\[
R:=D/2.
\]

Central symmetry immediately gives

\[
K\subseteq \overline B(0,R),
\tag{2.1}
\]

because `x,-x in K` implies `2|x|<=D`.

Let

\[
r:=\min_{|u|=1}h_K(u),
\tag{2.2}
\]

where `h_K` is the support function.  Since `K` is centrally symmetric,
`h_K(-u)=h_K(u)`.  If `u_0` realizes the minimum, then

\[
K\subseteq\{x:|x\cdot u_0|\le r\}.
\tag{2.3}
\]

Also `h_K(u)>=r` in every direction, so

\[
\overline B(0,r)\subseteq K.
\tag{2.4}
\]

Therefore

\[
K\subseteq
T_{R,r}:=
\overline B(0,R)\cap\{x:|x\cdot u_0|\le r\}.
\tag{2.5}
\]

Planar convex perimeter is monotone under inclusion, hence

\[
\operatorname{per}K\le\operatorname{per}T_{R,r}.
\tag{2.6}
\]

Write

\[
a:=r/R\in[0,1].
\tag{2.7}
\]

The boundary of `T_{R,r}` consists of two chords of length
`2R sqrt(1-a^2)` and two circular arcs whose total angle is `4 arcsin a`.
Thus

\[
\begin{aligned}
\operatorname{per}T_{R,r}
&=4R\sqrt{1-a^2}+4R\arcsin a\\
&=2D\left(\arcsin a+\sqrt{1-a^2}\right)\\
&=Df(a).
\end{aligned}
\tag{2.8}
\]

Hence

\[
\boxed{
\frac{\operatorname{per}K}{D}\le f(a).
}
\tag{2.9}
\]

The derivative is

\[
f'(a)
=2\frac{1-a}{\sqrt{1-a^2}}>0
\qquad(0\le a<1),
\tag{2.10}
\]

so `f` is strictly increasing on `[0,1]`, with

\[
f(0)=2,
\qquad
f(1)=\pi.
\tag{2.11}
\]

If

\[
p:=\frac{\operatorname{per}K}{D},
\]

then (2.9) gives

\[
a\ge\alpha(p).
\tag{2.12}
\]

Finally (2.4) yields

\[
\operatorname{area}K
\ge\pi r^2
=\frac{\pi D^2}{4}a^2
\ge\frac{\pi D^2}{4}\alpha(p)^2.
\tag{2.13}
\]

We record this independently.

### Lemma QPA — centrally symmetric perimeter/area tradeoff

Every centrally symmetric planar convex body `K` of diameter `D` and perimeter `P`
satisfies

\[
\boxed{
\operatorname{area}K
\ge
\frac{\pi D^2}{4}
\alpha\!\left(\frac PD\right)^2.
}
\tag{2.14}
\]

The lemma is deliberately one-sided.  It is not claimed to be the globally sharp
minimum-area body at fixed `(D,P)`.  The proof only needs the sharp **perimeter
envelope at fixed centered inradius**, supplied by the containing disk intersected
with the minimizing support strip.

---

## 3. Transfer back to the actual force hull

Apply Lemma QPA to the central symmetral `S`.  Equations (1.2) and (2.14) give

\[
\operatorname{area}S
\ge
\frac{\pi D^2}{4}
\alpha\!\left(\frac PD\right)^2.
\tag{3.1}
\]

Subtract the FS.4/FD area error (1.3):

\[
\operatorname{area}F
\ge
\frac{\pi D^2}{4}
\alpha\!\left(\frac PD\right)^2
-L_DP-\pi L_D^2.
\]

This is QPA.4.

Since `P<=pi D` and `L_D=O(D^{3/4})`, the error is

\[
L_DP+\pi L_D^2=O(D^{7/4})=o(D^2).
\tag{3.2}
\]

If `P/D->p`, continuity of `alpha` gives QPA.5.

At the maximal endpoint `p=pi`, `alpha(pi)=1`, so QPA.5 recovers FD's area conclusion

\[
\operatorname{area}F/D^2\to\pi/4
\]

whenever `P/D->pi`; the matching upper bound is isodiametricity.

---

## 4. Coupling to the existing DB and JC variables

For later optimization define

\[
y:=\lim\frac hD,
\qquad
p:=\lim\frac{\operatorname{per}F}{D},
\qquad
\lambda:=\lim\frac{e_{BB}+2s_C}{D}.
\tag{4.1}
\]

DB.3.3 gives, after division by `D`,

\[
\boxed{
p\ge g(y):=y+2\cos(y/2),
\qquad
2\rho\le y\le\pi.
}
\tag{4.2}
\]

The FSDB area theorem gives independently

\[
\boxed{
\liminf\frac{\operatorname{area}F}{D^2}
\ge
\Phi(y):=\frac{y+\sin y}{4}.
}
\tag{4.3}
\]

Combining (4.3) with QPA.5 therefore yields

\[
\boxed{
\liminf\frac{\operatorname{area}F}{D^2}
\ge
A(y,p):=\max\{\Phi(y),\Psi(p)\}.
}
\tag{4.4}
\]

The actual-perimeter version of JC retained in FD gives the necessary cavity
inequality

\[
\boxed{
A(y,p)-\frac\pi4\lambda^2
\le
\frac{\left(\lambda+\min\{y,p-y\}\right)^2}{4\pi},
}
\tag{4.5}
\]

where replacing `t=e_BB/D` by `lambda` is again the only pinned/contact relaxation in
the final scalar step.  Feasibility also retains

\[
2\rho\le y\le\pi,
\qquad
g(y)\le p\le\pi.
\tag{4.6}
\]

Equations (4.4)--(4.6) are a new explicit two-parameter feasible-region system.  They
strictly strengthen FSJC near its old endpoint because `Psi(p)` rises to `pi/4` as
`p->pi`, while reducing `p` shrinks the complementary JC perimeter budget `p-y`.

---

## 5. Audit and edge cases

### Degenerate lower endpoint

For any planar convex body of diameter `D`, Cauchy's width formula gives
`per(K)>=2D` in the degenerate limit.  Thus `P/D in [2,pi]`, the full domain of
`alpha`.  Post-ZF DB is much stronger: (4.2) and `y>=2rho` imply

\[
p\ge4\rho=2.9563405328\ldots .
\]

### Equality geometry in the strip envelope

No equality classification for QPA.14 is used downstream.  Equality in the perimeter
envelope (2.9) would require `K=T_{R,r}` up to perimeter-null degeneracy, while equality
in the area step (2.13) would require `K` to be the centered disk of radius `r`; these
conditions coincide only at `a=1`.  Therefore QPA is expected to be nonsharp away from
`p=pi`, which is harmless for a lower bound.

### Regular odd shell

Its normalized force hull approaches the radius-`1/2` disk, so `p->pi`,
`Psi(p)->pi/4`, and the theorem is asymptotically tight there.  It is not falsely
excluded by QPA alone.

### Isolates

The transfer from `F` to `S` uses FS.4, whose common circumcenter comes from the full
source hull.  No estimate on the number of contact-isolated source points is inserted.

---

## 6. What this changes

FD gave only the endpoint statement

```text
p -> pi  =>  area(F)/D^2 -> pi/4.
```

QPA supplies the quantitative continuum

```text
p in [2,pi]  =>  area(F)/D^2 >= Psi(p)-o(1).
```

Together with FSDB and the actual-perimeter JC bound, the post-ZF scalar frontier is
now the explicit compact optimization problem (4.4)--(4.6), rather than the old FSJC
one-variable relaxation with `p` discarded.

No numerical improvement is claimed in this first report.  The next step is to solve
that compact optimization rigorously and, if it beats `lambda_FSJC`, record the new
explicit pinned/contact floor separately so the geometric theorem and the numerical
certificate remain auditable in isolation.

---

## 7. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| central symmetral has diameter `D`, perimeter `P` | already proved in FD | exact difference-body identities |
| `S subset B(0,D/2)` | proved | central symmetry plus diameter |
| strip envelope `P/D<=f(2r/D)` | proved | support strip + disk containment + perimeter monotonicity |
| QPA finite force-hull area bound | proved | strip envelope + centered inball + FD area transfer |
| two-parameter lower area `max{Phi(y),Psi(p)}` | proved asymptotically | FSDB + QPA |
| actual-perimeter JC system (4.5) | already proved/used in FD | JC equality chain before `P<=pi D` relaxation |
| improved explicit `lambda` constant | not yet claimed | requires global optimization of (4.4)--(4.6) |
| Level I | still open | no structural upper contradiction yet |

---

## 8. Next run

Solve the compact feasible-region optimization (4.4)--(4.6).  The likely minimizer is
on the transition where the FSDB direction-area floor and the QPA perimeter-area floor
are equal; this must be proved rather than inferred from floating-point exploration.
A useful outcome is either an exact implicit characterization of the new minimum with
a certified rational lower bound, or a structural branch split strong enough to avoid
numerical optimization entirely.
