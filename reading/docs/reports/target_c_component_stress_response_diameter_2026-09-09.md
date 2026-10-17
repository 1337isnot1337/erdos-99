> Generated reading edition · [exact source](../../../docs/reports/target_c_component_stress_response_diameter_2026-09-09.md) · source SHA-256 `31414dfa0cedc9eea3591bd4119be2cf2098efd05992c3ae9ce34e197f7fc051`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-F8831FD9902B","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — HSR: harmonic component stress is controlled by response defect and attachment diameter

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-e43-scalar-stability`  
**Run type:** exact componentwise energy theorem / near-zero response localization  
**Target:** Target C C-II; ESN plus C66 near-zero phase  
**Depends on:** C11/C41 Schur response decomposition, C36/C40 attachment localization, normalized KKT stress  
**New external literature:** none  
**Computation:** none

## LEVEL I STATUS

**STILL OPEN.**

For one unloaded harmonic component `I_r`, let

- `A_r` be its loaded attachment set;
- `c^{(r)}_{st}` be its Kron-reduced response conductances;
- `S_r` be the total contact-stress mass on internal contacts of `I_r` and contacts from `I_r` to `B_+`;
- `L_r=diam(A_r)`.

Then the actual Euclidean coordinate functions give the exact component energy identity

```math
\boxed{
\sum_{s<t\in A_r}c^{(r)}_{st}|s-t|^2=S_r.
}
\tag{HSR.1}
```

Writing

```math
C_r:=\sum_{s<t\in A_r}c^{(r)}_{st}
```

and

```math
E_r:=\sum_{s<t\in A_r}c^{(r)}_{st}(D^2-|s-t|^2),
```

one has

```math
\boxed{E_r=D^2C_r-S_r.}
\tag{HSR.2}
```

Since every response pair lies in `A_r`, HSR.1 gives

```math
\boxed{C_r\ge \frac{S_r}{L_r^2}.}
\tag{HSR.3}
```

Therefore, whenever `L_r<D`,

```math
\boxed{
E_r
\ge
S_r\left(\frac{D^2}{L_r^2}-1\right),
}
\tag{HSR.4}
```

or equivalently

```math
\boxed{
S_r
\le
\frac{L_r^2}{D^2-L_r^2}E_r.
}
\tag{HSR.5}
```

This is the weighted theorem missing from the earlier component-diameter counts: a component whose loaded attachment hull is small compared with the source diameter can carry large contact stress only by paying a correspondingly large response defect.

For any family `R` with

```math
L_r\le L<D
\qquad(r\in R),
```

C41 gives the aggregate form

```math
\boxed{
\sum_{r\in R}S_r
\le
\frac{L^2}{D^2-L^2}\,D^2\varepsilon,
}
\tag{HSR.6}
```

where

```math
\varepsilon:=\sum_{b<k}c_{bk}-1
=\frac12\operatorname{tr}(\Lambda-L_H)
```

and

```math
D^2\varepsilon
=(D^2-1)S_{BB}+\sum_rE_r.
\tag{HSR.7}
```

Here `S_BB` is the total stress on direct loaded-loaded contacts.

### ESN near-zero consequence

At the forbidden ENS endpoint, ESN proves that there is one component `I_*` with

```math
\delta_*=(\lambda_E+o(1))D
```

and

```math
\sum_{r\ne *}\delta_r=o(D).
```

C40 gives

```math
L_r\le\delta_r+2.
```

Hence

```math
L_{small}:=\max_{r\ne *}L_r=o(D).
```

If simultaneously

```math
D\varepsilon\to0,
```

then HSR.6 gives

```math
\boxed{
\sum_{r\ne *}S_r=o(D).
}
\tag{HSR.8}
```

and HSR.7 gives

```math
\boxed{S_{BB}=o(1/D).}
\tag{HSR.9}
```

Since the normalized KKT virial identity is

```math
\sum_{e\in C}\alpha_e=D^2,
```

we conclude

```math
\boxed{
S_*=D^2-o(D).
}
\tag{HSR.10}
```

Thus ESN plus the C66 near-zero response phase does not merely produce one mechanically important cell. It forces essentially the entire `D^2` contact-stress mass into the unique macroscopic-diameter harmonic component.

---

## 1. Component Dirichlet energy

Fix `I_r`. Consider the contact network consisting of

1. all internal contacts with both endpoints in `I_r`; and
2. all contact edges from `I_r` to its loaded attachment set `A_r`.

Every such edge has unit Euclidean length and conductance equal to its positive KKT contact stress `alpha_e`.

The actual coordinate functions on `I_r` are harmonic for this weighted network because every unloaded vertex has zero diameter reaction:

```math
\sum_{xy\in C}\alpha_{xy}(p_x-p_y)=0.
\tag{1.1}
```

Therefore eliminating `I_r` preserves their Dirichlet energy. For the two Euclidean coordinate functions together, the network energy before elimination is

```math
\sum_{e\in E(I_r)\cup E(I_r,A_r)}
\alpha_e|p_u-p_v|^2.
```

Every contact length is one, so this equals exactly

```math
S_r.
\tag{1.2}
```

After Schur complementation, the same energy is

```math
\sum_{s<t\in A_r}c^{(r)}_{st}|s-t|^2.
```

This proves HSR.1.

---

## 2. Response mass versus attachment diameter

By definition of `L_r`,

```math
|s-t|^2\le L_r^2
\qquad(s,t\in A_r).
```

Use HSR.1:

```math
S_r
=\sum_{s<t}c^{(r)}_{st}|s-t|^2
\le L_r^2\sum_{s<t}c^{(r)}_{st}
=L_r^2C_r.
```

This proves HSR.3.

HSR.2 is the identity

```math
\begin{aligned}
E_r
&=\sum_{s<t}c^{(r)}_{st}(D^2-|s-t|^2)\\
&=D^2C_r-S_r,
\end{aligned}
```

using HSR.1 in the last step.

Substitute HSR.3 into HSR.2:

```math
E_r
\ge D^2\frac{S_r}{L_r^2}-S_r
=S_r\left(\frac{D^2}{L_r^2}-1\right).
```

This proves HSR.4 and HSR.5.

---

## 3. Aggregate family form

Let `R` be any set of components with `L_r<=L<D`. HSR.5 gives

```math
S_r
\le
\frac{L^2}{D^2-L^2}E_r.
```

Sum over `R`:

```math
\sum_{r\in R}S_r
\le
\frac{L^2}{D^2-L^2}\sum_{r\in R}E_r.
\tag{3.1}
```

C41 decomposes the global defect as

```math
D^2\varepsilon
=(D^2-1)S_{BB}+\sum_rE_r,
```

with every term nonnegative. Hence

```math
\sum_{r\in R}E_r\le D^2\varepsilon,
```

which gives HSR.6.

The same identity immediately gives

```math
\boxed{
S_{BB}
\le
\frac{D^2}{D^2-1}\varepsilon.
}
\tag{HSR.11}
```

---

## 4. Recover SSR as the singleton special case

For a singleton component `x`, all loaded attachments lie on the unit circle centered at `x`, so

```math
L_x\le2.
```

HSR.5 yields

```math
S_x
\le
\frac4{D^2-4}E_x,
```

or

```math
E_x\ge\frac{D^2-4}{4}S_x,
```

exactly the main singleton estimate in SSR.

Thus SSR is the explicit star/Kron-reduction proof of the sharp local special case, while HSR identifies the general energy mechanism.

---

## 5. Apply ESN concentration

ESN gives

```math
\sum_{r\ne *}\delta_r=o(D).
```

Therefore

```math
\max_{r\ne *}\delta_r=o(D),
```

and C40 gives

```math
L_{small}
\le
2+\max_{r\ne *}\delta_r
=o(D).
\tag{5.1}
```

Apply HSR.6 with all components except `I_*`:

```math
\sum_{r\ne *}S_r
\le
\frac{L_{small}^2}{D^2-L_{small}^2}D^2\varepsilon.
\tag{5.2}
```

If `D epsilon ->0`, then `D^2 epsilon=o(D)`. The prefactor in (5.2) is `o(1)`, so

```math
\sum_{r\ne *}S_r=o(D),
```

proving HSR.8.

HSR.11 gives

```math
S_{BB}=O(\varepsilon)=o(1/D),
```

which is HSR.9.

Finally the contact-stress normalization

```math
D^2
=S_{BB}+\sum_rS_r
```

gives HSR.10.

---

## 6. What the giant component now carries

Under ESN plus `D epsilon ->0`, the unique giant component satisfies simultaneously

```math
S_*=D^2-o(D),
```

```math
\delta_*=(\lambda_E+o(1))D,
```

```math
\tau_*=(\lambda_E+o(1))D.
```

Its response defect obeys

```math
0\le E_*\le D^2\varepsilon=o(D).
```

Therefore HSR.2 gives

```math
C_*
=\frac{S_*+E_*}{D^2}
=1-o(1/D).
\tag{6.1}
```

So essentially unit total boundary response and essentially all mechanical stress coexist in one component, while its total diameter defect is only `o(D)`.

This is the exact anisotropic cell that must be excluded next. It is stronger than the earlier statement that one component merely carries a positive fraction of stress.

---

## 7. Regression audit

- HSR is an energy identity plus a diameter bound; it does not infer conductance from support count.
- If `L_r` is comparable with `D`, HSR.5 can be weak. This is unavoidable: a component can transfer stress efficiently between nearly diametral terminals.
- No assumption that attachment response is a tree or star is used.
- Direct loaded-loaded stress is controlled separately by C41 because those contacts have response distance one.
- ESN is required only for the unique-giant corollary, not for HSR itself.
- HSR.10 is conditional on the near-zero response phase `D epsilon ->0`; large trace/response defect remains a separate branch.

## 8. Next target

The remaining ESN/C66 low-response object is now one component with

```math
S_*=D^2-o(D),\qquad
C_*=1-o(1/D),\qquad
E_*=o(D),
```

and graph diameter/attachment-contact budget `(lambda_E+o(1))D`.

C66 says the mechanical diameter reactions are simultaneously concentrated on one boundary star. The next high-value theorem is therefore a **giant-cell near-diameter response localization**:

> show that a circular-planar harmonic component carrying `D^2-o(D)` unit-contact stress and only `o(D)` response defect cannot route essentially unit response through a single near-diameter terminal star while its attachment/contact diameter is only `lambda_E D+o(D)`.

The bridge-hinge / deep-cell machinery of PR #126 is a second route if the giant component contains macroscopic bridge depth.

## 9. Compact handoff

```text
HSR exact component theorem.
For component r, let S_r be total contact stress on its internal+attachment edges,
C_r total Kron response conductance, E_r its C41 diameter defect, and
L_r=diam(A_r). Harmonic coordinate energy gives exactly
    sum c_st^(r)|s-t|^2 = S_r.
Hence
    C_r >= S_r/L_r^2,
    E_r = D^2 C_r-S_r
        >= S_r(D^2/L_r^2-1).
So for L_r<D,
    S_r <= [L_r^2/(D^2-L_r^2)] E_r.
For any family with L_r<=L,
    sum S_r <= [L^2/(D^2-L^2)] D^2 epsilon.
Also direct loaded-loaded stress
    S_BB <= D^2 epsilon/(D^2-1).

ESN has one component * with delta_*/D->lambda_E and
sum_{r!=*}delta_r=o(D), so max_{r!=*}L_r=o(D).
If D epsilon->0, then
    sum_{r!=*}S_r=o(D),
    S_BB=o(1/D),
and total contact stress D^2 forces
    S_*=D^2-o(D).
Moreover E_*=o(D), so C_*=1-o(1/D).
The low-response branch is reduced to one giant anisotropic harmonic component.
```
