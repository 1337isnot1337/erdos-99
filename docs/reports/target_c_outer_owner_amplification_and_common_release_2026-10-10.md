<!-- theorem-state: {"artifact_id":"ART-125DECAFF3AF","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II — upper-safe amplification and common contact release

**Date:** 2026-10-10. **Worker:** Slot 01.\
**Starting main:** `ab6dd3336f9f8d440f2bada76edb32153391cddc`.\
**Theorem state:** `2026-10-10.audit.234`.\
**Branch:** `research/sol61-slot01-outer-motion-20261010`.\
**Classification:** proved candidates awaiting independent audit, conditional
finite endpoints, and exact regression repair. This report is unreviewed and
noncanonical. **C-II and Level I remain OPEN.** No external theorem is imported.

## 1. The endpoint and the new mechanism

This continues
`target_c_owner_component_anchoring_and_source_realized_sink_2026-10-10.md`.
That report constructs a connected nonglobal source whose actual binary owner
formula has only the zero model. Here the same source admits strict full-source
improvements without splitting its repeated owners: increasing one owner's
amplitude, or translating both owners by one common vector, releases contacts
and repairs all binary blockers.

For a canonical source, the analytic candidates certify larger upper-safe
move families, give a full-source common-release implication criterion, and
force weighted two-sided contact balance in prospective large independently
upper-safe families. None extracts the parent family or proves universal
nonzero feasibility.

The closure chains are:

```text
supplied exact O–O owners + actual normal-window bound
 -> upper-safe amplitude box after deleting proposals
 -> a strict lower-feasible amplitude endpoint
 -> contact loss, or old-diameter loss when amplitudes are binary.

supplied narrowly aligned exact O–O owners + actual normal-window bound
 -> upper-safe common translation that opens every cut contact
 -> implication-only lower system with a sink free of unary blockers
 -> same-cardinality contact loss at diameter at most D.
```

The last existence implications are conditional. Source labels are never
deleted when proposals are discarded.

## 2. Exact setup and canonical dependencies

Use the canonical triangle-free contact-minimal, then actual-diameter-pair-
minimal global source A with D>=9, connected positive-contact core V, full actual
diameter graph H, and d_H=|V(H)|-|H|. All source labels, including contact
isolates, remain. Put

\[
 L=\sqrt{D^2-1},\qquad \gamma=D-L.
\]

Supply disjoint nonempty proper core owners G_1,...,G_r, leaving a core label
fixed. Supply nonzero d_i=delta_i v_i with unit v_i in one oriented interval of
width w<pi/2 centered at v. Assume every old contact is exactly preserved under
every binary choice of these owners. This forces no old contact between
distinct owners: its four-state mixed squared-length difference is
`-2 d_i dot d_j`, which is strictly negative. Assume the parent family is an
actual subfamily-stable O–O system, so bounded nonquadrilateral faces are uncut
and bounded-face isolates have the compatible rigid face assignment. Other
isolates follow the fixed canonical long-pair anchor map, or remain fixed if
unanchored. Let

\[
 s=\operatorname{diam}\{0,d_1,\ldots,d_r\}.
\]

Each original parent singleton is assumed weakly upper-safe on every actual H
pair. This is a supplied geometric hypothesis, not inferred from stress gain.
Fix the canonical exceptional inactive-upper set E, |E|<=d_H. Discard owners
containing either a core endpoint or the anchor of an isolate endpoint of E.
At most 2d_H owners are discarded and every E endpoint then remains fixed.
Bounded-face isolates cannot be E endpoints, by the canonical face variance
bound. Discarded owners' points become fixed; no point is removed.

Canonical inputs are:

- `C-WOODALL`: every subgraph of actual H has at most as many edges as incident
  vertices (H is a forest or one odd-unicyclic graph with pendant leaves).
- `C-CII-ACTUAL-DIAMETER-NORMAL-ATOMLESS`, Audit.205: for any choices of actual
  partners, the number of loaded endpoints with selected oriented normal in
  a window of half-width theta<pi/2 is at most

  \[
  F_D(\theta)=1+{D\sin\theta+2L_D\over\cos\theta}.
  \]

- `C-FS-DIAMETER-MIDPOINT-D2-3`, Audit.206: one common center has all actual
  diameter midpoints within L_D=7D^(2/3). This is full-source geometry.
- `C-LONG-PAIR-ISOLATE-DISPATCH`: outside E, an inactive pair longer than L has
  identical endpoint displacements under the anchor assignment. There is no
  protected inactive core-core long pair.
- `C-OO-LOWER-BLOCKER-LOCALIZATION`: small actual O–O motions have lower
  blockers only at unary strict rhombi and actual outer-face near-unit pairs.

The multi-displacement upper argument only needs the long-pair structural
statement: protected long pairs have equal displacements and all other
inactive pairs have old length <=L. It is not an import of a binary theorem
with amplitudes silently substituted. The lower localization used below is
also proved directly from old near-unit cofaciality and rigid bounded-face
transport; contact preservation at the endpoint is not needed for it.

For completeness, the finite window inequality follows directly from the
midpoint bound. Write each selected endpoint as `p=m+(D/2)n` and project onto
the tangent to the window center. The projection span is at most
`D sin(theta)+2L_D`. Two successive endpoints in this window's convex boundary
order have their forward chord direction between the tangents of their
selected strict support normals. Its tangent projection is therefore at least
`cos(theta)` times its length, and thus at least cos(theta) by unit separation.
Adding consecutive projection gaps gives `(N-1)cos(theta)<=D sin(theta)+2L_D`.
The strict support property is full-source: for an actual partner p', every
other source point x satisfies
`((p-p')/D) dot (x-p)<=-|x-p|^2/(2D)<0`. These inequalities hold for any
partner choices, so the endpoint count used by AB and IM is uniform.

## 3. Candidate AB: a full upper-safe amplitude box

Fix M>1 with Ms<min(gamma,sqrt(2)-1), and put

\[
 \theta_M={w\over2}+\arcsin{Ms\over2D}<\pi/2.
\]

After discarding at most

\[
 2d_H+4\lfloor F_D(\theta_M)\rfloor                 \tag{AB.1}
\]

supplied owners, every full-source endpoint with amplitudes
`0<=x_i<=M` and displacement `x_i d_i` passes every upper bound. Old contact
lower bounds pass whenever each x_i belongs to `{0} union [1,M]`. A cut contact
of owner i has exact squared length

\[
 1+x_i(x_i-1)\delta_i^2.                           \tag{AB.2}
\]

Thus a strict lower-feasible endpoint in this domain is a contact-loss
contradiction if some x_i>1. If all nonzero amplitudes are one, the strict
weighted gain candidate SG in the preceding report supplies old-diameter
loss. That binary consequence is a dependency on another unreviewed candidate;
the contact-loss consequence for x_i>1 is independent of SG.

### Proof of the deletion bound

If an actual H pair can grow at amplified singleton i, orient its vector r
from the moving endpoint to the fixed endpoint. Original singleton safety and
amplified failure say

\[
 r\cdot v_i\le-\delta_i/2,
 \qquad r\cdot v_i>-M\delta_i/2.
\]

Since |r|=D and delta_i<=s, the projective direction of this pair is within
`arcsin(Ms/(2D))` of Jv_i, hence in the projective window centered at Jv with
half-width theta_M. Call the set of all such witness pairs W. At each endpoint
incident to W choose a partner along one of its W edges. Its oriented normal
is in one of two opposite theta_M windows. Audit.205, uniform in partner
choice, bounds their union by `2 floor(F_D(theta_M))`. Woodall gives
`|W|<=|V(W)|`; each pair touches at most two disjoint core owners. Deleting all
owners incident to W therefore costs at most `4 floor(F_D(theta_M))` owners.
These counts concern actual full-source H, not positive-stress H alone.

### Proof of the complete upper ledger

For an old H pair joining two distinct surviving owners, let g_i and g_j be
the singleton squared changes at amplitude M. Both are <=0, and the joint
change is

\[
 g_i+g_j-2M^2d_i\cdot d_j<0.
\]

Pairs internal to an owner are unchanged; one moving endpoint has the checked
singleton state. Thus every vertex of the amplitude cube `{0,M}^r` is safe for
every actual H pair. The squared length of each pair is a convex function of
the amplitude vector, being the squared norm of an affine vector. A point of
the cube is a convex combination of its vertices, so its squared length is
<=D^2 as well. This is a pairwise maximum-diameter proof.

The relative displacement in the entire amplitude box is at most Ms. Indeed
each endpoint displacement lies in the convex hull of `{0,Md_1,...,Md_r}`;
that hull has diameter Ms. Protected inactive long pairs have equal
displacements by the fixed dispatch and hence keep their old length. E pairs
are fixed. All other inactive pairs have length at most L and new length at
most `L+Ms<D`. This checks every previously inactive upper pair and every
isolate.

For an owner crossing contact, exact original preservation gives
`r dot d_i=-delta_i^2/2`; substitution proves (AB.2). Every other old contact
has equal endpoint displacements or stays fixed. If x_i>1, connectedness of V
and absence of contacts between owners supply a cut contact, which opens.
When every old noncontact stays strictly above one, the endpoint has a strict
subset of the old contact graph, is triangle-free, retains cardinality, and
has diameter <=D. If it has smaller diameter it contradicts globality; if its
diameter is D it contradicts contact minimality. QED.

### Scope

For fixed M, w=o(1), and s<gamma/M, (AB.1) is `2d_H+o(D)`; the finite bound is
explicit. This does not say enough parent owners exist after deletion or that
lower-feasible amplitudes can be chosen. In particular amplitudes in (0,1)
generally violate the old cut contacts and cannot be used as a continuous
interpolation from zero.

## 4. Candidate CT: a common translation removes incompatibilities

Suppose there is rho with

\[
 \delta_{\max}+4\sin(w/4)<\rho<\min\{\gamma,\sqrt2-1\}.
                                                               \tag{CT.1}
\]

Let b=rho v and

\[
 \theta_b=w/2+\arcsin(\rho/(2D))<\pi/2.
\]

Discard the E owners as above and every owner whose singleton translation by
b grows any actual H pair. At most

\[
 2d_H+4\lfloor F_D(\theta_b)\rfloor                 \tag{CT.2}
\]

parents are discarded. Then every binary common-b choice of the survivors:

1. passes every full-source upper bound;
2. strictly opens all its old cut contacts;
3. has an exact old-noncontact lower formula consisting only of implications
   and forced-zero unary clauses, with no pairwise incompatibility clause.

The formula has a nonzero model precisely when some sink strongly connected
component of its implication graph contains no forced-zero variable. Any such
model with strict old-noncontact lower slack is a full-source finite contact-
loss contradiction. Thus in a canonical survivor every sink must contain a
unary blocker. This is a conditional obstruction reduction, not a proof that
a unary-free sink exists.

### Actual-upper witnesses and all upper pairs

A singleton target failure has `r dot v>-rho/2`, while original safety gives
`r dot v_i<=-delta_i/2<0`. If `r dot v<=0`, its projective direction is within
`arcsin(rho/(2D))` of Jv. If `r dot v>0`, the sign change between v and v_i
puts it within w/2 of Jv. Either case lies in the stated theta_b window.
The partner-choice, pseudoforest, and two-endpoint count from AB proves
(CT.2).

All survivors' target singleton H states are safe. Two moving endpoints have
the same b, so their distance is unchanged. If a diameter joins different
surviving owners, their two opposite singleton changes would sum to
`2rho^2>0`, contradicting singleton safety; therefore no such pair remains.
The inactive-upper proof uses the cloud `{0,b}` of diameter rho, the same
fixed E ledger, and the same rigid/anchor isolate assignments. Every inactive
pair remains strictly shorter than D.

### Contacts and the exact lower formula

For a crossing unit vector r of owner i,

\[
 r\cdot v\ge r\cdot v_i-|v-v_i|
 \ge-\delta_i/2-2\sin(w/4).
\]

Consequently

\[
 |r+b|^2-1\ge\rho\bigl(\rho-\delta_i-4\sin(w/4)\bigr)>0. \tag{CT.3}
\]

No old contact joins distinct parents. Internal contacts move rigidly and all
fixed contacts stay unit. Each selected owner has an old contact to the fixed
core, by connectedness and properness, so every nonzero choice loses a contact.

Consider an old noncontact joining labels of two different surviving owners,
or their assigned isolates. Orient r from the second to the first and put
c=|r|^2-1>0. Its local squared lower slacks at choices 00,10,01,11 are

\[
 c,\quad c+2r\cdot b+\rho^2,\quad
 c-2r\cdot b+\rho^2,\quad c.                        \tag{CT.4}
\]

The two singleton slacks sum to `2c+2rho^2>0`, so at most one is <=0.
If 10 is bad the clause is i=>j; if 01 is bad it is j=>i. Choice 11 can never
be bad. A pair against a fixed label supplies a forced-zero unary clause if
its selected state is <=0. A pair internal to an owner is unchanged. Equality
is treated as bad so that feasible assignments create no new contact.

Only old pairs of length <=1+rho can be bad, by the triangle inequality.
Since 1+rho<sqrt(2), canonical old near-unit cofaciality applies. A bounded
nonquadrilateral face is uncut and its vertices and assigned isolates move
rigidly, giving no blocker. An old near-unit pair incident to a bounded-face
isolate is in that face and moves rigidly. The remaining bounded-face clauses
are the two diagonals of a cut strict rhombus, hence unary. All other clauses
come from actual outer-face near-unit pairs, including exterior isolates.
These arguments use the original face geometry; they do not assume the
contact-opening endpoint still has the old face decomposition.

Finally, a finite implication graph always has a sink SCC downstream of any
nonempty implication-closed set. If a nonzero feasible model exists, a sink
reachable from any selected variable is entirely selected and has no unary
forced-zero variable. Conversely selecting one sink SCC with no unary gives
a nonzero model. CT.3 and the strict treatment of equality prove the contact-
loss consequence with every source pair checked. QED.

### What CT changes, and what it does not

The binary acute model can have an implication cycle with an internal
incompatibility. The common translation proves that this particular form of
sink obstruction disappears. Every remaining failed sink must have a unary
geometric witness. This is an exact algebraic change of the lower formula,
supported by a full upper ledger. It neither bounds the number of unaries nor
limits how many owners one unary can reach by implications. Condition CT.1 is
strong: it requires an angular width of order at most 1/D, not merely o(1).
No canonical phase theorem is claimed to extract such a family.

## 5. Exact repair of the source-realized binary sink

Retain all definitions and labels of the preceding report's family. For
integer H, put t=1/(100H^2),

\[
 \delta_A={12t\over1+9t^2},\qquad
 \delta_B={4t\over1+t^2},\qquad D^2=H^2+25.
\]

There are H+79 source labels, eight three-rung actual O–O trains, and two
repeated owners A,B. Its binary formula realizes `A=>B`, `B=>A`, and
`not(A and B)` and admits only zero. The source is connected and triangle-
free, but lacks a positive full-contact KKT equilibrium and is explicitly
nonglobal. These repairs are not canonical-source examples.

### Repair AR: owner amplitudes (1,2)

Move every A-owned label by delta_A upwards and every B-owned label by
2delta_B upwards. Exactly twelve B rungs open, with squared length
`1+2delta_B^2`; all other old contacts remain unit. Every old noncontact is
strictly longer than one. The exact new squared diameter is

\[
 D^2-4H\delta_B+4\delta_B^2<D^2.                  \tag{AR.1}
\]

The unique longest endpoint pair is the old right diameter pair. No isolate
or source label is dropped. This repairs the repeated-owner sink without
owner-component refinement.

### Repair CR: both owners move by 2delta_A

Translate every A- and B-owned label upwards by the common displacement
b=(0,2delta_A), fixing all zero labels. Exactly 24 old rungs open. Their
squared lengths are

\[
 1+2\delta_A^2\quad(A),\qquad
 1+2\delta_A(2\delta_A-\delta_B)\quad(B).
\]

Every other old contact remains unit. Every old noncontact is strictly longer
than one, and the exact new squared diameter is

\[
 D^2-4H\delta_A+4\delta_A^2<D^2.                  \tag{CR.1}
\]

Both old diameter pairs attain this new maximum. The cloud 2delta_A is below
gamma, certified by `4D delta_A<1`, which implies
`2delta_A<1/(2D)<gamma`.

### Analytic family proof and symbolic critical slacks

The previous report proves that, at t=0, the fixed low source cluster has
exactly eleven noncontact pairs at unit distance, while 5,751 other
noncontacts of its H=30 low-source fixture are strictly longer. The same
low-cluster pairs are the only ones requiring continuity for growing H;
later vertical-chain sites are farther than one except their old vertical
contacts. The checker gives these leading squared lower slacks:

| Pair | AR leading term | CR leading term |
| --- | --- | --- |
| Af-2:LAstraight2 | 72t^2 | 72t^2 |
| Am0:Bm0 | 12t | 20t |
| Af0:Bf0 | 12t | 12t |
| Cf-2:RCstraight2 | 8t^2 | 8t^2 |
| Cm0:Dm0 | 12t | 4t |
| Cf0:Df0 | 12t | 12t |
| Emj:Fmj, j=0,1,2 | 8t^2 | 56t^2 |
| DFarmB2:DFvertical5 | 4t | 4t |
| FQleft1:FQcap2 | 88t^2 | 88t^2 |

Every expression is rational in t with positive denominator at zero and
positive leading numerator coefficient. Thus all eleven slacks are strictly
positive on one common interval 0<t<t_0. Finitely many other low-cluster pairs
stay strictly separated by continuity. The fixed-cluster/higher-chain check
is the same uniform one as in the preceding report. Therefore both endpoints
are lower feasible for every sufficiently large H. The claim is asymptotic;
H=30,31,100 are individually certified, not asserted as a uniform onset.

For upper bounds the low cluster remains in [-6,6]x[0,23]. Its internal squared
diameter is <=673, whereas the proposed endpoint maximum is at least
`H^2+25-4H delta_A>H^2+25-0.48/H`. Points with y<1 are exactly the two bottom
moving labels and their fixed counterparts. Write
`a_A=(1-9t^2)/(1+9t^2)` and `a_B=(1-t^2)/(1+t^2)`. A fixed counterpart has
coordinates `(plus-or-minus (5-a_i),delta_i/2)`. Its squared distance to the
top chain label is `(5-a_i)^2+(H-delta_i/2)^2`. For H>=30, a_i>0.9, so the
gap from either stated new maximum to this distance is at least

\[
 25-4.1^2-4H\delta_A-\delta_A^2/4>8.
\]

The bottom moving labels have |x|=5. In AR, delta_A>2delta_B and both are <H,
so the right label uniquely gives AR.1. In CR their heights equal 2delta_A,
so both give CR.1. Each distance to the vertical high chain is largest at its
top label. For all other low labels y>=1, the squared distance to a high chain
point is <=`(H-1)^2+36`, below either endpoint maximum because
`2H-12-4H delta_A>0` for H>=30. The chain's internal diameter is at most H-22.
These cases prove the upper maximum uniformly for H>=30; lower feasibility
is the preceding sufficiently-large-H statement. At H=30,31,100 the checker
also verifies every pair individually. No weighted-average-to-maximum step
is used.

## 6. Certificates and limits

Run, in an environment with SymPy:

```sh
python3 research/verify_target_c_source_realized_owner_sink_2026_10_10.py \
  --heights 30 31 100 --symbolic-limit --amplitude-repair
```

The checker verifies the original four binary states, the previously proved
refined endpoint, AR, and CR. It checks 194,684 full pair-state instances,
exact old/contact-opening identities, strict old-noncontact margins, every
new actual maximum, the 12/24 contact losses, and the cloud condition. Strict
comparisons use rational square-root enclosures; contact equalities and
critical Taylor signs use symbolic rational expressions. No floating-point
decision is used. Saved output is
`research/certificates/target_c_owner_amplitude_release_2026_10_10.jsonl`.

The original five-state invocation retains its original output and certificate.
These computations verify finite nonglobal fixtures and the finite symbolic
critical-pair calculation. They do not verify the universal candidate AB/CT
proofs independently, source-family extraction, canonical lower feasibility,
global optimality, or Level I closure. Neither candidate is promoted here.

Repository validation at this checkpoint: theorem-state consistency,
`check_theorem_state_pr.py --base-ref origin/main`, active-route summaries,
all 22 theorem-state/PR/route checker unit tests, Ruff check/format, and the
full branch whitespace check passed locally. Generated artifact metadata
registers this report as unreviewed. No canonical theorem dependency or state
version was changed; the registered canonical certificate suite was not
rerun for this candidate-only change. The historical hosted run executed zero steps; local results above are
reported separately. Main remained at the recorded SHA/state and
PR #947 remained open, so no pending claims from it were imported.

## 7. Candidate IM: stress-imbalanced owners have a concentrated loaded port

This is a finite source-level restriction on the proposed family, independent
of AB's larger endpoints. It explains an additional extraction obstacle.

### Exact statement

Let pairwise disjoint nonempty proper core subsets G_i have singleton
translations d_i=delta_i v_i that preserve every old contact and weakly shorten
every actual diameter. No lower feasibility or simultaneous selection is
assumed. Let 0<delta_i<=s<2 and let the oriented v_i window have width w.
Use the canonical positive contact stress alpha and nonnegative actual-diameter
stress beta. Every crossing contact vector, oriented from G_i to its
complement, has one of the two forms

\[
 r=-{\delta_i\over2}v_i
       \mathbin{\pm}\sqrt{1-\delta_i^2/4}\,Jv_i.       \tag{IM.1}
\]

Let A_i^+,A_i^- be the sums of alpha in these two classes, A_i=A_i^++A_i^->0,
and define the weighted orientation imbalance

\[
 \sigma_i={|A_i^+-A_i^-|\over A_i}\in[0,1].
\]

For every such owner there is a crossing actual diameter with positive beta
and oriented normal n_i at its endpoint in G_i such that

\[
 0<-n_i\cdot v_i
 \le {\delta_i\over
          2\sqrt{\delta_i^2/4+(1-\delta_i^2/4)\sigma_i^2}}. \tag{IM.2}
\]

Consequently, for any sigma_0>0 with

\[
 z_0={s\over2\sigma_0\sqrt{1-s^2/4}}<1,
 \qquad \theta_0=w/2+\arcsin z_0<\pi/2,
\]

the number of supplied owners with sigma_i>=sigma_0 is at most

\[
 \boxed{2\lfloor F_D(\theta_0)\rfloor.}              \tag{IM.3}
\]

In particular, singleton-upper-safe owners whose crossing contact forces are
all parallel with one orientation have sigma_i=1 and number at most this bound
with sigma_0=1. A single coherent oriented train cut is such an owner. This
does not say every O–O owner has one oriented train cut.

### Complete proof

Exact preservation of a crossing unit contact gives `r dot v_i=-delta_i/2`;
the two possible transverse coordinates of a unit vector give IM.1.
Summing KKT equilibrium over G_i cancels every internal contact and diameter
force. The full crossing-contact resultant is therefore

\[
 F_i=-{A_i\delta_i\over2}v_i
       +(A_i^+-A_i^-)\sqrt{1-\delta_i^2/4}\,Jv_i
     =\sum_{h\in\delta_H(G_i)}\beta_h r_h.
\]

Put `B_i=sum beta_h` on these crossing actual diameters and
`c_i=sqrt(delta_i^2/4+(1-delta_i^2/4)sigma_i^2)`. The resultant has norm
`A_i c_i`; since every actual diameter vector has length D, triangle
inequality gives `A_i c_i<=D B_i`. Its negative v_i projection is
`A_i delta_i/2>0`, so B_i>0. Singleton diameter safety gives
`r_h dot v_i<=-delta_i/2<0` for every crossing actual H pair, even if beta_h=0.
For the positive-beta pairs the weighted mean of `-n_h dot v_i` is

\[
 {A_i\delta_i\over2D B_i}\le{\delta_i\over2c_i}.
\]

At least one positive-beta pair is no larger than this mean, proving IM.2.
For sigma_i>=sigma_0 its right side is <=z_0. Its projective normal is thus
within arcsin(z_0) of Jv_i, hence within theta_0 of Jv.

Choose one such endpoint and actual partner for each counted owner. The chosen
endpoints are distinct because the G_i are disjoint. Their oriented normals
lie in two opposite theta_0 windows. Extend these partner choices arbitrarily
to all other loaded endpoints and apply the canonical partner-uniform window
bound to each window. This proves IM.3. Neither a first-order motion nor an
affine-kernel theorem is applied to contact isolates. They remain in the
full-source geometry used to bound the actual diameter normals. QED.

### Quantitative near-balance consequence

If s<gamma and w=O(D^(-1/3)), take sigma_0=D^(-2/3). Since gamma<=1/D,
`z_0=O(D^(-1/3))`, `theta_0=O(D^(-1/3))`, and L_D=7D^(2/3), IM.3 gives

\[
 \#\{i:\sigma_i\ge D^{-2/3}\}=O(D^{2/3}).           \tag{IM.4}
\]

Thus all but O(D^(2/3)) owners in any supplied linear-size family have both
cut orientations present and their positive contact stress masses equal to
relative error <D^(-2/3). More generally w=o(1) gives o(D) imbalanced owners
at any fixed positive imbalance threshold. These conclusions hold in both
canonical branches for the stated supplied-owner hypotheses. They are not
an unconditional O–O train count, because singleton actual-upper safety is an
essential hypothesis and a many-train owner can have balanced opposite cuts.
The canonical terminal O–O depletion theorem instead uses its separate
Type-II terminal/shore hypotheses without assuming these singleton proposals.

IM converts positive KKT equilibrium into a weighted two-sided boundary
requirement for a prospective large family. The fixture in Section 5 lacks
that equilibrium and its repaired upper-safe owners therefore do not validate
canonical extraction. AB/CT must be realized through actual source regions
with the required stress balance, or through a different finite mechanism.

### Stronger relative-imbalance tail bound

Define the dimensionless transverse-to-longitudinal ratio

\[
 R_i={\sigma_i\sqrt{1-\delta_i^2/4}\over\delta_i}.
\]

IM.2 is exactly `-n_i dot v_i<=1/sqrt(1+4R_i^2)`. For every T>0 with
`w/2+arctan(1/(2T))<pi/2`, the same distinct-endpoint proof yields

\[
 \#\{i:R_i\ge T\}
 \le2\left\lfloor F_D\left(w/2+\arctan{1\over2T}\right)\right\rfloor.
                                                               \tag{IM.5}
\]

For exactly parallel translation directions (w=0), trigonometric substitution
gives the particularly simple finite inequality

\[
 \boxed{\#\{i:R_i\ge T\}
 \le2+{D\over T}+4L_D\sqrt{1+{1\over4T^2}}.}        \tag{IM.6}
\]

For w=O(1/D), fixed T>=1, and L_D=7D^(2/3), this is
`# {R_i>=T}<=D/T+O(D^(2/3))`. In a family with r>=cD, taking T=2/c
(or any larger fixed T>=1) leaves at least `cD/2-O(D^(2/3))` owners with
`sigma_i< T delta_i/sqrt(1-delta_i^2/4)=O(1/D)`. More generally, for every
fixed epsilon>0, all but epsilon D+O(D^(2/3)) owners have relative stress
imbalance bounded by `O_epsilon(delta_i)`. The constants are explicit in IM.5;
the displayed O statements merely expand that finite bound.

This is stronger than the absolute IM.4 threshold for the width required by
CT. The near-balance is at each owner's displacement scale. It does not assert
an exactly balanced cut, a uniform stress lower bound, or the existence of a
finite motion beyond the supplied singleton proposal.

### Adversarial check: upper safety cannot be dropped from IM

The unit square is a triangle-free global four-point optimum with D=sqrt(2).
For a convex quadrilateral one interior angle is >=pi/2, so its adjacent unit-
separated sides force their opposite endpoints at distance >=sqrt(2). For a
point inside a triangular hull, two of the three rays from it have angle
>=2pi/3, forcing an outer pair at distance >=sqrt(3); a collinear four-point
source has diameter >=3. Thus the square's globality here is elementary.

Use vertices `(0,0),(1,0),(1,1),(0,1)` in that order and move the left column.
Let eps=200/10001, eta=9999/10001, so eps^2+eta^2=1, and
`d=2eps(eps,eta)`. All four old contacts remain exactly unit. The two old
diameter squared changes are respectively

\[
 -4\epsilon\eta=-{7999200\over100020001},\qquad
 +4\epsilon\eta=+{7999200\over100020001}.
\]

Contact and diameter weights are all 1/2; equilibrium is positive and its
PSD stress is `Omega=(1,-1,1,-1)(1,-1,1,-1)^T/2`, with affine kernel and rank
one. The contact cut has sigma=1, yet its only diameter normals are diagonal,
not within the IM.2 narrow horizontal window. One old diameter grows: the
singleton-upper-safety hypothesis fails. The weighted old-diameter change is
zero, which does not repair that failure. This small global example lies
outside the D>=9 canonical counting scope; it illustrates exactly the
sign/averaging step of IM that would be invalid if upper safety were omitted.
The four contact identities, two diameter changes, and stress kernel were
checked with exact SymPy rational arithmetic. No unbounded-family conclusion
is drawn from it.

## 8. Candidate UCC: include actual uppers in the common-release closure

The common-translation alternative need not discard all singleton-unsafe
owners. Actual upper implications can be retained and solved together with the
lower implications. This removes independent singleton actual-H safety from
the integrated endpoint criterion, at the cost of keeping these geometric
clauses in the graph.

### Exact full-source theorem

Let a finite triangle-free unit-separated source A have diameter D and a
connected contact core V. Supply disjoint nonempty proper core owners leaving
a core label fixed, and assign every isolate to one owner or to zero. Suppose
no old contact joins distinct nonzero owners. Supply a common b!=0 such that
every old contact joining an owner to the fixed source strictly opens when
that owner translates by b. CT.1–CT.3 are one sufficient mechanism for this
last hypothesis; they are not necessary for UCC. No upper safety is assumed.

At each full-source pair, calculate its lengths in each possible local binary
state. Require unchanged old contacts to stay unit, opened old contacts to be
strictly longer than one, every old noncontact to stay strictly longer than
one, and every pair to have length <=D. The resulting exact feasibility system
has only directed implications and forced-zero unary clauses.

Build its directed graph and let Z be the vertices that can reach a forced-zero
vertex. Then `x_i=0 for i in Z` and `x_i=1 otherwise` is its unique maximal
feasible assignment. It is nonzero if and only if a sink SCC has no unary
blocker. Whenever it is nonzero, it constructs a same-cardinality triangle-
free endpoint with a strict subset of old contacts and diameter <=D.

For a canonical global contact-minimal source, Z must therefore contain every
owner. A zero-only outcome has an explicit source certificate: a directed path
from each owner through actual lower/upper witness pairs to an actual unary
witness. The graph is constructed from all source coordinates and all source
pairs, rather than supplied as an abstract Horn graph.

### Complete proof

For a pair in two different moving owners, states 00 and 11 have exactly the
old distance because both endpoints have either displacement zero or b.
There is no old contact between these owners by hypothesis, so both states
have old noncontact length >1 and length <=D. Each singleton state 10 or 01
can either pass or fail the prescribed lower/upper tests. A failed 10 state
gives i=>j; a failed 01 state gives j=>i. Both failures give two implications,
equivalently equality of the variables. No incompatibility is possible since
11 is admissible. This argument includes actual diameter pairs and previously
inactive upper pairs; it does not infer their feasibility from a weighted sum.

A pair with one owner and one fixed label is either always feasible or forces
that owner to zero. An internal-owner pair is unchanged. Old contact cuts
strictly open by hypothesis, and fixed/internal contacts stay unit. Thus these
cases exhaust every lower and upper pair and prove exact equivalence with the
implication/unary system. A previously inactive upper pair may reach D; this
is allowed and fully checked, since the contact-loss contradiction does not
require minimizing the new number of diameter pairs.

Every feasible selected vertex must have all vertices reachable from it
selected, and cannot reach a unary forced-zero vertex. Hence all vertices in
Z must be zero in every feasible model. Conversely the complement of Z is
implication-closed: an edge from i outside Z to j in Z would give i a path to
a unary, a contradiction. It contains no unary variable. Selecting precisely
this complement is feasible and includes every feasible selection. The sink
criterion follows by the finite SCC argument in CT.

Every nonzero model selects a proper nonempty subset of V. Since V is
connected, its cut has an old contact. No contact joins distinct nonzero
owners, so this contact goes to the zero-labeled core and strictly opens.
All old noncontacts stay strict. The new contact graph is a strict subgraph
of the old one, still triangle-free; all original source labels and all pairs
were retained. The endpoint has diameter <=D. It contradicts globality if
the diameter is smaller, and canonical contact minimality otherwise. QED.

### Canonical sparse ledger and exact repair

Under CT's actual O–O/face hypotheses and rho=|b|<gamma, the pairs needing an
explicit upper clause are only actual H and E: dispatch makes all other
inactive upper pairs strict regardless of selection. The lower clauses are
outer-face pairs of old length <=1+rho and unary cut-rhombus diagonals. These
are full-source coordinate statements, including isolates. Instead of marking
the E owners fixed, UCC can keep their actual upper clauses; an E pair with two
moving owners again supplies implications rather than an incompatibility.

For the Section 5 source, check additionally the common singleton states
`A moves by 2delta_A, B fixed` and `B moves by 2delta_A, A fixed`. Their actual
pair witnesses give exactly A=>B at Am0:Bm0 and B=>A at Cm0:Dm0, with no unary
or upper blocker. The maximal assignment is therefore (1,1), whose actual
full-source endpoint is CR. The checker certifies all nine states, including
these two singletons, for H=30,31,100: 250,308 pair-state checks. Run

```sh
python3 research/verify_target_c_source_realized_owner_sink_2026_10_10.py \
  --heights 30 31 100 --symbolic-limit --amplitude-repair \
  --common-implication-system
```

Saved output is
`research/certificates/target_c_common_release_implication_2026_10_10.jsonl`.
This is a finite nonglobal repair of the formerly zero-only repeated-owner
formula, not a proof of a nonzero UCC model in a canonical source. UCC is a
contact-opening extension and specialization of the canonical exact pairwise
2-SAT compilation; its new consequence concerns the changed move, its full
upper clauses, and contact loss. Merely changing the compilation of the old
contact-preserving binary family would not remove its incompatibility.

## 9. One precise next obligation

Prove the following source extraction and unary-avoidance statement, or find
its exact canonical obstruction:

> Every sufficiently large canonical triangle-free C-II source contains an
> actual subfamily-stable O–O owner family satisfying CT.1, with fixed dispatch
> and bounded-face isolate transport, whose integrated common-b lower/actual-H/E
> implication graph has a sink SCC containing no full-source lower or upper
> unary blocker.

Together with UCC this gives a full-source finite contact-loss contradiction.
The theorem must concern the actual source, its actual owners, and every
retained isolate. IM shows that a linear family in the stated narrow direction
window and with independently upper-safe singletons must use almost balanced
opposite contact-force classes rather than single coherent train shores. The
integrated UCC criterion also permits singletons coupled by actual upper
implications. Normal atomlessness or a source-free Horn graph by itself does
not establish the source extraction or nonzero-model statement.
