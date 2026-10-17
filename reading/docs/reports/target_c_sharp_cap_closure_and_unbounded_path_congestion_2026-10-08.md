> Generated reading edition · [exact source](../../../docs/reports/target_c_sharp_cap_closure_and_unbounded_path_congestion_2026-10-08.md) · source SHA-256 `2c08e17b61bdc57d4b1901a8be372c8e6c95957b4f9a9a6108a578bdb2adee0b`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-595A0A1630F0","canonical":false,"claim_ids":["C-FAN-PATH-COMMON-TRUNK-REGRESSION"],"claim_statuses":{"C-FAN-PATH-COMMON-TRUNK-REGRESSION":"regression"},"index":"docs/state/artifact-index.jsonl","status":"regression","target":"target-c"} -->
# Target C: sharper finite cap closure and unbounded fan-path congestion

Date: 2026-10-08.
Run base: `35a588bd2d9cab829c1b13c68871ac1d602bd0bd`.
Canonical base: `fdbf00ea44e0b49bd519c39b732c33a5ea656044`.
State: `2026-10-08.audit.152`.
Classification: proved candidates awaiting independent audit/promotion;
the source-realized congestion family is a regression.
Registry: unreviewed; canonical=false. Level I and C-II remain open.

Rechecked after rebasing onto
`6e8dc144e2a0c268d261a43f298a47524c22b7f1`,
state `2026-10-08.audit.155`. The new conditional cap/grid
claims and diffuse-strain regression change no premise used here.

## 1. Exact source-preserving chain

The [canonical fan closure](../audits/target_c_centered_fan_blocker_closure_independent_audit_2026-10-08.md)
forces a blocker path to depth D/10 for a degree-two diameter fan.
The upper-pair argument actually needs no fan hypothesis. A sharper
midpoint calculation gives the following finite full-source gate.

    actual diameter endpoint
      + its shallow full-source lower-blocker closure
      -> simultaneous translation, with every source label retained
      -> no new contact or diameter pair, and an old diameter removed
      -> contradiction to the canonical lexicographic normalization.

Hence the closure must reach the depth stated below. For fan seeds the
first blocker remains a strict old noncontact. This is a finite motion
test with no deletion or refill premise.

The separate aggregate inference is not proved. The explicit family
below has an unbounded number of disjoint fan triples whose **unique**
directed near-unit paths all use one long isolate trunk. This survives
an analytic augmentation to asymptotically maximal area and leading
packing population. The configurations are nonglobal and have no
normalized KKT stress. No canonical-source overlap theorem is refuted.

## 2. Sharper cap upper-pair lemma

Let p,a be source points at distance D>=10 in a configuration of
diameter D. Put

```math
 u=(p-a)/D,\quad s(x)=u\cdot(p-x),\quad
 \kappa=1-\sqrt3/2,\quad 0<\delta\le1/D,\quad
 H=\kappa D-\delta/4.
```

All old source points satisfy |x-a|<=D and s(x)>=0. Suppose
s(x)<H, and translate x to x'=x-delta u while fixing y.
If |x'-y|>|x-y|, then **|x'-y|<D**.

Proof. Translate a to zero. Write t=s(y)-s(x), and
m=(s(x)+s(y))/2. The increase condition is exactly t<delta/2.
The midpoint identity gives

```math
 |x-y|^2\le4\{D^2-| (x+y)/2 |^2\}
          \le4(2Dm-m^2).
```

Here 0<=m<H+t/2<=H+delta/4=kappa D<D. Therefore

```math
 |x'-y|^2
 \le4(2Dm-m^2)-2\delta t+\delta^2
 <F(t):=4\{2D(H+t/2)-(H+t/2)^2\}-2\delta t+\delta^2.
```

On t in [-H,delta/2], the derivative

```math
 F'(t)=4(D-H-t/2)-2\delta>0,
```

since D-H-delta/4=(sqrt(3)/2)D and delta<=1/D.
Thus

```math
 |x'-y|^2<F(\delta/2)
   =4\{2D\kappa D-(\kappa D)^2\}=D^2.
```

The strict sign follows already from s(x)<H; t<delta/2 supplies
another strict inequality. No new-point ball containment or approximate
midpoint localization is assumed.

The leading coefficient kappa cannot be increased using only the
diameter geometry. The old four-point source

