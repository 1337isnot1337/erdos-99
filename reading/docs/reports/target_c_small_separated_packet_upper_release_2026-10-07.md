> Generated reading edition · [exact source](../../../docs/reports/target_c_small_separated_packet_upper_release_2026-10-07.md) · source SHA-256 `212c3065d2b81c3014d33d5462d0952b5e8560e9a4db26c49027e0de0ab2bfb3`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-A2CF8FB478BA","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C: small separated packets with weak diameter upper bounds

Date: 2026-10-07.
Research base: 0f970f223f1b6019c36eaee38dfba7c409b900b4.
Canonical state inspected: 2026-10-08.audit.128.
Classification: proved candidate awaiting independent audit and promotion.
Artifact lifecycle: unreviewed, noncanonical.
Level I and C-II remain open.

## Exact implication being investigated

Finite packet dilation with simultaneous inward motion opens internal contacts
and all packet-involving diameter equalities. For a full-source equal-cardinality
replacement of a contact-minimal triangle-free global source, this contradicts
contact-minimality if an old contact was removed. A universal construction of
such replacements would close C-II. The result below does not construct them.

The finite lemma uses no global optimality or stress. Its global corollary uses
the universal circumradius theorem FS.1 in
[the full-source geometry audit](../targets/target-c/58-full-source-geometry-audit.md).
The circumradius theorem applies to every noncollinear global minimizer,
including one containing triangles.

## 1. Finite simultaneous upper release

Let $`Q=T\cup Y`$ be a finite planar unit-separated set of actual diameter $`D>0`$,
contained in a closed disk $`B(o,R)`$. Partition $`Y`$ into nonempty packets
$`Y_1,\ldots,Y_r`$. Suppose:

1. Each packet lies in a disk $`B(c_i,\rho_i)`$, with $`\rho=\max_i\rho_i`$.
2. Every packet-to-retained pair and every pair from distinct packets has
   distance strictly greater than one.
3. $`R+2\rho<D`$.

Keep every point of $`T`$ fixed. For $`p\in Y_i`$, define

```math
p(t)=p+t(o+p-2c_i)
     =c_i-t(c_i-o)+(1+t)(p-c_i).
```

There is $`t_0>0`$ such that, for every $`0<t\le t_0`$, all pair distances involving
$`Y(t)`$ are strictly between one and $`D`$. Thus the motion opens every new unit
contact and every upper equality involving an inserted point, simultaneously.
No point is deleted. The containing disk is used to certify the motion; the
motion is not claimed to stay in that disk.

### Internal pairs

For two points in one packet, their difference is multiplied by $`1+t`$.
Internal unit contacts open immediately. Initially, all internal distances
are at most $`2\rho<D`$, so internal upper distances have strict slack.

### Active packet-to-retained upper pairs

Translate coordinates so $`o=0`$. Let $`p\in Y_i`$, $`q\in T`$, and
$`r=p-q`$ with $`|r|=D`$. Since $`|q|\le R`$, we have $`|p|\ge D-R`$. Also
$`R\ge D/2`$, because the containing disk contains a diameter pair. Hence

```math
r\cdot p
=\frac{D^2+|p|^2-|q|^2}{2}
\ge \frac{D^2+(D-R)^2-R^2}{2}
=D(D-R).
```

The velocity of $`p`$ is $`v_p=-p+2(p-c_i)`$. Therefore

```math
r\cdot v_p
\le -D(D-R)+2D\rho
=-D(D-R-2\rho)<0.
```

So every active upper pair of this type shortens to first order.

### Active upper pairs between packets

For $`p\in Y_i`$, $`q\in Y_j`$, $`i\ne j`$, again write $`r=p-q`$ and $`|r|=D`$.
Then

```math
v_p-v_q=-r+2\big((p-c_i)-(q-c_j)\big),
```

and

```math
r\cdot(v_p-v_q)
\le -D^2+2D(\rho_i+\rho_j)
\le -D(D-4\rho)<0.
```

The last strict inequality follows from $`R\ge D/2`$ and $`R+2\rho<D`$.
No active diameter pair can be internal to one packet.

### A common positive finite time

Put

```math
\alpha=\min\{D(D-R-2\rho),D(D-4\rho)\}>0.
```

Let $`\sigma`$ be the minimum squared lower slack $`|p-q|^2-1`$ over
packet-to-retained and cross-packet pairs, and let $`\lambda`$ be the minimum
squared upper slack $`D^2-|p-q|^2`$ over inactive upper pairs involving $`Y`$.
Both minima are positive when their indexing sets are nonempty. Omit a
minimum's time bound if its indexing set is empty. Choose

```math
t_0=\min\left\{
\frac12,\frac{\alpha}{4D^2},
\frac{\sigma}{8D^2},\frac{\lambda}{16D^2}
\right\}.
```

