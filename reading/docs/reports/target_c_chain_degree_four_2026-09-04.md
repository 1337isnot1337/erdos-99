> Generated reading edition · [exact source](../../../docs/reports/target_c_chain_degree_four_2026-09-04.md) · source SHA-256 `ca63e9711fc6947472109eb4c0aab0ab2f3e8df705f70f9907c770ce41551a34`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-2D2ABC4BAF1D","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C: degree-four rigidity along the C80 diameter chain

**Date:** 2026-09-04  
**Repository base:** `89c17412`  
**Run type:** exact local-structure continuation of C65+C80  
**Target:** Target C C-II, pure-rhombic C80 chain-face branch  
**Status:** proved working result; not yet promoted  
**LEVEL I STATUS:** STILL OPEN

Let

`z=x_0,x_1,...,x_D=a`

be the exact straight unit-contact diameter chain supplied by C80, with

`p_(x_i)=p_z+i u`, `|u|=1`, and `|z-a|=D`.

In the C65 lexicographically normalized triangle-free source, choose a
relative-interior KKT stress. Then every actual unit contact has positive stress and
every actual diameter pair is force-visible.

The internal chain vertices are much more rigid than the generic C26 conclusion
`3<=deg_C<=5`:

> **Chain degree-four lemma.** For every `1<=i<=D-1`, the full unit-contact degree of
> `x_i` is exactly four. Besides the two chain contacts `x_i x_(i-1)` and
> `x_i x_(i+1)`, there is exactly one contact neighbor in each open half-plane bounded
> by the chain line.

In the pure simply connected strict-rhombic-disk realization used by C80, this has a
topological consequence:

> **Boundary-chain matching lemma.** The chain edges that lie on the outer boundary of
> the rhombic disk form a matching in the path `x_0...x_D`. Hence at most
> `ceil(D/2)` chain edges are boundary edges, and at least `floor(D/2)` chain edges are
> interior edges incident to a strict unit rhombus on each side.

Thus the exact C80 chain is not an arbitrary boundary-hugging geodesic. At least half
of its edges pass through a two-sided rhombic strip.

---

## 1. Internal chain vertices are not diameter endpoints

Fix `i` with `1<=i<=D-1`. Since

`p_(x_i)=(1-i/D)p_z+(i/D)p_a`,

`x_i` lies in the relative interior of the segment `za`. In particular it is not an
extreme point of `conv A`.

Canonical Lemma 5.1 says every endpoint of an actual diameter pair is an extreme point
of `conv A`. Therefore

`x_i notin V(H)`.

By C65, the complete actual diameter graph is the positive diameter support of the
relative-interior stress, so `x_i` carries no diameter reaction.

## 2. Positive contact equilibrium at `x_i`

C65 also gives positive contact stress on every actual unit contact. KKT equilibrium at
`x_i` is therefore

`sum_(x_i y in C) alpha_(x_i y) (p_(x_i)-p_y)=0`,

with every `alpha_(x_i y)>0`.

The two chain neighbors contribute the two opposite contact rays `+u` and `-u`.
Their transverse components vanish.

If all other contact rays lay in one closed half-plane bounded by `R u`, then every
non-chain ray would have transverse component of the same weak sign. At least one
non-chain ray is necessary: otherwise the two opposite chain contacts would make
`x_i` an unloaded degree-two contact vertex, excluded by C26.3 (or directly by
contact-minimal Theorem 6.1 because `x_i` is not a diameter endpoint).

Since all coefficients are strictly positive, the transverse component of equilibrium
could not vanish unless there were a non-chain ray in each open half-plane.

Hence `x_i` has at least one off-chain contact neighbor above the chain line and at
least one below it.

## 3. Triangle-freeness permits at most one ray in either open half-plane

For two distinct unit-contact neighbors `y,w` of a vertex `x`, let `theta` be the
smaller angle between the rays `xy,xw`. Then

`|y-w|=2 sin(theta/2)`.

Unit separation gives `theta>=pi/3`. Equality would make `x,y,w` a unit equilateral
triangle, so in a triangle-free source

`theta>pi/3`.

Consider one of the open semicircles from the ray `+u` to the ray `-u`. If it
contained two additional contact rays, then the three consecutive angular gaps from
`+u` to the first ray, from the first to the second, and from the second to `-u`
would each be strictly larger than `pi/3`. Their sum would then exceed `pi`, impossible.

Thus each open half-plane contains at most one off-chain contact ray.

Combined with Section 2, there is exactly one on each side. Together with the two chain
neighbors this proves:

### Theorem — exact degree four on the chain interior

