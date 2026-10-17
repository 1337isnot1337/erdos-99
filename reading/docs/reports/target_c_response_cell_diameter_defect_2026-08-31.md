> Generated reading edition · [exact source](../../../docs/reports/target_c_response_cell_diameter_defect_2026-08-31.md) · source SHA-256 `d878e6bd3868dfb4377dbd58161aee30af0d63ea3051ec79a89c9127d49c54b0`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-AE5B1E785BA7","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C47: C41 response defect localizes onto attachment-cell diameters

**Date:** 2026-08-31  
**Target:** C-II  
**Depends on:** canonical C11 response identity, C33-C36, mainline C41 strict response diameter defect, C43-C46  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

C41 proves that the Kron-reduced contact response has a strictly positive diameter-defect trace. C47 decomposes that defect across the harmonic attachment cells.

For one unpinned component `I_r`, let

- `E_r` be its internal contact edges together with its contact edges to `B_+`;
- `W_r=sum_{e in E_r} alpha_e` be its original contact-stress mass;
- `A_r` its distinct loaded attachment set;
- `P_r=conv(A_r)` its C43 cell;
- `d_r=diam(P_r)`; and
- `c_st^(r)>0` the complete-graph conductances of the Kron response of component `I_r` on `A_r`.

Then

`W_r = sum_{s<t in A_r} c_st^(r) |b_s-b_t|^2`.

If `C_r=sum c_st^(r)`, the component contribution to the C41 unscaled diameter defect is

`D_r = D^2 C_r-W_r`.

Since every response chord lies in `P_r`,

`W_r <= d_r^2 C_r`,

so

`D_r >= W_r(D^2/d_r^2-1)`.

Direct loaded-loaded unit contacts contribute exactly `(D^2-1)alpha_e` each.

Consequently, if `M=Lambda-L_H` is the C11 response-minus-diameter matrix and

`mu_BB = (1/D^2) sum_{e in C[B_+]} alpha_e`,

`mu_r=W_r/D^2`,

then `mu_BB+sum_r mu_r=1` and

```math
\boxed{
\frac12\operatorname{tr}M
\ge
\mu_{BB}(D^2-1)
+
\sum_r\mu_r\left(\frac{D^2}{d_r^2}-1\right).}
```

C46 says at most three cells have `d_r=D` exactly. Thus all contact-stress mass outside at most three exact-diameter cells and the loaded-loaded contacts pays a strictly positive response-defect factor.

---

## 1. Response decomposition by unpinned components

Pin `B_+` and decompose the unpinned contact graph into components `I_r`. The full contact Laplacian Kron-reduces as the sum of:

1. direct loaded-loaded contact Laplacians, with conductance `alpha_{bb'}` on a unit edge `bb'`; and
2. the independent Kron responses `Lambda_r` of the components `I_r` on their attachment sets `A_r`.

Thus

`Lambda = L_BB^contact + sum_r Lambda_r`.

Because each `I_r` is connected and every attachment vertex has a positive conductance edge into it, `Lambda_r` is an irreducible response M-matrix. Hence for every distinct `s,t in A_r`,

`(Lambda_r)_{st}=-c_st^(r)` with `c_st^(r)>0`.

---

## 2. Coordinate energy equals original component stress mass

Use the two coordinate functions as Dirichlet boundary data on `A_r`. The actual source coordinates on `I_r` are harmonic by positive KKT equilibrium, so they are exactly the energy-minimizing harmonic extension used in the Kron response.

The original network energy is

`sum_{e in E_r} alpha_e |p_i-p_j|^2`.

Every edge in `E_r` is a unit contact, so this equals `W_r`.

The reduced complete-graph energy is

`sum_{s<t in A_r} c_st^(r) |b_s-b_t|^2`.

Therefore

```math
\boxed{
W_r
=
\sum_{s<t\in A_r}c_{st}^{(r)}|b_s-b_t|^2.}
\tag{C47.1}
```

