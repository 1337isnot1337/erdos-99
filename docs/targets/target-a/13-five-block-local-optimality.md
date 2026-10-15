# Target A — local five-block quartic optimality

This audited addendum complements Section 160. Section 160 constructs a toe-out
translation of the Section 157 five rigid blocks with paper-normalized middle-gap gain

\[
v_{\rm toe}(d)=\frac{\sqrt3}{9}d^4-\frac29d^5+O(d^6).
\]

It explicitly does not claim optimality among other five-block translations. The result
below closes that exponent-level question in the local identity branch: arbitrary
simultaneous, asymmetric translations of the same five rigid blocks still cannot
produce a middle lift larger than order `d^4`.

**LEVEL I STATUS: STILL OPEN. TARGET A REMAINS UNRESOLVED.**

---

# 161. Local rigid five-block gain is exactly quartic

Work in the Kuperberg paper normalization of Sections 157 and 160, where nearest-neighbor
center distance is two. The upper half triangular lattice is shifted initially by
`(0,d)`, `d>0`, and the exact five blocks are `B_1,\ldots,B_5` from Section 157.
All centers outside those five blocks remain fixed.

Allow completely arbitrary rigid translations

\[
\tau_i=(x_i,y_i),\qquad 1\le i\le5,
\tag{161.1}
\]

with no symmetry assumption, no move ordering, no rotations, and no internal block
deformation. Put

\[
E=\max_{1\le i\le5}\|\tau_i\|.
\tag{161.2}
\]

Call an endpoint feasible when every center distance is at least two. The quantity
`y_3` is the vertical lift of the middle `\Delta_{n-1}` block, hence the aligned local
gap gain along its base.

The exact Section 157 coordinate partition contains the following original
nearest-neighbor contacts for every `n>=3`:

1. a horizontal chain from fixed upper lattice through
   `B_1-B_2-B_3-B_4-B_5` back to fixed upper lattice;
2. for each of `B_1,B_2,B_4,B_5`, fixed-upper diagonal contacts in both directions
   `(\pm1,\sqrt3)`;
3. for each outer block `B_1,B_5`, two fixed-lower diagonal contacts, whose relative
   vectors from the upper point are `(\pm1,-\sqrt3-d)`;
4. a left `B_3`-to-`B_2` diagonal contact with base vector `(-1,\sqrt3)` and its
   right reflected `B_3`-to-`B_4` contact `(1,\sqrt3)`.

These are subfamilies of the complete nearest-neighbor interface enumeration already
audited in Sections 157 and 160.

## 161.1 Horizontal contact chain kills all first-order horizontal motion

Introduce virtual endpoint translations

\[
\tau_0=\tau_6=0.
\tag{161.3}
\]

Every link in the horizontal chain has original difference vector `(2,0)`. Feasibility
gives

\[
\left|(2,0)+\tau_{i+1}-\tau_i\right|^2\ge4,
\qquad 0\le i\le5,
\tag{161.4}
\]

and therefore

\[
x_{i+1}-x_i
\ge-\frac14\|\tau_{i+1}-\tau_i\|^2.
\tag{161.5}
\]

Sum (161.5) from the left fixed endpoint to `B_k`. The first increment has norm at
most `E` and every later increment has norm at most `2E`, so

\[
x_k\ge-5E^2.
\]

Summing instead from `B_k` to the right fixed endpoint gives the opposite bound.
Thus

\[
\boxed{|x_k|\le5E^2\qquad(1\le k\le5).}
\tag{161.6}
\]

In particular, every identity-convergent feasible family has zero first-order
horizontal velocity, without any symmetry assumption.

## 161.2 Fixed-upper and fixed-lower diagonal cages

For `i\in\{1,2,4,5\}`, the two fixed-upper contacts give

\[
\left|(1,\sqrt3)-\tau_i\right|^2\ge4,
\qquad
\left|(-1,\sqrt3)-\tau_i\right|^2\ge4.
\tag{161.7}
\]

