> Generated reading edition · [exact source](../../../docs/reports/target_b_explicit_general_phase_interpolation_2026-09-05.md) · source SHA-256 `966cf3e23f3ac2c3d47875781f702653aec42f7205ff05ba8c3cee59f5b60ae2`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-D1618F69CC1E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-b"} -->
# Erdos Problem #99 - Target B explicit general coherent-phase interpolation

**Date:** 2026-09-05  
**Run type:** quantitative stability / general class-size interpolation  
**Target:** close the remaining local `M>b` versus exact two-max interpolation gap  
**Depends on:** explicit unique-max grid argument; balanced tripartite combinatorial stability; dual-tree complete-grid extraction; trimmed-grid diameter theorem  
**LEVEL I STATUS:** STILL OPEN globally

## 1. Statement

Let one coherent three-phase component have phase classes

`A,B,C`

with sizes

`|A|=M`, `|B|=b`, `|C|=a`,

and

`M>=b>=a`.

Put

`t=b/M`, `s=a/M`

and assume the fixed dense-component lower ratio

`t>=tau>0`.                                               (1.1)

Let `E` be the physical crossing count inside the component and define its Theorem-51 extremal deficit

`Delta=[M(a+b)-E]/M^2`.                                  (1.2)

Assume the same component-scale hypotheses as the explicit phase-gap reports:

1. no transversal triangle;
2. the three phase directions are `o(1)`-coherent around triangular projective directions;
3. crossings involving trains outside this component are `o(M^2)`;
4. the component carries the global quadratic rhombus core at its scale, so `R=E+o(M^2)` and `T=O(M)`.

Set

`mu_0=8*10^(-5)`.                                       (1.3)

Then the general component has an explicit uniform deficit

### Theorem GPI - explicit general phase gap

`liminf Delta >= delta_GPI(tau)`,                        (1.4)

where the conservative choice

`boxed{delta_GPI(tau)=4*10^(-17) tau^2}`                (1.5)

is valid.

The constant is intentionally tiny. Its role is only to remove the last unspecified interpolation modulus between the unique-max and tied/balanced local phase regimes.

This theorem remains local to a component carrying the global quadratic core. It does not solve the multi-grain local-to-global transfer problem.

## 2. Uniform missing floor for the largest-second phase pair

Write

`e_AB=Mb-x`

and

`mu=x/(Mb)`.

The geometric part of the explicit unique-max proof yields a fact stronger than the final `kappa tau` deficit statement: the pair `A-B` itself cannot be arbitrarily complete, uniformly in the class gap.

We reproduce the argument because no `kappa` is needed.

Assume

`mu<=mu_0`.

Put `r=sqrt(mu)`. The corrected dual-tree extraction gives a complete grid after retaining

`A' subset A`, `B' subset B`

with

`|A'| >= (1-r)M`,

`|B'| >= (1-mu-2r)b-O(1)`.

Normalize the omitted two-phase train population by `M`:

`L=(M-|A'|)/M + (b-|B'|)/M`.

Since `t<=1`,

`L <= 3r+mu+o(1)`.                                      (2.1)

Let the third phase have normalized size `s`. The trimmed-grid theorem optimizes its entire coherent signed cancellation and gives the full ideal squared-diagonal function `F(s,t)`. Its uniform margin is

`F(s,t)-c(s+t) >= gamma_0`,                              (2.2)

where

`c=2sqrt(3)/pi`

and

`gamma_0=3/4-c/2=0.1986711045...`.

The omitted `A/B` trains are paid once for shortening the coherent grid sums and once again for arbitrary signed diagonal contribution. Hence

`D^2/M^2 >= F(s,t)-4sqrt(3)L-o(1)`.                     (2.3)

At `mu_0=8*10^(-5)`, the explicit unique-max computation gives

`4sqrt(3)(3sqrt(mu_0)+mu_0)<0.1865<gamma_0`.            (2.4)

Therefore

`D^2/M^2 > c(s+t)+0.01`                                 (2.5)

for all sufficiently large terms.

But `E<=M(a+b)`, the component carries all but `o(M^2)` rhombi, and `T=O(M)`. Hence

`n/M^2 <= s+t+o(1)`

and the strict triangular-lattice comparison gives

`D^2/M^2 < c(s+t)+o(1)`,                                (2.6)

a contradiction.

Thus:

