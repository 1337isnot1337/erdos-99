> Generated reading edition · [exact source](../../../docs/reports/near_extremal_activation_monomer_regression_2026-08-30.md) · source SHA-256 `a2be769d611d5cad27b98bde010371e26c448e8356624094baf187ffd9a4224c`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "fd54d3d528e314324bd036b36848f770a4c17420", "source_canonical": false, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "unreviewed", "source_path": "docs/reports/near_extremal_activation_monomer_regression_2026-08-30.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "cabd91445a431a35b35c9d0f26fb5ca9187ae9a16260f46729f607635eb0902e"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle was `unreviewed`; it is retained as provenance only. Destination status remains unreviewed/noncanonical.

# Erdős Problem #99 — near-extremal activation/monomer regression

**Date:** 2026-08-30
**Repository state:** `research/bhs-scale-activation-regression-2026-08-30`, based on `82a4348577f01011cbba056a169b5a8ac9d11cd2`
**Run type:** audit / exact regression
**Target:** A
**Active prompt:** `docs/prompts/erdos_problem_99_1.7.2_FINAL_CONTINUATION_PROMPT.md`
**External web search:** used only to recheck the quantitative-gap route; no external theorem is imported below
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

The result below is an exact regression. It is not a counterexample to Erdős Problem #99 because the constructed configurations are not proved to be global minimum-diameter configurations.

## 1. Starting endpoint

The authoritative Target A endpoint is

```math
\boxed{\dim\ker S\ge \Delta_\Lambda-d_{\rm int}},
```

or equivalently

```math
\boxed{\operatorname{rank}S\le d_{\rm int}+|C^\partial|-\Delta_\Lambda.}
```

Section 152 already proves that quadratic activation rigidity rank, a fixed diameter pair, planarity, and coherent neutral monomer incidence do not force positive scaffold nullity. Its explicit patch has diameter `D=8L`, so it deliberately does not model the sharp scalar cardinality/diameter regime.

This run tests the stronger possible implication

```text
near-extremal scalar geometry
+ almost-full persistent activation rank
+ coherent monomer incidence
-> positive scaffold/Schur nullity.
```

The implication is false without exact global minimum-diameter information.

## 2. Strongest genuinely new audited theorem

### Theorem 153 candidate: near-extremal activation/monomer compatibility regression

Let

```math
e_1=(1,0),\qquad e_2=\left(\frac12,\frac{\sqrt3}{2}\right),
\qquad \Lambda=\mathbb Ze_1+\mathbb Ze_2,
```

and put

```math
b=\frac{e_1+e_2}{3},\qquad
a_0=\frac{\sqrt3}{2},\qquad
c=\frac{2\sqrt3}{\pi}.
```

For every integer $`L\ge10`$, there is a finite triangle-free unit-separated configuration $`A_L`$, together with a one-point-at-a-time activation sequence ending at $`A_L`$, with the following properties.

1. The two fixed anchors
   
   ```math
   a_\pm=\pm L(0,1)
   ```

   are the unique diameter pair throughout the activation sequence, so
   
   ```math
   \boxed{D_L=\operatorname{diam}A_L=2L.}
   ```


2. If $`n_L=|A_L|`$, then
   
   ```math
   \boxed{
   \left|n_L-\frac{D_L^2}{c}\right|\le4D_L.
   }
   \tag{153.1}
   ```

   Thus the construction lies at the sharp translated-triangular-lattice bulk scale up to boundary order.

3. If $`H_L=\operatorname{conv}A_L`$ and $`P_L=\operatorname{per}H_L`$, then
   
   ```math
   \boxed{B_{L-3}\subset H_L,}
   \tag{153.2}
   ```

   and hence
   
   ```math
   \boxed{0\le \pi D_L-P_L\le6\pi.}
   \tag{153.3}
   ```

   In particular the perimeter deficit is bounded independently of $`L`$.

4. Every activation move acts on a currently strict patch point, creates exactly one new unit contact, and preserves every earlier contact. The final activation edges form disjoint row paths. If $`R_L`$ is their bar-rigidity matrix, then
   
   ```math
   \boxed{
   \operatorname{rank}R_L
   \ge n_L-\frac{2}{\sqrt3}D_L-22
   =n_L-O(D_L).
   }
   \tag{153.4}
   ```


