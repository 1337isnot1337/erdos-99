> Generated reading edition · [exact source](../../../docs/reports/target_c_superstable_bar_sap_2026-09-09.md) · source SHA-256 `e6fd27b64d4f8807307e9788f31d99cd7ebc435fe9853fe55087782c5441a325`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-3BAC45892652","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — ZR/ZF superstable-bar and Strong Arnold consequences

**Date:** 2026-09-09  
**Repository base:** `2c476b38ee07218bb17a594b397717866c58b971`  
**Run type:** exact structural continuation / literature bridge  
**Target:** Target C Gate C-II / Level I  
**LEVEL I STATUS:** STILL OPEN

This note records two exact consequences of the audited report-level ZR/ZF state.
They do not prove the remaining face inequality and they do not promote ZR/ZF.

The first consequence is that the equality bar framework on the complete active
contact/diameter support is superstable and therefore universally rigid. The second
is that the same maximal-rank PSD stress has the Strong Arnold Property (SAP), so the
signed support graph has signed Colin-de-Verdiere parameter at least three and hence
contains one of the two exact forbidden signed minors from Arav--Hall--Li--van der
Holst.

A critical sign caveat is part of the theorem: the KKT stress is *not* proper for the
actual cable/strut inequality orientation `contacts >= 1`, `diameters <= D`. Therefore
Connelly's tensegrity super-stability theorem cannot be used to claim universal
rigidity of the inequality tensegrity. Only the associated equality bar framework is
certified.

## 1. Setup

Work in the same sufficiently large lexicographically normalized hypothetical C-II
source as ZR and ZF. Let `V` be the `v` vertices of the nonisolated contact core, let
`C` be the full unit-contact graph on that core, and let `H` be the full actual
diameter graph. Choose the relative-interior normalized KKT stress. Thus

```math
\alpha_e>0\quad(e\in C),\qquad
\beta_h>0\quad(h\in H),
```

and

```math
\Omega=L_C(\alpha)-L_H(\beta)\succeq0.
\tag{U1}
```

ZR gives

```math
\ker\Omega=\operatorname{span}\{\mathbf 1,P_x,P_y\},
\qquad
\operatorname{rank}\Omega=v-3.
\tag{U2}
```

ZF proves that the ordinary bar framework whose edge set is

```math
E:=C\cup H
```

is infinitesimally rigid in the plane, so its bar rigidity matrix has rank
`2v-3`.

## 2. The equality bar framework is superstable

### Theorem U1 — superstable mixed equality framework

Treat every edge in `C union H` as an ordinary bar fixed at its present length. Then
this planar bar framework is superstable and hence universally rigid.

### Proof

Equation (U1) is an equilibrium stress matrix for the bar framework: its edge stress
is `+alpha_e` on a contact edge and `-beta_h` on a diameter edge. Bar stresses have no
sign restriction. By (U2), the stress matrix is PSD of maximal planar rank `v-3`.

It remains to check the conic-at-infinity condition. If a nonzero symmetric `2 x 2`
matrix `S` satisfied

```math
(p_i-p_j)^T S(p_i-p_j)=0
\qquad(ij\in E),
\tag{U3}
```

then the affine velocity field `u_i=S p_i` (or, equivalently, a suitable nonzero
linear field obtained from `S`) would have zero first variation on every bar. This is
a non-Euclidean infinitesimal affine flex unless `S=0`. ZF's infinitesimal rigidity
therefore rules out (U3) for nonzero `S`.

Connelly's super-stability theorem for bar frameworks now applies: a PSD equilibrium
stress of rank `v-d-1=v-3` together with the conic condition implies universal
rigidity. QED.

### Exact meaning

If another configuration in any Euclidean dimension has exactly the same lengths on
all edges of `C union H`, then it is congruent to the source core.

This is stronger than ZF's infinitesimal equality-bar rigidity, but it does **not**
say that every configuration satisfying

```math
|ij|\ge1\ (ij\in C),\qquad |hk|\le D\ (hk\in H)
```

is congruent.

## 3. Why the tensegrity shortcut is invalid

Use the standard tensegrity convention in which a cable has the upper-bound
constraint and a strut has the lower-bound constraint. Thus in the present packing
problem

- diameter edges `H` are cables (`|h| <= D`);
- contact edges `C` are struts (`|e| >= 1`).

With the weighted-Laplacian convention used by Oba--Tanigawa and Connelly, a proper
stress is nonnegative on cables and nonpositive on struts. Our KKT/bar weights are
instead

```math
\omega_e=+\alpha_e>0\quad(e\in C),\qquad
\omega_h=-\beta_h<0\quad(h\in H),
```

the opposite signs. Hence this stress is strictly *anti-proper* for the actual
packing inequalities.

Therefore the tensegrity version of Connelly's theorem is not applicable to the
packing inequality system. This blocks the tempting but false implication

```text
ZR + ZF -> every same-or-better packing of the core is congruent.
```

The valid implication is only the equality-bar statement in Theorem U1.

## 4. The ZR stress has the Strong Arnold Property

Let `P` be the `v x 3` affine-coordinate matrix whose `i`th row is

```math
\widehat p_i^T=(1,p_{i,x},p_{i,y}).
```

Then (U2) says `ker Omega = col(P)`.

Recall the SAP condition for a symmetric matrix with support graph `G=(V,E)`: if a
symmetric matrix `X` satisfies

```math
\Omega X=0,
\qquad X_{ii}=0,
\qquad X_{ij}=0\quad(ij\in E),
\tag{U4}
```

then `X=0`.

### Theorem U2 — Strong Arnold Property

The relative-interior ZR stress matrix `Omega` satisfies SAP with respect to the mixed
support graph `G=(V,C union H)`.

### Proof

