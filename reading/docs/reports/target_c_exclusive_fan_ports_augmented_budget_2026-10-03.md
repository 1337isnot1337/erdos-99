> Generated reading edition · [exact source](../../../docs/reports/target_c_exclusive_fan_ports_augmented_budget_2026-10-03.md) · source SHA-256 `ee582320ddac0ed472c1bbbddb6bd33fbadc95b59027feec491bf1a037703698`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-A64E0BABD08F","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C: exclusive fan ports strengthen the augmented defect budget

**Date:** 2026-10-03.
**Base:** `7a327e1ad95cd2e9cb035b9b96fb34fd8f12114d`.
**State:** `2026-09-14.audit.51`; C-II and Level I OPEN.
**Branch:** `research/full-settlement-20261003`.
**Classification:** proved candidate awaiting promotion; finite regression.
No canonical state change.
**Certificate:** `research/verify_target_c_exclusive_fan_ports_2026_10_03.py`.

## 1. Exact implication and result

```text
canonical full-source midpoint bound -> third fan port has ONE loaded neighbor
-> marked attachment vertices have only nontriangular polygon sides
-> T + sum Q_r^+ + 2 d_tile <= 2(e_BB-k)
-> half the former high-t collar allowance in the same currency;
   a stronger lower defect charge or strict source competitor is still required.
```

Let X be the canonical triangle-free global source, retaining every source point,
and D>=10000. Let B be all actual diameter endpoints, q=|B|, and let a selected
internal good-fan vertex p have unique diameter partner a, unit fan neighbors
p_-,p_+, and |p-a|=|p_--a|=|p_+-a|=D. Its full contact degree is two or three.
Let U,T count those two classes across ALL selected fan runs and put I=U+T.
Use k=d_H+s_Z and canonical Section-123 component notation.

The new finite statements are:

1. A third unit neighbor z of any degree-three selected vertex p has **exactly
   one loaded unit neighbor**, namely p. This is stronger than injectivity
   along one same-carrier fan. Thus all T third ports are globally distinct.
2. The full source has a matching of at least ceil(U/2) strict blocker pairs
   1<|p-y|<=1+1/D, with loaded degree-two fan endpoint p and diameter-inactive
   endpoint y. More generally, it has a matching of at least
   max(T,ceil(I/2)) loaded-to-diameter-inactive pairs of distance <=1+1/D,
   where the T third-port pairs are actual unit contacts. The second bound is
   a single matching cardinality lower bound, not the sum of two matchings.
3. For the harmonic augmented graphs,

       T <= sum_r(a_r-T_r),
       T + sum_r Q_r^+ + 2 d_tile <= 2(e_BB-k).             (1)

The proof-only high-t chain gives
T>=2 per(F)-2t_D D-5nu-5x_B-4 and e_BB-k=t_D D-m_nonunit.
Conditional on exactly those finite inputs, (1) therefore gives

    sum_r Q_r^+ + 2d_tile
      <=4t_D D-2 per(F)+5nu+5x_B+4-2m_nonunit.             (2)

In the Type-II square-root branch this becomes

    limsup (sum_r Q_r^+ + 2d_tile)/D <=4t-2pi.             (3)

This is stronger than the prior collar allowance 8t-4pi whenever t>pi/2.
At t=1.860 it is 1.1568146928...; that low-matching/low-outer-loss regime
was already excluded in this run by the separate fan/train threshold.
At its new necessary endpoint t=3pi/5, the remaining allowance in (3)
is 2pi/5. It stays positive: no closure is claimed.

## 2. A finite short-hull-chain estimate

Canonical Section 58, FS.6 places every actual diameter midpoint within

    L_D=sqrt(D eta+eta^2), eta=3^(1/4)sqrt(D),

of the full-source circumcenter. For D>=10000,

    L_D^2/D^2 <4/(3 sqrt(D))+7/(4D)
              <=4/300+7/40000 <1/64.

Thus L_D<D/8. This is a statement about the complete source, not an
affine-kernel extension to its isolates.

For loaded vertices p,q, choose any actual partners a_p,a_q and let
n_p=(p-a_p)/D,n_q=(q-a_q)/D. These are exposed outward hull normals.
Writing m_p,m_q for their midpoints gives

    D(n_p-n_q)=2(p-q)-2(m_p-m_q).

