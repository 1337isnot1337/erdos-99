<!-- theorem-state: {"artifact_id":"ART-3511434F1B9B","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-b"} -->
# Audit — Target B two-largest-tie phase stability exclusion

**Date:** 2026-09-05  
**Candidate:** `docs/reports/target_b_two_max_phase_stability_exclusion_2026-09-05.md`  
**Verdict:** PASS under the stated coherent near-saturation hypotheses.  
**LEVEL I status:** STILL OPEN.

## 1. Fixed-gap algebra

For class sizes `M,M,a`, write

`e_AB=M^2-x`, `e_AC=Ma-y`, `e_BC=z`.

Triangle-freeness gives

`a e_AB + M e_AC + M e_BC <=2M^2a`.

Substitution reduces exactly to

`Mz<=ax+My`.

With `s=a/M`, this is `z<=sx+y`. Hence the extremal deficit

`delta=x+y-z`

satisfies

`delta>=(1-s)x`.

If `1-s>=kappa>0` and `delta=o(M^2)`, then `x=o(M^2)`.

PASS.

## 2. Ordered complete-grid extraction

The two largest coherent phase classes are pairwise noncrossing internally. Their crossing neighborhoods are intervals, so `o(M^2)` missing crossings imply a complete `(M-o(M)) x (M-o(M))` subgrid by the audited interval-bigraph lemma.

PASS.

## 3. Third-phase handling

The trimmed-grid diameter proof only needs one complete grid. Every third-phase train contributes to the chosen diagonal with coefficient in `{-1,0,1}`; coherence bounds the whole third-phase contribution by an arbitrary scalar in its projective direction with magnitude at most `a+o(M)`.

Thus incomplete third-phase incidence cannot make the lower bound weaker than the already optimized `F(s,t)`.

PASS.

## 4. Fixed-gap diameter contradiction

For the retained tied grid, `t=1-o(1)`. The constrained minimum satisfies `F(s,1)=3` for every `0<=s<=1`. Thus

`D^2>=(3-o(1))M^2`.

Near saturation gives `n=(1+s+o(1))M^2`, while the strict translated-lattice comparison gives

`D^2<(c(1+s)+o(1))M^2<= (2c+o(1))M^2`.

Since `2c=4sqrt(3)/pi<3`, contradiction follows uniformly in `s`.

PASS.

## 5. Reduction when `a/M->1`

Put `m=a`. Then `M-m=o(M)`. Delete `M-m` trains from each of the two largest classes. This removes at most `o(M^2)` crossing edges because only `o(M)` vertices are deleted and each has `O(M)` possible phase neighbors.

The retained classes all have size `m`. Moreover

`M(M+m)-2m^2=(M-m)(M+2m)=o(M^2)`.

Hence the induced equal-size tripartite graph has `(2-o(1))m^2` edges. The audited balanced stability theorem applies and supplies an almost-complete phase pair, from which ordered extraction gives a complete `(m-o(m)) x (m-o(m))` grid.

The deleted `o(M)` trains contribute only `o(m)` to any train-coordinate diagonal and are harmless in the trimmed-grid error term.

PASS.

## 6. Exhaustion of class-size regimes

For any sequence with two equal largest class sizes, pass to a subsequence. Either the third-class ratio stays below `1-kappa` for some `kappa>0`, or it tends to one. The preceding two arguments exclude both cases.

PASS.

## Scope

TM4 is an endpoint theorem. It assumes the coherent three-phase core already has crossing count within `o(M^2)` of the Theorem-51 extremal bound and that only `o(M^2)` quadratic crossings lie outside the core. It does not prove that arbitrary pure-rhombic survivors reach this near-saturated regime.

Audited conclusion:

> Combined with unique-max stability, every class-size regime of a near-saturated coherent Theorem-51 phase core is excluded. The remaining Target B gate is the upstream transfer forcing near saturation from the global shell/crossing inequalities.
