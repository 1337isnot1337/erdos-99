> Generated reading edition · [exact source](../../../docs/reports/target_c_fixed_star_common_witness_pairs_2026-10-01.md) · source SHA-256 `0027bba452109a1667e0edc397992c037a032f7578aea95b854f0e2b5eab50c4`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-7BFC4947969D","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II -- fixed-star common witness-pair extraction

Date: 2026-10-01  
Base main: 77988b19e7e8b815c3e23a6a96f7bf618b0ab530  
Status: proof-only; C-II remains open.

## Theorem

Let $`\mathcal T`$ be a family of pairwise disjoint non-singleton global
outer-to-outer stopped trains whose crosscuts lie on one complement-dual path. Assume
all train projective directions lie in an interval $`J`$ of width $`W`$. Fix a
diameter vertex $`v`$, and let $`\mathcal L\subseteq\mathcal T`$ be a subfamily such
that every train in $`\mathcal L`$ is single-star two-sided braced by $`v`$ in the
sense of audited Section 157.

Put
```math
a_D=\arcsin\frac1{2D},
\qquad
M(W,D)=2\left(\left\lfloor\frac{W}{2a_D}\right\rfloor+1\right)+1.
\tag{1}
```

Then there is a subfamily $`\mathcal L'\subseteq\mathcal L`$ and two fixed distinct
actual diameter edges
```math
h_+=vx_+,\qquad h_-=vx_-
```
such that
```math
\boxed{
|\mathcal L'|\ge \frac{|\mathcal L|}{2M(W,D)}
}
\tag{2}
```
and $`h_+,h_-`$ cross every train cut in $`\mathcal L'`$ with opposite strict
transverse signs.

For a Section-90 phase shore $`W=4K/D`$. Since
```math
2a_D=2\arcsin\frac1{2D}\ge\frac1D,
```
one may take
```math
\boxed{M_K=2\lfloor4K\rfloor+3}
\tag{3}
```
and obtain
```math
\boxed{
|\mathcal L'|\ge \frac{|\mathcal L|}{2M_K}.
}
\tag{4}
```

No endpoint limit is used.

## Proof

Current main proves global diameter-star contiguity. The directions of all diameter
edges incident with $`v`$ form one interval $`I_v`$, and every global diameter
direction in $`I_v`$ is incident with $`v`$. Hence successive $`v`$-incident
directions are consecutive global directions. Their two edges share $`v`$, so the
canonical shared-gap bound gives separation at least $`2a_D`$.

Therefore the number $`N`$ of $`v`$-incident diameter directions lying in $`J`$
satisfies
```math
N\le \left\lfloor\frac{W}{2a_D}\right\rfloor+1.
\tag{5}
```

Choose a real lift of $`J`$. Partition $`J`$ into the $`N`$ singleton
diameter-direction thresholds and the open intervals between them, including the two
possible end intervals. There are at most
```math
2N+1\le M(W,D)
\tag{6}
```
classes.

For a fixed $`v`$-incident diameter ray $`r`$, the sign of $`r\cdot Ju`$, as a
function of projective train direction $`u\in J`$, can change only when $`u`$ equals
the projective direction of $`r`$. Thus on each open class every fixed ray has a
constant sign. On a singleton class all train directions are equal. In particular,
every strict witness sign is constant throughout one class.

The dual-path cuts are linearly ordered and $`v`$ lies in one complement region. At
least half of $`\mathcal L`$ lie on one side of that region. Retain that side and
pigeonhole its trains among the at most $`M(W,D)`$ phase classes. This gives a family
$`\mathcal L'`$ satisfying (2), all on one side of $`v`$ and all in one phase class.

Choose $`\tau_*\in\mathcal L'`$ whose cut is farthest from $`v`$ in the path order.
Since $`\tau_*`$ is single-star braced by $`v`$, choose two $`v`$-incident actual
diameter edges $`h_+,h_-`$ crossing $`\tau_*`$ with opposite strict transverse signs.

Each of these diameter rows has one endpoint in the layer containing $`v`$ and crosses
the farthest selected cut. By the exact laminar interval-support theorem, its support
contains every selected cut between $`v`$ and $`\tau_*`$. Hence
```math
h_+\pitchfork\tau,\qquad h_-\pitchfork\tau
\quad
(\tau\in\mathcal L').
\tag{7}
```

Finally, all train directions in $`\mathcal L'`$ lie in one phase class, so neither
strict transverse sign can change. Thus the same two fixed diameter edges are
opposite-sign witnesses for every train in $`\mathcal L'`$. This proves the theorem.

## Application to current main's complete O-O rectangle

Current main gives, in the fixed-star endpoint alternative, distinct diameter vertices
$`v\ne w`$ and a complete O-O rectangle $`A_v\times B_w`$ with
```math
|A_v|,|B_w|
\ge
\left(
\frac{\kappa^4}{16\pi^3 C_K}-o(1)
\right)D,
\qquad
C_K=\lfloor4K\rfloor+2,
\tag{8}
```
where $`v`$ single-star braces every train in $`A_v`$ and $`w`$ single-star braces
every train in $`B_w`$.

Each shore is pairwise noncrossing. Fixing one train on the opposite shore gives a
proper transversal crossing every crosscut on that shore exactly once. Hence the
crosscuts on each shore are linearly ordered on one complement-dual path.

Apply the theorem independently to both shores. There are subfamilies
```math
A^\sharp\subseteq A_v,\qquad B^\sharp\subseteq B_w
```
with
```math
\boxed{
|A^\sharp|,|B^\sharp|
\ge
\left(
\frac{\kappa^4}{32\pi^3 C_K M_K}-o(1)
\right)D
}
\tag{9}
```
and four fixed actual diameter edges
```math
h_A^+,h_A^-\ni v,
\qquad
h_B^+,h_B^-\ni w
\tag{10}
```
such that $`h_A^+,h_A^-`$ are opposite-sign witnesses for every train in
$`A^\sharp`$, while $`h_B^+,h_B^-`$ are opposite-sign witnesses for every train in
$`B^\sharp`$.

Every pair in $`A^\sharp\times B^\sharp`$ still crosses in an actual strict rhombus.
The two edges in each witness pair are distinct. The two witness pairs can share an
edge only if that edge is $`vw`$. Thus the retained linear-by-linear grid has a
universal Section-157 witness system supported on at most four fixed actual diameter
edges.

In the exact simultaneous laminar-shear coordinates on either shore, the two common
witness rows have full support on every retained train coordinate. Their first
derivatives $`2r_h\cdot Ju_i`$ have opposite strict signs throughout that shore.

## Remaining bottleneck

The fixed-star branch is reduced from cut-dependent witness pairs to
```math
\boxed{
\text{two linear crossing laminar families}
+
\text{at most four fixed full-support diameter rows}.
}
\tag{11}
```

The next target is a compatibility theorem between those rows, the convex
diameter-thrackle order, and the two inverse-phase complete-grid orders. The
split-star and inactive-interface branches remain separate.

No computation, numerical experiment, verifier, or CI output is used.
