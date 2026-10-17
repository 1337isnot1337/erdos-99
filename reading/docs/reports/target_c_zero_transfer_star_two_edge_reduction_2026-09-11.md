> Generated reading edition · [exact source](../../../docs/reports/target_c_zero_transfer_star_two_edge_reduction_2026-09-11.md) · source SHA-256 `be6eb85b15591572701b8d5ba6e0a0474a469278c138e4a6653a2fc2e6ab7987`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-C0BA4B1C1CC9","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — zero transfer leaves only one- and two-edge diameter stars

**Date:** 2026-09-11  
**Repository state:** `053e1e1b85643b738b4cde306838d150ea325783`  
**Run type:** exact zero-transfer topology reduction  
**Target:** Target C, C-II  
**Status:** STILL OPEN; hold as report

This report gives a further conditional reduction of the zero-transfer branch. It
uses the report-level bridge-collapse theorem and the promoted/independently
audited mixed-support connectivity and degree bounds. It does not address the
strict-negative-transfer branch or contact-isolated source points.

## 1. Theorem

Consider a sufficiently large fully force-visible C-II source and assume

```math
K=Q^{\mathsf T}\Lambda^+Q=\operatorname{diag}(\beta_e^{-1})
\tag{1.1}
```

on the full positive diameter graph $`H`$. Assume the report-level zero-transfer
bridge-collapse statement: the nonisolated contact graph $`C`$ has one nontrivial
bridgeless block $`B_0`$, and every vertex outside $`B_0`$ is a singleton leaf
attached to it by a contact bridge. Assume also:

1. every contact bridge is crossed by at least two diameter edges;
2. every loaded contact vertex has contact degree at most three;
3. every unloaded contact vertex has contact degree at most five; and
4. the zero-transfer response separator theorem: if a component of $`H`$ is a
   star with $`k\ge3`$ edges, there is a contact vertex $`z`$ such that every
   component of $`C-z`$ contains at most one terminal of that star.

Then every connected component of $`H`$ has at most two edges. Therefore

```math
\boxed{h\le2d_H.}
\tag{1.2}
```

Combining this with the report-level diameter density

```math
\liminf h/D\ge2\rho,
\qquad \rho=\cos\rho=0.7390851332\ldots,
\tag{1.3}
```

and the report-level surplus estimate

```math
\liminf\frac{e_{BB}+2s_C-3d_H}{D}
\ge0.597+\varepsilon_{597},
\tag{1.4}
```

gives

```math
\boxed{
\liminf\frac{d_H}{D}\ge\rho,
}
\tag{1.5}
```

and

```math
\boxed{
\liminf\frac{e_{BB}+2s_C}{D}
\ge0.597+3\rho+\varepsilon_{597}
=2.8142553996\ldots+\varepsilon_{597}.
}
\tag{1.6}
```

## 2. Preliminary observation: singleton contact leaves are not diameter leaves

Let $`p`$ be a vertex outside $`B_0`$. The edge joining $`p`$ to the block is a
contact bridge whose far side is the singleton $`\{p\}`$. By the bridge-bypass
assumption, at least two diameter edges cross this cut. Every such edge has an
endpoint at $`p`$, so

```math
\deg_H(p)\ge2.
\tag{2.1}
```

Thus no singleton contact leaf can be a degree-one leaf of a diameter component.
In particular, if a diameter component is a star with at least three edges, all
of its degree-one terminals lie in $`B_0`$. Its center may be in $`B_0`$ or may
be a singleton contact leaf.

## 3. The star contradiction

Suppose a component $`T`$ of $`H`$ is a star with $`k\ge3`$ edges. Let
$`U`$ be its terminal set, so $`|U|=k+1`$. By (1.1) and the zero-transfer
response theorem, $`T`$ is indeed a star; the assumption here is only that its
size is at least three.

Let $`z`$ be the separator supplied by assumption 4. We show that no location
of $`z`$ is possible.

### 3.1 The separator is not a singleton contact leaf

If $`z\notin U`$ is outside $`B_0`$, then deleting $`z`$ leaves the connected
block $`B_0`$ and all the other singleton leaves attached to it. By Section 2,
all degree-one terminals of $`T`$ lie in $`B_0`$, so $`C-z`$ has a component
containing at least the $`k`$ leaves of $`T`$, contradicting the separator
property.

