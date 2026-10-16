<!-- theorem-state: {"artifact_id":"ART-4C21CDB00D9E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Inverse-phase geometry, curved loaded boundaries, and exceptional faces

Date: 2026-10-09. Research base: `5a664f35c973810156576a9a8d014cd9a65c8d95`.
Sections 8--12.3 were developed after the compared state refresh to
`868761a47a9344d7df98fe5a8c880ed87f020a06`, state `2026-10-09.audit.179`.
Sections 12.4--14 use the same mathematical inputs after comparing and importing
`0fde3ae454a71103945b8daac3274b278218a86f`, state `2026-10-09.audit.180`.
Classification: **proved candidate awaiting independent audit and promotion**.
Artifact lifecycle: **unreviewed**. No canonical state is changed.

Publication reading note: only exact separately audited sections inherit their
manifest scopes. Audit.202's later global Lipschitz chart and `O(D^(4/5))`
inference from a vanishing face tail are withdrawn; use the
[Audit.236 sequence proof](../audits/target_c_global_inverse_phase_face_tail_second_referee_2026-10-10.md)
for the audited-working exclusion. The fixed-face-cutoff rate in Section 6 below
has stronger hypotheses and is not the withdrawn variable-tail inference.

## 1. Implication to the endpoint

```text
one global O(1/D) six-direction phase frame
 + vanishing high-degree hull-augmented face tail
 -> zero lattice holonomy and local positional chart control
 -> localized curved-boundary capacity gives q=o(D)
 -> contradict canonical q>=h>=ceil(D).
```

This excludes a source class with actual contact geometry and a tail condition.
Neither the global phase frame nor the tail condition follows from the current
canonical grain extraction. The theorem is not C-II or Level I closure.

Section 7 adds the stronger Type-II implication

```text
one whole harmonic cell with an O(1/D) six-direction frame
 + canonical short local routes outside eta D bad attachment incidences
 -> its actual loaded attachment population is o(D)
 -> contradict the canonical uniform linear attachment lower bound.
```

That implication needs no vanishing global face tail and allows other cells to
have different, unrestricted contact geometry. Its cell-wide phase premise
is still not supplied by the selected-grid extraction.

Section 8 gives an unconditional source consequence: every actual loaded
boundary contact walk carrying a linear endpoint population has linear
total directional strain from every unit rhombic lattice frame. This applies
to the whole core in either global branch and to the internal/attachment
contact boundary of every Type-II cell. It does not convert that strain
to a finite replacement or canonical area payment.

Sections 9--10 fuse the actual diameter-normal measure with train/face
cancellation at all-branch scope. They retain the actual source quantities
`P_F` and `R_4` in the macroscopic-container branch; their Type-II scalar
specializations are already canonical. No source competitor follows yet.

All contact isolates remain in the full unit-separated source and its ball hull.
The proof uses the preceding unreviewed candidate
`target_c_localized_curved_boundary_slow_lattice_deformation_2026-10-09.md`.

## 2. Finite graph setting

Let `A` be a finite triangle-free unit-separated source of diameter `D`, and `G` a connected
triangle-free straight-line unit-contact graph on a subset `V subset A`.
Let `F=conv(V)` be two-dimensional. Suppose every extreme vertex of `F` belongs
to the actual diameter-endpoint set of `A`. Add the missing hull sides to `G`
to obtain a plane graph `Ghat` whose bounded faces have this structure:

1. an old convex unit-edge bounded contact face; or
2. a convex pocket bounded by one simple actual unit-contact path and one hull
   side closing that path.

For such a face `Q`, let `m(Q)` be the length in unit edges of the first
boundary, or of the pocket's actual unit path. Thus an old unit face has
diameter at most `m(Q)`, and a pocket also has diameter at most `m(Q)`.
The hull-closing side need not be a contact. Define

\[
T_M=\sum_{Q:\,m(Q)>M}m(Q),\qquad M\ge4. \tag{2.1}
\]

The canonical C-II core and its loaded-hull augmentation have precisely this
face structure, by Section 67 and the canonical hull-augmented cell theorem.
In this canonical application `F=conv(B)` and its hull vertices are all the
actual loaded endpoints. The source hypotheses, rather than abstract planar
graph assumptions, supply convexity and the face decomposition.

## 3. Finite routing with an explicit tail term

**Lemma 3.1.** Under Section 2, any `p,q in V` have an actual contact path with

\[
d_G(p,q)\le C_M(|p-q|+1)+2T_M,
\quad C_M=56M(M+1)^2+42M(M+1). \tag{3.1}
\]

**Proof.** A triangle-free unit-contact graph has degree at most five: six
unit neighbors would force six equal `60`-degree gaps and triangles. Hull
augmentation adds at most two edges at each vertex, so `Ghat` has degree at
most seven.

Join `p,q` inside `F` by a generic two-segment polygonal arc lying within
distance `1/10` of the straight segment and of length at most `|p-q|+1/10`.
It can be chosen to avoid graph vertices except its endpoints and to avoid
edge coincidences. Each convex face is met in at most one interval by each
of the two segments, so at most twice overall.

In an old bounded face, replace each crossed interval by a boundary arc
of length at most `m(Q)`. In a pocket, a path in `int(F)` cannot cross the
hull-closing side; both entry and exit lie on its actual contact path
(including an endpoint if `p` or `q` is a pocket tip). Replace that interval
by the intervening actual unit path, of length at most `m(Q)`. This makes a
continuous curve on `G` from `p` to `q`. Its length bounds the unit-edge
graph distance: partial-edge backtracking can be removed in the metric graph.

Large faces contribute at most `2T_M`, counting each face at most twice.
Every small crossed face has a vertex within `M+1/10` of the straight
segment, since its diameter is at most `M`. A vertex belongs to at most
seven distinct faces, so there are at most seven times the number `N` of
nearby source vertices such small faces. Radius-`1/2` source disks have
disjoint interiors. Their union is contained in the tube of radius `M+1`
about the segment; hence

\[
N\le 4(M+1)^2+{8(M+1)\over\pi}|p-q|
\le 4(M+1)^2+3(M+1)|p-q|.
\]

Small faces cost at most `14MN`, giving
`56M(M+1)^2+42M(M+1)|p-q|`. This is bounded by the first term in (3.1).
QED.

This route is an actual contact path. No diameter edge or missing hull side
is used as a motion or transport edge.

## 4. Zero holonomy of a global inverse-phase frame

Assume that for every graph in an unbounded sequence there are unit vectors
`u_D,v_D` of angle exactly `pi/3` such that each oriented actual unit-contact
edge vector `e` is within `K/D` of one member of

\[
\mathcal U_D=\{\mathord\pm u_D,\mathord\pm v_D,
                         \mathord\pm(v_D-u_D)\}, \tag{4.1}
\]

where `K` is fixed. Assign the nearest such reference vector to each oriented
edge, consistently negating it on the reverse edge. For large `D` the nearest
choice is unique.

**Lemma 4.1.** If the maximum degree of an old bounded contact face is `o(D)`,
the reference vectors have zero sum around every closed graph walk, for large
`D`. Thus there is a well-defined map `ell:V -> Z u_D+Z v_D`, up to one
common translation, whose edge increments are the assigned reference vectors.

**Proof.** Around a bounded contact face with `m` unit sides, the actual edge
vectors sum to zero. The reference sum belongs to the unit triangular lattice
and has norm at most `mK/D=o(1)`. That lattice has minimum nonzero norm one,
so the reference sum is zero. Bounded facial cycles generate the cycle space
of a connected plane graph, including graphs with bridges. The reference sum
therefore vanishes around every closed walk, and path integration defines
`ell`. QED.

The map need not be assumed injective for the counting below. The sufficiently
small local rounding error itself proves injectivity on each counted patch.
No unproved global embedding or source/scaffold identification is used.

Set `g(p)=p-ell(p)`. Every actual unit edge has a displacement increment of norm
at most `K/D`. Lemma 3.1 therefore gives the finite pair estimate

\[
|g(p)-g(q)|\le {K C_M\over D}(|p-q|+1)+{2K T_M\over D}.
\tag{4.2}
\]

## 5. Vanishing face tail forces sublinear loaded population

**Theorem 5.1.** In the setting of Section 2, suppose (4.1) holds with fixed
`K` and

\[
\lim_{M\to\infty}\limsup_{D\to\infty}{T_M\over D}=0. \tag{5.1}
\]

Suppose also that every actual diameter endpoint of `A` belongs to `V`.
Then its actual loaded endpoint population satisfies `q=o(D)`.

**Proof.** Condition (5.1) implies that the largest old contact-face degree is
`o(D)`: it is at most `M+T_M`, and one first fixes `M` and then sends
`D` to infinity and `M` to infinity. Lemma 4.1 defines `ell` for large `D`.

Fix `M` and a small constant `delta>0`, and set `r=delta D`. Cover the
loaded-hull boundary by `O(D/r+1)` patches as in Section 5 of the localized
curved-boundary report. In one patch choose a loaded endpoint `p_0`. For every
other loaded endpoint `p` assigned there, `|p-p_0|<=r`; (4.2) gives

\[
|p-[\ell(p)+g(p_0)]|
\le \epsilon_D:={K C_M\over D}(r+1)+{2K T_M\over D}. \tag{5.2}
\]

For sufficiently large `M`, (5.1) makes `limsup 2K T_M/D` arbitrarily small;
afterward choose `delta` so small that `limsup epsilon_D<1/8`. Each patch's
reference positions thus lie in one translated unit triangular lattice, and
its rounding is injective because the actual source points are unit-separated.
The localized curved-boundary estimate gives

\[
q\le C(D/r+1)\left(r\epsilon_D+(Dr)^{1/3}+1\right).
\]

Here `C` is absolute and does not depend on `M,delta,K`. At fixed `M,delta`,
the Fourier and constant terms divided by `D` tend to zero. Hence

\[
\limsup_{D\to\infty}{q\over D}
\le C\left(K C_M\delta+2K\limsup_{D\to\infty}{T_M\over D}\right).
\]

Send `delta` to zero at fixed `M`, and then send `M` to infinity using
(5.1). This proves `q=o(D)`. The order of limits is essential: no convergence
rate for the face tail is assumed. QED.

## 6. Canonical exclusion and exact remaining alternatives

For canonical C-II representatives, `q>=h>=ceil(D)` contradicts Theorem 5.1.
Thus they cannot simultaneously have one global inverse-diameter phase frame
and a vanishing tail of the actual hull-augmented contact faces.

For fixed `M`, the stronger quantitative consequence of Lemma 3.1 and the
slow-chart theorem is `q=O_{M,K}(D^(4/5))` when every augmented face has at
most `M` actual unit edges. A fixed physical bow is permitted.

This is a source-level geometric exclusion, not an abstract train-graph count.
Its global phase hypothesis concerns every actual contact in the positive core,
including contacts on exceptional faces. Current canonical inverse-phase grids
control selected trains and selected rhombi. They do not establish (4.1) on
the entire core; several macroscopic grain phase frames remain possible.
Likewise the current face-tail alternative records (5.1) as an unresolved
condition. The general macroscopic-container branch remains open.

The next bridges are explicit: either force this single frame and tail in
every survivor, or charge their failure at source level strongly enough to
produce a finite competitor or exact unit triangle. Section 7 strengthens
the exclusion in Type II, using canonical local routes instead of a global
tail hypothesis; it still does not extract the needed contact phase frame.

## 7. Every Type-II harmonic cell must resist an inverse-phase frame

The full-core Type-II branch supplies two canonical inputs stronger than the
abstract setting in Section 2:

1. `C-UNIFORM-HARMONIC-CELL-AREA` (Audit.173) gives a fixed `c>0` such that
   every nonempty unloaded component `I`, with actual loaded attachment set
   `A_I`, satisfies `|A_I|>=cD/3` eventually. One may take any fixed
   `c<sin(pi/12)/2`. All these attachments are actual diameter endpoints.
2. `C-TYPEII-FACE-TAIL-PORT-MULTIPLICITY` (Audit.173 supplement) gives, for
   every fixed `lambda,eta>0`, a fixed `rho>0` such that fewer than `eta D`
   attachment incidences `(a,I)` fail to have an actual contact route of
   length `<lambda D` to **every** `z in I cap closed B(a,rho D)`. The
   route starts at `a` and otherwise stays in `I`.

Their precise authority is the claim registration in
`docs/state/theorem-state.yaml`, with proofs in the independent uniform-cell
and face-tail/port audits. The second input permits a linear global face tail;
it controls that tail's multiplicity near loaded ports.

**Theorem 7.1 (single-cell exclusion).** Fix `K<infinity`. Along no unbounded
canonical Type-II C-II sequence can there be a nonempty unloaded component
`I_D` for each source and a triangular six-direction frame `U_D` such that
every actual contact within `I_D`, and every actual contact from `I_D` to
its loaded attachments, is within `K/D` of a member of `U_D`.

The frame may vary with `D`, and other components and loaded-loaded contacts
are completely unrestricted. No high-degree face-tail hypothesis or zero
holonomy is assumed.

**Proof.** Suppose such components exist. Fix small constants `lambda,eta>0`
and obtain `rho` from input 2. Decrease `rho` to be at most one if necessary.
Set `r=rho D/2`. Cover the loaded-hull boundary by `N<=C(D/r+1)` patches
`B(c_j,r/2)`, with centers `c_j` on that boundary and hence in the full-source
ball hull `W`. This is the arclength cover used in the localized
curved-boundary report. Assign each attachment of `I_D` to one covering patch.

In a patch containing a good attachment choose one, `a_0`. For every other
assigned attachment `a`, choose one actual neighbor `z in I_D`. Then
`|a_0-z|<=r+1<=rho D` for large `D`. By goodness, there is a contact path
from `a_0` to `z` of length `<lambda D`. Append the actual edge `za`.
All edges of this path lie in the scope of the assumed frame.

Orient each edge along the chosen path and replace its vector by a nearest
member of `U_D`. Their sum belongs to the one unit triangular lattice
`Lambda_D` generated by that frame. Consequently, for some `ell_a in Lambda_D`,

\[
|a-(a_0+ell_a)|<=epsilon_D:=K(lambda+1/D). \tag{7.1}
\]

Different attachments may use different paths. No agreement of path sums
around cycles is needed: choose one path for each attachment. If
`epsilon_D<1/8`, unit separation makes their chosen lattice labels distinct.
Thus the entire assigned population of a patch having a good attachment
is within `epsilon_D` of one translated triangular lattice.

A patch without a good attachment contains only bad attachment incidences.
Because attachments were assigned once, all such patches together contain
fewer than `eta D` attachments of `I_D`. Apply the local curved-boundary
estimate to each remaining patch; its constants are absolute and independent
of `lambda,eta,rho`:

\[
|A_{I_D}|<=eta D+C(D/r+1)
             \{r epsilon_D+(Dr)^{1/3}+1\}. \tag{7.2}
\]

First fix `lambda,eta,rho` and send `D` to infinity. Since `r=rho D/2`,
the last two patch terms are `o(D)`, and (7.2) gives

\[
limsup_{D\to\infty}|A_{I_D}|/D<=eta+C'K lambda. \tag{7.3}
\]

Here `C'` is absolute: `(D/r+1)r/D=1+r/D<=3/2`.
Choose `lambda` small enough for both `K lambda<1/16` and
`C'K lambda<c/12`, and choose `eta<c/12`. Equation (7.3) is then less
than `c/6`, contradicting the uniform canonical lower bound `c/3`.
For `K=0` the same proof uses `epsilon_D=0` and any positive `lambda`.
Every contact isolate remains in the ball hull and in the source.
QED.

This is a per-cell theorem. It forbids assigning one inverse-diameter phase
frame even to a single whole harmonic cell and its attachment contacts.
It is stronger than requiring one frame for the entire positive core.
It does not forbid an inverse-phase selected complete grid **inside** that
cell: the other actual contacts on routes and at attachments can leave the
grid's frame. The canonical grid extraction does not control those edges.

The remaining synthesis question is therefore inside a cell: can the necessary
phase changes between its quadratic coherent mass and its loaded attachments
be paid against a canonical budget or turned into a compatible finite motion?
This report proves their necessity, not that payment or motion.

## 8. Linear directional strain on an actual loaded boundary walk

The preceding theorem needs no replacement packet. A stronger quantitative
statement also needs no extracted lattice chart, path-length estimate, or
vanishing exceptional-face tail. Its input is the **actual contact walk**
around a set of actual diameter endpoints.

For a unit rhombic lattice `Lambda`, generated by unit vectors at angle in
`[pi/3,2pi/3]`, let

\[
 U(Lambda)=\{z\in Lambda:|z|=1\},\qquad
 d_L(w)=\min_{z\in U(Lambda)}|w-z| \quad (|w|=1).
\]

There are four unit lattice vectors, or six at a triangular endpoint.
The lattice and its orientation may depend on `D`.

### 8.1 Actual diameter normals have a uniform window count

Suppose all actual diameter midpoints of a unit-separated source lie in
`B(o,L)`. For each actual diameter endpoint `p`, choose one actual partner
`p'` and write `m_p=(p+p')/2`, `n_p=(p-p')/D`. Then

\[
 p=m_p+(D/2)n_p,
 \qquad n_p\cdot(x-p)\le-|x-p|^2/(2D)<0\quad(x\ne p). \tag{8.1}
\]

Thus `n_p` is a strict supporting normal of the **full-source** hull at
`p`, including all contact isolates. For any oriented normal window of
half-width `t<pi/2`, the number of selected endpoints whose chosen normals
lie in that window is at most

\[
 1+{D\sin t+2L\over\cos t}. \tag{8.2}
\]

Indeed, order those endpoints by their supporting normals. The forward
chords along the corresponding convex boundary chain all make angle at
most `t` with its central tangent. Each consecutive chord has length at
least one and hence advances tangent projection by at least `cos t`.
Equation (8.1) puts their projections in an interval of length at most
`D sin t+2L`. This proves (8.2); intervening source hull vertices cause
no loss.

For canonical global minimizers, the full-source circumradius theorem gives

\[
 L=L_D:=\sqrt{D\eta_D+\eta_D^2},\qquad
 \eta_D=3^{1/4}\sqrt D,\qquad L_D=o(D). \tag{8.3}
\]

No Type-II force-hull assumption is used in this midpoint estimate.

### 8.2 A finite inequality for a lattice-referenced walk

Let `S` be `a` distinct actual diameter endpoints in convex cyclic order.
Suppose a closed actual unit-edge walk encounters a chosen occurrence of
each point of `S` in that cyclic order. Repeated vertices and bridges are
allowed. Define its occurrence-counted directional strain by

\[
 A_L:=\sum_{\text{walk steps }w}d_L(w).
\]

Fix `M>=1`, `0<epsilon<=1/8`, and assume

\[
 t:=2epsilon+(4M+8L)/D\le1/4.
\]

Put `N_M=4(M+1)^2`. Then

\[
 \boxed{
 a\le {\pi D\over M}+{A_L\over epsilon}+2
       +N_M\{4D epsilon+8M+20L+1\}.} \tag{8.4}
\]

**Proof.** Replace each oriented unit step by a nearest vector of
`U(Lambda)` and form its reference lattice prefix `ell_j`. For the
actual walk prefix `p_j`, set `g_j=p_j-ell_j`. Its total variation is
exactly `A_L`. Split the indices into nonempty bins according to
`floor(TV(g_0,...,g_j)/epsilon)`. There are at most
`floor(A_L/epsilon)+1` such bins. In each bin, every pair of displacement
values differs by less than `epsilon`.

There are at most `pi D/M` consecutive `S`-chords longer than `M`,
because `per(conv S)<=pi D`. Among the remaining chords, at most the
number of bins have their endpoint occurrences in different bins,
including the closing chord. Every other chord `w=q-p` satisfies

\[
 |w-z|<epsilon
 \quad\text{for a nonzero }z\in Lambda,
 \qquad |z|\le M+epsilon. \tag{8.5}
\]

Nonzeroness follows from `|w|>=1`. Its direction differs from that of
`z` by at most `2epsilon`. Every unit rhombic lattice has minimum
nonzero norm one: its Gram matrix has least eigenvalue at least `1/2`,
and direct examination of integer vectors of squared coordinate norm
at most two covers the only borderline cases. Disjoint radius-`1/2`
disks about lattice points in `B(0,M+epsilon)` therefore bound the
number of possible nonzero vectors in (8.5) by
`4(M+epsilon+1/2)^2<=N_M`.

For this short chord, the midpoint identity gives

\[
 |n_p-n_q|\le(2M+4L)/D.
\]

The two strict support inequalities in (8.1) have opposite signs on
`w`, so `|n_p dot (w/|w|)|<=(2M+4L)/D`. Consequently `n_p` is within
angle `(4M+8L)/D` of one of the two normals to `w`. Together with
(8.5), it lies in a normal window of half-width `t` about `Jz/|z|`
or `-Jz/|z|`. The lattice vector alphabet is symmetric, so these are
at most `N_M` windows, not `2N_M` additional windows.

For `t<=1/4`, (8.2) is at most

\[
 1+2Dt+4L=4D epsilon+8M+20L+1.
\]

Every good short chord has a distinct starting endpoint. Counting the
long chords, the bin changes, and these normal windows proves (8.4).
Reference prefixes need not close or agree with any labels chosen
using other contact paths. No zero-holonomy assertion was used. QED.

### 8.3 Uniform linear strain, including each Type-II harmonic cell

**Theorem 8.3 (proved candidate awaiting independent audit/promotion).**
Fix `gamma>0`. Along any unbounded canonical source sequence, let an
actual unit-edge walk encounter at least `gamma D` distinct actual diameter
endpoints in their convex cyclic order. There is `kappa(gamma)>0`,
independent of the unit rhombic lattice and its orientation, such that

\[
 A_L\ge kappa(gamma)D \tag{8.6}
\]

for all sufficiently large `D`.

One explicit choice is

\[
 M=\lceil32/gamma\rceil+1,\quad N_M=4(M+1)^2,\quad
 epsilon_0=\min\{1/32,gamma/(32N_M)\},\quad
 kappa(gamma)=gamma epsilon_0/2. \tag{8.7}
\]

To prove the theorem, insert `M,epsilon_0` in (8.4). The long-chord
term is less than `gamma D/8`, and the `4N_M D epsilon_0` term is at
most `gamma D/8`. By `L_D=o(D)`, all remaining terms except
`A_L/epsilon_0` are at most `gamma D/4` for large `D`. This proves
(8.6). The normal-window restriction on `t` is also eventually met.

There are two actual-source applications.

1. **Whole core, both global branches.** Its outer contact facial walk
   visits all `q` loaded vertices in cyclic hull order. Canonical ZF and
   Woodall give `q>=h>=ceil D`; thus (8.6) applies with coefficient one.
   The walk length is `b<=2q<=2pi D` by the canonical Euler ledger.

2. **Every Type-II harmonic cell.** Use only the internal contacts of
   `I_r` and its actual contacts to `A_r`. Omit loaded-loaded contacts
   from this graph. It is connected, is contained in `conv A_r` by the
   canonical harmonic maximum principle, and every point of `A_r` is
   an extreme vertex. Its outer facial walk encounters those vertices
   in cyclic order. This follows also by adding the attachment polygon
   sides as in canonical Section 123: its exterior pockets concatenate
   actual unit paths between the consecutive polygon vertices.
   The planar triangle-free Euler identity is

   \[
    L_r^0+Q_r^0=4a_r-6-2s_r,
    \qquad s_r=e_r+t_r-2|I_r|-1\ge0.
   \]

   Hence `L_r^0<=4a_r<=4pi D`. Canonical Audit.173 supplies one
   fixed positive coefficient `gamma` with `a_r>=gamma D`, uniformly
   for every nonempty Type-II cell. Equations (8.6)--(8.7) apply
   to **each such cell**, using only internal and attachment contacts.
   They do not spend or count a loaded-loaded contact.

In either application, an outer facial walk uses each physical edge at
most twice. Its length is at most `16D`. Since `d_L(w)<=2`, (8.6)
also implies that at least `kappa(gamma)D/8` distinct physical contact
edges on that walk satisfy

\[
 d_L(w)>kappa(gamma)/32. \tag{8.8}
\]

Indeed, the contribution of steps below the threshold is at most half
of (8.6); the other steps must number at least `kappa(gamma)D/4`,
and each physical edge accounts for at most two steps.

This is an actual source boundary-contact statement, not a claim about
selected grids. A coherent inverse-phase grid inside a cell can coexist
with (8.8); its frame must fail on linearly many distinct contacts of
that cell's outer walk. The proof gives a concrete interface bank and
a positive angular scale. It does not give disjoint moves, a contact
budget for a replacement packet, or a strict sub-`D` full-source
competitor. All contact isolates remain in the source geometry.

## 9. Hull-train depletion does not need the Type-II disk limit

The normal-window proof also extends one existing canonical mechanism to
both exhaustive source branches. This section does **not** claim a new
full-core scalar endpoint: that endpoint is already canonical in
`C-FULLCORE-HULL-DEPLETION-FLOOR`. Its new scope is the actual hull-train
crossing bound without a Type-II force-hull disk hypothesis.

Use the canonical full stopped-train forest, including singleton contacts.
Let `H_L` be the train family having a distinguished exterior occurrence
on at least one actual unit side of the loaded hull. Put

\[
 g=q-m,\qquad T=q-k+2f,\qquad N_0=T-|H_L|,
 \qquad R_H=\#\{\text{rhombi incident to a train in }H_L\}.
\]

Here `m` counts nonunit loaded-hull sides, `f` counts physical bounded
nonquadrilateral contact faces, and `k=d_H+s_Z`. Canonical train topology
gives `|H_L|>=g-2`: at most two trains can have two distinguished hull
ends. Also `T<=3q<=3pi D`.

**Theorem 9.1 (proved candidate awaiting independent audit/promotion).**
For every unbounded canonical C-II source sequence, in either global
branch and retaining all source points,

\[
 R_H=o(D^2),\qquad N_0\ge2\sqrt{R_4}-o(D). \tag{9.1}
\]

**Proof.** Fix a phase width `epsilon>0`, small enough for the estimates
below. Canonical Section 69 removes `O_epsilon(D)` crossing relations
so that every retained crossing has both train potentials in one real
phase bin of width `epsilon`; train direction is its potential plus
one of three labels times `pi/3`. Section 68 supplies the required
angular budget `E_4=O(D)` in **every** post-ZF branch.

A train in `H_L` in one bin has a distinct unit loaded-hull side in
one of its three projective direction intervals. Orient that side in
loaded-hull cyclic order and let `p` be its starting endpoint. Both
endpoints are actual diameter endpoints. The short-chord argument of
Section 8.2, with chord length one and no lattice approximation error,
puts the chosen strict diameter normal `n_p` within
`(4+8L_D)/D` of one of the two normals to this side. Its bin therefore
gives six oriented normal windows of half-width

\[
 t=epsilon/2+(4+8L_D)/D.
\]

Each starting endpoint accounts for at most one cyclic hull side.
Equation (8.2), for all sufficiently large `D`, bounds the number of
these sides, and hence the number `h_j` of `H_L` trains in the bin, by

\[
 h_j\le6\{1+2Dt+4L_D\}
      =6epsilon D+120L_D+54. \tag{9.2}
\]

This bound is uniform over phase-bin shifts and over the bin location.
It uses strict actual diameter support, not a disk inside the loaded
hull and not a correspondence with source-hull sides.

Let `T_j` be the total train population of the bin. Simplicity of the
actual train-crossing graph bounds its retained crossing relations
incident to `H_L` by `sum_j h_j T_j`. Since `sum_j T_j=T<=3pi D`,

\[
 R_H\le(6epsilon D+120L_D+54)3pi D+O_epsilon(D).
\]

For each fixed `epsilon`, division by `D^2` and `L_D=o(D)` give
`limsup R_H/D^2<=18pi epsilon`. Taking `epsilon` to zero after the
sequence limit proves the first claim of (9.1). Delete `H_L` only
from the auxiliary train graph. Its remaining simple triangle-free
graph has `N_0` vertices and `R_4-R_H` edges. Mantel's inequality gives
`N_0>=2 sqrt(R_4-R_H)`, and
`sqrt(R_4-R_H)>=sqrt(R_4)-sqrt(R_H)` proves the second claim. No source
point, contact, diameter, or rhombus is deleted. QED.

Combining (9.1) with the exact existing train/face ledger gives the
all-branch parametric inequality

\[
 \boxed{5(q-k)+x_B+m+2\ge3P_F+2\sqrt{R_4}-o(D).} \tag{9.3}
\]

Indeed,

\[
 N_0\le(q-k)+2Q-q+m+2
       =5(q-k)-3b+x_B+m+2,
\]

while `b>=P_F`. There is no substitution `P_F~pi D` or
`R_4~pi D^2/(2sqrt(3))` in (9.3). Those substitutions belong to Type II.
For a Type-I source, the actual `P_F` and `R_4` remain in the inequality.

The canonical nearby-diameter-endpoint incidence theorem further says
that every loaded-loaded unit contact is a side of the full source
hull, for all sufficiently large `D`: take any fixed
`1<t<sqrt(2)` in Audit.103. It is consequently a loaded-hull side as
well. Thus the actual loaded-contact count is `e_BB=q-m` in both
branches at that large-`D` scope. With

\[
 mu_DD=e_{BB}+2s_C-3k=q+m-k-2c_I-4,
\]

the existing exact slack identity, combined with (9.1), becomes

\[
 \boxed{4mu_DD\ge2P_F+2\sqrt{R_4}+k+3m-o(D).} \tag{9.4}
\]

Here `c_I=O(D^(2/3))` is the canonical all-phase component theorem,
so its correction is absorbed in `o(D)`. Neither (9.3) nor (9.4)
creates a packet or eliminates a macroscopic inactive container.
They retain a spendable actual-core quantity in the Type-I branch,
instead of importing the full-core disk or density there.

## 10. Separate-face cancellation also has an all-branch form

Canonical Audit.174 compares selected loaded-hull normals with the
atomless surface measure of a limiting disk. For its selected **short
outer chains**, actual strict diameter normals supply an atomless
measure in both global branches. A macroscopic loaded-hull gap has a
long side, which the fixed chain-length cutoff excludes.

### 10.1 Atomless actual-normal measure and oriented short chords

Choose one strict actual diameter normal for each loaded endpoint and set

\[
 nu_D=D^{-1}\sum_{p\in B}\delta_{n_p}.
\]

Its mass is at most `pi`. By (8.2), a window of half-width `t<pi/2`
has mass at most `1/D+(sin t+2L_D/D)/cos t`. Continuous majorants of
a point supported in successively smaller windows show that every weak
limit of `nu_D` is atomless. This is uniform over normal choices and
does not require a disk limit for the loaded hull.

For fixed `L`, consecutive loaded endpoints with chord length at most
`L` have chosen normals differing by `o(1)`. Their **forward** chord
tangent differs by `o(1)` from `Jn_p`, with the same oriented sign.
Indeed, cyclic order of strict supporting normals agrees with cyclic
hull-vertex order. The alternative long cyclic interval between two
nearly equal normals would put every other chosen loaded normal in the
complementary `o(1)` window. Equation (8.2) would give `q=o(D)`, against
`q>=ceil D`. Thus the short interval is used, and the forward chord
tangent lies between its two rotated normals.

### 10.2 All-branch face floor

**Theorem 10.2 (proved candidate awaiting independent audit/promotion).**
For every unbounded canonical C-II source sequence, in either global
branch and retaining all source points,

\[
 \boxed{f-k\ge(6/5)\sqrt{R_4}-o(D),} \tag{10.1}
\]

and consequently, for `z=b-P_F>=0`,

\[
 \boxed{2(q-k)-k-z\ge P_F+(6/5)\sqrt{R_4}-o(D),} \tag{10.2}
\]

\[
 q-k\ge P_F/2+(3/5)\sqrt{R_4}+(k+z)/2-o(D). \tag{10.3}
\]

These are asymptotic sequence inequalities, not explicit finite error
bounds. In Type II, substituting canonical disk and rhombus-population
limits recovers Audit.174's already promoted floor. In Type I, the
actual `P_F` and `R_4` remain in the statement.

**Proof.** We reconstruct the limiting bridge before using Audit.174's
exact separate-face incidence calculation. Pass to a joint-limit
subsequence with `R_4/D^2->r`. Disjoint actual rhombi have area at least
`sqrt(3)/2`, so this ratio is bounded. Put mass `1/D` at each complete
physical train direction, including singleton contacts. The total mass
is at most `3pi`; let its weak limit have atomic mass `a`.

The simple actual crossing graph makes its ordered crossing measure
dominated in the limit by the product train measure. Canonical
all-branch `E_4=O(D)` supports that limit on the projective 60-degree
relation, which a product measure charges only on atom pairs. Weighted
Mantel, first on finite atom neighborhoods and then on their exhaustion,
gives `r<=a^2/4`, hence `a>=2 sqrt(r)`.

Select complete trains `A_D` through shrinking finite neighborhoods
exhausting those atoms, with null neighborhood boundaries and a
diagonal sequence. As in the canonical atom-selection argument,

\[
 |A_D|/D\to a,\qquad
 \sum_{tau\notin A_D}d_{tau}=o(D^2), \tag{10.4}
\]

where `d_tau` is actual crossed-rhombus degree. Train terminal-midpoint
distance is at most that degree. Markov leaves only `o(D)` complementary
trains with terminal separation greater than `epsilon_D D`, for some
`epsilon_D->0`. Singleton terminal midpoints coincide. These selections
remove no source point or active packing row.

Make one recipient for each outer contact chain `W_i` between consecutive
loaded vertices and one **separate** recipient for each bounded physical
nonquadrilateral face. Each complementary train joins its two actual
terminal recipients. Retain loops and parallel edges. Let `c_partial`
count components meeting an outer recipient, and `f_partial` count the
exceptional faces in those components.

Fix recipient count cutoff `M` and recipient walk-length cutoff `L`.
Components having more than `M` recipients number at most
`(q+f)/(M+1)`. Components with a recipient walk longer than `L` number
at most `(b+4f+Q)/(L+1)`. Components containing a long complementary
train from (10.4) number `o(D)`. The numerators are `O(D)` by the
canonical Euler/train ledger.

In each remaining boundary component, bounded recipient walks and at
most `M` connecting short complementary trains put all chain bases and
facial occurrences within `o(D)` of one another. The actual-normal
identity `D(n_p-n_q)=2(p-q)-2(m_p-m_q)` puts its chain bases' normals
within `o(1)` of one common normal. Section 10.1 gives a common
**oriented** limiting tangent for all forward outer chords, each of
length between one and `L`.

Every bounded facial boundary sums to zero, and each complementary
train's two oriented terminal vectors cancel. Thus exactly

\[
 \sum_{W_i\text{ in component}}(b_{i+1}-b_i)
  =\sum_{\text{selected atomic terminal occurrences in component}}e.
                                                        \tag{10.5}
\]

The left side has a nonzero limit, since the bounded list of forward
chords has one common oriented tangent and each chord length is at least
one. Mark the component by one chosen chain-base diameter normal and
its ordered list of at most `ML` selected atomic terminal vectors.
Normalize record measures by `1/D`.

Every vector-coordinate marginal is dominated by the selected terminal
measure and has limiting support in the countable signed atomic
direction set. There are countably many finite lists from that set.
Equation (10.5) determines the limiting normal as the right rotation
of the normalized nonzero list sum. The normal marginal is countably
supported. Distinct components choose distinct chain bases, so it is
also dominated by `nu_D`, whose limits are atomless. It must be zero.
For fixed `M,L`, retained boundary components therefore number `o(D)`.
The discarded-component estimates, followed by `M,L->infinity`, give

\[
 c_partial=o(D). \tag{10.6}
\]

This replaces the disk surface-measure bridge. No loaded-hull gap
bound or Type-II population equality was used.

Retain the exact incidence calculation, including interior-only
components. Let `N_partial,N_circ` count complementary trains in
boundary and interior-only recipient components; let `Q_circ` be
exceptional-face excess in the latter. Component edge count and the
terminal handshake give

\[
 N_partial\ge q+f_partial-c_partial,
\]
\[
 0\le a_partial=b+4f_partial+Q-Q_circ-2N_partial
       \le2f_partial-Q_circ-2k+2c_partial.
\]

Since `Q_circ>=f-f_partial`,

\[
 3f_partial\ge f+2k-2c_partial. \tag{10.7}
\]

The interior-only atomic terminal population is
`4(f-f_partial)+Q_circ-2N_circ`. Adding both atomic populations,
dividing by two, and using the boundary edge lower bound yields

\[
 |A_D|+N_circ\le2f-f_partial-k+c_partial.
\]

Combine with (10.7):

\[
 3(|A_D|+N_circ)\le5(f-k+c_partial). \tag{10.8}
\]

Divide by `D` and use `a>=2 sqrt(r)`, (10.4), (10.6), and
`N_circ>=0`. This proves `liminf(f-k)/D>=6 sqrt(r)/5` on every
joint-limit subsequence. Any subsequence violating (10.1) has a further
one of this kind, so (10.1) holds. Finally
`Q-k=2(q-k)-k-P_F-z>=f-k` proves (10.2)--(10.3). QED.

This fuses universal full-source diameter geometry with actual
train/face cancellation. Its new bridge is the actual-endpoint normal
measure in place of a Type-II loaded-hull disk measure. It supplies
neither positive face width nor a vacancy or full-source finite move.

## 11. A sharper universal diameter-midpoint bound

The all-branch normal measure above used the canonical `O(D^(3/4))`
midpoint ball. The full-source area budget improves this to `O(D^(2/3))`.
This statement holds for **every** noncollinear global minimizer; no
triangle-free, contact-normalization, or Type-II hypothesis is needed.

**Theorem 11.1 (proved candidate awaiting independent audit/promotion).**
Let `K=conv A`, `D=D(n)>=7`, and let `o` be a circumcenter of `K`.
Every actual diameter midpoint `m` satisfies

\[
 \boxed{|m-o|\le7D^{2/3}.} \tag{11.1}
\]

**Proof.** Translate `o` to zero. Canonical full-source geometry gives
`D/2<=R<D/2+eta`, `R-r<eta`, and

\[
 eta=3^{1/4}\sqrt D,\qquad
 A(K)>\pi D^2/4-c_0P,\quad c_0=\sqrt3/4,\quad P\le\pi D.
\]

If `o'` is an incenter, containment of its inball in the circumdisk
gives `|o'|<=R-r<eta`. Its support function satisfies
`h>=r-|o'|>=R-2eta>=D/2-2eta`, including the range where that
lower bound is negative. Thus the support function `h(theta)` obeys

\[
 D/2-2eta\le h\le D/2+eta,
 \qquad \int h=P\le\pi D.
\]

Set `g=h-D/2`. Then `|g|<=2eta` and `int g<=0`. Minkowski's planar
area formula, using `dS_K=h+h''` distributionally and integration by
parts, gives

\[
 2A(K)=\int_0^{2pi}(h^2-(h')^2)\,dtheta.
\]

It follows that

\[
 \begin{aligned}
 \int(h')^2
 &=\int h^2-2A(K)\\
 &\le\pi D^2/2+8pi eta^2-2A(K)\\
 &<8pi eta^2+2c_0pi D
   ={17pi\sqrt3\over2}D=:C_ED. \tag{11.2}
 \end{aligned}
\]

For `D>=7`, `h<=R<=D`. Convexity says `h''+h` is a nonnegative
measure, so `h''>=-D` distributionally. If `h'(theta)=s>0` at a
differentiability point, then for almost every `0<=t<=s/D`,
`h'(theta+t)>=s-Dt`. Since `|h'|<=R<=D`, this interval has length
at most one. Integrating its squared lower bound in (11.2) gives

\[
 s^3/(3D)\le C_ED,
 \qquad |h'(theta)|\le(3C_E)^{1/3}D^{2/3}. \tag{11.3}
\]

For a negative derivative the same argument runs backwards. The support
function of a polygon is smooth inside each strict vertex normal cone
and has only upward derivative jumps at side normals, so the stated
one-sided inequalities apply directly; they also follow from the
distributional inequality.

For a diameter pair `p,p'`, let `n=(p-p')/D` and `m=(p+p')/2`.
The diameter support inequality strictly exposes `p` in direction `n`
and `p'` in direction `-n`. Therefore

\[
 m\cdot Jn=p\cdot Jn=h'(n),\qquad
 h(n)+h(-n)=D.
\]

Both supports are at most `D/2+eta`, so `|m dot n|<=eta`.
Equation (11.3) bounds the tangential component. Finally
`C_E<187/4`, using `pi<22/7` and `sqrt(3)<7/4`; hence
`(3C_E)^(1/3)<6`. Thus

\[
 |m|^2\le36D^{4/3}+eta^2
        <38D^{4/3}<49D^{4/3},
\]

which proves (11.1). Every source point is retained in `K`. QED.

### 11.2 Quantitative all-branch hull-train depletion

Theorem 9.1 can now be made quantitative:

\[
 \boxed{R_H=O(D^{5/3}),\qquad
 N_0\ge2\sqrt{R_4}-O(D^{5/6}).} \tag{11.4}
\]

The constants are universal for canonical C-II sources. In (9.2), use
the midpoint bound `L<=7D^(2/3)` and phase width `epsilon=D^(-1/3)`.
The exact Section-69 phase-coarea deletion bound is
`(3/pi+1/epsilon)Delta`, with `Delta=O(D)` uniformly by Section 68.
Thus the omitted crossings number `O(D^(4/3))`; the retained crossings
incident to hull-ended trains number
`O((epsilon D+L+1)D)=O(D^(5/3))`. Mantel and
`sqrt(x-y)>=sqrt(x)-sqrt(y)` give the second claim in (11.4).

The all-branch inequality (9.3) likewise has an `O(D^(5/6))` error.
In (9.4), canonical `c_I=O(D^(2/3))` is smaller and fits the same
error. The separate-face atomic compactness in Section 10 still has an
unspecified `o(D)` error; (11.4) does not give it a convergence rate.
None of these quantitative estimates constructs a source move.

### 11.3 Actual diameter graph dispersion

The improved midpoint ball also sharpens two existing geometric scales.
For a fixed source point `p`, every actual diameter partner `q` lies in
`B(2o-p,14D^(2/3))` and on the radius-`D` circle centered at `p`.
For all sufficiently large `D`, their circular span is at most
`2D arcsin(14D^(-1/3))<=56D^(2/3)`. Consecutive unit-separated
partners have arclength at least one. Thus

\[
 \deg_H(p)\le56D^{2/3}+1. \tag{11.5}
\]

For a canonical C-II source, `h>=ceil D`. Greedy matching removes at
most `2 maxdeg(H)-1` edges per chosen edge, so the actual diameter
graph has a matching of at least

\[
 {D\over112D^{2/3}+1}=Omega(D^{1/3}) \tag{11.6}
\]

edges. Its disjoint actual diameter segments cross pairwise by the
canonical planar diameter-thrackle theorem; every midpoint remains in
the common `7D^(2/3)` ball. These are actual source bars, not selected
new contacts or a lower-dimensional scaffold.

If the actual diameter graph has an odd cycle of length `ell`, orient
its successive vertices `p_0,...,p_{ell}=p_0` and midpoints `m_i`.
The recurrence `p_{i+1}=-p_i+2m_i`, iterated around an odd cycle,
gives `p_0` as an alternating sum of its midpoints. Since every actual
diameter endpoint has `|p_0-o|>=D/2-eta`,

\[
 \ell\ge{D/2-eta\over7D^{2/3}}=Omega(D^{1/3}). \tag{11.7}
\]

The normalization is about the same circumcenter in this calculation.
Neither the matching nor the cycle-length bound asserts a lower bound
on the stress weights of its bars or a feasible motion. Both exponents
are weaker than independently canonical square-root conclusions:
Audit.126 already gives a square-root matching for every linear actual
diameter subgraph, and C17 gives square-root actual odd-cycle girth.
The new assertion of this section is the uniform midpoint bound, not
a matching or cycle-girth improvement.

## 12. Short hull trains have a scoped face-end capacity

The finite five-hull-end pentagon regression remains binding. A universal
two-end rule is false. The following asymptotic statement additionally
uses actual source roundness and the quantitative rarity of **long**
hull-ended trains; the finite flower has neither hypothesis.

### 12.1 A small oriented window in a short unit polygon

For a simple closed unit-edge polygon with unit-separated vertices:

- a five-edge polygon has at most two directed edges in any oriented
  direction window of half-width `1/100`;
- a six-edge polygon has at most two;
- a seven-edge polygon has at most three.

For five or seven edges, more would make the projection of the selected
unit edges exceed the maximum opposite projection of all remaining
edges: `3cos(1/100)>2` and `4cos(1/100)>3`.

For six edges, suppose three directed edges are within `delta=1/100`
of one unit tangent `t`. Closure implies for the other three edges

\[
 \sum(1+w\cdot t)\le3(1-\cos delta)\le(3/2)delta^2.
\]

Each of these edges is within `sqrt(3)delta` of `-t`, while each
selected edge is within `delta` of `t`. The total discrepancy from
a closed six-step reference walk of three `+t` and three `-t` steps
is less than `9delta<1`. A closed unit-step walk on a line of length
six repeats a vertex before its final return. The corresponding two
actual polygon vertices would be less than one apart, contradiction.
Four or more selected edges are already excluded by projection.
This proof does not infer a uniform nonparallel-angle bound for arbitrary
large polygons.

### 12.2 The face normal is the normal at the actual hull end

Orient a nonsingleton train from a bounded terminal face toward its
distinguished unit hull end. Its contact edge direction is constant.
Across each rhombus, the terminal-edge midpoint advances strictly in
the outward normal of the starting face edge, by at least `sqrt(3)/2`.
At a shared intermediate edge, the next rhombus lies on the other side,
so this transverse sign persists along the train. At the hull end,
the actual supporting normal of the hull must have the same sign:
the preceding edge lies inside the hull. Thus the starting face-edge
outward normal equals the hull-side outward normal. A singleton side
shared by the bounded face and the hull has the same conclusion directly.

For sufficiently large canonical sources, Audit.103 says that every
unit pair of loaded endpoints is a full-source hull side. Hence the
distinguished unit loaded-hull side in this argument is also a side
of `K=conv A`, retaining all source isolates.

By Theorem 11.1's support-derivative proof, every point `y` of such a
full-source side, with its outward unit normal `n`, obeys

\[
 |y\cdot Jn|\le6D^{2/3},\qquad
 y\cdot n\ge D/2-2eta.
\]

The derivative bound also holds for the two one-sided limits at a side
normal, and hence for their convex combinations along the side. Its
outward normal therefore differs from `y/|y|` by `O(D^(-1/3))`.

### 12.3 Actual global face-end budget

**Theorem 12.3 (proved candidate awaiting independent audit/promotion).**
In either global canonical C-II branch, the number `E_HF` of bounded
physical exceptional-face terminal occurrences belonging to trains with
a distinguished unit loaded-hull end satisfies

\[
 \boxed{E_HF\le2Q+O(D^{5/6}).} \tag{12.1}
\]

Let a hull-ended train be long when its rhombus degree exceeds
`D^(5/6)`. Equation (11.4) bounds their total degree by `2R_H=O(D^(5/3))`,
so there are `O(D^(5/6))` long trains. Each has at most one bounded
face end and is charged to the error in (12.1).

For every other hull-ended train, its bounded face-edge midpoint `x`
and unit hull-side midpoint `y` are at distance at most `D^(5/6)`.
The two outward normals agree by Section 12.2. If several such ends
occur on the same face of degree five, six, or seven, their `x` points
are within seven of one another; their `y` points and normals consequently
lie within `O(D^(-1/6))` of one common radial normal. Their oriented
face-edge vectors thus lie in one window of width tending to zero.
For large `D`, Section 12.1 bounds their number by two, two, or three.
These bounds are each at most `2(deg F-4)`.

For a face of degree at least eight, the trivial occurrence bound
`deg F<=2(deg F-4)` suffices. This retains every large face and uses
no face-degree-tail assumption. Sum over all physical exceptional
faces and add the long-train error to prove (12.1).

The exact outer-end count also gives

\[
 2(q-m)-b-4\le E_HF.
\]

Indeed, at most two trains have two distinguished hull ends. Each
other distinguished end must be paired with a nondistinguished outer
end or a bounded face end, and there are only `b-(q-m)` nondistinguished
outer occurrences. Thus (12.1) yields

\[
 \boxed{4(q-k)\ge2(q-m)+b-O(D^{5/6}),} \tag{12.2}
\]

equivalently, writing `u_B=b-q-m`,

\[
 \boxed{q+m\ge4k+u_B-O(D^{5/6}).} \tag{12.3}
\]

This pays a specific bounded-face terminal bank using actual full-source
geometry. It does not resurrect the false finite local two-end theorem:
large faces are retained, long hull trains are explicitly charged, and
the small-face conclusion is only eventual in the canonical large-`D`
regime. It supplies no compatible contact motion or refill packet.

### 12.4 A sharper budget with an explicit pentagon term

Let `f_5` be the number of actual bounded physical unit-pentagon faces.
Then the same argument gives the sharper estimate

\[
 \boxed{E_HF\le Q+f_5+O(D^{5/6}).} \tag{12.4}
\]

Here large faces are again retained; no face-tail hypothesis is introduced.
In addition to charging the long hull-ended trains as before, separate
the exceptional faces of degree greater than `D^(5/6)`. Their number
is at most `Q/(D^(5/6)-4)=O(D^(1/6))`, since `Q<=2q<=2pi D`.
For each of these faces the trivial terminal count is its degree,
which exceeds its contribution to `Q` by exactly four. Their total
extra charge is therefore `O(D^(1/6))`.

For each remaining exceptional face, its diameter is at most its degree,
hence at most `D^(5/6)`. All its short hull-ended terminal midpoints
are within that distance of one another. The argument in Section 12.3
therefore places all corresponding outward normals, and all oriented
face-edge vectors, in one common window of half-width `O(D^(-1/6))`.
This estimate is uniform over all such faces, including faces whose
degrees grow with `D`.

For any closed unit-edge polygon of degree `d>=7`, if `k` of its
oriented edge vectors belong to a window of half-width `delta=1/100`,
closure and projection give

\[
 k\cos\delta\le d-k.
\]

If `k>=d-3`, the right side is at most three whereas the left side is
at least `4cos(delta)>3`. Thus `k<=d-4` for every `d>=7`, uniformly.
The six-edge bound in Section 12.1 likewise gives `k<=2=d-4`.
The five-edge bound gives `k<=2=(d-4)+1`, which explains precisely
the additional `f_5` in (12.4). Summation proves the claim.

Combining the exact lower end count with (12.4), and using
`Q=2(q-k)-b` and `b=q+m+u_B`, yields

\[
 \boxed{f_5\ge2(k-m)-O(D^{5/6}).} \tag{12.5}
\]

The cancellation of `u_B` is exact:
`2(q-m)-b-Q=2(k-m)`. Consequently any canonical sequence with
`liminf (k-m)/D>0` has a linear population of actual unit-pentagon
faces. This is a conditional population consequence, not a proof that
`k-m` is positive. Such pentagons still obey the canonical common-angle
bit-collapse theorem. Their presence does not by itself produce a
source-compatible finite move.

Audit.186's newly imported carrier regression does not enter this
proof. In particular no shared carrier edge budget is identified with
the cost of full-graph disjoint paths.

## 13. A loaded unit chain constrains single lattice ports

The two-port chart theorem does not cover a loaded vertex that has two
loaded hull neighbors and only one unloaded contact neighbor. The
following finite lemma uses the neighboring loaded unit sides to supply
the additional constraints. It is a new candidate, with unreviewed
lifecycle; the local lattice-port package is not extracted by the
canonical selected-grid theorem.

### 13.1 Seven collinear sites and five triangular-lattice ports

Let `t` be a unit vector and `p_i=i t` for `0<=i<=6`. Let `Lambda`
be a translate of a unit triangular lattice. Suppose `a_1,...,a_5`
are points of `Lambda` in one closed half-plane bounded by the line
through the `p_i`, satisfying

\[
 |a_i-p_i|=1,\qquad |a_i-p_j|\ge1\quad(0\le j\le6),
 \qquad a_i\ne a_{i+1}\quad(1\le i<5).
 \tag{13.1}
\]

**Lemma 13.1.** The vector `t` is one of the six unit vectors of
`Lambda`. No uniqueness of the anchor displacement is asserted.

**Proof.** Use coordinates with `t=(1,0)` and with the anchor half-plane
below the horizontal line. Write `a_i=(i+x_i,y_i)`. Distances from
`p_{i-1}` and `p_{i+1}` give
`-1/2<=x_i<=1/2`. The unit distance to `p_i` then gives

\[
 -1\le y_i\le-\sqrt3/2.
\]

Put `delta=1-sqrt3/2<1/7` and `w_i=a_{i+1}-a_i`, for `1<=i<=4`.
Every `w_i` is a nonzero triangular-lattice vector. Its horizontal
coordinate lies between zero and two, and its vertical coordinate
has magnitude at most `delta`. It cannot have zero horizontal
coordinate, since then its length would be less than one. Thus

\[
 w_i\cdot t>0,\qquad |w_i\cdot Jt|\le\delta,
 \qquad |w_i|^2\le4+\delta^2<5.
\]

The triangular-lattice Gram form is `a^2+ab+b^2`; its nonzero values
below five are exactly `1,3,4`. The corresponding vectors have lengths
`1,sqrt3,2`: the length-two vectors are twice unit lattice vectors,
and the length-`sqrt3` vectors are at angles `pi/6` modulo `pi/3`
from the unit directions.

At least one `w_i` has length one. Otherwise all four have horizontal
coordinate at least `sqrt(3-delta^2)>5/4`, contradicting

\[
 \sum_{i=1}^4w_i\cdot t
   =4+x_5-x_1\le5.
\]

Let `u` be such a unit vector. Its angle from `t` has magnitude at
most `arcsin(delta)`. No length-`sqrt3` vector can meet the vertical
strip condition, because

\[
 \sqrt3\sin(\pi/6-\arcsin\delta)>\delta.
\]

No other unit direction, or its double, can meet that condition either:
the nearest different unoriented unit direction is at angle `pi/3`
from `u`, and
`sin(pi/3-arcsin(delta))>delta`. Positivity of the horizontal
coordinate rules out `-u` and `-2u`. Hence every increment is `u`
or `2u`.

Two consecutive increments must both be `u`. If not, at most two
of the four increments are `u`, so their sum has horizontal coordinate
at least `6(u dot t)>=6sqrt(1-delta^2)>5`, the same contradiction.
For the resulting three consecutive anchor/site pairs, write their
relative displacements as `v`, `v+(t-u)`, `v+2(t-u)`. All three have
norm one. Taking a second finite difference of their squared norms
gives `2|t-u|^2=0`. Thus `t=u`. QED.

The distinct-consecutive-anchor condition matters. A common anchor
for adjacent loaded unit sites would be a unit equilateral triangle;
such a common anchor is excluded in the actual triangle-free source.
No forbidden local finite-motion conclusion is used here.

### 13.2 Stable actual source version

Consider seven consecutive actual loaded hull vertices connected by
six unit hull sides in a canonical source with `D->infinity`. Suppose
each of the five interior loaded vertices has a chosen actual unit
neighbor outside `B`. Suppose those five chosen neighbors are within
`epsilon_D->0` of one translated unit triangular lattice, with its
orientation chosen from `J` reference orientations, where `J` is fixed.
The translation may vary freely from one seven-vertex window to another.

Then the loaded unit sides in that window have direction within
`tau_D->0` of a unit vector in the corresponding reference lattice.
This convergence is uniform over all such windows and translations.

Indeed, Section 12.2 puts their hull normals within `O(D^(-1/3))`
of their local radial normals. A fixed seven-vertex window has bounded
physical diameter, so those radial normals, and then all its unit-side
directions, agree up to `o(1)`. Normalize one site and extract a
contrary sequence. The seven loaded sites converge to the collinear
unit chain. All actual chosen neighbors lie inside the full source hull,
so their limits lie in its inner half-plane. Their unit distances and
all other source lower bounds pass to the limit.

Consecutive chosen actual neighbors are distinct, since sharing one
would make an actual unit triangle. Their reference lattice sites
are also distinct for large `D`: two distinct source neighbors are
at least one apart and cannot round to the same site with error
`epsilon_D<1/2`. After fixing the bounded lattice differences and
passing to a subsequence, the limit satisfies (13.1). Lemma 13.1
contradicts the assumed persistent distance of the tangent from all
six reference directions. This proves uniform stability by compactness;
no algebraic perturbation rate is claimed.

The hull is `conv A` of the full source, including every contact isolate.
Each chosen neighbor is an actual source point. Neither a selected
scaffold nor a hypothetical lattice packet is substituted for it.

### 13.3 A single-port atlas obstruction on long unit runs

Choose an unloaded unit neighbor at every loaded vertex except a set
of `b_0` exceptions. Suppose the chosen neighbors are assigned to `J`
charts with unit triangular reference lattices, and the chart assignment
changes `R_D` times in cyclic loaded-hull order. Assume that any five
chosen neighbors belonging to one chart in a seven-vertex unit window
are `epsilon_D->0` close to one translate of that chart's reference
lattice. A whole actual slow chart with Lipschitz constant `K/D`
satisfies this local condition: those five anchors have bounded pairwise
physical distance, hence bounded reference distance, and their chart
displacements differ by `O(K/D)`.

Let `m` count nonunit loaded-hull sides as above. A center whose
seven-vertex window fails the six-unit-side condition is charged to one
of at most `6m` centers. A missing chosen neighbor is charged to at
most `5b_0` centers. A chart transition in the five-anchor window is
charged to at most `4R_D` centers. Every remaining center satisfies
Section 13.2.

Those remaining loaded vertices have their chosen actual diameter
normals within `o(1)` of the `6J` oriented normals perpendicular to
the reference unit directions. The uniform window bound of Section 8,
now with midpoint radius `7D^(2/3)`, bounds their number by `o(D)`.
The reference orientations may vary with `D`; the bound is uniform.
Consequently

\[
 \boxed{q\le6m+5b_0+4R_D+o(D).} \tag{13.2}
\]

In particular the canonical source cannot have simultaneously
`m=o(D)`, `b_0=o(D)`, and `R_D=o(D)` under this actual local single-port
atlas condition, because `q>=D`. This excludes a class not covered by
the two-anchor port theorem: the loaded vertex may have only one
unloaded contact neighbor, with its other contacts along the loaded
unit hull run.

Neither small `m` nor the single-port atlas is presently canonical.
The inequality supplies no move for a surviving large-`m` source and
does not control an atlas with linearly many changes or failures.
It is a finite geometric bridge and a scoped source obstruction,
not C-II or Level I closure.

### 13.4 Three fixed ports admit only finitely many chain directions

**Lemma 13.4.** There is also a more general finite statement, without a triangular
lattice or half-plane hypothesis. Fix distinct planar anchors
`a_0,a_1,a_2` and integers `0<r<s`. Among placements

\[
 p_0=z,\qquad p_r=z+r t,\qquad p_s=z+s t,
 \qquad |t|=1,
\]

satisfying `|p_0-a_0|=|p_r-a_1|=|p_s-a_2|=1`, at most ten
distinct directions `t` occur. Translation of the whole anchor triple
does not affect that direction set. A translation family at one
fixed direction is allowed.

**Proof.** Translate `a_0` to zero and write `A=a_1-a_0`,
`B=a_2-a_0`. Thus `A,B` are nonzero and distinct. For fixed `t`,
the equations, after subtracting `|z|^2=1`, are

\[
 z\cdot(rt-A)=-\tfrac12|rt-A|^2,\qquad
 z\cdot(st-B)=-\tfrac12|st-B|^2. \tag{13.3}
\]

Their determinant is

\[
 d(t)=\det(t,sA-rB)+\det(A,B).
\]

If it vanishes identically on the unit circle, then
`sA-rB=0`, so `A/r=B/s=c`. Equations (13.3) imply
`z dot(t-c)=-r|t-c|^2/2=-s|t-c|^2/2`; hence `t=c`.
This gives at most one unit direction.

Otherwise `d(t)` has at most two zeros on the unit circle. Away
from those zeros, (13.3) gives `z(t)` rationally by Cramer's rule.
Its numerator coordinates have degree at most two in `t`, because
`|rt-A|^2=r^2+|A|^2-2r t dot A` is affine on that circle;
its denominator is affine. Thus `|z(t)|^2=1` is a polynomial
of degree at most four after clearing denominators. It has at most
eight circle intersections unless it holds identically on the circle.
Together with the two determinant zeros this gives the stated ten,
once the identity case is excluded.

Put `C=sA-rB`. In the present case `C` is nonzero. Taking `s`
times the first equation minus `r` times the second shows that
`z(t) dot C` is an affine function of `t`. Rotate coordinates so
`C` is horizontal. Then the first coordinate of `z(t)` is
`L(t)=c_0+c_1 t_x+c_2 t_y`, and the second is rational on the
circle.

If `|z(t)|=1` holds identically, `1-L(t)^2` must be a rational
square on the circle. If `L` is constant, both coordinates of
`z` are constant. If `L` is nonconstant, each of the two distinct
level sets `L=1` and `L=-1` must have only even-order zeros on
the complexified unit circle: a rational square has even valuation
at every point, and these two factors share no zero. Each level
line normally has two simple intersections. Both must therefore
be tangent. Their tangent conditions are

\[
 (c_0-1)^2=c_1^2+c_2^2=(c_0+1)^2.
\]

Consequently `c_0=0`, `c_1^2+c_2^2=1`, and
`z(t)=O t` for one fixed orthogonal matrix `O`. This is also
seen directly by squaring the perpendicular linear coordinate.
The sign is fixed on a nonempty interval, hence as a rational identity.

A constant `z=v` would require `|v+r t-A|=1` identically,
so `A=v` and `r=1`; the third anchor would likewise require
`B=v` and `s=1`, contrary to `r<s`.

In the orthogonal case, `|(O+rI)t-A|=1` identically forces
`(O+rI)^T(O+rI)` to be scalar and `(O+rI)^T A=0` by its
second and first circle harmonics. A nontrivial reflection fails
the scalar condition. For a rotation `O`, the matrix `O+rI`
is invertible unless `r=1` and `O=-I`. The invertible case
would give `A=0`, contrary to distinct anchors. In the remaining
case the third equation has the invertible matrix `(s-1)I`
and forces `B=0`, also contrary to distinct anchors. Thus no
identity case survives. QED.

This proof classifies the possible tangent directions, not all
assemblies or finite motions. It uses the ordinary conic/rational
zero-count argument explicitly; no numerical root count is substituted.

**Repeated-anchor variant.** The anchors may coincide if the additional
source lower bound `|p_r-a_0|>=1` is imposed. There are still at most
ten feasible tangents. The same calculation applies; only the identity
case needs another check. A constant `z` is excluded exactly as before.
For `z=O t`, a nontrivial reflection still fails the second-harmonic
condition. For a rotation, `O+sI` is invertible since `s>=2`, so
the third unit-circle identity forces `B=0`. Both `p_0` and `p_s`
then lie on the unit circle about `a_0=0`. Their strict intermediate
point `p_r=(1-r/s)p_0+(r/s)p_s` lies in its open disk, contradicting
`|p_r-a_0|>=1`. Thus identity branches contribute no permitted
directions away from the at most two determinant zeros. The remaining
polynomial roots are bounded as before. This explicitly uses a
cross-pair lower constraint; it cannot be inferred from the three
chosen unit contacts alone.

### 13.5 Sparse single ports in a finite rhombic-chart atlas

Consider a canonical sequence in either source branch. Let `W_D`
be loaded vertices with chosen actual unloaded unit neighbors,
and let `a_D=|W_D|`. Assign these neighbors to `J` actual charts,
where `J` is fixed. Each chart has a unit rhombic reference lattice
with basis angle in `[pi/3,2pi/3]`. The bases may vary with `D`.
Assume the following local property: for every fixed `M`, neighbors
assigned to one chart within an `M`-vertex loaded unit run are
`epsilon_{D,M}->0` close to one common translate of its reference
lattice. Distinct actual neighbors must round to distinct reference
sites. Actual slow charts of Lipschitz constant `K/D` satisfy the
property on these bounded physical windows.

Then

\[
 m=o(D)\quad\Longrightarrow\quad a_D=o(D). \tag{13.4}
\]

In particular a finite actual slow-chart atlas cannot cover a linear
population of chosen single unloaded ports along a loaded hull with
only a sublinear number of nonunit sides. This needs neither
consecutive ports at every vertex nor a small atlas-change count.

To prove this, fix `M` and partition the cyclic loaded sequence into
blocks of at most `M` vertices. Discard blocks crossing a nonunit side;
they cost at most `Mm` vertices. In every remaining block containing
more than `2J` chosen ports, three ports belong to one chart. Their
indices, relative to the first, are `0<r<s<M`. The bounded physical
window makes their actual unloaded neighbors distinct for large `D`.
Adjacent loaded ports cannot share a neighbor without a triangle.
Two nonadjacent ports in a unit run cannot share one in the straight
window limit: distance greater than two is impossible, and distance
two would put the common neighbor at an intervening loaded site,
violating its lower separation. Reference rounding therefore preserves
three distinct anchors.

After rotating and passing to a subsequence, every one of the `J`
unit rhombic bases converges to a nondegenerate reference basis.
There are only finitely many possible anchor-difference patterns
within an `M` window, uniformly over these bases: the lower singular
value is bounded away from zero, while the physical differences are
bounded by `M+2+o(1)`. Lemma 13.4 supplies at most ten tangent
directions for each limiting pattern. The same normalized-window
compactness as in Section 13.2 puts every such rich block's tangent
within `o(1)` of this fixed finite set. It is unnecessary to track
roots continuously through changing bases.

The actual diameter-normal window count consequently puts only `o(D)`
loaded vertices in all rich blocks. Each other undiscarded block
has at most `2J` ports. Hence, for every fixed `M`,

\[
 a_D\le Mm+2J\left(\lceil q/M\rceil+1\right)+o(D).
 \tag{13.5}
\]

When `m=o(D)`, divide by `D`, use `q<=pi D`, take the limit
at fixed `M`, and then send `M` to infinity. This proves (13.4).
The order of limits is part of the proof.

Canonical Type-II cells already have a uniform linear attachment
population. Thus (13.4) excludes `m=o(D)` if their actual chosen
single-port neighbors lie in such a finite atlas. Canonical local
selected grids do not establish that positional atlas. The proof
still leaves large `m`, atlas failures, and the source-compatible
replacement obligation open.

### 13.6 Near-unit hull saturation replaces the exact unit-run condition

The exact contact condition on the loaded sides can be weakened. Retain
the finite single-port atlas of Section 13.5, with its local property now
required on every bounded physical loaded window, not just exact unit
runs. Actual `K/D` slow charts have precisely this property. Then

\[
 P_F-q=o(D)\quad\Longrightarrow\quad a_D=o(D). \tag{13.6}
\]

This applies in either global branch. In particular it applies when
`q/D->pi`, without any assumption on the number `m` of nonunit
sides or on chart transitions.

Write the loaded hull side lengths as `ell_i>=1`. Their total excess
is `E_D=sum(ell_i-1)=P_F-q`. If `E_D=o(D)`, choose
`delta_D->0` so that `E_D/delta_D=o(D)`, for example
`delta_D=sqrt(E_D/D)+D^(-1/10)`. Only `o(D)` sides have
`ell_i>1+delta_D`. Partition into fixed `M`-vertex blocks and
discard every block containing one of these sides. This costs `o(D)`
vertices at each fixed `M`.

Every remaining side has length `1+o(1)`. For large `D`, its length
is below a fixed `t in (1,sqrt2)`, so canonical Audit.104 makes it
an actual full-source hull side even when it is not a unit contact.
The support-derivative bound and bounded block diameter make each
such block converge, after normalization, to a straight unit chain.

Any block containing more than `2J` ported vertices has three ports
in one chart. Their chosen neighbors and rounded sites may repeat;
distinct actual source neighbors still round to distinct sites. The
limiting pattern satisfies the repeated-anchor variant of Lemma 13.4,
because the first chosen neighbor is unloaded and has source distance
at least one from the middle loaded port. The finite direction and
diameter-normal argument
therefore makes the total rich-block population `o(D)`, just as
before. The other blocks contain at most `2J` ports each, giving

\[
 a_D\le2J\left(\lceil q/M\rceil+1\right)+o(D)
\]

at fixed `M`. Sending `D` and then `M` to infinity proves (13.6).
Every full-source cross lower bound is retained. Audit.104 is used
for the near-unit full-hull-side identification, not to supply a
distinct-port matching.

Thus a fixed finite slow-chart atlas covering `a_D>=gamma D`
actual single unloaded ports forces a positive asymptotic gap in
`(P_F-q)/D`. Equivalently, such a family cannot approach loaded-hull
unit-length saturation. The gap is conditional and nonexplicit;
the atlas itself is not currently extracted. In Type II, the canonical
linear attachment population would supply the port count once the
actual neighbor atlas was justified.

## 14. Bounded shore variation supplies the local single-port condition

The pointwise `K/D` slow-chart hypothesis can be removed for actual
additive charts. Consider a fixed number `J` of source charts of the form

\[
 x_{ij}=x_{00}+i u+jv+a_i+b_j,
 \qquad a_0=b_0=0,
 \qquad \sum_i|a_i-a_{i-1}|+\sum_j|b_j-b_{j-1}|\le C,
 \tag{14.1}
\]

where `u,v` are unit rhombic bases of angle in `[pi/3,2pi/3]`
and `C` is fixed. The actual chosen unloaded contact neighbors are
occupied chart positions. Other chart positions need not be occupied,
and no whole-cell chart identification is assumed.

**Theorem 14.1 (proved candidate awaiting independent audit/promotion).**
If `P_F-q=o(D)`, the number of loaded vertices that have even one
chosen actual unloaded unit neighbor in these `J` charts is `o(D)`.
Fixed-size shore jumps and arbitrary chart assignment changes are
permitted. In particular a positive linear port bank cannot be covered
by finitely many such actual charts in the loaded-hull near-unit regime.

**Proof.** Fix a loaded block size `M`. The displacement in (14.1)
has norm at most `C`. Consequently two anchors in one bounded
physical loaded block have reference-position distance at most
`M+2+2C+o(1)`. The dual basis functionals have norms at most two,
so their two index differences are at most the fixed integer

\[
 L=\lceil2(M+3+2C)\rceil.
\]

Call a shore increment bad if its norm exceeds `delta_D=D^(-1/4)`.
There are at most `C/delta_D=O_C(D^(1/4))` bad increments in each
chart, combining its two shores. Exclude chosen anchors whose index
is within `L` of one of these bad increments.

This excludes only `O_{C,M}(D^(3/4))` loaded ports per chart.
Indeed, indices within `L` of a given first-shore cut lie in a
physical strip of fixed width `O(C+L+1)` around the corresponding
line parallel to `v`; a second-shore cut gives a line parallel to
`u`. The full displacement has norm at most `C`, and passing from
an anchor to its loaded unit neighbor widens the strip by at most
two. The exact endpoint strip bound (12.3) in the localized report,
reconstructed there directly from an actual diameter partner, puts
at most `O_{C,M}(sqrt D+1)` loaded endpoints in each strip.
Union-bound over the `O_C(D^(1/4))` cuts. Multiple ports assigned
to one strip do not alter this endpoint count.

For any remaining same-chart anchors within the fixed loaded block,
each shore index difference is at most `L`. No intervening shore
increment is bad: the chosen endpoints were excluded within `L`
of every bad increment. Their additive displacements therefore
differ by at most `2L delta_D=o(1)`. They are all `o(1)` close
to one common translate of the chart's reference lattice, exactly
the local property required in Section 13.6. Reference bases remain
nondegenerate uniformly, and distinct occupied chart positions have
distinct index labels.

Now apply the near-unit-block argument of Section 13.6, counting the
excluded ports separately. At fixed `M`, it gives

\[
 a_D\le O_{J,C,M}(D^{3/4})
       +2J\left(\lceil q/M\rceil+1\right)+o(D).
\]

Divide by `D`, take the limit, and then send `M` to infinity.
This proves the theorem. All strips and all anchors are actual
full-source objects; no independent exchange is assembled from
one-at-a-time candidates. QED.

The angular-surplus implication in Section 13 of the localized report
provides (14.1) for an **actual consecutive additive chart** whose
every shore increment participates in `cD` actual rhombus faces and
whose rhombus surplus is at most `C_0D`. Thus finitely many such
grains can carry only a sublinear bank of direct loaded unit ports
when `P_F-q=o(D)`. A selected coherent train grid is still not
automatically such an additive chart; that distinction is preserved.

This is a contact-access exclusion. It gives neither global atlas
coverage of the actual attachment neighbors nor a finite outside-grain
payment. The source may retain a linear collar population outside
these grains, or a linear hull side-length excess. C-II is unchanged.

## 15. Compared use of the one-pin oblique refill

After the preceding candidates were developed, the review worktree
imported `fb2cd24629417d9c6e7cd20f1d7fd03c23ae2f29`, state
`2026-10-09.audit.181`. Independent Audit.187 is canonical input
only at its recorded actual-wall scope. Its four promoted claims and
triangular pinned-motion regression were read in full before import.

For an actual near-oblique rectangular unit wall of side counts
`m,n>=3`, with reference angle `pi/3<phi<=pi/2`, put

\[
 L=m+n,\qquad K=(m-1)(n-1),\qquad
 g={(1-2\cos\phi)^4\over25\cdot10^{12}L^{20}}.
\]

The reference one-pin packet has `K` strict sites after deleting
the boundary label `p_(1,0)`. If the actual interior population
`z<=K-1`, replacing all `z` interior labels plus that wall label
by `z+1` packet sites contradicts contact-minimal global optimality.
Thus the promoted conclusion is `z>=K`, counting all isolates.
It does **not** exclude an actual wall whose population is `K`
or larger. An exact complete oblique source grid has exactly `K`
interior chart vertices and satisfies this lower bound.

The audit statement uses the conservative tolerance `g/(4(L+1))`;
the manifest and current ledger use `g/(4L)`. The latter still
preserves strict target-wall separation in the same proof: the
displayed squared-distance loss `2(L+1)eta` is then at most
`7g/12<g` because `L>=6`. All other containment and crossing
checks use only `eta<<1/100` and remain valid. This numerical
tolerance distinction is kept explicit; it is not a claim of
arbitrary-wall robustness.

For a convex qualifying wall, Audit.187 gives

\[
 r_W\le mn(\sin\phi/(\sqrt3/2)-1)
       +{2L\eta+L\eta^2\over\sqrt3/2}.
\]

That local residual estimate and Section 14's chart-port obstruction
are different conclusions. Section 14 requires only bounded shore
variation and bounded-window positional errors tending to zero.
Audit.187 instead requires pointwise wall error on the scale
`g/L`, which degenerates as the **fourth power** of the obliquity
and as `L^(-21)`. A near-triangular actual additive chart with
small but variable shore increments is not thereby within this
much smaller tolerance of a constant oblique frame. No such
identification is made.

The fixed-wall lock regression remains compatible: all pins fixed
can lock the complete interior; deleting one pin permits strict
opening of `K` interior sites but has not supplied the `K+1` sites
needed to restore that pin when the old interior population is `K`.
The new theorem pays exactly one deficient population, not a
general one-site surplus.

A valid fused step still needs actual wall extraction with the
stated tolerance and a population deficit, or an independently
proved aggregate residual capture/overlap theorem. The finite chart
port exclusions above do not supply either. No canonical state is
changed by this comparison.

## 16. Restoring the deleted pin inside the wall has a uniform local gap

Classification: **regression**, proved here analytically, awaiting independent
audit; not promoted. This is a finite pinned model, not a global minimizer.

Let `m,n>=3`, `L=m+n`, `u=(1,0)`, `v=(c,a)` with
`pi/3<=phi<=pi/2`, `c=cos(phi)`, `a=sin(phi)`. Start from the
full grid `p_ij=i u+jv`. Keep every boundary label except `p_(1,0)`
fixed. Allow all interior labels **and** `p_(1,0)` to move, requiring
that their final positions remain in the closed reference parallelogram
and that every pair is at least one apart. Write their displacements
as `xi_ij` and put `rho=max|xi_ij|`, including the restored pin.
Then

\[
 \boxed{\rho=0\quad\hbox{or}\quad
        \rho\ge {a\over2(L+1)}
        \ge{\sqrt3\over4(L+1)}.} \tag{16.1}
\]

In particular every continuous feasible path from this full reference
grid, confined to the old parallelogram and retaining the other pins,
is constant. This gap is uniform in the obliquity; deleting the label
and leaving it absent, as in Audit.187, is a different problem.

**Proof.** Each old unit edge in direction `e=u` or `v` gives

\[
 e\cdot(\xi_b-\xi_a)\ge-\tfrac12|\xi_b-\xi_a|^2
                                  \ge-2\rho^2.
\]

Every horizontal interior row has both endpoints fixed. Summing from
each endpoint gives `|u dot xi_ij|<=2m rho^2`. For the restored
bottom pin, the two fixed neighbors `p_(0,0),p_(2,0)` give the
stronger direct bound `|u dot xi_(1,0)|<=rho^2/2`.

The restored pin lies in the closed parallelogram, so its vertical
coordinate displacement is nonnegative. Since `0<=c<=1/2`,

\[
 v\cdot\xi_{1,0}
   =c(u\cdot\xi_{1,0})+a(\xi_{1,0})_y
   \ge-\rho^2/4.
\]

For column one, summing the unit-edge inequalities upward from this
pin and downward from its fixed top endpoint gives

\[
 -(2n+1)\rho^2\le v\cdot\xi_{1,j}\le2n\rho^2.
\]

Every other interior column has both endpoints fixed and obeys the
same weaker bound. Thus every movable label satisfies
`|u dot xi|<=2m rho^2` and `|v dot xi|<=(2n+1)rho^2`.
The dual vectors to `u,v` have norm `1/a`, so

\[
 \rho\le{2m+2n+1\over a}\rho^2
       \le{2(L+1)\over a}\rho^2.
\]

This proves (16.1). Continuity cannot cross the open displacement
gap. Extra triangular unit constraints at `phi=pi/3` only strengthen
the hypothesis; they were not needed. QED.

### 16.2 An exact near-triangular one-pin capacity plateau

For each fixed `m,n>=3`, there is a nonexplicit `epsilon_(m,n)>0`
such that, for `pi/3<phi<pi/3+epsilon_(m,n)`, deleting boundary
pin `p_(1,0)` leaves exactly `K=(m-1)(n-1)` available sites in
the **open** reference parallelogram, with unit separation from
all retained boundary pins. This is true for weak unit separation;
Audit.187 also supplies `K` sites with strict separation from all
retained labels, so the corresponding strict capacity is exactly
`K` as well. No extra interior site is gained by that deletion.

The literature input was rechecked in the original
[Böröczky--Ruzsa manuscript, page 2](https://www.renyi.hu/~carlos/wegner.pdf).
Its Groemer equality statement uses center separation two; dividing
coordinates by two gives the present normalization: equality in
`N<=area/(sqrt3/2)+perimeter/2+1`, for a two-dimensional hull,
requires a triangulation by unit equilateral triangles using all
source points. The segment case is separate and is inapplicable
to this fixed parallelogram. This source is used only for that
equality classification, not for diameter optimality.

**Proof of the plateau.** If the claim failed, choose angles
`phi_k->pi/3` with `K+1` unit-separated interior targets clear of
all retained wall pins. The `2(m+n)-1` retained pins and these
targets form `N=(m+1)(n+1)` distinct source points. The closed
parallelograms are uniformly bounded, so pass to a limit. Unit
separation keeps all labels distinct. The four fixed corner pins
make the limiting hull the full triangular-lattice parallelogram
of area `mn(sqrt3/2)` and perimeter `2(m+n)`. Its `N` points
attain Groemer equality.

The resulting unit-triangle tiling puts all points on one unit
triangular lattice. Retained unit boundary segments in directions
`u,v`, and the retained corner at the origin, fix its orientation
and phase. There are exactly `N` lattice sites in that parallelogram,
namely the original full grid; hence the limiting point set is
exactly that grid. Match the `K+1` targets to its unfixed labels:
the original `K` interior sites and `p_(1,0)`.

Their maximum displacement from the corresponding oblique reference
grid tends to zero as `phi_k->pi/3`. All retained pins are exactly
the reference pins, and all target positions lie in the closed
reference parallelogram. Equation (16.1), whose gap is uniform in
the angle, forces every matched target to be exactly its original
reference site for sufficiently large `k`. This includes `p_(1,0)`
on the boundary, contradicting that all targets were in the open
parallelogram. Therefore `K+1` interior sites are impossible near
the triangular endpoint. The old `K` interior grid sites give the
weak lower bound, and Audit.187 gives the strict lower bound. QED.

This plateau is for fixed `m,n`; it supplies no joint rate for
growing frames. It does not exclude distant configurations at
other oblique angles, changed walls, or sites outside the wall.

The lemma excludes a local restoration **inside** the old wall after
the Audit.187 packet. It does not exclude a distant alternative,
a restored point outside the wall, a changed wall, or a paid deletion
elsewhere. Any such endpoint still needs the full-source lower and
diameter checks. No source-compatible restoration is inferred.

## 17. Mean diameter-midpoint geometry from support-function energy

Sections 11--12 used a worst-case `O(D^(2/3))` midpoint radius. The
same full-source support-function energy also bounds the *mean* midpoint
displacement. This statement is independent of a KKT weight floor and
does not assume a lattice chart.

### 17.1 A weak second-moment bound for any chosen diameter partners

Let `B` be every actual diameter endpoint in a noncollinear global
minimizer, with circumcenter `o`. For each `p in B` choose any one
actual partner `p'`, independently, and set `m_p=(p+p')/2`.
There is an absolute constant `C` such that, for sufficiently large
`D` and all `s>=4*3^(1/4)*sqrt(D)`,

\[
 \boxed{|\{p\in B:|m_p-o|\ge s\}|\le C D^2/s^2.} \tag{17.1}
\]

The constant is uniform over every partner selection. Consequently

\[
 \boxed{\sum_{p\in B}|m_p-o|=O(D^{3/2}),\qquad
 \sum_{p\in B}|m_p-o|^2=O(D^2\log D).} \tag{17.2}
\]

**Proof.** Translate `o` to zero and use the full-source support function
`h` from Section 11. It satisfies
`E=int(h')^2<=C_E D`, `h''>=-D`, and `|h'|<=6D^(2/3)`.
At the strict diameter supporting normal `n_p`, differentiation is
valid and

\[
 m_p\cdot Jn_p=h'(n_p),\qquad |m_p\cdot n_p|\le\eta,
 \quad\eta=3^{1/4}\sqrt D. \tag{17.3}
\]

Fix `a>=eta` and count first those chosen endpoints for which
`a<=h'(n_p)<2a`. Consider just the components of the open positive
superlevel set `h'>a/2` that contain such a chosen normal. One-sided
derivative values at the finitely many face normals do not affect its
length or energy; the chosen strict diameter normals are not face
normals. Their total angular length is at most `4E/a^2`.

Each such component contains a value at least `a`. Going forward from
that value, the inequality `h''>=-D` keeps `h'` at least `a/2`
for length `a/(2D)`, before that component can end. The component
therefore consumes at least `a^3/(8D)` of the energy. Its number
is at most `8DE/a^3`. The circular support derivative has mean zero,
so no positive superlevel component occupies the whole circle.
Upward derivative jumps only strengthen the forward ramp inequality.

Subdivide those components into windows of fixed maximum angular width,
say `1/2`. For the *counted band*, (17.3) gives
`|m_p|<=sqrt(4a^2+eta^2)<=3a`. The normal-window estimate (8.2)
applies to this selected subset with that local midpoint bound,
irrespective of uncounted endpoints in the same window. Summing the
windows bounds its population by

\[
 C\{D E/a^2+(a+1)(DE/a^3+E/a^2)\}
 \le C' D^2/a^2. \tag{17.4}
\]

Here `a<=6D^(2/3)<=D` for sufficiently large `D`; above that range
there are no counted endpoints. For the negative band use
`h'<-a/2`, running the semiconvex ramp backwards. The same bound
holds. Sum dyadic bands starting at any `a>=eta` to obtain
`#{|h'(n_p)|>=a}<=C D^2/a^2`.

If `|m_p|>=s>=4eta`, then (17.3) forces
`|h'(n_p)|>=s/2>=eta`, proving (17.1). Every endpoint is a
strict full-hull extreme point, so `|B|<=per(K)<=pi D`.
Integrating the counting function below `4eta` with this population
bound, and above it with (17.1), gives the first estimate in (17.2).
Integrating `2s` times the same counting function, up to the worst-case
radius `7D^(2/3)`, gives the second estimate. QED.

This is a bound on unweighted actual source geometry. No assertion
about `sum beta_e |m_e|`, selected stress concentration, or the
largest diameter error of a proposed move follows from it.

### 17.2 Every actual diameter edge, with endpoint injection retained

For a canonical C-II source the full actual diameter graph is the
Woodall graph in the current ledger. It is a pseudoforest: either
one odd cycle with pendant leaves, or caterpillar components.
Assign each tree edge to its child after choosing a root; assign
cycle edges cyclically to their head, and pendant edges to their leaf.
Every actual diameter edge is assigned a distinct endpoint.

Apply (17.1)--(17.2) with each assigned endpoint choosing its assigned
edge as partner, extending the choice arbitrarily to other endpoints.
Thus, for the actual edge midpoints `m_e`,

\[
 \#\{e\in H:|m_e-o|\ge s\}\le C D^2/s^2,
 \quad \sum_{e\in H}|m_e-o|=O(D^{3/2}),
 \quad \sum_{e\in H}|m_e-o|^2=O(D^2\log D). \tag{17.5}
\]

In particular, for every `omega(D)->infinity`, all but
`O(D/omega(D)^2)` actual diameter edges have midpoint displacement
at most `omega(D)*sqrt(D)`. Their endpoints and all source labels
remain present. This is not a stress-mass assertion.

One can recover `sum deg_H^2=O(D^(3/2))` geometrically: the
midpoints in each star are pairwise at least `1/2` apart on a
radius-`D/2` circle. Inside the common `o(D)` midpoint ball, any
radius-`r` subball about `o` catches at most `C(r+1)` of them.
Summing the ordered radii gives a star cost at least
`c deg_H(p)^2-C deg_H(p)`. Summing over all vertices charges each
edge midpoint twice in (17.5). With `h>=D`, a maximum matching's
endpoint cover and Cauchy--Schwarz again give a square-root matching.
That matching conclusion is **already canonical** from Audit.126;
it is not a new frontier claim. The mean midpoint estimates are the
additional geometric information.

### 17.3 The uniform midpoint estimate extends to almost-diameter pairs

For any source pair `p,x` with `d=|p-x|>=D-s`, put
`nu=(p-x)/d`. Its support deficits in directions `nu,-nu` are
nonnegative and sum to at most `s`, since
`h(nu)+h(-nu)<=D`. Each is consequently at most `s`.
Set `epsilon=D^(-1/3)`, and write `p_n=p dot nu`,
`p_t=p dot Jnu`. For sufficiently large `D`,

\[
 p_n\cos\epsilon+p_t\sin\epsilon\le h(nu+\epsilon),
 \quad |h(nu+\epsilon)-h(nu)|\le6D^{2/3}\epsilon.
\]

Using `p_n>=h(nu)-s`, `h<=D`, and
`sin(epsilon)>=epsilon/2` gives

\[
 |p_t|\le13D^{2/3}+2sD^{1/3}. \tag{17.6}
\]

The lower bound uses `nu-epsilon` in the same way; the partner
obeys the same estimate with the opposite normal. The midpoint's
normal component has magnitude at most `2eta+s/2`. Hence every
pair whose diameter deficit is bounded by a fixed constant has
midpoint displacement `O_s(D^(2/3))`, without being an actual
diameter edge or carrying a KKT multiplier. The estimate does not
bound how many such almost-diameter pairs there are.

For a positive-contact loaded leaf this also sharpens the anchor
proximity in Section 10 of the local capacity report. All actual
diameter normals at the leaf, and all normals of pairs of length
at least `D-2`, lie within `O(D^(-1/3))` of its radial direction
by (17.6), the radial support lower bound, and `d>=D-2`.
The contact direction is a normalized positive combination of its
actual diameter normals. Its scalar product with every such
almost-diameter normal is therefore `1-O(D^(-2/3))`.
The same squared-distance and supporting-line argument in that
report gives

\[
 \operatorname{dist}(a,\partial\!\bigcap_{x\in A}
                \overline B(x,D-1))=O(D^{-2/3}). \tag{17.7}
\]

The counting exponents there are controlled by local chart error,
so this improved anchor proximity does not change those exponents.
It supplies neither a packet slot nor a source-compatible motion.

## 18. Oler sharpens the unloaded separator population budget

This section is a **proved candidate awaiting independent audit/promotion**,
against refreshed commit `a071f97896ccd02aeb4f648fab6ee2e8b60292aa`,
state `2026-10-09.audit.184`. It uses canonical Audit.180's
pinned-rank/exterior-walk reconstruction and the canonical Oler
inequality. It does not change the canonical separator theorem.

Let S be an endpoint-inclusive contact separator from a terminal set
X to the loaded set B, with `k=|S|`. Let U be the union of the
components of `C-S` meeting `X-S`. With the notation of Audit.180,
let `c_U,c_K,e_S,Q_K` denote the component counts of `C[U]` and
`K=C[U union S]`, the internal S contacts, and the componentwise
bounded-face degree defect. Set

\[
 b_*:=4k-2c_U-4c_K-2e_S-Q_K.
\]

The canonical pinned-rank proof gives `0<=b_K<=b_*`, where
`b_K` is the sum of the exterior walk lengths of the connected
components of K, each considered separately. Every K component
contains a separator vertex, hence `c_K<=k`. For each such
component, its convex-hull perimeter `p_j` is at most its exterior
walk length `b_j`. Oler and isoperimetry give, with
`a0=sqrt(3)/2`,

\[
 |V(K_j)|\le {\operatorname{area}(\operatorname{conv}V(K_j))\over a_0}
                 +{p_j\over2}+1
       \le {p_j^2\over4\pi a_0}+{p_j\over2}+1.
\]

This also covers point and segment hulls by the degenerate Oler
inequality. Sum over components, use
`sum p_j^2<=(sum p_j)^2`, and subtract the k separator vertices.
The resulting exact candidate is

\[
 \boxed{|U|\le {b_*^2\over4\pi a_0}+{b_*\over2}+c_K-k.} \tag{18.1}
\]

The simpler uniform consequence is

\[
 \boxed{|U|\le {8\over\pi\sqrt3}k^2+2k.} \tag{18.2}
\]

It improves Audit.180's coefficients `16/pi^2` and `8/pi`
to `8/(pi sqrt(3))` and two. Formula (18.1) also retains the
actual component, separator-contact, and face-defect debits rather
than discarding them. No contact-isolated source point is counted
in U or removed from the full configuration.

For a bank of a distinct complete physical trains of degree at
least L, the canonical rail multiplicity at most five therefore gives

\[
 \boxed{(a-5k)_+(L+1)\le {40\over\pi\sqrt3}k^2+10k.} \tag{18.3}
\]

In Audit.180's positive-bulk notation, put
`a_*=(2/3)sqrt(r-epsilon)`, `ell=epsilon/(3pi)`, and
`beta=40/(pi sqrt(3))`. Its argument now yields the candidate

\[
 \boxed{\liminf{k\over D}\ge
 {\sqrt{25\ell^2+4\beta a_*\ell}-5\ell\over2\beta}>0.} \tag{18.4}
\]

Indeed any limiting `x<a_*/5` must satisfy
`ell(a_*-5x)<=beta x^2`; its nonnegative root is (18.4).
When `x>=a_*/5`, the same bound follows because that root is
strictly smaller than `a_*/5`. Menger still gives endpoint-inclusive
paths, potentially of length zero when a chosen train terminal is
loaded. The sharpened constant does not create a positive path-length
bound or restrict these paths to the smaller Audit.179 carrier.

The implication is a stronger necessary cut/return budget. Even with
Audit.189's deep crop, the returned source population can fit in
the ordinary packing allowance of the macroscopic boundary strip.
No payment against exceptional faces or source-compatible exchange
is proved by (18.1)--(18.4).

LEVEL I STATUS: STILL OPEN.
