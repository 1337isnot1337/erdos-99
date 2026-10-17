> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_d2_direction_saturation_2026-09-09.md) · source SHA-256 `4dd33f3596e934dee07a6251362fda065a2fc8a1a402a11ce358e668eb447bc5`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-65289DA7879E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic `d_H=2`: doubled-gap budget forces exact within-tree shell incidence

**Date:** 2026-09-09  
**Repository branch:** `research/post-zf-currency-coupling-2026-09-09`  
**Run type:** cross-route diameter-direction saturation  
**Target:** cyclic primitive endpoint, `d_H=2`  
**Depends on:** DP direction-defect theorem and D2 two-tree normal form on this branch; DG doubled spacing for vertex-disjoint diameter edges from PR #119  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

In the cyclic `d_H=2` phase, DP gives only `2/D+O(D^-2)` total projective diameter-direction excess above the universal shared-endpoint spacing quantum. DG says a consecutive pair of **vertex-disjoint** diameter edges costs twice that quantum.

Those two facts almost exhaust the direction budget by themselves: the two tree components must switch at least twice around the projective direction circle.

The resulting structure is exact for all sufficiently large `D`.

### Theorem D2S

Let

$$
H=T_A\sqcup T_B
$$

be the two diameter-tree components in the cyclic `d_H=2` phase, and order the `h=q-2` diameter edges by projective direction around `R/pi Z`.

Then for all sufficiently large `D`:

1. the directions of `T_A` form one consecutive block and the directions of `T_B` form the complementary consecutive block;
2. the only consecutive direction pairs that are vertex-disjoint are the two component-switch pairs;
3. every consecutive pair of edges inside one tree shares a terminal;
4. if
   $$
   e=zy,\qquad e'=zw
   $$
   are such consecutive within-tree edges with common endpoint `z`, then `y,w` are consecutive vertices of the unit contact shell;
