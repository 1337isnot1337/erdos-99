<!-- theorem-state: {"artifact_id":"ART-6EFE5808EFA6","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C explicit 2.934 central-block gap

**Date:** 2026-09-05  
**Branch:** `research/target-c-c97-caterpillar-fan-capacity-2026-09-04`  
**Run type:** quantitative exact-envelope stability plus phase-complete grid  
**Target:** C80–C96 low-train chain-face branch  
**Status:** LEVEL I STILL OPEN

## 1. Result

### Theorem QH1

Every asymptotic canonical C80–C96 chain-face survivor satisfies

`liminf T/D > 2.934`.

This strengthens the preceding explicit `2.933` theorem.  The proof uses the exact
three-variable TS4 envelope, not the older incompatible cross-wall relaxation.  The
two boundary sides are coupled only after a genuine common train block is extracted;
the final distance estimate uses the two actual diagonals of that complete grid.

Write

`Delta=pi/(2sqrt(3))`,

`r=T/D-2`,

`G(z)=integral_0^z sqrt(1-3t^2/4) dt`,

`U(z)=G'(z)=sqrt(1-3z^2/4)`.

Assume for contradiction that a survivor subsequence has

`r<=0.934+o(1)`.

All crossing counts below are divided by `D^2` and all train populations by `D`.

## 2. Scalar-envelope slack is below 0.000975

The exact two-side capacity theorem gives

`Delta <= G(lambda)+G(mu)+max(lambda q,q^2/4)`

for

`lambda>=mu>=0`, `q>=0`, `lambda+mu+q<=r`,

and its exact envelope is

`2G(r/2)`.

Use the elementary binomial upper bound

`sqrt(1-x) <= 1-x/2-x^2/8-x^3/16-5x^4/128`

for `0<=x<1`.  With `x=3t^2/4`, integration gives

`G(z) <= P(z)`

where

`P(z)=z-z^3/8-9z^5/640-27z^7/7168-45z^9/32768`.

At `z=0.467`, direct decimal evaluation gives

`P(0.467)<0.45393701`.

The safe elementary bounds

`pi>3.1415926535`,

`sqrt(3)<1.732050808`

give

`Delta>0.90689968`.

Therefore

`2G(0.467)-Delta`

`<2(0.45393701)-0.90689968`

`<0.000975`.

Put

`delta=0.000975`.

Every nonnegative capacity deficit used below is individually smaller than `delta`.

## 3. Exact complement bound: q<0.0023

The crude transfer estimate `q<=delta/(1-r)` is wasteful at `r=0.934`.  We instead
use the exact fixed-q optimization.

Let

`q_0=0.0023`.

The transfer argument in the exact-envelope theorem says that reducing complement mass
and moving it into the two side populations never decreases capacity.  Hence, if a
configuration with `q>=q_0` were feasible, there would be a feasible capacity point
with exactly `q=q_0`.  It is enough to rule out that slice.

At fixed `q_0`, capacity is increasing with unused side mass, so put

`lambda+mu=0.934-q_0=0.9317`.

Write

`m=0.46585`,

`lambda=m+d`,

`mu=m-d`,

`0<=d<=m`.

### 3.1 Star bad term

For the `lambda q_0` branch define

`F(d)=G(m+d)+G(m-d)+q_0(m+d)`.

Its derivative is

`F'(d)=U(m+d)-U(m-d)+q_0`.

The function

`H(d)=U(m-d)-U(m+d)`

is strictly increasing for `d>0`, because `-G''(z)` is positive.  Direct square-root
bounds give

`H(0.01)>0.0076>q_0`.

Thus `F` is decreasing for every `d>=0.01`; its maximum lies in `[0,0.01]`.

On this interval

`-G''(z)=3z/(4U(z))>0.372`

for every `z in [m-0.01,m+0.01]`.  Hence the symmetric sum is strongly concave:

`G(m+d)+G(m-d) <= 2G(m)-0.372 d^2`.

Therefore

`F(d) <= 2G(m)+q_0 m+q_0^2/(4*0.372)`.

The polynomial bound above gives

`G(m)<0.4528850`,

so

`F(d)<2(0.4528850)+0.0023(0.46585)+0.0023^2/1.488`

`<0.90684502`

`<Delta`.

### 3.2 Mantel bad term

For the `q_0^2/4` branch, concavity of `G` gives

`G(lambda)+G(mu)+q_0^2/4`

`<=2G(m)+q_0^2/4`

`<0.905772`

`<Delta`.

Both branches fail.  Consequently

### (QH2)

`q<0.0023`.

## 4. Both side populations exceed 0.4

We next prove

`mu>0.4`.

Suppose `mu<=0.4`.  For fixed `q<0.0023`, use the full population budget

`lambda=0.934-mu-q`.

For the star branch, differentiating while moving mass from `lambda` to `mu` gives

`d/dmu [G(lambda)+G(mu)+lambda q]`

`=U(mu)-U(lambda)-q`.

In this range

`U(mu)>=U(0.4)>0.938`,

while

`lambda>=0.934-0.4-0.0023=0.5317`

and hence

`U(lambda)<=U(0.5317)<0.888`.

Therefore the derivative is greater than

`0.938-0.888-0.0023>0.047`.

The Mantel branch has the still larger derivative `U(mu)-U(lambda)>0`.  Thus for each
fixed q the capacity is maximized at `mu=0.4`.

At `mu=0.4`, both bad-term branches decrease as q increases.  Indeed, with
`lambda<=0.534`,

`d/dq [G(lambda)+lambda q]`

`=-U(lambda)+lambda-q`

`< -U(0.534)+0.534<0`,

and

`d/dq [G(lambda)+q^2/4]`

`=-U(lambda)+q/2<0`.

So the maximum over `mu<=0.4` occurs at

`mu=0.4`, `q=0`, `lambda=0.534`.

The same polynomial upper bound gives

`G(0.534)+G(0.4)`

`<0.51430374+0.39184947`

`<0.906154`

`<Delta`.

Contradiction.  Hence

### (QH3)

`lambda>=mu>0.4`.

## 5. Each side has more than 0.3889 long nested rows

Fix one side with total population `a<=0.934`.  Let `b` be the normalized population
of short rows crossing at most `D/2` exact chain tracks.  The long rows contribute at
most `G(a-b)`, while the short rows contribute at most `b/2`.  Thus the loss from the
full one-side capacity is at least

`G(a)-G(a-b)-b/2`

`>=b(U(a)-1/2)`.

Since

`U(a)>=U(0.934)>0.5879`,

one unit of short-row population costs more than `0.0879` in normalized capacity.
The wall deficit is below `delta=0.000975`, so

`b<0.000975/0.0879<0.0111`.

Together with QH3, each side therefore has more than

### (QH4)

`0.3889D`

long rows.  Their crossing intervals are nested by the audited same-side wall theorem.

## 6. Deep 0.34-prefixes share a 0.842 chain block

Order the long rows of one side by decreasing exact-chain interval length.  Let `d(t)`
be the normalized common interval length of the first `tD` rows.  The wall
parallelogram gives

`d(t)<=U(t)+o(1)`.

As noted above, the long-row integral deficit is itself below `delta`.

Choose

`p=0.34`,

`h=0.045`.

QH4 ensures

`p+h=0.385<0.3889`,

so the interval `[p,p+h]` lies inside the long-row stack.  Nestedness gives

`delta`

`> integral_p^(p+h) (U(t)-d(t)) dt`

`>=h(U(p+h)-d(p))+o(1)`.

Now

`U(0.385)>0.9427`.

Hence

`d(0.34)>0.9427-0.000975/0.045-o(1)`

`>0.9210-o(1)`.

Thus on each boundary side the deepest `0.34D` long rows cross a common consecutive
interval of more than `0.9210D` exact chain tracks.

The two side intervals lie in the same ordered D-track chain family.  Their
intersection is consecutive and has normalized size greater than

`2(0.9210)-1=0.8420`.

Put

### (QH5)

`M=0.8420`.

We have a common consecutive center block of more than `(M-o(1))D` exact chain tracks.

## 7. Extract a contiguous residual-phase leaf block of size 0.34D

The two selected side prefixes contain

`0.68D+o(D)`

chain-adjacent residual trains.  There are only two leading projective residual
phases, at `+60 degrees` and `-60 degrees` from the chain direction.  Therefore one
phase, call it B, occurs at least

### (QH6)

`0.34D-o(D)`

times in the union of the two prefixes.

Within either side wall, any B-row omitted after the selected mixed-phase prefix is
shallower than every retained B-row.  The central-stack order lemma CP1 therefore says
that the retained B-rows from the two sides form one contiguous block in the global
order of the noncrossing B-phase family.  B-tracks omitted outside this block do not
separate vertices inside the strip bounded by its extremal tracks.

Likewise, exact chain tracks outside the consecutive common center block from QH5 do
not separate vertices inside its strip.

Consequently the retained center and B families form a genuine complete topological
train grid of normalized dimensions at least

`M=0.8420`,

`b=0.34`,

with no displacement leakage from omitted tracks in those same two phases.

## 8. Two-diagonal estimate removes every phase-orientation sign

Trim an arbitrarily small fixed fraction from the two complete grid families as in
TG1.  Let their coherent vector sums be `U_0` and `V_0`.  Up to `o(D)` angular error,

`|U_0|=(M-o(1))D`,

`|V_0|=(b-o(1))D`.

Let the other chain-adjacent residual phase have projective line `w`.  Its contribution
to either grid diagonal may be an arbitrary real multiple of `w`; we impose no
population restriction on it.

The four grid corners supply two source differences whose principal parts are

`U_0+V_0`,

`U_0-V_0`.

Project both onto the one-dimensional quotient perpendicular to `w`.  The chain and B
projective lines are the other two triangular directions, so, regardless of orientation
choices,

`max(|det(U_0+V_0,w)|, |det(U_0-V_0,w)|)`

`>= (sqrt(3)/2)(M+b-o(1))D`.

Indeed the two determinant values have the form `A+B` and `A-B` up to sign, with

`|A|=(sqrt(3)/2)|U_0|`,

`|B|=(sqrt(3)/2)|V_0|`,

and `max(|A+B|,|A-B|)=|A|+|B|`.

Thus one of the two actual diagonals retains this full transverse component even after
**arbitrary** coherent cancellation by the opposite residual phase.

The atomic complement has population `qD`, so its entire vector contribution to either
diagonal has norm at most `qD`.  By QH2 this costs less than `0.0023D`.

All remaining non-atomic / nonleading-phase train crossings with a positive-density
complete grid are `o(D^2)`.  TG1 says that, after the fixed trim, every such train
which separates a selected diagonal must spend `Omega(D)` crossings through the grid.
Therefore only `o(D)` of them contribute, for an additional `o(D)` vector error.

Hence some source distance is at least

`[(sqrt(3)/2)(M+b)-0.0023-o(1)]D`.

Using the safe bound

`sqrt(3)/2>0.866`,

we obtain

`(sqrt(3)/2)(M+b)-0.0023`

`>0.866(0.8420+0.34)-0.0023`

`>1.021`.

The arbitrarily small fixed trim may be chosen to preserve a positive margin above
one.  This contradicts the global diameter D.

## 9. Conclusion

No canonical C80–C96 chain-face survivor sequence can have a subsequential limit with

`T/D<=2.934`.

Therefore

`liminf T/D > 2.934`.

The remaining numerical window below the C94 transition is

`2.934 < T/D < 3`.

The next improvement should optimize the same finite stability mechanism or replace
the coarse one-phase pigeonhole `b>=p` by a phase-resolved wall-capacity inequality.