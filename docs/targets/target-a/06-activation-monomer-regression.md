# Target A — activation/monomer compatibility regression

This module continues the audited Target A frontier after Sections 148–151. It records
an exact finite regression showing that a quadratic one-point-at-a-time activation
forest can coexist on the same points with a Hall-neutral coherent monomer scaffold.
The construction is **not** globally minimum-diameter optimal; that missing hypothesis
is exactly what any successful activation-to-Schur theorem must use.

**LEVEL I STATUS: STILL OPEN. TARGET A REMAINS UNRESOLVED.**

---

# 152. Activation rank does not force monomer-scaffold nullity

Use the triangular-lattice basis

\[
e_1=(1,0),\qquad e_2=\left(\frac12,\frac{\sqrt3}{2}\right),
\qquad Q(a,b)=|ae_1+be_2|^2=a^2+ab+b^2.
\tag{152.1}
\]

Fix

\[
\alpha=\frac1{20},\qquad \eta=\frac1{100},\qquad L\ge2,
\qquad s=1+\frac\alpha L.
\tag{152.2}
\]

For \(0\le i,j<L\), define the final patch points

\[
p_{ij}=\left(i+\frac13\right)e_1+
\left(sj+\frac13\right)e_2,
\tag{152.3}
\]

and add two fixed anchors

\[
a_-=-4Le_1,\qquad a_+=4Le_1.
\tag{152.4}
\]

The anchor distance is \(D=8L\).

> **Theorem 152.1 (activation/monomer compatibility regression).** For every integer
> \(L\ge2\), there is a finite one-point-at-a-time activation sequence from a strict
> initial placement of the \(L^2\) patch points to (152.3) such that:
>
> 1. every intermediate configuration is unit-separated, triangle-free, and has
>    diameter exactly \(D=8L\);
> 2. every previously active pair persists, and each move acts on a currently strict
>    patch point and creates exactly one new unit contact;
> 3. the new unit contacts form \(L\) disjoint row paths and therefore have independent
>    rigidity rows of total rank
>    \[
>    L(L-1)=\frac{D^2}{64}-\frac D8;
>    \tag{152.5}
>    \]
> 4. relative to the unstrained triangular lattice, every patch point has exact strict
>    conflict neighborhood
>    \[
>    N_\Lambda(p_{ij})=\{(i,j),(i+1,j),(i,j+1)\};
>    \tag{152.6}
>    \]
>    throughout the activation sequence; and
> 5. the assignment \(p_{ij}\mapsto(i,j)\) is a matching saturating every patch point.
>    Hence the corresponding monomer-scaffold left nullity is exactly zero.
>
> In particular, a quadratic independent activation rank, a fixed diameter pair,
> planarity, and coherent neutral monomer incidence do not by themselves force positive
> scaffold or Schur nullity.

## Proof

Initially put

\[
p^0_{ij}=p_{ij}+\frac{\eta i}{L^2}e_1.
\tag{152.7}
\]

Process the rows in any fixed order and, within each row, process
\(i=1,\ldots,L-1\) from left to right, replacing \(p^0_{ij}\) by \(p_{ij}\).
The points with \(i=0\) remain fixed.

### Unit separation and activation order

Within one row, two processed points differ by an integer multiple of \(e_1\), two
unprocessed points have an additional positive horizontal separation, and a processed
point to the left of an unprocessed point has separation

\[
(k-i)+\frac{\eta k}{L^2}>1
\]

when adjacent and larger otherwise. Hence same-row distances are at least one, with
equality exactly on already-created neighboring row contacts.

For different rows, first omit the horizontal perturbations. If the row difference is
\(b\ne0\), the difference vector is \(ae_1+sbe_2\) for an integer \(a\). For
\(|b|\ge2\),

\[
Q(a,sb)=\left(a+\frac{sb}{2}\right)^2+\frac34s^2b^2>1.
\]

For \(|b|=1\), the minimum over integers \(a\) is

\[
1-s+s^2
=1+\frac\alpha L+\frac{\alpha^2}{L^2}.
\tag{152.8}
\]

At every intermediate state the relative horizontal perturbation has norm less than
\(\eta/L\), while

