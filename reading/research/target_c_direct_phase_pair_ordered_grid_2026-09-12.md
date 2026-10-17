> Generated reading edition · [exact source](../../research/target_c_direct_phase_pair_ordered_grid_2026-09-12.md) · source SHA-256 `10d2375f32ec2d0bf981635388237795efbcbb7140d20710966c078ffabe765d`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "30f465971124dadd6a50737c34b4132e9d33118f", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_direct_phase_pair_ordered_grid_2026-09-12.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "9201decfd47ee08703fb208b44702180d69ffc2ee6234af8c3bdd322da1d9ef4"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C — direct ordered-grid extraction from one full phase-label pair

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Status:** proof-only research candidate; theorem authority unchanged.

Canonical Section 91 first makes a quadratic **phase-threshold cut** before it obtains
one common monotone coordinate. That cut is unnecessary. After the canonical
Section-68 phase-circle cut, any fixed pair of distinct phase labels already has one
common monotone coordinate if both label families are given their canonical train
orientations. The reason is that their two canonical displacement cones together have
angular width strictly smaller than `pi` on every finite source.

This removes the density-squaring loss

$$
E\asymp D^2\longmapsto {E^2\over T^2}
$$

from the beginning of Section 91. Combining the direct monotonicity with its
endpoint-balanced slab argument and the exact interval-block counting theorem gives a
linear-by-linear complete ordered grid directly from one full phase-label pair.

The theorem is structural progress, not C-II closure. The oblique-lattice regression
in `research/target_c_oblique_lattice_structural_regression_2026-09-12.md` shows why a
large ordered grid alone cannot close the problem.

---

## 1. Starting carrier and phase-circle cut

Work in one full-core Type-II harmonic carrier. Let `R_D` be its number of strict
rhombi and `T_D` its number of local train segments. Suppose fixed constants `r,C_0>0`
satisfy, for all sufficiently large members of the sequence,

$$
R_D\ge rD^2,
\qquad
T_D\le C_0D.
\tag{1.1}
$$

Canonical Section 90 begins from exactly this situation. Apply the canonical
Section-68 phase-circle cut. It deletes only `O(D)` crossing rhombi and places every
remaining train reduced phase in one common open interval

$$
I=(s,s+L),
\qquad L={\pi\over3}.
\tag{1.2}
$$

Thus, after increasing the threshold on `D`, at least

$$
{3r\over4}D^2
\tag{1.3}
$$

carrier crossings remain. Every retained crossing joins two distinct labels in
`Z/3Z`, so one of the three unordered label pairs supports at least

$$
\boxed{E\ge\eta D^2,
\qquad \eta:={r\over4}.}
\tag{1.4}
$$

Let `A,B` be the local train segments in that pair. Relabel cyclically so that

$$
\ell_B-\ell_A\equiv1\pmod3.
\tag{1.5}
$$

Choose integer lifts with `ell_B=ell_A+1`; if the labels wrap modulo three, add `3`
to the lift of `ell_B`. For a train write

$$
\alpha_a=x_a+L\ell_A,
\qquad
\beta_b=x_b+L\ell_B.
\tag{1.6}
$$

At every actual `A`--`B` crossing the canonical oriented phase law gives

$$
\boxed{x_b-x_a=\delta_{ab}>0.}
\tag{1.7}
$$

No inverse-diameter defect cutoff is used.

Because the two label families are disjoint subsets of the local train set,

$$
\boxed{|A|+|B|\le T_D\le C_0D.}
\tag{1.8}
$$

---

## 2. The full label pair already has one common monotone coordinate

Let

$$
x_-:=\min_{A\cup B}x_\tau,
\qquad
x_+:=\max_{A\cup B}x_\tau.
$$

The train set is finite and all reduced phases lie in the open interval (1.2), so

$$
\boxed{x_+-x_-<L.}
\tag{2.1}
$$

Canonical Theorem 10.6 orients a train with physical unit-edge argument `alpha` so
that every elementary centerline displacement has argument in

$$
(\alpha+L,\alpha+2L).
\tag{2.2}
$$

