> Generated reading edition · [exact source](../../../docs/reports/target_c_chain_monotone_rows_2026-09-04.md) · source SHA-256 `7a488baf5c1f7d16be85f82c516ace24f92151256207433a5ee9d7bc656e884f`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-0E934405AC7B","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C: monotone off-chain rows and forced terminal twist

**Date:** 2026-09-04  
**Repository base:** `89c17412` plus branch commit `c6cc7744`  
**Run type:** exact geometric continuation of the C80 degree-four chain  
**Target:** Target C C-II, pure-rhombic C80 chain-face branch  
**Status:** proved working result; not yet promoted  
**LEVEL I STATUS:** STILL OPEN

The preceding branch report proves that every internal vertex of the exact C80 chain
has exactly one unit-contact neighbor on each side of the chain line. This report uses
only unit separation and the diameter bound to order those two neighbor rows.

The main conclusions are:

1. the upper off-chain contact angle is nonincreasing along the chain;
2. the lower off-chain contact angle is nondecreasing;
3. equality at one step is exactly the rhombic continuation step;
4. one side cannot have rhombi at **both** terminal chain edges, because that would
   create a second parallel length-`D` diameter segment;
5. consequently the first and last chain edges are both outer-boundary edges of the
   pure rhombic disk, and their outer sides are opposite;
6. after reflection if necessary, every upper off-chain contact along the chain points
   backward and every lower off-chain contact points forward, with an explicit
   `1/(2D)` longitudinal margin at the terminal rows.

This replaces the earlier picture of arbitrary alternating boundary breaks by a
one-sided monotone shear profile with a forced terminal twist.

---

## 1. Coordinates and the unique off-chain neighbors

Set

`p_(x_i)=i u`, `0<=i<=D`, `|u|=1`,

with `x_0=z`, `x_D=a`; translate so `p_z=0`.

For `1<=i<=D-1`, let

`y_i=x_i+v_i`

be the unique upper unit-contact neighbor and write

`v_i=(cos theta_i)u+(sin theta_i)Ju`,

where the degree-four theorem gives

`pi/3 < theta_i < 2pi/3`.

Let

`w_i=x_i+r_i`

be the unique lower neighbor. Write its oriented angle from `+u` as

`alpha_i in (-2pi/3,-pi/3)`,

so

`r_i=(cos alpha_i)u+(sin alpha_i)Ju`.

## 2. Adjacent upper contacts force monotone angle

Unit separation gives

`|y_(i+1)-y_i|>=1`.

But

`y_(i+1)-y_i=u+v_(i+1)-v_i`.

Put

`m=(theta_i+theta_(i+1))/2`,

`delta=(theta_(i+1)-theta_i)/2`.

A direct trigonometric expansion gives

`|u+v_(i+1)-v_i|^2-1
 =4 sin(delta) [sin(delta)-sin(m)].`

Because both angles lie in `(pi/3,2pi/3)`,

`sin(m)>sqrt(3)/2`,

while `|delta|<pi/6`, hence `|sin(delta)|<1/2`.

If `delta>0`, the first factor is positive and the bracket is negative, contradicting
unit separation. Therefore

`theta_(i+1)<=theta_i`.

If `delta<0`, both factors in the displayed product are negative and the product is
strictly positive. Hence equality in the distance bound occurs exactly when
`delta=0`.

### Lemma C-row-U

For `1<=i<D-1`,

`theta_(i+1)<=theta_i`,

with

`|y_(i+1)-y_i|=1  <=>  theta_(i+1)=theta_i`.

In the pure rhombic disk, the equality case is precisely the upper rhombus
continuation across `x_i x_(i+1)`: then

`y_(i+1)-y_i=u`.

A strict upper boundary break therefore gives a strict angle drop.

## 3. The lower row is monotone in the opposite oriented sense

The same calculation for

`w_(i+1)-w_i=u+r_(i+1)-r_i`

uses

`m=(alpha_i+alpha_(i+1))/2 in (-2pi/3,-pi/3)`

and hence

`sin(m)<-sqrt(3)/2`.

The unit-separation inequality now excludes `delta<0` and allows strict inequality only
for `delta>0`. Thus:

### Lemma C-row-L

For `1<=i<D-1`,

`alpha_(i+1)>=alpha_i`,

with

`|w_(i+1)-w_i|=1  <=>  alpha_(i+1)=alpha_i`.

Thus lower boundary breaks are strict increases of the oriented lower angle.

The upper and lower rows can have many breaks, but all upper jumps have one sign and
all lower jumps have the opposite oriented sign. Their total angular variations are
each strictly less than `pi/3`.

## 4. Two terminal rhombi on one side are impossible

Suppose, for contradiction, that the first and last chain edges

`x_0x_1`, `x_(D-1)x_D`

both have a rhombus on the upper side.

The first rhombus supplies an upper neighbor

`y_0=x_0+v_0`

with `v_0=v_1`. The last supplies

`y_D=x_D+v_D`

with `v_D=v_(D-1)`.

Apply the same adjacent-unit-separation calculation to the entire sequence
`y_0,...,y_D`. It gives

`theta_D<=...<=theta_0`.

Since all source distances are at most `D`,

`|y_D-y_0|=|D u+v_D-v_0|<=D`.

Monotonicity gives

`u dot (v_D-v_0)=cos(theta_D)-cos(theta_0)>=0`,

