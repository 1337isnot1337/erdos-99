> Generated reading edition · [exact source](../../../docs/reports/target_c_force_visible_endpoint_count_2026-08-31.md) · source SHA-256 `fd7e71e01ed93adf9b4821627ef80ae0de4c7b278a1e9c35397c1e2f85b8a47d`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-8132E11ACCAC","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C34: fully force-visible sources have linearly many positive diameter endpoints

**Date:** 2026-08-31
**Repository state:** `b1bcefd` (`research/target-c-promote-c30-c32-2026-08-31`)
**Run type:** proof / C-II global counting reduction and dependency audit
**Target:** Target C-II
**Depends on:** canonical Lemma 5.2, canonical Theorem 12.2, promoted Target C12
positive-support connectivity, and promoted C26 loaded-or-barycenter dichotomy
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

This addendum proves a new count in the fully force-visible branch. It does not
contradict that branch, but it forces the positive diameter support to have linearly
many endpoints and edges as the source diameter grows.

Let `A` be a contact-minimal, diametrally saturated, triangle-free global minimizer
with diameter `D`, and assume

$$
C=C_*.
\tag{C34.1}
$$

For a relative-interior normalized KKT stress, let `B_+` be the endpoints of its
positive diameter support. Then

$$
\boxed{2|B_+|\ge \lceil D\rceil+2.}
\tag{C34.2}
$$

Consequently, if `H_+` is the positive diameter support,

$$
\boxed{|H_+|\ge \frac{\lceil D\rceil+2}{4}.}
\tag{C34.3}
$$

The conclusion is an exact finite inequality; no lower bound on an individual KKT
diameter multiplier is used.

## 1. Identifying the pin set

Choose a relative-interior point of the normalized KKT polytope. Since `C=C_*`,

$$
C_+=C.
\tag{C34.4}
$$

Let

- `A^\circ=V(C)` be the nonisolated contact core,
- `m=|A^\circ|`,
- `e=|C|`, and
- `Q^\circ` be the set of all source diameter endpoints that lie in `A^\circ`.

The inclusion

$$
B_+\subseteq Q^\circ
\tag{C34.5}
$$

is canonical Lemma 5.2: every endpoint of a positive diameter edge lies in the
vertex set of the positive contact support. Using (C34.4), that support is `C`, so
such an endpoint is in the contact core and is, of course, a source diameter
endpoint.

For the reverse inclusion, apply the promoted C26 loaded-or-strict-barycenter
dichotomy. A vertex incident to a contact but outside `B_+` is a strict convex
combination of its contact neighbors, hence is not an extreme point and cannot be a
source diameter endpoint. Every member of `Q^\circ` is incident to a contact, so

$$
Q^\circ\subseteq B_+.
\tag{C34.6}
$$

Therefore

$$
\boxed{Q^\circ=B_+.}
\tag{C34.7}
$$

This is the only point where C26 is needed: it identifies the canonical pinned set
in Theorem 12.2 with the KKT-visible diameter endpoint set.

## 2. The pinned-core lower bound

Canonical Theorem 12.2 applies to the contact-minimal triangle-free core with its
nonisolated diameter endpoints pinned. Hence

$$
e\ge 2\bigl(m-|Q^\circ|\bigr).
\tag{C34.8}
$$

Substituting (C34.7), and writing `q=|B_+|`, gives

$$
e\ge 2(m-q).
\tag{C34.9}
$$

This is a rank consequence of the zero pinned expansive cone in Theorem 12.2. It is
not a prestress-stability or stress-matrix assertion.

## 3. The same graph has large contact diameter

Promoted Target C12 says that the positive contact support of every normalized KKT
stress has exactly one nontrivial connected component and contains both endpoints of
every positive diameter edge. By (C34.4), the entire core graph `C` is therefore
connected and contains a contact pair at Euclidean distance `D`.

Let `\delta` be the graph diameter of `C`. Every contact edge has Euclidean length
one, so a contact path joining that pair has at least `D` edges. Since `\delta` is an
integer,

$$
\delta\ge \lceil D\rceil.
\tag{C34.10}
$$

The graph is triangle-free because it is a subgraph of the triangle-free unit-contact
graph. Eppstein's connected triangle-free penny-graph inequality, already imported in
the canonical theorem stack, gives

$$
e\le 2m-\delta-2
\le 2m-\lceil D\rceil-2.
\tag{C34.11}
$$

Combining (C34.9) and (C34.11),

$$
2m-2q\le 2m-\lceil D\rceil-2,
$$

and cancellation yields (C34.2). `\square`

## 4. Consequences for the force-visible branch

Every endpoint in `B_+` is incident to a positive diameter edge. Counting endpoint
incidences gives

$$
2|H_+|\ge |B_+|.
$$

Together with (C34.2), this proves (C34.3). Thus a fully force-visible survivor has
`Omega(D)` positive diameter edges, even if their positive weights are spread across
many edges and each individual weight is small.

The force hull `F=conv B_+` also has perimeter at least `|B_+|`: its consecutive
vertices are distinct unit-separated source points. Hence

$$
\operatorname{per}(F)\ge |B_+|\ge \frac{\lceil D\rceil+2}{2}.
\tag{C34.12}
$$

The existing upper bound `per(F)\le \pi D` is larger, so (C34.12) is a structural
count and not yet a contradiction.

## 5. C-II effect and audit boundaries

C34 strengthens the fully force-visible C-II normal form in a way orthogonal to the
bridge-stress split:

```text
C = C_*  ->  Q^circ = B_+
          ->  e >= 2(m-|B_+|)
          ->  e <= 2m-ceil(D)-2
          ->  2|B_+| >= ceil(D)+2.
```

It does not close C-II. In particular, it does not give a positive lower bound for
any individual `beta_h`, a density contradiction, or a PSD/Loewner comparison for a
Dirichlet response.

The hypotheses are essential:

- If `C\ne C_*`, the full contact graph need not equal the positive support, so C12
  cannot be applied to all contact edges and C26 need not identify `Q^\circ` with
  `B_+`.
- Contact-isolated weak diameter endpoints may remain outside `Q^\circ`; C34 counts
  only the diameter endpoints in the nonisolated core.
- The proof uses global contact-minimality through Theorem 12.2 and triangle-freeness
  through Eppstein's upper bound.

**Classification: proved C-II reduction, not Level I closure.** The exact endpoint
count is a new consequence of the promoted theorem stack. The remaining C-II task is
still to rule out a connected, fully force-visible, triangle-free full-diameter
network satisfying this count.
