> Generated reading edition · [exact source](../../../docs/audits/target_c_shared_carrier_disjoint_return_independent_audit_2026-10-09.md) · source SHA-256 `8b6eb1d014ed9816b62f5db7cc7b650523340aefcf95be1309ecc1264041ef4f`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-3F862A8F9EEC","canonical":false,"claim_ids":["C-SHARED-CARRIER-DISJOINT-RETURN-COST-REGRESSION"],"claim_statuses":{"C-SHARED-CARRIER-DISJOINT-RETURN-COST-REGRESSION":"regression"},"index":"docs/state/artifact-index.jsonl","status":"regression","target":"target-c"} -->
# Independent audit: shared-carrier disjoint-return cost regression

**Date:** 2026-10-09
**Audit base:** origin/main=13b85eb8ad44f4977d4442f4c8c00d60f0761b7a, state 2026-10-09.audit.179.
**Target:** C-II. C-I is closed; C-II and Level I remain open.
**Frozen source:** research/level-i-closure at 12f6833725f281ce39a6d04ebcb45630b3a6768f.
**Source report SHA-256:** 73f65612ab38b46a9c9077a65fe3cd03019c2809ffd2c4268a9fee94f960c7c0.
**Source verifier SHA-256:** 2bff52b7c060ff5bef102dca9d727292eae58cf3973404d55212de81bc366f1e.
**Run type:** independent audit and promotion of a scoped regression. No discovery branch was modified.

## Exact claim and scope

For every integer $`m\ge12`$, there is a finite rational unit-separated source with

- exactly $`2m(m+1)+2`$ points and exactly the index-adjacent unit contacts;
- $`2m(m-1)`$ strict unit rhombi, $`4m+2`$ complete contact trains, and total strict-rhombus area excess $`O(m)`$;
- a $`6m`$-vertex artificial pin set $`B_m`$, strictly positive pinned contact equilibrium, and full pinned infinitesimal contact rigidity;
- a train-bank carrier $`K_N`$ with exactly $`8m`$ contact edges;
- $`|X_m|=m/3+O(1)`$ distinct train terminals whose maximum number of vertex-disjoint returns to $`B_m`$ is 2 inside $`K_N`$, but $`|X_m|`$ in the full contact graph, with every such full-graph return system using at least $`|X_m|\lfloor m/3\rfloor=\Omega(m^2)`$ edge occurrences.

The source is strictly nonglobal for every $`m\ge12`$, and $`B_m`$ is not its actual diameter-endpoint set. This is therefore a regression to the reduced inference

```math
\text{small common contact carrier + positive pinned equilibrium and rigidity}
\;\not\Rightarrow\;
\text{full-graph disjoint returns paid once by the carrier edge count}.
```

It is not a counterexample to any theorem requiring actual loaded diameter endpoints, canonical full-source KKT, or global minimum-diameter optimality. In particular it does not contradict C-TRAIN-CUT-HULL-BANK or C-QUADRATIC-CORE-DISJOINT-TRAIN-RETURNS.

## Independent reconstruction

Set $`u=(1,0)`$,
```math
r_m=\frac{\lfloor m/\sqrt3\rfloor+2}{m},\qquad
v_m=\left(\frac{1-r_m^2}{1+r_m^2},\frac{2r_m}{1+r_m^2}\right),
```
and let $`R(t)`$ be rotation by $`2\arctan t`$. For $`1\le j\le m`$, put
```math
t_j=\frac{m+1-2j}{100m^2},\qquad
v_j^-=R(t_j)v_m,\quad v_j^+=R(-t_j)v_m,\quad
V_j^\pm=\sum_{k=1}^jv_k^\pm,\quad V_0^\pm=0.
```
The symmetry $`t_{m+1-j}=-t_j`$ gives $`V_m^-=V_m^+`$. Include labels $`(i,j)`$ for $`0\le i\le m-1`$, and $`m+1\le i\le2m`$, at positions $`iu+V_j^-`$ and $`iu+V_j^+`$, respectively, for $`0\le j\le m`$. Include only the two middle labels $`(m,0),(m,m)`$, at their common endpoint positions. Thus $`n_m=2m(m+1)+2`$. Define $`B_m`$ by $`i\in\{0,2m\}`$ or $`j\in\{0,m\}`$.

