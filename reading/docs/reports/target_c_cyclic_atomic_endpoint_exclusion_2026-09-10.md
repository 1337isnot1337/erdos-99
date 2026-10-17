> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_atomic_endpoint_exclusion_2026-09-10.md) · source SHA-256 `59f3468b019d4a7aba75b1b971862573915a2467a84533300bfe8aa9fd657640`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-32488DD27EEF","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic atomic endpoint exclusion by exceptional-face direction rigidity

**Date:** 2026-09-10

**Repository base:** `1adc420e9227476135d6891b61f1a75193aa90ab` plus the cyclic reports on this branch

**Run type:** C-II endpoint exclusion / equality-case audit

**Target:** post-ZF `s_Z=0`, Woodall cyclic branch `d_H=0`

## LEVEL I STATUS

`STILL OPEN`.

The preceding atomic-endpoint theorem proves

$$
\liminf {e_{BB}+2s_C\over D}
\ge
\lambda_A
:={\pi\over
\sqrt{\pi^2+\left(\frac54-\sqrt{\frac{\pi}{2\sqrt3}}\right)^2}}
=0.99554058458\ldots .
\tag{AX.1}
$$

This report proves that the endpoint itself is impossible.  Consequently there are
absolute constants `epsilon_A>0` and `D_0<infinity` such that every sufficiently
large cyclic `s_Z=0` survivor satisfies

$$
\boxed{
{e_{BB}+2s_C\over D}
\ge \lambda_A+\epsilon_A.
}
\tag{AX.2}
$$

The contradiction uses two equality consequences of the same endpoint:

1. essentially every exceptional-face boundary incidence is an endpoint of an atomic
   train, and all atomic train directions lie in one three-point `pi/3` orbit;
2. one exceptional face has perimeter `Theta(D)` and asymptotically maximal area for
   that perimeter, so its boundary-edge direction measure is asymptotically uniform.

A macroscopic convex face cannot satisfy both conclusions.

No quantitative value of `epsilon_A` is claimed.  In particular this report does not
assert that the lower bound crosses `1`.

---

## 1. Assume an endpoint sequence

Assume for contradiction that an unbounded cyclic circuit sequence satisfies

$$
\nu_D:={e_{BB}+2s_C\over D}\longrightarrow\lambda_A=:\nu<1.
\tag{1.1}
$$

Use the notation of the preceding report:

$$
\xi=\lim Q/D,
\qquad
\varphi=\lim f/D,
\qquad
w=\xi-\varphi,
\tag{1.2}
$$

$$
r=\lim R/D^2,
\qquad
\tau=\lim T/D,
\tag{1.3}
$$

and let `s` be the total atomic mass of the limiting empirical train-direction
probability measure.

The proof of AX.1 is a chain of monotone inequalities.  Equality in its final equation
forces equality throughout that chain.  Hence

$$
\boxed{
\xi=\nu,
\qquad
w=\pi\sqrt{1-\nu^2},
\qquad
\varphi=\nu-w,
}
\tag{1.4}
$$

$$
\boxed{
r=\Delta\nu^2,
\qquad
s\tau=2\sqrt r,
\qquad
2s\tau=\xi+4\varphi,
\qquad
\Delta={\pi\over2\sqrt3}.
}
\tag{1.5}

In particular `w>0` and `s>0`.

The first equality in (1.4) also combines with the exact PC ledger

