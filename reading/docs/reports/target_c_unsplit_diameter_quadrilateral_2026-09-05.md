> Generated reading edition · [exact source](../../../docs/reports/target_c_unsplit_diameter_quadrilateral_2026-09-05.md) · source SHA-256 `bb6a0de0942f693a8e1289d64842b80a2a7db4e61127ca02ffc49ae0c28f5f35`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-78A69A7E7B3A","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C100: unsplit paired-diameter quadrilateral identities

**Date:** 2026-09-05  
**Repository base:** C99 branch after `8f9162c2`  
**Status:** LEVEL I STILL OPEN  
**Depends on:** C87 paired orientations, C98 unsplit-level rigidity

C98 shows that in the low-train branch all but at most `s+2` interior prefix levels are physically unsplit: there is exactly one selected source endpoint on each hull arc at that level. When a C87 prefix-tree edge joins two unsplit levels, its two required physical orientations are therefore forced onto the same four source points. Both crossing diagonals of that four-point quadrilateral are global diameters.

This note records the exact Euclidean consequences.

## 1. Setup

Let `i<j` be two interior C98-unsplit levels joined by one C87 prefix-tree edge. Denote the unique selected source endpoints at level `k` by

`L_k in L`, `U_k in U`.

C87's two orientations over `{i,j}` then include the diameter pairs

`L_i U_j` and `U_i L_j`.

Thus

`|L_i-U_j|=|U_i-L_j|=D`.

All four points are distinct, and every other mutual distance is at most `D` because `D` is the source diameter.

Define layer midpoints and transverse vectors

`m_k=(L_k+U_k)/2`,

`w_k=U_k-L_k`,

and put

`d=m_j-m_i`.

Then

`U_j-L_i = d+(w_i+w_j)/2`,

`L_j-U_i = d-(w_i+w_j)/2`.

## 2. Exact midpoint orthogonality

The two displayed vectors have equal norm `D`. Subtracting their squared norms gives

`2 d dot (w_i+w_j)=0`.

Hence

### Theorem C100.1

`boxed: d dot (w_i+w_j)=0.`

Adding the two squared-norm equations gives

### Theorem C100.2

`boxed: |d|^2 + |w_i+w_j|^2/4 = D^2.`

So the displacement of the two layer midpoints is exactly perpendicular to the sum of the two layer-transverse vectors, and their lengths satisfy a Pythagorean identity.

## 3. Acute transverse transport

The same-side vectors are

`L_j-L_i=d-(w_j-w_i)/2`,

`U_j-U_i=d+(w_j-w_i)/2`.

Both have norm at most `D`. Averaging their squared norms yields

`|d|^2+|w_j-w_i|^2/4 <= D^2`.

Comparing with C100.2 gives

`|w_j-w_i|^2 <= |w_j+w_i|^2`,

or equivalently

### Theorem C100.3 — acute transverse transport

`boxed: w_i dot w_j >= 0.`

Thus along every prefix-tree edge whose two levels are unsplit, the two physical `L-to-U` transverse vectors make an angle at most `90 degrees`.

Keeping the two same-side diameter inequalities separately and using C100.1 also gives

`boxed: |d dot (w_j-w_i)| <= w_i dot w_j.`

This is the exact asymmetric remainder hidden by the averaged inequality.

## 4. Ptolemy side-product lower bound

The cyclic quadrilateral is

`L_i, L_j, U_j, U_i`.

Its two diagonals are the selected diameter pairs and both have length `D`. Ptolemy's inequality for four Euclidean points gives

`D^2 <= |L_i-L_j| |U_i-U_j| + |L_i-U_i| |L_j-U_j|`.

Write

`A_ij=|L_i-L_j|`,

`B_ij=|U_i-U_j|`,

`W_k=|w_k|=|L_k-U_k|`.

Then

### Theorem C100.4 — paired-diameter Ptolemy budget

`boxed: A_ij B_ij + W_i W_j >= D^2.`

Consequently, for any `0<=lambda<1`, if

`W_i<=lambda D` and `W_j<=lambda D`,

then

`A_ij B_ij >= (1-lambda^2)D^2`.

Since each of `A_ij,B_ij` is at most `D`, this forces separately

`A_ij >= (1-lambda^2)D`,

`B_ij >= (1-lambda^2)D`.

Thus an unsplit edge has a strict geometric alternative: either one of its two layer widths is macroscopically large, or both same-arc endpoint chords are macroscopically close to diameter scale.

## 5. Unit-separation input

At every unsplit interior level, `L_k` and `U_k` are distinct source points, so

`1<=W_k<=D`.

Likewise all same-side endpoint pairs appearing above are distinct and hence have distance at least one.

These lower bounds are weak individually, but C100.4 makes them usable in aggregate once a bound is available on how many near-diameter chords can coexist on either hull arc.

## 6. Interaction with C98-C99

C98 forces at least

`D-s-3`

unsplit interior levels. C99 identifies the prefix tree with a monotone lattice path. Delete the at most `s+2` split interior vertices from that tree. Every surviving edge between unsplit levels obeys C100.1-C100.4.

Thus the remaining obstruction has been reduced to an explicit metric graph problem on a nearly spanning subforest of the C99 lattice-path tree:

- vertex variable: one transverse segment `w_k` joining the two hull arcs;
- edge condition: midpoint displacement perpendicular to `w_i+w_j`;
- edge norm identity: `|d|^2+|w_i+w_j|^2/4=D^2`;
- edge sign condition: `w_i dot w_j>=0`;
- edge Ptolemy budget: `A_ij B_ij+W_iW_j>=D^2`.

## 7. Frontier

C100 is not a contradiction. It supplies the missing metric content absent from the abstract caterpillar classification. The next target is a quantitative packing/container theorem for a long C99 path segment obeying these identities. A useful theorem would show that either

1. many `W_k` are `Omega(D)`, forcing excessive transverse hull width/area; or
2. many same-arc chords are near diameter, forcing a forbidden multi-diameter container by the same global area mechanism as C18.

Either conclusion would turn C98's `0.813799...D` unsplit levels into a global contradiction.
