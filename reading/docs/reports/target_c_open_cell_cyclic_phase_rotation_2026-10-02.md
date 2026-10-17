> Generated reading edition · [exact source](../../../docs/reports/target_c_open_cell_cyclic_phase_rotation_2026-10-02.md) · source SHA-256 `9814337d8a550b18259a2a8d2780b44fa42138f0254a7f60423a020512571979`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-5886E29A96D7","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II -- global cyclic phase rotation in one open witness cell

Date: 2026-10-02
Starting commit: 78a65968d51af7871a0ce5a865bf2db1a2c2e0ec
Branch: swarm/nonconstant/cyclic-phase-rotation-20261002
Status: proof-only new finite-move theorem; no canonical promotion claimed. C-II and Level I remain open.

> candidate lemma -> exact canonical quantity -> contradiction / strict competitor / Level I consequence
>
> cyclic permutation of all retained train phases
> -> one inverse-D contact-preserving global layer motion
> -> global TWO-SIGN active-diameter response or a nonlocal inverse-D inactive blocker
> -> remaining task is to eliminate the global TWO-SIGN alternative or convert the inactive blocker network to a strict competitor / triangle.

## 1. Mission

Current main proves an exact finite block transposition for any two distinct retained
train phases in one open global-diameter witness cell. That theorem moves one slab
and swaps the two boundary train directions.

The same contact algebra has a stronger global consequence which is not recorded on
main: the whole ordered phase word can be cyclically rotated by one position with a
single layerwise translation. The translations telescope, so every source point moves
only O(D^-1), independent of the number of retained layers.

This produces a global finite fork and upgrades the complete-grid local-immunity
statement: under the cyclic move the entire retained strict-rhombus grid is permuted
row-by-row, so no retained grid diagonal can be the inactive blocker.

## 2. Setup and dependencies

Work in the fixed-star complete global O--O rectangle on the nonconstant-phase side.
Fix one retained shore after the common open witness-cell extraction. Let

```math
\tau_1,\ldots,\tau_m
```

be its ordered pairwise-disjoint train crosscuts, with coherent oriented unit contact
directions

```math
u_1,\ldots,u_m
```

all lying in one open interval J between two consecutive global actual-diameter
directions.

The Section-90 window gives

```math
\operatorname{diam}_{\mathbb{RP}^1}\{[u_i]\}
\le {4K\over D}.
\tag{2.1}
```

Assume the phase word is nonconstant.

Let

```math
R_0,R_1,\ldots,R_m
```

be the physical layers cut out by the ordered shore, with tau_i separating
R_{i-1} from R_i.

Imported proof-only dependencies from current main:

1. exact O--O train cutset/layer property;
2. the hostile-audited exact simultaneous O--O multishear, including its signed
   split-row KKT resultant;
3. full-support positive KKT normalization;
4. the open witness cell contains no actual diameter direction;
5. complete retained A x B crossings are actual strict unit rhombi;
6. contact-minimal then diameter-pair-minimal normalization.

The multishear dependency is already hostile-audited at proof-only O--O cutset scope
in research/target_c_global_outer_train_exact_multishear_hostile_audit_2026-09-15.md.
The non-grazing argument below is rederived directly from the current open-cell
geometry.

## 3. Exact cyclic contact permutation

Define layer translations X_j by

```math
X_0=0,\qquad X_m=0,
\tag{3.1}
```

and, for 1<=j<=m-1,

```math
\boxed{
X_j=u_{j+1}-u_1.
}
\tag{3.2}
```

Translate every source point in R_j by X_j.

Put u_{m+1}:=u_1.

### Theorem 3.1 -- every old unit contact is preserved exactly

For every i=1,...,m,

```math
\boxed{
u_i+(X_i-X_{i-1})=u_{i+1}.
}
\tag{3.3}
```

Hence the move cyclically rotates the shore phase word

```math
(u_1,u_2,\ldots,u_m)
\longmapsto
(u_2,u_3,\ldots,u_m,u_1)
\tag{3.4}
```

while preserving every old unit contact exactly.

#### Proof

For i=1,

```math
X_1-X_0=u_2-u_1.
```

For 2<=i<=m-1,

```math
X_i-X_{i-1}
=(u_{i+1}-u_1)-(u_i-u_1)
=u_{i+1}-u_i.
```

For i=m,

```math
X_m-X_{m-1}
=-(u_m-u_1)
=u_1-u_m.
```

This proves (3.3).

Every contact in the cutset of tau_i is oriented from R_{i-1} to R_i with vector
u_i, so (3.3) replaces it by the unit vector u_{i+1}. Every other old contact has
both endpoints in the same layer and is unchanged.

Thus every old contact remains exactly unit.

Equivalently, put

```math
\delta_i:=X_i-X_{i-1}=u_{i+1}-u_i.
\tag{3.5a}
```

Each delta_i is exactly the one-train finite-shear vector which rotates the unit
contact vector u_i to the next unit vector u_{i+1}. The cyclic construction is
therefore a special case of the repository's hostile-audited exact simultaneous
O--O multishear. This observation will be used for the KKT orientation signs below.