If d=|p-q|<=2+2/D and theta is the smaller ordinary normal angle, then

    sin(theta/2) <=(d+2L_D)/D <1/4+(2+2/D)/D <51/200.

Since (51/200)^2+(29/30)^2<1, put c=cos(theta/2)>29/30.
All sides of the hull chain corresponding to the short normal interval
have normal between n_p,n_q. Projection onto its bisector tangent is at
least c times their length, with a common sign. All full-source hull sides
have length at least one by unit separation. Consequently a chain of j
sides gives d>=jc. Because 3c>2+2/D, p,q are either immediate full-hull
neighbors or have exactly one intervening full-hull vertex r.

Every good fan contact is a full-source hull side, not merely a loaded-hull
side. In coordinates around its common diameter carrier, its endpoints are
(sqrt(D^2-1/4),+-1/2). A source point in the closed minor cap beyond their
chord is within distance <1 of the nearer endpoint, since

    (D-sqrt(D^2-1/4))^2+1/4<1.

Thus no other source point is in that cap or on the chord segment. The two
fan neighbors p_-,p_+ are p's immediate full-source hull neighbors. This
also retains and rules out an intervening contact isolate rather than deleting it.

## 3. Global loaded-contact exclusivity of a third port

First z is diameter-inactive. If it were loaded, the short-chain estimate
with |p-z|=1 forces hull adjacency (two sides have projection >1). But p's
two immediate neighbors are already p_-,p_+, so z could not be a third neighbor.

Suppose z also has a loaded unit neighbor q distinct from p. Then |p-q|<=2.
If p,q are adjacent hull vertices, their edge is one of p's two unit fan
edges. The three unit contacts pq,pz,qz would form a forbidden equilateral
triangle. Otherwise the short hull chain is p,r,q. Its first side has length
one and its second length ell>=1. Projection gives

    d >= (1+ell)c, hence ell <=2/c-1 <31/29,
    d >=2c >29/15.

Both r and z lie in the intersection of the closed radius-31/29 disks
about p,q: r has distances 1,ell and z has distances 1,1. This lens has
diameter at most sqrt(4(31/29)^2-d^2), which is strictly less than one because

    4(31/29)^2-(29/15)^2 <1.

The lens bound follows by centering at the midpoint: membership in both
disks implies squared distance from that midpoint <=rho^2-d^2/4.
Thus |r-z|<1. They are distinct, since r is a fan neighbor and z is the
third neighbor. This contradicts source unit separation and proves exclusivity.

This argument works across different carriers and against loaded q that is
not an internal good-fan vertex. No lower bound on a contact multiplier is used.

## 4. A half-population source blocker matching

For a degree-two fan vertex, the solo reflection

    F_p(p)=p-(p-a)/D^2, F_p(x)=x for x!=p,

preserves its two unit contacts and moves it by 1/D. For every original source
y at distance d from p, the full-source diameter bound to a gives

    |F_p(p)-y|^2-d^2 <=-(d^2-1)/D^2.

All upper constraints are protected. If every old noncontact remained >1,
the map would preserve every old contact, shorten p's actual diameter, and
create no new contact or diameter. Global optimality or diameter-pair minimality
would be contradicted. Thus choose one strict blocker y_p with
|p-y_p|>1 and |F_p(p)-y_p|<=1. Necessarily |p-y_p|<=1+1/D.
It is diameter-inactive: if loaded, the short-chain estimate would make it
an immediate fan neighbor and hence an old unit neighbor.

For a degree-three vertex choose its actual third port instead. Write c_p=F_p(p)
in the degree-two case, and c_p=p in the degree-three case. Every chosen port y_p
has |c_p-y_p|<=1, and is diameter-inactive. If one port were chosen by two
nonadjacent selected fan vertices p,q, their old distance is <=2+2/D. Their
short hull chain is p,r,q with both sides unit: both selected vertices have
unit immediate hull neighbors. Hence |p-q|>=2c, while

    |c_p-c_q| >=2c-2/D >29/15-1/5000 >sqrt(3).

