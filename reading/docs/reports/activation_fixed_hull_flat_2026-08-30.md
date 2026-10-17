> Generated reading edition · [exact source](../../../docs/reports/activation_fixed_hull_flat_2026-08-30.md) · source SHA-256 `8f542597f1da1c8f4620b93f9c25f1cc7a121c4ff71c5b158660268b4102109e`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "9aa2a2eb18dfed14338f2886b089495e39dc6848", "source_canonical": false, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "unreviewed", "source_path": "docs/reports/activation_fixed_hull_flat_2026-08-30.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "bafe7c3de755792b8c6d1d35c5c9d160d15cbe6f6d50a299ea4367ed4e5202a4"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle was `unreviewed`; it is retained as provenance only. Destination status remains unreviewed/noncanonical.

# Erdős Problem #99 — fixed-hull activation flat and backbone Hall obstruction

**Date:** 2026-08-30
**Repository state:** `origin/main` at `bd5c534`; work branch
`research/activation-flat-2026-08-30` (merged with the promoted Section 157 rate)
**Run type:** closing proof / audit / promotion
**Target:** A
**Active prompt:** `docs/prompts/erdos_problem_99_1.7.5_FINAL_CONTINUATION_PROMPT.md`
**External web search:** used only to recheck the Kuperberg gap-defect proof
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

## 1. Starting endpoint

The exact Target A endpoint was

```math
\dim\ker S\ge s,
\qquad
s=\Delta_\Lambda-d_{\rm int},
\tag{R1.1}
```

equivalently

```math
\operatorname{rank}S
\le d_{\rm int}+|C^\partial|-\Delta_\Lambda.
\tag{R1.2}
```

The attempted implication chain was

```text
monotone source activation
-> finite same-hull global-optimum directions beyond KKT stress
-> source/capacity transition control
-> Schur nullity or strict smaller-diameter replacement.
```

This run proves the first two arrows and an exact transition localization. Combined
with the concurrently promoted Sections 154–155, it also gives a coembedded
source/scaffold affine family in the very-super-boundary subbranch. It does not prove
the final two-shadow/backbone compatibility.

## 2. Strongest genuinely new audited theorem

### Theorem

Run the canonical monotone activation sequence

```math
A_0,A_1,\ldots,A_\ell
```

from a triangle-free global minimizer of cardinality $`n`$ and diameter
$`D=D(n)>1`$. Let $`r_i`$ be the strict point moved at step $`i`$, and let
$`e_i=r_iq_i`$ be the unique unit or diameter pair created at that step. Put

```math
E_{\rm new}=\{e_1,\ldots,e_\ell\},
\qquad
M=\{r_1,\ldots,r_\ell\}.
```

Let $`A^*=A_\ell`$, $`H^*=\operatorname{conv}A^*`$,
$`b=|M\cap\partial H^*|`$, and let $`d_D`$ be the number of diameter
activations. Then:

1. $`E_{\rm new}`$ is a forest, every one of its edges is a bridge in the full
   terminal active graph, and
   $`\operatorname{rank}R_{E_{\rm new}}=\ell`$.
2. There is a linear space $`\mathcal L_{\rm act}`$ and a neighborhood of zero
   in it whose vectors give triangle-free global minimizers inside the fixed hull
   $`H^*`$ by direct affine displacement.
3. Its dimension obeys
   ```math
   \boxed{
   \dim\mathcal L_{\rm act}
   \ge\max\{0,\ell-2b+d_D\}.
   }
   \tag{R2.1}
   
   ```
4. If $`R_0`$ is a specified set of $`r_0`$ initial strict rattlers, then
   ```math
   \boxed{
   \dim\mathcal L_{\rm act}
   \ge
   \max\left\{0,
   \left\lceil\frac{r_0}{2}\right\rceil
   -2\lfloor\pi D\rfloor
   \right\}.
   }
   \tag{R2.2}
   
   ```

After the Section 121 maximal triangle-free extension, one may take
$`r_0=|R_B|\ge\rho-5\widehat p_H`$. Thus the activated terminal
representative has a fixed-terminal-hull affine family of dimension at least

