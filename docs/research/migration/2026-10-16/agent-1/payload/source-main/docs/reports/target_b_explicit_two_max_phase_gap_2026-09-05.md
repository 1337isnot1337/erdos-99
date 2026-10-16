<!-- theorem-state: {"artifact_id":"ART-88A461FC72A6","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-b"} -->
# Erdős Problem #99 — Target B explicit two-largest-tie phase gap

**Date:** 2026-09-05  
**Run type:** quantitative stability / uniform tied-class interpolation  
**Target:** dense coherent three-phase global deficit-transfer gate  
**Depends on:** tied-max transversal-triple algebra; explicit balanced gap; dual-tree grid extraction; trimmed-grid phase-star diameter theorem  
**LEVEL I STATUS:** STILL OPEN

## 1. Statement

Let a coherent three-phase train component have phase classes

`A,B,C`

with

`|A|=|B|=b`, `|C|=a<=b`.

Assume:

1. the phase crossing graph has no transversal triangle;
2. the three phase directions are `o(1)`-coherent around the triangular projective directions;
3. crossings involving trains outside this coherent component are `o(b^2)`;
4. `T=O(b)`.

Let

`E`

be the crossing count inside the component and define

`q=1-a/b`,

`eta=[b(b+a)-E]/b^2`.

### Theorem 1 — uniform explicit two-max phase deficit

Every sufficiently large admissible component satisfies

`liminf eta >= 10^(-10)/1.001`

`=9.99000999...*10^(-11)`.

In particular the simpler conservative bound

`liminf eta >=9.9*10^(-11)`

holds uniformly for every `0<=a/b<=1`.

The constant is tiny because it bridges the fixed-gap tied regime to the exactly balanced regime without any compactness modulus.

## 2. The largest pair itself has a fixed missing-crossing floor

Write

`e_AB=b^2-x`.

### Lemma 2 — tied largest-pair missing floor

`liminf x/b^2 >=10^(-3)`.                               (2.1)

### Proof

Suppose instead that along a subsequence

`mu=x/b^2 <=10^(-3)`.

Apply the corrected dual-tree extraction to the internally noncrossing `A,B` phase families. There is a complete crossing grid after deleting normalized train population at most

`L<=3sqrt(mu)+mu+o(1)`.

At `mu=10^(-3)`,

`L<=0.09586833...+o(1)`.

The omitted `A/B` trains can themselves separate the chosen grid diagonal, so charge the same quantity a second time. The complete tied grid has normalized phase parameters

`t=1`, `s=a/b in [0,1]`.

The trimmed-grid constrained minimum is exactly

`F(s,1)=3`

for every `s`. Hence, after the standard further central trim controlling truly external trains,

`D^2/b^2 >=3-4sqrt(3)L-o(1)`

`>2.3357-o(1)`.                                         (2.2)

On the other hand the phase extremal bound gives

`E<=b(b+a)<=2b^2`.

Since the coherent component carries all but `o(b^2)` rhombi,

`R<=2b^2+o(b^2)`,

and Euler gives

`n<=2b^2+o(b^2)`.

The strict triangular-lattice comparison gives

`D^2/b^2<2c+o(1)`

with

`2c=4sqrt(3)/pi=2.2053155817...`,

contradicting (2.2).

Thus (2.1) holds. `square`

For later use set

`mu_0=10^(-3)`.                                          (2.3)

## 3. Tied-max algebra converts class imbalance into phase deficit

Write

`e_AC=ba-y`,

`e_BC=z`.

The transversal-triple count gives

`b z <= a x+b y`.

Therefore the tied extremal deficit satisfies

`eta b^2=x+y-z`

`>= (1-a/b)x`

`= q x`.

Using Lemma 2,

### Corollary 3

`liminf eta >= mu_0 q`.                                  (3.1)

This is strong away from the balanced point `q=0`, but degenerates there.

## 4. Near the balanced point, `q+eta` has a fixed floor

We now prove the complementary inequality

### Lemma 4 — balanced-distance floor

`liminf (q+eta) >= epsilon_0`,

where

`epsilon_0=10^(-7)`.                                    (4.1)

### Proof

Suppose for contradiction that along a subsequence

`e:=q+eta < epsilon_0`.

Put

`a=(1-q)b`.