```math
 a=(0,0),\ p=(D,0),\
 x=(\sqrt3D/2,D/2),\ y=(\sqrt3D/2,-D/2)
```

is unit-separated for D>=10, has actual diameter D, and has
s(x)=s(y)=kappa D. Moving x by -delta u makes
|x'-y|^2=D^2+delta^2. This proves sharpness of the **leading**
coefficient, not optimality of the finite delta/4 correction.
The four-point source is explicitly nonglobal.

## 3. Full-source closure at every loaded endpoint

Use a triangle-free global minimizer selected contact-minimal and then
actual-diameter-pair-minimal, with all source labels retained. Fix any
actual pair pa and the parameters of Section 2. Define x -> y when

```math
 \begin{cases}
 |x-\delta u-y|\le1,& |x-y|>1,\\
 |x-\delta u-y|<1,& |x-y|=1.
 \end{cases}
```

Every arrow has

```math
 1\le d=|x-y|\le1+\delta,\qquad
 s(y)-s(x)>\delta/2,
```

and

```math
 d-1\le\delta\{s(y)-s(x)\}-\delta^2/2.
```

Let R contain p, be closed under all arrows leaving R, and lie in
s<H. Translate every label in R by -delta u; fix all other labels.
Closure preserves all lower constraints and prevents every strict
old pair from becoming a new unit contact. Internal pairs are unchanged.
Every increasing crossing upper pair is strictly below D by Section 2;
nonincreasing pairs remain at most their old lengths. Thus no new
actual diameter pair appears. The carrier a is outside R, and pa
shortens from D to D-delta.

The new source has the same cardinality and a contact graph contained
in the old triangle-free graph. A smaller diameter violates global
minimality. At diameter D, a contact loss violates the primary
normalization; if contacts are unchanged, loss of pa with no diameter
replacement violates the secondary normalization. Therefore R cannot
exist.

Following the finite arrow closure from p gives a path of distinct
source labels ending at its first depth >=H. Its length L and gap sum
satisfy

```math
 L\ge {H\over1+\delta},\qquad
 \sum(d_j-1)<\delta(H+1+\delta)-L\delta^2/2.
```

For delta=1/D and D>=20 this gives

```math
 L\ge D/8,\qquad
 \sum(d_j-1)<\kappa+1/D+3/(4D^2)-L/(2D^2).
```

All these near-unit paths are embedded, since 1+delta<sqrt(2).
Embedding alone supplies no disjointness or bounded congestion.

If p has exactly two contact neighbors p_-,p_+, all three at distance
D from a, delta=1/D is the exact reflection displacement. Its two old
contacts remain unit, so the first arrow is a strict old noncontact.
The canonical first-blocker estimate
s(x_1)>sqrt(3)/2-1/(4D) is unchanged. The extension to arbitrary
loaded endpoints allows contact arrows at the first step and makes
no isolated-population claim there.

## 4. An unbounded family with forced common trunks

Fix any integer q>=1. Put K=3q, M=64K^2 and

```math
 \sigma={1\over4M},\quad
 D=M+{1\over16M},\quad \delta=1/D,\quad
 w={1-\sigma^2\over1+\sigma^2},\quad
 z=1-\delta^2/2+i\delta w.
```

Then |z|=1. Write z=exp(i theta), so
delta<=theta<1.01 delta. Let a=0 and
p_j=D z^j for -1<=j<=K+1. All these coordinates are rational.
Consecutive p_j have distance one. Set

```math
 c=1+1/K,\quad \rho=1+\delta^2/100,\quad
 r_j=(D-3+c(D-\Re p_j),\Im p_j)\quad(0\le j\le K).
```

The r_j form an inward-facing row. Adjacent distances are strictly
greater than one and at most 1+delta. Choose the q+1 roots
p_i with i=0,3,...,K. Their contact-neighbor triples are pairwise
disjoint.

For each chosen i let u_i=p_i/D and f_i=p_i-rho u_i.
Join f_i to r_i by two almost-unit segments using a middle point m_i.
An exact equal-length construction is

```math
 v_i=r_i-f_i,\quad
 \lambda_i^2={\rho^2-|v_i|^2/4\over|v_i|^2},\quad
 m_i=(f_i+r_i)/2+\lambda_i Jv_i.
```

