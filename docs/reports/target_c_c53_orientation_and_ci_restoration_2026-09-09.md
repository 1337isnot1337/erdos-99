<!-- theorem-state: {"artifact_id":"ART-919E969AC4EA","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — projective-orientation audit and restoration of the C-I proof

**Date:** 2026-09-09
**Base:** `c26d6ab20f6e8e48ff548a20f0e84ac0d904bbe5`
**Run type:** dependency audit, exact correction, and continuation
**LEVEL I STATUS: STILL OPEN.**

This report corrects a consequential error in the September 5 pentagon regression,
including this agent's subsequent acceptance of it in the September 8 audit.
The purported counterexample uses incompatible projective ordering and orientation.
The general C53 sign lemma survives a complete finite-type reduction, not merely
the correction of that one example. Combining it with the circular-planar resistance
theorem restores universal selected-stress PSD and the C63 finite-release proof.

**Mathematical conclusion:** C-I is closed under the canonical source definitions.
This is an audited restoration of existing C53/C63 mathematics, not a claim to have
newly invented those results. C-II, including interior isolated points, remains open.
No infinite globally optimal triangle-free family or Level I proof is supplied.

## 1. The exact failed regression

For a regular pentagon p_j=(cos(2pi*j/5),sin(2pi*j/5)), write
e=03, f=13, g=02. Their line directions, reduced modulo pi to [0,pi), are
respectively 18,54,162 degrees.

For this cut, orient into the **upper** half-plane. The oriented edges are
30,31,02. On the interval {0}, using head-minus-tail signs, their signs are
(1,0,-1), not (1,0,1). Both C53 inequalities hold.

Alternatively orient into the **right** half-plane. The directions are then
-18,18,54 degrees in the order g,e,f, with oriented edges 20,30,31 and signs
(1,1,0). Again both inequalities hold.

The rejected script used the first order e,f,g and the second orientation
30,31,20. In that mixed convention the slopes are tan(18),tan(54),tan(-18),
which are not increasing. Thus it violates the very normalization used by C52.R.
Reversing every sign, as the old script does, does not repair the inconsistent cut.

Equal chord lengths and the exact pentagon coordinates do not remedy this error.
The previously reported product +1 is real arithmetic on inadmissible input, not
a counterexample to C53.T or universal PSD.

## 2. Complete geometric reduction for the chord-sign lemma

Let three distinct pairwise-intersecting chords join vertices of a strictly convex
polygon. Shared endpoints are allowed. Choose a line-direction cut avoiding all
three chords, orient each chord into the same open half-plane defined by that cut,
and order those oriented directions through that half-plane. For a circular vertex
interval A let z_h=1_A(head h)-1_A(tail h).

**Lemma.** For the ordered chords e<f<g,

\[
z_g(z_e-z_f)\le0,\qquad z_e(z_g-z_f)\le0.                 \tag{1}
\]

### Why finitely many endpoint models suffice

There are at most six distinct endpoints. Delete the other polygon vertices;
the endpoints remain in strict convex position, and a circular interval restricts
to a circular interval on them. Thus it suffices to treat n=3,4,5,6 endpoints.

The space of strictly convex labeled n-gons in one cyclic orientation is connected.
Here is an explicit justification, needed to make the finite check universal.
Translate an interior point to the origin and write p_i=r_i u_i in angular order.
The angular gaps delta_i lie in (0,pi). The strict left-turn condition at p_i,
divided by r_(i-1) r_i r_(i+1), is

\[
\frac{\sin\delta_{i-1}}{r_{i+1}}
+\frac{\sin\delta_i}{r_{i-1}}
-\frac{\sin(\delta_{i-1}+\delta_i)}{r_i}>0.             \tag{2}
\]

This is linear in the reciprocal radii. Interpolating them to a common positive
constant preserves (2), because the terminal circular polygon is strictly convex.
The polygon remains simple: its edges stay in consecutive disjoint angular wedges.
Strict turns and simplicity therefore preserve strict convexity. On the circle,
interpolate the angular gaps to 2pi/n, preserving positivity and the sum 2pi.
This connects the polygon to a regular polygon. In particular it connects any two
strictly convex realizations with the same cyclic vertex order.

Throughout such a deformation two distinct chords in our triple cannot become
parallel: disjoint chords continue to cross, and shared-endpoint chords would
require three collinear convex vertices. Their projective cyclic order consequently
cannot change. Moving the cut past a chord rotates the order and reverses that
chord's orientation. These are exactly the cut operations in the finite check.
The remaining choice of opposite half-plane reverses all three signs; (1) is
unchanged by that operation.

### Exhaustive finite certificate

Use p_i=(i,i^2), i=0,...,n-1, as a strictly convex representative. A forward
chord ij has slope i+j. Among pairwise-intersecting chords these slopes are distinct.
Enumerate all triples of edges, retain exactly those whose pairs share an endpoint
or have alternating endpoints, sort by i+j, test all three cyclic cuts with the
wrapped orientations reversed, and test every circular interval.

The exact integer enumeration `chord_types()` in
`research/near_diameter_path_audit.py` performs these operations. It has 27,252
cases and produces precisely

```text
(-1,-1,-1) (-1,-1,0) (-1,-1,1) (-1,0,0) (-1,0,1) (-1,1,1)
(0,-1,-1) (0,-1,0) (0,0,-1) (0,0,0) (0,0,1) (0,1,0) (0,1,1)
(1,-1,-1) (1,0,-1) (1,0,0) (1,1,-1) (1,1,0) (1,1,1).
```

Direct substitution verifies (1) for every listed triple. The set is closed under
global sign reversal. The deformation and endpoint-restriction arguments above
prove that this finite certificate covers every allowed geometric input. There is
no floating-point or generic-position inference beyond the stated strict convexity.

## 3. Weighted Robinson lemma, independently checked

Let L be symmetric, have zero row sums, and satisfy
`L_ij=-gamma_i gamma_j s_ij` off the diagonal, with gamma_i>0. Assume
`s_ik<=min(s_ij,s_jk)` whenever i<j<k, and Lt=0 for a strictly increasing vector t.
Then L is positive semidefinite.

To prove this, put Gamma=diag(gamma), A=Gamma^{-1}L. Let D_f take consecutive
first differences and let T take cumulative sums, so D_f T=I. Put H=D_f A T.
For an off-diagonal entry H_ir with r>i, its formula is a sum over j>r of
`gamma_j(s_ij-s_(i+1,j))`, hence is nonpositive. For r<i, use the zero row sums
to express it as a sum over j<=r of
`gamma_j(s_(i+1,j)-s_ij)`, also nonpositive.

Moreover H(D_f t)=0 and D_f t is strictly positive. Diagonal conjugation by
diag(D_f t) makes H a matrix with zero row sums and nonpositive off-diagonal
entries. Its Gershgorin disks lie in the closed right half-plane. Its spectrum is
the spectrum of A on the quotient by constants. A is similar to the symmetric
matrix Gamma^{-1/2} L Gamma^{-1/2}, so its eigenvalues are real. They are therefore
nonnegative, including the constant eigenvalue zero. Congruence now proves L>=0.

No strict separation between eigenvalues, lower bound on gamma, or generic rank
assumption is used.

## 4. Universal selected-stress PSD

Fix any normalized source KKT stress (alpha,beta), retaining only its positive
edges. The canonical support-connectivity theorem gives one connected positive
contact network; all other source vertices have zero stress rows. Its loaded set
B consists of endpoints of positive diameter edges. Such endpoints are strict
source convex-hull vertices: a strict convex combination of other source points
cannot be distance D from a source point, by the squared-norm identity.

The unit-contact drawing is planar. The network and its loaded terminals thus
have the circular-planar embedding in their actual convex-hull order. Let Lambda
be its positive-Laplacian Dirichlet response and R=Lambda^+. Let Q be oriented
diameter incidence, Beta=diag(beta), P centered terminal coordinates, and

\[
L_H=Q\mathrm{Beta}Q^T,\quad U=Q^TP,\quad K=Q^TRQ.
\]

Equilibrium and harmonic elimination give

\[
\Lambda P=L_HP,\qquad K\mathrm{Beta}U=U.                \tag{3}
\]

For a connected circular-planar positive network, its effective-resistance metric
has a nonnegative circular-interval split representation. This is exactly Forcey's
Theorems 4.2 and 3.7, [arXiv:2108.00550](https://arxiv.org/pdf/2108.00550).
We use only this forward implication, not a converse electrical realization.
The paper's opposite Laplacian sign does not change effective resistances.

If W is that metric, `K=-Q^T W Q/2`. An interval cut metric contributes
`z_A z_A^T`, where z_A=Q^T 1_A. By (1), K is a Robinson similarity in the
consistently cut and oriented projective order of the diameter chords. Diameter
chords are pairwise intersecting, so the lemma applies to every triple.

Choose a covector ell positive on the finitely many oriented diameter vectors,
and an independent coordinate m such that
`a_e=ell(U_e)>0`, `t_e=m(U_e)/a_e` are strictly increasing. Set E=diag(a_e).
In these coordinates U=E[1,t]. Put

\[
N=\mathrm{Beta}-\mathrm{Beta}K\mathrm{Beta},\qquad M=ENE.
\]

Equation (3) gives M1=Mt=0. Its off-diagonal entries are
`-gamma_e gamma_f K_ef`, with gamma_e=a_e beta_e>0. Section 3 proves M>=0.
Undoing the invertible congruences gives

\[
\mathrm{Beta}^{-1}-Q^T\Lambda^+Q\succeq0.              \tag{4}
\]

On 1-perpendicular, put B_0=Lambda^{-1/2} Q Beta^{1/2}. Equation (4) says
`B_0^T B_0<=I`, hence `B_0 B_0^T<=I`. Congruence yields

\[
\Lambda-L_H\succeq0.
\]

The full contact Dirichlet block is positive definite; the Schur complement of
`Omega=L_C(alpha)-L_H(beta)` is exactly Lambda-L_H. Thus Omega is PSD.
This argument assumes the loaded coordinates span two dimensions.

If they span one dimension, there are exactly two loaded vertices and one
diameter edge. Project equilibrium perpendicular to that line: the connected
positive contact Laplacian forces every contact vertex onto the line. Unit
separation makes the network a straight unit chain of D edges, each of weight D,
with diameter weight one. Its quadratic form is

\[
D\sum_{j=0}^{D-1}(f_{j+1}-f_j)^2-(f_D-f_0)^2\ge0
\]

by Cauchy–Schwarz. This is a selected-support calculation, not a reopening of
the canonically excluded one-dimensional *maximal* force hull.

Consequently **every** normalized KKT stress has Omega>=0 on **every** scalar
field, and its two-coordinate energy is nonnegative on every displacement.
Zero rows at contact-isolated vertices are retained. No global force-bulk estimate,
minimal positive stress, matching restriction, or selected-velocity restriction is
used.

## 5. Finite integration and C-I

For all strong active rows write the exact fixed-diameter constraints as
`g_*(x)=A_*x+Q_*(x)>=0`: contact quadratic terms are +|x_i-x_j|^2, diameter
terms are -|x_i-x_j|^2. Canonical C6 supplies a velocity v with A_*v=0 and
strict signed first variation on every weak active row.

Every nonzero nonnegative lambda with lambda^T A_*=0 has positive diameter
mass. Otherwise the virial identity would give a nonnegative pure contact
stress with sum(alpha)=0. Dividing by that positive mass makes lambda an actual
normalized KKT stress. Section 4 therefore proves

\[
\lambda^TQ_*(x)\ge0\quad\hbox{for every displacement }x. \tag{5}
\]

Farkas duality now makes `A_*y>=-g_*(x)` feasible for every x. For this fixed
matrix, Hoffman's error bound provides H<infinity and a feasible correction with
`|y|<=H |[g_*(x)]_-|`. The bound is uniform over feasible right-hand sides, not
over source configurations; see Peña–Vera–Zuluaga, Proposition 1,
[arXiv:1905.02894](https://arxiv.org/pdf/1905.02894).

Let epsilon(x)=|[g_*(x)]_-|. Since the quadratic map is fixed, some L satisfies

\[
\epsilon(x+y)\le L(H|x|\epsilon(x)+H^2\epsilon(x)^2).   \tag{6}
\]

Start at x_0=tv, whose error is O(t^2). Choose t so small that the right side
of (6) is at most epsilon(x)/2 whenever |x|<=2C_0t and epsilon(x)<=C_1t^2,
where |tv|<=C_0t and epsilon(x_0)<=C_1t^2. Successive corrections have total
norm at most 2HC_1t^2, which is <=C_0t after a further reduction of t. This
closes the induction. The iterates converge to x(t)=tv+O(t^2), and continuity
gives every strong inequality exactly. Each weak row has positive linear slack
of order t, which dominates the O(t^2) correction. Every initially inactive
pair retains its strict slack by finiteness and continuity.

Thus the resulting n points are unit-separated, have diameter <=D, have no new
unit contacts or diameter pairs, and lose every weak active pair. Global
optimality gives diameter exactly D. If a contact-minimal triangle-free global
source had a weak unit contact, the resulting configuration would have fewer
contacts and still be triangle-free. Contradiction. Therefore C=C_*: **C-I closes**.

This does not merely produce a formal second-order jet. The actual convergent
correction is why the quadratic regression in the September 8 report is irrelevant
to this conclusion: that regression fails (5) on transverse displacement fields.

## 6. Immediate continuation into C-II

Choose, among the contact-minimal triangle-free global minimizers, one minimizing
the number of diameter pairs. These minima exist as minima of nonempty sets of
nonnegative integer counts; no compactness assertion for the triangle-free subset
is needed. The same release argument excludes weak diameter pairs: if contacts
also opened it would violate the first minimum, and otherwise it violates the
second. Hence this representative satisfies

\[
C=C_*,\qquad H=H_*.
\]

Every mixed critical velocity consequently has zero first variation on all actual
active constraints. The construction in Section 5 integrates it at fixed diameter.
Lexicographic minimality forces all active lengths to remain exactly their old
values at the resulting nearby points. This restores the C65 setting for a genuine
hypothetical global survivor, with contact-isolated source points still present.

It does **not** prove that the critical cone consists only of rigid motions, that
the contact graph is a pure rhombic disk, that one diameter weight approaches one,
or that positive conductances have a numerical lower bound. Those are separate
C-II questions. The diameter-lens result applies immediately in the conditional
dominant-diameter branch; the local degree-three/degree-five regressions still
prevent its conversion into a C97 strip by local reasoning alone.

## 7. Branch ledger and adversarial disposition

### New consequence: a common-stress-kernel local normal form

Let p be the lexicographically normalized source from Section 6. Let S be its
normalized KKT polytope, choose a relative-interior stress s_bar (positive on every
actual active pair), and set Z=ker(Omega_(s_bar)) on all n source vertices.
Contact-isolated vertices contribute their full independent scalar coordinates.
Then

\[
Z=\bigcap_{s\in S}\ker\Omega_s,\qquad
\ker A\subseteq Z\otimes\mathbb R^2.                   \tag{7}
\]

Moreover every sufficiently nearby unit-separated configuration of diameter at
most D differs from p by an element of `Z tensor R^2` and preserves every active
unit and diameter length exactly. This is a simultaneous statement for **all**
normalized stresses, stronger than selecting one extreme stress for one velocity.

**Proof.** For any s in S, relative interior permits
`s_bar=t s+(1-t)s'` with 0<t<1 and s' in S. Since all stress matrices are PSD,
zero energy for s_bar forces zero energy for s. This proves the kernel identity.

Take any sufficiently small feasible displacement x. Inactive pairs stay strict;
global and lexicographic minimality force every active signed constraint g_e(x)
to be zero, just as in Section 6. For any s, equilibrium gives

\[
0=\sum_e\lambda_e g_e(x)
=x_x^T\Omega_s x_x+x_y^T\Omega_s x_y.
\]

Each summand is nonnegative. Thus both coordinate displacements lie in every
ker(Omega_s), proving the finite local statement. Finally every v in ker A is
critical, because all active rows are strong. Section 5 integrates it as
`x(t)=tv+O(t^2)`. Divide the finite kernel inclusion by t and take t to zero;
the kernel is a closed linear space. This proves (7). Square.

This is a new consequence extracted here from the restored C53/C63 and exact
lexicographic normalization, not a claim that generic PSD face selection has
maximal support. The generic exposed-face regressions lack this finite optimality
argument. A useful exact remaining rank consequence would be a contradiction
between the mixed rigidity kernel and (7) for all sufficiently large triangle-free
sources. No such rank contradiction is established here: the regular-shell
examples and their freely moving isolated interiors remain compatible with (7).

| Branch / exact hypotheses | Target invariant | Disposition | Binding check / next exact theorem |
| --- | --- | --- | --- |
| C53 circular-planar response, affine equilibrium, diameter thrackle | Omega_s>=0 for every normalized stress | **Closed by proof**, Sections 2–4 | Must use one consistent projective cut and orientation |
| September 5 pentagon alleged counterexample | C53.T sign failure | **Rejected by exact normalization audit** | Its ell-slopes are not increasing in its chosen order |
| C-I weak contact in contact-minimal global source | Finite same-D release | **Closed by contradiction**, Section 5 | All-displacement PSD makes every correction Farkas-feasible |
| Weak diameter in lexicographically minimal global source | Full actual diameter support | **Closed by contradiction**, Section 6 | Contacts and diameters are minimized in that order |
| Full actual support and lexicographic global minimality | Common stress kernel | **Reduced to sharper theorem:** (7) and the finite local inclusion | Still need a rigidity-kernel or global-capacity contradiction; isolates remain free coordinates |
| C-II with full actual support, arbitrary isolates/topology | Exclusion of sufficiently large source | **Reduced**, not closed | Must exclude this entire normal form or construct a strict competitor |
| C-II dominant-diameter near-chain, when C98–C102 hypotheses hold | Uniform exclusion of b->1 | **Reduced**, not closed | All internal path vertices are unloaded, but local stress/area does not force degree four |
| C-II force-bulk localization | Interior isolate count z_int | **False stronger claim remains rejected** | Exact globally optimal heptagon-plus-center regression is unaffected |
| Generic planar conductance floors / strict minors | Uniform positive response gap | **Not proved** | Near-star vanishing-conductance regressions remain binding |
| A and B global population/shell routes; infinite optimal disproof families | Original global quantifiers | **Unchanged** | Previous ledger endpoints still unproved |

The single remaining sufficient C-route theorem is now: there is n_0 such that
no contact/diameter-lexicographically minimal triangle-free global minimizer on
n>=n_0 points has C=C_* and H=H_*, **allowing contact-isolated points**.
This is the full C-II gate, not a claim that its subbranches have been exhausted.

## 8. Computation, literature, and repository changes

The 27,252 exact chord checks are a finite proof certificate because Section 2
proves the reduction to their exhaustive domain. The pentagon orientation check
is exact in angle order; no approximate angle test is needed for its proof.

`research/planar_diameter_stress_probe.py` separately sampled 600 LP stresses
on regular odd-polygon planar networks. None had a negative eigenvalue beyond
roundoff (the smallest was about -2.6e-14). This was exploratory, omitted unit
contact lengths and global optimality, and is **not used in any proof**.

The electrical and Hoffman imports above match finite networks/fixed matrices.
Neither imports packing relocation or a crystallization rate. The Erdős problem
[status page](https://www.erdosproblems.com/99) still lists #99 as open; that status
is context, not a premise of these proofs.

Required canonical reconciliation is explicit: withdraw the September 5 C53
regression; annotate this agent's September 8 acceptance; index this audit and
restore C53/C63 and the C65 lexicographic reduction, without promoting all later
C-II claims automatically. Separately, withdraw the false force-bulk localization
using its already recorded exact regression. Preserve both failed arguments as
history with their exact errors marked.
