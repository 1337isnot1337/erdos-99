# Target C — joint aggregate payment from the actual and augmented cell ledgers

**Date:** 2026-09-12  
**Status:** proof-only research theorem on top of canonical audit.46  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

Canonical Section 122 forces linear aggregate return demand,

\[
\liminf {1\over D}
\sum_r(L_r+P_{{\rm exc},r}-2d_r)
\ge {\pi\over2}(2-\sqrt3),
\]

while canonical Section 123 separately pays the exceptional-face term by
`10(e_BB-k)`.  The two exact local ledgers can be combined before making that loss.

For one unloaded component put

\[
X_r:=a_r-T_r+Q_r^+,
\]

where `a_r` is the attachment count and `T_r,Q_r^+` are the canonical augmented-cell
triangle and degree-defect variables of Section 123.  Let

- `c_r` be the number of actual loaded-loaded contacts whose two endpoints lie in
  `A_r`;
- `Q_r` be the actual induced graph's bounded degree-above-four defect;
- `f_r` be its number of bounded nonquadrilateral faces;
- `L_r` be its occurrence-counted outer-face walk length.

Then the two canonical exact ledgers imply

\[
\boxed{L_r+Q_r-2a_r=X_r-2c_r.}
\tag{ARP.1}
\]

Consequently

\[
\boxed{
L_r+P_{{\rm exc},r}-2a_r
\le
5X_r-2c_r-4(a_r-T_r).
}
\tag{ARP.2}
\]

Summing and using the exact Section-123 global identity gives

\[
\boxed{
\sum_r(L_r+P_{{\rm exc},r}-2a_r)
\le
10(e_{BB}-k-d_{tile})
-2C_A-4U_A,
}
\tag{ARP.3}
\]

where

\[
C_A:=\sum_rc_r\ge0,
\qquad
U_A:=\sum_r(a_r-T_r)\ge0.
\]

Therefore the exact Section-122 currency obeys

\[
\boxed{
\sum_r(L_r+P_{{\rm exc},r}-2d_r)
\le
10(e_{BB}-k-d_{tile})
+2\sum_r(a_r-d_r)
-2C_A-4U_A.
}
\tag{ARP.4}
\]

Combining with Section 122 yields the necessary Type-II condition

\[
\boxed{
\liminf {1\over D}
\left[
10(e_{BB}-k-d_{tile})
+2\sum_r(a_r-d_r)
-2C_A-4U_A
\right]
\ge {\pi\over2}(2-\sqrt3).
}
\tag{ARP.5}
\]

This is a finite source-level strengthening of the audit.46 payment step.  It uses no
boundary-face classification, no assumption that loaded-loaded chords avoid particular
augmented faces, and no identification of local boundary occurrences across different
harmonic cells.

---

## 1. Actual induced-cell ledger

Fix one canonical unloaded positive-contact component `I_r` and use Section-82
notation.  Write

\[
a=a_r,
\qquad
s=s_r,
\qquad
c=c_r,
\qquad
L=L_r,
\qquad
Q=Q_r.
\]

Canonical Section 82 proves the exact finite identity

\[
\boxed{L+Q=4a-6-2s-2c.}
\tag{ARP.6}
\]

This is the actual induced graph, including every loaded-loaded unit contact whose two
endpoints belong to the attachment set.  The outer walk is occurrence-counted, so
bridges and repeated articulation occurrences are already included.

If `f=f_r` is the number of bounded nonquadrilateral faces, then every such face has
degree at least five and

\[
P_{exc}=4f+Q.
\tag{ARP.7}
\]

---

## 2. Augmented-cell ledger

Canonical Section 123 starts instead from only internal and attachment contacts and
then adds all sides of the convex attachment polygon.  With `T=T_r` and `Q^+=Q_r^+`,
it proves

\[
\boxed{
a-3-s={a-T+Q^+\over2}.}
\tag{ARP.8}
\]

Define

\[
X:=a-T+Q^+.
\tag{ARP.9}
\]

Equation (ARP.8) is exactly

\[
X=2a-6-2s.
\tag{ARP.10}
\]

Subtract `2a` from (ARP.6) and insert (ARP.10):

\[
L+Q-2a
=2a-6-2s-2c
=X-2c.
\]

This proves (ARP.1) without any geometric correspondence between individual actual and
augmented faces.

---

## 3. Pay actual exceptional perimeter with the same augmented defect

From (ARP.7) and (ARP.1),

\[
\boxed{
L+P_{exc}-2a=X-2c+4f.
}
\tag{ARP.11}
\]

Canonical Section 123 proves

