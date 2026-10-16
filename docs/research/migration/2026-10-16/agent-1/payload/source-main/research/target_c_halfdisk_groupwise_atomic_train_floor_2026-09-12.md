# Target C — groupwise atomic train floor in the two-half-disk branch

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Status:** proof-only theorem stacked on the all-regime half-disk dichotomy and audited-working §§129/142; theorem authority unchanged.

The two-half-disk alternative has more information than the global stopped-train measure sees.  Each dominant cap group carries half of the quadratic strict-rhombus area.  Up to `o(D)` exceptional trains, strict-rhombus trains cannot move between harmonic cells.  Therefore the weighted-Mantel atomic-phase argument of §142 can be applied **separately** to the two dominant half-disk groups.

This doubles the number of independent quadratic crossing systems and raises the absolute atomic train-mass floor by a factor `sqrt(2)`:

\[
\boxed{
 x s\ge 2\sqrt{2\Delta_2}
 =2\sqrt{\frac{\pi}{\sqrt3}}
 =2.693547374177197\ldots,
}
\tag{1}
\]

where `T/D->x` and `s` is the total atomic mass of the global stopped-train phase probability measure.

Combining with the existing global exposed-hull theorem gives

\[
\boxed{
\liminf {T-q/2\over D}
\ge 2\sqrt{2\Delta_2}
=2.693547374177197\ldots .
}
\tag{2}
\]

Consequently

\[
\boxed{
\liminf {2f-k\over D}
\ge
2\sqrt{2\Delta_2}-{\pi\over2}
=1.122751047382300\ldots .
}
\tag{3}
\]

Repeating the audited §146 elimination yields the two-half-disk weighted diameter-edge floor

\[
\boxed{
\liminf {1\over D}
\left(
 h-{d_H\over9}-{10s_Z\over9}
\right)
\ge
{4\pi\over9}
+{4\over9}\sqrt{\frac{\pi}{\sqrt3}}
=1.994829484745952\ldots .
}
\tag{4}
\]

This is a structural gain, not a carrier-decimal improvement.  It uses the two independent quadratic half-disk train systems forced by the no-wrapping branch.

---

## 1. Half-disk groups carry half the rhombus count

Work along the finite diagonal in the two-half-disk alternative from
`target_c_allregime_halfdisk_dichotomy_2026-09-12.md`.  Let `G_1,G_2` be the two dominant groups.  That theorem gives

\[
\sum_{r\in G_i}A_{4,r}
=\left({\pi\over8}-o(1)\right)D^2,
\qquad i=1,2.
\tag{1.1}
\]

Put

\[
a_0={\sqrt3\over2},
\qquad
\Delta_2={\pi\over2\sqrt3}.
\]

Every strict triangle-free unit rhombus has area at least `a_0`.  In Type II the global strict-rhombus count and area satisfy

\[
{R_4\over D^2}\to\Delta_2,
\qquad
{A_4\over D^2}\to{\pi\over4}=a_0\Delta_2.
\tag{1.2}
\]

Therefore the global nonnegative rhombus-area excess

\[
E_4:=A_4-a_0R_4
\]

is `o(D^2)`.  Restricting a nonnegative excess to either group preserves that bound.  If

\[
R_i:=\sum_{r\in G_i}R_r
\]

is the local strict-rhombus count in group `i`, then

\[
0\le
\sum_{r\in G_i}A_{4,r}-a_0R_i
\le E_4=o(D^2).
\tag{1.3}
\]

Using (1.1),

\[
\boxed{
{R_i\over D^2}
\longrightarrow
{\pi/8\over a_0}
={\pi\over4\sqrt3}
={\Delta_2\over2},
\qquad i=1,2.
}
\tag{1.4}
\]

Thus each half-disk group carries one half of the global quadratic train-crossing mass.

---

## 2. Remove the `o(D)` trains that can change harmonic-cell label

Audited §129 gives

\[
0\le R_4-\sum_rR_r\le3c_I+5=o(D).
\tag{2.1}
\]

Call the rhombi counted by this difference **nonlocal rhombi**.  Every physical strict rhombus lies at the crossing of exactly two complete stopped trains.  Delete every complete train incident to at least one nonlocal rhombus.  Equation (2.1) deletes at most

\[
2(3c_I+5)=o(D)
\tag{2.2}
\]

trains.

