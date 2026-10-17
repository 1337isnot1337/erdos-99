> Generated reading edition · [exact source](../../research/target_c_m23_endpoint_structural_propagation_2026-09-14.md) · source SHA-256 `bb1eb5439539790b599d8c90a15f496b5abddc18f7dc276380ca700fee6244f2`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 23 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "77f67fac39451521e40b6aa1d8a52f2d778451ce", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_m23_endpoint_structural_propagation_2026-09-14.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "542911a5e77114a813df4959b3f99a9d63abba7a7c92e60dbaa6eb8af7a8e9a8"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Erdős Problem #99 — M23 endpoint propagation into the current structural gates

**Date:** 2026-09-14  
**Target:** Target C-II canonical full-core Type-II branch  
**Branch:** `research/c2-closure-sol-20260914-r7`  
**Claim class:** proof-only algebraic propagation of the certified `g=0.002123` minimax phase-star theorem  
**External input:** none

## LEVEL I STATUS

`STILL OPEN`

The certified minimax phase-star theorem gives the current strongest proof-only atomic gain

```math
 g=0.002123,
 \qquad
 C_g:=2\sqrt{\Delta_2}+g,
 \qquad
 \Delta_2={\pi\over2\sqrt3},
```

and the safe Section-171 floor

```math
\boxed{
 t:={q-k\over D}
 \ge t_{23}:={4\over9}\left(\pi+\sqrt{\Delta_2}\right)+0.0017327
 =1.82124623797944\ldots .
}
\tag{M23P.1}
```

Several active structural notes still display constants inherited from `g=0.00042`, `0.0009`, or `0.0021`. Their geometric proofs are parameter-free once `g` and the Section-171 endpoint are supplied. This note propagates M23 through those exact ledgers.

Put

```math
 s:=\sqrt{\Delta_2}=0.952312806863957\ldots,
```

and define the endpoint detour/topology budget

```math
\boxed{
 A_{23}:={9t_{23}\over4}-\pi-{C_g\over2}=0.002837075.
}
\tag{M23P.2}
```

Equivalently, every endpoint limit satisfies

```math
2\delta+{\kappa\over2}\le 2A_{23}=0.00567415,
\qquad
\delta={b-P_F\over D},\quad \kappa={k\over D}.
\tag{M23P.3}
```

---

## 1. Pentagon sea and flat-center population

The low-`t` pentagon ledger gives, after dropping nonnegative `delta,kappa` bonuses,

```math
\boxed{
{p_5\over D}
\ge
P_{23}-o(1),
\qquad
P_{23}:=\pi+C_g-{5t_{23}\over2}
=0.495225672369096\ldots .
}
\tag{M23P.4}
```

On the true small-residual branch `R_F=o(D)`, trapezoid stability plus the flat-center injectivity theorem therefore gives the same lower bound for the number `V_flat` of **distinct actual flat centers**:

```math
\boxed{
{V_{flat}\over D}
\ge0.495225672369096\ldots-o(1).
}
\tag{M23P.5}
```

This is the correct M23 replacement for the older `0.494416...` and `0.494493...` values.

---

## 2. Loaded flat centers cannot absorb the whole sea

A loaded flat center has contact degree exactly two and contributes two distinct singleton stopped trains incident with its pentagon and the outer face. Thus, if `L` is the loaded-flat-center population and `S` the total singleton-train population,

```math
2|L|\le S.
\tag{M23P.6}
```

The exact all-train ledger gives

```math
{T\over D}\le 5t-2\pi-2\delta+o(1),
```

while the M23 rhombic-only transfer gives

```math
\boxed{
{T_R\over D}\ge2s+g-o(1).
}
\tag{M23P.7}
```

Therefore

```math
\limsup {S\over D}
\le5t-2\pi-2\delta-2s-g.
\tag{M23P.8}
```

At the safe endpoint, and conservatively dropping the positive `delta` improvement,

```math
\boxed{
\limsup {|L|\over D}
\le0.458148634494861\ldots .
}
\tag{M23P.9}
```

Subtracting from (M23P.5) gives an **unconditional unloaded flat-center floor on the small-residual branch**:

```math
\boxed{
\liminf {|U_3|+|U_4|\over D}
\ge U_{23}:=0.0370770378742349\ldots .
}
\tag{M23P.10}
```

In exact symbolic form,

```math
\boxed{
U_{23}=2\pi+3s+{3g\over2}-5t_{23}.
}
\tag{M23P.11}
```

The coefficient remains positive throughout

```math
\boxed{
t<1.8286616455542917\ldots}
\tag{M23P.12}
```

before using either `delta` or `kappa` bonuses.

The inherited unloaded-center dichotomy therefore sharpens to at least one of

```math
\boxed{
{|H_4|\over D}
\ge {U_{23}\over9}-o(1)
=0.0041196708749150\ldots-o(1),
}
\tag{M23P.13}
```