The integer floor is exact: $`\lfloor m/\sqrt3\rfloor=\lfloor\sqrt{3m^2}/3\rfloor=\operatorname{isqrt}(3m^2)//3`$. If $`\theta`$ is the direction angle of $`v_m`$, then
```math
\frac1{\sqrt3}+\frac1m<r_m<\frac1{\sqrt3}+\frac2m<\frac34.
```
Since $`2/(1+r^2)>32/25`$ for $`r<3/4`$, the mean-value theorem gives $`\theta-\pi/3>32/(25m)`$. Each perturbation angle has magnitude less than $`1/(50m)`$, so every increment angle exceeds $`\pi/3+63/(50m)`$. The largest increment angle is less than $`2\arctan(3/4)+1/600<\pi/2`$. Also $`\cos(2\arctan(3/4))=7/25`$ and cosine is 1-Lipschitz, so each x-coordinate is greater than $`7/25-1/600=167/600>1/4`$; the angle lower bound makes it less than $`1/2`$. Thus
```math
\frac14<(v_j^\pm)_x<\frac12,\qquad (v_j^\pm)_y>\frac45,\qquad |v_j^\pm|=1.
```
The chord bound for a rotation gives
```math
|V_j^\pm-jv_m|<\frac1{50}.
```

These estimates classify every pair, not just the intended contact rows. Within one grain, row difference at least two gives vertical separation greater than $`8/5`$. For adjacent rows, the same-column pair has unit length; the nearest off-column diagonal has squared length $`2-2(v_j^\pm)_x>1`$, and pairs with larger column difference have horizontal separation greater than one. Same-row distinct points have integer horizontal separation. Across grains, column indices differ by at least two. For row difference at most one the horizontal separation exceeds $`2-1/2-1/25>1`$; for row difference at least two the vertical separation exceeds $`8/5-1/25>1`$. The middle labels are the corresponding common endpoints, so the same within-grain bounds apply. Therefore the actual unit contacts are exactly horizontal and vertical index-adjacent pairs. Index-sum parity makes the contact graph bipartite, hence triangle-free; there are no contact isolates.

Every cell in either grain is a strict unit rhombus: its sides are $`u`$ and $`v_j^\pm`$, and its area is $`(v_j^\pm)_y>\sqrt3/2`$. There are $`2m(m-1)`$ cells. The direction error from $`v_m`$, and the angle excess of $`v_m`$ over $`\pi/3`$, are $`O(1/m)`$; the sine function is Lipschitz, so each cell's excess area is $`O(1/m)`$, and total excess is $`O(m)`$.

For the pinned equilibrium, orient vertical edges upward and assign weight $`1/(v_j^\pm)_y`$. Write $`s_j^\pm=(v_j^\pm)_x/(v_j^\pm)_y=\cot(\arg v_j^\pm)`$ and $`\beta_j^\pm=s_{j+1}^\pm-s_j^\pm`$. The left angles strictly decrease, so $`\beta_j^->0`$; the right angles strictly increase, so $`\beta_j^+<0`$. On interior-row horizontal edges assign
```math
a_{i,j}^-=(m-1-i)\beta_j^-\quad(0\le i\le m-2),\qquad
a_{i,j}^+=(i-m)(-\beta_j^+)\quad(m+1\le i\le2m-1).
```
These weights are strictly positive. At every unpinned vertex the vertical weighted force sum is $`-\beta_j^\pm u`$, while the horizontal weighted force sum is $`+\beta_j^\pm u`$, including the one-sided inner-wall vertices. Top and bottom horizontal edges have both endpoints pinned and may be assigned weight one. Thus every unpinned vertex is in exact positive equilibrium; reactions on $`B_m`$ are unrestricted artificial-pin reactions.

Pinned infinitesimal rigidity is also direct. On each horizontal row, the horizontal bar equations make the x-velocity constant from its pinned outer endpoint, hence zero throughout the row. With these x-velocities zero, each vertical bar equation has nonzero y coefficient $`(v_j^\pm)_y`$; starting from the pinned bottom row forces every y-velocity to zero. This yields an explicit full-column-rank triangular minor of order $`2|A_m\setminus B_m|`$.

## Carrier and return accounting

