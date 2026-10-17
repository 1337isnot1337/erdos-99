> Generated reading edition · [exact source](../../../docs/reports/target_c_explicit_2933_central_block_gap_2026-09-05.md) · source SHA-256 `eab173c8ab2eb94f0d6d997ebe4da3f1cd2304d7e54cf8d1f3a3948f9a6da553`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-B4453F3F8EC0","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C explicit 2.933 central-block gap

**Date:** 2026-09-05  
**Branch:** `research/target-c-c97-caterpillar-fan-capacity-2026-09-04`  
**Run type:** quantitative two-wall stability plus phase-complete central grid  
**Target:** C80–C96 low-train chain-face branch  
**Status:** LEVEL I STILL OPEN

## 1. Result

This report makes the central-phase-block repair quantitative and improves the audited
chain-face train bound to

### Theorem QG1

Every asymptotic canonical C80–C96 chain-face survivor satisfies

`liminf T/D > 2.933`.

The proof does **not** use the invalid cross-wall C91 Cartesian assumption.  Cross-side
geometry is used only to identify ordered central train blocks.  The source-difference
formula comes from the valid TG1 train-coordinate grid.

## 2. Exact scalar envelope and a numerical slack certificate

Write

`Delta=pi/(2sqrt(3))`,

`r=T/D-2`,

and

`G(z)=integral_0^z sqrt(1-3t^2/4) dt`.

The exact audited two-side envelope gives, for `0<=r<=1`,

`Delta <= G(lambda)+G(mu)+max(lambda q,q^2/4)`

with

`lambda>=mu>=0`, `q>=0`, `lambda+mu+q<=r`,

and

`G(lambda)+G(mu)+max(lambda q,q^2/4) <= 2G(r/2)`.

Assume for contradiction that a subsequence has

`r<=0.933+o(1)`.

We need a safe upper bound on

`delta_0:=2G(0.933/2)-Delta`.

Put `z=0.4665`.  From

`sqrt(1-x) <= 1-x/2-x^2/8-x^3/16-5x^4/128`

for `0<=x<1`, with `x=3t^2/4`, integration gives

`G(z)`

`<= z-z^3/8-9z^5/640-27z^7/7168-45z^9/32768`

`<0.45347967`.

Also the elementary decimal bounds

`pi>3.1415926535`,

`sqrt(3)<1.732050808`

imply

`Delta>0.90689968`.

Hence

`delta_0 < 2(0.45347967)-0.90689968`

`<0.00005966`

and in particular

### (QG2)

`delta_0<6*10^(-5)`.

Every capacity loss used below is normalized by `D^2`.

## 3. Complement atomic mass is below 0.000896 D

The proof of the exact envelope eliminates complement mass by moving it into the two
chain-adjacent side populations.

For the `lambda q` branch, moving one unit from `q` to the smaller side changes the
capacity at rate

`G'(mu)-lambda`.

For `0<=mu<=lambda` and `lambda+mu<=r<=0.933`,

`G'(mu)=sqrt(1-3mu^2/4)>=1-mu`,

so

`G'(mu)-lambda >=1-(lambda+mu)>=1-r>=0.067`.

When the two sides become equal, splitting further transferred mass equally between
them has an even larger positive derivative.

For the `q^2/4` branch, the one-variable envelope

`2G((r-q)/2)+q^2/4`

has derivative

`-G'((r-q)/2)+q/2`,

whose absolute value is also larger than `1-r` on this range.

Therefore retaining complement mass `q` loses at least

`(1-r)q >=0.067 q`

relative to the exact envelope.  Since a survivor has capacity at least `Delta`, QG2
gives

### (QG3)

`q < (6*10^(-5))/0.067 < 0.000896`.

This bound is deliberately coarse; the actual optimized `q` near 2.933 is much
smaller.

## 4. Both side populations exceed 0.35 D

Suppose `mu<=0.35`.  Since `lambda+mu<=r`, monotonicity and concavity of `G` give

`G(lambda)+G(mu)`

`<=G(0.933-mu)+G(mu)`

`<=G(0.583)+G(0.35)`.

The same binomial upper bound used in Section 2 gives

`G(0.583)+G(0.35)<0.901752`.

The bad term is at most

`0.933 q <0.000836`

by QG3.  Thus the whole TS4 capacity would be below

`0.902588<Delta`,

a contradiction.  Therefore

### (QG4)

`mu>0.35`,

and hence both boundary-side populations exceed `0.35D+o(D)`.

## 5. Fewer than 0.00068 D rows per wall are short

Fix one side with total normalized population `a<=0.933`.  Split its rows into

- `bD` short rows crossing at most `D/2` exact chain tracks;
- `(a-b)D` long rows.

Long rows have the nested one-side capacity `G(a-b)D^2+o(D^2)`, while the short rows
contribute at most `bD^2/2`.  Hence the loss from the full `G(a)` capacity is at least

`G(a)-G(a-b)-b/2`

`>=b(G'(a)-1/2)`.

On `a<=0.933`,

`G'(a)>=G'(0.933)`

`=sqrt(1-3(0.933)^2/4)`

`>0.589`.

So each unit of short-row population costs more than `0.089D^2` in capacity.

