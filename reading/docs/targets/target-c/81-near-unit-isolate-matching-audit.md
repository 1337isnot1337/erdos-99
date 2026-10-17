> Generated reading edition · [exact source](../../../../docs/targets/target-c/81-near-unit-isolate-matching-audit.md) · source SHA-256 `c2405b23826fee8e4cdd077ad7b1d1e347a323eef6d07aa1b3af72a69fb7a38e`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target C — near-unit matching inside a macroscopic inactive chamber

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

Canonical Section 77 forces, in the subquadratic positive-core branch, one actual
convex inactive chamber containing quadratically many contact-isolated source points
while spending only boundary-order Oler slack. This module extracts the first genuinely
metric consequence of that near-capacity statement.

It does **not** assert an exact new unit contact. Instead it proves that near-unit
pairs are quantitatively unavoidable. At scale `1+epsilon`, the chamber contains a
large vertex-disjoint matching of pairs whose distances lie in

$$
(1,1+\epsilon].
$$

In particular, for a suitable fixed `K`, the canonical Section-77 chamber contains
`Omega(D)` vertex-disjoint pairs at distance

$$
1<|x-y|\le1+{K\over D}.
$$

The proof is finite and uses only Oler's inequality plus the chamber's exact Oler
slack. No lattice stability theorem, Voronoi theorem, or KKT multiplier estimate is
used.

---

# 81. Boundary-order Oler slack forces many almost-contacts

Let `C` be any convex body containing a specified set `Z` of `z` source points. Assume
these points are contact-isolated in the full unit-separated source, so

$$
|x-y|>1\qquad(x\ne y\in Z).
\tag{81.1}
$$

Write

$$
A:=\operatorname{area}(C),
\qquad
P:=\operatorname{per}(C),
\qquad
a_0:={\sqrt3\over2},
\tag{81.2}
$$

and define the isolate-only Oler slack

$$
\boxed{
\sigma:={A\over a_0}+{P\over2}+1-z\ge0.
}
\tag{81.3}
$$

Canonical Section 77 supplies exactly such a triple `(C,Z,sigma)` for every inactive
chamber.

For `epsilon>0`, define the **epsilon-near-contact graph** `G_epsilon` on `Z` by

$$
xy\in E(G_\epsilon)
\quad\Longleftrightarrow\quad
|x-y|\le1+\epsilon.
\tag{81.4}
$$

Because of (81.1), every edge of this graph has strict length

$$
1<|x-y|\le1+\epsilon.
\tag{81.5}
$$

Let `nu_epsilon` denote the maximum matching number of `G_epsilon`.

## 81.1 Exact matching inequality

### Theorem 81.1

For every `epsilon>0`,

$$
\boxed{
2\nu_\epsilon
\ge
{A\over a_0}
\left(1-{1\over(1+\epsilon)^2}\right)
+{P\over2}
\left(1-{1\over1+\epsilon}\right)
-\sigma.
}
\tag{81.6}
$$

Equivalently, since `nu_epsilon>=0`, the right side may be replaced by its positive
part.

### Proof

Fix a maximum matching `M` in `G_epsilon`, with `|M|=nu_epsilon`, and let `U` be the
unmatched vertex set. Then

$$
|U|=z-2\nu_\epsilon.
\tag{81.7}
$$

A maximum matching is maximal. Therefore two unmatched vertices cannot be adjacent in
`G_epsilon`; otherwise their edge could be added to `M`. Hence

$$
|x-y|>1+\epsilon
\qquad(x\ne y\in U).
\tag{81.8}
$$

Scale the chamber and the unmatched set by the factor `(1+epsilon)^(-1)` about any
fixed origin. The scaled copy of `U` is unit-separated and lies in the scaled convex
body. Oler's finite packing inequality gives

$$
|U|
\le
{A\over a_0(1+\epsilon)^2}
+{P\over2(1+\epsilon)}+1.
\tag{81.9}
$$

Substitute (81.7), then use the exact slack identity (81.3),

$$
z={A\over a_0}+{P\over2}+1-\sigma.
\tag{81.10}
$$

Subtracting (81.9) from (81.10) gives exactly (81.6). `square`

---

## 81.2 Small-scale form

For `0<epsilon<=1`,

$$
1-{1\over(1+\epsilon)^2}
={\epsilon(2+\epsilon)\over(1+\epsilon)^2}
\ge {3\over4}\epsilon.
\tag{81.11}
$$

The perimeter contribution in (81.6) is nonnegative, so

$$
\boxed{
\nu_\epsilon
\ge {3A\over8a_0}\,\epsilon-{\sigma\over2}
\qquad(0<\epsilon\le1).
}
\tag{81.12}
$$

Thus the matching count is controlled by the bulk-area gain obtained by scaling the
packing, with only the original Oler slack as a loss.

### Corollary 81.2 — mesoscopic near-contact abundance

Suppose along an unbounded sequence

$$
A\ge\alpha D^2,
\qquad
\sigma\le SD
\tag{81.13}
$$

for fixed `alpha>0` and `S<infinity`. Let `epsilon_D<=1` satisfy

$$
\epsilon_DD\longrightarrow\infty.
\tag{81.14}
$$

Then

$$
\boxed{
\nu_{\epsilon_D}=\Omega(\epsilon_DD^2).
}
\tag{81.15}
$$

Indeed (81.12) gives