Adding them cancels the horizontal term:

\[
2\|\tau_i\|^2-4\sqrt3\,y_i\ge0.
\]

Hence

\[
\boxed{
y_i\le\frac{\|\tau_i\|^2}{2\sqrt3}\le E^2.
}
\tag{161.8}
\]

For an outer block `i\in\{1,5\}`, use its two fixed-lower contacts. Adding the two
expanded inequalities gives

\[
2\|\tau_i\|^2
+4(\sqrt3+d)y_i
+4\sqrt3\,d+2d^2
\ge0.
\tag{161.9}
\]

Therefore

\[
y_i\ge-
\frac{\|\tau_i\|^2+2\sqrt3\,d+d^2}{2(\sqrt3+d)}
\ge-d-E^2.
\tag{161.10}
\]

Combining with (161.8),

\[
\boxed{|y_1|,|y_5|\le d+E^2.}
\tag{161.11}
\]

## 161.3 Exact quadratic cage for the middle block

On the left, use one fixed-upper contact of `B_2` with base vector
`(-1,\sqrt3)`. Its feasibility inequality is

\[
\|\tau_2\|^2+2x_2-2\sqrt3\,y_2\ge0.
\tag{161.12}
\]

The `B_3`-to-`B_2` contact with the same base vector gives

\[
\|\tau_2-\tau_3\|^2
-2(x_2-x_3)+2\sqrt3(y_2-y_3)
\ge0.
\tag{161.13}
\]

Adding (161.12) and (161.13) cancels the full linear motion of `B_2`:

\[
\|\tau_2\|^2+\|\tau_2-\tau_3\|^2
+2x_3-2\sqrt3\,y_3
\ge0.
\tag{161.14}
\]

The reflected pair on the right gives

\[
\|\tau_4\|^2+\|\tau_4-\tau_3\|^2
-2x_3-2\sqrt3\,y_3
\ge0.
\tag{161.15}
\]

Adding again removes the middle horizontal translation. Thus every feasible endpoint
satisfies the exact inequality

> **Lemma 161.1 (middle quadratic cage).**
> \[
> \boxed{
> 4\sqrt3\,y_3
> \le
> \|\tau_2\|^2+\|\tau_2-\tau_3\|^2
> +\|\tau_4\|^2+\|\tau_4-\tau_3\|^2.
> }
> \tag{161.16}
> \]

No sequential path, symmetry, or stationarity assumption enters (161.16). In
particular, because each difference has norm at most `2E`,

\[
y_3<2E^2.
\tag{161.17}
\]

## 161.4 Bootstrap from `O(E^2)` to `O(d^4)`

Assume from now on that

\[
y_3\ge0.
\tag{161.18}
\]

Rearrange (161.13):

\[
y_2
\ge y_3+\frac{x_2-x_3}{\sqrt3}
-\frac{\|\tau_2-\tau_3\|^2}{2\sqrt3}.
\tag{161.19}
\]

Using (161.6), `y_3>=0`, and
`\|\tau_2-\tau_3\|\le2E`, we get

\[
y_2\ge-7E^2.
\tag{161.20}
\]

The reflected inequality gives the same lower bound for `y_4`. Together with
(161.8),

\[
\boxed{|y_2|,|y_4|\le7E^2.}
\tag{161.21}
\]

Equations (161.6), (161.17), and (161.21) imply the coarse norm bounds

\[
\|\tau_2\|,\|\tau_4\|\le12E^2,
\qquad
\|\tau_3\|\le7E^2.
\tag{161.22}
\]

For the outer blocks, (161.6) and (161.11) give

\[
\|\tau_1\|,\|\tau_5\|
\le d+6E^2.
\tag{161.23}
\]

Since `E` is the maximum of the five norms,

\[
E\le d+12E^2.
\tag{161.24}
\]

Now impose the fixed local identity neighborhood

