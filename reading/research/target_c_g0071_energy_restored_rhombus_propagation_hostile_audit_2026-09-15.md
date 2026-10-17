> Generated reading edition · [exact source](../../research/target_c_g0071_energy_restored_rhombus_propagation_hostile_audit_2026-09-15.md) · source SHA-256 `fa85bdaae4e97c1910a42d7bfd9a9edda4755ebe07e546d6be7f45d56c4efcb1`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "2a255a3373c31833a68ce3f6eba4c73f90f31d67", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_g0071_energy_restored_rhombus_propagation_hostile_audit_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "53fd68b33dee322f4f8b0665cf6e4c8ccb7a75daea9cd94bae870c80832779f7"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — `g=0.0071` propagation through restored rhombus energy

**Date:** 2026-09-15  
**Reviewed:**
- `research/target_c_g0071_energy_restored_rhombus_propagation_2026-09-15.md`
- `research/verify_target_c_g0071_energy_restored_rhombus_propagation.py`
- hostile-audited branch-aware matched gap `g=0.0071` (`43f9692`)
- hostile-audited restored complement-rhombus energy stack (`d6c1443` and parents)

**Disposition:** **PASS at proof-only full-core Type-II scope.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The candidate replaces the old matched atomic input

```math
C_{50}=2\sqrt{\Delta_2}+0.0050
```

by the newly hostile-audited

```math
C_{71}=2\sqrt{\Delta_2}+0.0071
```

inside the restored complement-rhombus incidence theorem.  It claims the safe floor

```math
\boxed{(q-k)/D\ge1.84323-o(1)}.
```

The new scalar root is bracketed by

```math
1.84323535293446<t_*<1.84323535293447.
```

The propagation is valid.  The only nontrivial audit issue is that the new `t` interval
allows the Section-171 upper envelope `U` to reach about `2.0114`, slightly beyond the
`U<2.007` numerical range used in the earlier rhombus-incidence certificate.  That is
a certificate-range issue, not a theorem-domain boundary; the candidate supplies fresh
bounds on the enlarged interval.

---

## 1. The `g=0.0071` input is now independently audited

The branch-aware iterative-pruning theorem has received a hostile audit and an
independent exact Machin-formula certification of the `pi` enclosure used by its
Fraction verifier.  The audited conclusions include

```math
\liminf {T-q/2\over D}
\ge 2\sqrt{\Delta_2}+0.0071
```

and the matched strict-rhombus statement

```math
\liminf {T_R\over D}
\ge 2\sqrt{\Delta_2}+0.0071.
```

The candidate uses only the all-train inequality as the lower endpoint `C71`; the
rhombic counterpart is not silently reused.

**Verdict:** PASS.

---

## 2. The Section-171 network envelope is symbolic in `C0`

The existing low-`t` stack gives

```math
C_0\le C={T-q/2\over D}
\le U={9t\over2}-2\pi-2\delta-\kappa/2.
```

Therefore any valid stronger lower bound `C0` immediately implies

```math
2\delta+\kappa/2
\le {9t\over2}-2\pi-C_0.
```

No coefficient in this rearrangement was fitted to `0.0050`.  Replacing `C50` by
`C71` is exact.

**Verdict:** PASS.

---

## 3. The two-bin dominant-orbit theorem remains in scope above `U=2`

The previous hostile audit happened to work on an interval where `U<2`, but the actual
two-bin theorem is based on

```math
4\Delta_2\le M^2+(A-M)^2,
```

whose upper root is

```math
m_2(A)={A+\sqrt{8\Delta_2-A^2}\over2}.
```

Its required domain is

```math
A^2<8\Delta_2,
```

not `A<2`.  In the new candidate interval the exact certificate gives

```math
U<2.012,
```

while

```math
8\Delta_2>7.25>2.012^2.
```

Thus the square root and upper-root branch remain valid with large room.

Also `A>=2sqrt(Delta2)` physically, and on that interval

```math
m_2'(A)<0.
```

Hence

```math
A\le C\le U
\quad\Longrightarrow\quad
M\ge m_2(A)\ge m_2(C)\ge m_2(U),
```

and

```math
C-m_2(C)\le U-m_2(U).
```

The complement-train ceiling used by the retained-mass theorem therefore keeps the
correct direction.

**Verdict:** PASS.

---

## 4. Shared retention and rhombus incidence do not depend on the old gap value

The hostile-audited shared-retention theorem requires only an upper bound on the number
of complete trains outside the dominant orbit.  The two-bin replacement supplies the
valid ceiling

```math
N_c\le U+(t+\kappa)/2-m_2(U).
```

Thus

