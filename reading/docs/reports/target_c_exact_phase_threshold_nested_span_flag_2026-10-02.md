> Generated reading edition · [exact source](../../../docs/reports/target_c_exact_phase_threshold_nested_span_flag_2026-10-02.md) · source SHA-256 `6cc69041e80928e5bfcf6e752d9579268793167b9a7189565c9721ef52015e5e`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-5A449FE55F8F","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II -- threshold staircase is a nested span flag

Date: 2026-10-02
Base main: e85d3270b7ed5f99fb0d9fd80ecc89100898e9b2
Status: proof-only strengthening of the threshold exact-phase branch; C-II remains open.

Dependencies:
- docs/reports/target_c_exact_phase_threshold_paired_staircase_2026-10-01.md
- docs/reports/target_c_threshold_transverse_fullspan_hostile_audit_2026-10-01.md
- docs/reports/target_c_global_diameter_star_cubic_budget_2026-10-02.md

## Theorem

Let T be the simple gap tree on the ordered vertices 0,...,m supplied by the
threshold exact-phase paired-staircase theorem. For a simple edge e={a,b},
a<b, write

    I(e)=[a,b],   ell(e)=b-a.

Then the m simple staircase intervals form one strict inclusion flag. There are
unique edges e_1,...,e_m such that

    ell(e_r)=r

and, writing I_r=I(e_r)=[L_r,R_r],

    I_1 proper-subset I_2 proper-subset ... proper-subset I_m=[0,m].
                                                            (1)

For every 1<=r<m, exactly one endpoint is added:

    (L_(r+1),R_(r+1))=(L_r-1,R_r)

or

    (L_(r+1),R_(r+1))=(L_r,R_r+1).                         (2)

Thus the quotient tree has an exact extreme-peeling description. Starting from
the unique length-one edge, each larger-scale edge adds one new extreme gap
vertex and joins it to the opposite old extreme. Reversing the construction,
one extreme vertex is a leaf at every stage.

Let e_int be the number of simple staircase edges with both endpoints in
{1,...,m-1}. Then:

1. the internal edges are exactly e_1,...,e_(e_int);
2. their A-support lengths are exactly 1,...,e_int;
3. the boundary-touching edges are exactly e_(e_int+1),...,e_m, so their
   A-support lengths are exactly e_int+1,...,m;
4. one of the original extremes 0,m is a leaf of T, and every proper
   boundary-touching edge is incident to the other extreme;
5. if j_* is that fan center, then

       deg_T(j_*) = m-e_int.                                (3)

The hostile-audited transverse full-span theorem therefore becomes
span-resolved. For every 1<=r<=e_int, both selected physical diameter
representatives over e_r have exact A-support length r and full support on the
opposite retained shore B={sigma_1,...,sigma_n}. Consequently, for the selected
internal representatives H_int^sel,

    sum_(h in H_int^sel) |supp_A(h)|
      = 2 sum_(r=1)^(e_int) r
      = e_int(e_int+1),                                    (4)

while

    sum_(h in H_int^sel) |supp_B(h)|
      = 2 e_int n.                                         (5)

Every one of these rows also crosses the unique common A-train.

Hence the previous threshold fork sharpens as follows.

- If e_int>=m/2, then for every 1<=r<=floor(m/2) there are two selected actual
  diameters with exact A-span r, full B-support, and strictly nested A-supports.
  Thus the full-opposite-support packet is not an arbitrary linear family: it
  contains one paired support type at every short scale through m/2.

- If e_int<m/2, then one extreme A-layer is incident to exactly
  2(m-e_int)>m selected diameter-edge incidences. This is stronger than the
  previous degree-pigeonhole input and localizes all long support scales to one
  extreme fan. Combining it with the current full-source cubic diameter-star
  incidence theorem gives the same square-root carrier order with the sharper
  packet size J=2(m-e_int), rather than the older J>m/2 input.

No closure is claimed.

## Proof

The paired-staircase theorem gives the antitone rule: for distinct simple
edges (a,b),(c,d), with a<b and c<d,

    a<c  implies  b>=d.                                    (6)

Take any two distinct simple edges and suppose a<=c. If a<c, (6) gives

    [c,d] subset [a,b].

If a=c, their right endpoints differ, so one interval strictly contains the
other. Therefore every two simple staircase intervals are comparable by strict
inclusion.

There are exactly m simple edges. Strict inclusion of integer intervals
strictly increases the integer length b-a. All lengths lie in {1,...,m}.
Therefore the m distinct lengths are exactly

    {1,2,...,m}.                                            (7)

