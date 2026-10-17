> Generated reading edition · [exact source](../../research/target_c_high_t_tb1_thin_guard_gap_endpoint_trap_t18687_2026-09-17.md) · source SHA-256 `7895e32a5159930a7972311887e05a30b4cfa322ab45d4974d718acf9ef3baa8`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "62691ff3610516cc8bf32d29467553aa2d8a1c38", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_high_t_tb1_thin_guard_gap_endpoint_trap_t18687_2026-09-17.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "529622e6981bf9723c60b7be01424448ed77b896cacd3d16c4e65224b5181ed0"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II - homogeneous FENCE-UNIQUE THIN braid is trapped in two fixed guard gaps

**Date:** 2026-09-17  
**Status:** proof-only corollary of the asymmetric unique-grid normal form; no canonical promotion claimed  
**Scope:** GUARD/FENCE-UNIQUE sector of the THIN 15-spaced one-sign strong-TB1 Horn upper family through `t=(q-k)/D<=1.8687`  
**Dependencies:** asymmetric THIN unique-grid theorem; proper-crosscut train pseudosegment model; unit separation  
**Certificate:** `research/verify_target_c_high_t_tb1_thin_guard_gap_endpoint_trap_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The asymmetric unique-grid theorem leaves, in its GUARD-UNIQUE branch,

$$
\left({1\over24\log5}-o(1)\right)\sqrt{\log D}
$$

pairwise-crossing THIN chords with one identical exact incidence interval against

$$
2\sqrt{\log D}+o(\sqrt{\log D})
$$

ordered noncrossing train guards.  The endpoint-rank proof contains a stronger
conclusion which was not recorded there: after the orientation split, an identical
guard-incidence interval fixes the two endpoint **gaps** themselves.

Thus the surviving braid is a local two-window braid.  On each of the two complementary
boundary shores there is one fixed gap between consecutive guard endpoints, and every
surviving THIN chord has one endpoint in the first gap and one endpoint in the second.
The matching between those two windows is reversed, since every two THIN chords cross
properly.

This also covers the all-avoid case.  If the common guard-incidence interval is empty,
pairwise crossing plus monotonic endpoint ranks force every chord to use the same gap
rank on both shores.  The empty-incidence escape is therefore not a collection of
unrelated fence cells: the whole growing braid is trapped in one corresponding pair of
cells.

---

## 1. Rank notation

Use the GUARD-UNIQUE system from the asymmetric theorem.  Fix one common row and let
`P,Q` be its complementary outer-boundary shores.  Write the fixed guards in their
compatible noncrossing order as

$$
g_1,\ldots,g_m,
\qquad
m=(2+o(1))\sqrt{\log D}.
\tag{GT.1}
$$

Let their boundary endpoints be

$$
p_1,\ldots,p_m\in P,
\qquad
q_1,\ldots,q_m\in Q,
\tag{GT.2}
$$

in compatible orders.

For a THIN chord `e`, define the endpoint gap ranks

$$
\alpha(e)=\#\{j:p_j\text{ precedes }p(e)\},
\qquad
\beta(e)=\#\{j:q_j\text{ precedes }q(e)\}.
\tag{GT.3}
$$

The exact incidence theorem gives

$$
I(e)=
\{\min(\alpha,\beta)+1,\ldots,\max(\alpha,\beta)\}.
\tag{GT.4}
$$

Order the pairwise-crossing chords by their `P` endpoints.  Then

$$
\alpha_1\le\alpha_2\le\cdots,
\qquad
\beta_1\ge\beta_2\ge\cdots.
\tag{GT.5}
$$

The asymmetric theorem retained one orientation class, either

$$
\alpha_i\le\beta_i\quad\forall i
\tag{GT.6}
$$

or

$$
\alpha_i>\beta_i\quad\forall i.
\tag{GT.7}
$$

It then retained a sub-braid `H_D` on which `I(e)` is one fixed set `I_*`.

---

## 2. A nonempty common interval fixes both gap ranks

Assume first that

$$
I_*=\{a+1,a+2,\ldots,b\}
\tag{GT.8}
$$

is nonempty, so `0<=a<b<=m`.

In orientation (GT.6), (GT.4) reads

$$
I(e)=\{\alpha(e)+1,\ldots,\beta(e)\}.
$$

Equality with (GT.8) therefore forces

$$
\boxed{
\alpha(e)=a,
\qquad
\beta(e)=b
\quad(e\in H_D).
}
\tag{GT.9}

In orientation (GT.7), the same argument gives

\[
\boxed{
\alpha(e)=b,
\qquad
\beta(e)=a
\quad(e\in H_D).
}
\tag{GT.10}

Thus a nonempty homogeneous incidence interval fixes both endpoint gaps exactly, not
only the set of crossed guards.

---

## 3. The empty-incidence case also has one fixed gap

Suppose now

\[
I_*=\varnothing.
\tag{GT.11}
$$

Equation (GT.4) gives

$$
\alpha_i=\beta_i
\quad\text{for every retained chord.}
\tag{GT.12}
$$

Together with (GT.5),

$$
\alpha_1\le\alpha_2\le\cdots
\quad\text{and}\quad
\alpha_1\ge\alpha_2\ge\cdots.
$$

Hence

$$
\boxed{
\alpha_1=\cdots=\alpha_h
=\beta_1=\cdots=\beta_h=:a.
}
\tag{GT.13}

So even when every selected chord avoids every fixed guard, all chord endpoints lie in
the same rank-`a` guard gap on `P` and the corresponding rank-`a` gap on `Q`.

---

## 4. Two fixed boundary windows contain the whole homogeneous braid

For `0<=a<=m`, let `W_P(a)` be the open boundary interval on `P` between the `a`th and
`(a+1)`st guard endpoints, with the obvious boundary-end conventions at `a=0,m`.
Define `W_Q(b)` analogously.

Sections 2--3 prove that there are fixed ranks `a,b` such that every chord in `H_D`
has

\[
\boxed{
p(e)\in W_P(a),
\qquad
q(e)\in W_Q(b).}
\tag{GT.14}

Moreover

\[
I_*=\{\min(a,b)+1,\ldots,\max(a,b)\}.
\tag{GT.15}

The endpoint windows are therefore source-level objects determined by two consecutive
members of the fixed train fence.  They do not depend on the chord.

Every two chords of `H_D` cross properly and the matching is vertex-disjoint.  Hence
the `P` endpoints are all distinct, the `Q` endpoints are all distinct, and their
orders are reversed in the compatible shore coordinates.

The size from the asymmetric theorem is

\[
\boxed{
|H_D|\ge
\left({1\over24\log5}-o(1)\right)\sqrt{\log D}.
}
\tag{GT.16}

Thus the FENCE-UNIQUE branch contains a growing reversed matching between two fixed
fence cells.

---

## 5. Unit separation forces both windows to have growing boundary length

All endpoints of THIN chords are source vertices on the convex hull.  Order the
`|H_D|` selected source vertices inside `W_P(a)` along the hull.  Between two
consecutive selected vertices, the hull subarc has Euclidean arclength at least their
straight-line distance, which is at least one by source separation.  The selected
subarcs are internally disjoint, so

\[
\operatorname{len} W_P(a)\ge |H_D|-1.
\tag{GT.17}
$$

The same argument on `Q` gives

$$
\operatorname{len} W_Q(b)\ge |H_D|-1.
\tag{GT.18}
$$

Consequently

\[
\boxed{
\operatorname{len}W_P(a),\operatorname{len}W_Q(b)
\ge
\left({1\over24\log5}-o(1)\right)\sqrt{\log D}.
}
\tag{GT.19}

This lower bound is not yet contradictory: the outer boundary has `Theta(D)` scale.
Its value is structural.  Any future attempt to close FENCE-UNIQUE may now work with
one fixed pair of train-defined boundary windows rather than a moving incidence word.

---

## 6. Frontier effect

The GUARD/FENCE-UNIQUE escape is now

```text
sqrt(log D) pairwise-crossing, vertex-disjoint THIN almost-diameters;
2 sqrt(log D) ordered noncrossing fixed train guards;
one exact consecutive guard interval I_* crossed once by every chord;
one fixed P-shore guard gap containing every P endpoint;
one fixed Q-shore guard gap containing every Q endpoint;
reversed endpoint matching between those two windows;
D^(1/2-o(1)) common inverse-D phase rows;
and a D^(1/2-o(1))-long consecutive selected-row block topologically crossed by
all selected chords and all fixed guards.
```

If `I_*` is empty, the two windows have the same guard-gap rank.  If it is nonempty,
its two endpoint ranks are exactly the endpoints of `I_*`.

The missing closure statement is now metric: use the near-diameter condition and the
near-equilateral train scaffold to bound the possible geometry of a reversed
near-diameter matching whose two endpoint populations are trapped in one fixed pair of
train-defined boundary windows.  No such bound is proved here.

**Disposition:** upgraded homogeneous FENCE-UNIQUE incidence to exact two-window
endpoint localization; C-II and Level I remain open.
