> Generated reading edition · [exact source](../../../../docs/targets/target-c/57-zr-zf-rigidity-audit.md) · source SHA-256 `754086809cdfd077235829e3e7647f3163fd73d9bcdce925097cd1716743ed06`.
> [Current theorem state](../../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

# Target C — independent ZR/ZF rigidity audit

**Date:** 2026-09-11  
**LEVEL I STATUS:** **STILL OPEN.**  
**Disposition:** ZR/ZF certified and promoted as a load-bearing post-zero-transfer dependency.

This module closes a theorem-state registration gap. The September 11 audits of the
post-ZF scalar chains used the ZF ledgers, but the older Z/ZR/ZF campaign report was
still classified as unreviewed. The argument below independently checks the part of
that campaign needed by the promoted downstream theorems.

The proof uses the already-canonical C53/C63 restoration and the canonical zero-transfer
exclusion. It does not promote the rest of the old campaign report.

Throughout Sections 1--5, `V` is the **nonisolated positive-contact core** of the
lexicographically normalized source, `v=|V|`, `e` is the number of unit-contact edges
on that core, and `H` is the actual active diameter-edge set after weak diameter rows
have been removed. Every endpoint of an edge of `H` is loaded by a relative-interior
stress and therefore lies in `V`. Contact-isolated source points remain part of the
full global configuration, but they are not vertices of the stress matrix or mixed
rigidity matrix used below. No statement in this module bounds or deletes that isolated
source population.

## 1. C56 minimum-transfer dichotomy

For one relative-interior normalized KKT stress, orient the positive diameter edges in
strict projective order. With positive weights `gamma_i`, put

```math
M=\Gamma(B^{-1}-K)\Gamma,
\qquad M\mathbf 1=Mt=0,
```

where C53 gives `M>=0` and the Robinson inequalities for the symmetric transfer matrix
`K`. Let

```math
c=\min_{i\ne j}K_{ij}.
```

Set `A_ij=K_ij-c` off diagonal and let `L_A` be its weighted Laplacian. Then

```math
L_A=M-c(G\Gamma-\gamma\gamma^T).
```

After centering the strict slope vector `t`,

```math
L_A t^0=-cG\Gamma t^0.
```

Since `L_A` is positive semidefinite, `c<=0`.

If `c=0`, the zero energy of the strictly increasing vector forces every off-diagonal
`K_ij` to vanish. Hence `M=0` and `K=B^{-1}`: this is the zero-transfer phase.

If `c<0`, `t^0` attains the generalized Fiedler value `-cG`. The weighted Robinson
plateau argument is valid with arbitrary positive weights: a proper plateau forces equal
outside similarities, and the converse plateau lemma forces every Fiedler vector to be
constant on that interval. Thus a strictly increasing Fiedler vector makes this
eigenspace one-dimensional. Consequently

```math
\ker M=\operatorname{span}\{\mathbf1,t\}.
```

The delicate converse-plateau case is sound. If a plateau interval `J=[r,s]` has
endpoint similarity `alpha=A_rs`, irreducibility gives `alpha>0`. All common outside
similarities are at most `alpha`. If their weighted sum is strictly below its maximal
value, the one-vertex test vector has Rayleigh quotient below the internal plateau
mode. At equality all outside similarities equal `alpha`; because a Robinson matrix
with zero minimum has `A_{0,m-1}=0`, the complement of `J` has nonempty left and right
parts, and the left/right test vector has strictly smaller energy due to the zero
extreme similarity. This supplies the strict inequality required by the converse.

## 2. Zero transfer is unavailable

The canonical zero-transfer theorem gives, for the lexicographically normalized C-II
source with `D>=9`,

```math
\min_{e\ne f}K_{ef}<0.
```

Therefore the relative-interior stress is in the `c<0` branch above, not the
zero-transfer branch. Its edge defect has nullity exactly two.

## 3. ZR: scalar stress kernel has exactly the affine modes on the contact core

Work on the zero-sum terminal space. With `Q` the diameter incidence matrix and `B`
the positive diagonal diameter-weight matrix, put

```math
Y=\Lambda^{-1/2}QB^{1/2}.
```

The edge defect is congruent to

```math
I-Y^TY.
```

Its nullity is two by Section 1. Singular-value decomposition gives the same
multiplicity two for the zero eigenvalue of `I-YY^T`. Congruence then identifies the
terminal Schur defect

```math
\Lambda-L_H
```

as having exactly two zero modes on the zero-sum terminal space. Restoring constants
adds one kernel dimension.

The positive contact Laplacian on `V` has an invertible grounded interior block, so
Schur elimination preserves nullity. Hence the scalar signed stress matrix on the
nonisolated contact core satisfies

```math
\boxed{\ker\Omega_V=\operatorname{span}\{\mathbf1,P_x|_V,P_y|_V\}},
\qquad
\operatorname{rank}\Omega_V=v-3.
```

The three displayed vectors are already in the kernel by equilibrium and are
independent because the force hull is two-dimensional. Thus there are no additional
scalar zero modes **on `V`**. If the full source has contact-isolated points, extending
`Omega_V` to the full source by zero rows and columns adds the corresponding trivial
kernel directions. ZR does not exclude those directions and does not imply a bound on
the number of isolated source points.

## 4. ZF: the mixed active framework on the contact core is infinitesimally rigid

Choose a triangle-free global minimizer lexicographically: first minimize unit contacts,
then minimize actual diameter pairs. Let `u_V` be an arbitrary infinitesimal bar flex
of the mixed active contact/diameter framework on `V`. Extend it to a velocity `u` of
the full source by setting `u=0` at every contact-isolated source point. Those omitted
points are incident to no active unit-contact or diameter row, so all active first
variations remain zero. Every inactive pair involving an omitted point has strict
slack (`>1` for contact and `<D` for diameter). Thus the extended `u` is a legitimate
full-source critical velocity to which C63 applies.

C63 integrates `u` to nearby feasible configurations

```math
x(t)=tu+O(t^2).
```

Contact minimality removes weak contact rows. The identical finite argument applied to
diameter-pair count removes weak diameter rows. For sufficiently small `t`, inactive
pairs retain strict slack, so the integrated configuration preserves every active
contact and diameter length exactly.

Restrict the integrated motion to `V`. Pair the exact squared-length identities on
active rows with a relative-interior normalized KKT stress. Since
`Omega_V(P_x|_V)=Omega_V(P_y|_V)=0`, exact preservation gives

```math
x_1(t)|_V^T\Omega_V x_1(t)|_V+x_2(t)|_V^T\Omega_V x_2(t)|_V=0.
```

C53 gives `Omega_V>=0`. Divide by `t^2` and let `t->0`; both coordinate fields of
`u_V` lie in `ker Omega_V`. By ZR,

```math
(u_V)_i=b+A p_i\qquad(i\in V)
```

for one vector `b` and one `2x2` matrix `A`. No claim is made about arbitrary motions
of contact-isolated source points; they are absent from the mixed active framework.

Every active diameter row is strong, hence has zero radial first variation. For each
active diameter vector `r`,

```math
r^T(A+A^T)r=0.
```

There is no circular use of the ZF edge-count conclusion here. The earlier canonical
C34 boundary count gives

```math
q\ge {\lceil D\rceil+2\over2}.
```

Thus `D>=9` gives `q>=6` before ZF is invoked. Every loaded terminal is incident to at
least one active diameter edge, so an edge cover of the `q` loaded terminals contains at
least `ceil(q/2)>=3` diameter edges. Distinct length-`D` segments in a diameter-`D`
planar set have distinct projective directions. If two share an endpoint, collinearity
would either repeat the other endpoint or place the two other endpoints at distance
`2D`. If they are disjoint and parallel, resolving the displacement into components
parallel and perpendicular to the segments shows that one cross-endpoint distance is
strictly larger than `D` unless the segments coincide. Hence the quadratic form above
vanishes on at least three distinct projective directions.

A nonzero homogeneous quadratic in two variables has at most two projective zeros.
Therefore

```math
A+A^T=0.
```

So every mixed active bar flex **on `V`** is Euclidean. The mixed rigidity matrix on
`V` has rank

```math
\boxed{2v-3}.
```

The normalized KKT stress is a nonzero row dependence, therefore

```math
\boxed{e+h\ge2v-2}.
```

Combining this with Eppstein's triangle-free penny-graph bound for the contact core

```math
e\le2v-\delta-2
```

gives

```math
\boxed{h\ge\delta\ge\lceil D\rceil}.
```

This is the ZF input used by the later exact defect ledgers. It is a statement about
the nonisolated contact core, not a rigidity statement for the full source including
contact-isolated points.

## 5. Exact ledger consequence

Define on the nonisolated contact core

```math
r_E=2v-\delta-2-e\ge0,
\qquad
s_Z=e+h-(2v-2)\ge0.
```

Then, exactly,

```math
h=\delta+r_E+s_Z.
```

All subsequent ZE/ZT/PC/ZK bookkeeping is algebra from this identity, planar
Euler/face incidence, and the pinned-contact definitions. The independent PR #188
audit already rederived those ledger identities coefficient by coefficient using this
same core convention.

Accordingly the post-ZF scalar theorems may use ZF without an implicit unreviewed
premise. This promotion does not assert any control of the contact-isolated source
population and does not assert any of the unrelated train, bridge-dominance,
near-zero-response, or pure-rhombic conclusions from the old campaign report.