5. consequently
   $$
   |y-w|=1
   $$
   and the projective direction gap is exactly
   $$
   \boxed{
   g(e,e')=\delta_D:=2\arcsin\frac1{2D}.
   }
   \tag{D2S.1}
   $$

Thus every within-tree direction transition is an exact local equality configuration: two diameter spokes at one endpoint and the unit shell edge joining their opposite endpoints.

Only the two transitions between the two trees can carry projective direction defect.

---

## 1. Total projective defect is only `2/D+O(D^-2)`

DP defines

$$
E_{dir}:=
\sum_{i=1}^h(g_i-\delta_D)
=
\pi-h\delta_D.
$$

Its exact cyclic asymptotic is

$$
E_{dir}=\frac{d_H}{D}+O(D^{-2}).
$$

In the present phase `d_H=2`, hence

$$
\boxed{
E_{dir}=\frac2D+O(D^{-2}).
}
\tag{1.1}

Also

\[
\delta_D
=\frac1D+O(D^{-3}).
\tag{1.2}

---

## 2. There are exactly two vertex-disjoint consecutive direction pairs

Let `m` be the number of cyclically consecutive direction pairs whose diameter edges are vertex-disjoint.

DG proves that such a pair has gap at least

\[
2\delta_D,
$$

whereas every consecutive pair has gap at least `delta_D`. Therefore

$$
E_{dir}
=\sum_i(g_i-\delta_D)
\ge m\delta_D.
\tag{2.1}

If `m>=3`, then by (1.1)-(1.2)

\[
\frac2D+O(D^{-2})
\ge
\frac3D+O(D^{-3}),
$$

impossible for large `D`. Thus

$$
m\le2.
\tag{2.2}

On the other hand both `T_A,T_B` contain edges. In the cyclic direction word over the two labels `A,B`, every change of label gives a vertex-disjoint consecutive pair, because the two tree components have disjoint vertex sets. A cyclic word containing both labels has at least two changes. Hence

\[
m\ge2.
\tag{2.3}

Therefore

\[
\boxed{m=2.}
\tag{2.4}

Exactly two label changes occur, so the A-edges form one direction interval and the B-edges form the complementary interval. This proves items 1-3 of D2S.

Moreover, after subtracting the two mandatory doubled-gap charges from (1.1), the total remaining excess is only

\[
\boxed{
\sum_{\substack{i:\ e_i,e_{i+1}\text{ in same tree}}}
(g_i-\delta_D)
=O(D^{-2}).
}
\tag{2.5}

Thus every individual within-tree gap satisfies

\[
0\le g_i-\delta_D=O(D^{-2}).
\tag{2.6}

---

## 3. Consecutive spokes have opposite endpoints at distance `1+O(1/D)`

Take a within-tree consecutive pair. By Section 2 it shares an endpoint; write

\[
e=zy,
\qquad
e'=zw,
\qquad
|z-y|=|z-w|=D.
$$

Let their projective angle be `g`. Since they are consecutive and `g=delta_D+O(D^-2)`, for large `D` this is their ordinary acute angle at `z`.

The chord formula gives

$$
|y-w|
=2D\sin\frac g2.
\tag{3.1}

By definition

\[
2D\sin\frac{\delta_D}{2}=1.
$$

Taylor expansion of (3.1) at `delta_D`, whose derivative is

$$
D\cos(\delta_D/2)=D+O(D^{-1}),
$$

together with (2.6), gives

$$
\boxed{|y-w|=1+O(D^{-1}).}
\tag{3.2}

Unit separation gives the lower bound `|y-w|>=1`, so the chord is asymptotically unit.

---

## 4. Circular-segment exclusion: no shell vertex can lie between `y,w`

All source points lie in the closed disk

\[
\overline B(z,D),
$$

because `D` is the source diameter. The endpoints `y,w` lie on its boundary.

Let `c=|y-w|`. By (3.2), `c=1+O(1/D)`.

The chord `yw` separates the convex shell into two boundary arcs. The arc not containing `z` lies on the side of the chord opposite `z`. Every point of that arc is therefore contained in the minor circular segment of `B(z,D)` cut off by `yw`.

The maximum distance of this segment from the chord is its sagitta

$$
s_D
=D-\sqrt{D^2-c^2/4}
=\frac{c^2}{8D}+O(D^{-3})
=O(D^{-1}).
\tag{4.1}

Suppose a third shell vertex `p` occurred strictly between `y,w` on this arc. Unit separation gives

\[
|p-y|\ge1,
\qquad
|p-w|\ge1.
\tag{4.2}

Every point in the minor segment projects orthogonally to the chord interval `yw`. For a point whose distances from both chord endpoints are at least one, the perpendicular distance from the chord is at least

\[
\sqrt{1-c^2/4}
=\frac{\sqrt3}{2}+O(D^{-1}).
\tag{4.3}

Indeed the minimum is attained at the intersection of the two unit circles centered at `y,w` on the segment side.

But (4.1) is `O(1/D)`, contradicting (4.3) for large `D`.

Hence no shell vertex lies between `y,w` on the boundary arc avoiding `z`.

Therefore `y,w` are consecutive vertices of the convex contact shell.

---

## 5. Consecutive shell vertices make the gap exact

The cyclic primitive contact graph is exactly the unit shell cycle. Consecutive shell vertices therefore satisfy

\[
|y-w|=1.
$$

Insert this into the chord formula (3.1):

$$
1=2D\sin\frac g2.
$$

Since `0<g<pi`,

$$
g=2\arcsin\frac1{2D}=\delta_D.
$$

This proves D2S.1 and items 4-5.

Thus (2.5) improves from an `O(D^-2)` aggregate statement to **exact zero defect on every within-tree transition**.

---

## 6. The two cross-tree gaps carry all projective defect

Let the two component-switch gaps be `G_1,G_2`. Every other gap equals `delta_D`, so

$$
\boxed{
G_1+G_2
=
\pi-(h-2)\delta_D.
}
\tag{6.1}

DG gives individually

\[
G_j\ge2\delta_D.
$$

Using `h=q-2` and RP/DP's cyclic perimeter expansion, their total excess above `4delta_D` is only lower order. DGE on PR #119 further says neither switch can attain `2delta_D` exactly: exact equality for two disjoint consecutive diameter edges would create an additional intermediate diameter direction. Hence the two positive strict switch defects exhaust the entire nonzero direction slack.

This isolates all non-Reinhardt geometry to two direction transitions.

---

## 7. Structural interpretation

D2 originally reduced the phase to two ordered caterpillars on four alternating terminal blocks. D2S adds a second, transverse ordering:

```text
projective diameter-direction circle:
    one contiguous T_A block
    one contiguous T_B block
    exactly two cross-tree transition gaps;

inside either block:
    consecutive diameter edges share a terminal;
    their opposite terminals are consecutive on the unit shell;
    the direction gap is exactly delta_D.
```

So each tree is assembled from exact local pieces of the regular/Reinhardt diameter-shell incidence pattern. The only places where that pattern can fail are the two A/B direction switches.

This is a much smaller finite target than an arbitrary pair of convex-thrackle caterpillars.

---

## 8. What remains

D2S does not yet classify how the common endpoint changes from one exact spoke pair to the next. Long star runs are still possible: a shell arc may consist of consecutive unit vertices all at diameter distance from one opposite terminal, as in a Reuleaux-type constant-width boundary. A sequence may also switch the shared endpoint along a caterpillar spine.

The next exact target is therefore a **center-switch classification**:

> classify a direction-ordered diameter tree in a convex unit shell for which every consecutive edge pair shares one endpoint and the two nonshared endpoints are consecutive shell vertices.

If every center switch forces an additional projective gap or a second local shell defect, D2S would collapse each tree to one star run. If center switches instead assemble a Reuleaux-polygon chain, combine that exact chain with the unique KKT transition parallelogram D2.2.

Either outcome is finite and exact; coefficient degeneration no longer enters this local classification.

---

## 9. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| exactly two disjoint consecutive direction pairs | proved for large `D` | DP defect budget + DG doubled gap + two tree labels |
| one contiguous direction block per tree | proved | exactly two cyclic label switches |
| every within-tree consecutive pair shares endpoint | proved | no remaining disjoint pair budget |
| within-tree gap `delta_D+O(D^-2)` | proved | remaining nonnegative defect budget |
| opposite partners are shell-consecutive | proved | thin minor circular segment versus unit separation |
| exact within-tree gap `delta_D` | proved | unit shell side + chord formula |
| cross gaps contain all direction defect | proved | all other gaps exact |
| center-switch classification | open | Reuleaux/star-run patterns remain |
| Level I | still open | two switch defects and KKT compatibility remain |