```math
\max\left\{0,
\left\lceil
\frac{\max\{0,\rho-5\widehat p_H\}}2
\right\rceil
-2\lfloor\pi D\rfloor
\right\}.
\tag{R2.3}
```

### Scope

This is an exact theorem about the actual global-minimizer activation sequence. Its
family is finite-amplitude, triangle-free, and contained in the terminal activated
hull. That hull need not equal the original source hull in general. Corollary 156.3
below gives an exact composition with the independently constructed smaller optimum
and prescribed-phase inner scaffold under the Section 155 threshold.

### Proof

Immediately before step $`i`$, the creator $`r_i`$ is strict, hence isolated in
the current active graph. Adding $`e_i`$ therefore attaches an isolated vertex by
one edge. Persistence of every active pair makes $`r_i`$ permanently non-strict, so
the creators are distinct. If $`q_i`$ is itself a creator, it must have been moved
earlier: if it were still strict, $`e_i`$ would make it non-strict and prevent a
later move. Thus the creation order orients every created edge from a new isolated
vertex toward an earlier or never-moved vertex.

Inductively, adding an edge at an isolated endpoint creates no cycle and cannot later
be placed on a cycle, because every later edge again has a new isolated endpoint.
Hence $`E_{\rm new}`$ is a forest and every created edge remains a bridge in the
full terminal active graph. Leaf elimination in the rigidity matrix proves that the
$`\ell`$ nonzero forest rows are independent.

Let

```math
I=M\cap\operatorname{int}H^*.
```

Define $`\mathcal L_{\rm act}`$ to consist of velocity fields supported on $`I`$
and satisfying

```math
(p_x-p_y)\cdot(v_x-v_y)=0
\tag{R2.4}
```

for every created unit pair $`xy`$. There are $`2(\ell-b)`$ variables and at
most $`\ell-d_D`$ equations. This proves (R2.1).

Every endpoint of a diameter pair lies on $`\partial H^*`$. Thus all created
diameter pairs are fixed by these velocities. Every old active pair is also fixed:
no creator can have been incident to an old active pair, because old pairs persist
and would have prevented it from being strict when moved.

For a created unit pair and any $`v\in\mathcal L_{\rm act}`$,

```math
\begin{aligned}
|(p_x+v_x)-(p_y+v_y)|^2
&=1+2(p_x-p_y)\cdot(v_x-v_y)+|v_x-v_y|^2\\
&=1+|v_x-v_y|^2\ge1.
\end{aligned}
\tag{R2.5}
```

Every nonactive pair has terminal distance strictly between $`1`$ and $`D`$, so
all its inequalities persist for sufficiently small velocities. Every moved point in
$`I`$ has positive distance from $`\partial H^*`$, so a common sufficiently small
neighborhood stays in $`H^*`$. An old fixed diameter pair retains length $`D`$.
The perturbed set is therefore unit-separated, has diameter exactly $`D=D(n)`$,
and is another global minimizer. Its contact graph is a subgraph of the terminal
triangle-free contact graph, so it remains triangle-free.

If $`h=|A^*\cap\partial H^*|`$, the boundary arcs between cyclically consecutive
points have length at least one. Hence

```math
b\le h\le\operatorname{per}(H^*)\le\pi D,
\tag{R2.6}
```

and therefore $`b\le\lfloor\pi D\rfloor`$.

At termination every point of a specified initial strict set $`R_0`$ is incident to
a created pair. One pair covers at most two members of $`R_0`$, so
$`\ell\ge\lceil r_0/2\rceil`$. Equations (R2.1) and (R2.6) give
(R2.2), and the canonical retained-rattler estimate gives (R2.3). $`\square`$

### Coembedded Section 155 subbranch

Because the terminal activated representative is itself a global minimizer with the
same cardinality and diameter, the Bonnesen alignment theorem of Section 155 applies
to its hull. Under the Section 155 threshold, the smaller optimum, its unit collar,
and the prescribed-phase inner scaffold all lie in that terminal hull. Every terminal
hull vertex is frozen by the affine construction, so the hull remains fixed throughout
the family. The exact fixed-source Hall theorem consequently gives, uniformly over
the family,

```math
\nu(X_m,A^*(v))\ge m-\widehat p_{H^*},
\qquad
\nu(Y_{\rm in},A^*(v))\ge |Y_{\rm in}|-\widehat p_{H^*}.
\tag{R2.7}
```

