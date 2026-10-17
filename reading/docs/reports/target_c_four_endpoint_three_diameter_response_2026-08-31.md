> Generated reading edition · [exact source](../../../docs/reports/target_c_four_endpoint_three_diameter_response_2026-08-31.md) · source SHA-256 `994a43aeb5369400b7f8c79ef3ded64a72cf8841bc03e50fddb22578581250ef`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-0CE14B464EF7","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_four_endpoint_three_diameter_response_2026-08-31.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=a347bf528d2d6aca92fb9aebb15051ab86f2beb9; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — Target C: the four-endpoint three-diameter reduction

**Date:** 2026-08-31
**Repository state:** 43bae6e (research/target-c-next-2026-08-31), with the route-map edits recorded with this addendum
**Run type:** exact response-matrix reduction / C-I support audit
**Target:** Target C Gate C-I
**Active prompt:** docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md
**External web search:** not used for the proof
**Computation:** not used

## LEVEL I STATUS

~~~text
STILL OPEN
~~~

The response-inertia theorem C30 leaves a three-positive-diameter forest in three
endpoint regimes: four, five, or six force-hull endpoints. This addendum eliminates the
four-endpoint regime as a source of a negative response mode, and gives an exact
conditional C-I closure when the resulting three-edge stress is the full strong
diameter support.

The new reduction is

~~~text
three diameter edges on four force-hull vertices
    -> rank-one affine response defect
    -> nonnegative defect from a non-diameter hull side
    -> strict positivity in the triangle-free case
    -> rho < 1 in the C30 scalar test
~~~

## 1. Starting endpoint

Theorem C30 gives, for a normalized stress whose positive diameter endpoints span two
dimensions,

```math
\nu_-(\Omega_s)\le\operatorname{rank}L_{H_s}-2.
```

For a three-edge diameter forest, the only possible negative mode is the scalar mode
$`\rho_s-1`$, where

```math
\rho_s=\sum_{h\in H_s}\beta_hR_{\mathrm{eff}}^{C_s}(h)-2.
```

The first unresolved endpoint is therefore the case $`|H_s|=3`$ and
$`|V(H_s)|=4`$. The theorem below proves that this case has no negative mode, and
that its response defect is strictly positive in the triangle-free setting.

## 2. Strongest genuinely new audited theorem

### Theorem C31 (four-endpoint three-diameter response positivity)

Let $`A`$ be a diametrally saturated source with $`D>1`$, and let
$`s=(\alpha,\beta)`$ be a normalized KKT stress. Let $`G_s=(V_s,C_s)`$ be its
connected positive unit-contact graph, let $`H_s`$ be its positive diameter support,
and put $`B=V(H_s)`$. Assume that $`H_s`$ is a three-edge forest and

```math
|B|=4,\qquad \operatorname{aff}B\text{ is two-dimensional}.
```

Then

```math
\boxed{\Omega_s=L_{C_s}(\alpha)-L_{H_s}(\beta)\succeq0.}
\tag{C31.1}
```

If, in addition, $`A`$ is triangle-free, then

```math
\boxed{\ker\Omega_s=\operatorname{span}\{\mathbf1,x,y\},
\qquad \operatorname{rank}\Omega_s=|V_s|-3.}
\tag{C31.2}
```

Equivalently, in the C30 three-edge scalar notation,

```math
\boxed{\rho_s\le1\quad\text{in general},\qquad
\rho_s<1\quad\text{for a triangle-free source}.}
\tag{C31.3}
```

### Scope

The statement is about one actual positive KKT support of a finite diametrally
saturated source. The positive contact graph is the source network, not an independent
scaffold. The strict kernel statement uses triangle-freeness; the semidefinite
statement does not. No global-optimality assertion beyond the canonical KKT support,
diameter, and contact-separation hypotheses is hidden in (C31.1).

### Proof

Because a three-edge forest with four non-isolated endpoints is a tree, all four
points of $`B`$ are vertices of their strictly convex quadrilateral in cyclic order.
Let $`I=V_s\setminus B`$, let $`\Lambda`$ be the positive contact Dirichlet
response on $`B`$, and write

