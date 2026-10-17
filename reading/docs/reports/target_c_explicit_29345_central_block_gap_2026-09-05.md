> Generated reading edition · [exact source](../../../docs/reports/target_c_explicit_29345_central_block_gap_2026-09-05.md) · source SHA-256 `190d619e4244f7601981e919762a475a6cef85a99454759f12f4da1291b9e1b9`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-C8AA001E0F81","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C explicit 2.9345 central-block gap

**Date:** 2026-09-05  
**Branch:** `research/target-c-c97-caterpillar-fan-capacity-2026-09-04`  
**Run type:** sharpened quantitative two-wall stability certificate  
**Target:** C80–C96 low-train chain-face branch  
**Status:** LEVEL I STILL OPEN

## 1. Result

### Theorem QI1

Every asymptotic canonical C80–C96 chain-face survivor satisfies

`liminf T/D > 2.9345`.

The proof is the same phase-complete central-grid mechanism as the explicit `2.934`
report, with tighter but still elementary constants.  The two-diagonal formulation is
used throughout, so no orientation sign is hidden.

Write

`Delta=pi/(2sqrt(3))`,

`r=T/D-2`,

`G(z)=integral_0^z sqrt(1-3t^2/4) dt`,

`U(z)=G'(z)=sqrt(1-3z^2/4)`.

Assume for contradiction that a survivor subsequence satisfies

`r<=0.9345+o(1)`.

## 2. Scalar slack

Use the same polynomial upper bound

`G(z)<=P(z)`

with

`P(z)=z-z^3/8-9z^5/640-27z^7/7168-45z^9/32768`.

At

`z=0.46725`

direct decimal evaluation gives

`P(z)<0.45416564`.

Together with

`Delta>0.90689968`

this yields

`2G(0.46725)-Delta`

`<2(0.45416564)-0.90689968`

`<0.001432`.

Put

`delta=0.001432`.

As before, every individual nonnegative good-wall or bad-crossing capacity loss is
smaller than `delta`.

## 3. Complement mass satisfies q<0.0035

Let

`q_0=0.0035`.

The exact-envelope transfer argument reduces any putative point with `q>=q_0` to one
with exactly `q=q_0` without decreasing capacity.  At the worst train budget
`r=0.9345`, put

`lambda+mu=0.931`,

`m=0.4655`,

`lambda=m+d`,

`mu=m-d`.

For the star bad term define

`F(d)=G(m+d)+G(m-d)+q_0(m+d)`.

The derivative is

`F'(d)=U(m+d)-U(m-d)+q_0`.

The difference

`U(m-d)-U(m+d)`

is increasing in `d`, and at `d=0.01` it exceeds `0.0076>q_0`.  Hence the maximum of
`F` lies in `[0,0.01]`.

On that interval

`-G''(z)>0.371`,

so

`G(m+d)+G(m-d)<=2G(m)-0.371d^2`.

Therefore

`F(d)<=2G(m)+q_0m+q_0^2/(4*0.371)`.

The polynomial bound gives

`G(m)<0.45256472`,

and consequently

`F(d)<2(0.45256472)+0.0035(0.4655)+0.0035^2/1.484`

`<0.906767`

`<Delta`.

For the Mantel branch, concavity gives

`G(lambda)+G(mu)+q_0^2/4`

`<=2G(m)+q_0^2/4`

`<0.905133`

`<Delta`.

Thus

### (QI2)

`q<0.0035`.

## 4. Both side populations exceed 0.4

Suppose `mu<=0.4`.  Use the full side budget

`lambda=0.9345-mu-q`.

For the star branch,

`d/dmu [G(lambda)+G(mu)+lambda q]`

`=U(mu)-U(lambda)-q`.

Here

`U(mu)>=U(0.4)>0.938`,

while

`lambda>=0.9345-0.4-0.0035=0.531`

and hence

`U(lambda)<=U(0.531)<0.889`.

So the derivative is larger than

`0.938-0.889-0.0035>0.045`.

