> Generated reading edition · [exact source](../../research/target_c_sp1625_global_and_low_t_propagation_2026-09-14.md) · source SHA-256 `e6f82a9bac2edae34e99ef615668e169969b38a523ee54e7c1269c9983cf8783`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "5ffc4c3e4414232c1cc3e2de1e0c661328cad2cb", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_sp1625_global_and_low_t_propagation_2026-09-14.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "54c0863cb5d31ea930c136cb20013cb5687dfce61b487e26ccd21e5f7b6d7f19"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Erdős Problem #99 — SP1625 global and low-`t` propagation

**Date:** 2026-09-14  
**Target:** Target C-II, canonical full-core Type-II branch  
**Repository branch:** `research/c2-gluing-sol-20260914-r9`  
**Claim class:** proof-only propagation of the six-pair atomic theorem `eta_grid=0.001625`  
**Dependencies:** audited Section 171; the existing correlated/chamber ledgers; latest-main low-`t` pentagon/network and outer-tooth/long-side theorems  
**LEVEL I STATUS:** `STILL OPEN`

The six-pair theorem raises the proof-only atomic train gain to

```math
\boxed{g=0.001625.}
```

This note propagates that value through the existing scalar endpoint and then substitutes the resulting endpoint into the newest low-`t` structural theorems. No new local geometric inequality is introduced here.

Put

```math
\Delta_2={\pi\over2\sqrt3},\qquad
s_2=\sqrt{\Delta_2},\qquad
C_{146}={4\over9}(\pi+s_2),
```

and let

```math
\rho=0.7390851332151606\ldots
```

be the positive solution of `rho=cos(rho)` used in the existing correlated split.

---

## 1. Correlated stopped-train split

The exact identity

```math
\rho_{rec}+\sigma_R-q
=2\left(T-{q\over2}-2\sqrt{R_4}\right)
```

and SP1625 give

```math
\boxed{
\liminf {\rho_{rec}+\sigma_R-q\over D}\ge0.00325.
}
\tag{P1625.1}
```

Using `q/D>=2rho-o(1)`,

```math
\boxed{
\liminf {\rho_{rec}+\sigma_R\over D}
\ge2\rho+0.00325.
}
\tag{P1625.2}
```

Therefore at least one of

```math
\boxed{
S={\rho_{rec}\over2}
\ge\left({\rho\over2}+0.0008125-o(1)\right)D
=0.370355066607580\ldots D-o(D)
}
\tag{P1625.3}
```

or

```math
\boxed{
\sigma_R
\ge(\rho+0.001625-o(1))D
=0.740710133215161\ldots D-o(D)
}
\tag{P1625.4}
```

must hold.

On the rhombic branch,

```math
M_R={\sigma_R\over8}
\left(4\sqrt{R_4}+{\sigma_R\over2}\right)
```

gives

```math
\boxed{
\liminf {M_R\over D^2}
\ge0.386984591857829\ldots .
}
\tag{P1625.5}
```

The post-endpoint scalar identity similarly gives

```math
\boxed{
\liminf\mu_D\ge1.785704210824532\ldots .
}
\tag{P1625.6}
```

The direct correlated endpoint/interface floor is

```math
\boxed{
\liminf {J\over D}
\ge2\rho+4s_2-\pi+0.00325
=2.149078840296357\ldots .
}
\tag{P1625.7}
```

---

## 2. Section-171 endpoint with `g=0.001625`

For

```math
t=\lim{q-k\over D},
\qquad
\delta=\lim{b-P_F\over D}\ge0,
```

audited Section 171 requires

```math
F_t(\delta)=
10t-5\pi-5\delta
+\left(81(\pi+\delta)^2\delta\right)^{1/3}
-{8\Delta_2\over9t/2-2\pi-2\delta}
\ge0.
\tag{P1625.8}
```

The atomic gain restricts the feasible detour interval to

```math
0\le\delta\le
{{9\over2}(t-C_{146})-g\over2}.
\tag{P1625.9}
```

Set

```math
g=0.001625,
\qquad
\varepsilon_{1625}=0.001628,
\qquad
t_{1625}=C_{146}+\varepsilon_{1625}.
\tag{P1625.10}
```

Then

```math
\boxed{
t_{1625}=1.8211415379794447\ldots
}
\tag{P1625.11}
```

