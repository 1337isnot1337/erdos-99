> Generated reading edition · [exact source](../../research/target_c_support7_endpoint_reduction_2026-09-19.md) · source SHA-256 `9e8fb04bca58e7b55644c6d5d614669cf577c4b2255140a2f122d3b04e606004`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "cedee75de46913142bc1dbe3d1a724cf6f9063a6", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_endpoint_reduction_2026-09-19.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "6da6709d5d9d5ac2be7f1c9b68c217b9c76c3af0cd773630209c17d14052df1c"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — degree-pure support seven is noncollapsed and has a finite reciprocal endpoint

**Date:** 2026-09-19  
**Status:** proof-only structural strengthening; theorem-state authority unchanged  
**Scope:** degree-pure support-seven one-anchor relation components after maximal two-anchor activation  
**Depends on:** audited one-anchor relation-component theorem; bounded pentagon no-parallel-side theorem; completed support-five/support-six exclusions; reciprocal unit-force construction; local `2+3` reciprocal hull alternation theorem; reciprocal hull-angle bound `>2pi/3`; reciprocal signed trace identity  
**Certificate:** `research/verify_target_c_support7_endpoint_reduction_2026_09_19.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The support-six endpoint is now completely excluded. The next degree-pure one-anchor endpoint has seven strict unit pentagons. This note reduces that endpoint sharply.

The main conclusions are:

```math
\boxed{
R\text{ is four-regular on seven vertices, so }\overline R=C_7\text{ or }C_3\sqcup C_4.
}
\tag{S7.1}
```

```math
\boxed{y_1,\ldots,y_7\text{ are pairwise distinct}.}
\tag{S7.2}
```

Thus, unlike support six, support seven has no collapsed or partially collapsed reciprocal branch. Adding the ground value `y_0=0` gives a nondegenerate reciprocal graph

```math
\boxed{H=K_8\setminus \overline R,\qquad \overline R\in\{C_7,C_3\sqcup C_4\},}
\tag{S7.3}
```

with signed unit-magnitude equilibrium at all eight reciprocal vertices.

The local pentagon theorem still forces every non-ground reciprocal hull angle to exceed `2pi/3`. Consequently the reciprocal hull has size `5,6,7`, or `8`; a five-vertex hull is impossible, and a six-vertex hull forces an exact `3+4` ground sign split.

For the fully convex `H8` branch, exact local sign compatibility leaves only `23` reflection orbits. Two `C7` orbits with a `2+5` ground split are excluded by exact signed-length certificates, and one further `C7` `3+4` orbit is excluded directly from the ground equilibrium by a monotone-cosine projection. Therefore

```math
\boxed{
\text{fully convex support-seven candidates reduce to }20\text{ exact reflection orbits, all with ground }3+4.
}
\tag{S7.4}
```

This does not exclude degree-pure support seven. The surviving `H6/H7` branches and the `20` fully convex `H8` order/sign orbits remain.

---

## 1. Relation graph at the degree-pure support-seven endpoint

Let `K` be a nonzero one-anchor relation component with exactly seven residual faces, all of degree five. Every face has one outside/activated anchor and therefore exactly four residual internal side occurrences.

The audited one-anchor theorem gives relation degree at least four at every face of a nonzero component. Since there are only four residual internal occurrences, every one is a relation edge and

```math
\deg_R(F)=4
```

for every face. The endpoint transport graph is simple, so `R` is a simple four-regular graph on seven vertices.

Its complement in `K_7` is therefore simple two-regular. Every component of a simple two-regular graph is a cycle of length at least three. The only partitions of seven into integers at least three are

```math
7,
\qquad
3+4.
```

Hence

```math
\boxed{
\overline R=C_7\quad\text{or}\quad C_3\sqcup C_4.
}
\tag{1.1}
```

There are fourteen relation edges.

---

## 2. Any repeated dual value would force total collapse

Write

```math
y_i=c_i a_i\ne0,
\qquad i=1,\ldots,7,
```

for a nonzero fiber mode on the seven one-anchor faces.

Partition the seven vertices into classes of equal dual value. Consider two distinct classes `A,B`. If one vertex `i in A` had two relation neighbors `j,k in B`, then

```math
y_i-y_j=y_i-y_k\ne0.
```

The transpose equations on relation edges `ij` and `ik` would make the two corresponding physical train directions at face `i` projectively parallel. Both are sides of the same strict unit pentagon, contradicting the bounded-pentagon no-parallel-side theorem.

Therefore:

```math
\boxed{
\text{between two distinct dual-value classes, the relation edges form a matching.}
}
\tag{2.1}
```

Now suppose `S` is a proper equal-value class with `s=|S|>=2`. Every vertex outside `S` has at most one relation neighbor in `S`, so it has at least `s-1` nonrelation neighbors in `S`. But the nonrelation graph `\overline R` has degree exactly two.

If `s>=4`, one outside vertex would need at least three nonrelation neighbors in `S`, impossible.

If `s=3`, each of the four outside vertices needs at least two nonrelation edges into `S`, for at least eight cross edges of `\overline R`. The three vertices of `S` have total complement degree only six. Impossible.

If `s=2`, each of the five outside vertices needs at least one nonrelation edge into `S`, for at least five cross edges. The two vertices of `S` have total complement degree only four. Impossible.

Thus there is no proper collision class:

```math
\boxed{
\text{either all seven }y_i\text{ are distinct, or all seven are equal.}
}
\tag{2.2}
```

The exact verifier independently enumerates all `877` set partitions for representatives of both complement types. Under the matching condition (2.1), only the discrete partition and total collapse survive.

---

## 3. Odd support excludes total collapse

Assume for contradiction

```math
y_1=\cdots=y_7=v\ne0.
```

Every outside anchor direction is then projectively parallel to `v`. Sum the seven physical pentagon closure equations. Every internal relation side occurs twice with opposite oriented unit vectors and cancels. What remains is the sum of the seven oriented unit anchor sides.

Since all seven anchors are projectively parallel, after fixing one unit vector `u` the remaining equation has the form

```math
\epsilon_1u+\cdots+\epsilon_7u=0,
\qquad
\epsilon_i\in\{+1,-1\}.
```

This would require

```math
\epsilon_1+\cdots+\epsilon_7=0,
```

impossible for seven signs.

Therefore total collapse is impossible. Combining with (2.2),

```math
\boxed{y_1,\ldots,y_7\text{ are pairwise distinct}.}
\tag{3.1}
```

This is the main structural difference between support six and support seven.

---

## 4. The support-seven reciprocal graph is fully nondegenerate

Put

```math
y_0=0.
```

The seven non-ground values are nonzero and pairwise distinct. For every relation edge `ij`, the reciprocal difference `y_i-y_j` is nonzero and projectively parallel to the corresponding physical train direction. Every anchor edge `0i` is also nonzero.

Adding the seven ground edges to the fourteen relation edges gives

```math
H=K_8\setminus \overline R,
\qquad
\overline R\in\{C_7,C_3\sqcup C_4\},
\tag{4.1}
```

where all missing edges lie among the seven non-ground vertices.

Exactly as in the audited support-six reciprocal construction, every present edge `ij` has a signed scalar `lambda_ij` satisfying

```math
y_i-y_j=\lambda_{ij}w_{ij}^{(i)},
\qquad
|\lambda_{ij}|=|y_i-y_j|.
```

The five physical unit sides of each non-ground pentagon close, so

```math
\sum_{j:ij\in E(H)}{y_i-y_j\over\lambda_{ij}}=0,
\qquad i=1,\ldots,7.
\tag{4.2}
```

Summing over the seven non-ground vertices cancels every internal edge and gives the ground equilibrium

```math
\sum_{j=1}^7{y_0-y_j\over\lambda_{0j}}=0.
\tag{4.3}
```

Thus `H` carries a signed unit-magnitude central-force equilibrium. If

```math
s_{ij}=\operatorname{sgn}\lambda_{ij},
\qquad
d_{ij}=|y_i-y_j|,
```

then the standard tensor cancellation and trace give

```math
\boxed{
\sum_{ij\in E(H)}s_{ij}d_{ij}=0.
}
\tag{4.4}
```

No collapsed edge has to be removed or treated separately.

---

## 5. Hull reduction: `H5` is impossible and `H6` forces ground `3+4`

At every non-ground reciprocal hull vertex there are exactly five incident reciprocal rays, one for the anchor and four for relation edges. The audited local pentagon argument is graph-independent at this point: the raw rays lie in the open hull cone, the `1+4` split is excluded by the two-turn inequality, and the surviving `2+3` split has its size-two sign class in raw positions two and four. The same source-gap argument gives

```math
\boxed{\phi_i>{2\pi\over3}}
\tag{5.1}
```

for every non-ground reciprocal hull vertex.

Let the reciprocal hull have `h` vertices.

If the ground point is interior, all `h` hull vertices are non-ground. The polygon angle sum and (5.1) give

```math
(h-2)\pi>h{2\pi\over3},
```

so `h>6`. Since only seven non-ground points exist, the only interior-ground possibility is

```math
h=7.
\tag{5.2}
```

If the ground point is on the hull, the same count on the other `h-1` hull vertices excludes `h<=4`. Hence

```math
\boxed{h\in\{5,6,7,8\}.}
\tag{5.3}
```

For ground-on-hull cases,

```math
\phi_0<(h-2)\pi-(h-1){2\pi\over3}
={h-4\over3}\pi.
\tag{5.4}
```

In particular,

```math
H5:\quad\phi_0<\frac\pi3,
\qquad
H6:\quad\phi_0<\frac{2\pi}3.
\tag{5.5}
```

Now use the seven signed unit vectors at the ground. Their raw directions lie in the ground hull cone of width `phi_0`. Let `p<=3` be the smaller sign class. After moving it to the other side of the equilibrium, the resultant of the `7-p` majority vectors must equal the resultant of the `p` minority vectors.

Projection of the majority onto the cone bisector is at least

```math
(7-p)\cos(\phi_0/2),
```

while the minority resultant has norm at most `p`. Therefore a necessary condition is

```math
(7-p)\cos(\phi_0/2)\le p.
\tag{5.6}
```

For `H5`, `phi_0<pi/3`, and even the weakest case `p=3` gives

```math
(7-p)\cos(\phi_0/2)
>4\cos(\pi/6)=2\sqrt3>3=p.
```

Hence

```math
\boxed{H5\text{ is impossible}.}
\tag{5.7}
```

For `H6`, `phi_0<2pi/3`. If `p<=2`,

```math
(7-p)\cos(\phi_0/2)
\ge5\cos(\phi_0/2)
>5\cos(\pi/3)=\frac52>2\ge p.
```

Thus

```math
\boxed{H6\Longrightarrow\text{ground sign split }3+4.}
\tag{5.8}
```

The `H7` and `H8` branches remain.

---

## 6. Fully convex `H8`: exact local sign census

Assume all eight reciprocal points are hull vertices and label them in cyclic order

```math
0,1,2,3,4,5,6,7,
```

with `0` the ground point.

The missing non-ground graph is either `C7` or `C3+C4`. On the seven labelled non-ground hull positions there are

```math
{(7-1)!\over2}=360
```

undirected `C7` embeddings, and

```math
\binom73\cdot3=105
```

`C3+C4` embeddings.

Fix one missing graph. At each non-ground hull vertex, delete the two missing non-neighbors from the seven raw hull rays. The five present rays retain a definite cyclic order. The local pentagon theorem says that for one chosen global sign color either

- positions `2,4` are positive; or
- positions `1,3,5` are positive.

Thus there are only `2^7` local choices. Requiring each undirected reciprocal edge to receive the same sign from both endpoints is exact finite combinatorics.

The verifier finds:

```math
\begin{array}{c|c|c}
\text{missing type}&\text{labelled embeddings surviving}&\text{signings per embedding}\\\hline
C_7&24&2\\
C_3\sqcup C_4&14&2
\end{array}
\tag{6.1}
```

The two signings are global complements. Quotienting by reflection of the hull fixing `0` leaves

```math
\boxed{15\ C_7\text{ orbits and }8\ (C_3\sqcup C_4)\text{ orbits}.}
\tag{6.2}
```

Their ground sign splits are

```math
\begin{array}{c|c}
\text{class}&\text{reflection orbits}\\\hline
C_7,\ 2+5&2\\
C_7,\ 3+4&13\\
C_3\sqcup C_4,\ 3+4&8.
\end{array}
\tag{6.3}
```

No `C3+C4` survivor has a `2+5` ground split.

---

## 7. Exact trace certificates exclude both `H8` ground `2+5` orbits

For a reciprocal sign assignment define

```math
L=\sum_{e\in P}d_e-\sum_{e\in E(H)\setminus P}d_e.
\tag{7.1}
```

The reciprocal trace identity requires `L=0`. Global sign reversal replaces `L` by `-L`, so it is enough to exclude one representative of each complementary pair.

Use the following strict residuals for points in convex position:

```math
T(ab;ac,bc)=d_{ab}-d_{ac}-d_{bc}<0,
\tag{7.2}
```

by strict triangle inequality, and, for cyclically ordered `a,b,c,d`,

```math
Q(ab,cd;ac,bd)=d_{ab}+d_{cd}-d_{ac}-d_{bd}<0.
\tag{7.3}
```

For (7.3), if `X` is the intersection of diagonals `ac,bd`, then

```math
d_{ab}<d_{aX}+d_{Xb},
\qquad d_{cd}<d_{cX}+d_{Xd},
```

and the right sides sum to `d_ac+d_bd`.

### Orbit A

Take

```math
M_A=\{12,17,23,34,45,56,67\},
```

and positive reciprocal edges

```math
P_A=\{03,05,14,16,25,27,36,47\}.
```

The exact verifier checks the coefficient identity

```math
6L_A=\sum_r c_rR_r,
\tag{7.4}
```

where every coefficient `c_r` below is a positive integer and every `R_r` is a strict negative residual of type `T` or `Q`:

```text
6 T(16;01,06)
1 T(03;02,23)
1 T(05;02,25)
3 T(27;02,07)
1 T(03;07,37)
2 T(05;07,57)
1 T(27;12,17)
3 T(14;13,34)
2 T(36;13,16)
1 T(17;15,57)
1 T(25;24,45)
1 T(56;25,26)
1 T(27;26,67)
1 T(36;34,46)
2 T(36;35,56)
1 T(56;45,46)
2 T(47;46,67)
1 Q(12,05;02,15)
2 Q(14,05;04,15)
4 Q(03,47;04,37)
1 Q(23,14;13,24)
2 Q(45,16;15,46)
4 Q(34,25;24,35)
1 Q(36,27;26,37)
3 Q(25,67;26,57)
```

Hence `L_A<0`, contradicting `L_A=0`.

### Orbit B

Take

```math
M_B=\{14,15,25,26,36,37,47\},
```

and

```math
P_B=\{02,06,13,17,24,35,46,57\}.
```

Here the certificate is shorter:

```math
\begin{aligned}
2L_B={}&T(02;01,12)+T(13;01,03)+T(35;03,05)+T(57;05,07)\\
&+T(06;07,67)+T(13;12,23)+T(24;23,34)+T(35;34,45)\\
&+T(46;45,56)+T(57;56,67)\\
&+Q(24,06;04,26)+Q(02,47;04,27)\\
&+Q(26,17;16,27)+Q(46,17;16,47).
\end{aligned}
\tag{7.5}
```

Every term is strictly negative, so `L_B<0`, again contradicting the reciprocal trace identity.

Therefore both `2+5` reflection orbits are impossible.

---

## 8. One further `H8` orbit dies at the ground equilibrium

Among the remaining local-sign survivors, exactly one `C7` reflection orbit has ground minority sign pattern

```math
\{1,3,7\}
```

or its reflected pattern

```math
\{1,5,7\}.
```

Let the seven raw ground directions have angles

```math
\theta_1<\theta_2<\cdots<\theta_7<\theta_1+\pi
```

and unit vectors `u_i=(cos theta_i,sin theta_i)`.

### Pattern `{1,3,7}`

A ground equilibrium would imply

```math
u_1+u_3+u_7=u_2+u_4+u_5+u_6,
```

or

```math
0=(u_2-u_1)+(u_4-u_3)+u_5+(u_6-u_7).
\tag{8.1}
```

Dot with `u_5`. Because cosine is strictly decreasing on `(0,pi)`,

```math
(u_2-u_1)\cdot u_5
=\cos(\theta_5-\theta_2)-\cos(\theta_5-\theta_1)>0,
```

```math
(u_4-u_3)\cdot u_5>0,
\qquad u_5\cdot u_5=1,
\qquad (u_6-u_7)\cdot u_5>0.
```

The right side of (8.1) therefore has positive dot product with `u_5`, contradiction.

### Pattern `{1,5,7}`

Now equilibrium would give

```math
0=(u_2-u_1)+u_3+(u_4-u_5)+(u_6-u_7).
\tag{8.2}
```

Dot with `u_3`. Again each term has strictly positive dot product with `u_3`:

```math
(u_2-u_1)\cdot u_3>0,
\qquad u_3\cdot u_3=1,
```

```math
(u_4-u_5)\cdot u_3>0,
\qquad (u_6-u_7)\cdot u_3>0.
```

Contradiction.

Reflection exchanges the two patterns. Hence one additional `C7` reflection orbit is impossible.

Combining Sections 6--8 leaves exactly

```math
\boxed{20}
```

fully convex `H8` reflection orbits, all with ground `3+4`.

---

## 9. What remains

The degree-pure support-seven endpoint is now in the following normal form.

1. The relation graph is `K7-C7` or `K7-(C3+C4)`.
2. All seven non-ground dual values are pairwise distinct, so the reciprocal is fully nondegenerate.
3. Every non-ground reciprocal hull vertex has the exact local `2+3` alternation rule and hull angle `>2pi/3`.
4. `H5` is impossible.
5. `H6` has ground sign split `3+4`.
6. `H7` remains, with the ground either on the hull or interior.
7. Fully convex `H8` is reduced to `20` exact reflection orbits, all ground `3+4`.

This does **not** improve the global one-anchor coefficient beyond the already proved `1/7`. Support seven has not been excluded. The next clean targets are:

- finish the `20` convex `H8` metric/sign orbits, preferably with exact triangle/quadrilateral or ground-resultant certificates;
- classify `H6/H7` order types using the same local alternation theorem; or
- bypass casework by deriving a signed-distance or stress invariant for the two relation graph types.

No theorem-state file is changed.

**Disposition:** support seven has no collapsed branch; its relation graph has only two complement types; `H5` is impossible; `H6` forces ground `3+4`; exact convex-H8 sign enumeration plus three exact exclusions reduces the fully convex branch to 20 reflection orbits. C-II remains open.
