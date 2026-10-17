> Generated reading edition · [exact source](../../research/target_c_shallow_tooth_apex_injectivity_2026-09-14.md) · source SHA-256 `c4461ce299696b4c57c94d518374fc82c7966b9e610a4e749757d855cb058877`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "3f16e495d3056c6baee11d4b122834d42777c50f", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_shallow_tooth_apex_injectivity_2026-09-14.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "c092e0ece089e12e595a7ca684e3877425aacc37541555cdade9e8d9bf65b2d6"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — shallow-tooth apex injectivity

**Date:** 2026-09-14  
**Repository base:** `815c8b6ce3c4d8ce1b5c256f384e85811e25f995`  
**Status:** proved proof-only strengthening of the shallow-tooth branch; theorem-state authority unchanged  
**Scope:** Type-II two-edge tooth branch; numerical corollary uses the current AG42/§171 low-`t` floor  
**LEVEL I STATUS:** `STILL OPEN`

The preceding shallow-tooth penetration theorem proves that one unloaded apex supports
at most two sufficiently shallow outer teeth. Convexity of the loaded force hull
removes the remaining factor two: in fact one apex supports at most one shallow outer
tooth under the same angular hypothesis.

This doubles the certified population of distinct shallow apices and doubles the
resulting distinct inward-penetration edge floor.

## 1. Setup

Let an `eta`-shallow two-edge outer tooth have loaded base endpoints `a,b`, unloaded
apex `x`, and

```math
|a-x|=|b-x|=1,
\qquad
|a-b|\ge 2-\eta.
```

Put

```math
\alpha_\eta:=\arccos(1-\eta/2).
```

As in the preceding penetration theorem, the smaller central angle at `x` between the
base endpoints is at least

```math
\pi-2\alpha_\eta.
\tag{AI.1}
```

Every contact neighbor of `x` lies on the unit circle centered at `x`. Unit separation
of the source implies that any two such neighbor directions have circular separation
at least `pi/3`.

Assume throughout

```math
\boxed{\alpha_\eta<\pi/12.}
\tag{AI.2}
```

This is the same hypothesis used in the preceding theorem.

## 2. One apex cannot support two shallow teeth

### Lemma AI.1 — shallow-tooth apex injectivity

Under (AI.2), one unloaded apex `x` is the apex of at most one `eta`-shallow outer
tooth.

### Proof

Suppose two distinct shallow teeth have the same apex `x`.

First suppose their loaded base pairs share one endpoint `a`. For a shallow tooth,
any possible partner of `a` lies in the arc of angular radius `2 alpha_eta` centered
at the antipodal direction to `a`. That partner arc has total width

```math
4\alpha_\eta<\pi/3.
```

Two distinct contact neighbors cannot both lie in such an arc, because their mutual
angular separation is at least `pi/3`. Hence two shallow base pairs through `x` cannot
share a loaded endpoint.

The two hypothetical bases therefore have four distinct loaded endpoints on the unit
circle about `x`. Both bases are edges of the same convex loaded force hull `F`.
Distinct convex-hull edges do not cross in their relative interiors, so the endpoint
pairs do not alternate around the circle.

After cyclic relabeling, the four endpoint directions occur as

```math
a,b,c,d
```

with base pairs `ab` and `cd`. Let the four consecutive angular gaps be
`g_ab,g_bc,g_cd,g_da`. Unit separation gives

```math
g_{ab},g_{bc},g_{cd},g_{da}\ge\pi/3.
\tag{AI.3}
```

Since the other three gaps already sum to at least `pi`, each one of the four gaps is
at most `pi`. Thus the smaller central angles for the two base pairs are exactly
`g_ab` and `g_cd`. By (AI.1),

```math
g_{ab},g_{cd}\ge\pi-2\alpha_\eta.
```

Therefore

