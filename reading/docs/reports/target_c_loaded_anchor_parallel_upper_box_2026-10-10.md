> Generated reading edition · [exact source](../../../docs/reports/target_c_loaded_anchor_parallel_upper_box_2026-10-10.md) · source SHA-256 `8209ff78aef0f9a88157d47d2260ec8965fc4c496c08d415ade348ae8f1e3c0a`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-894D4E050EB2","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# A parallel upper box from local loaded-anchor coverage

**Worker:** Slot 01, source-realized outer-face finite motion.

**Checkpoint date:** 2026-10-11, continuing the run started 2026-10-10.

**Base:** `ab6dd3336f9f8d440f2bada76edb32153391cddc`.

**Authority:** `2026-10-10.audit.234`; pending PR #947 is not a premise.

**Classification:** proved candidates awaiting independent audit; exact finite regression.

**Status:** C-II and Level I remain open.

The new geometric result supplies a common parallel upper-safe amplitude box
when the near-diameter-relevant labels in each owner are covered within
R=o(D) by actual loaded anchors in that same owner. Long owners may use several
anchors. Only labels participating in a potentially active upper pair need
coverage, including assigned isolates. After discarding o(D) owners, every
original inactive upper pair stays strict throughout the box. This requires
neither the exceptional-pair set E nor rho<D-sqrt(D^2-1). The price is an
explicit local coverage hypothesis, not extracted here.

The implication chain is

```text
supplied owner-local coverage by actual loaded anchors
  -> full-source upper-safe common-ray box after normal-window deletion
  -> inclusive floor closure needs only strict lower constraints
  -> any surviving core owner gives contact loss or a full-source
     contact-preserving diameter-pair contradiction.
```

The last finite endpoint uses
[IFC and LCR](target_c_inclusive_floor_closure_and_locked_contact_release_2026-10-10.md),
whose complete proofs are provided there. Neither source-family extraction nor
nonempty lower closure is asserted. The present theorem reduces an upper
obligation for this narrower actual-source class. In this box the anchor proof
also gives old-diameter loss directly, so neither PSD nor an additional isolate
normalization is needed to obtain that finite lexicographic consequence.
GC below proves global loaded-vertex proximity for all near-diameter labels
in the canonical full-core branch; owner membership and crossing incidence
are the remaining port conditions.

## 1. Finite phase lemma at an arbitrary subdiameter slack

Let a finite planar source of diameter D lie in a constant-width-D body W.
Put Delta_W=pi D^2/4-area(W). For two source partners q_1,q_2 of z with
|z-q_j|>=D-epsilon, assume 0<epsilon<=D/10. Let theta be the angle between
the two rays z-q_j. Then

```math
 \boxed{\theta\le\max\left\{
       \sqrt{96\epsilon/D},\ (192\Delta_W/D^2)^{1/3}\right\}.}       \tag{1}
```

This is an extension of the one-vertex argument in canonical Audit.126 to
epsilon that may exceed a fixed inverse-D scale. The extension needs no
degree count or unit-neighbor angular gap. We prove it rather than applying
the inverse-D theorem outside its promoted parameter range.

### Proof

The source diameter gives

```math
 \cos\theta\ge1-\frac{D^2}{2(D-\epsilon)^2}>0,
```

so theta<pi/2. Set a=theta/2<pi/4 and center the normal interval I=[-a,a]
between the two rays. The support function h of W satisfies
h(theta)+h(theta+pi)=D. Its curvature measure rho_W=h+h'' obeys
rho_W(theta)+rho_W(theta+pi)=D dtheta, so it has bounded density between
zero and D. Consequently h is in W^{2,infinity}.

For either endpoint normal n=(z-q_j)/|z-q_j|, constant width and q_j in W
give 0<=h(n)-z dot n<=epsilon. Sublinearity of h bounds the intermediate
support slack y(t)=h(t)-z dot n(t) by epsilon cos(t)/cos(a)<=2epsilon.