\[
E\le\frac1{24}.
\tag{161.25}
\]

Then `12E^2<=E/2`, so (161.24) yields

\[
\boxed{E\le2d.}
\tag{161.26}
\]

Substituting into (161.22),

\[
\|\tau_2\|,\|\tau_4\|\le48d^2,
\qquad
\|\tau_3\|\le28d^2,
\tag{161.27}
\]

and hence

\[
\|\tau_2-\tau_3\|,
\|\tau_4-\tau_3\|
\le76d^2.
\tag{161.28}
\]

Finally Lemma 161.1 gives

\[
4\sqrt3\,y_3
\le2(48^2+76^2)d^4
=16160d^4.
\]

Therefore:

> **Theorem 161.2 (universal local quartic upper bound).** For every `n>=3`, every
> feasible rigid translation endpoint of the Section 157 five-block aligned-gap
> architecture satisfying
> \[
> E\le\frac1{24},
> \qquad y_3\ge0,
> \]
> obeys
> \[
> \boxed{
> E\le2d,
> \qquad
> 0\le y_3\le\frac{4040}{\sqrt3}d^4.
> }
> \tag{161.29}
> \]
> In particular, for any feasible family with `d->0`, `E(d)->0`, and `y_3(d)>=0`,
> the three inner/middle block translations are `O(d^2)` and
> \[
> \boxed{y_3(d)=O(d^4).}
> \tag{161.30}
> \]

## 161.5 Matching lower bound from Section 160

Define the local five-block translation value

\[
V_5^{\rm loc}(d)
:=
\sup\left\{
 y_3:
 \begin{array}{l}
 \text{the five Section 157 blocks are translated rigidly,}\\
 \text{the exterior is fixed, the endpoint is feasible,}\\
 E\le1/24
 \end{array}
\right\}.
\tag{161.31}
\]

For sufficiently small `d`, the toe-out analytic branch of Section 160 lies in this
neighborhood and has

\[
y_3
=\frac{\sqrt3}{9}d^4-\frac29d^5+O(d^6).
\tag{161.32}
\]

Theorem 161.2 supplies the matching upper order. Hence:

> **Corollary 161.3 (local exponent optimality of the rigid five-block model).**
> \[
> \boxed{
> V_5^{\rm loc}(d)=\Theta(d^4)
> \qquad(d\downarrow0).
> }
> \tag{161.33}
> \]

Thus Section 160 is exponent-optimal among **all local identity-branch translations of
the same five rigid blocks**, even though its leading coefficient is not proved
optimal. In particular, no asymmetric or simultaneous rescheduling of those five
rigid translations can change the widening-stage exponent from `d^{-3}` by producing a
`d^2` or `d^3` one-step gain.

## 161.6 Scope and Target A consequence

Corollary 161.3 is a local architecture theorem, not a global optimality theorem for
all finite gap rearrangements. It does not exclude:

- a feasible five-block endpoint that stays a fixed positive distance from the
  identity as `d->0`;
- rotations or internal deformation of the five blocks;
- a different finite block/contact architecture;
- a nonlocal rearrangement; or
- constructive use of the exterior source/scaffold blockers.

It also does not solve exterior compatibility. Extra points in an actual embedded
Target A monomer domain can only add constraints to the free five-block calculation,
but no theorem here turns those added blockers into response nullity.

The exact Target A closure remains

\[
\boxed{
\dim\ker S\ge\Delta_\Lambda-d_{\rm int}
}
\tag{161.34}
\]

or an actual `N`-point unit-separated competitor of diameter strictly below `D(N)`.

The strain route is now more sharply partitioned:

1. Section 160 gives the strongest current free five-block construction and explicit
   support constant;
2. Section 161 proves that the quartic exponent cannot be improved inside the local
   rigid five-block translation model;
3. therefore an exponent-level improvement must change the finite architecture or
   allowed motions, while a direct use of the existing construction must attack
   exterior compatibility rather than translation scheduling.