### Lemma GPI.1 - universal largest-pair missing floor

`liminf x/(Mb) >= mu_0=8*10^(-5)`.                      (2.7)

No lower bound on `1-b/M` is used.

## 3. Small total phase deficit forces all three class sizes to balance

Write

`e_AC=Ma-y`,

`e_BC=z`.

The transversal-triple count gives

`M z <= a x+b y`.                                       (3.1)

Therefore

`Delta M^2=x+y-z`

`>= (1-a/M)x+(1-b/M)y`

`>= (1-s)x`.                                            (3.2)

Using Lemma GPI.1 and `b=tM`,

`Delta >= mu_0 t(1-s)+o(1)`.                           (3.3)

Since `t>=tau`,

`1-s <= Delta/(mu_0 tau)+o(1)`.                        (3.4)

Because `s<=t<=1`, the same bound controls both class imbalances:

`1-t <=1-s`,

`t-s <=1-s`.                                            (3.5)

Thus a hypothetical sequence with `Delta->0` is automatically asymptotically balanced in **all three** phase populations. This uses the geometric missing floor; graph theory alone would not force it.

## 4. Random balanced restriction

Choose uniformly random subsets

`A_0 subset A`, `B_0 subset B`

with

`|A_0|=|B_0|=a`,

and retain all of `C`.

An `A-B` edge survives with probability

`(a/M)(a/b)=s^2/t`.

An `A-C` edge survives with probability `s`, and a `B-C` edge with probability `s/t`. Since `s<=t<=1`, both of those probabilities are at least `s^2/t`.

Therefore some deterministic choice satisfies

`E_0 >= (s^2/t)E`.                                      (4.1)

Since `a^2=s^2M^2`,

`E_0/a^2 >= E/(tM^2)`

`=(s+t-Delta)/t`.                                       (4.2)

Let

`epsilon_bal=2-E_0/a^2`

be the deficit of this equal-size tripartite graph. Then

`epsilon_bal`

`<= 2-(s+t-Delta)/t`

`=(t-s+Delta)/t`

`<= (1-s+Delta)/tau`.                                   (4.3)

Combining with (3.4),

`epsilon_bal <= [Delta/(mu_0 tau)+Delta]/tau+o(1)`.     (4.4)

## 5. Explicit complete grid inside the balanced restriction

The explicit balanced combinatorial lemma is purely graph-theoretic: a balanced tripartite graph with deficit `epsilon_bal` and no transversal triangle contains a phase pair with missing density at most

`mu <=4sqrt(epsilon_bal)`.                               (5.1)

Apply the corrected dual-tree extraction to that pair. Put `r=sqrt(mu)`. The complete grid omits, relative to the balanced size `a`, at most

`L_grid <=6 epsilon_bal^(1/4)+4sqrt(epsilon_bal)+o(1)`  (5.2)

from the two selected balanced phase classes.

As in the explicit balanced theorem, this loss is paid twice: once for shortening the two coherent grid vector sums and once for arbitrary signed contributions of omitted trains from those two classes.

There is one additional error: the random restriction discarded original trains before the balanced argument. The total number discarded from `A` and `B` is

`(M-a)+(b-a)`

`=M(1-s+t-s)`

`<=2M(1-s)`.                                            (5.3)

Relative to `a=sM`, their entire possible train-coordinate contribution has norm at most

`L_del=2(1-s)/s`.                                       (5.4)

This error is adversarial; no sign or crossing assumption is imposed on the deleted original trains.

The remaining balanced phase class of size `a` receives its full arbitrary coherent cancellation and is already included in the balanced ideal value

`F(1,1)=3`.

Trains genuinely outside the original coherent component contribute `o(a)` after the standard fixed-fraction central trim and TG1, because `a/M->1` under the small-deficit hypothesis below.

Consequently

`D/a >= sqrt(3)-2L_grid-L_del-o(1)`.                    (5.5)

Using the same safe squaring as the explicit balanced report,

`D^2/a^2`

`>=3-4sqrt(3)L_grid-2sqrt(3)L_del-o(1)`.                (5.6)

## 6. Insert the conservative threshold

Assume for contradiction

`Delta < delta_GPI(tau)=4*10^(-17)tau^2`.               (6.1)

Then (3.4) gives

`1-s < [4*10^(-17)tau^2]/[8*10^(-5)tau]+o(1)`

