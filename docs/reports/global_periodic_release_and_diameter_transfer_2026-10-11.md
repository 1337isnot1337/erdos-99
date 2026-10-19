<!-- theorem-state: {"artifact_id":"ART-1FC8B0FF87EB","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
<!-- migration-provenance: {"destination_status": "unreviewed_noncanonical", "source_blob": "8ee7966fb6a367784f7729fdc256898ac0464718", "source_branch_refs": ["refs/heads/research/sol/global-e99-20261011"], "source_commit": "f75b300c5d2804d4da83f317c79fef142398581c", "source_lifecycle": "unreviewed", "source_path": "docs/reports/global_periodic_release_and_diameter_transfer_2026-10-11.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "7f317cc5be49952c5837d0ee634f96f5821b489a3196dee554612fcdffe7cf56"} -->

> **Imported unreviewed branch research.** Source branch status is historical only; no destination claim is promoted.

# Erdős Problem #99 — periodic release and the diameter-transfer obstruction

**Date:** 2026-10-11

**Repository base:** `ab6dd3336f9f8d440f2bada76edb32153391cddc`

**State version:** `2026-10-10.audit.234`

**Run type:** independent global-route investigation and exact regression

**Target:** Level I; no A/B/C closing theorem imported

**Active prompt:** `docs/prompts/erdos_problem_99_GPT6_ASTRA_FULL_SOLUTION_PROMPT.md`

**Computation:** `research/verify_periodic_release_diameter_transfer.py`

## LEVEL I STATUS

**STILL OPEN.** The results below distinguish global cell compression from
finite-source diameter compression. They do not assert novelty over the
periodic-packing literature and do not use another worker's claimed solution.

## 1. Proposed global chain

```text
triangle-free periodic contact graph -> finite cell release
-> full-source strict diameter decrease -> Level I contradiction
```

The first arrow holds under the explicit hypotheses in Section 2. The second
arrow does not hold generally. Sections 3–5 identify its failure with exact
examples and a bound on how many old diameter constraints standard
periodization can encode. No source label is silently removed.

## 2. Periodic area-or-contact release

**Classification:** proved candidate awaiting promotion; artifact unreviewed.

Let a unit-separated packing have `N` labeled centers modulo an invertible
period matrix `B`. Suppose its complete unit-contact graph on the flat torus
is connected and cellular, and every facial boundary has at least four edge
occurrences. A simple triangle-free contact graph with cellular embedding has
this property. Then a nontrivial finite packing deformation exists with:

- the same labels and periodicity type;
- no decreased old contact length and no violated lower pair constraint;
- nonincreasing period-cell area;
- either strictly decreased area, or unchanged area and strictly fewer contacts.

The theorem permits the full symmetric cell strain. It does not fix the shape
of the torus, control the diameter of a finite crop, or require every old
contact to remain exactly unit. It assumes cellularity rather than deriving it
for arbitrary disconnected sources.

### Proof

Let `M` be the number of contact-edge orbits. Euler gives `N-M+F=0`, and the
facial degree sum gives `4F<=2M`; hence `M<=2N`.

Use a symmetric `2x2` strain `E` and periodic label velocities `v_i`, modulo
their common translation. There are `3+2N-2=2N+1` variables. For a contact
vector `r=p_j+Bz-p_i`, impose the bar equation

\[
r\mathbin\cdot(Er+v_j-v_i)=0.
\]

There are at most `2N` equations, so a nonzero solution exists. If necessary
reverse its sign to obtain `tr(E)<=0`. Define

\[
B(t)=(I+tE)B,\qquad p_i(t)=(I+tE)p_i+t v_i.
\]

Every old contact vector becomes `r+t w`, where `w=Er+v_j-v_i`, and its squared
length is exactly `1+t^2|w|^2`. Thus all old lower constraints hold at finite
`t`. For small `t`, all old noncontacts remain longer than one: only finitely
many image pairs have bounded length, and the infinitely many distant image
pairs stay distant under an invertible near-identity cell map and bounded
periodic velocities.

For a symmetric matrix,

\[
{\det B(t)\over\det B}=1+t\operatorname{tr}E+t^2\det E.
\]

If the trace is negative, area strictly decreases for small positive `t`.
If it is zero and `E!=0`, symmetry gives `det E<0`, again strictly decreasing
area. If `E=0`, area is unchanged. Connectedness and nontriviality modulo a
common translation then give some contact with `w!=0`, which strictly opens.
No new contact appears for sufficiently small `t`, so the contact count drops.
This is an actual finite endpoint, not only a tangent vector.

If the initial packing is collectively jammed with the cell fixed, the last
case cannot occur. Thus under that extra hypothesis the packing has a strict
finite area decrease once cell shape is allowed to vary.

## 3. An exact collectively jammed fixed-cell example

**Classification:** regression and proved candidate awaiting promotion;
artifact unreviewed.

Let `u,v` be unit vectors with `u.v=-1/7`, and use periods

\[
g_1=3u+v,\qquad g_2=u+3v.
\]

Their squared lengths are `64/7`, and their mutual inner product is `32/7`,
so this period cell is triangular. There are eight lattice labels modulo the
periods, represented by `p_i=i u`, `i=0,...,7`. In label coordinates a positive
`u` contact advances by one and a positive `v` contact advances by five modulo
eight. Both are eight-cycles. There are exactly sixteen contact-edge orbits,
and eight rhombus faces. The torus has shortest period length `8/sqrt(7)>3`;
the contact graph is simple and triangle-free.

For fixed-cell infinitesimal strut displacements let `X_i=u.v_i` and
`Y_i=v.v_i`. The `u`-cycle inequalities sum to zero, hence all `X_i` are equal;
the `v`-cycle does the same for `Y_i`. Since `u,v` are independent, only common
translation remains. This also proves local finite collective jamming: a
sequence of nontrivial arbitrarily small feasible displacements, normalized
by its largest displacement after translation removal, would have a nonzero
limiting infinitesimal strut motion, which was just excluded.

Nevertheless take, in Cartesian coordinates,

\[
u=(1,0),\quad v=(-1/7,4\sqrt3/7),\qquad
E=\begin{pmatrix}0&2\sqrt3\\2\sqrt3&1\end{pmatrix}.
\]

Both `u.Eu` and `v.Ev` vanish. Apply `I-tE` and divide all lengths, including
the periods, by `sqrt(1+12t^2)`. The new unit-basis inner product and cell-area
ratio are

\[
c(t)={-1-48t+12t^2\over7(1+12t^2)},\qquad
a(t)={1-t-12t^2\over1+12t^2}.
\]

For `0<t<1/18`, one has `-1/2<c(t)<-1/7` and `0<a(t)<1`.
At `t=1/18`, `c=-1/2` and `a=7/8`, and unit triangles appear.

All infinitely many lower pair constraints hold. For any integer pair
`(a,b)!=(0,0)` and `|c|<=1/2`,

\[
|au+bv|^2=a^2+b^2+2cab\ge a^2+b^2-|ab|\ge1.
\]

In the open angle interval only `(+/-1,0),(0,+/-1)` give equality. Thus the
entire initial segment is triangle-free and strictly denser, despite the
initial fixed-cell collective jamming. The period-cell shape changes.

## 4. Finite diameter goes in the opposite direction

**Classification:** exact regression; artifact unreviewed.

For the same basis, the finite `m by m` crop

\[
P_m(c)=\{iu+jv:0\le i,j\le m\}
\]

has `(m+1)^2` labels, minimum distance one, and diameter squared

\[
d(P_m(c))^2=2m^2(1+|c|).
\]

Convexity of squared norm puts the maximum on the corners of the difference
box `[-m,m]^2`, proving the formula. The cell-compression path of Section 3
strictly **increases** this diameter. These crops are not claimed globally
optimal.

There is also an attained-optimum guard: `D(4)=sqrt(2)` is achieved by a unit
square, which is triangle-free. A symmetric shear followed by normalization
to unit sides decreases the square-lattice cell area but changes this finite
square's diameter squared to

\[
{2(1+|t|)^2\over1+t^2}>2\quad(0<|t|<1).
\]

To check optimality of the old square, any convex quadrilateral has an angle
at least `pi/2`, whose opposite diagonal has length at least `sqrt(2)` by the
cosine law and unit adjacent sides. If one of four points is in the triangle
of the other three, two directions from it have angle at least `2pi/3`, giving
an outer-pair distance at least `sqrt(3)`. Degenerate cases obey at least the
same `sqrt(2)` lower bound. The square attains the bound.

This finite regression refutes an unrestricted transfer implication; it does
not refute a sufficiently-large theorem using additional global hypotheses.

## 5. Standard shield periodization represents at most three diameter pairs

**Classification:** proved candidate awaiting promotion; artifact unreviewed.

Let a finite unit-separated source `A` have diameter `D>0`. Let a period
lattice `Lambda` have every nonzero vector of length at least `D+1`.
Then `A+Lambda` is unit-separated. Its cross-copy unit contacts can represent
at most **three distinct old diameter pairs**.

Indeed

\[
|\lambda+q-p|\ge|\lambda|-|q-p|\ge(D+1)-D=1.
\]

Equality requires a shortest lattice vector of length `D+1` and an old
diameter vector antiparallel to it. Distinct shortest lattice vectors have
angle at least `pi/3`, because their difference is a nonzero lattice vector.
There are therefore at most six shortest vectors, or three unoriented
directions.

There can be at most one old diameter pair per unoriented direction. If two
different such pairs are `p,p+Du` and `q,q+Du`, with `w=q-p!=0`, then the two
cross-pair squared distances have sum

\[
|Du+w|^2+|Du-w|^2=2D^2+2|w|^2>2D^2,
\]

contrary to diameter `D`. This proves the bound. If the shortest lattice
vector is strictly longer than `D+1`, there are no cross-copy unit contacts.

Consequently this periodization does not encode every upper constraint of any
source having more than three actual diameter pairs. It cannot be treated as
an equivalent rigidity problem without a separate theorem. No premise about
canonical stress selection or large-source diameter counts is needed for this
finite bound.

## 6. Exact computation, literature, and claim limits

Run `python3 research/verify_periodic_release_diameter_transfer.py`.
Rational Gram-matrix arithmetic checks the eight-label torus, its contact
cycles, fixed-cell rank `14`, free-strain rank `16`, strain identities,
normalized Gram matrices, decreasing cell area, increasing finite-crop
diameter, and the globally optimal square guard. Infinite lattice separation
is proved by the quadratic-form inequality above; finite enumeration is only
a regression check.

For terminology and comparison, checked primary sources are:

- R. Connelly and W. Dickinson, *Periodic Planar Disk Packings* (2012),
  Section 1.5 and Theorems 2–3:
  <https://pi.math.cornell.edu/~connelly/Connelly-Dickinson-V3.pdf>.
- A. Donev, S. Torquato, F. H. Stillinger and R. Connelly, *A Linear Programming
  Algorithm to Test for Jamming in Hard-Sphere Packings*, J. Comput. Phys. 197
  (2004), 139–166, Section 4.3:
  <https://pi.math.cornell.edu/~connelly/pdf/10.1016_j.jcp.2003.11.022.pdf>.

The first source's fixed triangular-torus results do not forbid variable-cell
compression. The second explicitly permits symmetric cell strain for strict
jamming. No fixed-torus density theorem is imported as a finite-diameter
theorem. The arguments in Sections 2–5 are supplied here rather than delegated
to a literature analogy.

## 7. Frontier effect and continuing obligation

**Promotion recommendation:** unreviewed. No canonical frontier is changed.

| Claim | Classification | Scope |
| --- | --- | --- |
| Finite periodic area-or-contact release | Proved candidate awaiting promotion | Connected cellular contact graph; all facial degrees at least four |
| Eight-label collectively jammed fixed-cell example with variable-cell release | Regression | Exact unit-rhombic lattice; no finite-source globality claim |
| Cell area decrease implies finite diameter decrease | Rejected without additional hypotheses | Crop family and globally optimal four-point square |
| At most three old diameter pairs in shield-periodization contacts | Proved candidate awaiting promotion | Shortest period length at least `D+1` |
| Periodic route closes Level I | Unproved | Full-source upper constraints have not been transferred |

The next obligation for this route is a construction from an attained global
source whose finite endpoint retains every label, satisfies **all** lower and
upper pair constraints, and has strictly smaller diameter. Periodic area,
collective jamming, or a bulk contact-count argument cannot substitute for
those endpoint checks. The independent closing run continues.
