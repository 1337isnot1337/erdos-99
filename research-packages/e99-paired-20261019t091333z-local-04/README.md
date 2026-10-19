# One movable exterior guard row still gives zero insertion capacity

**Status:** unreviewed exact geometric regression and endpoint. No theorem
promotion is claimed. **Base:** `7d0a450fe66991036541023f95c44c064a04b6a8`.
**State / priority / catalogue:** `2026-10-15.publication.2` /
`public-frontier.3` / `public-frontier.9`. **Assignment:**
`c-mobile-guard-extra-row-paired-20261019`; refined scope key
`f02b31d636580a141fdc01bd`.

Prepared by OpenAI Codex (GPT-6 Luna xhigh), local-04. This agent derived the
guarded rectangular formulas and wrote the exact checker; no independent
mathematical audit has occurred. The note and checker are offered under
Apache-2.0. No third-party text or code is copied.

## Question and exact quantity

PR #126 moves a fully labelled rhombic grid coherently and proves zero
full-source strict-safe insertion capacity for that moving container. This
successor adds one exterior labelled row beyond PR #126's `j=m` boundary and
moves that guard row with every other row. The changed quantity is
\[
\mathcal C(A,K)=\{x\in K: |x-a|\ge1\text{ for every }a\in A\},
\]
the set of positions that could accept an additional label while the complete
source remains in place. A positive value would supply a site for a later
population-restoration step. The result below gives an exact obstruction for
this coherent one-row extension: `\mathcal C(A,K)=\varnothing` at every point
of the path, despite quadratic terminal Oler slack and retention of every
guard label.

The same path also gives a full-source, same-cardinality endpoint of strictly
smaller diameter for this family. Thus insertion capacity is not necessary for
that endpoint. The family is nonglobal and is not extracted from a canonical
C-II source.

## Exact all-size statement

For every integer `m>=7`, set
\[
d_m=m^2-6m-3,\qquad c_m=\frac{\sqrt{d_m}}{2m},\qquad
s_m=\frac{\sqrt3(m+1)}{2m},\qquad \theta_m=\arccos(c_m).
\]
Let `u=(1,0)`, `v_\theta=(cos(theta),sin(theta))`, and for
`theta_m<=theta<=pi/2` define
\[
A_{m,\theta}=\{iu+jv_\theta:0\le i\le m,\ 0\le j\le m+1\},
\qquad K_{m,\theta}=\operatorname{conv}(A_{m,\theta}).
\]
Rows `j=0,...,m` are PR #126's core grid; `j=m+1` is one exterior guard row.
All `(m+1)(m+2)` labels, including all `m+1` guard labels, follow the same
generator motion. The guard is included in the source's initial actual
diameter bound.

Throughout this continuous path:

1. Every distinct source pair stays at distance at least one. The exact
   unit-contact graph is the `(m+1)`-by-`(m+2)` rectangular grid, with
   `m(m+2)+(m+1)^2=2m^2+4m+1` contacts. It is bipartite and has no isolates.
2. The actual diameter is
   \[
   D_{m,\theta}^2=m^2+(m+1)^2+2m(m+1)\cos\theta
   \le D_{m,\theta_m}^2,
   \]
   where
   \[
   D_{m,\theta_m}^2=m^2+(m+1)^2+(m+1)\sqrt{d_m}.
   \]
   At `theta=pi/2`, `D^2=m^2+(m+1)^2`, strictly below the initial value by
   `(m+1)sqrt(d_m)`. The endpoint keeps every source and guard label.
3. The entire closed container is strictly covered by unit neighborhoods of
   source labels, so `\mathcal C(A_{m,\theta},K_{m,\theta})=\varnothing` for
   every angle, including the endpoint.
4. With area `Q=m(m+1)sin(theta)`, perimeter `p=4m+2`, and population
   `n=(m+1)(m+2)`, all-label Oler slack is
   \[
   S_{m,\theta}=\frac{2Q}{\sqrt3}+\frac p2+1-n
   =m(m+1)\left(\frac{2}{\sqrt3}\sin\theta-1\right).
   \]
   It increases from `S_{m,theta_m}=m+1` to
   `S_{m,pi/2}=(2/sqrt(3)-1)m(m+1)`, which is quadratic in the endpoint
   diameter.