### Uniform inverse-D displacement

Equation (2.1) and the chord bound give, uniformly,

```math
\boxed{
|X_j|\le {4K\over D}.
}
\tag{3.5}
```

More strongly, define

```math
\phi(0)=\phi(m)=u_1,\qquad
\phi(j)=u_{j+1}\quad(1\le j\le m-1).
\tag{3.6}
```

Then

```math
X_j=\phi(j)-u_1
```

for every j. Hence for any source pair xy with layer indices a,b,

```math
\boxed{
\Delta_{xy}:=X_b-X_a=\phi(b)-\phi(a),
}
\tag{3.7}
```

so

```math
\boxed{
|\Delta_{xy}|\le {4K\over D}.
}
\tag{3.8}
```

Thus the relative motion of every pair, not merely the motion of one point, is
inverse-D.

## 4. Every moved actual diameter is uniformly non-grazing

Let h=xy be an old actual diameter, |r_h|=D, with relative displacement

```math
\Delta_h=\phi(b)-\phi(a).
```

If Delta_h=0, h is unchanged.

Assume Delta_h is nonzero and put

```math
s_h:=|\Delta_h|,\qquad
w_h:={\phi(a)-\phi(b)\over s_h},
\tag{4.1}
```

so

```math
\Delta_h=-s_hw_h.
```

The two distinct unit directions phi(a),phi(b) lie in the same open witness cell J.
Let m_h be their projective midpoint and let epsilon_h be their projective
separation. Then

```math
s_h=2\sin{\epsilon_h\over2}.
\tag{4.2}
```

Because both directions lie strictly inside J, the midpoint m_h lies at projective
distance strictly greater than epsilon_h/2 from either boundary of J. No global
actual-diameter direction lies in J. Therefore the actual diameter direction [r_h]
satisfies

```math
d_{\mathbb{RP}^1}([r_h],m_h)>{\epsilon_h\over2}.
```

Since w_h is the quarter-turn of m_h,

```math
\boxed{
|r_h\cdot w_h|>{Ds_h\over2}.
}
\tag{4.3}
```

Equivalently,

```math
\boxed{
|r_h\cdot\Delta_h|>{D s_h^2\over2}.
}
\tag{4.4}
```

Hence

```math
|r_h+\Delta_h|^2-D^2
=
2r_h\cdot\Delta_h+s_h^2
\tag{4.5}
```

has the same sign as r_h dot Delta_h for D>1. In particular every moved old diameter
strictly shortens or strictly lengthens; no moved diameter remains at D.

## 5. KKT virtual work forces at least one strict shortener

For each cut tau_i, let A_i>0 be the total positive KKT contact weight on its contact
cutset.

For an old actual diameter h, choose an arbitrary orientation r_h and write
Delta_h for the corresponding relative layer displacement. Let beta_h>0 be its
full-support KKT diameter coefficient.

For an arbitrarily oriented diameter pair h=xy, let

```math
\sigma_{hi}:=\mathbf1_{S_i}(y)-\mathbf1_{S_i}(x)\in\{-1,0,1\}
```

be its signed incidence across cut tau_i, using the same shore convention as the
audited multishear theorem. The hostile-audited signed cut resultant is

```math
\boxed{
A_i u_i
=
\sum_h\beta_h\sigma_{hi}r_h.
}
\tag{5.1}
```

The exact multishear placement gives

```math
\Delta_h
=
\sum_{i=1}^m\sigma_{hi}\delta_i,
\qquad
\delta_i=X_i-X_{i-1}=u_{i+1}-u_i.
\tag{5.2}
```

Therefore, merely by exchanging the two finite sums,

```math
\begin{aligned}
\sum_h\beta_h r_h\cdot\Delta_h
&=
\sum_i\delta_i\cdot
\left(\sum_h\beta_h\sigma_{hi}r_h\right)\\
&=
\sum_i A_i u_i\cdot\delta_i.
\end{aligned}
\tag{5.3}
```

This is the same virtual-work identity that one obtains by summing the vertex
equilibria against the layer translations, but (5.1) fixes the orientation signs
using an already hostile-audited repository theorem.

Using (3.3),

```math
\sum_h\beta_h\, r_h\cdot\Delta_h
=
\sum_{i=1}^m
A_i\,(u_i\cdot u_{i+1}-1),
\qquad u_{m+1}=u_1.
\tag{5.4}
```

Every summand on the right is nonpositive. Since the cyclic phase word is
nonconstant, at least one consecutive cyclic pair is distinct, and A_i>0. Therefore

```math
\boxed{
\sum_h\beta_h\, r_h\cdot\Delta_h<0.
}
\tag{5.5}
```

Consequently at least one moved actual diameter has

```math
r_h\cdot\Delta_h<0.
```

By Section 4, that diameter strictly shortens under the full finite cyclic move.

## 6. Global cyclic fork

