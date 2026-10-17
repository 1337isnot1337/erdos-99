> Generated reading edition · [exact source](../../../docs/audits/target_c_low_response_mu_floor_hostile_audit_2026-09-12.md) · source SHA-256 `dfc735ccf9c8ccfddf5ea43467c4aab6085ec19e621b762622cecd80382e925a`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-DCD8A7C7D6A6","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Hostile audit — Target C low-response stress localization

**Date:** 2026-09-12  
**Audited artifact:** [`target_c_low_response_mu_floor_2026-09-12.md`](../reports/target_c_low_response_mu_floor_2026-09-12.md)  
**State lock:** `2026-09-12.audit.46`  
**Verdict:** **PASS at proof-only branch scope; not canonical.**

The audited candidate is a valid finite response-energy reduction. It gives a useful
new description of the `D\varepsilon_D\to0` branch, while leaving the exact source-level
closure unresolved. The theorem-state manifest and active route are unchanged.

## 1. Scope and notation

Use the contact-minimal, then diameter-pair-minimal C-II representative and retain the
full source, including contact-isolated points. For a positive-contact component
`I_r` with loaded attachment set `A_r`, put

```math
 L_r=\operatorname{diam}(A_r),\qquad
 S_r=\sum_{e\text{ incident to }I_r}\alpha_e.
```

Let `S_BB` be the contact stress on direct loaded-loaded contacts, and let
`c^{(r)}_{st}` be the Schur-response conductances of `I_r` on `A_r`. Define

```math
 C_r=\sum_{s<t}c^{(r)}_{st},\qquad
 E_r=\sum_{s<t}c^{(r)}_{st}(D^2-|s-t|^2),
```

and let `\varepsilon_D=\sum_{s<t}c_{st}-1` be the C41 response defect. All sums
are over actual source vertices or actual response pairs; no isolated source point is
placed in the core stress matrices.

## 2. Audit of the component energy identity

The weighted contact equilibrium equations at an unloaded component make the two
coordinate functions harmonic with the loaded attachment values as boundary data.
Schur elimination therefore preserves their Dirichlet energy. Since every actual
contact has unit length,

```math
 \boxed{S_r=\sum_{s<t\in A_r}c^{(r)}_{st}|s-t|^2.}
\tag{LR-A.1}
```

This uses only the positive KKT stress on the nonisolated contact core. It does not
assert a lower bound on an individual multiplier and does not extend the §57 affine
kernel to contact-isolated coordinates.

Because all source distances are at most `D`,

```math
 E_r=D^2C_r-S_r\ge0,
\qquad
 S_r\le L_r^2C_r.
\tag{LR-A.2}
```

For `L_r<D`, eliminating `C_r` gives the exact finite estimate

```math
 \boxed{
 E_r\ge S_r\left({D^2\over L_r^2}-1\right),
 \qquad
 S_r\le {L_r^2\over D^2-L_r^2}E_r.
 }
\tag{LR-A.3}
```

The inequalities are in the correct direction: a component with short attachment
diameter can carry substantial contact stress only by paying response defect.

## 3. Audit of the global response decomposition

The C41 coordinate-energy identity and the normalized KKT virial partition give

```math
 \boxed{
 D^2\varepsilon_D
 =(D^2-1)S_{BB}+\sum_rE_r,
 \qquad
 S_{BB}+\sum_rS_r=D^2.
 }
\tag{LR-A.4}
```

Every term is nonnegative. In particular,

```math
 S_{BB}\le {D^2\over D^2-1}\varepsilon_D.
\tag{LR-A.5}
```

For any family of components with `L_r\le L<D`, summing (LR-A.3) and using (LR-A.4)
gives

```math
 \sum S_r\le {L^2\over D^2-L^2}D^2\varepsilon_D.
\tag{LR-A.6}
```

No hidden assumption that response conductance is supported on actual diameter pairs
is used here; `E_r` is exactly the weighted deficit of the Schur response pairs.

## 4. Audited branch consequence

Let `L_*` be the largest component attachment diameter. If `L_*<D`, set
`T=\sum_rS_r=D^2-S_{BB}`. Equation (LR-A.6) implies

```math
 {L_*^2\over D^2}\ge {T\over T+D^2\varepsilon_D}.
\tag{LR-A.7}
```

For `D\ge2`, (LR-A.5) gives `D^2\varepsilon_D\ge S_{BB}`, hence the denominator
in (LR-A.7) is at least `D^2`. Thus

```math
 L_*\ge D\sqrt{1-\varepsilon_D}
 \qquad(0\le\varepsilon_D\le1).
\tag{LR-A.8}
```

Canonical C40 gives `L_*\le\delta_*+2`, while the Section-62 component ledger gives
`\sum_r\delta_r\le\mu_DD+6`. Therefore

```math
 \boxed{
 \mu_D\ge\sqrt{1-\varepsilon_D}-{8\over D}.
 }
\tag{LR-A.9}
```

The case `L_*=D` satisfies the same conclusion directly. If there were no unloaded
component, then `S_{BB}=D^2`, contradicting (LR-A.5) for `D>\sqrt2` and
`\varepsilon_D\le1`; so the largest component is defined in the stated range.

If `D\varepsilon_D\to0`, the argument with
`\eta_D=\sqrt{\varepsilon_D/D}` is also valid. Components with
`L_r\le(1-\eta_D)D` carry total stress at most

```math
 O(D^2\varepsilon_D/\eta_D)
 =O(D^2\sqrt{D\varepsilon_D})=o(D^2),
```

and the remaining stress lies in components with `L_r=D-o(1)`. Their graph diameters
are `D-o(1)` by C40, while `\sum_r\delta_r\le2+2\pi D`; consequently there are at
most six such components for all sufficiently large `D`. This is a stress
localization statement, not a claim that one component is unique.

## 5. Hostile checks

1. **No full-source kernel extension.** The proof uses only harmonic coordinates on
   the nonisolated positive-contact components. Contact-isolated points remain in the
   global source and contribute neither `S_r` nor a false affine-kernel row.
2. **No individual stress floor.** The conclusion follows from weighted energy and
   nonnegativity; it does not assume that any contact or response conductance is
   uniformly positive.
3. **No response/diameter identification.** The response pairs can be non-diameter
   pairs. Their distance deficit is precisely what pays `E_r`.
4. **Correct asymptotic scale.** `D\varepsilon_D\to0` implies
   `D\varepsilon_D=o(1)`, so `D\eta_D=\sqrt{D\varepsilon_D}=o(1)` and the claimed
   `D-o(1)` attachment scale is justified.
5. **Global-minimality quantifier.** The candidate is a branch reduction for the
   canonical normalized global minimizer. It constructs no competitor and does not
   assert that near-diameter stress localization contradicts global minimality.

## 6. Disposition and exact remaining bridge

The audited result is **audited-working / proof-only**, not canonical. It sharpens the
live low-response branch to one of at most six near-diameter attachment cells carrying
essentially all contact stress. It does not close that branch because the current
stack has no theorem converting this weighted near-diameter geometry into an exact
unit equilateral triangle or a same-cardinality strict sub-`D` source.

The remaining theorem target is therefore source-level:

```math
\text{near-diameter attachment cell(s)}
 +\text{ concentrated contact stress}
 \Longrightarrow
 \text{exact triangle, strict competitor, or diameter contradiction}.
```

The separate high-response branch `D\varepsilon_D\not\to0` and the macroscopic
inactive-container branch remain untouched.