This is an exact full-source obstruction to inferring a positive strict-safe
insertion site from this movable-guard architecture or from its Oler slack.
It is not an obstruction to arbitrary same-cardinality motion: the displayed
path itself gives a strictly sub-`D` endpoint for this nonglobal family.

## Proof

The identity
\[
d_m+3(m+1)^2=4m^2
\]
gives `c_m^2+s_m^2=1`. For `m>=7`, `0<c_m<1/2`. Write
`c=cos(theta)`, so `0<=c<=c_m<1/2` along the path. A source difference has
the form `a u+b v_theta` with `|a|<=m`, `|b|<=m+1`, and squared length
\[
|a u+b v_\theta|^2=a^2+b^2+2ab c.
\]
If one coordinate is zero, every nonzero difference has length at least one,
with equality only at a coordinate unit step. If `ab>0`, the squared length
is greater than one. If `ab<0`, put `r=|a|`, `t=|b|`; then
\[
|a u+b v_\theta|^2=(r-t)^2+2rt(1-c)
>(r-t)^2+rt\ge1.
\]
Thus the only contacts are coordinate steps. The grid's checkerboard parity
is a bipartition, and its exact edge count is the sum of its horizontal and
vertical edges.

The squared norm is convex in `(a,b)`, so its maximum on
`[-m,m]x[-(m+1),m+1]` is attained at a corner. Since `c>=0`, same-sign
corners attain the maximum, giving the displayed actual diameter. It is
monotone in `c`, which decreases as `theta` moves to `pi/2`; hence every
source pair stays under the initial actual-diameter bound. At `pi/2`, the
same source index set is a rectangular square-grid endpoint with identical
cardinality and unit separation, proving the strict diameter decrease.

Tile `K_{m,theta}` by its `m(m+1)` unit rhombi and split each along its
shorter diagonal `u-v_theta`. Each resulting triangle has circumradius `R`
with
\[
R^2=\frac{|u-v_\theta|^2}{4\sin^2\theta}
    =\frac{2-2c}{4(1-c^2)}=\frac{1}{2(1+c)}\le\frac12<1.
\]
For any point `x` in one such triangle with vertices `w_1,w_2,w_3`, write
its barycentric coordinates as `lambda_i`, and let `o` be the circumcenter.
The weighted square identity gives
\[
\sum_i\lambda_i|x-w_i|^2=R^2-|x-o|^2\le R^2.
\]
At least one vertex is therefore at distance at most `R<1` from `x`.
All vertices are source labels and the triangles cover the closed container,
including its boundary. This proves zero strict-safe capacity continuously,
not only at sampled points.

Finally, substituting `Q`, `p`, and `n` into the displayed Oler expression
gives the slack identity. Since `sin(theta)` increases on this interval, the
slack grows along the path. At the start,
`sin(theta_m)=sqrt(3)(m+1)/(2m)` gives `m+1`; at the endpoint it gives the
stated positive quadratic expression.

## Guard-cap interpretation and exact controls

Here `D_{m,theta_m}` is the actual diameter of the **guarded** source. If one
instead insists on keeping PR #126's unguarded source cap
`D_{PR126}^2=m^2(2+2c_m)`, the extra adjacent row is already inadmissible at
the starting angle:
\[
D_{m,theta_m}^2-D_{PR126}^2=2m+1+\sqrt{d_m}>0.
\]
Thus the guarded family cannot be silently assigned the old smaller cap.

`verify.py` uses only integer and quadratic-surd signs. For `m=7,8,12,24`,
it checks every possible grid difference vector at the initial angle, all
lower bounds and original-diameter upper bounds there, and all endpoint lower
bounds and original-diameter upper bounds. Translation invariance makes this
the full pair ledger for each sampled size. It checks the rectangular contact
count, population including the guard, exact diameter drop, slack identities,
and cover-radius bound. A negative control at cosine `3/4` gives
`|u-v|^2=1/2<1`, so extending the angle range past `cos(theta)=1/2` fails
unit separation. The universal path conclusions follow from the analytic
proof above; finite arithmetic is corroboration only.
The stop condition for this scoped pass is the all-size cover and pair-bound
proof plus these bounded exact controls; no canonical-source search follows
from this family alone.

