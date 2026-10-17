> Generated reading edition · [exact source](../../../docs/reports/target_c_two_phase_star_common_core_uniqueness_2026-10-01.md) · source SHA-256 `cdeb975851d8ac7a7c0aac934d7c97c69605b576e9ce8c77907a7ee8060ec4cc`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-D6D6F32FA9C1","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II -- uniqueness of a two-phase diameter star near the rooted endpoint

Base main: \`4ebb870269f4b68a5adf3ee5e16e7c4b9b7a542f\`. Proof-only; C-II remains open.

Let

```math
a_D=\arcsin\frac1{2D},
\qquad
E_D=\pi-2a_Dq.
```

Current main proves global diameter-star contiguity: for every diameter vertex $`v`$,
the projective directions of the edges incident with $`v`$ form one interval
$`I_v`$ of length at most $`\pi/3`$, and every diameter-edge direction lying in
$`I_v`$ is incident with $`v`$. It also proves that every shared consecutive
direction gap contributes its excess above $`2a_D`$ as a nonnegative summand of
$`E_D`$.

Section 90 supplies two fixed inverse-phase train shores $`A_*,B_*`$. Their
reduced phases lie in one half-open interval

```math
[s,s+W_D),
\qquad
W_D=\frac{4K}{D},
```

and their phase labels are distinct.

## Theorem (common-core obstruction)

For all sufficiently large $`D`$, after swapping the two shores if necessary
and choosing one real lift of the projective direction circle, the train
directions can be written as

```math
\theta(\tau)=x_\tau,\quad \tau\in A_*,
\qquad
\theta(\sigma)=x_\sigma+\frac\pi3,\quad \sigma\in B_*,
```

with every $`x_\rho\in[s,s+W_D)`$.

Suppose two distinct diameter vertices $`v,w`$ each straddle at least one
direction from $`A_*`$ and at least one direction from $`B_*`$. Then

```math
\boxed{
E_D\ge \frac\pi6-\frac{W_D}{2}-2a_D.
}
\tag{1}
```

Consequently, whenever

```math
E_D<\frac\pi6-\frac{W_D}{2}-2a_D,
\tag{2}
```

there is at most one two-phase diameter star.

### Proof

Fix one two-phase star $`v`$. Choose
$`\tau\in A_*`$ and $`\sigma\in B_*`$ whose directions are straddled by $`v`$.
Write

```math
a=x_\tau,
\qquad
b=x_\sigma+\frac\pi3.
```

Because $`v`$ straddles both directions, current main gives $`a,b\in I_v`$.
Also $`|I_v|\le\pi/3`$. For large $`D`$, $`W_D<\pi/6`$, so
$`b-a\in(\pi/6,\pi/2)`$; hence this is the unique shorter projective arc
between the two directions. Since a connected projective interval of length at
most $`\pi/3`$ contains both $`a`$ and $`b`$, necessarily

```math
b-a\le\frac\pi3.
```

Thus $`x_\sigma\le x_\tau`$, and the whole shorter arc $`[a,b]`$ lies in
$`I_v`$. Since

```math
a\le s+W_D,
\qquad
b\ge s+\frac\pi3,
```

every two-phase star interval contains the same deterministic core

```math
J_D:=
\left[s+W_D,\ s+\frac\pi3\right],
\qquad
|J_D|=\frac\pi3-W_D.
\tag{3}
```

Now suppose $`v\ne w`$ are both two-phase stars. Then
$`J_D\subset I_v\cap I_w`$.

By global diameter-star contiguity, every diameter edge whose direction lies in
$`I_v`$ is incident with $`v`$. Therefore any diameter edge incident with $`w`$
whose direction lies in $`J_D`$ is incident with both $`v`$ and $`w`$. Since
the diameter graph is simple, there is at most one such edge, namely $`vw`$.

Order the directions of the edges incident with $`w`$ along $`I_w`$. The core
$`J_D\subset I_w`$ contains at most one of those directions. If it contains
none, one consecutive pair of $`w`$-incident directions brackets all of
$`J_D`$, so its gap is at least $`|J_D|`$. If it contains exactly one direction,
that point splits $`J_D`$ into two subintervals, one of length at least
$`|J_D|/2`$; the consecutive $`w`$-incident gap on that side has at least that
length. In either case there is a shared consecutive diameter-direction gap
$`g`$ with

```math
g\ge\frac{|J_D|}{2}
=\frac\pi6-\frac{W_D}{2}.
\tag{4}
```

A shared gap has baseline $`2a_D`$, and its excess is a nonnegative summand of
the global excess $`E_D`$. Hence

```math
E_D\ge g-2a_D
\ge
\frac\pi6-\frac{W_D}{2}-2a_D,
```

which proves (1).

## Endpoint and near-endpoint consequences

In the rooted wrapping branch current main gives

```math
E_D\le\Delta(\lambda)+o(1),
\qquad
\Delta(\lambda)
=
\frac\pi2-
\left(\lambda+4\lambda\sqrt{1-\lambda^2}\right).
```

Therefore any rooted sequence with

```math
\limsup_D\Delta(\lambda_D)<\frac\pi6
```

has, for all sufficiently large $`D`$, at most one two-phase diameter star.

At the exact rooted endpoint,
$`\Delta(\lambda_1)=0`$, so

```math
\boxed{
\text{for all sufficiently large endpoint survivors, at most one diameter
vertex straddles directions from both Section-90 phase shores.}
}
\tag{5}
```

Combining (5) with the previous star-span estimate, that unique vertex, if it
exists, has

```math
\deg_H(v)\ge\left(\frac\pi3-o(1)\right)D.
\tag{6}
```

The Section-157 corollary is immediate: all single-star two-sided bracing that
uses the same diameter vertex for at least one train from each inverse-phase
shore can occur at only one diameter vertex. This strengthens the previous
"at most three" conclusion.

The remaining escape is now sharper. Either one asymptotically maximal diameter
star absorbs the cross-phase single-star bracing, or the Section-157 witnesses
for a linear train family must be phase-separated among different stars and/or
split across star transitions. The next target is to bound the multiplicity of
that split-star mechanism.

No computation, verifier, numerical experiment, or CI result is used.
