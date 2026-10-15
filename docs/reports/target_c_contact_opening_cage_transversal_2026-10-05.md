<!-- theorem-state: {"artifact_id":"ART-5A833823CAF0","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — contact-opening cage transversal

Date: 2026-10-05. Base: `3c94a1a93641a5f8fa24d43068d487594d3e38cd`.
State: `2026-10-05.audit.57`.
Classification: **proved candidate awaiting independent audit**; registry
status remains **unreviewed**. Level I and C-II remain open.
No external literature or computation is used in the universal proof.

## 1. Objective

```
delete a vertex transversal of every normalized positive KKT support
-> a straight motion strictly opens surviving contacts and shortens diameters
-> any sufficiently robust certified refill packet restores cardinality
-> strict sub-D competitor.
```

Unlike the exact-contact chart, this motion may lengthen original contacts.
It gives a smaller linear obstruction cone. It does not certify a finite
opening large enough to activate a pentagon or any refill capacity.
Canonical normalization `C-ZTA` is used to identify the actual active
contacts and diameter pairs. No C-I reopening is involved.

## 2. Finite first-order theorem

For any finite unit-separated source A of diameter D>1, and U subset A,
let A_U=A\U, C_U its actual unit contacts, and H_U its actual D-pairs.
For each c=ij define the lower signed row

    a_c(u)=(p_i-p_j) dot (u_i-u_j),

and for each h=ij define the upper signed row

    a_h(u)=-(p_i-p_j) dot (u_i-u_j).

There is a velocity with a_c(u)>0 for every c in C_U and a_h(u)>0
for every h in H_U if and only if A_U has no normalized nonnegative
KKT stress with contact coefficients alpha>=0, diameter coefficients
beta>=0, and sum beta=1.

### Proof

A nonnegative row relation among the signed rows is vertex equilibrium
for alpha,beta. Pair that relation with the position field p. It gives

    sum_C_U alpha_c = D^2 sum_H_U beta_h.

Hence a nonzero nonnegative relation cannot have beta=0; otherwise all
alpha vanish as well. Every such relation can therefore be normalized
by sum beta=1.

The converse strict-separation argument is elementary. If zero is in
the convex hull of the signed rows, its convex weights give a nonzero
nonnegative relation. If it is outside, take the nearest point z of
that compact convex hull to zero. With any inner product on the finite
velocity dual, nearest-point minimality gives

    <z,a_e> >= ||z||^2>0

for every row. The velocity dual to z evaluates all signed rows positively.
An empty active row set is vacuous and the source needs no motion. QED.

For a sufficiently small positive time, the straight realization p+t u
has all its previously unit pairs >1 and all its previously D-pairs <D.
Every inactive pair keeps its strict finite slack. Thus the entire
reduced source is unit-separated with diameter <D, provided it has at
least two points. Singletons have diameter zero and need no upper check.
No implicit-function theorem, PSD inference or finite pivot procedure
is required for this first step.

## 3. A transversal of the original normalized KKT polytope

Let P(A) be the original normalized nonnegative KKT polytope. For each
stress s let E_D(s) be its positive diameter support. A reduced source
A\U has a normalized KKT stress exactly when an original stress has
no positive contact or diameter edge incident to U: extend by zero at
deleted labels in one direction, and restrict in the other.

For the canonical C-II source every endpoint of H is an extreme vertex
of the source hull. At an extreme vertex with no positive diameter
reaction, any nonnegative contact equilibrium has zero contact
coefficients on all incident contacts. Indeed a strictly supporting
linear functional evaluates all vectors from that vertex to its
contact neighbors with the same strict sign; their nonnegative sum can
vanish only when every coefficient is zero. Thus if U consists of
loaded vertices, absence of positive diameter edges incident to U
already implies absence of positive contact edges incident to U.

Consequently define

    kappa_open(A)=min |U|, U subset loaded vertices,
       such that every normalized KKT stress has a positive diameter
       edge incident to U.

Every such U admits the straight strict motion in Section 2. It suffices
to test extreme points of P(A): if a stress vanishes on all incident
edges, every extreme point with positive coefficient in its convex
decomposition vanishes there as well. Conversely a missed extreme
point is itself a reduced-source stress.

The polytope is compact: the virial identity gives sum alpha=D^2 and
normalization gives sum beta=1. Hence its extreme-point description is
finite. Finiteness does not supply an efficient enumeration bound or
a useful geometric upper bound on kappa_open.

## 4. Comparison with the exact-contact cost

Let kappa(H,G) be the first-order strict-descent cost on the original
exact-contact tangent space from the
[residual-cage report](target_c_residual_cage_release_refill_2026-10-05.md).
If U admits that tangent direction, a normalized KKT stress on A\U
would pair its nonnegative surviving contact coefficients with zero
contact derivatives, and its positive diameter weights with strictly
negative derivatives. Equilibrium excludes this. Therefore

    kappa_open <= kappa(H,G) <= tau_*(H,G) <= s_Z+1.

The first inequality can be strict: signed contact coefficients are
allowed in dependencies of diameter rows restricted to the exact
contact tangent space, whereas a packing KKT obstruction requires
nonnegative contact coefficients.

There is also a second-order distinction. A singleton zero diameter
covector is a positive circuit and must be hit for *first-order* strict
descent. Its exact length can nevertheless decrease quadratically
along a nonzero contact path. Thus kappa(H,G) is a first-order sufficient
cost, not necessarily the minimum deletion cost for finite release.

For an exact abstract local regression, use a one-dimensional chart t
with active excesses

    ell_1(t)=t, ell_2(t)=-t, ell_3(t)=-t^2.

The differential rows are 1,-1,0, with full rank one and positive equal
weights satisfying stationarity. Their exact weighted identity is

    (ell_1+ell_2+ell_3)/3 = -t^2/3.

The full active cage remains locally sharp. If the three diameter edges
are disjoint, its positive-circuit transversal cost is two: one deletion
for the opposing pair and one for the zero row. But after deleting edge
2, taking t<0 shortens both surviving edges, including edge 3 quadratically.
One deletion suffices for finite release. This is a smooth abstract cage
with a nonnegative stress-energy identity; it is not a plane source,
unit-contact realization or global-minimizer example.

Any assertion that the covector positive-circuit cost is the exact
nonlinear deletion optimum must therefore add a nondegeneracy or
second-order argument. None was claimed in the preceding report.

## 5. Packet composition and the finite opening gap

A strict refill packet certified at the original source survives a
sufficiently small motion of A\U by its finite lower and upper margins.
Its surplus can pay |U| exactly as in the residual-cage proof. If it
becomes available only *after* a substantial contact-opening motion,
the present theorem gives no guarantee of reaching that state.

In particular the [noncontact-wall shield](target_c_noncontact_wall_shield_2026-10-05.md)
requires a fixed positive side-length increase before a pentagon can
gain a guarded site. The first inactive lower constraint may activate
before this threshold; all source-specific slacks and velocities must
be controlled. A finite active-set pivot can also encounter a new KKT
support on the reduced source. Neither the finite number of labelled
graphs nor a strict first step proves termination before such an event.

At the original canonical source the
[one-spare contact-minimality endpoint](target_c_one_spare_site_contact_minimality_endpoint_2026-10-05.md)
already excludes every strict packet with one spare site. The real use
of contact opening would therefore be a packet that is unavailable at
the original source and is certified only after an actual finite motion.

## 6. Classification and next obligation

| Claim | Classification | Scope |
| --- | --- | --- |
| Absence of reduced KKT stress gives strict straight descent | Proved candidate awaiting audit | Finite source with deleted labels |
| kappa_open<=kappa<=s_Z+1 | Proved candidate awaiting audit | Canonical source, first-order costs |
| Covector cost is nonlinear optimum | Rejected overstatement | Exact abstract quadratic regression |
| First descent guarantees a capacity-producing finite pivot | Unproved | Requires actual source slack control |

The next exact nonlocal obligation is to reach a finite reduced-source
state with a certified refill packet before the newly activated lower
constraints or a new KKT support block the required opening. The theorem
constructs the initial strict step, not the missing cardinality recovery.
No authoritative theorem state is edited.