5. Relative to the unstrained triangular lattice, every patch point has exactly three strict conflict neighbors, namely the vertices of one elementary lattice triangle, throughout the sequence. The assignment to the lower-left lattice vertex is an injective matching saturating the entire patch shore. Consequently the corresponding patch monomer/transversal left nullity is exactly zero.

Therefore even the conjunction

```math
\boxed{
\begin{array}{c}
 n=D^2/c+O(D),\\
 \pi D-P=O(1),\\
 \operatorname{rank}R_{\rm act}=n-O(D),\\
 \text{persistent one-at-a-time activation},\\
 \text{fixed diameter pair},\\
 \text{coherent exact monomer incidence}
\end{array}
\not\Longrightarrow
\text{positive scaffold/Schur nullity}
}
\tag{153.5}
```

without an additional exact global hypothesis.

### Scope

The theorem concerns arbitrary finite feasible configurations, not global minimizers. It supplies exact finite geometry and exact incidence/rank statements. It does not assert saturation, plateau terminality, or any relation to an independently chosen smaller optimum.

### Proof

Put

```math
s_L=L-L^{-1},\qquad \varepsilon_L=L^{-4},
```

and define the raw shifted-lattice patch

```math
Q_L^{\rm raw}=(b+\Lambda)\cap B_{s_L}(0).
\tag{153.6}
```

Delete only points in a tiny neighborhood of the two anchors:

```math
E_L=
\left\{
q\in Q_L^{\rm raw}:
\min\{|q-a_-|,|q-a_+|\}\le1+L^{-2}
\right\},
\qquad
Q_L=Q_L^{\rm raw}\setminus E_L.
\tag{153.7}
```

Every $`q\in b+\Lambda`$ is uniquely

```math
q=b+ie_1+je_2.
```

Replace it by the slightly row-strained point

```math
p_{ij}=b+ie_1+(1+\varepsilon_L)je_2.
\tag{153.8}
```

Let $`P_L^*`$ be the set of these points for $`q\in Q_L`$, and set

```math
A_L=P_L^*\cup\{a_-,a_+\}.
\tag{153.9}
```

#### 2.1 The anchor deletion costs only a constant

The points of $`b+\Lambda`$ are mutually at least unit-separated. Around every raw point deleted near one anchor place the closed disk of radius $`1/2`$. These disks have disjoint interiors and lie in a disk of radius

```math
1+L^{-2}+\frac12\le1.51.
```

Therefore the number deleted near one anchor is at most

```math
\left\lfloor\frac{\pi(1.51)^2}{\pi(1/2)^2}\right\rfloor
=9.
```

Thus

```math
\boxed{|E_L|\le18.}
\tag{153.10}
```

#### 2.2 Perturbation size

The vertical coordinate of $`q=b+ie_1+je_2`$ is

```math
\frac{\sqrt3}{2}\left(j+\frac13\right).
```

Since $`|q|\le s_L<L`$,

```math
|j|\le\frac{2L}{\sqrt3}+\frac13.
\tag{153.11}
```

Hence the strain displacement obeys

```math
|p_{ij}-q|
=\varepsilon_L|j|
<\frac{1.2}{L^3}
\qquad(L\ge10).
\tag{153.12}
```

This is much smaller than both the deletion margin $`L^{-2}`$ and every fixed gap used below.

#### 2.3 Unit separation and exact cross-row gap

For two final patch points in different rows, write their difference as

```math
ae_1+(1+\varepsilon_L)ke_2,
\qquad k\ne0,\quad a,k\in\mathbb Z.
\tag{153.13}
```

Using

```math
Q(x,y)=|xe_1+ye_2|^2=x^2+xy+y^2,
```

if $`|k|\ge2`$, then

```math
Q(a,(1+\varepsilon_L)k)
=\left(a+\frac{(1+\varepsilon_L)k}{2}\right)^2
 +\frac34(1+\varepsilon_L)^2k^2
>1.
\tag{153.14}
```

