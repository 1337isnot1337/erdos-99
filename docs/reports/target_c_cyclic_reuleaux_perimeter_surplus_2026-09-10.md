<!-- theorem-state: {"artifact_id":"ART-DF29EF9E5806","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic Reuleaux perimeter saturation and a 0.693 circuit floor

**Date:** 2026-09-10

**Repository base:** `1adc420e9227476135d6891b61f1a75193aa90ab`

**Run type:** C-II closing attempt / exact cyclic-branch reduction

**Target:** post-ZF `s_Z=0`, Woodall cyclic branch `d_H=0`

**External input:** none beyond the already imported C17 Reuleaux-polygon facts and RSJ inequality

## LEVEL I STATUS

`STILL OPEN`.

This report proves a new geometric normal form for the exact circuit phase when the
loaded diameter graph is in Woodall's cyclic case.  C17 traps the entire source in the
Reuleaux polygon determined by the odd diameter cycle.  FS.3 makes every arc angle of
that Reuleaux polygon `O(D^{-1/4})`.  The skeleton perimeter therefore saturates
Cauchy's diameter-perimeter inequality:

\[
\boxed{
0\le \pi D-P_F
\le {\pi D\over24}\Theta_D^2
=O(\sqrt D),
}
\tag{CRP.1}
\]

where `P_F=per(F)` is the actual force-hull perimeter and `Theta_D` is the FS.3
shared-diameter angle bound.  In particular

\[
\boxed{P_F/D\to\pi.}
\tag{CRP.2}
\]

Feeding this forced perimeter into the exact `s_Z=0,d_H=0` SZ/RSJ cavity inequality
raises the cyclic circuit floor from E597's `>0.597` to

\[
\boxed{
\liminf {e_{BB}+2s_C\over D}
\ge
\lambda_C
:={\pi(\sqrt{3\pi^2+4}-1)\over2(\pi^2+1)}
=0.6932725422883145\ldots .
}
\tag{CRP.3}
\]

The endpoint cannot occur.  Hence there are absolute `epsilon_C>0` and `D_0` such
that every sufficiently large cyclic `s_Z=0` survivor satisfies

\[
\boxed{
{e_{BB}+2s_C\over D}\ge\lambda_C+\epsilon_C.
}
\tag{CRP.4}
\]

This does not close the cyclic branch: no upper bound below the right side is proved.
The new content is that the cyclic diameter topology forces the actual response hull
onto the maximal-perimeter/disk end of the RSJ geometry, eliminating the entire
low-surplus portion of that branch.

---

## 1. Hypotheses and dependencies

Assume an unbounded sequence of lexicographically normalized triangle-free global
minimizers satisfying the audited post-ZF hypotheses and

\[
s_Z=0,
\qquad d_H=0.
\tag{1.1}
\]

By WT, the full loaded diameter graph `H` is connected and unicyclic: it contains one
odd cycle `Gamma`, and every vertex outside `Gamma` is a pendant diameter leaf.  Write
`r` for the length of `Gamma`.

The proof uses only the following existing statements.

1. **C17.2.**  The vertices of any odd diameter cycle are exactly the vertices of a
   Reuleaux `r`-gon `R_Gamma` of width `D`; the entire source is contained in that
   Reuleaux polygon.
2. **FS.3.**  If two actual diameter pairs share an endpoint, their angle is at most
   `Theta_D=O(D^{-1/4})`.
3. **SZ.**  In `s_Z=0`, with
   \[
   \nu_D={e_{BB}+2s_C-3d_H\over D},
   \]
   every subsequential limit `(nu,y,p)` satisfies the RSJ cavity inequality
   \[
   A_*(y,p)-{\pi\over4}\nu^2
   \le {\bigl(\nu+m(y,p)\bigr)^2\over4\pi},
   \quad
   m(y,p)=\min\{y,p-y\},
   \tag{1.2}
   \]
   where
   \[
   y=\lim h/D,
   \quad p=\lim P_F/D,
   \quad
   A_*(y,p)=\max\{\Phi(y),\Psi(p)\},
   \tag{1.3}
   \]
   and
   \[
   \Psi(p)={\pi\over(\pi-2)^2}\left({p\over2}-1\right)^2.
   \tag{1.4}
   \]
4. **DD.2 and ZG.**  The outer-pocket area obeys
   \[
   H_{out}\le {1\over\sqrt6}(x_B+a)^{3/2}\sqrt{b-P_F},
   \tag{1.5}
   \]
   while the force-hull uncovered gap satisfies
   \[
   G\le H_{out}+A_{exc}+O(D),
   \tag{1.6}
   \]
   with `A_exc/D^2 <= (Q/D)^2/(4pi)+o(1)` in the asymptotic form used by SZ/E597.

Since `d_H=0`, the SZ currency is simply

\[
\nu_D={e_{BB}+2s_C\over D}.
\tag{1.7}
\]

---

## 2. Reuleaux arc angles are uniformly small

Let the circular sides of `R_Gamma` have central angles

\[
\theta_1,\ldots,\theta_r>0.
\tag{2.1}
\]

Each side has radius `D`.  Its center is one cycle vertex and its two endpoints are the
two diameter-cycle neighbors of that center in the Reuleaux indexing.  Hence each
`theta_i` is the angle between two actual diameter chords sharing one endpoint.  FS.3
therefore gives

\[
\boxed{0<\theta_i\le\Theta_D\quad(1\le i\le r).}
\tag{2.2}
\]

Barbier gives `per(R_Gamma)=pi D`.  Since its boundary is the disjoint union of the
radius-`D` arcs of lengths `D theta_i`,

\[
\boxed{\sum_{i=1}^r\theta_i=\pi.}
\tag{2.3}
\]

No regularity of the Reuleaux polygon is assumed.

---

## 3. The cycle skeleton has almost maximal perimeter

Let

\[
S_\Gamma=\operatorname{conv}V(\Gamma)
\tag{3.1}
\]

be the Reuleaux skeleton.  The chord underlying the arc of angle `theta_i` has length

\[
2D\sin(\theta_i/2),
\]

and these chords are exactly the sides of `S_Gamma`.  Therefore

\[
\operatorname{per}S_\Gamma
=2D\sum_i\sin(\theta_i/2).
\tag{3.2}
\]

For `x>=0`, `sin x>=x-x^3/6`, so

\[
0\le \theta-2\sin(\theta/2)\le {\theta^3\over24}.
\tag{3.3}
\]

Using (2.3),

\[
\begin{aligned}
0\le\pi D-\operatorname{per}S_\Gamma
&=D\sum_i\left(\theta_i-2\sin(\theta_i/2)\right)\\
&\le {D\over24}\sum_i\theta_i^3\\
&\le {D\Theta_D^2\over24}\sum_i\theta_i\\
&={\pi D\over24}\Theta_D^2.
\end{aligned}
\tag{3.4}
\]

C17 puts the cycle vertices among the loaded force-hull terminals, so
`S_Gamma subset F`.  Perimeter is monotone under inclusion for planar convex bodies.
Cauchy's perimeter-diameter inequality gives `P_F<=pi D`.  Hence

\[
0\le\pi D-P_F
\le\pi D-\operatorname{per}S_\Gamma
\le {\pi D\over24}\Theta_D^2.
\tag{3.5}
\]

FS.3 has `Theta_D=O(D^{-1/4})`, proving CRP.1--CRP.2.

### Scope check

The pendant diameter leaves from WT are irrelevant to this estimate.  The unique odd
cycle alone already supplies the near-maximal skeleton.  No claim is made that the
cycle is regular, that `H` is a bare cycle, or that the full source equals the Reuleaux
skeleton.

---

## 4. The cyclic circuit branch has a 0.693272... surplus floor

Take any subsequence along which

\[
\nu_D\to\nu,
\qquad y_D:=h/D\to y.
\tag{4.1}
\]

By CRP.2,

\[
p=P_F/D\to\pi.
\tag{4.2}
\]

Because `d_H=0`, `h=q`.  The force hull has `q` unit-separated convex vertices, so
`q<=P_F`; hence

\[
y\le\pi.
\tag{4.3}
\]

SZ also gives `P_F<=2h` in this phase, so

\[
y\ge\pi/2.
\tag{4.4}
\]

Therefore

\[
m(y,\pi)=\min\{y,\pi-y\}=\pi-y\le\pi/2.
\tag{4.5}
\]

The RSJ symmetric area term becomes exactly

\[
\Psi(\pi)
={\pi\over(\pi-2)^2}\left({\pi\over2}-1\right)^2
={\pi\over4}.
\tag{4.6}
\]

Thus the SZ necessary inequality (1.2) implies

\[
{\pi\over4}-{\pi\over4}\nu^2
\le {\left(\nu+m(y,\pi)\right)^2\over4\pi}
\le {\left(\nu+\pi/2\right)^2\over4\pi}.
\tag{4.7}
\]

Equivalently,

\[
(\pi^2+1)\nu^2+\pi\nu-{3\pi^2\over4}\ge0.
\tag{4.8}
\]

The left side is strictly increasing for `nu>=0`.  Its unique positive root is

\[
\boxed{
\lambda_C
={\pi(\sqrt{3\pi^2+4}-1)\over2(\pi^2+1)}.
}
\tag{4.9}
\]

Hence `nu>=lambda_C` on every convergent subsequence, which proves CRP.3.

The displayed decimal is diagnostic only; the proof uses the exact root (4.9).

---

## 5. The endpoint is impossible

Assume for contradiction that an unbounded cyclic circuit sequence satisfies

\[
\nu_D\to\lambda_C.
\tag{5.1}
\]

Every relaxation in (4.7) must then be asymptotically sharp.  Since the threshold is
strictly decreasing in the available cavity parameter `m`, (4.5) forces

\[
\boxed{y=h/D=q/D\to\pi/2.}
\tag{5.2}
\]

The exact circuit perimeter identity is

\[
b+Q=2h.
\tag{5.3}
\]

By CRP.2, `P_F/D->pi`, while `b>=P_F`.  Combining with (5.2)--(5.3) gives

\[
\boxed{
{b\over D}\to\pi,
\qquad {Q\over D}\to0,
\qquad {b-P_F\over D}\to0.
}
\tag{5.4}
\]

Also `x_B=b-q=O(D)` and `a<=q=O(D)`.  DD.2 therefore gives

\[
\boxed{H_{out}=o(D^2).}
\tag{5.5}
\]

The exceptional-face isoperimetric estimate and `Q=o(D)` give

\[
\boxed{A_{exc}=o(D^2).}
\tag{5.6}
\]

ZG now yields

\[
\boxed{G=o(D^2).}
\tag{5.7}
\]

On the other hand, (4.6) and the RSJ transfer give

\[
\operatorname{area}F=(\pi/4-o(1))D^2.
\tag{5.8}
\]

The exact ZK/SZ attachment estimate, with `d_H=0`, gives

\[
\limsup {1\over D^2}\sum_r\operatorname{area}(P_r)
\le {\pi\over4}\lambda_C^2.
\tag{5.9}
\]

Since `lambda_C<1`, the definition

\[
G=\operatorname{area}F-\sum_r\operatorname{area}(P_r)
\]
therefore gives the fixed lower bound

\[
\liminf {G\over D^2}
\ge {\pi\over4}(1-\lambda_C^2)>0,
\tag{5.10}
\]

contradicting (5.7).

Thus the endpoint (5.1) is impossible.

If no uniform positive gap in CRP.4 existed, one could choose a sequence with
`D_j->infinity` and `nu_{D_j}<lambda_C+1/j`; CRP.3 would then force
`nu_{D_j}->lambda_C`, contradicting the endpoint exclusion.  This proves CRP.4.

---

## 6. Regression audit

### Regular odd shell

The shell remains a valid FS/C17 geometric regression.  Its diameter graph is cyclic,
but the regular shell has `s_Z=2`, not `s_Z=0`, so CRP.3--CRP.4 do not apply.  CRP.1
is compatible with it: its Reuleaux/skeleton angles are `pi/r` and its perimeter tends
to `pi D`.

### Pendant leaves

WT permits pendant diameter leaves on the odd cycle.  CRP.1 uses only the cycle
skeleton, so leaves neither need to be discarded nor assumed absent.

### Contact-isolated source points

C17 traps the entire source, including contact-isolated points, in `R_Gamma`.  The
perimeter proof uses only actual cycle vertices, so no small-isolate hypothesis is
introduced.

### Operator-response caution

No operator norm or conductance lower bound is inferred from FS.4.  The only response
input after the geometric perimeter theorem is the already audited scalar SZ/RSJ
cavity inequality.

---

## 7. Exact remaining branch

CRP does not prove an upper bound on `e_BB+2s_C`, so the cyclic circuit branch remains
possible only in the high-surplus regime

\[
{e_{BB}+2s_C\over D}\ge\lambda_C+\epsilon_C.
\]

The Woodall forest branch remains separate and still carries the E597 component charge
`3d_H/D`.

A useful next theorem must therefore do one of the following:

1. bound the cyclic high-surplus currency from above using its single contact hub block,
   outer-pocket geometry, or circuit sparsity; or
2. in the caterpillar-forest branch, sum the CS/RR diameter-bypass requirement over
   components without reusing one contact attachment currency arbitrarily many times.

Neither statement is asserted here.

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

In WT-C (`s_Z=0,d_H=0`), let Gamma be the unique odd diameter cycle.
C17 gives a Reuleaux polygon R_Gamma of width D with skeleton S_Gamma=conv Gamma.
If theta_i are its arc angles, then
    sum theta_i=pi,
and FS.3 gives
    max theta_i<=Theta_D=O(D^-1/4).
Therefore
    per(S_Gamma)=2D sum sin(theta_i/2),
    0<=pi D-per(S_Gamma)
      <=(D/24)sum theta_i^3
      <=(pi D/24)Theta_D^2
      =O(sqrt D).
Since S_Gamma subset F and per(F)<=pi D,
    per(F)/D -> pi.

In the s_Z=0,d_H=0 SZ/RSJ inequality this forces Psi(p)->pi/4 and
m<=pi/2. Hence
    (pi^2+1)nu^2+pi nu-3pi^2/4 >=0,
so
    nu=(e_BB+2s_C)/D
       >= lambda_C
       =pi(sqrt(3pi^2+4)-1)/(2(pi^2+1))
       =0.693272542288... .

Endpoint equality forces h/D=q/D->pi/2. Then b+Q=2h together with
per(F)/D->pi gives
    Q=o(D), b-per(F)=o(D).
DD gives H_out=o(D^2), exceptional-face area is o(D^2), and ZG gives G=o(D^2).
But area(F)->pi D^2/4 while attachment cells carry at most
(pi/4)lambda_C^2 D^2, so
    G/D^2 >= (pi/4)(1-lambda_C^2)+o(1)>0,
a contradiction. Thus there is a uniform positive gap above lambda_C.

Next: cyclic high-surplus upper bound or WT-F caterpillar component/bypass summation.
```
