# Hostile audit — Target C Section 132 cellwise rhombus boundary payment

**Date:** 2026-09-12
**Reviewed:** `research/target_c_section132_cellwise_rhombus_boundary_payment.md`
**Disposition:** **PASS as a proof-only Type-II tradeoff.** C-II remains open.

## 1. Local boundary theorem

Canonical Section 82 makes every bounded quadrilateral face of the actual induced harmonic graph `H_r` a strict unit rhombus.  Apply the canonical strict-rhombus boundary theorem to precisely this finite face collection.  If `B_{4,r}` is its physical boundary occurrence count, then

\[
B_{4,r}\ge4\sqrt{R_{4,r}}.
\]

For an edge occurrence on this rhombus-complex boundary, the face on the other side in the plane graph `H_r` is either the outer face or a bounded nonquadrilateral face.  The first class has at most `L_r` occurrences and the second at most `P_exc,r`.  Hence

\[
4\sqrt{R_{4,r}}
\le B_{4,r}
\le L_r+P_{exc,r}.
\]

Bridges and repeated outer vertices are harmless because `L_r` is occurrence-counted.

**Verdict:** PASS.

## 2. Global upper payment

Recompute the algebra from Sections 124 and 127.  Section 124 gives

\[
\sum_r(L_r+P_{exc,r}-2a_r)
\le10(e_{BB}-k-d_{tile})-6C_A.
\]

The exact attachment-incidence identity is

\[
a=3q-6-2(e_{BB}-k)-2s_C-d_{tile}.
\]

Therefore

\[
\sum_r(L_r+P_{exc,r})
\le6(q-k)+6e_{BB}-4s_C-12d_{tile}-6C_A-12.
\]

Section 127 gives

\[
e_{BB}-C_A\le2d_{tile},
\]

so the middle three terms satisfy

\[
6e_{BB}-6C_A-12d_{tile}\le0.
\]

Thus

\[
\boxed{
\sum_r(L_r+P_{exc,r})
\le6(q-k)-4s_C-12.
}
\]

Combining with the local lower bounds gives

\[
\boxed{
3(q-k)-2s_C
\ge2\sum_r\sqrt{R_{4,r}}+6.
}
\]

Since `q-k=h-s_Z`, Section 132.3 follows.

**Verdict:** PASS.  The constant `-12` and the factor `2` after division are correct.

## 3. Ownership of unloaded-only global rhombi

Take a global bounded quadrilateral contact face with no loaded vertex.  Its four vertices are unloaded and its four contact edges form a connected cycle, so all four vertices lie in one unloaded component `I_r`.  The global face interior contains no contact-graph vertex or edge.  Passing to the induced graph `H_r` cannot insert a new edge or vertex into that interior; the same four-cycle remains a bounded quadrilateral face of `H_r`.

Thus every unloaded-only global strict rhombus contributes to at least one `R_{4,r}`.

A global quadrilateral face touching the loaded set can be charged to a loaded vertex-face incidence.  A loaded positive-contact vertex has degree at most three, hence is incident to at most three bounded contact faces.  Therefore the number of loaded-touching quadrilateral faces is at most `3q=O(D)`.

Consequently

\[
\sum_rR_{4,r}\ge R_4-O(D).
\]

In Type II, `R_4/D^2 -> Delta_2`, so

\[
\sum_r\sqrt{R_{4,r}}
\ge\sqrt{\sum_rR_{4,r}}
\ge(\sqrt{\Delta_2}-o(1))D.
\]

**Verdict:** PASS.

## 4. Regression against the withdrawn Type-II interface floor

Section 132 concludes only

\[
{3(h-s_Z)-2s_C\over D}
\ge2\sqrt{\Delta_2}-o(1).
\]

It does **not** infer

\[
(q-k)/D\ge2\sqrt{\Delta_2}
\]

or the withdrawn `0.6676585...` nonmatching floor.  A large `s_C` requires a correspondingly larger `q-k`; the pinned-surplus term cannot be discarded.

**Verdict:** no regression.

## 5. Partition refinement

For disjoint groups of component indices `G_j`,

\[
\sum_{r\in G_j}\sqrt{R_{4,r}}
\ge\sqrt{\sum_{r\in G_j}R_{4,r}}.
\]

Hence groupwise quadratic rhombus-count floors may be charged separately.  This is a valid algebraic refinement, but Section 132 correctly does not insert a numerical group decomposition without first proving the corresponding groupwise rhombus-area statements.

**Verdict:** PASS.  The refinement is the main new structural value of the theorem.

## 6. Final classification

Section 132 is a valid proof-only theorem conditional on the already proof-only Sections 124/125/127.  It retains all source points, uses no full-source affine-kernel extension, and remains compatible with the corrected main-branch Type-II interface audit.

**PASS. Theorem state unchanged. C-II remains open.**
