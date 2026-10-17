<!-- theorem-state: {"artifact_id":"ART-6A2B2DD16E5B","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-a"} -->
# Erdős Problem #99 — Target A nine-site unit-tube bound

**Date:** 2026-09-04  
**Branch:** `research/target-c-c97-caterpillar-fan-capacity-2026-09-04`  
**Run type:** exact improvement of Section 174 tube shielding  
**Target:** locked three-channel Schur sector branch  
**Status:** LEVEL I STILL OPEN

## 1. Result

Section 174.1 uses Oler's inequality to bound the number of unit triangular-lattice sites at distance `<1` from a unit contact edge by eleven. The lattice itself gives a stronger bound immediately.

### Theorem NT1 — nine sites per unit edge

Let `Lambda` be a unit triangular lattice and let `e` be any unit segment in the plane. Then

`#{y in Lambda : dist(y,e)<1} <= 9`.

Consequently, for every finite unit-contact graph `Sigma` with no isolated vertices,

`|T_Sigma| <= 9 |E(Sigma)|`.

### Proof

Take any two distinct lattice sites `y,y'` in the open unit tube of `e`. Choose `x,x' in e` with

`|y-x|<1`, `|y'-x'|<1`.

Since `e` has length one,

`|x-x'|<=1`.

Therefore

`|y-y'| <= |y-x|+|x-x'|+|x'-y'| < 3`.

Now partition the triangular lattice into the nine cosets of the index-nine sublattice

`3 Lambda`.

Two distinct sites in the same coset differ by `3 lambda` for a nonzero `lambda in Lambda`, hence are at distance at least `3`, because the shortest nonzero lattice vector has length one. Thus our open-tube set contains at most one site from each of the nine cosets. This proves the bound.

For a contact graph with no isolated vertices, every point of `|Sigma|` lies on a unit contact edge. Apply the one-edge bound and take a union bound over the edges. QED.

## 2. Improved basis-closed shield constants

Section 174 defines

`W_Sigma^0 = V(Sigma) sqcup T_Sigma`

and then closes under the fixed basis matching `mu_0:B->Z`:

`W_hat_Sigma = W_Sigma^0 union mu_0(B cap W_Sigma^0) union mu_0^{-1}(Z cap W_Sigma^0)`.

Because `mu_0` is a bijection,

`|W_hat_Sigma| <= 2 |W_Sigma^0|`.

Theorem NT1 therefore improves (174.11) to

`|W_hat_Sigma| <= 2|V(Sigma)| + 18|E(Sigma)|`.

For the locked three-channel fan, Section 174.6 has a connected unicyclic contact graph, so

`|E(Sigma)|=|V(Sigma)|`.

Hence the explicit shield bound improves from

`|W_hat_Sigma| <= 24|V(Sigma)|`

to

### Corollary NT2 — twenty-per-vertex locked shield

`|W_hat_Sigma| <= 20|V(Sigma)|`.

This is a strict one-sixth reduction in the only explicit shielding constant entering the locked three-sector branch.

## 3. Why the argument is exact

The proof uses the strict tube inequality. The factor `3` is exactly the sum

`1 + length(e) + 1`.

The congruence partition then matches that strict diameter threshold exactly: distinct points in one coset of `3Lambda` have distance at least `3`. No Oler slack, orientation estimate, or generic-position assumption is used.

The theorem does not by itself prove the three-sector population inequality (174.23). It reduces the exceptional/shield population that a successful sector argument must absorb.
