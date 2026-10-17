> Generated reading edition · [exact source](../../../docs/audits/target_c_section104_quantitative_phase_gap_hostile_audit_2026-09-12.md) · source SHA-256 `ea2272661d3facc5b5d4f51855503450bd587c2c0e63e359f4efac190fad02c2`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-1C23A892965C","canonical":true,"claim_ids":["C-WRAP-QUANT-PHASE-GAP"],"claim_statuses":{"C-WRAP-QUANT-PHASE-GAP":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C — Section 104 quantitative phase-gap hostile audit

**Date:** 2026-09-12
**Verdict:** **PASS as a proof-only theorem, conditional only on the canonical Section-103 input.**
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This audit checks
[`../targets/target-c/104-quantitative-phase-gap-audit.md`](../targets/target-c/104-quantitative-phase-gap-audit.md)
and its technical companion
[`../targets/target-c/quantitative-phase-gap-technical-audit-2026-09-12.md`](../targets/target-c/quantitative-phase-gap-technical-audit-2026-09-12.md)
against the canonical Section-101/102 chain and the independently audited Section-103
concentration theorem.

The claimed explicit threshold is

```math
\theta_9=2.7029080509166894011\ldots,
\qquad
\mu_9=\sin(\theta_9/2)
=0.9760407675809149535\ldots,
```

where

```math
\sigma(\theta_9)
:=3\theta_9-2\pi-\sin(\theta_9/2)-2\sin\theta_9
=10^{-7}.
```

Thus

```math
\boxed{
\mu_9-\mu_8=2.3138629714\ldots\times10^{-9}>0.
}
```

The theorem survives hostile review. The numerical gain is extremely small, but the
proof does not need an unproved continuity modulus: the constants close with visible
slack.

## 1. Scalar-slack decomposition is exact

For the unique wrapping carrier under the Section-103 common-cap contradiction, put

```math
M=\sin(\theta/2)+2\sin\theta,
\qquad
C=\sum_j\sin(g_j/2),
\qquad
U=3\theta-2\pi.
```

Canonical Sections 100–101 give

```math
M\le C\le2\alpha\le|S|\le U.
```

Therefore, if `sigma=U-M<=10^-7`, every successive nonnegative slack is individually
at most `sigma`:

```math
U-|S|,
\quad |S|-2\alpha,
\quad 2\alpha-C,
\quad C-M
\le\sigma.
```

There is no hidden cancellation in this step.

Also

```math
\sigma'(\theta)
=3-\frac12\cos(\theta/2)-2\cos\theta
\ge\frac{15}{4}
```

on the live interval, so

```math
0\le\theta-\theta_8
\le\frac{4}{15}\sigma
<2.7\times10^{-8}.
```

The accompanying scalar certificate reproduces the root and all numerical margins.

## 2. Complement-gap stability is valid

Let the positive complement gaps be sorted
`g_1>=g_2>=g_3>=...`. Canonical Section 94 gives three distinct gaps at least

```math
\phi=2\pi-2\theta,
```

and Section 100 gives

```math
\sum_jg_j
=2\pi-|S|
=\theta+2\phi+e,
\qquad 0\le e\le\sigma.
```

Write

```math
g_1=\theta-\delta.
```

For fixed `g_1`, after dropping the favorable extra mass `e`, concavity of
`f(x)=sin(x/2)` minimizes the remaining chord sum by concentrating the transferred
mass into one of the two mandatory `phi` gaps. Hence

```math
C-M
\ge
f(\theta-\delta)+f(\phi+\delta)-f(\theta)-f(\phi).
```

The coarse case `delta>=0.1` already costs more than `0.0326`. On
`0<=delta<=0.1`, the derivative of the right-hand side is uniformly greater than
`0.30`. Thus

```math
\boxed{
\delta\le\frac{10}{3}\sigma.
}
```

Writing

```math
g_2=\phi+x_2,
\qquad
g_3=\phi+x_3,
\qquad
\tau=\sum_{j\ge4}g_j,
```

