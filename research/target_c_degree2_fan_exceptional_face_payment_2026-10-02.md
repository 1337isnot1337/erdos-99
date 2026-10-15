# Target C: degree-two diameter-leaf fans pay exceptional-face currency

**Date:** 2026-10-02  
**Base main:** \`71ae9deca2f8927a202dc74d999aca14d56f53a5\`  
**Status:** proof-only source/contact-topology reduction. Level I and C-II remain open.

## 1. Statement

Work in the canonical post-ZF source. Let

- \(B\) be the loaded actual-diameter endpoint set, cyclically ordered on
  \(F=\operatorname{conv}(B)\);
- \(q=|B|\);
- \(b\) be the occurrence-counted outer positive-contact-face boundary walk;
- \(x_B=b-q\);
- \(Q\) be the bounded nonquadrilateral face excess
  \[
  Q=\sum_{G\ {\rm exceptional}}(\deg G-4).
  \]

Consider the exact same-carrier good diameter-leaf fans from the current
low-\(x_B\), square-root-matching branch. Let \(U\) be the number of internal
good-fan vertices whose positive contact degree is exactly two.

Then
\[
\boxed{
U\le 2x_B+3Q+4.
}
\tag{1}
\]

Consequently, in the branch
\[
\nu(H)\le K_\nu\sqrt D,
\qquad
x_B\le K_x\sqrt D,
\tag{2}
\]
the current fan theorem gives
\[
I\ge
\lceil D\rceil-(4K_\nu+2K_x)\sqrt D
\tag{3}
\]
internal good-fan vertices. If the degree-two population is the larger half,
\[
U\ge I/2,
\]
then
\[
\boxed{
Q
\ge
{I\over6}-{2\over3}x_B-{4\over3}
}
\tag{4}
\]
and hence
\[
\boxed{
Q
\ge
{D\over6}
-
\left(
{2K_\nu\over3}
+
K_x
\right)\sqrt D
-O(1).
}
\tag{5}
\]

In particular,
\[
\boxed{
U\ge I/2
\quad\Longrightarrow\quad
Q\ge(1/6-o(1))D.
}
\tag{6}
\]

Thus the degree-two fan-flip / almost-unit branch cannot remain a low-face-defect
regression: a linear population of degree-two diameter leaves is already paid by
canonical exceptional-face currency, up to the \(O(x_B)\) bridge budget.

No computation is used.

## 2. Exact fan geometry

Fix one internal degree-two good-fan vertex \(p\), its two adjacent fan vertices
\(p_-,p_+\), and its common diameter carrier \(a\).

Put
\[
u={p-a\over D},
\qquad
\varepsilon={1\over2D},
\qquad
\tau=\sqrt{1-\varepsilon^2}.
\tag{7}
\]

The exact fan coordinates are
\[
p=a+Du,
\]
and
\[
p_\pm
=
a+(D-\varepsilon)u\pm\tau t
\tag{8}
\]
for a unit tangent \(t\).

Hence
\[
|p-p_-|=|p-p_+|=1
\tag{9}
\]
and
\[
|p_--p_+|=2\tau>1
\tag{10}
\]
for the large-\(D\) regime.

Since \(p\) has positive contact degree exactly two, its only positive-contact
edges are
\[
p_-p,\qquad pp_+.
\tag{11}
\]

Both are sides of the loaded convex hull \(F\).

## 3. Loaded-hull bridge contacts are paid by \(x_B\)

Let \(J\) be the number of unit loaded-hull sides that are bridges of the positive
contact graph.

### Lemma 3.1
\[
\boxed{J\le x_B.}
\tag{12}
\]

### Proof

Use the Section-63 decomposition of the outer boundary walk into the \(q\) subwalks
\[
W_i:b_i\leadsto b_{i+1},
\qquad
|W_i|=\ell_i\ge1,
\]
with
\[
b=\sum_i\ell_i,
\qquad
x_B=\sum_i(\ell_i-1).
\tag{13}
\]

If the loaded hull side \(b_ib_{i+1}\) is a unit contact and is a bridge, that edge
occurs twice on the outer-face boundary walk.

One of its two occurrences may supply the direct one-edge passage in \(W_i\).
The other occurrence is a distinct additional outer-walk occurrence. It cannot be
the sole occurrence of another length-one subwalk \(W_j\), because a length-one
\(W_j\) joins exactly \(b_j\) to \(b_{j+1}\), and the cyclic loaded hull side
\(b_ib_{i+1}\) has those endpoints only for \(j=i\).

Thus every bridge loaded-hull side injects one distinct occurrence into the
\[
\sum_i(\ell_i-1)=x_B
\]
outer-walk excess positions. This proves (12). QED.

A bridge loaded-hull edge is incident with at most two internal fan vertices.
Therefore the number \(U_{\rm br}\) of degree-two internal fan vertices for which
at least one of the two edges in (11) is a bridge obeys
\[
\boxed{
U_{\rm br}\le2J\le2x_B.
}
\tag{14}
\]

## 4. Every remaining degree-two fan leaf lies on an exceptional bounded face

Now suppose neither \(p_-p\) nor \(pp_+\) is a bridge.

Each is a convex-hull edge, so one side of each edge is the outer face. A nonbridge
plane edge has two distinct incident faces. Since \(p\) has contact degree two, the
interior sectors of \(p_-p\) and \(pp_+\) belong to the same bounded face; call it
\(G(p)\).

Thus the boundary walk of \(G(p)\) contains the consecutive two-edge path
\[
p_-\;-\;p\;-\;p_+.
\tag{15}
\]

### Lemma 4.1 — \(G(p)\) is not a quadrilateral

Suppose \(G(p)\) had degree four. Its complementary boundary path from \(p_+\) back
to \(p_-\) would have two unit contact edges through one source vertex \(z\):
\[
p_+\;-\;z\;-\;p_-.
\tag{16}
\]

Therefore \(z\) is a common unit-distance point of \(p_-\) and \(p_+\).

The two unit circles centered at \(p_-\) and \(p_+\) have exactly two intersection
points. One is \(p\). The other is the reflection of \(p\) across the chord line
\(p_-p_+\), namely the exact fan-flip point
\[
p'
=
a+(D-2\varepsilon)u
=
a+\left(D-{1\over D}\right)u.
\tag{17}
\]

Hence
\[
z=p'.
\]
But
\[
|p-z|=|p-p'|={1\over D}<1,
\tag{18}
\]
contradicting source unit separation.

Thus \(G(p)\) cannot be a quadrilateral.

A triangular bounded face is already forbidden by the triangle-free contact graph
(and in the present geometry \(p_-p_+\) is not a unit edge by (10)).
Therefore
\[
\boxed{
\deg G(p)\ge5.
}
\tag{19}
\]

So \(G(p)\) is one of the bounded exceptional faces counted by \(Q\).

No blocker point from the fan-flip theorem is needed for this conclusion. It follows
directly from the exact \((D,D,1)\) fan geometry and contact degree two.

## 5. Run counting sharpens the exceptional-face payment

Let
\[
U_{\rm exc}:=U-U_{\rm br}.
\]

Color every nonbridge loaded-hull contact edge by its unique bounded interior face.
For an exceptional face \(G\), let

- \(e_G\) be the number of loaded-hull edges colored by \(G\); and
- \(c_G\) be the number of nonempty cyclic runs formed by those edges on the loaded
  hull cycle.

Assume first that \(G\) does not contain the entire loaded hull cycle.

A degree-two fan vertex assigned to \(G\) occurs only where its two consecutive hull
edges have the same color \(G\). A run of \(\ell\) consecutive \(G\)-colored hull
edges contains at most \(\ell-1\) such internal vertices. Therefore, if \(r_G\) is
the number of degree-two fan vertices assigned to \(G\),
\[
\boxed{
r_G\le e_G-c_G.
}
\tag{20}
\]

The boundary walk of \(G\) contains all \(e_G\) colored hull-edge occurrences.
Between two successive hull runs, the face boundary must traverse at least one
non-hull edge occurrence; the same is true for the return from the last run to the
first. Hence it contains at least \(c_G\) non-hull edge occurrences. Therefore
\[
\boxed{
\deg G\ge e_G+c_G.
}
\tag{21}
\]

Combining (20)--(21),
\[
r_G
\le
\deg G-2c_G
\le
\deg G-2.
\tag{22}
\]

Let \(\mathcal F_*\) be the used exceptional faces and \(f_*=|\mathcal F_*|\).
Put
\[
Q_*:=\sum_{G\in\mathcal F_*}(\deg G-4)\le Q.
\]
Every used exceptional face has degree at least five, so
\[
f_*\le Q_*.
\tag{23}
\]

Summing (22),
\[
\begin{aligned}
U_{\rm exc}
&\le
\sum_{G\in\mathcal F_*}(\deg G-2)\\
&=
Q_*+2f_*\\
&\le
3Q_*\\
&\le
3Q.
\end{aligned}
\tag{24}
\]

### Whole-hull exceptional face

There is one exceptional case in the cyclic run count: one bounded face \(G_0\)
may be incident with every loaded-hull contact edge. Then all degree-two leaves
charged through hull edges can be assigned to \(G_0\), and
\[
U_{\rm exc}\le q.
\]
But
\[
\deg G_0\ge q,
\qquad
Q\ge \deg G_0-4,
\]
so
\[
U_{\rm exc}\le Q+4.
\tag{25}
\]

Combining the proper-run case and the whole-hull case gives the uniform bound
\[
\boxed{
U_{\rm exc}\le3Q+4.
}
\tag{26}
\]

With the bridge contribution (14),
\[
\boxed{
U
=
U_{\rm br}+U_{\rm exc}
\le
2x_B+3Q+4.
}
\tag{27}
\]

This proves the sharpened form of (1).

## 5.1 The flip blocker is trapped in the same exceptional face

The current exact fan-flip theorem gives, for every degree-two internal fan vertex
\(p\), a previously strict source pair
\[
py,
\qquad
1<|p-y|\le1+{1\over D},
\tag{24}
\]
where the blocker \(y\) is diameter-inactive and lies strictly inside
\[
\operatorname{conv}\{a,p_-,p_+\}\subseteq F.
\]

For \(D\ge3\),
\[
|p-y|<\sqrt2.
\tag{25}
\]

### Lemma 5.1 — short blocker segments do not cross contact edges

The open segment \(py\) crosses no positive unit-contact edge and contains no third
source point.

**Proof.**
If \(py\) properly crossed a unit contact edge \(rs\), the four distinct source
points would form a convex quadrilateral whose diagonals are \(py\) and \(rs\).
Some interior angle of a convex quadrilateral is at least \(\pi/2\). The two source
sides incident with that angle both have length at least one, so the opposite
diagonal has length at least \(\sqrt2\) by the cosine law. But
\[
|rs|=1,
\qquad
|py|<\sqrt2,
\]
a contradiction.

If a third source point \(z\) lay in the open segment \(py\), then unit separation
would give
\[
|p-y|
=
|p-z|+|z-y|
\ge2,
\]
again contradicting (25). QED.

Because \(y\) lies inside \(F\), the segment \(py\) leaves \(p\) through the interior
sector between the only two contact edges \(p_-p\) and \(pp_+\). By Lemma 5.1 it
cannot leave that contact face. Hence, whenever neither adjacent fan contact is a
bridge,
\[
\boxed{
py\subseteq\overline{G(p)}.
}
\tag{26}
\]

This gives an exact localization of the flip obstruction.

- If \(y\) is contact-isolated in the positive-contact graph, then \(y\) is strictly
  inside the bounded exceptional face \(G(p)\). It cannot lie on a boundary contact
  edge by unit separation.
- If \(y\) is nonisolated in the positive-contact graph, then \(y\) is a boundary
  vertex of \(G(p)\).

Therefore all but at most \(2x_B\) degree-two fan leaves have their canonical
inverse-\(D\) flip obstruction localized to a bounded exceptional face that already
pays the occurrence in (1).

This is stronger than the scalar \(Q\)-payment alone: the almost-unit obstruction is
not allowed to escape to an unrelated part of the source.

## 6. Square-root matching consequence

The current global fan theorem gives (3). If
\[
U\ge I/2,
\]
then (27) gives
\[
3Q
\ge
U-2x_B-4
\ge
{I\over2}-2x_B-4.
\]
Therefore
\[
\boxed{
Q
\ge
{I\over6}-{2\over3}x_B-{4\over3}.
}
\tag{28}
\]

Substitute
\[
I\ge
\lceil D\rceil-(4K_\nu+2K_x)\sqrt D
\]
and
\[
x_B\le K_x\sqrt D
\]
to obtain
\[
\boxed{
Q
\ge
{\lceil D\rceil\over6}
-
\left(
{2K_\nu\over3}
+
K_x
\right)\sqrt D
-{4\over3}.
}
\tag{29}
\]

Hence
\[
\boxed{
Q\ge(1/6-o(1))D.
}
\tag{30}
\]

This proves the sharpened forms of (4)--(6).

## 7. Combined fan frontier

The degree-two-heavy side is no longer best viewed as merely a family of
inverse-\(D\) flip blockers.

The exact contact topology gives the stronger canonical payment
\[
\boxed{
U\ {\rm linear}
\quad\Longrightarrow\quad
Q\ {\rm linear}
}
\]
when \(x_B=O(\sqrt D)\).

Combine this with the current degree-three harmonic-return theorem
\[
\texttt{research/target_c_leaf_fan_port_harmonic_return_2026-10-02.md}.
\]

In the low-\(x_B\), square-root-matching branch, the fan population therefore has the
following reduced alternatives:

1. **exceptional-face branch**
   \[
   Q\ge(1/10-o(1))D;
   \]
2. **off-carrier harmonic-return branch:** a linear family of canonical fan
   attachment incidences has nonlocal loaded returns with fixed radial support depth;
3. **large harmonic-cell branch:** one \(\Omega(\sqrt D)\)-diameter attachment cell
   carries \(\Omega(\sqrt D)\) exact fan attachment vertices.

This removes the degree-two fan-flip branch as a low-\(Q\) escape.

## 8. Remaining bottleneck

This still does not close C-II.

The sharpened exceptional-face floor must be coupled to one of the existing canonical
face currencies. Section 63 gives
\[
q-x_B=Q+2(d_H+s_Z),
\]
so a \(D/10\) exceptional-face payment is feasible at the scalar level. A closing
argument must use where these exceptional faces occur: each one counted here touches
an exact same-carrier loaded fan arc, not an arbitrary internal defect location.

The next exact target is therefore one of:

- convert a linear family of fan-adjacent exceptional-face boundary occurrences into
  stopped-train terminal currency and compare with the current O--O/train endpoint
  budget; or
- exploit the harmonic-return alternatives from the degree-three branch to force the
  same exceptional/interface currency.

No C-II closure or Level I closure is claimed.

**Disposition:** exact proof-only contact-topology strengthening. No numerical
experiment, verifier execution, CI output, or unexecuted certificate code is used.
