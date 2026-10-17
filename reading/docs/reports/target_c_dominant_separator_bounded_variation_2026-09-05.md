> Generated reading edition · [exact source](../../../docs/reports/target_c_dominant_separator_bounded_variation_2026-09-05.md) · source SHA-256 `9f5cb4049d17eb28f96ad22b97724661c74e7ea511c54e2ef3eaa295dcb43ba2`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-E41689BAEC81","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C102: bounded total variation of a dominant diameter's separator stack

**Date:** 2026-09-05  
**Run type:** exact KKT/train stability theorem  
**Target:** C98-C100 one-leaf near-chain phase  
**Depends on:** C77 train coordinates; C99 partial-cube path structure; C100 nested dominant separators and train-angle stationarity  
**LEVEL I STATUS:** STILL OPEN

C100 proves that when one diameter edge `h_0=za` has KKT weight `b>2/3`, every train separating `z` from `a` is pairwise noncrossing and uniformly close to the diameter direction. The pointwise cone bound still allows the train directions to oscillate rapidly across the ordered stack.

C102 removes that escape.

Let

`P={tau_1,...,tau_k}`

be the dominant separator trains in their nested order from `z` to `a`. Orient every separator train vector from the `z` side to the `a` side and call it `a_j`, with `|a_j|=1`. Put

`p_a-p_z=D u`, `|u|=1`,

`b=beta_(za)`, `eta=1-b`.

Then the entire ordered direction sequence has total chordal variation

`sum_(j=0)^k |a_(j+1)-a_j| <= 4 eta/(2b-1)`,

where

`a_0=a_(k+1)=u`.

Consequently its total angular variation is at most

`2 pi eta/(2b-1)`.

Thus `b->1` forces the whole near-chain separator stack to converge to the diameter direction in bounded variation, not merely uniformly or in mean square.

## 1. KKT force crossing one separator

For each active diameter `h`, train coordinates write its contribution on train `tau_j` as

`a_(h,j)=d_(h,j) a_j`,

where `d_(h,j) in {-1,0,1}`. Because the separator family is nested, the nonzero support of one diameter on `P` is one consecutive interval. If the diameter is oriented from its lower prefix level toward its higher prefix level, the sign `d_(h,j)` is constant on that interval.

Define the signed diameter vector carried across `tau_j` by

`F_j := sum_h beta_h d_(h,j) r_h`,

where `r_h` is the oriented diameter vector of length `D`.

The train-angle KKT equation is

`F_j dot J a_j = 0`.

The train virtual-work identity is

`F_j dot a_j = A_j`,

where

`A_j=sum_(e in tau_j) alpha_e >0`

is the total positive contact stress carried by that train. Therefore

### Lemma C102.1 — separator force is exactly tangent to the train

`F_j=A_j a_j`.

This packages the two scalar train identities into one vector equation.

## 2. Remove the dominant diameter

The dominant diameter `h_0=za` crosses every separator from the `z` side to the `a` side, so its contribution to every `F_j` is the same vector

`bD u`.

Write

`F_j=bD u+G_j`,

where

`G_j=sum_(h!=h_0) beta_h d_(h,j) r_h`.

The residual beta mass is exactly

`sum_(h!=h_0) beta_h=eta`.

Hence, pointwise,

`|G_j|<=D eta`.

Therefore

`A_j=|F_j|>=D(b-eta)=D(2b-1)`.

This is positive for `b>1/2`.

## 3. Interval support gives an exact total-variation bound

Extend the residual sequence by

`G_0=G_(k+1)=0`.

One residual diameter `h!=h_0` contributes the constant vector

`beta_h d_h r_h`

to one consecutive interval of indices and zero elsewhere. Across the extended sequence it therefore creates exactly one entry jump and one exit jump, each of norm `beta_h D`.

By the triangle inequality, summing over all residual diameters gives

### Lemma C102.2 — residual-force bounded variation

`sum_(j=0)^k |G_(j+1)-G_j|
 <= 2D sum_(h!=h_0) beta_h
 = 2D eta`.

Since the dominant vector `bD u` is constant,

