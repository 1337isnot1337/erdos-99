# Erdős Problem #99 — post-endpoint train-slack resolution

**Date:** 2026-09-14
**Repository base:** `438d19079eedbb5defdd2b92e9283276af8069e9`
**State version:** `2026-09-14.audit.51`
**Run type:** closing-proof reduction / exact train-boundary decomposition
**Target:** Target C-II, canonical full-core branch
**Starting input:** `research/target_c_fullcore_post_endpoint_defect_split_2026-09-14.md`
**External literature:** not used
**Computation:** a dependency-free regression script checks the finite algebra and component inequalities

## LEVEL I STATUS

`STILL OPEN`

This note resolves the opaque train-boundary slack in the current post-endpoint
four-way split into two separate geometric currencies. The resulting refinement is
useful away from the excluded exact floor endpoint: if its train-isoperimetric part
is sublinear, then the full strict-rhombus complex already has a unique dominant
component and an asymptotically Mantel-extremal train-crossing graph, even when
`mu_D-mu_TC` stays bounded away from zero for some other reason.

No source-preserving diameter decrease or exact unit triangle is proved here.

## 1. Canonical input

Work in a canonical full-core near-disk Type-II survivor. Use the notation of the
post-endpoint defect split:

- `q` is the number of loaded force-hull vertices;
- `k=d_H+s_Z`;
- `p=per(F)` is the loaded force-hull perimeter;
- `b` is the occurrence-counted old outer contact-face walk length;
- `f` is the number of bounded nonquadrilateral contact faces;
- `Q=sum_F(deg(F)-4)` over those faces;
- `R_4` is the number of strict unit-rhombus faces;
- `B_4` is the number of contact-edge occurrences incident to exactly one strict
  rhombus;
- `T=B_4/2` is the number of stopped strict-rhombus trains;
- `m_B` is the number of nonunit loaded force-hull sides; and
- `c_I=O(D^(2/3))` is the unloaded-component count.

The exact outer-face identity is

\[
b+Q=2(q-k).
\tag{TS.1}
\]

Canonical Section 85 gives two inequalities before they are composed:

\[
B_4\le b+4f+Q,
\qquad
B_4\ge4\sqrt{R_4}.
\tag{TS.2}
\]

The first is an occurrence-capacity statement: every boundary occurrence of the
strict-rhombus complex faces either the old outer face or one bounded
nonquadrilateral face. The second is Theorem 10.6: `B_4=2T` and the train-crossing
graph is simple and triangle-free, hence `R_4<=T^2/4` by Mantel.

The previous post-endpoint note packages (TS.2) only through

\[
\tau_D:=(q-k)+2f-2\sqrt{R_4}\ge0.
\tag{TS.3}
\]

Its exact surplus identity is

\[
\mu_DD
=\frac{2p+2\sqrt{R_4}}5
+m_B+\frac25(Q-f)+\frac25(b-p)+\frac15\tau_D
-2c_I-4.
\tag{TS.4}
\]

## 2. Exact resolution of the train slack

Define two nonnegative defects

\[
\boxed{\rho_D:=b+4f+Q-B_4\ge0}
\tag{TS.5}
\]

and

\[
\boxed{\sigma_D:=B_4-4\sqrt{R_4}\ge0.}
\tag{TS.6}
\]

`rho_D` is **recipient-capacity waste**: it counts the unused occurrence capacity
left after the strict-rhombus boundary occurrences are injected into outer-face and
nonquadrilateral-face occurrences. It is an integer.

`sigma_D` is **train-isoperimetric slack**: it measures failure of the complete
strict-rhombus train system to attain Theorem 10.6's boundary lower bound. It need
not be an integer because of `sqrt(R_4)`.

### Theorem TS.1 — exact two-currency split

The old train slack satisfies the finite identity

\[
\boxed{2\tau_D=\rho_D+\sigma_D.}
\tag{TS.7}
\]

Consequently (TS.4) sharpens, without any asymptotic argument, to

\[
\boxed{
\begin{aligned}
\mu_DD
={}&\frac{2p+2\sqrt{R_4}}5
+m_B+\frac25(Q-f)+\frac25(b-p)\\
&+\frac1{10}\rho_D+\frac1{10}\sigma_D
-2c_I-4.
\end{aligned}}
\tag{TS.8}
\]

#### Proof

By (TS.1),

\[
b+4f+Q=2(q-k)+4f=2[(q-k)+2f].
\]

Therefore

