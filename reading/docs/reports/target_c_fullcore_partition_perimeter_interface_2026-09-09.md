> Generated reading edition · [exact source](../../../docs/reports/target_c_fullcore_partition_perimeter_interface_2026-09-09.md) · source SHA-256 `6559b0680334e5d6adc54d7749379a68dcb33475e98c4de88999f091e16b3fbf`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Presentation repairs: 1 exact-source-bound TeX/escape correction(s); [reviewed repair ledger](../../../docs/publication/reading-tex-repairs.json). Frozen source bytes are unchanged.

<!-- theorem-state: {"artifact_id":"ART-A8427449EF5D","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_fullcore_partition_perimeter_interface_2026-09-09.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=241144d9da2c78fb4ec554f8047a421d3571693e; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — full-core partition perimeter forces two diameter units of loaded-interface defect

**Date:** 2026-09-09  
**Repository branch:** `research/post-uf-attachment-fill-2026-09-09`  
**Run type:** full-core near-circle perimeter/ledger theorem  
**Target:** remove the cap-minimal hypothesis from LI  
**Depends on:** HG, C36/C44/C49, finite Oler, NC, HBd, NBd, local component Euler identity  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

The earlier LI theorem proved

```math
Q_B\ge(2-o(1))D
```

only in the cap-minimal full-core subbranch `S/D->2`.  The cap-minimal assumption is unnecessary.

Let

- `I_r` be the unloaded harmonic components;
- `K_r=conv(I_r)`;
- `k_r` be the outer-face walk length of `C[I_r]`;
- `Q_r` be its bounded-face degree excess;
- `K_I=sum_r k_r`;
- `Q_I=sum_r Q_r`;
- `Q_B=Q-Q_I` be the bounded-face degree excess on faces incident to at least one loaded terminal;
- `S=sum_r delta_r` and `R_I=sum_r r_r`;
- `s_B` be the unused loaded contact-degree slack.

Then every full-core near-circle sequence satisfies

```math
\boxed{
K_I\ge(\pi+2-o(1))D,
}
\tag{FP.1}
```

and hence

```math
\boxed{
S+R_I\ge\left(1+\frac\pi2-o(1)\right)D.
}
\tag{FP.2}
```

More sharply, the exact near-circle ledgers give the asymptotic identity

```math
\boxed{
Q_B=K_I-\pi D+2s_B+o(D).
}
\tag{FP.3}
```

Therefore

```math
\boxed{
Q_B\ge(2-o(1))D+2s_B.
}
\tag{FP.4}
```

In particular

```math
\boxed{Q_B\ge(2-o(1))D}
\tag{FP.5}
```

throughout the entire full-core near-circle branch, with no assumption that `S/D->2`.

This supersedes LI's cap-minimal scope.  The new proof identifies the geometric origin of the constant two: it is the unavoidable internal partition perimeter of the two half-disk harmonic groups.

---

## 1. Component hulls have only linear total perimeter

C36 and C44 give

```math
K_r\subseteq P_r,
\qquad
\operatorname{diam}K_r\le\operatorname{diam}P_r\le\delta_r+2.
```

For every planar convex body, perimeter is at most `pi` times diameter.  Therefore

```math
\operatorname{per}(K_r)\le\pi(\delta_r+2).
```

Summing and using the post-ZF bounds `S=O(D)` and HBd's `c_I=o(D)` gives

```math
\boxed{
\sum_r\operatorname{per}(K_r)=O(D).
}
\tag{1.1}
```

This makes the perimeter term in componentwise Oler only boundary-order.

---

## 2. The component hulls themselves fill the two semicircle groups

HG proves that the attachment-cell decomposition has two dominant groups `G_1,G_2`, each contained asymptotically in one of two complementary diameter-`D` semicircular caps and each carrying

```math
N_i:=\sum_{r\in G_i}n_r
=(\Delta/2+o(1))D^2,
\qquad
\Delta=\frac\pi{2\sqrt3}.
\tag{2.1}
```

Apply Oler to the `n_r` unit-separated vertices of `I_r` inside their own convex hull `K_r`:

```math
\frac{\sqrt3}{2}(n_r-1)
\le
\operatorname{area}(K_r)
+\frac{\sqrt3}{4}\operatorname{per}(K_r).
\tag{2.2}
```

Sum over one dominant group.  By (1.1) the total perimeter term is `O(D)=o(D^2)`, and HBd gives only `o(D)` components, so the `-1` terms are also `o(D^2)`.  Thus

```math
\sum_{r\in G_i}\operatorname{area}(K_r)
\ge
\frac{\sqrt3}{2}N_i-o(D^2)
=
\left(\frac\pi8-o(1)\right)D^2.
\tag{2.3}
```

But `K_r subset P_r`, the cell interiors are pairwise disjoint by C49, and HG puts the whole group inside one semicircular cap of area `(pi/8+o(1))D^2`.  Hence equality holds at leading order:

```math
\boxed{
\sum_{r\in G_i}\operatorname{area}(K_r)
=
\left(\frac\pi8+o(1)\right)D^2.
}
\tag{2.4}
```

Let

```math
U_{i,D}:=\bigcup_{r\in G_i}K_r.
```

The interiors of the `K_r` are pairwise disjoint, so (2.4), together with containment in the corresponding asymptotic cap, says that after scaling by `D`, `U_{i,D}` converges in measure to that semicircle.

---

## 3. Perimeter lower semicontinuity forces the half-disk partition cost

For a finite union of convex bodies, its planar perimeter is at most the sum of the component perimeters:

```math
\operatorname{Per}(U_{i,D})
\le
\sum_{r\in G_i}\operatorname{per}(K_r).
\tag{3.1}
```

Planar perimeter is lower semicontinuous under convergence in measure of sets of finite perimeter.  Applying this after scaling by `D`, and using the measure convergence from Section 2, gives

```math
\liminf
\frac1D\operatorname{Per}(U_{i,D})
\ge
\operatorname{per}(C_i),
\tag{3.2}
```

where `C_i` is a radius-`1/2` semicircle.  Its perimeter is

```math
\operatorname{per}(C_i)=1+\frac\pi2.
```

Therefore

```math
\boxed{
\sum_{r\in G_i}\operatorname{per}(K_r)
\ge
\left(1+\frac\pi2-o(1)\right)D.
}
\tag{3.3}
```

The remaining non-dominant groups contribute nonnegative perimeter.  Summing `i=1,2` yields

```math
\boxed{
\sum_r\operatorname{per}(K_r)
\ge(\pi+2-o(1))D.
}
\tag{3.4}
```

Every extreme vertex of `K_r` lies on the outer face of the straight-line connected graph `C[I_r]`.  The closed outer walk has geometric length exactly `k_r` and convex hull `K_r`, so the closed-walk perimeter inequality gives

```math
k_r\ge\operatorname{per}(K_r).
```

Consequently

```math
\boxed{K_I:=\sum_r k_r\ge(\pi+2-o(1))D,}
```

which proves FP.1.

The constant `2D` is the two-sided internal partition boundary introduced when a disk is split into two asymptotic semicircles: each semicircle has perimeter `(1+pi/2)D`, while the original disk boundary has perimeter `pi D`.

---

## 4. Exact local Euler identity converts perimeter to ZK currency

For every unloaded component,

```math
r_r=\frac{k_r+Q_r}{2}-\delta_r.
```

Equivalently,

```math
\delta_r+r_r=\frac{k_r+Q_r}{2}.
```

Summing gives the exact identity

```math
\boxed{
S+R_I=\frac{K_I+Q_I}{2}.
}
\tag{4.1}
```

Since `Q_I>=0`, FP.1 immediately gives

```math
S+R_I
\ge
\frac{K_I}{2}
\ge
\left(1+\frac\pi2-o(1)\right)D,
```

proving FP.2.

This strengthens HG.4,

```math
S+R_I\ge(\pi/\sqrt2-o(1))D,
```

throughout the full-core near-circle phase.

---

## 5. Exact cancellation identifies loaded-interface defect with partition perimeter

NC and HBd simplify the exact boundary budget NBd to

```math
\boxed{
S+R_I+s_B+s_C=(\pi+o(1))D.
}
\tag{5.1}
```

HBd also simplifies the terminal ledger to

```math
\boxed{
Q+2s_C=(\pi+o(1))D.
}
\tag{5.2}
```

Use (4.1) in (5.1):

```math
s_C
=
\pi D-\frac{K_I+Q_I}{2}-s_B+o(D).
\tag{5.3}
```

Insert this into (5.2):

```math
\begin{aligned}
Q
&=
\pi D-2s_C+o(D)\\
&=
K_I+Q_I+2s_B-\pi D+o(D).
\end{aligned}
\tag{5.4}
```

Since `Q_B=Q-Q_I`, all internal-face defect cancels:

```math
\boxed{
Q_B=K_I-\pi D+2s_B+o(D).
}
```

This proves FP.3.

Insert FP.1:

```math
Q_B
\ge
(\pi+2-o(1))D-\pi D+2s_B
=(2-o(1))D+2s_B.
```

This proves FP.4 and FP.5.

---

## 6. Consequences

First, because `s_B>=0`, every full-core near-circle survivor satisfies

```math
\boxed{Q\ge Q_B\ge(2-o(1))D.}
\tag{6.1}
```

This improves UF's full-core bound `Q/D>=1.390168...` and removes the cap-minimal hypothesis from TE/LI's two-unit bound.

Second, FP.2 and (5.1) give

```math
\boxed{
s_B+s_C
\le
\left(\frac\pi2-1+o(1)\right)D.
}
\tag{6.2}
```

Third, FP.3 is a stability identity.  Any positive linear excess in either

```math
K_I-(\pi+2)D
```

or `s_B` appears with the same sign in `Q_B-2D`.  Thus the only way to remain near the minimum interface defect is simultaneously to have

1. asymptotically perimeter-minimal harmonic partition;
2. asymptotically saturated loaded degree, `s_B=o(D)`.

This gives a sharply defined equality branch for further work.

---

## 7. Equality branch

Suppose in addition

```math
Q_B=(2+o(1))D.
\tag{7.1}
```

Then FP.3-FP.4 force

```math
\boxed{s_B=o(D)}
\tag{7.2}
```

and

```math
\boxed{K_I=(\pi+2+o(1))D.}
\tag{7.3}
```

Hence every inequality in the perimeter argument is asymptotically sharp.  In particular each dominant semicircle group satisfies

```math
\sum_{r\in G_i}k_r
=
\left(1+\frac\pi2+o(1)\right)D,
\tag{7.4}
```

and the total component convex-hull perimeter in that group has the same leading value.

So the remaining minimal-interface model is not an arbitrary nested harmonic decomposition.  It is a perimeter-minimizing partition of each semicircle together with essentially complete use of the one remaining loaded contact slot.

A quantitative equality classification of (7.4) is now the shortest local target.  Any macroscopic internal partition interface inside one semicircle would add twice its length to the sum of component perimeters and therefore force `Q_B>2D` by FP.3.

---

## 8. Scope and audit notes

- No cap-minimal condition on `S=sum delta_r` is used.
- The theorem does use the **full-core** hypothesis through HG's two half-density semicircle groups.
- It also uses the PR #119 near-circle hypothesis `x_B=o(D)` through NC/HBd and the disk-limit geometry.
- The perimeter lower-semicontinuity step is standard for planar finite-perimeter sets.  It is used only after the component hull union is proved to converge in measure to the semicircle; no Hausdorff convergence of that generally disconnected union is assumed.
- The result is asymptotic at the `D` scale.  No finite `O(1)` correction is claimed.
- LEVEL I remains open because the perimeter-minimal two-semicircle partition is geometrically feasible at leading order.

---

## 9. Next target

FP reduces the entire full-core near-circle phase to two alternatives:

1. `Q_B>(2+c)D` for some positive linear excess, which immediately consumes additional exact terminal/boundary currency;
2. `Q_B=(2+o(1))D`, in which case `s_B=o(D)` and both harmonic semicircle groups are perimeter-minimizing.

The second branch should be attacked by a **semicircle partition-perimeter stability theorem**: show that perimeter equality forces one dominant component per half-disk, with all remaining component perimeter `o(D)`.  That would recover the two-carrier TS geometry without assuming `S/D->2`, and would force two `D+o(D)` interface contact paths directly from perimeter minimality.