```math
z+p\ge
\pi-(t+\kappa)/2-[U-m_2(U)]-o(1).
```

The complement train-length/rhombus-incidence theorem then gives

```math
p(1-\delta)-e_c/2\le [U-m_2(U)]^2/2+o(1).
```

Neither finite geometric statement contains the constant `0.0050`; it entered only
through the allowed scalar range.  The dominant/complement energy disjointness likewise
remains exact, so

```math
e_c\le\delta-F(z)+o(1).
```

**Verdict:** PASS.

---

## 5. Elimination of `p` is monotone and introduces no new allocation assumption

Combining the preceding inequalities gives

```math
p\le
{\delta-F(z)+r(U)^2\over2(1-\delta)},
\qquad r(U)=U-m_2(U),
```

and therefore

```math
G(z):=
 z+{\delta-F(z)+r(U)^2\over2(1-\delta)}
\ge S.
```

On the new interval the certificate gives `delta<0.05`.  Since

```math
0\le F'(z)\le1-\sqrt3/2<0.134
```

for the relevant `0<=z<=pi`,

```math
G_z
=1-{F'(z)\over2(1-\delta)}
>0.929.
```

Thus the implicit threshold `Z_*` is unique and every survivor must obey

```math
\delta\ge F(Z_*).
```

No complement lower-energy term is required.  The elimination is the same one already
hostile-audited at `g=0.0050`.

**Verdict:** PASS.

---

## 6. `kappa=0` remains the weakest topology point

Write

```math
r'(U)=1-m_2'(U).
```

The enlarged-range certificate gives

```math
-0.062<m_2'(U)<0,
\qquad
1<r'(U)<1.062.
```

At fixed `t,delta`,

```math
U_\kappa=-1/2,
\qquad
S_\kappa=(r'-1)/2>0,
\qquad
G_U={rr'\over1-\delta}>0.
```

Implicit differentiation of `G(Z_*)=S` yields

```math
G_z Z_{*,\kappa}=S_\kappa+G_U/2>0.
```

Therefore `F(Z_*)-delta` increases with `kappa`, and the weakest point remains

```math
\boxed{\kappa=0.}
```

**Verdict:** PASS.

---

## 7. Maximal detour remains the weakest detour point on the enlarged interval

The certificate verifies

```math
U<2.012,
\quad
\delta<0.050,
\quad
r<0.111,
\quad
r'<1.062.
```

Consequently

```math
G_U={rr'\over1-\delta}<0.125,
\qquad
G_z>0.929.
```

At fixed `t,kappa`, `U_delta=-2` and `S_delta=2r'`.  The direct partial derivative of
`G` with respect to `delta` at fixed `z,U` is positive, so dropping it gives the safe
upper bound

```math
Z_{*,\delta}
< {2(1.062)+2(0.125)\over0.929}
<2.56.
```

Thus

```math
{d\over d\delta}[F(Z_*)-\delta]
<2.56(0.134)-1
<-0.65.
```

The contradiction margin strictly decreases with detour.  Combined with the topology
result, its weakest point is

```math
\boxed{
\kappa=0,
\qquad
\delta=\frac12\left({9t\over2}-2\pi-C_{71}\right),
\qquad
U=C_{71}.
}
```

**Verdict:** PASS.

---

## 8. Boundary certificate

At the boundary put

```math
M_0=m_2(C_{71}),
\qquad
r_0=C_{71}-M_0,
```

```math
\delta_0(t)
={1\over2}\left({9t\over2}-2\pi-C_{71}\right),
\qquad
S_0(t)=\pi-t/2-r_0.
```

The unique `Z_0` solves

```math
Z_0+{\delta_0-F(Z_0)+r_0^2\over2(1-\delta_0)}=S_0.
```

The independent Decimal verifier obtains

```math
H_0(1.84323)=1.2672491576\times10^{-5}>0,
```

```math
H_0(1.84324)=-1.1001428615\times10^{-5}<0,
```

and

```math
H_0(1.84323535293446)>0,
\qquad
H_0(1.84323535293447)<0.
```

The same verifier certifies all enlarged-range derivative bounds used above.

**Verdict:** PASS.

---

## 9. Scope

This is a quantitative composition of proof-only results.  It does not prove an exact
unit equilateral triangle, construct a diameter-decreasing competitor, or promote the
canonical theorem state.  Its value is that the newly audited phase information is
actually propagated to the strongest current outer-train obstruction instead of being
left as an isolated train-measure constant.

**Final verdict:** PASS at proof-only full-core Type-II scope.  The safe low-`t` floor is

```math
\boxed{1.84323}.
```

C-II and Level I remain open.
