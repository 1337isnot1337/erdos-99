> Generated reading edition · [exact source](../../research/target_c_ec335_global_low_t_propagation_2026-09-14.md) · source SHA-256 `60f10d4b379daf0b32e0cef8cfefbc394a72fcdc52f3b0418e85128f95c011a2`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "b1cb105c5c83bc3b709543777feee7630caaa5b8", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_ec335_global_low_t_propagation_2026-09-14.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "cf6724a05a34d432f81e327478ce773b0f8e7c34739f06458a0847b86c539702"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Erdős Problem #99 — `eta_grid=0.00335` global and low-`t` propagation

**Date:** 2026-09-14  
**Target:** Target C-II, canonical full-core Type-II branch  
**Repository branch:** `research/c2-effective-sixpair-sol-20260914`  
**Claim class:** proof-only propagation of the effective six-pair theorem  
**LEVEL I STATUS:** `STILL OPEN`

The effective six-pair theorem gives

```math
\boxed{g=\eta_{grid}=0.00335.}
\tag{P335.1}
```

This note propagates that value through the existing correlated split, audited
Section 171, the low-`t` topology/pentagon package, and the outer-tooth/long-side
burden.  No new local geometric inequality is introduced here.

Put

```math
\Delta_2={\pi\over2\sqrt3},
\qquad
s_2=\sqrt{\Delta_2},
\qquad
C_{146}={4\over9}(\pi+s_2),
```

and let

```math
\rho=0.7390851332151606\ldots
```

be the positive solution of `rho=cos(rho)`.

---

## 1. Correlated stopped-train split

The exact correlated identity and (P335.1) give

```math
\boxed{
\liminf {\rho_{rec}+\sigma_R-q\over D}\ge0.00670.
}
\tag{P335.2}
```

Hence every survivor lies in at least one of

```math
\boxed{
{S\over D}
\ge{\rho\over2}+{g\over2}-o(1)
=0.371217566607580\ldots-o(1),
}
\tag{P335.3}
```

or

```math
\boxed{
{\sigma_R\over D}
\ge\rho+g-o(1)
=0.742435133215161\ldots-o(1).
}
\tag{P335.4}
```

On the rhombic branch the existing exact formula gives

```math
\boxed{
\liminf {M_R\over D^2}
\ge0.387965863252786\ldots .
}
\tag{P335.5}
```

The direct correlated interface floor is

```math
\boxed{
\liminf {J\over D}
\ge2\rho+4s_2-\pi+2g
=2.152528840296358\ldots .
}
\tag{P335.6}
```

---

## 2. Section-171 endpoint

Take

```math
\varepsilon_{335}=0.0019905,
\qquad
 t_{335}=C_{146}+\varepsilon_{335}.
\tag{P335.7}
```

Then

```math
\boxed{
 t_{335}=1.8215040379794445\ldots .
}
\tag{P335.8}
```

The atomic gain restricts the feasible detour endpoint to

```math
\delta_{335}
={{9\over2}\varepsilon_{335}-g\over2}
=0.002803625.
\tag{P335.9}
```

The outward rational certificate

`research/verify_target_c_ec335_global_propagation.py`

proves the same monotonicity conditions used by the earlier AG42/LA90/SB234
propagations and verifies strict endpoint negativity with margin greater than
`3e-5`.  Therefore

```math
\boxed{
\liminf {q-k\over D}
\ge C_{146}+0.0019905
=1.8215040379794445\ldots .
}
\tag{P335.10}
```

The numerical root of the unchanged endpoint equation is

```math
0.00199061785789379\ldots,
```

so the certified value retains about `1.18e-7` of offset slack.

---

## 3. Low-`t` topology budget

The low-`t` network theorem uses

```math
C_0=2s_2+g,
\qquad
R(t)={9t\over2}-2\pi-C_0.
```

At `t=t335`,

```math
\boxed{
C_0=1.907975613727915\ldots,
\qquad
R(t_{335})=0.00560725.
}
\tag{P335.11}
```

