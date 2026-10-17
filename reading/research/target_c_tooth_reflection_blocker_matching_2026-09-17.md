> Generated reading edition · [exact source](../../research/target_c_tooth_reflection_blocker_matching_2026-09-17.md) · source SHA-256 `9caf7c5ceaf9ad62cc7f59005d03d1dbfdecd4619ea249d431610a5e24df48ce`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "08d7a680b3b655e4447d8e51c3649b4f0e0febc6", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_tooth_reflection_blocker_matching_2026-09-17.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "f0dce22b895252559d599f82c62c0bf4e6bb8892e564862000ce6f39372aefe9"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — fixed-slack reflection blockers have sublinear multiplicity and a growing matching

**Date:** 2026-09-17  
**Status:** proof-only continuation of the shallow-tooth reflection branch; no canonical promotion claimed  
**Scope:** Type-II full-core shallow-tooth branch after the matching/reflection coupled floor  
**Dependencies:** matching/reflection coupled floor; universal full-source circumradius bound; source unit separation  
**Certificate:** `research/verify_target_c_tooth_reflection_blocker_matching_2026_09_17.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The current reflection/perimeter branch produces a linear set of distinct shallow apices, each of which has a normal-aligned inactive upper blocker. The remaining stated obstruction was blocker multiplicity: one source point could, in principle, block many nearby tooth bases.

Constant multiplicity is false in the near-circular model, but linear multiplicity is also impossible. The universal circumradius estimate gives a sharp enough fixed-slack near-diameter star bound.

For the exact reflection geometry at `eta=15/56`, put

```math
C={\sqrt{3135}\over56}=0.9998405485\ldots<1.
\tag{RB.1}
```

Every reflected upper blocker has original length

```math
\boxed{|xy|>D-C.}
\tag{RB.2}
```

The fixed-slack graph on all source pairs satisfying (RB.2) has maximum degree

```math
\boxed{
\Delta_C(D)
\le
\left(448\,3^{1/8}+o(1)\right)D^{3/4}.
}
\tag{RB.3}
```

The factor `448` is exact at the leading level because

```math
C^2={3135\over3136},
\qquad
\sqrt{1-C^2}={1\over56}.
\tag{RB.4}
```

The coupled tooth/reflection theorem supplies

```math
\boxed{
U_D>
(0.243036024157656\ldots-o(1))D
}
\tag{RB.5}
```

distinct forced-degree shallow apices with upper reflection blockers. Choose one blocker edge from every such apex. Since the apices are distinct, every source vertex is a chosen tail at most once; (RB.3) bounds the number of possible chosen heads through one vertex.

A greedy matching therefore contains

```math
\boxed{
M_D>
(0.0002364408355527\ldots-o(1))D^{1/4}
}
\tag{RB.6}
```

pairwise vertex-disjoint reflection blockers.

Thus the low-`t` shallow-tooth branch now contains an unbounded family of disjoint almost-diameters, each retaining its own shallow-tooth apex/base tag and reflection normal cone. The previous uncontrolled-multiplicity escape has been reduced to a sublinear `D^{3/4}` star phenomenon.

---

## 1. Fixed-slack midpoint localization

Let `A` be any unit-separated planar source of diameter `D`. Let `o` be the full-source circumcenter from the audited geometry theorem, so

```math
A\subset B(o,R_D),
\qquad
R_D<{D\over2}+\eta_D,
\qquad
\eta_D=3^{1/4}\sqrt D.
\tag{RB.7}
```

Fix any constant

```math
0<C<1
```

and let `xy` be a source pair with

```math
\ell:=|x-y|\ge D-C.
```

Its midpoint `m=(x+y)/2` satisfies the parallelogram identity

```math
|m-o|^2
={|x-o|^2+|y-o|^2\over2}-{\ell^2\over4}.
```

Therefore

```math
\begin{aligned}
|m-o|^2
&<\left({D\over2}+\eta_D\right)^2-{(D-C)^2\over4}\\
&=D\eta_D+\eta_D^2+{DC\over2}-{C^2\over4}.
\end{aligned}
\tag{RB.8}
```

Define

```math
L_{C,D}
:=\sqrt{D\eta_D+\eta_D^2+{DC\over2}}.
\tag{RB.9}
```

Since `C` is fixed,

```math
\boxed{
|m-o|<L_{C,D}
=(3^{1/8}+o(1))D^{3/4}.
}
\tag{RB.10}
```

Thus fixed additive slack below diameter has the same leading midpoint-localization scale as actual diameter edges and inverse-`D` inactive upper witnesses.

---

## 2. A fixed vertex has only `O(D^{3/4})` fixed-slack neighbors

Fix a source vertex `x` and two distinct neighbors `y,z` with

```math
D-C\le r:=|y-x|,\ s:=|z-x|\le D.
\tag{RB.11}
```

By (RB.10), the two midpoints are both in `B(o,L_{C,D})`, so

```math
|y-z|\le4L_{C,D}.
\tag{RB.12}
```

Let

```math
u={y-x\over r},
\qquad
v={z-x\over s}
```

and let `theta` be the smaller angle between the two rays. Then

```math
|u-v|
\le {2|y-z|\over D-C}
\le {8L_{C,D}\over D-C},
```

hence all such neighbor directions lie in an ordinary angular interval of width

```math
\Theta_{C,D}
:=2\arcsin\left({4L_{C,D}\over D-C}\right)
=(8\,3^{1/8}+o(1))D^{-1/4}.
\tag{RB.13}
```

Distinct neighbors also have a minimum angular separation. Unit separation gives

```math
1\le|y-z|^2
=(r-s)^2+4rs\sin^2{\theta\over2}.
\tag{RB.14}
```

Because

```math
|r-s|\le C<1,
\qquad rs\le D^2,
```

we obtain

```math
\sin{\theta\over2}
\ge {\sqrt{1-C^2}\over2D}.
\tag{RB.15}
```

Thus distinct near-diameter rays are separated by at least

```math
\delta_{C,D}
:=2\arcsin\left({\sqrt{1-C^2}\over2D}\right)
={\sqrt{1-C^2}+o(1)\over D}.
\tag{RB.16}
```

Packing these directions into the interval (RB.13) gives

```math
\boxed{
\Delta_C(D)
\le
1+{\Theta_{C,D}\over\delta_{C,D}}
\le
\left(
{8\,3^{1/8}\over\sqrt{1-C^2}}+o(1)
\right)D^{3/4}.
}
\tag{RB.17}
```

This is the fixed-slack version of the existing inverse-`D` inactive near-diameter degree theorem.

---

## 3. Exact specialization to the reflection constant

For the matching/reflection geometry,

```math
C={\sqrt{3135}\over56}.
```

Exactly,

```math
C^2={3135\over3136}
```

and therefore

```math
\sqrt{1-C^2}={1\over56}.
\tag{RB.18}
```

Substitute this into (RB.17):

```math
\boxed{
\Delta_C(D)
\le
\left(448\,3^{1/8}+o(1)\right)D^{3/4}.
}
\tag{RB.19}
```

Numerically the leading coefficient is

```math
448\,3^{1/8}=513.946805317\ldots .
```

The constant is large because the reflection slack lies very close to one, but the exponent is strictly sublinear.

---

## 4. Greedy matching of the reflection blockers

The current matching/reflection coupled floor gives a set `X_D` of distinct shallow apices with

```math
|X_D|>
(u_0-o(1))D,
\qquad
u_0=0.2430360241576561830\ldots,
\tag{RB.20}
```

such that every `x in X_D` has at least one upper reflection blocker `y(x)` with

```math
|x-y(x)|>D-C.
```

Choose one such blocker for each apex and orient the selected edge from `x` to `y(x)`. The tails are distinct.

For any source vertex `v`, at most one selected edge leaves `v`. The number of selected edges entering `v` is at most the number of fixed-slack neighbors of `v`, hence at most `Delta_C(D)`.

Therefore at most

```math
\Delta_C(D)+1
```

selected edges are incident to any one source vertex. A greedy matching step selecting edge `xy` deletes at most

```math
2(\Delta_C(D)+1)-1
=2\Delta_C(D)+1
```

selected edges. Hence

```math
|M_D|
\ge
{|X_D|\over2\Delta_C(D)+1}.
\tag{RB.21}
```

Using (RB.19)--(RB.20),

```math
\boxed{
|M_D|>
\left(
{u_0\over896\,3^{1/8}}-o(1)
\right)D^{1/4}.
}
\tag{RB.22}
```

The coefficient is

```math
{u_0\over896\,3^{1/8}}
=0.0002364408355527397\ldots,
```

which proves (RB.6).

---

## 5. Geometry retained by the matching

Every matched edge is still the original inactive blocker chosen by the shallow-tooth reflection argument. Thus it retains:

- one distinct unloaded shallow apex;
- the associated loaded tooth base and reflected competitor point;
- the exact normal-cone inequality from the reflection theorem;
- original length larger than `D-sqrt(3135)/56`;
- midpoint in the common `O(D^{3/4})` ball around the full-source circumcenter.

Only the blocker endpoints are made pairwise disjoint. No claim is made that the loaded base endpoints of different gadgets are disjoint.

This distinction is important: the theorem is a blocker-multiplicity reduction, not a full gadget-disjointness theorem.

---

## 6. Remaining closure target

The previous reflection frontier explicitly allowed one blocker point to serve a linear family of neighboring shallow bases. Equation (RB.19) rules that out and (RB.22) forces an unbounded matching.

The remaining escape is subtler. These matched edges are inactive pairs of length `D-C`, not actual diameter edges. The next useful target is therefore to couple their retained reflection normal cones and shallow-tooth base order strongly enough to obtain either

1. a crossing/alternation contradiction for a growing vertex-disjoint family;
2. promotion of a positive subfamily to `D-o(1)` or actual diameter edges; or
3. a same-cardinality finite reflection motion decreasing the actual diameter graph while preserving unit separation.

**Disposition:** proved fixed-slack near-diameter maximum degree `O(D^(3/4))` and converted the linear shallow-tooth reflection population into an explicit `Omega(D^(1/4))` vertex-disjoint blocker matching. C-II and Level I remain open.
