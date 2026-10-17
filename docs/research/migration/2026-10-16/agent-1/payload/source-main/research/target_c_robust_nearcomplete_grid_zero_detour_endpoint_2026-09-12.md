# Target C — robust near-complete train grids exclude the §154 zero-detour floor

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Status:** proof-only theorem candidate; theorem authority unchanged.  
**Base:** `231fcc455f19c54974a3ffd1aaa27f00ca436a86`.  
**Dependencies:** audited-working §§142 and 154; canonical/audited §76 signed `X`-monotone complete-grid order/diameter geometry; elementary near-Mantel stability as already proved in §153.

Put

\[
\Delta_2={\pi\over2\sqrt3},
\qquad
s_2:=\sqrt{\Delta_2},
\qquad
 t_0:={\pi\over2}+{2\over5}s_2
 =1.9517214495404795\ldots .
\]

Audited-working §154 proves that every Type-II survivor sequence with asymptotically
geodesic old outer contact walk

\[
{b-\operatorname{per}(F)\over D}\to0
\tag{0.1}
\]

satisfies

\[
\liminf {q-k\over D}\ge t_0.
\tag{0.2}
\]

This note excludes equality:

\[
\boxed{
(0.1)
\quad\Longrightarrow\quad
{q-k\over D}\not\longrightarrow t_0.
}
\tag{0.3}
\]

The new ingredient is a robust version of the §76 complete-grid diameter argument.
If two phase-pure train families have linear sizes, shrinking phase width, and only
`o(D^2)` missing cross-family crossings, then after removing only `o(D)` trains one can
put both shores in global crossing order. A single opposite-corner crossing then gives
the same two-leg path used by a complete grid, with shore sizes replaced by minimum
degrees. Consequently

\[
|A|+|B|>{2\over\sqrt3}D+cD
\]

is impossible even when `o(D^2)` product crossings are absent.

At the hypothetical §154 endpoint, exact endpoint-capacity saturation forces all
quadratic strict-rhombus crossing mass into one `pi/3` phase orbit. Near-Mantel
stability then produces one atomic family of size `s_2D+o(D)` and an opposite atomic
family of size at least `(s_2/2)D+o(D)`, with only `o(D^2)` missing crossings. Their
combined coefficient is

\[
{3\over2}s_2
=1.428469210295936\ldots
>{2\over\sqrt3}
=1.1547005383792517\ldots ,
\]

contradicting the robust diameter theorem.

No finite forbidden pentagon pattern is used. In particular this theorem is compatible
with the explicit near-three-axis triangle-free pentagon regression.

---

# 1. Robust near-complete grid theorem

We first isolate the geometric statement independently of the endpoint application.

For each `D`, let `A_D,B_D` be two families of complete train centerlines in one
source configuration. Assume:

1. **linear shore sizes**
   \[
   |A_D|=aD+o(D),
   \qquad
   |B_D|=bD+o(D),
   \qquad a,b>0;
   \tag{1.1}
   \]
2. **shrinking two-phase support:** after choosing projective lifts, every `A_D` contact
   direction has angle
   \[
   \alpha_u=\alpha_D+o(1),
   \]
   and every `B_D` contact direction has angle
   \[
   \beta_v=\alpha_D+{\pi\over3}+o(1);
   \tag{1.2}
   \]
3. **near-complete crossing:** the number of absent pairs in `A_D x B_D` is `o(D^2)`;
   every present pair crosses in one actual strict unit rhombus.

Same-shore trains are automatically pairwise disjoint for all sufficiently large `D`:
two directions in one shrinking atom neighborhood have projective separation
`o(1)<pi/3`, whereas a strict triangle-free unit-rhombus crossing requires separation
strictly greater than `pi/3`.

### Theorem 1.1 — robust near-complete grid diameter bound

Under (1.1)--(1.3),

\[
\boxed{
1\ge {\sqrt3\over2}(a+b).
}
\tag{1.3}
\]

Equivalently,

\[
\boxed{
a+b\le{2\over\sqrt3}.}
\tag{1.4}
\]

Thus the leading §76 complete-grid diameter bound is stable under `o(D^2)` missing
product crossings.

The proof is finite after three `o(D)` prunings.

---

## 1.1 Almost all phase values can be strictly separated

Write `L=pi/3`. Choose the real projective lifts in (1.2) so that all large-`D` pairs
satisfy