Orient **both** `A` and `B` trains canonically. Every elementary displacement of an
`A` train then has argument in the common interval

$$
(x_-+L\ell_A+L,\ x_++L\ell_A+2L),
$$

while every elementary displacement of a `B` train has argument in

$$
(x_-+L\ell_A+2L,\ x_++L\ell_A+3L).
$$

The union is contained in

$$
J=(x_-+L\ell_A+L,\ x_++L\ell_A+3L),
\tag{2.3}
$$

whose length is

$$
|J|=(x_+-x_-)+2L<3L=\pi.
\tag{2.4}
$$

Choose a unit vector `e` whose argument is the midpoint of `J`. Every selected
centerline displacement then has strictly positive projection on `e`. Hence

$$
\boxed{X(p):=e\cdot p}
\tag{2.5}
$$

strictly increases along every selected canonically oriented train.

This is the point missed by the phase-threshold step in Section 91: reversing the
second shore requires a phase separation, but orienting both shores canonically does
not.

At an actual crossing `ab`, (1.7) gives

$$
L<\beta_b-\alpha_a<2L.
\tag{2.6}
$$

The local forward centerline displacement on the canonical `A` train is `v_b`; the
local forward displacement on the canonical `B` train is `-u_a`. Therefore

$$
\det(v_b,-u_a)=\det(u_a,v_b)>0.
\tag{2.7}
$$

Both vectors have positive `X` component by (2.5), so all actual `A`--`B` crossings
have one common graph-crossing sign.

Trains in one label family cannot cross one another: every strict-rhombus crossing
has two distinct phase labels. The canonical pseudosegment theorem then makes each
family pairwise disjoint.

We have proved:

> **Lemma 2.1 — direct phase-pair monotonicity.** After the canonical phase-circle
> cut, every fixed pair of distinct phase-label families can be canonically oriented
> so that all selected train centerlines are strictly monotone in one common linear
> coordinate, the two shores are internally disjoint, and every actual cross-shore
> crossing has one common sign. No phase-threshold cut and no `O(1/D)` defect cutoff
> is required.

---

## 3. Endpoint-balanced slabs applied directly to the quadratic pair

Fix an integer `M>=2`. Perturb `e` within the strict cone if necessary so that all
selected train-end `X` coordinates are distinct and no slab boundary passes through a
crossing.

Partition the `X` axis into `M` consecutive open slabs, with cuts between endpoint
coordinates, so that if `p_j` is the number of train endpoints in slab `j`, then

$$
\max_jp_j\le {2N\over M}+2,
\qquad
N:=|A|+|B|\le C_0D.
\tag{3.1}
$$

Assign every crossing edge to the slab containing its crossing. Call an assigned
edge bad when **both** of its train segments have an endpoint in that slab. If a slab
contains `A_j` such `A` trains and `B_j` such `B` trains, then

$$
A_j+B_j\le p_j,
\qquad
\#\text{bad}_j\le A_jB_j\le {p_j^2\over4}.
$$

Since `sum_j p_j<=2N`,

$$
\begin{aligned}
\#\text{bad}
&\le {1\over4}(\max_jp_j)\sum_jp_j\\
&\le {N^2\over M}+N\\
&\le {C_0^2\over M}D^2+C_0D.
\end{aligned}
\tag{3.2}
$$

Put

$$
\boxed{M_0:=\left\lfloor{2C_0^2\over\eta}\right\rfloor+1.}
\tag{3.3}
$$

Then `C_0^2/M_0<eta/2`, so for all sufficiently large `D`, (1.4) and (3.2) leave at
least

$$
\left({\eta\over2}-o(1)\right)D^2
\tag{3.4}
$$

nonbad crossing edges.

For every nonbad edge, at least one of its two train segments has no endpoint in the
crossing slab. Since that train is `X`-monotone and contains a point in the slab, its
two endpoints lie on opposite sides: the train spans the whole slab.

Assign each nonbad edge to one spanning shore. One shore receives at least half the
assignments, and one of the `M_0` slabs receives at least the average. Thus some slab
`S` contains a pairwise-disjoint spanning family, say `B_S`, and incident `A` trains
with

