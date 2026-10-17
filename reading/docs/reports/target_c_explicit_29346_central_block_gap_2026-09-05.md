> Generated reading edition · [exact source](../../../docs/reports/target_c_explicit_29346_central_block_gap_2026-09-05.md) · source SHA-256 `bb4b1141ac35a7037feaff6cb5aa5a649e5762c6bc288249848a9587ede89a09`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-5D800045CE8C","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C explicit 2.9346 central-block gap

**Date:** 2026-09-05  
**Branch:** `research/target-c-c97-caterpillar-fan-capacity-2026-09-04`  
**Run type:** sharpened quantitative two-wall stability certificate  
**Target:** C80–C96 low-train chain-face branch  
**Status:** LEVEL I STILL OPEN

## 1. Result

### Theorem QJ1

Every asymptotic canonical C80–C96 chain-face survivor satisfies

`liminf T/D > 2.9346`.

This is a small but rigorous sharpening of QI1.  It uses exactly the audited
phase-complete central-block mechanism of CP1/TG1 and the exact TS4 envelope.  No
cross-side Cartesian assumption is introduced.

Write

`Delta=pi/(2sqrt(3))`,

`r=T/D-2`,

`G(z)=integral_0^z sqrt(1-3t^2/4) dt`,

`U(z)=G'(z)=sqrt(1-3z^2/4)`.

Assume for contradiction that a survivor subsequence satisfies

`r<=0.9346+o(1)`.

All train populations below are normalized by `D`, and all crossing counts by `D^2`.

## 2. Scalar slack is below 0.001524

Use the same elementary polynomial majorant

`G(z)<=P(z)`,

`P(z)=z-z^3/8-9z^5/640-27z^7/7168-45z^9/32768`.

At

`z=0.4673`,

direct rational-decimal evaluation gives

`P(z)<0.45421136`.

Together with

`Delta>0.90689968`,

this yields

`2G(0.4673)-Delta`

`<2(0.45421136)-0.90689968`

`<0.001524`.

Put

`delta=0.001524`.

As in QH1/QI1, every individual nonnegative one-side wall deficit or bad-crossing
capacity loss is smaller than `delta`.

## 3. Exact complement bound: q<0.0037

Let

`q_0=0.0037`.

By the exact-envelope transfer argument, if a feasible capacity point had `q>=q_0`,
complement mass could be transferred into the smaller side until `q=q_0` without
decreasing capacity.  It is therefore enough to rule out the fixed slice `q=q_0`.

At the worst train budget `r=0.9346`, use the full side budget

`lambda+mu=0.9309`.

Write

`m=0.46545`,

`lambda=m+d`,

`mu=m-d`,

`d>=0`.

For the star bad term define

`F(d)=G(m+d)+G(m-d)+q_0(m+d)`.

Then

`F'(d)=U(m+d)-U(m-d)+q_0`.

The difference

`U(m-d)-U(m+d)`

is increasing in `d`, and direct squaring gives at `d=0.01`

`U(m-0.01)-U(m+0.01)>0.0076>q_0`.

Hence the maximum of `F` lies in `0<=d<=0.01`.

On this interval

`-G''(z)=3z/(4U(z))>0.371`.

Therefore

`G(m+d)+G(m-d)<=2G(m)-0.371d^2`,

and consequently

`F(d)<=2G(m)+q_0m+q_0^2/(4*0.371)`.

The same polynomial majorant gives

`G(m)<0.4525190`.

Thus

`F(d)`

`<2(0.4525190)+0.0037(0.46545)+0.0037^2/1.484`

`<0.906770`

`<Delta`.

For the Mantel branch, concavity gives

`G(lambda)+G(mu)+q_0^2/4`

`<=2G(m)+q_0^2/4`

`<0.905042`

`<Delta`.

Both branches fail.  Hence

### (QJ2)

`q<0.0037`.

## 4. Both side populations exceed 0.403

Suppose `mu<=0.403`.  With the full population budget write

`lambda=0.9346-mu-q`.

For fixed `q<0.0037`, the star branch has derivative under transfer from `lambda` to
`mu`

`U(mu)-U(lambda)-q`.

Throughout `mu<=0.403`,

`U(mu)>=U(0.403)>0.9371`,

while

`lambda>=0.9346-0.403-0.0037=0.5279`,

so

`U(lambda)<=U(0.5279)<0.8894`.

Therefore

`U(mu)-U(lambda)-q`

`>0.9371-0.8894-0.0037`

`>0.044`.

The Mantel branch has the larger derivative `U(mu)-U(lambda)>0`.  Thus, for every
fixed admissible q, capacity on `mu<=0.403` is maximized at `mu=0.403`.

