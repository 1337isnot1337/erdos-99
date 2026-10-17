> Generated reading edition · [exact source](../../../docs/reports/target_c_response_diameter_defect_trace_2026-08-31.md) · source SHA-256 `5bd6227eea1e6531ad2f65dd3a1e8e91c7f2bc8ad8e3c54a66ade0415a9ed777`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-8FE844BFE0E1","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C41: the circular-planar response has a strict diameter-defect trace

**Date:** 2026-08-31  
**Target:** C-II  
**Depends on:** C11, C15, C26, C36, positive KKT contact stress  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

Let `Lambda` be the C11 Dirichlet-to-Neumann response of the fully positive contact network on the loaded force-hull boundary `B_+`, and write

$$
c_{bk}:=-\Lambda_{bk}\ge0\qquad(b\ne k).
$$

Let `L_H` be the `beta`-weighted positive-diameter Laplacian. Then every sufficiently large fully force-visible triangle-free survivor satisfies the exact identity

$$
\boxed{
\frac{D^2}{2}\operatorname{tr}(\Lambda-L_H)
=
\sum_{b<k}c_{bk}\bigl(D^2-|b-k|^2\bigr)
>0.
}
\tag{C41.1}
$$

In particular

$$
\boxed{\operatorname{tr}\Lambda>2=\operatorname{tr}L_H.}
\tag{C41.2}
$$

At the same time C11 still gives

$$
(\Lambda-L_H)\mathbf1=0,
\qquad
(\Lambda-L_H)P_B=0.
\tag{C41.3}
$$

Thus the response defect is a nonzero equilibrium stress on the convex loaded boundary, annihilates the three affine scalar modes, and has strictly positive trace.

The strictness decomposes componentwise: every unpinned harmonic component contributes a positive amount to the right side of C41.1, and every direct loaded-loaded unit contact also contributes positively. No uniform quantitative gap is claimed; arbitrarily small KKT/effective conductances remain a binding obstruction.

---

## 1. Response decomposition by unpinned components

Work in the contact-minimal fully force-visible branch and choose a relative-interior normalized KKT stress. Then `C_+=C`, every contact conductance `alpha_e` is positive, and C26 gives

$$
Q^\circ=B_+.
\tag{C41.4}
$$

Let

$$
I=V(C)\setminus B_+
$$

and let `I_1,...,I_{c_I}` be the connected components of `C[I]`. For each component define its loaded attachment set

$$
A_r:=N_C(I_r)\cap B_+.
\tag{C41.5}
$$

C36 proves

$$
|A_r|\ge3.
\tag{C41.6}
$$

Order the weighted contact Laplacian by `B_+,I_1,...,I_{c_I}`. The interior Dirichlet block is block diagonal across the `I_r`, so the Schur complement decomposes as

$$
\Lambda=L_{BB}^{\rm dir}+\sum_{r=1}^{c_I}\Lambda^{(r)},
\tag{C41.7}
$$

where `L_{BB}^{dir}` is the Laplacian of direct loaded-loaded unit contacts and `Lambda^(r)` is the response contribution obtained by eliminating only `I_r`.

Write

$$
c^{(r)}_{st}:=-\Lambda^{(r)}_{st}
\qquad(s\ne t,\ s,t\in A_r).
\tag{C41.8}
$$

### Lemma C41.1 — each harmonic attachment set is a strict response clique

For every `r` and every distinct `s,t in A_r`,

$$
\boxed{c^{(r)}_{st}>0.}
\tag{C41.9}
$$

#### Proof

The principal Dirichlet block `L_{I_rI_r}` is an irreducible nonsingular M-matrix because `I_r` is connected, all contact conductances are positive, and `I_r` is attached to the Dirichlet boundary. Hence

$$
L_{I_rI_r}^{-1}>0
$$

entrywise.

The off-diagonal Schur contribution is

$$
-\,L_{B I_r}L_{I_rI_r}^{-1}L_{I_rB}.
$$

Both `s` and `t` have a strictly negative contact-Laplacian entry to at least one vertex of `I_r`; strict positivity of the inverse makes the `(s,t)` entry strictly negative. Therefore `c^{(r)}_{st}>0`. `square`

Thus the full response conductance on a boundary pair is

$$
c_{st}=\alpha^{BB}_{st}+\sum_r c^{(r)}_{st},
\tag{C41.10}
$$

with absent terms interpreted as zero.

---

## 2. Every response source creates strict subdiameter energy

For sufficiently large triangle-free global minimizers, C15 excludes three pairwise diametral source points.

Fix an unpinned component `I_r`. By C41.6 choose three distinct vertices `a,b,c in A_r`. Lemma C41.1 gives positive response conductance on all three pairs. C15 says at least one of

$$
|a-b|,\ |b-c|,\ |c-a|
$$

is strictly smaller than `D`. Therefore