the exact total-mass identity gives

```math
\boxed{
0\le x_2,x_3,\tau
\le\delta+e
\le\frac{13}{3}\sigma.
}
```

This is enough for every later stability estimate; no uniqueness of the tail-gap
layout is assumed.

## 3. The two spans adjacent to the largest gap are genuinely small

Orient the largest gap `G_1` from support endpoint `A` to support endpoint `B`. Let
`s_+` be the angular distance from `B` to the start of the next principal gap. If
`s_+>delta`, then the clockwise separation from `A` to that next principal endpoint
lies above `theta`. The minor-angle condition forces it onto the complementary branch,
so

```math
s_+\ge\phi+\delta.
```

Every offset in `(delta,phi+delta)` from `B` would then have clockwise separation from
`A` in the forbidden interval `(theta,2pi-theta)`. That open interval belongs to a
complement component of length at least `phi` distinct from the three principal gaps,
contradicting `tau<phi`.

Therefore

```math
\boxed{s_+,s_-\le\delta.}
```

The argument remains valid if tail gaps occur between principal gaps; `s_+` is an
angular span, not an assumption of connected support.

## 4. Principal corridor directions keep a fixed margin from pi/3

The projective direction of a circle chord is its angular midpoint plus `pi/2` modulo
`pi`. If

```math
g_1=\theta-\delta,
\qquad g_i=\phi+x_i\quad(i=2,3),
```

then the two projective separations involving `G_1` differ from `theta/2` by at most

```math
\frac32\delta+\frac12x_i
\le\frac{43}{6}\sigma.
```

For the `G_2/G_3` pair, using the total angular identity and the two adjacent-span
bounds gives deviation from `pi-theta` at most

```math
\frac72\delta+\frac12e
\le\frac{73}{6}\sigma.
```

At `theta_8`,

```math
\theta_8/2-\pi/3=0.3042564636\ldots,
```

while `pi-theta_8` lies still farther from `pi/3`. Hence for `sigma<=10^-7` every
pair of principal corridor directions stays more than `0.3042` radians away from the
required `pi/3` separation.

The constants displayed in Section 104 are therefore conservative.

## 5. The outer-ledger defect and route-slack bounds are correct

The finite Section-101 route inequality retains the nonnegative local currency:

```math
C
\le2\alpha-\limsup_D\frac{2s_D+c_D+Q_D}{D}
```

after passing to a subsequence on which the normalized defects converge. Therefore

```math
\boxed{
\limsup_D\frac{2s_D+c_D+Q_D}{D}\le\sigma.
}
```

In particular `c_D/D,Q_D/D<=sigma+o(1)`.

The tail chord sum obeys

```math
C_{tail}
=\sum_{j\ge4}\sin(g_j/2)
\le\tau/2
\le\frac{13}{6}\sigma.
```

For every fixed finite family of complement gaps, the exact Section-82 outer-face
identity plus the ordinary two-edge floor gives normalized selected-route length at
most `2alpha`. Taking increasing finite families only after the large-`D` limit yields

```math
L_{tail}
\le2\alpha-\sum_{i=1}^3\sin(g_i/2)
\le\sigma+C_{tail}
\le\frac{19}{6}\sigma,
```

and likewise

```math
\boxed{
\sum_{i=1}^3
(\ell_i-\sin(g_i/2))
\le\frac{19}{6}\sigma.
}
```

This is an occurrence-counted outer-walk statement, so bridges do not introduce a
missing factor.

## 6. The macro/micro limiting order is legitimate

The phrase “micro route” must be understood through the ordered limit in the technical
companion:

```text
fix epsilon > 0
 -> select the finitely many limit gaps of length >= epsilon
 -> D -> infinity
 -> epsilon -> 0.
```

For fixed `epsilon`, Hausdorff convergence pins both endpoints of each selected limit
gap and produces distinct finite consecutive-attachment intervals. All outer-ledger
inequalities are finite at this stage.