## Predecessor comparison and limits

- **PR #126** ([source head
  `684429c4780f8a4491cc432ffa2733a31ff867eb`](https://github.com/1337isnot1337/erdos-99/pull/126))
  proves zero capacity along a coherent moving-wall path for the square
  `(m+1)`-by-`(m+1)` source. This note changes the labelled domain by one
  exterior row, keeps every added guard label through a rectangular
  same-cardinality endpoint, and gives its new diameter and population-slack
  formulas. The predecessor package was produced by OpenAI Codex (GPT-6 Luna
  xhigh), homelab-05; its source attribution is retained, and no code is
  copied here. Its five immutable package-file SHA-256 values were verified:
  `README.md` `86a42da1149d131c2808ff79304812b179c67d7074f14ffdf5011e6c703f3933`,
  `SOURCES.json` `de0971b6967c21d1e13c6183f67a07077ddedae7a0693c9afb912a8fa5d3ebf6`,
  `TASK.json` `30b63c5a681bb3fc1ecc891981b0ca3635cf6d22ee89959e13796eaf52a5b543`,
  `VERIFY.json` `5850a8a3d106a62442f039887a0692e2106fed2d9e6da7804a823674545dbb70`,
  `verify.py` `f4f1cb6ed06e8920d7e99f258e364386af04c01aa02f8dc99a59eaa567291ab0`.
- **PR #129** ([head
  `f4dc4c6ec3a6bb08097ca9a963336ae454e14229`](https://github.com/1337isnot1337/erdos-99/pull/129))
  studies fixed-wall collective-refill funding and a reduced 51-label opened
  endpoint. **PR #143** ([head
  `b6e60e8b0c8efa8675b143b1c10bdf2e1d5fe488`](https://github.com/1337isnot1337/erdos-99/pull/143))
  audits that exact scope. They do not include this one-row coherent motion
  or an endpoint retaining every guard label. PR #143's verdict is limited
  to its audited regression and ledger.
- The audited PR #97 predecessor is a fixed-wall square-grid capacity result
  with linear Oler slack. The current task card records a source-bound
  independent check as `agent-audited` at `beddec1de9620741f2a7baff8584afa0b2bd094f`,
  while the original report artifact remains unreviewed in the corpus. Audit.110
  is a canonical static exterior-packet barrier; it supplies no movable-core
  construction or interior capacity.
  Audit.188 exhibits a moved-core refill in a different nonglobal six-spoke
  family. This rhombic calculation is a separate, exact guard-row family and
  establishes no canonical source extraction.

All labels in the present family are retained, and the checker covers every
lower and upper pair class for its endpoint. There are no contact-isolated
labels in this grid. The result does not prove the guard geometry occurs in a
canonical minimizer, does not rule out nonuniform or multi-cell motions, and
does not close the macroscopic-container branch, C-II, or Level I. A strict
safe site is only one possible restoration mechanism; the displayed endpoint
uses direct motion instead.

## Open next question

- **Downstream decision and quantity:** can an actual canonical macroscopic
  container yield a full-source same-cardinality C-II endpoint? The quantity
  controlled here is strict-safe capacity in the convex hull of a moved source.
- **Changed hypothesis:** replace the full two-direction row coherence by an
  explicitly extracted nonuniform displacement of the wall and exterior
  guard row, while retaining every source label, including contact isolates.
- **Outcome:** positive capacity would supply one restoration site; a zero
  bound for the extracted class would require direct collective motion or a
  different architecture. Either result must check all lower and actual or
  inactive diameter upper pairs before it can affect the endpoint.
- **First step:** derive the guard displacement constraints from one actual
  canonical source and test their exact pair inequalities.
- **Blocker:** no theorem extracts this rectangular family or a nonuniform
  guarded motion from every sufficiently large C-II global minimizer.

Required repository-wide theorem-certificate replay is **deferred to the
merging agent**. This artifact does not claim full verification or independent
mathematical review.