`=5*10^(-13)tau+o(1)`

`<=5*10^(-13)+o(1)`.                                    (6.2)

Thus `s>0.999999999999` for all sufficiently large terms, and

`L_del<3*10^(-12)`                                      (6.3)

is a safe bound.

Also (4.4) gives

`epsilon_bal`

`< [5*10^(-13)tau+4*10^(-17)tau^2]/tau+o(1)`

`<6*10^(-13)+o(1)`.

In particular the safe weaker bound

`epsilon_bal<10^(-12)`                                  (6.4)

holds eventually.

Therefore (5.2) gives

`L_grid < 6*10^(-3)+4*10^(-6)+o(1)`

`<0.00601`.                                              (6.5)

Insert (6.3)-(6.5) into (5.6):

`D^2/a^2 > 3-4sqrt(3)(0.00601)-10^(-10)`

`>2.95`                                                  (6.6)

for all sufficiently large terms. The displayed `2.95` is deliberately much weaker than the actual lower value.

Now use the full original component for the global upper bound. Since

`R/M^2=E/M^2+o(1)=s+t-Delta+o(1)`

and `n=R+O(M)`, the lattice comparison gives

`D^2/a^2`

`< c(s+t-Delta)/s^2+o(1)`.                              (6.7)

Under (6.2), `s,t<=1` and `s=1-o(1)`, so the right side is

`<2.21`                                                  (6.8)

for all sufficiently large terms, because `2c=2.2053155817...`.

Equations (6.6) and (6.8) contradict each other.

Hence (6.1) is impossible, proving Theorem GPI.

## 7. Relation to the previous explicit regimes

The result is intentionally weaker numerically than the specialized theorems:

- fixed-gap unique max: `Delta >=8*10^(-5) kappa tau`;
- exact balanced: deficit at least `10^(-7)` in balanced normalization;
- exact two-max: deficit at least `~9.99*10^(-11)` in tied normalization;
- general sizes: `Delta >=4*10^(-17)tau^2`.

The point of GPI is uniformity over the remaining `M>b` interpolation, including sequences with `M/b->1` at an arbitrary rate.

For a fixed Section-50 pruning parameter `lambda`, retained minimum degree and `T<=C_TD` give a fixed lower phase ratio. Indeed an `A`-phase vertex has at most `a+b<=2b` possible neighbors, while its retained degree is at least `lambda D`, so

`b>=lambda D/2`.

Since `M<=T<=C_TD`, one may take

`tau>=lambda/(2C_T)`.                                   (7.1)

Thus GPI supplies a completely explicit local phase deficit coefficient for every fixed dense-core regime.

## 8. What remains globally

GPI closes only the **local class-size interpolation** noted as open in the explicit two-max audit.

It does not solve the principal Target B transfer gap. The proof still assumes that the selected coherent component carries the global quadratic rhombus core at its scale. Section 50 may instead leave several linearly sized coherent grains whose crossing masses sum to `Theta(D^2)`. A component of size `M=Theta(D)` can then fit inside the global diameter because the lattice upper bound uses the rhombi in all grains, not just that component.

The remaining theorem is therefore genuinely multi-component:

> combine componentwise phase deficits, inter-component virtual determinant mass, deleted physical interface crossings, and global source diameter in one inequality.

The PC3/MCP penetration reports on PR #103 address the deleted-physical/interface part of exactly this problem.

## Handoff

```text
New explicit general local gap.

For M>=b>=a, t=b/M>=tau, and Delta=[M(a+b)-E]/M^2:

1. the largest-second pair has a uniform geometric missing floor
     missing(A,B)/(Mb) >= mu_0=8e-5;
2. transversal-triple algebra gives
     1-a/M <= Delta/(mu_0 tau)+o(1);
3. if Delta were tiny, all three classes would therefore be nearly equal;
4. randomly trim A,B to size a, obtaining a balanced graph with
     epsilon_bal <= [Delta/(mu_0 tau)+Delta]/tau+o(1);
5. balanced combinatorial stability + dual-tree extraction gives a nearly full complete grid;
6. explicitly restore all trains deleted by the balancing restriction as adversarial diagonal error.

The conservative contradiction threshold

  Delta >=4e-17 tau^2

holds under the standard dominant coherent-component hypotheses.

This removes the remaining local M>b versus M=b interpolation modulus. Global multi-grain transfer remains open.
```