$$
\nu_{\epsilon_D}
\ge {3\alpha\over8a_0}\epsilon_DD^2-{S\over2}D,
$$

and the second term is lower order under (81.14).

So every scale larger than `1/D` already contains the expected bulk number of
disjoint almost-contacts.

---

## 81.3 The inverse-diameter scale

The same inequality reaches the critical `1/D` scale if the constant is chosen large
enough.

### Corollary 81.3 — linear matching at distance `1+K/D`

Assume (81.13). If

$$
K>{4a_0S\over3\alpha},
\tag{81.16}
$$

then for all sufficiently large `D`, with

$$
\epsilon={K\over D},
$$

we have

$$
\boxed{
\nu_{K/D}
\ge
\left({3\alpha K\over8a_0}-{S\over2}\right)D
=\Omega(D).
}
\tag{81.17}
$$

Consequently there are `Omega(D)` pairwise vertex-disjoint pairs of actual source
points satisfying

$$
\boxed{
1<|x-y|\le1+{K\over D}.
}
\tag{81.18}
$$

No pair in (81.18) is an actual contact: every chamber point under consideration is
contact-isolated in the full source.

---

## 81.4 Application to canonical Section 77

In canonical Section 77's subquadratic-core branch, the selected chamber `C_*`
satisfies

$$
A_*\ge\alpha_*D^2
\tag{81.19}
$$

for some absolute `alpha_*>0` along all sufficiently large survivors; Section 77 gives
the explicit asymptotic choice

$$
\alpha_*<{4A_{SC}^2\over169\pi},
\qquad
A_{SC}:={2\rho+\sin(2\rho)\over4},
\quad \rho=\cos\rho,
\tag{81.20}
$$

with any fixed smaller positive constant valid eventually. It also gives

$$
\sigma_*=O(D).
\tag{81.21}
$$

The implied constant is absolute over the canonical post-ZF class. Therefore there is
an absolute constant `K_0<infinity` such that every sufficiently large survivor in the
Section-77 subquadratic-core branch contains, inside one actual inactive chamber, at
least `cD` vertex-disjoint pairs for some absolute `c>0`, each satisfying

$$
\boxed{
1<|x-y|\le1+{K_0\over D}.
}
\tag{81.22}
$$

This is stronger than the qualitative statement that the minimum isolate-isolate
distance tends to one.

Proof-only Section 79, if independently promoted, extends the same conclusion to any
subsequence on which the inactive population has positive quadratic density: its
Branch A again supplies one chamber with `A=Omega(D^2)` and `sigma=O(D)`.
Section 79 is not needed for the canonical Section-77 application above.

---

## 81.5 A useful contrapositive

Theorem 81.1 also quantifies how impossible a uniformly expanded isolate packing is.
If `nu_epsilon=0`, then

$$
{A\over a_0}
\left(1-{1\over(1+\epsilon)^2}\right)
\le\sigma,
\tag{81.23}
$$

after dropping the nonnegative perimeter term. If `A>=alpha D^2` and
`sigma<=SD`, this forces

$$
\epsilon=O(D^{-1}).
\tag{81.24}
$$

Thus a macroscopic boundary-slack chamber cannot keep all of its isolated points at a
common separation `1+omega(1/D)`.

---

## 81.6 What this changes and what remains open

The canonical Section-77 chamber endpoint can now be sharpened, at proof-only status,
to

```text
one actual convex inactive chamber C_*
  area(C_*) = Omega(D^2)
  contact-isolated population = Omega(D^2)
  Oler slack = O(D)
        |
        v
for some absolute K_0:
  Omega(D) vertex-disjoint actual source pairs
  have distance in (1, 1+K_0/D].
```

This materially narrows the chamber branch. The inactive population cannot be both
near-capacity and metrically diffuse at the inverse-diameter scale.

It still does **not** create a unit contact or a unit equilateral triangle. A tiny
collective perturbation can keep all these distances strictly above one. Nor does the
matching by itself give compatible motions of the matched pairs relative to the
chamber boundary.

The next chamber-side theorem should exploit the simultaneous nature of these
`Omega(D)` disjoint almost-contacts. Examples of genuinely closing targets are:

1. a boundary-protected perturbation theorem showing that `Omega(D)` disjoint
   `1+O(1/D)` pairs force one exact contact under diameter minimality;
2. a second-order packing-stability inequality charging a positive amount of Oler
   slack for maintaining all matched gaps strictly positive; or
3. a source-preserving deformation using the matched almost-contact graph and the
   chamber boundary to construct a strict sub-`D` competitor.

No such closing implication is asserted here.

---

## 81.7 Dependency audit

The finite matching theorem (81.6) requires only:

- a convex chamber `C`;
- a specified contact-isolated unit-separated source subset `Z` in `C`;
- the finite Oler inequality; and
- the exact isolate-only Oler slack definition.

The canonical Target C application uses only `C-INACTIVE-CHAMBER` (Section 77), which
supplies a chamber with `A=Omega(D^2)` and `sigma=O(D)` in the subquadratic-core
branch.

No Section-78 grid theorem, no annular Voronoi theorem, no KKT coefficient lower bound,
no lattice-stability theorem, and no deletion of source points is used.

**Status:** canonical after the independent matching promotion audit.
**Theorem state:** promoted as `C-INACTIVE-NEAR-MATCHING`; C-II remains open.
