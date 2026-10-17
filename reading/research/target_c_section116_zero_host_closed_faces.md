> Generated reading edition · [exact source](../../research/target_c_section116_zero_host_closed_faces.md) · source SHA-256 `4f2f8b0977246e620ab92f5d5712f3b781411a26c407770d1f0c881a199e4ff6`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target C — Section 116: zero-displacement hosts absorb every defect-face train end

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Status:** proof-only research candidate, stacked on the signed train-return theorem.

The signed train-return report leaves a directional bad-end profile as the obstruction
in its three-host area theorem.  For the full strict-rhombus complex of one harmonic
carrier, bounded nonquadrilateral faces do not actually need to be treated as bad.
Their full boundary cycles have zero displacement.  If a zero-displacement walk is
assigned the host vector `q=0`, the exact projection identity still holds, and all
closed defect-face cycles contribute the same single zero host.

This gives an exact finite theorem with **no bad physical train ends**: split the
occurrence-counted outer-face walk into three directed arcs and add every bounded
nonquadrilateral face boundary as a closed walk.  The three open outer arcs give at
most three unit host directions; all closed cycles give the common host `0`.  The
signed return / three-host area argument survives unchanged after this zero host is
added.

For a harmonic carrier with outer-walk length `L`, bounded-nonquadrilateral perimeter

```math
P_{\rm exc}:=\sum_{f\ \rm nonquad}\deg f,
```

strict-rhombus area `A_4`, and convex attachment-cell diameter `d`, choose three cyclic
cut occurrences on the outer walk at vertices `p_1,p_2,p_3` and put

```math
\Pi_3(p_1,p_2,p_3)
=|p_1-p_2|+|p_2-p_3|+|p_3-p_1|.
```

Then

```math
\boxed{
 d\bigl(L+P_{\rm exc}-\Pi_3(p_1,p_2,p_3)\bigr)
 \ge (2-\sqrt3)A_4.
}
\tag{116.1}
```

In particular, maximizing over the three cuts,

```math
\boxed{
 d\bigl(L+P_{\rm exc}-\Pi_3^{\max}\bigr)
 \ge (2-\sqrt3)A_4.
}
\tag{116.2}
```

Canonical Section 82 gives `P_exc<=5Q`, and the attachment polygon has three vertices
and contains a diameter pair, so `Pi_3^max>=2d`.  Hence

```math
\boxed{
 d(L+5Q-2d)\ge(2-\sqrt3)A_4.
}
\tag{116.3}
```

Using `L+Q=4a-6-2s-2c`, this also gives

```math
\boxed{
 d\bigl(4a-6-2s-2c+4Q-2d\bigr)
 \ge(2-\sqrt3)A_4.
}
\tag{116.4}
```

These are source-level finite inequalities on the actual harmonic carrier.  They do
not close C-II by themselves: the outer-walk detour `L-Pi_3^max` can still be linear.
But the new formulation removes bounded defect-face endpoints entirely from the bad
population.  The remaining obstruction is an outer-boundary three-arc detour theorem,
not a diffuse internal-endpoint theorem.

---

## 116.1 Zero-displacement walks fit the exact signed-return identity

Let `W` be any directed unit-edge walk with steps `v_1,...,v_ell` and displacement

```math
z=\sum_{r=1}^{\ell}v_r.
```

Define its host vector by

```math
q(W)=
\begin{cases}
z/|z|,&z\ne0,\\
0,&z=0.
\end{cases}
\tag{116.5}
```

Then in both cases

```math
\boxed{
\ell-|z|
=\sum_{r=1}^{\ell}(1-q(W)\cdot v_r).
}
\tag{116.6}
```

For `z!=0`, this is the exact projection identity from the signed-return theorem.  For
`z=0`, it is simply `ell=sum_r 1`.

Thus the finite signed-return proof needs only

```math
|q(W)|\le1,
```

not that every host vector have norm exactly one.

Let `Q` be the set of distinct host vectors of a collection of walks, now allowed to
contain `0`, and put

```math
w_Q(u)=\max_{q\in Q}q\cdot u-\min_{q\in Q}q\cdot u.
\tag{116.7}
```

The two physical ends of a complete train have opposite induced boundary orientations
`u,-u`.  If they are assigned injectively to occurrences on walks with hosts `q_i,q_j`,
their exact contribution to the total route excess is

```math
(1-q_i\cdot u)+(1+q_j\cdot u)
=2-(q_i-q_j)\cdot u
\ge2-w_Q(u).
\tag{116.8}
```

Therefore the signed-return inequality remains valid verbatim:

```math
\boxed{
E\ge\sum_{\tau\in\mathcal T_{gg}}(2-w_Q(u_\tau)).
}
\tag{116.9}
```

A zero host cannot create width two.  Since every `q in Q` lies in the closed unit
disk, `q dot u` lies in `[-1,1]`; if `w_Q(u)=2`, the extrema must be `+1` and `-1`,
which can only be attained by the genuine unit hosts `u` and `-u`.  Hence the
antipodal-return and four-oriented-corridor corollaries remain valid after adding any
number of closed walks: all of those walks contribute only the one host vector `0`.

