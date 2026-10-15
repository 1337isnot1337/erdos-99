<!-- theorem-state: {"artifact_id":"ART-AB49E50DD703","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdos Problem #99 - cyclic Reuleaux and atomic transport for arbitrary mixed surplus

**Date:** 2026-09-11

**Repository base:** `053e1e1b85643b738b4cde306838d150ea325783`

**Run type:** C-II branch extension / removal of the `s_Z=0` restriction from the cyclic geometry and train transport

**Target:** post-ZF Woodall cyclic diameter topology, with arbitrary `s_Z>=0`

## LEVEL I STATUS

`STILL OPEN`.

This report removes a restriction from the September 10 cyclic branch.  The earlier
Reuleaux-cap, rhombus-excess, and atomic-endpoint reports were stated in the exact
circuit phase `s_Z=0`.  Their geometric part in fact survives for every post-ZF
source whose full diameter graph is in Woodall's cyclic topology.  The `s_Z` terms
also cancel exactly in the full-source Oler decomposition.

The resulting all-surplus theorem is:

> **Theorem CX.**  Let an unbounded sequence of lexicographically normalized
> triangle-free C-II survivors have Woodall cyclic diameter topology, so `d_H=0`
> but `s_Z` is arbitrary.  Put
> \[
> \lambda_D={e_{BB}+2s_C\over D},\qquad
> \kappa_D={s_Z\over D},\qquad
> \nu_D={e_{BB}+2s_C-3s_Z\over D}=\lambda_D-3\kappa_D.
> \]
> Then:
> 1. `P_F=pi D-O(sqrt(D))`, `b-P_F=O(sqrt(D))`, and
>    `area(F)/D^2 -> pi/4`;
> 2. the outer-pocket area is `o(D^2)`;
> 3. the total strict-rhombus angular-area excess is `E=O(D)`;
> 4. every subsequential limit satisfies the generalized cyclic cavity/train
>    inequalities in Section 6 below;
> 5. in particular
>    \[
>    \liminf \lambda_D\ge
>    \lambda_A=
>    {\pi\over\sqrt{\pi^2+
>    (5/4-\sqrt{\pi/(2\sqrt3)})^2}}
>    =0.9955405845835427\ldots;
>    \]
> 6. equality at `lambda_A` is impossible even when `s_Z` is not identically zero.
>    Hence there are absolute `epsilon_CX>0` and `D_0` such that every sufficiently
>    large cyclic post-ZF survivor satisfies
>    \[
>    {e_{BB}+2s_C\over D}\ge\lambda_A+\epsilon_{CX}.
>    \]

This is a genuine extension of the September 10 atomic result: it covers the positive
mixed-surplus cyclic branch, including sequences with `s_Z>0` and regular-shell-type
combinatorics.  It still does not give an opposing upper bound on
`(e_BB+2s_C)/D`, so it does not close C-II.

---

## 1. Dependencies and notation

Use the audited post-ZF source and the notation of ZE/ZT/ZU/PC/ZK.  In particular

\[
d_H=q-h,\qquad
s_Z=e+h-(2v-2)\ge0,
\]

and the exact identities are

\[
b+Q=2(h-s_Z),                                           \tag{1.1}
\]

\[
q=x_B+Q+2(d_H+s_Z),                                    \tag{1.2}
\]

\[
e_{BB}=d_P+Q+2(d_H+s_Z)+c_B.                          \tag{1.3}
\]

The ZK attachment-radius identity is

\[
\sum_r\delta_r+R_I+s_B+3(d_H+s_Z)
=6+e_{BB}+2s_C.                                        \tag{1.4}
\]

Assume the Woodall cyclic topology.  Then `d_H=0`, `h=q`, and the full diameter
graph is one odd-unicyclic component with every off-cycle vertex a pendant leaf.
No assumption is made on `s_Z`.

We use the already proved full-source statements FS.3 and FS.4, the C17 Reuleaux
container, the OP/DD pocket decomposition, C51 strict convexity of contact faces, DT/DE,
and the exact global translated-lattice comparison.

---

## 2. Reuleaux perimeter and outer-pocket detour do not use `s_Z=0`

Let `Gamma` be the unique odd cycle of the full diameter graph.  C17 gives the
width-`D` Reuleaux polygon `R_Gamma` determined by that cycle and contains the entire
source in it.

If `theta_i` are the central angles of its circular sides, then

\[
\sum_i\theta_i=\pi.                                    \tag{2.1}
\]

Each `theta_i` is the angle between two actual diameter chords sharing the same cycle
vertex.  FS.3 therefore gives

\[
0<\theta_i\le\Theta_D=O(D^{-1/4}).                    \tag{2.2}
\]

The skeleton perimeter is

\[
2D\sum_i\sin(\theta_i/2).
\]

Using `0<=theta-2sin(theta/2)<=theta^3/24`, inclusion of the cycle skeleton in
`F`, and Cauchy's perimeter-diameter inequality gives exactly

\[
\boxed{
0\le\pi D-P_F
\le {\pi D\over24}\Theta_D^2
=O(\sqrt D).
}                                                       \tag{2.3}
\]

Nothing in this argument refers to `s_Z`.

Woodall also puts every loaded terminal on `partial R_Gamma`: a pendant terminal is at
distance `D` from its cycle neighbor and lies in the same diameter-`D` Reuleaux
container.  Thus the force-hull sides cut the Reuleaux boundary into subarcs of angles
`phi_j`, with

\[
\sum_{j=1}^q\phi_j=\pi,
\qquad
0<\phi_j\le\Theta_D.                                  \tag{2.4}
\]

For a missing force-hull side, OP's convex outer pocket lies inside the corresponding
radius-`D` circular cap.  Perimeter monotonicity gives, exactly as in CRC,

\[
0\le b-P_F
\le {D\over24}\sum_j\phi_j^3
\le {\pi D\over24}\Theta_D^2
=O(\sqrt D).                                           \tag{2.5}
\]

Again no circuit identity is used.

Since (1.1) now reads

\[
b+Q=2(q-s_Z)\le2q,                                    \tag{2.6}
\]

and `q<=P_F<=pi D`, we still have `b,x_B,a=O(D)`.  DD.2 and (2.5) therefore imply

\[
\boxed{H_{out}=o(D^2)}.                                \tag{2.7}
\]

Finally FS.4 plus (2.3), through the promoted maximal-perimeter disk-rigidity argument,
gives

\[
\boxed{{\operatorname{area}F\over D^2}\to{\pi\over4}.} \tag{2.8}
\]

Thus every cyclic post-ZF survivor, not merely a circuit survivor, has disk-limit
force-hull geometry and negligible outer-pocket area.

---

## 3. The full-source Oler cancellation survives `s_Z` exactly

Let `R_4` be the number of bounded quadrilateral contact faces, `f` the number of
bounded exceptional faces, and

\[
Q=\sum_{F\text{ exceptional}}(\deg F-4).
\]

Let `m` be the nonisolated contact-core population.  Euler and face incidence always
give

\[
2m=2R_4+2f+b+Q+2.                                     \tag{3.1}
\]

Using (2.6),

\[
\boxed{m=R_4+f+q-s_Z+1.}                              \tag{3.2}
\]

This is the only place where the old circuit proof used `s_Z=0`; the correction is the
single term `-s_Z`.

Put

\[
a_0={\sqrt3\over2},\qquad c_0={\sqrt3\over4}={a_0\over2}.
\]

C51 makes each quadrilateral face a strict unit rhombus.  Write

\[
A_4=a_0R_4+E,
\qquad E\ge0.                                          \tag{3.3}
\]

If `z_i` is the number of contact-isolated source points inside exceptional face
`F_i`, the same facewise Oler calculation as CRE gives

\[
A_{exc}\ge a_0(Z_{def}+f)+c_0Q.                       \tag{3.4}
\]

From (3.2)--(3.4),

\[
a_0(m+Z_{def})
\le A_{bnd}-E-c_0Q+a_0(q-s_Z)+a_0.                   \tag{3.5}
\]

OP's exact estimate for contact-isolated source points in the outer contact region
inside `F` is unchanged:

\[
a_0Z_{in}\le H+c_0(P_F-b).                           \tag{3.6}
\]

Add (3.5) and (3.6).  The boundary term cancels because

\[
c_0(b+Q)=c_0\,2(q-s_Z)=a_0(q-s_Z).                   \tag{3.7}
\]

Therefore the circuit formula survives **without any error term**:

\[
\boxed{
a_0N_F\le\operatorname{area}F+c_0P_F+a_0-E,
}                                                       \tag{3.8}
\]

where `N_F` is the entire source population in the force hull, including every
contact-isolated source point there.

For the source points in `R_Gamma\setminus F`, apply Oler to each Reuleaux cap together
with its two loaded chord endpoints.  Summing the `q` cap inequalities gives

\[
a_0Z_{ext}
\le\operatorname{area}(R_Gamma)-\operatorname{area}F
+c_0(P_F+\pi D)-a_0q.                                 \tag{3.9}
\]

Add (3.8) and (3.9), subtract `a_0`, and use `a_0=2c_0`:

\[
a_0(n-1)
\le\operatorname{area}(R_Gamma)
+c_0(2P_F+\pi D-2q)-E.                                \tag{3.10}
\]

The strict translated-lattice comparison gives

\[
a_0(n-1)>{\pi D^2\over4}.
\]

With

\[
\delta_R={\pi D^2\over4}-\operatorname{area}(R_Gamma)\ge0,
\]

we obtain the exact all-surplus inequality

\[
\boxed{
E+\delta_R<c_0(2P_F+\pi D-2q).
}                                                       \tag{3.11}
\]

Since `P_F<=pi D` and `q>=0`,

\[
\boxed{E=O(D).}                                        \tag{3.12}
\]

Thus the phase-cut angular-defect budget is boundary order throughout the entire
cyclic topology.  No `s_Z=0` identity was needed after the exact cancellation (3.7).

---

## 4. Generalized cavity variables

Pass to a subsequence on which the normalized quantities below converge.  Write

\[
\lambda={e_{BB}+2s_C\over D},\qquad
\kappa={s_Z\over D},\qquad
\nu=\lambda-3\kappa,                                  \tag{4.1}
\]

\[
\xi={Q\over D},\qquad
\varphi={f\over D},\qquad
w=\xi-\varphi\ge0.                                    \tag{4.2}
\]

ZK says the squared attachment-radius currency is

\[
L_2=6+e_{BB}+2s_C-3s_Z=6+\nu_DD.                     \tag{4.3}
\]

It is nonnegative.  Hence every limit has `nu>=0`, and the attachment-cell area
estimate gives

\[
\limsup {1\over D^2}\sum_r\operatorname{area}(P_r)
\le {\pi\over4}\nu^2.                                \tag{4.4}
\]

By (2.8), the uncovered force-hull cavity therefore satisfies, when `nu<1`,

\[
\liminf {G\over D^2}\ge {\pi\over4}(1-\nu^2).        \tag{4.5}
\]

The refined exceptional-face isoperimetric estimate is purely face-combinatorial and
remains

\[
\limsup {A_{exc}\over D^2}\le {w^2\over4\pi}.        \tag{4.6}
\]

Together with (2.7) and ZG this gives

\[
\boxed{
w\ge\pi\sqrt{1-\nu^2}}
\qquad(0\le\nu<1).                                    \tag{4.7}
\]

The loaded-contact PC identity with `d_H=0` is

\[
e_{BB}=d_P+Q+2s_Z+c_B.                               \tag{4.8}
\]

Hence

\[
\nu_DD=Q-s_Z+d_P+c_B+2s_C,
\]
so in the limit

\[
\boxed{\xi\le\nu+\kappa.}                            \tag{4.9}
\]

This is the precise replacement for the circuit inequality `xi<=nu`.

---

## 5. Train transport also survives arbitrary `s_Z`

By (2.8), (3.12), and (4.6), the quadrilateral faces have density

\[
r:=\lim R_4/D^2
\]
(after extraction) satisfying

\[
\boxed{
r\ge r_{min}(w):={\pi^2-w^2\over2\pi\sqrt3}}
\tag{5.1}
\]

whenever the right side is positive.  In the range relevant to the minimum below this
is strictly positive.

DT gives exactly

\[
T={b+Q\over2}+2f=q-s_Z+2f.                            \tag{5.2}
\]

Equation (2.5) gives `b/D->pi`, so

\[
\tau:=\lim T/D={\pi+\xi\over2}+2\varphi.             \tag{5.3}
\]

In particular the `s_Z` term cancels from the limiting train count.  The hypotheses of
DE hold: `T=O(D)`, (5.1) and Mantel give `T=Omega(D)`, the rhombus area excess is
`o(D^2)` by (3.12), and the scaled force hull tends to the unit-diameter disk.

Let `s` be the total atomic mass of the limiting empirical train-direction measure.
DE's pre-relaxation estimate gives

\[
\boxed{s\tau\ge2\sqrt r.}                             \tag{5.4}
\]

The outer contact-walk direction measure is also unchanged.  Its mass is `b/D->pi`,
and its projection variation is at least twice the force-hull width.  Since the
normalized force hull tends to the disk, the projective cosine-transform argument
forces

\[
{1\over D}\sum_{e\in\partial_{out}C}\delta_{\theta_e}
\Rightarrow d\theta.                                  \tag{5.5}
\]

Thus finitely many shrinking atomic direction windows contain only `o(D)` outer train
end incidences.

Every remaining stopped-train end lies on an exceptional bounded face.  Their exact
capacity is

\[
Q+4f.
\]

The same limiting endpoint count as AE therefore yields

\[
\boxed{2s\tau\le\xi+4\varphi.}                        \tag{5.6}
\]

Combining (5.4)--(5.6) and `xi=w+varphi` gives

\[
4\sqrt r\le w+5\varphi,                               \tag{5.7}
\]

hence

\[
\boxed{
\xi\ge {4\over5}\left(w+\sqrt{r_{min}(w)}\right).
}                                                       \tag{5.8}
\]

No circuit sparsity theorem is used in Sections 3--5.

---

## 6. The all-surplus `lambda_A` floor

We prove that every subsequential limit of the ordinary surplus

\[
\lambda_D={e_{BB}+2s_C\over D}
\]

is at least `lambda_A`.

If `nu>=1`, then `lambda=nu+3kappa>=1>lambda_A`, so assume `nu<1`.
Let

\[
w_0(\nu)=\pi\sqrt{1-\nu^2}.                           \tag{6.1}
\]

For the endpoint range `w<=1`, the function

\[
H(w)=w+\sqrt{r_{min}(w)}
\]

is strictly increasing; this follows from

\[
H'(w)=1-{w\over2\pi\sqrt3\sqrt{r_{min}(w)}}>0.
\tag{6.2}
\]

When `w>=1`, (5.8), (4.9), and `nu<=sqrt(1-1/pi^2)` already give an ordinary-surplus
lower bound much larger than one, so it cannot minimize `lambda`.  Thus at a minimizing
sequence we may use `w>=w_0(nu)` in the increasing range and obtain

\[
\nu+\kappa\ge\xi
\ge F(\nu):={4\over5}
\left(\pi\sqrt{1-\nu^2}+\nu\sqrt\Delta\right),
\qquad
\Delta={\pi\over2\sqrt3}.                             \tag{6.3}
\]

Therefore

\[
\kappa\ge\max\{0,F(\nu)-\nu\},                       \tag{6.4}
\]

and

\[
\lambda=\nu+3\kappa
\ge
\begin{cases}
\nu,&F(\nu)\le\nu,\\
3F(\nu)-2\nu,&F(\nu)>\nu.
\end{cases}                                            \tag{6.5}
\]

The equation `F(nu)=nu` is

\[
\left({5\over4}-\sqrt\Delta\right)\nu
=\pi\sqrt{1-\nu^2}.                                   \tag{6.6}
\]

Its unique solution in `(0,1)` is

\[
\boxed{
\lambda_A={\pi\over
\sqrt{\pi^2+(5/4-\sqrt\Delta)^2}}.
}                                                       \tag{6.7}
\]

For `nu>=lambda_A`, the first line of (6.5) gives `lambda>=nu>=lambda_A`.
For `nu<lambda_A` in the relevant `w_0<=1` interval, `F(nu)>nu` and
`3F(nu)-2nu` is strictly decreasing up to `lambda_A`; hence its minimum there is its
endpoint value `lambda_A`.  The already separated `w>=1` range has a larger bound.
Thus

\[
\boxed{\lambda\ge\lambda_A.}                          \tag{6.8}
\]

Since this holds on every convergent subsequence,

\[
\boxed{
\liminf_{D\to\infty}{e_{BB}+2s_C\over D}\ge\lambda_A.
}                                                       \tag{6.9}
\]

The new point is not the numerical constant itself; it is that no assumption
`s_Z=0` remains.

---

## 7. Equality at `lambda_A` still cannot occur

Assume an unbounded cyclic post-ZF sequence satisfies

\[
\lambda_D\to\lambda_A.                                \tag{7.1}
\]

Every inequality in Section 6 must be sharp.  In particular

\[
\boxed{\kappa_D\to0,\qquad\nu_D\to\lambda_A.}         \tag{7.2}
\]

Also the Section 4--5 chain has the same endpoint profile as the September 10 atomic
report:

\[
\xi\to\lambda_A,
\qquad
w\to\pi\sqrt{1-\lambda_A^2}>0,
\qquad
\varphi\to\lambda_A-w,                                \tag{7.3}
\]

\[
r\to\Delta\lambda_A^2,
\qquad
s\tau=2\sqrt r,
\qquad
2s\tau=\xi+4\varphi.                                  \tag{7.4}
\]

The exact PC identity (4.8) now gives

\[
{d_P+c_B+2s_C\over D}
=\nu-\xi+\kappa\to0.                                  \tag{7.5}
\]

The refined exceptional-face square inequality is also sharp.  Writing
`u_i=deg(F_i)-5>=0`, the same convexity argument as AX gives one exceptional face
`F_*` with

\[
{\operatorname{per}F_*\over D}\to w,
\qquad
{\operatorname{area}F_*\over D^2}\to {w^2\over4\pi}. \tag{7.6}
\]

Hence `F_*/D` converges to a disk and its projective unit-edge direction measure tends
to uniform Lebesgue measure of total mass `w`.

On the train side, equality in DE's Mantel step may again be refined by the three
orbits of `theta -> theta+pi/3`.  Since all quadratic crossing mass lies on angular
separation `pi/3`, equality forces all atomic train mass into one three-point
projective orbit

\[
\{\theta_0,\theta_0+\pi/3,\theta_0+2\pi/3\}.          \tag{7.7}
\]

Equation (7.4), together with (5.5), says atomic train ends exhaust all exceptional-face
incidences up to `o(D)`: outer atomic ends are `o(D)` and the total exceptional
capacity equals `2sT+o(D)`.  Therefore all but `o(D)` boundary edges of the macroscopic
face `F_*` have directions in shrinking neighborhoods of the three points (7.7).
This contradicts the uniform non-atomic edge-direction limit forced by (7.6).

Thus no sequence (7.1) exists.

By the usual compactness contradiction, there are absolute `epsilon_CX>0` and `D_0`
such that every cyclic post-ZF survivor with `D>=D_0` satisfies

\[
\boxed{
{e_{BB}+2s_C\over D}\ge\lambda_A+\epsilon_{CX}.
}                                                       \tag{7.8}
\]

The gap is qualitative; this report does not claim it crosses one.

---

## 8. Regression audit

- **Regular odd shells.**  They have cyclic diameter topology and `s_Z=2`, so they are
  now inside the theorem's scope.  Their ordinary surplus is `e_BB/D~pi`, far above
  the lower endpoint, so there is no contradiction.
- **Sublinear positive `s_Z`.**  This is the main formerly uncovered regime.  The exact
  face cancellation removes it from the cyclic geometric argument; at a `lambda_A`
  endpoint (7.2) shows it is asymptotically invisible, and the endpoint contradiction
  still applies.
- **Linear `s_Z`.**  It is retained.  PC contributes the exact `2s_Z` loaded-contact
  charge while ZK contributes the exact `-3s_Z` attachment-radius charge.  Section 6
  keeps both signs rather than silently setting `s_Z=0`.
- **Contact isolates.**  They are counted in (3.8)--(3.10) and in the Reuleaux caps.
  No population localization is assumed.
- **Exceptional faces and holes.**  DT stops trains at them; no pure-disk train order is
  imported.
- **Outer bridges/repeated walk edges.**  The outer direction measure and pocket
  identities count edge occurrences exactly as in AE/DT.
- **No circuit sparsity import.**  The local `s_r+m_r<=2a_r-4` theorem is not used,
  so there is no hidden `s_Z=0` dependence through circuit extraction.

---

## 9. Exact surviving obstruction

The cyclic positive-mixed-surplus branch is no longer separate at the current
boundary-surplus scale.  Every cyclic survivor lies in one all-surplus normal form:

```text
P_F = pi D-o(D),
area(F) = (pi/4+o(1))D^2,
b-P_F=o(D),
H_out=o(D^2),
E=O(D),
(e_BB+2s_C)/D >= lambda_A+epsilon_CX.
```

What is still missing is an opposing upper tradeoff or a finite global competitor.
In particular, none of the exact ledgers currently proves

\[
e_{BB}+2s_C<D
\]

or any stronger upper bound that conflicts with (7.8).  High loaded-loaded contact
count and high pinned-contact stress surplus remain combinatorially possible.

The next useful cyclic target is therefore not another `s_Z=0` reduction.  It is a
metric/response theorem converting the disk-limit Reuleaux boundary and the
`O(D)` phase defect into an upper restriction on the same ordinary surplus, or directly
into a strict sub-`D` source competitor.

## Audit classification

| Claim | Status |
| --- | --- |
| Reuleaux perimeter and cap detour for arbitrary cyclic `s_Z` | proved |
| disk-limit force hull for arbitrary cyclic `s_Z` | proved from FS.4 + perimeter saturation |
| exact `s_Z` cancellation in full-source Oler decomposition | proved |
| `E=O(D)` for arbitrary cyclic `s_Z` | proved |
| generalized cavity/train inequalities | proved from post-ZF ZK/PC/ZG + DT/DE |
| ordinary surplus `liminf >= lambda_A` for all cyclic topology | proved |
| equality at `lambda_A` impossible for all cyclic topology | proved |
| uniform positive gap above `lambda_A` | proved qualitatively |
| upper bound crossing the lower floor | not proved |
| Level I | still open |