Both the common port and r lie in the closed unit lens about c_p,c_q, because
solo reflections preserve the unit neighbor r. Its diameter is less than one.
The port is distinct from r because it is inactive while r is loaded (a fan
neighbor). This is a contradiction. Thus a port can serve only two consecutive
fan vertices, and never two degree-three ones by Section 3.

The full hull has at least four vertices when a selected fan exists: a
three-vertex hull with two unit sides at p would have diameter <=2. Any three
selected fan vertices therefore contain a nonadjacent pair. Each inverse port
fiber has size at most two. Distinct port endpoints are disjoint from all the
loaded fan endpoints, so choosing one pair from each fiber gives a source
matching of at least ceil(I/2), and the third-port matching gives T. The same
argument restricted to degree-two vertices gives ceil(U/2) strict blocker pairs.
These are exact matching statements; no simultaneous feasibility of reflections
on adjacent fan vertices is asserted.

## 5. Charge the SAME Section-123 currency

A degree-three selected loaded vertex p has exactly one unloaded contact pz.
Assign p to the unloaded component I_r containing z. Its unique loaded contact
exclusivity from Section 3 means z has no other loaded unit neighbor. In J_r^+,
p is a polygon vertex with exactly one contact to I_r, plus its two added
polygon sides. Neither polygon side incident with p can bound a triangular
face: such a face would require z to contact the next loaded polygon vertex.
A face with three loaded vertices would require the entire attachment polygon
to be a triangle with no component in its interior; I_r is nonempty, so it
cannot be a bounded triangular face. A contact-only triangle is already forbidden.

Let M_r count these marked polygon vertices. Their 2M_r polygon-side
incidences are on nontriangular sides; each side has at most two marked ends.
Every triangular bounded face uses one distinct added polygon side. Therefore

    M_r <= a_r-T_r.

The assignment is unique because p has only one unloaded contact. Summing
gives T<=sum_r(a_r-T_r). Insert this into the canonical exact identity

    2(e_BB-k)=sum_r(a_r-T_r+Q_r^+)+2d_tile

to prove (1). No port, face, or tiling defect is charged twice. The marked-side
argument subsumes the old collar count S when applied to adjacent marked vertices
in one component, but does not require a chosen collar face or an adjacent TT pair.

For the Type-II application the finite T population and e_BB-k identity stated
in Section 1 give (2) by subtraction; dividing by D gives (3). Those population
inputs remain proof-only, while the exact Section-123 composition is canonical
at its stated harmonic-cell hypotheses. This report does not promote that chain.

There is a stronger structural corollary when ALL internal good fans are selected.
The preceding report in this run proves q-N_adj<=3nu. Removing at most x_B bad
adjacencies leaves at least q-3nu-x_B good fan edges in at most nu+x_B nonempty
runs. A run of g edges has g-1 internal vertices. Therefore

    I>=q-4nu-2x_B.

Every fan vertex of contact degree two has no unloaded attachment; every
degree-three one appears in exactly one A_r. Each remaining loaded vertex has
at most three contacts, hence appears in at most three attachment sets. Thus

    T <= sum_r a_r <= T+12nu+6x_B,
    sum_r T_r <=12nu+6x_B.                                  (4)

For the second inequality, every triangular polygon side must have two
unmarked endpoints; the number of such sides in a polygon is at most its
number of unmarked vertices. This bound uses actual marked sides, not an
Eppstein near-equality interpretation. Summing the exact component identity
2s_r=a_r+T_r-Q_r^+-6 gives

    T-sum Q_r^+-6c_I <=2s_C
      <=T-sum Q_r^+-6c_I+24nu+12x_B.                       (5)

In the Type-II low-matching/low-outer-loss branch c_I=o(D),
s_C=(pi-t_D)D+o(D), q=pi D+o(D). Write u=U/D. Equations (4)--(5) and the
definition of d_tile give the necessary normalized relations

    T/D=pi-u+o(1),
    (sum Q_r^+)/D=2t_D-pi-u+o(1),
    d_tile/D=u+o(1),
    E/D=2t_D-pi+u+o(1),  0<=u<=2t_D-pi+o(1).             (6)