Equation (5.5) supplies a strict shortener. There are now exactly two possibilities.

### CYCLIC TWO-SIGN

Some moved old actual diameter satisfies

```math
r_g\cdot\Delta_g>0.
```

Then the cyclic move has both signs among its moving actual diameters:

```math
\boxed{
\exists h,g:
\quad
r_h\cdot\Delta_h<0<r_g\cdot\Delta_g.
}
\tag{6.1}
```

By Section 4, h strictly shortens and g strictly lengthens at the full finite
endpoint.

### CYCLIC ONE-SIGN

No moved old actual diameter has positive first-order work. The non-grazing estimate
excludes zero work for every nonzero Delta_h, so every moved old actual diameter has

```math
r_h\cdot\Delta_h<0
```

and therefore strictly shortens.

There is at least one moved old diameter by (5.3).

If every previously strict source pair remained strictly between 1 and D after the
cyclic move, the endpoint configuration would preserve every old contact exactly,
would create no new contact, and would create no new diameter pair.

If at least one old diameter is unchanged, the endpoint is another global
diameter-D minimizer with the same contact count and strictly fewer diameter pairs,
contradicting the canonical diameter-pair-minimal choice.

If no old diameter is unchanged, every old diameter strictly shortens, so the new
diameter is below D, contradicting global minimality.

Therefore some previously strict pair xy must violate one of the two metric bounds.
By (3.8),

```math
\boxed{
1<|xy|\le1+{4K\over D}
}
\tag{6.2}
```

or

```math
\boxed{
D-{4K\over D}\le|xy|<D.
}
\tag{6.3}
```

We have proved the global finite fork

```math
\boxed{
\text{CYCLIC TWO-SIGN active-diameter response}
\quad\text{or}\quad
O(D^{-1})\text{ inactive near-activity}.
}
\tag{6.4}
```

Unlike the pairwise block fork, this move acts on the entire retained nonconstant
shore at once.

## 7. The entire complete grid is immune to a cyclic inactive blocker

Fix any retained transverse train sigma on the opposite shore.

At the crossing of tau_i with sigma, the old strict rhombus has side directions
u_i and v_sigma. Under the cyclic layer move:

- the A-side contact vector u_i becomes u_{i+1};
- every sigma-contact edge is internal to an A-layer and is unchanged.

Therefore the transformed rhombus is congruent to the old retained rhombus at

```math
(\tau_{i+1},\sigma),
```

with cyclic convention tau_{m+1}=tau_1.

Thus the cyclic move permutes the complete retained grid row-by-row.

Every diagonal of every transformed retained grid rhombus has exactly the length of
a diagonal of an old retained strict unit rhombus. The short diagonal is >1 by unit
separation plus triangle-freeness, and the long diagonal is at most 2<D for large D.

Hence:

```math
\boxed{
\text{no diagonal of any retained complete-grid rhombus can be the blocker in
(6.2)--(6.3).}
}
\tag{7.1}
```

This is global grid immunity, not merely the two boundary-row immunity of one block
transposition.

## 8. Reverse cyclic rotation

The same construction with the opposite cyclic orientation sends

```math
(u_1,\ldots,u_m)
\longmapsto
(u_m,u_1,\ldots,u_{m-1})
```

and gives the same inverse-D displacement bound, strict KKT shortener, global
TWO-SIGN/ONE-SIGN fork, and all-grid immunity.

No compatibility claim between the two cyclic forks is made here.

## 9. Hostile audit

The theorem does not say:

1. that the CYCLIC TWO-SIGN branch is impossible;
2. that a CYCLIC ONE-SIGN blocker is an active pair;
3. that near-activity implies equality;
4. that the inactive blocker belongs to the complete grid -- Section 7 proves the
   opposite;
5. that an intermediate interpolation between the original and cyclic endpoint stays
   feasible. Only the finite endpoint comparison is used;
6. that arbitrary permutations have inverse-D displacement. The one-step cyclic
   permutation is special because its prefix translations telescope.

The proof also does not use a routing hub or the old high-t common-axis theorem.

## 10. Frontier effect

For a nonconstant open-cell shore, current main's pairwise finite transpositions can
now be supplemented by one global inverse-D contact automorphism:

```math
\text{nonconstant phase word}
\to
\text{cyclically rotate every train direction}
\to
\text{move every layer only }O(D^{-1})
\to
\text{preserve all old contacts exactly}
\to
\text{permute the entire strict-rhombus grid}
```

and then

```math
\text{KKT}
\to
\text{at least one old diameter strictly shortens}
\to
\begin{cases}
\text{another old diameter strictly lengthens},&\text{CYCLIC TWO-SIGN},\\
\text{a non-grid inverse-D inactive blocker},&\text{CYCLIC ONE-SIGN}.
\end{cases}
```

The next closing target is correspondingly global: eliminate CYCLIC TWO-SIGN using
convex-diameter order/support, or combine the forward and reverse cyclic moves to
force one inactive pair to block incompatible opposite finite displacements.

C-II and Level I remain open.
