<!-- theorem-state: {"artifact_id":"ART-5DBAB6192F79","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C selected-stress Kalmanson lemma for the regular six-endpoint matching

**Date:** 2026-08-31
**Repository state:** `c116a10` (`research/target-c-promote-c30-c32-2026-08-31`)
**Run type:** exact response inequality / C-I subcase
**Target:** Target C Gate C-I, six-endpoint three-diameter matching
**Depends on:** promoted C11 response identity, promoted C30 response-inertia budget,
and the circular-planar resistance theorem cited below
**Arithmetic:** exact symbolic elimination

## LEVEL I STATUS

`STILL OPEN`

This addendum closes the six-endpoint response inequality when the force hull is a
regular hexagon and the three positive diameter edges are its opposite pairs. It does
not claim that an arbitrary convex six-endpoint matching is regular.

Let \(B=(p_0,\ldots,p_5)\) be a regular hexagon in cyclic order and let

\[
H_s=\{03,14,25\},
\qquad
\beta_{03}=a,\quad \beta_{14}=u,\quad \beta_{25}=v,
\qquad a+u+v=1,
\tag{RH.1}
\]

with \(a,u,v>0\). Let \(\Lambda\) be the positive contact Dirichlet response on
\(B\), arising from a connected circular-planar positive-conductance network with
the boundary order \(0,1,\ldots,5\), and assume the C11 affine response identity

\[
\Lambda P_B=L_{H_s}P_B.
\tag{RH.2}
\]

Then, writing \(R=\Lambda^+\) and

\[
W_{ij}=R_{ii}+R_{jj}-2R_{ij}
\tag{RH.3}
\]

for effective resistance, one has

\[
\boxed{
aW_{03}+uW_{14}+vW_{25}\le3.}
\tag{RH.4}
\]

For the C30 notation this is \(\rho_s\le 1\), and therefore

\[
\boxed{\Omega_s=L_{C_s}(\alpha)-L_{H_s}(\beta)\succeq0.}
\tag{RH.5}
\]

The proof uses the circular order essentially through Kalmanson inequalities.

## 1. Circular-planar input

For cyclic indices (i<j<k<\ell), define the two Kalmanson expressions

\[
\begin{aligned}
\mathcal K_1(i,j,k,\ell)
  &:=W_{ik}+W_{j\ell}-W_{ij}-W_{k\ell},\\
\mathcal K_2(i,j,k,\ell)
  &:=W_{ik}+W_{j\ell}-W_{i\ell}-W_{jk}.
\end{aligned}
\tag{RH.6}
\]

The literature input is the following exact necessary property:

> If \(\Lambda\) is the response matrix of a connected circular-planar electrical
> network, its effective-resistance matrix \(W\) obeys
> \(\mathcal K_1,\mathcal K_2\ge0\) for every cyclic quadruple.

This is Theorem 4.2 of Stefan Forcey, *Circular planar electrical networks, Split
systems, and Phylogenetic networks*, arXiv:2108.00550,
[https://arxiv.org/abs/2108.00550](https://arxiv.org/abs/2108.00550). The theorem's
network hypotheses match C11: a finite connected positive-conductance network with
the displayed boundary order. Only necessity is used here.

## 2. Exact algebraic certificate

Because the regular hexagon is centered, an invertible rescaling of its two coordinate
columns gives

\[
X=(2,1,-1,-2,-1,1)^{\mathsf T},qquad
Y=(0,1,1,0,-1,-1)^{\mathsf T}.
\tag{RH.7}
\]

The rescaling does not change (RH.2). Directly,

\[
L_{H_s}X=(4a,2u,-2v,-4a,-2u,2v)^{\mathsf T},
\tag{RH.8}
\]

and

\[
L_{H_s}Y=(0,2u,2v,0,-2u,-2v)^{\mathsf T}.
\tag{RH.9}
\]

Both coordinate columns are centered. Hence \(R\Lambda\) is the identity on their
span, and (RH.2) gives

\[
R L_{H_s}X=X,qquad R L_{H_s}Y=Y.
\tag{RH.10}
\]

Put

\[
N:=ua+v(1-v),qquad
\Delta:=a+u(u+v).
\tag{RH.11}
\]

Both \(N\) and \(\Delta\) are positive. Expanding \(W_{ij}\) from (RH.3), using
\(R\mathbf1=0\), and eliminating the two constant columns in (RH.10) gives the
following identity:

\[
\begin{aligned}
3-aW_{03}-uW_{14}-vW_{25}
={N\over2\Delta}\bigl(&
\mathcal K_2(0,1,2,5)
 +a\mathcal K_1(0,2,3,5)
 +a\mathcal K_1(0,3,4,5)\\
 &+u\mathcal K_2(1,2,3,5)
 +(1-v)\mathcal K_2(2,3,4,5)\bigr).
\end{aligned}
\tag{RH.12}
\]

For auditability, (RH.12) is a linear identity in the entries of \(R\): substitute
\(W_{ij}=R_{ii}+R_{jj}-2R_{ij}\), then use the twelve scalar equations in (RH.10)
and the six equations \(R\mathbf1=0\). No positivity or unlisted response property
is used in this elimination.

Every Kalmanson term on the right of (RH.12) is nonnegative, and every displayed
coefficient is nonnegative. Therefore (RH.4) follows. `\square`

## 3. Response-inertia consequence

The three opposite edges form a three-edge forest on six endpoints, and the regular
hexagon is two-dimensional. C30 says that the only possible non-affine negative mode
of \(\Omega_s\) is controlled by

\[
\rho_s=aW_{03}+uW_{14}+vW_{25}-2.
\tag{RH.13}
\]

Equation (RH.4) gives \(\rho_s\le1\). The C30 spectral alternative therefore yields
(RH.5). This is a genuine circular-planar closure of the six-endpoint regular
matching subcase; C33 shows why the circular-planar hypothesis cannot be omitted.

## 4. Equality and the exact remaining C-I boundary

Since \(a,u,v>0\), equality in (RH.4) forces all five Kalmanson expressions in
(RH.12) to vanish. This does not automatically give the exact affine kernel needed
for finite integration: C30 permits the equality case \(\rho_s=1\) with one additional
scalar kernel mode.

The equality branch is not removable from response theory alone. For example, attach a
single interior hub to each terminal \(i\) with conductance \(2\beta_i\), where

\[
\beta_0=\beta_3=a,qquad
\beta_1=\beta_4=u,qquad
\beta_2=\beta_5=v.
\]

The resulting circular-planar star response satisfies (RH.2), and its opposite-pair
effective resistances are \(W_{03}=1/a\), \(W_{14}=1/u\), and \(W_{25}=1/v\), so equality
holds in (RH.4). Thus connectedness and circular planarity do not by themselves
upgrade \(\rho_s\le1\) to \(\rho_s<1\).

If an additional source-specific argument supplies \(\rho_s<1\) for the
direction-dependent C13 stress, and if this regular matching is the full strong
diameter support, then C30 gives the exact affine kernel. The three matching directions
are distinct projective directions, so the symmetric part of the induced affine
velocity vanishes; subtracting the common rotation gives the C7 finite same-diameter
release and contradicts contact minimality.

## 5. Scope and classification

**Proved conditional C-I reduction.** The RH lemma proves the PSD response conclusion
for the regular-hexagon opposite matching using an exact circular-planar resistance
inequality. It does not prove the corresponding statement for an arbitrary convex
six-endpoint matching, does not exclude the equality/star response, and does not settle
C-I without the support-selection and equality-mode steps.

The live six-endpoint problem is therefore reduced to either:

1. a geometric theorem that rules out the regular-hexagon equality mode for an actual
   triangle-free unit-contact source; or
2. a direct extension of the Kalmanson certificate from the regular hexagon to every
   admissible convex diameter matching.