Thus the residual is quantitative. It can sit in the tiling deficit even
when the augmented exceptional-face excess vanishes. This is not an existence
assertion about a canonical source.

## 6. An exact pentagon defeats a proposed stronger endpoint capacity

The tempting claim that an exceptional pentagon admits at most two contact
edges in an arbitrarily narrow projective direction window is false, even with
two consecutive actual good-fan edges in that window.

For any integer k>=100 put

    c=(k^2-1)/(k^2+1), s=2k/(k^2+1),
    h=sqrt(1-(c-1/2)^2), D=1/(2s).

Take the unit pentagon in the displayed cyclic order

    P0=(0,0), P1=(c,s), P2=(2c,0),
    Z2=(c+1/2,-h), Z0=(c-1/2,-h).

Its five edges are unit. Its five diagonals have squared lengths
4c^2, 1+2c (twice), and 2-2c^2+c+2sh (twice), all strictly greater than one.
For the last expression, its excess over one is
(1-c)(2c+1)+2sh>0. Thus the complete five-point source is triangle-free and
unit separated. The three edges P0P1,P1P2,Z2Z0 have projective angles
atan(s/c),-atan(s/c),0, which tend to zero as k tends to infinity.

This can be an ACTUAL fan boundary face, rather than only an edge-vector
network. Add the carrier a=(c,s-D) and two more circle points

    Pleft=(c-2c(1-2s^2), s-4s c^2),
    Pright=(c+2c(1-2s^2), s-4s c^2).

The five points Pleft,P0,P1,P2,Pright lie on B(a,D) in that order with unit
consecutive chords. All pairs in this full eight-point source are unit separated
and at distance <=D; its only diameter pairs join a to those five points.
The pentagon is a bounded contact face. P0,P2 are internal degree-three
diameter leaves with exclusive ports Z0,Z2; P1 is an internal degree-two leaf
whose solo reflection is blocked by both ports. The certificate checks all
source pairs and all these assertions exactly in Q(h), for the listed k values.
The arbitrary-small-window assertion follows analytically from s/c->0.

Here is also a uniform verification, so the parameter family is not inferred
from five samples. For k>=100, c>99/100, 0<s<1/50, 4/5<h<1 and D>25.
The consecutive fan chord lengths are exactly one; chords skipping two,
three or four steps have lengths 2c, 3-4s^2 and 4c(1-2s^2), respectively,
all strictly between one and four. The distances from P0,P1,P2 to the ports
are exactly the pentagon edge and diagonal expressions already given.
For Pleft or Pright, even the smaller horizontal distance to a port is
2c(1-2s^2)-1/2>1, so these pairs are strict. All seven noncarrier points
lie in a box of width <4 and height <51/50, so their pair distances are <5<D.
For a port put v=s+h, with 4/5<v<51/50. Its squared carrier distance is
1/4+(D-v)^2<D^2, since 2Dv-v^2>40-(51/50)^2>1/4.
These checks give exactly the claimed contacts and diameter pairs.
The pentagon is strictly convex in the displayed order; the carrier lies
below it and Pleft,Pright lie to its left and right. Thus no extra vertex
or contact enters its bounded face. Finally the reflected P1 is (c,-s).
Its squared distance to either port minus one is
(1-c)(2c+1)-2sh<3s^2-8s/5<0. This proves both strict lower blockers
for every k>=100, and completes the arbitrary-parameter source regression.

This source is nonglobal: a is contact-isolated, and the two-port unloaded
component is not harmonic or inside a three-vertex attachment polygon.
It is NOT a regression to canonical Section 123 or to a conjectured global
defect lower bound. It refutes only the face-geometry endpoint-capacity claim.
No extension of the core rigidity theorem is made for its isolated carrier.

Nonglobality can also be certified by an explicit full-source competitor:
fix a and translate all other seven points downward by 1/10. Their mutual
unit and inactive distances are unchanged. Their distances to a strictly
decrease, since every vertical separation exceeds D-51/50>23. After the
move each remains at distance >D-51/50-1/10>1 from a. Every pair is still
unit separated and every pair has distance strictly below D. This is a
same-cardinality strict sub-D map on this exact source, checked on all pairs
by the certificate. Its extension to the canonical source is unavailable:
the isolated carrier and absence of external contact cut edges are hypotheses
that its positive-contact core does not supply. This source-preserving
construction cannot be advertised as a global Target C descent.

