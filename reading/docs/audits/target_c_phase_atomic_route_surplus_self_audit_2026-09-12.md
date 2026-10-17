> Generated reading edition · [exact source](../../../docs/audits/target_c_phase_atomic_route_surplus_self_audit_2026-09-12.md) · source SHA-256 `467ee66e100ec87a34ddede865b5406736540a26c77fcf219872fc6b51716a1c`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-37769EEEB3AD","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — hostile self-audit of phase-atomic route surplus

**Date:** 2026-09-12  
**Artifact audited:** `research/target_c_phase_atomic_route_surplus.md`  
**Disposition:** PASS at proof-only scope after the checks below.  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

## 1. What must fail if the theorem is wrong

The theorem assumes a Type-II subsequence with

```math
S_D:=(b+P_{exc})-\operatorname{per}(F)=o(D)
```

and derives two incompatible descriptions of the limiting area-weighted reduced-phase measure:

1. simple-crossing capacity plus `sum delta_e=O(D)` makes the limit purely atomic;
2. the rotating equilateral punctured-return inequalities make convolution with a kernel having every nonconstant Fourier coefficient nonzero constant, hence force Haar measure.

The audit separately checks both implications.

## 2. The stopped train graph really is simple

The full strict-rhombus complex is a finite edge-to-edge strict-rhombus complex, possibly disconnected and with holes. Canonical Theorem 10.6, already used in the promoted pseudosegment-grid audit, applies componentwise: every stopped train centerline is a simple arc, no train closes, and two train centerlines cross at most once.

Every strict rhombus is exactly one proper crossing of its two stopped train centerlines. Hence the train crossing graph has exactly `R_4` edges and no repeated edge between one pair of stopped trains.

This simplicity is essential. Without it, `Theta(D^2)` rhombi could in principle be carried by repeated crossings of only `O(D)` phase pairs, and the pair-capacity argument in Section 3 of the research note would not follow.

## 3. The train count is at most half the route length

Every stopped train has exactly two terminal strict-rhombus side occurrences. The opposite face at each terminal occurrence is either the global outer face or one bounded nonquadrilateral face. Therefore both terminals occur in the route system counted by

```math
B_{route}=b+P_{exc}.
```

A route occurrence may fail to border a strict rhombus, so equality is not asserted. The safe inequality is

```math
2T_D\le B_{route}.
```

Under `S_D=o(D)` and Type-II `per(F)/D->pi`, this gives

```math
T_D/D\le\pi/2+o(1).
```

No harmonic-cell multiplicity enters.

## 4. Phase-close pair capacity forces atoms in the raw train measure

Let

```math
\mu_D=D^{-1}\sum_\tau\delta_{x_\tau}.
```

At a strict-rhombus crossing the circular reduced-phase distance is exactly the acute-angle excess `delta_e` because `0<delta_e<=pi/6`, half the reduced-phase circle length. Canonical Section 68 gives

```math
\sum_e\delta_e=O(D).
```

For each fixed `epsilon>0`, all but `O(D/epsilon)` crossing edges therefore join train phases at circular distance at most `epsilon`.

Because the graph is simple, those are distinct unordered train pairs. Thus

```math
(\mu_D\times\mu_D)\{d(x,y)\le\epsilon\}
\ge2R_4/D^2-o(1).
```

For the closed `epsilon`-diagonal neighborhood, Portmanteau gives the inequality in the required direction:

```math
\limsup_D(\mu_D\times\mu_D)(F_\epsilon)
\le(\mu\times\mu)(F_\epsilon).
```

Since the left side has lower bound `2Delta_2`, the limit does as well. Sending `epsilon downarrow0` yields

```math
\sum_x\mu(\{x\})^2\ge2\Delta_2=\pi/\sqrt3.
```

So the limiting raw train measure has atoms. The diagonal/self-pair contribution `T_D/D^2` tends to zero and does not affect the constant.

## 5. A diffuse raw phase part cannot carry positive edge-endpoint mass

This is the most delicate step.

Let `eta_D` be the probability measure obtained by placing one unit of mass at each endpoint of each train-crossing edge and normalizing by `2R_4`. Fix a compact set `E` containing no atom of the weak limit `mu`.

For any `varepsilon>0`, uniform nonatomicity on `E` permits a finite interval cover, refined to disjoint half-open intervals `J_i`, such that

```math
\mu(J_i^{+})<2\varepsilon
```

for arbitrarily small fixed enlargements `J_i^+`, with all endpoints chosen as continuity points of `mu`.

For fixed phase radius `epsilon`, all but `O(D/epsilon)` graph edges are `epsilon`-good. A good directed edge endpoint in `J_i` must have its opposite endpoint in `J_i^epsilon`. Simplicity therefore gives

```math
M_D(J_i)
\le N_D(J_i)N_D(J_i^\epsilon)+O(D/epsilon),
```

