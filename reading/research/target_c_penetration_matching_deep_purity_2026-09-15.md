> Generated reading edition · [exact source](../../research/target_c_penetration_matching_deep_purity_2026-09-15.md) · source SHA-256 `adecc44d05003ff4f8960172eea7425d62ddf0a851913aa8548cc0343a571a02`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 7 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "5138e7e7e75d1f14f6216001f5357a25c44a6a9f", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_penetration_matching_deep_purity_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "31e726334d17968a044955bf9b0dcec920b402ca522da6aecd47a1fc4a8d1a21"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — deep penetration endpoints are attachment-free internal vertices

**Date:** 2026-09-15  
**Status:** proof-only Type-II strengthening; theorem-state authority unchanged  
**Depends on:** the shallow-tooth penetration matching theorem and Section-124
fixed-scale loaded-hull flatness  
**LEVEL I STATUS:** `STILL OPEN`

The penetration matching theorem produces a distinct inner endpoint `w` for every
selected shallow tooth apex `x`. This note shows that `w` cannot have **any** loaded
contact neighbor. Hence each matched inner endpoint has full contact degree three to
five entirely inside its unloaded component.

At the current low-`t` floor and `eta=4/15`, the matching has size at least
`0.4255744656D-o(D)`. The two matching layers therefore force at least
`0.8511489312D-o(D)` distinct internal contact edges incident to them, and at least the
same number of loaded-to-unloaded tooth attachments.

---

## 1. Geometry of a matched endpoint

For one shallow tooth, use coordinates

```math
a=(-u,0),\qquad b=(u,0),\qquad x=(0,h),
```

with

```math
u=\cos\alpha,\qquad h=\sin\alpha,\qquad
0<\alpha\le\alpha_\eta<\pi/6.
\tag{DP.1}
```

Let `w` be its matched inner endpoint and write

```math
w-x=(r,v),\qquad r^2+v^2=1.
```

The audited shallow-tooth geometry gives

```math
v>\sin(\pi/3-\alpha),
\tag{DP.2}
```

so

```math
|r|<\cos(\pi/3-\alpha),
\tag{DP.3}
```

and

```math
\boxed{
\operatorname{depth}_{ab}(w)=h+v>\sqrt3/2.
}
\tag{DP.4}
```

---

## 2. Any loaded neighbor would lie beyond a base endpoint in tangent order

Suppose a loaded vertex `c` satisfies `|c-w|=1`.

First, `c` cannot equal `a` or `b`. If `c=a`, then

```math
|a-x|=|x-w|=|w-a|=1,
```

which is a forbidden unit equilateral triangle; similarly for `b`.

Also

```math
|c-a|\le |c-w|+|w-x|+|x-a|=3.
\tag{DP.5}
```

Thus `a,b,c` lie in one fixed-scale loaded-boundary window. Section-124 local flatness
puts all loaded-hull sides on the short boundary arc in an `o(1)` tangent cone around
the base direction `t`, with normal displacement `o(1)` from the base line.

Because `ab` is itself one global loaded-hull side and `c` is a distinct loaded-hull
vertex, convex cyclic order places `c` beyond `a` or beyond `b`. Every intervening
loaded-hull side has length at least one by source separation and tangent projection
`1-o(1)`. Therefore, with `M=(a+b)/2`,

```math
\boxed{
|t\cdot(c-M)|
\ge u+1-o(1).
}
\tag{DP.6}
```

The bound is asymptotically sharp when `c` is the loaded vertex immediately adjacent
to `a` or `b` beyond the tooth base.

---

## 3. The unit circle around the deep endpoint gives the opposite bound

The normal coordinate of `c` relative to the base line is `o(1)`, while (DP.4) puts
`w` at depth greater than `sqrt(3)/2`. Since `|c-w|=1`,

```math
|t\cdot(c-w)|<1/2+o(1).
\tag{DP.7}
```

Equation (DP.3) gives

```math
|t\cdot(w-M)|<\cos(\pi/3-\alpha).
\tag{DP.8}
```

Hence

```math
\boxed{
|t\cdot(c-M)|
<\cos(\pi/3-\alpha)+{1\over2}+o(1).
}
\tag{DP.9}
```

But for every `alpha<pi/6`,

```math
\cos\alpha+1
-
\left(\cos(\pi/3-\alpha)+{1\over2}\right)
=
{1\over2}+\cos\alpha-\cos(\pi/3-\alpha)
>{1\over2}.
\tag{DP.10}
```