\[
Q\le Q^+.
\tag{ARP.12}
\]

Every actual nonquadrilateral face contributes at least one unit to `Q`, so

\[
f\le Q\le Q^+.
\tag{ARP.13}
\]

Therefore

\[
L+P_{exc}-2a
\le X-2c+4Q^+.
\tag{ARP.14}
\]

But from the definition of `X`,

\[
Q^+=X-(a-T).
\tag{ARP.15}
\]

and hence

\[
L+P_{exc}-2a
\le
5X-2c-4(a-T).
\]

This proves (ARP.2).

The two credits have direct meanings:

1. every actual loaded-loaded contact internal to the attachment set reduces the actual
   outer/face ledger by two through Section 82;
2. every unit of augmented triangle deficit `a-T` is defect that Section 123 would
   otherwise discard when bounding only `Q^+`.

Neither credit is introduced by a new geometric assumption; both are already present
in the exact canonical identities.

---

## 4. Global sum

Canonical Section 123 gives

\[
\boxed{
e_{BB}-k
={1\over2}\sum_rX_r+d_{tile},}
\tag{ARP.16}
\]

so

\[
\boxed{
\sum_rX_r=2(e_{BB}-k-d_{tile}).
}
\tag{ARP.17}
\]

Put

\[
C_A:=\sum_rc_r,
\qquad
U_A:=\sum_r(a_r-T_r).
\tag{ARP.18}
\]

Both are nonnegative.  Sum (ARP.2) and use (ARP.17):

\[
\begin{aligned}
\sum_r(L_r+P_{{\rm exc},r}-2a_r)
&\le5\sum_rX_r-2C_A-4U_A\\
&=10(e_{BB}-k-d_{tile})-2C_A-4U_A.
\end{aligned}
\]

This is (ARP.3).

For each cell,

\[
L_r+P_{{\rm exc},r}-2d_r
=(L_r+P_{{\rm exc},r}-2a_r)+2(a_r-d_r),
\]

so (ARP.4) follows exactly.

Finally insert canonical Section 122's aggregate lower bound to obtain (ARP.5).

---

## 5. Hostile audit

The proof deliberately avoids the fragile route used in the first draft of this file.
No claim is made that a nonconsecutive loaded-loaded chord cannot alter one specified
side-adjacent augmented face.  Such a face-by-face claim is unnecessary.

The proof uses only these canonical finite statements:

1. Section 82 actual face ledger `L+Q=4a-6-2s-2c`;
2. Section 123 augmented ledger `a-3-s=(a-T+Q^+)/2`;
3. Section 123 monotonicity `Q<=Q^+` under the loaded-loaded chord insertion;
4. the tautological face inequality `f<=Q`;
5. Section 123 global identity (ARP.16);
6. Section 122 aggregate return floor.

The following scope checks are immediate.

- **Occurrence multiplicity:** contained in Section 82's `L` by definition.
- **Repeated use of one loaded contact in different cells:** allowed.  `C_A` is a
  favorable local credit appearing after summing valid local inequalities; no global
  injectivity of those contacts is asserted.
- **Exceptional faces:** only scalar `Q<=Q^+` is used, exactly as in canonical Section
  123.
- **Contact-isolated source points:** all remain in the global source; none is moved,
  deleted, or promoted to the positive core.
- **ZR/ZF scope:** no affine-kernel statement on isolated coordinates is used.
- **Global-minimizer quantifiers:** the theorem is a necessary inequality for every
  survivor in the canonical Type-II branch.  It does not replace the full source by a
  carrier.

Thus the proof is independent of the discarded first-draft boundary-pocket
classification.

---

## 6. What remains after the theorem

The audit.46 frontier treats

\[
\sum_r(L_r-2d_r)
\]

as the unstructured residue after paying `P_exc`.  Equations (ARP.3)--(ARP.5) reduce
that residue further.  After the exact augmented defect is paid, the only positive
term not already in loaded-hull/dissection currency is

\[
\boxed{\sum_r(a_r-d_r).}
\]

The next useful theorem should therefore attack this term jointly with `e_BB-k` rather
than upper-bound the complete outer walk from scratch.  Three concrete routes remain:

1. bound `sum(a_r-d_r)` from the common near-circle attachment geometry;
2. show that large `a_r-d_r` forces one near-global cell with transverse train width
   incompatible with diameter `D`;
3. use the alternative large `e_BB-k` regime with the loaded-hull/diameter-thrackle
   structure.

No C-II closure is claimed here.

**Theorem state:** unchanged.  This result is proof-only pending independent hostile
audit and lifecycle promotion.
