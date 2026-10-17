> Generated reading edition · [exact source](../../../../docs/targets/target-a/28-zero-slack-boundary-order-source-frontier.md) · source SHA-256 `f3d1d0cee6ba98caa5264a5b0f15de8758949f9046e294fc0b91ce85f3ca0db1`.
> [Current theorem state](../../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

# Target A — zero-slack boundary-order source frontier

This module promotes the exact source-side consequences that were proved after Section
168 but never incorporated into the Target A route map. It is independent of the
locked-fan improvement in Section 175.

**LEVEL I STATUS: STILL OPEN. TARGET A REMAINS UNRESOLVED.**

---

# 176. Boundary-order defect of the zero-slack source

Assume the zero-slack branch of Section 168. Let

```math
A^0\subset H
```

be the triangle-free unit-separated source saturating the fixed-hull capacity, and let
`X^* subset K^*` be the plateau-terminalized response optimum with

```math
m^*=|X^*|,
\qquad
\operatorname{diam}K^*=d.
```

Section 168.2 gives a strict-conflict matching saturating `X^*` into `A^0`. Section
168.3 defines

```math
k=|A^0\cap K^*|,
\qquad
r=m^*-k.
\tag{176.1}
```

Every saturating matching has at least `r` source endpoints outside `K^*`.

## 176.1 Exterior source labels are boundary-order

Fix any saturating source matching and write `a_x` for the source label of
`x in X^*`. Put

```math
G_{\rm ext}=\{x\in X^*:a_x\notin K^*\}.
```

> **Lemma 176.1 (exterior labels start in the unit boundary layer).**
> ```math
> x\in G_{\rm ext}
> \Longrightarrow
> \operatorname{dist}(x,\partial K^*)<1.
> \tag{176.2}
> ```

### Proof

The segment `[x,a_x]` has length below one, starts in the closed convex body `K^*`,
and ends outside it. It therefore meets `partial K^*` between the endpoints, at
strictly smaller distance from `x` than `|x-a_x|<1`. $`\square`$

> **Lemma 176.2 (response boundary-layer count).**
> ```math
> \#\{x\in X^*: \operatorname{dist}(x,\partial K^*)\le1\}
> \le12d+9.
> \tag{176.3}
> ```

### Proof

Put disjoint radius-`1/2` disks around the counted response points. They lie in the
closed `3/2`-neighborhood of `partial K^*`. For a convex body with perimeter `P`, the
area of that boundary neighborhood is at most

```math
3P+\frac94\pi.
```

Indeed the outer parallel body contributes `3P/2+9pi/4`, while the inner boundary
layer has area at most `3P/2`. Dividing by the radius-`1/2` disk area `pi/4` gives

```math
12P/\pi+9.
```

Cauchy's perimeter inequality `P<=pi d` gives (176.3). $`\square`$

Combining the two lemmas:

> **Theorem 176.3 (uniform exterior-gate budget).** Every saturating source matching
> obeys
> ```math
> \boxed{|G_{\rm ext}|\le12d+9.}
> \tag{176.4}
> ```

Since Section 168.3 gives `|G_ext|>=r` for every such matching:

> **Corollary 176.4 (inner-source capacity defect).**
> ```math
> \boxed{
> r\le12d+9,
> \qquad
> |A^0\cap K^*|\ge m^*-(12d+9).
> }
> \tag{176.5}
> ```

Thus failure of exact plateau descent is confined to a boundary-order population; it
is never a quadratic missing-source population.

## 176.2 Source labels cross a contact shield at bounded multiplicity

Let `Sigma` be any finite unit-contact shield in `X^*`. For
`x in X^*\setminus V(Sigma)`, suppose the source-label segment `[x,a_x]` intersects
`|Sigma|`.

If it properly crosses a unit contact edge `pq`, then the unit-edge crossing barrier
forces

```math
|a_x-p|<1
\quad\text{or}\quad
|a_x-q|<1.
\tag{176.6}
```

The same conclusion is immediate when the segment meets a shield vertex. A collinear
overlap with the relative interior of a unit contact is impossible because `x` is a
distinct point of the unit-separated set `X^*` and the source-label segment has length
below one.

An open unit disk contains at most five points of the unit-separated set `A^0`: among
six points, two consecutive polar angles differ by at most `pi/3`, and for radii
`r,s<1` their squared distance is at most `r^2+s^2-rs<1`.

The matching has distinct source endpoints. Therefore:

> **Theorem 176.5 (source-label shield-crossing budget).**
> ```math
> \boxed{
> \#\{x\in X^*\setminus V(\Sigma):[x,a_x]\cap|\Sigma|\ne\varnothing\}
> \le5|V(\Sigma)|.
> }
> \tag{176.7}
> ```

## 176.3 Combined sector-local source matching

Let `D_1,...,D_k` be the components of `K^*\setminus|Sigma|`. Call an off-shield
response vertex sector-good when its source label lies in `K^*` and in the same
component as the response vertex.

An internal label in a different sector must have its straight source-label segment
cross `|Sigma|`, so Theorem 176.5 charges it. Exterior labels are charged by Theorem
176.3. Hence:

> **Theorem 176.6 (zero-slack source localization).** For every saturating
> `X^* -> A^0` source matching and every finite unit-contact shield,
> ```math
> \boxed{
> \#\{x\in X^*\setminus V(\Sigma):x\text{ is not sector-good}\}
> \le5|V(\Sigma)|+12d+9.
> }
> \tag{176.8}
> ```

After deleting that explicit boundary-order exceptional set, the genuine-source
matching restricts sector by sector.

For the three-channel locked fan this can be used together with Section 175, but it
also applies to arbitrary finite unit-contact shields in the zero-slack source branch.

## 176.4 What this does and does not prove

The source side is now quantitatively close to the smaller response hull:

```math
|A^0\cap K^*|=m^*-O(d),
```

and its saturating matching is sector-preserving up to

```math
5|V(\Sigma)|+O(d).
```

This does **not** prove a relation between the inner-source defect `r` and the Schur
demand

```math
s=\Delta_\Lambda-d_{\rm int},
```

and it does not identify the independent saturating matchings from `X^*` and
`Y_in` into `A^0`. The Section-166 common-neighbor SDR collision remains binding.

The zero-slack branch therefore has two exact ways forward:

1. prove a global relation converting the boundary-order source defect and co-phased
   monomer/lozenge cells into the required Schur deficiency; or
2. prove that repeated plateau descent cannot persist for an unbounded sequence of
   counterexamples and convert the descent to a strict source-cardinality competitor.

Counting local source labels alone is no longer the missing step.
