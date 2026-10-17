> Generated reading edition · [exact source](../../../docs/reports/target_c_macroscopic_component_stress_fraction_2026-08-31.md) · source SHA-256 `6140d090d354b1de084b23ef41004fa6cd42253e6398a1d979a428cbec26f94e`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-B9896D1513B7","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_macroscopic_component_stress_fraction_2026-08-31.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=7e3d1156c196dc7a894e26b05e1e9181e5d640d4; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — Target C C45: the macroscopic-response branch carries a fixed fraction of contact stress

**Date:** 2026-08-31  
**Target:** C-II  
**Depends on:** C11, C41, C44  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

C44 proves that if the uniformly short C11 response mass is below `1/2`, then all response conductance on pairs longer than `rho_0 D` is carried by at most `K_0` macroscopic harmonic components. The proof actually yields more than the stated total-conductance bound.

### Theorem C45 — fixed component stress fraction

In C44 Branch B there is an unpinned harmonic component `I_r` for which the **long response mass**

```math
L_r
:=
\sum_{\substack{s<t\in A_r\\|s-t|>\rho_0D}}c^{(r)}_{st}
\tag{C45.1}
```

satisfies

```math
\boxed{L_r>\frac1{2K_0}.}
\tag{C45.2}
```

Let `E_r` be the set consisting of all contact edges internal to `I_r` together with all contact edges from `I_r` to `B_+`. Then the positive contact-stress mass carried by this one harmonic component obeys

```math
\boxed{
\sum_{e\in E_r}\alpha_e
>
\frac{\rho_0^2}{2K_0}D^2.
}
\tag{C45.3}
```

Since the normalized full contact stress satisfies

```math
\sum_{e\in C}\alpha_e=D^2,
```

this one unloaded component carries a fixed absolute fraction

```math
\boxed{\frac{\rho_0^2}{2K_0}>0}
\tag{C45.4}
```

of the entire KKT contact-stress mass.

Combined with C44, the same component also has

```math
\operatorname{diam}A_r>\rho_0D,
\quad
\delta_r>\rho_0D-2,
\quad
|A_r|>\frac{\rho_0D+1}{3},
\quad
t_r>\rho_0D+1.
\tag{C45.5}
```

Thus the non-short-response branch is not merely a large geometric cell. It is one macroscopic harmonic cell simultaneously carrying linear boundary incidence, linear graph diameter, and a positive fraction of the full normalized contact stress.

---

## 1. Long response mass cannot disperse over many components

In C44 Branch B,

```math
S_{short}<\frac12.
```

C41 gives total response conductance

```math
C_{resp}>1,
```

so the total response mass on pairs longer than `rho_0D` is

```math
C_{long}=C_{resp}-S_{short}>\frac12.
\tag{C45.6}
```

C44 proves that no direct loaded-loaded unit contact and no nonmacroscopic harmonic component contributes to `C_long`. There are at most `K_0` macroscopic components. Therefore

```math
C_{long}=\sum_{r\in\mathcal M}L_r
\tag{C45.7}
```

for a set `mathcal M` of at most `K_0` components.

By pigeonhole, some `r in mathcal M` satisfies

```math
L_r\ge\frac{C_{long}}{|\mathcal M|}
>\frac1{2K_0},
```

which proves C45.2. `square`

---

## 2. Componentwise Dirichlet energy equals component contact-stress mass

The C11 response is obtained by Schur complement of the positive contact Laplacian. Because the unpinned components `I_r` are disconnected from one another after deleting `B_+`, the response decomposes componentwise.

For one component, let `Lambda^(r)` be its Schur response on `A_r`, so

```math
-\Lambda^{(r)}_{st}=c^{(r)}_{st}\qquad(s\ne t).
```

The actual two coordinate functions on `I_r` are harmonic for the `alpha` conductances. Therefore their Dirichlet energy equals the boundary response energy:

```math
\boxed{
\sum_{e=uv\in E_r}\alpha_e|u-v|^2
=
\sum_{s<t\in A_r}c^{(r)}_{st}|s-t|^2.
}
\tag{C45.8}
```

Every edge in `E_r` is a unit contact, hence

```math
\boxed{
\sum_{e\in E_r}\alpha_e
=
\sum_{s<t\in A_r}c^{(r)}_{st}|s-t|^2.
}
\tag{C45.9}
```

Restrict the right side to the long response pairs counted by `L_r`. Every such pair has squared distance greater than `rho_0^2D^2`, so

```math
\sum_{e\in E_r}\alpha_e
>
\rho_0^2D^2L_r.
\tag{C45.10}
```

Insert C45.2:

```math
\sum_{e\in E_r}\alpha_e
>
\frac{\rho_0^2}{2K_0}D^2.
```

This proves C45.3. `square`

---

## 3. Exact effect on C-II

C44-C45 replace a diffuse “tiny KKT weights might hide everything” obstruction by a clean binary alternative:

```text
fully force-visible response:
    Branch A:
        short response mass >= 1/2
        -> absolute trace gap tr(Lambda-L_H)>=gamma_0

    Branch B:
        one unpinned harmonic component I_r has
            long response mass > 1/(2K_0)
            contact stress mass > [rho_0^2/(2K_0)] D^2
            attachment diameter > rho_0 D
            graph diameter > rho_0 D-2
            |A_r| > (rho_0 D+1)/3
            t_r > rho_0 D+1
```

Branch B now has a fixed positive fraction of the same `D^2` stress budget that drives the reciprocal polygon. This creates a direct interface with the C27 bridge-stress split and with any future block/area theorem that can localize reciprocal stress inside a harmonic cell.

The shortest Branch-B target is:

> **Macroscopic harmonic-cell exclusion.** Exclude an unloaded component satisfying C45.3-C45.5 in a sufficiently large triangle-free global minimizer.

A proof could use its convex attachment hull, C42 strict-rhombic bulk, the reciprocal stress geometry, or a finite-container packing inequality. No individual-edge stress lower bound is needed.

---

## 4. Regression audit

- **Stress concentrated on a few edges:** allowed; C45 uses only the aggregate component stress.
- **Long response mass spread over many tiny components:** impossible by C44's constant macroscopic-component count.
- **A single large component with tiny response:** still possible in Branch A, but then enough response mass is uniformly short to give the absolute trace gap.
- **Component response has additional short pairs:** allowed; C45 lower-bounds stress using only its long-pair submass.
- **C-I:** outside scope.

```text
C45:
In C44 Branch B the total long response mass is >1/2 and is carried by <=K_0
macroscopic harmonic components. Hence one component has long response mass
L_r>1/(2K_0).

For that component, the C11 harmonic Dirichlet identity gives
    sum_{e in E_r} alpha_e
      = sum_{s<t in A_r} c_st^(r)|s-t|^2
      > rho_0^2 D^2 L_r
      > [rho_0^2/(2K_0)]D^2.
Thus one unloaded harmonic component carries a fixed positive fraction of the entire
D^2 contact-stress mass, in addition to C44's linear diameter/attachment bounds.
```