\[
\begin{aligned}
\rho_D+\sigma_D
&=(b+4f+Q-B_4)+(B_4-4\sqrt{R_4})\\
&=2[(q-k)+2f-2\sqrt{R_4}]\\
&=2\tau_D.
\end{aligned}
\]

Substitute `tau_D=(rho_D+sigma_D)/2` into (TS.4).  No inequality is lost.

## 3. The train-isoperimetric slack is exactly a Mantel deficit

Let `G_D` be the train-crossing graph. It has `T` vertices and exactly `R_4`
edges. Define its Mantel deficit

\[
M_D:=\frac{T^2}{4}-R_4\ge0.
\tag{TS.9}
\]

Because `B_4=2T`, rationalizing (TS.6) gives

\[
\begin{aligned}
\sigma_D
&=2T-4\sqrt{R_4}
=2(T-2\sqrt{R_4})\\
&=\boxed{\frac{8M_D}{T+2\sqrt{R_4}}}.
\end{aligned}
\tag{TS.10}
\]

Thus (TS.8) can equivalently be written

\[
\boxed{
\begin{aligned}
\mu_DD
={}&\frac{2p+2\sqrt{R_4}}5
+m_B+\frac25(Q-f)+\frac25(b-p)\\
&+\frac1{10}\rho_D
+\frac{4M_D}{5(T+2\sqrt{R_4})}
-2c_I-4.
\end{aligned}}
\tag{TS.11}
\]

This makes the graph-theoretic meaning of the fifth currency explicit. A first-order
surplus carried by `sigma_D` is not a small perturbation of the Mantel endpoint: it
is a quadratic crossing deficit.

## 4. Quantitative dichotomy for the train graph

The canonical full-core asymptotics include

\[
\frac{R_4}{D^2}\longrightarrow
\Delta_2:=\frac{\pi}{2\sqrt3}>0.
\tag{TS.12}
\]

### Corollary TS.2 — linear train slack gives quadratic Mantel deficit

Along any subsequence with

\[
\sigma_D\ge\delta D
\]

for a fixed `delta>0`,

\[
\boxed{
M_D\ge
\left(\frac{\delta\sqrt{\Delta_2}}4-o(1)\right)D^2.
}
\tag{TS.13}
\]

Indeed, (TS.10) is equivalent to

\[
M_D=\frac{\sigma_D(T+2\sqrt{R_4})}{8}
\ge\frac{\sigma_D\sqrt{R_4}}4.
\]

### Corollary TS.3 — sublinear train slack forces near-Mantel structure

If instead

\[
\sigma_D=o(D),
\tag{TS.14}
\]

then

\[
T=2\sqrt{R_4}+o(D)
=(2\sqrt{\Delta_2}+o(1))D
\tag{TS.15}
\]

and, by (TS.10),

\[
\boxed{M_D=o(D^2).}
\tag{TS.16}
\]

Hence the existing elementary Mantel-stability lemma applies to `G_D`: there is a
partition of the stopped trains into two shores of size `T/2+o(D)` such that the
number of within-shore crossings and the number of missing cross-shore crossings
are both `o(D^2)`.

The point is the scope. Earlier Mantel stability was obtained at the now-excluded
special endpoint `mu_D->mu_TC`. Here the antecedent is only the single geometric
condition `sigma_D=o(D)`. The other post-endpoint currencies may remain linear, so
this near-bipartite train structure persists throughout a much larger portion of the
surviving high-surplus branch.

## 5. Sublinear train slack also forces one dominant rhombic component

Decompose the strict-rhombus complex into edge-connected components. Let component
`i` have `T_i` stopped trains and `R_i` rhombi. Tracks do not pass between distinct
components, and Theorem 10.6 applies componentwise:

\[
R_i\le\frac{T_i^2}{4}.
\tag{TS.17}
\]

Let `T_max=max_i T_i`. Since `sum_i T_i=T` and `sum_i R_i=R_4`,

\[
\begin{aligned}
M_D
&=\frac{T^2}{4}-\sum_iR_i\\
&\ge\frac{T^2-\sum_iT_i^2}{4}\\
&\ge\frac{T(T-T_{\max})}{4}.
\end{aligned}
\tag{TS.18}
\]

The last inequality uses `sum_i T_i^2<=T_max sum_i T_i=T_max T`.
Under (TS.14), (TS.15)--(TS.16) therefore imply

\[
\boxed{T-T_{\max}=o(D).}
\tag{TS.19}
\]

All components other than a maximizing one together contain only `o(D)` trains.
Applying Theorem 10.6 to their disjoint union gives

