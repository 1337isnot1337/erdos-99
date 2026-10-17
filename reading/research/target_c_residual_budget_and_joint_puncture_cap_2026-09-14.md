> Generated reading edition · [exact source](../../research/target_c_residual_budget_and_joint_puncture_cap_2026-09-14.md) · source SHA-256 `1f5ec6a5ab3209a89d0968b331b09e58f3b14aea0cdc0c4c80ebbf0f5ff24de5`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "50b8d8e819d768bc26ebb7a68bc12eca5927d487", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_residual_budget_and_joint_puncture_cap_2026-09-14.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "a8139c878f5c77b23978513a203c72439f049b00cf57c08a020107045e6af3da"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Erdős Problem #99 — residual budget cap and joint-puncture coupling

**Date:** 2026-09-14
**Repository base:** `ac0bc77f`
**Target:** Target C-II canonical full-core Type-II branch
**Claim class:** proof-only finite reduction plus asymptotic coefficient
**External literature:** no new import

## LEVEL I STATUS

`STILL OPEN`

The raw chamber Oler slack contains the mandatory interface boundary `J`.  After that
baseline is removed, the pre-existing force-hull residual is

```math
R_F={A_F\over a_0}+{P_F\over2}+1-N_F-{E_4\over a_0}\ge0,
\qquad a_0={\sqrt3\over2}.
```

The exterior-cap gluing ledger gives

```math
R_F+\Sigma_{ext}=\Omega_K+L_{cap},
\tag{RB.1}
```

where

```math
\Omega_K:=\Sigma_K-{E_4\over a_0},
\quad
L_{cap}:=P_F-P_{com}-r\ge0.
```

This note supplies an explicit source-level upper bound for the right side and then
composes it with the Section-124 joint puncture theorem.

## 1. The cap chord excess is bounded by the force-hull side excess

The noncommon force-hull sides are a subset of the `q` sides of the convex force hull.
If their lengths are `ell_i`, then Section 77 gives one nondegenerate exterior cap per
such side and

```math
L_{cap}=\sum_{i\in noncommon}(\ell_i-1).
```

Every force-hull side joins distinct source points, hence every side length is at least
one. Therefore

```math
\boxed{
0\le L_{cap}\le P_F-q.
}
\tag{RB.2}
```

No contact-edge assumption is used for the closing chords.

## 2. Global minimality caps the punctured full-source slack

Put

```math
\delta_K:={\pi D^2\over4}-A_K\ge0.
```

For a global minimizer, the strict triangular-lattice comparison used in canonical
Section 68 gives

```math
a_0(n-1)>{\pi D^2\over4}.
```

Hence

```math
\begin{aligned}
\Sigma_K
&={A_K\over a_0}+{P_K\over2}+1-n\\
&<{P_K\over2}-{\delta_K\over a_0}.
\end{aligned}
```

Subtract `E_4/a_0`:

```math
\boxed{
\Omega_K
<{P_K\over2}-{\delta_K+E_4\over a_0}.
}
\tag{RB.3}
```

Combining (RB.1)--(RB.3) gives the finite residual-budget cap

```math
\boxed{
R_F+\Sigma_{ext}
<{P_K\over2}+P_F-q-{\delta_K+E_4\over a_0}.
}
\tag{RB.4}
```

In particular, after dropping the final nonnegative subtraction,

```math
R_F+\Sigma_{ext}<{P_K\over2}+P_F-q.
\tag{RB.5}
```

## 3. Explicit Type-II coefficient

Cauchy's perimeter-diameter inequality gives

```math
P_K\le\pi D,\qquad P_F\le\pi D.
```

The current `q-k` bootstrap gives

```math
{q-k\over D}\ge t_{42}-o(1),
\qquad
t_{42}=1.820888637979444\ldots,
```

and `k>=0`, so `q/D>=t_42-o(1)`. Therefore (RB.5) yields

```math
\boxed{
\limsup {R_F+\Sigma_{ext}\over D}
\le {3\pi\over2}-t_{42}
=2.891500342405245\ldots .
}
\tag{RB.6}
```

This is an actual upper bound on the corrected packing residual.  It should not be
confused with the raw chamber slack, whose mandatory interface baseline is already
`2.489387...D`.

## 4. Loaded-incident rhombus excess is boundary-order

Let `E_4^0` be the strict-rhombus area excess from rhombi whose four vertices are
unloaded, as in Section 124, and put

```math
E_4^L:=E_4-E_4^0.
```

Every rhombus counted by `E_4^L` has at least one loaded force-hull vertex.  Canonical
C35 gives contact degree at most three at every loaded vertex.  A loaded vertex is on
the outer face of the positive-contact embedding, so at least one of its incident face
sectors is the outer face.  It is therefore incident to at most two bounded faces, and
hence at most two strict rhombi.  Summing loaded-vertex incidences gives

```math
\#\{\text{loaded-incident strict rhombi}\}\le2q.
\tag{RB.7}
```

A unit rhombus has area at most one, while its triangular-lattice baseline is `a_0`.
Consequently

```math
\boxed{
0\le E_4^L\le2q(1-a_0).
}
\tag{RB.8}
```

Using `q<=P_F<=pi D`,

```math
\boxed{
{E_4^L\over a_0D}
\le2\pi\left({1\over a_0}-1\right)
=0.972012149757286\ldots .
}
\tag{RB.9}
```

The coefficient is coarse; the important point is that the omitted loaded-incident
part in Section 124 is provably only boundary-order.

## 5. Joint puncture now shares the corrected residual budget

Section 124 proves

```math
E_4^0+\Omega_{tooth}-a_0H_{chord}
\le \mathscr O_A,
\qquad
\mathscr O_A=a_0\Sigma_K.
\tag{RB.10}
```

Since

```math
a_0\Sigma_K=a_0\Omega_K+E_4,
```

(RB.10) is equivalent to

```math
{\Omega_{tooth}\over a_0}-H_{chord}
\le\Omega_K+{E_4^L\over a_0}.
\tag{RB.11}
```

Use (RB.1) to eliminate `Omega_K`:

```math
\boxed{
{\Omega_{tooth}\over a_0}-H_{chord}+L_{cap}
\le R_F+\Sigma_{ext}+{E_4^L\over a_0}.
}
\tag{RB.12}
```

Thus the tooth Oler remainder, exterior-cap residual, force-hull residual, cap chord
excess, and loaded-rhombus area excess are not independent boundary-order currencies.
They lie in one shared full-source budget.

Combining the coarse coefficients (RB.6) and (RB.9) gives

```math
\limsup {1\over D}
\left({\Omega_{tooth}\over a_0}-H_{chord}+L_{cap}\right)
\le3.863512492162531\ldots .
\tag{RB.13}
```

This last number is not close to contradiction and is recorded only to make the scale
explicit.  The finite inequality (RB.12) is the useful statement.

## 6. What remains

The corrected residual route is now sharply separated from the mandatory interface
ledger:

```text
raw chamber layer:
    Sigma_ch = J + a + L_add + R_F,
    J/D >= 2.4893872118... - o(1);

true residual layer:
    R_F + Sigma_ext
      < P_K/2 + P_F - q - (delta_K+E_4)/a0;

joint puncture layer:
    Omega_tooth/a0 - H_chord + L_cap
      <= R_F + Sigma_ext + E_4^L/a0.
```

A closure through this route now needs geometry that forces a positive fraction of the
left side of (RB.12) while simultaneously shrinking the right side.  Pure local Oler
strictness cannot do this: the explicit pentagon regression shows zero uniform local
gap.

**Disposition:** proof-only residual-budget theorem. C-II remains open.
