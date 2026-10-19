> Generated reading edition · [exact source](../../../docs/audits/target_c_pr952_loaded_anchor_upper_box_independent_audit_2026-10-19.md) · source SHA-256 `28607516f5ffd04bbca104c6331973b336f6cc144b97c09672ce0f999f999511`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-15B269A89E1C","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Independent destination audit of the PR #952 loaded-anchor upper box

**Disposition: PASS, conditional on the exact supplied hypotheses below.**
This is an independent review of one candidate at destination main
7d0a450fe66991036541023f95c44c064a04b6a8. It changes no theorem lifecycle.
Target C-II and Level I remain open.

## Exact target and audit boundary

The reviewed candidate is
TARGET-C-PR952-LOADED-ANCHOR-UPPER-BOX, represented at the destination by
[the analytic report](../reports/target_c_loaded_anchor_parallel_upper_box_2026-10-10.md),
[its finite verifier](../../../research/verify_target_c_loaded_anchor_upper_box_2026_10_10.py),
and [its saved output](../../../research/certificates/target_c_loaded_anchor_upper_box_2026_10_10.jsonl).
Their destination SHA-256 values are, respectively:

- report: 8209ff78aef0f9a88157d47d2260ec8965fc4c496c08d415ade348ae8f1e3c0a
- verifier: e344779df3f4bac62d2c8b37b786986f18300b1bf8326d4f49626296d1e16d4d
- saved output: a81a9de0b052779ea2023a57e877c5fa3288d0fa5966fb01ba4ca37eacfe3fb8

