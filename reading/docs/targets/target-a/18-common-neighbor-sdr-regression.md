> Generated reading edition · [exact source](../../../../docs/targets/target-a/18-common-neighbor-sdr-regression.md) · source SHA-256 `d585a57280fa391816a3354d07af96f618c7e1a3cf640f36d0f8a9445f9c2629`.
> [Current theorem state](../../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

# Target A — common-neighbor SDR regression

This audited regression follows the common-neighbor lifts of Sections 164–165. It
shows that the local triangular-lattice theorem cannot be upgraded, from local geometry
alone, to a distinct common lattice neighbor for every source-matched left vertex.
Even two disjoint strict source-matching edges can be forced to use the same unique
common lattice site.

**LEVEL I STATUS: STILL OPEN.**

---

# 166. Exact two-pair obstruction to a perfect common-neighbor lift

Use the unit triangular lattice
```math
\Lambda=\mathbb Z e_1+\mathbb Z e_2,
\qquad
e_1=(1,0),
\qquad
e_2=\left(\frac12,\frac{\sqrt3}{2}\right).
\tag{166.1}
```
Put
```math
\begin{aligned}
x_1&=\left(-\frac3{10},-\frac1{10}\right),
& a_1&=\left(\frac12,-\frac{13}{20}\right),\\
x_2&=\left(\frac35,\frac7{20}\right),
& a_2&=\left(-\frac14,\frac3{20}\right).
\end{aligned}
\tag{166.2}
```
Let
```math
X=\{x_1,x_2\},
\qquad A=\{a_1,a_2\}.
\tag{166.3}
```

> **Proposition 166.1 (two-pair common-neighbor collision).** The two shores `X` and
> `A` are unit-separated, the pairing `x_i-a_i` is a strict-conflict matching, and
> for each `i` the two endpoints have exactly one common strict lattice neighbor,
> namely the origin:
> ```math
> \boxed{
> N_\Lambda(x_1)\cap N_\Lambda(a_1)
> =N_\Lambda(x_2)\cap N_\Lambda(a_2)
> =\{0\}.
> }
> \tag{166.4}
> ```
> Consequently no injective assignment can choose a distinct common lattice neighbor
> for both matched pairs.

### Proof

The four relevant pairwise squared distances are
```math
|x_1-a_1|^2=\frac{377}{400}<1,
\qquad
|x_2-a_2|^2=\frac{61}{80}<1,
\tag{166.5}
```
while
```math
|x_1-x_2|^2=\frac{81}{80}>1,
\qquad
|a_1-a_2|^2=\frac{481}{400}>1.
\tag{166.6}
```
Thus the two shores are unit-separated and the indicated pairing consists of strict
conflicts. By Theorem 163.1 its two straight matching segments are automatically
disjoint.

A direct triangular-lattice distance check gives
```math
\begin{aligned}
N_\Lambda(x_1)
&=\{0,-e_1,-e_1+e_2,-e_2\},\\
N_\Lambda(a_1)
&=\{0,e_1-e_2,e_1\},\\
N_\Lambda(x_2)
&=\{0,e_2,e_1\},\\
N_\Lambda(a_2)
&=\{0,-e_1,-e_1+e_2\}.
\end{aligned}
\tag{166.7}
```
For an exact check of the strict inequalities, the squared distances to the closest
lattice site *outside* each displayed neighborhood are respectively
```math
\frac75-\frac{\sqrt3}{10},
\quad
\frac{869}{400}-\frac{13\sqrt3}{20},
\quad
\frac{673}{400}-\frac{7\sqrt3}{20},
\quad
\frac{267}{200}-\frac{3\sqrt3}{20},
\tag{166.8}
```
and every one is strictly greater than one. The displayed included sites have squared
distance strictly below one; for example the largest included squared distances are
```math
\frac45+\frac{\sqrt3}{10},
\quad
\frac{269}{400},
\quad
\frac{193}{400},
\quad
\frac{117}{200},
\tag{166.9}
```
all below one. The triangular-lattice shell ordering then excludes every more distant
site. Equation (166.7) follows, and its two intersections are exactly `{0}`. $`\square`$

## 166.1 Exact scope

This is not a regression against Theorem 164.1: each matched pair does have a common
lattice neighbor. It is a regression against the tempting stronger assertion
```math
\text{a strict matching }X\to A
\Longrightarrow
\text{a matching of the same size through distinct common lattice sites}.
\tag{166.10}
```
That implication is false even for two pairs, even though both shores are
unit-separated and the source-matching segments are noncrossing.

Therefore the factor-five bounded-congestion extraction in Sections 164–165 cannot be
removed by a purely local Hall argument that uses only unit separation, strict paired
conflicts, and the individual common-neighbor theorem. Any near-perfect
source-certified response matching must use additional global structure: the
minimum-diameter origin of the source, the plateau response matroid, nonlocal cell
phase information, or another global invariant.

The example does **not** prove that the factor five is sharp. It only proves that zero
loss is false under the local hypotheses.