Every moved velocity has norm at most $`R+2\rho<D`$, and every pair velocity has
norm at most $`2D`$. For an active upper pair, the squared-distance change is
at most $`-2\alpha t+4D^2t^2\le-\alpha t<0`$. For a strict lower pair, its
new squared distance is at least $`1+\sigma-4D^2t\ge1+\sigma/2`$.
For an inactive upper pair, its squared-distance increase is at most
$`4D^2t+4D^2t^2\le8D^2t\le\lambda/2`$. Internal lower pairs were already
handled by exact dilation. These bounds prove all claims for the same time.

## 2. Global contact-minimal replacement obstruction

Let $`A`$ be a triangle-free, unit-separated global minimum-diameter
$`n`$-point source, with $`D=D(n)\ge64`$, chosen to minimize the number of unit
pairs among triangle-free global minimizers. Delete a set $`S\subset A`$ and
write $`T=A\setminus S`$. Suppose an inserted set $`Y`$ of cardinality $`|S|`$
gives a full-source unit-separated placement $`Q=T\cup Y`$ of diameter at most
$`D`$. Retain every label of $`T`$, including its contact isolates.

Suppose $`Y`$ has a partition into packets satisfying the strict cross-pair
lower bounds in Section 1, and each packet has a containing disk of radius
at most $`D/8`$. Then such a replacement is impossible if either:

1. $`S`$ removes at least one old unit contact; or
2. $`S`$ meets every actual diameter pair of $`A`$.

### Proof

If $`Q`$ has diameter less than $`D`$, it already contradicts global optimality.
Otherwise $`Q`$ is an $`n`$-point global minimizer, whether or not it contains
triangles. It is noncollinear: a collinear unit-separated $`n`$-point set has
$`D\ge n-1`$, whereas the canonical strict lattice comparison gives
$`D^2<(2\sqrt3/\pi)(n-1)\le(2\sqrt3/\pi)D`$, incompatible with $`D\ge64`$.

FS.1 gives an enclosing circle with

```math
R<\frac D2+3^{1/4}\sqrt D<\frac{2D}{3}.
```

For the last inequality, use $`3^{1/4}<4/3`$ and
$`(4/3)\sqrt D\le D/6`$ when $`D\ge64`$. Thus

```math
R+2\rho<\frac{2D}{3}+\frac D4=\frac{11D}{12}<D.
```

Apply Section 1. The resulting placement $`T\cup Y(t)`$ is unit-separated and
has no unit contacts involving $`Y(t)`$; all its diameter pairs lie in $`T`$.
Its contact graph is precisely the induced old graph on $`T`$, and so it is
triangle-free even if the initial packet contained triangles.

If an old contact was removed, either its diameter decreases or it is a
triangle-free global minimizer with fewer contacts than $`A`$. Both are
contradictions. If $`S`$ meets every old diameter pair, then no retained pair
has distance $`D`$, and all pairs involving $`Y(t)`$ have distance less than
$`D`$, so its diameter decreases. This proves the two alternatives.

## 3. Relation to the existing frontier

[Audit.112](../audits/target_c_separated_packet_release_independent_audit_2026-10-07.md)
permits new unit anchors to the retained source when a strict separator opens
them, but requires every inserted upper distance to start strictly below $`D`$.
This candidate permits initial diameter equalities but requires strict lower
separation from the retained source and between packets, as well as small
containing disks. Neither statement implies the other at its exact scope.

The candidate applies to initial packets containing equilateral triangles;
internal contacts are all opened. It needs no secondary diameter-pair
minimum, loaded hull, contact stress, face integration, or displacement
control on the original deleted source.

It does not apply to a packet with a retained unit anchor. It does not
establish any packing capacity, clear a hole against retained labels, supply
a physical wall, or infer a simultaneous endpoint from individually feasible
insertions. In particular, a universal equal-cardinality replacement remains
unproved. Full-core and macroscopic-container C-II branches remain open.

## 4. Exact finite checks and their scope

The verifier
[verify_target_c_small_packet_upper_release_2026_10_07.py](../../../research/verify_target_c_small_packet_upper_release_2026_10_07.py)
uses rational arithmetic only. It checks two eight-point placements at three
certified positive times, every pair, retained positions, removal of four
internal unit contacts, and opening of inserted diameter equalities. One
fixture has packet-to-retained diameter pairs; the other has a cross-packet
diameter pair and a retained diameter pair that stays fixed.

It also checks two failures outside the hypotheses: a retained unit anchor
shortened by inward motion, and a large packet whose dilation increases its
diameter. These are failures of this deformation under weaker hypotheses.
They are not regressions against global optimality or C-II.

The finite checks neither establish the general analytic lemma nor prove that
the fixtures are global minimizers. The analytic proof is in Sections 1--2.
There has been no independent audit or promotion.