Assume (U4). Since every column of `X` lies in `ker Omega=col(P)` and `X` is
symmetric, there is a symmetric `3 x 3` matrix `A` such that

```math
X=PAP^T.
\tag{U5}
```

One direct construction is to let `L=(P^TP)^{-1}P^T` and put `A=LXL^T`; symmetry of
`X` and the fact that both its row and column spaces lie in `col(P)` give (U5).

Write

```math
A=\begin{pmatrix}a&b^T\\ b&Q\end{pmatrix},
```

where `Q` is symmetric `2 x 2`. For an edge `ij in E`, the diagonal and edge zeros in
(U4) imply

```math
0=X_{ii}+X_{jj}-2X_{ij}
=(p_i-p_j)^TQ(p_i-p_j).
\tag{U6}
```

Thus all mixed-framework edge directions lie on the conic at infinity defined by
`Q`. ZF infinitesimal rigidity forces `Q=0`.

Now the diagonal condition becomes

```math
0=X_{ii}=a+2b\cdot p_i
\qquad(i\in V).
\tag{U7}
```

The core affinely spans the plane because it contains a two-dimensional force hull.
Hence the affine function in (U7) vanishes identically, so `a=0` and `b=0`. Therefore
`A=0`, and (U5) gives `X=0`. QED.

## 5. Signed Colin-de-Verdiere consequence

Define a signed graph `(G,Sigma)` on the mixed support by declaring

- contact edges even;
- diameter edges odd, so `Sigma=H`.

Because `D>1`, `C` and `H` are disjoint. Off diagonal,

```math
\Omega_{ij}<0\quad(ij\in C),
\qquad
\Omega_{ij}>0\quad(ij\in H),
```

so `Omega` belongs to the signed matrix class `S(G,Sigma)` of
Arav--Hall--Li--van der Holst. It is PSD, has SAP by U2, and has nullity three by ZR.
Therefore

```math
\boxed{\nu(G,\Sigma)\ge3.}
\tag{U8}
```

Their exact excluded-minor theorem says a signed graph has `nu<=2` iff it has no
minor isomorphic to either

- `K_4^o=(K_4,E(K_4))`, the all-odd signed `K_4`; or
- `K_3^=`, obtained from an all-even triangle by adding an odd edge parallel to every
  even edge.

Taking the contrapositive gives:

### Corollary U3 — forced signed minor

The mixed contact/diameter signed support graph contains a signed minor isomorphic to

```math
\boxed{K_4^o\quad\text{or}\quad K_3^=.}
\tag{U9}
```

This is an exact topological consequence of ZR/ZF. It is not yet a geometric
contradiction: signed contractions/switchings do not preserve the literal distinction
between a unit contact and a geometric diameter edge.

## 6. Literature imported

1. R. Connelly, super-stability theorem for frameworks; a convenient modern statement
   is Theorem 2.5 of R. Oba and S. Tanigawa, *Characterizing the universal rigidity of
   generic tensegrities*, Mathematical Programming 197 (2023), 109--145,
   <https://doi.org/10.1007/s10107-021-01730-2>. Only the sufficiency theorem is used.
2. M. Arav, F. J. Hall, Z. Li, H. van der Holst, *Signed graphs whose signed Colin de
   Verdiere parameter is two*, J. Combin. Theory Ser. B 116 (2016), 440--455,
   <https://doi.org/10.1016/j.jctb.2015.09.007>. The exact input is their theorem
   `nu(G,Sigma)<=2` iff there is no `K_4^o` or `K_3^=` signed minor.

Neither source contains an Erdős #99 packing theorem.

## 7. Effect on the live endpoint

The direct closing inequality remains

```math
 b+\sum_F(\deg F-4)>2h.
```

U1/U2 add two pieces of structure that were not previously recorded:

1. the equality mixed framework is globally determined by its active lengths, not
   merely infinitesimally rigid;
2. the signed support must contain one of two explicit parity minors.

The highest-value continuation is to test whether the forced signed minor can be
localized relative to the planar contact embedding and convex diameter thrackle. A
successful localization that forces a literal diameter triangle, a forbidden contact
triangle, or a finite same-diameter release would close C-II. A signed-minor argument
that uses arbitrary switching without recovering geometric edge types is insufficient.

## 8. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| Equality bar framework universally rigid | proved, conditional on audited ZR/ZF | Maximal-rank PSD stress plus ZF conic exclusion. |
| ZR stress has SAP | proved | Direct affine-kernel calculation plus ZF. |
| `nu(G,H)>=3` | proved | Definition of signed `nu`. |
| Forced `K_4^o` or `K_3^=` signed minor | proved | Arav--Hall--Li--van der Holst. |
| Actual packing tensegrity universally rigid | rejected | KKT stress has the wrong proper-stress signs for `contacts>=1`, `diameters<=D`. |
| Forced signed minor already gives a unit triangle | not proved | Signed minor operations lose literal geometric edge type. |

## 9. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

ZR + ZF imply two exact new facts for the nonisolated C-II core:

(1) Treat C union H as equality bars. Omega=L_C(alpha)-L_H(beta) is PSD of rank v-3,
and ZF excludes a conic at infinity. Hence the equality bar framework is superstable
and universally rigid.

(2) Omega has SAP. With contacts even and diameters odd, Omega is a PSD SAP matrix of
signed nullity 3. Therefore the mixed signed support contains a K_4^o or K_3^= signed
minor.

Do NOT apply tensegrity super-stability to the actual packing inequalities: contacts
are struts and diameters are cables, while the KKT weights have the opposite proper
signs.

Direct endpoint remains b+sum_F(deg F-4)>2h. Next: localize the forced signed minor
using the planar contact embedding / diameter thrackle, or return to the ZM mass lemma.
```