The full stopped-train crossing graph is simple and has `T=O(D)` vertices by audited §142.  Hence deleting `o(D)` train vertices removes only

\[
o(D)\,O(D)=o(D^2)
\tag{2.3}
\]

strict-rhombus crossings.

It remains to check that every undeleted train belongs to one harmonic cell whenever it participates in a rhombus.  Consecutive rhombi on one train share a positive contact edge.

- If that shared edge has an unloaded endpoint, the two rhombi contain a vertex from the same connected unloaded component, so two local realizations have the same harmonic-cell label.
- If both endpoints are loaded, the edge is a loaded-loaded unit contact.  The audited Type-II localization `c_B=0` makes it a side of the global force hull.  A force-hull side has the force hull on only one side, so it cannot have two bounded strict-rhombus faces on opposite sides inside the core.  Thus a train cannot change from one local cell to another across such an edge.

Therefore every undeleted train containing a strict rhombus has one well-defined harmonic-cell label.  Assign it to the corresponding dominant group when that cell belongs to `G_1` or `G_2`.

Let `\mathcal T_{i,D}` be the retained trains assigned to `G_i`, and let `R'_{i,D}` be their mutual strict-rhombus crossings.  By (1.4) and (2.3),

\[
\boxed{
{R'_{i,D}\over D^2}\to{\Delta_2\over2}.
}
\tag{2.4}
\]

The two train families `\mathcal T_{1,D}` and `\mathcal T_{2,D}` are disjoint subsets of the complete global train set.

---

## 3. Run the §142 atomic-phase argument inside each group

Pass to one further common subsequence on which

\[
{|\mathcal T_{i,D}|\over D}\to x_i,
\qquad i=1,2,
\tag{3.1}
\]

and their empirical projective phase measures converge:

\[
\mu_{i,D}\Rightarrow\mu_i.
\]

Equation (2.4) and Mantel already imply `x_i>0`.

Let `s_i` be the total atomic mass of the probability measure `\mu_i`.  The proof of §142.3 is local to a simple triangle-free train-crossing graph and the rhombus angle-excess estimate, so it applies verbatim to each retained group:

1. the induced group crossing graph is simple and triangle-free;
2. the global nonnegative strict-rhombus area excess is `o(D^2)`, so for every fixed `epsilon>0` only `o(D^2)` group crossings have projective phase separation at least `pi/3+epsilon`;
3. hence every group crossing-measure limit is supported on the exact relation `psi-phi=+-pi/3 mod pi`;
4. simplicity bounds that crossing measure by the product phase measure;
5. the exact `+-pi/3` relation receives product-measure mass only from phase atoms; and
6. weighted Mantel on the atomic phase-orbit graph gives

\[
{\Delta_2/2\over x_i^2}
\le {s_i^2\over4}.
\tag{3.2}
\]

Therefore

\[
\boxed{
 x_i s_i\ge2\sqrt{\Delta_2/2},
\qquad i=1,2.
}
\tag{3.3}
\]

No exposed-hull theorem is used groupwise.

---

## 4. Atomic masses of the two positive train measures add

It is cleaner here to use absolute train measures.  Put

\[
\lambda_D:={1\over D}\sum_{\tau\in\mathcal T_D}\delta_{[u_\tau]},
\qquad
\lambda_{i,D}:={1\over D}\sum_{\tau\in\mathcal T_{i,D}}\delta_{[u_\tau]}.
\tag{4.1}
\]

Along the common subsequence,

\[
\lambda_D\Rightarrow\lambda,
\qquad
\lambda_{i,D}\Rightarrow\lambda_i=x_i\mu_i.
\]

Because the two retained group train sets are disjoint subsets of the global train set, after passing to a limit there is a positive residual measure `\lambda_0` with

\[
\lambda=\lambda_1+\lambda_2+\lambda_0.
\tag{4.2}
\]

For finite positive measures, total atomic mass is additive: if `At(\nu)=\sum_x\nu(\{x\})`, then

\[
At(\nu_1+\nu_2)=At(\nu_1)+At(\nu_2).
\tag{4.3}
\]

The global measure has total mass `x` and atomic mass `xs`; each group measure has atomic mass `x_i s_i`.  Therefore (3.3) gives

\[
\begin{aligned}
xs
=At(\lambda)
&\ge At(\lambda_1)+At(\lambda_2)\\
&=x_1s_1+x_2s_2\\
&\ge4\sqrt{\Delta_2/2}.
\end{aligned}
\]

Thus

\[
\boxed{
xs\ge2\sqrt{2\Delta_2}
=2\sqrt{\frac\pi{\sqrt3}}.
}
\tag{4.4}
\]

This is (1).  There is no loss when the two group measures have atoms at the same projective direction: positive atomic masses at the same point add rather than cancel.

---

## 5. The global exposed-hull theorem converts atomic mass to a train floor

Now use §142.4 only once, globally.  Its exposed-hull inequality is

\[
{q\over T}\le2(1-s).
\tag{5.1}
\]

Multiplying by `x=T/D` gives

\[
xs\le x-{q\over2D}
={T-q/2\over D}.
\tag{5.2}
\]

Combine (4.4) and (5.2):

\[
\boxed{
\liminf {T-q/2\over D}
\ge
2\sqrt{2\Delta_2}
=2.693547374177197\ldots .
}
\tag{5.3}
\]

This is (2).

Since

\[
T-q=2f-k
\tag{5.4}
\]

and the loaded convex hull obeys `q<=per(F)<=pi D`,

\[
\boxed{
\liminf {2f-k\over D}
\ge
2\sqrt{2\Delta_2}-{\pi\over2}
=1.122751047382300\ldots .
}
\tag{5.5}
\]

This is (3).  In particular the two-half-disk branch contains at least

\[
\left({1\over2}\left[2\sqrt{2\Delta_2}-{\pi\over2}\right]-o(1)\right)D
= (0.561375523691150\ldots-o(1))D
\]

bounded nonquadrilateral faces even when `k=o(D)`.

---

## 6. Weighted diameter-edge consequence

Repeat the audited §146 elimination with the strengthened input

\[
C_{HD}:=2\sqrt{2\Delta_2}
\le\liminf {T-q/2\over D}.
\tag{6.1}
\]

Pass to a subsequence with

\[
{h\over D}\to y,
\qquad
{d_H\over D}\to d,
\qquad
{s_Z\over D}\to z.
\]

Using `T=q+2f-k`, `q=h+d_H`, and `k=d_H+s_Z`, (6.1) gives

\[
\liminf {f\over D}
\ge {C_{HD}\over2}-{y\over4}+{d\over4}+{z\over2}.
\tag{6.2}
\]

The exact outer ledger and Type-II perimeter convergence give

\[
\limsup{Q\over D}+2z\le2y-\pi.
\tag{6.3}
\]

Since `Q>=f`, combine (6.2)--(6.3):

\[
{9y\over4}
\ge
\pi+{C_{HD}\over2}+{d\over4}+{5z\over2}.
\]

Therefore

\[
\boxed{
\liminf {1\over D}
\left(
 h-{d_H\over9}-{10s_Z\over9}
\right)
\ge
{4\pi\over9}+{2C_{HD}\over9}
={4\pi\over9}+{4\over9}\sqrt{\frac\pi{\sqrt3}}.
}
\tag{6.4}
\]

Numerically the right side is

\[
\boxed{1.994829484745952\ldots .}
\tag{6.5}
\]

This is (4).

---

## 7. Scope and live obstruction

The theorem applies only to the **two-half-disk alternative** of the proof-only all-regime dichotomy.  The center-wrapping branch remains separate.

The argument:

- does not delete any source point;
- deletes only `o(D)` train vertices inside an auxiliary proof graph;
- does not extend the affine-kernel theorem to contact-isolated coordinates;
- uses no outer-detour smallness or scalar-slack endpoint;
- uses the global exposed-hull theorem only after the two groupwise atomic lower bounds have been established.

It does not yet contradict `h<=q<=pi D`.  The surviving two-half-disk branch has a much narrower boundary-order profile: it must carry at least `1.122751D-o(D)` of `2f-k` defect and weighted diameter-edge density at least `1.994829D-o(D)`.

The next useful attack is therefore not another generic train-count lower bound.  It should exploit either:

1. the geometry/rank cost of the forced linear defect-face population inside two complementary half-disks; or
2. the fact that each half-disk group independently needs atomic phase mass `2sqrt(Delta_2/2)` while both systems share one near-circular loaded boundary and one global diameter graph.

**Disposition:** proof-only branch-specific strengthening; C-II remains open.