and the right endpoint of (P1625.9) is exactly

```math
\boxed{\delta_{1625}=0.0028505.}
\tag{P1625.12}
```

The outward rational certificate

`research/verify_target_c_sp1625_global_propagation.py`

proves:

1. `F_t` is strictly increasing in `delta` throughout the feasible interval;
2. `F_{t1625}(delta1625)<0` with certified outward margin greater than `6e-5`;
3. `F_t(delta)` is strictly increasing in `t` on the same domain.

Therefore no Type-II limit can have `t<=t1625`, and

```math
\boxed{
\liminf {q-k\over D}
\ge C_{146}+0.001628
=1.8211415379794447\ldots .
}
\tag{P1625.13}
```

The unchanged endpoint equation has numerical root

```math
\varepsilon_*=0.0016282052646300867\ldots,
```

so the certified value retains approximately `2.05e-7` of offset slack. Further decimal tuning of Section 171 is again immaterial.

---

## 3. Chamber, rhombus-deficit, and residual consequences

Using

```math
{T-q/2\over D}\ge2s_2+0.001625-o(1),
```

`J=2T-P_F`, `P_F/D->pi`, and (P1625.13),

```math
\boxed{
\liminf {J\over D}
\ge j_{1625}
:=t_{1625}+2(2s_2+0.001625)-\pi
=2.492050111845481\ldots .
}
\tag{P1625.14}
```

Hence

```math
\boxed{
\liminf {\Sigma_{ch}\over D}
\ge2.492050111845481\ldots .
}
\tag{P1625.15}
```

The exact relation

```math
H={J\over2}+(q-k)-{P_F\over2}
```

gives

```math
\boxed{
\liminf {H\over D}
\ge1.496370267107289\ldots .
}
\tag{P1625.16}
```

Therefore

```math
\boxed{
\liminf {A_{ch}-a_0Z_{ch}\over D}
\ge0.647947332391309\ldots,
}
\tag{P1625.17}
```

and

```math
\boxed{
\liminf {\Delta_2D^2-R_4\over D}
\ge0.748185133553644\ldots .
}
\tag{P1625.18}
```

The corrected residual cap becomes

```math
\boxed{
\limsup {R_F+\Sigma_{ext}\over D}
\le {3\pi\over2}-t_{1625}
=2.891247442405245\ldots .
}
\tag{P1625.19}
```

The scalar chamber/residual ledgers still do not contradict one another.

---

## 4. Low-`t` topology budget at the stronger endpoint

The latest-main low-`t` network theorem uses

```math
C_0=2s_2+g
```

and

```math
R(t)={9t\over2}-2\pi-C_0.
```

At `g=0.001625` and `t=t1625`,

```math
\boxed{C_0=1.906250613727915\ldots}
\tag{P1625.20}
```

and, because `(9/2)C146-2pi=2s_2`,

```math
\boxed{R(t_{1625})=4.5(0.001628)-0.001625=0.005701.}
\tag{P1625.21}
```

Thus every survivor at the endpoint profile satisfies

```math
\boxed{
\delta\le0.0028505+o(1),
\qquad
\kappa={k\over D}\le0.011402+o(1).
}
\tag{P1625.22}
```

The loaded diameter graph consequently satisfies

```math
\boxed{
{h\over q}\ge0.993778046871087\ldots-o(1).
}
\tag{P1625.23}
```

In the caterpillar-forest branch,

```math
\boxed{
{q\over d_H}\ge159.7212364479\ldots-o(1).
}
\tag{P1625.24}
```

So the stronger endpoint still leaves a near-extremal Woodall graph, now with a slightly smaller total topology/rigidity defect budget.

---

## 5. Pentagon sea becomes still more concentrated

The low-`t` pentagon theorem gives

```math
{f\over D}
\ge {C_0\over2}-{t\over4}+{\kappa\over4}-o(1).
```

Dropping the favorable `kappa` term gives at `t=t1625`

```math
\boxed{
{f\over D}\ge0.497839922369096\ldots-o(1).
}
\tag{P1625.25}
```

The total excess degree above pentagons satisfies

```math
\boxed{
{Q-f\over D}\le0.0028505+o(1).
}
\tag{P1625.26}
```

Hence the actual pentagon count obeys

```math
\boxed{
{p_5\over D}\ge0.494989422369096\ldots-o(1).
}
\tag{P1625.27}
```