Hence every endpoint-profile survivor satisfies

```math
\boxed{
\delta\le0.002803625+o(1),
\qquad
\kappa={k\over D}\le0.0112145+o(1).
}
\tag{P335.12}
```

Since `h=q-d_H` and `d_H<=k`,

```math
\boxed{
{h\over q}
\ge0.993880948019239\ldots-o(1).
}
\tag{P335.13}
```

In the caterpillar-forest branch this forces average component size at least

```math
\boxed{
{q\over d_H}
\ge163.4240080\ldots-o(1).
}
\tag{P335.14}
```

Thus the loaded diameter graph is within about `0.612%` of maximal Woodall density.

---

## 4. Pentagon sea

The existing low-`t` face inequalities give, after dropping the favorable `kappa`
term,

```math
\boxed{
{f\over D}
\ge {C_0\over2}-{t_{335}\over4}-o(1)
=0.498611797369096\ldots-o(1).
}
\tag{P335.15}
```

The total excess degree above pentagons obeys

```math
\boxed{
{Q-f\over D}
\le0.002803625+o(1).
}
\tag{P335.16}
```

Therefore the actual pentagon count satisfies

```math
\boxed{
{p_5\over D}
\ge0.495808172369096\ldots-o(1).
}
\tag{P335.17}
```

The closure-rank theorem and `s_Z<=k` give

```math
\boxed{
{\operatorname{rank}C_{P_5}\over D}
\ge0.980401844738193\ldots-o(1).
}
\tag{P335.18}
```

Degree-at-least-six exceptional faces carry at most

```math
\boxed{
{B_{\ge6}\over D}
\le0.01682175+o(1)
}
\tag{P335.19}
```

terminal occurrences, while the number of distinct complete trains touching a
pentagon satisfies

```math
\boxed{
{N_5\over D}
\ge1.239520430922741\ldots-o(1).
}
\tag{P335.20}
```

The endpoint remains an almost pure pentagon defect network.

---

## 5. Outer-to-outer trains and physical boundary burden

The existing outer-to-outer train count becomes

```math
\boxed{
\liminf {L_{OO}\over D}
\ge3\pi-5t_{335}
=0.317257770872157\ldots .
}
\tag{P335.21}
```

Every such cut remains two-sidedly diameter-braced.  As before, one may not count
fresh diameter edges by summing over nested cuts.

The exact outer-tooth/long-side theorem gives

```math
\boxed{
\liminf {N_2+2L_{>2}\over D}
\ge5\pi+2C_0-10t_{335}
=1.308874115610351\ldots .
}
\tag{P335.22}
```

Consequently

```math
\boxed{
\liminf {1\over D}\max\{N_2,L_{>2}\}
\ge0.436291371870117\ldots .
}
\tag{P335.23}
```

The physical boundary split is therefore essentially stationary under further atomic
improvement: the larger `g` is largely offset by the larger certified `t`.  The
benefit of `g=0.00335` is instead the smaller topology defect and purer pentagon
network.

---

## 6. Current endpoint profile

A low-`t` survivor at the present proof-only frontier must simultaneously have

- `k<=0.0112145D+o(D)`;
- a loaded diameter graph with `h/q>=0.993881-o(1)`;
- at least `0.495808D-o(D)` actual pentagonal contact faces;
- pentagon closure rank at least `0.980402D-o(D)`;
- at least `1.23952D-o(D)` distinct pentagon-touching stopped trains;
- at least `0.317258D-o(D)` outer-to-outer train cuts; and
- at least `1.308874D-o(D)` units of combined two-edge-tooth / loaded-long-side burden.

The scalar system remains feasible.  The next useful move is geometric: current
`main` already turns the tooth alternative into many inward contacts.  Near-disk
locality can strengthen that theorem by preventing shallow teeth from reusing apices
or penetration edges.  The long-side alternative still needs a separate coupling to
the near-extremal Woodall diameter graph.

**Disposition:** proof-only propagation.  C-II and Level I remain open.
