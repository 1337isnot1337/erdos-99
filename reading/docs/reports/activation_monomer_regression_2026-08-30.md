> Generated reading edition · [exact source](../../../docs/reports/activation_monomer_regression_2026-08-30.md) · source SHA-256 `2999f15760b7aee4c9f7cb8e732755b4a3056faae48291db6a338f4d01179377`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-582D2B734BAF","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# Exact activation-forest/monomer-scaffold regression

This report is the proof-level audit behind Section 152 of
[`../targets/target-a/06-activation-monomer-regression.md`](../targets/target-a/06-activation-monomer-regression.md).
It records a finite geometric obstruction to a purely local completion of the
activation-to-Schur route. A quadratic family of independent activation rows can
coexist, on the same points, with an exactly matchable monomer scaffold.

The construction is **not** a global diameter minimizer; that omission is precisely the
datum any successful source-to-Schur theorem must use.

Use the unit triangular-lattice basis

```math
e_1=(1,0),\qquad e_2=(1/2,\sqrt3/2),\qquad
Q(a,b)=|ae_1+be_2|^2=a^2+ab+b^2.
```

Fix

```math
\alpha=\frac1{20},\qquad \eta=\frac1{100},\qquad L\ge2,
\qquad s=1+\frac\alpha L.
```

For $`0\le i,j<L`$, let the final patch point be

```math
p_{ij}=\left(i+\frac13\right)e_1+
\left(sj+\frac13\right)e_2.
\tag{1}
```

Add two fixed anchors

```math
a_-=-4Le_1,\qquad a_+=4Le_1.
\tag{2}
```

The anchor distance is $`D=8L`$.

## Theorem

There is a sequence of configurations from a strict initial placement of the
$`L^2`$ patch points to (1), moving one currently strict patch point at a time, such
that:

1. every configuration is unit-separated, triangle-free, and has diameter exactly
   $`D=8L`$;
2. every old active pair persists and each move creates exactly one new unit pair;
3. the new unit pairs are the $`L`$ disjoint row paths, with
   
   ```math
   |F_{\rm act}|=L(L-1)=\frac{D^2}{64}-\frac D8;
   \tag{3}
   ```

4. relative to the unstrained triangular lattice, every $`p_{ij}`$ has exact strict
   conflict neighborhood
   
   ```math
   N(p_{ij})=\{(i,j),(i+1,j),(i,j+1)\};
   \tag{4}
   ```

   throughout the activation sequence; and
5. the map $`p_{ij}\mapsto(i,j)`$ is a matching saturating the patch shore. Hence
   its scaffold transversal nullity is exactly zero.

In particular, the activation forest has $`\Theta(D^2)`$ independent rigidity rows,
while the monomer scaffold on the same points has no left Hall deficiency.

## Proof

Initially place

```math
p^0_{ij}=p_{ij}+\frac{\eta i}{L^2}e_1.
\tag{5}
```

Process the rows in any fixed order and, within each row, process
$`i=1,\ldots,L-1`$ from left to right. At the step for $`(i,j)`$, replace
$`p^0_{ij}`$ by $`p_{ij}`$. Points already processed have zero horizontal shift;
points not yet processed retain the shift in (5).

We first check every lower-distance constraint. In one row, the left-to-right order
gives only three possibilities. Two processed coordinates differ by an integer; two
unprocessed adjacent coordinates differ by more than one; and a processed coordinate
to the left of an unprocessed coordinate has separation

```math
(k-i)+\frac{\eta k}{L^2}>1
```

when the indices are adjacent, and is still larger otherwise. Thus same-row distances
are at least one, with equality exactly on already-created neighboring row contacts.

For different rows, first omit the horizontal shifts. If the row difference is
$`b\ne0`$, the difference vector is $`ae_1+sbe_2`$ for an integer $`a`$. For
$`|b|\ge2`$, completing the square gives

```math
Q(a,sb)=\left(a+\frac{sb}{2}\right)^2+\frac34s^2b^2>1.
```

For $`|b|=1`$, the minimum over integers $`a`$ is

```math
1-s+s^2=1+\frac\alpha L+\frac{\alpha^2}{L^2}.
\tag{6}
```

