# Target C — exact conservation of inactive-chamber boundary residual

**Date:** 2026-09-12  
**Status:** proof-only consequence of canonical Sections 67 and 77; theorem-state unchanged.  
**LEVEL I STATUS:** STILL OPEN. C-II REMAINS OPEN.

The inactive-chamber ledger uses the isolate-only Oler slack

\[
 \sigma_j={A_j\over a_0}+{P_j\over2}+1-z_j,
 \qquad a_0={\sqrt3\over2}.
\]

For an internal exceptional face, the prescribed boundary is a cycle of actual unit
contacts. For an outer pocket, the hull-augmented graph supplies a simple convex
boundary cycle containing actual source vertices, with one added force-hull side.
Applying Oler to the assigned inactive points **together with those augmented boundary
vertices** shows that a large part of `sigma_j` is mandatory boundary credit rather
than possible packing spare.

The main exact identity is

\[
 \boxed{
 \sum_j(\sigma_j-k_j)
 =R_F
 :={A_F\over a_0}+{P_F\over2}+1-N_F-{E_4\over a_0}
 \ge0,
 }
\tag{0.1}
\]

where `k_j` is the augmented graph-boundary vertex count of chamber `j`, `F` is the
force hull, `P_F=per(F)`, `N_F=|A cap F|`, and `E_4` is total strict-rhombus area
excess.

Thus all inactive chambers share one force-hull Oler residual. Their residual packing
allowances do not add independently.

---

## 1. Canonical data

Use canonical Section 67 notation:

- `R_4` strict-rhombus bounded faces;
- `f` bounded nonquadrilateral faces;
- `Q=sum(deg P-4)` over those exceptional faces;
- `b` occurrence-counted old outer contact walk length;
- `q=|B|` loaded force-hull vertices;
- `k=d_H+s_Z`;
- `a` hull sides added to form the 2-connected hull-augmented graph `Ghat`;
- `L_add` total Euclidean length of those added sides;
- `P_F=per(F)`.

The exact identities needed below are

\[
 m=R_4+f+q-k+1,
\tag{1.1}
\]

\[
 b+Q=2(q-k),
\tag{1.2}
\]

\[
 P_F=q-a+L_{add}.
\tag{1.3}
\]

Let the inactive chambers be the `f` exceptional bounded faces plus the `a` convex
outer pockets of `Ghat`.

Canonical Section 77 gives

\[
 A_{ch}=A_F-A_4,
 \qquad A_4=a_0R_4+E_4,
\tag{1.4}
\]

\[
 Z_{ch}=N_F-m,
\tag{1.5}
\]

and the number of chambers

\[
 s=f+a.
\tag{1.6}
\]

For exceptional faces, total Euclidean perimeter is

\[
 \sum_{exc}P_j=4f+Q.
\tag{1.7}
\]

For outer pockets, canonical (67.24)--(67.25) give

\[
 \sum_{out}k_j=b+2a-q,
\tag{1.8}
\]

\[
 \sum_{out}P_j=b+2L_{add}-P_F.
\tag{1.9}
\]

Hence

\[
 P_{ch}=4f+Q+b+2L_{add}-P_F.
\tag{1.10}
\]

---

## 2. Every chamber has a nonnegative boundary residual

Define `k_j` as follows.

- For an exceptional bounded face, `k_j=deg(C_j)`. Its entire boundary consists of
  actual unit contact edges and source vertices.
- For an outer pocket, `k_j` is the graph-boundary edge/vertex count in `Ghat` used in
  canonical (67.24). The boundary consists of one added hull side and an old contact
  route; all graph-boundary vertices are original source points.

Canonical face/pocket Oler applied to the `k_j` boundary source vertices together with
the `z_j` assigned inactive source points gives

\[
 z_j+k_j\le {A_j\over a_0}+{P_j\over2}+1.
\tag{2.1}
\]

For outer pockets this is exactly canonical (67.28), including the convention that a
source point on an added hull side is assigned to the unique interior pocket.

Therefore

\[
 \boxed{
 r_j:=\sigma_j-k_j
 ={A_j\over a_0}+{P_j\over2}+1-z_j-k_j\ge0.
 }
\tag{2.2}
\]

For an internal exceptional face, `r_j` is the fixed-boundary residual
`r_partial` in the contact-wall repacking theorem.

The total augmented boundary count is