where `M_D` counts directed graph-edge endpoints and `N_D` train vertices. Sum over `i`, divide by `2R_4=Theta(D^2)`, first take `D->infinity`, then choose `epsilon` below the fixed enlargement widths. Since every enlarged interval has `mu` mass below `2varepsilon`, the sum is at most a constant times

```math
\varepsilon\sum_i\mu(J_i)
\le\varepsilon\mu(\mathbb T_L).
```

Letting `varepsilon->0` gives `eta(E)=0`. Inner regularity then shows that the entire nonatomic part of `mu` has zero `eta` mass.

Thus every weak limit of `eta_D` is supported on the countable atom set of `mu` and is purely atomic.

This argument does not require the raw measure `mu` itself to be purely atomic; only the **edge mass** must be.

## 6. Area weighting changes the endpoint measure by `o(1)`

Write every strict-rhombus area as

```math
a_0+\epsilon_R,
\qquad\epsilon_R\ge0.
```

Canonical Section 68 gives

```math
E_4:=\sum_R\epsilon_R=O(D),
```

while Type II gives `R_4=Theta(D^2)` and `A_4=Theta(D^2)`. For any test function of sup norm at most one, the difference between the area-weighted and constant-`a_0` endpoint averages is bounded by a constant multiple of

```math
E_4/A_4=o(1).
```

Therefore the return-relevant probability measure `nu_D` has the same weak limits as `eta_D`; every such limit is purely atomic.

## 7. Every equilateral rotation is realizable to `o(1)` host error

Type-II Hausdorff convergence of `D^{-1}F` to the radius-`1/2` disk is uniform in support direction. If `x_D(u)` is a support-maximizing vertex in direction `u`, then

```math
u\cdot x_D(u)\ge1/2-o(1),
\qquad
|x_D(u)|\le1/2+o(1),
```

uniformly in `u`, so its transverse component is uniformly `o(1)`.

For three support directions spaced by `2pi/3`, the chosen loaded extreme vertices therefore approach three equally spaced circle points. For all sufficiently large `D` they are distinct and occur in cyclic outer-face order. Their chord unit vectors approach a rotated equilateral host triple uniformly, and their triangle perimeter is

```math
(3\sqrt3/2+o(1))D.
```

Since width of a finite host set is Lipschitz in the host vectors, the return error is `o(A_4)=o(D^2)` uniformly in the rotation.

## 8. The route upper bound has exactly the disk mean under zero surplus

Under `S_D=o(D)`,

```math
B_{route}/D\to\pi.
```

Thus for every realized equilateral rotation,

```math
D(B_{route}-\Pi_3)
\le
\left(\pi-3\sqrt3/2+o(1)\right)D^2.
```

The punctured-return master gives this as an upper bound for actual return. Dividing by `2A_4`, with `2A_4/D^2->pi/2`, yields

```math
(k*\nu_D)(\rho)
\le2-3\sqrt3/\pi+o(1)
=\bar k+o(1)
```

uniformly in `rho`.

But the rotational mean of every convolution `k*nu_D` is exactly `bar k`. Any weak limit therefore satisfies `k*nu<=bar k` everywhere with average `bar k`, hence `k*nu` is identically constant.

## 9. Fourier coefficient check

Center one period at zero. The kernel is

```math
k(t)=2-\sqrt3\cos t,
\qquad |t|\le\pi/6,
```

periodically extended with period `pi/3`. For `n>=1`,

```math
\int_{-\pi/6}^{\pi/6}\cos t\cos(6nt)\,dt
={(-1)^{n+1}\over36n^2-1}.
```

Therefore the cosine coefficient is

```math
\widehat k_n
={6\sqrt3\over\pi}{(-1)^n\over36n^2-1},
```

which never vanishes. A constant convolution therefore kills every nonconstant Fourier coefficient of `nu`, forcing normalized Haar measure. Haar measure is nonatomic, contradicting Section 6.

## 10. Quantifier check

The research theorem states only

```math
\liminf S_D/D>0
```

along a Type-II survivor sequence. If the liminf were zero, one could pass to a subsequence with `S_D/D->0`; all Type-II asymptotics used above survive passage to a subsequence. That is exactly the contradiction proved.

No effective universal coefficient is claimed. A later compactness argument may extract one, but the present theorem does not need it.

## 11. What this does not prove

The theorem does **not** rule out Type II. It forces

```math
(b-\operatorname{per}(F))+P_{exc}=\Omega(D)
```

along every Type-II survivor sequence. Canonical Section 84 allows linear boundary-order mass in doubled near-geodesic inactive corridors or in a diffuse collection of smaller defects. Those cases remain live.

The macroscopic inactive-container branch remains completely separate.

**Audit verdict:** PASS at proof-only scope. No theorem-state promotion is attempted.