```math
M=\Lambda-L_H.
```

The force-hull response identity gives

```math
M\mathbf1=0,\qquad MP_B=0.
\tag{C31.4}
```

Since $`\mathbf1,x,y`$ are independent on a two-dimensional four-point set,
$`\operatorname{rank}M\le1`$. Let $`a\ne0`$ span the orthogonal complement of
$`\operatorname{span}\{\mathbf1,x,y\}`$. Thus

```math
M=\lambda aa^{\mathsf T}
\tag{C31.5}
```

for some scalar $`\lambda`$. The affine-dependence coefficients of a strictly convex
quadrilateral alternate in sign around its boundary, so

```math
a_i a_{i+1}<0
\tag{C31.6}
```

for every cyclically adjacent pair.

Only three of the four boundary sides can belong to the three-edge support $`H_s`$.
Choose a boundary side $`ij\notin H_s`$. A Kron reduction of a positive Laplacian
has nonpositive off-diagonal entries, so

```math
M_{ij}=\Lambda_{ij}\le0.
```

By (C31.5)--(C31.6), this forces $`\lambda\ge0`$. Therefore $`M\succeq0`$, and
the Schur congruence

```math
\Omega_s\sim_{\mathrm{cong}}
M\oplus L_{C_s}[I,I]
\tag{C31.7}
```

proves (C31.1), because the interior block is positive definite.

It remains to prove strictness of the rank-one response defect in the triangle-free
case. Suppose, for contradiction, that $`\lambda=0`$, so $`\Lambda=L_H`$.

First, no positive contact can join two points of $`B`$. A contact between a positive
diameter pair is impossible because $`D>1`$. A contact on a non-diameter pair would
make the corresponding off-diagonal entry of $`\Lambda`$ strictly negative, whereas
the same entry of the tree Laplacian $`L_H`$ is zero.

Consider a connected component $`K`$ of $`G_s[I]`$, and let $`T_K\subseteq B`$ be
the set of its boundary attachments. The inverse of the positive interior block on
K is entrywise positive. Consequently, if K attaches to two distinct terminals i and
j, its contribution to $`\Lambda_{ij}`$ is strictly negative. If $`|T_K|\ge3`$,
every pair in $`T_K`$ would therefore be an edge of $`H_s`$, contradicting that
$`H_s`$ is a tree. A one-terminal component is impossible by the harmonic maximum
principle C22: its vertices would all lie in the convex hull of one boundary point,
and hence would coincide with that point despite carrying unit contacts. Thus every
component has exactly two attachments, and those two terminals form an edge of
$`H_s`$. Conversely, every edge of $`H_s`$ must be realized by at least one such
component because $`\Lambda_{ij}=(L_H)_{ij}<0`$.

Apply the same C22 maximum principle to one such component K. Its vertices lie on the
segment joining its two terminals. Since K is connected by unit contacts and all
points are unit-separated, a path from one terminal to the other forces

```math
D\in\mathbb N,
```

and K is exactly the straight chain of points at integer positions
$`1,2,\ldots,D-1`$ between the terminals. Two different components attached to the
same terminal pair would contain two points at the same integer position and violate
unit separation. Hence the whole positive contact support is the union of three
straight unit chains, one replacing each edge of the tree $`H_s`$.

The tree has a vertex b incident with two diameter edges to, say, i and j. Let
$`\theta`$ be the angle between the rays $`bp_i`$ and $`bp_j`$. Since all source
distances are at most D,

```math
2D\sin(\theta/2)=|p_i-p_j|\le D,
\qquad\text{so}\qquad \theta\le\frac\pi3.
\tag{C31.8}
```

The first unit-chain neighbors of b on those two rays are themselves at distance
$`2\sin(\theta/2)\le1`$. Unit separation gives the reverse inequality, so equality
holds. These two neighbors and b form a unit equilateral triangle, contrary to the
triangle-free hypothesis. This contradiction proves $`\lambda>0`$.

