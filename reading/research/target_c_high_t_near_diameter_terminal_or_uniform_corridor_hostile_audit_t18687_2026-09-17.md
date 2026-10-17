> Generated reading edition · [exact source](../../research/target_c_high_t_near_diameter_terminal_or_uniform_corridor_hostile_audit_t18687_2026-09-17.md) · source SHA-256 `25c1db422dcceb4c9fc75efbb8c1c31f69a915a1b77c47b227da9e6612ae4d89`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 1 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "76fd862e48c8d38ac5d2a589045aac2983f9b26e", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_high_t_near_diameter_terminal_or_uniform_corridor_hostile_audit_t18687_2026-09-17.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "26a76c331b0e9b9faf3b26272ae3f553127ef400405c364d0ea2567ee2ff2c34"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — near-diametrical terminal piece or uniform fixed-aperture corridor

**Date:** 2026-09-17  
**Reviewed:** `research/target_c_high_t_near_diameter_terminal_or_uniform_corridor_t18687_2026-09-17.md`  
**Certificate:** `research/verify_target_c_high_t_near_diameter_terminal_or_uniform_corridor_t18687.py`  
**Verdict:** **PASS at proof-only high-`t` scope.**  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The candidate sharpens the paired no-TB1 branch to an unusually clean alternative:

- one projectively narrow TT pair forces the far terminal piece to be asymptotically almost diametrical; or
- every paired center, regardless of destination type, has the full parent aperture and the fixed-aperture vanishing-mass dense-grid corridor exists on an unbounded consecutive physical block.

The argument survives hostile review. The two points that require care are the ordinary/projective angle lift at a TT pair and the use of the construction-level `o(D)` physical-hole statement. Both are valid. A further uniform central-crossing localization corollary is recorded in Section 7 below and has been added to the regression certificate.

---

## 1. Projectively narrow TT pairs must use the near-antipodal ordinary lift

At one exact-force center let the two consistently oriented force directions in the common switching semicircle have ordinary separation

```math
\Delta\in(0,\pi).
```

Their projective gap is

```math
\eta=\min\{\Delta,\pi-\Delta\}.
```

The host transverse-margin theorem gives

```math
\Delta\ge2\gamma_H-o(1),
\qquad
\gamma_H=\arcsin c_H,
\qquad
c_H=0.453819885927\ldots .
```

Since

```math
\nu={113\over10{,}000{,}000}=1.13\times10^{-5}
\ll2\gamma_H,
```

any TT pair with `eta<nu` cannot satisfy `Delta=eta` for sufficiently large sources. Hence necessarily

```math
\boxed{\Delta=\pi-\eta>\pi-\nu.}
```

There is no third ordinary lift inside the fixed open semicircle.

**Verdict:** PASS.

---

## 2. The terminal support-normal conclusion has the correct orientation

Orient each diameter from its hubward partner `y` to its birth endpoint `x`:

```math
d={x-y\over D}.
```

For an actual diameter chord, the source lies between the two support lines perpendicular to `d`. Thus `+d` is an outward support normal at `x`, while `-d` is an outward support normal at `y`.

At a TT center both partner endpoints lie in `T_m`, so the two terminal outward normals are exactly

```math
-d^A,\qquad-d^B.
```

Their ordinary angular separation is the same `Delta` as that of `d^A,d^B`. Monotone support-normal order on the convex boundary therefore gives

```math
\boxed{
\operatorname{normalspan}(T_m)\ge\Delta>\pi-\nu.
}
```

No Type-II near-circle approximation is needed for this support-normal statement.

**Verdict:** PASS.

---

## 3. Midpoint localization gives the near-diametrical terminal chord

Let `m^A,m^B` be the diameter midpoints. The full-source theorem gives

```math
|m^A-o|,|m^B-o|\le L_D,
\qquad
L_D=O(D^{3/4})=o(D).
```

Since

```math
y^\sigma=m^\sigma-{D\over2}d^\sigma,
```

we have

```math
|y^A-y^B|
\ge{D\over2}|d^A-d^B|-2L_D
=D\sin{\Delta\over2}-2L_D.
```

For the near-antipodal lift `Delta=pi-eta`,

```math
\sin{\Delta\over2}=\cos{\eta\over2}>\cos{\nu\over2}.
```

Therefore

```math
\boxed{
\operatorname{diam}(T_m\cap S)
\ge
\bigl(\cos(\nu/2)-o(1)\bigr)D.
}
```

The coefficient is

```math
\cos(\nu/2)=0.9999999999840388\ldots .
```

The theorem correctly keeps the `o(D)` midpoint error. The displayed decimal is asymptotic and must not be interpreted as a finite-`D` estimate.

**Verdict:** PASS.

---

## 4. The central-angle statement follows uniformly

At a diameter partner endpoint,

```math
y-o=-{D\over2}d+O(L_D).
```

Since `L_D/D->0`, the radial direction from `o` to `y` differs uniformly by `o(1)` from `-d`. Hence the two TT terminal radial directions have separation

```math
\Delta-o(1)>\pi-\nu-o(1).
```

Thus

```math
\boxed{
\operatorname{angdiam}_o(T_m\cap S)
\ge\pi-\nu-o(1).
}
```

**Verdict:** PASS.

---

## 5. The alternative really gives aperture on the entire paired population

If the near-diametrical branch does not occur eventually, then no TT center has projective gap below `nu`; hence every TT center has gap at least `nu`.

