> Generated reading edition · [exact source](../../../docs/audits/target_c_sections107_108_area_phase_audit_2026-09-12.md) · source SHA-256 `4abde4af5d6fc6d6f70e04432b30a91eebef31d5ed0db948ff112109d0c95edd`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-C7399F70F9B1","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — Sections 107–108 hostile area/phase audit

**Date:** 2026-09-12  
**Verdict:** **PASS as proof-only theorems.** The geometric, combinatorial, limit, and
numerical steps checked below are valid. C-II remains open and theorem state remains
`2026-09-12.audit.43` pending a separate promotion transaction.

The independently checked theorem sources are:

- `docs/targets/target-c/107-wrapping-support-area-rigidity-audit.md`;
- `docs/targets/target-c/108-area-boosted-quantitative-phase-gap-audit.md`.

The numerical regressions are:

- `research/verify_target_c_wrapping_support_area_rigidity.py`;
- `research/verify_target_c_area_boosted_phase_gap.py`.

This audit does not treat those scripts as proofs. The main purpose here is to verify
the steps that the scripts cannot certify: the circular-segment decomposition, the
wide-window gap majorization, the transfer from support area to rhombus mass, the
rerun of the Section-90 train extraction, countable route exhaustion, leakage
bookkeeping, projective/oriented direction handling, bridge multiplicity, and the final
compactness transfer.

## 1. Section 107 circular-segment decomposition

Let `S` be a compact wrapping subset of the radius-`1/2` circle, let
`K=conv(S)`, and let the connected components of the circle complement have angular
lengths `g_j`.

The claimed identity

```math
\operatorname{area}(K)
={\pi\over4}-{1\over8}\sum_j(g_j-\sin g_j)
```

is valid for arbitrary compact `S`, including infinitely many complement components.

### 1.1 Every complement gap has length below `pi`

Wrapping means the origin belongs to `conv(S)`. A complement gap longer than `pi`
would place all of `S` in the opposite open semicircle. A gap of length exactly `pi`
has antipodal endpoints in `S`; that contradicts the standing pairwise minor-angular
diameter bound `theta<pi`. Hence every `g_j<pi`.

Since the endpoints of a connected complement component belong to compact `S`, the
minor arc between those endpoints is exactly the empty gap. The endpoint chord is
therefore a supporting chord of `K`: the open minor arc lies on one side of the chord,
and every point of `S` lies on the opposite closed side.

### 1.2 The circular segments are exactly the disk outside `K`

The open circular segment between a gap and its endpoint chord is disjoint from `K`.
Distinct gap segments have disjoint interiors because their boundary arcs are disjoint
connected components of the circle complement.

Conversely, if `z` lies in the radius-`1/2` disk but outside `K`, strict convex
separation gives a line separating `z` from `K`. The cap containing `z` cannot contain
the disk center, because the center lies in `K`. Its boundary arc is therefore a minor
arc of length below `pi`, and it contains no point of `S`. That empty arc lies inside
one complement component of `S`; the corresponding small cap is contained in the full
circular segment cut off by that component. Thus `z` lies in one of the gap segments.

The disk-minus-`K` region is therefore, up to zero-area boundaries, the countable
disjoint union of these circular segments. A radius-`1/2` segment with angular width
`g` has area `(g-sin g)/8`, so countable additivity proves the identity.

No boundary smoothness, finite-gap assumption, or hidden cap theorem is used.

## 2. Section 107 wide-window complement-gap stability

Section 107 rederives rather than imports the Section-104 gap stability. This is
important because the window is enlarged from `sigma<=10^-7` to `sigma<=10^-3`.

Canonical Sections 94, 100, and 101 give

```math
M\le C\le2\alpha\le |S|\le U,
\qquad
\sigma=U-M,
```

and at least three distinct complement gaps of length at least
`phi=2pi-2theta`.

### 2.1 Largest gap

Writing `g_1=theta-delta`, the `delta>=0.1` barrier is valid. After decreasing excess
complement mass while preserving three gaps at least `phi`, the extremal vector

```math
(theta-0.1,\,phi+0.1,\,phi,0,\ldots)
```

majorizes every feasible competitor under the largest-coordinate cap. Concavity of
`f(x)=sin(x/2)` therefore gives the displayed lower bound for `C-M`, and the regression
checks that the barrier stays above `0.0326` throughout the `sigma<=10^-3` interval.
This is far larger than the allowed slack.

For `0<=delta<=0.1`, the transfer function

```math
h_theta(delta)=f(theta-delta)+f(phi+delta)-f(theta)-f(phi)
```

has derivative

```math
{1\over2}\left[
\cos{phi+delta\over2}-\cos{theta-delta\over2}
\right].
```

It decreases with `delta` and increases with `theta`, so its minimum on the relevant
rectangle occurs at `theta=theta_8, delta=0.1`. The independently recomputed minimum
is `0.3084268...>0.30`. Hence `delta<=(10/3)sigma`.

### 2.2 Remaining gaps

