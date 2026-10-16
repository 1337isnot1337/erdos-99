<!-- theorem-state: {"artifact_id":"ART-A50582E7EE36","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C: Robinson-kernel localization

**Date:** 2026-08-31  
**Repository base:** `adbfe102` (main after C54 / PR #56)  
**Run type:** exact equality-kernel classification  
**Target:** Target C Gate C-I  
**Depends on:** C53 arbitrary-thrackle contraction, C54 null-face selection

## LEVEL I STATUS

**STILL OPEN.**

C53 proves selected-stress PSD and C54 reduces the second-order obstruction to a
stress-kernel problem. This report classifies that kernel far enough to localize every
possible nonconstant diameter angular rate.

After passing to consecutive projective diameter-direction gaps, the C53 weighted
Robinson defect becomes a singular `M`-matrix with a strictly positive nullvector.
Its irreducible components are contiguous intervals. Scalar stress-kernel functions
are piecewise affine in the ordered diameter slope. Requiring both coordinate
components of a tangential diameter velocity to lie in the stress kernel forces the
angular rate to be constant on every component containing at least two consecutive
direction gaps.

Therefore a genuine diameter shear can occur only across an **isolated one-gap
component** of the Robinson transform. Such a gap has an exact split-cone signature:
any positive Kalmanson interval split that distinguishes the two adjacent diameter
edges is supported on those two edge coordinates only.

The remaining C-I problem is now a concrete electrical-hinge exclusion.

## 1. C53 edge-space setup

Fix a normalized two-dimensional KKT stress and use the C53 projective edge order

\[
e_0<e_1<\cdots<e_{m-1}.
\]

Choose Euclidean axes so every oriented diameter vector has positive first coordinate,

\[
u_i=a_i(1,t_i),
\qquad
a_i>0,
\qquad
t_0<t_1<\cdots<t_{m-1}.
\tag{C55.1}
\]

Let

\[
\gamma_i=a_i\beta_i,
\qquad
\Gamma=\operatorname{diag}(\gamma_i),
\]

and let `M` be the C53 scaled edge defect. Then

\[
M\succeq0,
\qquad
M\mathbf1=0,
\qquad
Mt=0,
\tag{C55.2}
\]

and for `i!=j`,

\[
M_{ij}=-\gamma_i\gamma_jK_{ij},
\tag{C55.3}
\]

where `K` is Robinson:

\[
K_{ik}\le\min(K_{ij},K_{jk})
\qquad(i<j<k).
\tag{C55.4}
\]

## 2. Difference-space transform

Let `D` be the `(m-1) x m` first-difference matrix,

\[
(Dx)_i=x_{i+1}-x_i,
\]

and let `T` be the cumulative right inverse

\[
(Ty)_0=0,
\qquad
(Ty)_r=\sum_{h<r}y_h.
\]

Thus

\[
DT=I,
\qquad
TDx=x-x_0\mathbf1.
\tag{C55.5}
\]

Define

\[
C=D\Gamma^{-1}D^{\mathsf T},
\qquad
G=T^{\mathsf T}MT,
\qquad
H=D\Gamma^{-1}MT.
\tag{C55.6}
\]

Because `M1=0`,

\[
M=D^{\mathsf T}GD,
\qquad
H=CG.
\tag{C55.7}
\]

Here `C` is positive definite and `G` is symmetric positive semidefinite. Hence `H`
has real nonnegative spectrum, with

\[
\ker H=\ker G.
\tag{C55.8}
\]

Put

\[
y=Dt,
\qquad y_i=t_{i+1}-t_i>0.
\]

Then `Mt=0` gives

\[
Hy=0.
\tag{C55.9}
\]

The C52 weighted-Fiedler calculation applies verbatim. For `k<i`,

\[
H_{ik}
=-\sum_{r\le k}\gamma_r(K_{ri}-K_{r,i+1})\le0,
\tag{C55.10}
\]

and for `k>i`,

\[
H_{ik}
=\sum_{r>k}\gamma_r(K_{ir}-K_{i+1,r})\le0.
\tag{C55.11}
\]

Thus `H` is a singular `Z`-matrix with a strictly positive right nullvector.

## 3. Positive left nullvector and block decomposition

Since `C` is a tridiagonal positive-definite `M`-matrix, its inverse is entrywise
strictly positive. Set

\[
\ell=C^{-1}y>0.
\tag{C55.12}
\]

Then

\[
H^{\mathsf T}\ell
=GC\ell
=Gy
=0.
\tag{C55.13}
\]

Scale the columns by the positive right nullvector:

\[
\mathcal L=H\operatorname{diag}(y).
\tag{C55.14}
\]

Its off-diagonal entries are nonpositive and its row sums vanish. Therefore
`-mathcal L` is the generator of a finite directed continuous-time Markov chain.
Equation (C55.13) supplies a strictly positive stationary left vector after the same
positive scaling.

A finite directed generator with positive stationary mass on every state has no
transient strongly connected component. If its condensation graph had an edge,
choose a source component with an outgoing edge. It has no incoming flow and strictly
positive outgoing stationary flow, contradicting stationarity of the total mass of
that component. Hence the condensation graph has no edges.

Therefore the negative-off-diagonal graph of `H` is a disjoint union of irreducible
blocks, with no off-block entries.

The Robinson formulas make each block contiguous. Indeed, if `i<k` and
`H_ik<0`, then for every `i<j<k`, (C55.11) for column `j` contains every summand
present for column `k` plus additional nonpositive summands, so

\[
H_{ij}<0.
\tag{C55.15}
\]

The analogous statement holds to the left using (C55.10). Thus an edge in the
off-diagonal graph joins all intermediate indices into the same component. Every
irreducible component is an interval of consecutive gap indices.

Write these blocks as

\[
I_1,\ldots,I_r,
\qquad
\{0,\ldots,m-2\}=I_1\sqcup\cdots\sqcup I_r,
\tag{C55.16}
\]

with each `I_a` a consecutive interval.

## 4. Scalar kernel functions are piecewise affine in slope

### Theorem C55.1

For a scalar vector `x in R^m`,

\[
Mx=0
\]

if and only if, on every gap block `I_a`, there is a scalar `c_a` such that

\[
\boxed{
x_{i+1}-x_i=c_a(t_{i+1}-t_i)
\quad(i\in I_a).}
\tag{C55.17}
\]

Equivalently, `x` is a continuous piecewise-affine function of the ordered sample
points `t_i`, with possible slope changes only between Robinson blocks.

#### Proof

If `Mx=0`, then by (C55.5)

\[
H(Dx)=D\Gamma^{-1}Mx=0.
\]

Conversely, if `H(Dx)=0`, then `D Gamma^{-1}Mx=0`, so
`Gamma^{-1}Mx=c1` for some scalar `c`. Since `1^T Mx=0`,

\[
0=c\sum_i\gamma_i,
\]

hence `c=0` and `Mx=0`.

On each irreducible block, the singular `M`-matrix `H[I_a,I_a]` has a
one-dimensional right kernel by Perron-Frobenius. Its positive kernel vector is the
restriction of `y=Dt`. Hence

\[
(Dx)_i=c_a y_i
\quad(i\in I_a),
\]

which is exactly (C55.17). `square`

## 5. Angular shear can live only on singleton gap blocks

Let a vector velocity field `v` lie in the full selected stress kernel,

\[
\Omega_sV_x=\Omega_sV_y=0,
\tag{C55.18}
\]

and suppose, as for every fixed-diameter critical velocity, that every positive
diameter edge has zero radial first variation. Thus

\[
v_{a_i}-v_{b_i}
=\omega_iJ u_i
=\omega_i a_i(-t_i,1).
\tag{C55.19}
\]

Schur equality and the C53 edge reduction imply that the normalized diameter-edge
differences of each scalar velocity coordinate lie in `ker M`. Explicitly,

\[
\omega=(\omega_i)_{i=0}^{m-1}\in\ker M,
\qquad
(t_i\omega_i)_{i=0}^{m-1}\in\ker M.
\tag{C55.20}
\]

(The first vector comes from the second Euclidean velocity coordinate and the second,
up to a harmless sign, from the first.)

### Theorem C55.2 (kernel localization of diameter shear)

On every Robinson block `I_a` containing at least two consecutive gap indices,

\[
\boxed{
\omega_i=\omega_{i+1}
\quad\text{for every }i\in I_a.
}
\tag{C55.21}
\]

Consequently, if the angular-rate vector is nonconstant, at least one irreducible
component of `H` is a singleton gap `{i}`.

#### Proof

By C55.1, on a block `I_a` the samples `omega_i` are affine in `t_i`:

\[
\omega_i=c_at_i+d_a
\]

through all vertices incident to the gaps in that block. The second vector in
(C55.20) must also be affine in `t` on the same block. Its values are

\[
t_i\omega_i=c_at_i^2+d_at_i.
\]

If the block contains two consecutive gaps, it contains at least three strictly
ordered sample points. A quadratic polynomial agrees with an affine function at
three distinct points only if its quadratic coefficient is zero. Thus `c_a=0`, and
`omega` is constant across every gap in that block. `square`

Since the blocks partition every consecutive direction gap, a nonconstant angular
rate is therefore supported entirely on singleton gap components.

## 6. Exact split-cone signature of an isolated gap

Suppose `{i}` is a singleton component. Then

\[
H_{ik}=0
\qquad(k\ne i).
\tag{C55.22}
\]

Write the C50 Kalmanson decomposition in edge space as

\[
K=\sum_A\lambda_A z_Az_A^{\mathsf T}
\quad\text{modulo the annihilated sum-matrix part},
\qquad
\lambda_A\ge0.
\tag{C55.23}
\]

For one split vector `z`, its contribution to (C55.10), for `k<i`, is

\[
-(z_i-z_{i+1})\sum_{r\le k}\gamma_rz_r,
\tag{C55.24}
\]

and its contribution to (C55.11), for `k>i`, is

\[
(z_i-z_{i+1})\sum_{r>k}\gamma_rz_r.
\tag{C55.25}
\]

The C53 interval-sign lemma makes every contribution in (C55.24)-(C55.25)
nonpositive. Since their nonnegative split-weighted sum is zero at an isolated gap,
every positive split contributes zero separately.

If `lambda_A>0` and `z_i!=z_{i+1}`, equations (C55.24) for all `k<i` give

\[
\sum_{r\le k}\gamma_rz_r=0
\qquad(k<i).
\]

Taking consecutive differences and using `gamma_r>0` yields

\[
z_r=0\qquad(r<i).
\]

Likewise (C55.25) for all `k>i+1` gives

\[
z_r=0\qquad(r>i+1).
\]

Hence:

### Theorem C55.3 (two-edge split localization)

If `{i}` is an isolated Robinson gap, then every positive Kalmanson interval split
that distinguishes the adjacent diameter edges `e_i,e_{i+1}` satisfies

\[
\boxed{
\operatorname{supp}z_A\subseteq\{i,i+1\}.
}
\tag{C55.26}
\]

Thus the electrical response can distinguish the two angular sectors only through
interval splits that see no other positive diameter edge.

## 7. Exact C-I effect

Combine C54 with C55. If a weak contact survives, choose a relative-interior
weak-release flex and a null-face stress annihilating it. Any nonconstant angular rate
on the selected positive diameter support must cross an isolated Robinson gap. At
that gap the entire positive Kalmanson split support that distinguishes the two
adjacent diameter edges is confined to those two coordinates.

Therefore the former broad kernel-rigidity problem has become:

> **C56 electrical-hinge exclusion.** Show that the actual connected positive
> unit-contact network of a sufficiently large triangle-free global minimizer cannot
> have an isolated Robinson direction gap of the form (C55.26) for a null-face KKT
> stress carrying a genuine strong-diameter shear.

A proof may proceed by converting (C55.26) into a one- or two-vertex terminal
separator, or by showing that the isolated sector is a finitely integrable hinge and
therefore releases the weak contacts directly.

## 8. Regressions and scope

- If `M=0`, every direction gap is isolated. C55 correctly gives no angular rigidity;
  this is the full electrical-equality boundary and must be handled structurally.
- A block containing one gap has only two slope samples, so the product argument
  cannot force a constant angular rate there. This is a genuine algebraic limitation,
  not a proof artifact.
- C55 does not infer a quantitative spectral gap or conductance lower bound.
- The near-star C-II regression remains compatible: C55 is an exact zero-pattern
  theorem, not a numerical minor estimate.

## 9. Verification

- The factorization `H=CG` was checked algebraically from `DT=I`, `TD=I-1e_0^T`,
  and `M1=0`.
- The off-diagonal formulas are the exact C52 weighted-Fiedler formulas.
- Positive left and right nullvectors make the reducible `Z`-matrix decomposition an
  elementary finite Markov-chain argument; no irreducibility is assumed.
- The angular product step uses three distinct slope samples and therefore treats
  singleton blocks separately rather than silently discarding them.

## 10. Compact handoff

**LEVEL I STATUS:** still open.

**C55.1:** scalar C53 stress-kernel functions are piecewise affine in projective
diameter slope, on contiguous irreducible blocks of the difference-space singular
`M`-matrix.

**C55.2:** for a tangential diameter velocity in the full stress kernel, both
`omega` and `t omega` lie in the edge kernel. Hence `omega` is constant on every
block with at least two consecutive gaps. Nontrivial shear requires an isolated
one-gap block.

**C55.3:** at an isolated gap, every positive Kalmanson interval split that
distinguishes the adjacent diameter edges is supported on those two edge coordinates
only.

**Next:** exclude or finitely integrate this two-edge electrical hinge.
