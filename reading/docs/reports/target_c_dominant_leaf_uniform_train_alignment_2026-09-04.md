> Generated reading edition · [exact source](../../../docs/reports/target_c_dominant_leaf_uniform_train_alignment_2026-09-04.md) · source SHA-256 `d0495394ae4b86d7a529063ec9d058cb26402d61c3ea3aab37270faa1d6726fa`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-8428C467D0A9","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C100 candidate: uniform alignment and noncrossing of a dominant diameter's separators

**Date:** 2026-09-04
**Repository base:** branch after C99 (`798bcdd1`)
**Run type:** exact train-angle KKT theorem
**Target:** one-leaf near-chain phase
**Depends on:** Target B train virtual-work identities; C77 strict-rhombic train geometry; C98 dominant leaf
**Status:** proved working result; audit pending
**LEVEL I STATUS:** STILL OPEN

C99 converts a dominant diameter weight into an average train-alignment statement. C100 sharpens this to **uniform** alignment using the coordinatewise KKT equations.

Let `h_0=za` be an actual diameter pair in a pure simply connected strict-rhombic disk. Put

`r_0=p_a-p_z=D u`, `|u|=1`,

and let `P` be the train tracks separating `z,a`. For `tau in P`, orient its unit train-edge vector from the `z` side toward the `a` side and call it `a_tau`.

Let

`b=beta_(h_0)`, `eta=1-b`, `rho=eta/b`.

Then for every `tau in P`,

`|a_tau dot Ju| <= rho`,

and

`a_tau dot u >= -rho`.

If `rho<1/sqrt(2)`, these combine to

`a_tau dot u >= sqrt(1-rho^2)>0`.

Therefore every separating train lies within angle `arcsin rho` of the dominant diameter direction. If `rho<1/2`, equivalently `b>2/3`, any two such train directions differ by less than `pi/3`; two strict triangle-free unit-rhombus trains can cross only at an angle strictly between `pi/3` and `2pi/3`. Hence the entire separator family `P` is pairwise noncrossing.

This produces an exact ordered nested separator family as soon as one beta edge exceeds `2/3`, with no exact-chain assumption.

---

## 1. Train-angle stationarity

For any active diameter `h`, use the standard train-coordinate notation

`r_h=sum_tau d_(h tau) u_tau`,

`a_(h tau)=d_(h tau)u_tau`,

with `d_(h tau) in {-1,0,1}`.

Rotating one train angle preserves every unit-contact length to first order. Applying the normalized KKT stationarity equation to that virtual motion gives, for every train `tau`,

`sum_h beta_h [r_h dot J a_(h tau)] = 0`.

For `tau in P`, `a_(h_0 tau)=a_tau`, so

`b D [u dot J a_tau]
 = -sum_(h!=h_0) beta_h [r_h dot J a_(h tau)]`.

Every summand on the right has absolute value at most `D beta_h`, because `|r_h|=D` and `|a_(h tau)|` is zero or one. The residual beta mass is `eta`. Hence

### Lemma C100.1 — uniform transverse alignment

`|u dot J a_tau| <= eta/b = rho`

for every `tau in P`.

This is pointwise in the train label. No averaging or flow decomposition is used.

## 2. Contact-stress positivity selects the forward branch

Target B's train virtual-work identity gives the total contact stress carried by train `tau`:

`A_tau=sum_(e in tau) alpha_e
     =sum_h beta_h lambda_(h tau) >=0`,

where

`lambda_(h tau)=r_h dot a_(h tau)`.

For `tau in P`, the dominant term is

`b D (u dot a_tau)`.

The residual terms have total absolute value at most `eta D`. Therefore

`b D (u dot a_tau) >= -eta D`,

or

### Lemma C100.2 — no macroscopic backward separator

`u dot a_tau >= -rho`.

Now write

`x=u dot a_tau`, `y=Ju dot a_tau`.

Then `x^2+y^2=1`, `|y|<=rho`, and `x>=-rho`.