```math
\begin{aligned}
2\pi
&=g_{ab}+g_{bc}+g_{cd}+g_{da}\\
&\ge 2(\pi-2\alpha_\eta)+{2\pi\over3}.
\end{aligned}
```

But (AI.2) implies the right side is strictly larger than `2pi`. Contradiction.

Hence one apex supports at most one `eta`-shallow outer tooth. QED.

The proof actually needs only `alpha_eta<pi/6` in the disjoint-endpoint case; the
stronger `pi/12` condition is needed only for the shared-endpoint exclusion and is
already the standing shallow-tooth hypothesis.

## 3. Improved penetration-edge count

Let `N_sh(eta)` be the number of `eta`-shallow two-edge teeth and let `d_out` be the
metric outer detour. The preceding exact detour count gives

```math
N_{sh}(\eta)\ge N_2-{d_{out}\over\eta}.
\tag{AI.4}
```

Lemma AI.1 says these teeth have pairwise distinct apices. Therefore the number of
distinct shallow apices is at least `N_sh(eta)`, not merely `N_sh(eta)/2`.

At every such apex, canonical contact degree and triangle-freeness give an extra unit
contact whose inward component relative to the shallow base is greater than

```math
Y_\eta:=\sin(\pi/3-\alpha_\eta).
\tag{AI.5}
```

Choose one such extra contact at every shallow apex. One undirected contact edge can
be selected by at most its two endpoints. Hence the number `E_pen(eta)` of distinct
selected penetration contacts satisfies

```math
\boxed{
E_{pen}(\eta)
\ge {N_{sh}(\eta)\over2}
\ge {1\over2}\left(N_2-{d_{out}\over\eta}\right).
}
\tag{AI.6}
```

This improves the preceding factor `1/4` to `1/2` without any new stress-weight or
area hypothesis.

## 4. Current low-`t` numerical corollary

At the present proof-only floor

```math
t_{42}=C_{146}+0.0013751,
```

the low-`t` squeeze gives

```math
{d_{out}\over D}\le0.002883975+o(1),
```

while the tooth alternative gives

```math
{N_2\over D}\ge
0.4363893718701161781\ldots-o(1).
```

Choose the exact convenient value

```math
\eta={1\over15}.
```

Then

```math
\cos\alpha_\eta={29\over30}>\cos(\pi/12),
```

so (AI.2) holds. Equation (AI.4) gives

```math
\boxed{
{N_{sh}(1/15)\over D}
\ge0.3931297468701161781\ldots-o(1).
}
\tag{AI.7}
```

All these shallow teeth have distinct unloaded apices. Equation (AI.6) then gives

```math
\boxed{
{E_{pen}(1/15)\over D}
\ge0.1965648734350580890\ldots-o(1).
}
\tag{AI.8}
```

The inward normal component is explicitly

```math
\boxed{
Y_{1/15}
={29\sqrt3-\sqrt{59}\over60}
=0.7091387945271472222\ldots .
}
\tag{AI.9}
```

Thus the tooth branch now forces almost `0.197D` distinct physical unit contacts with
a uniformly large inward component, rather than the previous `0.073D` certificate.

## 5. Frontier effect

The low-`t` tooth branch now has the source-level form

```text
N_2 >= 0.436389 D
+ d_out <= 0.002884 D
 -> N_sh(1/15) >= 0.393129 D
 -> the shallow-tooth apex map is injective
 -> E_pen >= 0.196564 D distinct inward unit contacts
 -> every selected contact has inward component > 0.709138.
```

This still does not close C-II: no positive KKT-weight floor for these contacts is
available. Its value is that the penetration population is now large enough that a
weight-free incidence, phase-boundary, or simultaneous-shear theorem can lose a
substantial constant factor and still remain linear.

The separate rounded-long-side branch remains to be converted into equally physical
contact geometry.

## 6. Reproducibility

Run

```bash
python3 research/verify_target_c_shallow_tooth_apex_injectivity.py
```

for the Decimal certificate.