This is the coembedded affine two-shadow family of Corollary 156.3 in the canonical
module. It is not a claim that the two matchings use the same source labels.

### Fixed-basis transition corollary

Rebuild the capacity endpoint and fixed-basis flag in $`H^*`$. On a relatively open
chamber of $`\mathcal L_{\rm act}`$ where the strict conflict graph is constant,
all exchanged configurations remain same-hull global optima. If every configuration
at one fixed transition contains a unit triangle, then one fixed labeled triangle
persists throughout the chamber. It either lies entirely among inserted capacity
points, or every retained source vertex in it is fixed by all of
$`\mathcal L_{\rm act}`$.

Indeed, finitely many algebraic triangle loci cover the chamber, so one has relative
interior and its distance polynomials vanish identically. If a persistent triangle
contains a source vertex $`x`$ and an inserted fixed vertex $`z`$, then for every
direction $`w\in\mathcal L_{\rm act}`$,

```math
|p_x+v_x+t w_x-z|^2=1
```

for small $`t`$. Its quadratic coefficient is $`|w_x|^2`$, forcing
$`w_x=0`$. This applies to every retained source vertex in the triangle.

### Dependencies

- `docs/targets/target-a/03-source-response.md`, Theorem 142.1 and Sections 143–145;
- `docs/theory/01-local-structure.md`, the diameter-endpoint boundary fact;
- the retained-rattler bound from Section 121;
- Cauchy's perimeter-diameter inequality, already canonical.

### Why it is new

Section 144 recorded only selected first unit contacts and explicitly allowed those
edges to become non-bridges later. The creation-order argument shows that limitation
is false for the monotone sequence: every later pair also attaches an isolated point.
Section 145 extracted rank, and Section 153 proved universal zero KKT weight, but
neither constructed the fixed-hull affine family (R2.5) or its exact dimension.

## 3. Exact target implication

The result converts a super-boundary strict-rattler population into a
super-boundary-dimensional affine family of genuine, triangle-free global minimizers
inside one fixed terminal hull. In the Section 155 regime it coembeds the smaller
optimum and inner scaffold, and it reduces any universally triangle-producing
fixed-basis transition to inserted points and source labels frozen by that family.

It does **not** change $`\zeta=\dim\ker S`$ directly. The exact endpoint remains
(R1.1). The new source quantities available for transport are
$`\mathcal L_{\rm act}`$, the two uniform Hall shadows (R2.7), and the captured
rattler set in the Section 157 backbone witness.

## 4. Exact remaining lemma

The missing statement is a global activation-flat/two-shadow transport theorem:

> In the Section 155 common placement, use the uniform Hall shadows over
> $`\mathcal L_{\rm act}`$, the Section 157 backbone witness, and its captured
> strict rattlers to induce at least $`s=\Delta_\Lambda-d_{\rm int}`$ independent
> boundary-response null directions, or produce an $`N`$-point unit-separated
> configuration of diameter strictly below $`D`$. Outside that subbranch, the
> missing source/scaffold coordinate transport must be supplied first.

Local incidence cannot prove this statement; the construction must use the genuine
global relation between the source and the independently chosen smaller optimum.

In the Section 155 common placement, Proposition 157.3 adds the exact graft
inequality
```math
|Q|-|N_A(Q)\cup C|\le-1
```
for every source diameter cover $`C`$. Hence a backbone-maximizing witness of
deficiency $`h`$ captures at least $`h-|C|+1`$ strict rattlers; with a minimum cover
and $`h\ge\tau_D(A)`$, at least one rattler is forced. This remains a source-side
statement and supplies no response-kernel map.

## 5. Audit classification of other claims