Writing

```math
g_2=phi+x_2,\qquad g_3=phi+x_3,\qquad
\tau=\sum_{j\ge4}g_j,
```

and `e=U-|S|`, the total complement measure gives the exact identity

```math
x_2+x_3+\tau=\delta+e.
```

All terms are nonnegative and `e<=sigma`, so

```math
0\le x_2,x_3,\tau\le {13\over3}\sigma.
```

There is no omitted finite-gap error in this identity.

## 3. Section 107 area floor and rhombus count

For

```math
G(x)={x-\sin x\over8},
```

`G` is increasing on `[0,pi]`, and

```math
G(a+b)-G(a)-G(b)
={\sin a+\sin b-\sin(a+b)\over8}\ge0
```

whenever `a,b>=0` and `a+b<=pi`. Thus the total tail-segment loss is maximized by
concentrating the tail angular mass: `sum_{j>=4}G(g_j)<=G(tau)`.

At `sigma=10^-3`, Section 107's monotone upper bounds on the three principal gaps and
tail mass therefore give

```math
\operatorname{area}(K)
\ge
{\pi\over4}-G(\bar\theta)-2G(\phi_8+q_*)-G(q_*)
=0.4731076260226828\ldots>0.473.
```

Independent recomputation also gives the exact endpoint value
`0.4735509805082776...`.

If `P_D/D` converges in Hausdorff distance to `K`, planar convex area continuity gives
`area(P_D)/D^2 -> area(K)`. Local rhombic saturation gives
`A_{4,D}=area(P_D)-o(D^2)`. Every strict unit rhombus has Euclidean area at most one,
so its count satisfies `R_D>=A_{4,D}`. Therefore

```math
R_D\ge(0.473-o(1))D^2,
```

and the conservative finite lower bound `R_D>=0.472D^2` is valid for all sufficiently
large members of the selected sequence.

**Section 107 verdict: PASS.**

## 4. Section 108 contradiction setup

Assume all positive-area macroscopic harmonic-cell limits have normalized diameter at
most `mu_12`. Canonical Section 103 then gives a unique wrapping macroscopic carrier.
Canonical Section 101 puts its angular diameter in
`[theta_8,theta_12]`, so its scalar slack is at most `4.5e-5`, well inside Section
107's `10^-3` area window.

The resulting `R_D>=0.472D^2` is compatible with the other local budgets used in
Section 108:

- Section 89 gives `T_D<=6a_D+O(1)`. Section 101 has
  `2a_D/D -> 2alpha<=|S|<=U`; on this tiny neighborhood `alpha<1`, so the coarse
  `T_D<=6D` used by Section 108 is safe after increasing the large-`D` threshold.
- Canonical Section 68 bounds total acute-angle defect over the entire source by
  `<5.317D`; restricting to one carrier only decreases the sum.

Thus the stronger area theorem can legitimately be fed into the canonical Section-90
local extraction without changing its hypotheses.

## 5. Section 108 stronger phase shores

After deleting the canonical `O(D)` phase-circle cut from at least `0.472D^2`
carrier crossings, the fixed lower bound `0.471D^2` is valid for sufficiently large
`D`.

With `K=1000`, the phase-defect budget permits at most
`0.005317D^2` nongood crossings, leaving at least `0.465683D^2`. One of the three
unordered phase-label pairs therefore supports at least one third of that mass.

Randomly shifted bins of width `20K/D` retain at least `19/20` of those good crossings
inside common bins. Hence internal-bin crossing density is at least

```math
{19\over20}{0.465683\over3}=0.1474662833\ldots .
```

For the fixed label pair, both total shores are bounded by the full train count `6D`.
If every bin had one shore below `0.012D`, bins small on the first shore contribute at
most `0.012*6 D^2=0.072D^2`; among all remaining bins, those small on the second shore
contribute another at most `0.072D^2`. This caps the total at `0.144D^2`, contradicting
the retained crossing mass.

Therefore one inverse-diameter phase bin has both shores at least `0.012D`. The bin
width is `O(1/D)`, so each shore has one limiting projective direction. Their fixed
distinct phase labels force projective separation exactly `pi/3` in the limit.

Each local train segment has exactly two physical boundary ends. Distinct local train
segments on one shore have distinct boundary-end occurrences, so each selected phase
family supplies at least `0.024D` physical endpoints. No complete-biclique theorem or
minimum-degree pruning is used.

## 6. Countable outer-route exhaustion

Section 108 correctly rederives the stronger route-excess budget instead of depending
on Sections 105 or 106.

For every fixed finite family `J` of positive complement gaps, the Section-82
outer-walk identity gives distinct occurrence subchains and

```math
\sum_{j\in J}\ell_j\le2\alpha.
```

Take a diagonal subsequence on which every fixed positive gap and its normalized route
length converge. Since route lengths are nonnegative, monotone exhaustion of the
countable complement components gives

```math
\sum_j\ell_j\le2\alpha.
```