## 116.2 The sharp two-direction/three-unit-host constant survives adding `0`

The signed-return report proves the following optimization for at most three unit host
vectors.  If `u,v` are unit train directions at projective angle
`phi in (0,pi/2]` and `a,b>0`, then

```math
\min
\{a(2-w_Q(u))+b(2-w_Q(v))\}
=a+b-\sqrt{a^2+b^2+2ab\cos\phi}.
\tag{116.10}
```

The same minimum holds when the common zero host is also allowed.

### Lemma 116.1 — zero-host stability of the three-host optimization

Let

```math
Q=Q_1\cup\{0\},
\qquad |Q_1|\le3,
\qquad Q_1\subset S^1.
```

Then

```math
\boxed{
 a(2-w_Q(u))+b(2-w_Q(v))
 \ge
 a+b-\sqrt{a^2+b^2+2ab\cos\phi}.
}
\tag{116.11}
```

Moreover the bound is sharp.

### Proof

Choose the sign of `v` so `u dot v=cos phi>=0`, and put

```math
\mathcal P=\{au,-au,bv,-bv\}.
```

As in the original three-host proof,

```math
a w_Q(u)+b w_Q(v)
=\sum_{p\in\mathcal P}\max_{q\in Q}p\cdot q.
\tag{116.12}
```

Write

```math
\Lambda
:=a+b-\sqrt{a^2+b^2+2ab\cos\phi}.
```

If, for some `p in P`, zero is the only possible maximizing host, then that support
maximum is zero rather than its unconstrained value `|p|`.  The loss is `a` or `b`.
But

```math
\Lambda\le\min(a,b),
\tag{116.13}
```

because the square root is at least `max(a,b)`.  Thus the desired total support loss
already occurs.

Otherwise each of the four support maxima has a realizing host in `Q_1`.  Assign one
such realizing unit host to each vector in `P`.  Since `|Q_1|<=3`, two of the four
vectors share a host.  The original collision argument then loses at least `Lambda`
from the unconstrained total support `2(a+b)`: an acute cross pair loses exactly at
least `Lambda`, an obtuse cross pair loses more, and an opposite pair loses `2a` or
`2b`, also at least `Lambda`.  This proves (116.11).

For sharpness use

```math
r={au+bv\over|au+bv|},
\qquad
Q_1=\{r,-u,-v\}.
```

The original three-host theorem attains equality on `Q_1`.  Also

```math
|au+bv|\,r+a(-u)+b(-v)=0,
```

so `0` lies in `conv(Q_1)`.  Adding `0` therefore does not change any support maximum,
and equality remains attained. `square`

For `a=b=1` and a strict unit rhombus, the two crossing train directions have
projective angle strictly greater than `pi/3`.  Hence for three unit outer hosts plus
the common zero host,

```math
\boxed{
(2-w_Q(u))+(2-w_Q(v))\ge2-\sqrt3=:c_{ret}>0.
}
\tag{116.14}
```

The weak endpoint constant is sufficient and is uniform over all strict rhombi.

## 116.3 Every bounded defect-face endpoint can be assigned to a zero host

Fix one harmonic carrier and let `H` be its induced planar contact graph.  Let
`mathcal R` be the full set of bounded strict-rhombus faces.  Canonical Section 82
proves that every other bounded face is a convex polygon of degree at least five and
that every physical boundary edge occurrence of `mathcal R` faces either

1. the outer face of `H`, or
2. one bounded nonquadrilateral face.

Take one bounded nonquadrilateral face `f`.  Its boundary is a simple contact cycle.
Orient the full cycle clockwise, so `f` is on its right.  Whenever an edge occurrence
of this cycle is also a physical boundary edge of `mathcal R`, the incident strict
rhombus lies on the other side and therefore on the left.  Thus the cycle occurrence
has exactly the physical boundary orientation required by signed return.

The full face cycle is closed, so its displacement is zero and its host vector under
(116.5) is `0`.  Edges of the face cycle that are not physical rhombus-boundary ends
are harmless additional walk occurrences and receive no train endpoint assignment.

Do this for every bounded nonquadrilateral face.  Their total walk length is

```math
P_{\rm exc}
=\sum_{f\ \rm nonquad}\deg f
=4f_{\rm exc}+Q
\le5Q,
\tag{116.15}
```

where the final inequality is canonical Section 82's `f_exc<=Q`.

Hence every physical train end facing a bounded defect face is good, and all such
closed routes add only the single host vector `0` to the return-width geometry.

## 116.4 Three outer arcs absorb every remaining physical train end

Let the occurrence-counted outer-face walk of `H` have length `L`.  Choose three
cyclic cut occurrences at outer-face vertices `p_1,p_2,p_3`.  They divide the outer
walk into three directed arcs `W_1,W_2,W_3`.  Orient the outer walk with the bounded
side on the left.