Choose uniformly random subsets

`A_0 subset A`, `B_0 subset B`

with

`|A_0|=|B_0|=a`,

and retain all of `C`.

An `A-B` edge survives with probability `(a/b)^2=(1-q)^2`; an `A-C` or `B-C` edge survives with probability `1-q`, which is larger. Hence some choice satisfies

`E_0 >= (1-q)^2 E`.

Since

`a^2=(1-q)^2b^2`,

we obtain

`E_0/a^2 >= E/b^2`

`=2-q-eta`

`=2-e`.                                                   (4.2)

Thus the equal-size tripartite graph `A_0,B_0,C` has balanced deficit at most `e`.

The explicit balanced combinatorial stability lemma gives a pair among those three classes with missing density at most

`mu <=4sqrt(e)`.                                         (4.3)

Apply the dual-tree extraction to this pair. Its complete grid omits normalized train population, relative to the balanced size `a`, at most

`L_grid <=6 e^(1/4)+4sqrt(e)+o(1)`.                      (4.4)

As before this loss is paid twice: once for shortened grid vector sums and once for arbitrary contributions of the omitted trains from the selected balanced pair.

There is one additional error absent from the exactly balanced theorem. The random restriction deleted

`2(b-a)=2qb`

trains from the original `A,B` classes. Regardless of their signs, their total train-coordinate contribution to the selected diagonal has norm at most

`L_del a`,

where

`L_del=2qb/a=2q/(1-q)`.                                  (4.5)

The remaining balanced phase class of size `a` receives its full arbitrary coherent cancellation and is already included in `F(1,1)=3`. Truly non-core trains again contribute only `o(a)` after a fixed-fraction central trim; here `a/b=1-o(1)` because `q<epsilon_0`.

Therefore

`D/a >= sqrt(3)-2L_grid-L_del-o(1)`,

and hence

`D^2/a^2 >=3-4sqrt(3)L_grid-2sqrt(3)L_del-o(1)`.         (4.6)

At

`e<=epsilon_0=10^(-7)`,

`L_grid<=0.107961676...+o(1)`,

while

`L_del<=2.000001*10^(-7)`.

Thus the right side of (4.6) is larger than

`2.2520`

for all sufficiently large terms.

Now use the full original tied component for the global upper bound. It has

`R/b^2=2-q-eta+o(1)=2-e+o(1)`.

Since `a^2=(1-q)^2b^2`,

`D^2/a^2`

`< c(2-e)/(1-q)^2+o(1)`.

Under `0<=q<=e<=10^(-7)`, the right side is at most

`2.205317+o(1)`,

strictly below the lower bound from (4.6). Contradiction.

Therefore (4.1) holds. `square`

## 5. Uniform interpolation

From (3.1), asymptotically

`eta >= mu_0 q`.

Hence

`q <= eta/mu_0`.

From Lemma 4,

`epsilon_0 <= q+eta`

`<= eta(1+1/mu_0)`.

Therefore

`eta >= epsilon_0 mu_0/(1+mu_0)`

`= [10^(-7)*10^(-3)]/1.001`

`=10^(-10)/1.001`

`=9.99000999...*10^(-11)`.

This proves Theorem 1.

## 6. Why this matters

The two-largest-tie/balanced branch no longer requires an unspecified compactness constant. Every tied coherent component dominating its local quadratic crossing scale pays at least

`~10^(-10)b^2`

crossings below the cyclic-order extremal value.

Together with the fixed-gap unique-max coefficient, the remaining quantitative task is to transfer an almost-tied original class triple `M>=b>=a` to the exact tied setting while explicitly charging the `M-b` excess trains. That is now a finite error-budget problem.

## 7. Audit cautions

- The `A-B` missing floor is geometric, not purely graph-theoretic; it uses the global diameter comparison and the assumption that non-core crossing mass is `o(b^2)`.
- The random balanced restriction is used only to obtain a dense equal-size tripartite graph. Deleted original trains are then restored as an explicit adversarial diagonal error `L_del`; they are not treated as `o(b)` unless the contradiction assumption itself forces `q=o(1)`.
- The original false linear-stack lemma is not used; every complete grid comes from the dual-tree extraction theorem.
- The result is local to a coherent component and still needs global deficit transfer.