At `mu=0.403`, increasing q decreases both branches.  Indeed

`lambda<=0.5316`,

`U(lambda)>=U(0.5316)>0.8877`,

and therefore for the star branch

`-U(lambda)+lambda-q < -0.8877+0.5316<0`,

while for the Mantel branch

`-U(lambda)+q/2 < -0.8877+0.00185<0`.

Hence the maximum occurs at

`mu=0.403`, `q=0`, `lambda=0.5316`.

Direct evaluation of the same polynomial majorant gives

`G(0.5316)+G(0.403)`

`<0.906837`

`<Delta`.

Contradiction.  Therefore

### (QJ3)

`lambda>=mu>0.403`.

## 5. Each side has more than 0.3855 long rows

Fix one side of normalized population `a<=0.9346`, and let `b` be its population of
short rows crossing at most `D/2` exact chain tracks.  The audited replacement
inequality gives

`wall deficit >= b(U(a)-1/2)`.

Since

`U(a)>=U(0.9346)>0.5872`,

we obtain

`b<0.001524/0.0872<0.01748`.

Using QJ3, each side therefore has more than

`0.403-0.01748>0.3855`

normalized long-row population.

### (QJ4)

Each boundary side contains more than `0.3855D` long nested rows.

## 6. A common chain block from the p=0.33 prefixes

Choose

`p=0.330`,

`h=0.055`.

Then

`p+h=0.385<0.3855`,

so the whole stability window lies inside the long-row stack on each side.

Let `d(p)` be the normalized common exact-chain interval of the first `pD` deepest
long rows on one side.  The long-wall integral deficit is below `delta`, hence

`d(p)>=U(p+h)-delta/h-o(1)`.

Now

`U(0.385)>0.9427`,

so

`d(0.330)`

`>0.9427-0.001524/0.055-o(1)`

`>0.91499-o(1)`.

The two side intervals are consecutive subintervals of the same ordered D-track chain
family.  Their intersection therefore has normalized size greater than

`2(0.91499)-1>0.82998`.

Put

### (QJ5)

`M=0.82998`.

## 7. Residual phase block

The two selected side prefixes contain `2pD=0.660D` chain-adjacent residual trains.
The chain orbit has only two leading residual projective phases.  Therefore one phase,
call it B, occurs at least

### (QJ6)

`pD=0.330D-o(D)`

times in their union.

By CP1, the retained B-trains form a central contiguous block in the global order of
the B phase.  Omitted B-trains lie outside its extremal tracks and do not separate the
central grid corners.  Exact chain tracks outside the consecutive M-block likewise do
not separate those corners.

Thus the M center tracks and the B leaf block form a genuine complete topological grid
with no same-phase leakage.

## 8. Two actual diagonals exceed D

Trim an arbitrarily small fixed fraction from the complete grid and then take the
asymptotic limit.  Let the coherent center and leaf vector sums be `U_0,V_0`.  The
other chain-adjacent residual phase lies on the third triangular projective line `w`
and may contribute an arbitrary real multiple of `w`.

The two actual grid diagonals have principal parts

`U_0+V_0`,

`U_0-V_0`.

Project perpendicular to `w`.  Since the center and B directions are the other two
triangular directions,

`max(|det(U_0+V_0,w)|,|det(U_0-V_0,w)|)`

`>= (sqrt(3)/2)(M+p-o(1))D`.

This uses only the scalar identity

`max(|A+B|,|A-B|)=|A|+|B|`.

The full atomic complement contributes norm at most `qD<0.0037D`.  By TG1, every
nonleading train which separates a trimmed diagonal spends `Omega(D)` crossings in the
complete grid; the total such crossing mass is `o(D^2)`, so only `o(D)` of these trains
contribute.

Hence one actual source distance is at least

`[(sqrt(3)/2)(M+p)-0.0037-o(1)]D`.

Using the safe bound `sqrt(3)/2>0.866`,

`(sqrt(3)/2)(M+p)-0.0037`

`>0.866(0.82998+0.330)-0.0037`

`>1.0008`.

Choose the fixed trim small enough to preserve the positive margin, then let `D` grow.
The resulting source distance is strictly greater than D, contradiction.

## 9. Conclusion

No canonical C80–C96 chain-face survivor has a subsequential limit with

`T/D<=2.9346`.

Therefore

`liminf T/D > 2.9346`.

The present constant chain has only about `8*10^(-4)D` final projected-distance
margin.  Numerical optimization of this same proof template fails near
`T/D=2.93465`; further useful progress should therefore change the structural input,
not continue decimal tuning.  The most promising additions are C93's quadratic
secondary-separator demand and C96's near-spanning common-cut caterpillar.
