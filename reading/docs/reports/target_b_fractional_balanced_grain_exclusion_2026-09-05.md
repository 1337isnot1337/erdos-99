> Generated reading edition · [exact source](../../../docs/reports/target_b_fractional_balanced_grain_exclusion_2026-09-05.md) · source SHA-256 `f8bbcd81a2c3cf3511e816b4ecda0a1e5f59165d57d159b18c3ad024a06bf40b`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "f90cb0eed4d237320daed6d5719867a1309a51b1", "source_canonical": false, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "unreviewed", "source_path": "docs/reports/target_b_fractional_balanced_grain_exclusion_2026-09-05.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "edc65430bd4a1fbcc11b325cd4cafb9170ec7206708754d2c199e080c4bce2be"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle was `unreviewed`; it is retained as provenance only. Destination status remains unreviewed/noncanonical.

# Erdos Problem #99 - Target B fractional balanced-grain exclusion

**Date:** 2026-09-05  
**Run type:** quantitative local-to-global diameter/train coupling  
**Target:** remove dominant-component hypothesis in the balanced phase regime  
**Depends on:** coarea grain decomposition; GMC1-GMC2; balanced tripartite stability and corrected dual-tree grid extraction; trimmed-grid diameter estimate; componentwise Mantel  
**LEVEL I STATUS:** STILL OPEN

## 1. Setup

Let a coarea train component `H` be asymptotically balanced, with three coherent phase classes of equal size

`m,m,m`

up to `o(D)` errors. Write its internal physical crossing count as

`E=(2-epsilon)m^2+o(D^2)`,                              (1.1)

where `epsilon>=0` is the balanced Theorem-51 deficit.

Let `R_*` be the total retained crossing count after an `o(D^2)` coarea cut, so

`R_*/D^2 -> Delta_2=pi/(2sqrt(3))=1/c`.                (1.2)

Let

`Theta=E/R_*`                                           (1.3)

be the global crossing-mass fraction of this grain, and put

`x=T/D`.                                                 (1.4)

Assume `Theta` has a fixed positive lower limit, so `m=Theta(D)`. The coarea interface has only `o(D^2)` crossing edges; after a fixed-fraction central trim, TG1 therefore makes genuinely external separator contributions `o(m)`. Sending the trim fraction to zero after the asymptotic limit gives the same balanced grid estimate as in the dominant-component proof, but now with the exact global fraction `Theta` retained.

## 2. Exact global normalization for one fractional grain

From (1.1)-(1.3),

`(2-epsilon)m^2 = Theta Delta_2 D^2+o(D^2)`.

Therefore

### Lemma FBG1 - fraction/diameter identity

`boxed{
D^2/m^2
 = c(2-epsilon)/Theta + o(1).
}`                                                       (2.1)

This replaces the dominant-component upper bound used in the previous balanced report. It is an identity and is valid no matter how the residual rhombi are distributed among the other grains.

## 3. Balanced grid gives an upper bound on the grain fraction

The audited balanced combinatorial lemma says that a balanced tripartite graph with deficit `epsilon` and no transversal triangle contains a phase pair with missing density at most

`mu<=4sqrt(epsilon)`.                                   (3.1)

The corrected dual-tree extraction gives a complete grid after omitting, normalized by `m`, at most

`L(epsilon)=6 epsilon^(1/4)+4sqrt(epsilon)+o(1)`        (3.2)

from the two selected phase classes.

The balanced trimmed-grid diameter argument, including the full coherent cancellation of the third phase and paying the omitted selected-phase trains twice, gives

`D^2/m^2`

`>=3-4sqrt(3)[6epsilon^(1/4)+4sqrt(epsilon)]-o(1)`.     (3.3)

Put

`Q(epsilon)=3-4sqrt(3)[6epsilon^(1/4)+4sqrt(epsilon)]`. (3.4)

Whenever `Q(epsilon)>0`, combine (2.1) and (3.3):

### Theorem FBG2 - fractional balanced-grain cap

`boxed{
Theta
<= U(epsilon):=c(2-epsilon)/Q(epsilon)+o(1).
}`                                                       (3.5)

At exact balanced saturation,

`U(0)=2c/3=0.7351051939...`.                            (3.6)

Thus an exact or nearly exact balanced phase component cannot carry an arbitrary fraction of the global rhombi even when other macroscopic grains are present.

## 4. The same grain and the residual grains consume train count

The balanced grain itself uses

`3m`

train vertices. All other coarea components use disjoint train vertices.

Their total crossing mass is

`R_*-E=(1-Theta)Delta_2D^2+o(D^2)`.

Componentwise Mantel, aggregated over the residual components, gives a train requirement of at least

`2sqrt((1-Theta)Delta_2)D-o(D)`.                        (4.1)

