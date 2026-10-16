<!-- theorem-state: {"artifact_id":"ART-A9AB888F16A9","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — loaded hull-contact slack and primitive boundary dichotomy

**Date:** 2026-09-09  
**Repository base:** PR #118 after `f34d63a4d80d13fb391efa1c8220079792a4a741`  
**Run type:** exact outer-face / convex-boundary refinement  
**Target:** Target C, C-II after ZF  
**Depends on:** C35 loaded boundary geometry, NM outer-walk interval decomposition, ZT exact terminal partition, DB only for the asymptotic constant  
**External web search:** not used  
**Computation:** displayed decimals only

## LEVEL I STATUS

`STILL OPEN`

NM splits the outer contact-face walk into the `q` intervals between consecutive loaded force-hull vertices. Extracting the unit-side consequence gives an exact coupling not previously recorded in the post-ZF ledger:

\[
\boxed{e_{BB}+x_B\ge q.}
\tag{LH.1}
\]

Equivalently, using ZT,

\[
\boxed{
e_{BB}\ge Q+2(d_H+s_Z).
}
\tag{LH.2}
\]

Thus every exceptional-face defect unit costs at least one direct loaded-loaded unit contact, and every diameter-tree/mixed-row defect unit costs two, up to an explicitly classifiable nonnegative boundary slack.

A useful immediate consequence is the primitive two-branch theorem

\[
\boxed{
\max\{e_{BB},x_B\}\ge q/2.}
\tag{LH.3}
\]

Since DB gives `liminf q/D>=2rho`, `rho=cos rho`, every unbounded post-ZF survivor satisfies

\[
\boxed{
\liminf\frac1D\max\{e_{BB},x_B\}
\ge\rho
=0.7390851332\ldots .}
\tag{LH.4}
\]

Unlike KC, this dichotomy involves two primitive geometric counts only: direct unit contacts among loaded hull vertices versus excess length of the outer contact-face walk.

---

## 1. Hull-side notation

Write the loaded force-hull vertices in cyclic order as

\[
b_1,\ldots,b_q.
\]

Let

\[
s_i:=|b_i-b_{i+1}|
\]

with cyclic indices. Unit separation gives

\[
s_i\ge1.
\tag{1.1}
\]

NM chooses one cyclic pass of the outer contact-face boundary walk and splits it into subwalks

\[
W_i:b_i\leadsto b_{i+1}.
\]

Let `ell_i` be the number of unit-contact edge occurrences in `W_i`. Then

\[
ell_i\ge s_i,
\qquad
\ell_i\in\mathbb Z_{\ge1},
\tag{1.2}
\]

and

\[
\sum_i\ell_i=b=q+x_B.
\tag{1.3}
\]

Consequently

\[
\boxed{
\sum_i(\ell_i-1)=x_B.}
\tag{1.4}
\]

This is NM's exact outer-interval identity.

Let `m` be the number of convex force-hull sides with

\[
s_i>1.
\]

If `s_i>1`, then (1.2) and integrality force

\[
\ell_i\ge2,
\]

so that interval contributes at least one unit to (1.4). Therefore

\[
\boxed{m\le x_B.}
\tag{1.5}
\]

For every remaining side `s_i=1`, the two consecutive loaded vertices themselves form a unit contact. These `q-m` hull-side contacts are distinct edges counted by `e_BB`. Hence

\[
\boxed{e_{BB}\ge q-m\ge q-x_B,}
\tag{1.6}
\]

which proves LH.1. `square`

This proof does not assume that the outer contact walk is simple. Bridge excursions and repeated articulation vertices are already included in the integer lengths `ell_i`.

---

## 2. Exact slack decomposition

Define the two nonnegative integers

\[
\boxed{u_B:=x_B-m\ge0,}
\tag{2.1}
\]

and

\[
\boxed{c_B:=e_{BB}-(q-m)\ge0.}
\tag{2.2}
\]

Here

- `u_B` is outer-walk excess beyond the one mandatory excess edge required for each nonunit convex hull side;
- `c_B` counts loaded-loaded contacts beyond the `q-m` unit convex-hull sides. Such extra edges join nonconsecutive loaded hull vertices and are straight interior chords.

Then

\[
\begin{aligned}
e_{BB}
&=q-m+c_B\\
&=q-x_B+u_B+c_B.
\end{aligned}
\tag{2.3}
\]

ZT gives

\[
q-x_B=Q+2(d_H+s_Z).
\tag{2.4}
\]

Therefore:

### Theorem LH — exact loaded-hull contact slack

\[
\boxed{
 e_{BB}
 =Q+2(d_H+s_Z)+u_B+c_B,
\qquad
u_B,c_B\ge0.}
\tag{LH.5}
\]

Equivalently,

\[
\boxed{
e_{BB}-Q-2(d_H+s_Z)=u_B+c_B.}
\tag{LH.6}
\]

This identifies the complete slack in LH.2. It consists only of deeper outer-walk detours and additional loaded-loaded contact chords.

No stress coefficient or response conductance appears in this identity.

---

## 3. Metric decomposition of `x_B`

Let

\[
P:=\operatorname{per}(F)=\sum_i s_i.
\]

Because `s_i>=1`,

\[
P-q\ge0.
\tag{3.1}
\]

Because each outer subwalk has Euclidean length `ell_i` and joins endpoints at distance `s_i`,

\[
b-P
=\sum_i(\ell_i-s_i)
\ge0.
\tag{3.2}
\]

Hence the outer-walk currency has the exact geometric split

\[
\boxed{
 x_B
 =b-q
 =(P-q)+(b-P).}
\tag{LH.7}
\]

The first term is convex-hull side-length surplus above the unit lower bound; the second is contact-walk detour length above the convex perimeter.

This split is deliberately metric rather than combinatorial. A nonunit hull side may have length `1+o(1)`, so `P-q` does not lower-bound the number `m` by a fixed constant per missing unit side. The integer outer-walk identity (1.4), not a false uniform metric gap, is what proves `m<=x_B`.

---

## 4. Loaded-loaded outerplanar cap with missing-side correction

The straight-line graph on the `q` loaded convex vertices with edge set consisting of the `e_BB` unit contacts is outerplanar and triangle-free.

Add the `m` missing convex-hull sides. The resulting plane graph contains the complete convex `q`-cycle, has

\[
E'=e_{BB}+m
\]

edges, and is 2-connected. Let `t` be its number of bounded triangular faces.

Every triangular face must use at least one added hull side: otherwise its three edges were all original unit contacts, giving a forbidden unit triangle. Each added hull side borders at most one bounded face, so

\[
t\le m.
\tag{4.1}
\]

Euler gives `F_b=E'-q+1` bounded faces. Face incidence therefore gives

\[
\begin{aligned}
2E'
&=q+\sum_{F\ bounded}\deg F\\
&\ge q+3t+4(F_b-t)\\
&=q+4F_b-t\\
&\ge q+4(E'-q+1)-m.
\end{aligned}
\]

Rearranging:

\[
\boxed{
2e_{BB}+m\le3q-4.}
\tag{LH.8}
\]

In terms of the extra loaded chord count `c_B`, since `e_BB=q-m+c_B`,

\[
\boxed{
2c_B\le q+m-4.}
\tag{LH.9}
\]

The cap is not a closing inequality; it records that the slack `c_B` in LH.5 is itself constrained by outerplanarity and triangle-freeness.

---

## 5. Primitive diameter-scale split

LH.1 gives

\[
\max\{e_{BB},x_B\}\ge q/2.
\]

DB gives

\[
\liminf\frac hD\ge2\rho,
\qquad
\rho=\cos\rho,
\]

and `q>=h`. Dividing by `D` proves LH.4.

Thus the post-ZF source cannot distribute all of its mandatory defect only into the abstract currencies `Q,s_C,s_Z,d_H`. At diameter scale, it must exhibit one of two directly visible phenomena:

1. at least `(rho-o(1))D` direct unit contacts between loaded convex-hull vertices; or
2. at least `(rho-o(1))D` excess unit-edge occurrences in the outer contact-face walk beyond the `q` loaded vertices.

This is weaker numerically than KC's `0.886902...D` max bound on the composite currencies, but geometrically more concrete.

---

## 6. Interaction with GU and KC

GU's low pinned/contact-surplus branch assumes

\[
\limsup\frac{e_{BB}+2s_C}{D}<\lambda_*,
\qquad
\lambda_*=\sqrt{\frac{\sqrt3}{\pi}}
=0.7425152492\ldots .
\]

Since `e_BB<=e_BB+2s_C`, LH.1 gives

\[
\frac{x_B}{D}
\ge
\frac qD-rac{e_{BB}}D.
\]

Together with DB, if `limsup (e_BB+2s_C)/D<=lambda<lambda_*`, then

\[
\boxed{
\liminf\frac{x_B}{D}
\ge2\rho-\lambda.}
\tag{LH.10}
\]

Letting `lambda` approach `lambda_*` gives the threshold value

\[
\boxed{
2\rho-\lambda_*
=0.7356550176\ldots .}
\tag{LH.11}
\]

So GU's low-surplus branch simultaneously has

- a quadratic attachment-cell gap `G=Omega(D^2)`;
- `x_B>=(0.735655-o(1))D` outer-walk excess;
- KC's stronger composite bound `x_B+Q>=(0.983160-o(1))D`.

The next low-surplus attack can therefore work with a macroscopic cavity together with a genuinely macroscopic outer contact-face detour, not merely an unspecified boundary defect.

---

## 7. Equality structure

Equality in LH.1 is highly constrained.

If

\[
e_{BB}+x_B=q,
\]

then LH.5 forces

\[
u_B=c_B=0.
\]

Therefore:

1. every nonunit convex-hull side contributes exactly one unit of outer-walk excess;
2. every unit convex-hull side is itself a loaded-loaded contact;
3. there are no additional loaded-loaded contact chords.

More concretely, for each nonunit hull side the corresponding outer subwalk has exactly two unit-contact edges, while every unit hull side has a one-edge outer subwalk. Thus the outer contact boundary is obtained from the convex loaded polygon by replacing exactly `x_B` nonunit sides by two-edge unit detours and leaving every other side as a direct unit contact.

The intermediate vertex of each two-edge replacement is not a convex-hull vertex and hence is not a diameter endpoint. In fully force-visible C-II, C26 forbids such an unloaded positive-contact vertex from having total contact degree one or two. Consequently each simple intermediate detour vertex must participate in additional contact structure beyond its two boundary edges. Repeated/articulation degeneracies must instead be charged to the outer-walk topology. This identifies a concrete stability target for the high-`x_B` branch.

---

## 8. Regression audit

### Regular odd shell

All `q` hull sides are unit contacts, so

\[
m=x_B=u_B=c_B=0,
\qquad e_{BB}=q.
\]

LH.1 and LH.5 are equalities. Thus the regular-shell regression is retained.

### Unit square

Again all four hull sides are unit contacts and there are no loaded chords:

\[
e_{BB}=q=4,
\qquad x_B=0.
\]

LH.1 is exact.

### Pure two-edge replacement

A convex hull side of length strictly between one and two may be replaced in the outer contact walk by two unit edges. It contributes exactly one to `m` and one to `x_B`; LH does not assert a positive metric area gap for that replacement. The detour can be arbitrarily shallow as its hull chord approaches length two.

### Bridge excursions

If a unit hull side remains present but the outer walk makes an articulation/bridge excursion before advancing to the next loaded vertex, the side is still counted among the `q-m` unit hull contacts while the extra walk length enters `u_B`. Thus LH.5 does not misclassify bridge repetition as a missing hull side.

---

## 9. Next theorem

LH turns the post-ZF boundary problem into two primitive branches.

### High `e_BB`

Exploit that a linear family of unit contacts joins vertices that are all actual diameter endpoints, with loaded degree at most three and with the diameter graph a convex geometric thrackle. The missing theorem should couple these two graphs rather than merely count either one.

### High `x_B`

Use the exact metric split LH.7 and the equality/stability picture above. A large outer-walk detour is either carried by many nonloaded outer vertices or by substantial articulation/bridge repetition. The former is subject to C26 and interior attachment; the latter is subject to the ZBR/ZBC bridge machinery.

This is a more concrete split than treating `x_B,Q,s_Z` as interchangeable linear currencies.

---

## 10. Promotion recommendation

**Hold as report pending independent audit.**

The proof is elementary downstream of the report-level post-ZF normalization and NM's outer-walk decomposition. It should not be promoted independently of those dependencies.

---

## 11. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Let m be the number of consecutive loaded force-hull sides whose Euclidean length
is >1. NM's outer-walk intervals have integer lengths ell_i and
  sum(ell_i-1)=x_B.
Every nonunit hull side forces ell_i>=2, so
  m<=x_B.
The other q-m hull sides have length exactly 1 and are direct loaded-loaded contacts.
Thus
  e_BB>=q-m>=q-x_B,
so exactly
  e_BB+x_B>=q.
Using ZT, q-x_B=Q+2(d_H+s_Z), hence
  e_BB>=Q+2(d_H+s_Z).

Define
  u_B=x_B-m,
  c_B=e_BB-(q-m).
Then
  e_BB=Q+2(d_H+s_Z)+u_B+c_B.
This is the complete slack decomposition.

Also
  x_B=(per(F)-q)+(b-per(F))
with both terms nonnegative.
Adding the m missing hull sides to the B-B contact graph gives
  2e_BB+m<=3q-4.

Primitive split:
  max(e_BB,x_B)>=q/2,
so DB gives
  liminf max(e_BB,x_B)/D>=rho=0.7390851332... .

In GU's branch A=e_BB+2s_C <= lambda D < lambda_*D,
  liminf x_B/D >=2rho-lambda;
at lambda_*=0.7425152492... this is 0.7356550176... .
Together with KC, that same branch has
  G=Omega(D^2),
  x_B=Omega(D),
  x_B+Q>=(0.983160-o(1))D.

Next: high-e_BB coupling of the unit-contact graph to the diameter thrackle,
or high-x_B conversion of outer detours/repetition into bridge or packing cost.
```
