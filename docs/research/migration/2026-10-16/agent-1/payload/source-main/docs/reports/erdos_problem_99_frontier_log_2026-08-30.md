<!-- theorem-state: {"artifact_id":"ART-299651E39599","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# Erdős Problem #99 — frontier log (2026-08-30)

This is a chronological working log for the current research run.  It is
subordinate to [`docs/canonical/erdos_problem_99_1.7.0.md`](../canonical/erdos_problem_99_1.7.0.md),
which remains the theorem-state document.  A result is recorded here only when
its hypotheses and constants have been checked against the canonical stack.

## Entry 1 — the super-boundary branch has a thick collar

Let \(N\) be the cardinality of a hypothetical triangle-free global minimizer,
let \(D=D(N)\), and let \(\rho\) be the retained strict-rattler count in the
Target A branch.  Put

\[
m=N-\rho,
\qquad d=D(m),
\qquad t=\frac{D-d}{2}.
\]

The canonical stack supplies the strict translated-lattice upper bound

\[
d^2<c,m,
\qquad c=\frac{2\sqrt3}{\pi},
\]

and the Oler/isodiametric lower bound

\[
D\ge \sqrt{c(N-1)+\frac34}-\frac{\sqrt3}{2}.
\]

The following quantitative refinement is immediate.

> **Lemma 1 (explicit collar-thickness bound).**  For every (m\ge2),
> 
> \[
> \boxed{
> D^2-d^2>c(\rho-1)-\sqrt3D.
> }
> \tag{1}
> \]
> Consequently
> 
> \[
> \boxed{
> t>
> \frac{c(\rho-1)-\sqrt3D}{4D}.
> }
> \tag{2}
> \]
> In particular, along every super-boundary sequence with
> \(\rho/D\to\infty\), one has \(t\to\infty\).

### Proof

Set

\[
x=c(N-1)+\frac34,
\qquad b=\frac{\sqrt3}{2}.
\]

The lower bound on (D) gives (\sqrt{x}\le D+b).  Hence

\[
\begin{aligned}
D^2-d^2
&>\left(\sqrt{x}-b\right)^2-cm\\
&=c(\rho-1)+\frac32-\sqrt3\sqrt{x}\\
&\ge c(\rho-1)+\frac32-\sqrt3(D+b)\\
&=c(\rho-1)-\sqrt3D.
\end{aligned}
\]

Since (d\le D),

\[
t=\frac{D^2-d^2}{2(D+d)}
\ge\frac{D^2-d^2}{4D},
\]

which proves both displayed inequalities.  The final assertion follows by
dividing (2) by (1) and using \(\rho/D\to\infty\).  \(\square\)

### What this does and does not buy

The lemma upgrades the source-side regime from a merely fixed-width collar to a
collar whose width diverges whenever the strict-rattler population is genuinely
super-boundary.  It does **not** close Target A: the safe-collar count still has
an uncontrolled boundary-order loss, and the desired statement is an exact
integer Hall surplus, not an asymptotic population estimate.  In particular,
the lemma cannot be used to replace the source-to-response theorem by a density
argument.

The next live question is whether a thick collar permits a *layered* exchange
argument: each additional unit-width annulus might contribute an independent
alternating obstruction, while the existing one-layer proof only exposes the
single (O(D)) boundary reserve.

## Entry 2 — exact multi-layer capacity for free homothetic strain

Let \(e_1,e_2\) be unit vectors with \(e_1\cdot e_2=1/2\). For
\(L\ge2\), \(\varepsilon>0\), and
\[
r=\lfloor\varepsilon(L-1)\rfloor,
\]
the strained patch
\[
P_{L,\varepsilon}
=(1+\varepsilon)\{ie_1+je_2:0\le i,j\le L-1\}
\]
has a hull containing the lattice patch
\[
Q_{L,r}=\{ie_1+je_2:0\le i,j\le L-1+r\}.
\]
The latter is unit-separated, has
\[
|Q_{L,r}|- |P_{L,\varepsilon}|=2Lr+r^2,
\]
and no larger diameter than the strained patch. Therefore one complete coordinate
layer gives \(2L+1\) extra sites, and \(r\) layers give \(2Lr+r^2\).

This is a new exact finite-capacity result, proved in canonical Section 141 and
checked by exact Fraction arithmetic in the research regression. It removes the
external Kuperberg dependency for this particular free rectangular candidate.
It still does not solve Target A: the candidate must be separated from all exterior
source points, and the actual coherent monomer domain is not known to be a
homothetic patch.

## External-status check

The official public record checked during this run still labels Problem #99
open.  No external source has been promoted into the canonical theorem stack.

## Entry 3 — exact nonuniform rectilinear capacity

The homothetic hypothesis can be removed for a coherent product domain.  For

\[
P=\{x_i e_1+y_j e_2:0\le i,j<L\}
\]

with consecutive coordinate gaps at least one, write

\[
r_1=\lfloor x_{L-1}-x_0\rfloor-(L-1),\qquad
r_2=\lfloor y_{L-1}-y_0\rfloor-(L-1).
\]

The translated integer triangular-lattice patch with those coordinate spans lies in
\(\operatorname{conv}P\), has no larger diameter, and gains exactly

\[
L(r_1+r_2)+r_1r_2
\]

sites.  A single accumulated layer in one coordinate therefore gives \(L\) sites;
the two-direction homothetic formula \(2Lr+r^2\) is a special case.  This is proved
as Theorem 142.1 in the canonical report and checked by exact Fraction arithmetic in
research/rectilinear_capacity.py.

The new statement is a finite, nonuniform protected-capacity theorem.  It advances
the gap-concentration route but leaves its decisive hypothesis visible: the integer
candidate must remain separated from all exterior points.  No source-derived
monomer domain is currently known to provide that protection, so Target A and the
Level I problem remain open.

## Entry 4 — the naive barycentric transport is falsified locally

I tested a possible direct route to the scaffold rank inequality: assign each
smaller-optimum point the ordinary barycentric weights of one incident unit
triangle and interpret those weights as a fractional matching to triangular-lattice
vertices.  This rule is not valid, even for triangle-free point sets.

Take three lattice directions separated by (120^\circ), and place points at

\[
p_i=\frac35 u_i.
\]

Their pairwise squared distances are (27/25>1), so the three-point set is
unit-separated and has no unit equilateral triangle.  In a chosen incident
triangle for each point, the barycentric coefficient of the common lattice vertex
is (1-3/5=2/5).  The total mass assigned to that one vertex is therefore

\[
3\cdot\frac25=\frac65>1.
\]

The conflict graph itself is not deficient: each point lies on a lattice-edge
interface with a four-site dimer neighborhood, and the three points can be matched
to distinct outer lattice vertices.  The failure is specifically the single-
triangle barycentric rule, which discards the extra dimer vertex.  The exact
calculation and regression are in
`research/local_hat_regression.py` and
`docs/reports/local_hat_matching_regression_2026-08-30.md`.

This closes off one attractive but incorrect proof shortcut.  Any fractional
source-to-lattice transport must retain the full monomer--dimer incidence or use a
different phase-aware weighting; a central-vertex hat-mass estimate cannot supply
the missing Schur nullity.

## Entry 6 — strict interior coverage for small-gap product patches

The rectilinear capacity instrument now has a source-side covering criterion.  For
each cell with coordinate gaps \(a_i,b_j\ge1\), set

\[
\sigma_{ij}=a_i^2-a_i b_j+b_j^2,
\]

the squared length of the short diagonal.  Splitting the cell along that diagonal
gives two triangles with side lengths
\(a_i,b_j,\sqrt{\sigma_{ij}}\).  If \(\sigma_{ij}<3\), their vertex covering
radius is \(<1\): in the acute case the circumradius is
\(\sqrt{\sigma_{ij}}/\sqrt3<1\), and in the obtuse case the half-longest-side
bound is \(<1\).  Hence the open product hull is covered by the open unit disks
around the product patch.

Therefore no additional unit-separated source point can lie in the patch interior;
all exterior blockers are forced to the product-hull boundary.  Equality is sharp:
a cell with side gaps \((\sqrt3,\sqrt3)\) has an interior circumcenter at distance
exactly one from three corners.  The exact implementation and threshold tests are
in `research/rectilinear_capacity.py`.

This is a genuine source-side bridge for coherent product domains, and it explains
why a sufficiently regular monomer patch would be exterior-protected after a finite
boundary buffer.  The actual Target A scaffold still supplies only local
monomer/dimer cells, not the global product structure or the small-gap condition, so
the Schur-rank/Hall-surplus endpoint remains open.
## Entry 5 — boundary-buffered finite exchange

The nonuniform rectilinear capacity theorem now has a protected-core consequence.
For a product patch with floor spans \(K_1,K_2\), retain only lattice candidates with
two coordinate steps from every side.  Each retained site is at least \(\sqrt3\) from
the product-hull boundary, so arbitrary exterior points cannot be strict conflicts.
The protected core has

\[
\bigl(K_1-3\bigr)_+\bigl(K_2-3\bigr)_+
=\bigl(L+r_1-4\bigr)_+\bigl(L+r_2-4\bigr)_+
\]

sites.  Four complete layers in both directions therefore suffice to leave an
\(L\times L\) replacement core; a one-sided square patch needs
\(\left\lceil4+4L/(L-4)\right\rceil\) layers.  For \(L=10\), the exact threshold is
eleven.

This is a finite gap-concentration transfer under explicit hull isolation.  It does
not yet apply to the actual Target A source because other source points may occupy
the product hull of a chosen monomer domain.  The Schur-rank/Hall-surplus endpoint
therefore remains open.

## Entry 7 — exact localized bad-cell hazard mask

The interior-covering criterion can be localized instead of requiring every
coordinate cell to be near-hexagonal.  Mark a cell bad when its short-diagonal
square \(\sigma(a,b)=a^2-ab+b^2\) is at least \(3\).  Strict-good cells are covered
by open unit disks at their four corners, so any additional unit-separated source
point in the product hull must lie in the union of the closed bad cells.

I added exact rational oblique-cell projections and a protected candidate mask:
integer lattice sites must be at least one unit from the product-hull boundary and
from every closed bad cell.  This gives a direct finite separation certificate for
all remaining source points.  The regression includes a \(15\times15\) patch with
one localized bad row: fourteen bad cells remain, but \(230>225\) protected sites
survive and the candidate diameter still fits.

This is a sharper finite gap-concentration instrument, not the missing scaffold
theorem.  Target A still needs a mechanism producing a large coherent product
region and proving that its bad-cell hazard mask leaves at least \(\Delta_\Lambda\)
usable sites (or otherwise supplies the Schur nullity).

## Entry 8 — cell-union localization of free sinks

The exact scaffold cells carry a further metric certificate. If \(x\) is a blocker
and \(C_x\) is the convex hull of its three or four strict conflict vertices, then

\[
C_x\subset B(x,1)
\]

by the triangle inequality and convex-combination coordinates. Therefore

\[
\Lambda\cap C_x=N_\Lambda(x),\qquad
\Lambda\cap\bigcup_xC_x=N_\Lambda(X).
\]

The free inner-lattice sinks are exactly the lattice sites in the geometric gaps of
the cell union, and they give the explicit lower bound

\[
h(G)\ge\left|Y_{\rm in}\setminus\bigcup_xC_x\right|.
\]

Thus a survivor with \(h(G)\le j-1\) has at most \(j-1\) lattice sites in those
gaps. This does not control long narrow lattice-hole-free strips or the residual
Hall routing, so the Schur-rank/Hall-surplus endpoint remains open. Exact triangle
centroid and lozenge-center margins are regression-tested in
`research/cell_union_certificate.py`.

## Entry 9 — exact degree-zero sink extraction

For every scaffold blocker \(x\), the complete local classification makes its
strict conflict cell \(C_x\) an elementary triangle or elementary lozenge.  The
convexity of the open unit disk around \(x\), together with the fact that these
cells contain no other lattice sites, gives the exact identity

\[
\Lambda_v\cap C_x=N_\Lambda(x).
\]

Consequently the sites in
\[
Y_{\rm free}=Y_{\rm in}\setminus\bigcup_x C_x
\]
are exactly the degree-zero vertices on the inner lattice shore.  Taking them as
a Hall witness gives the new bound
\[
h(G)\ge |Y_{\rm free}|,
\]
and any survivor with \(h(G)\le j-1\) has at most \(j-1\) such geometric holes.
The exact lattice-trace and free-sink operations are regression-tested in
research/cell_union_certificate.py.

This extracts only the zero-degree portion of the right shore.  It does not bound
the remaining Hall deficiency from overlapping neighborhoods or long,
hole-free strips, so the Target A and Level I endpoints remain open.

## Entry 10 — exact alternating Hall-core decomposition

The scaffold incidence matcher now exposes a DM-style alternating core.  Starting
from every unmatched left cell in a fixed maximum matching, traverse unmatched
cell-to-lattice edges and then matching edges back to cells.  The reached left set
\(S\) satisfies
\[
|S|-|N(S)|=d_{\rm sc},
\]
and each connected component of the reached incidence graph has positive deficiency;
the component deficiencies add exactly to \(d_{\rm sc}\).

This is a useful exact localization of the Hall nullity and is regression-tested
over neutral phases, disconnected deficient cores, and the remote-cell hidden-core
example in `research/scaffold_cells.py`.  It still does not turn
matching deficiency into spatially additive phase charge, so the Target A endpoint
remains open.  Applying the cell-complex identity componentwise gives an exact
non-overlapping charge certificate of \(12d_\ell\) on component \(\ell\); the
remaining target is the disjoint-root inequality
\[
\sum_\ell d_\ell\ge\Delta_\Lambda.
\]

## Entry 11 — sub-half anchors bound the remaining Hall charge

There is a general exact bound behind the Hall-neutrality of the mixed-interface
regression.  For a selected blocker set \(S\), call a blocker central when none of
its strict lattice conflict vertices is closer than \(1/2\).  Every noncentral
blocker has a conflict vertex at distance \(<1/2\).  Choosing one such vertex for
each noncentral blocker is injective: two unit-separated blockers cannot both be
within \(1/2\) of the same lattice site, by the triangle inequality.

Consequently
\[
|N(S)|\ge |S\setminus C|,
\qquad
|S|-|N(S)|\le |S\cap C|,
\]
where \(C\) is the central subset.  Maximizing over \(S\) gives the exact
sub-half-anchor Hall bound \(h(G)\le |C|\).  For the certified mixed diagonal
interface, every anchor has squared distance \(3t^2<1/4\), so \(C=\varnothing\)
and the whole arbitrarily long interface is Hall-neutral.  This is a genuine
local obstruction to arguments that try to convert a long mixed interface
directly into positive Hall charge.

The result is implemented and regression-tested in
research/mixed_monomer_interface.py.  It still does not control central blockers
in the actual Target A scaffold, and therefore does not prove the missing
source-response inequality.