The radicand is positive. Replace lambda_i by its rational upper
approximation with denominator 10^6 M^6. Both segment lengths then
belong to [rho,1+delta^2/50). This makes the complete family rational.
Finally add the isolate trunk

```math
 t_j=(D-3-j\rho,0),\qquad
 1\le j\le T=\lceil D/7\rceil.
```

Take all the listed points as the source. There are
N=8q+7+T<D/5 points.

### 4.1 Separation and actual source graphs

The following uniform bounds give a direct all-q verification.
For 0<=j<=K, h_j=D-Re p_j lies in [0,.008); wall endpoints
at -1,K+1 have h_j<.02. All relevant angles are below .01.
The points f_i have normal depth in [.99,1.02] and tangential
offset from p_i below .011. The m_i have normal depth in
[1.98,2.02] and tangential offset below .17. The r_j have
normal depth in [2.98,3]. Distinct chosen column indices differ by
three, giving tangential separation at least 2.97 before offsets.

For completeness, |v_i| is between 1.9 and 2rho. In the equal-length
middle construction the perpendicular offset is below .16:

```math
\rho^2-|v_i|^2/4\le4(\rho-1)+3h_i<.16^2.
```

To see positivity explicitly, put A=c+1-rho/D. Then

```math
 |v_i|^2=(3-\rho)^2+
 h_i\{-2(3-\rho)A+2\rho^2/D\}
 h_i^2(A^2-\rho^2/D^2)\le(3-\rho)^2<4\rho^2.
```

The coefficient after factoring out h_i is negative using
1.9<A<2.4, 3-rho>1.9 and h_i<.008. Thus the square root is
real at every q, not just in the enumerated cases.

Rational upward rounding adds less than 3/(10^6 M^6) to each
segment length and preserves the displayed boxes. Hence every
listed near-unit segment is strict except the old wall edges.
Every other pair has distance greater than 1+delta: between a
middle and a nonmatching row point use the lower squared-distance
bound .96^2+.82^2>1.59; other exclusions follow from the separated
depth boxes or the three-index column spacing. Nonadjacent row
points have distance at least the corresponding circle chord,
which is greater than 1.99.
For a first column point and a different wall point, the exact
identity is
|f_i-p_j|^2=rho^2+(1-rho/D)|p_i-p_j|^2>1.99.

Every nonwall point lies strictly inside the radius-D disk about a.
All noncarrier source points have total normal range at most D/6
and tangential range below 2K, so their mutual distances are below
D. Consequently the complete actual diameter graph is exactly the
star joining a to every p_j. The complete unit-contact graph is
exactly the wall path. All f_i,m_i,r_j,t_j and a are contact-isolated.
There is no unit triangle. Each selected p_i is an actual degree-two
diameter fan leaf.

### 4.2 Unique arrows and unbounded congestion

For a root i use its own direction u_i and amplitude delta. The path

```math
 p_i\to f_i\to m_i\to r_i\to r_{i-1}\to\cdots\to r_0
       \to t_1\to t_2\to\cdots
```

consists of strict old noncontact arrows. Its two old wall contacts
remain exactly unit under the initial reflection.

The first and connector arrows have forward projection at least .9.
The trunk arrows have projection at least .99rho. To check a row
arrow j -> j-1 with 1<=j<=i, put

```math
 A_j=\sin((j-1/2)\theta),\quad B_j=\cos((j-1/2)\theta).
```

Its vector is (c A_j,B_j), its squared length is
1+(c^2-1)A_j^2, and its projection on u_i is
c A_j cos(i theta)+B_j sin(i theta). The uniform bounds imply

```math
 (c^2-1)A_j^2
 \le {5\over2}(j-1/2)\delta^2,\qquad
 2\delta\,u_i\cdot(c A_j,B_j)-\delta^2
 \ge(98j/25-99/50)\delta^2.
```

The right side exceeds the left for j>=1. Thus translating the
parent alone produces distance strictly below one.

The full near-unit graph contains only the wall edges, the listed
column segments, consecutive row edges, the row-to-trunk edge and
consecutive trunk edges. Reverse edges have negative forward
projection. At a selected root its two unit wall edges are not
arrows. At a row point a connector returning towards the wall is
not an arrow. Therefore the displayed path is **unique**, through
its first depth-H vertex, for each root.