Put p=h-D/2 and f=p+p''=rho_W-D/2. Both are antiperiodic. On antiperiodic
H^1 functions let E(g)=integral(g'^2-g^2). Odd Fourier modes have eigenvalues
j^2-1>=0, so E is positive semidefinite and its first-harmonic kernel causes
no difficulty. The support-area formula gives E(p)=2Delta_W. Polarization
and semidefinite Cauchy--Schwarz give

```math
 |\langle f,g\rangle|^2=|E(p,g)|^2\le2\Delta_W E(g).             \tag{2}
```

On I set g(t)=cos(t)/cos(a)-1, set its negative on I+pi, and zero elsewhere.
It is antiperiodic and H^1. Direct integration, with k=tan(a)-a, gives

```math
 E(g)=4k,\quad\int_Ig=2k,\quad k\ge a^3/3.                     \tag{3}
```

The last inequality follows by differentiating tan(a)-a-a^3/3: its derivative
is tan^2(a)-a^2>=0 since tan(a)>=a. Integration by parts using y''+y=rho_W,
g''+g=-1, g(+-a)=0 and g'(+-a)=mp tan(a) gives

```math
 \int_I\rho_Wg=\tan(a)(y(-a)+y(a))-\int_Iy
 \le2\epsilon\tan(a).
```

Antiperiodicity therefore gives

```math
 -\langle f,g\rangle
 =2Dk-2\int_I\rho_Wg
 \ge2Dk-4\epsilon\tan(a)\ge2Dk-8\epsilon a.                    \tag{4}
```

Here tan(a)<=2a for 0<=a<=pi/4: the derivative of 2a-tan(a) is
2-sec^2(a)>=0 and its value at zero is zero. If a^2>=24epsilon/D,
(3) gives Dk>=8epsilon a; (2)--(4) imply D^2k^2<=8Delta_W k.
For a>0 this gives k<=8Delta_W/D^2 and theta^3<=192Delta_W/D^2.
Otherwise theta<sqrt(96epsilon/D). The theta=0 case is immediate. QED.

A constant-width completion of the full source hull is available by the
completion argument independently reconstructed in Audit.126. It has
Delta_W<=delta_K=pi D^2/4-area(conv(A)). For canonical global sources,
`C-FS-GEOM` gives delta_K<pi sqrt(3)D/4. Thus (1) has the explicit global
upper bound

```math
 \Theta=\max\{\sqrt{96\epsilon/D},\ (48\pi\sqrt3/D)^{1/3}\}.      \tag{5}
```

In particular epsilon=o(D) gives Theta=o(1). No uniform near-diameter degree
bound is inferred; Audit.126's inactive-star regression remains binding.

## 2. AS: the loaded-anchor common-ray upper box

Use the canonical C-II full source, D>=9. Supply pairwise disjoint proper core
owners with their fixed full-source isolate assignments. Write G_i for the
entire moving label group. A group may include isolates, but has a nonempty
proper core part. Keep at least one core label outside the family.
Require each owner's old contact cut to be nonempty, as it is for an actual
O--O shore.

Suppose the parent translations d_i=delta_i v_i, delta_i>0, preserve every
old contact in every binary selection. Their unit directions lie in an
oriented interval of width w<pi/2 centered at v. Assume each parent singleton
passes every actual diameter upper constraint. No inactive upper or lower
feasibility is assumed here.

These hypotheses force no old contact between distinct moving groups. For
such a pair, the mixed difference of its four binary squared lengths is
-2 d_i dot d_j, which is negative because the directions are in an acute
interval. It cannot equal zero as exact preservation in all four states
would require.

Each owner has a crossing actual diameter edge z_i h_i with z_i in G_i and
h_i outside G_i. Indeed contact preservation makes each crossing contact's
projection on d_i equal -|d_i|^2/2; summing positive KKT equilibrium over the
proper core owner gives a negative crossing diameter resultant. An actual
crossing edge therefore exists. All actual diameter endpoints lie in V.
Thus at least one actual anchor exists; this does not give local coverage.
For each owner fix a finite nonempty anchor set A_i of loaded labels z in G_i.
For each z in A_i choose an actual crossing diameter z h_z, with h_z outside
G_i, and write n_z=(z-h_z)/D. Parent singleton upper safety gives

```math
 n_z\cdot v_i\le-\delta_i/(2D)<0\qquad(z\in A_i).              \tag{6}
```

Choose rho>0. Call p in G_i upper-relevant if some q outside G_i has
|p-q|>=D-rho. **Local coverage hypothesis:** every upper-relevant p satisfies

```math
 \min_{z\in A_i}|p-z|\le R.                                    \tag{7}
```

It is essential that (7) cover upper-relevant assigned isolates as well as
core points. Merely knowing that an owner contains a loaded endpoint does not
suffice. The whole owner need not have diameter o(D); different labels may
use different anchors. Labels with no pair of length at least D-rho outside
their owner require no coverage, since the triangle inequality handles them.

Assume R+rho<=D/10. Put epsilon=R+rho. Use Theta from (5), or the tighter
bound (1) if a completion's actual deficit is known, and set

```math
 \Phi=w/2+\Theta+
       \arcsin\frac{R}{D-\rho}+
       \arcsin\frac{\rho}{2(D-\rho)}<\pi/2.                     \tag{8}
```

Discard an owner if any of its chosen n_z lies in either closed normal window
of half-width Phi around Jv or -Jv. With L_D=7D^{2/3} and

```math
 F_D(\Phi)=1+\frac{D\sin\Phi+2L_D}{\cos\Phi},
```

at most 2 floor(F_D(Phi)) owners are discarded. Every full-source placement

```math
 Q_p=P_p+s_i v\ (p\in G_i),\quad 0\le s_i\le\rho,              \tag{9}
```

with discarded groups and all other labels fixed, has diameter at most D.
Every old inactive upper pair remains strictly below D throughout this box.
This is a theorem about upper constraints only; some contacts contract for
intermediate heights, and lower feasibility is still checked separately.

### Full-source upper proof

For a retained owner and every chosen anchor z, the angle between v_i and v
is at most w/2. By (6), n_z cannot lie on the positive-v side outside the
perpendicular window. Since it is outside the closed windows in (8),

```math
 n_z\cdot v<-\sin\Phi.
```

First translate only G_i by rho v, and fix all other labels. For p in G_i,
q outside G_i, put r=p-q. If |r|<D-rho, the triangle inequality makes the
new length strictly below D. Otherwise p is upper-relevant. Choose z in A_i
by (7), giving |z-q|>=D-rho-R=D-epsilon. Compare this ray at z with the actual
ray z-h_z: equation (5) bounds their angle by Theta. If q=h_z this angle is
zero. The ray p-q differs from z-q by at most
arcsin(R/(D-rho)): a radius-R ball about r subtends at most that angle,
since |r|>=D-rho>R.

Thus the normal r/|r| lies within Theta+arcsin(R/(D-rho)) of n_z and remains
on the negative-v side by a margin greater than arcsin(rho/[2(D-rho)]).
Consequently

```math
 \frac{r\cdot v}{|r|}<-\frac{\rho}{2(D-\rho)},
 \qquad r\cdot v<-\rho/2.
```

Therefore |r+rho v|^2=|r|^2+2rho r dot v+rho^2<|r|^2<=D^2. This proves
strict upper safety for **every** moved/fixed pair, including all isolates
and near-diameter pairs that were inactive. Nothing was inferred from an
actual-diameter degree estimate alone.

At a vertex of the box (9), every group moves either zero or rho v.
Pairs between two moved groups, or two fixed groups, are unchanged; every
moved/fixed pair is strictly shorter than D. Thus all upper constraints hold
at every box vertex, and every originally inactive pair is strict there.
Squared pair length is convex in the height variables. It is bounded by its
maximum over the finitely many box vertices, giving (9) and strictness for
all originally inactive pairs everywhere in the box.

No actual diameter joins two retained owners. If it did, moving either endpoint
group alone by rho v would give squared changes 2rho r dot v+rho^2 and
-2rho r dot v+rho^2. Their sum is 2rho^2>0, contradicting upper safety of
both box vertices. Consequently every chosen retained anchor edge ends in
the fixed group. Its projection satisfies r dot v<-rho/2 by the proof above.
At every positive height s<=rho it strictly shortens, since
2s r dot v+s^2< -s rho+s^2<=0.

### Deletion count and asymptotic scope

Canonical actual-diameter midpoint and hull-normal geometry gives at most
2 floor(F_D(Phi)) loaded vertices supporting a diameter edge with normal in
these two windows. The proof is the projection count: normal-window endpoints
are within 2L_D+D sin(Phi) in the transverse coordinate, while successive
unit-separated hull endpoints contribute at least cos(Phi) each.
Between two such successive endpoints on the same convex normal-window arc,
every intervening side has transverse projection at least cos(Phi) times its
length. The intervening length is at least the endpoints' unit separation;
the projection gaps therefore sum to the stated count even if other hull
vertices intervene. Each endpoint has transverse coordinate within
[-L_D-D sin(Phi)/2,L_D+D sin(Phi)/2] by its actual diameter midpoint bound.
Choose one bad anchor label z for each discarded owner. These labels are
distinct because the actual moving core sets are disjoint, and each is among
the counted loaded vertices. Hence the owner loss is at most
2 floor(F_D(Phi)), regardless of the number of anchors needed within an owner.
This uses the canonical actual-normal count from the earlier Slot 01 amplitude
report; it needs neither an actual-edge degree estimate nor an inactive-pair
degree bound. Woodall is not needed for this vertex charge.

If R=o(D), rho=o(D), and w=o(1), (8) has Phi=o(1), and

```math
 2\lfloor F_D(\Phi)\rfloor=O(D\Phi+D^{2/3})=o(D).               \tag{10}
```

Thus a supplied linear-sized locally covered family retains a linear-sized
upper-safe family. The theorem does not prove that such a family exists.
An owner of diameter comparable with D can qualify if its upper-relevant
labels have several nearby anchors. A single favorable anchor with distant
uncovered upper-relevant labels does not qualify.

### Native-direction upper box

If w<=pi/3, the same retained family also has the upper-safe box

```math
 Q_p=P_p+s_i v_i\quad(p\in G_i),\qquad 0\le s_i\le\rho.          \tag{12}
```

Every originally inactive pair stays strict. This protects each parent's
original contact-preserving displacement whenever delta_i<=rho; it does not
assert lower feasibility of the entire native-direction box.

To prove (12), write Psi=Phi-w/2. For every retained anchor,
angle(n_z,-v_i)<pi/2-Psi. Repeating the near-diameter ray comparison in the
upper proof with direction v_i gives r dot v_i<-rho/2 for every pair from
G_i to its complement with |r|>=D-rho. Such a pair is strictly nonexpansive
under the full native singleton translation rho v_i.

At a native box vertex, if a pair with |r|>=D-rho has both owner groups i,j
moving, apply this conclusion from both endpoints:
r dot v_i<-rho/2 and r dot v_j>rho/2. Its squared change is

```math
 2\rho r\cdot(v_i-v_j)+\rho^2|v_i-v_j|^2
 <-2\rho^2+2\rho^2(1-v_i\cdot v_j)<0.
```

The last inequality uses v_i dot v_j>=1/2. If |r|<D-rho, the two-owner
relative displacement has length rho|v_i-v_j|<=rho; the triangle inequality
keeps that pair strictly below D. Pairs with only one moving group were
already checked, and pairs within a group are unchanged. Convexity over the
native height box finishes the proof, including strictness for inactive pairs.
Every chosen anchor diameter joins the fixed group, as established using the
common-direction box, and strictly shortens at every positive native height.

The lower costs for different directions v_i are not IFC's common-direction
difference costs. We use (12) below to certify original singletons for a
canonical capacity theorem, rather than falsely applying a parallel lower
solver to the native-direction system.

## 3. GC: global actual-loaded coverage in the full-core branch

The local coverage distance in AS is not an additional global shape assumption
in the canonical full-core near-disk branch. The issue there is ownership and
external diameter incidence.

Let F=conv(V), with every vertex of F an actual loaded endpoint. Suppose
F contains a disk centered at c of radius r_-=(1/2-eta)D, where
0<eta<1/4. Keep all original source labels, all of whose pair distances are at
most D. If rho<r_- and a source point p has a source partner q with
|p-q|>=D-rho, then there is an actual loaded vertex z of F with

```math
 \boxed{|p-z|\le R_{\rm global}
       :=D\bigl(2\eta+\sqrt{2\eta}\bigr)+\rho.}                \tag{11}
```

This covers contact isolates outside F, not just positive-contact coordinates.

### Complete finite proof

For every source p and every x in F, convexity of the norm extends the
full-source inequalities to |p-x|<=D. Taking the opposite point of the
inner disk gives |p-c|+r_-<=D. Hence the entire source, and F itself, lie
in the concentric disk of radius r_+=(1/2+eta)D.

The near-diameter pair gives |p-c|>=|p-q|-|q-c|>=r_- -rho>0. Let x be the
intersection of the ray from c through p with the boundary of F. Its radius
lies in [r_-,r_+], whereas p's radius lies in [r_- -rho,r_+]. Therefore
|p-x|<=2eta D+rho.

The boundary point x lies on a loaded hull side zz', or is already a loaded
vertex. The side's supporting line has distance h>=r_- from c. Its endpoints
lie in the disk of radius r_+, so

```math
 |z-z'|\le2\sqrt{r_+^2-h^2}
          \le2\sqrt{r_+^2-r_-^2}=2D\sqrt{2\eta}.
```

Choose the nearer endpoint, at distance at most D sqrt(2eta) from x. The
triangle inequality proves (11). No packing density or omitted source labels
enter this finite geometric argument.

For the canonical source, every hull vertex of V is loaded: if it had no
actual diameter multiplier, positive KKT equilibrium would express it as a
convex combination of its distinct unit-contact neighbors in V, impossible
for an extreme vertex. Canonical `C-FULLCORE-NEAR-DISK` says that, in the
no-macroscopic-container branch, F/D converges to a radius-1/2 disk. The inner
disk above therefore exists with eta=o(1). For any rho=o(D), (11) gives
R_global=o(D) for **every** near-diameter label in the full original source.
The full-core theorem's macroscopic chamber/cap alternative remains separate.

This does not prove AS's owner-local coverage. The loaded vertex from (11)
may belong to a different moving owner or to the fixed group; its actual
diameter partners may all lie in the same owner as it. Neither defect is
removed by the distance estimate. If an actual owner family supplies nearby
loaded vertices in the correct owner with a crossing actual diameter, (11)
provides an admissible subdiameter coverage scale and AS removes the upper
system after o(D) deletions. Thus the remaining port bridge is explicitly
about source ownership and diameter incidence, rather than unproved global
phase coverage.

## 4. The remaining finite system has only lower costs

In (9) choose inclusive contact floors F_i computed from the actual common
direction v. They satisfy

```math
 F_i\le\delta_i+4\sin(w/4),
```

because each cut unit vector has projection -delta_i/2 on v_i and differs in
projection on v by at most |v-v_i|<=2sin(w/4). A choice
rho>max_i delta_i+4sin(w/4) allows every group individually to clear its floor;
this does not settle other lower pairs.

All full-source upper inequalities are already satisfied throughout the box,
with every inactive pair strict. Consequently IFC may use only the original
noncontact lower costs (4) of its report and the height bounds rho. No actual
or newly active upper constraint needs to be guessed or omitted. If that
lower closure retains a core owner, the source endpoint either opens a contact
or preserves all contacts. In the latter case each active owner's chosen
anchor pair strictly shortens, as just proved. Those chosen pairs are distinct:
each joins its own disjoint moving group to the fixed group. Hence k active
owners remove at least k old diameter pairs and create none. This supplies
the lexicographic contradiction directly, without using PSD to extract a
weighted old-diameter gain. Both outcomes contradict the canonical minimum.

This is a genuine upper-system reduction under supplied geometric hypotheses,
not an unconditional lower feasibility theorem. Bounded unary rhombus blockers,
cyclic near-unit clauses, and fixed-root lower constraints remain present.

### LDE: low-defect family exclusion without a 2d_H loss

In a canonical Type-II near-disk sequence, supply a subfamily-stable O--O
family with all of Audit.106's contact, unary-rhombus, small-cloud, isolate
assignment, and outer lower-witness localization hypotheses. Instead of
assuming its inactive upper tests, assume AS's local port coverage with
R=o(D), w=o(1), and rho=o(D), where max_i delta_i<=rho. Let Phi be (8).
Then, for sufficiently large D, its original number r of owners obeys

```math
 \boxed{r\le2\lfloor F_D(\Phi)\rfloor+147(x_B+m_B).}             \tag{13}
```

There is no d_H term. In particular x_B+m_B=o(D) implies r=o(D), excluding
every such linear-sized family even when d_H is linear in D.

Discard only AS's bad-anchor owners, at cost at most 2 floor(F_D(Phi)).
Eventually w<=pi/3. Each retained original singleton is in (12), hence passes
**all** upper tests strictly for old inactive pairs and shortens its chosen
actual anchor diameter. It preserves every old contact by the parent premise
and still passes the supplied unary tests. Discarding proposals changes neither
source labels nor any retained displacement or isolate assignment. Thus all
of canonical `C-OO-LOWER-WITNESS-OWNER-CAPACITY` (Audit.106)'s exact Type-II
hypotheses hold for this retained family, including the specified outer
lower-witness scope. That theorem gives k<=147(x_B+m_B). Adding the discarded
owners proves (13). Equation (10) gives the claimed o(D) implication.

For comparison, canonical Audit.114's original-family extension discards up
to 2d_H owners touched by E and gives r<=147(x_B+m_B)+2d_H. The new port
coverage hypothesis replaces that exceptional-pair deletion with the actual
normal-window deletion above; it is not inferred from Audit.114. This changes
the sufficient conditions for excluding a proposed large owner family,
without extracting one or establishing low boundary defect in every survivor.

## 5. Exact finite checks and necessity of localization

For D in {300,500,1000}, let delta=2/D, rho=3/D, a=sqrt(1-1/D^2), and use
the circle of radius D/2 centered at (0,D/2). Put

```math
 p=(0,0),\ q=(0,D),\ l=(-a,1/D),\ r=(a,1/D).
```

The only contacts involving p are pl,pr. Their floor is delta. Reflection by
delta v with v=(0,1) preserves both; height rho opens both to squared length
1+3/D^2.

**Localized full-source check:** add the two circle points (+-D/2,D/2) and
the isolate u=(0,2). Move G={p,u}. It lies within R=2 of the actual anchor
p, whose diameter partner is q and whose normal is -v. The other labels,
including all isolates, stay fixed. The given circle is a constant-width
completion with Delta_W=0, so (1) gives Theta=sqrt(96(2+rho)/D).
For D>=300 this is below 17/20. Using arcsin(x)<=2x for 0<=x<=1/2 bounds
Phi by 17/20+4/(D-rho)+rho/(D-rho)<9/10<pi/2. The chosen normal is outside
the window. Exact full-pair checks confirm every claimed upper constraint at
zero, delta, and rho, including the moved isolate. At rho the contact count
falls from two to zero and the surviving diameter is the horizontal circle
pair.

**Far-label regression:** instead of the horizontal circle pair and u, add

```math
 b=(-L/2,D/2-\delta/4),\quad c=(L/2,D/2+\delta/4),
 \qquad L^2=D^2-\delta^2/2.
```

All six original points lie in the same circle and are unit-separated. Move
G={p,b}; p still supplies the good actual anchor. The parent height delta
preserves contacts and is upper-safe for every source pair. Its diameter is
strictly smaller than D. However, the common release height rho has

```math
 |b+\rho v-c|^2=D^2+\delta^2/2>D^2.
```

The blocking pair was inactive, with original squared length D^2-delta^2/4.
The distance |b-p| is of order D, so (7) with subdiameter R fails. A good
loaded anchor, source containment in a disk, and parent singleton upper
safety do not justify moving distant owner labels by the larger common
amplitude. This is precisely the hypothesis gap AS avoids. It is not a
counterexample to a canonical minimizer theorem.

The localized and far-label fixtures contribute 324 full pair-state checks.
An additional native-direction fixture places two independent two-contact
owners on the same circle, with angular separation theta given by
tan(theta/2)=1/80. Writing c=cos(theta), s=sin(theta), its second owner is
z=(Ds/2,D(1-c)/2), its fixed diameter partner is the opposite circle point,
and its fixed unit neighbors are z+(-s,c)/D plus or minus a(c,s).
The directions are (0,1) and (-s,c). The script checks all four native box
vertices and the two-parent contact-preserving endpoint for each D: 420
additional full pair-state checks. The simultaneous native release opens all
four contacts, while the parent endpoint preserves them; both have exact
squared diameter D^2-1. All original inactive pairs remain strict.

Thus the executable checks 744 pair-state instances and exact contact,
diameter, and failure identities. These fixtures are explicitly nonglobal;
their cardinalities are six, seven, or eight with D>=300. They validate finite
geometry and regression, not the general phase-energy proof, normal count,
canonical family extraction, the conditional capacity consequence (13), or
lower-closure survival. A closer attempted two-owner spacing at
tan(theta/2)=1/100 failed original unit separation at D=300; the full-pair
checker rejected it before any endpoint claim. No numerical tolerance was
used to excuse that lower violation.

Reproduce the checks with

```bash
python3 research/verify_target_c_loaded_anchor_upper_box_2026_10_10.py \
  --diameters 300 500 1000
```

The script requires SymPy and the original Slot 01 enclosure helper. Saved
output is `research/certificates/target_c_loaded_anchor_upper_box_2026_10_10.jsonl`.
It uses symbolic equality checks and directed rational enclosures, with no
floating-point feasibility decisions. Its independent exact bounds also check
source containment in the stated disk and the localized example's phase-window
parameters. No independent audit of the general analytic proof is claimed.

Canonical dependencies are KKT equilibrium and actual endpoints on V,
`C-FS-GEOM`, `C-FS-DIAMETER-MIDPOINT-D2-3`, the actual hull-normal projection
count, `C-FULLCORE-NEAR-DISK` for GC's asymptotic scope, and the source's
lexicographic minimum. LDE additionally uses the exact promoted
`C-OO-LOWER-WITNESS-OWNER-CAPACITY` from Audit.106 and all its stated
localization hypotheses. The constant-width support
machinery is reconstructed above from Audit.126's audited completion argument.
The local phase extension and upper box are new candidates, not canonical
imports from that audit.

## 6. Next source theorem

Extract, from every sufficiently large canonical C-II survivor in a specified
remaining branch, a family of r>=cD actual independent owners satisfying the
parent singleton upper tests, w=o(1), and owner-respecting crossing diameter
anchors for (7), including every upper-relevant assigned isolate. In the
full-core near-disk branch, GC supplies the global subdiameter proximity scale
but not its ownership or crossing incidence. Then prove that after AS's
normal-window deletion, the
strict lower-only inclusive closure retains a core owner. This would give an
actual finite same-cardinality contradiction by AS plus LCR.

The alternative is a source-specific payment for owners with upper-relevant
labels that remain far from all loaded ports in their own owner. The far-label
regression shows why that case cannot be handled merely by choosing one
favorable loaded endpoint.
Neither alternative is proved here, and no canonical obstruction is declared
closed.
