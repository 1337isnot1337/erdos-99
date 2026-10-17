> Generated reading edition · [exact source](../../../docs/reports/target_c_near_equilateral_strict_rhombic_regression_2026-09-11.md) · source SHA-256 `fc76f9f9e9adebcd85817a035ea6187c792a61a3b72aa6f0a3871f36e3e06582`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-9EC2C87BDD08","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_near_equilateral_strict_rhombic_regression_2026-09-11.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=0d6f83c4e31f0734739f22f02febce04005714a9; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — strict near-equilateral rhombic regression

**Date:** 2026-09-11
**Target:** Target C, C-II
**Status:** proved regression, hold report

## Statement

There is no uniform density or angular-area gap for triangle-free unit-separated
configurations. More precisely, for every large (D), let

```math
\theta_D=\frac\pi3+D^{-2},
\qquad
u=(1,0),qquad v=(\cos\theta_D,\sin\theta_D),
```

and let

```math
\Lambda_D=\mathbb Zu+\mathbb Zv,qquad
X_D=\Lambda_D\cap B(0,D/2).
```

Then:

1. every two distinct points of (X_D) have distance at least one;
2. (X_D) contains no unit equilateral triangle;
3. (|X_D|/D^2	o\pi/(2\sqrt3)), the triangular-packing density in this
   normalization;
4. the complete bulk parallelogram cells are strict unit rhombi and their total area
   excess above (sqrt3/2) is (O(1)).

The construction is not asserted to be a diameter minimizer. It is a regression
against proofs that try to obtain the Erdős conclusion from a fixed angular gap,
fixed positive rhombic area excess, or a purely asymptotic density deficit.

## Proof

For an integer vector (au+bv),

```math
|au+bv|^2=a^2+b^2+2ab\cos\theta_D.
```

If (ab\ge0) and both coefficients are nonzero, this is greater than one; if one
coefficient is zero, it is at least one, with equality only for the four vectors
(±u,±v). If (ab<0), put (p=|a|), (q=|b|). Since
(cos\theta_D<1/2),

```math
|au+bv|^2>p^2+q^2-pq\ge1.
```

Thus the shortest nonzero lattice vectors are exactly (±u,±v), all of length
one. This proves unit separation of (X_D). It also proves that the only unit edges
in the full lattice have those four directions. The difference of any two distinct
vectors from ({pm u,pm v}) has length strictly greater than one, so three lattice
points cannot form a unit equilateral triangle.

The fundamental parallelogram of (Lambda_D) has area

```math
\det(u,v)=\sin\theta_D.
```

The standard lattice-point estimate for a disk, obtained by covering the disk
boundary strip by (O(D)) fundamental cells, is

```math
|X_D|=\frac{\pi D^2}{4\sin\theta_D}+O(D).
```

Because

```math
\sin\theta_D=\frac{\sqrt3}{2}+\frac{1}{2D^2}+O(D^{-4}),
```

we get

```math
\frac{|X_D|}{D^2}\longrightarrow
\frac{\pi}{2\sqrt3}.
```

Away from the disk boundary, the lattice contact complex contains the parallelogram
tiling with unit sides (u,v). Every complete bulk cell has area
(sin\theta_D), so its excess above (a_0=sqrt3/2) is

```math
\sin\theta_D-a_0=\frac{1}{2D^2}+O(D^{-4}).
```

There are (O(D^2)) complete bulk cells, so their total excess is (O(1)). This claim
deliberately does not assign an excess to the (O(D)) boundary faces of the truncated
contact complex. (square)

## Exact use in C-II

The regression shows why the following implications are invalid without a
source-specific global-optimality argument:

```math
\text{triangle-free}\Longrightarrow
\text{uniform angle gap above }\pi/3,
```

```math
\text{triangle-free rhombic bulk}\Longrightarrow E\ge cD^2,
```

and

```math
\text{asymptotically optimal density}\Longrightarrow
\text{a unit equilateral triangle}.
```

The construction is compatible with the current (E=O(D)) ledger and, after taking
(	heta_D-pi/3) even smaller, with any prescribed sublinear bulk angular-excess
scale. It does not pass the global-minimality requirement: the construction only
gives a feasible packing with the correct leading density. Proving or disproving
that a globally diameter-minimal source can realize this near-equilateral phase is
still the unresolved global step.
