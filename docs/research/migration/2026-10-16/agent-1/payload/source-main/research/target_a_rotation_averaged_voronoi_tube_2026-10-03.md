# Target A: rotation-averaged Voronoi tube bound

Date: 2026-10-03
Base main: `7a327e1ad95cd2e9cb035b9b96fb34fd8f12114d`
Status: proof-only candidate, noncanonical. Target A and Level I remain open.

This note is independent of the active Target B coarea/Mantel-density route and the
finite Target C nine-no-root certificate route. It sharpens the deterministic
right-shore tube payment in Target A Section 175.

Let \(\Sigma\) be a finite connected unit-contact graph in the fixed response optimum.
Its geometric realization is fixed before the triangular response lattice is chosen.
Canonical Section 154 permits any rotated and translated unit triangular lattice.

For a lattice \(\Lambda\), put

\[
T_\Sigma(\Lambda)=
\{y\in\Lambda:\operatorname{dist}(y,|\Sigma|)<1\}.
\]

The theorem below chooses one lattice rotation from the geometry of \(\Sigma\), and
then holds for every translation of that rotated lattice.

## 1. Minkowski tube lemma for a connected graph

Let \(G\) be a finite connected straight-edge graph and \(K\) a convex body. If
\(n_e\) is a unit normal to edge \(e\), then

\[
\boxed{
\operatorname{area}(G+K)
\le
\operatorname{area}(K)
+\sum_{e\in E(G)} |e|\,w_K(n_e).
}
\tag{1}
\]

Here \(w_K(n)\) is the width of \(K\) in direction \(n\).

Proof. Begin with one graph vertex. Order a spanning tree so that each new edge has
one endpoint in the already built graph, then append the non-tree edges. Suppose
\(e=[p,q]\) is added and \(p\) is already present. The previous Minkowski sum contains
\(p+K\), while

\[
\operatorname{area}(e+K)
=
\operatorname{area}(K)+|e|w_K(n_e).
\]

Therefore the new area contributed by \(e+K\) is at most
\(|e|w_K(n_e)\). Summing proves (1). \(\square\)

## 2. Voronoi-cell enclosure

Let \(V_\phi\) be the Voronoi hexagon of a unit triangular lattice rotated by
\(\phi\). Then

\[
\operatorname{area}(V_\phi)=\frac{\sqrt3}{2},
\qquad
\operatorname{per}(V_\phi)=2\sqrt3.
\tag{2}
\]

Put

\[
K_\phi=V_\phi+B_1.
\]

Steiner's formula gives

\[
\operatorname{area}(K_\phi)
=
\frac{5\sqrt3}{2}+\pi,
\tag{3}
\]

and width additivity gives

\[
w_{K_\phi}(n)=w_{V_\phi}(n)+2.
\tag{4}
\]

Fix any translation \(v\) of the rotated lattice. If
\(y\in T_\Sigma(\Lambda_\phi+v)\), choose \(x\in|\Sigma|\) with \(|x-y|<1\).
Then the full Voronoi cell \(y+V_\phi\) lies in

\[
|\Sigma|+B_1+V_\phi=|\Sigma|+K_\phi.
\]

The Voronoi-cell interiors are disjoint, so (1)--(4), with every contact edge of
length one, imply

\[
|T_\Sigma(\Lambda_\phi+v)|\frac{\sqrt3}{2}
\le
\frac{5\sqrt3}{2}+\pi
+
2|E(\Sigma)|
+
\sum_{e\in E(\Sigma)}w_{V_\phi}(n_e).
\tag{5}
\]

Thus

\[
|T_\Sigma(\Lambda_\phi+v)|
\le
5+\frac{2\pi}{\sqrt3}
+\frac4{\sqrt3}|E(\Sigma)|
+\frac2{\sqrt3}
\sum_e w_{V_\phi}(n_e).
\tag{6}
\]

This estimate is pointwise in the translation \(v\).

## 3. Optimize one common lattice rotation

The regular hexagonal Voronoi cell has width period \(\pi/3\). Cauchy's projection
formula gives its mean width

\[
\frac1\pi\int_0^\pi w_V(\theta)\,d\theta
=
\frac{\operatorname{per}(V)}{\pi}
=
\frac{2\sqrt3}{\pi}.
\tag{7}
\]

Hence the same mean holds over one rotation period:

\[
\frac3\pi\int_0^{\pi/3}w_{V_\phi}(n)\,d\phi
=
\frac{2\sqrt3}{\pi}
\tag{8}
\]

for every fixed direction \(n\). Summing (8) over all contact edges shows that some
single rotation \(\phi_*\) satisfies

\[
\sum_{e\in E(\Sigma)}w_{V_{\phi_*}}(n_e)
\le
\frac{2\sqrt3}{\pi}|E(\Sigma)|.
\tag{9}
\]

Insert (9) into (6). Since the left side is an integer, for every translation \(v\),

\[
\boxed{
|T_\Sigma(\Lambda_{\phi_*}+v)|
\le
\left\lfloor
5+\frac{2\pi}{\sqrt3}
+
\left(\frac4{\sqrt3}+\frac4\pi\right)|E(\Sigma)|
\right\rfloor .
}
\tag{10}
\]

The edge coefficient is

\[
\frac4{\sqrt3}+\frac4\pi
=
3.582640621493666\ldots .
\tag{11}
\]

This is smaller than both the current-main \(9\)-per-edge bound and the
unrotated worst-direction Voronoi coefficient
\(\frac4{\sqrt3}+\frac43=3.6427344100\ldots\).

## 4. Target A consequence

For the Section-172 locked three-channel fan, \(\Sigma\) is connected and unicyclic,
so

\[
|E(\Sigma)|=|V(\Sigma)|=:v.
\]

Choose the response-lattice rotation \(\phi_*\) from (9), then choose any admissible
generic translation. Canonical Section 154 permits a prescribed rotated/translated
triangular lattice, and generic translation can still avoid the finite response
degeneracies. Because (10) holds for every translation after the rotation is fixed,
no independent minimization of the phase-dependent Schur surplus is being assumed.

Since \(T_Z\subseteq T_\Sigma\), Section 175.4 closes the locked branch whenever

\[
\boxed{
|O_{\rm iso}|+Q_\Sigma
\ge
j_*+
\left\lfloor
5+\frac{2\pi}{\sqrt3}
+
\left(\frac4{\sqrt3}+\frac4\pi\right)v
\right\rfloor .
}
\tag{12}
\]

The exact Section-175 criterion with the actual \(|T_Z|\) remains stronger.

## 5. Scope

This is a deterministic existence theorem for one lattice orientation and is proof-only.
No numerical search, verifier, CI result, or heuristic is a premise. The decimal in
(11) only evaluates the exact coefficient.

Target A remains open. The remaining locked-branch problem is still to force enough
right-sector sink surplus \(|O_{\rm iso}|+Q_\Sigma\) relative to \(j_*\) and the
actual interior tube population. The present result lowers the universal pointwise
tube coefficient while preserving the phase quantifiers needed by the Schur argument.