For every physical rhombus-boundary edge on the outer face, the incident rhombus is on
the bounded side, so its outer-walk occurrence has exactly its physical boundary
orientation.  Assign each such train end to that occurrence.  Occurrence counting
handles any repeated outer-face vertex without identifying distinct edge traversals.

Together with the closed defect-face assignments of §116.3, every physical end of
every complete train in `mathcal R` is now good, and the assignment is injective.

The three outer arcs have displacements

```math
z_1=p_2-p_1,
\qquad z_2=p_3-p_2,
\qquad z_3=p_1-p_3.
```

Therefore

```math
\sum_{i=1}^3|z_i|
=\Pi_3(p_1,p_2,p_3).
\tag{116.16}
```

Their total route excess is

```math
L-\Pi_3(p_1,p_2,p_3).
```

Every bounded defect-face cycle has zero displacement, hence excess equal to its full
length.  Thus the total excess of all designated walks is exactly

```math
\boxed{
E=L+P_{\rm exc}-\Pi_3(p_1,p_2,p_3).
}
\tag{116.17}
```

There are at most three nonzero unit hosts from the outer arcs, together with the
common zero host from all closed cycles.

## 116.5 Full-area transport with no bad endpoint term

Select **all** complete trains of `mathcal R`.  Every one has two good ends by §116.4.
At every retained rhombus, its two crossing trains satisfy the zero-host-stable local
bound (116.14).

For a train `tau` write

```math
\delta_\tau=2-w_Q(u_\tau).
```

Multiply (116.14) by the rhombus area and sum over every strict rhombus.  Reorganizing
by trains gives

```math
c_{ret}A_4
\le
\sum_\tau\delta_\tau
\sum_{R\in\tau}\operatorname{area}(R).
\tag{116.18}
```

Along one complete train with edge direction `u`, crossing a rhombus increases the
transverse coordinate `h_u=det(u,x)` by exactly the area of that rhombus.  Hence

```math
\sum_{R\in\tau}\operatorname{area}(R)
```

is exactly the transverse displacement between the two terminal boundary-edge
midpoints.  Both points lie in the convex attachment cell of diameter `d`, so this
sum is at most `d`.

The zero-host signed-return inequality (116.9), with every train double-good, now gives

```math
c_{ret}A_4
\le d\sum_\tau\delta_\tau
\le dE.
```

Substituting (116.17) proves the exact finite theorem (116.1).

Since it holds for every choice of three outer cut occurrences, maximizing their
triangle perimeter proves (116.2).

## 116.6 Canonical coarse corollaries

Every attachment vertex is an extreme vertex of the convex attachment polygon and lies
on the outer face of `H`.  The attachment set has at least three vertices.  Choose a
diameter pair `p_1,p_2` of the attachment polygon, so

```math
|p_1-p_2|=d,
```

and choose any third attachment vertex `p_3`.  The triangle inequality gives

```math
|p_1-p_3|+|p_3-p_2|\ge d.
```

Therefore

```math
\boxed{\Pi_3^{\max}\ge2d.}
\tag{116.19}
```

Together with `P_exc<=5Q`, (116.2) gives

```math
d(L+5Q-2d)\ge c_{ret}A_4,
```

which is (116.3).

Finally canonical Section 82 gives the exact local face ledger

```math
L+Q=4a-6-2s-2c.
```

Hence

```math
L+5Q=4a-6-2s-2c+4Q,
```

and (116.4) follows.

These inequalities should be compared with the older train-span estimate

```math
2A_4\le T_Rd,
\qquad 2T_R=P_R\le L+5Q.
```

That route implies only

```math
d(L+5Q)\ge4A_4.
```

Section 116 spends the same actual boundary occurrences differently: it retains the
three-cut outer displacement and uses oriented train return.  Depending on the ratio
`A_4/d^2`, neither inequality uniformly dominates the other; both are valid and can be
combined.

## 116.7 Scope and next obligation

The theorem removes a genuine obstruction from the signed-return program:
**bounded defect-face endpoints are not bad endpoints at all** once their full closed
face cycles are used as zero-displacement hosts.

The remaining all-regime full-core problem is therefore sharper.  One must control

```math
L+P_{\rm exc}-\Pi_3^{\max}
```

from above strongly enough to contradict the area lower bound, or exploit more of the
outer-walk structure than its scalar length.  Equivalently, the hard quantity is now
the detour of the actual outer boundary after subtracting the best three-chord return,
not the directional concentration of internal defect-face train ends.

The theorem does **not** assert that this detour is sublinear.  A long curved outer
boundary can have linear three-cut detour.  It also does not affect the separate
macroscopic inactive-container branch.

Dependencies:

- canonical Theorem 10.6 for complete train paths, exactly two physical ends, and
  opposite induced terminal orientations;
- canonical Section 82 for local convex faces, the exhaustive rhombus-boundary
  classification, `P_exc<=5Q`, and `L+Q=4a-6-2s-2c`;
- canonical Section 89 for the exact train/area transverse-span geometry;
- proof-only signed train-return SR/TW/AT from PR #325, extended here to the zero host.

**Theorem state:** unchanged.  C-II and LEVEL I remain open.
