# Target C-II — common FREE lower-run order/orientation parity sharpens the cycle-rank fork

**Date:** 2026-09-18  
**Status:** proved candidate awaiting promotion; graph-topological refinement of the common-lower-run branch  
**Scope:** `COMMON-LOWER-RUNS` after the ordered two-normal skeleton extraction  
**Dependencies:** ordered two-normal shared FREE skeleton; common FREE trunk/cycle-rank fork  
**Certificate:** `research/verify_target_c_tooth_reflection_common_lower_run_order_orientation_parity_2026_09_18.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The existing common-run theorem treats the two shared lower paths only as undirected paths. The ordered two-normal theorem carries one extra bit of structure on the selected common matching: the selected edges have one fixed relative traversal orientation (`SAME` or `OPPOSITE`) and one fixed ancestry-order parity (`SAME-ORDER` or `REVERSE-ORDER`). Those two bits cannot be chosen independently inside a connected component of the path intersection.

Let

\[
P:=R_i,\qquad Q:=R_j
\]

be the two simple all-lower paths from `COMMON-LOWER-RUNS`, and let

\[
\mathcal M:=Q^*_{ij}\subseteq E(P)\cap E(Q),\qquad q:=|\mathcal M|.
\]

The matching edges are pairwise vertex-disjoint. By the ordered-skeleton theorem, after the existing thinning there is one uniform relative traversal orientation

\[
\sigma\in\{\mathrm{SAME},\mathrm{OPPOSITE}\}
\]

and one uniform occurrence-order parity

\[
\tau\in\{\mathrm{SAME\!\!\!-ORDER},\mathrm{REVERSE\!\!\!-ORDER}\}.
\]

Identify `SAME` with `SAME-ORDER` and `OPPOSITE` with `REVERSE-ORDER`. Then exactly one of the following two parity regimes holds.

## PARITY-COMPATIBLE

\[
\boxed{\sigma=\tau.}
\tag{PC.1}
\]

A connected component of

\[
I:=P\cap Q
\]

may contain many selected matching edges. The existing balanced trunk/cycle-rank fork remains the correct general conclusion: for every `s>=1`, either one intersection component contains at least `s` selected edges, or

\[
\beta(P\cup Q)\ge q/s-1.
\tag{PC.2}
\]

Moreover, any multi-edge common trunk has its traversal type fixed:

- `SAME` + `SAME-ORDER`: both ancestries traverse the common trunk in the same direction;
- `OPPOSITE` + `REVERSE-ORDER`: the two ancestries traverse the common trunk in opposite directions.

This is the only regime in which a long common trunk can survive.

## PARITY-MISMATCH

\[
\boxed{\sigma\ne\tau.}
\tag{PC.3}
\]

Then no connected component of `I=P\cap Q` can contain two selected edges. Consequently

\[
\boxed{c(I)\ge q}
\tag{PC.4}
\]

and the exact two-path Euler-characteristic identity gives

\[
\boxed{
\beta(P\cup Q)=c(I)-1\ge q-1.
}
\tag{PC.5}
\]

Because `P\cup Q` is a connected plane subgraph of the common short-edge graph, it therefore has at least

\[
\boxed{q-1}
\tag{PC.6}

bounded faces.

This removes the square-root loss from half of the order/orientation cases. In the tuned small-external branch,

\[
q=\Omega\!\left({\kappa_DD^{1/4}\over Z_D+1}\right),
\]

so PARITY-MISMATCH yields directly

\[
\boxed{
\beta(P\cup Q)
=\Omega\!\left({\kappa_DD^{1/4}\over Z_D+1}\right),
}
\tag{PC.7}
\]

rather than only the balanced

\[
\Omega\!\left(
\sqrt{\kappa_D}\,{D^{1/8}\over\sqrt{Z_D+1}}
\right)
\]

scale. With the canonical small-external choice

\[
\kappa_D\ge\sqrt{Z_D+1},
\]

this gives

\[
\boxed{
\beta(P\cup Q)
=\Omega\!\left({D^{1/4}\over\sqrt{Z_D+1}}\right)
\to\infty
}
\tag{PC.8}
\]

under `Z_D=o(sqrt(D))`.

The metric information on every selected edge is unchanged:

\[
1<|e|\le1+{K\over D},
\]

and each selected edge is an exact lower gate in both separated FREE repairs.

---

## Proof of the parity obstruction

Every connected component `C` of `I=P\cap Q` is a path or an isolated vertex because `I` is a subgraph of each simple path. If `C` contains an edge, the restriction of `P` to `C` traverses the whole component in one of its two directions, and the restriction of `Q` does the same.

Therefore there are only two possibilities on a fixed edge-containing component `C`:

1. `P` and `Q` traverse `C` in the same direction. Then every common edge in `C` has relative traversal orientation `SAME`, and the occurrence order of any two common edges in `C` is the same in `P` and `Q`.
2. `P` and `Q` traverse `C` in opposite directions. Then every common edge in `C` has relative traversal orientation `OPPOSITE`, and the occurrence order of any two common edges in `C` is reversed between `P` and `Q`.

Hence, if one component contained two selected edges, the orientation bit and order bit of those two selected edges would necessarily agree. Under the global PARITY-MISMATCH hypothesis they do not agree. Thus each intersection component contains at most one selected edge, proving (PC.4).

Since `q>=1`, the paths share an edge and `H=P\cup Q` is connected. Euler-characteristic inclusion-exclusion for two paths gives

\[
\beta(H)=c(I)-1.
\]

Combining this with (PC.4) proves (PC.5). Planarity converts cycle rank into bounded-face count, proving (PC.6).

---

## Consequence for the current seam

The residual common-run obstruction now has only two forms:

1. **compatible parity:** a genuinely shared trunk may survive, and its traversal direction relative to the two module normals is known exactly;
2. **mismatched parity:** the full selected matching, not merely a square-root subfamily, is converted into planar cycle rank.

The next geometric attack should therefore use the known same-direction/opposite-direction support monotonicity on a compatible trunk, while any mismatched branch should be charged at the stronger `q-1` bounded-face scale.

C-II remains open. No theorem-state authority is changed.

**Disposition:** used the order/orientation data already carried by the two-normal skeleton to show that an incompatible parity class cannot place two selected gates in one common intersection component; this upgrades the cycle-rank branch from `sqrt(q)-1` to `q-1` in those cases.
