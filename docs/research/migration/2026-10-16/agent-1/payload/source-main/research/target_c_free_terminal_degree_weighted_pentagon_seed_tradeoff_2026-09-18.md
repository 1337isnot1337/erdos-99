# Target C-II — degree-weighted pentagon seeds sharpen the live corank/flex tradeoff

**Date:** 2026-09-18  
**Status:** proof-only structural strengthening; theorem-state authority unchanged  
**Scope:** canonical full-core stopped-train system after maximal two-anchor activation; live terminal consequence in the current `t_D <= mu_*+0.00710+o(1)` window  
**Depends on:** maximal two-anchor activation; bounded-face endpoint-pair simplicity; bounded-pentagon no-parallel-side theorem; pentagon bootstrap row-minor construction; activated-endpoint pair-shield exact flex; live detour pinching; sealed dual-component corank-to-flex law; exact defect partition `k=d_H+p_D+sigma_C`  
**Certificate:** `research/verify_target_c_free_terminal_degree_weighted_pentagon_seed_tradeoff_2026_09_18.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The previous pentagon-bootstrap theorem treated every residual pentagon as if its
pentagon--pentagon transport degree were five.  The random-order proof actually has a
strictly better degree-dependent loss: degree at most three costs no seed, degree four
costs `1/5` in expectation, and degree five costs `1/3`.

In the residual transport geometry, a degree-five vertex of the residual pentagon graph
is necessarily a zero-anchor face: all five terminal trains of that pentagon already go
to five residual pentagons.  Keeping this information gives the finite corank bound

\[
\boxed{
\sigma_C
\le {2\over5}(f-a_F)
   +{8\over5}(Q-f)
   +{4\over15}n_0.
}
\tag{WS.1}
\]

Here `a_F` is the number of faces activated by the maximal two-anchor process and `n_0`
is the number of final residual zero-anchor faces.  If

\[
E_U:=a_F+{x_A\over2}+{n_0+n_2\over2},
\]

is the exact structural correction already present in the pair-shield manifold, then
(WS.1) implies

\[
\boxed{
\sigma_C
\le {2\over5}f+{8\over5}(Q-f)+{8\over15}E_U.
}
\tag{WS.2}
\]

Thus a large pure-contact closure corank cannot be hidden in degree-five residual
pentagon blocks without paying directly into exact finite contact flex.

In the current live terminal window the certified bounds

\[
{f\over D}<0.76152405+o(1),
\qquad
{Q-f\over D}<0.000141+o(1)
\]

give the safe threshold

\[
B_0:={2\over5}(0.76152405)+{8\over5}(0.000141)
=0.30483522.
\tag{WS.3}
\]

Consequently

\[
\boxed{
{E_U\over D}
\ge {15\over8}
\left({\sigma_C\over D}-0.30483522\right)_+-o(1).
}
\tag{WS.4}
\]

Combining this with the pair-shield exact manifold and the previously audited sealed
component law gives the two-slope flex envelope

\[
\boxed{
{m_D\over D}
>
1.1988388040
+
\max\left\{
 {1\over4}{\sigma_C\over D},
 {15\over8}
 \left({\sigma_C\over D}-0.30483522\right)_+
\right\}
-o(1).
}
\tag{WS.5}
\]

The second term overtakes the old quarter-slope at

\[
{\sigma_C\over D}
={15\over13}B_0
=0.351732946153846\ldots .
\tag{WS.6}
\]

Using the exact defect partition

\[
k=d_H+p_D+\sigma_C
\]

and the live lower bound

\[
{k\over D}>1.1812298040-o(1),
\]

the weighted branch of (WS.5) is equivalent to the new global tradeoff

\[
\boxed{
{m_D\over D}
+{15\over8}{d_H+p_D\over D}
>2.8420786490-o(1).
}
\tag{WS.7}
\]

Together with the existing quarter-weight relation

\[
{m_D\over D}+{1\over4}{d_H+p_D\over D}>1.4941462550-o(1),
\tag{WS.8}
\]

the two lower half-planes intersect at

\[
{d_H+p_D\over D}
=0.829496857846153\ldots,
\qquad
{m_D\over D}
=1.286772040538461\ldots .
\tag{WS.9}
\]

So every convergent live subsequence has at least one of

\[
\boxed{
\lim {m_D\over D}>1.2867720405
\quad\text{or}\quad
\lim {d_H+p_D\over D}>0.8294968578.
}
\tag{WS.10}
\]

The old quarter-weight line remains stronger close to the minimum flex floor; the new
line is stronger once appreciable pure-contact corank is present.  The point is not a
new universal flex floor.  It removes the high-corank/moderate-flex part of the live
feasible region.

---

## 1. Weighted random-order seed lemma

Let `G` be any finite graph with maximum degree at most five.  Choose a uniformly random
ordering of `V(G)` and put a vertex `v` into `W` when at most three neighbors of `v`
occur before it.  Reverse the induced ordering on `W`.  Every vertex of `G[W]` then has
at most three later neighbors, so `G[W]` is 3-degenerate in the exact ordering needed by
the pentagon pivot construction.

For `d=deg_G(v)`, the rank of `v` among `v` and its `d` neighbors is uniform, hence

\[
\Pr(v\in W)=\min\left\{1,{4\over d+1}\right\}.
\]

Therefore the probability that `v` is excluded from `W` is

\[
0,0,0,0,{1\over5},{1\over3}
\]

for degrees `0,1,2,3,4,5`, respectively.  If `z_4,z_5` are the numbers of degree-four
and degree-five vertices, then

\[
\mathbb E|V(G)\setminus W|
={z_4\over5}+{z_5\over3}
\le {|V(G)|\over5}+{2z_5\over15}.
\tag{1.1}
\]

Thus some ordering has a 3-degenerate induced subset `W` whose complement satisfies
(1.1).  This refines, rather than replaces, the previous coarse `|W|>=2|V|/3` lemma.
No forbidden-subgraph hypothesis is used.

---

## 2. Degree five means zero outside anchors

Run maximal two-anchor activation.  Let

\[
U=U_5\sqcup U_{\ge6}
\]

be the residual exceptional faces, let `u_5=|U_5|`, `u_6=|U_{>=6}|`, and let `G_5` be
the simple graph on residual pentagons whose edges are complete stopped trains joining
two residual pentagons.

A pentagon has exactly five terminal train occurrences.  Bounded endpoint-pair
simplicity makes `G_5` simple.  Hence if a residual pentagon has degree five in `G_5`,
its five distinct pentagon neighbors already consume all five terminal train
occurrences.  It has no train to the outer/activated side and no residual train to a
nonpentagonal face.  In the maximal-activation notation it is therefore an `n_0` face.

If `z_5` denotes the number of degree-five vertices of `G_5`, then exactly

\[
\boxed{z_5\le n_0.}
\tag{2.1}
\]

Also every residual face of degree at least six contributes at least one unit to

\[
Q-f=\sum_F(\deg F-5),
\]

so

\[
\boxed{u_6\le Q-f.}
\tag{2.2}
\]

---

## 3. Weighted seeds give a larger closure-row minor

Apply Section 1 to `G_5`.  Put every residual nonpentagonal face into the seed set and
also put the excluded pentagons `U_5\setminus W` into the seed set:

\[
S:=U_{\ge6}\cup(U_5\setminus W).
\]

By (1.1),

\[
|S|
\le u_6+{u_5\over5}+{2z_5\over15}.
\tag{3.1}
\]

Process the pentagons of `W` in the 3-degeneracy order.  Each pentagon has five terminal
trains and at most three trains to still-unprocessed vertices of `W`; hence it has at
least two trains going to the outer face, an activated face, a seed face, or a previously
processed `W` face.  The bounded-pentagon no-parallel-side theorem makes the two chosen
projective directions nonparallel.

Use those two trains as pivot columns for that pentagon's two closure rows.  Together
with the original pivots on the activated faces, the same ordering argument as in the
pentagon-bootstrap theorem gives a block-upper-triangular selected square minor with
invertible `2x2` diagonal blocks.  Seed rows are omitted; a train ending at a seed face
is a legitimate pivot because the seed endpoint is absent from the selected row set.

Thus

\[
\operatorname{rank}C_{face}\ge2(f-|S|),
\]

and the exact closure-corank identity gives

\[
\sigma_C=2f-\operatorname{rank}C_{face}
\le2|S|.
\tag{3.2}
\]

Insert (3.1):

\[
\sigma_C
\le2u_6+{2\over5}u_5+{4\over15}z_5.
\tag{3.3}
\]

Since `u_5+u_6=f-a_F`, equations (2.1)--(2.2) yield

\[
\begin{aligned}
\sigma_C
&\le {2\over5}(f-a_F)
 +{8\over5}u_6
 +{4\over15}z_5\\
&\le {2\over5}(f-a_F)
 +{8\over5}(Q-f)
 +{4\over15}n_0,
\end{aligned}
\]

which is (WS.1).

This is a finite row-rank statement.  It does not claim that the omitted seed closure
equations integrate nonlinearly, and it does not infer a full train-angle manifold from
the selected minor alone.

---

## 4. Transfer from zero-anchor seeds to exact finite flex

The activated-endpoint pair-shield theorem supplies an exact finite contact-preserving
manifold satisfying

\[
m_D\ge {b-f\over2}+E_U+p_U,
\qquad
E_U=a_F+{x_A\over2}+{n_0+n_2\over2},
\tag{4.1}
\]

with `p_U>=0`.  In particular

\[
E_U\ge {n_0\over2}.
\tag{4.2}
\]

Drop the favorable `-(2/5)a_F` term in (WS.1), use (4.2), and obtain

\[
\sigma_C
\le {2\over5}f+{8\over5}(Q-f)+{8\over15}E_U,
\]

which is (WS.2).  Rearranging gives the finite positive-part form

\[
\boxed{
E_U
\ge {15\over8}
\left(
\sigma_C-{2\over5}f-{8\over5}(Q-f)
\right)_+.
}
\tag{4.3}
\]

The coefficient `15/8` is not an optimization over floating-point data.  It is the
exact reciprocal of the random-order degree-five surcharge `8/15` after transferring
`n_0/2` into the pair-shield manifold.

---

## 5. Live numerical envelope

Write

\[
r={Q-f\over D}.
\]

The live detour-pinching theorem gives the safe asymptotic upper bounds

\[
{f\over D}<0.76152405+o(1),
\qquad
r<0.000141+o(1).
\tag{5.1}
\]

Hence

\[
{2f\over5D}+{8r\over5}
<0.30483522+o(1).
\tag{5.2}
\]

Equation (4.3) gives (WS.4).  The live pair-shield baseline satisfies

\[
{b-f\over2D}>1.1988388040-o(1),
\tag{5.3}
\]

so (4.1) and (WS.4) give

\[
{m_D\over D}
>
1.1988388040
+{15\over8}
\left({\sigma_C\over D}-0.30483522\right)_+
-o(1).
\tag{5.4}
\]

Independently, the hostile-audited sealed dual-component theorem gives

\[
{m_D\over D}
>
1.1988388040+{1\over4}{\sigma_C\over D}-o(1).
\tag{5.5}
\]

Taking the stronger of (5.4) and (5.5) proves (WS.5).  Solving equality of their two
corank payments gives (WS.6).

---

## 6. New weighted flex/topology-stress conservation law

Put

\[
x_D={d_H+p_D\over D},
\qquad
s_D={\sigma_C\over D}.
\]

The exact defect partition is

\[
{k\over D}=x_D+s_D.
\tag{6.1}
\]

The live endpoint gives

\[
\liminf{k\over D}>1.1812298040.
\tag{6.2}
\]

Let `lambda=15/8` and `B_0=0.30483522`.  Equation (5.4) is

\[
{m_D\over D}
>C_0+\lambda(s_D-B_0)_+-o(1),
\qquad C_0=1.1988388040.
\tag{6.3}
\]

If `s_D<=B_0`, then (6.1)--(6.2) give

\[
x_D\ge1.1812298040-B_0-o(1).
\]

If `s_D>B_0`, add `lambda x_D` to (6.3) and use `x_D+s_D>=1.1812298040-o(1)`.  Both cases
give the same inequality

\[
{m_D\over D}+\lambda x_D
>
C_0+\lambda(1.1812298040-B_0)-o(1).
\]

The right side is exactly the safe decimal

\[
1.1988388040+{15\over8}(1.1812298040-0.30483522)
=2.8420786490.
\]

This proves (WS.7).

Intersecting (WS.7) with the existing audited quarter-weight line (WS.8) gives the exact
safe-rational values

\[
x_*={673966197\over812500000}
=0.829496857846153\ldots,
\]

\[
m_*={16728036527\over13000000000}
=1.286772040538461\ldots .
\]

Every convergent live subsequential pair `(M,X)` must lie above both lines.  Therefore
`M>m_*` or `X>x_*`, proving (WS.10).  No assertion about which branch is realized is
made.

---

## 7. Scope and remaining bottleneck

The new argument is deliberately narrow.

- It uses only finite graph degree information already present after maximal activation.
- It does not assume `K_6` or any other abstract degree-five graph is geometrically
  impossible.
- It does not promote a selected closure-row minor to a full nonlinear realization.
- Exact finite flex enters only through the already proved pair-shield manifold.
- Contact-isolated source points remain outside the core matrices and are not deleted.
- The theorem state is unchanged.

The remaining live obstruction has a sharper feasible region.  Low-flex survivors are
still forced by the old quarter-weight law to have large `d_H+p_D`; high-corank
survivors now pay much faster than the old quarter-slope once `sigma_C/D` exceeds about
`0.351733`.  A closing step still has to control the unconverted quantity `d_H+p_D` or
show that the actual straight-line diameter graph cannot positively lock the exact
manifold in this narrowed region.

**Disposition:** refined the pentagon bootstrap by its exact degree-dependent random-order
loss, charged degree-five residual blocks to zero-anchor pair-shield flex, and obtained
the new weighted conservation law (WS.7).  C-II remains open.