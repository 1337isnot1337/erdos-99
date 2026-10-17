> Generated reading edition · [exact source](../../research/target_c_high_t_tb1_superdiameter_inactive_thrackle_t18687_2026-09-17.md) · source SHA-256 `758077b428562c76c030247d36e220da1cb9c4946a74e100bf5db4bea7949b82`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "cd544343df6d46045fb20f8cd413c3db32d5204e", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_high_t_tb1_superdiameter_inactive_thrackle_t18687_2026-09-17.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "cc32baf88ac93ad0b825e3fe3eeda1e4eb658063dd20af5bcd9f9c045bb93c20"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — the superthin TB1 inactive shell is a genuine geometric thrackle

**Date:** 2026-09-17  
**Status:** proof-only high-`t` structural strengthening; no canonical promotion claimed  
**Scope:** the near-diameter side of the one-sign strong-TB1 exact-swap branch through `t=(q-k)/D<=1.8687`  
**Dependencies:** exact-swap slack-ratio theorem; unit separation; diameter bound; near-diameter midpoint/degree theorem  
**Certificate:** `research/verify_target_c_high_t_tb1_superdiameter_inactive_thrackle_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The exact-swap slack-ratio theorem allows the relative slack threshold `tau` to be chosen arbitrarily small before the final density split. Choosing it below the sharp `sqrt(D^2-1)` scale converts the THIN alternative from an arbitrary inactive near-diameter graph into a straight-line **geometric thrackle**.

The geometric input is independent of TB1 and is sharp.

> **Superdiameter-thrackle lemma.** Let `S` be a unit-separated planar set of diameter `D>1`. Join every source pair `xy` satisfying
> 

$$

> |xy|>\sqrt{D^2-1}.
> 
$$


> Then every two such segments meet: they either share a source endpoint or cross properly.

The threshold cannot be improved in general. The `1 x sqrt(D^2-1)` rectangle has two vertex-disjoint opposite sides of length exactly `sqrt(D^2-1)` which do not cross, while its diagonals have length `D`.

Applying the lemma to the TB1 exact-swap witnesses gives a sharper positive-density alternative. Put

$$
\tau_*={1\over128{,}000{,}000}.
$$

On the near-diameter exact-swap side, after one final halving there are more than

$$
{s_0\over16}D-o(D)
=(1.544921875\times10^{-7})D-o(D)
$$

distinct tagged witnesses satisfying either

$$
r\cdot w_i\le-(\tau_*-o(1))D,
$$

or

$$
D-|r|<\tau_*q_i.
$$

In the second case,

$$
31.4\times10^6\tau_*=0.2453125<\frac14,
$$

so eventually

$$
D-|r|<{1\over4D}.
$$

But

$$
\sqrt{D^2-1}<D-{1\over2D},
$$

hence every THIN witness satisfies

$$
|r|>\sqrt{D^2-1}.
$$

Therefore all THIN witnesses, although still inactive nondiameters, already form a geometric thrackle. Using the existing near-diameter degree bound then extracts an

$$
\Omega(D^{1/4})
$$
vertex-disjoint family whose every two chords cross properly. Every endpoint of every such chord is a convex-hull vertex, every chord retains a distinct physical layer tag, and every midpoint remains in the common `O(D^{3/4})` central ball.

This is the first current conversion of the inactive TB1 diameter shell into the same **crossing-order type** that previously belonged only to actual diameter edges. No KKT or active-diameter claim is made for these chords.

---

## 1. Long-enough pairs have only hull-vertex endpoints

Let `xy` be a source pair with

$$
|xy|>\sqrt{D^2-1}.
\tag{STH.1}

We first prove that `x` is a vertex of `conv(S)`. Suppose not. Then

\[
x\in\operatorname{conv}(S\setminus\{x\}).
$$

Put

$$
u={x-y\over|x-y|}.
$$

Writing `x` as a convex combination of other source points shows that some `z!=x` satisfies

$$
u\cdot(z-x)\ge0.
\tag{STH.2}

Unit separation gives

\[
|z-x|\ge1.
\tag{STH.3}

Therefore

\[
\begin{aligned}
|z-y|^2
&=|(x-y)+(z-x)|^2\\
&=|x-y|^2
+2|x-y|\,u\cdot(z-x)
+|z-x|^2\\
&>|D^2-1}+0+1
=D^2,
\end{aligned}
\tag{STH.4}

contradicting the source diameter. Hence `x` is a hull vertex. The same argument applies to `y`.

Thus

\[
\boxed{
|xy|>\sqrt{D^2-1}
\Longrightarrow x,y\in V(\operatorname{conv}S).
}
\tag{STH.5}

This conclusion uses the unit lower separation essentially.

---

## 2. Two vertex-disjoint superdiameter chords must cross

Take two vertex-disjoint source pairs `AB` and `CD` satisfying

\[
|AB|,|CD|>\sqrt{D^2-1}.
\tag{STH.6}

By Section 1 all four endpoints are hull vertices. Suppose the straight segments do not cross properly. In the cyclic order of these four hull vertices, the two disjoint noncrossing pairs must be opposite sides of their induced convex quadrilateral. Relabel cyclically so the order is

\[
A,B,C,D
$$

and the selected long sides are `AB` and `CD`.

Put the oriented side vectors

$$
x=B-A,
\qquad y=C-B,
\qquad z=D-C,
\qquad w=A-D.
\tag{STH.7}

The two connector sides are source pairs, so

\[
|y|=|BC|\ge1,
\qquad
|w|=|DA|\ge1.
\tag{STH.8}

All source distances are at most `D`. In particular

\[
|x+y|=|AC|\le D,
\qquad
|y+z|=|BD|\le D,
\tag{STH.9}

and also

\[
|z+w|=|CA|\le D,
\qquad
|w+x|=|DB|\le D.
\tag{STH.10}

Now

\[
\begin{aligned}
2x\cdot y
&=|x+y|^2-|x|^2-|y|^2\\
&<D^2-(D^2-1)-1=0.
\end{aligned}
\tag{STH.11}

The same calculation at the other three vertices gives

\[
\boxed{
x\cdot y<0,
\quad y\cdot z<0,
\quad z\cdot w<0,
\quad w\cdot x<0.}
\tag{STH.12}

Because `A,B,C,D` is a convex quadrilateral in cyclic order, the four exterior turning angles from

\[
x\to y\to z\to w\to x
$$

all lie in `(0,pi)` and sum to `2pi`. Equation (STH.12) says every one of those turns is strictly greater than `pi/2`. Their sum would therefore be strictly greater than `2pi`, a contradiction.

Hence the two selected chords cross properly.

Together with the shared-endpoint case, this proves:

$$
\boxed{
G_{>}(S):=\{xy:|xy|>\sqrt{D^2-1}\}
\text{ is a straight-line geometric thrackle.}
}
\tag{STH.13}

No active-diameter property is used.

---

## 3. The threshold is sharp

Take a Euclidean rectangle with side lengths

\[
1,
\qquad
L=\sqrt{D^2-1}.
\tag{STH.14}

Its two diagonals have length exactly `D`. Its two long opposite sides have length exactly `L`, are vertex-disjoint, and do not cross.

Thus replacing `>` by `>=` in (STH.13) is false, and no universal threshold below `sqrt(D^2-1)` can force the same conclusion.

This sharp rectangle is the same metric scale already appearing in the cyclic P1 endpoint geometry elsewhere in the repository.

---

## 4. Enter the exact-swap near-diameter branch

Retain the notation of the exact-swap slack-ratio theorem. In the one-sign strong-TB1 branch there are more than

\[
{s_0\over4}D-o(D)
\tag{STH.15}

distinct exact-swap witnesses. After splitting by lower versus upper active boundary, the near-diameter alternative contains more than

\[
{s_0\over8}D-o(D)
\tag{STH.16}

distinct tagged pairs.

At tag `i`, write

\[
q_i=|a_i+b_i|,
\qquad
q_i<{31.4\times10^6\over D}+o(D^{-1}),
\tag{STH.17}

and orient the witness vector `r_i` from its fixed endpoint into the translated physical layer. Its initial length obeys

\[
D-q_i\le|r_i|<D.
\tag{STH.18}

For any prescribed threshold `tau`, the slack-ratio theorem partitions these witnesses into

\[
\text{SIGNED: }
 r_i\cdot w_i\le-(\tau-o(1))D,
\tag{STH.19}

and

\[
\text{THIN: }
 0<D-|r_i|<\tau q_i.
\tag{STH.20}

At least one class has more than

\[
\boxed{
{s_0\over16}D-o(D)
=(1.544921875\times10^{-7})D-o(D).
}
\tag{STH.21}

---

## 5. A fixed threshold puts THIN strictly above `sqrt(D^2-1)`

Choose once and for all

\[
\boxed{
\tau_*={1\over128{,}000{,}000}
=7.8125\times10^{-9}.}
\tag{STH.22}

Then

\[
31.4\times10^6\tau_*
=0.2453125
<\frac14.
\tag{STH.23}

Combining (STH.17) and (STH.20), every THIN witness satisfies

\[
D-|r_i|
< {0.2453125+o(1)\over D}.
\tag{STH.24}

Hence for all sufficiently large sources,

\[
\boxed{
D-|r_i|<{1\over4D}.}
\tag{STH.25}

On the other hand

\[
\left(D-{1\over2D}\right)^2
=D^2-1+{1\over4D^2}
>D^2-1,
$$

so

\[
\sqrt{D^2-1}<D-{1\over2D}<D-{1\over4D}.
\tag{STH.26}

Equations (STH.25)--(STH.26) give

\[
\boxed{|r_i|>\sqrt{D^2-1}}
\tag{STH.27}

for every THIN witness.

Therefore the full THIN witness graph from (STH.21) is a straight-line geometric thrackle by (STH.13).

The competing SIGNED branch now has the explicit fixed transverse margin

\[
\boxed{
r_i\cdot w_i
\le-\left(7.8125\times10^{-9}-o(1)\right)D.}
\tag{STH.28}

The constant is deliberately tiny because its purpose is to cross the sharp `sqrt(D^2-1)` metric threshold on the other side of the fork.

---

## 6. The THIN thrackle contains an unbounded vertex-disjoint crossing braid

Every THIN edge remains an `O(D^-1)`-near-diameter pair, so the existing inactive near-diameter degree estimate applies:

\[
\Delta(G_D^{near})
\le(8\,3^{1/8}+o(1))D^{3/4}.
\tag{STH.29}

Greedy matching applied to the linear THIN edge population (STH.21) therefore gives a vertex-disjoint matching of size

\[
\boxed{
\left(
{s_0\over256\,3^{1/8}}-o(1)
\right)D^{1/4}.}
\tag{STH.30}

Numerically,

\[
\boxed{
{s_0\over256\,3^{1/8}}
=8.4167878956\ldots\times10^{-9}.}
\tag{STH.31}

Because the entire THIN graph is a geometric thrackle, every two edges of this matching cross properly.

Each matching edge also retains the previous midpoint localization

\[
\left|{x+y\over2}-o\right|
<(3^{1/8}+o(1))D^{3/4},
\tag{STH.32}

and Section 1 gives the stronger endpoint statement

\[
x,y\in V(\operatorname{conv}S).
\tag{STH.33}

The exact-swap construction additionally assigns each distinct witness one representative physical layer tag. The tag assignment remains injective after taking a matching, and one endpoint of the edge lies in its tagged layer.

Thus the THIN branch contains

```text
Omega(D^(1/4)) vertex-disjoint inactive chords
+ every two chords cross properly
+ all endpoints are convex-hull vertices
+ all chord lengths exceed sqrt(D^2-1)
+ all midpoints lie in one O(D^(3/4)) central ball
+ distinct exact physical layer tags.
```

This is a genuine crossing braid even though none of its edges is asserted to be an active diameter.

---

## 7. Frontier effect

The near-diameter escape from the one-sign TB1 branch is now substantially narrower. At positive linear density it must produce either

```text
SIGNED:
    inactive D-O(1/D) pairs with a fixed negative projection
    against the local TB1 swap axis;

or

SUPERTHIN THRACKLE:
    inactive pairs above the sharp sqrt(D^2-1) threshold,
    hence a geometric thrackle and an Omega(D^(1/4))
    vertex-disjoint complete crossing braid of hull chords.
```

The second branch has recovered the crossing-order feature that was previously exclusive to actual diameter edges. What it still lacks is active-diameter KKT weight and the exact common-hub support interval. The next useful step is to exploit the distinct layer tags of the superthin crossing braid: after fixing one tagged endpoint host, pairwise crossing should strongly order the partner endpoints and may allow the inactive braid to be fused with the common train ladder in the same way as the active nested rail.

**Disposition:** proved the sharp superdiameter-thrackle lemma and used the exact-swap relative-slack freedom to convert the THIN inactive near-diameter TB1 alternative into a genuine tagged crossing braid. C-II and Level I remain open.
