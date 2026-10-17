> Generated reading edition · [exact source](../../research/target_c_0021_physical_contact_normal_form_2026-09-15.md) · source SHA-256 `59f5cd49150d805459b1fc5045cf18fbe2142ca9c0c65acf03a08b438162cab5`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 10 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "2003c384700503ce96fafbf53cbf8aff470aaef7", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_0021_physical_contact_normal_form_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "87a14879b2feefeedefecbdad18a0f6d71374dbd4d66881e7bdde4f064773660"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — audited `0.0021` physical-contact normal form

**Date:** 2026-09-15  
**Status:** proof-only numerical propagation; theorem-state authority unchanged  
**Scope:** canonical full-core Type-II branch at the audited minimax atomic-gap checkpoint `g=0.0021`  
**LEVEL I STATUS:** `STILL OPEN`

Several physical-contact reductions were proved after the original AG42 `0.00042`
checkpoint, but their displayed low-`t` constants still use that older value.  This
note propagates the independently audited minimax atomic gap

```math
\boxed{g=0.0021}
```

through the already-proved low-`t` scalar squeeze, the outer tooth/long-side split,
the global-turn shallow-tooth penetration theorem, and bridge-suppressed long-side
straight-event theorem.  No geometric lemma is changed.

Put

```math
\Delta_2={\pi\over2\sqrt3},\qquad
s=\sqrt{\Delta_2},\qquad
C_0=2s+0.0021.
\tag{PN.1}
```

The current audited proof-only low-`t` floor is

```math
\boxed{
t_{21}={4\over9}(\pi+s)+0.0017279
=1.8212414379794447\ldots .
}
\tag{PN.2}
```

For

```math
R(t):={9t\over2}-2\pi-C_0,
\tag{PN.3}
```

the §171 detour/topology squeeze gives

```math
2\delta+{\kappa\over2}\le R(t),
\qquad
\delta={b-P_F\over D},\quad
\kappa={k\over D}.
\tag{PN.4}
```

At `t=t_21`,

```math
\boxed{R(t_{21})=0.00567555,\qquad
\delta\le0.002837775.}
\tag{PN.5}
```

The physical outer-route theorem then reduces every low-`t` survivor to one of two
actual contact structures:

1. a shallow-tooth branch carrying many strongly inward unit contacts; or
2. a rounded long-side branch carrying many strongly transverse unit contacts.

At the audited `0.0021` checkpoint the corresponding safe densities are

```math
\boxed{
{E_{tooth}\over D}
\ge0.2128458578100580890\ldots-o(1),
}
\tag{PN.6}
```

and

```math
\boxed{
{E_{perp}\over D}
\ge0.0391132714948321095\ldots-o(1).
}
\tag{PN.7}
```

Every tooth-branch edge in (PN.6) has inward component greater than

```math
\boxed{
Y_{4/15}
={13\sqrt3-2\sqrt{14}\over30}
=0.5011115241615840681\ldots,
}
\tag{PN.8}
```

while every long-side edge in (PN.7) has transverse component greater than `1/2`
relative to its corresponding long-side tangent direction.

Thus a current-floor survivor cannot hide the low-`t` boundary defect in anonymous
perimeter currency: it carries a linear family of physical contact edges with a
uniform directional component bounded away from zero.

## 1. Updated scalar branch floor

The existing tooth/long-side theorem gives, after eliminating the same nonnegative
correction terms used in the audited low-`t` squeeze, a branch quantity with normalized
floor

```math
\boxed{
F(t):={\pi-t-2R(t)\over3}.
}
\tag{PN.9}
```

At `t=t_21`,

```math
\boxed{
F(t_{21})
=0.4363333718701161781\ldots .
}
\tag{PN.10}
```

The theorem says that the current physical endpoint enters either the two-edge tooth
branch at scale at least `F(t)D-o(D)` or the rounded long-side branch at the same
scalar scale, with the separate geometric conversions recalled below.

## 2. Tooth branch with global-turn apex control

The global-turn shallow-tooth theorem applies to every threshold `eta` satisfying

```math
\alpha_\eta:=\arccos(1-\eta/2)<\pi/6.
```

It gives

```math
\boxed{
E_{tooth}(\eta)
\ge {1\over2}
\left(N_2-{d_{out}\over\eta}-2\right).
}
\tag{PN.11}
```

Use the exact threshold

```math
\boxed{\eta={4\over15}.}
\tag{PN.12}
```

Then

```math
1-{\eta\over2}={13\over15}>{\sqrt3\over2},
```

so `alpha_eta<pi/6`.  On the tooth branch,