If $`z\in U`$ is the star center and is outside $`B_0`$, then the same argument
leaves all $`k`$ degree-one terminals in the connected block $`B_0`$, again a
contradiction. A degree-one terminal cannot be outside $`B_0`$ by (2.1).

Consequently either the separator is in $`B_0`$, or it is a star center outside
$`B_0`$, and the latter case has already been ruled out. Hence

```math
z\in B_0.
\tag{3.1}
```

### 3.2 Components of $`B_0-z`$ cost two contact edges each

Every component $`W`$ of $`B_0-z`$ that is nonempty has at least two contact
edges to $`z`$. Otherwise its unique edge to $`z`$ would be a bridge of
$`B_0`$, contrary to the definition of the nontrivial bridgeless block.

If $`z`$ is not a terminal of $`T`$, all $`k+1`$ terminals lie in $`B_0`$,
except possibly the star center if it is a singleton leaf. In the latter case
there are still $`k`$ degree-one terminals in $`B_0`$. The separator property
requires distinct components of $`B_0-z`$ for these terminals. Their contact
edges to $`z`$ therefore number at least $`2k`$, which is at least six. This
contradicts degree at most five if $`z`$ is unloaded, and contradicts degree at
most three if $`z`$ is loaded.

If $`z`$ is a degree-one terminal of $`T`$, it is loaded and has contact degree
at most three. If the star center lies in $`B_0`$, the remaining $`k`$ terminals
lie in distinct components of $`B_0-z`$, requiring at least $`2k\ge6`$ incident
contact edges. If the star center is the one possible singleton contact leaf,
then the remaining $`k-1`$ degree-one terminals lie in distinct components of
$`B_0-z`$, requiring at least $`2(k-1)\ge4`$ incident contact edges. Both
contradict the loaded degree bound three.

If $`z`$ is the center and lies in $`B_0`$, the remaining $`k`$ leaves lie in
distinct components of $`B_0-z`$, so the same lower bound $`2k\ge6`$ applies;
the center is loaded and has contact degree at most three.

All cases contradict the degree bounds. Therefore no star component of $`H`$
can have $`k\ge3`$. Since the zero-transfer theorem already says every
component is a star, every component has at most two edges, proving (1.2).
$`\square`$

## 4. Quantitative consequence

From (1.2),

```math
d_H\ge h/2.
```

Using (1.3) gives (1.5). Put

```math
\nu_D=\frac{e_{BB}+2s_C-3d_H}{D}.
```

Then

```math
\frac{e_{BB}+2s_C}{D}=\nu_D+3\frac{d_H}{D}.
```

Substitute (1.4) and (1.5) to obtain (1.6). $`\square`$

## 5. What remains

This is a real reduction of the zero-transfer branch, but it is not a closure.
Two-edge diameter stars remain possible. Their zero-transfer separator can be a
degree-four unloaded articulation of the bridgeless block, which is allowed by
the current degree bounds. The high-surplus lower bound (1.6) has no opposing
global upper bound in the promoted stack.

The strict-negative alternative $`\min K_{ef}<0`$ is untouched. The proof also
does not bound contact-isolated source points, which are outside $`C`$ and may
remain a quadratic population.

## 6. Regression audit

- **Singleton loaded contact leaves:** allowed only as diameter degree at least
  two; this is why they cannot be degree-one terminals of a large star.
- **A bridgeless block with cut vertices:** retained. The proof uses only two
  incident edges per component after deleting the separator; it does not assume
  vertex 2-connectivity.
- **Two-edge stars:** retained as the exact surviving zero-transfer topology.
- **Matching components:** retained; the separate matching exclusion is not used.
- **Regular odd shells:** not claimed to satisfy the zero-transfer hypotheses.
- **Contact-isolated sources:** retained and not charged.

## 7. Classification

| Claim | Status |
|---|---|
| zero-transfer components are stars | report-level proved |
| singleton contact leaves have $`H`$-degree at least two | proved from bridge bypass |
| zero-transfer star size at most two | proved conditional on listed inputs |
| $`d_H/D\ge\rho`$ in zero transfer | proved conditional on listed inputs |
| ordinary surplus floor $`2.8142554D+o(D)`$ | proved conditional on listed inputs |
| C-II / Level I | not proved |

**Promotion recommendation:** hold as an unpromoted addendum until the bridge
collapse and zero-transfer separator dependencies receive the repository's
required independent audit.