Assume `rho<1/sqrt(2)`. If `x<0`, then `|x|<=rho`, so

`y^2=1-x^2 >=1-rho^2>rho^2`,

contradicting `|y|<=rho`. Thus `x>0`, and then

`x=sqrt(1-y^2)>=sqrt(1-rho^2)`.

### Theorem C100.3 — uniform cone theorem

If `rho<1/sqrt(2)`, every train separating the dominant diameter satisfies

`a_tau dot u >= sqrt(1-rho^2)`

and

`angle(a_tau,u)<=arcsin rho`.

In particular all separator contributions point forward; none is tangent or backward.

## 3. Improved separator-count stability

Train coordinates give

`D u=sum_(tau in P)a_tau`.

Taking the `u` component and using C100.3,

`D=sum_(tau in P)u dot a_tau
   >= k sqrt(1-rho^2)`,

where `k=|P|`.

Therefore

### Corollary C100.4

`D <= k <= D/sqrt(1-rho^2)`.

Equivalently,

`0<=k-D
 <= D[1/sqrt(1-rho^2)-1]`.

For `eta=o(1)`, `rho=eta/(1-eta)=o(1)`, so

`k-D=O(D eta^2)`.

This improves C99's flow-only bound `O(D eta)`.

The exact C99 identity

`sum_(tau in P)|a_tau-u|^2=2(k-D)`

then gives the same quadratic improvement in total direction defect.

## 4. Pairwise noncrossing once b>2/3

Suppose

`rho<1/2`,

which is equivalent to

`(1-b)/b<1/2`, hence `b>2/3`.

C100.3 puts every oriented separator direction in the open cone

`angle(a_tau,u)<pi/6`.

Therefore two separator train lines have acute angle strictly less than `pi/3`.

If two train tracks cross in a rhombus, their contact-edge directions are the two side directions of that unit rhombus. Triangle-freeness makes both diagonals strictly longer than one. If `theta` is the angle between the side directions, this is equivalent to

`pi/3<theta<2pi/3`.

Thus the acute angle between the two unoriented train lines is strictly greater than `pi/3`.

Contradiction.

### Theorem C100.5 — dominant separators are nested

If `beta_(za)>2/3`, all trains separating `z,a` are pairwise noncrossing proper crosscuts of the rhombic disk.

Since every one separates `z` from `a`, the family is linearly ordered/nested between the two `z`-to-`a` outer-boundary arcs. It therefore defines exact prefix levels even though its directions are not literally identical.

## 5. Insert C98

In C71-B with `D epsilon->0`, C98 gives one diameter edge with

`b=1-o(1)`.

Hence eventually `b>2/3`, and C100 gives:

- all `z`-`a` separator trains are pairwise noncrossing;
- each is at angle `o(1)` from `u` uniformly;
- `k=D+O(D(1-b)^2)=D+o(D)`;
- the C99 shortest path crosses the nested separator family once each and no other train.

Thus the one-leaf branch has an exact ordered **near-parallel separator stack**, not merely an average near-geodesic.

## 6. Why C87 does not yet apply verbatim

The exact C80 chain has one common separator direction `u`, so every non-chain diameter interval has

`g_h|P=eta_h 1_I`.

C87 uses that constant row to obtain an exact zero-divergence positive prefix circulation and then paired orientations for every interval.

Under C100 the directions `a_tau` vary by `o(1)`. The interval support remains exact because the nested separator family gives prefix levels, but the gradient entries are

`(g_h)_tau=r_h dot J a_tau`,

which vary with `tau`. Thus the C87 circulation acquires a small but nonzero cut imbalance. Treating it as exactly divergence-free would be invalid.

The next theorem must either:

1. control that imbalance strongly enough to recover a paired full-span interval quantitatively; or
2. use the nested separator stack directly to derive a hull/shell contradiction without passing through C87's exact circulation.

C100 removes the previous topological ambiguity: the only remaining defect from the exact chain stack is small angular variation and the sublinear/in fact `O(D eta^2)` excess train count.
