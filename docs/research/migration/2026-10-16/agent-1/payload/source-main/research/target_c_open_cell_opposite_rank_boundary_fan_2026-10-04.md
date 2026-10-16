# Target C: open-cell opposite-rank boundary-fan localization

Date: 2026-10-04
Base main: e7edb6d19eeb3a1d04b315f1c2fcf7eb7816e845
Status: proof-only Target C-II candidate; theorem-state authority unchanged.
LEVEL I STATUS: STILL OPEN. C-II REMAINS OPEN.

This note stays entirely in the nonconstant open-witness-cell strong-SCC route.
It combines the current maximal A-staircase, four-host geometry, joint two-shore
switch budget, and opposite-shore rank theorem.

Let the selected A shore have cuts tau_1,...,tau_m and the opposite B shore
sigma_1,...,sigma_n. Use the four host intervals in cyclic order

    I_A^+, I_B^+, I_A^-, I_B^-.

The A-layer varies on the A-hosts and is constant at 0,m on the two B-hosts;
symmetrically the B-layer varies on the B-hosts and is constant at 0,n on the
two A-hosts.

For an actual diameter h let t_A(h),t_B(h) be its internal incidence-switch
counts. Current main gives

    t_A(h)+t_B(h) <= 2.                                    (1)

In the strong open-cell branch, all nonempty A-support types form one maximal
staircase. Let I be the number of internal staircase types 0<a<b<m, and let
s=m-I. The s noninternal types form one initial one-sided boundary run. Its
proper part is a fan of f=s-1 support types, all incident with layer 0 or all
incident with layer m.

Assume I>0. Current main then supplies an actual diameter e=xy over an internal
A-support. Its endpoints have internal A-layers, lie on opposite A-hosts, and e
is full-support on B.

## Lemma 1: same-B-host exclusion

No actual diameter has both endpoints in I_B^+, and none has both endpoints in
I_B^-.

Indeed, either B-host interval lies wholly in one boundary arc cut off by x,y.
A chord with both endpoints in one B-host does not cross e. It cannot share an
endpoint with e because A-hosts and B-hosts are disjoint. This contradicts the
convex diameter-thrackle property.

## Lemma 2: two B-switches force A-full support

If t_B(g)=2, then both endpoints of g lie on B-host intervals: the joint-switch
proof gives

    t_B(g) <= number of endpoints of g on B-hosts.

Lemma 1 forbids the same B-host, so the endpoints lie on opposite B-hosts.
Those hosts have opposite extreme A-layers 0,m. Hence g is full-support on A.

## Lemma 3: a B-proper row cannot be A-empty

Let g have nonempty proper B-support and t_A(g)=0. Its A-support is empty or
full. Suppose it is empty.

Since the B-support is proper and nonempty, at least one endpoint lies on a
B-host, hence has extreme A-layer k in {0,m}. A-empty support makes both
endpoints have the same A-layer k.

The nested A-crosscuts give boundary-layer order

    0,1^+,...,(m-1)^+,m,(m-1)^-,...,1^-.

Thus all boundary points of A-layer 0 form one exterior boundary interval, and
all boundary points of A-layer m form the opposite exterior interval. Since
e has internal-layer endpoints on opposite A-hosts, each extreme interval is
contained in one of the two boundary arcs between x and y. Both endpoints of g
therefore lie on the same boundary arc between x and y, so g does not cross e.
They cannot share an endpoint because e has internal A-layers. This again
contradicts the diameter-thrackle property. Thus g is A-full.

## Theorem: opposite-rank normal form

Assume I>0. Every actual diameter with nonempty proper B-support is exactly one
of:

1. A-full; or
2. t_A=t_B=1, hence a shared-switch corner row.

For a B-proper row, t_B is 1 or 2. The t_B=2 case is Lemma 2. If t_B=1,
(1) gives t_A<=1; t_A=0 is Lemma 3, leaving t_A=1.

Every row in class 2 has nonempty proper A-support touching exactly one
A-extreme. The open cell makes every nonempty A-support row transversely active,
and the strong-SCC classification says every such support type is one of the
maximal staircase types. Therefore every corner row lies on the proper part of
the single one-sided A-boundary fan.

The joint-switch corner theorem further puts all such corner rows in at most two
adjacent grid-corner types, hence on one common host interval.

## Opposite-rank ledger

Let N_full be the number of rows that are A-full and B-proper. For each proper
A-boundary-fan support q, let mu_q be the number of B-proper corner rows over q.
The B-rank theorem gives at least n-2 distinct B-proper diameter rows, so

    N_full + sum_q mu_q >= n-2.                            (2)

If B is exact phase, the right side improves to n-1.

Consequently

    N_full >= (n-2)/2
    or
    sum_q mu_q >= (n-2)/2.                                (3)

If f>0 and N_full<M, then some one fan support satisfies

    mu_q >= ceil((n-2-M+1)/f)                             (4)

whenever the numerator is positive. If f=0, every B-proper rank row is A-full.

This is stronger than the existing count h>=2I+n-2. It identifies where every
opposite-rank row can live. In particular, the old boundary-heavy case is no
longer diffuse whenever I>0: its B-rank residue is either a linear A-full/B-proper
packet or corner multiplicity on the same one-sided A-boundary fan. The only
boundary-heavy case not covered is the pure star I=0.

After excluding the inverse-D inactive-near-activity alternative, the strong
open-cell branch is therefore reduced to:

1. pure one-sided A-star staircase, I=0;
2. I>0 with a linear A-full/B-proper packet; or
3. I>0 with a linear corner packet supported on the one-sided A-boundary fan
   and at most two adjacent physical grid corners.

No computation, verifier, numerical experiment, or CI result is used. The result
does not bound fan multiplicity or exclude the A-full packet; those are the next
source-level contact/KKT obligations.

Disposition: proof-only Target C candidate. C-II and Level I remain open.