Each route dominates its endpoint chord `f(g_j)=sin(g_j/2)`, and Section 101 gives
`C=sum_j f(g_j)` with `0<=2alpha-C<=sigma`. Therefore

```math
\sum_j(\ell_j-f(g_j))\le2\alpha-C\le\sigma.
```

This is an occurrence-walk statement. Bridge edges are counted with their outer-walk
multiplicity, exactly as in the canonical Section-82 ledger; no physical-edge
single-counting assumption is introduced.

## 7. Reuse of the Section-104 leakage theorem on the wider window

The Section-104 technical companion is scale-free once its gap-stability hypotheses
hold. Section 107 re-establishes those hypotheses with the same constants on the
`10^-3` window.

At Section 108's much smaller `sigma<=4.5e-5`:

- `delta<=(10/3)sigma<1.5e-4`, so the largest-gap local analysis is far inside its
  `delta<0.1` domain;
- the tail angular mass is at most `(13/3)sigma<2e-4`, vastly smaller than the
  principal gap `phi≈0.877`, so the adjacent-span/fourth-gap exclusion remains valid;
- the main support region still has oriented tangent variation below `pi`, so the
  projective-to-oriented lift used in the tangent-window estimate remains unique;
- the exact Section-82 slack bounds still give the same nonquadrilateral,
  nonprincipal-route, micro-route, and base-excess budgets;
- `h=0.0088` keeps good tooth bases in `[1,1+h]`, where the elementary tooth-angle
  formula and convex tangent-window bound apply without modification.

Thus one phase family has off-principal endpoint density at most

```math
L(\sigma,h)=
\left({\pi\over3}-\arccos{1+h\over2}\right)
+\left({1\over h}+{169\over6}\right)\sigma.
```

At `sigma=4.5e-5, h=0.0088`, this is
`0.0114693143423...`. Subtracting from the `0.024` endpoint supply and pigeonholing
among three principal corridors yields a valid fixed density `rho=0.00417` on one
principal corridor for each selected phase family.

## 8. Projection/orientation contradiction

Let a selected phase family of limiting projective direction `u` put at least
`rho D` physical endpoints on one principal corridor with projective chord direction
`q`.

The oriented-lift issue found during the Section-102 audit does not recur: on the
relevant main boundary region, convex side directions occupy one interval of length
below `pi`, so an `o(1)` projective phase window selects one consistent oriented lift.
If an endpoint edge is encountered with the opposite route orientation, its projection
loss is larger, not smaller.

Consequently every selected endpoint edge contributes at least
`1-cos Delta` to route-length minus chord projection, where
`Delta=dist_RP1(u,q)`. The total principal-route excess is at most `sigma D+o(D)`, so

```math
rho(1-\cos\Delta)\le\sigma.
```

At maximal slack and `rho=0.00417`, exact inversion gives
`Delta<=0.1470430677...`.

The two phase families cannot use the same principal corridor because their directions
are `pi/3` apart while `2Delta<pi/3`. Hence they use two distinct principal corridors,
whose projective separation must lie within `2Delta<0.294087` of `pi/3`.

The independently rederived gap stability gives, for every principal corridor pair,

```math
\left|dist_{RP^1}(q_i,q_j)-{\pi\over3}\right|
>
{\theta_8\over2}-{\pi\over3}-{73\over6}\sigma
=0.3037089636\ldots
```

at `sigma=4.5e-5`. The contradiction margin exceeds `0.00962` radians.

Independent arithmetic reproduces

```math
\theta_{12}=2.7029176003825128\ldots,
\qquad
\mu_{12}=0.9760418064930821\ldots .
```

## 9. Finite carrier transfer and scope

The contradiction excludes any full-core Type-II countersequence for which all
positive-area macroscopic harmonic-cell limits have normalized diameter at most
`mu_12`. The standard finite-macroscopic-cell compactness transfer therefore yields an
actual locally rhombus-saturated quadratic-area carrier with

```math
\operatorname{diam}(P_*)
\ge(0.9760418064930821\ldots-o(1))D.
```

Sections 105 and 106 are not logical premises: Section 108 rederives both the sharp
all-route excess bound and the stronger phase-shore extraction. They may remain
proof-only optimization waypoints without entering the canonical dependency graph.

Contact-isolated source points are unchanged, and bridge multiplicity is handled by the
outer-walk occurrence convention. No KKT coefficient lower bound, rejected Reuleaux
cap theorem, or external pseudosegment theorem is used.

**Section 108 verdict: PASS.**

## 10. What remains open

These theorems materially improve the full-core quantitative carrier bound, but they do
not settle C-II. They do not force an exact unit equilateral triangle, do not construct
a same-cardinality source of strict diameter below `D`, and do not resolve the separate
macroscopic inactive-container branch.

A theorem-state promotion, if performed, should therefore preserve **LEVEL I OPEN /
C-II OPEN** and should distinguish the explicit Section-108 coefficient from the
possibly stronger but nonnumerical strict gap already supplied by canonical Section
102.
