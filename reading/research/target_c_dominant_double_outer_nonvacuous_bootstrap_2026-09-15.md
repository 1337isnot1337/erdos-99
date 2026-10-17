> Generated reading edition · [exact source](../../research/target_c_dominant_double_outer_nonvacuous_bootstrap_2026-09-15.md) · source SHA-256 `a9e1707a5a919762b945b3316d2e6ff1acc21162146e3d91f3ccf1c1bd19aa1e`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 20 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "c64f3cd81107c980f9c7a5467e1c4bf402a361ab", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_dominant_double_outer_nonvacuous_bootstrap_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "fb8bfc8682442b768711f13f9cc7fba9436d293520bcde357779101968a90440"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — nonvacuous dominant double-outer train bootstrap

**Date:** 2026-09-15  
**Status:** proof-only structural strengthening  
**Scope:** fully force-visible no-container/full-core Type-II branch with `t=(q-k)/D<=1.844`  
**Depends on:** hostile-audited `g=0.0071` matched train floor; hostile-audited two-bin dominant-orbit bound; hostile-audited shared endpoint retention and complement-rhombus incidence  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The first dominant double-outer bootstrap was stated only for `t<=1.843`, after the
low-`t` scalar floor had already advanced past `1.84323`; that range is vacuous for a
survivor.  This note reruns the bootstrap on the genuinely live interval

```math
1.84323\lesssim t\le1.844.
```

The result is still strong:

```math
\boxed{
P_{OO}^{dom}\ge0.29D-o(D),
}
\tag{DO.1}
```

where `P_OO^dom` is the retained pair weight of dominant-orbit complete stopped trains
whose two terminal incidences are both on the outer face.

Thus every survivor in the first `7.7e-4`-wide band above the current scalar floor
already contains a linear family of dominant-phase O--O cuts.  This is the structural
object needed for a cyclic-endpoint/crossing argument; it is not another decimal
improvement.

---

## 1. Variables and audited inequalities

Write

```math
t={q-k\over D},\qquad
\kappa={k\over D},\qquad
\delta={d_{out}\over D},
```

and

```math
U={9t\over2}-2\pi-2\delta-\kappa/2.
\tag{DO.2}
```

The hostile-audited branch-aware atomic theorem gives

```math
\boxed{U\ge C_{71}:=2\sqrt{\Delta_2}+0.0071,}
\qquad
\Delta_2={\pi\over2\sqrt3}.
\tag{DO.3}
```

Hence, on `t<=T:=1.844`,

```math
\delta\le\delta_{max}:=
{(9/2)T-2\pi-C_{71}\over2}
=0.0515445395\ldots .
\tag{DO.4}
```

Let

```math
m_2(U)={U+\sqrt{8\Delta_2-U^2}\over2},
\qquad r(U)=U-m_2(U).
\tag{DO.5}
```

The hostile-audited shared-retention stack supplies retained dominant outer-terminal
mass `z` and retained complement O--O pair mass `p` with

```math
\boxed{
z+p\ge
S(t,\delta,\kappa):=
\pi-U-{t+\kappa\over2}+m_2(U)-o(1).}
\tag{DO.6}
```

The dominant selected occurrences alone pay

```math
\boxed{\delta\ge F(z)-o(1),
\qquad F(z):=z-6\sin(z/6).}
\tag{DO.7}
```

The energy-restored complement-rhombus incidence theorem gives

```math
\boxed{
p\le
{\delta-F(z)+r(U)^2\over2(1-\delta)}+o(1).}
\tag{DO.8}
```

All three inputs have already been hostile-audited independently.

---

## 2. One bootstrap step

Assume a current lower bound

```math
z\ge z_0-o(1).
\tag{DO.9}
```

Then (DO.7) gives

```math
\delta\ge F(z_0)-o(1).
```

Since `t<=T`, `kappa>=0`, and `U` decreases with `delta`,

```math
\boxed{
U\le U_0(z_0):={9T\over2}-2\pi-2F(z_0)+o(1).}
\tag{DO.10}
```

On the present interval `m_2'(U)<0`, so `r(U)` is increasing.  Therefore

```math
r(U)\le r(U_0(z_0))+o(1).
\tag{DO.11}
```

