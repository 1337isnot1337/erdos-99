> Generated reading edition · [exact source](../../research/target_c_cusp27_g0035_global_floor_2026-09-14.md) · source SHA-256 `e54499edfa4e5703f5f6ec718a96389f257491c105a3324641dab955ad2e6db0`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "e37f4cbeb5572a35c4704911b2e4a71dfb716648", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_cusp27_g0035_global_floor_2026-09-14.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "cc3a3378b3600c73d735f4dc3035a18cbfdf314ffa48ebd02aa5d46e7a781d19"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Erdős Problem #99 — coefficient-27 cusp propagation with `eta_grid=0.0035`

**Date:** 2026-09-14  
**Target:** Target C-II, canonical full-core Type-II branch  
**Dependency branch:** `research/c2-cusp35-sol-20260914`  
**Claim class:** proof-only propagation of the iterative-pruning atomic gap and three-cusp outer-detour theorem  
**LEVEL I STATUS:** `STILL OPEN`

This note combines two independent proof-only improvements:

1. the iterative-pruning six-pair theorem gives
   
   ```math
   C:={T-q/2\over D}\ge C_0:=2\sqrt{\Delta_2}+0.0035-o(1),
   \qquad \Delta_2={\pi\over2\sqrt3};
   ```

2. the three-cusp theorem replaces the Section-171 outer-atom coefficient `81` by `27` whenever
   
   ```math
   {\delta\over\pi+\delta}\le{\pi^3\over5184},
   \qquad
   \delta:=\lim {b-\operatorname{per}(F)\over D}.
   ```


Together they raise the all-Type-II scalar floor from the previous proof-only
`1.82129...` range to

```math
\boxed{
\liminf {q-k\over D}
\ge C_{146}+0.00452
=1.824033537979444\ldots,
}
\tag{C35.1}
```

where

```math
C_{146}={4\over9}\left(\pi+\sqrt{\Delta_2}\right).
```

The gain is not decimal tuning: most of it comes from summing all three separated outer cusps.

## 1. Coefficient-27 Section-171 scalar inequality

On a convergent Type-II subsequence write

```math
t=\lim {q-k\over D},
\qquad \delta=\lim {b-\operatorname{per}(F)\over D}.
```

The audited Section-171 algebra, with the three-cusp theorem substituted at its only changed step, gives the necessary inequality

```math
\boxed{
F_t^{(27)}(\delta):=
10t-5\pi-5\delta
+\left(27(\pi+\delta)^2\delta\right)^{1/3}
-{8\Delta_2\over {9t\over2}-2\pi-2\delta}
\ge0.
}
\tag{C35.2}
```

The atomic lower bound `C>=C_0` and the same Section-171 upper bound

```math
C\le {9t\over2}-2\pi-2\delta
```

imply

```math
0\le\delta\le
{ {9\over2}(t-C_{146})-0.0035\over2}.
\tag{C35.3}
```

## 2. Test the endpoint `t=C146+0.00452`

Set

```math
\varepsilon_{35}=0.00452,
\qquad
 t_{35}=C_{146}+\varepsilon_{35}.
```

Then the right endpoint of (C35.3) is exactly

```math
\boxed{\delta_{35}=0.00842.}
\tag{C35.4}
```

At this endpoint the denominator in (C35.2) is exactly

```math
2\sqrt{\Delta_2}+0.0035.
```

The exact certificate proves

```math
F_{t_{35}}^{(27)}(\delta_{35})<-3.8\times10^{-4}.
\tag{C35.5}
```

The direct floating-point value is about `-4.96e-4`; the displayed bound is the outward rational certificate.

## 3. The whole feasible interval lies in the three-cusp regime

Since every feasible detour under `t<=t35` satisfies `delta<=0.00842`,

```math
{\delta\over\pi+\delta}
\le {0.00842\over\pi+0.00842}
<0.002674.
```

The three-cusp threshold is

```math
{\pi^3\over5184}>0.005981.
```

Thus the coefficient-27 theorem is valid throughout the entire scalar domain used in the elimination, not merely at the endpoint.

## 4. Monotonicity closes the rectangle

Put

```math
q(\delta)=\left(27(\pi+\delta)^2\delta\right)^{1/3}.
```

For `delta>0`,

```math
q'(\delta)
={q(\delta)\over3}
\left({1\over\delta}+{2\over\pi+\delta}\right).
\tag{C35.6}
```

Equivalently, with `r=delta/(pi+delta)`,

```math
q'(\delta)=r^{-2/3}+2r^{1/3},
```

which strictly decreases as `delta` increases in `(0,infinity)`.

Also the denominator in the last term of (C35.2) is at least `C_0`. Hence throughout
`0<delta<=0.00842` and `t<=t35`,

```math
{\partial F_t^{(27)}\over\partial\delta}
\ge
-5+q'(0.00842)-{16\Delta_2\over C_0^2}
>43.
\tag{C35.7}
```

The exact certificate proves the last inequality. Thus `F_t^(27)` is strictly increasing in `delta` over the full feasible interval. It is also strictly increasing in `t`, since