Now $`M`$ has rank one and kernel exactly
$`\operatorname{span}\{\mathbf1,x,y\}`$. The positive interior block in (C31.7) is
positive definite. Its harmonic extension of the three boundary affine functions is
the actual coordinate field, by the interior KKT equilibrium equations. Therefore the
full stress matrix has exactly the affine kernel and rank stated in (C31.2).

Finally, C30.1 identifies the third nonzero eigenvalue of the conjugated response as
$`\rho_s`$. Semidefiniteness gives $`\rho_s\le1`$, and the absence of an additional
kernel mode in (C31.2) gives $`\rho_s<1`$. $`\square`$

## 3. Conditional C-I closure supplied by the theorem

### Corollary C31.1 (fully visible three-edge witness closes C-I)

Let A be a contact-minimal, triangle-free global minimizer with a weak unit contact.
Let $`v`$ be the strict weak-release velocity from the critical-cone theorem, and let
$`s`$ be the direction-dependent second-order KKT stress supplied by C13. Assume

```math
H_s=H_*,\qquad |H_*|=3,\qquad |V(H_*)|=4,
\tag{C31.9}
```

with $`H_*`$ a forest. Then this situation is impossible.

### Proof

Theorem C31 gives $`\Omega_s\succeq0`$ and its exact affine kernel. C13 gives
$`\operatorname{tr}(V^{\mathsf T}\Omega_sV)\le0`$, so equality holds and every
coordinate column of v lies in the affine kernel. Thus on $`V_s`$,

```math
v_i=Ap_i+t
```

for one linear map A and translation t. Let $`S=(A+A^{\mathsf T})/2`$. Since v is
critical, every positive diameter direction r satisfies

```math
r^{\mathsf T}Sr=0.
```

The three edges of a four-vertex diameter tree have three distinct projective
directions. Two edges sharing an endpoint cannot be parallel: the same ray would
repeat an endpoint and opposite rays would put two endpoints at distance $`2D`$.
Two disjoint diameter edges are crossing diagonals of the convex quadrilateral, hence
are not parallel. A nonzero planar quadratic form has at most two projective zero
directions, so $`S=0`$ and $`A=\eta J`$.

By (C31.9), this is a common angular rate on every strong diameter chord. The canonical
C7 finite-integration theorem then subtracts the common rigid rotation and produces a
nearby same-D minimizer in which every weak active row is strict, contradicting the
contact-minimal choice of A. $`\square`$

The qualification $`H_s=H_*`$ is explicit. C13 is direction-dependent and does not
assert that its stress has maximal support. If a three-edge four-endpoint source
survives outside Corollary C31.1, the remaining issue is therefore support selection,
not a hidden negative response mode.

## 4. Exact target implication

Before C31, the three-edge forest branch split as

~~~text
|V(H_s)|=4, 5, or 6
    -> one possible non-affine negative response mode.
~~~

After C31 it is

~~~text
|V(H_s)|=4
    -> Omega_s is positive semidefinite;
       it is strictly affine-kernel in the triangle-free case;
|V(H_s)|=5 or 6
    -> the one-mode response test remains open.
~~~

In particular, the scalar inequality $`\rho_s\le1`$ is proved for every relevant
three-edge forest with four endpoints, and strengthened to $`\rho_s<1`$ under the
triangle-free hypothesis. A fully diameter-visible C13 witness in this topology would
close C-I by Corollary C31.1.

## 5. Exact remaining lemma

The next shortest C-I statement is:

> **Three-edge support-selection lemma.** If $`|H_*|=3`$ and
> $`|V(H_*)|=4`$, then the C13 second-order witness for a strict weak-release
> direction can be chosen with $`H_s=H_*`$, or the zero-energy witness face has an
> integrable blocker preserving every row it supports.

The first alternative invokes Corollary C31.1. The second would extend the C25 finite
integration argument beyond its forest blocker classification. Neither alternative
is asserted here.

## 6. Audit classification of other claims