The source is the still-open legacy-repository PR
[1337isnot1337/e-99#952](https://github.com/1337isnot1337/e-99/pull/952),
head 3536c0b6f6c2a929d9c96fffbdcfc480735fea3b, tree
a6503b1817dbd885f9378ca42677d811fe363c84. Authenticated GitHub API reads at
that exact head reproduced all three source hashes above. The historical source
candidate was unreviewed. On destination main, the candidate registry and
artifact index also say unreviewed, with no claim IDs. This review is bound to
the destination bytes and does not inherit or change source lifecycle.

The task is the three conditional implications in the candidate: the
same-owner common-ray and native-direction upper boxes, the full-core
near-disk loaded-vertex proximity estimate, and the Type-II owner-capacity
bound. It does not review the other PR #952 reports, establish the owner
family, prove the hypotheses for every canonical source, prove lower-closure
survival, or promote a claim.

Concrete route quantity: the upper box controls every full-source pair with
at least one moving label, including inactive upper pairs and assigned
isolates; the LDE implication controls the supplied family size by
2 floor(F_D(Phi)) + 147(x_B+m_B). Its possible downstream use is conditional
exclusion of a linear-sized O--O family in the low-defect Type-II branch.

Falsification test: remove same-owner coverage and keep a distant
upper-relevant label despite a good local loaded anchor; check whether the
larger common release can cross D while the parent singleton remains safe.
The report's far-label fixture is exactly this control. Stop when the
conditional proof and finite controls are independently checked; source-wide
owner extraction and lower closure are separate work.

## Canonical dependencies and lifecycle

The report uses the following canonical premises at their stated scopes:

- C-FS-GEOM, for the full-source area allowance and
  delta_K < pi sqrt(3) D / 4;
- C-FS-DIAMETER-MIDPOINT-D2-3, for every actual diameter midpoint being
  within 7 D^(2/3) of a common full-source circumcenter;
- C-LOADED-HULL, for actual loaded endpoints and the loaded force hull;
- C-CII-ACTUAL-DIAMETER-NORMAL-ATOMLESS, whose finite oriented-window
  projection estimate is independent of partner choices;
- C-FULLCORE-NEAR-DISK, only for the no-macroscopic-container Type-II
  asymptotic branch used by the proximity corollary; and
- C-OO-LOWER-WITNESS-OWNER-CAPACITY ([Audit.106](target_c_outer_owner_witness_capacity_independent_audit_2026-10-07.md)), for its supplied-family
  Type-II bound after all exact singleton hypotheses are met. Its exact
  canonical inputs are C-OO-LOWER-BLOCKER-LOCALIZATION,
  C-DIAMETER-ENDPOINT-LOCAL-DEGREE-TWO,
  C-NEARBY-DIAMETER-ENDPOINTS-FULL-HULL-SIDE, and
  C-OO-OUTER-ISOLATE-COLLAR-BOUND ([Audit.105](target_c_outer_isolate_collar_independent_audit_2026-10-07.md)); the last result's localization proof also uses
  C-LONG-PAIR-ISOLATE-DISPATCH, C-RHOMBUS-POP, and the canonical Section 77
  exterior-cap partition. These apply only inside the supplied Type-II family
  and stated isolate and lower-witness localization hypotheses.

These claim IDs are canonical in [docs/state/theorem-state.yaml](../../../docs/state/theorem-state.yaml).
The destination artifact-index entry ART-894D4E050EB2 and candidate-registry
record remain unreviewed. The theorem state remains 2026-10-15.publication.2, priority revision
public-frontier.3, and catalogue revision public-frontier.9. The candidate
remains unreviewed. No manifest, priority, accepted lifecycle, certificate
registration, or release setting changed.

The proof below reconstructs the candidate rather than treating its finite
checker or the source PR status as proof. The only external geometric input
needed for the completion step is the planar characterization that a compact
convex body has constant width exactly when each boundary point lies on a
diameter; see Kupitz, Martini, and Wegner, Proposition 1.3,
[A Linear-Time Construction of Reuleaux Polygons](https://emis.de/ft/11518).
Their Theorem 0.1 is not used: its Hamiltonian diameter-graph hypothesis
would be too narrow for an arbitrary source hull.

**Exposure order:** I derived the phase, upper-box, global-proximity, and
capacity arguments before inspecting earlier audit conclusions for this
candidate. I then checked the destination source report, the pinned verifier,
and the canonical prerequisite proofs, including Audit.106. The prior exposure
is therefore to the source argument, its canonical dependencies, and finite
controls; the live destination search found no earlier audit of this exact
candidate.

## Independent reconstruction

### Phase estimate for two near-diameter rays

Let a diameter-D source lie in a constant-width-D body W. At a source point
z, let two partner rays have lengths at least D-epsilon, where
0 <= epsilon <= D/10, and let theta be their angle. The partner points are
at distance at most D. Writing the ray lengths as l_1,l_2, the cosine rule
and (l_1/l_2 + l_2/l_1)/2 >= 1 give

    cos(theta) >= 1 - D^2 / (2(D-epsilon)^2) > 0.

Put a=theta/2<pi/4 and take I=[-a,a] centered between the rays. For the
support function h of W, the endpoint slack
y(t)=h(t)-z dot n(t) satisfies 0 <= y(-a),y(a) <= epsilon: if
q=z-l n is a partner along a unit vector n, then q in W and constant width
give h(n)-z dot n <= D-l. The intermediate normal is a nonnegative
combination of the endpoint normals whose coefficients sum to
cos(t)/cos(a) < 2. Sublinearity therefore gives 0 <= y(t) <= 2 epsilon
throughout I.

The curvature measure mu=h+h'' is between 0 and D times angular measure,
because mu(t)+mu(t+pi)=D dt. Thus h is in W^(2,infinity). Set p=h-D/2
and f=p+p''. Both are antiperiodic. With

    E(g)=integral_0^(2pi) (g'(t)^2-g(t)^2) dt,

the odd Fourier modes show E is positive semidefinite, its kernel being
the first harmonics. The support-area identity gives E(p)=2 Delta_W, where
Delta_W=pi D^2/4-area(W); integration by parts and semidefinite
Cauchy-Schwarz give |integral f g|^2 <= 2 Delta_W E(g).

Set k=tan(a)-a. On I let g(t)=cos(t)/cos(a)-1, put -g on I+pi,
and put zero elsewhere. Then g is antiperiodic and in H^1,
E(g)=4k, integral_I g=2k, and k>=a^3/3. On I, g''+g=-1,
g(+-a)=0, g'(-a)=tan(a), and g'(a)=-tan(a). Since y''+y=mu,
integration by parts at the endpoints of I gives

    integral_I mu g
      = tan(a)(y(-a)+y(a))-integral_I y
      <= 2 epsilon tan(a).

Consequently -integral f g >= 2Dk-4 epsilon tan(a)
>= 2Dk-8 epsilon a, using tan(a)<=2a. If a^2>=24 epsilon/D, this
is at least Dk. The energy inequality then yields
D^2 k^2 <= 8 Delta_W k, hence theta^3<=192 Delta_W/D^2.
If a^2<24 epsilon/D, then theta<sqrt(96 epsilon/D). The theta=0
case is immediate. Thus

    theta <= max(sqrt(96 epsilon/D), (192 Delta_W/D^2)^(1/3)).

For a canonical full source hull K, C-FS-GEOM gives
delta_K=pi D^2/4-area(K)<pi sqrt(3)D/4. A constant-width completion W
contains K, so Delta_W<=delta_K and the report's
Theta=max(sqrt(96 epsilon/D),(48 pi sqrt(3)/D)^(1/3)) is valid.
For completeness, such a completion exists: take a maximal compact convex
superset of K with diameter at most D. All candidates lie in a fixed
D-ball and chain unions have compact convex closures. If a boundary point
had no diametral partner, compactness would give a positive distance margin,
so a small outward displacement would enlarge the body without exceeding
D, contradicting maximality. The cited planar characterization then gives
constant width D.

### Common-ray upper box, normal-window deletion, and native box

For disjoint proper core owners G_i with assigned isolates, assume the
parent translations d_i=delta_i v_i preserve every old contact in every
binary selection, with directions in an oriented acute interval of width
w<pi/2. Assume each parent singleton satisfies every actual-diameter upper
constraint. If two moving owners had an old contact, the mixed difference
of its four squared lengths would be -2 d_i dot d_j<0, contradicting
preservation of all four lengths. Summed positive KKT equilibrium over a
proper core owner with a nonempty positive contact cut supplies an actual
crossing diameter edge z h_z. Indeed, for each crossing contact the exact
parent equality gives (x-y) dot v_i=-delta_i/2, for x in G_i intersect V
and y outside G_i.
Summing the core stationarity identity over U=G_i intersect V cancels
internal contact and diameter rows. The remaining contact resultant is
negative along v_i, equal to -delta_i/2 times the positive total multiplier
on the owner's contact cut. By stationarity it equals the remaining
diameter resultant. If no actual diameter crossed U, that resultant would
also vanish, a contradiction. Thus a crossing actual diameter exists.
Its loaded endpoint z lies in that owner, and singleton upper safety gives

    n_z dot v_i <= -delta_i/(2D),   n_z=(z-h_z)/D.

Require every upper-relevant label p in G_i, including assigned isolates,
to lie within R of some chosen such crossing endpoint z in the same owner.
Here upper-relevant means that some q outside G_i has |p-q|>=D-rho.
Assume R+rho<=D/10 and

    Phi=w/2+Theta+asin(R/(D-rho))+asin(rho/(2(D-rho))) < pi/2,
    epsilon=R+rho.

Discard an owner if any chosen anchor normal falls in either closed
half-width-Phi window around Jv or -Jv. For a retained anchor, the negative
projection on v_i and angle(v_i,v)<=w/2, together with removal of those
windows, imply n_z dot v < -sin(Phi).

For a moved label p and fixed external label q, put r=p-q. If
|r|<D-rho, a translation by rho v stays strictly below D by the triangle
inequality. Otherwise p is upper-relevant. Choose its same-owner anchor z.
Then |z-q|>=D-(R+rho), so the phase estimate bounds the angle between
z-q and z-h_z by Theta. Replacing z by p changes the ray direction by
at most asin(R/(D-rho)). The remaining angular margin gives

    r dot v / |r| < -rho/(2(D-rho)), hence r dot v < -rho/2.

Thus |r+rho v|^2=|r|^2+2rho r dot v+rho^2<|r|^2<=D^2.
This includes every full-source label and every near-D pair, whether
active or inactive. At each vertex of the independent-height box
Q_p=P_p+s_i v for 0<=s_i<=rho, moved/fixed pairs are strict; pairs
moving together or fixed together keep their old lengths. Squared distance
is convex in the heights, so the bound extends to the whole box and all
originally inactive upper pairs stay strict.

No actual diameter can join two retained owners: moving either endpoint
owner alone by rho v would give two squared-length changes whose sum is
2rho^2>0, although each vertex of the box is upper-safe. Hence each chosen
anchor diameter ends in the fixed group and is strictly shortened at every
positive height. Distinct retained owners have distinct anchor pairs, so
each active owner supplies a distinct removed diameter pair.

The deletion count follows from the canonical midpoint bound and hull
projection. In one normal window the loaded endpoint projections onto v
lie in an interval of width D sin(Phi)+2L_D, with L_D=7D^(2/3).
In hull order, intervening sides have projection increments at least
cos(Phi) times their length, and every side length is at least one.
Thus each window contains at most

    floor(1+(D sin(Phi)+2L_D)/cos(Phi)) = floor(F_D(Phi))

distinct loaded endpoints. Charge one bad anchor endpoint to each discarded
owner; owner disjointness makes these charges distinct. At most
2 floor(F_D(Phi)) owners are discarded. If R=o(D), rho=o(D), and w=o(1),
then Theta=o(1), Phi=o(1), and this deletion count is o(D).

When w<=pi/3, the same retained owners have a native-direction box
Q_p=P_p+s_i v_i. For a near-D pair with both endpoint owners moving, the
same anchor argument, with remaining margin Psi=Phi-w/2, gives the
single-owner estimate from both ends: r dot v_i < -rho/2 and
r dot v_j > rho/2. Since v_i dot v_j>=1/2, its squared-distance change
is

    2rho r dot(v_i-v_j)+rho^2|v_i-v_j|^2
      < -2rho^2+2rho^2(1-v_i dot v_j) < 0.

Pairs shorter than D-rho remain strictly below D since
rho|v_i-v_j|<=rho. One-owner pairs use the common singleton estimate;
within-owner pairs do not change. Convexity over the native height box
proves all upper constraints, including inactive pairs. This establishes
upper feasibility only; it does not establish simultaneous lower
feasibility.

### Global loaded-vertex proximity

In the full-core near-disk branch, let F=conv(V) contain the disk centered
at c of radius r_-=(1/2-eta)D, with 0<eta<1/4, and put
r_+=(1/2+eta)D. For any source point p and x in F,
|p-x|<=D by convexity from the full-source pair bounds. The opposite
point of the inner disk therefore gives |p-c|<=r_+. If p has a source
partner q with |p-q|>=D-rho, rho<r_-, then |q-c|<=r_+ gives
|p-c|>=r_--rho.

Intersect the ray from c through p with the boundary of F at x.
Its radius is in [r_-,r_+], while p's radius is in [r_--rho,r_+];
therefore |p-x|<=2eta D+rho. The point x lies on a loaded hull side
zz' (or is itself a loaded vertex). The side support distance h from c
is at least r_-, and z,z' lie in the outer disk, so

    |z-z'|<=2 sqrt(r_+^2-r_-^2)=2D sqrt(2eta).

Choosing the nearer endpoint proves
|p-z|<=D(2eta+sqrt(2eta))+rho. No source label was removed; p may be
a contact isolate outside F. In the canonical no-container branch eta=o(1),
so R_global=o(D) if rho=o(D). This estimate does not place z in p's owner
or guarantee an owner-crossing diameter.

### Type-II LDE bound

Take a supplied subfamily-stable Type-II O--O family under
C-OO-LOWER-BLOCKER-LOCALIZATION, satisfying Audit.106 for a fixed
1<t<sqrt(2): actual disjoint owners and canonical isolate assignments;
contact preservation under every binary selection; the small-cloud and
fixed-t outer lower-witness localization hypotheses; each counted singleton
passes all actual-diameter upper constraints, every unary strict-rhombus
test, and strictly shortens an old diameter pair. Assume also the same-owner
AS coverage above, with
R=o(D), w=o(1), rho=o(D), and max_i delta_i<=rho.

Here q=|B| is the number of actual diameter endpoints, b is the
occurrence-counted length of the old outer contact walk,
x_B=b-q, and m_B is the number of nonunit sides of the loaded hull.
Every noncontact lower witness that reaches equality or violation in a
counted singleton has old length at most t. Let r be the supplied family
size and k the size remaining after AS deletion.

Delete only the AS bad-anchor owners. Every retained original singleton is
in the native upper box at height delta_i<=rho, so all old upper constraints
hold, every old inactive upper pair remains strict, and its selected anchor
diameter strictly shortens. Contact, unary, isolate-assignment, small-cloud,
and lower-witness hypotheses persist by the stated subfamily stability.
Audit.106's Type-II conclusion applies to the retained family of size k:
k<=147(x_B+m_B). Adding back the deleted owners gives

    r <= 2 floor(F_D(Phi)) + 147(x_B+m_B).

There is no 2 d_H charge in this conditional statement. Since Phi=o(1),
the deleted term is o(D); thus x_B+m_B=o(D) implies r=o(D).
Audit.106 does not supply the family or the low-defect condition. The
canonical Audit.114 original-family estimate retains its 2d_H term when
the owner-local coverage hypothesis is absent.

## Adversarial and finite checks

I replayed the unchanged verifier with the provisioned Python 3.14.8
environment and its SymPy dependency, under the required shared compute
lock:

~~~sh
python3 research/verify_target_c_loaded_anchor_upper_box_2026_10_10.py \
  --diameters 300 500 1000 > /tmp/local10-pr952-replay.jsonl
cmp /tmp/local10-pr952-replay.jsonl research/certificates/target_c_loaded_anchor_upper_box_2026_10_10.jsonl
~~~

The rerun was byte-identical to the saved JSONL: nine fixture outputs and
744 complete pair-state checks. The localized seven-label fixture moves a
contact isolate with its owner and checks all 21 source pairs at each of
three heights. The six-label far-label regression checks all 15 pairs at
three heights: its parent height preserves contacts and strictly lowers
the old diameter, but the larger common release creates an upper violation
on a formerly inactive pair. In the report's notation that pair moves from
old squared length D^2-delta^2/4 to D^2+delta^2/2. This confirms why one
good anchor does not replace coverage of all upper-relevant labels.
The eight-label native-direction fixture checks all 28 pairs at five
states, including all four native-box vertices and a two-parent endpoint.
The three fixture counts per D are 63, 45, and 140; for D=300,500,1000
they total 744.

The candidate verifier uses exact SymPy equalities and directed rational
interval bounds from
verify_target_c_source_realized_owner_sink_2026_10_10.py (SHA-256
df2cd04d208b0370cb85b3c15a2cef308b11be2a942058c724473456ad85da25).
Its square-root enclosures use integer square roots at 120-bit scale; no
floating-point feasibility decision is used. These finite controls validate
the stated fixtures and regression, not the continuum phase-energy proof,
the general normal-window count, family extraction, low defect, or lower
closure.

## Limits and next lemma

I found no missing step in the three conditional implications under the
hypotheses stated here. The destination candidate remains unreviewed until
the maintainer records any lifecycle decision. This audit does not change
canonical status or theorem state.

The next exact source obligation is to derive, in a canonical C-II branch,
a linearly sized subfamily-stable O--O family with parent singleton tests
and owner-respecting crossing loaded anchors within R=o(D) of every
upper-relevant label, including assigned isolates. The global proximity
lemma supplies distance to some loaded vertex only. Even with that family,
one must establish x_B+m_B=o(D) or pay the high-defect case, and show the
strict lower-only closure retains a core owner. Until then no canonical
endpoint, universal minimizer result, C-II closure, or Level I consequence
follows.

## Provenance and AI disclosure

The source proof and verifier are credited to Slot 01 in legacy PR #952;
their pinned bytes were not edited. This audit was performed by the
independent Codex reviewer session local-10 (GPT-6 Luna xhigh), which did
not author or modify the candidate proof or checker. The mathematical
review and this text are AI-produced; no human mathematical review or
external validation is claimed. The new audit text is offered under the
repository's Apache-2.0 contribution terms. No third-party paper text or
private dependency was copied.
