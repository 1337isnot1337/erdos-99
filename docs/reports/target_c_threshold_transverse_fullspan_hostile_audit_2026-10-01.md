<!-- theorem-state: {"artifact_id":"ART-F12EEDA44B96","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II -- hostile audit of the threshold transverse full-span lift

**Date:** 2026-10-01
**Starting commit:** 78a65968d51af7871a0ce5a865bf2db1a2c2e0ec
**Mission:** hostile audit of the threshold exact-phase staircase / opposite-shore full-span claim
**Primary candidate:** PR #603, target_c_threshold_transverse_fullspan_dichotomy_2026-10-01.md
**Cross-check:** PR #605, target_c_threshold_side_fiber_and_transverse_support_2026-10-01.md
**Classification:** audited-working conditional theorem; no canonical promotion claimed
**LEVEL I STATUS:** STILL OPEN. C-II remains open.

candidate lemma -> exact canonical quantity -> contradiction / strict competitor / Level I consequence

The candidate lemma is the disputed host-coherence step:

> If an edge of the threshold paired staircase has both gap endpoints in interior
> A-layers, then both selected physical diameter representatives are full-span on
> the opposite complete B-shore.

The exact quantity is the number N_full^B of actual diameter rows with full
B-support. The audit result is **PASS**. The only delicate point is that the train
crosscuts live in the resolved outer-face disk while the physical labels L_j,U_j
are convex-hull source vertices. Once that transfer is stated in terms of cyclic
order, the full-span conclusion is exact.

## 1. Dependencies and scope

Canonical dependencies used for the ambient source are only:

- every actual diameter endpoint is an extreme source-hull vertex;
- actual diameter chords form a convex geometric thrackle;
- the full source is retained.

The audited application additionally uses these proof-only October 1 inputs from
current main:

1. the fixed-star complete O--O rectangle;
2. its four-host boundary decomposition;
3. exact laminar interval support for diameter rows;
4. the threshold exact-phase paired staircase on the A-shore;
5. the physical representatives L_p U_q and L_q U_p over every simple staircase edge.

The opposite-shore rank theorem is used only for the final edge-count corollary.
No claim from PR #603 or PR #605 is assumed when proving host coherence.

The older C97 terminal-twist audit is a provenance cross-check for the standard
outer-boundary / convex-hull cyclic-order fact. The needed argument is repeated
below.

## 2. Boundary objects must be kept distinct

Let

\[
A=\{\tau_1,\ldots,\tau_m\},\qquad
B=\{\sigma_1,\ldots,\sigma_n\}.
\]

On the resolved outer-face boundary the four host intervals occur cyclically as

\[
I_A^+,\ I_B^+,\ I_A^-,\ I_B^-.
\tag{2.1}
\]

Every A-crosscut joins I_A^+ to I_A^- and every B-crosscut joins I_B^+ to I_B^-.
Endpoint resolution is chosen away from source vertices.

Let \(\ell_A\) be the A-layer. On the two B-host intervals, \(\ell_A\) is
constant at the two extreme values 0 and m. Symmetrically, the B-layer \(\ell_B\)
is constant at opposite extreme values 0 and n on I_A^+ and I_A^-.

In the threshold branch there is an actual full-support diameter h_0=za.
The paired-staircase report splits the **convex-hull boundary** at z,a into two
source-hull arcs L,U, both directed from A-layer 0 to A-layer m.

These hull arcs are not literally the two resolved outer-face paths: an outer path
may contain non-hull vertices, bridge occurrences, or pocket vertices. Only cyclic
order is needed.

### Lemma 2.1 -- outer-path to hull-arc transfer

Let P_L,P_U be the two resolved outer-boundary paths from z to a. Restrict each
path to its extreme source vertices. The resulting two ordered subsequences are
exactly the two convex-hull arcs L,U, up to swapping their names.

### Proof

Every extreme source vertex lies on the unbounded face of the straight-line contact
embedding. Extreme vertices occur there in the same cyclic order as on the convex
hull; otherwise hull chords between consecutive extreme vertices would have
alternating boundary order and would cross the outer-face embedding. Resolving train
endpoints away from source vertices does not change that order. Deleting non-extreme
boundary occurrences from the two z-to-a paths therefore gives the two convex-hull
arcs. \(\square\)

No simple outer boundary is assumed. Repeated non-hull occurrences are harmless
because the statement is only about the extreme-vertex subsequence.

## 3. Interior host coherence

### Theorem 3.1

After possibly swapping I_A^+ and I_A^-, every extreme source vertex on L with
A-layer in \(\{1,\ldots,m-1\}\) lies in I_A^+, while every extreme source vertex
on U with interior A-layer lies in I_A^-.

### Proof

Because h_0=za has full A-support, every selected A-crosscut separates z from a.
Thus each outer-boundary path P_L,P_U contains exactly one resolved endpoint of
every selected A-crosscut.

Along either path the A-layer starts at 0, ends at m, and changes by one when the
path passes the appropriate A-crosscut endpoint. With the z-to-a orientation it is
therefore nondecreasing.

By (2.1), moving on the boundary from one A-host interval to the other necessarily
passes through a B-host interval. A B-host interval has constant A-layer 0 or m.
A nondecreasing 0-to-m path can therefore change A-hosts only while still on its
initial 0-plateau or after reaching its terminal m-plateau. Every portion carrying
an interior A-layer lies in one A-host interval.

The two paths use opposite A-hosts for their interior portions. For each selected
A-crosscut, one endpoint is on P_L and the other on P_U, while its two endpoints
lie on opposite A-host intervals. Lemma 2.1 transfers the conclusion from the
resolved outer paths to the convex-hull arcs L,U. \(\square\)

This does **not** assert that all of L or U lies in one A-host interval. Layer-0
and layer-m plateaus may extend into B-host intervals or A-host tails.

## 4. Internal staircase representatives are B-full-span

Take a simple threshold staircase edge \(\{p,q\}\) with

\[
0<p<q<m.
\]

The paired-staircase theorem supplies two distinct actual diameter bars

\[
h_1=L_pU_q,\qquad h_2=L_qU_p.
\tag{4.1}
\]

By Theorem 3.1, each L-endpoint lies in one A-host interval and each U-endpoint
lies in the other. On these two A-host intervals the B-layer is constant at
opposite extreme values 0,n. Hence both rows in (4.1) have B-layer endpoints 0,n.

Exact laminar interval support on the B-shore gives

\[
\boxed{
\operatorname{supp}_B(h_1)
=
\operatorname{supp}_B(h_2)
=
\{1,\ldots,n\}.
}
\tag{4.2}
\]

Thus every internal simple staircase edge contributes two distinct actual
B-full-span diameter rows. If e_int is the number of simple staircase edges with
both gap endpoints interior,

\[
\boxed{N_{\rm full}^B\ge 2e_{\rm int}.}
\tag{4.3}
\]

This validates the strongest disputed assertion of PR #603.

## 5. Relation to PR #605

For an internal A-support interval (p,q], the signed A-incidence has two internal
switches, so t_A(h)=2. Current main gives

\[
t_A(h)+t_B(h)\le2,
\]

hence t_B(h)=0. That inequality alone permits either empty or full B-support.

PR #605 is therefore correct but non-sharp for the specifically identified paired
internal threshold representatives. Their physical endpoint locations select the
full-support alternative. The upgrade (4.2) uses the four-host topology plus exact
laminar support; it does not require the numerical joint-switch inequality.

## 6. Edge-budget corollary

The opposite-shore rank theorem gives

\[
N_{\rm prop}^B\ge n-2,
\]

or \(n-1\) if B is exact phase. Full-support and nonempty proper-support rows are
disjoint, so (4.3) gives

\[
\boxed{h\ge n+2e_{\rm int}-2,}
\tag{6.1}
\]

and in the exact-B case

\[
\boxed{h\ge n+2e_{\rm int}-1.}
\tag{6.2}
\]

Thus the edge-budget conclusions in PRs #603 and #605 survive. The audit identifies
the 2e_int excluded rows as genuinely B-full-span, rather than merely B-nonswitching.

## 7. Boundary-fan formula

The staircase equality case has

\[
a_i=i-1,\qquad B_i=\{t_i,\ldots,t_{i-1}\},\qquad t_0=m,
\]

so \(\{0,m\}\) is a simple edge.

A proper edge \(\{0,b\}\), b<m, and a proper edge \(\{a,m\}\), a>0, cannot coexist:
antitonicity with 0<a would force b>=m. Therefore all proper boundary-touching
simple edges form one fan side.

If f is their number,

\[
e_{\rm int}+f=m-1.
\tag{7.1}
\]

Combining with (6.1),

\[
\boxed{
f\ge \frac{2m+n-h-4}{2}.
}
\tag{7.2}
\]

This part of PR #605 also passes.

## 8. Side-fiber bookkeeping cross-check

PR #605 defines side-resolved fiber counts n_{X,j}, genuine side-split excess

\[
S=\sum_{X\in\{L,U\}}\sum_{j=0}^m(n_{X,j}-1),
\]

the overlap count o at z,a, and r_0, the number of literal h_0 endpoints already
present in the paired graph.

Its forest counts

\[
c_{\rm pair}=2+S-o,\qquad
c_0=3+S-o-r_0
\tag{8.1}
\]

are exact: the selected common-cut diameter graphs are bipartite, and a bipartite
subgraph of the convex diameter thrackle has no cycle.

Consequently

\[
\sum_{j=0}^m(n_j-1)=m+c_0.
\tag{8.2}
\]

Subtracting the mandatory two-sided contribution in the interior layers gives the
PR #603 residual identity

\[
(n_0-1)+(n_m-1)+\sum_{j=1}^{m-1}(n_j-2)=c_0+1.
\tag{8.3}
\]

The two reports are therefore algebraically compatible.

The global side-split upper budget in PR #605 also checks:

\[
S\le q-2m-4+o+r_0\le q-2m.
\tag{8.4}
\]

No contradiction follows from (8.4) at the current extraction constant.

## 9. Adversarial checks and failed stronger claims

1. **Boundary mismatch:** resolved by Lemma 2.1. No source point is deleted; only
   the cyclic order of extreme vertices is extracted.
2. **Endpoint plateaus:** the host-coherence theorem is restricted to interior
   A-layers. Extending it to layer 0 or m is unjustified.
3. **Nonswitching in general:** t_B=0 does not imply full support for an arbitrary
   row. The full-span upgrade uses the named physical representatives L_pU_q and
   L_qU_p.
4. **Raw fiber count:** the current-main quantity sum(n_j-1)=m+c_0 includes a
   mandatory doubled-side baseline. It is not itself Omega(D) new side-fiber defect.
5. **No row-count closure:** a linear antitone family of B-full-span diameter chords
   between opposite host intervals is abstractly compatible with convex-thrackle
   order. A unit-contact co-embedding or finite source move is still required.

## 10. Current implication chain and remaining gap

The audited threshold chain is

\[
\text{threshold paired staircase}
\Longrightarrow
\begin{cases}
\text{exact side-fiber accounting},\\
\text{every internal staircase edge gives two B-full-span diameters},\\
N_{\rm full}^B\ge2e_{\rm int},\\
h\ge n+2e_{\rm int}-2,\\
\text{or a one-sided boundary fan}.
\end{cases}
\]

The next obligation is source-geometric:

1. eliminate a linear family of actual B-full-span diameter bars coexisting with
   the opposite strict-rhombus contact grid and its proper-support rows; or
2. eliminate the one-sided threshold boundary-fan regime while retaining physical
   endpoint fibers.

Either route still has to produce an exact unit triangle or a same-cardinality
strict sub-D source. Split-star, inactive-interface, open-cell exact phase,
nonconstant phase, and macroscopic inactive-container branches remain open.

## 11. Audit disposition

- PR #603 host-coherence lemma: **PASS**, after explicit outer-boundary/hull-order transfer.
- PR #603 transverse full-span theorem: **PASS**.
- PR #603 edge-budget and staircase-degree formulas: **PASS**.
- PR #605 side-fiber accounting and S<=q-2m: **PASS**.
- PR #605 t_B=0 conclusion: **PASS but non-sharp** for paired internal rows; they are B-full-span.
- C-II / Level I: **OPEN**.

No computation, numerical experiment, verifier, external literature, or canonical
state edit is used in this audit.


## 12. Live-main and threshold--threshold continuation

While this audit was being written, main advanced to fbeae9b3 with
target_c_threshold_transverse_rail_saturation_2026-10-01.md. That report states the
same interior-host / opposite-rail theorem audited in Sections 2--4. The present
report therefore also functions as an independent audit of that newly merged
proof-only main result; it does not change its lifecycle status.

PR #605 also added a threshold--threshold overlap bound. Let H_0^A and H_0^B be the
two selected paired threshold systems. Partition each by its switch count on its own
shore:

\[
|A_2|=2e_{\rm int}^A,\quad |A_1|=2f_A,\quad |A_0|=3,
\]
\[
|B_2|=2e_{\rm int}^B,\quad |B_1|=2f_B,\quad |B_0|=3.
\]

For an edge shared by the two selected systems, the same physical row satisfies

\[
t_A(h)+t_B(h)\le2.
\]

If the shared row lies outside \(A_0\cup B_0\), both switch counts are positive,
hence they are exactly \(t_A=t_B=1\). Therefore

\[
H_0^A\cap H_0^B
\subseteq
A_0\cup B_0\cup(A_1\cap B_1),
\]

and consequently

\[
|H_0^A\cap H_0^B|
\le 6+2\min(f_A,f_B).
\tag{12.1}
\]

Since \(|H_0^A|=2m+1\) and \(|H_0^B|=2n+1\),

\[
\boxed{
h\ge2m+2n-4-2\min(f_A,f_B).
}
\tag{12.2}
\]

This argument is exact. No hidden assumption about physical endpoint disjointness is
used; it counts actual diameter edges and allows arbitrary reuse consistent with the
joint switch inequality.

The host-localization continuation in PR #605 is weaker than the audited theorem.
From \(t_A=2\) alone one may classify a row as B-empty when its endpoints occupy the
same A-host and B-full-span when they occupy opposite A-hosts. But the actual paired
internal representatives are \(L_pU_q,L_qU_p\), and Sections 2--4 prove their
interior L/U endpoints occupy opposite A-hosts. Thus the B-empty alternative does not
occur for these named paired rows. It remains a legitimate abstract classification
for an unidentified row with \(t_A=2\), not an escape for the paired staircase lift.

Audit disposition for the live continuation:

- threshold--threshold overlap bound (12.2): **PASS**;
- same-host / opposite-host abstract classification: **PASS but non-sharp**;
- B-empty paired internal threshold representative: **excluded by host coherence**;
- no new Level I or C-II closure follows from the overlap count at current constants.


## 13. New strengthening: corner-localized threshold--threshold reuse

The overlap estimate (12.1) can be sharpened using the corner-localization clause of
the current joint switch theorem together with the physical pairing of each boundary
fan edge.

Let

\[
C:=A_1\cap B_1.
\]

Every row in C switches once on each shore. The joint switch theorem says all such
shared-switch diameter rows occupy at most two adjacent corner types among

\[
(A^+,B^+),\ (A^+,B^-),\ (A^-,B^+),\ (A^-,B^-).
\]

Hence all rows in C share one common host interval: either one A-host or one B-host.

Now fix one proper boundary-fan edge of the A staircase. It is either \(\{0,j\}\)
or \(\{j,m\}\) with \(1\le j\le m-1\). Its two paired physical representatives
have their unique A-switching endpoints at \(L_j\) and \(U_j\). By Theorem 3.1
these lie on opposite A-host intervals. Therefore, for either fixed A-host,
**at most one** of the two representatives over that fan edge switches there.
Summing over the f_A fan edges, exactly f_A selected A_1 rows switch on each A-host.

Symmetrically, exactly f_B selected B_1 rows switch on each B-host.

If the two adjacent corner types supporting C share an A-host, then

\[
|C|\le f_A
\]

(and of course \(|C|\le2f_B\)). If they share a B-host, then

\[
|C|\le f_B
\]

(and \(|C|\le2f_A\)). Therefore

\[
\boxed{
|A_1\cap B_1|
\le
g(f_A,f_B)
:=
\min\!\bigl(
\max(f_A,f_B),\,
2\min(f_A,f_B)
\bigr).
}
\tag{13.1}
\]

Indeed, if \(f_A\le f_B\), the worst of the two possible common-host orientations is

\[
\max\{f_A,\min(f_B,2f_A)\}
=
\min(f_B,2f_A),
\]

which is (13.1).

Rows shared by the two selected threshold systems but outside C must lie in
\(A_0\cup B_0\), whose union has at most six actual edges. Thus

\[
\boxed{
|H_0^A\cap H_0^B|
\le
6+g(f_A,f_B).
}
\tag{13.2}
\]

Taking the union gives the strengthened two-threshold diameter budget

\[
\boxed{
h
\ge
2m+2n-4-g(f_A,f_B).
}
\tag{13.3}
\]

This improves PR #605 equation (22), which subtracts \(2\min(f_A,f_B)\), whenever
the two fan sizes are within a factor of two. In particular, when \(f_A=f_B=f\),
the overlap penalty drops from \(2f\) to \(f\).

A convenient coarser symmetric form follows from

\[
g(f_A,f_B)\le\frac23(f_A+f_B).
\]

Using
\(f_A=m-1-e_{\rm int}^A\) and
\(f_B=n-1-e_{\rm int}^B\),

\[
\boxed{
3h
\ge
4(m+n)
+
2(e_{\rm int}^A+e_{\rm int}^B)
-8.
}
\tag{13.4}
\]

The proof is purely source-level incidence bookkeeping: it counts actual diameter
edges, uses the already proved physical L/U host separation, and permits arbitrary
endpoint sharing. No degree bound, KKT weight lower bound, or quotient-to-source
identification is used.

### Scope

Equation (13.3) is still not a contradiction at the current small complete-grid
extraction constant. It is a genuine tightening of the double-threshold branch,
not a Level I closure. The next source-geometric step remains to exploit the actual
strict-rhombus co-embedding or positive source equilibrium, rather than another
unweighted row count.
