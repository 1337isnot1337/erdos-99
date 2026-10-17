> Generated reading edition · [exact source](../../../docs/reports/target_c_secondary_diameter_visibility_2026-08-31.md) · source SHA-256 `0cde62af4f70318817c7cd44ac661fbaabe71bbdc1e51d6289cd11ae00e3a21f`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-1448A484DA71","canonical":false,"claim_ids":["C-SECONDARY-DIAMETER-VISIBILITY"],"claim_statuses":{"C-SECONDARY-DIAMETER-VISIBILITY":"superseded"},"index":"docs/state/artifact-index.jsonl","status":"superseded","target":"target-c"} -->
# Erdős Problem #99 — Target C: secondary normalization makes every diameter pair force-visible

**Date:** 2026-08-31  
**Repository base:** `a2d5cc7d` (main after C64 / PR #67)  
**Run type:** exact secondary-normalization corollary of C63  
**Target:** Target C Gate C-II  
**Depends on:** C6 strong/weak active-row duality, C63 Newton–Hoffman critical-cone integrability, Gate C-I closure

**Lifecycle correction (2026-10-10):** The full-support normalization `C=C_*`,
`H=H_*` and the strict `(1,D)` slack of contact-isolated source points are
mathematically valid but already contained in canonical
[`56-ci-restored-frontier.md`](../targets/target-c/56-ci-restored-frontier.md)
and [`57-zr-zf-rigidity-audit.md`](../targets/target-c/57-zr-zf-rigidity-audit.md).
This report is retained for provenance and is superseded as a separate theorem
source. It adds no separate canonical theorem. Its proposed frontier summary is not
the current C-II obligation; see [`CURRENT.md`](../targets/target-c/CURRENT.md).

## LEVEL I STATUS

**STILL OPEN.**

Gate C-I proves that, in a contact-minimal triangle-free global minimizer, every unit contact is strong. The same nonlinear integration theorem gives a second exact normalization.

Among all contact-minimal triangle-free global minimizers, choose one with the minimum number of diameter pairs. Then every diameter pair is strong:

```math
\boxed{H=H_*.}
```

Thus one relative-interior normalized KKT stress is positive on the entire contact graph and the entire actual diameter graph. Every actual diameter endpoint belongs to the positive contact core. Every source point outside that core is a fully inactive rattler whose distance from every other source point is strictly between `1` and `D`.

## 1. Lexicographic source choice

Assume a triangle-free global minimizer exists for the cardinality under consideration. Choose a source `A` lexicographically as follows:

1. minimize the number of unit contacts;
2. among those sources, minimize the number of diameter pairs.

The first coordinate is exactly the contact-minimal normalization used by Target C. By C63,

```math
C=C_*.
\tag{C65.1}
```

The second coordinate is a finite nonnegative integer and therefore attains a minimum.

## 2. A weak diameter pair contradicts the secondary minimum

Suppose

```math
H\setminus H_*\ne\varnothing.
\tag{C65.2}
```

C6 gives a relative-interior critical velocity

```math
v\in\operatorname{ri}\mathcal K_D(A)
```

such that every strong active row has zero signed first variation and every weak active row has strict feasible first variation.

Because C=C_*, there are no weak unit-contact rows. Hence every weak row is a diameter row, and its strict feasible derivative means that diameter pair shortens to first order.

Apply C63, Theorem C63, to this `v`. For every sufficiently small positive parameter it gives an actual displacement

```math
x(t)=tv+O(t^2)
```

such that all strong active rows remain feasible. C63 also proves that every weak active row remains strict and every initially inactive row retains strict slack. Therefore the resulting real configuration `A(t)` satisfies

```math
C(A(t))\subseteq C_*=C(A),
\tag{C65.3}
```

and

```math
H(A(t))\subseteq H_*\subsetneq H(A).
\tag{C65.4}
```

It is unit-separated and has diameter at most `D`; global minimality of `D=D(n)` forces its diameter to equal `D`.

If (C65.3) were strict, `A(t)` would be a triangle-free global minimizer with fewer unit contacts than the primary normalization. Hence

```math
C(A(t))=C(A).
\tag{C65.5}
```

But (C65.4) is strict, so `A(t)` belongs to the same minimum-contact class and has fewer diameter pairs, contradicting the secondary normalization.

Thus:

### Theorem C65 — full diameter visibility

For the lexicographically normalized source,

```math
\boxed{C=C_*,\qquad H=H_*.}
\tag{C65.6}
```

Equivalently, a relative-interior point of the normalized KKT polytope can be chosen with

```math
\boxed{
\alpha_e>0\quad(e\in C),
\qquad
\beta_h>0\quad(h\in H).
}
\tag{C65.7}
```

So the selected positive diameter graph used by the C-II response machinery can be taken to be the **entire actual diameter graph of the source**.

## 3. Contact-isolated points are fully inactive

The canonical positive-support connectivity theorem says every endpoint of a positive diameter edge belongs to the unique nontrivial positive contact component. By C65 every actual diameter edge is positive.

Hence a contact-isolated source point `x` cannot be incident to any diameter pair. Therefore, for every `j!=x`,

```math
\boxed{1<|x-p_j|<D.}
\tag{C65.8}
```

The lower inequality is contact-isolation. The upper inequality follows because equality would make `xj` an actual diameter pair and force `x` into the positive contact core.

Thus every source point outside the force-visible core is strict for both distance bounds. There are no hidden weak diameter endpoints outside the response network.

## 4. Full actual diameter boundary

Every actual diameter endpoint is now loaded. Conversely every loaded KKT boundary vertex is, by definition, incident to a diameter edge. Hence

```math
\boxed{B_+=V(H).}
\tag{C65.9}
```

All existing boundary-count, circular-planar response, and diameter-thrackle statements therefore apply to the source's complete diameter graph, not merely to a selected subgraph.

In particular C30 gives

```math
2|V(H)|\ge \lceil D\rceil+2.
\tag{C65.10}
```

## 5. Exact effect on Gate C-II

After C65 a hypothetical counterexample may be assumed simultaneously to have:

- every unit contact positive in one relative-interior KKT stress;
- every actual diameter pair positive in the same stress;
- the positive contact graph equal to the entire nonisolated active core;
- the response boundary equal to the complete diameter-endpoint set;
- every source point outside the core completely inactive, with all distances in `(1,D)`.

Thus all active geometry is force-visible. The remaining force-bulk issue concerns only fully inactive rattlers.

## 6. Scope

C65 is a normalization of a hypothetical counterexample; it does not assert that every triangle-free global minimizer has `H=H_*`. This is sufficient for contradiction: if any counterexample exists, the finite lexicographic choice above produces one with C65.6.

## 7. Compact handoff

**LEVEL I STATUS:** still open.

**C65:** minimize contacts, then diameter pairs. Gate C-I gives `C=C_*`. If a weak diameter remained, C6 supplies a relative-interior velocity shortening it, and C63 integrates that velocity while preserving all strong rows and keeping every weak row strict. Primary contact minimality prevents loss of contacts, so the new minimizer has the same contact count and fewer diameter pairs, contradiction.

**Conclusion:** `H=H_*`. The full actual diameter graph is KKT-visible, and every non-core source point is a fully inactive rattler.

**Next:** use classical diameter-graph structure and/or eliminate the fully inactive rattler population.
