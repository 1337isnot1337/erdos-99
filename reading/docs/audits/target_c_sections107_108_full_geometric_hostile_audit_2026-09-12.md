> Generated reading edition · [exact source](../../../docs/audits/target_c_sections107_108_full_geometric_hostile_audit_2026-09-12.md) · source SHA-256 `2099f2eb908877a4a7f62507ad6696cb240783bebf4351e87321737c51760b2d`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-CC0A8BDAD1CC","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — Sections 107–108 full geometric hostile audit

**Date:** 2026-09-12  
**Verdict:** **PASS as proof-only theorems.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This audit supplements the existing Sections 107–108 scalar/finite-count audit.  Its
scope is the proof-level geometry that the earlier audit explicitly left unresolved:

- the exact circular-segment decomposition for an arbitrary compact wrapping support;
- the majorization and gap-stability transfer on the `sigma<=10^-3` window;
- the finite carrier-area and rhombus-population transfer;
- the Section-108 stronger phase-shore extraction;
- reuse of the Section-104 macro/micro and tangent-window leakage lemmas on the wider
  window; and
- the final projective corridor/phase contradiction.

Both sections survive this review.  In particular the Section-108 proof-only carrier
coefficient

```math
\mu_{12}=0.9760418064930821\ldots
```

is supported by the stated inputs.  Neither section closes C-II.

## 1. Section 107: every complement gap is a minor gap

Let `S` be a compact wrapping subset of the radius-`1/2` circle and assume the pairwise
minor angular diameter is at most `theta<pi`.  Every connected component of
`T\S` is an open arc with endpoints in `S`.

A complement component cannot have length greater than `pi`: its complementary arc
would then be an open semicircle containing `S`, contradicting wrapping.  It cannot
have length exactly `pi`, because its two endpoints would be antipodal points of `S`,
contradicting the strict angular-diameter bound.  Hence every gap length satisfies

```math
0<g_j<\pi.
```

Since its endpoints are in `S`, their minor angular separation is exactly `g_j`, so
also `g_j<=theta`.

This validates the minor-segment convention used throughout Section 107.

## 2. Section 107: the circular-segment area identity is exact

For a gap `G_j` of angular length `g_j<pi`, let `c_j` be the chord joining its two
endpoints.  The open minor arc `G_j` contains no support point.  The remainder of the
circle lies in the closed half-plane opposite that minor arc across `c_j`; therefore
all of `S`, and hence `K=conv(S)`, lies on that opposite side.  Thus `c_j` is a
supporting chord of `K`, and the open circular segment between `G_j` and `c_j` is
outside `K`.

Distinct connected complement arcs are disjoint.  Their minor circular segments have
disjoint interiors as well: each is the convex cap on the side of its own supporting
chord containing that gap arc, and two such caps can meet only along boundary when the
arcs are disjoint.

Conversely take a point `z` in the radius-`1/2` disk but outside `K`.  Because `K` is
closed and convex, strictly separate `z` from `K` by a line.  Wrapping with
`theta<pi` implies `0` lies in the interior of `K`; therefore the side containing `z`
is a proper minor circular cap, with boundary arc of length below `pi`.  That boundary
arc contains no support point, so it lies in one connected component of `T\S`.
The separating cap is contained in the full segment over that component.  Hence every
point of the disk outside `K` belongs to one of the gap segments.

Therefore, up to boundary sets of zero area,

```math
B_{1/2}\setminus K
=\bigsqcup_j \operatorname{Seg}(G_j).
```

The area of a radius-`1/2` circular segment subtending angle `g` is

```math
{g-\sin g\over8}.
```

Countable additivity now gives the exact identity

```math
\boxed{
\operatorname{area}(K)
={\pi\over4}-{1\over8}\sum_j(g_j-\sin g_j).
}
```

No finite-support, smoothness, or finite-gap assumption is hidden in this step.

## 3. The superadditive tail estimate is valid for countably many gaps

Put

```math
G(x)={x-\sin x\over8}.
```

For `a,b>=0` with `a+b<=pi`,

```math
8(G(a+b)-G(a)-G(b))
=\sin a+\sin b-\sin(a+b)\ge0.
```

Thus `G` is superadditive on finite families whose total is at most `pi`.  Since
`G>=0` and is continuous, finite partial sums followed by monotone convergence yield

```math
\sum_kG(t_k)\le G\left(\sum_kt_k\right)
```

for countable families with total at most `pi`.

Section 107 applies this only to the tail whose total angular mass is at most
`q_*=0.00434...`, so the hypothesis has enormous margin.

## 4. Section 107 gap stability is independent of Sections 104–106

Canonical Sections 94, 100, and 101 provide