\[
1+\frac\alpha L+\frac{\alpha^2}{L^2}
>
\left(1+\frac\eta L\right)^2
\tag{152.9}
\]

because \(\alpha>2\eta\). The reverse triangle inequality therefore keeps every
cross-row distance strictly greater than one.

Every patch coordinate has Euclidean norm less than \(2L\). Hence every patch point is
strictly between \(2L\) and \(6L\) from either anchor, every patch-patch distance is
less than \(4L\), and the two anchors remain the unique diameter pair at distance
\(8L\). Thus every intermediate configuration has diameter exactly \(D\).

Immediately before \(p_{ij}\), \(i\ge1\), moves, it has no unit or diameter pair and
is therefore strict. Moving it creates exactly the contact with its processed left
neighbor \(p_{i-1,j}\); the right neighbor is still shifted, all cross-row distances
are strict, and all previous row contacts persist. The final unit graph is the disjoint
union of the \(L\) row paths, so it is triangle-free and has \(L(L-1)\) edges. By the
forest-row independence theorem from the activation analysis, these rows are
independent rigidity constraints, proving (152.5).

### Exact monomer neighborhood

Let

\[
c=\frac{e_1+e_2}{3}.
\]

The point \(c\) is at distance \(1/\sqrt3\) from the three vertices of one elementary
\(+\)-triangle. For an arbitrary lattice coordinate \((a,b)\),

\[
Q\left(a-\frac13,b-\frac13\right)
=a^2+ab+b^2-a-b+\frac13.
\tag{152.10}
\]

The integer part is zero only for
\((a,b)=(0,0),(1,0),(0,1)\), and is at least one otherwise. Therefore the three cell
vertices are at distance \(1/\sqrt3\), while every other lattice point is at distance
at least \(2/\sqrt3\).

Relative to \(c+ie_1+je_2\), the accumulated vertical strain is less than \(\alpha\),
and the temporary horizontal shift is less than \(\eta\). Since

\[
\alpha+\eta
<\frac2{\sqrt3}-1
<1-\frac1{\sqrt3},
\tag{152.11}
\]

the triangle inequality keeps exactly the three displayed cell vertices strictly
within unit distance and every other lattice point outside unit distance throughout the
sequence. This proves (152.6). The lower-left vertices \((i,j)\) are all distinct and
are genuine conflict neighbors, so \(p_{ij}\mapsto(i,j)\) is a matching saturating the
entire patch shore. Its left transversal nullity is therefore zero. \(\square\)

## 152.1 Exact Target A consequence

The regression simultaneously realizes several known local obstructions:

- \(\Theta(D^2)\) independent activation constraints;
- one-point-at-a-time activation with persistence of every old active pair;
- a fixed diameter pair;
- straight-chain contact components;
- the \(O(1/L)\) strained-monomer scale; and
- coherent neutral monomer cells with zero left Hall deficiency.

Yet the activation rank does not create any scaffold nullity. Therefore the implication

\[
\boxed{
\text{large activation rigidity rank}
+\text{fixed diameter}
+\text{local monomer incidence}
\not\Longrightarrow
\text{positive scaffold/Schur nullity}
}
\tag{152.12}
\]

is false without additional global input.

The construction is deliberately **not** a globally optimal packing for its
cardinality. Consequently it is not a counterexample to Erdős Problem #99 and does not
contradict the canonical Target A endpoint

\[
\dim\ker S\ge\Delta_\Lambda-d_{\rm int}.
\]

Instead it sharpens the transport requirement: any theorem converting the activation
forest of Section 145 into Schur nullity must use global minimum-diameter optimality,
the exact relation to the independently chosen smaller optimum, or another genuinely
global source-to-response invariant. Local activation geometry, planarity, and
monomer-scaffold incidence are insufficient.

The full arithmetic audit is recorded in
[`../../reports/activation_monomer_regression_2026-08-30.md`](../../reports/activation_monomer_regression_2026-08-30.md).
The exact rational implementation and tests are
[`../../../research/activation_monomer_regression.py`](../../../research/activation_monomer_regression.py)
and
[`../../../research/test_activation_monomer_regression.py`](../../../research/test_activation_monomer_regression.py).

**LEVEL I STATUS: STILL OPEN. TARGET A REMAINS UNRESOLVED.**
