<!-- theorem-state: {"artifact_id":"ART-EDD23EAB1C17","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-b"} -->
# Target B: separable Oler transfer, an explicit global subcase, and exact near misses

**Status:** unreviewed proof and literature-transfer audit; finite controls are
separate from the analytic arguments. **LEVEL I STATUS: STILL OPEN.**

**Source main:** `e396ea07887dd0528b817ce4e656ff0e6b01f8fb`.
**State:** `2026-10-15.publication.2`; **priority:** `public-frontier.3`;
**catalogue:** `public-frontier.7`.
**Task:** `literature-shell-stability-near-miss-audit`, selected after live
handoff inspection on 2026-10-17. The snapshot had no open PRs/Issues and four
Discussion hubs, with no specific handoff. This is coverage, not a novelty claim.

## 1. Question, scope, and outcome

Can a finite-packing or crystallization theorem supply the missing Target B bound
under hypotheses actually available for the canonical full source?
Write

\[
 a_0=\frac{\sqrt3}{2},\quad c_0=\frac{\sqrt3}{4},\quad
 K=\operatorname{conv}A,\quad P=\operatorname{per}K,\quad N=|A|.
\]

For the source's chosen strict unit-rhombic complex, retain every label, put
\(t=N-v\), and use the actual complex Euler characteristic \(\chi\). The
objective is

\[
 G+E\ge c_0B+a_0(t+\chi-1).                         \tag{1}
\]

Section 36 of the [Target B route](../targets/target-b/01-jammed-rhombic-branch.md)
proves the strict reverse for every global minimizer. Its full proof uses the
nonconstant integer-valued translated triangular-lattice count to obtain
\(D(N)^2<(2\sqrt3/\pi)(N-1)\), then isodiametry and
\(N=R+B/2+\chi+t\). Thus (1), with the global quantifiers and full-source
hypotheses, would close this branch.

This audit obtains a smaller valid implication: **no global minimizer of
cardinality \(N\ge153\) has a totally separable radius-\(1/2\) disk packing**.
More generally, making a large global source totally separable by deleting
labels requires a positive fraction of its population; boundary-order deletion
is insufficient. A convex partition into totally separable cells likewise
requires quadratic interface length plus cell count.
It also reconstructs the required convex-hull separable bound independently.
Triangle-free contacts do not imply total separability. An exact all-size
rhombic family demonstrates that mismatch and shows why the combinatorial
crystallization defect does not uniformly pay angular area surplus.

The first experiment was to normalize the finite bounds, then substitute a
near-triangular rhombic patch. The falsification targets were missing
separability, contact-energy minimization, topology conventions, and boundary
order. Stop after identifying those failures and the explicit valid subcase;
this is not an exhaustive literature survey or an audit of GPI's proof chain.

## 2. Primary-source comparison

The sources below were checked on 2026-10-17. They are linked, not redistributed.
Equations use center separation one. The first two bounds use convex hulls,
which erase internal holes and grain interfaces; those data require separate
transfer arguments.