Using (2.1), the balanced grain uses

`3m/D=3sqrt(Theta Delta_2/(2-epsilon))+o(1)`            (4.2)

of train count in diameter scale.

Hence:

### Theorem FBG3 - balanced-grain train budget

`boxed{
x
>=
3sqrt(Theta Delta_2/(2-epsilon))
+2sqrt((1-Theta)Delta_2)
-o(1).
}`                                                       (4.3)

This is independent of the detailed phase structure of all residual grains.

## 5. Combine with global grain concentration

When

`x<2sqrt(2Delta_2)`,

GMC2 forces the largest coarea grain to have fraction at least

`G(x)=1/2[1+sqrt(1-(x^2/(4Delta_2)-1)^2)]`.             (5.1)

Suppose the **largest** grain is balanced. Then any asymptotic survivor must admit a number `Theta` satisfying simultaneously

`G(x)<=Theta<=U(epsilon)`                               (5.2)

and

`x>=3sqrt(Theta Delta_2/(2-epsilon))`

`   +2sqrt((1-Theta)Delta_2)`.                          (5.3)

Equations (5.2)-(5.3) are an explicit fractional balanced-grain feasibility test. No dominant-component assumption remains.

## 6. Exact consequence at the current Section-39 train lower edge

The current Section-39 lower coefficient is

`x_0=8/(3sqrt(c))=2.5395008183...`.                     (6.1)

At this value GMC2 gives

`G(x_0)=0.8142696805...`.                               (6.2)

For `epsilon=0`, the train-budget right side in (5.3) is strictly larger than `x_0` throughout

`G(x_0)<=Theta<8/9`,

and equals `x_0` at

`Theta=8/9`.                                             (6.3)

Thus a balanced largest grain at the lower train edge must satisfy

`Theta>=8/9-o(1)`.                                      (6.4)

Now `U(epsilon)` is continuous and increasing from `U(0)=0.735105...` for sufficiently small positive `epsilon`. Let `epsilon_*` be the first positive solution of

`U(epsilon_*)=8/9`.                                     (6.5)

Direct evaluation gives

`boxed{
epsilon_*=2.3516153... * 10^(-8).
}`                                                       (6.6)

Therefore:

### Corollary FBG4 - explicit fractional balanced deficit at the train lower edge

Along any survivor sequence with

`T/D -> 8/(3sqrt(c))`,

if the largest coarea grain is balanced, then

`boxed{
liminf epsilon >=2.3516*10^(-8).
}`                                                       (6.7)

This conclusion allows the residual `1-Theta` fraction of the rhombi to occupy arbitrary other grains.

It is genuinely stronger in scope than the existing `10^(-7)` dominant balanced-gap theorem: the coefficient is smaller, but no assumption `Theta->1` is made.

## 7. Neighborhood of the lower edge

The same argument is stable. For every

`x<2sqrt(2Delta_2)`,

define `epsilon_min(x)` as the infimum of `epsilon>=0` for which there exists

`Theta in [G(x),min(1,U(epsilon))]`

satisfying the train budget (5.3). Then a balanced largest grain must obey

`epsilon>=epsilon_min(x)-o(1)`.                         (7.1)

The function is explicit and can be evaluated without any additional geometric input. It remains positive on a nontrivial interval above `x_0` and eventually falls to zero before the two-equal-grain threshold as the global train budget loosens.

## 8. Scope

FBG2-FBG4 treat only a balanced largest coherent grain. They do not classify unique-max or strongly unbalanced largest grains, and they do not by themselves improve the global lower bound on `T/D`.

The next useful extension is the corresponding fractional theorem for a general three-phase grain. The exact identity is already

`D^2/M^2=c(s+t-Delta)/Theta+o(1)`,                       (8.1)

and the explicit local grid proofs provide lower bounds on the left side whenever the relevant phase pair is sufficiently dense. The task is to optimize those inequalities jointly with the residual-grain Mantel train budget.

## Handoff

```text
Balanced coarea grain:
  E=(2-epsilon)m^2,
  Theta=E/R_*.

Exact global identity:
  D^2/m^2=c(2-epsilon)/Theta+o(1).

Balanced grid geometry:
  D^2/m^2 >= Q(epsilon)-o(1),
  Q=3-4sqrt(3)(6epsilon^(1/4)+4sqrt(epsilon)).

Therefore
  Theta <= U(epsilon)=c(2-epsilon)/Q(epsilon).

Train accounting, including all residual grains:
  x=T/D >= 3sqrt(Theta Delta_2/(2-epsilon))
             +2sqrt((1-Theta)Delta_2)-o(1).

At x=8/(3sqrt(c)), a balanced largest grain requires Theta>=8/9 and hence
  epsilon>=2.3516e-8.

No dominant-component assumption is used.
```
