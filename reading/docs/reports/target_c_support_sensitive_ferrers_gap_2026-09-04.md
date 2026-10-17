> Generated reading edition · [exact source](../../../docs/reports/target_c_support_sensitive_ferrers_gap_2026-09-04.md) · source SHA-256 `32e1f8ed4d6073188aa864f75e710726ecd077b68f81a922181794d1fe7b25e6`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-AA5618F107DA","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C support-sensitive Ferrers gap

**Date:** 2026-09-04  
**Repository base:** research branch after `8499b779`  
**Run type:** exact support-sensitive refinement of C91-C92  
**Target:** pure-rhombic C80-C96 chain-face branch  
**Status:** LEVEL I STILL OPEN

## 1. Result

Write

`Delta=pi/(2sqrt(3))=0.90689968...`.

C92 treated all chain-orbit residual atomic trains with one four-wall Ferrers bound.
That is sharp at the C89 endpoint, where the limiting phase support is the star

`B -- A -- C`

centered at the exact chain phase `A`. Away from the endpoint, however, the scalar
bad-crossing extremizer can switch to the path

`A -- B -- C`.

In that path only the `B` phase can carry positive-density crossings with the exact
chain family `P`; hence only **two**, not four, boundary walls carry good chain
crossings.

Keeping the star and path cases separate yields a much larger explicit gap.

### Theorem S1 — support-sensitive train surplus

Every asymptotic canonical pure-rhombic C80-C96 chain-face survivor satisfies

`liminf T/D > 2.91`.

This replaces the `2.9071996821...` bound from the exact bad-crossing refinement and
the older C92 bound `2.9069996821...`.

The proof uses only already-established phase-atomic structure, the C91 wall geometry,
and elementary mass accounting. It does not use C78's track-degree bound.

## 2. Normalize by D rather than T

Pass to a subsequence with

`x=T/D <=2.91`

and put

`r=x-2 <=0.91`.

The C87 endpoint count gives `q/D>=2+o(1)`. As in C92, Target B Section 39 then gives
total atomic train mass at most `1-1/x` in T-normalization. Since the exact C80 chain
family `P` has T-normalized mass `1/x`, the number of atomic trains outside `P` is at
most

`rD+o(D)`.

The total leading train-crossing count is

`Delta D^2+o(D^2)`.

The limiting phase graph is supported on the three-point projective `60-degree`
orbits and is triangle-free.

Call a leading crossing **good** if one endpoint is an exact chain train in `P`.
All other leading crossings are **bad**.

## 3. Star support

First suppose the chain phase orbit has two positive-density chain-residual edges and
no residual-residual edge. This is the star support

`B -- A -- C`,

where `A` is the chain phase.

Let

- `sD` be the total population of the two residual chain-orbit phases `B,C`;
- `eD` be extra atomic train mass parallel to `P`;
- `tD` be atomic mass in all other phase orbits.

Then

`e+s+t <= r`.

Because the chain orbit is a star, bad crossings inside it use the extra chain-parallel
mass and have capacity at most

`es D^2`.

All other phase orbits together are triangle-free on `tD+o(D)` trains, so weighted
Mantel gives bad capacity at most

`t^2 D^2/4`.

Thus, if `B` is the bad leading crossing coefficient in units of `D^2`,

`B <= es+t^2/4`.

For `r<1`,

`es+t^2/4 <= r(e+t) <= r(r-s)`.

Hence the good chain-crossing coefficient `g` satisfies

`g >= Delta-r(r-s)`.

### Four-wall capacity

Each of the two residual phase directions splits according to which of the two
`z`--`a` hull arcs contains its train terminals. Thus there are at most four walls.

Among the `sD+o(D)` residual trains, the number of missing incidences with the exact
`D` chain trains is

`(s-g)D^2+o(D^2)`.

Delete every residual train crossing at most `D/2` chain trains. Such a row misses at
least `D/2`, so all deleted rows together contribute at most

`(s-g)D^2+o(D^2)`