If $`|k|=1`$, minimization over integer $`a`$ gives

```math
Q_{\min}
=1-(1+\varepsilon_L)+(1+\varepsilon_L)^2
=1+\varepsilon_L+\varepsilon_L^2.
\tag{153.15}
```

Thus every cross-row distance is strictly greater than one. Same-row retained points differ by an integer multiple of $`e_1`$, so their distances are at least one. The final patch is unit-separated, and its only possible unit contacts join consecutive retained points in one row.

The anchors are also strictly separated from the patch. Before strain every retained raw point satisfies

```math
|q-a_\pm|>1+L^{-2}.
```

Equation (153.12) is smaller than $`L^{-2}`$, so

```math
|p_{ij}-a_\pm|>1.
\tag{153.16}
```

#### 2.4 The anchors are the unique diameter pair

Every final patch point has norm at most

```math
s_L+1.2L^{-3}.
```

Consequently

```math
|p_{ij}-a_\pm|
\le L+s_L+1.2L^{-3}
=2L-L^{-1}+1.2L^{-3}<2L,
\tag{153.17}
```

and every patch-patch distance is at most

```math
2s_L+2.4L^{-3}<2L.
\tag{153.18}
```

Since $`|a_+-a_-|=2L`$, the anchors are the unique diameter pair and $`D_L=2L`$.

#### 2.5 Activation sequence

Fix a row index $`j`$. Before deletion, the points of $`Q_L^{\rm raw}`$ in this row form one consecutive interval of integer $`i`$-values. After deleting $`E_L`$, split the retained row into maximal consecutive segments. In each segment enumerate the points from left to right by

```math
r=0,1,\ldots,m.
```

Put

```math
\tau_L=\frac{\varepsilon_L}{1000L}
\tag{153.19}
```

and start the point of local index $`r`$ at

```math
p^0_{ij}=p_{ij}+\tau_L r e_1.
\tag{153.20}
```

Leave every segment-leftmost point $`r=0`$ fixed. In each segment, process $`r=1,2,\ldots,m`$ from left to right, moving the selected point continuously along the horizontal segment from $`p^0_{ij}`$ to $`p_{ij}`$. Process the row segments in any order.

A row chord in $`B_{s_L}`$ has length below $`2L`$, so a segment contains fewer than $`2L+2`$ points. Therefore every temporary horizontal shift is less than

```math
(2L+1)\tau_L<\frac{3}{1000}\varepsilon_L.
\tag{153.21}
```

For points in different rows, (153.15) gives

```math
|p-p'|\ge\sqrt{1+\varepsilon_L+\varepsilon_L^2}
>1+\frac{\varepsilon_L}{3}.
\tag{153.22}
```

A temporary horizontal displacement changes this distance by less than $`3\varepsilon_L/1000`$, so all cross-row distances remain strictly greater than one throughout the activation.

Within one row segment, all processed points sit at their final positions, while an unprocessed point of local index $`r`$ has positive rightward offset $`\tau_Lr`$. When that point moves left, its distance from its already processed immediate left neighbor decreases continuously to exactly one. Its immediate right neighbor, if any, is still shifted farther right, so that distance stays strictly greater than one. Nonadjacent points are farther apart. Across a deleted hole, the underlying lattice index gap is at least two, so no new unit contact can occur there.

The anchor estimates remain strict because (153.21) is negligible compared with the deletion margin. Equations (153.17)-(153.18) also remain strict. Hence each moving point is strict immediately before its move, the move creates exactly one new unit contact at its endpoint, and all old contacts persist. At every time the unit graph is a disjoint union of row paths, so every intermediate configuration is triangle-free.

#### 2.6 Almost-full activation rank

Let $`r_L`$ be the number of retained row segments. The number of row indices meeting the raw disk is at most

```math
\frac{4L}{\sqrt3}+2.
\tag{153.23}
```

Deleting one point can increase the number of segments by at most one, so by (153.10)

```math
r_L\le\frac{4L}{\sqrt3}+20.
\tag{153.24}
```

The final activation graph is a forest with

```math
|P_L^*|-r_L
```