```math
M\le C\le2\alpha\le|S|\le U,
\qquad U-M=\sigma.
```

For `sigma<=10^-3`, every individual slack in this chain is at most `sigma`.  If the
largest gap is `g_1=theta-delta`, the same concave-majorization argument used at the
smaller Section-104 endpoint remains valid:

- if `delta>=0.1`, after discarding favorable extra complement mass while retaining
  three mandatory `phi` gaps, the extremal vector is
  `(theta-0.1,phi+0.1,phi,0,...)`, and its chord-sum cost exceeds `0.0326`, far above
  `10^-3`;
- for `0<=delta<=0.1`, the transfer derivative
  `f'(phi+delta)-f'(theta-delta)` remains greater than `0.30` over the full Section-107
  window.

Hence

```math
\delta\le{10\over3}\sigma.
```

Writing the next two principal gaps as `phi+x_2`, `phi+x_3` and the remaining tail
mass as `tau`, the exact total complement-mass identity gives

```math
x_2+x_3+\tau=\delta+e,
\qquad 0\le e\le\sigma,
```

so

```math
0\le x_2,x_3,\tau\le{13\over3}\sigma.
```

No statement from Sections 104–106 is required.

## 5. The Section-107 area floor follows from monotone worst-case enlargement

Throughout `sigma<=10^-3`, let `bar theta` be the unique solution of
`sigma(bar theta)=10^-3`, let `phi_8=2pi-2theta_8`, and put

```math
q_*={13\over3}10^{-3}.
```

The preceding bounds imply

```math
g_1\le\bar\theta,
\qquad
g_2,g_3\le\phi_8+q_*,
\qquad
\sum_{j\ge4}g_j\le q_*.
```

Because `G` is increasing on `[0,pi]` and superadditive on the tail,

```math
\sum_jG(g_j)
\le
G(\bar\theta)+2G(\phi_8+q_*)+G(q_*).
```

Substitution into the exact area identity yields

```math
\operatorname{area}(K)
\ge0.4731076260\ldots>0.473.
```

The inequalities are deliberately one-sided in the safe direction: each principal gap
is enlarged to its separate worst-case upper bound and all tail mass is concentrated
into one gap, which maximizes the superadditive segment-area loss.

## 6. Finite area and rhombus-count transfer are sound

For the normalized harmonic attachment cells, Hausdorff convergence of planar compact
convex bodies implies convergence of area.  Therefore

```math
D^{-2}\operatorname{area}(P_D)
\to\operatorname{area}(K)>0.473.
```

On a locally rhombus-saturated carrier,

```math
A_{4,D}/\operatorname{area}(P_D)\to1.
```

Every strict unit rhombus has area at most one, so if `R_D` is its count then

```math
R_D\ge A_{4,D}.
```

Consequently

```math
R_D\ge(0.473-o(1))D^2,
```

and the explicit finite constant `R_D>=0.472D^2` is valid after increasing the
large-`D` threshold.

This is the only Section-107 input used quantitatively by Section 108.

## 7. Section 108 stronger phase-shore extraction is correct

Under the common cap `mu_12`, canonical Section 103 selects the unique wrapping
macroscopic carrier; canonical Section 101 puts its angle in
`[theta_8,theta_12]`.  Since the corresponding scalar slack is at most `4.5e-5`,
Section 107 applies and supplies `R_D>=0.472D^2`.

The phase-circle cut removes only `O(D)` crossings, so at least `0.471D^2` remain for
large `D`.  With defect cutoff `K=1000`, the canonical global defect budget removes at
most

```math
5.317D/(1000/D)=0.005317D^2,
```

leaving at least `0.465683D^2` good crossings.  One of three unordered phase-label
pairs carries at least one third of them.  Random bins of width `20000/D` retain at
least `19/20` for one shift, yielding more than

```math
0.14746628D^2
```

internal-bin edges.

For one fixed label pair let `a_j,b_j` be the two shore sizes in a bin.  The local
train count gives

```math
\sum_j a_j,\sum_j b_j\le6D.
```

If every bin had `a_j<0.012D` or `b_j<0.012D`, bins small on the first shore would
carry at most `0.072D^2` crossing edges and the remaining bins, necessarily small on
the second shore, at most another `0.072D^2`.  Simplicity of the train-crossing graph
justifies `e_j<=a_jb_j`.  The resulting `0.144D^2` ceiling contradicts the retained
mass.

Thus a common inverse-phase bin has both shores of size at least `0.012D`; its width
is `O(1/D)`, and the two distinct labels give limiting projective directions exactly
`pi/3` apart.  Two physical ends per local train therefore give endpoint supply
`E_0=0.024` per `D` for each family.

