<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "d32be42cda60bef0d7d3c7c3d410b99d6fe8a485", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_atomic_gap_shore_balance_00059_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "b8a7091ece2f2d4c26b2ea404cefa63b5db790bf547dfda01652059ac50c8f09"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — coupled shore-balance refinement of the atomic grid gap

**Date:** 2026-09-15  
**Repository base:** `729b7bac8d5e82812c4762cb0dc809f3f60fb92e`  
**Status:** proof-only quantitative strengthening; theorem-state authority unchanged  
**Scope:** the audited §163/§168 Type-II train-phase argument  
**LEVEL I STATUS:** `STILL OPEN`

The current AG42 proof certifies

\[
x\sigma\ge 2\sqrt{\Delta_2}+0.00042,
\qquad
\Delta_2={\pi\over2\sqrt3},
\]

by applying finite Mantel stability to one dominant three-direction atomic orbit.  Its
last numerical step is deliberately wasteful: after assigning the three atom windows
to their majority Mantel shores, it lower-bounds **each** retained shore by subtracting
the full total minority-window loss.  The same minority mass cannot be lost from both
shores simultaneously.

Keeping the two retained shore masses coupled strengthens the opposite-corner path
bound without changing any geometric input, phase-order argument, or degree-pruning
argument.  The resulting safe round constant is

\[
\boxed{\eta_{grid}=0.00059.}
\]

The scalar root of this revised bookkeeping is approximately

\[
0.0005994655685586\ldots,
\]

so `0.00059` retains substantial numerical margin.

---

## 1. Inherited dominant-orbit constants

Put

\[
s_2:=\sqrt{\Delta_2},
\qquad
\bar A:=2s_2+\eta.
\]

Assume for contradiction that the absolute atomic train mass satisfies

\[
A=x\sigma\le \bar A.
\]

Exactly as in audited §168, one dominant exact `pi/3` orbit has mass at least

\[
M_0={4s_2^2\over\bar A}.
\tag{SB.1}
\]

The remaining atomic mass is at most

\[
R_0:=\bar A-M_0,
\]

and the dominant-orbit finite crossing graph has Mantel deficit at most

\[
\boxed{
d_0:={\bar A^2\over4}-s_2^2+{R_0^2\over4}.
}
\tag{SB.2}
\]

Let its actual normalized orbit mass be `M>=M_0`.  The standard maximum-degree
near-Mantel partition gives two shores `X,Y` with

\[
|X|+|Y|=(M+o(1))D,
\tag{SB.3}
\]

\[
\min\{|X|,|Y|\}
\ge\left({M\over2}-\sqrt{d_0}-o(1)\right)D,
\tag{SB.4}
\]

and at most

\[
(2d_0+o(1))D^2
\tag{SB.5}
\]

missing cross-shore pairs.

These are precisely the §168 bounds; no new stability theorem is used.

---

## 2. Total minority mass is one global loss

Freeze the at most three atom windows of the dominant orbit.  Write their normalized
populations on the two Mantel shores as

\[
(x_i,y_i),\qquad i=1,2,3.
\]

Trains in the same sufficiently narrow direction window do not cross in strict
rhombi.  Hence every same-window cross-shore pair is missing, so (SB.5) gives

\[
\sum_{i=1}^3 x_i y_i\le2d_0+o(1).
\tag{SB.6}
\]

Assign each atom window to its majority shore and discard the minority population.
Let

\[
L:=\sum_i\min(x_i,y_i).
\]

Since `min(x_i,y_i)<=sqrt(x_i y_i)`, Cauchy gives

\[
\boxed{
L\le\sqrt{3\sum_i x_i y_i}
\le\sqrt{6d_0}+o(1).
}
\tag{SB.7}
\]

Let `P,Q` be the retained normalized masses on the two shores after this one global
discard.  Then

\[
\boxed{
P+Q\ge M-\sqrt{6d_0}-o(1),
}
\tag{SB.8}
\]

while (SB.4) and the fact that the total discard is at most the right side of (SB.7)
give

\[
\boxed{
\min(P,Q)
\ge {M\over2}-\sqrt{d_0}-\sqrt{6d_0}-o(1).
}
\tag{SB.9}
\]

The old AG42 bookkeeping replaced both `P` and `Q` separately by the lower bound in
(SB.9).  That pays the same total minority loss twice.

---

## 3. Coupled two-family mass bound

After the majority assignment, every one of the at most three atom windows belongs to
one shore.  Both retained shores are nonempty in the numerical range below.  Thus one
shore contains at most one atom family and the other contains at most two.

Choose `A_1` to be the unique family on the one-family shore and `B_1` to be the
larger family on the other shore.  If the one-family shore has mass `P`, then

\[
|A_1|/D+|B_1|/D\ge P+{Q\over2}-o(1).
\]

If instead it has mass `Q`, the corresponding bound is `Q+P/2`.  Therefore in all
cases

\[
{ |A_1|+|B_1|\over D}
\ge
\min\left\{P+{Q\over2},Q+{P\over2}\right\}-o(1).
\]

Using

\[
\min\left\{P+{Q\over2},Q+{P\over2}\right\}
={P+Q+\min(P,Q)\over2}
\]

with (SB.8)--(SB.9) yields the strengthened coupled family floor

\[
\boxed{
{ |A_1|+|B_1|\over D}
\ge
{3M\over4}
-{\sqrt{d_0}\over2}
-\sqrt{6d_0}
-o(1).
}
\tag{SB.10}
\]

Since `M>=M_0`, it is enough to use

