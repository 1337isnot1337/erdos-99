<!-- theorem-state: {"artifact_id":"ART-D46AB56198A3","canonical":true,"claim_ids":["C-ALMOST-ACCESSIBLE-STRESS-TRANSVERSAL"],"claim_statuses":{"C-ALMOST-ACCESSIBLE-STRESS-TRANSVERSAL":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C: almost-accessible transversals from exceptional-face codimension

Date: 2026-10-08.
Run base: `5f8ece96`.
Canonical base: `d32a55f224e484609b1557bf5b8d531869b20558`.
State: `2026-10-08.audit.148`.
Independent Audit.171 disposition: the finite mixed loaded/unloaded stress-transversal
theorem is canonical. The Type-II grid specialization remains conditional on its
separate unreviewed candidate. The adjacent star-face sharpening is excluded here and
remains unreviewed. C-II and Level I remain open.

## 1. Exact improvement of the finite-source gate

The [preceding alternative](target_c_accessible_stress_transversal_or_degenerate_face_2026-10-08.md)
gave a deletion inside a supplied accessible loaded set `W` only when
its exceptional zero-reaction face `P_0` was empty. A nonempty face
forced large selected circuit defects but supplied no located deletion.

The new chain is:

    actual W and b_0=|H[B\W]|
      -> dim P_0 <= b_0-1 by canonical contact-row independence
      -> at most b_0 unloaded exceptions kill P_0
      -> each chosen exception removes an independent affine dimension
      -> remaining accessible loaded deletions restore total cost <=s_Z+1
      -> canonical finite strict descent of the reduced full source
      -> Level I only after a verified refill restores every label.

No uniform KKT coefficient bound is needed. No exceptional circuit
is declared impossible. The cardinality-restoration arrow remains open.

## 2. Canonical inputs and exact support sets

Use the canonical C-II source `D>=9`, `C=C_*`, `H=H_*`.
Let `V` be its nonisolated positive-contact core, `B` its full actual
diameter-endpoint set, `I=V\B`, and `P` its normalized KKT polytope.
Retain every source label, including all contact isolates.

The load-bearing inputs are:

- [Section 64](../targets/target-c/64-extreme-circuit-transfer-audit.md):
  `P` is compact and `dim_aff P=s_Z`.
- [Contact-face regularity](../audits/target_c_october_structural_promotion_audit_2026-10-05.md),
  Section 5: `rank R_C=e`, so every actual contact row is independent.
- [Audit.111](../audits/target_c_loaded_only_stress_scope_extension_independent_audit_2026-10-07.md),
  Section 3: every loaded-only normalized stress, if one exists,
  has positive diameter support incident to every actual loaded vertex.
  The full actual loaded hull is two-dimensional and `D>=6`.
- [Audit.87](../audits/target_c_contact_opening_transversal_independent_audit_2026-10-07.md):
  absence of a normalized retained-source stress gives a strict
  contact-opening and old-diameter-shortening finite motion.

Let `W` be any nonempty subset of `B`. Define

\[
f_b(s)=\sum_{h\ni b}\beta_h,\quad
F_b=P\cap\{f_b=0\},\quad
P_0=\bigcap_{b\in W}F_b,\quad
E_0=H[B\setminus W],\quad b_0=|E_0|.
\tag{AC1}
\]

All these are actual source objects. Each `f_b` is affine and
nonnegative on `P`. `P_0` is an exposed face, possibly empty.

## 3. Contact independence bounds the exceptional-face dimension

Equilibrium is

\[
R_C^T\alpha=R_H^T\beta.
\tag{AC2}
\]

If two stresses have the same `beta`, their contact difference
satisfies `R_C^T(delta alpha)=0`. Since `rank R_C=e`, that
difference is zero. Thus the projection `s -> beta` is injective
on the full affine equilibrium space.

Every stress in `P_0` has `beta` supported in `E_0` and normalized
by `sum beta=1`. If `P_0` is nonempty, necessarily `b_0>=1` and

\[
\boxed{\dim_{\rm aff}P_0\le b_0-1.}
\tag{AC3}
\]

The canonical relative-interior stress is positive on every actual
diameter row. Since `W` is nonempty, `P_0` is also a proper face of
`P`. Thus `dim P_0<=s_Z-1` whenever it is nonempty.
In particular `s_Z=0` always gives the empty-face alternative.

This bound would need an additional contact-fiber term if the contact
rows were dependent. Contact-row independence is a load-bearing
canonical premise, not a generic rigidity assumption.

## 4. A two-stage exposed-face lemma

Let `P` be any compact polytope of affine dimension `d`.
Let `f_w,g_y` be finite families of nonnegative affine functions
on `P`. Put `P_0=P intersect all {f_w=0}`. Suppose `P_0` is
nonempty of dimension `p` and

\[
P_0\cap\bigcap_y\{g_y=0\}=\varnothing.
\tag{AC4}
\]

Choose an inclusion-minimal set `Y_0` whose `g_y` zero faces
already have empty intersection with `P_0`, and write `k=|Y_0|`.
For every `i in Y_0` minimality gives a witness `s_i in P_0` with

\[
g_i(s_i)>0,\qquad g_j(s_i)=0\quad(j\ne i,\ j\in Y_0).
\tag{AC5}
\]

Applying the `g_j` to an affine dependence of these witnesses
shows that they are affinely independent. Hence

\[
k\le p+1.
\tag{AC6}
\]

Let `F=P intersect all_{i in Y_0}{g_i=0}`. If `F` is empty,
`Y_0` alone kills every point of `P` and `k<=p+1<=d+1`.

Otherwise choose `t in F`. The linear parts of the `g_i` evaluate
the vectors `s_j-t` as a diagonal matrix with strictly positive
diagonal. They therefore have rank `k` on the affine direction
space of `P`. Consequently

\[
\boxed{\dim_{\rm aff}F\le d-k.}
\tag{AC7}
\]

Because `F intersect P_0` is empty, finite Helly on `F` selects
at most `dim F+1<=d-k+1` of the `f_w` zero faces whose
intersection with `F` is empty. Call their indices `W_0`.
Thus

\[
\boxed{|Y_0|\le p+1,\qquad |Y_0|+|W_0|\le d+1.}
\tag{AC8}
\]

The codimension step is essential: simply adding two independent
Helly bounds would add `p+1` to the total deletion budget.

## 5. Apply the lemma to actual unloaded contact reactions

For every `r in I` define

\[
g_r(s)=\sum_{c\ni r}\alpha_c.
\tag{AC9}
\]

These are nonnegative affine functions. A stress with every
`g_r=0` is supported wholly on loaded vertices. Audit.111 says
its positive diameter support must be incident to every vertex of
`B`. Such a stress cannot lie in `P_0`, since `W` is nonempty.
Thus AC4 holds with the actual unloaded label set `I`.

If `P_0` is nonempty, apply Sections 3–4. There are `Y_0 subset I`
and `U subset W` such that

\[
\boxed{|Y_0|\le\min\{b_0,s_Z\},\qquad |Y_0|+|U|\le s_Z+1,}
\tag{AC10}
\]

and no normalized source stress has both zero contact reaction
on `Y_0` and zero diameter reaction on `U`.

If `P_0` is empty, ordinary Helly gives `U subset W`,
`|U|<=s_Z+1`, and take `Y_0` empty. Therefore for every nonempty
actual loaded set `W` there is a deletion `R=U union Y_0` with

\[
\boxed{
|R|\le s_Z+1,\qquad
R\cap B\subseteq W,\qquad
|R\cap I|\le\min\{b_0,s_Z\}.
}
\tag{AC11}
\]

Every normalized stress on the retained source extends by zero to
a source stress with all the deleted incident coefficients zero.
At a deleted loaded vertex, zero diameter reaction forces zero
contact reaction by the strict supporting-functional argument.
Such a stress would contradict the selected face cover.

The retained source is nonempty. If `P_0` is nonempty, an edge of
`E_0` has both endpoints outside `W`, and these loaded endpoints
are not deleted with `Y_0 subset I`. If `P_0` is empty and `W`
is proper, a loaded vertex outside `W` remains. If `W=B`, take
`U` inclusion-minimal; it is proper because `B minus {b}`
meets every actual diameter edge for any `b in B`.

Audit.87 now gives the strict finite reduced-source descent.
All contact isolates remain retained and all their inactive pair
constraints are checked by the finite source-dependent margins.

## 6. Grid-access consequence and the precise remaining gap

Conditional on the
the separate unreviewed uniform-cell/global diameter-access candidate,
in Type II, for each fixed `lambda,eta>0` and sufficiently large
`D`, one can choose `W` with actual short grid routes and
`b_0<=eta D`. Since `h>=D`, `eta<1` ensures `W` is nonempty.
AC11 then gives a stress-killing deletion of at most `s_Z+1`
labels with at most `eta D` unloaded exceptions. Every other
deleted label is one of the supplied grid-accessible loaded vertices.

This includes the nonempty, high-circuit-defect exceptional-face
alternative. It does not prove a uniform mass gap or eliminate that
face. The exceptions can be chosen by contact reactions rather than
by forcing every selected circuit to become nondegenerate.

Under the usual fixed-parameter quantifiers, a diagonal choice of
`lambda,eta` tending to zero gives short routes of `o(D)` and
`o(D)` unloaded exceptions along a Type-II survivor sequence.
This is a located deletion theorem only. The total deleted population
can still be linear in `D`; the routes and grids can overlap;
the diagonal choice need not retain one fixed positive grid-shore constant;
no capacity, compatible restoration, or same-cardinality strict-`D`
competitor is proved. The grid premise remains unreviewed, and the
separate macroscopic-container branch is not covered by that premise.

A separate unreviewed star-face candidate claims to sharpen
`|Y_0|<=b_0` to one when `E_0` lies in one actual diameter star. That claim is not
used in Sections 1–5 and is excluded from this audit.

## 7. Certificate scope

The [exact common checker](../../research/verify_target_c_exceptional_star_face_2026_10_08.py)
verifies seven exact nonglobal planar fixtures, their complete actual pair sets,
contact-row independence, equilibrium, PSD and mixed ranks, and smaller
same-cardinality competitors.
It also checks the two-stage face/codimension counts on exact
simplexes and joins of cubes with simplexes. Those abstract polytopes
are not planar sources.

Sections 3–5 contain the analytic candidate theorem. Computation
does not prove canonical grid access, the universal finite theorem,
or refill. Both C-II branches and the full Level I objective remain open.
