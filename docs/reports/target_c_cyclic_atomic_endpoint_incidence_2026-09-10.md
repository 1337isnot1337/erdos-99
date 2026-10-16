<!-- theorem-state: {"artifact_id":"ART-5CB4456266E2","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic outer-direction equidistribution and atomic train endpoint capacity

**Date:** 2026-09-10

**Repository base:** `1adc420e9227476135d6891b61f1a75193aa90ab` plus the three cyclic reports on this branch

**Run type:** C-II closing attempt / stopped-train measure transport / branch contraction

**Target:** post-ZF `s_Z=0`, Woodall cyclic branch `d_H=0`

## LEVEL I STATUS

`STILL OPEN`.

The cyclic cap theorem proves

\[
P_F/D\to\pi,
\qquad
(b-P_F)/D\to0,
\tag{AE.1}
\]

where `b` is the unit-edge outer contact-walk length.  This forces the projective
direction measure of the **outer contact walk** itself to converge to uniform
Lebesgue measure.  In particular, finitely many shrinking direction windows contain
only `o(D)` outer train-end incidences.

The DE stopped-train proof independently shows that a positive fraction of all trains
must lie in atoms of the limiting **train-direction** measure whenever the rhombus
area is quadratic.  Those atomic trains cannot end on the asymptotically uniform outer
walk at linear scale.  Their two endpoints therefore consume exceptional-face
incidences.

Combining this endpoint capacity with the cyclic exceptional-face area budget gives

\[
\boxed{
\liminf_{D\to\infty}{e_{BB}+2s_C\over D}
\ge
\lambda_A,
}
\tag{AE.2}
\]

where

\[
\boxed{
\lambda_A
=
{\pi\over
\sqrt{\pi^2+\left(\frac54-\sqrt{\frac{\pi}{2\sqrt3}}\right)^2}}
=0.9955405845835427\ldots .
}
\tag{AE.3}
\]

The decimal is diagnostic only.  This strictly strengthens the previous cyclic floor
`pi/sqrt(pi^2+1)=0.9528905...`.

At the formal equality endpoint, every inequality below is sharp.  In particular all
quadratic rhombi lie asymptotically on atomic train directions, the atomic crossing
graph is asymptotically Mantel-extremal, and essentially every exceptional-face
boundary incidence belongs to an atomic train.  Section 9 records this as the next
rigidity target; no endpoint exclusion is claimed in this report.

---

## 1. Outer contact-walk direction measure

Let `gamma_D` be the closed outer-face boundary walk of the positive contact core,
with every bridge occurrence counted separately.  Every traversed edge has length one,
so

\[
\operatorname{len}(\gamma_D)=b.
\]

Its image has convex hull exactly `F`.  Define a finite measure on the projective
direction circle `T=R/pi Z` by

\[
\boxed{
\mu_D^{out}:={1\over D}\sum_{e\in\gamma_D}\delta_{\theta_e},
}
\tag{1.1}
\]

where the sum is over edge **occurrences** in the walk and `theta_e` is the unoriented
edge direction.  Thus

\[
\mu_D^{out}(T)=b/D\to\pi
\tag{1.2}
\]

by AE.1.

For a unit vector direction `alpha`, the total variation of the scalar projection of
the closed walk is

\[
V_D(\alpha)
:=\int_T|\cos(\theta-\alpha)|\,d\mu_D^{out}(\theta).
\tag{1.3}
\]

A closed real-valued walk whose range has width `w` has total variation at least
`2w`.  Hence

\[
\boxed{
V_D(\alpha)\ge {2w_F(\alpha)\over D}.
}
\tag{1.4}
\]

The cyclic force hull has diameter `D`, perimeter `pi D-o(D)`, and by the FD/RSJ
compactness argument its normalized translates converge to the disk of diameter one.
Consequently

\[
{w_F(\alpha)\over D}\to1
\tag{1.5}
\]

uniformly in `alpha`.

---

## 2. Equality in the integrated projection inequality forces uniform directions

Take any weakly convergent subsequence

\[
\mu_D^{out}\Rightarrow\mu.
\tag{2.1}
\]

The kernel `|cos(theta-alpha)|` is continuous, so (1.4)--(1.5) give

\[
\int_T|\cos(\theta-\alpha)|\,d\mu(\theta)\ge2
\qquad(\alpha\in T).
\tag{2.2}
\]

On the other hand, Fubini and

\[
\int_0^\pi|\cos t|\,dt=2
\]

give

\[
\int_0^\pi
\int_T|\cos(\theta-\alpha)|\,d\mu(\theta)\,d\alpha
=2\mu(T)=2\pi.
\tag{2.3}
\]

The continuous integrand in (2.2) is everywhere at least two and has integral
`2pi`; hence it is identically two:

\[
\boxed{
\int_T|\cos(\theta-\alpha)|\,d\mu(\theta)=2
\quad\forall\alpha.
}
\tag{2.4}
\]

The projective cosine transform is injective on finite measures.  For completeness,
write the Fourier series

\[
|\cos t|
={2\over\pi}
+{4\over\pi}\sum_{n\ge1}
{(-1)^n\over1-4n^2}\cos(2nt).
\tag{2.5}
\]

Every nonconstant Fourier coefficient is nonzero.  Equation (2.4) therefore forces
every nonzero projective Fourier coefficient of `mu` to vanish.  Since `mu(T)=pi`,

\[
\boxed{d\mu(\theta)=d\theta.}
\tag{2.6}
\]

Every subsequential limit is the same, so the whole sequence converges:

\[
\boxed{\mu_D^{out}\Rightarrow d\theta.}
\tag{2.7}
\]

### Consequence AE.1 — finite shrinking direction windows contain `o(D)` outer ends

Let `theta_1,...,theta_k` be fixed projective directions.  For any `epsilon>0`, choose
disjoint arcs `U_i` around them with total Lebesgue length below `epsilon` and
boundaries avoiding all limiting atoms under discussion.  By (2.7),

\[
\limsup {1\over D}
\#\{\text{outer-walk edge occurrences with direction in }U=\cup U_i\}
\le |U|<\epsilon.
\tag{2.8}
\]

Letting the arcs shrink proves that any finite set of asymptotically fixed train
directions carries only `o(D)` outer train-end incidences.

The use of edge occurrences handles contact bridges correctly: a bridge appearing
twice in the outer walk contributes two possible outer train-end incidences.

---

## 3. Refined exceptional-face area with the face count retained

Let the bounded exceptional faces have

\[
r_i:=\deg(F_i)-4\ge1,
\qquad
\sum_{i=1}^f r_i=Q.
\tag{3.1}
\]

The CC estimate starts from

\[
A_{exc}
\le {1\over4\pi}\sum_i(r_i+4)^2.
\tag{3.2}
\]

For fixed integers `Q>=f>=1`, convexity of the square shows that the largest possible
`sum r_i^2` occurs at

\[
(Q-f+1,1,\ldots,1).
\]
Therefore

\[
\boxed{
\sum_i r_i^2\le(Q-f+1)^2+(f-1).
}
\tag{3.3}
\]

Since `Q,f=O(D)` in the cyclic branch, along a convergent subsequence put

\[
\xi:=\lim Q/D,
\qquad
\varphi:=\lim f/D,
\qquad
w:=\xi-\varphi\ge0.
\tag{3.4}
\]

Equations (3.2)--(3.3) give the sharper asymptotic capacity

\[
\boxed{
\limsup {A_{exc}\over D^2}
\le {w^2\over4\pi}.
}
\tag{3.5}
\]

The previous cyclic report corresponds to discarding `f` and replacing `w` by `xi`.

---

## 4. Cavity area forces `w` away from zero

Pass to a subsequence on which

\[
\nu:=\lim {e_{BB}+2s_C\over D}
\tag{4.1}
\]

exists.  If `nu>=1`, AE.2 is automatic, so assume `nu<1`.

The cyclic cap theorem gives

\[
H_{out}=o(D^2),
\qquad
{\operatorname{area}F\over D^2}\to{\pi\over4}.
\tag{4.2}
\]

The exact ZK/SZ attachment-cell estimate gives

\[
\limsup {1\over D^2}\sum_r\operatorname{area}(P_r)
\le {\pi\over4}\nu^2.
\tag{4.3}
\]

Hence

\[
\liminf {G\over D^2}
\ge {\pi\over4}(1-\nu^2).
\tag{4.4}
\]

ZG, (4.2), and (3.5) imply

\[
{\pi\over4}(1-\nu^2)
\le {w^2\over4\pi}.
\]
Thus

\[
\boxed{
w\ge w_0(\nu):=\pi\sqrt{1-\nu^2}.}
\tag{4.5}
\]

Also `0<=varphi<=xi<=nu` because `f<=Q<=e_BB<=e_BB+2s_C`.  In particular

\[
0\le w\le\nu<1.
\tag{4.6}
\]

---

## 5. Rhombus area lower bound

Let `R` be the number of bounded quadrilateral contact faces.  Their total area is

\[
A_4=a_0R+E,
\qquad a_0={\sqrt3\over2},
\tag{5.1}
\]

and CRE proves `E=O(D)`.

The force hull decomposes, up to boundaries, as

\[
F=A_4\sqcup A_{exc}\sqcup H_{out}.
\tag{5.2}
\]

Using (4.2), (3.5), and CRE,

\[
\liminf {R\over D^2}
\ge
r_{min}(w)
:={\pi^2-w^2\over4\pi a_0}
={\pi^2-w^2\over2\pi\sqrt3}.
\tag{5.3}
\]

Pass further so `R/D^2->r`; then

\[
\boxed{r\ge r_{min}(w)>0.}
\tag{5.4}
\]

---

## 6. DT/DE applies to the actual cyclic contact core

DT gives exactly

\[
T={b+Q\over2}+2f.
\tag{6.1}
\]

In the cyclic circuit branch `b+Q=2q`, so

\[
\boxed{T=q+2f.}
\tag{6.2}
\]

The cap theorem gives `b-P_F=o(D)` and `P_F/D->pi`; since `b+Q=2q`,

\[
\boxed{{q\over D}\to\gamma:={\pi+\xi\over2}.}
\tag{6.3}
\]

Consequently

\[
\boxed{\tau:=\lim T/D=\gamma+2\varphi.}
\tag{6.4}
\]

The hypotheses of DE hold:

- `T=O(D)` by (6.2) and `f<=Q<=q=O(D)`;
- `T=Omega(D)` because `R<=T^2/4` and (5.4) has `r>0`;
- `R/D^2->r>0` by extraction;
- CRE gives total rhombus area excess `E=O(D)=o(D^2)`;
- the normalized force hull tends to the unit-diameter disk.

Let `mu_train` be the weak limit of the empirical probability measures on projective
train directions, and let `s` be its total atomic mass.  The proof of DE establishes
before its final perimeter relaxation

\[
\boxed{{r\over\tau^2}\le {s^2\over4}.}
\tag{6.5}
\]

Thus

\[
\boxed{s\tau\ge2\sqrt r.}
\tag{6.6}
\]

---

## 7. Atomic trains must terminate on exceptional faces

Fix `epsilon>0`.  Choose finitely many atoms of `mu_train` carrying atomic mass at
least `s-epsilon`.  Choose pairwise disjoint small projective arcs `U` around them,
with boundaries of zero `mu_train` mass.  For fixed `U`, weak convergence gives

\[
\#\{\text{trains with direction in }U\}
\ge(s-2\epsilon)T
\tag{7.1}
\]

for all sufficiently large members of the subsequence after making the arcs small
enough that their non-atomic train mass is below `epsilon`.

Each stopped train has two endpoint incidences.  DT's endpoint count is exact:
outer-face endpoint incidences are the `b` outer-walk edge occurrences, while bounded
exceptional faces supply

\[
\sum_i\deg(F_i)=Q+4f
\tag{7.2}
\]

endpoint incidences.  This includes singleton trains and bridges with multiplicity in
the same way as DT's identity `2T=b+Q+4f`.

By AE.1, after the train limit is taken and then the arcs `U` are shrunk, only `o(D)`
outer endpoint incidences can have direction in `U`.  Therefore the atomic train ends
must satisfy

\[
2(s-2\epsilon)T
\le Q+4f+o_U(D).
\tag{7.3}
\]

Divide by `D`, pass to the limit, shrink `U`, and then let `epsilon->0`:

\[
\boxed{2s\tau\le\xi+4\varphi.}
\tag{7.4}
\]

Combining with (6.6),

\[
\boxed{4\sqrt r\le\xi+4\varphi.}
\tag{7.5}
\]

This is the new endpoint-capacity inequality.  It is not a generic train-count bound:
it uses the global-optimum cyclic geometry through outer-walk equidistribution.

---

## 8. Eliminate the train variables

Recall `xi=w+varphi`.  From (7.5) and (5.4),

\[
w+5\varphi
\ge4\sqrt{r_{min}(w)},
\]
so

\[
\boxed{
\varphi\ge {4\sqrt{r_{min}(w)}-w\over5}.
}
\tag{8.1}
\]

Since `nu>=xi=w+varphi`,

\[
\boxed{
\nu\ge {4\over5}\left(w+\sqrt{r_{min}(w)}\right).
}
\tag{8.2}
\]

On `0<=w<=1`, the function

\[
H(w):=w+\sqrt{r_{min}(w)}
\]

is strictly increasing.  Indeed

\[
H'(w)
=1-{w\over2\pi\sqrt3\sqrt{r_{min}(w)}}>0,
\tag{8.3}
\]

where the final inequality is immediate from `w<=1` and
`r_min(w)> (pi^2-1)/(2pi sqrt3)>1/2`.

By (4.5), (8.2) is weakest at `w=w_0(nu)`.  At that value,

\[
r_{min}(w_0)
={\pi\nu^2\over2\sqrt3}
=\Delta\nu^2,
\qquad
\Delta:={\pi\over2\sqrt3}.
\tag{8.4}
\]

Therefore every `nu<1` survivor limit satisfies

\[
\nu
\ge{4\over5}
\left(\pi\sqrt{1-\nu^2}+\nu\sqrt\Delta\right).
\tag{8.5}
\]

Put

\[
B:={5\over4}-\sqrt\Delta>0.
\tag{8.6}
\]

Then

\[
B\nu\ge\pi\sqrt{1-\nu^2}.
\tag{8.7}
\]

Both sides are nonnegative.  Squaring and rearranging gives

\[
\nu^2\ge{\pi^2\over\pi^2+B^2}.
\]
Thus

\[
\boxed{
\nu\ge
{\pi\over\sqrt{\pi^2+B^2}}
=\lambda_A,
}
\tag{8.8}
\]

which proves AE.2--AE.3.

---

## 9. Formal equality profile and next obstruction

If a sequence approached `lambda_A`, every relaxation used above would be sharp.
Writing `nu=lambda_A`, its limiting currencies would satisfy

\[
\boxed{
w=\pi\sqrt{1-\nu^2},
\qquad
\varphi=\nu-w,
\qquad
\xi=\nu,
}
\tag{9.1}
\]

and

\[
\boxed{
r=\Delta\nu^2,
\qquad
s\tau=2\sqrt r,
\qquad
2s\tau=\xi+4\varphi.
}
\tag{9.2}
\]

Numerically only for orientation,

\[
\nu=0.99554058458\ldots,
\quad
w=0.29635968228\ldots,
\quad
\varphi=0.69918090231\ldots,
\]

\[
q/D=2.06856661909\ldots,
\quad
r=0.89882923223\ldots,
\quad
T/D=3.46692842370\ldots .
\tag{9.3}
\]

Equality in (6.5) means the atomic trains alone asymptotically attain the Mantel
capacity for **all** `R=Theta(D^2)` train crossings.  Equality in (7.4) means their
ends asymptotically exhaust every exceptional-face incidence while using only `o(D)`
outer incidences.  The `O(D)` rhombus angular defect additionally forces those
quadratic crossings to occur between direction classes separated by `pi/3+o(1)`.

This is an extremely rigid two-phase candidate and should be attacked with the
promoted Target B interval extraction / coherent-biclique diameter theorem.  That
endpoint exclusion is a separate proof obligation; it is not assumed here.

## 10. Audit and regressions

- The outer measure is built from edge **occurrences**, so contact bridges are not
  undercounted.
- Uniformity follows from asymptotic equality in the closed-walk projection inequality,
  not from a false claim that each outer contact edge is tangent to the force hull.
- Atomicity refers to the DE empirical **train** measure.  The argument uses finite
  neighborhoods of finitely many atoms, then takes the limits in the order required;
  it never identifies the two measures pointwise.
- Exceptional-face endpoint capacity is the exact incidence count `Q+4f`; no face is
  assumed to be a hole in a pure rhombic disk.
- Regular odd shells have `s_Z=2`, so the circuit identities used here do not apply.
- The Target B sliding-interval regression remains binding away from the formal
  Mantel endpoint; no generic dense-graph biclique is inferred.

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Cyclic CRC gives b-P_F=o(D), P_F/D->pi, and F/D->disk.
The outer-walk projective direction measure
    mu_out=(1/D) sum_outer edge-occurrences delta_direction
has cosine transform >=2 width_F/D ->2 and total mass ->pi.
Its integrated transform also ->2pi, so every weak limit has constant cosine
transform 2.  The projective cosine transform is injective; hence
    mu_out -> Lebesgue measure on R/pi Z.
Therefore shrinking neighborhoods of finitely many fixed directions contain o(D)
outer train-end incidences.

For exceptional faces let xi=Q/D, phi=f/D, w=xi-phi.
Keeping f in CC gives
    A_exc/D^2 <= w^2/(4pi).
Cyclic cavity + attachment cells gives
    w >= pi sqrt(1-nu^2),
where nu=(e_BB+2s_C)/D<1.
The rhombus area density satisfies
    r >= r_min(w)=(pi^2-w^2)/(2pi sqrt3).

DE gives for train-direction atomic mass s and tau=T/D:
    s tau >=2 sqrt(r).
Atomic trains have o(D) outer ends, so their two endpoints must fit into the
exceptional-face incidence capacity Q+4f:
    2s tau <= xi+4phi.
Thus
    4sqrt(r)<=w+5phi,
    nu>=xi=w+phi >= (4/5)(w+sqrt(r_min(w))).
The RHS increases in w, so use w=pi sqrt(1-nu^2).  Since
    r_min=Delta nu^2, Delta=pi/(2sqrt3),
we obtain
    (5/4-sqrt(Delta))nu >= pi sqrt(1-nu^2),
therefore
    nu >= pi/sqrt(pi^2+(5/4-sqrt(Delta))^2)
       =0.9955405845835427... .

Next: exclude the formal endpoint using its asymptotically Mantel-extremal atomic
train graph and the promoted coherent-biclique diameter theorem.
```