At any intermediate state the relative horizontal perturbation has norm less than
$`\eta/L`$. The exact inequality

```math
1+\frac\alpha L+\frac{\alpha^2}{L^2}
>
\left(1+\frac\eta L\right)^2
\tag{7}
```

follows from $`\alpha>2\eta`$. Equations (6)–(7) and the reverse triangle inequality
prove that every cross-row distance is strictly greater than one.

Every patch coordinate in the lattice basis lies in a region of Euclidean norm less
than $`2L`$. Its distance from either anchor is therefore strictly between $`2L`$ and
$`6L`$, every patch-patch distance is less than $`4L`$, and the anchors remain the
unique diameter pair at distance $`8L`$. This proves unit separation and the fixed
diameter at every step.

Immediately before $`p_{ij}`$, $`i\ge1`$, moves, it has no active unit or diameter
pair. Moving it creates the single contact $`p_{i-1,j}p_{ij}`$; its right neighbor is
still shifted, all cross-row distances are strict, and all earlier row contacts and
the anchor diameter persist. Thus the moved point is currently strict and exactly one
active pair is created. The final unit graph is the disjoint union of the row paths,
which is triangle-free and has the edge count (3). The forest-row independence theorem
then gives rigidity rank $`L(L-1)`$.

It remains to audit the scaffold neighborhood. The unperturbed offset
$`c=(e_1+e_2)/3`$ has squared distance $`1/3`$ from the three vertices of one
elementary $`+`$-triangle. For any lattice coordinate $`(a,b)`$,

```math
Q\left(a-\frac13,b-\frac13\right)
=a^2+ab+b^2-a-b+\frac13.
\tag{8}
```

The integer part in (8) is zero only for
$`(a,b)=(0,0),(1,0),(0,1)`$, and is at least one otherwise. To see this directly,
for $`b\notin\{0,1\}`$ minimize the quadratic over real $`a`$; its minimum is
$`(3b^2-2b-1)/4\ge1`$. For $`b=0`$ it is $`a(a-1)`$, and for $`b=1`$ it is
$`a^2`$. Hence the three cell vertices are at distance $`1/\sqrt3`$, while every
other lattice point is at distance at least $`2/\sqrt3`$.

The extra offset from $`c+ie_1+je_2`$, including the accumulated strain and temporary
horizontal shift, has norm less than

```math
\alpha+\eta<\frac{2}{\sqrt3}-1<1-\frac1{\sqrt3}.
```

The triangle inequality therefore makes precisely the three displayed cell vertices
strict conflicts and every other lattice point a nonconflict throughout the sequence.
This proves (4). The lower-left vertices $`(i,j)`$ are distinct, so they give a
matching of all $`L^2`$ patch points and the left nullity is zero. $`\square`$

## Target A consequence

This theorem blocks a purely local completion of the activation-rank route:

```math
\text{large independent activation rank}
+\text{ coherent neutral monomer cells}
\centernot\Longrightarrow
\text{positive scaffold/Schur nullity}.
```

The model includes a fixed diameter pair, exact one-at-a-time activation, persistence
of every old active constraint, straight-chain contact components, the strained
monomer scale $`O(1/L)`$, and a quadratic activation population. What it does not
include is the decisive hypothesis: it is not globally optimal for its cardinality.
Accordingly it is not a counterexample to Erdős Problem #99.

A valid activation-to-Schur theorem must therefore use global optimality, the exact
relation to the independent smaller optimum, or another genuinely global transport
invariant; contact rank, fixed diameter, planarity, and local monomer incidence do not
suffice.

## Reproduction

The exact rational implementation is in
[`../../research/activation_monomer_regression.py`](../../../research/activation_monomer_regression.py),
with tests in
[`../../research/test_activation_monomer_regression.py`](../../../research/test_activation_monomer_regression.py).

Run:

```sh
python3 research/activation_monomer_regression.py
python3 -m unittest research/test_activation_monomer_regression.py
```

The implementation uses `fractions.Fraction` for all lattice-coordinate arithmetic;
there is no floating-point tolerance in the certificate checks.

**LEVEL I STATUS: STILL OPEN. TARGET A REMAINS UNRESOLVED.**
