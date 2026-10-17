> Generated reading edition · [exact source](../../research/target_c_attachment_route_signed_return_2026-09-12.md) · source SHA-256 `fdb8f58f12442b75ea4294f062c1b05cf6c5f0e2dee0ade25d155116bb6ddd03`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target C-II: attachment-route signed return

**Date:** 2026-09-12  
**Status:** audited-working, proof-only; canonical theorem state unchanged  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This note records a source-level refinement of the signed-return currency.  For one
harmonic carrier, cut the occurrence-counted outer walk at every consecutive
attachment vertex instead of retaining only a diameter pair.  The resulting excess is
measured above the actual attachment-polygon perimeter.

Let `A={p_1,...,p_a}` be the attachment occurrences in cyclic order, `P=conv(A)`,
`d=diam(P)`, and let `L` be the occurrence-counted outer-face walk length.  Write
`P_exc` for the total degree of bounded nonquadrilateral face occurrences.  For the
outer route `W_i:p_i\to p_{i+1}`, put

$$
\ell_i=|W_i|,\qquad z_i=p_{i+1}-p_i,\qquad q_i=z_i/|z_i|.
$$

The inherited Section-101 route partition gives

$$
\sum_i\ell_i=L,\qquad \sum_i|z_i|=\operatorname{per}(P).
$$

Give each bounded nonquadrilateral face its clockwise closed route and host `0`, and
set

$$
Q_{att}=\{q_1,\ldots,q_a,0\},\qquad
w_{Q_{att}}(u)=\max_{q\in Q_{att}}q\cdot u-\min_{q\in Q_{att}}q\cdot u.
$$

Define the exact attachment-route excess

$$
E_{att}=L+P_{exc}-\operatorname{per}(P).
\tag{AR.1}
$$

For the complete strict-rhombus trains `\mathcal T`, with terminal direction `u_\tau`,

$$
\boxed{E_{att}\ge\sum_{\tau\in\mathcal T}
       \bigl(2-w_{Q_{att}}(u_\tau)\bigr).}
\tag{AR.2}
$$

If `\mathcal R` is the strict-rhombus complex and `u_R,v_R` are the two train
directions through `R`, exact train-span transport gives

$$
\boxed{dE_{att}\ge\sum_{R\in\mathcal R}\operatorname{area}(R)
       \bigl[4-w_{Q_{att}}(u_R)-w_{Q_{att}}(v_R)\bigr].}
\tag{AR.3}
$$

The face ledger (`L+Q=4a-6-2s-2c` and `P_exc=4f_exc+Q`) also gives the finite identity

$$
\boxed{E_{att}=4a-6-2s-2c+4f_{exc}-\operatorname{per}(P).}
\tag{AR.4}
$$

## Proof and scope

For a directed unit-edge route of displacement `z`, with `q=z/|z|` (and `q=0` for a
closed route),

$$
|W|-|z|=\sum_{e\in W}(1-q\cdot v_e)\ge0.
$$

Summing over all attachment routes and defect-face cycles gives (AR.1).  A physical
train end is incident either with one outer-face occurrence or with one bounded
nonquadrilateral-face occurrence, so assign it to that occurrence.  The assignment is
injective on physical edge occurrences; repeated bridge traversals not incident with a
retained rhombus remain unassigned nonnegative terms.  Hole boundaries and
disconnected rhombus components are included by the same occurrence ledger.

The two terminal orientations of a train are `u` and `-u`.  If their assigned hosts are
`q_i,q_j`, their contribution is

$$
(1-q_i\cdot u)+(1-q_j\cdot(-u))
 =2-(q_i-q_j)\cdot u\ge2-w_{Q_{att}}(u),
$$

which proves (AR.2) after summing.  The span of a complete train equals its total
transverse rhombus area; both terminal midpoints lie in `P`, hence that span is at most
`d`.  Each rhombus lies on exactly two trains, yielding (AR.3).  Substitution of the
face identities proves (AR.4).

This is a finite geometric inequality on the actual source.  It retains
contact-isolated source points and makes no full-source affine-kernel claim.  It does
not provide a positive universal lower bound: the host set contains all attachment
chord directions, so the widths can approach `2`.  The remaining C-II obligation is a
source-specific capacity or diameter-descent theorem that compares the weighted right
side of (AR.3) with the exact left side (AR.4).  No canonical state or Level-I claim
is changed here.