---

## 3. Cell diameter lower-bounds response defect

Put

`C_r=sum_{s<t} c_st^(r)`.

The component's unscaled C41 diameter defect is

```math
\mathcal D_r
:=
\sum_{s<t\in A_r}c_{st}^{(r)}(D^2-|b_s-b_t|^2)
=D^2C_r-W_r.
\tag{C47.2}
```

Every attachment chord has length at most `d_r=diam(P_r)`, so C47.1 gives

`W_r <= d_r^2 C_r`.

Hence `C_r>=W_r/d_r^2`, and

### Theorem C47.1 — component diameter-defect bound

```math
\boxed{
\mathcal D_r
\ge
W_r\left(\frac{D^2}{d_r^2}-1\right).}
\tag{C47.3}
```

The right side is zero exactly at the level of this estimate when `d_r=D`; C41 remains strictly positive even then because a response clique on at least three distinct attachment vertices contains subdiameter pairs.

---

## 4. Direct loaded-loaded contacts

A direct loaded-loaded contact has source length exactly one and response conductance `alpha_e`. Its C41 defect contribution is

```math
\boxed{\alpha_e(D^2-1).}
\tag{C47.4}
```

Let

`W_BB=sum_{e in C[B_+]} alpha_e`.

The contact edges partition into the direct loaded-loaded edges and the sets `E_r`, so the KKT virial identity `sum_C alpha_e=D^2` gives

```math
\boxed{W_{BB}+\sum_rW_r=D^2.}
\tag{C47.5}
```

Define normalized stress masses

`mu_BB=W_BB/D^2`, `mu_r=W_r/D^2`.

Then

`mu_BB+sum_r mu_r=1`.

---

## 5. Global response-cell defect inequality

Write the full reduced response as a complete graph on `B_+` with conductances `c_st`, and recall `sum_H beta_h=1`. The coordinate response identity gives

`sum_{s<t} c_st |b_s-b_t|^2 = D^2`.

Therefore the C41 unscaled diameter defect is

`mathcal D = sum c_st(D^2-|b_s-b_t|^2)=D^2(sum c_st-1)`.

Since `tr(Lambda-L_H)=2(sum c_st-1)`,

`mathcal D=(D^2/2) tr M`.

Summing C47.3 and C47.4 yields:

### Theorem C47 — stress-weighted attachment-cell diameter defect

```math
\boxed{
\frac12\operatorname{tr}M
\ge
\mu_{BB}(D^2-1)
+
\sum_r\mu_r\left(\frac{D^2}{d_r^2}-1\right).}
\tag{C47.6}
```

Every term is nonnegative.

---

## 6. Interaction with C46

Because `P_r` is the convex hull of source vertices, `d_r=D` exactly iff `A_r` contains a full core diameter pair. C46 proves that, for sufficiently large minimizers, this can occur in at most three attachment cells.

Hence all but at most three cells satisfy `d_r<D` and therefore have a strictly positive factor

`D^2/d_r^2-1>0`.

C47 does **not** give a uniform positive lower bound for that factor: subdiameter attachment chords can approach `D`. Nor does it bound `tr M` from above by `o(1)`. Its exact content is a localization principle:

> any sequence with small normalized C41 response defect must concentrate almost all original contact-stress mass in at most three nearly/exactly diameter-spanning cells, while forcing direct loaded-loaded contact stress to be correspondingly tiny.

A quantitative stability theorem for near-diameter cells would turn C47 into a closing tool.

## Regression audit

- One component attached to all `B_+`: C47 is exactly the global C41 defect decomposition for that component.
- Direct loaded-loaded contact stress is heavily charged by the factor `D^2-1`, but no independent small upper bound on `tr M` is currently known.
- Cells with `d_r` arbitrarily close to `D` are allowed; no fake uniform gap is asserted.
- The component response conductances can be highly nonuniform; C47 uses only their exact coordinate energy.
