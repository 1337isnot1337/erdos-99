<!-- theorem-state: {"artifact_id":"ART-5D828DC633AC","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C: a capped wall lock does not survive its packet's actual diameter

Date: 2026-10-06. Authority: `583203ac1dc1d7bc49f0ca0574d75e85f9de2ee1`,
state `2026-10-05.audit.62`. Classification: **proved candidate awaiting
independent audit**, conditional on the specified entire-source geometry;
**regression** for the two finite packets. C-II and Level I remain open.

The implication checked here is

`coupled train motion on the entire capped packet -> preserved contacts
and all finite source pairs -> strictly smaller actual global diameter`.

This preserves PR #722's pinned-wall lock at its original scope. It
rejects the extra inference that arbitrary fixed wall pins are the actual
diameter constraints of that feasible packet. It does not extend a packet
motion through an arbitrary retained source outside the packet.

## 1. The actual source class

Take unit vectors `u,v` with angle `phi` satisfying
`49/100<cos(phi)<1/2`, and all grid points

\[
 p_{ij}=iu+jv,\qquad0\le i,j\le M,\quad M\ge24.
\tag{1}
\]

Place disjoint regular unit pentagon caps on selected boundary unit edges
whose integer index `k` lies between 8 and `M-9`. The explicit cap
coordinates and optional outward unit leaves are those of PR #722's
`verify_target_c_pentagon_capped_lock_2026_10_05.py`, at research tip
`ed535f5a3a45e3921d91a29c38a0cb37f1d27921`.
They are reconstructed in the new self-contained verifier rather than
imported as theorem authority. Every cap/leaf point is at Euclidean
distance below three from its base midpoint. Its normal coordinate is
outward from that grid side.

For the offset bound, `0<c72<1/2`, `0<s72,s36<1`, and the cap height
`h=s72+s36<2`. The outer cap vertices have coordinates
`(plus/minus(1/2+c72),s72)` or `(0,h)` relative to the midpoint.
The side leaves have absolute tangential coordinate below two and
normal coordinate below `3/2`, so norm below `5/2`; the central normal
leaf has coordinate `(0,h+1)` of norm below three. The extra leaf has
absolute tangential coordinate below one and normal coordinate below
`5/2`, so norm below three as well. All these normals are positive.

Assume the **entire source** consists of these grid/cap/leaf points,
that it is unit-separated, and that its actual unit contacts are exactly
the listed grid-neighbor, cap-cycle and optional leaf contacts. This
hypothesis is certified directly in the two finite cases below. It is
not asserted for every parameter without those source checks.

## 2. A uniform geometric certificate for the actual diameter

Represent positions by their coefficients in the unit basis `u,v`. Let
`C=7/2`. Because `sin(phi)>sqrt(3)/2`, a cap/leaf offset of norm below
three has each basis coefficient bounded by `3/sin(phi)<C`.
Its base midpoint index is in `[8.5,M-8.5]`. Consequently every source
point belongs to one of these five closed coefficient boxes:

\[
\begin{array}{ll}
G:&[0,M]\times[0,M],\\
B:&[5,M-5]\times[-C,0],\\
T:&[5,M-5]\times[M,M+C],\\
L:&[-C,0]\times[5,M-5],\\
R:&[M,M+C]\times[5,M-5].
\end{array}
\tag{2}
\]

For coefficient difference `(a,b)`, the squared Euclidean distance is
`a^2+b^2+2c ab`, where `c=cos(phi)`. On any pair of boxes, its maximum
is attained at a pair of vertices. The verifier checks the following
stronger polynomial fact for all real `M>=24` and
`c in [49/100,1/2]`: every vertex-pair distance is strictly below

\[
 D^2=2(1+c)M^2,
\tag{3}
\]

except the two opposite grid corners `(0,0),(M,M)`, which attain it.

This is a certificate for an infinite parameter range, not an enumeration
of integer sizes. Each box vertex coordinate is affine in `M`. Subtract
(3), substitute `M=24+z`, and obtain a quadratic in `z`. All its
coefficients are affine in `c`. At both endpoints `c=49/100,1/2`, the
quadratic and linear coefficients are nonpositive and the constant
coefficient is strictly negative for every other vertex pair. There are
380 endpoint coefficient checks, including the two zero equality cases.
The signs prove the assertion for every `z>=0` and intermediate `c`.

Strict convexity of squared distance excludes nongrid-corner maximizers
inside the grid box. All pairs involving other boxes have strict margin
by the coefficient certificate. Thus the entire source's **unique actual
diameter pair** is `p_00,p_MM`.

## 3. Coupled finite motion

Rotate `u` clockwise through a small positive angle `epsilon`, keeping
`v` fixed. Reconstruct every grid point by (1). Horizontal caps and their
leaves rotate rigidly with their base vector and move with their grid
base; vertical caps keep their base direction and translate with their
grid base. All original contact lengths remain exactly one.

The cap equalities are elementary identities: in an orthonormal base
`w,n`, their edge components are `(1,0)`, `(c72,s72)`,
`(-c36,s36)`, `(-c36,-s36)`, `(c72,-s72)`, where

\[
 c72=(\sqrt5-1)/4,\quad c36=(\sqrt5+1)/4,
 \quad c72^2+s72^2=c36^2+s36^2=1.
\]

The optional leaves use unit components `(s72,c72)`, `(0,1)`,
`(-s72,c72)` and `(15/17,8/17)`. Reconstruction preserves these
identities, rather than merely enclosing their distances numerically.

Every initially inactive lower pair remains strictly above one for a
sufficiently small `epsilon`, since the source is finite and its listed
contact set is the full set of unit pairs. This radius is source-dependent.
Cardinality and triangle-free status are unchanged.

The new basis angle is `phi+epsilon`, still in the scope of (2)--(3)
for sufficiently small positive `epsilon`. Therefore its actual global
diameter satisfies

\[
 D(\epsilon)^2=2M^2(1+\cos(\phi+\epsilon))<D(0)^2.
\tag{4}
\]

Every old diameter is strictly shortened and every initially inactive
upper pair remains below the old `D`, because (4) is a full-source maximum
certificate. This is a non-repacking strict competitor, not a spare-site
or weighted-energy argument. Such an entire-source packet cannot be a
global diameter minimizer.

It also cannot admit a normalized KKT stress for its actual active rows:
the contact derivatives vanish, while the unique actual diameter's
squared derivative is `-2M^2 sin(phi)<0`. Differentiating a normalized
stationarity identity along this motion would give zero equal to a
strictly negative number. Positive equilibria under arbitrary extra wall
pins do not repair this failure.

## 4. Two full finite certificates

The source basis is `u=(1,0)` and
`v=Rot(2atan(t))(1/2,sqrt(3)/2)`, with `t=1/(200M^3)`. The target uses
`u'=Rot(-2atan(s))u`, with `s=1/(2000M^3)`, and the same `v`.
The directed rational arithmetic scale is `10^24`; square roots and every
operation are enclosed outward. Exact unit contact identities are proved
as above; interval containment of one is only a consistency check.

| Case | Points | Caps | Preserved contacts | Old pair checks | New pair checks |
| --- | ---: | ---: | ---: | ---: | ---: |
| `M=24`, ordinary caps | 649 | 8 | 1232 | 210276 | 210276 |
| `M=32`, caps with outward leaves | 1145 | 8 | 2176 | 654940 | 654940 |

All inactive lower distances have certified strictly positive margin;
each source's unique actual diameter pair is the two opposite grid
corners. Every target pair is certified strictly below the lower bound
on the old squared diameter, by at least `1/10000000`.

These are strict competitors for feasible nonglobal sources. They are
not Level I counterfamilies, actual canonical full-core disks, or a proof
that all loaded returns can move with the same construction. The pinned
wall's zero-refill-capacity statement remains a valid regression in its
declared fixed-wall scope.

## 5. What a canonical embedding must add

If such a patch is only a subconfiguration of a canonical source, the
motion must be completed through its retained contacts, bounded faces,
loaded endpoints and inactive pairs. None of those outside data is present
in the full-packet certificates. Holding arbitrary outside wall coordinates
fixed imposes constraints that cannot be substituted for actual old
diameter inequalities without a geometric theorem.

A canonical completion must block the demonstrated motion by a real
outside lower constraint/contact coupling or an actual upper obstruction.
If a non-Euclidean full-core contact-preserving infinitesimal completion
existed with every old diameter weakly shortening, it would contradict
canonical audit.56. This identifies the completion obligation; it does
not count or discharge its blockers.

The next source-level task is therefore an exact global coupled motion
or a source-specific physical obstruction payment. The common-angle
quadratic endpoint test supplies a check after such a global proposal
is constructed. The one-vertex wall shield supplies a separate finite
endpoint after an enlarged protected packet is certified. Neither theorem
currently extracts that proposal/packet from every canonical survivor.
