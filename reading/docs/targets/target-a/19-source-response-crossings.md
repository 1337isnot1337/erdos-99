> Generated reading edition · [exact source](../../../../docs/targets/target-a/19-source-response-crossings.md) · source SHA-256 `768774bff9eda738bb564329f4692d105fb4371615da1c915bdbc75cac7a304f`.
> [Current theorem state](../../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

# Target A — source-label crossings in the actual response graph

This audited addendum follows the plateau-response lift of Section 165 and the local
SDR regression of Section 166. It records an exact geometric rule for the overlay of
the genuine-source matching with the planar radial response graph. A proper crossing
is not merely topological: it creates an additional strict source-to-lattice conflict.
The overlay also has constant proper-crossing congestion.

**LEVEL I STATUS: STILL OPEN. TARGET A REMAINS UNRESOLVED.**

---

# 167. Crossing transport for source-labeled response linkages

Work in the Section-165 common placement with the actual plateau-terminalized optimum
`X^*`, response lattice `Lambda+v`, and genuine source `A`. Since the Target A survivor
condition is pointwise over admissible generic translates, choose the response phase
generic simultaneously for the finite sets `X^*` and `A`: no point of either set lies
on the lattice and no point-to-lattice distance is exactly one.

Let
```math
Y_{\rm in}=(\Lambda+v)\cap\operatorname{int}(K^*+\mathbb B).
\tag{167.1}
```
The straight radial drawing of the response conflict graph
```math
G\subseteq X^*\times Y_{\rm in},
\qquad xy\in E(G)\iff |x-y|<1,
\tag{167.2}
```
is plane by Corollary 79.3. Let `M_A` be any strict source matching from a subset of
`X^*` into `A`; draw its edges as straight segments. Theorem 163.1 makes these source
segments pairwise disjoint.

## 167.1 Every proper overlay crossing is another source conflict

> **Theorem 167.1 (source-response crossing transport).** Let
> ```math
> xa\in M_A,
> \qquad uy\in E(G),
> \qquad x\ne u.
> \tag{167.3}
> ```
> If the closed segments `[x,a]` and `[u,y]` intersect, then
> ```math
> \boxed{|a-y|<1.}
> \tag{167.4}
> ```
> Thus every proper crossing of a source-matching segment with a response radial edge
> is itself certified by an actual strict edge in the source-to-lattice conflict graph.

### Proof

Assume instead that `|a-y|>=1`. The two-point set `{x,u}` is unit-separated because
it lies in `X^*`, and `{a,y}` is unit-separated by the assumed inequality. The pairs
`x-a` and `u-y` have lengths strictly below one. They therefore form a strict-conflict
matching between two unit-separated two-point shores whose straight matching segments
intersect. This contradicts Theorem 163.1. $`\square`$

The condition `x!=u` is necessary: two incident edges can meet at their common left
endpoint without forcing their opposite endpoints to be a strict conflict. In the
statements below, a **proper crossing** always excludes such shared-left-endpoint
incidences.

## 167.2 Constant proper-crossing congestion

For a generic point `z`, Section 79 gives
```math
3\le |N_\Lambda(z)|\le4.
\tag{167.5}
```
For a lattice point `y`, at most five source points of `A` lie in the open unit disk
`B(y,1)`. Indeed, if six distinct unit-separated source points had radii `<1` from
`y`, two consecutive polar angles would differ by at most `pi/3`; for radii `r,s<1`
and angular separation at most `pi/3`,
```math
|a_i-a_j|^2
=r^2+s^2-2rs\cos\theta
<r^2+s^2-rs
<1,
\tag{167.6}
```
where the last strict inequality follows because the maximum of
`r^2+s^2-rs` on `0<=r,s<=1` is one and equality occurs only on the boundary with
`max(r,s)=1`. This contradicts unit separation. The response radial graph also has
lattice-side degree at most five.

> **Corollary 167.2 (bounded overlay crossings).** In the straight overlay of `M_A`
> and `G`:
>
> 1. any one source segment has at most `20` proper crossings with response edges;
> 2. any one source segment can properly cross edges belonging to at most `4`
>    pairwise vertex-disjoint response paths that do not contain its left endpoint;
> 3. any one response radial edge has proper crossings with at most `5` source
>    segments.

### Proof

If a source segment `x-a` properly crosses a response edge `u-y`, Theorem 167.1 puts
`y in N_Lambda(a)`. There are at most four possible lattice endpoints `y`, and each
has response degree at most five, proving (1).

If properly crossed response edges lie on pairwise vertex-disjoint paths, distinct
paths use distinct lattice vertices. Theorem 167.1 again maps every crossed path to a
lattice neighbor of `a`, of which there are at most four, proving (2).

For (3), if `u-y` is properly crossed by distinct source segments `x_i-a_i`,
Theorem 167.1 gives `|a_i-y|<1`. The source matching makes the `a_i` distinct, and the
source set is unit-separated. The open-unit-disk argument above permits at most five
such source points. $`\square`$

Thus the two planar structures do not create an uncontrolled quadratic crossing
pattern. Their proper-crossing overlay is a bounded-congestion planarization, with
every crossing carrying a third-shore conflict certificate.

## 167.3 Consequence for Schur/Menger linkages

Let `B` be the Section-102 `Z`-basis and orient the response graph alternately with
respect to its basis matching. A family of `k=rank S` vertex-disjoint directed paths
from `C^partial` to `O` realizes the Schur rank.

Take the source labeling from Corollary 165.4. For a labeled terminal
`c in C^partial_src`, write `a_c` for its distinct source label and
```math
\sigma_c=[c,a_c].
\tag{167.7}
```

> **Corollary 167.3 (crossing extraction on a Menger family).** If `sigma_c` meets a
> response path `P` by properly crossing an edge of `P`, then there is a right vertex
> `y in V(P) cap Y_in` with
> ```math
> \boxed{|a_c-y|<1.}
> \tag{167.8}
> ```
> Moreover `sigma_c` can properly cross at most four paths of any pairwise
> vertex-disjoint Menger family that do not contain `c`.

### Proof

Choose a properly crossed radial edge `u-y` of `P`; then `u!=c`. Theorem 167.1 gives
(167.8), and Corollary 167.2(2) gives the path-count bound. $`\square`$

This is an exact source-to-linkage transport statement on the **actual** response
network. It is compatible with the full-rank planar-response regression because it
does not infer a separator merely from planarity. It says instead that every proper
crossing of the source-label matching through a high-rank Menger linkage creates
specific additional source-lattice conflicts, with constant congestion.

## 167.4 Remaining obligation

Sections 165 and 167 now put three exact objects in one geometry:

1. all but at most `p=widehat p_H` actual Schur terminals have distinct genuine-source
   labels;
2. a Schur-rank witness is a family of pairwise vertex-disjoint directed response
   paths from those terminals to `O`;
3. every proper crossing of a source-label segment with that path family creates a
   strict source-to-right conflict, and each source segment can properly cross at most
   four paths.

What is still missing is a global cut theorem. A sufficient next statement is:

> **Source-labeled planar Menger lemma.** Use the source labels, their noncrossing
> matching, the crossing-generated source conflicts, and the global minimum-diameter
> origin of `A` to prove that every `C^partial-to-O` linkage omits at least
> `s=Delta_Lambda-d_int` terminals, or else construct an `N`-point unit-separated
> configuration of diameter `<D`.

The local two-pair regression of Section 166 remains binding: one cannot obtain this
lemma simply by assigning a distinct common lattice vertex to every source-labeled
terminal. The missing input has to be global.
