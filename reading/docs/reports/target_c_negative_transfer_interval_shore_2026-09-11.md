> Generated reading edition · [exact source](../../../docs/reports/target_c_negative_transfer_interval_shore_2026-09-11.md) · source SHA-256 `7467ecc36eb4680af8d6d017e86bd8e519901c2c6ac67d3c619e096fa29c1a33`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-444FC3F188C8","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdos Problem #99 - strict-negative transfer has a small terminal shore

**Date:** 2026-09-11
**Target:** Target C, C-II strict-negative transfer branch
**Status:** STILL OPEN; hold report
**Dependencies:** the promoted C53 circular-interval split representation and the
straight-line diameter-thrackle property

## Result

Let (H) be the actual loaded diameter graph in the C-II representative, and let

$$
K=Q^{\mathsf T}\Lambda^+Q.
$$

Order the diameter edges in the legal C53 projective order.  If

$$
c:=K_{0,m-1}<0,
$$

then some positive circular-interval split (A|A^c) has a signed split vector (z_A)
with

$$
z_{A,0}z_{A,m-1}=-1.
$$

If (k_A=|\operatorname{supp}z_A|) is its number of crossing diameter edges, then one
of the two terminal shores contains no internal diameter edge and has at most (k_A)
loaded terminals.  In particular, a negative-transfer split with (k_A=2) cuts off a
terminal interval of size at most two, and (k_A=1) cuts off a single terminal.

This is a graph-geometric localization of the strict-negative branch.  It does not
close that branch: the split coefficients can be arbitrarily small, and a split with
large (k_A) need not have a bounded terminal shore.

## Proof

The circular-planar resistance split representation gives

$$
K=\sum_A\lambda_A z_Az_A^{\mathsf T},
\qquad \lambda_A\ge0,
$$

where (A) ranges over nonempty proper circular intervals of the loaded terminal
order.  Hence

$$
K_{0,m-1}=\sum_A\lambda_Az_{A,0}z_{A,m-1}.
$$

If this number is negative, at least one term with (lambda_A>0) has

$$
z_{A,0}z_{A,m-1}<0.
$$

Because split-vector entries are in ({-1,0,1}), this product is (-1), and both
diameter edges (e_0,e_{m-1}) cross (A|A^c).  Put

$$
k_A=|\{e\in H:e\text{ has one endpoint in }A	ext{ and one in }A^c\}|.
$$

Then (k_A=|\operatorname{supp}z_A|).

We next use only the straight-line thrackle property.  Suppose that (H[A]) and
(H[A^c]) both contained edges (g) and (h).  The four endpoints of (g) and
(h) lie in two disjoint cyclic intervals of the strictly convex terminal polygon.
The corresponding straight chords are disjoint and do not cross.  They also have no
common endpoint, contradicting that every two diameter edges meet.  Therefore at least
one shore, say (A), has no internal diameter edge.

Every terminal in (A) is incident with an actual diameter edge, by the definition of
the loaded set.  Since (H[A]) is empty, every incident diameter edge crosses the cut.
Each crossing edge has exactly one endpoint in (A), so

$$
|A|
\le \sum_{v\in A}\deg_H(v)
=k_A.
$$

This proves the claimed small-shore bound.  The final special cases follow by putting
(k_A=2) or (1).  $\square$

## Exact effect on C-II

The theorem supplies the following honest branch split:

```text
strict-negative transfer
    -> a positive circular split with opposite signs on the extreme transfer pair
    -> one split shore has at most as many loaded terminals as its crossing H-edge count.
```

It does not imply that (k_A) is bounded.  It also does not turn a circular split
coefficient into a physical contact cut: a positive Kalmanson split is a response
decomposition term, not necessarily a one- or two-edge cut in the contact graph.
Therefore the degree caps C26/C35 cannot be applied to the split shore without an
additional response-to-contact separator theorem.

The weighted four-cycle common-block regression remains compatible with this result.
It realizes a negative transfer through a two-edge terminal split while having no
contact bridge, so the single-bridge maximum-principle argument cannot be reused.

## What would be decisive

Any one of the following would turn this lemma into a closing step:

1. a uniform bound (k_A=O(1)) for a negative split of nonnegligible coefficient;
2. a theorem converting a (k_A)-terminal response split into a contact cut with at
   most (k_A) boundary ports, followed by the C35 degree/circuit charge; or
3. a lower bound on the negative split mass together with a summable forest/circuit
   cost for the crossing diameter edges.

None of these implications is established here.  In particular, the theorem is not a
global-optimality certificate and leaves the cyclic, forest, and (s_Z>0) ledgers
open.