\[
\begin{aligned}
 K_{ch}:=\sum_jk_j
 &=(4f+Q)+(b+2a-q)\\
 &=4f+q-2k+2a,
\end{aligned}
\tag{2.3}
\]

where the second line uses (1.2).

---

## 3. Exact residual conservation

By definition,

\[
 \sum_j\sigma_j
 ={A_{ch}\over a_0}+{P_{ch}\over2}+s-Z_{ch}.
\tag{3.1}
\]

Insert (1.1) and (1.4)--(1.10):

\[
\begin{aligned}
\sum_jr_j
={}&{A_F-a_0R_4-E_4\over a_0}
 +{4f+Q+b+2L_{add}-P_F\over2}\\
&+(f+a)-(N_F-m)\\
&-(4f+Q+b+2a-q).
\end{aligned}
\tag{3.2}
\]

Use `m=R_4+f+q-k+1` to cancel `R_4`, then collect terms. This gives

\[
\sum_jr_j
={A_F\over a_0}-N_F-{E_4\over a_0}
+2q-k-{Q+b\over2}+L_{add}-{P_F\over2}-a+1.
\tag{3.3}
\]

Equation (1.2) makes

\[
 {Q+b\over2}=q-k,
\]

so (3.3) becomes

\[
\sum_jr_j
={A_F\over a_0}-N_F-{E_4\over a_0}
+q+L_{add}-a-{P_F\over2}+1.
\tag{3.4}
\]

Finally (1.3) says `q+L_add-a=P_F`. Therefore

\[
 \boxed{
 \sum_jr_j
 ={A_F\over a_0}+{P_F\over2}+1-N_F-{E_4\over a_0}
 =R_F.
 }
\tag{3.5}
\]

Canonical Section 67 is exactly

\[
 a_0N_F\le A_F+{a_0\over2}P_F+a_0-E_4,
\]

so

\[
 \boxed{R_F\ge0.}
\tag{3.6}
\]

This independently verifies the sign forced by the chamber-by-chamber Oler argument.

---

## 4. Capacity interpretation

For every internal exceptional face `C_j`, let `M_partial(C_j)` be its fixed-boundary
packing capacity from the contact-wall theorem. Oler gives

\[
 0\le M_\partial(C_j)-z_j\le r_j.
\tag{4.1}
\]

Hence, even before checking whether those upper bounds are attainable,

\[
 \boxed{
 \sum_{j\in exc}\bigl(M_\partial(C_j)-z_j\bigr)
 \le\sum_{j\in exc}r_j
 \le R_F.
 }
\tag{4.2}
\]

So one cannot pay a diameter-vertex-cover repacking independently out of each
chamber's coarse `sigma_j`; all possible fixed-boundary spare is subordinated to the
single force-hull residual `R_F`.

For outer pockets, `r_j` is still the exact Oler residual after fixing all augmented
boundary source vertices, but the contact-wall theorem does not make this full
fixed-boundary capacity globally safe across the artificial hull chord. No such
extension is asserted.

---

## 5. Relation to the canonical `O(D)` chamber ledger

Canonical Section 77 proves

\[
 \sum_j\sigma_j=O(D),
\]

and `K_ch=O(D)` from the exact boundary ledgers. Equation (3.5) therefore also gives

\[
 \boxed{R_F=O(D)}
\tag{5.1}
\]

in the canonical chamber regime.

The point of (3.5) is not the order bound. It identifies the exact nonnegative
remainder after all mandatory boundary credit has been removed.

In particular, a future repacking theorem should compare the required diameter-cover
size with `R_F` or with a proven lower realization of the individual residuals, not
with the much larger-looking sum of raw chamber Oler slacks.

---

## 6. What this does and does not close

This theorem is an exact source-level accounting result. It does not infer a lower
bound on any chamber's actual packing extension and does not reverse Oler.

The inactive-container closure problem is sharpened to two distinct tasks:

1. **realization:** convert enough of the nonnegative residual `R_F` into actual
   fixed-boundary packing slots or a lexicographic exchange; or
2. **global contradiction:** prove that the canonical diameter topology requires more
   removable diameter vertices than the single residual can support, and then obtain a
   different strict-diameter deformation rather than a nonexistent packing extension.

The identity keeps every source point and does not use the Section-57 affine-kernel
statement on contact isolates.