At most about `0.5726%` of exceptional faces can be nonpentagonal at this profile.

Using the closure-rank theorem and `s_Z<=k`,

```math
\boxed{
{\operatorname{rank}C_{P_5}\over D}
\ge2{p_5\over D}-{\kappa}
\ge0.978576844738192\ldots-o(1).
}
\tag{P1625.28}
```

The total number of bounded terminal occurrences lying on degree-at-least-six exceptional faces is at most

```math
\boxed{
{B_{\ge6}\over D}\le6{Q-f\over D}
\le0.017103+o(1).
}
\tag{P1625.29}
```

The number `N_5` of distinct complete stopped trains touching at least one pentagon satisfies

```math
\boxed{
{N_5\over D}\ge{5p_5\over2D}
\ge1.237473555922740\ldots-o(1).
}
\tag{P1625.30}
```

Thus the endpoint geometry is even closer to a pure pentagon defect network than under AG42/LA90.

---

## 6. Endpoint-network counts

Let `B=Q+4f` be the bounded-face terminal occurrence count. The same identities give

```math
\boxed{
2.489199611845481\ldots
\le {B\over D}
\le2.503452111845481\ldots
}
\tag{P1625.31}
```

up to `o(1)`.

Since `2T=b+B` and `b/D=pi+delta`,

```math
\boxed{
2.815396132717637\ldots
\le {T\over D}
\le2.822522382717637\ldots
}
\tag{P1625.32}
```

at the endpoint profile.

The independent outer-to-outer count remains linear:

```math
\boxed{
\liminf {L_{OO}\over D}
\ge3\pi-5t_{1625}
=0.319070270872156\ldots .
}
\tag{P1625.33}
```

Every one of these outer-to-outer cuts is crossed by actual diameter edges of both transverse signs, by the independently audited bracing theorem. This statement is structural only: the same diameter edge may cross many nested train cuts, so (P1625.33) cannot be converted into an edge count by naive summation.

---

## 7. Outer-tooth / long-side burden

The latest-main exact finite inequality

```math
N_2+2L_{>2}\ge x_B-2d_{out}
```

and the low-`t` topology bound give

```math
\liminf {N_2+2L_{>2}\over D}
\ge5\pi+2C_0-10t.
```

At `t=t1625`,

```math
\boxed{
\liminf {N_2+2L_{>2}\over D}
\ge1.309049115610349\ldots .
}
\tag{P1625.34}
```

Consequently

```math
\boxed{
\liminf {1\over D}\max\{N_2,L_{>2}\}
\ge0.436349705203450\ldots .
}
\tag{P1625.35}
```

The stronger train gain does not materially increase this particular dichotomy because its positive `2g` contribution is almost cancelled by the higher certified `t` endpoint. The value of SP1625 here is instead the tighter detour/topology budget and stronger pentagon concentration.

---

## 8. Current closure frontier

The surviving endpoint profile must realize all of the following simultaneously:

- a loaded diameter graph with edge/vertex ratio at least `0.993778-o(1)`;
- topology/rigidity defect `k<=0.011402D+o(D)`;
- at least `0.494989D-o(D)` actual pentagonal contact faces;
- pentagon closure rank at least `0.978577D-o(D)`;
- at least `1.23747D-o(D)` stopped trains touching pentagons;
- at least `0.31907D-o(D)` outer-to-outer train cuts, each two-sidedly diameter-braced;
- and at least `1.30905D-o(D)` units of combined two-edge-tooth / loaded-long-side burden.

These constraints are substantially more rigid than the scalar endpoint alone, but they still do not produce a contradiction. Two tempting shortcuts remain invalid:

1. near-disk perimeter does **not** force individual `O(1)` loaded-hull side lengths to be nearly equal; a convex near-circle can support a nonuniform collection of bounded chord lengths while retaining `per(F)=pi D+o(D)`;
2. two-sided bracing of every outer-to-outer train does **not** imply two fresh diameter edges per train, because nested train cuts may reuse the same diameter edges.

The next genuinely new theorem must control that reuse/cyclic order, or couple the near-extremal Woodall caterpillar/odd-cycle topology directly to the pentagon endpoint network and tooth/long-side burden.

**Disposition:** proof-only propagation. C-II and Level I remain open.