For fixed `eta` this has a fixed positive lower bound. Equations (DP.6) and (DP.9)
therefore contradict one another for all sufficiently large `D`.

### Theorem DP.1 — deep endpoints have no loaded contacts

Every deep endpoint `w` of the shallow penetration matching has no contact edge to
`B_+`.

Because `w` is already known to be unloaded, all of its contacts lie inside its
unloaded component.

---

## 4. Degree and edge-incidence amplification

C26 gives every unloaded contact vertex full degree between three and five. By DP.1,
for every matched deep endpoint

```math
\boxed{3\le\deg_I(w)\le5.}
\tag{DP.11}
```

Let `M` be a penetration matching of size `Z`, with shallow endpoint set `X` and deep
endpoint set `W`. Then

```math
|X|=|W|=Z,
\qquad X\cap W=\varnothing.
\tag{DP.12}
```

Every `x in X` has at least its matched internal edge, so `deg_I(x)>=1`. Every
`w in W` has internal degree at least three. Therefore

```math
\sum_{v\in X\cup W}\deg_I(v)
\ge4Z.
\tag{DP.13}
```

Each physical internal contact edge contributes at most two incidences to this sum.
Hence the unloaded components containing the matching carry at least

```math
\boxed{2Z}
\tag{DP.14}
```

distinct internal contact edges incident to `X union W`.

Independently, every shallow tooth apex has exactly its two loaded base endpoints as
loaded contact neighbors. Different apexes give different physical attachment edges,
so the same matching components carry at least

```math
\boxed{2Z}
\tag{DP.15}
```

distinct loaded-to-unloaded contact edges incident to `X`.

The two edge classes are disjoint. Thus at least `4Z` distinct physical contacts are
incident to `X union W` when internal and loaded-to-unloaded contacts are combined.

---

## 5. Current low-`t` numbers at `eta=4/15`

The matching theorem gives

```math
{Z\over D}
\ge0.4255744656201161781\ldots-o(1).
\tag{DP.16}
```

Therefore

```math
\boxed{
{2Z\over D}
\ge0.8511489312402323562\ldots-o(1)
}
\tag{DP.17}
```

distinct internal contact edges are incident to matching endpoints, and at least the
same number of distinct loaded-to-unloaded tooth attachment edges occur.

Consequently the union of these two edge classes has size at least

```math
\boxed{
1.7022978624804647124\ldots D-o(D).
}
\tag{DP.18}
```

For `eta=4/15`,

```math
\sin\alpha_\eta={2\sqrt{14}\over15}
=0.4988876515698588514\ldots .
```

Thus every matched deep endpoint satisfies

```math
{\sqrt3\over2}
<\operatorname{depth}(w)
<1+{2\sqrt{14}\over15}+o(1),
\tag{DP.19}
```

so it lies in a fixed local shell between about `0.8660` and `1.4989` inside its tooth
support line.

The loaded-neighbor contradiction retains a fixed margin even at this widened
threshold:

```math
{1\over2}+{13\over15}-{13+2\sqrt{42}\over30}
=0.5012839534394759846\ldots .
\tag{DP.20}
```

---

## 6. A no-coalescence corollary for the entire shallow-apex layer

The proof of inner-endpoint injectivity in the matching theorem did not depend on which
extra contact was chosen. Hence:

> no unloaded vertex can be an extra contact neighbor of two distinct
> `eta`-shallow tooth apexes when `alpha_eta<pi/6`.

So every deep endpoint is adjacent to exactly one vertex of the shallow-apex class
through the selected penetration matching. Its other at least two internal incidences
cannot return to another shallow apex.

This matters for shell growth: the forced residual internal degree at the deep layer
cannot be absorbed by cross-linking the shallow layer.

---

## 7. Frontier effect

The tooth branch now carries a concrete two-layer contact structure:

```text
loaded hull
  |  two unit attachments per shallow apex
  v
X: >=0.4255744656 D distinct shallow unloaded apexes
  |  penetration matching
  v
W: >=0.4255744656 D distinct attachment-free unloaded vertices
   each with internal degree 3,4,or5
   and no second neighbor in the shallow-apex class
```

The deep layer therefore contributes at least two residual internal incidences per
matched vertex after the matching edge is removed. A valid next theorem should exploit
those residual contacts by a shell-growth or second-penetration argument rather than
seeking more first-layer edge count.

C-II remains open.