## 8. The sharp macroscopic-route excess bound remains valid

For every fixed finite family of positive limit gaps, the exact Section-82 outer ledger
and two-edge baseline on all unselected intervals give

```math
\sum_{j\in J}\ell_j\le2\alpha.
```

Take the scale limit first, then exhaust the countable positive complement components.
Nonnegativity gives

```math
\sum_j\ell_j\le2\alpha.
```

Canonical Section 101 gives `C=sum_j sin(g_j/2)` and `2alpha-C<=sigma`; every selected
outer route dominates its endpoint chord.  Hence

```math
\boxed{
\sum_j(\ell_j-\sin(g_j/2))\le\sigma.
}
```

The three principal routes therefore have total normalized path excess at most
`sigma`.  This is the correct budget for Section 108's projection step.

## 9. The Section-104 leakage machinery is valid on the Section-108 window

The technical companion to Section 104 is scale-free once the following inputs hold:

1. `delta<=10sigma/3` and `x_2,x_3,tau<=13sigma/3`;
2. the two support spans adjacent to the largest gap are at most `delta`;
3. the main support region has one oriented tangent-direction lift with variation
   strictly below `pi`;
4. the ordered limit is `epsilon fixed -> D -> infinity -> epsilon ->0`.

Section 107 re-proves (1).  The Section-104 adjacent-span proof uses only the angular
diameter alternative and `tau<phi`; at `sigma<=4.5e-5`,
`tau<2e-4` while `phi` is about `0.877`, so (2) holds with large margin.
Removing the three principal gaps and those two tiny spans leaves the same main support
arc as at the Section-101 endpoint, perturbed by only `O(10^-4)` radians; its tangent
variation remains strictly below `pi`, proving (3).  The technical companion explicitly
uses the ordered finite-cover limit in (4), so no growing-gap classification is being
assumed.

Thus for any cutoff `h>0` the inherited leakage formula

```math
L(\sigma,h)
=w(h)+\left({1\over h}+{169\over6}\right)\sigma,
\qquad
w(h)=\pi/3-\arccos((1+h)/2),
```

continues to hold.

At `h=0.0088` and `sigma=4.5e-5`, the published value

```math
L=0.0114693143\ldots
```

is below the endpoint supply `0.024`.  After pigeonholing the three principal
corridors, `rho=0.00417` is a safe retained endpoint-density constant.

## 10. The final projective-direction contradiction is valid

Let one principal route carry at least `rho D` endpoint occurrences from a phase family
of limiting projective direction `u`, and let `q` be the projective chord direction.
The train direction is the direction of its physical terminal edge, so there is no
transverse/tangent convention mismatch.

Orient the route along its chord.  Each selected unit-edge occurrence contributes at
least

```math
1-\cos\Delta-o(1),
\qquad
\Delta=\operatorname{dist}_{RP^1}(u,q),
```

to path length minus chord projection.  Distinct selected trains supply distinct
physical endpoint occurrences.  The principal-route excess budget therefore gives

```math
\rho(1-\cos\Delta)\le\sigma.
```

At `rho=0.00417` and `sigma=4.5e-5`, exact cosine inversion gives

```math
\Delta=0.1470431\ldots .
```

The two selected phase families cannot use the same principal corridor because they
are exactly `pi/3` apart while `2Delta<pi/3`.  For two distinct selected corridors,
the projective triangle inequality would force

```math
\left|\operatorname{dist}_{RP^1}(q_i,q_j)-\pi/3\right|
<2\Delta<0.294087.
```

The gap-stability geometry gives the incompatible lower bound

```math
{\theta_8\over2}-{\pi\over3}-{73\over6}\sigma
=0.3037089\ldots .
```

The contradiction margin is positive by more than `0.00962` radians.

## 11. Disposition

Sections 107 and 108 survive full geometric hostile review.

The valid proof-only conclusions are:

```math
\boxed{
\sigma\le10^{-3}
\Longrightarrow
\operatorname{area}(P_{\rm wrap})>(0.473-o(1))D^2
}
```

for a locally rhombus-saturated wrapping carrier, and

```math
\boxed{
\operatorname{diam}(P_*)
\ge(0.9760418064930821\ldots-o(1))D
}
```

for some quadratic-area locally rhombus-saturated harmonic carrier in every sufficiently
large Type-II survivor.

These remain carrier/structure theorems.  They do not force an exact unit equilateral
triangle, do not construct a source-preserving strict sub-`D` deformation, and do not
settle the separate container branch.  C-II and LEVEL I remain open.

**Theorem state:** unchanged; this audit does not promote Sections 107–108.
