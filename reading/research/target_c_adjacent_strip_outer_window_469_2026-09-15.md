> Generated reading edition · [exact source](../../research/target_c_adjacent_strip_outer_window_469_2026-09-15.md) · source SHA-256 `568912393a5a2f3a6ec1b064a79d6d334547b722dc2b7c8fe4d3e4a66a795387`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 11 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "52fb88dd22d33e4bd9af42b033d735d31627ba74", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_adjacent_strip_outer_window_469_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "8d9d8a93fac7735d1970a3c199f0d1c225083bac62b8d295f3dccead9e982a9d"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — one live adjacent strip occupies fewer than `469` outer-walk edges

**Date:** 2026-09-15  
**Status:** proof-only source-level structural strengthening  
**Scope:** full-core Type-II branch with `t=(q-k)/D<=1.844`  
**Dependencies:** optimized OP543 good-leaf backbone; audited proper O--O crosscuts; Type-II outer-walk identity; matched `g=.007707` residual envelope; adjacent switching-order theorem  
**Certificate:** `research/verify_target_c_adjacent_strip_outer_window_469.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The optimized live backbone contains more than

```math
pD-o(D),\qquad p=0.00682246453482\ldots
```

pairwise disjoint smallest-leaf O--O crosscuts.  Consecutive crosscuts cut the occurrence-counted outer boundary into two middle arcs.  Along a simple path these middle arcs are disjoint from strip to strip.  The entire outer facial walk has only

```math
(\pi+\delta)D+o(D)
```

unit-edge occurrences.  Therefore one adjacent strip has total middle-boundary length less than

```math
\boxed{469+o(1).}
```

Every switching diameter has one endpoint in the middle layer, and every actual diameter endpoint is an outer-boundary extreme point.  Hence all middle endpoints of the switching graph lie inside the two corresponding outer-walk windows.  If both switch orientations occur, the hostile-audited one-arc theorem puts all of them in just one of the two windows.

This converts the remaining adjacent diameter interface from a globally placed finite set into a **fixed-radius boundary patch**.

---

## 1. Optimized backbone input

Use the proof-only OP543 backbone.  It gives a simple complement-dual path

```math
P=(\tau_1,\ldots,\tau_m)
```

of pairwise disjoint smallest-leaf O--O trains with

```math
\boxed{m>pD-o(D),}
\tag{OW.1}
```

where, exactly,

```math
\begin{aligned}
A&={1851\over2500},\\
W&={53\over625},\\
N_C&={1063\over1000},\\
\lambda&={1601\over2500},\\
d_{low}&={1\over10000},
\end{aligned}
```

```math
r={\lambda-d_{low}\over N_C},
\qquad
d_{top}=\lambda-(1-r)N_C,
```

```math
g={ (A-\lambda)W\over N_C-\lambda},
\qquad
\boxed{p={d_{top}g\over rN_C}.}
\tag{OW.2}
```

The exact companion certificate gives

```math
p=0.00682246453482\ldots>0.0068.
\tag{OW.3}
```

Only the path length (OW.1) is used below.  No switch-count, KKT-mass, or phase-gap threshold is spent.

---

## 2. Consecutive proper crosscuts partition the relevant boundary intervals

Use the audited outer-face disk augmentation in which every selected O--O train is represented by a proper crosscut.  The selected trains are pairwise disjoint, and their complement-dual edges form the simple path `P`.

For each internal index

```math
1\le i<m,
```

the two crosscuts `tau_i,tau_{i+1}` cut out one middle region `M_i`.  Its intersection with the boundary occurrence circle is the disjoint union of two open arcs; call them

```math
J_i^+,\qquad J_i^-.
```

Let

```math
G_i:=\operatorname{len}_{out}(J_i^+)+\operatorname{len}_{out}(J_i^-),
\tag{OW.4}
```

where length is measured along the occurrence-counted outer facial walk.  Since every outer contact-edge occurrence has Euclidean length one, this is the ordinary metric length of those boundary-walk portions, including the natural half-edge contributions at crosscut terminal midpoints.

### Lemma OW.1 — strip boundary arcs are occurrence-disjoint

The interiors of

```math
J_i^+,J_i^-
\qquad(1\le i<m)
```

are pairwise disjoint on the outer boundary occurrence circle.

### Proof

Cut the disk successively by the pairwise disjoint crosscuts in their path order.  The regions appear linearly:

```math
R_0,\ M_1,\ M_2,\ldots,\ M_{m-1},\ R_m.
```

Each boundary occurrence belongs to the boundary trace of exactly one of these open regions away from the crosscut endpoints.  The two arcs `J_i^+,J_i^-` are precisely the outer-boundary trace of `M_i`.  Distinct middle regions have disjoint interiors, so their open boundary traces cannot overlap.  Endpoint coincidences have zero metric length.  `square`

Let `b` be the total number of outer facial edge occurrences.  Lemma OW.1 gives the finite inequality

```math
\boxed{
\sum_{i=1}^{m-1}G_i\le b.
}
\tag{OW.5}
```

This is an occurrence statement.  It remains valid when the physical outer face repeats a bridge, because the two appearances are distinct boundary-circle occurrences.

---

## 3. The full outer walk has density `pi+delta`

Write

```math
\delta={d_{out}\over D}.
```

The audited distinguished-route/outer-walk identity gives

```math
{b\over D}=\pi+\delta+o(1).
\tag{OW.6}
```

Equivalently, in the notation where the total internal route-occurrence count is `x_B=b-q`,

```math
{x_B\over D}
=\pi+\delta-t-\kappa+o(1),
\qquad
{q\over D}=t+\kappa,
```

and adding the two equations yields (OW.6).

At `t<=1.844`, use the scope-safe matched constant

```math
C_{707}=2\sqrt{\pi\over2\sqrt3}+0.007707.
```

The residual envelope is

```math
2\delta+{\kappa\over2}+h
={9t\over2}-2\pi-C_{707},
\qquad \kappa,h\ge0.
\tag{OW.7}
```

Hence

```math
\delta
\le {1\over2}
\left({9(1.844)\over2}-2\pi-C_{707}\right)+o(1)
=0.0512410395\ldots+o(1).
\tag{OW.8}
```

Therefore

```math
\boxed{
{b\over D}<3.192833694+o(1).
}
\tag{OW.9}
```

---

## 4. Averaging forces one `<469` middle-boundary window

Combine (OW.1), (OW.5), and (OW.9).  Some internal boundary satisfies

```math
G_i
\le {b\over m-1}
< {\pi+\delta_{max}\over p}+o(1).
\tag{OW.10}
```

The exact verifier uses only `Fraction` arithmetic, Machin enclosures for `pi`, and integer-square-root radical bounds.  It proves

```math
\boxed{
{\pi+\delta_{max}\over p}
<467.989<469.
}
\tag{OW.11}
```

The exact margin to `469` is greater than one unit.  Thus

```math
\boxed{
G_i<469+o(1).
}
\tag{OW.12}
```

In particular, for all sufficiently large sources one may use the simple finite form

```math
G_i<470.
\tag{OW.13}
```

No assumption is made that the two constituent arcs have comparable length; each individually is at most their sum.

---

## 5. Every switching middle endpoint lies in the short windows

For the selected consecutive pair, let

```math
L,\ M,\ R
```

be the three layer regions of the adjacent switching theorem.  The two outer-boundary portions of `M` are exactly `J_i^+,J_i^-`.

The signed interval-support theorem says every switching diameter edge has exactly one endpoint in `M`:

- a left switch joins `L` to `M`;
- a right switch joins `M` to `R`.

Every endpoint of an actual diameter pair is an extreme point of the source convex hull and hence occurs on the actual outer boundary.  Therefore its middle endpoint belongs to

```math
J_i^+\cup J_i^-.
```

Consequently:

```math
\boxed{
\text{every switching middle endpoint lies in two outer-walk windows of total length }<469+o(1).
}
\tag{OW.14}
```

Measured along the outer walk, each such endpoint is within `469+o(1)` of one of the four terminal midpoint occurrences of `tau_i,tau_{i+1}`.  Euclidean distance is no larger than outer-walk distance, so the switching middle endpoints lie in the union of four fixed-radius Euclidean neighborhoods as well.

If both left- and right-switch edges occur, the hostile-audited adjacent switching-order theorem is stronger: all participating middle endpoints lie on one common middle arc.  Hence in that case

```math
\boxed{
\text{all switching middle endpoints lie in one outer-walk interval of length }<469+o(1).
}
\tag{OW.15}
```

---

## 6. Why this is new information

The existing OP543 theorem controls **how many** switching diameter rows one selected boundary can have.  The three-ray/strip-opening program controls **how many directions** are needed to witness local translation blockage.  Neither controls where the load-bearing diameter endpoints occur on the source.

Equations (OW.14)--(OW.15) add that missing geometric localization:

```text
linear live O-O backbone
+ disjoint proper crosscuts
+ only (pi+delta)D outer-walk length
-> one adjacent layer has O(1) outer-boundary width
-> every switching diameter endpoint inside that layer is in that O(1) patch
-> mixed left/right switching collapses to one O(1) boundary interval.
```

Since the full source convex hull is globally disk-like after diameter normalization, a fixed-length boundary patch has vanishing normalized diameter.  A downstream compactness theorem can therefore collapse all diameter directions incident to one such patch to one asymptotic direction.  That last directional-collapse statement is not used here and is intentionally separated for independent audit.

**Disposition:** proved proof-only fixed-window localization for one live adjacent strip. C-II and Level I remain open.