The previously proved full-parent theorem independently gives, at every non-TT center,

```math
\eta_s\ge N\delta_D-o(1)\ge\nu-o(1).
```

Therefore

```math
\boxed{
\eta_s\ge\nu-o(1)
}
```

holds uniformly on the complete paired population. No `TT/mixed/OO` density split is left.

For a sequence on which narrow TT cells occur infinitely often, pass to that subsequence and obtain the terminal branch. Otherwise, on a tail no such TT cell exists and the uniform-aperture branch applies. This is the correct subsequential interpretation of the exhaustive alternative.

**Verdict:** PASS.

---

## 6. Physical block extraction legitimately uses the stronger hole statement

The uniform-corridor theorem invokes

```math
H_D=|I_D\setminus P_D|=o(D).
```

This is stronger than a mere lower bound on `|P_D|`. The preceding hostile audit verified it at construction level: `I_D` is a consecutive physical shore, and the near-full diagonal may be chosen as the **full survivor set** after explicit center-cost, separator-neighborhood, narrow-pair-neighborhood, shore-end, and finite bilateral deletions. The concrete diagonal schedule makes their total cardinality `o(D)`.

Consequently the paired population splits into only `H_D+1=o(D)` physical runs. Choosing a slow block length `m_D->infinity` with

```math
{m_D(H_D+1)\over D}\to0,
\qquad
{m_DT_D\over D}\to0
```

produces

```math
K_D\ge(\nu-o(1)){D\over m_D}\to\infty
```

pairwise interface-disjoint consecutive paired blocks.

The one-sided budget `sum B_i<=1` then selects one with total KKT mass at most `1/K_D->0`. Since every separator has safe fixed aperture `rho_*=nu/2`, the total compressed force coefficient mass tends to zero as well.

**Verdict:** PASS.

---

## 7. Additional corollary: every force-pair crossing lies in one fixed sublinear central ball

The candidate records the common central diamond but does not explicitly record the corresponding diagonal-intersection localization. The fixed aperture makes this uniform at no additional cost.

The wide-dipole central-crossing theorem states that a pair with projective gap at least a fixed `rho>0` has diagonal intersection `p` satisfying

```math
|p-o|<\left(1+{2\over\sin\rho}\right)L_D.
```

On the uniform corridor take the same safe fixed value

```math
\rho_*={\nu\over2}.
```

Then **every** force pair on the selected corridor satisfies

```math
\boxed{
|p_i-o|
< C_{\rm cross}L_D,
\qquad
C_{\rm cross}:=1+{2\over\sin(\nu/2)}
=353983.300886\ldots .
}
```

Since the coefficient is source-independent and `L_D=O(D^{3/4})`,

```math
\boxed{
\max_{i\in J_D}|p_i-o|=O(D^{3/4})=o(D).
}
```

This is stronger than the earlier shrinking-aperture corridor, where the coefficient in the crossing-point bound could diverge with the inverse pair gap. Here the entire unbounded force corridor has all tagged diagonal intersections in one common fixed-constant sublinear ball around the source circumcenter.

The regression certificate now checks

```math
C_{\rm cross}=353983.300886\ldots .
```

This does **not** yet locate where either diameter chord intersects the individual train rows. That remains the missing metric link.

**Verdict:** NEW VALID COROLLARY.

---

## 8. Dense-grid and coercivity inheritance are unaffected by destination type

Once a physical consecutive block of paired centers has been extracted, every separator is exact-antipodal. Exact phase therefore propagates across the entire block. The direct-sum argument gives the same full zero-sum cancellation-kernel coercivity floor

```math
\sqrt2c_H=0.64179823755\ldots .
```

The adjacent crossing-family drift is bounded by the low-complexity scale `T_D`, and `m_DT_D=o(D)`. Hence the running intersection retains `(0.6536-o(1))D` common columns. Exact co-phase lets one-row angular purification apply to every row simultaneously, and the existing train-step metric argument gives the common positive-density circumcenter flanks.

None of these steps distinguishes TT, mixed, or OO destination labels.

**Verdict:** PASS.

---

## 9. What is not proved

The near-diametrical terminal branch is not a contradiction by itself. A convex near-circular source can contain a boundary subarc with two almost antipodal vertices. An upper bound on the admissible terminal support-normal span or a terminal-ledger incompatibility is still required.

The uniform-corridor branch is also not closed by the new central-crossing localization. We know that each pair of diameter lines meets inside a common `o(D)` central ball, but the current train metric controls the row/column rhombus crossing centers, not the point where an actual switching diameter chord meets a row centerline. A straight diameter line can still thread the ordered train rectangle in ways not excluded by the present estimates.

The most specific next target is therefore:

```math
\boxed{
\text{control the row-centerline intersection of a centrally crossing switching diameter}
}
```

from its support interval, midpoint localization, fixed transverse margin, and the common ordered column flanks. A successful `o(D)` or fixed-fraction localization relative to the train crossing centers would connect the diameter weave to the metric grid for the first time.

**Final verdict:** PASS at proof-only scope. The terminal alternative is genuinely near-diametrical; otherwise the whole near-full paired population supports the uniform fixed-aperture massless/coercive/dense-grid corridor, and every tagged force-pair crossing is additionally confined to one common fixed-constant `O(D^{3/4})` central ball. C-II remains open.
