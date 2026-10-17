> Generated reading edition · [exact source](../../../docs/reports/target_c_dominant_leaf_uniform_train_alignment_2026-09-05.md) · source SHA-256 `d77b1e67ff5be52e6a933a34ca1a585fd6b055e91d1fc035fd505970604a4ca7`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-CCF44C14A01A","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C100: uniform alignment and nesting of a dominant diameter's separators

**Date:** 2026-09-05  
**Run type:** exact train-angle KKT theorem  
**Target:** C98-C99 one-leaf near-chain phase  
**Depends on:** Target B train virtual-work identities; C77 strict-rhombic train geometry; C98 dominant leaf  
**Audit:** `docs/audits/target_c_c99_c100_nearchain_audit_2026-09-05.md`  
**LEVEL I STATUS:** STILL OPEN

Let `h_0=za` be an actual diameter pair in a pure simply connected strict-rhombic disk. Put

`r_0=p_a-p_z=D u`, `|u|=1`,

and let `P` be the trains separating `z,a`. For `tau in P`, orient its unit train vector from the `z` side toward the `a` side and call it `a_tau`.

Let

`b=beta_(h_0)`, `eta=1-b`, `rho=eta/b`.

C100 proves, for every `tau in P`,

`|a_tau dot Ju|<=rho`

and

`a_tau dot u>=-rho`.

When `rho<1/sqrt(2)`, every separator is in fact forward and

`a_tau dot u>=sqrt(1-rho^2)`.

When `rho<1/2`, equivalently `b>2/3`, all separator trains are pairwise noncrossing and hence nested.

## 1. Coordinatewise train-angle stationarity

Rotating one train angle preserves all unit-contact lengths to first order. KKT stationarity therefore gives, for every train `tau`,

`sum_h beta_h [r_h dot J a_(h,tau)]=0`.

For `tau in P`, the dominant contribution is

`bD[u dot J a_tau]`.

Each residual diameter contribution has magnitude at most `D beta_h`, and the residual beta mass is `eta`. Hence

### Lemma C100.1

`|u dot J a_tau|<=eta/b=rho`

for every `tau in P`.

This is pointwise, not averaged.

## 2. Contact-stress positivity chooses the forward branch

The train virtual-work identity gives

`A_tau=sum_(e in tau)alpha_e=sum_h beta_h [r_h dot a_(h,tau)]>=0`.

For `tau in P`, the dominant contribution is

`bD[u dot a_tau]`;

the residual contributions have total absolute value at most `eta D`. Thus

`u dot a_tau>=-rho`.

Write

`x=u dot a_tau`, `y=Ju dot a_tau`.

Then `x^2+y^2=1`, `|y|<=rho`, and `x>=-rho`. If `rho<1/sqrt(2)` and `x<0`, then `|x|<=rho`, so

`y^2=1-x^2>=1-rho^2>rho^2`,

contradiction. Therefore `x>0` and

### Theorem C100.2 — uniform cone theorem

`a_tau dot u>=sqrt(1-rho^2)`

and

`angle(a_tau,u)<=arcsin rho`

for every separator train.

## 3. Quadratic separator-count stability

Train coordinates give

`D=sum_(tau in P)u dot a_tau`.

Using C100.2,

`D>=k sqrt(1-rho^2)`.

Therefore

### Corollary C100.3

`D<=k<=D/sqrt(1-rho^2)`.

Equivalently,

`0<=k-D<=D[1/sqrt(1-rho^2)-1]`.

As `b=1-eta->1`, `rho=eta/(1-eta)=O(eta)`, so

`k-D=O(D eta^2)`.

Together with C99's exact identity,

`sum_(tau in P)|a_tau-u|^2=2(k-D)=O(D eta^2)`.

## 4. Pairwise noncrossing threshold

If `b>2/3`, then `rho<1/2` and every separator direction lies within `pi/6` of `u`. Thus the acute angle between any two separator train lines is less than `pi/3`.

If two strict triangle-free unit-rhombus trains cross, their contact-edge directions are the two side directions of that rhombus. Both diagonals must exceed one, which forces the side angle into

`(pi/3,2pi/3)`.

Hence the acute angle between crossing train lines is strictly greater than `pi/3`, contradiction.

### Theorem C100.4 — dominant separators are nested

If

`beta_(za)>2/3`,

all trains separating `z,a` are pairwise noncrossing proper crosscuts of the disk. Since every one separates `z` from `a`, they are linearly ordered/nested between the two `z`-to-`a` outer-boundary arcs and define exact prefix levels.

## 5. C98 consequence

In C71-B with `D epsilon->0`, C98 gives

`b=1-o(1)`.

Eventually `b>2/3`, so:

- all dominant-diameter separators are pairwise noncrossing;
- every separator direction is uniformly `o(1)` from `u`;
- `k=D+O(D(1-b)^2)=D+o(D)`;
- a shortest contact path crosses the ordered separator family once each.

Thus C71-B has an exact ordered near-parallel separator stack.

## 6. Remaining finite defect

C87 cannot yet be applied verbatim. In the exact C80 chain, every gradient restriction on one interval is a constant row

`g_h|P=eta_h 1_I`.

Here the interval support remains exact because the separators are nested, but the entries are

`(g_h)_tau=r_h dot J a_tau`,

which vary with `tau`. C87's exact divergence-free prefix circulation therefore acquires a small but nonzero imbalance.

The next closing theorem must either control this imbalance strongly enough to recover a paired full-span interval, or bypass C87 and derive a direct hull/shell contradiction from the nested separator stack.