because cosine is decreasing on `(0,pi)` and `theta_D<=theta_0`.
Therefore

`|D u+v_D-v_0|^2
 =D^2+2D u dot(v_D-v_0)+|v_D-v_0|^2
 >=D^2`,

with equality only if `v_D=v_0`.

The diameter bound forces equality. Hence

`v_D=v_0`.

Since the angle sequence is monotone with equal endpoints, every `v_i` is the same
unit vector `v`. Thus

`y_i=x_i+v`

for all `0<=i<=D`, and

`|y_D-y_0|=D`.

So the source contains two distinct parallel diameter segments

`x_0x_D` and `y_0y_D`

separated by the nonzero translation `v`.

This is impossible in a set of diameter `D`. Indeed the two cross vectors are

`D u+v` and `D u-v`,

and

`|D u+v|^2+|D u-v|^2=2D^2+2>D^2+D^2`.

At least one cross distance would exceed `D`.

Therefore the upper side cannot have rhombi at both terminal chain edges. The same
argument applies to the lower side.

### Theorem C-terminal

For each side of the C80 chain, at least one of the two terminal chain edges has the
outer face on that side.

## 5. The two terminal chain edges are boundary edges on opposite sides

In a topological rhombic disk, a boundary edge has the outer face on exactly one side
and a rhombus on the other. An interior edge has rhombi on both sides.

The upper side needs at least one outer terminal incidence by Theorem C-terminal, and
the lower side needs at least one. There are only two terminal chain edges. One edge
cannot supply outer-face incidences on both sides.

Hence both terminal chain edges are boundary edges. Moreover their outer sides must be
opposite.

After reflecting across the chain line if needed, assume

- `x_0x_1` has the outer face above and a rhombus below;
- `x_(D-1)x_D` has a rhombus above and the outer face below.

This is the **forced terminal twist**.

It also implies that the chain line is not a supporting line of the convex hull: the
pure rhombic disk has source vertices on both sides of it. Thus these two terminal
chain edges are non-hull outer-boundary edges.

## 6. Every upper contact leans backward; every lower contact leans forward

The upper rhombus at the last edge gives a source point

`y_D=x_D+v_D`

with `v_D=v_(D-1)`.

Because `x_0` is a source point and the source diameter is `D`,

`|y_D-x_0|=|D u+v_D|<=D`.

Squaring gives

`D^2+1+2D cos(theta_D)<=D^2`,

hence

`cos(theta_D)<=-1/(2D)`.

Therefore

`theta_D>pi/2`.

The upper angles are nonincreasing, so for every internal chain vertex

`theta_i>=theta_(D-1)=theta_D>pi/2`.

Thus

`u dot v_i<0`

for every upper off-chain contact: the entire upper row leans back toward `z`.

Similarly, the lower rhombus at the first edge supplies

`w_0=x_0+r_0`, `r_0=r_1`.

The diameter constraint against `x_D` gives

`|x_D-w_0|=|D u-r_0|<=D`,

so

`cos(alpha_0)>=1/(2D)>0`.

Hence `alpha_0>-pi/2`. Since the lower angles are nondecreasing,

`alpha_i>=alpha_1=alpha_0>-pi/2`,

and therefore

`u dot r_i>0`

for every lower off-chain contact: the entire lower row leans forward toward `a`.

The opposite terminal-twist orientation gives the reflected statement.

### Corollary C-shear

Up to reflection, every internal C80 chain vertex has the exact contact pattern

```text
upper contact:  backward + upward
chain contacts: left and right
lower contact:  forward + downward
```

with upper angle monotone downward from left to right and lower oriented angle monotone
upward from left to right.

## 7. Quantitative virtual-row length bound

For the upper row,

`|y_(i+1)-y_i|
 <=1+|v_(i+1)-v_i|`.

Since the angles are monotone, the vectors `v_i` traverse a unit-circle arc of total
angle less than `pi/3`. Therefore

`sum_i |v_(i+1)-v_i|
 <= sum_i |theta_(i+1)-theta_i|
 < pi/3`.

Consequently every defined upper virtual row segment from index `r` to `s` has length
at most

`(s-r)+pi/3`.

The same bound holds for the lower row. Thus all boundary-break stretching accumulated
along either side is only `O(1)`, despite the possibility of `Theta(D)` distinct
breaks.

This is consistent with, but sharper in form than, a generic boundary-order shell
estimate.

## 8. Audit and remaining gap

- No endpoint contact is assumed unless a terminal rhombus supplies it.
- The parallel-diameter contradiction is exact and uses only the global diameter
  constraint.
- The forced terminal twist uses the pure disk fact that each terminal chain edge has
  exactly one outer-face side if it is a boundary edge.
- The monotonicity calculation is independent of KKT weights and independent of the
  train-coordinate formalism once the degree-four neighbors exist.
- The theorem does **not** eliminate internal boundary breaks. A monotone angle profile
  may have arbitrarily many arbitrarily small strict jumps.
- The `O(1)` total angular/virtual-length variation is not by itself incompatible with
  the global shell window, whose remaining error is `O(D)`.

The next closing question is whether this forced monotone terminal-twist strip can
coexist with the C87 paired full-span diameter staircase and the near-constant-width
hull. A direct route is to use the two terminal chain edges as explicit deep train
terminals in the C80/C83 train-coordinate system and propagate their one-sided support
depths through the ordered staircase.
