> Generated reading edition · [exact source](../../research/target_c_support6_reciprocal_h5_reduction_2026-09-18.md) · source SHA-256 `763e41ec1dd65ba938880d1f98ac2eebf42de52ed23663a54a80c3e50b17ac06`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "aa9e324214a1ae7ff52dcfe82569c7210a05d809", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support6_reciprocal_h5_reduction_2026-09-18.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "6f3bde1e4f5781d47411d7e083aa6dc9bfa24f17f604fce3277c3f8e4462d8be"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — exact finite reduction of the support-six reciprocal `H5` branch

**Date:** 2026-09-18  
**Status:** proof-only structural reduction; theorem-state authority unchanged  
**Scope:** the noncollapsed degree-pure support-six one-anchor endpoint after the `H7` and `H6` exclusions  
**Depends on:** `target_c_support6_reciprocal_h7_exclusion_2026-09-18.md`; `target_c_support6_reciprocal_h6_exclusion_2026-09-18.md`; the ground `3+3` semicircle sign-order lemma; local hull `2+3` sign alternation; closed-equilateral-pentagon two-turn inequality; bounded-pentagon no-parallel-side theorem  
**Certificate:** `research/verify_target_c_support6_reciprocal_h5_reduction_2026_09_18.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The preceding support-six work leaves two mechanisms:

1. the collapsed branch `y_1=\cdots=y_6\ne0`; and
2. the noncollapsed reciprocal `H5` branch.

This note makes the second branch finite at the sign/order level.

For the uniform `H5` stratum, an exact rank-three chirotope enumeration begins with all configurations of a convex reciprocal pentagon containing the ground point `0` and two interior non-ground points. After imposing the already proved ground and hull sign rules, and then imposing a new exact local consequence of the pentagon two-turn inequality at the two interior reciprocal vertices, only

```math
\boxed{48}
```

labelled signed order types survive. They are only

```math
\boxed{6}
```

orbits under hull reflection fixing the ground, interchange of the two interior labels, and global sign reversal.

The same check on every simple allowed ground-collinearity wall starts from `316` exact rank-three walls. After the same local tests, `80` labelled signed wall types survive, forming exactly

```math
\boxed{10}
```

symmetry orbits. The wall in which the two interior reciprocal points are collinear with the ground is eliminated completely.

Thus the generic and simple-wall `H5` problem is reduced to sixteen exact finite sign/order orbits. This does not prove those sixteen orbits are metrically realizable as reciprocal unit-force equilibria. It also does not remove higher-codimension multiple ground-collinearity strata. Those are now the remaining `H5` tasks.

---

## 1. `H5` setup

Use the reciprocal notation of the preceding support-six notes. The noncollapsed support-six relation graph is

```math
R=K_6\setminus M,
```

where `M` is a perfect matching on the six non-ground reciprocal vertices. Adding the ground reciprocal point `y_0=0` gives

```math
H=K_7\setminus M.
```

The `H7` and `H6` exclusions leave the case in which the reciprocal convex hull has exactly five vertices. Label that hull cyclically

```math
0,1,2,3,4,
```

with `0` the ground point, and label the two interior non-ground reciprocal points `5,6`.

The previous hull-angle theorem gives

```math
\phi_i>{2\pi\over3}\quad (i=1,2,3,4),
\qquad
\phi_0<{\pi\over3}.
```

Hence all six raw ground rays lie in an open cone of width less than `pi/3`, and the previous projection argument forces the ground unit-force equilibrium to have sign split exactly `3+3`.

At each non-ground hull vertex `i=1,...,4`, deleting the unique missing matching edge leaves five incident reciprocal rays in the open hull cone. The previously proved local alternation theorem says the size-two sign class occupies raw positions two and four; the size-three class occupies positions one, three, and five.

The two interior reciprocal vertices do not lie in a hull cone, so that alternation statement cannot be imported there. We use the physical pentagon directly.

---

## 2. The strict two-turn inequality gives a regular cross tournament

Let

```math
v_1,\ldots,v_5
```

be the five oriented unit side vectors of any strict closed equilateral pentagon, written in cyclic angular order, and let `delta_i` be the five positive consecutive direction gaps. The proved two-turn inequality is

```math
\delta_i+\delta_{i+1}<\pi
\qquad\text{for every }i\pmod5.
\tag{2.1}
```

Therefore

```math
\det(v_i,v_{i+1})>0,
\qquad
\det(v_i,v_{i+2})>0,
\tag{2.2}
```

while the complementary two directions lie more than `pi` counterclockwise from `v_i` and have negative determinant with `v_i`.

Orient the tournament on the five force directions by

```math
a\longrightarrow b
\quad\Longleftrightarrow\quad
\det(v_a,v_b)>0.
```

Every vertex then has outdegree exactly two. Hence

```math
\boxed{\text{the force-direction cross tournament of every physical pentagon is the regular 5-tournament.}}
\tag{2.3}
```

This is only a necessary condition, which is sufficient for the finite reduction.

At reciprocal vertex `i`, the force on edge `ij` is the raw reciprocal direction, possibly reversed according to the sign of `lambda_ij`. Thus for two incident edges `ij,ik`, the force cross-product sign is exactly

```math
\operatorname{sgn}(\lambda_{ij})
\operatorname{sgn}(\lambda_{ik})
\chi(i,j,k),
\tag{2.4}
```

where `chi` is the rank-three orientation sign of the reciprocal point configuration. Consequently (2.3) is an exact sign condition on the chirotope and reciprocal edge signs. No metric coordinates are needed. This is particularly useful at the two interior reciprocal vertices.

---

## 3. Uniform `H5`: exact rank-three extensions

Fix the convex hull `0,1,2,3,4` in counterclockwise order. Requiring each point `p in {5,6}` to lie inside the pentagon fixes its orientation sign against every directed hull edge.

Among the `35` triple signs, after the hull and interior boundary signs are fixed, exactly fifteen independent sorted triple-sign slots remain free in the verifier. It checks all `2^15` assignments against the uniform rank-three Grassmann-Pluecker chirotope axiom. Exactly

```math
\boxed{370}
\tag{3.1}
```

uniform chirotope extensions survive.

No realizability assumption is needed. If some surviving abstract chirotope is nonrealizable, the enumeration merely over-approximates the geometric candidate set, which is safe here.

---

## 4. Ground and hull sign compatibility leaves 600 labelled candidates

For any uniform `H5` chirotope, the six raw ground rays are distinct and lie in an open semicircle. The ground `3+3` lemma from the `H6` exclusion therefore applies. In increasing raw-ray order the sign word is

```math
\boxed{+--++-}
\tag{4.1}
```

or its global complement.

For each of the fifteen perfect matchings `M` on `{1,...,6}`, the verifier assigns the two ground sign words, deletes each hull vertex's matching mate, assigns either sign color to raw positions two and four at hull vertices `1,...,4`, and checks undirected edge-sign consistency. Exactly

```math
\boxed{600}
\tag{4.2}
```

labelled partial sign/order candidates survive. If the reciprocal edge `56` is present and not fixed by a hull endpoint, both signs are checked.

---

## 5. The interior pentagon test cuts 600 candidates to 48

For every complete edge signing from Section 4, apply the regular-tournament condition (2.3) at all six non-ground reciprocal vertices. The exact count is

```math
\boxed{48\text{ labelled uniform survivors}.}
\tag{5.1}
```

Every survivor has one of exactly four labelled missing matchings:

```math
\begin{aligned}
M_1&=\{12,35,46\},\\
M_2&=\{12,36,45\},\\
M_3&=\{15,26,34\},\\
M_4&=\{16,25,34\}.
\end{aligned}
\tag{5.2}
```

Each family contributes twelve survivors.

Quotient by the symmetries preserving the labelled `H5` setup: reflection of the reciprocal hull fixing ground vertex `0`, interchange of interior labels `5,6`, and global reciprocal sign reversal. The forty-eight survivors form exactly

```math
\boxed{6\text{ symmetry orbits},}
\tag{5.3}
```

each of orbit size eight. The four matchings in (5.2) lie in one symmetry orbit; the residual distinction lies in the two-interior order type and compatible edge signing.

---

## 6. Which simple collinearities can occur?

The preceding support-six theorem proves that no three non-ground reciprocal points are collinear.

Suppose instead that `y_0,y_i,y_j` are collinear. If `ij` were a present relation edge, then at physical pentagon `F_i` the outside anchor `i0` and relation train `ij` would be projectively parallel. The bounded-pentagon no-parallel-side theorem forbids this. Hence

```math
\boxed{ij\in M.}
\tag{6.1}
```

Because `5,6` are interior points, neither can lie on the boundary rays `01` or `04`. Therefore the only simple ground-collinearity triples compatible with the `H5` labeling are

```math
\boxed{025,\ 026,\ 035,\ 036,\ 056.}
\tag{6.2}
```

A configuration with exactly one such collinearity lies on a codimension-one wall between two uniform chirotopes differing only in that triple sign. The exact enumeration finds

```math
\begin{array}{c|ccccc}
\text{wall}&025&026&035&036&056\\
\hline
\text{count}&66&66&66&66&52
\end{array}
```

for a total of

```math
\boxed{316}.
\tag{6.3}
```

---

## 7. Duplicate ground rays must carry the same sign

On a simple wall `0,i,j`, the two ground unit rays `i,j` coincide and `ij` is the missing matching edge.

They cannot have opposite reciprocal signs. If they did, those terms would cancel from the ground `3+3` equilibrium, leaving

```math
u_a+u_b=u_c+u_d
\tag{7.1}
```

between two disjoint pairs of the remaining four distinct unit rays. All four lie in the same open ground cone, hence in one open semicircle.

For two unit vectors in an open semicircle, their sum determines the unordered pair: its direction is the angular bisector and its norm is `2 cos(alpha/2)`, with `0<alpha<pi`. Thus (7.1) forces the two unordered pairs to coincide, contrary to the four rays being distinct on a simple wall.

Therefore the duplicated ground rays have the same sign. After global sign reversal take both positive. The ground split is still `3+3`, so exactly one of the other four rays is positive.

---

## 8. Exact simple-wall reduction

For each of the 316 walls, the verifier forces the tied pair to be a missing matching edge, enumerates the ground signs from Section 7, deletes the matching mate before applying the hull positions-two-and-four rule, enforces undirected edge-sign consistency, and imposes the regular force tournament at every non-ground vertex.

The hull-sign stage leaves `488` labelled candidates. The regular-tournament test leaves exactly

```math
\boxed{80}
\tag{8.1}
```

labelled simple-wall survivors. They split as `20` for each of `025,026,035,036`, and

```math
\boxed{0}
\tag{8.2}
```

for the `056` wall. Thus

```math
\boxed{\text{the two interior reciprocal points cannot form the unique simple ground-collinear pair.}}
\tag{8.3}
```

Quotienting the eighty remaining labelled wall survivors by hull reflection, interior interchange, and global sign reversal leaves exactly

```math
\boxed{10\text{ simple-wall symmetry orbits}.}
\tag{8.4}
```

---

## 9. Scope and next target

The exact support-six `H5` state is now

```math
\boxed{
\begin{array}{ll}
\text{uniform reciprocal stratum:}&6\text{ sign/order orbits};\\[1mm]
\text{simple allowed ground-collinearity strata:}&10\text{ sign/order orbits};\\[1mm]
\text{simple }056\text{ wall:}&\text{empty}.
\end{array}}
\tag{9.1}
```

These sixteen orbits are necessary combinatorial types only. The verifier does not claim that any admits reciprocal coordinates satisfying the full signed unit-force equilibria

```math
\sum_{j:ij\in E(H)}
\operatorname{sgn}(\lambda_{ij})
{y_i-y_j\over |y_i-y_j|}=0.
\tag{9.2}
```

It also does not cover higher-codimension configurations with two or more simultaneous allowed ground collinearities. Such strata need their own duplicate-ray analysis.

The next `H5` target is finite and explicit: exclude the six uniform orbits by the full metric equilibrium and signed trace identity or exhibit a genuine realization; do the same for the ten simple-wall orbits; and enumerate the higher-codimension ground-ray degeneracies. The collapsed support-six branch remains separate.

No theorem-state file is changed.

**Disposition:** proved the regular-force-tournament reduction, exhaustively reduced the uniform `H5` reciprocal branch to six symmetry orbits, reduced all simple allowed ground-collinearity walls to ten symmetry orbits, and eliminated the simple `056` wall. C-II remains open.
