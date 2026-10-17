> Generated reading edition · [exact source](../../../docs/reports/target_c_near_geodesic_face_regression_2026-09-12.md) · source SHA-256 `98069d5ed9c48566da428db50e80d8fcc3ca985973f57e985bfd8acafc2e63ad`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-F6BE51D8D40B","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_near_geodesic_face_regression_2026-09-12.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=65d6d59a24ad878aced2ca105c0571d7b4831c7e; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — explicit near-geodesic face regression

**Date:** 2026-09-12  
**Repository commit:** `08039081de34f1b7afc6f9e84c0867d0b0cd50a0`  
**State version:** `2026-09-11.audit.34`  
**Run type:** Target C-II regression / Type-II interface-collapse audit  
**Classification:** regression; noncanonical  
**Certificate:** [`target_c_near_geodesic_face_regression_certificate.py`](../../../research/target_c_near_geodesic_face_regression_certificate.py)

## LEVEL I STATUS

`STILL OPEN`. This construction is not a global minimizer and does not close or
disprove C-II.

## 1. Exact construction

Put

```math
w={\sqrt{15}\over4},\qquad \delta={1\over2},
\qquad v=(\delta,w),
```

so `|v|=sqrt(19)/4>1`. Let `u_1,u_2` be the two unit vectors symmetric about
`v` whose sum is `v`. Explicitly,

```math
u_1=\left({1\over4}+{15\sqrt3\over8\sqrt{19}},
 {\sqrt{15}\over8}-{3\sqrt5\over4\sqrt{19}}\right),
```

```math
u_2=\left({1\over4}-{15\sqrt3\over8\sqrt{19}},
 {\sqrt{15}\over8}+{3\sqrt5\over4\sqrt{19}}\right).
```

For an integer `N`, take the two chains

```math
B_i=(i,0),\qquad T_i=(i+\delta,w),\qquad 0\le i\le N,
```

and add cap vertices

```math
R=B_N+u_1,\qquad L=T_0-u_1.
```

The convex polygon is traversed in the order

```math
B_0,B_1,\ldots,B_N,R,T_N,T_{N-1},\ldots,T_0,L.
```

Its boundary edges are the horizontal unit edges, followed by the four unit cap
edges `B_N R`, `R T_N`, `T_0 L`, and `L B_0`.

The turn signs are strictly positive: the edge directions occur in the order
`0`, `arg(u_1)`, `arg(u_2)`, `pi`, `arg(-u_1)`, `arg(-u_2)`, `2pi`. The exact
certificate checks the required signs algebraically.

## 2. Triangle-free face geometry

For a bottom/top pair,

```math
|B_i-T_j|^2=(i-j-\delta)^2+w^2
\ge {1\over4}+{15\over16}={19\over16}>1.
```

The cap coordinates have `u_{1x}>1/2`, so every cap-to-chain pair other than its
two designated boundary neighbors has horizontal separation greater than one.
The two cap vertices are also separated by more than one for `N\ge1`. Therefore
the only unit pairs are the boundary edges. The contact graph is a cycle, hence
triangle-free, and the polygon is an admissible local bounded face of a
triangle-free unit-contact graph.

This is a local face model, not a claim that an arbitrary surrounding contact graph
or KKT stress can be attached to it.

## 3. Linear area with zero inactive population

The parallelogram between the two long chains has area `wN`. The two cap triangles
have total area

```math
|u_1\times u_2|={3\sqrt{95}\over32}.
```

Thus

```math
\operatorname{area}(C_N)=wN+{3\sqrt{95}\over32}.
```

The horizontal span is `N+O(1)` and the vertical span is bounded, so
`diam(C_N)=N+O(1)`. With no source points in the face interior,

```math
{\operatorname{area}(C_N)-a_0 Z(C_N)\over\operatorname{diam}(C_N)}
\longrightarrow {\sqrt{15}\over4}
> {867\over5000}.
```

The limiting coefficient is substantially larger than the promoted
`C-TRAIN-INTERFACE-CURRENCY` Type-II floor.

## 4. Exact frontier effect

This regression falsifies the tempting implication

```text
linear train/face boundary currency
  -> o(D) inactive-chamber area/population deficit.
```

It also shows why the near-geodesic caveat in the promoted train-interface theorem
is substantive, not merely technical. A long convex face can carry linear area
currency while its boundary consists entirely of unit contacts and while its
interior contains no isolates at all.

The construction does **not** satisfy the whole Type-II normal form: it is not a
near-disk full-core source, and no positive KKT stress or global minimality is
claimed. Therefore it does not refute the remaining C-II closure target. It sharpens
that target:

> Any proof of `A_ch-a_0Z_ch=o(D)` must use the surrounding near-disk carrier,
> full-support response/KKT information, or a source-preserving strict diameter
> improvement. Face perimeter, convexity, triangle-freeness, and local unit-edge
> geometry are insufficient.

## 5. Computation

Run:

```sh
python3 research/target_c_near_geodesic_face_regression_certificate.py
```

The certificate uses exact SymPy radicals for the unit-edge, convexity, distance,
area, and rational-threshold checks. It does not certify a global embedding or
global optimality.