Every such path contains the first floor(D/8) trunk points before
reaching H. Indeed their support depth is at most
3+(D/8)rho+.008<H for D>=576. Hence q+1 distinct roots, with
disjoint fan triples, force congestion q+1 on a common Theta(D)
isolate trunk. The union of all their paths has only O(D+q) points.
No bounded-multiplicity or sum-of-path-populations conclusion follows
from these finite source hypotheses.

Even the total near-unit gap on each path tends to zero. Using
d-1<=(d^2-1)/2, the row contribution is at most
5K^2/(12D^2)<=5/(768D); the trunk contribution is below
2/(700D)+2/(100D^2); the three column edges contribute below
1/(10D^2). Their sum is below 1/(100D) for D>=576.
Small accumulated length excess does not make a path straight or
make different paths independent.

### 4.3 Global and stress scope

This family is not a global minimizer. N<D/5 ordinary square-lattice
points have squared diameter below 2N<D^2. Moreover a is a loaded
contact isolate. Every actual diameter edge points from a towards
positive first coordinate. A normalized nonnegative diameter stress
cannot satisfy equilibrium at a, so there is no normalized KKT stress.
The family is not a canonical C-II source.

There is also a contact-preserving strict competitor using the same
source labels: fix a and translate every other point by -delta(1,0).
All internal pairs retain their distances. Every carrier-involving
distance remains above one and strictly below D, since its old first
coordinate is at least 5D/6 and its old distance from a is at most D.
Thus this is a finite full-source diameter improvement, despite the
absence of a shallow closure for an individual fan's reflection.

## 5. Leading-density augmentation preserving forced congestion

The regression can also retain asymptotically maximal full-source
area and leading packing population. This extension is analytic;
it is not enumerated by the finite checker.

Let o=(D/2,0), R=D/2. All old points lie in B(o,R+.02). Let U be
B(o,R-3) with the closed radius-(1+delta) disks about all old points
removed. Its area is at least

```math
 \pi(R-3)^2-\pi(1+\delta)^2N=\pi D^2/4-O(D).
```

Choose a translation of the triangular lattice of systole
1+2delta that puts at least its mean number of sites in U.
Those added sites have mutual and old-involving distances greater
than 1+delta. Thus they are contact-isolated and isolated in the
entire radius-(1+delta) near-unit graph. Every root's unique arrow
path and its forced common trunk are preserved.

All new-involving distances are below D: new sites have distance
at most (R-3)+(R+.02)<D from old points, and at most D-6 from
one another. The old actual diameter star is unchanged. The total
population is

```math
 n={\pi\over2\sqrt3}D^2+O(D).
```

The [canonical Oler inequality](../theory/03-oler-shell.md), together
with per(K)<=pi D, gives area(K)=pi D^2/4-O(D).
Thus full-source leading density and near-maximal hull area alone
do not bound this congestion.

Nonglobality remains explicit under any such augmentation. Apply
the same finite translation to the original noncarrier points and
fix a and every added point. Old-to-added separation exceeds
1+delta, so translation preserves strict lower separation. Every
moved original point has first coordinate at least 5D/6; its
distance from o decreases under this translation. Thus new-to-old
upper pairs remain below D-2.98. Original internal pairs are
unchanged, added-involving pairs are below D, and every old
carrier diameter strictly shortens. The diameter is strictly
smaller with every label retained. The original loaded carrier
remains a contact isolate, so the KKT obstruction is unchanged.

## 6. Certificate and unresolved bridge

`research/verify_target_c_cap_closure_path_congestion_2026_10_08.py`
checks rational base families q=1,2,3. It reconstructs every actual
unit and diameter pair and every pair of length at most 1+delta,
checks every candidate outgoing arrow through first depth H, and
certifies uniqueness and the shared trunk. It retains all contact
isolates and checks same-cardinality square-grid competitors.
For the uniform translation it checks all changed carrier pairs;
all other original pairs retain their previously checked distances.
It also checks rational cross-pair cap samples and three exact
leading-height regressions in Q(sqrt(3)).

The universal cap lemma, all-q construction and leading-density
augmentation are analytic proofs, not conclusions from those samples.
No canonical shallow closed set is extracted. The regression shows
that leading packing density and near-maximal full-source hull area
do not replace a congestion bound using global optimality or the
canonical stress.
Neither the cap calculation nor the source paths provide exchange
currency, a refill packet, or Level I closure.
