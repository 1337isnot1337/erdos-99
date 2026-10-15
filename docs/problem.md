# Problem definition

For a finite nonempty set $A\subset\mathbb R^2$, define
$$
\operatorname{diam}(A)=\max\{|x-y|:x,y\in A\},
$$
where $|\cdot|$ is Euclidean distance. For an integer $n\ge2$, consider all sets $A$ with exactly $n$ points and
$$
|x-y|\ge1\qquad\text{for all distinct }x,y\in A.
$$
Write $D(n)$ for the infimum of their diameters. The attainment task in this repository asks contributors to verify that this infimum is attained; once that is established, $D(n)$ is a minimum.

A **global minimizer of size $n$** is a feasible set $A$ with $|A|=n$ and $\operatorname{diam}(A)=D(n)$. A **unit contact** is a pair of distinct points at distance exactly one. Three points form a **unit equilateral triangle** when all three pairwise distances are one.

Erdős Problem 99 asks whether
$$
\exists n_0\ \forall n\ge n_0\ \forall A,
\quad
\bigl(A\text{ is a global minimizer of size }n\bigr)
\Longrightarrow
\bigl(A\text{ contains a unit equilateral triangle}\bigr).
$$

Both universal quantifiers matter. A proof for one chosen minimizer at each size is insufficient. A triangle-free feasible set, including a finite set with a particularly large cardinality, does not disprove the eventual claim unless it is globally minimizing; a disproof requires triangle-free global minimizers at unboundedly many sizes. Local optimality and density estimates do not imply global minimality.

This definition concerns the centers of equal disks of radius $1/2$: pairwise center separation at least one is equivalent to nonoverlapping disk interiors. The target condition says that three disks mutually touch. This equivalent picture does not change the quantifiers.