Opposite sides of the $`2m(m-1)`$ strict rhombi give $`2(m-1)`$ horizontal trains of degree $`m`$, $`2m`$ vertical trains of degree $`m-1`$, and four singleton cap trains. Hence $`T=4m+2`$. Take the nonsingleton trains as the selected family and the four singleton trains as $`N`$. Under the canonical carrier definition, $`K_N`$ is the outer contact walk together with the middle-gap bounded face boundary; the cap edges are already on the outer walk, and the two inner walls add $`2m`$ edges. Directly, this is exactly the set of contact edges with both endpoints in $`B_m`$, together with the two inner-wall chains. Thus
```math
|E(K_N)|=8m\le2T.
```
The middle gap is a convex strip: its left-wall slope $`dx/dy=\cot(\arg v_j^-)`$ increases with height and its right-wall slope decreases, with collinear top and bottom caps. Its boundary has $`2m+4`$ sides and area $`O(m)`$.

Choose
```math
X_m=\{(m-1,j):\lceil m/3\rceil\le j\le\lfloor2m/3\rfloor\}.
```
These vertices lie on distinct vertical trains and are matched train terminals. The left inner wall in $`K_N`$ is a simple chain meeting $`B_m`$ only at its bottom and top ends. Deleting those two vertices separates all of $`X_m`$ from every pin; the two wall paths to those endpoints show that the endpoint-inclusive minimum vertex cut, and thus the maximum number of vertex-disjoint returns in $`K_N`$, is exactly two.

In the full contact graph, each row path from $`(m-1,j)`$ to $`(0,j)`$ is a contact path to a distinct pin, and these paths are pairwise vertex-disjoint. Their number
```math
|X_m|=\lfloor2m/3\rfloor-\lceil m/3\rceil+1=m/3+O(1)
```
is maximal because there are only $`|X_m|`$ roots. Every contact changes one index by one. From any chosen root, a path to a pin must reach $`i=0`$, $`i=2m`$, $`j=0`$, or $`j=m`$; the corresponding Manhattan distance is at least $`\lfloor m/3\rfloor`$. Therefore every full-graph disjoint return system has total length at least
```math
|X_m|\lfloor m/3\rfloor=\Omega(m^2),
```
whereas the shared carrier has $`8m`$ edges. In particular, for all sufficiently large $`m`$ the return length exceeds the entire carrier edge count, and the ratio grows without bound. This disproves a uniform one-time carrier-edge payment for full-graph disjoint returns under these weaker hypotheses.

## Why the scope does not conflict with canonical results

The point $`(m,0)\in B_m`$ is the midpoint of the collinear source points $`(m-1,0)`$ and $`(m+1,0)`$, so it is not a hull extreme point and cannot be an actual diameter endpoint. The pin set is therefore strictly larger than the actual loaded set. Independently, the opposite corners have horizontal separation greater than $`9m/4`$, so
```math
D_m^2>\frac{81}{16}m^2>2n_m\qquad(m\ge12).
```
An $`n_m`$-point crop of the unit square grid has squared diameter $`2(\lceil\sqrt{n_m}\rceil-1)^2<2n_m`$, a strict same-cardinality unit-separated competitor. Thus no member is globally optimal.

C-PINNED-GRID-RETURN-SQRT-REGRESSION bounds return count in a different pinned grid model; C-FAN-PATH-COMMON-TRUNK-REGRESSION concerns overlapping unique paths through an isolate trunk. Neither gives this train-rich family with a small canonical-style carrier and quadratic total length for a maximum full-graph disjoint return family. Conversely, this construction lacks actual loaded endpoints and globality, so it does not refute C-TRAIN-CUT-HULL-BANK, Audit.180's disjoint-return theorem, or the C-II source hypotheses. It records precisely why those two canonical conclusions cannot be combined into an independently paid carrier-length bound without an additional bridge.

## Certificate and disposition

I inspected and reproduced the frozen source checker, then made the promoted copy self-contained by embedding its integral vertex-split max-flow helper; it has no nonstandard dependencies. The registered checker uses exact Fraction arithmetic, verifies every source pair and contact, the positive stress and rigidity minor, and both endpoint-inclusive cut/flow values at $`m=12,16,24`$. These runs checked 919,727 source pairs in total and returned carrier/full-graph capacities $`2/5`$, $`2/5`$, and $`2/9`$, with carrier sizes $`96,128,192`$. Independent extra exact runs at $`m=13,25`$ also passed. This finite certificate checks fixtures only; the all-$`m`$ statements above are supplied by the analytic argument.

**Verdict: REGRESSION VALID — promote C-SHARED-CARRIER-DISJOINT-RETURN-COST-REGRESSION.** Its exact scope is the artificial-pin, pinned-equilibrium/rigidity implication stated above. The C-II frontier remains unchanged: an actual-source finite move or strict diameter improvement with all source lower and upper constraints is still required.