edges. Rows of the bar-rigidity matrix of a forest are linearly independent: in any linear dependence, a leaf vertex occurs in exactly one remaining edge row, forcing that coefficient to vanish, and leaf elimination finishes the proof. Therefore

```math
\begin{aligned}
\operatorname{rank}R_L
&=|P_L^*|-r_L\\
&=n_L-2-r_L\\
&\ge n_L-\frac{4L}{\sqrt3}-22\\
&=n_L-\frac{2}{\sqrt3}D_L-22.
\end{aligned}
\tag{153.25}
```

This proves (153.4).

#### 2.7 Exact monomer neighborhoods and zero left nullity

For an unperturbed cell-center point

```math
b+ie_1+je_2,
```

the three lattice sites

```math
ie_1+je_2,\qquad
(i+1)e_1+je_2,\qquad
ie_1+(j+1)e_2
\tag{153.26}
```

are all at distance $`1/\sqrt3`$. Every other lattice site is at distance at least $`2/\sqrt3`$. This follows from the exact identity

```math
Q\left(a-\frac13,b'-\frac13\right)
=a^2+ab'+b'^2-a-b'+\frac13,
\tag{153.27}
```

whose integer part is zero only for $`(a,b')=(0,0),(1,0),(0,1)`$ and is at least one otherwise.

By (153.12) and (153.21), every patch point stays within $`1/100`$ of its unperturbed cell center for $`L\ge10`$. Since

```math
\frac1{\sqrt3}+\frac1{100}<1,
\qquad
\frac2{\sqrt3}-\frac1{100}>1,
```

the strict conflict neighborhood is exactly the three sites in (153.26) throughout the sequence.

Assign every patch point to its first site $`ie_1+je_2`$. These sites are distinct for distinct patch points and are genuine strict conflicts. Hence this assignment is a matching saturating the entire patch shore. The patch transversal deficiency, equivalently its left monomer nullity, is exactly zero.

#### 2.8 Cardinality at the sharp bulk scale

Let

```math
M_L=|Q_L^{\rm raw}|,
\qquad r_0=\frac1{\sqrt3}
```

be the triangular-lattice covering radius. The Voronoi hexagons of $`b+\Lambda`$ have area $`a_0`$ and covering radius $`r_0`$. The union of cells whose centers lie in $`B_{s_L}`$ is contained in $`B_{s_L+r_0}`$, while it contains $`B_{s_L-r_0}`$. Therefore

```math
\frac{\pi(s_L-r_0)^2}{a_0}
\le M_L\le
\frac{\pi(s_L+r_0)^2}{a_0}.
\tag{153.28}
```

Since $`n_L=M_L-|E_L|+2`$, $`|E_L|\le18`$, and

```math
\frac{D_L^2}{c}
=\frac{4L^2}{2\sqrt3/\pi}
=\frac{\pi L^2}{a_0},
\tag{153.29}
```

we obtain

```math
\left|n_L-\frac{D_L^2}{c}\right|
\le
\frac{4\pi}{3}L
+\frac{14\pi}{3\sqrt3}
+16.
\tag{153.30}
```

For $`L\ge10`$, the right side is at most $`8L=4D_L`$, proving (153.1).

#### 2.9 Constant perimeter deficit

Fix any unit vector $`w`$ and put

```math
x=(L-2)w.
```

By the covering-radius property, choose $`q\in b+\Lambda`$ with $`|q-x|\le r_0`$. Then

```math
|q|\le L-2+r_0<s_L,
```

so $`q\in Q_L^{\rm raw}`$. Moreover

```math
|q-a_\pm|
\ge L-|q|
\ge2-r_0
>1+L^{-2},
```

so $`q\notin E_L`$. Let $`p\in P_L^*`$ be its strained image. By (153.12),

```math
p\cdot w
\ge q\cdot w-|p-q|
\ge L-2-r_0-1.2L^{-3}
>L-3.
\tag{153.31}
```

Thus the support function of $`H_L`$ dominates that of $`B_{L-3}`$ in every direction, proving

```math
B_{L-3}\subset H_L.
```

Perimeter is monotone under inclusion of planar convex bodies, so