\[
\sum_{i\ne i_*}R_i
\le\frac{(T-T_{\max})^2}{4}
=o(D^2),
\tag{TS.20}
\]

so the maximizing component satisfies

\[
\boxed{R_{i_*}=R_4-o(D^2).}
\tag{TS.21}
\]

Thus sublinear `sigma_D` forces a unique macroscopic rhombic carrier in the strong
sense relevant to the crossing graph: it contains all but `o(D)` trains and all but
`o(D^2)` strict rhombi.

### Corollary TS.4 — if both train slacks are sublinear, one component occupies almost every recipient slot

Assume in addition to `sigma_D=o(D)` that

\[
\rho_D=o(D).
\tag{TS.22}
\]

Let `i_*` be the dominant component from (TS.19)--(TS.21). Every stopped train has
exactly two boundary occurrences, so the total number of strict-rhombus boundary
occurrences belonging to all other components is

\[
2(T-T_{\max})=o(D).
\]

On the other hand, `rho_D` is exactly the difference between the total recipient
capacity `b+4f+Q` and the used strict-rhombus boundary capacity `B_4`. Therefore all
but `o(D)` outer-face/nonquadrilateral-face recipient occurrences are occupied by
boundary edges of the single dominant rhombic component.

This is stronger than merely saying the train graph is near-Mantel: when both pieces
of the old `tau_D` slack are sublinear, the same macroscopic component controls both
quadratic crossing mass and essentially the entire linear defect interface.

## 6. Refined post-endpoint branch split

The canonical endpoint exclusion gives a non-explicit `epsilon_*>0` with
`mu_D>=mu_TC+epsilon_*` for every sufficiently large canonical full-core survivor.
Combining that fact with (TS.8), `p/D->pi`, `R_4/D^2->Delta_2`, and `c_I=o(D)` yields

\[
\mu_D-\mu_{\rm TC}
=\frac1D\left[
 m_B+\frac25(Q-f)+\frac25(b-p)
 +\frac1{10}\rho_D+\frac1{10}\sigma_D
\right]+o(1).
\tag{TS.23}
\]

All five bracketed currencies are nonnegative. Consequently some non-explicit
`delta_*>0` satisfies, for all sufficiently large full-core survivors,

\[
\boxed{
\max\{m_B,Q-f,b-p,\rho_D,\sigma_D\}\ge\delta_*D.
}
\tag{TS.24}
\]

As in the four-way split, after increasing the diameter threshold one may take any
`delta_*<epsilon_*/4`: if every raw defect were below `delta_*D`, the weighted sum
in (TS.23) would be below `2delta_*D<epsilon_*D/2`, contradicting (TS.23) and the
uniform endpoint gap once the `o(1)` term is smaller than `epsilon_*/2`.

This yields a sharper research frontier:

1. **loaded-side branch:** `m_B=Omega(D)`;
2. **high-degree exceptional-face branch:** `Q-f=Omega(D)`;
3. **outer metric-detour branch:** `b-p=Omega(D)`;
4. **recipient-vacancy branch:** `rho_D=Omega(D)`; or
5. **train-Mantel branch:** `sigma_D=Omega(D)`, equivalently a quadratic Mantel
   deficit by (TS.13).

If branch 5 is absent, one does not return to an unstructured train system: Corollary TS.3 and equations (TS.19)--(TS.21) force an almost-balanced near-bipartite crossing graph concentrated in one macroscopic rhombic component. This is the main gain over leaving `tau_D` opaque.

## 7. Scope audit and next use

The argument uses only already-audited finite inputs:

- the occurrence identity `b+Q=2(q-k)`;
- the Section-85 recipient inequality `B_4<=b+4f+Q`;
- Theorem 10.6, including `B_4=2T` and `R_4<=T^2/4` for complexes with holes and
  disconnected components; and
- the proof-only post-endpoint identity (TS.4), itself an exact algebraic
  composition of current canonical full-core inputs.

No identification of repeated outer-walk vertices is made; all relevant quantities
are occurrence-counted. No contact-isolated source point is deleted. No lattice chart,
KKT force transfer, or source-preserving deformation is assumed.

This note is a proof-only refinement, not a theorem-state promotion. The most useful
next attack is now conditional and geometric: in the `sigma_D=o(D)` branch, exploit
the single dominant near-Mantel rhombic component together with the phase labels and
actual outer/exceptional recipient vacancies. The remaining obstacle is to convert
near-complete train crossing into a source-level complete-grid/deformation statement
without assuming the exact floor endpoint.