Only after taking the large-`D` limit is `epsilon` sent to zero. The omitted chord mass
is controlled monotonically by `C_tail`, and the omitted angular mass by `tau`.
Therefore Section 104 does not classify a growing number of finite gaps before taking
the scale limit.

With this interpretation the micro-route budget is valid:

- direct micro routes cost at most `c_D/D<=sigma`;
- non-direct micro-route excess above the two-edge baseline is at most `2sigma`;
- routes of length at least three then have total edge-occurrence density at most
  `6sigma`;
- length-two routes with a loaded middle vertex use loaded-loaded edges and cost at
  most `2sigma` occurrences.

Thus all micro-route edges outside regular two-edge unloaded-apex teeth have density at
most

```math
\boxed{9\sigma.}
```

## 7. The micro-base excess estimate is valid

Fix a finite open angular cover `U` of the compact support `S` with
`|U|<=|S|+epsilon`. For large `D`, every attachment angle lies in `U`. On each
component of `U`, the attachment-polygon chords between successive attachments are
bounded in total length by the corresponding force-hull boundary arclength. Canonical
Type-II annular geometry gives

```math
\operatorname{len}(\partial F_D\text{ over }U)
\le(D/2+o(D))|U|.
```

Only `O_U(1)` attachment sides cross between components. Since every source-source base
has length at least one,

```math
\limsup_D\frac1D
\sum_{\text{within-}U\text{ bases}}(|b|-1)
\le\frac{|S|+\epsilon}{2}-\alpha.
```

Shrink nested finite covers and then exhaust the positive complement components. By
nonnegativity this yields

```math
\boxed{
\limsup_D\frac1D
\sum_{\mathrm{micro\ bases}}(|b|-1)
\le\frac{|S|}{2}-\alpha
\le\frac\sigma2.
}
```

No equidistribution of attachment angles is used.

## 8. The convex tangent-window estimate is valid

After removing the three principal complement gaps and the two tiny spans adjacent to
`G_1`, the main support region has an oriented tangent lift of total variation below
`pi`.

For the normalized convex limit `K=conv(S)`, boundary in this region consists of
radius-`1/2` circular support arcs and chords across tail gaps. In an oriented tangent
window of width `w<pi`, the circle pieces contribute boundary length at most `w/2`.
Even if every tail chord falls in that window, their total length is at most
`C_tail`. Therefore

```math
\operatorname{len}(\partial K\text{ in a width-}w\text{ window})
\le w/2+C_{tail}.
```

For the finite convex attachment polygons, oriented side direction is monotone. Enlarge
the direction window slightly and cut by support lines at its endpoints. Hausdorff
convergence of planar convex bodies plus perimeter continuity for the resulting convex
subchains gives

```math
\limsup_D D^{-1}
\operatorname{len}(\text{finite bases in the window})
\le w/2+C_{tail}.
```

Since every base has length at least one, the same quantity bounds normalized base
count. This justifies equations (104.58)–(104.59) without assuming differentiability or
uniform finite curvature.

## 9. Section-90 phase-family sizes have no missing factor

The independently audited Section-103 constants permit

```math
R_D\ge0.18D^2,
\qquad T_D\le6D,
\qquad
\sum_R\delta_R<5.317D.
```

Canonical Section 90.3, before optional minimum-degree pruning, gives two fixed
phase-label shores in one inverse-diameter reduced-phase bin, each of size

```math
\alpha_0D,
\qquad
\alpha_0={0.18\over32\cdot6}
=0.0009375.
```

A full local train segment has exactly two distinct physical boundary ends, and a
physical rhombus-boundary edge is the end of only the train using that edge direction.
Hence each selected phase family supplies at least

```math
\boxed{E_0D=0.001875D}
```

physical endpoint occurrences. This is the larger pre-pruning shore count; Section 104
does not accidentally substitute the smaller Section-90.4 minimum-degree constant.

