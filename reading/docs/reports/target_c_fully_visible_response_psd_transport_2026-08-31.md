> Generated reading edition · [exact source](../../../docs/reports/target_c_fully_visible_response_psd_transport_2026-08-31.md) · source SHA-256 `e5c2903f0cff30640e91d8a533a232caf11c2b698b6fb5ab25c6d6f8fea75a31`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-D9D2C9447DD6","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_fully_visible_response_psd_transport_2026-08-31.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=8557c4d5f653cbae1b59ecb0f1b27e531105b466; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — Target C: fully visible response PSD and transport charging

**Date:** 2026-08-31  
**Repository base:** `5c2e17f9` (main after C63 / PR #65)  
**Run type:** C-II response correction / quantitative transport  
**Target:** Target C Gate C-II  
**Depends on:** C10-C11 Dirichlet response, C26 fully visible positive contact core, C54 universal PSD, C63 Gate C-I

## LEVEL I STATUS

**STILL OPEN. GATE C-I IS CLOSED.**

Several older C-II frontier notes retain a caution that no positive-semidefinite or
Loewner comparison between the contact Dirichlet response `Lambda` and the diameter
Laplacian `L_H` is known. That caution became obsolete after C54.

In the fully force-visible branch `C=C_*`, choose a relative-interior normalized KKT
stress. Every unit contact has positive stress, its positive contact graph is the
connected nonisolated contact core, and C54 gives

$$
\Omega=L_C(\alpha)-L_H(\beta)\succeq0.
$$

Schur complementation of the unloaded contact vertices now gives the exact boundary
comparison

$$
\boxed{M:=\Lambda-L_H\succeq0.}
$$

This is a genuine C-II Loewner theorem. It immediately turns each non-diameter response
conductance into diagonal defect mass and gives quantitative charging bounds for
terminal-disjoint response transport.

## 1. Fully visible relative-interior stress

Assume the C63 conclusion

$$
C=C_*.
\tag{C64.1}
$$

Choose a relative-interior point of the normalized KKT polytope. Then

$$
\alpha_e>0\qquad(e\in C)
\tag{C64.2}
$$

and its positive contact graph is the entire nonisolated contact core. By the promoted
support-connectivity theorem this graph is connected and contains both endpoints of
every positive diameter edge.

Let

$$
B=B_+=V(H_+)
$$

be the loaded boundary vertices and let

$$
I=V(C)\setminus B.
$$

Partition the positive contact Laplacian as

$$
L_C=
\begin{pmatrix}
A_{BB}&A_{BI}\\
A_{IB}&A_{II}
\end{pmatrix}.
\tag{C64.3}
$$

The diameter Laplacian is supported only on `B`.

Because the positive contact graph is connected and `B` is nonempty, the grounded
interior block is positive definite:

$$
\boxed{A_{II}\succ0.}
\tag{C64.4}
$$

Indeed, for `z in R^I`, extending it by zero on `B` gives

$$
z^{\mathsf T}A_{II}z
=\sum_{ij\in C}\alpha_{ij}(\tilde z_i-\tilde z_j)^2,
$$

which vanishes only when the extension is constant on the connected contact graph;
the zero boundary values then force that constant to be zero.

The Dirichlet response of the positive contact network on `B` is

$$
\Lambda=A_{BB}-A_{BI}A_{II}^{-1}A_{IB}.
\tag{C64.5}
$$

## 2. Boundary Loewner theorem

C54 gives, for this same normalized stress,

$$
\Omega
=
\begin{pmatrix}
A_{BB}-L_H&A_{BI}\\
A_{IB}&A_{II}
\end{pmatrix}
\succeq0.
\tag{C64.6}
$$

Since `A_II` is positive definite, the Schur complement theorem gives:

### Theorem C64 (fully visible response PSD)

$$
\boxed{
M:=\Lambda-L_H
=A_{BB}-L_H-A_{BI}A_{II}^{-1}A_{IB}
\succeq0.
}
\tag{C64.7}
$$

The affine response identities remain

$$
M\mathbf1=0,
\qquad
MP_B=0.
\tag{C64.8}
$$

Thus `M` is PSD with the three forced scalar affine zero modes. No generic strictness
is asserted.

This theorem is specific to the post-C54 state. It supersedes all older Target C notes
that treated `Lambda-L_H` as an indefinite response defect in C-II.

## 3. Diagonal defect masses

Write the Kron-reduced contact response as a weighted boundary Laplacian:

$$
\Lambda_{ij}=-c_{ij}\quad(i\ne j),
\qquad c_{ij}\ge0,
\tag{C64.9}
$$

and let

$$
s_i=\sum_{j:ij\in H_+}\beta_{ij}.
\tag{C64.10}
$$

Define

$$
d_i=M_{ii}=\Lambda_{ii}-s_i.
\tag{C64.11}
$$

Theorem C64 gives

$$
\boxed{d_i\ge0,}
\tag{C64.12}
$$

and

$$
\boxed{
\sum_i d_i=\operatorname{tr}M.
}
\tag{C64.13}
$$

Since `Lambda` and `L_H` are Laplacians,

$$
\operatorname{tr}M
=2\left(\sum_{i<j}c_{ij}-\sum_{h\in H_+}\beta_h\right)
=2\left(\sum_{i<j}c_{ij}-1\right).
\tag{C64.14}
$$

Thus C41's strict inequality `sum c_ij>1` is also immediate from nonzero PSD defect,
while its geometric trace identity remains the quantitative form.

## 4. Pairwise response transport off the diameter support

If `ij` is not a positive diameter edge, then `(L_H)_{ij}=0`, so

$$
M_{ij}=-c_{ij}.
\tag{C64.15}
$$

Every `2x2` principal minor of a PSD matrix is PSD. Hence

$$
d_i d_j-M_{ij}^2\ge0,
$$

which gives:

### Corollary C64.1 (geometric-mean transport bound)

For every boundary pair outside the positive diameter support,

$$
\boxed{
c_{ij}^2\le d_i d_j,
\qquad
c_{ij}\le\sqrt{d_i d_j}
\le\frac{d_i+d_j}{2}.
}
\tag{C64.16}
$$

In particular any response pair of length strictly less than `D` satisfies C64.16,
because a positive diameter edge has length exactly `D`.

For a positive diameter edge one instead has

$$
M_{ij}=\beta_{ij}-c_{ij},
$$

so PSD gives the companion estimate

$$
\boxed{
|\beta_{ij}-c_{ij}|\le\sqrt{d_i d_j}.
}
\tag{C64.17}
$$

Thus the contact response conductance differs from the diameter conductance only by
an amount controlled by the two endpoint defect masses.

## 5. Matching and bounded-degree charging

Let `E_0` be any set of boundary pairs containing no positive diameter edge. Suppose
the graph `(B,E_0)` has maximum degree `Delta`. Summing C64.16 gives

$$
\begin{aligned}
\sum_{ij\in E_0}c_{ij}
&\le\frac12\sum_{ij\in E_0}(d_i+d_j)\\
&=\frac12\sum_i\deg_{E_0}(i)d_i\\
&\le\frac\Delta2\operatorname{tr}M.
\end{aligned}
\tag{C64.18}
$$

Hence:

### Corollary C64.2 (terminal-disjoint transport)

If `E_0` is a matching of non-diameter boundary pairs, then

$$
\boxed{
\sum_{ij\in E_0}c_{ij}
\le\frac12\operatorname{tr}M.
}
\tag{C64.19}
$$

More generally a union of `r` matchings carries total response mass at most

$$
\frac r2\operatorname{tr}M.
\tag{C64.20}
$$

This gives the missing numerical currency for terminal-disjoint response transport:
strict circular minors or disjoint short-response pairs can no longer carry arbitrary
mass while the trace defect is tiny.

The theorem does **not** give a lower bound on the conductance of any individual pair.
It therefore does not by itself turn the CR4 count of `Omega(D)` strict minors into an
absolute trace gap.

## 6. Short-response phase

C43 supplies `rho_0<1` for sufficiently large sources. Every C44 short-response pair
satisfies

$$
|b_i-b_j|\le\rho_0D<D,
$$

so it is automatically outside `H_+` and C64.16 applies.

If `E_short` is any matching of short response pairs,

$$
\boxed{
\sum_{ij\in E_{\rm short}}c_{ij}
\le\frac12\operatorname{tr}M.
}
\tag{C64.21}
$$

This is compatible with C44 Branch A, where total short response mass at least `1/2`
already gives the stronger geometric trace lower bound

$$
\operatorname{tr}M\ge\gamma_0.
$$

The new content is localization: a large amount of short response mass on disjoint
terminal pairs consumes distinct diagonal defect mass and cannot be hidden by
cancellation elsewhere in the response matrix.

## 7. Endpoint defect and support comparison

C64.17 can also be summed over a matching `J` of positive diameter edges:

$$
\sum_{ij\in J}|\beta_{ij}-c_{ij}|
\le\frac12\operatorname{tr}M.
\tag{C64.22}
$$

Thus on any pairwise terminal-disjoint subset of the positive diameter graph, the
contact-response conductances and diameter reaction weights agree in total variation
up to half of the trace defect.

This is useful in the small-trace phase. If `tr M=o(1)`, every fixed collection of
disjoint positive diameter channels is asymptotically response-matched, while every
disjoint non-diameter response channel has total mass `o(1)`.

The remaining difficulty is combinatorial/geometric: the positive diameter graph is a
convex geometric thrackle and need not itself be a matching.

## 8. Exact C-II phase sharpened by C64

The old near-minimal response frontier split remains valid, but its interpretation
changes.

### Large trace

If

$$
\operatorname{tr}M\ge\gamma
$$

for an absolute `gamma>0`, one needs to turn a fixed PSD boundary defect with affine
kernel into a packing/container contradiction.

### Small trace

If

$$
\operatorname{tr}M=o(1),
$$

then C64 gives all of the following simultaneously:

1. every non-diameter response matching has total conductance `o(1)`;
2. every bounded-degree family of non-diameter response pairs has total conductance
   `o(1)`;
3. on every diameter matching, contact-response conductance is `o(1)`-close in total
   variation to the KKT diameter weights;
4. C41 forces almost all of the response conductance mass to be geometrically
   near-diametral.

Thus the small-trace branch is an **approximate diameter-response realization** rather
than merely an indefinite affine-kernel response matrix.

## 9. New shortest response targets

C64 suggests two concrete closing routes.

### C65-A: PSD trace-gap exclusion

Prove that a nonzero PSD boundary matrix `M` with

$$
M\mathbf1=MP_B=0,
$$

arising as the response defect of a fully visible triangle-free global minimizer must
have an absolute trace lower bound that contradicts the global packing geometry, or
must vanish. If `M=0`, then `Lambda=L_H`; the equality structure can be attacked by
the C56/C58 zero-transfer machinery at maximal support.

### C65-B: disjoint-minor conductance transport

Use CR4's `Omega(D)` terminal-disjoint strict circular minors to extract a bounded-
degree family of non-diameter response pairs with aggregate conductance bounded below
by an absolute constant. C64.18 would then force an absolute trace gap, feeding Branch
A.

The known near-star response regression shows that topology alone cannot provide that
aggregate lower bound; the extra input must come from force-hull geometry, the
`Theta(D)` loaded boundary, or global minimum-diameter packing.

## 10. Binding cautions

- C64 requires the C63 fully visible branch and a relative-interior normalized KKT
  stress. It does not assert `Lambda-L_H>=0` for an arbitrary pre-C54 abstract
  response model.
- Off-diagonal response conductances may vanish after Kron reduction when boundary
  terminals themselves lie on all connecting paths; no strict positivity is used.
- PSD gives upper bounds such as C64.16, not individual lower bounds.
- A fixed positive trace defect is not yet a contradiction.
- Contact-isolated source points remain outside the force-visible core.
- The outer-shell force-bulk obstruction remains live.

## 11. Compact handoff

**LEVEL I STATUS:** still open. **C-I is closed.**

**C64:** in the fully force-visible relative-interior stress,

$$
\boxed{\Lambda-L_H\succeq0.}
$$

For diagonal defect `d_i=(Lambda-L_H)_{ii}` and every non-diameter response pair,

$$
c_{ij}\le\sqrt{d_i d_j}\le(d_i+d_j)/2.
$$

Hence a matching of non-diameter response pairs carries at most
`tr(Lambda-L_H)/2` conductance, and a degree-`Delta` family carries at most
`Delta tr(Lambda-L_H)/2`. On diameter matchings the response and diameter weights
differ in total variation by at most the same trace budget.

**Next:** use this PSD transport currency to collapse the small-trace response phase,
then attack the remaining outer-shell/large-trace branch.
