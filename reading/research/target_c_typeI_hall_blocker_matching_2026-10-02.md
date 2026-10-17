> Generated reading edition · [exact source](../../research/target_c_typeI_hall_blocker_matching_2026-10-02.md) · source SHA-256 `0fde3534915db5703fe306936399789d4ffe143b6e08c31a6972be7f80113c71`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target C-II — Hall blocker matching in a protected inactive chamber

**Date:** 2026-10-02  
**Remote main immediately before writing:** `0031d1d932d07ad657bf5efa34cfd16a3d249b02`  
**Classification:** proved candidate awaiting independent audit; noncanonical.  
**LEVEL I STATUS:** STILL OPEN. C-II REMAINS OPEN.

## 1. Separation from the active fan route

The current October main tail is developing the full-core leaf-fan / degree-two-fan
route. This note attacks the other canonical branch: a macroscopic inactive container
with quadratic isolate population. It uses none of the recent fan reports.

The existing audited open-guard exchange rules out one extra protected packing site.
The new point here is a finite Hall strengthening: every finite unit-separated test
packing in a protected open region must have a system of distinct actual isolate
blockers.

Dependencies used below are only the contact-minimal canonical normalization, the
Section-77 macroscopic inactive chamber and its source partition, and elementary
convex geometry / Hall's marriage theorem. No KKT statement is applied to isolate
coordinates.

## 2. Abstract Hall blocker theorem

Let $`A`$ be a triangle-free global minimizer of cardinality $`n`$ and diameter
$`D=D(n)`$, chosen with the minimum number of unit contacts among triangle-free global
minimizers. Put $`K=\operatorname{conv}A`$.

Fix a nonisolated contact vertex $`v\in A`$, and let
$`Z\subset A\setminus\{v\}`$ be a finite set of actual contact-isolated source points.
Let $`W\subset\operatorname{int}K`$ be open and satisfy

```math
 |x-a|>1
 \qquad
 (x\in W,\ a\in A\setminus(Z\cup\{v\})).
\tag{H.1}
```

Take any finite unit-separated set $`B\subset W`$. Form a bipartite graph between
$`B`$ and $`Z`$ by

```math
b\sim z \iff |b-z|\le1.
\tag{H.2}
```

### Theorem H.1 — Hall blocker condition

For every $`T\subseteq B`$,

```math
\boxed{|N_Z(T)|\ge |T|.}
\tag{H.3}
```

Consequently there is an injection

```math
\boxed{\phi:B\hookrightarrow Z}
\tag{H.4}
```

with

```math
\boxed{|b-\phi(b)|\le1\quad(b\in B).}
\tag{H.5}
```

### Proof

Assume some $`T\subseteq B`$ has $`|N_Z(T)|<|T|`$. Put
$`Z_T=N_Z(T)`$, and choose

```math
T_0\subseteq T,\qquad |T_0|=|Z_T|+1.
\tag{H.6}
```

By definition of $`Z_T`$,

```math
|t-z|>1
\quad
(t\in T_0,\ z\in Z\setminus Z_T).
\tag{H.7}
```

The set $`T_0`$ is finite, $`W`$ is open, and every cross inequality in
(H.1) and (H.7) is strict. Dilate $`T_0`$ by a sufficiently small factor
$`1+\varepsilon`$ about any fixed center. For small positive $`\varepsilon`$, all
pairwise distances inside the moved set become strictly greater than one, all moved
points stay in $`W`$, and every strict cross inequality remains strict. Call the
moved set $`T_0'`$.

Define

```math
A'=\bigl(A\setminus(Z_T\cup\{v\})\bigr)\cup T_0'.
\tag{H.8}
```

Equation (H.6) gives $`|A'|=|A|`$. The new set is unit-separated and creates no
new unit contact. All new points lie in $`\operatorname{int}K`$, while retained old
points lie in $`K`$, so $`\operatorname{diam}A'\le D`$. If the inequality is strict,
global optimality is contradicted. Otherwise $`A'`$ is another triangle-free global
minimizer of diameter $`D`$.