This proves existence and uniqueness of e_r. The length-m interval is
necessarily [0,m], and (1) follows. Since consecutive lengths differ by one,
a strict inclusion I_r subset I_(r+1) can add exactly one adjacent integer gap
vertex. This is precisely (2).

The unique length-one interval is [s-1,s] for some s in {1,...,m}. It is
contained in every I_r, so every support interval (L_r,R_r] contains train
index s. Conversely the length-one support contains no other train. Thus
tau_s is the unique common retained train of the simple staircase family.

Now let T_r be the graph with edges e_1,...,e_r. We prove inductively that T_r
is a tree on the r+1 consecutive vertices of I_r. This is immediate for r=1.
By (2), I_(r+1) adds one new extreme vertex x to I_r. The new edge e_(r+1)
joins the two endpoints of I_(r+1), hence joins x to the opposite old extreme,
which belongs to T_r. Thus T_(r+1) is obtained from T_r by adding one leaf.
This proves the extreme-peeling description.

At the top scale I_(m-1) is either [1,m] or [0,m-1]. In the first case the
gap vertex 0 occurs only in e_m={0,m}, so deg_T(0)=1. In the second case
deg_T(m)=1. Once an original extreme disappears from the descending flag, it
cannot reappear at a smaller scale. Therefore the boundary-touching intervals
are exactly one terminal block of the flag. Equivalently, the internal support
types are exactly e_1,...,e_(e_int) and the boundary-touching types are the
remaining m-e_int edges.

After I_(m-1) removes one original extreme, every proper boundary interval can
touch only the other original extreme. Thus all proper boundary edges form one
fan, while e_m={0,m} also meets its center. The center degree is therefore
m-e_int, proving (3). This recovers the current boundary-fan count

    f=m-1-e_int

and strengthens it to the exact support-length stratification

    internal lengths:       1,...,e_int,
    boundary-fan lengths:   e_int+1,...,m.                 (8)

Current main's hostile-audited transverse theorem says that every internal
simple staircase edge contributes two selected actual diameter representatives
with full B-support. Applying it to the exact length set in (8) proves (4)-(5)
and the internal-heavy conclusion.

For the boundary-heavy conclusion, the fan center is incident to m-e_int
simple edges. Their paired physical lifts supply 2(m-e_int) distinct selected
diameter bars, each with one endpoint in that one extreme A-layer. This gives
the asserted incidence packet. The current additive cubic star theorem may
then be applied directly to its actual source carriers; no quotient vertex is
identified with a physical source vertex.

## Why this is new at the October threshold endpoint

The September chain-face reports already observed a length spectrum
{1,...,D} for the older exact C88 chain staircase. The current result is not
claimed as a new abstract fact about Ferrers staircases. Its contribution is
to transfer the exact total-inclusion/peeling structure to the October
threshold paired staircase and combine it with the now-audited opposite-shore
full-span theorem and source-wide star budget.

The resulting threshold normal form records, simultaneously:

- one paired actual-diameter support type at each scale 1,...,m;
- a binary left/right expansion word determining the entire simple gap tree;
- short scales exactly equal to the internal, full-opposite-support types;
- long scales exactly equal to one extreme boundary fan.

Those scale identifications are not present in the current threshold reports.

## Remaining bottleneck

Pure gap-tree combinatorics is now essentially exhausted. In the internal-heavy
branch, the source contains a nested ladder of paired actual diameters with
A-spans 1,...,floor(m/2), while every one spans the whole B-shore. In the
boundary-heavy branch, all long support scales are concentrated in one extreme
fan, with a linear actual-diameter incidence packet there.

The next useful theorem has to use source geometry omitted by the gap quotient:
the two quadratic populated threshold rail hulls, the strict-rhombus
co-embedding, positive source equilibrium, or a source-preserving strict
diameter decrease. A row-count or support-count refinement alone will not
close the branch.

This report is theorem/proof work only. No computation, numerical evidence,
verifier execution, CI result, or unexecuted verifier code is used.

## Recovery provenance — Slot 1, 2026-10-05

Copied to fresh `main` from `research/threshold-nested-span-flag-2026-10-02-r1` at exact tip `3b5f7498b09f01bf1dec8dd8d39fb07445265151`. This report remains an unreviewed, proof-only candidate; no theorem status or Target C route state is promoted. Its listed staircase, transverse-rail, and exact-multishear dependencies are present on the salvage base. The source artifact contains no verifier or computational certificate.
