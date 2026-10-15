# Problem statement

> This concise statement is the problem-definition module of the canonical v1.7.0
> theorem state. See the [current documentation map](../README.md).

## 1. The problem and its quantifiers

For $n\ge 2$, define

\[
D(n)=\min\left\{\operatorname{diam}(A):
A\subset\mathbb R^2,\ |A|=n,\ |x-y|\ge1\text{ for }x\ne y\right\}.
\]

A minimizing configuration is an $n$-point set $A$ with minimum pairwise distance (1) and diameter $D(n)$. Its **unit-contact graph** $G(A)$ has vertex set $A$ and edge set

\[
C(A)=\{xy:|x-y|=1\}.
\]

A unit equilateral triangle is exactly a triangle in $G(A)$, or equivalently three mutually tangent radius-$1/2$ disks in the associated equal-disk packing.

Erdős asks whether

\[
\exists n_0\ \forall n\ge n_0\ \forall A,
\quad A\text{ minimizing}\Longrightarrow G(A)\text{ contains a triangle}.
\]

The negation requires triangle-free global minimizers for arbitrarily large $n$. One finite counterexample, even a very large one, does not disprove the conjecture. Conversely, constructing one triangle-containing minimizer for every $n$ does not prove it, because the conjecture concerns **every** minimizer.

The disk formulation will be used throughout: the radius-$1/2$ disks centered at the points of $A$ have disjoint interiors, and

\[
\operatorname{diam}\left(\bigcup_{p\in A}B(p,1/2)\right)=D(n)+1.
\]

---