| Claim | Classification | Reason |
| --- | --- | --- |
| Every activation-created pair remains a bridge | proved | Each is added at a currently isolated creator; later edges have the same form. |
| All created activation rows are independent | proved | The complete created set is a forest, so leaf elimination applies. |
| The terminal representative has a same-hull affine global-optimum family | proved | Orthogonality removes the linear term and the quadratic term has the feasible sign. |
| The affine family maps canonically into $`\ker S`$ | unproved | Even in the Section 155 common placement, the two Hall shadows and the response have no proved compatible composition. |
| A large affine family automatically breaks the first transition | rejected as stated | A triangle may lie entirely on inserted/frozen support. |
| Kuperberg supplies a quantitative support-radius rate | not imported | The checked proof remains qualitative in the small-gap parameter. |
| Section 157 backbone deficiency gives a Target A contradiction | conditional only | Its strict-rattler capture is exactly the capacity slack mechanism, not a Schur certificate. |
| Section 157.3 graft inequality closes the target | rejected | It forces rattler capture in the aligned subbranch but still gives no scaffold-response transport. |

## 6. Regression tests

| Regression | Passed? | Exact reason |
| --- | --- | --- |
| Section 152 activation/monomer family | yes | It has the attachment geometry but is not globally minimum-diameter; it still forbids a local flat-to-Schur theorem. |
| Section 153 universal zero KKT load | yes | The affine family is consistent with, and explains, the zero multipliers. |
| Long straight activation chain | yes | Orthogonal linear displacement increases active unit lengths by a quadratic square. |
| Exact two-leaf cage | yes | The cage may be supported on affine-frozen and inserted vertices. |
| Full-rank planar response | yes | No source-to-response identification is claimed. |
| Overlapping circuits / annular full linkage | yes | The theorem changes source geometry only and asserts no separator from planarity. |
| Distributed strained monomer | yes | The theorem neither creates a density gap nor claims local incidence forces nullity. |

## 7. Failed routes and no-go results

The fixed-hull affine family does not alone produce an extra point in its hull; exact
finite capacity still bounds every replacement. Nor does high affine dimension force
a triangle-producing exchange to use a mobile source label. The persistent-triangle
corollary isolates the exact failure: the obstruction can live wholly on inserted
capacity points and labels frozen by the family. Section 157 improves the aligned
subbranch by forcing the backbone witness to touch enough rattlers, but does not yet
turn those captured rattlers into compatible scaffold replacements.

## 8. Literature imported

No external theorem is used in the new proof. The Kuperberg--Kuperberg--Kuperberg
gap-defect paper ([arXiv:math/0303366](https://arxiv.org/abs/math/0303366)) was
rechecked at theorem/proof level. Its planar proof chooses a
positive widening for each fixed gap and then a sufficiently large block for repeated
widening; it does not state an asymptotic lower bound on the widening or an upper bound
on witness support as the initial gap tends to zero. The canonical Section 150 scope
warning remains correct.

## 9. Computation and reproducibility

No computation was used. The new claims are finite graph, linear-algebra, and exact
Euclidean identities.

## 10. Canonical promotion recommendation

**Promote now.** Add Target A Section 156 as a new audited module; the route map and
active prompt already include the concurrent Sections 154–155 and 157. Mark the old
non-bridge limitation as superseded through Section 156 rather than rewriting the
historical Sections 111–145. Add this report to the current reports index.

## 11. Next run

Prove the global two-shadow/backbone compatibility theorem: in the Section 155 common
placement, combine the Section 156 affine family and Section 157 captured-rattler
witness with the co-phased inner scaffold to force the exact Schur nullity. A theorem
using only local activation incidence is excluded by Section 152.

## 12. Compact handoff

```text
LEVEL I STATUS: STILL OPEN

Strongest new theorem:
All pairs created by monotone activation form a bridge forest. The terminal activated
global minimizer has a fixed-hull affine family of triangle-free global minimizers of
dimension at least ell - 2b + d_D, hence at least
ceil(|R_0|/2) - 2 floor(pi D).

Exact endpoint now:
Still dim ker S >= Delta_Lambda - d_int. The new source object available for transport
is the super-boundary-dimensional fixed-hull space L_act.

Binding regressions/no-go results:
Sections 152 and 153 remain binding; two-leaf cages and full-rank planar responses can
live on support frozen by L_act.

Highest-value next lemma:
Transport frozen first-transition support into s independent boundary alternating
nonlinkages, or turn it into a strict smaller-diameter source replacement.

Authoritative files:
docs/targets/target-a/README.md
docs/targets/target-a/09-activation-fixed-hull-flat.md
```