`F_(j+1)-F_j=G_(j+1)-G_j`.

Define the virtual endpoint forces

`F_0=F_(k+1)=bD u`.

Their normalized directions are

`a_0=a_(k+1)=u`.

## 4. Normalize the force sequence

For nonzero vectors `x,y`,

`|x/|x|-y/|y|| <= 2|x-y|/min(|x|,|y|)`.

Every `F_j`, including the virtual endpoints, has norm at least `D(2b-1)`. Therefore

`|a_(j+1)-a_j|
 <= 2|F_(j+1)-F_j|/[D(2b-1)]`.

Sum and apply Lemma C102.2.

### Theorem C102 — bounded separator variation

For every dominant diameter edge with `b>1/2` whose separator family is nested,

`sum_(j=0)^k |a_(j+1)-a_j|
 <= 4 eta/(2b-1)`,

where `eta=1-b` and `a_0=a_(k+1)=u`.

In the C100 regime `b>2/3`, nesting is automatic, so the theorem applies directly.

If `phi_j` is the smaller angle between `a_j` and `a_(j+1)`, then

`|a_(j+1)-a_j|=2 sin(phi_j/2)`.

Since `phi_j<=pi`, `2 sin(phi_j/2)>=2phi_j/pi`. Hence

### Corollary C102.3 — total angular variation

`sum_(j=0)^k phi_j
 <= (pi/2) sum_(j=0)^k |a_(j+1)-a_j|
 <= 2 pi eta/(2b-1)`.

Thus the total turning tends to zero whenever `b->1`.

## 5. Shortest contact path inherits the same bounded turning

By C99, the rhombic contact graph is the region graph of the train arrangement and contact distance equals the number of separating trains. A shortest contact path from `z` to `a` therefore crosses every train in `P` exactly once and no other train.

Because the separators are nested, the path crosses them in their stack order. Oriented from `z` to `a`, its unit edge on `tau_j` is exactly `a_j`.

Hence there is a shortest contact path

`z=x_0,x_1,...,x_k=a`

whose successive unit edge directions are

`a_1,...,a_k`.

Therefore the same path has total turning at most

`2 pi eta/(2b-1)`.

Together with C100.3,

`k-D=O(D eta^2)`.

So the one-leaf phase contains a polygonal `z`-to-`a` contact geodesic with simultaneously:

1. only `O(D eta^2)` excess edges above Euclidean length;
2. uniform angular deviation `O(eta)` from `u`;
3. total turning `O(eta)`, independent of `D`.

This is substantially stronger than mean-square near-geodesicity.

## 6. Why this matters for C97 stability

The exact C97 contradiction uses a straight `D`-edge chain. C100 gave a uniformly narrow separator cone but still permitted `Theta(D)` alternating small angular errors. C102 forbids that: the entire ordered stack has only `O(eta)` total directional variation.

The remaining difference from C97 is now localized to two finite defects:

- the contact geodesic may have `k-D=O(D eta^2)` excess unit edges;
- its small total curvature need not vanish exactly, so internal path vertices need not be collinear or non-extreme.

A quantitative C97 extension can therefore work with total curvature rather than coordinatewise angular error.

## 7. Audit notes

- No monotonicity of the separator angles is assumed.
- The total-variation bound comes only from consecutive interval support of residual diameter bars and their total beta mass `eta`.
- A residual diameter spanning the whole separator stack is counted once on entry and once on exit in the extended sequence.
- The proof does not use response defect directly; C98 supplies `eta=o(1)` from `D epsilon->0` in C71-B.

## Handoff

In C71-B,

`D epsilon->0`

implies by C98 that one diameter edge has `b=1-o(1)`. C100 makes its separator trains nested. C102 then gives

`TV_chord(a_0,...,a_(k+1)) <= 4(1-b)/(2b-1)=o(1)`

and a shortest unit-contact path from one diameter endpoint to the other with the same `o(1)` total turning.

Next: convert this vanishing-total-curvature near-chain into a quantitative terminal-twist/prefix obstruction, or show that any nonzero total curvature/excess-edge defect forces enough response or shell cost to contradict `D epsilon->0`.