The combined good-wall capacity deficit is at most the total scalar slack `delta_0`:
if `e_good` and `e_bad` are the actual normalized leading good and bad crossing counts,
then

`(G(lambda)+G(mu)-e_good)`

`+(B_cap-e_bad)`

`<=2G(r/2)-Delta<=delta_0`,

and both summands are nonnegative.

Thus each wall individually has capacity deficit below `6*10^(-5)`, and therefore

### (QG5)

`b < (6*10^(-5))/0.089 < 0.00068`.

By QG4, each wall consequently contains more than

`0.3493D`

long nested rows.

## 6. A 0.3D deepest prefix crosses more than 0.9541D common chain tracks

Order the long rows in either wall by decreasing interval length.  Write `d(t)D` for
the common exact-chain interval of the first `tD` rows.  The one-side parallelogram
bound gives

`d(t)<=U(t)+o(1)`,

where

`U(t)=sqrt(1-3t^2/4)`.

The long-row capacity deficit is at most the full wall deficit, hence below
`6*10^(-5)D^2`.

Take

`p=0.30`,

`h=0.04`.

QG4–QG5 ensure that `p+h=0.34` lies strictly inside the long-row population on both
sides.  Since the nested row lengths are nonincreasing,

`6*10^(-5)`

`> integral_p^(p+h) (U(t)-d(t)) dt`

`>=h(U(p+h)-d(p))+o(1)`.

Now

`U(0.34)=sqrt(1-3(0.34)^2/4)>0.9556`.

Therefore

`d(0.30)>0.9556-(6*10^(-5))/0.04-o(1)`

`>0.9541-o(1)`.

So on **each** boundary side the deepest `0.30D` long rows share more than

`0.9541D`

consecutive exact chain tracks.

The two intervals live in the same ordered `D`-track family.  Their intersection is
therefore consecutive and has size greater than

### (QG6)

`M D`,

`M=2(0.9541)-1=0.9082`

up to `o(D)`.

## 7. One coherent residual phase supplies at least 0.30 D central leaf trains

The selected prefixes contain `0.60D+o(D)` residual rows in total.  At leading atomic
order there are at most two chain-adjacent residual projective phases.  After deleting
the `o(D)` phase-neighborhood exceptions, one phase, call it `B`, occurs at least

### (QG7)

`0.30D-o(D)`

times among those two prefixes.

Within each boundary side, those B-trains are a deepest prefix of the B-phase cap
stack.  By the central-stack order lemma CP1 from
`target_c_central_phase_block_endpoint_exclusion_2026-09-05.md`, their union is a
contiguous central block of the global noncrossing B-phase family (or a contiguous end
block if one side contributes none).  B-phase trains omitted outside it are
boundaryward and do not separate the central grid corners.

Likewise, exact P-trains outside the common consecutive block from QG6 lie outside its
extremal tracks and do not separate those corners.

Thus the selected center family and B-phase leaf family form a genuine complete
phase grid with normalized sizes at least

`M=0.9082-o(1)`,

`b=0.30-o(1)`,

without same-phase leakage from their omitted tracks.

## 8. Allow the opposite residual phase to cancel arbitrarily

Orient the coherent center and selected leaf directions as

`u=(1,0)`,

`v=(1/2,sqrt(3)/2)`.

The other chain-adjacent residual phase has projective direction

`w=(1/2,-sqrt(3)/2)`

up to `o(1)`.  We place **no population bound at all** on its coherent contribution.
Allow an arbitrary real multiple `xw`.

For any real `x`, the distance from `M u+b v` to the line spanned by `w` is

`|det(Mu+bv,w)|`

`=(sqrt(3)/2)(M+b)`.

Therefore even perfect coherent cancellation by the entire opposite phase leaves
normalized length at least

`(sqrt(3)/2)(M+b)`.

The complement atomic population from QG3 may have arbitrary directions, so subtract
its entire norm `q`.  Trains outside the three leading phase classes have only
`o(D^2)` crossings with the positive-density phase grid; after a fixed sufficiently
small TG1 trim, only `o(D)` of them can separate the chosen central diagonal.

Consequently some source difference has normalized length at least

`(sqrt(3)/2)(M+b)-q-o(1)`.

Using the safe numerical bounds

`sqrt(3)/2>0.866`,

`M>0.9082`,

`b>0.30-o(1)`,

`q<0.000896`,

we obtain

`(sqrt(3)/2)(M+b)-q`

`>0.866(1.2082)-0.000896`

`>1.044`.

The fixed TG1 trim can be chosen small enough to preserve a margin far above one.
Thus the configuration contains two source points at distance strictly greater than
`D`, contradiction.

## 9. Conclusion

The assumption `r<=0.933+o(1)` is impossible.  Hence

`liminf T/D > 2.933`.

This improves both

- the earlier audited strict certificate `2.9328`; and
- the exact scalar root `2.932935111451...` by a genuinely geometric stability
  argument.

The numerical margin in the final train-coordinate contradiction is much larger than
the scalar slack used to obtain it, so the constant 2.933 is intentionally
conservative.  Further optimization of `p,h` and the complement-mass estimate should
push the explicit decimal higher, but no such stronger decimal is claimed here.