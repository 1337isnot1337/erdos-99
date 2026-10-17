# Target C: next low-symmetry external-rank attack plan

Date: 2026-09-23

Status: research continuation note. No new theorem is claimed here.

## Current boundary

The recent finite certificates have pushed the four-support `p=3,m=4` branch to the point where the remaining four-support cases are not expected to yield to the support-nullity obstruction alone.

The completed support-nullity classification found that four-support support orbits split into:

- nullity-5 support classes, eliminated by the deletion-nullity condition;
- nullity-4 support classes, where the support-nullity argument is sharp and does not decide the branch.

The order-6 `(2,2,2,2)` shard was then closed by the coefficient-code and external-rank-increment test. The remaining work should reuse that mechanism rather than expanding the support-nullity search.

## Next attack target

Prioritize the remaining low-symmetry nullity-4 four-support cycle states:

1. enumerate support-set orbit representatives by stabilizer order;
2. reuse the existing singleton-block reduction to isolate states with touched complete-root nullity exactly one;
3. compute coefficient rank and generalized-weight filters before relation-rank calculations;
4. for the surviving states, measure the external relation-rank increment required by the arithmetic branch condition;
5. preserve exact certificates for every eliminated shard.

The order of attack should favor the largest number of labeled states eliminated per verifier cost. Low stabilizer order classes should be processed after confirming that the high-symmetry compression does not already cover their orbit types.

## Required proof discipline

A computational result should only be promoted when:

- the enumeration space is explicitly defined;
- orbit quotienting is independently checked;
- ranks are computed exactly or with a certified modular bound;
- every asserted count is reproducible by a repository verifier;
- the note distinguishes a finite shard closure from a full Target C closure.

## Remaining mathematical bottleneck

The main unresolved question for this route is whether the coefficient-nullspace directions in the remaining nullity-4 support classes can ever generate the external rank increment demanded by the `D=-1,d_root=1` arithmetic branch. A negative answer for all remaining classes would substantially narrow Target C; a positive example would identify the obstruction needed for the next proof route.