The Mantel branch is even more strongly increasing in `mu`.  Therefore both branches
are maximized at `mu=0.4`.

At `mu=0.4`, increasing q decreases either branch: `lambda<=0.5345`, while
`U(0.5345)>0.886`, making

`-U(lambda)+lambda-q<0`

and

`-U(lambda)+q/2<0`.

The maximum therefore occurs at

`mu=0.4`, `q=0`, `lambda=0.5345`.

The polynomial bound gives

`G(0.5345)+G(0.4)<0.906597<Delta`.

Contradiction. Hence

### (QI3)

`lambda>=mu>0.4`.

## 5. Long-row supply

On either side let `b` be the short-row population.  The same replacement inequality
as before gives

`wall deficit >= b(U(a)-1/2)`.

For `a<=0.9345`,

`U(a)>0.5873`,

so

`b<0.001432/0.0873<0.01641`.

Together with QI3, each side has more than

### (QI4)

`0.38359D`

long nested rows.

## 6. A common 0.8331D chain block

Take

`p=0.329`,

`h=0.053`.

Then

`p+h=0.382<0.38359`,

so this whole stability window lies inside the long-row stack on each side.

The long-wall integral deficit is below `delta`.  Therefore

`d(p)>=U(p+h)-delta/h-o(1)`.

Now

`U(0.382)>0.9436`,

so

`d(0.329)>0.9436-0.001432/0.053-o(1)`

`>0.91658-o(1)`.

The two side intervals are consecutive subintervals of the same D-track chain order.
Their intersection therefore has normalized size greater than

`2(0.91658)-1>0.8331`.

Put

### (QI5)

`M=0.8331`.

## 7. Residual leaf block

The two selected prefixes contain

`2pD=0.658D`

chain-adjacent residual trains.  There are only two leading residual projective
phases, so one phase B occurs at least

### (QI6)

`pD=0.329D-o(D)`

times.

By the central-stack order lemma, those retained B-trains form one contiguous block in
the global order of the B phase.  Omitted B-trains lie outside its extremal tracks and
do not separate the central grid corners.  The same is true for exact chain tracks
outside the consecutive M-block.

Thus the M center tracks and the B leaf block form a genuine complete topological grid
with no same-phase leakage.

## 8. Two diagonals force a distance above D

Trim an arbitrarily small fixed fraction from the complete grid.  Let the center and
leaf vector sums be `U_0,V_0`.  The other chain-adjacent residual phase lies on the
third triangular projective line `w` and may contribute an arbitrary multiple of `w`
to either diagonal.

The two actual grid diagonals have principal parts

`U_0+V_0`,

`U_0-V_0`.

Project perpendicular to `w`.  Independently of all orientation signs,

`max(|det(U_0+V_0,w)|,|det(U_0-V_0,w)|)`

`>= (sqrt(3)/2)(M+p-o(1))D`.

The entire atomic complement can alter either difference by norm at most `qD`, with
`q<0.0035`.  Nonleading/non-atomic trains which penetrate the fixed trimmed grid have
only `o(D^2)` total crossings with it; TG1 therefore leaves only `o(D)` such diagonal
contributors.

Hence one actual source distance is at least

`[(sqrt(3)/2)(M+p)-0.0035-o(1)]D`.

Use

`sqrt(3)/2>0.866`.

Then

`(sqrt(3)/2)(M+p)-0.0035`

`>0.866(0.8331+0.329)-0.0035`

`>1.0029`.

Choose the fixed trim sufficiently small that the positive margin remains.  The
resulting source distance is greater than D, contradiction.

## 9. Conclusion

No canonical C80–C96 chain-face survivor has a subsequential limit with

`T/D<=2.9345`.

Therefore

`liminf T/D > 2.9345`.

The method is now operating close to its coarse-constant limit: the final certified
margin is only about `0.0029D`.  Further decimal improvement is possible but is less
useful than proving a phase-resolved wall-capacity theorem or combining the central
block with C93/C96.
