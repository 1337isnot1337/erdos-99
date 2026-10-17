> Generated reading edition · [exact source](../../research/target_c_support7_h7b_nonnegative_closure_defect_2026-09-19.md) · source SHA-256 `f5cbec81de626d6e77caaac3daf20601c24f37d98031fc2bcf1b37ffcdd3dd80`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "b1b9b4b4b394e2da111da2f800897d9282be83c0", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_h7b_nonnegative_closure_defect_2026-09-19.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "cbf8898b75b5f5b7c60ebad994fe9d8dc25c6bb2c82b5809646f2c8f6cce1de3"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — a phase-free nonnegative closure defect for the 27 generic H7b cells

**Date:** 2026-09-19  
**Scope:** generic interior-ground `H7b`, after the 27-cell full-angle reduction  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The remaining generic `H7b` problem can be written as the vanishing of one explicit nonnegative analytic function on each 27-dimensional affine cell. This removes arbitrary force-polygon phases from the numerical/certification target and packages the complete metric and local force conditions into a single zero test.

## 1. Exact scalar closure defect for five unit directions

Let five unit vectors occur in cyclic direction order, and let their consecutive angular gaps be

```math
\delta_0,\ldots,\delta_4>0,
\qquad
\sum_{k=0}^4\delta_k=2\pi.
```

After a common rotation, write

```math
\theta_0=0,
\qquad
\theta_k=\delta_0+\cdots+\delta_{k-1}
\quad(k=1,\ldots,4),
```

and

```math
S=\sum_{k=0}^4e^{i\theta_k}.
```

Expanding the squared modulus gives

```math
|S|^2
=5+2\sum_{0\le a<b\le4}\cos(\theta_b-\theta_a).
```

Among the ten unordered pairs of five cyclic directions, five are adjacent and have cosine `cos(delta_k)`. The other five are two steps apart and have cosine

```math
\cos(\delta_k+\delta_{k+1}),
```

possibly after replacing an angle by its `2pi` complement, which leaves cosine unchanged. Therefore

```math
\boxed{
C(\delta)
:=
5
+2\sum_{k=0}^4\cos\delta_k
+2\sum_{k=0}^4\cos(\delta_k+\delta_{k+1})
=|S|^2\ge0.
}
\tag{1.1}
```

Consequently

```math
\boxed{C(\delta)=0\iff S=0.}
\tag{1.2}
```

Thus one equilateral force-pentagon closes if and only if the single scalar nonnegative defect `C` vanishes. The fact that one scalar equation encodes two real closure equations is not a dimension-count paradox: `C` is a sum of two squares and its zero set is singular in the expected way.

For the normalized turn variables of the current `H7b` system,

```math
x_{i,k}=\delta_{i,k}/\pi,
```

write

```math
C_i
=
5
+2\sum_{k=0}^4\cos(\pi x_{i,k})
+2\sum_{k=0}^4\cos\!\bigl(\pi(x_{i,k}+x_{i,k+1})\bigr).
\tag{1.3}
```

Then `C_i>=0` identically and the non-ground force pentagon at vertex `i` closes exactly when `C_i=0`.

## 2. Complete metric defects

From the complete metric-integrability reduction, let

```math
A_{ij}\in(0,\pi)
```

be the affine raw triangle angle at hull vertex `i` in triangle `0ij`. For each root-fan triangle

```math
2\le i<j\le7,
```

define

```math
M_{ij}
:=
\sin A_{1i}\,\sin A_{ij}\,\sin A_{j1}
-
\sin A_{i1}\,\sin A_{ji}\,\sin A_{1j}.
\tag{2.1}
```

The fifteen equations

```math
M_{ij}=0
```

are equivalent to exactness of the complete `K7` sine-law radius cochain. Under the strict full-angle hypotheses they are sufficient for reconstruction of one common reciprocal metric, up to similarity.

## 3. One global nonnegative residual

Define on any one of the 27 surviving affine cells

```math
\boxed{
\Phi
:=
\sum_{i=1}^7 C_i
+
\sum_{2\le i<j\le7}M_{ij}^2.
}
\tag{3.1}
```

Every term in (3.1) is nonnegative, so

```math
\Phi\ge0.
```

Moreover,

```math
\Phi=0
```

if and only if all seven non-ground force pentagons close and all fifteen complete metric-cycle equations hold. By the complete metric theorem, the latter reconstruct one common reciprocal coordinate configuration realizing the full angle data. By pairwise antisymmetry of edge-force contributions, closure at the seven non-ground vertices then forces closure at the ground automatically.

Hence, within the current generic `H7b` reciprocal model,

```math
\boxed{
\text{feasibility of a surviving cell}
\iff
\text{the strict affine cell contains a zero of }\Phi.
}
\tag{3.2}
```

This equivalence is only for the generic `H7b` reciprocal branch already encoded by the full-angle system. It is not a claim about the separate wall, `H7a`, `H6`, or `H8` branches.

## 4. Why this is a better certification target

The previous formulation required simultaneously tracking:

- fourteen real pentagon vector-closure residuals, with arbitrary per-face phase choices;
- fifteen complete sine-cycle conditions;
- a separate coordinate reconstruction step;
- a separate seven-force ground closure check.

Equation (3.1) removes the phase choices and the last two items. A rigorous generic-`H7b` exclusion is now exactly the statement

```math
\inf_{z\in\mathcal P_r}\Phi(z)>0
```

for each of the 27 open affine cells `P_r`, or an equivalent proof that every zero of `Phi` lies outside the strict cell. Since the strict cells have boundary, a certification procedure must also distinguish an interior zero from sequences tending to a forbidden wall; a positive numerical minimum by itself is not a proof.

The natural next implementation is validated interval branch-and-bound on the 27-dimensional equality coordinates, using the affine inequalities for pruning and interval bounds for the cosine/sine terms in (3.1). Boundary boxes should be routed to the already-separated reciprocal-collinearity/order-wall analysis rather than silently discarded.

No theorem-state file is changed. C-II remains open.