\[
|\alpha_u-\alpha_D|=o(1),
\qquad
|\beta_v-(\alpha_D+L)|=o(1).
\]

Put

\[
x_u:=\alpha_u,
\qquad
y_v:=\beta_v-L.
\]

If an `A`--`B` pair crosses in a strict rhombus, the local oriented phase law near this
chosen `+L` branch forces

\[
\boxed{y_v>x_u.}
\tag{1.5}
\]

Indeed the oriented direction difference is `L+delta` with `delta>0`. Therefore every
inversion

\[
x_u\ge y_v
\tag{1.6}
\]

is a missing pair. By hypothesis the number of inversions is `o(D^2)`.

We use the following elementary threshold lemma.

### Lemma 1.2 — few inversions imply separation after small tails

Let `X_D,Y_D` be real multisets of sizes `Theta(D)`. If

\[
\#\{(x,y):x\in X_D,y\in Y_D,x\ge y\}=o(D^2),
\]

then there is a threshold `t_D` and subsets obtained by deleting `o(D)` values from
each multiset such that

\[
\boxed{\max X_D'<t_D<\min Y_D'.}
\tag{1.7}
\]

#### Proof

Let `M_D` be the inversion count and, when `M_D>0`, put

\[
\epsilon_D={M_D\over |X_D||Y_D|}\to0,
\qquad
\delta_D=\sqrt{\epsilon_D}.
\]

For each occurrence `x` in `X_D`, let

\[
L_D(x):=\#\{y\in Y_D:y\le x\}.
\]

Then `sum_x L_D(x)=M_D`. Markov's inequality shows that the occurrences with
`L_D(x)>\delta_D|Y_D|` number at most `delta_D|X_D|=o(D)`. The remaining set is
nonempty for all sufficiently large `D`: otherwise `M_D>\delta_D|X_D||Y_D|`,
contradicting `epsilon_D<delta_D`.

Let `x_*` be the largest remaining value, counting its retained occurrence only once
as a value threshold. At most `delta_D|Y_D|=o(D)` occurrences of `Y_D` satisfy
`y<=x_*`, because `L_D(x_*)` has that bound. Delete the exceptional `X_D`
occurrences and those `Y_D` occurrences. The retained multisets satisfy

\[
\max X_D'=x_*<\min Y_D'.
\]

If `M_D=0`, every `x` is strictly smaller than every `y`, so no deletion is needed.
This handles arbitrary multiplicities and ties. `\\square`

Apply Lemma 1.2. Relabel the retained families again as `A_D,B_D`. Their sizes still
satisfy (1.1), their missing-pair count remains `o(D^2)`, and now