\[
e_{BB}=d_P+Q+c_B
$$

to give

$$
\boxed{d_P=o(D),\qquad c_B=o(D),\qquad s_C=o(D),}
\tag{1.6}
$$

although these three facts are not needed below.

---

## 2. Equality in the refined exceptional-face square bound produces one giant face

Let the exceptional faces have defects

$$
r_i:=\deg(F_i)-4\ge1,
\qquad
\sum_{i=1}^f r_i=Q.
\tag{2.1}
$$

The refined CC bound used in AX.1 is

$$
A_{exc}
\le{1\over4\pi}
\left(\sum_i r_i^2+O(D)\right)
\le{(Q-f+1)^2+O(D)\over4\pi}.
\tag{2.2}
$$

At the endpoint, the cavity lower bound, the vanishing outer-pocket area, and (1.4)
force

$$
\boxed{{A_{exc}\over D^2}\to{w^2\over4\pi}.}
\tag{2.3}
$$

Hence both inequalities in (2.2) are asymptotically sharp:

$$
\sum_i r_i^2=w^2D^2+o(D^2).
\tag{2.4}
$$

Let `r_*:=max_i r_i`.  Since

$$
\sum_i r_i^2\le r_*\sum_i r_i=r_*Q,
$$
(2.4) only gives a weaker positive lower bound on `r_*`.  To recover the sharp one,
write `u_i=r_i-1>=0`.  Then

$$
\sum_i u_i=Q-f=wD+o(D),
$$
while (2.4) and `Q,f=O(D)` imply

$$
\sum_i u_i^2=w^2D^2+o(D^2).
\tag{2.5}
$$

If `u_*:=max_i u_i`, then

$$
\sum_i u_i^2\le u_*\sum_i u_i,
$$
so (2.5) yields

$$
\boxed{u_*/D\to w.}
\tag{2.6}
$$

Thus one exceptional face `F_*` has perimeter

$$
k_*:=\deg(F_*)=r_*+4=u_*+5,
$$
with

$$
\boxed{k_*/D\to w.}
\tag{2.7}
$$

Moreover

$$
\sum_{i\ne *}u_i=o(D),
\qquad
\sum_{i\ne *}u_i^2=o(D^2).
\tag{2.8}
$$

The total area of all other exceptional faces is therefore `o(D^2)` after applying
(2.2) to that subfamily.  Equation (2.3) implies

$$
\boxed{
{\operatorname{area}(F_*)\over D^2}
\to {w^2\over4\pi}.
}
\tag{2.9}
$$

Since C51 makes `F_*` a convex unit-edge polygon of perimeter `k_*`, (2.7)--(2.9)
show that it asymptotically attains the planar isoperimetric inequality.

---

## 3. The giant face has asymptotically uniform edge directions

Translate `F_*` and divide coordinates by `D`.  The normalized convex bodies have
perimeters tending to `w`, areas tending to `w^2/(4pi)`, and uniformly bounded
diameter because they lie in the source hull of diameter one after scaling.

By Blaschke compactness, every subsequential Hausdorff limit has perimeter `w` and area
`w^2/(4pi)`.  Equality in the isoperimetric inequality forces the limit to be the disk
of radius

$$
R_*={w\over2\pi}.
\tag{3.1}
$$

Therefore the entire normalized sequence converges, after suitable translations, to
that disk.

Define the projective unit-edge direction measure of `partial F_*` by

$$
\sigma_D:={1\over D}
\sum_{e\subset\partial F_*}\delta_{\theta_e}.
\tag{3.2}
$$

Its total mass is `k_*/D->w`.  Because `partial F_*` is a convex polygonal boundary,
for every projective direction `alpha` its projection variation is exactly twice its
width:

$$
\int|\cos(\theta-\alpha)|\,d\sigma_D(\theta)
={2w_{F_*}(\alpha)\over D}
\longrightarrow {2w\over\pi}.
\tag{3.3}
$$

As in the outer-walk argument of the preceding report, the projective cosine transform
is injective because all nonconstant Fourier coefficients of `|cos|` are nonzero.
Thus

$$
\boxed{
\sigma_D\Rightarrow {w\over\pi}\,d\theta
\quad\text{on }\mathbb R/\pi\mathbb Z.
}
\tag{3.4}
$$

In particular, for three arcs of total projective length tending to zero, the fraction
of `F_*` boundary edges whose directions lie in those arcs tends to zero, not one.

---

## 4. Endpoint equality confines all atomic train directions to one three-point orbit

The DT/DE proof shows that asymptotically every quadratic train crossing has direction
pair separated by `pi/3`; all other angular crossing pairs cost positive rhombus area
excess, while CRE gives only `O(D)` total excess.

Partition the atoms of the limiting train-direction measure into orbits of the map

$$
\theta\mapsto\theta+\pi/3
\quad\text{on }\mathbb R/\pi\mathbb Z.
\tag{4.1}
$$

Each orbit has exactly three projective positions.  Let `s_j` be the total atomic mass
in orbit `j`, so `sum_j s_j=s`.

Crossing mass between two distinct orbits is `o(1)` after normalization by `T^2`.
Within one orbit the train-crossing graph is triangle-free, so Mantel gives at most
`s_j^2/4` normalized edge mass.  Therefore the DE inequality refines to

$$
{r\over\tau^2}
\le {1\over4}\sum_j s_j^2
\le {s^2\over4}.
\tag{4.2}
$$

Endpoint equality `s tau=2sqrt(r)` from (1.5) makes both inequalities in (4.2)
equalities.  Hence

$$
\sum_j s_j^2=s^2.
$$

For nonnegative `s_j`, equality is possible only when exactly one orbit carries all
atomic mass.  Thus there is a projective direction `theta_0` such that every atomic
train direction belongs to

$$
\boxed{
\{\theta_0,\theta_0+\pi/3,\theta_0+2\pi/3\}
}
\tag{4.3}
$$

in the limiting measure.

Equivalently, for every `eta>0`, three sufficiently small fixed arcs around those
positions contain all but `eta T` atomic-direction trains for all sufficiently large
members of the endpoint sequence.

---

## 5. Exceptional endpoint saturation forces the giant face into those three directions

The preceding atomic-endpoint theorem proves that atomic train directions have only
`o(D)` outer-face endpoint incidences.  Every stopped train has exactly two endpoint
incidences, and all non-outer endpoints lie on exceptional bounded faces.  The total
exceptional-face endpoint capacity is exactly

$$
Q+4f.
\tag{5.1}
$$

Endpoint equality (1.5) says

$$
2s\tau=\xi+4\varphi.
\tag{5.2}
$$

Therefore the number of exceptional-face boundary incidences that are **not** endpoints
of atomic trains is `o(D)`: atomic trains have `2sT+o(D)` total endpoints, lose only
`o(D)` of them to the outer face, and the exceptional faces have exactly
`(Q+4f)=2sT+o(D)` available incidences.

Every boundary edge of `F_*` is one such exceptional-face incidence and is the endpoint
edge of its stopped train.  Since `k_*=wD+o(D)` with `w>0`, (4.3) and the preceding
saturation imply:

> for every fixed `eta>0`, all but `o(D)+eta D` boundary edges of `F_*` have
> projective direction in three `eta`-neighborhoods of the positions (4.3).

First let `D->infinity`, then `eta->0`.  The limiting projective edge-direction measure
of `F_*` is therefore supported on the three-point set (4.3).

This contradicts (3.4), whose limit is the non-atomic uniform measure
`(w/pi)dtheta` with `w>0`.

Hence the endpoint sequence (1.1) cannot exist.

---

## 6. Uniform positive gap

If AX.2 were false, for every integer `j` there would be a cyclic `s_Z=0` survivor
with `D_j>=j` and

$$
{e_{BB}+2s_C\over D_j}<\lambda_A+{1\over j}.
$$

AX.1 forces the same ratios to converge to `lambda_A`, producing the endpoint sequence
just excluded.  Therefore some absolute `epsilon_A>0` and `D_0` exist, proving AX.2.

This compactness argument is qualitative.  No numerical value of `epsilon_A` is
claimed.

---

## 7. Adversarial audit

- **No pure-disk CR import.**  The proof does not use common crossing order through
  holes.  It uses only DT/DE crossing mass and endpoint incidences, both already proved
  with exceptional faces.
- **Face count retained.**  The giant-face conclusion uses `u_i=r_i-1`, not the false
  claim that `Q` itself concentrates in one face.  At the formal endpoint there remain
  `Theta(D)` essentially pentagonal exceptional faces.
- **Direction measures are different objects.**  The train atomic measure and the
  giant-face boundary measure are connected only through actual stopped-train endpoint
  edges; they are not identified globally.
- **Three-point support.**  This follows only at endpoint equality from the refined
  orbitwise Mantel inequality (4.2), not from `E=O(D)` alone.
- **Regular odd shell.**  It has `s_Z=2`, so the circuit identities and endpoint
  saturation do not apply.
- **Threshold above one is not claimed.**  Endpoint exclusion gives a nonexplicit
  positive gap above `0.99554...`; it does not by itself close the cyclic branch.

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Assume cyclic s_Z=d_H=0 and nu=(e_BB+2s_C)/D -> lambda_A.
Equality in the AE chain forces
    xi=Q/D -> nu,
    w=(Q-f)/D -> pi sqrt(1-nu^2)>0,
    r=R/D^2 -> Delta nu^2,
    s tau=2sqrt(r),
    2s tau=xi+4phi.

Keeping u_i=(deg F_i-5)>=0 in the exceptional-face square bound shows one face F_*
has perimeter k_*=wD+o(D) and area k_*^2/(4pi)-o(D^2).  Hence F_*/D -> disk, and
its unit-edge projective direction measure tends to uniform Lebesgue measure.

On the train side, equality in DE's Mantel bound can be refined orbitwise under
+pi/3.  Since different direction orbits carry no quadratic crossing mass and
sum s_j^2<=s^2, endpoint equality forces all atomic train mass into one 3-point orbit
{theta,theta+pi/3,theta+2pi/3}.

AE outer-direction equidistribution says atomic trains have o(D) outer endpoints.
The equality 2s tau=xi+4phi says their remaining endpoints exhaust all exceptional
face incidences up to o(D).  Therefore all but o(D) edges of the macroscopic face F_*
have directions in three shrinking windows, contradicting its uniform disk-like edge
direction measure.

Thus the endpoint is impossible and there exists epsilon_A>0 with
    (e_BB+2s_C)/D >= lambda_A+epsilon_A
for all sufficiently large cyclic circuit survivors.

Next: quantify this direction-measure contradiction strongly enough to test whether
the uniform gap crosses 1, or find an independent upper tradeoff for the cyclic
loaded-contact/pinned-stress currency.
```