For every `1<=i<=D-1`,

`deg_C(x_i)=4`.

If the upper off-chain ray makes angle `theta_i` from `+u`, then

`pi/3 < theta_i < 2pi/3`.

The analogous lower ray lies strictly between `-2pi/3` and `-pi/3` relative to `+u`.
All four consecutive contact-ray gaps are strictly larger than `pi/3`.

This improves C26.3 from the generic set `{3,4,5}` to the single value `4` on every
internal vertex of the exact C80 chain.

## 4. Pure-rhombic boundary consequence

Now assume the pure simply connected strict-rhombic-disk realization used by C80: the
contact complex is a topological disk, its bounded faces are strict unit rhombi, and
its outer boundary is simple.

At a boundary vertex of such a disk, the outer face occupies one angular sector
between two consecutive incident contact edges. At an internal chain vertex `x_i`,
the two chain rays `-u,+u` are **not** consecutive in cyclic order, because Section 3
puts one off-chain ray in each intervening semicircle.

Suppose both adjacent chain edges

`x_(i-1)x_i` and `x_i x_(i+1)`

were outer-boundary edges. Since the simple outer boundary uses exactly two incident
boundary edges at `x_i`, these two chain edges would have to bound the outer-face
sector there. But their rays are not consecutive; an off-chain contact ray lies in
either angular route between them. That ray would lie inside the outer-face sector,
contradicting planarity of the disk.

Therefore no two consecutive chain edges can both lie on the outer boundary.

### Corollary — outer chain edges form a matching

The set

`{x_i x_(i+1): 0<=i<D, x_i x_(i+1) subset partial R}`

is a matching in the `D`-edge chain path. Consequently its cardinality is at most
`ceil(D/2)`.

Every remaining chain edge is an interior edge of the rhombic disk. Because the disk
has no holes and every bounded face is a rhombus, every such edge is incident to one
strict unit rhombus on each side. Hence at least

`floor(D/2)`

chain edges have a two-sided rhombic neighborhood.

Each of these rhombi is distinct: a nondegenerate rhombus cannot contain two adjacent
collinear chain edges, nor can both of its opposite edges lie on the same chain line.
Thus the chain is incident to at least

`2 floor(D/2)`

distinct strict rhombi through its interior edges.

## 5. Translation propagation across an interior chain edge

Write `y_i` for the unique upper off-chain contact neighbor of an internal `x_i`, and
`w_i` for the unique lower neighbor.

If an internal chain edge `x_i x_(i+1)` has a rhombus on the upper side and both
endpoints are internal chain vertices, that rhombus must use `y_i` and `y_(i+1)` as
its other two vertices, by uniqueness of the upper contact ray at each endpoint.
A unit rhombus is a parallelogram, so

`y_(i+1)-y_i = x_(i+1)-x_i = u`.

Similarly a lower rhombus gives

`w_(i+1)-w_i=u`.

Thus on every consecutive run of interior chain edges the two off-chain rows propagate
as exact translates of the chain. Boundary chain edges are the only possible breaks
of the corresponding row on their outer side.

This is an exact finite statement, not an asymptotic approximation.

## 6. Audit and limitations

- C24 previously proves a four-neighbor angle fact only at the crossing point of two
  specially stressed full diameter chains. It does not imply the present lemma along
  all internal vertices of one C80 chain.
- C26.3 proves only degree `3,4,5` for a generic unloaded contact vertex. The two exact
  opposite C80 chain contacts are what force the degree down to exactly four here.
- No lower bound on individual KKT weights is used; only strict positivity from the
  C65 relative-interior normalization is needed.
- The boundary matching conclusion uses the pure simply connected rhombic-disk
  topology. The degree-four conclusion itself only needs C65+C80 and triangle-freeness.
- Half of the chain edges being interior is not itself a Level I contradiction.
  Boundary edges can alternate, so this theorem alone does not force a macroscopic
  uninterrupted translated row.
- Splitting the source along the straight chain and applying finite Oler separately to
  the two sides gives no automatic gain: the duplicated `D+1` chain vertices and the
  two added length-`D` boundary chords cancel exactly in the Oler boundary term.

## 7. Exact next obligation

The remaining geometric object is now a straight diameter chain whose internal
vertices all have four contacts, with boundary-chain breaks forming a matching and
exact translated rhombic rows between breaks.

A useful closing theorem would show that a linear density of alternating boundary
breaks incurs a forbidden hull/Oler loss; otherwise one obtains a long translated
strip that can be combined with the C87 paired diameter staircase and C94 active-face
flatness.
