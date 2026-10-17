> Generated reading edition · [exact source](../../../docs/reports/target_c_train_track_width_budget_2026-08-31.md) · source SHA-256 `5034ef8310b07e90c283eeb86aaa7e3011a3d3e868461e61ca2ae424cef0c3f9`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-8E979A7CE17B","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C78: train-track width budget

**Date:** 2026-08-31  
**Repository base:** `b8e60e7c` (main after C77 / PR #81)  
**Run type:** exact Euclidean-width / rhombic train-track theorem  
**Target:** Target C Gate C-II, C75/C77 near-capacity rhombic phase  
**Depends on:** C42, C75, C77  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

C77 turns every bounded quadrilateral contact face into one crossing of two global
rhombic train tracks. C78 adds metric information: a track cannot cross too many
rhombi because every crossing advances it by more than `sqrt(3)/2` in one fixed
normal direction, while the whole source has diameter `D`.

If `k_T` is the number of rhombi crossed by a train track `T`, then

```math
\boxed{k_T<\frac{2D}{\sqrt3}.}
```

Since C77 identifies `k_T=deg_Gamma(T)`, the train-track crossing graph has maximum
degree below `2D/sqrt(3)`.

Summing the width advance over all tracks gives the sharper global identity/inequality

```math
\boxed{
TD
>
\sqrt3 F_4+2c_{rh}\Sigma_{diag},
}
```

where `T` is the number of tracks, `F_4` the number of rhombic contact faces,
`Sigma_diag` the C75 total missing-short-diagonal slack, and

```math
c_{rh}=\frac{1-\sqrt3/2}{\sqrt2-1}.
```

Using the C77 endpoint budget `2T<=h+5Q` yields

```math
\boxed{
\sqrt3 F_4+2c_{rh}\Sigma_{diag}
<\frac D2(h+5Q).
}
```

Thus a near-capacity core necessarily has

```math
T\ge\frac\pi2D-O(1),
\qquad
h+5Q\ge\pi D-O(1).
```

This converts near-optimal packing capacity into a sharp linear amount of global
rhombic train-track/boundary complexity.

---

## 1. One crossing consumes normal width

Fix one C77 train track `T`. Orient its common unit transversal `u_T`, and let

```math
n_T:=Ju_T
```

point in the direction in which the track runs.

Suppose `T` crosses the consecutive rhombi

```math
f_1,\ldots,f_k.
```

Let `e_0,e_1,\ldots,e_k` be its consecutive tie edges, so `f_j` lies between the
opposite parallel unit edges `e_{j-1}` and `e_j`. Let `m_j` be the midpoint of `e_j`.

In a parallelogram, the vector between the midpoints of a pair of opposite sides is
exactly either one of the other side vectors. Hence

```math
|m_j-m_{j-1}|=1.
\tag{C78.1}
```

Let `phi_j in (pi/3,pi/2]` be the acute angle between the two train-track directions
crossing `f_j`. C77 gives the strict lower bound `phi_j>pi/3`.

By the orientation of `T`, the normal advance is positive and equals

```math
 n_T\cdot(m_j-m_{j-1})=\sin\phi_j>\frac{\sqrt3}{2}.
\tag{C78.2}
```

Summing along the track,

```math
 n_T\cdot(m_k-m_0)
=\sum_{j=1}^k\sin\phi_j
>\frac{\sqrt3}{2}k.
\tag{C78.3}
```

Both endpoint tie midpoints lie in the convex hull of source points, whose diameter is
`D`. Therefore

```math
|m_k-m_0|\le D,
```

and hence

### Theorem C78.1 — track crossing-degree bound

```math
\boxed{
 k_T<\frac{2D}{\sqrt3}.}
\tag{C78.4}
```

By C77, two tracks cross at most once and each rhombus on `T` is one crossing, so

```math
k_T=\deg_{\Gamma_R}(T).
```

Consequently

```math
\boxed{
\Delta(\Gamma_R)<\frac{2D}{\sqrt3}.}
\tag{C78.5}
```

This estimate uses only source diameter and strict unit separation.

---

## 2. Exact track-width sum

Define the normal span of a track by

```math
w_T:=n_T\cdot(m_k-m_0)>0.
\tag{C78.6}
```

Equation C78.3 is exact before the last inequality:

```math
\boxed{
w_T=\sum_{f\in T}\sin\phi_f.}
\tag{C78.7}
```

Every rhombic face belongs to exactly two train tracks. Its unit-side area is exactly

```math
\operatorname{area}(f)=\sin\phi_f.
```

Therefore summing C78.7 over all tracks gives the exact identity

### Lemma C78.2 — total track width equals twice rhombic area

```math
\boxed{
\sum_T w_T
=2\sum_{f\in F_4}\operatorname{area}(f).
}
\tag{C78.8}
```

Each `w_T<=D`, so

```math
\boxed{
2\sum_{f\in F_4}\operatorname{area}(f)\le TD.
}
\tag{C78.9}
```

The inequality can be strict because a train track need not span a full diameter.

---

## 3. Insert C75's missing-diagonal charge

For each rhombus `f`, C75 proves

```math
\operatorname{area}(f)
\ge
\frac{\sqrt3}{2}+c_{rh}(s_f-1),
\tag{C78.10}
```

where `s_f` is its short diagonal and

```math
c_{rh}:=\frac{1-\sqrt3/2}{\sqrt2-1}=0.32344\ldots .
```

Let

```math
\Sigma_{diag}:=\sum_{f\in F_4}(s_f-1).
```

Sum C78.10 and use C78.9:

### Theorem C78 — train-track width budget

```math
\boxed{
\sqrt3F_4+2c_{rh}\Sigma_{diag}
\le
2\sum_{f\in F_4}\operatorname{area}(f)
\le TD.
}
\tag{C78.11}
```

The first inequality is strict if all rhombi are strict and one uses the strict
concavity away from the chord endpoints, but the weak form above is the robust exact
statement needed later.

Equivalently,

```math
\boxed{
F_4
\le
\frac{TD}{\sqrt3}
-\frac{2c_{rh}}{\sqrt3}\Sigma_{diag}.
}
\tag{C78.12}
```

This is complementary to C77's Mantel bound `F_4<=T^2/4`: one is controlled by
pseudoline combinatorics, the other by Euclidean width.

---

## 4. Boundary form

C77 proves

```math
2T\le h+5Q,
\tag{C78.13}
```

where `h` is the outer contact-face walk and

```math
Q=\sum_{f\text{ bounded}}(k_f-4).
```

Combining C78.11 and C78.13 gives

### Corollary C78.3 — rhombic area consumes defect-boundary length

```math
\boxed{
\sqrt3F_4+2c_{rh}\Sigma_{diag}
\le
\frac D2(h+5Q).
}
\tag{C78.14}
```

Together with C42,

```math
F_4\ge m-5q+3c_I+3e_{BB}+5,
```

this gives the exact core inequality

```math
\boxed{
\sqrt3(m-5q+3c_I+3e_{BB}+5)
+2c_{rh}\Sigma_{diag}
\le
\frac D2(h+5Q).
}
\tag{C78.15}
```

C78.15 is weight-free.

---

## 5. Near-capacity consequence: at least pi D / 2 tracks

Assume a force-visible core sequence satisfies

```math
m\ge\Delta_2D^2-CD,
\qquad
\Delta_2=\frac\pi{2\sqrt3},
\tag{C78.16}
```

for a fixed constant `C`.

Since `q<=pi D`, C42 gives

```math
F_4
\ge
\Delta_2D^2-(C+5\pi)D+5.
\tag{C78.17}
```

Discard the favorable nonnegative slack term from C78.11. Then

```math
T\ge\frac{\sqrt3F_4}{D},
```

so

```math
\boxed{
T
\ge
\frac\pi2D-\sqrt3(C+5\pi)+O(D^{-1}).
}
\tag{C78.18}
```

Thus asymptotically

```math
\boxed{
\liminf\frac TD\ge\frac\pi2.
}
\tag{C78.19}
```

Since every track has two boundary ends, C77 then gives

```math
\boxed{
 h+5Q
\ge
\pi D-O(1).
}
\tag{C78.20}

```

A near-capacity rhombic core therefore requires essentially `pi D` rhombic-boundary
edge incidences, even before any extra penalty from C75 diagonal slack is counted.

---

## 6. Interpretation with C76

C76 says the exact mechanical star face is a single straight `D`-edge chain. C66-C74
show that the near-zero response phase converges toward that one-dimensional stress
certificate. C78 shows that a simultaneously near-capacity geometric core must contain
at least `(pi/2-o(1))D` distinct rhombic train tracks, each of normal span at most `D`,
and C77 says their crossing graph is triangle-free.

This makes the incompatibility quantitative in two separate currencies:

```text
stress limit:
    one almost-radial depth-D carrier;

geometry limit:
    >= (pi/2-o(1)) D global rhombic train tracks
    supporting Theta(D^2) triangle-free crossings.
```

The unresolved step is to make these currencies interact. A fixed KKT stress can
still put arbitrarily little weight on most of the transverse train tracks.

---

## 7. Next exact target

The most direct continuation is a train-track stability theorem.

1. Use C77 triangle-freeness plus C78's degree bound to isolate macroscopic families of
   tracks whose directions differ by `60+o(1)` degrees.
2. Use the fixed normal spans and the source diameter to bound the number of crossings
   such two-family systems can support inside a diameter-`D` set.
3. Charge any failure of the two-family model to track endpoints at nonquadrilateral
   defects, using C78.14.

A successful version with leading constant below `Delta_2` would close the
force-visible near-capacity branch independently of KKT weight lower bounds.

---

## 8. Regression audit

- A long square grid is consistent: a track can cross `Theta(D)` others, but never
  more than its normal width permits.
- A `60+o(1)` oblique grid nearly saturates the per-crossing lower width
  `sqrt(3)/2`; this is the binding local regression.
- The theorem does not assume train-track-convexity or a convex rhombic patch.
- Defect faces may terminate tracks and are retained explicitly through `h+5Q`.
- No KKT weight, reciprocal embedding, or force-bulk assumption is used.

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

C78:
For a train track T crossing k_T rhombi, consecutive tie-edge midpoints advance by
sin(phi_f)>sqrt(3)/2 in one fixed normal direction. Both endpoint midpoints lie in a
diameter-D hull, so
  k_T<2D/sqrt(3).
Thus Delta(Gamma_R)<2D/sqrt(3).

Exact track-width identity:
  sum_T w_T = 2 sum_(rhombi f) area(f),
with each w_T<=D. Using C75,
  sqrt(3) F_4 + 2 c_rh Sigma_diag <= T D.
Using C77, 2T<=h+5Q, hence
  sqrt(3) F_4 + 2 c_rh Sigma_diag <= D(h+5Q)/2.

If m>=Delta_2D^2-O(D), then C42 implies
  T >= (pi/2)D-O(1),
  h+5Q >= pi D-O(1).

Next: convert this many near-60-degree tracks into a two-family diameter loss or charge
track fragmentation to the defect boundary.
```