$$
\boxed{
E_S\ge\left({\eta\over4M_0}-o(1)\right)D^2
}
\tag{3.5}
$$

actual crossings inside `S`.

Enlarge this edge set to all actual crossings inside `S` between the incident `A`
trains and `B_S`. Because every curve is `X`-monotone, the `B_S` curves are pairwise
disjoint and span `S`, and every crossing has the same sign, the proof of canonical
Lemma 91.2 applies verbatim: each `A`-neighborhood in the vertical order of `B_S` is
an interval.

---

## 4. Exact interval counting gives a linear complete grid

We include the short counting step so this theorem is self-contained.

Let an interval-neighborhood bipartite graph have shore sizes `a,b` and `e` edges,
with the `b`-shore linearly ordered. For an integer `k>=1`, every row interval of
length `d_x` contains `max(d_x-k+1,0)` consecutive `k`-blocks. Hence the total number
of row/block incidences is at least

$$
e-a(k-1).
\tag{4.1}
$$

If no consecutive `k`-block were contained in at least `k` row neighborhoods, this
incidence count would be at most

$$
(k-1)(b-k+1).
\tag{4.2}
$$

Therefore a `K_{k,k}` exists whenever

$$
\boxed{e>(k-1)(a+b-k+1).}
\tag{4.3}
$$

In particular

$$
\boxed{k=\left\lfloor{e\over a+b}\right\rfloor}
\tag{4.4}
$$

is safe whenever it is positive. Indeed `e>=k(a+b)`, which is stronger than (4.3).

For the slab graph, `a+b<=N<=C_0D`. From (3.5), for every fixed

$$
0<c<{\eta\over4M_0C_0},
\tag{4.5}
$$

all sufficiently large sources therefore contain a complete ordered grid with

$$
\boxed{|A_0|,|B_0|\ge cD.}
\tag{4.6}
$$

Substituting `eta=r/4`, a convenient explicit coefficient is any

$$
\boxed{
0<c<c_{\rm dir}:={r\over16C_0M_0},
\qquad
M_0=\left\lfloor{8C_0^2\over r}\right\rfloor+1.
}
\tag{4.7}
$$

Ignoring only the harmless integer rounding in `M_0`, the leading coefficient is

$$
\boxed{c_{\rm dir}\sim {r^2\over128C_0^3}.}
\tag{4.8}
$$

The important improvement is the dependence on the original carrier crossing density.
The phase-threshold route in canonical Section 91 first replaces that density by a
quantity quadratic in it before the slab extraction. Equation (4.7) avoids that loss.

---

## 5. Diameter consequence and hostile non-closure check

The extracted shores have fixed distinct labels and every cross-shore pair is an
actual strict-rhombus crossing. Canonical Section 76 therefore supplies common order
and the defect-averaged diameter estimate

$$
d_*\ge {\sqrt3\over2}(|A_0|+|B_0|)
-{S_{A_0B_0}\over\min\{|A_0|,|B_0|\}}-2.
\tag{5.1}
$$

Every grid crossing is one source rhombus, so the global Section-68 angular-defect
budget gives

$$
S_{A_0B_0}\le C_{\rm phase}D.
\tag{5.2}
$$

Thus for fixed `c<c_dir`,

$$
\boxed{
d_*\ge\sqrt3\,cD-{C_{\rm phase}\over c}-2.
}
\tag{5.3}
$$

A direct contradiction with `d_*<=D` would require `c_dir>1/sqrt(3)`. The currently
certified constants do not give this. Hence the theorem removes a real combinatorial
loss but does not close the full-core branch.

The oblique-lattice regression shows that no theorem of this type can close C-II from
ordered-grid geometry alone: arbitrarily large triangle-free oblique-lattice disks
have exactly the same qualitative ordered-grid structure. The next step must combine
this improved coverage with a source-level currency absent from that regression,
most plausibly global-minimality/loaded-diameter response or an injective outer-walk
payment theorem.

No source point is moved or deleted, and no full-source ZR/ZF affine-kernel conclusion
is used.

**Disposition:** proved candidate. Theorem authority remains `2026-09-12.audit.44`.