The two-leaf blocker capacity in Section 4 is also sharp for local full-source
geometry. In the same five-point fan and carrier, replace the two pentagon ports
by the one inactive point

    y=(c/2+Hs, s/2-Hc), H=sqrt(3)/2+1/(4D).

It has old squared distance 1/4+H^2>1 from each of the adjacent internal
degree-two leaves P0,P1. Either solo reflection gives squared distance

    1/4+H^2+1/(2D^2)-2Hc/D <1.

Its excess over one is
sqrt(3)(1/4-c)/D+(9/16-c/2)/D^2<0 for c>99/100,D>25.
All distances to the other fan points exceed one by their horizontal separation,
and its carrier distance is below D. The script checks every pair at k=100000,
including both solo maps with y removed, which are fully feasible. Reflecting
both adjacent leaves instead makes their old unit edge exactly 1-1/D^2<1.
Thus the blocker assignment cannot be claimed injective on all adjacent leaves,
and separate feasible solo maps cannot be added. This seven-point source is also
nonglobal, with an isolated carrier; it delimits the new matching result without
giving a counterexample to global minimality.

## 7. Composition attempted and exact remaining obstruction

The allowance is now 4t-2pi in the same currency E=sum Q_r^++2d_tile, rather
than 8t-4pi. The separate fan/train threshold requires t>=3pi/5 when matching
and outer loss are sublinear. At that endpoint the bound is E/D<=2pi/5,
and T/D>=4pi/5. Thus a source-preserving, nonduplicating lower charge

    E >= T-o(D)

would force t>=2pi/3 and remove the entire interval 3pi/5<=t<2pi/3.
It has NOT been proved. Port exclusivity spends the nontriangular-side term
of Section 123; it cannot also be counted as Q_r^+ or d_tile. Bare endpoint
capacity counts supply only a fifth-scale global exceptional-face bound,
which is compatible with the new positive allowance. The pentagon above
blocks the proposed two-endpoint improvement based on narrow face directions
alone. Actual train cyclic order, harmonic continuation, or a source refill
must supply the missing charge. This run does not infer one from analogy.

For clarity, the current scalar composition has an exact feasible asymptotic
relaxation at t=3pi/5. In units alpha=pi/5, assign

    q=5, k=s_C=2, e_BB=b=5, t=3,
    U=Q=d_tile=f=1, T=sum a_r=4, sum T_r=sum Q_r^+=0,
    T_stop=5.

These are normalized limiting currencies (c_I/D=nu/D=x_B/D=0), not integer
finite graph data. They satisfy b+Q=2t, T+U=q,
2s_C=sum a_r+sum T_r-sum Q_r^+, the Section-123 payment T+E=2t,
the fan-train lower bound T_stop>=q, and its upper bound T_stop<=t+2f
with f<=Q. They also obey (6). Consequently these inequalities, even with
port exclusivity and the improved T-payment, cannot alone exclude that
endpoint. The certificate checks the normalized assignment with exact integers.
The nonglobal pentagon demonstrates a compatible local fan gap, but does not
co-embed or certify this asymptotic relaxation as a source.

Canonical dependencies: Section 58 FS.6, loaded contact degree bound, exact
Section-123 ledger. The marked-side result is analytic and finite. The high-t
numerical specialization is conditional on its stated proof-only fan population
and loaded-hull identity. The older same-fan injectivity and solo flip were
rederived and are not claimed as new; global loaded-neighbor exclusivity, the
half-population combined matching and the T-budget are the new bridges.
No external literature was imported. Promotion requires independent audit.

## Slot 2 recovery provenance — 2026-10-05

Recovered from `research/full-settlement-20261003` at exact source tip `c044a07f59dbe0993d69c801f73a21f1927838b0`; no original PR was associated with the source branch. This artifact is preserved as a unreviewed proof-only candidate. It does not change theorem state. Any conditional source hypotheses and limits remain as stated above; C-II and Level I remain open.