```math
P_L\ge2\pi(L-3).
\tag{153.32}
```

Cauchy's width formula gives $`P_L\le\pi\operatorname{diam}H_L=2\pi L`$. Hence

```math
0\le\pi D_L-P_L
=2\pi L-P_L
\le6\pi,
```

which is (153.3). The same inclusion and the isodiametric inequality also give

```math
0\le \frac{\pi D_L^2}{4}-\operatorname{area}H_L
\le 6\pi L-9\pi
=3\pi D_L-9\pi.
\tag{153.33}
```

This completes the proof. $`\square`$

### Dependencies

The proof is elementary once the canonical lattice normalization is fixed. It uses the same exact monomer-cell arithmetic as Target A Section 152 and the same sharp translated-lattice constant

```math
c=\frac{2\sqrt3}{\pi}
```

appearing in shared-theory Theorem 10.9. No external theorem beyond standard Voronoi covering geometry and Cauchy's perimeter formula is required.

### Why it is new

Section 152 uses an $`L\times L`$ patch with anchors at distance $`8L`$, so its activation rank is quadratic in $`D`$ but its cardinality is far below the sharp finite-packing scale. The present disk construction closes that loophole:

- its cardinality is $`D^2/c+O(D)`$;
- its convex hull has perimeter deficit at most $`6\pi`$;
- its activation forest has only $`O(D)`$ fewer rows than patch vertices;
- yet the coherent monomer shore remains perfectly matchable.

Thus merely adding asymptotically optimal scalar geometry to the hypotheses of the Section 152 false implication still does not produce response nullity.

## 3. Exact target implication

The canonical endpoint does not numerically change. The regression changes the admissible shape of a future activation-to-Schur theorem.

A valid theorem cannot have hypotheses consisting only of

```math
n=\frac{D^2}{c}+O(D),
\qquad
\pi D-P=O(1),
\qquad
\operatorname{rank}R_{\rm act}=n-O(D),
```

plus the local activation, planarity, fixed-diameter, and monomer-incidence conditions already present in Section 152.

Any successful bridge must use information absent here. The most obvious exact candidates are:

- global minimum-diameter optimality at the given cardinality;
- same-hull saturation or a stronger replacement consequence of global optimality;
- plateau terminalization;
- the exact relation to the independently chosen smaller optimum; or
- a source-to-response invariant that is not determined by bulk cardinality, hull perimeter, or local activation rank.

## 4. Exact remaining lemma

The direct remaining theorem is still

```math
\boxed{
\dim\ker S\ge\Delta_\Lambda-d_{\rm int}
}
```

for the genuine plateau-terminalized Target A source/scaffold pair.

For the activation route, this regression isolates the following useful discriminator problem.

> **Same-hull saturation discriminator.** Starting from the family above, determine whether one can extend each $`A_L`$ inside its own diameter-$`2L`$ hull to a maximal unit-separated set while preserving a linear-size coherent monomer subshore with zero Hall nullity and activation rank $`n-O(D)`$. Either an exact construction or an exact obstruction would advance Target A: a construction would show even same-hull saturation is insufficient, while an obstruction would identify a global-capacity mechanism not present in Sections 152–153.

This is narrower than “use global optimality”: it asks whether the first natural global strengthening, saturation in the actual hull, already separates the regression from a genuine source.

## 5. Audit classification of other claims

| Claim | Classification | Reason |
| --- | --- | --- |
| Near-extremal regression theorem above | proved candidate regression | Complete exact construction and proof given above; no numerical evidence is used. |
| `n=D^2/c+O(D)` alone transports activation rank to Schur nullity | rejected | The construction satisfies the scalar estimate and has zero patch monomer nullity. |
| Bounded perimeter deficit transports activation rank to Schur nullity | rejected | The construction has `0 <= pi D-P <= 6 pi`. |
| Almost-full activation rank forces positive monomer nullity | rejected | Rank is `n-O(D)` while the patch shore has a saturating matching. |
| Quantitative Kuperberg support rate `W(d)` | unchanged / not proved | Rechecking the gap-defect route did not produce an audited support-radius rate. |
| Global minimum-diameter optimality suffices for activation-to-Schur transport | open | The present regression deliberately omits this hypothesis. |