The deleted points $`Z_T`$ had no contacts, while $`v`$ had at least one, so in the
diameter-$`D`$ case $`A'`$ has strictly fewer unit contacts than $`A`$, contradicting
the contact-minimal normalization. Thus (H.3) holds.

Hall's marriage theorem now gives (H.4), and (H.5) is exactly the edge condition.
$`\square`$

The theorem is stronger than the scalar packing bound $`|B|\le|Z|`$: different test
sites require different actual isolate blockers.

## 3. Macroscopic internal-chamber consequence

Work in the canonical Section-77 subquadratic-core branch, where one actual convex
inactive chamber $`C_*`$ is macroscopic. Let $`Z_*`$ be its assigned contact-isolated
source set. Write

```math
z_*=|Z_*|,\qquad
A_*=\operatorname{area}(C_*),\qquad
P_*=\operatorname{per}(C_*).
```

Section 77 gives

```math
A_*=\Omega(D^2),\qquad
z_*=\Omega(D^2),\qquad
P_*=O(D),
\tag{H.9}
```

and isolate-only Oler slack $`\sigma_*=O(D)`$. From

```math
\sigma_*={A_*\over a_0}+{P_*\over2}+1-z_*,
\qquad a_0={\sqrt3\over2},
```

it follows that

```math
\boxed{A_*/a_0=z_*+O(D).}
\tag{H.10}
```

Take the open depth-one body

```math
W_*=(C_*)_{-1}
=\{x\in C_*:\operatorname{dist}(x,\partial C_*)>1\}.
\tag{H.11}
```

Every source point not assigned to $`Z_*`$ lies outside
$`\operatorname{int}C_*`$. Hence every $`x\in W_*`$ is strictly farther than one
from every such source point, so (H.1) holds.

For a convex body, inner-parallel coarea gives

```math
\operatorname{area}(W_*)\ge A_*-P_*=A_*-O(D)
\tag{H.12}
```

for all sufficiently large $`D`$. Therefore

```math
\boxed{\operatorname{area}(W_*)/a_0\ge z_*-O(D).}
\tag{H.13}
```

Let $`\Lambda`$ be the unit triangular lattice. Translation averaging over one
fundamental cell gives a translate $`t+\Lambda`$ for which

```math
B_t=(t+\Lambda)\cap W_*
```

satisfies

```math
|B_t|
\ge \operatorname{area}(W_*)/a_0
\ge z_*-O(D).
\tag{H.14}
```

The set $`B_t`$ is unit-separated, so Theorem H.1 gives an injection

```math
\phi:B_t\hookrightarrow Z_*,
\qquad
|b-\phi(b)|\le1.
\tag{H.15}
```

### Corollary H.2 — near-perfect lattice-to-isolate blocker matching

For every sufficiently large survivor in the canonical macroscopic internal-chamber
branch, one translate of the unit triangular lattice has at least

```math
\boxed{z_*-O(D)}
\tag{H.16}
```

sites in the protected depth-one body that match injectively to distinct actual
chamber isolates, each within distance at most one. Since
$`z_*=\Omega(D^2)`$, only $`O(D)`$ chamber isolates need remain unmatched.

This simultaneously strengthens the canonical pointwise unit-cover statement for the
protected body. It is one common lattice phase, not a collection of independently
chosen sites.

## 4. Remaining obstruction

No computation is used. The Hall theorem is exact, but it does not close Type I.
The displacement bound is only one; it does not identify the isolate packing with an
affine triangular lattice or create a spare site.

The new obstruction is sharper: a surviving macroscopic chamber must realize a
near-perfect system of distinct blockers for one global triangular-lattice test
packing. A next closing step must turn this bottleneck matching into a genuine spare
site, a source-preserving collective compression, or an exact-contact pattern
incompatible with triangle-free global minimality.

The full-core leaf-fan route is untouched.