where `H_4` is endpoint-disjoint and has aggregate hidden-contact excess `o(D)`, or

```math
\boxed{
{|E_3|\over D}
\ge {U_{23}\over4}-o(1)
=0.00926925946855875\ldots-o(1),
}
\tag{M23P.14}
```

where `E_3` is a distinct positive-contact family carrying total relative-interior KKT weight `o(D^2)`.

---

## 3. Updated outer/pentagon train fork

The outer/pentagon gate uses only the degree-excess estimate and the exact outer terminal ledger. With M23,

```math
A_g(t_{23})=A_{23}=0.002837075.
```

Hence

```math
\boxed{
W_{23}:=\pi-6A_{23}
=3.124570203589793\ldots .
}
\tag{M23P.15}
```

For `L_OO` outer-to-outer trains and `L_O5` outer-to-pentagon trains,

```math
\boxed{
2L_{OO}+L_{O5}
\ge(W_{23}-o(1))D.
}
\tag{M23P.16}
```

Thus

```math
\boxed{
\max\{L_{OO},L_{O5}\}
\ge1.041523401196598\ldots D-o(D).
}
\tag{M23P.17}
```

On `R_F=o(D)`, the leaf-localized version uses

```math
\boxed{
R_{23}:=2\pi-2t_{23}-5A_{23}
=2.626507456220697\ldots .
}
\tag{M23P.18}
```

If the outer-to-outer side of (M23P.17) fails, the exact same conflict extraction gives pairwise vertex-disjoint near-equilateral leaf teeth with one exact side on an outer-to-pentagon train at density

```math
\boxed{
{J_{leaf}\over D}
\ge
{R_{23}-{2W_{23}\over3}\over52}-o(1)
=0.0104511664197596\ldots-o(1).
}
\tag{M23P.19}
```

---

## 4. Boundary atoms and loaded-unit elimination

The exact boundary atom inequality is

```math
N_2+2e_{BB}\ge3q-b.
```

Under the M23 Section-171 budget its endpoint consequence is

```math
\boxed{
\max\{N_2,e_{BB}\}
\ge B_{23}D-o(D),
\qquad
B_{23}:={t_{23}\over4}+{C_g\over6}
=0.773102995116180\ldots .
}
\tag{M23P.20}
```

Thus the loaded-unit branch contains a matching of at least

```math
\boxed{0.386551497558090\ldots D-o(D)}
\tag{M23P.21}
```

actual unit hull contacts between loaded diameter endpoints.

The loaded-unit endpoint theorem eliminates `e_BB` into actual physical objects:

```math
N_2+J_{BI}+2s_B+2|E_{in}|
\ge3q-b-O(1).
```

If

```math
M_{phys}:=\max\{N_2,J_{BI},s_B,|E_{in}|\},
```

then the weighted left side is at most `6M_phys`, hence

```math
\boxed{
\liminf {M_{phys}\over D}
\ge {t_{23}\over8}+{C_g\over12}
=0.386551497558090\ldots .
}
\tag{M23P.22}
```

So the low-`t` boundary must contain at least `0.38655D` of one of four finite source objects:

```text
actual two-edge outer teeth,
loaded-to-unloaded attachments from single-unit endpoints,
loaded contact-degree slack,
strongly inward loaded-to-unloaded contacts.
```

---

## 5. Contact-curvature floor

The exact finite curvature identity remains

```math
s_B+n_3-n_5=4+q-2k.
```

Therefore `s_B+n_3>=4+q-2k`. At the M23 endpoint, the Section-171 constraint gives

```math
\boxed{
\liminf {1\over D}\max\{s_B,n_3\}
\ge0.904948968989722\ldots .
}
\tag{M23P.23}
```

This very large curvature population coexists with the pentagon sea and boundary-atom fork; it is not an independent scalar resource.

---

## 6. Current endpoint profile after M23

At proof-only scope, a small-residual survivor near the safe scalar floor must simultaneously realize:

```text
p_5 / D              >= 0.49522567,
V_flat / D           >= 0.49522567,
unloaded flat centers >= 0.03707704,

max(L_OO,L_O5) / D   >= 1.04152340,

max(N2,e_BB) / D     >= 0.77310300,
max(N2,J_BI,s_B,E_in)/D >= 0.38655150,

max(s_B,n_3) / D     >= 0.90494897.
```

These numbers are not separate costs that may simply be added. Their value is that every remaining escape is now represented by a large **actual source object** or a train family. The high-value closure targets are therefore compatibility theorems, not further scalar optimization:

1. order/rank restrictions on the `>1.04D` outer-ending train system versus the near-extremal diameter thrackle;
2. simultaneous activation or finite-motion control of the unloaded flat-center families; or
3. a global incidence theorem coupling the `~0.495D` pentagon sea to the boundary-atom/curvature populations.

**Disposition:** proof-only M23 propagation. C-II and Level I remain open.