| Claim | Classification | Reason |
| --- | --- | --- |
| C31 response positivity | proved | Rank-one affine defect and a non-diameter quadrilateral side force its sign. |
| C31 strict affine kernel in the triangle-free case | proved | Zero defect forces three straight diameter chains, whose branching creates a unit equilateral triangle. |
| C31 scalar bound $`\rho_s<1`$ | proved | C30 identifies the scalar mode, and C31.2 excludes equality. |
| Corollary C31.1 | proved conditional implication | It assumes the direction-dependent stress has the full strong diameter support. |
| C-I in all three-edge cases | not proved | C13 support selection and the five/six-endpoint cases remain. |
| General KKT stress PSD | rejected | C31 is limited to a three-edge, four-endpoint response defect. |

## 7. Regression tests and binding hypotheses

| Regression | Result |
| --- | --- |
| Two-edge crossing quadrilateral | Outside the theorem; it is the C23 case. |
| Three-edge forest with five or six endpoints | Not silently included; C30 remains the active statement there. |
| Three diameter edges forming a cycle on three endpoints | Outside the forest hypothesis; it is a Reuleaux-triple-type support. |
| Zero-response chain tree without triangle-freeness | Not ruled out by the response sign alone; the forced branch angle is exactly $`\pi/3`$, explaining the strict hypothesis. |
| Uneven positive contact coefficients | Covered; only positivity of the contact Laplacian and its maximum principle are used. |
| Independent scaffold or local jammed framework | Outside scope; the response is the actual source contact network. |

The proof does not assume a lower bound on a contact stress, a Loewner comparison for
five or six endpoints, or maximal support for the direction-dependent stress.

## 8. Dependencies

- docs/reports/target_c_three_edge_response_inertia_2026-08-31.md, Theorem C30:
  Schur congruence, the affine eigenvalue count, and the scalar $`\rho_s`$ formula.
- docs/reports/target_c_force_polygon_2026-08-30.md, Theorem C11:
  the actual contact Dirichlet response and $`\Lambda P_B=L_HP_B`$.
- docs/reports/target_c_two_terminal_bridge_collapse_2026-08-31.md,
  Theorem C22: the reaction-free-domain maximum principle used on interior response
  components.
- docs/reports/target_c_critical_cone_duality_2026-08-30.md, C6--C7:
  strict weak release and common-angular-rate finite integration.
- docs/reports/target_c_second_order_variance_2026-08-30.md, Theorem C13.3:
  the direction-dependent stress with nonpositive signed second-order energy.

No external theorem or computation is used.

## 9. Canonical promotion recommendation

**Promote now.** The proof is exact under the active Target C theorem stack and removes
the four-endpoint three-diameter forest from the negative-response search.

Files to update:

- docs/targets/target-c/README.md;
- docs/targets/target-c/01-force-hull-and-shear.md;
- docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md;
- this report under docs/reports/.

## 10. Next run

Attack the five-endpoint three-edge forest, or prove the C13 support-selection lemma
in the four-endpoint case. The highest-value geometric split is whether the forest is
a two-edge path plus one disjoint diameter edge, since the response defect then has
rank at most two but the three diameter directions still constrain affine equality.

## 11. Compact handoff

~~~text
LEVEL I STATUS: STILL OPEN.

NEW C31:
If a normalized KKT stress has three positive diameter edges forming a forest on four
force-hull endpoints, then Omega_s is PSD. The response defect M=Lambda-L_H has rank at
most one; a non-diameter quadrilateral side and alternating affine-dependence signs
force its rank-one coefficient to be nonnegative.

If the source is triangle-free, M cannot vanish. Zero response would make every
reaction-free interior component a straight unit chain replacing one diameter edge;
the diameter tree then has a branching vertex, and its two first chain neighbors are
forced to make a unit equilateral triangle. Hence ker Omega_s=span{1,x,y}, rank=|V|-3,
and the C30 scalar satisfies rho_s<1.

Conditional C-I closure:
if the C13 direction-dependent second-order witness has H_s=H_* with exactly these
three edges, its nonpositive energy plus C31 forces an affine velocity. The three
diameter directions force the symmetric part to vanish, so all strong diameter chords
have one common angular rate; C7 then integrates a weak-contact release.

Remaining:
five/six-endpoint three-edge forests, or support selection for a four-endpoint C13
witness. Do not generalize C31 to arbitrary >=3 diameter supports.
~~~
