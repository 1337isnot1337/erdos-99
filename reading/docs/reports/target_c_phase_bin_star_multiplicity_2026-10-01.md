> Generated reading edition · [exact source](../../../docs/reports/target_c_phase_bin_star_multiplicity_2026-10-01.md) · source SHA-256 `dcc35ca5748cd97e26bad9f78bf5400c7dad8f7415efad4a056e83491dcf69d9`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-F1F7ABF9BA79","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II -- bounded star multiplicity inside an inverse-diameter phase bin

Base main: aa872a0e2aa2b74a011e9a86b8083bc985a0bcb7. Proof-only; C-II remains open.

Let
```math
a_D=\arcsin\frac1{2D}.
```

Current main gives:

1. every diameter star occupies one contiguous projective-direction interval $`I_v`$, and every diameter-edge direction in $`I_v`$ is incident with $`v`$;
2. every consecutive shared-endpoint diameter-direction gap has length at least $`2a_D`$.

Call a projective direction $`u`$ straddled by $`v`$ if two diameter rays from $`v`$ have opposite strict transverse signs with respect to $`u`$, as in the current Section-157 corollary.

## Theorem 1 -- narrow-bin straddling multiplicity

Let $`J`$ be a projective-direction interval of length $`0<W<\pi`$, and put
```math
S(J)=\{v:\text{ some }u\in J\text{ is straddled by }v\}.
```
Then
```math
\boxed{|S(J)|\le \left\lfloor\frac{W}{2a_D}\right\rfloor+2.}
\tag{1}
```

### Proof

For each $`v\in S(J)`$, choose a straddled direction $`u_v\in J`$. Straddling is open in direction, so perturb $`u_v`$ arbitrarily slightly inside $`J`$ so that it is not itself a diameter-edge direction and remains straddled.

Choose a real lift of $`J`$. Let $`d_v^-<u_v<d_v^+`$ be the immediately preceding and following global diameter-edge directions.

Because $`v`$ straddles $`u_v`$, there are $`v`$-incident diameter directions on both sides of $`u_v`$. Hence $`d_v^-`$ and $`d_v^+`$ lie in the contiguous star interval $`I_v`$. Global star contiguity therefore forces both bounding diameter edges to be incident with $`v`$.

Thus
```math
G_v=(d_v^-,d_v^+)
```
is a shared-endpoint consecutive gap, so
```math
|G_v|\ge 2a_D.
\tag{2}
```

Distinct vertices give distinct gaps. If $`G_v=G_w`$, its two distinct bounding diameter edges would both be incident with both $`v`$ and $`w`$, impossible in a simple graph.

The global consecutive direction gaps have disjoint interiors. Among the distinct $`G_v`$ meeting $`J`$, at most two are not wholly contained in $`J`$, one through each endpoint. Every remaining $`G_v\subset J`$ has length at least $`2a_D`$, so there are at most
```math
\left\lfloor\frac{W}{2a_D}\right\rfloor
```
of them. Adding the two boundary gaps proves (1).

## Section-90 consequence

Section 90 puts every train on either retained phase shore into a reduced-phase interval of width
```math
W_D=\frac{4K}{D}.
```
Adding the fixed phase label preserves this width in actual projective direction. Since
```math
2a_D=2\arcsin\frac1{2D}\ge\frac1D,
```
Theorem 1 gives
```math
\boxed{|S(A_*)|,\ |S(B_*)|\le C_K:=\lfloor4K\rfloor+2.}
\tag{3}
```

Therefore single-star two-sided bracing cannot diffuse over $`\Theta(D)`$ diameter vertices within one Section-90 phase shore. Audited-working Section 157 says that a single-star two-sided brace must straddle the train direction, so all such braces from one shore use at most $`C_K`$ diameter vertices.

More precisely, let $`L_A`$ be any collection of outer-to-outer trains from $`A_*`$, and suppose $`s_A`$ of them have no single diameter vertex carrying opposite-sign Section-157 witnesses. Then some diameter vertex single-star braces at least
```math
\boxed{\frac{|L_A|-s_A}{C_K}}
\tag{4}
```
of the remaining trains. The same holds for $`B_*`$.

Thus any linear-sized outer-to-outer subfamily on one phase shore obeys the exact dichotomy
```math
\boxed{\text{either }\Omega(D)\text{ trains are genuinely split-star, or one fixed diameter star braces }\Omega(D)\text{ trains.}}
\tag{5}
```

No endpoint limit is needed.

## Theorem 2 -- crossing train directions cannot share one bracing star

If two retained Section-90 trains cross in a strict rhombus, Section 68 orients their directions so that
```math
\phi_2-\phi_1\equiv\frac\pi3+\delta_R\pmod\pi,
\qquad 0<\delta_R\le\frac\pi6.
```
Hence
```math
d_{\mathbb P}(\phi_1,\phi_2)=\frac\pi3+\delta_R>\frac\pi3.
\tag{6}
```

Every diameter-star interval has span at most $`\pi/3`$. Therefore
```math
\boxed{\text{no diameter vertex straddles the directions of two Section-90 trains that cross in a strict rhombus.}}
\tag{7}
```

In particular, if two crossing outer-to-outer trains are each single-star two-side braced, their bracing vertices are distinct.

## Frontier effect

The previous endpoint work reduced cross-phase single-star bracing to at most one two-phase star. The present theorem removes a separate diffuse escape inside each narrow phase shore: single-star bracing there concentrates into at most $`C_K`$ fixed diameter stars.

The next target is now exact. For any linear outer-to-outer Section-90 subfamily, either prove a multiplicity bound for the genuinely split-star trains, or contradict the alternative in which one fixed diameter star two-side braces a linear ordered train family.

This report does not assert that all Section-90 local trains are outer-to-outer. The Section-157 consequences apply only to outer-to-outer members.

No computation, verifier, numerical experiment, or CI result is used.