| Source and exact location | Normalized statement / hypotheses | First missing transfer |
| --- | --- | --- |
| K. J. Böröczky and I. Z. Ruzsa, *Note on an inequality of Wegner*, author manuscript dated 2007-01-02, printed pp. 2–3, (2), Theorem 1.1; [primary PDF](https://www.renyi.hu/~carlos/wegner.pdf), DOI `10.1007/s00454-006-1277-4` | Oler: \(A_K+c_0P\ge a_0(N-1)\). Wegner: \(A_K+P/2\ge a_0(N-1)+c_W W_N\), where \(c_W=(2-\sqrt3)/4\), \(W_N=\lceil\sqrt{12N-3}-3\rceil\). Finite nonoverlapping congruent disks; the container is convex. | This is the same scalar improvement already derived in the repository's [Wegner report](wegner_global_boundary_defect_2026-09-09.md), not a new shell theorem. It has no interface incidence or phase payment. |
| K. Bezdek and Z. Lángi, *Bounds for totally separable translative packings in the plane*, [arXiv:1710.06886v1](https://arxiv.org/abs/1710.06886v1), Theorem 1, printed p. 3, proof pp. 4–6 | With radius-\(1/2\) disks: \(N\le A_K+P/2+1\). The packing must be totally separable. The general theorem uses a permissible enclosing polygon and a minimal circumscribed parallelogram. For these disks its area is 1 and Minkowski perimeter is \(2P\). | The convex hull supplies the enclosing polygon. Total separability is an extra disk-arrangement hypothesis; triangle-free contact graphs do not supply it. Section 4 gives a three-label failure. |
| L. De Luca and G. Friesecke, *Crystallization in two dimensions and a discrete Gauss–Bonnet theorem*, [primary final PDF](https://cvgmt.sns.it/media/doc/paper/3321/DLF-final.pdf), Sections 2.3–2.4, Theorem 3.1, (1.5); [arXiv:1605.00034](https://arxiv.org/abs/1605.00034), DOI `10.1007/s00332-017-9401-6` | For unit-contact Heitmann–Radin energy, \(\mathcal H=-e=-3N+P_g+3\chi_g+\mu\). Here \(P_g\) is graph perimeter, wires counted twice, and \(\mu\) counts added triangulation edges. The identity needs no energy minimality; crystallization does. | Minimum diameter is not minimum contact energy. On a rhombic disk the identity reduces to Euler counting. Its defect \(\mu\) is not angular area \(E\); see Sections 4–5. |

For Wegner, scaling centers by two gives the disk hull \(2K+B_1\), with area
\(4A_K+2P+\pi\). Substitution in Theorem 1.1 and division by four gives the
table's formula. Combining it with Oler yields exactly

\[
 \mathscr O:=A_K+c_0P-a_0(N-1)
 \ \ge\ c_W[W_N-P]_+ .                              \tag{2}
\]

It does not state the required \(\mathscr O\ge c_0P\).
On the scalar leading-density/round-perimeter scale
\(N/D^2\to\pi/(2\sqrt3)\), \(P/D\to\pi\), the right side of (2), divided
by \(D\), tends to
\(c_W(\sqrt{2\pi\sqrt3}-\pi)\), whereas the target is \(c_0\pi\).
The two coefficients are about 0.01053815 and 1.36034952 respectively (decimal
evaluations for orientation; the displayed exact expressions are the claims).
A larger true surplus is possible; the
displayed bound alone does not establish it. This calculation does not claim
a geometric counterexample satisfying globality.

Downloaded source identities, for reproducing this reading rather than adding
private dependencies: separable PDF SHA-256
`b351551cd14a2ca470b587328e15e2a7fe4709be5f592dff707dc5b94909edc0`;
De Luca–Friesecke PDF SHA-256
`8267a485cf8e6c196c9a4079baa9097184e9c8dc67dbfb61a0d2060b08b10623`.
Wegner was accessible through the web PDF reader; direct local download returned
HTTP 403, so no local hash or downloaded-copy replay is claimed for it.

## 3. Independent reconstruction of the separable subcase

Total separability means that any two disks can be separated by a line avoiding
the interiors of **all** disks. For a finite totally separable radius-\(1/2\)
disk packing with center set \(A\), define
\(F(L)=\operatorname{area}(L)+\operatorname{per}(L)/2+1\) on convex sets.
Perimeter of a segment is twice its length. We prove \(F(K)\ge N\).

Induct on \(N\); the one-center case is immediate. Choose a separating line
with nonempty center sets on both sides, rotate it to \(y=0\), and note that
every center has \(|y|\ge1/2\). For a two-dimensional convex container \(L\)
containing the centers, cut at \(y=\pm1/2\). Call its upper/lower pieces
\(L_+,L_-\) and the two chord lengths \(\ell_+,\ell_-\).
The strip contains the trapezoid joining these chords, so its area is at least
\((\ell_++\ell_-)/2\). The two side arcs of the container across the strip
have total length at least 2. Therefore

\[
 \begin{aligned}
 A(L)&\ge A(L_+)+A(L_-)+(\ell_++\ell_-)/2,\\
 P(L)&\ge P(L_+)+P(L_-)-\ell_+-\ell_-+2,\\
 F(L)&\ge F(L_+)+F(L_-).
 \end{aligned}                                                   \tag{3}
\]

The convex hulls of the two center subsets lie in \(L_+,L_-\).
Area and perimeter are monotone for convex planar sets, and each subpacking is
totally separable. Induction gives the last two terms at least \(N_+,N_-\).
Use \(L=K+\varepsilon B_1\) and pass to \(\varepsilon\downarrow0\) if a
chord, a piece, or the original hull degenerates. This proves the required
special case, including collinear centers:

\[
                  N\le A_K+P/2+1.                         \tag{4}
\]

Now suppose the same **full** source is a global diameter minimizer, put
\(u=N-1>0\), and apply isodiametry, \(P\le\pi D\), and the complete
Section-36 strict lattice bound. Equation (4) gives

\[
 u\le \pi D^2/4+\pi D/2
   < a_0u+\frac{\sqrt{2\pi\sqrt3}}2\sqrt u.
\]

Consequently

\[
 u<\frac{2\pi\sqrt3}{4(1-\sqrt3/2)^2}
   =\pi(24+14\sqrt3)<\frac{15928}{105}<152.              \tag{5}
\]

The rational upper bound uses \(\pi<22/7\) and \(\sqrt3<26/15\).
Thus **\(N\ge153\) excludes total separability for every global minimizer**.
No triangle-free, jammed, simply connected, or no-isolate hypothesis was used.
This is a sufficient cutoff, with no optimality assertion.
It supplies a genuine global subcase implication; it does not prove that the
remaining nonseparable minimizers contain a unit triangle.

### Quantitative deletion and partition consequences

If \(S\subseteq A\) is any totally separable subset of a global minimizer and
\(k=N-|S|\), apply (4) to \(S\), then use its hull's area/perimeter bounds
at diameter at most \(D\). This yields the exact necessary inequalities

\[
\begin{aligned}
 k&\ge N-1-\pi D^2/4-\pi D/2,\\
 k&>(1-a_0)(N-1)-\frac{\sqrt{2\pi\sqrt3}}2\sqrt{N-1},\\
 k&>\kappa D^2-\pi D/2,
 \qquad \kappa=\frac{\pi(2\sqrt3-3)}{12}>0.
\end{aligned}                                         \tag{5a}
\]

The last line uses \(N-1>\pi D^2/(2\sqrt3)\), the same strict lattice
bound. Thus \(k\ge(1-a_0-o(1))N\) along any unbounded global-minimizer
sequence. This is an analytical statement about every subset, not an
authorization to discard labels from a source or a proposed competitor.
In particular, deleting only \(O(D)\) labels cannot make the source totally
separable for large \(D\).

For a second version, partition \(K\) into \(r\) convex cells of positive
area with disjoint interiors. Assign every source label to exactly one incident
cell, assume its assigned disks form a totally separable packing, and let \(T\)
be the total internal interface length, counted once. Equation (4), also valid for any
convex container by area/perimeter monotonicity, gives

\[
 N\le\sum_i A_i+\frac12\sum_i P_i+r
   =A_K+P/2+T+r.
\]

Since \(A_K<a_0(N-1)\) for a global source,

\[
 T+r>(1-a_0)(N-1)+1-\pi D/2
     >\kappa D^2+1-\pi D/2.                             \tag{5b}
\]

Consequently a convex total-separability partition with
\(T+r=O(D)\) is unavailable on large global sources. This is restricted to
the stated kind of cells. Canonical coherent grains are **not** known to be
totally separable, nor to form this convex partition; no general grain
decomposition is ruled out.

## 4. Exact unbounded witness to the missing hypotheses

For every integer \(m\ge2\), set

\[
 c_m=\frac{m^2-1}{2m^2},\quad s_m=\sqrt{1-c_m^2},\quad
 u=(1,0),\quad v=(c_m,s_m),\quad
 A_m=\{iu+jv:0\le i,j\le m\}.
\]

All squared pair distances are rational:
\(q(a,b)=a^2+b^2+2c_mab\), \(|a|,|b|\le m\).
If one coordinate vanishes, the shortest nonzero vectors are the four unit
axis steps. If both are nonzero, then

\[
 q(a,b)\ge(1-c_m)(a^2+b^2)\ge2(1-c_m)>1.
\]

Hence the complete contact graph is the square grid, with no triangle and no
contact isolates. Its \(R=m^2\) bounded faces are strict unit rhombi, and

\[
 N=(m+1)^2,\quad e=2m(m+1),\quad B=P=4m,\quad
 t=0,\quad\chi=1,\quad G=0.
\]

The angular surplus is positive but uniformly bounded:

\[
 E=\mathscr O=m^2(s_m-a_0)
  =\frac{1/2-1/(4m^2)}{s_m+a_0}
  <\frac1{2\sqrt3}.                                      \tag{6}
\]

The desired right side of (1) is \(c_0B=\sqrt3m\).
Thus even a regular pure rhombic disk with no isolated or omitted labels and
arbitrarily small relative Oler defect need not have the required surplus.

Already the three labels \(0,u,v\) disprove total separability. The only line
separating the tangent radius-\(1/2\) disks at \(0,u\) is \(x=1/2\).
Its distance from \(v\) is \(1/(2m^2)<1/2\), so it intersects the third disk's
interior. This is an obstruction in actual coordinates, not in an abstract
contact graph.

The diameter is attained by the long diagonal and satisfies
\(D_m^2=2m^2(1+c_m)=3m^2-1\): the positive-definite pair quadratic attains
its maximum over the difference square at a corner, with matching signs
maximal because \(c_m>0\). Replace each label \((i,j)\) by the square-grid
point \((i,j)\). Every lower pair bound is preserved and the new maximum
squared distance is \(2m^2<3m^2-1\). This is an explicit same-cardinality
strict competitor. **Every witness here is nonglobal**; no jamming or global
source-normal-form property is asserted.

There is also no contact-energy transfer: moving the same labels instead to
the triangular basis \((1,0),(1/2,\sqrt3/2)\) preserves separation and gains
exactly \(m^2\) short-diagonal contacts. Thus \(A_m\) is not an HR minimizer.
That move increases its long diagonal, illustrating why contact-energy
improvement is insufficient for minimum diameter.

## 5. Topology and the crystallization defect

On the disk in Section 4, the contact-graph defect is \(\mu=R=m^2\),
\(P_g=B\), and \(\chi_g=1\). The HR identity becomes

\[
 -e=-3N+B+3+R,
\]

which follows immediately from \(N=R+B/2+1\) and \(e=2R+B/2\).
It provides no extra metric payment. Equation (6) gives
\(E/\mu\to0\), so a uniform \(E\ge c\mu\), \(c>0\), is false even in
these regular triangle-free rhombic disks. The graph changes discontinuously
at the limiting 60-degree angle: short diagonals then become actual unit
contacts. A small metric perturbation can therefore preserve a large bond
defect without a comparable angular area cost.

For an explicit topology check, restrict to a connected regular rhombic
complex with \(h\) disjoint simple holes, no wires, no source labels outside
the complex, and no additional contact edges. Let hole \(j\) have \(k_j\)
boundary edges. The contact graph fills each hole as a bounded face in the
paper's convention. Accordingly

\[
 \chi_{\mathcal R}=1-h,\quad\chi_g=1,\quad
 P_g=B_{\rm out},\quad\mu=R+\sum_j(k_j-3).
\]

Substitution gives
\(-e=-3N+B+3\chi_{\mathcal R}+R\), again just the same edge/Euler
identities. Replacing \(\chi_g\) by \(\chi_{\mathcal R}\) in the original
formula loses \(3h\). The checker includes the 3-by-3 rhombic disk with its
central face omitted: \((N,e,R,B_{\rm out},B_{\rm holes},h)=(16,24,8,12,4,1)\).

This does not replace the metric hole payment. The existing
[HA proof](target_b_phase_cut_and_biclique_2026-09-05.md), Section 4, assumes
an edge-aligned hole tiled by unit rhombi; connected dual adjacency gives
\(r_H\ge(b_H-2)/2\), hence
\(G_{\rm holes}\ge c_0B_{\rm holes}-a_0h\). Its outer-boundary,
exceptional-face, disconnected-source and outside-label gaps remain visible.
The downstream [GPI dependency audit](target_b_dense_grid_penetration_interpolation_dependency_audit_2026-09-11.md)
likewise retains its dominant coherent-component hypothesis; none of the
imports above globalizes it.

## 6. Reproduction, credit, and verification ownership

Run from the repository root:

```sh
python research/verify_target_b_separable_literature_2026_10_17.py
python -O research/verify_target_b_separable_literature_2026_10_17.py
python tools/check_public.py
git diff --check
python tools/local_ci.py --base-ref origin/main
```

The checker uses Python's standard library and exact rational arithmetic.
It checks every possible full-patch difference for \(m=2,\ldots,64\), both
source and square competitor; a separate label-pair enumeration for
\(m=2,\ldots,12\) checks contacts and triangles. It verifies the rational
cutoff bound, surplus numerator, separating-line obstruction and topology
substitution. Failure controls cover a unit triangle at \(c=1/2\), overlap
at \(c=3/4\), and the wrong hole Euler characteristic. The normal and optimized
runs both passed: 63 source/competitor sizes and 44,220 independently enumerated
label pairs. Its finite success is not a proof of the all-\(m\) arguments,
external theorems, or global optimality.
Actual execution results are recorded with the submitted commit in the PR.
Required repository-wide theorem-certificate replay is **deferred to the
merging agent**; the scope planner is not a full-verification pass.

Predecessor credit: Groemer/Oler and Wegner for the finite packing inequalities;
Böröczky–Ruzsa for the primary transcription; Bezdek–Lángi for the separable
analogue; Heitmann–Radin and De Luca–Friesecke for crystallization and the
energy identity. The existing repository Wegner report already contains (2).
The Target B shared shell module, Sections 21 and 36, supplies the exact
topology and strict global upper bound. The
[earlier restoration audit](../audits/target_c_one_pin_restoration_gap_capacity_plateau_independent_audit_2026-10-10.md)
already uses exact triangular-patch Oler equality; the
[seamed-grain regression](target_b_seed084_near_disk_seamed_grain_regression_2026-10-13.md)
is a stronger pre-existing near-disk obstruction in a different class.
The grid here is a simple standard control, with no priority claim.

OpenAI Codex (GPT-6 agent) performed the source reading, independent disk-case
proof reconstruction, arithmetic derivations and checker implementation.
No independent second-agent audit has occurred. New claims remain unreviewed;
no canonical lifecycle or priority revision is changed.

## Open next questions

1. **Approximate separability with paid failures.** Can a source-derived
   separating-line decomposition of a canonical triangle-free jammed source
   retain (3) with total loss strictly below the gap to the global area bound?
   Equations (5a)–(5b) preclude repairing this by boundary-order deletion or a
   convex totally separable partition with boundary-order interface and count.
   First write the exact strip ledger for one actual nonseparable triple and
   its adjacent rhombi, including repeated disk charges. The obstruction is
   that the near-triangular family has quadratically many missing diagonals
   but bounded \(E\); contact counts alone cannot pay these failures.
2. **Outer-boundary transfer.** After HA pays its specified holes, obtain a
   source-specific joint estimate for outer boundary, multiple grains and
   all \(t\) outside labels that implies (1). First identify a globality or
   jamming input excluding the explicit square-competing patch. The present
   literature imports supply neither that input nor the full shell estimate.