## 6. Regression tests

| Regression | Passed? | Exact reason |
| --- | --- | --- |
| Section 152 square-patch family | yes | The present construction is a strengthening in scalar geometry, not a contradiction. |
| Local full-rank planar-response examples | yes | Zero monomer deficiency is explicitly realized by an injective matching. |
| Exact two-leaf cage | yes | No cage-to-Schur implication is used. |
| Closed-semicircle first-transition boundary cases | yes | No first-transition perturbation theorem is invoked. |
| Cyclic Hall circuits / overlapping circuits | yes | The proof uses an explicit saturating matching, not cycle counting. |
| Global-minimizer hypothesis | intentionally absent | This is exactly why the family is a regression rather than a counterexample to Problem #99. |

## 7. Failed routes and no-go results

### 7.1 “Add scalar near-optimality to Section 152”

Proposed implication:

```text
Section 152 local hypotheses
+ n=D^2/c+O(D)
+ small hull deficit
-> positive response nullity.
```

Failure: Theorem 153 candidate gives an exact counterfamily with the stronger perimeter estimate $`\pi D-P\le6\pi`$.

This route is dead unless the added hypothesis contains genuinely global replacement/optimality information rather than only asymptotic scalar closeness.

### 7.2 Quantitative gap-support shortcut

The Kuperberg gap-defect construction was rechecked as a possible source of an explicit support-radius rate for the canonical quantity $`W(d)`$. No proof-level asymptotic rate was extracted. Section 150's status therefore remains unchanged. No polynomial, exponential, or other rate is claimed here.

## 8. Literature imported

None.

The external gap-defect paper was inspected only to test whether the canonical support-radius gap could be closed immediately. No new theorem statement is imported into this report.

## 9. Computation and reproducibility

No computation was used. All estimates are symbolic and elementary.

A future regression script could enumerate finite $`L`$ instances as a sanity check, but such a script would not add logical force to the proof above.

## 10. Canonical promotion recommendation

**Promote regression only after independent audit.**

If the proof survives audit, the clean canonical change is to append it after Section 152 as the next Target A regression (or place it in a new short Target A regression module), then update:

- `docs/targets/target-a/README.md`;
- the active Target A continuation prompt;
- `docs/reports/README.md`.

Do not alter the exact Target A endpoint.

## 11. Next run

Attack the same-hull saturation discriminator stated in Section 4.

Two concrete directions are available:

1. greedily/maximally fill the annular and deleted-anchor regions and prove that a protected positive-density interior monomer subshore remains exactly matchable; or
2. prove that any maximal same-hull extension necessarily creates a Hall obstruction crossing the protected disk core, using the continuum source Hall/deletion-cavity machinery as the model.

Either outcome would separate another false proxy for global optimality from the exact hypothesis actually needed by Target A.

## 12. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Strongest new theorem:
For every L>=10 there is an exact triangle-free fixed-diameter activation family with
D=2L, n=D^2/c+O(D) (explicitly |n-D^2/c|<=4D), perimeter deficit
0<=pi D-P<=6pi, activation rigidity rank n-O(D), and an exactly matchable coherent
monomer patch shore of zero left nullity.

Exact endpoint now:
Unchanged: prove dim ker S >= Delta_Lambda-d_int for the genuine plateau-terminalized
Target A source/scaffold pair.

Binding new no-go:
Asymptotically sharp cardinality/diameter scale and even O(1) perimeter deficit do not
upgrade local activation rank into Schur/monomer nullity. A successful theorem must use
an exact global replacement/optimality/plateau invariant.

Highest-value next lemma:
Same-hull saturation discriminator: either preserve the zero-nullity monomer core under
a maximal unit-separated extension in the same hull, or prove that such saturation
forces a Hall obstruction.

Authoritative files:
docs/targets/target-a/README.md
docs/targets/target-a/06-activation-monomer-regression.md
docs/targets/target-a/03-source-response.md
docs/prompts/erdos_problem_99_1.7.2_FINAL_CONTINUATION_PROMPT.md
```