$$
\boxed{
E_r:=\sum_{s<t\in A_r}c^{(r)}_{st}\bigl(D^2-|s-t|^2\bigr)>0.
}
\tag{C41.11}
$$

Every direct loaded-loaded contact `bk` contributes

$$
\alpha_{bk}(D^2-|b-k|^2)
=\alpha_{bk}(D^2-1)>0
\tag{C41.12}
$$

because `D>1` in the sufficiently large regime.

The connected contact core is nontrivial. Hence either `I` is nonempty, so some `E_r>0`, or `I` is empty, in which case every contact is loaded-loaded and at least one positive term C41.12 exists.

Consequently

$$
\boxed{
\sum_{b<k}c_{bk}(D^2-|b-k|^2)>0.
}
\tag{C41.13}
$$

More precisely, C41.7 gives the decomposition

$$
\sum_{b<k}c_{bk}(D^2-|b-k|^2)
=
(D^2-1)\sum_{bk\in C[B_+]}\alpha_{bk}
+
\sum_{r=1}^{c_I}E_r.
\tag{C41.14}
$$

Every term on the right is nonnegative and every present response source contributes strictly positively.

---

## 3. Exact coordinate energy converts the defect into trace

C11 says the actual coordinate functions are the harmonic extensions of their boundary values and gives

$$
P_B^{\mathsf T}\Lambda P_B
=
\sum_{ij\in C}\alpha_{ij}(p_i-p_j)(p_i-p_j)^{\mathsf T}.
\tag{C41.15}
$$

Taking traces and using `|p_i-p_j|=1` on contacts and the normalized identity `sum_C alpha=D^2`,

$$
\boxed{
\sum_{b<k}c_{bk}|b-k|^2=D^2.
}
\tag{C41.16}
$$

Let

$$
C_{\rm resp}:=\sum_{b<k}c_{bk}.
$$

Subtract C41.16 from `D^2 C_resp`:

$$
D^2(C_{\rm resp}-1)
=
\sum_{b<k}c_{bk}(D^2-|b-k|^2).
\tag{C41.17}
$$

The right side is strictly positive by C41.13, so

$$
\boxed{C_{\rm resp}>1.}
\tag{C41.18}
$$

A weighted graph Laplacian has trace twice its total conductance, hence

$$
\operatorname{tr}\Lambda=2C_{\rm resp}>2.
\tag{C41.19}
$$

On the diameter side `sum_H beta=1`, so

$$
\operatorname{tr}L_H=2.
\tag{C41.20}
$$

Combining C41.17-C41.20 proves C41.1-C41.2. `square`

---

## 4. Exact effect on the C-II frontier

C41 adds a scalar invariant to the C33-C40 near-minimal response normal form:

```text
M = Lambda-L_H
M 1 = 0
M P_B = 0
tr M > 0

and exactly
(D^2/2) tr M
    = sum_response c_bk (D^2-|b-k|^2)
    = direct loaded-contact defect + sum_harmonic-component defects.
```

This is stronger than merely proving `Lambda != L_H`: it identifies the exact positive currency by which the contact response differs from a unit-total-weight network supported entirely on diameter pairs.

It does **not** imply `M` is positive semidefinite. The Connelly convex-polygon tensegrity theorem cannot be imported directly after Kron reduction because the positive effective response edges can be crossing interior chords rather than polygon-boundary cables.

A closing response theorem would need to combine the strict diameter-defect trace with circular-planar minors, C36-C40 noncrossing attachment structure, reciprocal geometry, or global packing.

---

## 5. Regression audit

- **Unit square:** `I=empty`; the four loaded-loaded unit contacts make the defect strictly positive. The resulting response stress is compatible with the known square PSD rank-one example.
- **No direct loaded-loaded contacts:** every unpinned component still contributes a positive `E_r` by C15 and C36.
- **Tiny component conductance:** allowed. C41 proves strict positivity, not a uniform lower bound independent of `n` or the KKT stress.
- **Near-minimal boundary surplus:** compatible. C33-C40 may make the number of response components `o(D)`, but C41 does not force any one component to carry macroscopic defect.
- **C-I:** outside scope because full contact positivity and C36 are C-II inputs.

```text
C41:
Decompose the C11 Kron response into direct B_+-B_+ contacts plus the responses of the
C36 unpinned components.  Every component attachment set has at least three vertices
and its Schur complement is a strict response clique.  C15 forces at least one
subdiameter pair in each such clique.  Direct loaded-loaded contacts are unit pairs.
Therefore
    sum c_bk(D^2-|b-k|^2)>0.
But C11 coordinate energy gives sum c_bk|b-k|^2=D^2, so
    (D^2/2) tr(Lambda-L_H)
      = D^2(sum c_bk-1)
      = sum c_bk(D^2-|b-k|^2)>0.
Thus tr Lambda>2=tr L_H while M still kills 1,x,y.
```