\[
\boxed{
\max_{u\in A_D}\alpha_u+L
<
\min_{v\in B_D}\beta_v.
}
\tag{1.8}

Because both direction clusters shrink, also

\[
\max_{u,v}(\beta_v-\alpha_u)<2L
\tag{1.9}
\]

for all sufficiently large `D`.

Equations (1.8)--(1.9) are exactly the strict angular hypotheses of the §76 common
projection construction.

---

## 1.2 Prune to near-full minimum degree

Let `M_D=o(D^2)` be the missing-pair count after phase separation. Choose any
`eta_D->0` such that

\[
M_D=o(\eta_DD^2).
\tag{1.10}
\]

For example one may take

\[
\eta_D=\sqrt{M_D/D^2+D^{-1}}.
\]

Delete every `A` train missing more than `eta_DD` members of `B`, and symmetrically
delete every `B` train missing more than `eta_DD` members of `A`. Markov's inequality
and (1.10) delete only `o(D)` trains on each shore.

Relabel the survivors `A,B`, with sizes

\[
|A|=aD+o(D),
\qquad
|B|=bD+o(D).
\tag{1.11}
\]

There is one number `r_D=o(D)` such that

\[
\boxed{
\deg_A(u)\ge |B|-r_D
\quad(u\in A),
\qquad
\deg_B(v)\ge |A|-r_D
\quad(v\in B).
}
\tag{1.12}

In particular for all large `D`, every two vertices on one shore have a common neighbor
and every three vertices on one shore have a common neighbor on the opposite shore.

---

## 1.3 Global crossing orders from only `K_{2,2}` consistency

By §76, equations (1.8)--(1.9) give one common scalar coordinate

\[
X(p)=e_D\cdot p
\tag{1.13}
\]

strictly increasing along every selected oriented train centerline, after orienting the
`A` trains canonically and the `B` trains oppositely. Every actual `A`--`B` crossing has
the same signed graph crossing orientation.

We now construct global orders without assuming a complete product.

Take two distinct trains `u_1,u_2 in A`. By (1.12) they have a common neighbor
`v in B`. Order `u_1,u_2` by the order of their crossings along the oriented train `v`.
This does not depend on the chosen common neighbor. Indeed, if `v'` is another common
neighbor, the four trains

\[
\{u_1,u_2\}\times\{v,v'\}
\]

form a complete signed `2 x 2` subgrid. The §76 signed monotone-grid order lemma applied
just to those four curves says `v` and `v'` see `u_1,u_2` in the same order.

This gives a pairwise total relation on `A`. It is transitive: for any three `A`
trains, (1.12) supplies one common `B` neighbor. Along that one oriented curve their
crossing order is an ordinary linear order. Thus we obtain a strict total order

\[
<_A
\]

on `A`.

The same argument gives a strict total order

\[
<_B
\]

on `B`.

Moreover, for any fixed `u in A`, its actual `B` neighbors occur along `u` in the
restriction of `<_B`, because `u` itself is a common `A` neighbor used in the
definition of every pairwise comparison. The symmetric statement holds along every
`v in B`.

This is the robust replacement for complete-grid order: high minimum degree plus local
`2 x 2` consistency already globalizes the crossing orders.

---

## 1.4 An opposite-corner crossing survives all missing pairs

Let `u_*` be the first train in the global order `<_A`. It has at least one neighbor.
Let `v_*` be the **last** member of `N(u_*)` in the global order `<_B`.

Then:

- `v_*` is the last selected `B` crossing encountered along oriented `u_*`; and
- `u_*` is the first selected `A` crossing encountered along oriented `v_*`, because
  `u_*` is globally first in `<_A`.

Thus `u_* cap v_*` is an exact opposite corner of the incomplete grid.

Write the `B` neighbors of `u_*` in their crossing order as

\[
v_1,\ldots,v_d=v_*,
\]

and the `A` neighbors of `v_*` as

\[
u_*=u_1,\ldots,u_s.
\]

Let `c_{ij}` denote the center of the strict-rhombus crossing of the corresponding
trains.

Follow the oriented centerline of `u_*` from `c_{1,1}` to `c_{1,d}`, then the oriented
centerline of `v_*` from `c_{1,d}` to `c_{s,d}`. Every elementary displacement on both
legs has positive `e_D` projection by the §76 cone argument.

Exactly as in §76.5, the selected crossings on the first leg contribute at least

\[
e_D\cdot\sum_{v\in N(u_*)}v-1,
\tag{1.14}
\]

where `v` now also denotes the consistently oriented unit contact-edge vector of that
train. The second leg contributes at least

\[
e_D\cdot\sum_{u\in N(v_*)}u-1.
\tag{1.15}
\]

Both path endpoints are centers of source rhombi, hence lie in the full source convex
hull, whose diameter is `D`. Projecting their endpoint displacement therefore gives

\[
\boxed{
D\ge
\sum_{v\in N(u_*)}e_D\cdot v
+
\sum_{u\in N(v_*)}e_D\cdot u
-2.
}
\tag{1.16}
\]

The two direction clusters shrink to axes separated by `L`. The §76 projection
`e_D` therefore tends to their angular bisector, so uniformly

\[
\min_{u\in A}e_D\cdot u,
\quad
\min_{v\in B}e_D\cdot v
\ge {\sqrt3\over2}-o(1).
\tag{1.17}
\]

Use the minimum-degree bounds (1.12) in (1.16):

\[
D
\ge
\left({\sqrt3\over2}-o(1)\right)
\bigl(|A|+|B|-2r_D\bigr)-2.
\]

Divide by `D` and use (1.11), proving

\[
1\ge{\sqrt3\over2}(a+b).
\]

This proves Theorem 1.1. `square`

---

# 2. Equality structure at the §154 zero-detour floor

Assume for contradiction that a Type-II survivor sequence satisfies both

\[
{b-\operatorname{per}(F)\over D}\to0
\tag{2.1}
\]

and

\[
{q-k\over D}\to t_0.
\tag{2.2}
\]

Canonical Type II gives `per(F)/D->pi`, hence `b/D->pi`. The exact outer ledger

\[
b+Q=2(q-k)
\]

then gives

\[
\boxed{
{Q\over D}\to {4\over5}s_2.
}
\tag{2.3}
\]

Audited §154 gives

\[
\liminf {Q+4f\over D}\ge4s_2.
\tag{2.4}
\]

Since every bounded nonquadrilateral face has degree at least five,

\[
f\le Q
\]

and therefore

\[
Q+4f\le5Q.
\]

Equations (2.3)--(2.4) squeeze

\[
\boxed{
{Q+4f\over D}\to4s_2,
\qquad
{f\over D}\to{4\over5}s_2,
\qquad
Q-f=o(D).
}
\tag{2.5}

Thus almost every bounded defect face is a pentagon. The proof below uses only the
first equality in (2.5), not any local pentagon obstruction.

Pass to a subsequence on which

\[
{T\over D}\to x
\]

and the empirical projective train-direction probability measures converge to `mu`.
Let `sigma` be the total atomic mass of `mu`.

Audited §142 gives

\[
x\sigma\ge2s_2.
\tag{2.6}
\]

The §154 endpoint-capacity proof gives

\[
\liminf {Q+4f\over D}\ge2x\sigma.
\tag{2.7}
\]

Together with (2.5),

\[
2x\sigma\le4s_2.
\]

Hence (2.6) is saturated:

\[
\boxed{x\sigma=2s_2.}
\tag{2.8}

In absolute `D` normalization, the total atomic train mass is therefore exactly
`2s_2`.

---

## 2.1 All atomic crossing mass lies in one `pi/3` orbit

Let the atoms of `mu`, in absolute `D` normalization, have masses `a_i`. Thus

\[
\sum_i a_i=2s_2.
\tag{2.9}
\]

The exact relation

\[
\phi\sim\phi+{\pi\over3}\pmod\pi
\]

partitions the projective phase circle into three-point orbits. Let `A_j` be the total
atomic mass in orbit `j`.

Audited §142 says every normalized strict-rhombus crossing-measure limit is supported on
this exact relation and is bounded by the product train-phase measure. The physical
train-crossing graph is triangle-free. Therefore the crossing mass `E_j` contributed
by one phase orbit satisfies weighted Mantel:

\[
E_j\le{A_j^2\over4}.
\tag{2.10}
\]

All Type-II strict-rhombus crossing mass is accounted for in these atomic relation
pairs, so

\[
\sum_jE_j=\Delta_2=s_2^2.
\tag{2.11}
\]

But

\[
\sum_jE_j
\le{1\over4}\sum_jA_j^2
\le{1\over4}\left(\sum_jA_j\right)^2
=s_2^2.
\tag{2.12}
\]

Every inequality in (2.12) is therefore an equality. In particular

\[
\sum_jA_j^2=\left(\sum_jA_j\right)^2,
\]

so exactly one `pi/3` orbit carries positive atomic mass. Call its three possible atom
directions

\[
\phi_0,
\qquad
\phi_0+{\pi\over3},
\qquad
\phi_0+{2\pi\over3}
\quad(\bmod\pi).
\tag{2.13}
\]

Its total absolute mass is `2s_2`, and its physical crossing graph is asymptotically
Mantel-extremal.

Using the standard order of limits from §154, choose shrinking disjoint neighborhoods
of these three atoms so that the selected train set `W_D` satisfies

\[
|W_D|=2s_2D+o(D)
\tag{2.14}
\]

and its induced crossing graph has

\[
e(W_D)=s_2^2D^2-o(D^2)
={|W_D|^2\over4}-o(D^2).
\tag{2.15}

---

## 2.2 Near-Mantel stability leaves a large near-complete atom pair

Apply the elementary near-Mantel stability lemma already proved in §153 to the
triangle-free graph on `W_D`. There is a partition

\[
W_D=X_D\sqcup Y_D
\]

with

\[
|X_D|=s_2D+o(D),
\qquad
|Y_D|=s_2D+o(D),
\tag{2.16}
\]

such that `X_D` is independent, `Y_D` has only `o(D^2)` internal crossing edges, and
only `o(D^2)` pairs in `X_D x Y_D` are missing.

For sufficiently small atom neighborhoods, two trains belonging to the same atom
cannot cross at all: their projective separation is less than `pi/3`. If one atom
contributed positive linear mass to both `X_D` and `Y_D`, all corresponding cross-side
same-atom pairs would be missing, contradicting the `o(D^2)` cross-missing count.
Thus, up to `o(D)` trains, every positive atom belongs to one side of the Mantel
partition.

Both sides have limiting mass `s_2`. With at most three atom groups, one side therefore
consists, up to `o(D)`, of a **single** atom group of mass

\[
\boxed{s_2D+o(D).}
\tag{2.17}
\]

The other side consists of one or two atom groups with total mass `s_2D+o(D)`. Choose
the larger group there. Its size is at least

\[
\boxed{{s_2\over2}D+o(D).}
\tag{2.18}
\]

Call these two atom families `A_D,B_D`. Since they lie on opposite Mantel shores, only
`o(D^2)` pairs in `A_D x B_D` fail to cross. Their limiting atom directions differ by
exactly `pi/3`, because distinct atoms in the unique orbit do.

Therefore Theorem 1.1 applies with

\[
a=s_2,
\qquad
b\ge{s_2\over2}.
\]

It gives

\[
1
\ge{\sqrt3\over2}(a+b)
\ge{3\sqrt3\over4}s_2.
\tag{2.19}
\]

But

\[
{3\sqrt3\over4}s_2
=1.237090624640176\ldots>1.
\tag{2.20}
\]

Contradiction.

---

# 3. Main endpoint theorem

### Theorem 3.1 — the §154 zero-detour floor is unattainable

There is no unbounded audited-working Type-II C-II survivor sequence satisfying

\[
{b-\operatorname{per}(F)\over D}\to0
\]

and

\[
\boxed{
{q-k\over D}
\to
{\pi\over2}+{2\over5}\sqrt{\frac\pi{2\sqrt3}}.
}
\tag{3.1}
\]

Equivalently, the lower endpoint in audited §154.17 is not attained.

As with §§153--154, this implies a qualitative sequence/diagonal separation above the
formal endpoint within the zero-detour Type-II class. No explicit numerical gap is
asserted here.

This is structurally stronger than the earlier §154 endpoint theorem: §154 excluded
saturation of the weaker `C_146=1.8195...` floor by bootstrapping to the zero-detour
bound `1.9517...`; Theorem 3.1 now excludes saturation of that **stronger zero-detour
bound itself**.

---

# 4. Hostile checks

1. **No complete-product assumption hidden in Theorem 1.1.** Completeness is used only
   on actual `2 x 2` subgrids to make pairwise crossing orders independent of the
   chosen common neighbor. High minimum degree supplies common neighbors for every pair
   and triple.
2. **Holes and bounded train endpoints remain.** The order construction uses only
   actual train centerlines, common `X` monotonicity, and local `2 x 2` signed order.
   No outer-boundary crosscut theorem is invoked.
3. **Phase separation is earned.** Noncrossing inversions are charged to the
   `o(D^2)` missing-pair budget, then removed by Lemma 1.2. The §76 projection is not
   applied before the strict `max alpha + pi/3 < min beta` inequality is established.
4. **Same-shore disjointness.** Shrinking one-atom neighborhoods have width below
   `pi/3`, so two same-atom trains cannot form a strict rhombus crossing.
5. **Endpoint path is source-level.** The two endpoints used in (1.16) are rhombus
   centers inside the full source convex hull. Their distance is at most the full source
   diameter `D`; no contact-isolated point is removed or inserted into the core kernel.
6. **Atomic orbit equality.** The chain (2.12) uses only nonnegative orbit masses.
   Equality of the total forces one positive orbit; no assumption that there were
   finitely many atoms globally is needed.
7. **Three-atom Mantel regression retained.** Equality may place one atom on one Mantel
   shore and two atoms on the other. The proof deliberately keeps this possibility and
   uses only the larger of the two opposite-shore atoms. It does not assert a false
   two-atom collapse.
8. **Pentagon regression retained.** No local pentagon direction or Oler gap is used.
   Triangle-free pentagons can approach all three atomic axes and zero Oler slack.
9. **Theorem authority.** This file is proof-only. Audit.46 remains the canonical
   theorem-state cutoff.

**Disposition:** new proof-only endpoint exclusion plus a reusable robust
near-complete-grid diameter theorem. C-II remains open away from the zero-detour
endpoint.