good crossings.

Inside each remaining wall, all intervals have length greater than `D/2`; the C90-C91
same-wall laminarity therefore forces them to be nested. If a wall has `lambda D`
rows, the C91 parallelogram argument bounds its crossing count by

`F(lambda)D^2+o(D^2)`,

where

`F(lambda)=integral_0^lambda sqrt(1-t^2)dt`.

Concavity of `F` over the four walls gives

`g <=4F(s/4)+(s-g)`.

Therefore every star survivor must satisfy

`2g <=4F(s/4)+s`.

Using the lower bound on `g`, a necessary condition is

`H_r(s):=4F(s/4)+s-2Delta+2r(r-s) >=0`.

## 4. The star condition is impossible for r<=0.91

For `0<=s<=r<=0.91`,

`H_r'(s)=sqrt(1-(s/4)^2)+1-2r`.

Since `s/4<=0.2275`, the square-root term is greater than `0.94`; hence

`H_r'(s)>0.94+1-1.82>0`.

Thus `H_r` is increasing and

`H_r(s)<=H_r(r)=4F(r/4)+r-2Delta`.

The right side is increasing in `r`, so it is at most its value at `r=0.91`.

Use

`sqrt(1-t^2)<=1-t^2/2`

on `[0,1]`. Then

`F(z)<=z-z^3/6`,

and hence

`4F(0.91/4)+0.91-2Delta`

`<=1.82-2Delta-0.91^3/96`.

The safe elementary numerical bound `Delta>0.9068` gives

`1.82-2Delta-0.91^3/96`

`<0.0064-0.00784<0`.

Therefore `H_r(s)<0` for every allowed `s`, contradicting the necessary star
condition.

So the star phase support is impossible whenever `x<=2.91`.

## 5. Path support is even more restrictive

Now suppose the chain orbit has support

`A -- B -- C`,

with no positive-density `A-C` edge. Only the `B` phase can carry good crossings with
`P`.

Let `sD` be the population of this `B` phase. All atomic mass not in `P` or `B` is at
most `(r-s)D+o(D)`. The same coarse accounting as above gives

`bad coefficient <= r(r-s)`,

so again

`g>=Delta-r(r-s)`.

But now the good `P-B` crossings split into only **two** side walls. Repeating the
C91 deletion and nesting argument gives

`2g <=2F(s/2)+s`.

Thus a necessary condition is

`K_r(s):=2F(s/2)+s-2Delta+2r(r-s)>=0`.

For `r<=0.91`,

`K_r'(s)=sqrt(1-(s/2)^2)+1-2r>0`,

so its maximum is at `s=r`. Since `F` is concave and `F(0)=0`,

`2F(r/2)<=4F(r/4)`.

Therefore

`K_r(r)<=H_r(r)<0`.

The path support is impossible as well.

The one-edge subcases are dominated by the path estimate. If the chain phase has no
positive-density edge at all, all leading crossings occur among at most `rD+o(D)`
non-chain atomic trains; Mantel gives at most `r^2D^2/4<Delta D^2`, impossible.

These cases exhaust the triangle-free support graphs on the chain three-phase orbit.

## 6. Conclusion

No asymptotic canonical chain-face survivor can satisfy

`T/D<=2.91`.

Hence

`liminf T/D>2.91`.

The gain comes from retaining one bit of combinatorial information discarded by C92:
whether the chain-orbit phase graph is a star or a path. The path escape cannot borrow
the star's four good walls.

## 7. Next target

The scalar support-sensitive argument stops once the four-wall star capacity becomes
large enough, at a value only slightly above `2.91`. To move toward `T/D=3`, one must
use additional geometry.

The best available next input is C78:

`deg_Gamma(tau)<2D/sqrt(3)`

for every train. In the dangerous three-phase path, the central phase must carry both
the `A-B` and `B-C` crossing blocks. Its per-train width/degree budget therefore
couples the good and bad blocks in a way not used above. The C93/C96 ordered
diameter structure remains the other independent route.