```math
{N_2\over D}\ge F(t_{21})-o(1),
```

and (PN.5) gives

```math
{d_{out}\over D}\le0.002837775+o(1).
```

Therefore

```math
\begin{aligned}
\liminf {E_{tooth}(4/15)\over D}
&\ge {1\over2}
\left(
F(t_{21})-{0.002837775\over4/15}
\right)\\
&=0.2128458578100580890\ldots .
\end{aligned}
\tag{PN.13}
```

This proves (PN.6).

The same global-turn theorem gives the uniform inward component

```math
Y_{4/15}
=\sin\left({\pi\over3}-\arccos{13\over15}\right)
={13\sqrt3-2\sqrt{14}\over30},
```

which proves (PN.8).

## 3. Rounded long-side branch after bridge suppression

The bridge-suppressed long-side theorem gives for any
`beta in(0,pi/3)`

```math
\boxed{
\liminf {10E_\perp(\beta)\over D}
\ge
\liminf {L_{>2}\over D}
-\delta\left(1+{2\over1-\cos\beta}\right).
}
\tag{PN.14}
```

The loaded degree-two internal-route escape has already been removed: every such
loaded repeated occurrence is an outer-bridge event, and bridge-subtracted
isoperimetry pays its total population from the same detour `delta`.

On the rounded long-side branch,

```math
{L_{>2}\over D}\ge F(t_{21})-o(1).
```

Choose

```math
\boxed{\beta={\pi\over6}.}
\tag{PN.15}
```

Then

```math
1-\cos\beta=1-{\sqrt3\over2},
\qquad
\sin(\pi/3-\beta)={1\over2}.
```

Using (PN.5) in (PN.14),

```math
\begin{aligned}
\liminf {E_\perp(\pi/6)\over D}
&\ge {1\over10}
\left[
F(t_{21})
-0.002837775
\left(1+{2\over1-\sqrt3/2}\right)
\right]\\
&=0.0391132714948321095\ldots .
\end{aligned}
\tag{PN.16}
```

This proves (PN.7).  Every selected edge has absolute transverse component strictly
larger than `1/2` relative to its long-side tangent direction.

## 4. Current proof-only physical normal form

At the audited `g=0.0021` checkpoint, every low-`t` full-core Type-II survivor at the
current scalar floor satisfies at least one of

```text
TOOTH BRANCH
  >= 0.2128458578 D-o(D) distinct physical unit contacts,
  each pointing inward with component > 0.5011115241;

ROUNDED LONG-SIDE BRANCH
  >= 0.03911327149 D-o(D) distinct physical unit contacts,
  each with transverse component > 1/2 relative to its carrier side.
```

This normal form is independent of the small-`R_F` pentagon-reflection endpoint.  In
particular it remains available before splitting on the true force-hull residual.

The constants are not a C-II closure.  The new frontier is to charge these directional
physical contacts to the stopped-train phase/interface network or to a source-level
boundary deformation.  Counting them alone is insufficient; neither theorem supplies
a KKT coefficient floor.

## 5. Exact arithmetic certificate

The displayed values come from the symbolic formulas

```math
\begin{aligned}
C_0&=2\sqrt{\Delta_2}+0.0021,\\
t_{21}&={4\over9}(\pi+\sqrt{\Delta_2})+0.0017279,\\
R&={9t_{21}\over2}-2\pi-C_0,\\
\delta_{max}&={R\over2},\\
F&={\pi-t_{21}-2R\over3},\\
E_{tooth}/D&\ge {1\over2}\left(F-{\delta_{max}\over4/15}\right),\\
E_\perp/D&\ge {1\over10}
\left[F-\delta_{max}
\left(1+{2\over1-\sqrt3/2}\right)\right].
\end{aligned}
\tag{PN.17}
```

A companion verifier should use high-precision `Decimal` arithmetic; no floating-point
value is a proof premise.

## 6. Scope audit

- No new geometric lemma is introduced here; this is a propagation/composition note.
- The `0.0021` atomic gap is the audited minimax checkpoint, not the newer provisional
  `0.002123` value.
- The global-turn shallow-tooth theorem supplies the finite factor `1/2` and the
  `eta=4/15` admissibility.
- The long-side theorem already includes bridge suppression of loaded degree-two
  internal-route events.
- All counted objects are actual unit-contact edges in the source.
- Contact-isolated source points remain retained in the full source.
- No KKT multiplier lower bound is assumed.
- No exact unit equilateral triangle or strict same-cardinality sub-`D` competitor is
  produced.

**Disposition:** proof-only current-checkpoint normal form.  C-II and Level I remain open.