\[
\boxed{
G_0:={3M_0\over4}
-{\sqrt{d_0}\over2}
-\sqrt{6d_0}.
}
\tag{SB.11}
\]

This is the only mathematical change from AG42.

For the separate common-neighbor/transitivity check we retain the old individual shore
floor

\[
S_0:={M_0\over2}-\sqrt{d_0}-\sqrt{6d_0}.
\tag{SB.12}
\]

Thus no part of the inherited §163 order-consistency proof is weakened.

---

## 4. The inherited pruning losses remain six `p_0`

Put

\[
p_0:=\sqrt{2d_0}.
\tag{SB.13}
\]

The total missing-pair budget between `A_1` and `B_1` is still at most
`(2d_0+o(1))D^2`.

The tie-safe phase-order pruning from §163 deletes at most `p_0D+o(D)` trains from
each family.  The subsequent minimum-degree pruning deletes at most another
`p_0D+o(D)` from each family.  Every retained endpoint train then misses at most
`p_0D+o(D)` trains on the opposite shore.

Consequently the opposite-corner degree sum in §163.7 is at least

\[
\boxed{
E_{bal}(\eta)D-o(D),
\qquad
E_{bal}(\eta)
:=G_0-6p_0.
}
\tag{SB.14}
\]

The six `p_0` losses have the same provenance as in audited §168:

1. phase pruning from `A_1`;
2. phase pruning from `B_1`;
3. degree pruning from `A_1`;
4. degree pruning from `B_1`;
5. the missing-neighbor allowance at the chosen `A_1` corner;
6. the missing-neighbor allowance at the chosen `B_1` corner.

No pruning loss has been removed or merged.

The old individual floor (SB.12) still guarantees the common-neighbor hypotheses.  In
particular it suffices that

\[
{S_0\over2}-2p_0>3p_0,
\tag{SB.15}
\]

which has very large slack at the chosen constant.

---

## 5. Numerical certification at `eta=0.00059`

Take

\[
\boxed{\eta=0.00059.}
\]

High-precision evaluation gives

\[
\begin{aligned}
s_2&=0.9523128068639573458\ldots,\\
\bar A&=1.9052156137279146917\ldots,\\
M_0&=1.9040357964368939231\ldots,\\
d_0&=0.0005622995732597827303\ldots,\\
\sqrt{d_0}&=0.0237128567081189678\ldots,\\
p_0&=0.0335350435592316692\ldots,\\
\sqrt{6d_0}&=0.0580843992786246898\ldots .
\end{aligned}
\tag{SB.16}
\]

The old individual-shore quantity is

\[
S_0=0.8702206422317033040\ldots,
\]

so

\[
{S_0\over2}-2p_0
=0.368040233997388314\ldots
>3p_0
=0.100605130677695008\ldots .
\tag{SB.17}
\]

Thus the inherited common-neighbor and global crossing-order argument is comfortably
valid.

The new coupled corner coefficient is

\[
\boxed{
E_{bal}(0.00059)
=1.1568757583395962534\ldots .
}
\tag{SB.18}
\]

Every selected train vector has common projection tending to `sqrt(3)/2`, so the
opposite-corner path inequality would force

\[
1\ge {\sqrt3\over2}E_{bal}(0.00059)-o(1).
\]

But

\[
\boxed{
{\sqrt3\over2}E_{bal}(0.00059)
=1.0018837957444775105\ldots>1.
}
\tag{SB.19}
\]

This is a margin of about `1.88e-3`, more than ten times the final margin in AG42 at
`0.00042`.

A numerical root search for the unchanged formulas gives

\[
E_{bal}(\eta)={2\over\sqrt3}
\]

at

\[
\eta\approx0.0005994655685586,
\tag{SB.20}
\]

so the displayed `0.00059` is deliberately conservative.

### Theorem SB.1 — shore-balanced atomic grid gap

Every Type-II §142 train-measure subsequential limit in the audited §163/§168 scope
satisfies

\[
\boxed{
x\sigma\ge2\sqrt{\Delta_2}+0.00059.}
\tag{SB.21}
\]

The theorem is proof-only and does not mutate canonical theorem state.

---

## 6. Immediate propagation

The exposed-hull step used in §§142/164 is unchanged, hence

\[
\boxed{
\liminf {T-q/2\over D}
\ge2\sqrt{\Delta_2}+0.00059.
}
\tag{SB.22}
\]

Using `T-q=2f-k`,

\[
\boxed{
\liminf {2f-k\over D}
\ge2\sqrt{\Delta_2}-\frac\pi2+0.00059.
}
\tag{SB.23}
\]

The same argument also restricts to the non-singleton rhombic train graph wherever the
independent §168 rhombic-only audit applies.

---

## 7. Scope and audit boundaries

- The finite near-Mantel partition, phase-order pruning, degree pruning, and
  opposite-corner source-diameter path are exactly those already audited in §§163 and
  168.
- The only new inequality is the coupled shore-mass estimate (SB.10).
- The total minority-window loss is used once in `P+Q` and once, legitimately, in a
  lower bound for `min(P,Q)`; this yields one total coefficient `sqrt(6d_0)` in
  (SB.10), not two separate shore deductions.
- The old individual floor `S_0` is retained for the common-neighbor argument, so no
  transitivity hypothesis is inferred from the coupled sum alone.
- Contact-isolated source points never enter the positive-contact train graph.
- No outer-detour hypothesis or new source deformation is used.

C-II remains open.  The immediate next step is to replace the AG42 constant by (SB.21)
in the dominant-orbit outer-energy theorem and re-optimize its scalar exclusion.