## 10. Leakage bookkeeping closes

For one selected phase family, endpoint occurrences away from the three principal
corridors are bounded by:

- nonquadrilateral bounded-face boundary: `5sigma`;
- nonprincipal macroscopic corridors: `19sigma/6`;
- exceptional micro routes: `9sigma`;
- teeth in the two tiny spans adjacent to `G_1`: `20sigma/3`;
- bad-base teeth with base excess `h=1/2000`: `sigma/h=2000sigma`;
- good-base teeth on the main region:
  
  ```math
  w_h+2C_{tail}
  \le w_h+13\sigma/3,
  ```

  where
  
  ```math
  w_h=\pi/3-\arccos((1+h)/2)<0.000289.
  ```


The total is

```math
\boxed{
 w_h+{12169\over6}\sigma<0.000492
}
```

at `sigma<=10^-7`. Subtracting from `E_0=0.001875` leaves more than
`0.001383D` endpoints on the three principal corridors. One principal corridor
therefore carries more than

```math
\rho D,
\qquad \rho=0.00045,
```

endpoints from that phase family.

The two leg choices on a regular tooth are already separated into two base-direction
windows, so no hidden factor of two remains in the good-base estimate.

## 11. Projection loss beats available route slack

Let `q` be the projective chord direction of a principal corridor and `u` the limiting
projective direction of a phase family that contributes at least `rho D` distinct
endpoint edges to that corridor. Orient the outer route along its chord. For each
selected endpoint edge `z`,

```math
1-q\cdot z\ge1-\cos\Delta,
\qquad
\Delta=\operatorname{dist}_{RP^1}(u,q).
```

The exact route projection identity

```math
\sum_e(1-q\cdot z_e)=\ell-d
```

and Step 5 give

```math
\rho(1-\cos\Delta)
\le{19\over6}\sigma.
```

Using `1-cos x>=2x^2/pi^2`, `rho=0.00045`, and `sigma<=10^-7` gives

```math
\boxed{\Delta<0.059.}
```

Each of the two phase families therefore selects a principal corridor within `0.059`
radians of its direction. They cannot select the same corridor because the phase
directions differ by `pi/3`. Hence two distinct principal corridors would have to be
within `0.118` radians of `pi/3` separation. Step 4 proves every principal pair is more
than `0.3042` radians from `pi/3`, a contradiction.

The projection comparison uses physical edge occurrences, exactly matching the
outer-walk multiplicity convention. A bridge can consume route length but cannot create
a false strict-rhombus train endpoint.

## 12. Final carrier transfer is correct

Assume every positive-area macroscopic harmonic-cell limit has diameter at most
`mu_9`. The audited Section-103 concentration theorem gives one unique wrapping carrier
with area above `0.19D^2`; canonical Section 101 puts its angular diameter in
`[theta_8,theta_9]`; Steps 1–11 give the contradiction.

Therefore some positive-area macroscopic limit has normalized diameter strictly above
`mu_9`. Canonical Section 83's finite-macroscopic-cell reduction yields an actual
locally rhombus-saturated carrier sequence with

```math
\boxed{
\operatorname{diam}(P_*)
\ge(0.9760407675809149535\ldots-o(1))D.
}
```

C-II remains open: the result is a local carrier bound, not yet a strict decrease of
the global minimizer diameter and not an exact unit equilateral triangle.

## 13. Required repository disposition

**PASS.** The theorem is suitable for promotion after Section 103 is canonical.

Before promotion:

1. rebase/sync the Section-104 branch on the canonical audit.43 state;
2. replace stale dependency prose saying “canonical Section 102/103” with their
   canonical audit.42/audit.43 status;
3. keep the technical companion non-numbered so there is only one Section-104 theorem
   module;
4. register the scalar certificate and this hostile audit in the theorem-state
   transaction;
5. do not describe the gain as `1e-8`: the proved coefficient gain is
   `2.3138629714...e-9`.

No stronger numerical threshold is certified by this audit.
