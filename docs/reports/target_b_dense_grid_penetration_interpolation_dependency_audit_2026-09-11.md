<!-- theorem-state: {"artifact_id":"ART-212DE83C2067","canonical":true,"claim_ids":["TB-DENSE-GRID"],"claim_statuses":{"TB-DENSE-GRID":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-b"} -->
# Erdős Problem #99 — independent audit of Target B dense-grid, penetration, and interpolation chain

**Date:** 2026-09-11  
**Run type:** independent dependency / regression audit  
**Target:** Target B pure-rhombic coherent-phase chain  
**LEVEL I STATUS:** STILL OPEN

## 1. Scope and verdict

This audit treats the September 5 `PASS` files as claims rather than as authority and rechecks the load-bearing chain used by the theorem-state entry `TB-DENSE-GRID`.

Audited candidates:

1. `target_b_dual_tree_dense_grid_extraction_correction_2026-09-05.md` (DT1--DT4);
2. `target_b_trimmed_grid_phase_star_exclusion_2026-09-05.md` (TG1--TG3);
3. `target_b_positive_density_dual_tree_grid_2026-09-05.md` (PDG);
4. `target_b_penetration_charged_grid_cancellation_2026-09-05.md` (PC1--PC3);
5. `target_b_multicomponent_penetration_budget_2026-09-05.md` (MCP1--MCP2);
6. `target_b_balanced_phase_stability_exclusion_2026-09-05.md` (the balanced graph lemma used downstream);
7. `target_b_explicit_general_phase_interpolation_2026-09-05.md` (GPI).

**Verdict:** the chain is mathematically valid under its stated pure-disk/coherence/dominant-component hypotheses. One proof-presentation correction is required in MCP2: its componentwise `o(D)` coherence losses may be summed only after using the fixed-`lambda` Section-50 component-count bound. That bound is available, so the theorem survives unchanged at the `o(D^2)` scale.

This audit does **not** prove the Target B shell-stability endpoint and does not globalize GPI across several macroscopic grains.

## 2. DT1--DT4: the dual-tree repair is correct

The original statement

```text
pairwise noncrossing proper crosscuts of a disk => complement dual is a path
```

is false. The correction replaces it with the exact statement that the complement dual is a tree.

For `b` pairwise disjoint proper crosscuts, adding one crosscut splits one current region into two. Hence the complement has `b+1` regions and its region/crosscut dual is connected with `b` edges, therefore a tree.

A transverse train crosses each `B` train at most once, so its region sequence is an edge-simple trail in this tree. An edge-simple trail in a tree cannot revisit a vertex and is therefore a simple path. Thus each crossing set is a tree path.

If an `A-B` pair has missing density `epsilon=o(1)`, one `A` path contains at least `(1-epsilon)b` tree edges. Every other `A` crossing path intersects this backbone in a connected subpath. Markov plus trimming by `eta b` at both ends, with `eta->0` and `epsilon/eta->0`, yields a complete

```text
(M-o(M)) x (b-o(b))
```

grid.

No global path structure of the full complement dual is used.

## 3. TG1--TG3: trimmed-grid penetration and diameter cost

For two internally noncrossing families with complete mutual crossing, their endpoints occur in four alternating boundary blocks and the union is a topological rectangular grid.

After trimming `k` and `l` layers, every point of the retained central rectangle has both grid coordinates at least the corresponding trim depth, up to a fixed corner convention. Every disk-boundary region is exterior in at least one coordinate. Therefore any external proper train that separates a retained diagonal pair must cross at least

```text
min(k,l)-O(1)
```

selected grid tracks. The reported finite `min(k,l)-2` lower bound is safe.

The train-coordinate diagonal has the form

```text
p_11-p_00 = U+V+E.
```

The third coherent phase can contribute only coefficients in `{-1,0,1}`. Allowing its signed total to be any `xw` with `|x|<=a+o(M)` is therefore a worst-case relaxation, not an extra hypothesis.

For normalized class sizes `t=b/M`, `s=a/M`, the exact constrained squared norm is

```text
F(s,t)=1+t+t^2-s(1-t)+s^2,              s<(1-t)/2,
F(s,t)=3(1+t)^2/4,                       s>=(1-t)/2.
```

With `c=2sqrt(3)/pi`, the proof that `F(s,t)>c(s+t)` on `0<=s<=t<=1` is correct. The weaker uniform margin used later,

```text
gamma_0 = 3/4-c/2 = 0.1986711045...,
```

is safe: in the first branch the boundary value is `(1+t)(3(1+t)/4-c/2)>=gamma_0`, while the second branch has substantially larger margin on its feasible range.

Thus complete coherent phase stars carrying the quadratic pure-disk core are excluded under TG's stated hypotheses.

## 4. PDG: positive density gives a complete macroscopic rectangle

Let `l_alpha` be the length of the tree path crossed by `alpha`. Since

```text
sum l_alpha = rho M b,
```

paths of length at least `rho b/2` carry at least `rho M b/2` total length. Cauchy--Schwarz gives

```text
sum_long l_alpha^2 >= rho^2 M b^2/4.
```

A path of length `l` has at least `l^2/64` pairs formed by an edge in its first quarter and an edge in its last quarter. Fewer than `b^2/2` unordered tree-edge pairs exist. Double counting therefore gives a pair lying in at least

```text
rho^2 M/128
```

of the `A` paths. Every one of those paths contains the unique tree subpath between that edge pair, of length at least

```text
rho b/4-O(1).
```

Hence the reported complete rectangle bounds

```text
|A'| >= rho^2 M/128,
|B'| >= rho b/4-O(1)
```

are correct.

The same-phase noncrossing premise is also valid in the triangle-free strict-rhombic branch: if two unit-rhombus trains cross with acute projective angle `theta`, both diagonals being at least one forces `theta>=pi/3`; equality creates a unit equilateral triangle. An `o(1)` coherent phase class therefore cannot contain a crossing pair for sufficiently large `D`.

## 5. PC1 and PC3: penetration charging is exact

Let `S_ext` be external separator trains for a retained diagonal and put `d=min(k,l)-2>0`. TG1 gives at least `d` grid crossings for every separator. These are distinct physical rhombi, and they are disjoint from the internal `M b` complete-grid rhombi. Thus, if `X` is their count,

```text
X >= d |S_ext|,
|E| <= |S_ext| <= X/d,
D >= |U+V|-|E|,
```

which yields exactly

```text
R >= M b + d(|U+V|-D)_+.
```

The coherent three-phase functional in PC3 is also consistent. For

```text
u=(1,0),
v=(1/2,sqrt(3)/2),
w=(-1/2,sqrt(3)/2),
L(x,y)=x+y/sqrt(3),
```

one has `L(u)=L(v)=1`, `L(w)=0`, and `||L||=2/sqrt(3)`. In-component third-phase trains cancel `L` at rate at most `1+o(1)` per separator, while arbitrary outside-component trains cancel at rate at most `2/sqrt(3)`.

Every crossing between a retained-component train and a train outside that retained component is a deleted Section-50 edge; otherwise both endpoints would lie in the same retained component. Therefore `X_out<=E_del(H)` is valid, and elimination gives the reported PC3 interface term with coefficient

```text
2/sqrt(3)-1.
```

The symmetric PC1 threshold is also numerically correct: the positive root of

```text
t^2 + (sqrt(3)t-1)^2/(8sqrt(3)) = pi/(2sqrt(3))
```

is

```text
t = 0.9374561097455733...
```

## 6. MCP1--MCP2: multiplicity two is correct; summability must be stated

For complete grids chosen in distinct retained components, internal grid crossing sets are disjoint.

A physical crossing edge can be used as an external penetration charge by at most the retained components containing its two train endpoints. Therefore it appears in at most two `X_j` sets. If both endpoints lie in one retained component, it can be charged only there; if the edge is an internal grid edge, it is not an external penetration edge for that grid. Thus

```text
2R >= sum_j (|G_j|+|X_j|)
```

and MCP1 is exact.

Similarly,

```text
sum_j E_del(H_j) <= 2 E_del.
```

The existing MCP2 presentation writes a componentwise phase-coherence error as `o(D)` inside `sum_j d_j(...)`. A bare sum of little-oh terms would be unjustified if the number of components grew without control.

The required control is available. For fixed Section-50 pruning parameter `lambda>0`, every nonempty retained component has minimum degree at least `lambda D`, hence at least `lambda D+1` train vertices. Target B has total train count `T=O(D)`. Therefore the number of retained components is `O_lambda(1)`. Also `d_j=O(D)`, and the coherent angular error is uniform `o(1)` on the selected coherent components. Consequently the total phase-coherence contribution is

```text
sum_j d_j o(D) = o(D^2)
```

for fixed `lambda`.

With that explicit quantifier order, the additive MCP2 form is valid at the stated `D^2` scale. The positive-part form remains the sharper statement.

## 7. Balanced graph lemma: the explicit `4 sqrt(epsilon)` constant is safe

For three classes of size `m` and no transversal triangle, define

```text
d(a,b,c)=2-[1_ab+1_bc+1_ca].
```

Then

```text
sum d = 2m^3-mE <= epsilon m^3.
```

If one phase pair is already missing at most `4sqrt(epsilon)m^2` edges, stop. Otherwise remove at most `sqrt(epsilon)m` high-defect vertices from each of two shores and choose a low-defect missing edge `a_0b_0` with good endpoints. Its common-neighbor set in the third class has size at least

```text
(1-sqrt(epsilon)/2)m.
```

The induced two-color decomposition gives

```text
|A_1||B_1||C_*| <= epsilon m^3,
```

so one of `A_1,B_1` has size at most `sqrt(2epsilon)m`. Counting all possible missing edges from that small set, from `C\C_*`, and from the good block gives a coefficient below `3 sqrt(epsilon)` for small `epsilon`. Thus the downstream explicit relaxation

```text
missing density <= 4 sqrt(epsilon)
```

is safe.

The older report's use of an interval-neighborhood theorem must be read through DT1--DT4; the combinatorial lemma itself is unaffected.

## 8. GPI: the local interpolation theorem is valid

Let `M>=b>=a`, `t=b/M>=tau>0`, `s=a/M`, and

```text
Delta=[M(a+b)-E]/M^2.
```

### 8.1 Largest-second missing floor

If the missing density `mu` in the `A-B` pair were at most

```text
mu_0=8e-5,
```

DT4 with `eta=sqrt(mu)` yields an almost-full complete grid whose total two-shore omission, normalized by `M`, is

```text
L <= 3sqrt(mu)+mu+o(1).
```

Relative to the ideal TG vector, omitted `A/B` trains can shorten the two coherent sums and can reappear with arbitrary signed separator coefficients. The total norm perturbation is at most `2LM+o(M)`. Since the ideal optimized norm is at most `sqrt(3)M`,

```text
D^2/M^2 >= F(s,t)-4sqrt(3)L-o(1).
```

At `mu_0`,

```text
4sqrt(3)(3sqrt(mu_0)+mu_0)
=0.1864574568...,
```

while `gamma_0=0.1986711045...`; the residual margin is about `0.01221`. Thus the uniform missing floor is not a rounding artifact.

### 8.2 Transversal-triple inequality

Writing

```text
e_AB=Mb-x,
e_AC=Ma-y,
e_BC=z,
```

triangle-freeness gives

```text
M z <= a x+b y.
```

Therefore

```text
Delta M^2=x+y-z
             >=(1-s)x+(1-t)y
             >=(1-s)x,
```

and the missing floor gives

```text
1-s <= Delta/(mu_0 tau)+o(1).
```

Hence small `Delta` forces all three class sizes to balance.

### 8.3 Random balancing and restored trains

Randomly restrict `A,B` to size `a` and keep `C`. The `AB`, `AC`, `BC` edge survival probabilities are respectively `s^2/t`, `s`, `s/t`, and the latter two are at least `s^2/t`. Thus some deterministic balanced restriction has

```text
E_0/a^2 >= (s+t-Delta)/t.
```

Its balanced deficit satisfies

```text
epsilon_bal <= [Delta/(mu_0 tau)+Delta]/tau+o(1).
```

The balanced lemma plus DT4 yields an almost-full complete grid. Every original train deleted by the random balancing step is restored as arbitrary signed train-coordinate error; their normalized total is bounded by

```text
L_del=2(1-s)/s.
```

Genuinely external-component separators are `o(a)` after a fixed positive central trim because the hypothesis gives only `o(a^2)` external crossing mass and TG1 charges `Theta(a)` crossings per separator. Sending the trim fraction to zero after the asymptotic limit is valid.

### 8.4 Explicit threshold

Under

```text
Delta < 4e-17 tau^2,
```

one obtains eventually

```text
1-s < 5e-13,
epsilon_bal < 1e-12,
L_grid < 0.00601,
```

and therefore

```text
D^2/a^2 > 2.95.
```

The dominant-component hypothesis gives the incompatible translated-lattice upper bound

```text
D^2/a^2 < 2.21
```

eventually. The numerical margins are enormous relative to the chosen constant. Thus

```text
liminf Delta >= 4e-17 tau^2
```

is valid under GPI's stated dominant coherent-component hypotheses.

## 9. Exact scope after audit

The following statements may be promoted as canonical scoped Target B tools:

- corrected dual-tree dense-grid extraction DT1--DT4;
- complete-grid penetration TG1 and phase-star exclusion TG2--TG3;
- positive-density grid extraction PDG;
- penetration-charged cancellation PC1 and coherent interface form PC3;
- multicomponent multiplicity budget MCP1 and fixed-`lambda` additive MCP2;
- explicit dominant-component interpolation GPI.

The following remain **unproved** by this chain:

1. the full Target B shell-stability inequality;
2. a theorem forcing one dominant coherent component to carry the global quadratic core;
3. a globalization of GPI across several macroscopic grains;
4. a contradiction from Section 50 + density-only PDG constants alone.

The active multi-grain obstruction is therefore real: retained physical crossings, deleted/interface crossings, and virtual noncrossing determinant mass still need one common global inequality.