```math
{\partial F_t^{(27)}\over\partial t}
=10+{36\Delta_2\over({9t\over2}-2\pi-2\delta)^2}>0.
\tag{C35.8}
```

Therefore for every `t<=t35` and every feasible `delta`,

```math
F_t^{(27)}(\delta)
\le F_{t35}^{(27)}(\delta_{35})<0,
```

contradicting the necessary condition (C35.2). This proves (C35.1).

The numerical root of the same endpoint equation is

```math
\varepsilon_*=0.00452427393213\ldots,
```

so `0.00452` keeps a visible certification margin.

## 5. Immediate global propagation

Write

```math
g=0.0035,
\qquad
C_0=2\sqrt{\Delta_2}+g
=1.908125613727914\ldots .
```

The correlated stopped-train split improves to

```math
\boxed{
\liminf {\rho_{rec}+\sigma_R-q\over D}\ge0.007,
}
\tag{C35.9}
```

so every survivor lies in at least one of

```math
\boxed{
{S\over D}\ge0.371292566607580\ldots-o(1)
}
\tag{C35.10}
```

or

```math
\boxed{
{\sigma_R\over D}\ge0.742585133215160\ldots-o(1).
}
\tag{C35.11}
```

The mandatory chamber/interface floor becomes

```math
\boxed{
\liminf {J\over D}
\ge t_{35}+2C_0-\pi
=2.498692111845480\ldots .
}
\tag{C35.12}
```

Using

```math
H={J\over2}+(q-k)-{\operatorname{per}(F)\over2},
```

one gets

```math
\boxed{
\liminf {H\over D}\ge1.502583267107288\ldots,
}
\tag{C35.13}
```

hence

```math
\boxed{
\liminf {A_{ch}-a_0Z_{ch}\over D}
\ge0.650637640308165\ldots,
}
\tag{C35.14}
```

and

```math
\boxed{
\liminf {\Delta_2D^2-R_4\over D}
\ge0.751291633553644\ldots .
}
\tag{C35.15}
```

The corrected residual allowance drops to

```math
\boxed{
\limsup {R_F+\Sigma_{ext}\over D}
\le {3\pi\over2}-t_{35}
=2.888355442405245\ldots .
}
\tag{C35.16}
```

There is still no scalar contradiction.

## 6. Revised low-`t` structural window

The topology budget is

```math
2\delta+{\kappa\over2}
\le R(t):={9t\over2}-2\pi-C_0,
\qquad \kappa={k\over D}.
\tag{C35.17}
```

At the new floor profile,

```math
R(t_{35})=0.01684,
```

so the coarse individual bounds are

```math
\delta\le0.00842,
\qquad
\kappa\le0.03368.
```

Those coarse bounds are weaker than the old coefficient-81 endpoint bounds because the scalar floor has moved substantially upward. The coefficient-27 inequality carries additional information that should not be discarded: just above `t35`, feasibility forces `delta` extremely close to its maximum, and therefore forces `kappa` back toward zero. This near-endpoint activation is treated separately rather than hidden in a coarse worst-case substitution.

Dropping `delta,kappa>=0` gives the endpoint-profile face bounds

```math
\boxed{
{f\over D}\ge0.498054422369096\ldots-o(1),
}
\tag{C35.18}
```

```math
\boxed{
{Q-f\over D}\le0.00842+o(1),
}
\tag{C35.19}
```

and

```math
\boxed{
{p_5\over D}\ge0.489634422369096\ldots-o(1).
}
\tag{C35.20}
```

The outer-to-outer train count remains linear:

```math
\boxed{
\liminf {L_{OO}\over D}\ge3\pi-5t_{35}
=0.304610270872157\ldots .
}
\tag{C35.21}
```

The outer-tooth / long-side burden becomes

```math
\boxed{
\liminf {N_2+2L_{>2}\over D}
\ge1.283879115610350\ldots,
}
\tag{C35.22}
```

hence

```math
\boxed{
\liminf {1\over D}\max\{N_2,L_{>2}\}
\ge0.427959705203450\ldots .
}
\tag{C35.23}
```

## 7. Frontier effect

The coefficient-27 cusp theorem changes the character of the scalar frontier. The correct next variable is no longer the absolute upper bound on detour; it is the **unused detour slack**

```math
\delta_{max}(t)-\delta.
```

By (C35.17), that slack controls the complete topology/rigidity defect:

```math
\kappa\le4\bigl(\delta_{max}(t)-\delta\bigr).
```

Since the scalar inequality forces `delta` toward `delta_max(t)` near the endpoint, the next closing theorem should combine this activation with the pentagon closure-rank and near-extremal Woodall structures. This is quantitatively stronger than using only `kappa<=2R(t)`.

Run

```bash
python3 research/verify_target_c_cusp27_g0035_global_floor.py
```

for the outward rational endpoint, cusp-regime, and derivative checks.

**Disposition:** proof-only global propagation. C-II and Level I remain open.
