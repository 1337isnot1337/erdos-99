> Generated reading edition · [exact source](../../research/target_c_quantitative_atomic_outer_endpoint_charge_hostile_audit.md) · source SHA-256 `711393d4cbc828958f9788331c65a18d0042369541904b487211a126022382d2`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "3a2f106690d86a2ebc63e1fbfdbe34ff3d166637", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_quantitative_atomic_outer_endpoint_charge_hostile_audit.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "b98547f34653f49fabd93dfb3593c475d7b5800bf7823e064245629d60dd0042"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit and correction — quantitative atomic outer-endpoint charge

**Date:** 2026-09-12  
**Audited source:** `research/target_c_quantitative_atomic_outer_endpoint_charge.md`  
**Verdict:** **core theorem (AO.4) PASS; scalar corollary (AO.21) has one factor-two typo and is corrected below.**  
**Theorem-state authority:** unchanged.  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

## 1. Cusp inequality — PASS

Let `mu_out` be a limiting normalized outer-walk projective direction measure,

```math
M=\|\mu_{out}\|=\pi+\lambda,
\qquad
H(\alpha)=\int|\cos(\theta-\alpha)|\,d\mu_{out}(\theta).
```

Type-II width convergence gives `H>=2`, while `H<=M`. Put `g=H-2>=0`.
Because

```math
\int_0^\pi|\cos t|dt=2,
```

```math
\int_0^\pi g=2\lambda.
```

Distributionally on the projective circle,

```math
(|\cos|)''+|\cos|=2\delta_{\pi/2},
```

so

```math
g''=2R_*\mu_{out}-H\ge-M.
```

An atom of mass `A` gives an upward derivative jump `2A`. Hence either the right
derivative is at least `A` or the left derivative is at most `-A`. Since
`g''>=-M`, on the corresponding side

```math
g(t)\ge At-{M\over2}t^2
\qquad(0\le t\le A/M).
```

Therefore

```math
2\lambda=\int g\ge {A^3\over3M^2},
```

so

```math
\boxed{A^3\le6M^2\lambda.}
```

The distributional inequality is legitimate: `g'+Mt` is a nondecreasing BV function;
positive singular mass can only increase its derivative. No smoothness of the outer
walk is assumed.

**Disposition:** PASS.

## 2. Global atomic train-mass upper bound — PASS

The source uses

```math
T=h-s_Z+2f.
```

Canonical/audited ledgers give

```math
h\le q\le\pi D,
\qquad
f\le Q\le q.
```

The last inequality follows from

```math
b+Q=2(q-k),
\qquad b=q+x_B,
\qquad x_B\ge0,
```

so `Q=q-2k-x_B<=q`. Hence

```math
T\le3\pi D,
```

and the limiting absolute atomic train mass `A` satisfies `A<=3pi`.

**Disposition:** PASS.

## 3. Heavy/light crossing capacity — PASS

The exact limiting phase relation has degree two: each projective phase atom can cross
at leading order only its two `+-pi/3` neighbors.

For threshold `tau`, heavy-light pair capacity is at most

```math
2\tau H\le2\tau A,
```

because each heavy atom has at most two light phase neighbors. Within a three-atom
orbit whose entries are all light,

```math
ab+bc+ca\le\tau(a+b+c),
```

so all light-light capacity is at most `tau A`. Therefore crossing capacity incident
to at least one light atom is at most

```math
3\tau A\le9\pi\tau.
```

The remaining heavy-heavy physical crossing graph is still triangle-free, so weighted
Mantel gives

```math
H_\tau\ge2\sqrt{\Delta_2-9\pi\tau}.
```

Also `N_tau<=3pi/tau`. These are the exact constants used in (AO.4).

**Disposition:** PASS.

## 4. Endpoint hosting — PASS

Every complete train has two terminal occurrences, and an outer terminal edge has the
same projective contact direction as its train. For a heavy limiting train atom, a
shrinking-neighborhood/then-source-limit argument sends its outer terminal population
to an atom of `mu_out` at the same direction. The cusp lemma therefore caps those
outer endpoints by

```math
C_{atom}(\lambda)
=[6(\pi+\lambda)^2\lambda]^{1/3}.
```

Summing the residual endpoint demand over the heavy atoms gives

```math
\boxed{
\liminf {Q+4f\over D}
\ge
4\sqrt{\Delta_2-9\pi\tau}
-{3\pi\over\tau}C_{atom}(\lambda).
}
\tag{AOC.1}
```

This is source equation (AO.4).

**Disposition:** PASS.

## 5. Correction to the scalar corollary

The source then uses

```math
{Q+4f\over D}\le5{Q\over D}
```

and

```math
{Q\over D}=2{q-k\over D}-\pi-\lambda+o(1).
```

If

```math
F(\lambda,\tau)
:=4\sqrt{\Delta_2-9\pi\tau}
-{3\pi\over\tau}C_{atom}(\lambda),
```

then

```math
5\left(2{q-k\over D}-\pi-\lambda\right)
\ge F(\lambda,\tau)-o(1).
```

Dividing by `10` gives the corrected formula

```math
\boxed{
\liminf {q-k\over D}
\ge
{\pi+\lambda\over2}
+{2\over5}\sqrt{\Delta_2-9\pi\tau}
-{3\pi\over10\tau}C_{atom}(\lambda).
}
\tag{AOC.2}
```

The source file prints `3pi/(20tau)` in its equation (AO.21). That coefficient is too
small by a factor of two. Equation (AOC.2) supersedes source (AO.21).

At `lambda=0`, the penalty vanishes and `tau->0` still recovers exactly

```math
{q-k\over D}
\ge{\pi\over2}+{2\over5}\sqrt{\Delta_2},
```

so the connection to audited-working §154 is unchanged.

## 6. Small-detour asymptotics

The core theorem (AOC.1) has

```math
C_{atom}(\lambda)=O(\lambda^{1/3}).
```

Choosing `tau` on the scale `lambda^(1/6)` balances the square-root capacity loss and
the `C_atom/tau` term. Therefore

```math
{Q+4f\over D}
\ge4\sqrt{\Delta_2}-O(\lambda^{1/6})
```

as `lambda->0`. This asymptotic claim is unaffected by the scalar-corollary typo.

## 7. Final disposition

- **AO.4 / AOC.1:** certified proof-only quantitative endpoint-host theorem.
- **AO.5:** certified.
- **AO.21:** rejected as printed only because of the factor-two arithmetic slip.
- **AOC.2:** corrected scalar consequence.
- **Whole Type-II closure:** not obtained.

The useful new structural result is AOC.1: linear outer detour can host atomic train
endpoints only according to an explicit cusp-stability modulus, while the remainder
must be absorbed by bounded defect faces.
