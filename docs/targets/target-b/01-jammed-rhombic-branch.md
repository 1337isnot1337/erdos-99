# Target B: jammed almost-rhombic branch

> Canonical v1.7.0 route module. The original section numbering is preserved for
> cross-references; see the [route map](README.md).
> The promoted [2026-09-05 phase-cut/crossing-family addendum](../../reports/target_b_phase_cut_and_biclique_2026-09-05.md)
> supersedes the feedback-set, dense-core long-cycle, and coherent-star
> additive-realization and coherent near-equality gaps in Sections 49–56.
> The general Target B endpoint
> remains open; the route map states its live scope.

# 24. Perimeter saturation and the linear support-depth theorem

Throughout, let

\[
K=\operatorname{conv}A,\qquad
P=\operatorname{per}(K),\qquad
D=D(n),
\]

and use

\[
a_0=\frac{\sqrt3}{2},
\qquad
c_0=\frac{\sqrt3}{4},
\qquad
c=\frac{2\sqrt3}{\pi},
\qquad
C_0=\sqrt{2\pi\sqrt3}.
\]

The following results were obtained in the subsequent continuation and are to be treated as part of the established research state.

## 24.1 Perimeter lower bound for every global minimizer

Every global minimizer satisfies

\[
\boxed{
P\ge
\sqrt{
C_0^2(n-1)+\frac{3\pi^2}{4}
}
-\frac{\pi\sqrt3}{2}.
}
\tag{24.1}
\]

Together with Cauchy's perimeter-diameter inequality \(P\le \pi D\) and the
strict \(n-1\) lattice bound of Section 36, this in fact gives the uniform strict
estimate

\[
\boxed{
0\le \pi D-P
<
\frac{\pi\sqrt3}{2}
=
2.7206990463\ldots .
}
\tag{24.2}
\]

Thus the convex hull of a global minimizer has perimeter within an absolute \(O(1)\) error of the maximum possible perimeter for its diameter.

This is a much stronger global statement than the previous \(P=O(D)\).

**Audit derivation.** Finite Oler gives

\[
\operatorname{area}(K)+c_0P\ge a_0(n-1),
\]

while the planar isoperimetric inequality gives

\[
\operatorname{area}(K)\le\frac{P^2}{4\pi}.
\]

Therefore

\[
P^2+4\pi c_0P-4\pi a_0(n-1)\ge0,
\]

and the positive quadratic root is exactly (24.1). The strict translated-lattice
bound of Section 36 gives \(\pi D<C_0\sqrt{n-1}\). If
\(A=C_0\sqrt{n-1}\) and \(b=\pi\sqrt3/2\), then (24.1) says
\(P\ge\sqrt{A^2+b^2}-b\), so
\[
A-P\le A-\sqrt{A^2+b^2}+b<b.
\]
Therefore \(\pi D-P<A-P<b\), which is (24.2).

## 24.2 Uniform width saturation

Let \(w_K(\phi)\) denote the width of \(K\) in direction \(\phi\).

The bounded perimeter deficit implies

\[
\boxed{
\min_\phi w_K(\phi)
=
D-O(n^{1/6}).
}
\tag{24.3}
\]

Since \(D=\Theta(\sqrt n)\),

\[
w_K(\phi)=D-o(D)
\]

uniformly in direction.

Thus every surviving global minimizer is asymptotically constant-width at the scale relevant to the rhombic train system.


**Audit derivation.** Let \(m=\min w_K\) and put \(L=K-K\). Then \(L\) is centrally
symmetric, \(L\subset B(0,D)\), and

\[
h_L(u)=w_K(u).
\]

In a direction attaining \(m\), central symmetry therefore places \(L\) inside the
strip \(|u\cdot x|\le m\). Brunn--Minkowski gives

\[
\operatorname{area}(L)\ge4\operatorname{area}(K).
\]

Hence \(4\operatorname{area}(K)\) is at most the area of the radius-\(D\) disk with
the two caps beyond \(|u\cdot x|=m\) removed. If \(\delta=D-m\), one such cap has
area

\[
D^2\arccos\frac mD-m\sqrt{D^2-m^2}
\asymp
D^{1/2}\delta^{3/2}
\]

for \(\delta=o(D)\). Since Section 36 and Oler give

\[
\frac{\pi D^2}{4}-\operatorname{area}(K)=O(D),
\]

we obtain \(D^{1/2}\delta^{3/2}=O(D)\), hence

\[
\delta=O(D^{1/3})=O(n^{1/6}).
\]

This proves (24.3) without assuming smoothness of the hull.

## 24.3 Exact support depth of a train end

For a rhombic boundary edge \(e\), let \(\nu_e\) be its outward unit normal and \(m_e\) its midpoint. Define its support depth

\[
\boxed{
d_e
=
h_K(\nu_e)-\nu_e\cdot m_e.
}
\tag{24.4}
\]

For a train track \(\tau\), whose two end edges are \(e_-,e_+\), let

\[
L_\tau
=
\sum_{F\in\tau}\sin\theta_F.
\]

Then the train span is exactly

\[
\boxed{
w_K(\nu_\tau)
=
L_\tau+d_{e_-}+d_{e_+}.
}
\tag{24.5}
\]

Summing over all tracks gives

\[
\boxed{
\sum_\tau w_K(\nu_\tau)
=
2\sum_F\sin\theta_F+H_*,
}
\tag{24.6}
\]

where

\[
\boxed{
H_*=\sum_{e\in\partial\mathcal R}d_e.
}
\tag{24.7}
\]

This completes the earlier directional train-width inequality to an equality.

## 24.4 Linear support-depth budget

Every sufficiently large triangle-free jammed survivor satisfies

\[
\boxed{
H_*
\ge
\left(
2\sqrt{\frac{2\sqrt3}{\pi}}-\sqrt3
\right)n
-
O(n^{2/3}).
}
\tag{24.8}
\]

Numerically,

\[
\boxed{
H_*
\ge
0.3680994640\ldots\,n
-
O(n^{2/3}).
}
\tag{24.9}
\]

Equivalently,

\[
\boxed{
\frac{H_*}{D}
\ge
0.3505458338\ldots\sqrt n-o(\sqrt n).
}
\tag{24.10}
\]

This is an order-\(n\) support-depth constraint.

**Audit derivation of (24.8).** For the full rhombic core,
\(T=B/2=O(D)\) and Mantel gives \(T\ge2\sqrt R\). Uniform width saturation and the
exact train identity give

\[
H_*
\ge
T\bigl(D-O(D^{1/3})\bigr)
-2\sum_F\sin\theta_F.
\]

Moreover

\[
2\sum_F\sin\theta_F
=\sqrt3R+O(D),
\qquad
R=n-O(D),
\qquad
D=\sqrt{cn}+O(1).
\]

Therefore

\[
H_*
\ge
2\sqrt R\,D-\sqrt3R-O(D^{4/3})
=
(2\sqrt c-\sqrt3)n-O(n^{2/3}),
\]

which is (24.8).

## 24.5 Deep-end tail: audit disposition

The earlier continuation recorded a specific numerical lower bound on the number of
macroscopically deep train ends. On second audit, that numerical statement was not
self-contained at this stage because a lower bound on the number of boundary ends is
not, by itself, an upper bound on how widely support depth can be distributed.

The underlying total-depth theorem (24.8)--(24.10) **is retained**. In the pure
rhombic-disk branch, the later audited phase/exposed-hull theorem gives the stronger
bound

\[
\frac{T}{D}\ge 2.5395008183\ldots+o(1),
\]

which in turn yields a rigorous and substantially stronger support-depth tail theorem.
That theorem is proved in Section 44. Thus the old constants are not used as an
independent premise anywhere in v1.0.0.

## 24.6 Important negative conclusion: raw depth is not Oler currency

The coefficient in (24.9) does not directly close the finite packing inequality.

If one attempted a scalar conversion

\[
\mathscr O(A)
\ge
\Lambda \frac{H_*}{D}
-o(\sqrt n),
\]

then the previously identified Oler threshold would require

\[
\boxed{
\Lambda>4.0749855583\ldots.
}
\tag{24.13}
\]

No such valid scalar conversion was obtained.

More strongly, explicit near-equilateral triangular or pentagonal indentation geometries show that a train end can be macroscopically deep while the associated local Oler slack tends to zero.

Therefore:

> **Raw support depth is not an independent positive contribution to Oler surplus.**

Any successful use of \(H_*\) must exploit global transport, support turning, diametral-hull geometry, train coherence, or a variational obstruction.

---

# 25. Exact support-turning and mixed-area identities

The next continuation completed the support-depth bookkeeping. These results supersede any attempt to count \(H_*\) as an independent shell surplus.

For clarity, write the full support depth as

\[
\rho_e^K
=
h_K(\nu_e)-\nu_e\cdot m_e.
\]

This is the same geometric quantity as \(d_e\) above.

## 25.1 Exact train equality

For every finite edge-to-edge strict unit-rhombus complex \(\mathcal R\subset K\),

\[
\boxed{
w_K(\nu_\tau)
=
L_\tau+\rho_{e_-}^K+\rho_{e_+}^K.
}
\tag{25.1}
\]

Hence

\[
\boxed{
\sum_\tau w_K(\nu_\tau)
=
2\sum_{F\in\mathcal R}\sin\theta_F
+
H_\partial^K,
}
\tag{25.2}
\]

where

\[
H_\partial^K
=
\sum_{e\in\partial\mathcal R}\rho_e^K.
\]

## 25.2 Pocket support-turning defect

In the pure rhombic-disk case, consider one indentation pocket \(C\).

Suppose its unit-edge chain has outward normals

\[
\nu_1,\ldots,\nu_r
\]

and its closing hull chord has length \(L\) and outward normal \(n\).

Define

\[
\boxed{
\mathfrak J(C)
=
\sum_{i=1}^r h_K(\nu_i)
-
Lh_K(n).
}
\tag{25.3}
\]

Support-function sublinearity gives

\[
\boxed{
\mathfrak J(C)\ge0.
}
\tag{25.4}
\]

The exact pocket identity is

\[
\boxed{
\sum_{i=1}^r \rho_{e_i}^K
=
2\operatorname{area}(C)
+
\mathfrak J(C).
}
\tag{25.5}
\]

The proof uses

\[
\sum_i\nu_i=Ln
\]

and the signed Green identity

\[
\sum_i\nu_i\cdot m_{e_i}
-
Ln\cdot m_f
=
-2\operatorname{area}(C).
\]

## 25.3 Global pure-disk identity

Let

\[
G=
\operatorname{area}(K)
-
\sum_{F\in\mathcal R}\operatorname{area}(F)
\]

be the total convexification/pocket area and put

\[
\mathfrak J
=
\sum_C\mathfrak J(C).
\]

Then

\[
\boxed{
H_\partial^K
=
2G+\mathfrak J.
}
\tag{25.6}
\]

Combining with the train equality gives

\[
\boxed{
\sum_\tau w_K(\nu_\tau)
=
2\operatorname{area}(K)+\mathfrak J.
}
\tag{25.7}
\]

This is the exact cancellation hidden in the raw support-depth theorem.

## 25.4 Train zonotope formulation

For every train \(\tau\), let \(u_\tau\) be its unit edge direction and define the train zonotope

\[
\boxed{
Z=
\sum_\tau
[-u_\tau/2,u_\tau/2].
}
\tag{25.8}
\]

Then

\[
\boxed{
\operatorname{per}(Z)=B,
}
\tag{25.9}
\]

where \(B\) is the rhombic boundary-edge count.

Mixed area gives

\[
\boxed{
2V(K,Z)
=
\sum_\tau w_K(\nu_\tau).
}
\tag{25.10}
\]

Therefore, in the pure rhombic-disk case,

\[
\boxed{
\mathfrak J
=
2\bigl(
V(K,Z)-\operatorname{area}(K)
\bigr).
}
\tag{25.11}
\]

Thus the order-\(n\) support-turning mass is a mixed-area excess.

## 25.5 Global area and perimeter deficits

For every global minimizer, with no triangle-free or rigidity hypothesis, the later
translated-lattice \(n-1\) improvement in Section 36 strengthens the area-deficit
estimate to