Also `S` is minimized by taking `t=T`, `kappa=0`, and the smallest allowed detour
`delta=F(z_0)`: indeed

```math
\partial_\kappa S=-{m_2'(U)\over2}>0,
\qquad
\partial_\delta S=2(1-m_2'(U))>0.
```

Thus

```math
\boxed{
S\ge
S_0(z_0):=
\pi-U_0(z_0)-{T\over2}+m_2(U_0(z_0))-o(1).}
\tag{DO.12}
```

For the complement pair ceiling, use simultaneously

```math
\delta\le\delta_{max},
\qquad F(z)\ge F(z_0),
\qquad r(U)\le r(U_0(z_0)).
```

Equation (DO.8) yields

```math
\boxed{
p\le
P_0(z_0):=
{\delta_{max}-F(z_0)+r(U_0(z_0))^2
\over2(1-\delta_{max})}+o(1).}
\tag{DO.13}
```

Combining (DO.6), (DO.12), and (DO.13),

```math
\boxed{z\ge \mathcal B(z_0):=S_0(z_0)-P_0(z_0)-o(1).}
\tag{DO.14}
```

This is a monotone finite bootstrap, not a fixed-point assumption.

---

## 3. Exact rational bootstrap

The companion exact verifier proves the following five strict implications:

```math
\begin{aligned}
z\ge0
&\Longrightarrow z>2.0720-o(1),\\
z\ge2.0720
&\Longrightarrow z>2.1850-o(1),\\
z\ge2.1850
&\Longrightarrow z>2.2033-o(1),\\
z\ge2.2033
&\Longrightarrow z>2.2064-o(1),\\
z\ge2.2064
&\Longrightarrow z>2.2069-o(1).
\end{aligned}
\tag{DO.15}
```

The certificate uses exact `Fraction` arithmetic, Machin's identity for `pi`, outward
integer-square-root enclosures, and alternating Taylor bounds for `sin`.  No displayed
decimal is load-bearing.

Hence every survivor with `t<=1.844` satisfies

```math
\boxed{z\ge2.2069-o(1).}
\tag{DO.16}
```

---

## 4. Convert terminal mass into double-outer trains

Freeze shrinking phase windows around the dominant exact orbit.  For one dominant
complete stopped train `tau`, let `a_tau,b_tau in[0,1]` be the retained weights of its
two outer terminal occurrences, with a missing outer terminal assigned weight zero.
Then

```math
a_\tau+b_\tau
\le1+\min(a_\tau,b_\tau).
\tag{DO.17}
```

Let

```math
P_{OO}^{dom}:=
{1\over D}\sum_{\tau\ dom}\min(a_\tau,b_\tau).
```

If `M_dom D` is the number of dominant-window trains, summing (DO.17) gives

```math
z\le M_{dom}+P_{OO}^{dom}+o(1).
\tag{DO.18}
```

The dominant-window train mass is at most the total atomic train mass, hence at most
`C=(T-q/2)/D`, and therefore at most `U`.  By (DO.7) and `t<=T`,

```math
M_{dom}\le U
\le {9T\over2}-2\pi-2F(2.2069)+o(1).
\tag{DO.19}
```

The exact verifier bounds the right side by

```math
U<1.915963.
```

Together with (DO.16)--(DO.19),

```math
P_{OO}^{dom}
>2.2069-1.915963-o(1)
>0.2909-o(1).
```

Therefore

```math
\boxed{P_{OO}^{dom}>0.29-o(1).}
\tag{DO.20}
```

This proves (DO.1).

---

## 5. Frontier effect

For every currently live survivor with

```math
1.84323\lesssim t\le1.844,
```

the dominant exact three-phase orbit now has two simultaneous properties:

1. it carries more than `2.2069D` retained outer terminal mass; and
2. more than `0.29D` retained train weight consists of complete O--O trains.

Each of those O--O trains is subject to the audited Section-157 two-sided diameter
bracing theorem, and trains from different dominant phase classes obey the ordinary
Jordan endpoint-alternation crossing rule.

The next useful theorem should therefore distribute the `0.29D` pair weight among the
three phase classes and compare forced crossings from their cyclic outer endpoint
locations with the triangle-free center/leaf crossing structure of the dominant orbit.
That is a genuinely new closure interface.

C-II remains open.