\[
\boxed{
\frac{\pi D^2}{4}
-
\operatorname{area}(K)
<
c_0P.
}
\tag{25.12'}
\]

This supersedes the earlier bound \(c_0\pi D+a_0\).

Also, the stronger pointwise form of Section 24 is

\[
\boxed{
0\le
\pi D(n)-\operatorname{per}(\operatorname{conv}A)
<
\frac{\pi\sqrt3}{2}
}
\tag{25.13}
\]

for every global minimizer in the range where the finite Oler formulation applies.
Thus both the isodiametric area deficit and the perimeter deficit are sharply controlled at boundary scale or better.

## 25.6 Exact cancellation identity

Define

\[
\mathfrak M(K)
=
\frac{DP}{2}
-
2\operatorname{area}(K)
\ge0
\tag{25.14}
\]

The nonnegativity is itself exact. Let \(L=K-K\). Brunn--Minkowski gives
\(\operatorname{area}(L)\ge4\operatorname{area}(K)\). Since \(L\) is centrally
symmetric and has circumradius at most \(D\), its support function satisfies
\(h_L\le D\). The planar Minkowski area formula then gives

\[
\operatorname{area}(L)
=\frac12\int h_L\,dS_L
\le \frac D2\operatorname{per}(L)
=DP,
\]

because \(\operatorname{per}(K-K)=2P\). Hence
\(4\operatorname{area}(K)\le DP\), which is exactly \(\mathfrak M(K)\ge0\).

and

\[
\Delta_\tau
=
\sum_\tau
\left(
D-w_K(\nu_\tau)
\right)
\ge0.
\tag{25.15}
\]

Then

\[
\boxed{
\mathfrak J
=
\frac D2(B-P)
+
\mathfrak M(K)
-
\Delta_\tau.
}
\tag{25.16}
\]

This equation explains exactly why the large support-depth term cannot simply be added to the Oler shell budget: support turning and train-width deficit cancel it.

## 25.7 Sharpened exact contradiction threshold

The support/perimeter bookkeeping first improved the sufficient Oler contradiction
threshold from

\[
\mathscr O(A)\ge c_0\pi D+a_0
\]

to

\[
\mathscr O(A)\ge c_0P+a_0.
\]

Section 36 subsequently removes the remaining \(+a_0\) by proving the stronger
translated-lattice bound

\[
D(n)^2<\frac{2\sqrt3}{\pi}(n-1).
\]

Hence the current exact sufficient threshold is

\[
\boxed{
\mathscr O(A)\ge c_0P.
}
\tag{25.17'}
\]

This is the threshold that should be used from now on.

## 25.8 Exact remaining Target B lemma in the pure rhombic-disk case

Let

\[
E=
\sum_{F\in\mathcal R}
\left(
\sin\theta_F-a_0
\right).
\]

The strengthened shell window from Section 36 gives, for every pure rhombic-disk
global minimizer,

\[
\boxed{
G+E<c_0B.
}
\tag{25.18'}
\]

Therefore a sufficient contradiction is now simply

\[
\boxed{
G+E\ge c_0B.
}
\tag{25.19'}
\]

Equivalently, using

\[
H_\partial^K-\mathfrak J=2G,
\]

it is enough to prove

\[
\boxed{
2E+H_\partial^K-\mathfrak J
\ge
a_0B.
}
\tag{25.20'}
\]

The former \(+a_0\) term is obsolete.

The general topology-corrected version must still incorporate:

- bounded nonquadrilateral faces;
- holes;
- multiple rhombic components;
- vertices outside the rhombic core;
- the bridge-forest residue.

## 25.9 Order-\(n\) support turning has zero guaranteed Oler coefficient

Since

\[
H_\partial^K=2G+\mathfrak J
\]

and \(G\) is only boundary order in the relevant regime, (24.9) implies

\[
\boxed{
\mathfrak J
\ge
\bigl(0.3680994640\ldots+o(1)\bigr)n.
}
\tag{25.21}
\]

This is a genuine order-\(n\) support-turning mass.

However, after the exact subtraction in the Oler identity, the guaranteed usable Oler-surplus coefficient contributed by this term is

\[
\boxed{0.}
\tag{25.22}
\]

This is a decisive strategic correction.

The next proof must work with the residual

\[
\boxed{
H_\partial^K-\mathfrak J=2G,
}
\]

not with \(H_\partial^K\) alone.

---

# 26. Further deductions developed after Sections 24–25

The results in this section were derived from the established theorem stack during the continuation in ChatGPT. They are included because they appear structurally important.

Where a result has not yet received the same adversarial audit as Sections 24–25, that is stated explicitly.

---

## 26.1 Sixfold phase energy of the train graph

For every train \(\tau\), let

\[
\phi_\tau\in\mathbb R/\pi\mathbb Z
\]

be its unoriented edge direction and define

\[
\boxed{
z_\tau=e^{6i\phi_\tau}.
}
\tag{26.1}
\]

If tracks \(\tau,\sigma\) cross, their rhombus has acute angle

\[
\theta_{\tau\sigma}
=
\frac\pi3+\delta_{\tau\sigma}.
\]

Therefore

\[
\frac{z_\sigma}{z_\tau}
=
e^{\pm6i\delta_{\tau\sigma}}
\]

and

\[
|z_\tau-z_\sigma|
\le
6\delta_{\tau\sigma}.
\]

Since \(0<\delta\le\pi/6\),

\[
|z_\tau-z_\sigma|^2
\le
6\pi\delta_{\tau\sigma}.
\]

Summing over crossings gives

\[
\boxed{
\sum_{\tau\sigma\in E(\Gamma)}
|z_\tau-z_\sigma|^2
\le
6\pi\sum_F\delta_F
=
O(D).
}
\tag{26.2}
\]

Since

\[
|E(\Gamma)|=F_4=\Theta(D^2),
\]

the average sixfold phase energy per crossing is \(O(D^{-1})\).

This converts the local statement “almost every rhombus is nearly \(60^\circ\)” into a global coherence constraint on train orientations.

### Status

The derivation of (26.2) is elementary from the established angular-defect theorem.

---

## 26.2 Macroscopic grain decomposition

Fix \(0<\eta<1\).

Delete every train crossing with

\[
\delta_{\tau\sigma}>D^{-1+\eta}.
\]

Because

\[
\sum\delta_{\tau\sigma}=O(D),
\]

only

\[
O(D^{2-\eta})=o(D^2)
\]

crossings are deleted.

Next repeatedly delete any track of current degree \(<\lambda D\), for fixed \(\lambda>0\).

Since there are \(T=O(D)\) tracks, this deletes at most

\[
O(\lambda D^2)
\]

additional crossings.

Every surviving component has minimum degree \(\lambda D\), while containing only \(O(D)\) tracks. A shortest-path neighborhood argument therefore bounds its graph diameter by \(O_\lambda(1)\).

Consequently all tracks in one surviving component have sixfold phases differing by

\[
O_\lambda(D^{-1+\eta}).
\]

Thus every component has a phase \(\phi_0\) such that

\[
\boxed{
\phi_\tau
=
\phi_0
+
k_\tau\frac\pi3
+
O_\lambda(D^{-1+\eta})
\pmod\pi,
\qquad
k_\tau\in\{0,1,2\}.
}
\tag{26.3}
\]

Hence, for every fixed \(\varepsilon>0\), after deleting at most \(\varepsilon n+o(n)\) rhombi, the remaining rhombic bulk is a bounded number of macroscopic grains, each asymptotically aligned with one triangular-lattice orientation modulo \(60^\circ\).

A quantitative choice such as defect cutoff \(D^{-2/3}\) yields an all-but-\(O(n^{5/6})\) version with \(O(n^{1/6})\) components and phase error \(O(D^{-1/3})\).

### Status

This is a direct graph-theoretic consequence of (26.2) and the already established \(T=O(D)\) train bound. It should nevertheless receive a short audit before being promoted into the core report.

---

## 26.3 Scalar phase-potential structure inside a grain

Choose local representatives of the three direction classes as

\[
A:\quad \phi=a,
\]

\[
B:\quad \phi=\frac\pi3+b,
\]

\[
C:\quad \phi=\frac{2\pi}3+c,
\]

where the offsets are small.

Then strict triangle-freeness gives, at a crossing,

\[
A\text{-}B:
\qquad
b-a>0,
\]

\[
B\text{-}C:
\qquad
c-b>0,
\]

\[
C\text{-}A:
\qquad
a-c>0.
\tag{26.4}
\]

Thus crossing incidences inside a coherent grain can be oriented by a genuine scalar phase potential.

Any directed cycle in this induced inequality system is impossible.

This is a promising way to replace arbitrary defect transport by an ordered continuation network.

### Status

The local sign calculation is exact. Its strongest global combinatorial consequence has not yet been fully extracted.

---

## 26.4 Train zonotope: missing crossings and mixed area

For the train zonotope

\[
Z=
\sum_\tau[-u_\tau/2,u_\tau/2],
\]

one has

\[
\operatorname{area}(Z)
=
\sum_{\tau<\sigma}
|\det(u_\tau,u_\sigma)|.
\tag{26.5}
\]

Let

\[
S=
\sum_{F\in\mathcal R}\sin\theta_F
\]

and define the missing-crossing determinant mass

\[
M
=
\sum_{\substack{\tau<\sigma\\
\tau,\sigma\text{ do not cross}}}
|\det(u_\tau,u_\sigma)|.
\]

Because each crossing pair contributes exactly one rhombus,

\[
\boxed{
\operatorname{area}(Z)
=
S+M.
}
\tag{26.6}
\]

Combined with (25.10),

\[
2V(K,Z)
=
2S+H_\partial^K.
\]

Thus both support depth and missing train crossings have exact convex-geometric interpretations.

---

## 26.5 Exact zonotope anisotropy identity

Define

\[
C_k
=
\sum_\tau e^{2ik\phi_\tau}.
\]

The Fourier expansion of the zonotope support function gives

\[
\boxed{
\operatorname{per}(Z)^2
-
4\pi\operatorname{area}(Z)
=
8\sum_{k\ge1}
\frac{|C_k|^2}{4k^2-1}.
}
\tag{26.7}
\]

In a hexatically coherent grain,

\[
|C_3|
=
(1-o(1))T_{\rm grain}.
\]

Therefore its zonotopal completion obeys

\[
\boxed{
P_Z^2
-
4\pi A_Z
\ge
\frac8{35}
(1-o(1))
T_{\rm grain}^2.
}
\tag{26.8}
\]

So a macroscopic triangularly coherent grain has a quantitatively anisotropic zonotopal completion, even though the true minimizing hull satisfies

\[
P(K)=\pi D-O(1)
\]

and is asymptotically constant-width.

### Strategic interpretation

A large survivor must reconcile strongly anisotropic crystalline train systems with an almost constant-width diametral hull through only a boundary-order defect network.

Scalar mixed-area inequalities alone appear too weak; the missing information is the **incidence/transport structure** of the trains.

---

## 26.6 Train-angle realization modes

A pure rhombic complex admits train-coordinate realizations.

Choose a side label

\[
\epsilon_\tau(v)\in\{0,1\}
\]

for each vertex relative to every train.

Up to translation,

\[
p_v
=
\sum_\tau
\epsilon_\tau(v)u_\tau.
\tag{26.9}
\]

Replacing each train vector \(u_\tau\) independently by another unit vector preserves every rhombic contact length.

Thus an unconstrained pure rhombic complex carries one angle parameter per train.

Modulo global Euclidean motions, this suggests at least

\[
\boxed{
T-1
}
\tag{26.10}
\]

independent train-angle modes before the defect/hull shell constraints are imposed.

### Strategic interpretation

The \(n-O(D)\) rhombic bulk carries \(\Theta(D)\) natural shear modes, and the \(O(D)\)-scale hull/defect structure must lock them all.

### Status

The train-coordinate representation is standard for simply connected rhombic tilings. Extension across holes, multiple components, and all topologies in the full survivor requires explicit hypothesis management before this becomes a universal theorem.

---

## 26.7 Difference-body transport bound for a convex defect face

Let \(F\) be a convex unit-sided contact face.

For each side \(e\), let \(\nu_e\) be its outward normal.

Then the polygonal mixed-area formula gives

\[
\boxed{
\sum_{e\subset\partial F}
w_F(\nu_e)
=
\operatorname{area}(F-F).
}
\tag{26.11}
\]

The planar Rogers-Shephard difference-body inequality gives

\[
\boxed{
\operatorname{area}(F-F)
\le
6\operatorname{area}(F).
}
\tag{26.12}
\]


For completeness, the planar constant \(6\) can be derived self-containedly. Put
\(C=F-F\) and

\[
f(x)=\operatorname{area}(F\cap(F+x)),
\qquad x\in C.
\]

Fubini gives

\[
\int_C f(x)\,dx=\operatorname{area}(F)^2.
\]

Moreover \(g=f^{1/2}\) is concave on \(C\): for \(x,y\in C\), convexity gives

\[
(1-t)(F\cap(F+x))+t(F\cap(F+y))
\subseteq
F\cap(F+((1-t)x+ty)),
\]

and planar Brunn--Minkowski yields concavity of square roots of areas. Along every
ray from \(0\) to \(\partial C\),

\[
g(rx)\ge(1-r)g(0),
\qquad 0\le r\le1.
\]

Integrating the square of this cone lower bound over homothetic shells \(rC\) gives

\[
\int_C f(x)\,dx
\ge
\frac16\operatorname{area}(F)\operatorname{area}(C).
\]

Comparison with the Fubini identity proves (26.12). Thus no external use of the
full Rogers--Shephard theorem is needed here.

Hence

\[
\boxed{
\sum_{e\subset\partial F}
w_F(\nu_e)
\le
6\operatorname{area}(F).
}
\tag{26.13}
\]

A weighted analogue applies to an outer convex pocket: the unit-edge chain cannot absorb more than a constant multiple of the pocket area in local transverse width.

### Consequence

A boundary-order amount of defect-face/pocket area can absorb only boundary-order local width.

Therefore the order-\(n\) global support-depth mass cannot be interpreted as order-\(n\) *local defect-cell width*. Most depth is transported globally through the rhombic body.

This reinforces the exact cancellation in Section 25.

---

## 26.8 Correction: large \(H_*\) is not itself anomalous

A disk-like family of chord tracks naturally has quadratic total support-depth deficit.

For a Euclidean disk of radius \(R=D/2\), a unit-spaced parallel family has asymptotic missing span

\[
\int_{-R}^{R}
\left(
2R-2\sqrt{R^2-x^2}
\right)\,dx
=
(4-\pi)R^2.
\tag{26.14}
\]

Thus one family naturally contributes

\[
\left(1-\frac\pi4\right)D^2,
\]

and two such families contribute

\[
\boxed{
\left(
2-\frac\pi2
\right)D^2
=
0.4292036\ldots D^2.
}
\tag{26.15}
\]

The Section 24 lower bound is only approximately

\[
0.3338\,D^2.
\]

Therefore a quadratic \(H_*\) is compatible with ordinary disk-like geometry.

The anomaly is not the **amount** of raw depth; it is the need to realize it simultaneously with:

- strict triangle-freeness;
- almost-equilateral rhombi;
- diametral hull vertices;
- near-constant width;
- exact global diameter optimality;
- boundary-order Oler budget;
- locking of all train/shear modes.

This correction should be treated as a regression test against future scalar-depth arguments.

---

## 26.9 Fixed-oblique-lattice scaling heuristic

Suppose a large relevant region really lies in a single rank-two unit lattice generated by two unit vectors at angle

\[
\theta>\frac\pi3.
\]

The fundamental-cell area is

\[
s=\sin\theta>a_0.
\]

A finite lattice-polygon capacity estimate of Pick/Oler type gives schematically

\[
n
\lesssim
\frac{\pi D^2}{4\sin\theta}
+
O(D).
\]

Combining with the global competitor

\[
D^2<\frac{2\sqrt3}{\pi}n
\]

forces

\[
\boxed{
\theta-\frac\pi3
=
O(D^{-1}).
}
\tag{26.16}
\]

This identifies the natural final scale:

\[
\boxed{
\delta\asymp D^{-1}.
}
\]

Bulk density loss from a positive shear and boundary-order gains compete exactly at this scale.

### Status

This scaling conclusion is highly plausible and consistent with the exact capacity calculations. Any use of the precise finite-lattice formula or lattice-point constants should be independently checked before becoming part of the trusted theorem stack.

---

# 27. Historical post-synthesis route log

The intermediate Sections 27--35 of the pre-v1 addendum were strategic working
notes rather than independent theorem blocks. Their surviving mathematical content
is retained elsewhere in this report:

- raw support depth is quadratic but is cancelled by support turning and cannot be
  converted directly into Oler surplus;
- low-slack defect cells should be viewed as train continuation/merge structures,
  not as local scalar penalties;
- the sixfold phase energy motivates a polycrystalline decomposition into
  near-triangular grains;
- pure rhombic disks carry train-angle realization modes that must be locked by the
  boundary shell;
- Target A remains the separate super-boundary bridge-forest problem;
- the essential regression examples are the unit square, the \(n=8\) rattler,
  regular odd-prime shells, dense shell fillings, five-sector \(C_5\) complexes,
  the 11-point sun, near-equilateral low-slack pockets, and disk-like chord depth.

The old numerical thresholds and "current frontier" language from those sections
are superseded by Sections 38--48 below and are intentionally not duplicated here.

---

# 36. Translated-lattice \(n-1\) improvement

This section records a later exact improvement that supersedes every previous
\(n\)-based triangular-lattice upper bound in the report.

## 36.1 Strict \(n-1\) diameter upper bound

Let \(\Lambda\) be the unit triangular lattice, whose fundamental-cell area is

\[
a_0=\frac{\sqrt3}{2}.
\]

Choose an open disk \(B_r\) so that the average number of lattice points in a
translated copy is exactly \(n-1\):

\[
\frac{\pi r^2}{a_0}=n-1.
\]

Periodize the indicator of \(B_r\) over \(\Lambda\).  The resulting translated
lattice-point count is integer valued and has mean \(n-1\).

It is not constant.  Indeed, choose a generic point of one circular boundary
away from all pairwise boundary intersections.  Crossing that boundary changes
the periodized count by exactly one locally.

An integer-valued nonconstant function with integer mean \(n-1\) must exceed its
mean somewhere.  Hence some translate of the open disk contains at least \(n\)
lattice points.

Any \(n\) of them are unit-separated and, because the disk is open, have
diameter strictly less than \(2r\).  Therefore

\[
\boxed{
D(n)
<
\sqrt{\frac{2\sqrt3}{\pi}(n-1)}.
}
\tag{36.1}
\]

Equivalently,

\[
\boxed{
D(n)^2
<
c(n-1),
\qquad
c=\frac{2\sqrt3}{\pi}.
}
\tag{36.2}
\]

This is unconditional.

## 36.2 Topology-corrected shell consequence

For a rhombic complex \(\mathcal R\), recall

\[
n=R+\frac B2+\chi+t,
\]

and

\[
\operatorname{area}(K)
=
a_0R+E_{\mathcal R}+G_{\mathcal R}.
\]

The isodiametric inequality and (36.2) give

\[
\operatorname{area}(K)
<
a_0(n-1).
\]

Hence

\[
\boxed{
G_{\mathcal R}+E_{\mathcal R}
<
c_0B+a_0(t+\chi-1).
}
\tag{36.3}
\]

Combined with the existing Oler lower side,

\[
G_{\mathcal R}+E_{\mathcal R}
\ge
c_0(B-P)+a_0(t+\chi-1),
\]

the exact remaining shell window becomes

\[
\boxed{
c_0(B-P)+a_0(t+\chi-1)
\le
G_{\mathcal R}+E_{\mathcal R}
<
c_0B+a_0(t+\chi-1).
}
\tag{36.4}
\]

Its width is exactly

\[
\boxed{c_0P.}
\tag{36.5}
\]

All previous \(+a_0\) closing thresholds are superseded.

## 36.3 Pure rhombic disk

For \(t=0,\chi=1\),

\[
\boxed{
c_0(B-P)
\le
G+E
<
c_0B.
}
\tag{36.6}
\]

Thus the exact sufficient contradiction is

\[
\boxed{
G+E\ge c_0B.
}
\tag{36.7}
\]

## 36.4 Oler-surplus and area-deficit consequences

The Oler surplus

\[
\mathscr O(A)
=
\operatorname{area}(K)+c_0P-a_0(n-1)
\]

satisfies

\[
\boxed{
0\le\mathscr O(A)<c_0P.
}
\tag{36.8}
\]

Also,

\[
\boxed{
\frac{\pi D^2}{4}
-
\operatorname{area}(K)
<
c_0P.
}
\tag{36.9}
\]

The Cartesian-block restriction sharpens correspondingly to

\[
\boxed{
ab+
\frac{4\sqrt3-6}{\pi}\Delta_{a,b}
<
\frac2\pi(n-1).
}
\tag{36.10}
\]

---

# 37. Train-angle Hessian and the exact backward-train mechanism

This section records the exact second-variation identities found by projecting the
diameter objective into train-angle coordinates.

Assume for this section a simply connected pure rhombic disk so that standard
train coordinates are available.

Let

\[
u_\tau=(\cos\phi_\tau,\sin\phi_\tau)
\]

be the unit edge vector of train \(\tau\).

For vertices \(i,j\), write

\[
r=p_i-p_j
=
\sum_\tau d_\tau u_\tau,
\qquad
d_\tau\in\{-1,0,1\}.
\]

Let

\[
f_{ij}(\phi)
=
\frac12|r|^2.
\]

## 37.1 Exact Hessian trace

Let

\[
k_{ij}
=
\#\{\tau:d_\tau\ne0\}.
\]

Differentiation with respect to the independent train angles gives

\[
\boxed{
\operatorname{tr}\nabla_\phi^2 f_{ij}
=
k_{ij}-|p_i-p_j|^2.
}
\tag{37.1}
\]

For an active diameter pair,

\[
|p_i-p_j|=D,
\]

hence

\[
\boxed{
\operatorname{tr}\nabla_\phi^2 f_{ij}
=
k_{ij}-D^2
\le
T-D^2
=
-\Theta(D^2).
}
\tag{37.2}
\]

Thus each active diameter function is strongly superharmonic in aggregate on the
train-angle space.

## 37.2 Exact signed-variance formula

Put

\[
a_\tau=d_\tau u_\tau,
\qquad
\lambda_\tau=r\cdot a_\tau.
\]

For an angle velocity \(v=(v_\tau)\), set

\[
c=\sum_\tau v_\tau a_\tau.
\]

The first variation of the diameter vector is \(Jc\). First-order neutrality is

\[
r\cdot Jc=0.
\]

In the plane this means \(c\) is parallel to \(r\). Since

\[
r\cdot c=\sum_\tau\lambda_\tau v_\tau,
\]

write

\[
\bar v=
\frac{1}{D^2}\sum_\tau\lambda_\tau v_\tau,
\qquad
c=\bar v\,r.
\]

Using \(\sum_\tau\lambda_\tau=D^2\), the exact second variation is

\[
\boxed{
\mathrm d^2f_{ij}[v,v]
=
-\sum_\tau
\lambda_\tau(v_\tau-\bar v)^2.
}
\tag{37.3'}
\]

This identity is valid with arbitrary signs of \(\lambda_\tau\). If every
\(\lambda_\tau\ge0\), it is nonpositive; equality requires common angular velocity
on all trains with positive \(\lambda_\tau\).

## 37.3 What backward and tangent trains can do

A separating train is **backward** for the diameter pair if

\[
\boxed{
\lambda_\tau=d_\tau\,r\cdot u_\tau<0.
}
\tag{37.4}
\]

Equation (37.3') shows that **positive quadratic curvature requires at least one
backward incidence whose deviation \(v_\tau-\bar v\) is nonzero**.

The second-pass audit corrects an earlier overstatement: this does *not* classify all
higher-order locking. A separating train with

\[
d_\tau\ne0,
\qquad
\lambda_\tau=0
\]

is tangent to the diameter vector and contributes no quadratic sign, but balanced
classes of such tangent trains can block at quartic order. That exact mechanism is
proved in Section 43. A train with \(d_\tau=0\) is instead invisible to this particular
diameter bar at every order.

## 37.4 Coordinate-flip obstruction

If \(a_\tau=d_\tau u_\tau\) is backward, then

\[
|r-a_\tau|^2
=
D^2+1-2r\cdot a_\tau
>
D^2.
\tag{37.6}
\]

Hence the coordinate-flipped extreme vertex cannot exist while all other train
coordinates are held fixed; otherwise the configuration would already contain a
pair longer than \(D\).

This gives the geometric interpretation of backwardness:

> a backward train certifies a missing train-coordinate flip.

The natural next step is to propagate this missing flip along the ordered train to
its terminal boundary/fault structures and charge it without overcounting.

## 37.5 Proposed boundary backtracking estimate (UNPROVED)

The following estimate is a research target, not an available theorem. A suitable
boundary arc of length \(L\) joining a diameter pair has not been defined with a
non-overcounted charging map. If such an arc and charging map can be constructed,
one would seek

\[
\boxed{
\sum_{\lambda_\tau<0}
(-\lambda_\tau)
\le
\frac D2(L-D).
}
\tag{37.7}
\]

Until that missing construction is supplied, (37.7) must not be used to bound
positive curvature or to close a rank contradiction.

## 37.6 Pure-disk hull contact degree

At a hull vertex of a pure strict-rhombic disk, if the contact degree is \(d\),
then \(d-1\) rhombi occupy the convex interior angle.

Every rhombic corner is \(>\pi/3\), while the hull interior angle is \(<\pi\).
Therefore

\[
(d-1)\frac\pi3<\pi
\]

and

\[
\boxed{d\le3.}
\tag{37.8}
\]

Thus each diametral hull reaction is transmitted into the rhombic bulk through
only two or three unit bars.

---

---

# 38. Second-pass audit ledger for the recent work

This section is authoritative for the disposition of claims developed after the
post-synthesis addendum.

## 38.1 Claims that survive the second review

The following are retained as established under their stated hypotheses:

- the strict translated-lattice bound
  \[
  D(n)^2<\frac{2\sqrt3}{\pi}(n-1);
  \]
- the sharpened topology-corrected shell window and, in a pure rhombic disk,
  \[
  G+E<c_0B;
  \]
- the perimeter deficit \(\pi D-P=O(1)\), isodiametric area deficit \(O(D)\),
  and uniform width estimate \(\min w_K=D-O(D^{1/3})\);
- the exact support-depth, support-turning, pocket, and mixed-area identities;
- the sixfold phase-energy inequality and macroscopic grain decomposition;
- the train-coordinate realization of a simply connected pure rhombic disk;
- the exact train-angle gradient, Hessian, trace, and signed-variance formulas;
- the forbidden-coordinate-flip interpretation of a strict backward incidence;
- the stress-projected signed train-Laplacian identity and its negative-coupling
  positive-inertia bound;
- the backward-flip rank/equality-space dichotomy proved below;
- the terminal-pair localization of every separating train with \(\lambda\le0\);
- the generalized phase-atomic/exposed-hull theorem proved in Section 39, which
  strengthens the earlier full-cusp exclusion theorem;
- the secondary stressed-cusp theorem and tangent transfer identity of Section 42;
- the conditional invisible-coordinate continuation lemma for a lexicographically maximal pure representative;
- the existence of a genuine quartic tangent-class blocking mechanism.

## 38.2 Claims corrected or downgraded

The audit made the following changes.

### (a) Tangent trains cannot be discarded

The old sentence that every genuinely positive higher-order blocker must be
"backward or diameter-invisible" is false. Strict backward trains are necessary for
positive **quadratic** curvature. At quadratic equality, separating tangent trains
with \(\lambda=0\) can produce positive quartic curvature.

### (b) Corrected tangent expansion

A previous expansion through sixth order omitted the generally present term
\(-DS_5t^5/60\). The corrected expansion appears in Section 43. The omission does
not invalidate the main quartic conclusion because, when \(S_3=0\) and \(S_2\ne0\),
the positive \(t^4\) term dominates all fifth-order terms for sufficiently small
nonzero \(t\).

### (c) Full backward rank has an equality alternative

Local optimality does not by itself imply that the strict backward-flip map is
injective. The correct statement is:

\[
\operatorname{rank}\mathcal B=\dim\mathcal L
\]

**or** its kernel is contained in the exact quadratic-equality space of at least one
active diameter bar. The equality branch is precisely where tangent quartic locking
lives.

### (d) One diameter bar can have linear quartic capacity

It is false that one active diameter bar can kill only \(O(1)\) higher-order modes.
A same-oriented class of \(2s\) parallel tangent trains can quartically block an
\(s\)-dimensional paired-angle subspace. Any final proof must therefore charge train
classes / fault structure, not merely active diameter bars.

### (e) Two bar-rotation values are not a proved global flex theorem

For a secondary stress, two rotation values strongly constrain the bars in the
*stress support*. However an unsupported active equality bar can still block the
same train-angle line at higher order. Therefore no theorem in v1.0.0 claims that
"two rotation classes imply a global same-diameter family" without an additional
support-saturation hypothesis.

### (f) The old deep-end numerical claim is superseded

The old deep-end constants are not used as an independent lemma. Section 44 derives
a stronger pure-disk tail estimate from the newly audited lower bound on \(T/D\).

## 38.3 Claims still unproved

The following remain targets, not theorems:

- an ordered pseudoline/matroid bound forcing insufficient rank for the combined
  backward/tangent shell blockers;
- a conversion from that rank failure to \(G+E\ge c_0B\) in the general
  topology-corrected shell;
- an extension of the pure train-angle argument across all \(O(D)\) exceptional
  faces, holes, components, and outside vertices;
- the super-boundary forest-capacity theorem \(\ell=O(D)\) in Target A.

---

# 39. Generalized phase-atomic and exposed-hull theorem

This section strengthens the earlier full first-order cusp exclusion. It applies to
**every** sufficiently large triangle-free pure-rhombic-disk global minimizer in the
jammed branch.

Let \(R\) be the number of rhombi, \(T\) the number of trains, and \(q\) the number
of hull/diameter vertices. Then

\[
n=R+T+1,
\qquad
B=2T,
\qquad
R=n-O(D),
\qquad
T=\Theta(D),
\qquad
\frac{R}{D^2}\to\frac1c.
\tag{39.1}
\]

For train \(\tau\), let \(\phi_\tau\in\mathbb R/\pi\mathbb Z\) be its unoriented
direction and put

\[
\mu_T=\frac1T\sum_\tau\delta_{\phi_\tau}.
\]

Pass to an arbitrary subsequence on which \(\mu_T\) converges weakly to a probability
measure \(\mu\). Let \(s\) be the total mass of the atomic part of \(\mu\), and write

\[
y=\lim\frac qT
\]

along a further subsequence.

## 39.1 Leading crossing mass is carried only by phase atoms

For a crossing pair \(\tau,\sigma\), the rhombus defect satisfies

\[
\operatorname{dist}_{S^1}(6\phi_\tau,6\phi_\sigma)
\le6\delta_{\tau\sigma},
\]

and

\[
\sum_{\tau\sigma\in E(\Gamma)}\delta_{\tau\sigma}=O(D)=O(T).
\]

To keep the normalization explicit, define the symmetric **ordered** crossing
measure

\[
\eta_T
=\frac1{T^2}
\sum_{\{\tau,\sigma\}\in E(\Gamma)}
\left(
\delta_{(\phi_\tau,\phi_\sigma)}+
\delta_{(\phi_\sigma,\phi_\tau)}
\right).
\tag{39.2a}
\]

Its total mass is \(2R/T^2\). Since the crossing graph is simple,
\(\eta_T\) is dominated on rectangles, up to the vanishing diagonal term, by
\(\mu_T\times\mu_T\). The defect estimate and Markov's inequality imply that any
weak limit \(\eta\) is supported on the projective \(60^\circ\)-relation

\[
\mathcal S=
\{(\phi,\psi):\psi-\phi\equiv\pm\pi/3\pmod\pi\}.
\]

For a product measure, this graph has mass only through atoms:

\[
(\mu\times\mu)(\mathcal S)
=
\int \bigl(\mu\{\phi+\pi/3\}+\mu\{\phi-\pi/3\}\bigr)\,d\mu(\phi),
\]

so the non-atomic part of \(\mu\) carries no positive-density crossing mass.
Restricting to the atomic train mass, the limiting crossing graph remains
triangle-free because every finite train-crossing graph is triangle-free. Weighted
Mantel therefore gives an unordered edge density at most one quarter of the square
of the total atomic mass:

\[
\boxed{
\limsup\frac{R}{T^2}\le\frac{s^2}{4}.
}
\tag{39.2}
\]

This formulation is deliberately weaker than saying that the whole train measure is
atomic. A survivor may retain a non-atomic train population; that population simply
cannot carry \(\Theta(T^2)\) crossings.

## 39.2 Exposed hull chains force non-atomic train mass

The \(2T\) outer rhombic boundary edges are partitioned into \(q\) chains between
consecutive convex-hull vertices. Every hull side has length at least \(1\).

Fix a large integer \(M\). At most \(2T/(M+1)\) of these chains contain more than
\(M\) unit edges. Thus

\[
q-O(T/M)
\]

chains have bounded length.

Now choose finitely many atoms of \(\mu\) carrying at least \(s-\varepsilon\) of
its atomic mass. Fix these atoms, fix \(M\), and let \(U_\delta\) be disjoint
\(\delta\)-neighborhoods of their projective directions. If a bounded chain uses
only train ends whose directions lie in \(U_\delta\), its hull chord is a sum of at
most \(M\) such unit vectors. Because the chord has length at least \(1\), its
normal lies in a finite union \(V_{M,\delta}\) of arcs whose total circular measure
is \(O_M(\delta)\). The constant is uniform for sufficiently small \(\delta\):
the lower bound on the chord length excludes the cancellation singularity.

On the other hand, after scaling by \(D\), the minimizing hulls converge in Hausdorff
distance to the disk of diameter \(1\): the area deficit is \(O(D)\), so every
subsequential convex limit has diameter at most \(1\) and maximal area \(\pi/4\),
forcing the disk. The corresponding perimeter/surface-area measures converge weakly
to the non-atomic circular measure. In the plane this can be seen directly from
support functions: after translation, Hausdorff convergence is uniform convergence
of \(h_K\), while the curvature/perimeter measure is \(h_K+h_K''\) in the
distributional sense, so it converges weakly to the constant measure of the disk.
Since every hull side has length at least \(1\), the number of bounded chains whose
entire terminal-direction list lies in \(U_\delta\) is at most
\[
C_M\delta T+o_\delta(T).
\]
This is \(O(\delta T)\) for fixed \(\delta\), not \(o(T)\) for a fixed neighborhood.
Apart from these chains and the \(O(T/M)\) long chains, every hull chain contains a
train end outside \(U_\delta\). In the weak limit the fraction of trains capable of
supplying such an end is at most \(1-s+\varepsilon+o(1)\), and each such train has
only two terminal ends. Consequently

\[
\frac qT
\le C_M\delta+o_\delta(1)+2(1-s+\varepsilon)+O(1/M).
\]

Let \(T\to\infty\) first, then \(\delta\downarrow0\), then \(M\to\infty\), and
finally \(\varepsilon\downarrow0\). This gives

\[
\boxed{
s\le1-\frac y2.
}
\tag{39.3}
\]

Consequently,

\[
\boxed{
\limsup\frac{R}{T^2}
\le
\frac14\left(1-\frac y2\right)^2.
}
\tag{39.4}
\]

## 39.3 Exact pinned-rank lower bound on \(q/T\)

For a pure rhombic disk,

\[
|E(C)|=2R+T,
\qquad
n=R+T+1.
\]

Let \(e_{QQ}\) be the number of contact edges with both endpoints on the pinned
hull. Pinned rigidity gives

\[
2R+T-e_{QQ}\ge2(R+T+1-q),
\]

hence

\[
\boxed{
2q\ge T+2+e_{QQ},
\qquad
q\ge\frac T2+1.
}
\tag{39.5}
\]

Thus every asymptotic limit has \(y\ge1/2\).

## 39.4 Quantitative train and hull ratios

Put

\[
x=\frac TD.
\]

Because \(R/D^2\to1/c\), (39.4) gives

\[
\boxed{
x\ge\frac{2}{\sqrt c(1-y/2)}+o(1).}
\tag{39.6}
\]

Using \(y\ge1/2\),

\[
\boxed{
\liminf\frac TD
\ge
\frac8{3\sqrt c}
=2.5395008183\ldots.
}
\tag{39.7}
\]

Therefore

\[
\boxed{
\liminf\frac BD
\ge
5.0790016366\ldots.
}
\tag{39.8}
\]

Since \(q\le P=\pi D+o(D)\), one also has \(xy\le\pi+o(1)\). Combining with
(39.6) yields

\[
\boxed{
\limsup\frac qT
\le
\frac{2C_0}{4+C_0}
=0.9039456812\ldots.
}
\tag{39.9}
\]

Thus

\[
\boxed{
\liminf\frac{T-q}{D}
\ge
\frac{4-C_0}{2\sqrt c}
=0.3338292869\ldots.
}
\tag{39.10}
\]

This strengthens the earlier theorem \(q<T\) to a macroscopic linear gap.

---

# 40. Macroscopic first-order-neutral train space

Let \(H\) be the set of active diameter pairs and work in the train-angle quotient

\[
V=\mathbb R^T/\langle\mathbf1\rangle,
\qquad
\dim V=T-1.
\]

For \(h\in H\), let \(g_h\) be the train-angle gradient of
\(f_h=|r_h|^2/2\). The ordinary normalized KKT stress satisfies

\[
\sum_{h\in H}\beta_hg_h=0,
\qquad
\beta_h\ge0,
\qquad
\sum_h\beta_h=1,
\]

because every unit contact is exactly preserved by train-angle first variations.
Hence

\[
\operatorname{rank}\{g_h:h\in H\}\le |H|-1.
\]

The diameter graph on the \(q\) convex-hull vertices has at most \(q\) edges. Here is
a self-contained support-cone proof. For a diameter pair \(h=ij\), orient

\[
r=p_i-p_j.
\]

Then \(p_i\) is the **unique** maximizer of \(r\cdot x\) on \(K\), and \(p_j\) is
the unique minimizer. Indeed, if \(x\ne p_i\) shared the maximum support value, then
\(r\cdot(x-p_i)=0\) and

\[
|x-p_j|^2
=|r+(x-p_i)|^2
=D^2+|x-p_i|^2>D^2,
\]

a contradiction; the minimum case is identical.

For a convex \(q\)-gon, the directions on \(S^1\) for which a fixed vertex is the
unique support maximizer form the interior of its normal cone. These \(q\) open
normal-cone intervals partition the circle up to their \(q\) boundary rays. The
unique support minimizer is the maximizer in the antipodal direction, so the common
refinement of the maximizer partition and its antipodal copy has at most \(2q\) open
cells. On each cell the ordered pair (unique maximizer, unique minimizer) is constant.

The direction \(r/D\) of every oriented diameter pair lies in one of these open
cells, and distinct ordered diameter pairs require distinct cells. Every unordered
diameter pair appears twice, in antipodal cells with the two orientations reversed.
Therefore

\[
2|H|\le2q,
\qquad
\boxed{|H|\le q}.
\tag{40.0}
\]

This is the only diameter-graph edge bound needed below.

Define

\[
\mathcal L=\bigcap_{h\in H}\ker g_h\subset V.
\]

Then

\[
\boxed{
\dim\mathcal L\ge T-|H|\ge T-q.
}
\tag{40.1}
\]

Combining with (39.10),

\[
\boxed{
\dim\mathcal L
\ge
0.3338292869\ldots D-o(D).
}
\tag{40.2}
\]

Therefore the higher-order problem is intrinsically macroscopic: a survivor must
block \(\Theta(D)\) independent train-angle directions after all first-order
diameter gradients have been annihilated.

The former "full first-order train cusp" is consequently impossible as an immediate
corollary, with a fixed asymptotic gap rather than merely \(q<T\).

---

# 41. Stress-projected signed train Laplacian

Retain the pure simply connected train-coordinate representation

\[
p_v=p_0+\sum_{\tau=1}^T\epsilon_\tau(v)u_\tau,
\qquad
u_\tau=(\cos\phi_\tau,\sin\phi_\tau).
\]

For an oriented active diameter pair \(h=ij\), write

\[
r_h=\sum_\tau d_{h\tau}u_\tau,
\qquad
 a_{h\tau}=d_{h\tau}u_\tau,
\qquad
\lambda_{h\tau}=r_h\cdot a_{h\tau},
\]

and \(k_h=\#\{\tau:d_{h\tau}\ne0\}\).

The gradient and Hessian are

\[
(g_h)_\tau=r_h\cdot J a_{h\tau},
\tag{41.1}
\]

\[
(H_h)_{\tau\tau}=d_{h\tau}^2-\lambda_{h\tau},
\qquad
(H_h)_{\tau\sigma}=a_{h\tau}\cdot a_{h\sigma}
\quad(\tau\ne\sigma).
\tag{41.2}
\]

Fix any normalized KKT stress \((\alpha,\beta)\). For train \(\tau\), put

\[
A_\tau=\sum_{e\text{ a contact edge of }\tau}\alpha_e.
\]

Define

\[
M_{\tau\sigma}
=(u_\tau\cdot u_\sigma)
\sum_h\beta_h d_{h\tau}d_{h\sigma}.
\tag{41.3}
\]

Using the virtual-work field \(\xi_v=\epsilon_\tau(v)u_\tau\) gives

\[
\boxed{
A_\tau=\sum_h\beta_h\lambda_{h\tau}\ge0,
\qquad
\sum_\sigma M_{\tau\sigma}=A_\tau.
}
\tag{41.4}
\]

Therefore the stress-weighted train Hessian

\[
Q=\sum_h\beta_hH_h
\]

is exactly

\[
\boxed{
Q
=-\sum_{\tau<\sigma}
M_{\tau\sigma}
(e_\tau-e_\sigma)(e_\tau-e_\sigma)^{\mathsf T}.
}
\tag{41.5}
\]

Its trace is

\[
\boxed{
\operatorname{tr}Q
=\sum_h\beta_h(k_h-D^2)
\le T-D^2
=-\Theta(D^2).
}
\tag{41.6}
\]

If \(N_\beta\) is the graph of train pairs for which \(M_{\tau\sigma}<0\), then on
any train-angle subspace \(W\), the positive index obeys

\[
\boxed{
n_+(Q|_W)
\le
\operatorname{rank}
(B_{N_\beta}^{\mathsf T}|_W).
}
\tag{41.7}
\]

Indeed, the terms with \(M\ge0\) are negative semidefinite; all positive inertia is
contained in the span of incidence vectors belonging to negative couplings.

**Limitation.** A fixed KKT stress is not known to make \(Q\) nonnegative on the
whole critical space; the second-order normal stress may depend on the chosen
critical direction. Thus (41.7) is a rank diagnostic, not by itself a contradiction.

---

# 42. Backward-flip rank, terminal localization, and the secondary cusp

For \(v\in\mathcal L\), define

\[
s_h(v)=\frac1{D^2}\sum_\tau\lambda_{h\tau}v_\tau,
\qquad
\ell_{h\tau}(v)=v_\tau-s_h(v).
\tag{42.1}
\]

The exact neutral signed-variance identity is

\[
\boxed{
H_h[v,v]
=-\sum_\tau
\lambda_{h\tau}\ell_{h\tau}(v)^2.
}
\tag{42.2}
\]

## 42.1 Backward-flip map

Define

\[
\mathcal B:\mathcal L\to
\mathbb R^{\{(h,\tau):\lambda_{h\tau}<0\}},
\qquad
(\mathcal Bv)_{h\tau}=\ell_{h\tau}(v).
\tag{42.3}
\]

For each active bar put

\[
\mathcal Z_h=
\left\{
 v\in\mathcal L:
 \ell_{h\tau}(v)=0
 \text{ for every }\lambda_{h\tau}>0
\right\}.
\tag{42.4}
\]

On \(K=\ker\mathcal B\), equation (42.2) becomes

\[
H_h[v,v]
=-\sum_{\lambda_{h\tau}>0}
\lambda_{h\tau}\ell_{h\tau}(v)^2
\le0.
\tag{42.5}
\]

Therefore a locally diameter-minimal strict-rhombic realization satisfies the exact
dichotomy

\[
\boxed{
\operatorname{rank}\mathcal B=\dim\mathcal L
\quad\text{or}\quad
\ker\mathcal B\subseteq\mathcal Z_h
\text{ for some active }h.
}
\tag{42.6}
\]

**Proof.** If \(K\ne0\) and no \(\mathcal Z_h\) contains \(K\), then the finite union
of proper subspaces \(K\cap\mathcal Z_h\) cannot cover \(K\). Choose
\(v\in K\) outside their union. Then every active diameter has
\(H_h[v,v]<0\). Along the exact train-angle line \(\phi+tv\), all unit contacts stay
unit and every active diameter decreases to second order; all inactive inequalities
retain their strict slack for sufficiently small \(t\). This contradicts global (and
local) diameter minimality. \(\square\)

Thus full higher-order survival requires either at least \(\dim\mathcal L\) independent
backward-flip covectors, or a genuine tangent/equality branch.

## 42.2 Forbidden coordinate flip

If \(\lambda_{h\tau}<0\), then

\[
\boxed{
|r_h-a_{h\tau}|^2
=D^2+1-2\lambda_{h\tau}>D^2.
}
\tag{42.7}
\]

Hence the train-coordinate vertex obtained by toggling \(\tau\) toward the opposite
endpoint cannot exist with all other train coordinates fixed. Each backward row is
therefore an actual missing coordinate flip, not a merely formal Hessian sign.

Rows belonging to the same train have the form

\[
 e_\tau^*-s_h^*.
\]

Modulo the span of the bar-rotation functionals \(s_h^*\), all rows from one train
have the same class \([e_\tau^*]\). Repeated use of one terminal train cannot create
arbitrary rank for free; extra rank is carried explicitly by the bar-rotation space.

## 42.3 Terminal localization for every nonpositive separating train

Let \(h=ij\) be an active diameter and let \(\tau\) separate its endpoints.
If

\[
\lambda_{h\tau}\le0,
\]

then **both terminal boundary edges of \(\tau\) are non-hull edges**.

For \(\lambda<0\), orient either disk-boundary arc from \(j\) to \(i\). It crosses
\(\tau\) at one terminal edge with displacement \(a_{h\tau}\). A hull edge on either
convex-hull chain from the minimum support point \(j\) to the maximum support point
\(i\) has nonnegative \(r_h\)-projection, contradicting \(\lambda<0\).

For \(\lambda=0\), a hull terminal edge would be perpendicular to \(r_h\) and hence
would lie in a support face perpendicular to \(r_h\). Those maximum and minimum
support faces are singletons: if \(x\ne p_i\) shared the maximum support value with
\(p_i\), then

\[
|x-p_j|^2
=D^2+|x-p_i|^2>D^2.
\]

Thus equality is impossible as well.

Consequently, every strict-backward or tangent separating train consumes a pair of
non-hull terminal edges.

## 42.4 Secondary-cusp theorem

Take nonzero \(v\in\ker\mathcal B\), so every active diameter has
\(H_h[v,v]\le0\). Put

\[
E(v)=\{h:H_h[v,v]=0\}.
\]

Then

\[
\boxed{
0\in\operatorname{conv}\{g_h:h\in E(v)\}.
}
\tag{42.8}
\]

Otherwise strict separation supplies a train-angle acceleration \(w\) with
\(g_h\cdot w<0\) for every \(h\in E(v)\). For

\[
\phi(t)=\phi+t v+\frac{\varepsilon t^2}{2}w,
\]

the coefficient

\[
H_h[v,v]+\varepsilon g_h\cdot w
\]

is negative for every equality bar and remains negative for all bars with
\(H_h[v,v]<0\) when \(\varepsilon\) is sufficiently small. Every active diameter
would decrease to second order, contradicting minimality.

More strongly, apply the direction-dependent second-order normal-stress theorem to
this critical velocity. Along the exact train-angle path every unit contact has
identically constant length. Applying the first-order equilibrium identity to the
path acceleration converts the theorem's velocity-square expression exactly into
the weighted second derivative of the diameter functions. Thus it supplies a
normalized proper stress \((\alpha^{(v)},\beta^{(v)})\) for which

\[
\sum_h\beta_h^{(v)}H_h[v,v]
=
\sum_h\beta_h^{(v)}|\dot r_h|^2
-
\sum_e\alpha_e^{(v)}|\dot r_e|^2
\ge0.
\]

Every summand is nonpositive, hence

\[
\boxed{
\beta_h^{(v)}>0
\Longrightarrow
h\in E(v),
\qquad
\sum_h\beta_h^{(v)}H_h[v,v]=0.
}
\tag{42.9}
\]

Thus every surviving equality direction carries an actual **secondary stressed
cusp** supported only on second-order-flat diameter bars.

## 42.5 Train-by-train vector balance and tangent transfer

For the secondary stress, use the virtual field
\(\xi_x=\epsilon_\tau(x)w\) with arbitrary \(w\in\mathbb R^2\). This gives the vector
identity

\[
\boxed{
\sum_{h\in E(v)}
\beta_h d_{h\tau}r_h
=A_\tau u_\tau,
\qquad
A_\tau\ge0.
}
\tag{42.10}
\]

Suppose \(h\) is a stress-supported equality bar, \(\tau\) separates its endpoints,
and

\[
\lambda_{h\tau}=0,
\qquad
v_\tau\ne s_h(v).
\]

The term \(\beta_h d_{h\tau}r_h\) is nonzero and perpendicular to \(u_\tau\), whereas
the right side of (42.10) is parallel to \(u_\tau\). Another stress-supported bar
\(k\ne h\) must therefore separate \(\tau\) and have a nonzero perpendicular
component.

There is at most one active diameter segment in any prescribed unoriented direction:
if two distinct parallel length-\(D\) segments differed by a nonzero translation
\(s\), then

\[
|r+s|^2+|r-s|^2=2D^2+2|s|^2,
\]

so one cross-distance would exceed \(D\). Hence \(k\) cannot also be tangent to
\(\tau\); therefore \(\lambda_{k\tau}\ne0\).

Since \(k\in E(v)\), equality in (42.5) forces

\[
\boxed{
v_\tau=s_k(v).
}
\tag{42.11}
\]

Thus every moving tangent train of a stress-supported bar transports an exact
**difference of diameter-bar rotation potentials**:

\[
\boxed{
v_\tau-s_h=s_k-s_h.}
\tag{42.12}
\]

This is a major refinement of the raw quartic model. Tangent velocities in an actual
secondary cusp are not arbitrary; they are coupled to rotation potentials of other
loaded diameter bars.


## 42.6 Proposed invisible-coordinate selection (UNPROVED)

Call a train \(\tau\) **globally invisible to the active diameter support** if

\[
d_{h\tau}=0\qquad(h\in H).
\tag{42.13}
\]

There is a useful canonical-selection idea, but the first-event argument below has
an unresolved triangle-wall case.

> **Proposed Lemma 42.6.** Among all
> triangle-free global minimizers for a fixed \(n\), choose one first maximizing the
> number of unit contacts and then maximizing the number of active diameter pairs.
> **If that lexicographically maximal representative is a pure strict-rhombic disk,**
> then it has no globally invisible train.

The proposed proof varies an invisible train until the first constraint event. A
first event may be a rhombus reaching the \(60^\circ\) boundary, which creates a
unit triangle. That endpoint is not an admissible triangle-free minimizer, so it
does not contradict the lexicographic choice. The other first events (a new
triangle-free unit contact or a new active diameter pair) would give the intended
contradiction, but they do not exhaust the possibilities. No downstream theorem
may invoke Lemma 42.6 until this gap is closed. Section 53 correctly keeps the
local same-diameter train-flat alternative instead of relying on this lemma.

This lemma does **not** say that every pure survivor can be replaced by a pure
lexicographically maximal survivor; the canonical selection can change the contact
complex. It is therefore retained as an auxiliary normalization, not used in the
main pure-disk contradiction unless that compatibility is established.

---

# 43. Corrected tangent-class higher-order expansion

Fix an active diameter bar \(h\) and a direction \(v\in\mathcal L\) satisfying the
quadratic equality conditions for \(h\). Subtract the common bar rotation
\(s_h(v)\). Every separating train with \(\lambda\ne0\) is then stationary relative
to the bar. Only tangent trains

\[
d_{h\tau}\ne0,
\qquad
\lambda_{h\tau}=0
\]

can move it.

Let

\[
e_h=\frac{r_h}{D},
\qquad
 a_{h\tau}=\sigma_{h\tau}J e_h,
\qquad
\sigma_{h\tau}\in\{\pm1\},
\]

and let

\[
w_\tau=v_\tau-s_h(v).
\]

Define the signed moments

\[
S_m=\sum_\tau\sigma_{h\tau}w_\tau^m.
\tag{43.1}
\]

First-order neutrality gives

\[
S_1=0.
\tag{43.2}
\]

The exact bar change is

\[
\Delta r_h(t)
=
-\left(\sum_\tau\sigma_{h\tau}\sin(w_\tau t)\right)e_h
+
\left(\sum_\tau\sigma_{h\tau}(\cos(w_\tau t)-1)\right)J e_h.
\tag{43.3}
\]

Therefore the corrected expansion is

\[
\boxed{
\begin{aligned}
|r_h(t)|^2-D^2
={}&
\frac D3S_3t^3
+
\frac{S_2^2}{4}t^4
-
\frac D{60}S_5t^5\\
&+
\left(
\frac{S_3^2}{36}
-
\frac{S_2S_4}{24}
\right)t^6
+O(t^7).
\end{aligned}
}
\tag{43.4}
\]

The omitted fifth-order term is the principal formula correction made in the
v1.0.0 audit.

Consequences:

1. if \(S_3\ne0\), one sign of \(t\) decreases this diameter at cubic order;
2. if \(S_3=0\) and \(S_2\ne0\), the positive \(t^4\) term dominates, so the bar is a
   genuine two-sided quartic blocker for sufficiently small nonzero \(t\);
3. if \(S_2=S_3=0\), still higher signed moments must be examined.

## 43.1 One bar can have linear quartic capacity

Suppose \(2s\) tangent trains have the same oriented contribution

\[
a_{h\tau_j}=\sigma J e_h
\]

and choose paired relative velocities

\[
w_{2j-1}=x_j,
\qquad
w_{2j}=-x_j.
\]

Then exactly

\[
\boxed{
|r_h(t)|^2-D^2
=
\left[
2\sum_{j=1}^s(\cos(x_jt)-1)
\right]^2.
}
\tag{43.5}
\]

Its leading term is

\[
t^4\left(\sum_{j=1}^s x_j^2\right)^2.
\]

Thus one active diameter can quartically block an \(s\)-dimensional paired train
subspace. This definitively rules out any closing argument that charges only one
higher-order mode per active diameter bar.

## 43.2 What simultaneous optimality adds

Equation (43.5) is a valid warning model, but Section 42.5 shows that in a genuine
secondary stressed cusp every moving tangent train of a supported bar must satisfy

\[
w_\tau=s_k-s_h
\]

for another supported diameter bar \(k\). Hence the true residual object is an
ordered train network carrying differences of bar-rotation potentials, not a set of
independent paired variables.

This coupling is established. What is **not** established is that the potential
network has too little rank, or that two potential values automatically produce a
global flex. Unsupported active equality bars remain a possible higher-order
obstruction.

---

# 44. Additional audited quantitative consequences

## 44.1 Stronger pure-disk support-depth theorem

For a pure rhombic disk, the exact train identity gives

\[
H_\partial^K
=
\sum_\tau w_K(\nu_\tau)
-2\sum_F\sin\theta_F.
\]

Uniform width saturation gives

\[
\sum_\tau w_K(\nu_\tau)
=TD-o(D^2),
\]

while

\[
2\sum_F\sin\theta_F
=\sqrt3R+o(D^2)
=\frac\pi2D^2+o(D^2).
\]

Therefore

\[
\boxed{
\frac{H_\partial^K}{D^2}
=
\frac TD-\frac\pi2+o(1).
}
\tag{44.1}
\]

Using (39.7),

\[
\boxed{
H_\partial^K
\ge
0.9687044915\ldots D^2-o(D^2)
}
\tag{44.2}
\]

and, since \(D^2/n\to c\),

\[
\boxed{
H_\partial^K
\ge
1.0681495546\ldots n-o(n).
}
\tag{44.3}
\]

This does **not** create Oler surplus: \(H_\partial^K=2G+\mathfrak J\), and the
order-\(n\) support-turning term \(\mathfrak J\) still cancels.

## 44.2 Audited support-depth tail

Every support depth satisfies \(0\le\rho_e^K\le D\), and there are \(2T\) train ends.
For fixed \(0<a<1/2\), let \(N_a\) be the number with

\[
\rho_e^K\ge aD.
\]

Then

\[
H_\partial^K
\le
N_aD+(2T-N_a)aD.
\]

Combining with (44.1), for every fixed \(a\) for which the numerator below is
positive,

\[
\boxed{
\liminf\frac{N_a}{D}
\ge
\frac{
\frac8{3\sqrt c}(1-2a)-\frac\pi2
}{1-a}.
}
\tag{44.4}
\]

For the clean choice \(a=0.1\),

\[
\boxed{
N_{0.1}
\ge
0.5120048087\ldots D-o(D)
=
0.5376435191\ldots\sqrt n-o(\sqrt n).
}
\tag{44.5}
\]

This is the audited replacement for the earlier, weaker deep-end numerical claim.

## 44.3 Boundary curvature identity

Let \(h_2,h_3\) count hull boundary vertices of contact degree \(2,3\); let
\(r_3,r_4,r_5\) count non-hull boundary vertices of degree \(3,4,5\); and let
\(i_5\) count interior degree-five vertices. In a pure strict-rhombic disk, Euler and
degree counting give

\[
\boxed{
h_2=4+r_4+2r_5+i_5.
}
\tag{44.6}
\]

Since \(q=h_2+h_3\) and the boundary has \(2T\) vertices,

\[
\boxed{
r_3\ge2(T-q)+4.
}
\tag{44.7}
\]

Using (39.10),

\[
\boxed{
r_3
\ge
0.6676585739\ldots D-o(D).
}
\tag{44.8}
\]

Thus a hypothetical pure survivor has a linear family of non-hull degree-three
reflex boundary vertices. These are natural terminal resources for any future
missing-flip/fault-wall rank theorem.

---

# 45. Current exact Target B frontier

The pure-rhombic-disk branch is now forced into the following simultaneous regime:

\[
\boxed{
\begin{array}{c}
G+E<c_0B,\\[1mm]
q/T\le0.9039456812\ldots+o(1),\\[1mm]
T/D\ge2.5395008183\ldots+o(1),\\[1mm]
(T-q)/D\ge0.3338292869\ldots-o(1),\\[1mm]
\dim\mathcal L\ge0.3338292869\ldots D-o(D),\\[1mm]
\text{full first-order train locking is impossible},\\[1mm]
\text{quadratic survival requires full backward-flip rank or an equality kernel},\\[1mm]
\text{every nonpositive separating train terminates twice off-hull},\\[1mm]
\text{every equality-kernel direction carries a secondary stressed cusp},\\[1mm]
\text{moving tangent trains transport differences of bar-rotation potentials},\\[1mm]
\text{one tangent class can nevertheless have linear quartic capacity.}
\end{array}
}
\tag{45.1}
\]

The exact unresolved pure-disk theorem can therefore be stated as follows.

> **Ordered higher-order shell-rank theorem (open).** In a sufficiently large
> triangle-free pure-rhombic-disk global minimizer with \(G+E<c_0B\), the ordered
> pseudoline/fault network cannot simultaneously support either
>
> 1. full rank of the backward-flip map on the macroscopic neutral space
>    \(\mathcal L\); or
> 2. a residual secondary cusp whose tangent train classes provide enough quartic
>    rank to block the remaining kernel,
>
> unless a rhombus phase difference becomes exactly zero (equivalently an acute
> angle is exactly \(60^\circ\)), a forbidden Cartesian block appears, or there is an
> actual diameter-decreasing feasible motion.

The most concrete data available for proving this theorem are:

- each backward/tangent train has a pair of non-hull terminals;
- same-phase train families are internally noncrossing and ordered;
- leading crossing mass lies in a small number of near-triangular phase classes;
- tangent velocities are exact differences \(s_k-s_h\) of loaded diameter-bar
  potentials;
- the shell contains at least \(0.6676585739D-o(D)\) degree-three reflex boundary
  vertices;
- one cannot charge by active-bar cardinality because of the quartic tangent-class
  example;
- one cannot charge raw support depth because of support-turning cancellation.

## 45.1 General topology correction remains necessary

Even a proof of the pure-disk theorem is not by itself the entire jammed branch.
The actual almost-rhombic core may have \(O(D)\) exceptional nonquadrilateral faces,
holes, multiple components, and vertices outside the rhombic complex. The Oler shell
window already handles these corrections exactly at scalar level, but the
train-coordinate/higher-order rank argument must either be extended through them or
combined with a reduction that removes them without losing global optimality.

Thus Target B has two final layers:

1. close the pure ordered higher-order shell-rank theorem;
2. make the argument topology-correct at the same boundary scale.


# 46. Fixed-angle oblique lattice exclusion

The remaining almost-rhombic branch cannot be an exact finite patch of a
unit-rhombic lattice whose angle stays macroscopically away from the triangular
angles.  The proof uses only a fundamental-cell packing estimate and the strict
translated-triangular-lattice upper bound for \(D(n)\).

Let \(u,v\) be unit vectors with angle
\[
\theta\in[\,\pi/3,\ 2\pi/3\,],
\tag{46.1}
\]
and let
\[
\Lambda_\theta=\mathbb Zu+\mathbb Zv.
\]
For any finite \(P\subset\Lambda_\theta\) with \(|P|=n\), put
\(K=\operatorname{conv}P\) and \(D_P=\operatorname{diam}P\).

> **Theorem 46.1 (fixed-angle oblique-lattice exclusion).** For every
> \(\delta\in(0,\pi/6)\), there is \(N_\delta\) such that no \(n\)-point global
> minimizer can be a subset \(P\subset\Lambda_\theta\) with
> \[
> \theta\in[\pi/3+\delta,\ 2\pi/3-\delta]
> \tag{46.2}
> \]
> whenever \(n\ge N_\delta\).

### Proof

Use the centered fundamental parallelogram
\[
F_\theta=\{su+tv:-\tfrac12\le s,t<\tfrac12\}.
\tag{46.3}
\]
Its translates by \(\Lambda_\theta\) tile the plane, its area is
\(\sin\theta\), and \(F_\theta\subseteq\mathbb B\).  The last assertion follows
because the squared norm is convex in \((s,t)\), so its maximum on the closed
coefficient square occurs at a corner, where
\[
\left|\frac{\pm u\pm v}{2}\right|^2
=\frac{1\pm\cos\theta}{2}\le1.
\tag{46.4}
\]
The \(n\) cells \(p+F_\theta\), \(p\in P\), are disjoint and lie in
\(K+\mathbb B\).  Steiner's formula, followed by the isodiametric and
Cauchy inequalities, gives
\[
n\sin\theta
\le\operatorname{area}(K+\mathbb B)
=\operatorname{area}K+\operatorname{per}K+\pi
\le\frac{\pi D_P^2}{4}+\pi D_P+\pi.
\tag{46.5}
\]

For a global minimizer, the strict triangular-lattice comparison gives
\[
D_P^2=D(n)^2<\frac{2\sqrt3}{\pi}n.
\tag{46.6}
\]
With \(a_0=\sqrt3/2\) and \(c=2\sqrt3/\pi\), (46.5)--(46.6) imply
\[
n(\sin\theta-a_0)
<
\pi\sqrt{cn}+\pi.
\tag{46.7}
\]
On the interval (46.2),
\[
\sin\theta-a_0
\ge \sin(\pi/3+\delta)-a_0
=:b_\delta>0.
\tag{46.8}
\]
The left side of (46.7) is therefore at least \(nb_\delta\), while the right side
is \(O_\delta(\sqrt n)\), a contradiction for all sufficiently large \(n\).
\(\square\)

The estimate also gives the quantitative necessary condition for any exact
one-lattice survivor in the reduced angle range:
\[
\boxed{
\sin\theta-\frac{\sqrt3}{2}=O(n^{-1/2}).
}
\tag{46.9}
\]
The endpoint \(\theta=2\pi/3\) is equivalent, after replacing \(v\) by \(-v\), to
the triangular angle \(\pi/3\).  Thus the theorem removes fixed-angle oblique
lattice bulk, but it does not remove a varying-angle or nonlattice rhombic mesh.
In particular, it supplies no higher-order shell rank and does not close Target B.


# 47. Fixed affine-lattice bulk exclusion

The preceding argument does not depend on equal basis lengths.  It extends to
every fixed rank-two affine lattice and gives the exact scale at which a lattice
deformation can remain competitive with the triangular comparison.

Let \(u,v\) be linearly independent vectors, let
\[
\Lambda=\mathbb Zu+\mathbb Zv,
\qquad
a_\Lambda=|\det(u,v)|,
\tag{47.1}
\]
and put
\[
R_\Lambda=\frac12\max\{|u+v|,\ |u-v|\}.
\tag{47.2}
\]
For a finite \(n\)-point subset \(P\subset\Lambda\), write
\(K=\operatorname{conv}P\) and \(D_P=\operatorname{diam}P\).

> **Theorem 47.1 (fixed affine-lattice exclusion).** Every such P satisfies
> \[
> n a_\Lambda
> \le \operatorname{area}\bigl(K+\mathbb B(0,R_\Lambda)\bigr)
> \le \frac{\pi}{4}(D_P+2R_\Lambda)^2.
> \tag{47.3}
> \]
> If P is a global minimizer, then with
> \(c=2\sqrt3/\pi\),
> \[
> \boxed{
> a_\Lambda-\frac{\sqrt3}{2}
> <
> \pi R_\Lambda\sqrt{\frac cn}
> +\frac{\pi R_\Lambda^2}{n}.
> }
> \tag{47.4}
> \]
> In particular, every fixed lattice with
> \(a_\Lambda>\sqrt3/2\) is excluded as the carrier of sufficiently large global
> minimizers.

### Proof

Use the half-open centered fundamental parallelogram
\[
F=\{su+tv:-\tfrac12\le s,t<\tfrac12\}.
\tag{47.5}
\]
Its translates tile the plane, each has area \(a_\Lambda\), and
\(F\subseteq\mathbb B(0,R_\Lambda)\).  Indeed, the squared norm is convex in
\((s,t)\), so its maximum on the closed coefficient square occurs at a corner,
where the norm is one of \(|u+v|/2\) or \(|u-v|/2\).  Hence the \(n\) disjoint
cells \(p+F\), \(p\in P\), lie in \(K+\mathbb B(0,R_\Lambda)\), proving the
first inequality in (47.3).

The Minkowski sum in (47.3) has diameter at most \(D_P+2R_\Lambda\), so the
isodiametric inequality proves the second.  For a global minimizer, the strict
triangular-lattice comparison gives
\[
D_P^2=D(n)^2<c n.
\tag{47.6}
\]
Substitution into (47.3) yields
\[
n a_\Lambda
<
\frac{\pi}{4}(\sqrt{cn}+2R_\Lambda)^2
=\frac{\sqrt3}{2}n+\pi R_\Lambda\sqrt{cn}+\pi R_\Lambda^2,
\]
which is (47.4). \(\square\)

Thus any sequence of exact affine-lattice survivors must have covolume
\(a_\Lambda-\sqrt3/2=O(n^{-1/2})\) when \(R_\Lambda=O(1)\).  This removes fixed
anisotropic affine bulk, but leaves affine lattices whose covolume approaches the
triangular value at the boundary scale, as well as nonlattice meshes and exterior
boundary constraints.  It supplies no higher-order shell rank and does not close
Target B.


# 48. Bounded-displacement affine-lattice exclusion

Exact lattice membership is stronger than needed.  Let \(P=\{p_1,\ldots,p_n\}\)
be an \(n\)-point configuration and suppose there are distinct points
\(z_1,\ldots,z_n\) in a fixed affine lattice \(\Lambda=\mathbb Zu+\mathbb Zv\)
such that
\[
|p_i-z_i|\le\varepsilon
\qquad(1\le i\le n).
\tag{48.1}
\]
Define \(a_\Lambda\) and \(R_\Lambda\) as in (47.1)--(47.2), and put
\(K=\operatorname{conv}P\), \(D_P=\operatorname{diam}P\).

> **Theorem 48.1 (near-lattice cell bound).** Under (48.1),
> \[
> \boxed{
> n a_\Lambda
> \le
> \operatorname{area}\bigl(K+\mathbb B(0,R_\Lambda+\varepsilon)\bigr)
> \le
> \frac{\pi}{4}\bigl(D_P+2R_\Lambda+2\varepsilon\bigr)^2.
> }
> \tag{48.2}
> \]
> If P is a global minimizer, then with \(c=2\sqrt3/\pi\),
> \[
> \boxed{
> a_\Lambda-\frac{\sqrt3}{2}
<
> \pi(R_\Lambda+\varepsilon)\sqrt{\frac cn}
> +\frac{\pi(R_\Lambda+\varepsilon)^2}{n}.
> }
> \tag{48.3}
> \]

### Proof

Take the centered fundamental parallelogram \(F\) from (47.5).  Its translates
by \(\Lambda\) are disjoint and have area \(a_\Lambda\), while
\(F\subseteq\mathbb B(0,R_\Lambda)\).  Since \(z_i\) is within \(\varepsilon\)
of \(p_i\in K\),
\[
z_i+F\subseteq K+\mathbb B(0,R_\Lambda+\varepsilon).
\]
The \(n\) cells are disjoint, proving the first inequality in (48.2).  The
Minkowski sum has diameter at most \(D_P+2R_\Lambda+2\varepsilon\), so the
isodiametric inequality proves the second.

For a global minimizer, \(D_P^2=D(n)^2<c n\).  Substituting into (48.2) gives
\[
n a_\Lambda
<
\frac{\pi}{4}\bigl(\sqrt{cn}+2R_\Lambda+2\varepsilon\bigr)^2
=\frac{\sqrt3}{2}n
 +\pi(R_\Lambda+\varepsilon)\sqrt{cn}
 +\pi(R_\Lambda+\varepsilon)^2,
\]
which is (48.3). \(\square\)

For fixed \(R_\Lambda\) and uniformly bounded \(\varepsilon\), (48.3) still
excludes every fixed lattice with \(a_\Lambda>\sqrt3/2\) for all sufficiently
large n.  Thus a near-lattice survivor must either use a lattice whose covolume
approaches the triangular value at the \(n^{-1/2}\) boundary scale, or have no
single global affine carrier.  The theorem does not control piecewise lattices,
unbounded displacement, or exterior boundary constraints, so the Target B shell
rank problem remains open.

# 49. Quantized defect on train cycles

The sixfold phase estimate controls total angular defect, but it does not say
which train cycles can carry that defect. A closed train cycle has an arithmetic
refinement.

Let
\[
\phi_0,\phi_1,\ldots,\phi_m=\phi_0\pmod\pi
\]
be a closed walk in the train-crossing graph of a strict-rhombic complex. For
the crossing between \(\phi_i\) and \(\phi_{i+1}\), let
\[
\theta_i=\frac{\pi}{3}+\delta_i,
\qquad
0<\delta_i\le\frac{\pi}{6},
\tag{49.1}
\]
be the acute angle of the corresponding rhombus. Choose the signed lift of
each projective direction change so that
\[
\phi_{i+1}-\phi_i=\varepsilon_i\theta_i,
\qquad
\varepsilon_i\in\{-1,+1\}.
\tag{49.2}
\]
After recursively choosing the lifts, closure means
\[
\sum_{i=0}^{m-1}\varepsilon_i\theta_i=k\pi
\tag{49.3}
\]
for some integer \(k\). Put \(S=\sum_i\varepsilon_i\).

> **Lemma 49.1 (mod-three phase-cycle charge).** If
> \(S\not\equiv0\pmod3\), then
> \[
> \boxed{\sum_{i=0}^{m-1}\delta_i\ge\frac{\pi}{3}.}
> \tag{49.4}
> \]
> Consequently, if \(\eta_i=\sin\theta_i-\sqrt3/2\) is the area surplus of
> the \(i\)-th rhombus over the triangular value, then
> \[
> \boxed{\sum_{i=0}^{m-1}\eta_i\ge2-\sqrt3.}
> \tag{49.5}
> \]

### Proof

Subtract \((\pi/3)S\) from (49.3):
\[
\sum_i\varepsilon_i\delta_i
=\pi\left(k-\frac S3\right).
\tag{49.6}
\]
If \(S\not\equiv0\pmod3\), the right side has absolute value at least
\(\pi/3\). Since
\[
\left|\sum_i\varepsilon_i\delta_i\right|\le\sum_i\delta_i,
\]
(49.4) follows.

On \(0\le\delta\le\pi/6\), concavity of sine places
\(\sin(\pi/3+\delta)-\sin(\pi/3)\) above the chord from \(0\) to \(\pi/6\):
\[
\sin\left(\frac\pi3+\delta\right)-\frac{\sqrt3}{2}
\ge\frac{6(1-\sqrt3/2)}{\pi}\,\delta.
\tag{49.7}
\]
Multiplying (49.4) by the coefficient in (49.7) gives
\(\sum_i\eta_i\ge2-\sqrt3\). \(\square\)

The same conclusion applies to any edge-disjoint family of such cycles:
their total area surplus is at least \((2-\sqrt3)\) times the number of
cycles. Thus a global \(O(D)\) area-defect budget allows only \(O(D)\)
edge-disjoint mod-three-charged cycles.

This is a refinement of the phase-potential observation. Cycles with
\(S\equiv0\pmod3\) are not charged by this lemma; they form the residual
three-balanced network that a closing theorem must analyze. The lemma also
does not by itself provide a large edge-disjoint family of charged cycles,
nor does it handle exceptional faces and holes. It therefore narrows, but
does not close, the ordered higher-order shell-rank theorem.

## 49.1 The exact \(\mathbb Z/3\) obstruction

There is a useful graph-theoretic way to state what remains after the charged
cycles are removed. Discard the right-angle rhombi for this paragraph, and let
\(G_{<}\) be the train-crossing graph on the remaining edges. The deletion is
only an exceptional \(O(D)\)-scale operation: a right-angle rhombus has
\(\delta=\pi/6\), so the global angular-defect estimate bounds their number by
\(O(D)\). For an oriented edge \(e=(\tau,\sigma)\), put

\[
\gamma(e)=\varepsilon_e\in\mathbb Z/3,
\qquad
\gamma(\sigma,\tau)=-\gamma(\tau,\sigma),
\tag{49.8}
\]

where \(\varepsilon_e\) is the signed projective direction change in (49.2).
For \(\theta_e<\pi/2\) this sign is determined by the two projective
directions; the reverse-edge convention makes the gain antisymmetric.

> **Lemma 49.2 (three-class potential).** Let \(H\) be a connected subgraph
> of \(G_{<}\). The following are equivalent:
>
> 1. every closed walk \(W\) in \(H\) has
>    \(\sum_{e\in W}\gamma(e)=0\) in \(\mathbb Z/3\);
> 2. there is a map \(\lambda:V(H)\to\mathbb Z/3\), unique up to an additive
>    constant, such that
>    \[
>    \gamma(\tau,\sigma)=\lambda(\sigma)-\lambda(\tau)\pmod3
>    \tag{49.9}
>    \]
>    on every oriented edge of \(H\).

### Proof

Fix a root \(r\). Under (1), define \(\lambda(v)\) to be the gain sum of any
path from \(r\) to \(v\), reduced modulo \(3\). Two such paths give a closed
walk after reversing one of them, so (1) makes the value independent of the
chosen path. Appending the edge \((\tau,\sigma)\) proves (49.9). Conversely,
the gains telescope around every closed walk. Changing the root value adds a
constant to every \(\lambda(v)\), and this is the only freedom. \(\square\)

The potential has a direct geometric interpretation. Along a path
\(\tau_0,\ldots,\tau_m\), choose the recursive signed lifts from (49.2). Then

\[
\phi_{\tau_m}-\phi_{\tau_0}
\equiv
\frac{\pi}{3}\bigl(\lambda(\tau_m)-\lambda(\tau_0)\bigr)
\;+\;
\sum_{i=0}^{m-1}\varepsilon_i\delta_i
\pmod\pi.
\tag{49.10}
\]

Thus a three-balanced component has three discrete phase classes, with all
failure of exact triangular alignment represented by the additive defect term
in (49.10). In particular, if a closed walk \(W\) in such a component has
\(\sum_{e\in W}\delta_e<\pi\), then (49.6) and \(S\equiv0\pmod3\) force

\[
\sum_{e\in W}\varepsilon_e\delta_e=0.
\tag{49.11}
\]

The conclusion is deliberately local. Lemma 49.1 controls the number of
edge-disjoint nonzero-gain cycles by area surplus, but an edge-disjoint-cycle
packing bound is not an upper bound for the size of a feedback edge set in an
arbitrary dense graph. Therefore (49.8)--(49.11) do not justify deleting only
\(O(D)\) edges to obtain a three-class potential. A closing argument previously
needed either a structural bound on the gain-graph feedback set for train
arrangements, or a direct way to exploit the potential despite many overlapping
charged cycles. **Superseded:** PC in the promoted 2026-09-05 addendum proves
an explicit feedback bound `floor(3 Delta/pi)` directly from the phase-circle
geometry. It does not infer a feedback bound from cycle packing alone.

## 49.2 Audit: no facial localization in the train graph

An attempted extension of Lemma 49.1 tried to localize the gain charge on bounded
faces of \(G_{<}\).  That extension is **rejected**.  The train-crossing graph has
one vertex for each train and one edge for each crossing; it is an intersection
graph, not the planar rhombus complex.  In the pure branch,
\[
|V(G_{<})|=O(D),
\qquad
|E(G_{<})|=R-O(D)=\Theta(D^2).
\]
The established two-crossing exclusion makes this a simple graph, so for large D
it cannot have a planar embedding: a simple planar graph with \(T\) vertices has
at most \(3T-6\) edges.  Consequently \(G_{<}\) has no inherited bounded-face
system, and the proposed facial charge \(\chi(f)\), charged-face estimate, and
dual-cut conclusion are not valid.

The physical rhombic complex is planar, but the gain labels in (49.8) live on pairs
of trains rather than on edges of that planar 1-skeleton.  A valid face-localization
theorem would require a new planar incidence or cocycle construction that preserves
the train-pair gain; none is supplied here.  Lemmas 49.1 and 49.2 remain valid, as
does their explicit warning that an edge-disjoint-cycle budget does not control a
general gain-graph feedback set.

---

# 50. Dense low-defect cores are exactly three-phase-balanced

The cycle charge can be combined with the linear train count to produce an exact
potential on every sufficiently dense low-defect component.  This is stronger than
weak phase concentration: the surviving component has no nonzero-gain cycle at all.

Let \(\Gamma=(V,E)\) be the train-crossing graph of a pure strict-rhombic disk,
write \(T=|V|\), and assign to each crossing \(e\) its angular defect
\(\delta_e\in(0,\pi/6]\).  Let \(\Gamma_{<}\) denote the graph after omitting
right-angle crossings (\(\delta_e=\pi/6\)); these are among the high-defect edges
deleted below for all sufficiently large \(D\).  On the remaining edges the signed
\(\mathbb Z/3\) gain is the one defined in Section 49.  The established shell
estimates give constants \(C_\delta,C_T\), independent of the disk, with

\[
\sum_{e\in E}\delta_e\le C_\delta D,
\qquad
T\le C_TD.
\tag{50.1}
\]

For an oriented edge \(e=(\tau,\sigma)\) of \(\Gamma_{<}\), let
\(\gamma(e)\in\mathbb Z/3\) be the signed phase gain from Section 49, so that
\(\gamma(\sigma,\tau)=-\gamma(\tau,\sigma)\).

> **Theorem 50.1 (dense-core three-phase potential).** Fix
> \(0<\eta<1\) and \(0<\lambda<1\).  Form \(\Gamma_{D,\eta,\lambda}\) by first
> deleting every edge with
> \(\delta_e>D^{-1+\eta}\), and then repeatedly deleting every vertex whose
> current degree is less than \(\lambda D\).  For all sufficiently large \(D\),
> every connected component \(H\) of the remaining graph has a potential
> \(\ell:V(H)\to\mathbb Z/3\) satisfying
> \[
> \boxed{\gamma(\tau,\sigma)=\ell(\sigma)-\ell(\tau)\pmod3}
> \tag{50.2}
> \]
> on every oriented edge of \(H\).  The number of deleted edges is at most
> \[
> \boxed{
> C_\delta D^{2-\eta}+C_T\lambda D^2.
> }
> \tag{50.3}
> \]
> The number of retained components is at most \(C_T/\lambda+1\).

### Proof

The high-defect deletion removes fewer than
\[
\frac{C_\delta D}{D^{-1+\eta}}=C_\delta D^{2-\eta}
\]
edges.  During the subsequent vertex pruning, charge every removed current edge
to the first endpoint deleted.  Each deleted vertex has current degree less than
\(\lambda D\), so the total additional charge is less than
\(\lambda DT\le C_T\lambda D^2\).  This proves (50.3).

Every retained component has minimum degree at least \(\lambda D\).  If a shortest
path in such a component has length \(L\), the open neighborhoods of every third
vertex on the path are pairwise disjoint: a common neighbor would give a path of
length two between vertices whose path distance is at least three.  Hence
\[
\left(\left\lfloor\frac L3\right\rfloor+1\right)\lambda D\le T,
\]
so every component has graph diameter at most
\[
L_0:=\left\lceil\frac{3T}{\lambda D}\right\rceil.
\tag{50.4}
\]

Fix a root \(r\) in a retained component and an edge \(e=(u,v)\).  Join the
root to \(u\) and \(v\) by shortest paths and close the resulting walk with \(e\).
Its length is at most \(2L_0+1\), while every edge on it has defect at most
\(D^{-1+\eta}\).  If the gain sum of this closed walk were nonzero in
\(\mathbb Z/3\), the phase-cycle identity (49.6) would force
\[
\frac\pi3
\le (2L_0+1)D^{-1+\eta}.
\tag{50.5}
\]
But (50.1) and (50.4) make \(L_0\le 3C_T/\lambda+1\), so (50.5) is false for
all sufficiently large \(D\).  Thus every such root-to-root edge walk has zero
gain.  Defining \(\ell\) by the gain of a path from \(r\) to a vertex is therefore
path-independent, and gives (50.2).

Finally, every retained component has at least \(\lambda D+1\) vertices.  Since
there are at most \(T\le C_TD\) vertices total, their number is at most
\(C_T/\lambda+1\). \(\square\)

> **Corollary 50.2 (long directed cycles).** Orient every retained edge
> \(\tau\sigma\) from \(\tau\) to \(\sigma\) when
> \(\ell(\sigma)=\ell(\tau)+1\) in \(\mathbb Z/3\).  Every directed cycle in a
> retained component has length at least
> \[
> \boxed{\pi D^{\,1-\eta}.}
> \tag{50.6}
> \]

### Proof

On a directed cycle of length \(m\), every signed step in (49.2) is \(+1\), so
\(S=m\).  Since the cycle is closed and the potential telescopes,
\(m\equiv0\pmod3\).  Equation (49.6) then says
\[
\sum_{e\in C}\delta_e
=\pi\left(k-\frac m3\right).
\]
The left side is positive, so the integer in parentheses is at least one.  Hence
\(\sum_{e\in C}\delta_e\ge\pi\).  Every retained edge has
\(\delta_e\le D^{-1+\eta}\), which gives (50.6). \(\square\)

> **Lemma 50.3 (acyclic defect relaxation).** Suppose the canonical orientation
> of a retained component \(H\) is acyclic.  Then there is a train-angle velocity
> \(v\), supported on the trains of \(H\), for which
> \[
> \frac{d}{dt}\Big|_{t=0}\delta_e(\phi+tv)<0
> \qquad(e\in E(H)).
> \tag{50.7}
> \]
> Every rhombic contact remains exactly unit along this variation.  For a fixed
> finite disk, \(v\) can be scaled so that all crossings outside \(H\) remain
> strict as well.

### Proof

Choose a topological rank \(r:V(H)\to\mathbb Z\) with
\(r(\tau)<r(\sigma)\) on every canonically oriented edge
\(\tau\to\sigma\).  Set \(v_\tau=-r(\tau)\) on \(H\) and \(v_\tau=0\) outside
\(H\).  For an oriented edge of \(H\), the local signed lift in (49.2) is
\(\phi_\sigma-\phi_\tau=\pi/3+\delta_e\), so
\[
\dot\delta_e=v_\sigma-v_\tau=-(r(\sigma)-r(\tau))<0.
\]
Changing train angles preserves the length of every edge in the train-coordinate
realization.  Every crossing outside \(H\) has a positive angular defect at the
fixed configuration; because there are finitely many of them, a sufficiently small
multiple of \(v\) keeps all of them positive. \(\square\)

The lemma is only a defect-relaxation direction.  It is not claimed to be
diameter-nonincreasing.  Its exact first-order obstruction can nevertheless be
written down.  Let \(B_H\) be the oriented incidence matrix whose row for
\(\tau\to\sigma\) is \(e_\sigma-e_\tau\), and let \(G_D\) be the matrix of active
diameter gradients in train-angle coordinates.

> **Proposition 50.4 (diameter certificate for blocked relaxation).** If no
> train-angle velocity satisfies
> \[
> B_Hv<0,
> \qquad
> G_Dv\le0,
> \tag{50.8}
> \]
> then there are vectors
> \[
> \alpha\ge0,\quad \alpha\ne0,\qquad \beta\ge0
> \]
> such that
> \[
> \boxed{B_H^{\mathsf T}\alpha+G_D^{\mathsf T}\beta=0.}
> \tag{50.9}
> \]
> If \(H\)'s canonical orientation is acyclic, necessarily \(\beta\ne0\).

### Proof

The homogeneous system (50.8) is equivalent, after scaling, to
\(B_Hv\le-\mathbf1\) and \(G_Dv\le0\).  The alternative theorem of the
finite-dimensional Farkas lemma gives nonnegative multipliers
\((\alpha,\beta)\) annihilating the coefficient matrix and satisfying
\(\mathbf1^{\mathsf T}\alpha>0\), which is (50.9).  If \(\beta=0\), then
\(B_H^{\mathsf T}\alpha=0\) is a nonnegative circulation on the acyclic
orientation.  A finite DAG has no nonzero nonnegative circulation (take a source
of the support), contradicting \(\alpha\ne0\). \(\square\)

Thus an acyclic dense phase core can fail to relax its defects only through a
specific positive flow-to-diameter balance.  Establishing that such a balance is
incompatible with the diametral-hull shell, or charging its support to the
boundary-order budget, is a sharper remaining problem than the original
unstructured higher-order rank statement.

The geometric content is explicit.  On a path of length at most \(L_0\), equation
(50.2) and the signed lift formula (49.10) place every train direction within
\(L_0D^{-1+\eta}\) of one of three phase classes.  More importantly, the phase
classes are now globally consistent on the dense component, rather than chosen
independently on overlapping local patches.

For every fixed \(\varepsilon>0\), choosing \(\lambda\) small and then taking
\(D\) large leaves a core containing all but at most \(\varepsilon D^2+o(D^2)\)
crossing edges, split into only \(O_\varepsilon(1)\) three-phase-balanced
components.  This is a genuine reduction of the ordered shell problem.  It still
does not control the deleted defect/interface edges at the boundary-order rank
scale, so it does not by itself prove the missing higher-order shell-rank theorem.

# 51. Cyclic-order edge bound in a phase core

The dense-core potential gives an exact extremal bound without needing more than
the directed-triangle exclusion in Corollary 50.2. The promoted 2026-09-05
addendum now proves that these dense components are acyclic for sufficiently
large `D`; the former long-cycle alternative is absent. A directed
3-cycle is already impossible at the low-defect scale, and that is the only
cycle exclusion needed for the count below.

Let \(H\) be a retained component of Theorem 50.1, with phase classes
\[
V(H)=V_0\sqcup V_1\sqcup V_2,
\qquad
n_i=|V_i|,
\qquad
T_H=n_0+n_1+n_2.
\tag{51.1}
\]
Orient every crossing from \(V_i\) to \(V_{i+1}\) modulo \(3\).

> **Theorem 51.1 (cyclic-order edge bound).** For all sufficiently large \(D\),
> \[
> \boxed{
> |E(H)|\le\max_{i\in\{0,1,2\}} n_i(T_H-n_i).
> }
> \tag{51.2}
> \]
> In particular, if \(n_i=(1/3+o(1))T_H\) for all three classes, then
> \[
> \boxed{
> |E(H)|\le\left(\frac{2}{9}+o(1)\right)T_H^2.
> }
> \tag{51.3}
> \]

### Proof

Let \(e_{01},e_{12},e_{20}\) be the numbers of edges of the three types.  For
each triple \((a,b,c)\in V_0\times V_1\times V_2\), at most two of \(ab,bc,ca\)
can be edges.  If all three were present, their prescribed orientations would
form the directed cycle
\[
a\longrightarrow b\longrightarrow c\longrightarrow a.
\]
This is forbidden by Corollary 50.2 for large \(D\).  Counting triples by their
edges gives
\[
n_2e_{01}+n_0e_{12}+n_1e_{20}
\le2n_0n_1n_2.
\tag{51.4}
\]

Assume \(n_0=\max_i n_i\).  Rearranging (51.4) gives
\[
e_{12}\le
2n_1n_2-\frac{n_2}{n_0}e_{01}
-\frac{n_1}{n_0}e_{20}.
\]
Consequently,
\[
\begin{aligned}
|E(H)|
&\le
\left(1-\frac{n_2}{n_0}\right)e_{01}\;+\;
\left(1-\frac{n_1}{n_0}\right)e_{20}\;+\;2n_1n_2\\
&\le
(n_0-n_2)n_1+(n_0-n_1)n_2+\;2n_1n_2\\
&=n_0(n_1+n_2),
\end{aligned}
\]
using \(e_{01}\le n_0n_1\), \(e_{20}\le n_0n_2\), and the nonnegativity of the
two coefficients.  This proves (51.2), and (51.3) follows immediately. \(\square\)

The bound is an exact phase-sensitive refinement of the generic Mantel estimate
for balanced three-class cores.
It does not identify a complete bipartite block of the product size needed by the
Cartesian determinant inequality. By the promoted acyclicity consequence, Lemma 50.3 supplies a
strict first-order defect-relaxation direction; the remaining obstruction is then
the explicit flow-to-diameter certificate of Proposition 50.4, rather than an
undifferentiated crossing-rank problem.

# 52. Equality classification for a balanced phase core

The endpoint of Theorem 51.1 has a rigid finite equality case.  This does not yet
originally gave no additive train block, because a bipartite crossing graph
may split each phase class between the two sides.  It does, however, isolate the
only combinatorial shape compatible with exact maximal phase density.

> **Theorem 52.1 (balanced equality classification).** Let \(G\) be a tripartite
> graph with classes \(A,B,C\), each of size \(m\), and no triangle with one
> vertex in each class.  Then
> \[
> |E(G)|\le 2m^2.
> \]
> If equality holds, \(G\) is bipartite: there is a two-colouring
> of \(A\sqcup B\sqcup C\) such that two vertices in different colours are
> adjacent whenever they lie in different tripartite classes, and vertices of
> the same colour are nonadjacent. At most one original class splits between
> the colours; at least two original classes are monochromatic with opposite
> colours. In particular, a complete \(m\times m\) phase pair occurs. The
> graph need not be complete bipartite, since opposite-coloured vertices of
> the same original class remain nonadjacent.

### Proof

For \(a\in A,b\in B,c\in C\), let \(x_{ab},y_{bc},z_{ca}\) be the indicators of
the three possible edges.  Triangle-freeness gives

\[
x_{ab}+y_{bc}+z_{ca}\le2.
\tag{52.1}
\]

Summing over all \(m^3\) triples counts each edge exactly \(m\) times, so
\(m|E(G)|\le2m^3\).  This proves the bound.  If equality holds, every triple
has exactly two edges.

We now construct the two-colouring.  If some \(a_0b_0\) is a nonedge, then every
\(c\in C\) is adjacent to both \(a_0\) and \(b_0\), by the equality condition.
Give \(a_0,b_0\) colour \(0\) and all vertices of \(C\) colour \(1\).  For each
\(a\in A\), give \(a\) colour \(0\) when \(ab_0\) is a nonedge and colour \(1\)
when \(ab_0\) is an edge.  Equality in the triples \((a,b_0,c)\) then says that
\(a\) is adjacent to every \(c\in C\) exactly when its colour differs from that
of \(c\).  Define the colours of \(B\) analogously using \(a_0\).  Applying
(52.1) with an arbitrary triple \((a,b,c)\) now forces \(ab\) to be an edge
exactly when the colours of \(a,b\) differ.

If every \(A\)-\(B\) pair is an edge, give all of \(A\) colour \(0\) and all of
\(B\) colour \(1\).  Equality says \(y_{bc}+z_{ca}=1\) for every \((a,b,c)\),
so each \(c\in C\) receives the colour for which it is adjacent to exactly the
opposite-coloured vertices in \(A\) and \(B\).  The same relation gives the
claimed adjacency rule for the other two pairs. Thus \(G\) is bipartite with
the stated cross-class adjacency rule. If two original classes split, choosing
one vertex of each in the colour of a vertex of the third class would give a
triple with no edges. If precisely one class splits, the other two must have
opposite colours for the same reason. If no class splits, both colours must
occur. This proves the full-phase-pair conclusion. The six-vertex regression
EC in the promoted 2026-09-05 addendum rules out the stronger literal
complete-bipartite wording.
\(\square\)

For an exact balanced phase core with \(T_H=3m\), Theorem 52.1 therefore turns
the density endpoint

\[
|E(H)|=2m^2=\frac{2}{9}T_H^2
\]

into the stated bipartite crossing pattern with a complete phase pair. The
2026-09-05 addendum excludes the coherent core-sized exact endpoint using
that pair, without requiring an additive block. Its IS/TS stability and interval
extraction lemmas also handle `|E(H)|=(2/9-o(1)) T_H^2` when the three classes
are asymptotically balanced and account for the quadratic source core. More
generally NE excludes coherent core-sized near-extremal three-class graphs,
including unbalanced classes, with a uniform positive tolerance. What remains
is coverage: no theorem puts every survivor in this near-extremal one-core
regime. Multiple grains and a fixed quadratic density deficit are not excluded.

# 53. A sharp obstruction to any boundary-order density gap

It is tempting to seek a constant \(\kappa>0\) such that every triangle-free
unit-separated set of diameter at most \(D\) has at most

\[
\frac{\pi}{2\sqrt3}D^2-\kappa D+O(1)
\tag{53.1}
\]

points.  This is false, even if one requires the minimum distance to be exactly
one.  The failure is not numerical; it comes from an explicit oblique-lattice
family whose shear vanishes faster than the boundary scale.

> **Proposition 53.1 (sub-boundary oblique-lattice competitors).** Let \(D\to\infty\)
> and set
> \[
> \theta_D=\frac\pi3+D^{-3}.
> \tag{53.2}
> \]
> Let \(u_D,v_D\) be unit vectors with angle \(\theta_D\), and let
> \(\Lambda_D=\mathbb Zu_D+\mathbb Zv_D\).  There is a finite set
> \(A_D\subset\Lambda_D\) with
> \[
> \operatorname{diam}(A_D)<D,
> \qquad
> \min_{x\ne y\in A_D}|x-y|=1,
> \tag{53.3}
> \]
> no unit equilateral triangle, and
> \[
> \boxed{
> |A_D|\ge
> \frac{\pi}{2\sqrt3}D^2-o(D).
> }
> \tag{53.4}
> \]

### Proof

For \(\theta_D\in(\pi/3,\pi/2)\), the shortest nonzero vectors of
\(\Lambda_D\) are exactly \(\pm u_D,\pm v_D\).  Indeed, for integer
> coefficients \((a,b)\), vectors with \(ab\ge0\) have squared length at least
> one, with equality only for the four basis directions; for \(ab<0\), writing
> \(p=|a|,q=|b|\),
> \[
> |au_D+bv_D|^2=p^2+q^2-2pq\cos\theta_D
> \ge2-2\cos\theta_D>1.
> \tag{53.5}
> \]
> Thus three lattice points cannot form a unit equilateral triangle: the two unit
> vectors from one vertex would have to be two distinct members of
> \(\{\pm u_D,\pm v_D\}\), whose difference has length either
> \(|u_D-v_D|>1\) or \(|u_D+v_D|>1\).

> Translate the open disk \(B(0,D/2)\) through one fundamental cell of \(\Lambda_D\).
> The average number of lattice points in the translated disk is
> \[
> \frac{\pi D^2}{4\sin\theta_D}.
> \tag{53.6}
> \]
> Hence some translate contains at least this many lattice points.  Its finite
> lattice subset has diameter strictly less than \(D\), is unit-separated, and by
> the preceding paragraph is triangle-free.

> It remains only to ensure an exact unit pair.  The unit-neighbor graph of
> \(\Lambda_D\) is a square grid.  Any independent subset of the lattice points in
> a disk of radius \(D/2\) has at most half of those points plus \(O(D)\): pair points
> on each horizontal lattice line consecutively, leaving only one unpaired point
> per line.  The total number of lattice sites in the disk is itself
> \(\pi D^2/(4\sin\theta_D)+O(D)\), since only \(O(D)\) fundamental cells meet the
> circular boundary.  The translate in (52.6) contains the mean plus a nonnegative
> amount, whereas an independent subset contains at most half the mean plus
> \(O(D)\).  For large \(D\) it therefore contains a unit-neighbor pair.
> Consequently its minimum distance is exactly one.  Finally,
> \(\sin\theta_D=\sqrt3/2+O(D^{-3})\), so (52.6) gives
> \[
> \frac{\pi D^2}{4\sin\theta_D}
> =\frac{\pi}{2\sqrt3}D^2+O(D^{-1}),
> \]
> which implies (52.4).  \(\square\)

This proposition rules out a universal boundary-order density deficit for
triangle-free feasible sets.  It does not produce global minimizers: for the
cardinality \(|A_D|\), a different configuration may have smaller diameter.  The
global conjecture therefore needs a comparison that detects the sign of the
vanishing shear at the finite optimality scale, not merely a density estimate.

# 54. A two-wing determinant inequality

The exact equality pattern from Theorem 52.1 has a stronger geometric consequence
when its two complete-bipartite wings are actually aligned in the train coordinates.
The following elementary lemma is the relevant test.

> **Lemma 54.1 (aligned two-wing determinant bound).** Let a point set of diameter
> \(D\) contain the six points
> \[
> p,\quad p+U,\quad p+V,\quad p+U+V,\quad p+W,\quad p+U+W.
> \tag{54.1}
> \]
> If \(\det(U,V)\) and \(\det(U,W)\) have opposite signs, then
> \[
> \boxed{
> D^2\ge2\bigl(|\det(U,V)|+|\det(U,W)|\bigr).
> }
> \tag{54.2}
> \]
> The same conclusion holds if the second four-point block is based at \(q\)
> instead of \(p\), provided \(q-p\) is parallel to \(U\).

### Proof

For the common-base case, set \(X=V-W\) and \(Y=U\).  The two vectors

\[
X+Y=(p+U+V)-(p+W),
\qquad
X-Y=(p+V)-(p+U+W)
\]

are differences of points in the set, and hence each has norm at most \(D\).  The
parallelogram determinant identity gives

\[
D^2\ge|\det(X+Y,X-Y)|=2|\det(V-W,U)|.
\]

Opposite signs of the two determinants make

\[
|\det(V-W,U)|=|\det(U,V)|+|\det(U,W)|,
\]

which proves (54.2).  If the second block is based at \(q\), replace \(X\) by
\(V-W-(q-p)\).  The added term is parallel to \(U\), so its determinant with
\(U\) vanishes.  The same calculation applies.  \(\square\)

The exact loss when the two bases are not aligned is also elementary.

> **Lemma 54.2 (unresolved-base displacement penalty).** Suppose the first
> four-point block in (54.1) is based at \(p\), while the second is based at
> \(q\), with no assumption on \(Z=q-p\).  Then
> \[
> D^2\ge2\left|\det\bigl(U,V-W-Z\bigr)\right|.
> \tag{54.5}
> \]
> If \(\det(U,V)\) and \(\det(U,W)\) have opposite signs, then, with
> \(S=|\det(U,V)|+|\det(U,W)|\),
> \[
> D^2\ge2\bigl(S-|\det(U,Z)|\bigr).
> \tag{54.6}
> \]
> The same four blocks also give \(D^2\ge2|\det(U,Z)|\), and consequently
> \[
> D^2\ge S.
> \tag{54.7}
> \]

### Proof

Put \(X=V-W-Z\).  The differences
\[
(p+U+V)-(q+W)=X+U,\qquad
(p+V)-(q+U+W)=X-U
\]
have norm at most \(D\).  The parallelogram determinant identity gives
\[
D^2\ge|\det(X+U,X-U)|
=2|\det(U,X)|.
\]

which proves (54.5).  Since

\[
\det(U,X)=\det(U,V)-\det(U,W)-\det(U,Z),
\]

the opposite-sign assumption and the triangle inequality give (54.6).  The
points \(p,p+U,q,q+U\) are all present, so the same parallelogram identity gives

\[
D^2\ge2|\det(U,Z)|.
\]

Taking the larger of this bound and (54.6) yields

\[
D^2\ge
\max\{2|\det(U,Z)|,\,2S-2|\det(U,Z)|\}
\ge S,
\]

which proves (54.7).  \(\square\)

Thus a transverse base displacement can erase the factor of two in the aligned
estimate: the determinant argument alone retains only the one-wing-scale bound
(54.7).  Any endpoint contradiction must either control
\(|\det(U,q-p)|\) for many wing pairs, or use a second independent common
direction.  This is the precise geometric content of the alignment gap.

# 55. Near-triangular additive blocks are even more expensive

The determinant estimate in Theorem 10.9 uses only the area of an additive block.
Near-triangular phase coherence also controls its diagonal lengths.

> **Lemma 55.1 (coherent-block norm bound).** Consider an additive
> \(a\times b\) block
> \[
> p_{ij}=p+x_i+y_j,\qquad
> 0\le i\le a,\qquad 0\le j\le b,
> \]
> with unit increments \(u_i=x_i-x_{i-1}\) and \(v_j=y_j-y_{j-1}\).  Suppose
> all \(u_i\) lie within angle \(\alpha\) of one direction \(u_*\), all \(v_j\)
> lie within angle \(\alpha\) of one direction \(v_*\), and the angle between
> \(u_*,v_*\) is within \(\beta\) of either \(\pi/3\) or \(2\pi/3\).  Put
> \(\varepsilon=\beta+2\alpha<\pi/6\).  Then the block diameter satisfies
> \[
> \boxed{
> D^2\ge \cos^2\!\alpha\,
> \left(a^2+b^2+2\cos\left(\frac{\pi}{3}+\varepsilon\right)ab\right).
> \}
> \tag{55.1}
> \]

### Proof

Set \(U=\sum_i u_i\) and \(V=\sum_jv_j\).  Projection onto \(u_*\) and
\(v_*\) gives

\[
|U|\ge a\cos\alpha, \qquad |V|\ge b\cos\alpha.
\]

The angle between \(U,V\) is within \(\varepsilon\) of either \(\pi/3\) or
\(2\pi/3\), so

\[
|U\cdot V|\ge |U|\,|V|\cos\left(\frac{\pi}{3}+\varepsilon\right).
\]

The four block corners contain both differences \(U+V\) and \(U-V\).  Therefore

\[
D^2\ge\max{|U+V|^2,|U-V|^2}
=|U|^2+|V|^2+2|U\cdot V|,
\]

which yields (55.1).  \(\square\)

In particular, for a balanced coherent \(m\times m\) block with
\(\alpha,\beta=o(1)\),

\[
D^2\ge(3-o(1))m^2.
\tag{55.2}
\]

This gives a stronger conditional exclusion at the exact phase endpoint than
Lemma 54.1.  If the equality-classification block \(A_0\times A_1\) is an
additive block and its train directions are supplied by a low-defect phase core,
then \(R=2m^2+o(m^2)\) implies \(n=2m^2+o(m^2)\), while the global comparison
gives

\[
D(n)^2<\left(\frac{4\sqrt3}{\pi}+o(1)\right)m^2.
\tag{55.3}
\]

Since \(3>4\sqrt3/\pi\), such a block cannot occur in a global minimizer.  The
former geometric task was to promote a complete crossing family to an
additive block or control intervening trains. **Superseded:** CR in the promoted
2026-09-05 addendum proves a sufficient diameter lower bound directly from
the complete coherent crossing family in a pure disk. Its two-train path proof
allows different bases and arbitrarily many intervening trains. General phase
core coverage and topology remain open.

# 56. Weighted coherent-star endpoint exclusion

The previous block estimate gives a uniform contradiction for a full phase-star,
provided the two non-maximal phase classes remain on the quadratic scale.

> **Proposition 56.1 (coherent-star exclusion).** Let \(0\le a\le b\le M\) be
> the sizes of three phase classes, with \(M\) the largest.  Suppose a coherent
> additive \(M\times b\) block occurs between the largest class and the larger
> of the other two classes.  Fix \(\tau>0\), assume \(b/M\ge\tau\), and assume
> the phase-star accounts for the quadratic core:
> \[
> R=M(a+b)+o(M^2),
> \tag{56.1}
> \]
> and the two block directions have angular error \(o(1)\) from the triangular
> phase angles.  Then this core cannot occur in a global minimizer.

### Proof

Apply Lemma 55.1 with block dimensions \(M\) and \(b\).  Writing
\(t=b/M\in(0,1]\), the block contributes
\[
D^2\ge(1-o(1))M^2(1+t+t^2).
\tag{56.2}
\]
Because \(a\le b\), the core count satisfies
\[
R\le2Mb+o(M^2).
\]
The three phase classes exhaust \(T\), so \(T=M+a+b=O(M)\), and for a pure
rhombic disk \(n=R+T+1=R+o(M^2)\).  The strict translated-lattice comparison
therefore gives, with \(c=2\sqrt3/\pi\),
\[
D(n)^2<c\,n
<\bigl(2ct+o(1)\bigr)M^2.
\tag{56.3}
\]
The difference between the leading coefficients in (56.2) and (56.3) is
\[
1+t+t^2-2ct.
\]
Its discriminant is \((2c-1)^2-4<0\), because \(1/2<c<3/2\).  Hence this
quadratic is uniformly positive for \(0<t\le1\), and the \(o(1)\) terms cannot
close the gap.  This contradicts (56.2)--(56.3).  \(\square\)

At the exact equality endpoint of Theorem 52.1, the equality colouring supplies
a full \(M\times M\) phase pair, so \(\tau=1\).  If \(b/M\to0\), the same
argument remains valid under the stronger remainder hypothesis
\(R=M(a+b)+o(Mb)\) (and with the harmless \(O(M)\) train term absorbed when
\(b\to\infty\)).  Thus the remaining promotion is geometric:
one formerly needed to prove additivity or an equivalent diagonal-length cost.
**Superseded:** PS in the promoted 2026-09-05 addendum removes the additive-block
hypothesis entirely in a pure disk and also removes the lower bound on `b/M`.
It retains the core-sized phase-star count and a complete coherent crossing
pair. No theorem establishes those hypotheses for every survivor.
