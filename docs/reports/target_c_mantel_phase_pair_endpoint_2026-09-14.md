<!-- migration-source: path=docs/reports/target_c_mantel_phase_pair_endpoint_2026-09-14.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=9c7eb6cefb969430ea3daf332cc670826e7f6790; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — near-Mantel phase-pair exclusion at the full-core endpoint

Date: 2026-09-14

Status: unreviewed proof candidate. This report does not change theorem-state
authority and does not close Target C-II or Level I.

Target: Target C-II / full-core Type-II branch

Repository commit: ef941ab2b44aa393bdc461926769247b45754202

## LEVEL I STATUS

STILL OPEN

This report excludes a specific asymptotic endpoint of the full-core branch:
there is no canonical survivor sequence with

    mu_D -> mu_TC

where

    mu_TC=(2 pi+2 sqrt(Delta_2))/5,
    Delta_2=pi/(2 sqrt(3)).

The proof does not exclude sequences with normalized surplus bounded strictly
above this endpoint, and it does not address the macroscopic-container branch.

## 1. Candidate chain

The exact chain tested here is

    mu_D -> mu_TC
        -> train crossing graph is asymptotically Mantel-extremal
        -> a large two-label near-complete pair survives phase cleaning
        -> an almost-complete monotone two-arm path has length
           (sqrt(3)/2)(p+q)-o(D)
        -> D >= (3/4)sqrt(3 Delta_2)D-o(D) > D,
           a contradiction.

The new step is the near-complete two-label path lemma. It is a geometric
replacement for an unavailable complete-biclique extraction theorem.

All source points remain in the canonical source. The argument concerns the
actual local train segments of the strict-rhombus complex, not a separately
constructed scaffold.

## 2. Canonical endpoint data and notation

Work in a canonical full-core near-disk Type-II sequence, retaining the full
source and using the canonical phase cut. Let

    R_D = number of strict-rhombus faces,
    T_D = number of local train segments,
    G_D = train-crossing graph after the O(D) phase-cut deletions.

The canonical full-core cell and train ledgers give

    R_D/D^2 -> Delta_2,
    Delta_2=pi/(2 sqrt(3)),

and the occurrence-counted train boundary identity

    2 T_D = B_(4,D).

The canonical endpoint inequalities are

    T_D >= 2 sqrt(R_D),

    T_D/D <= (q-k)/D + 2 f/D + o(1),

where q is the loaded-hull vertex count, k=d_H+s_Z, and f is the number of
bounded nonquadrilateral contact faces. The canonical loaded-chord and
train-coupled surplus floor gives

    mu_D >= (2 pi + 2 sqrt(Delta_2))/5-o(1),

with

    mu_D=(e_BB+2s_C-3k)/D.

Suppose, for contradiction, that along a survivor sequence

    mu_D -> mu_TC=(2 pi+2 sqrt(Delta_2))/5.
    (2.1)

The exact loaded-chord identity and the canonical inequalities used in the
surplus-floor proof then force

    (q-k)/D -> mu_TC,

    f/D -> f_TC=(4 sqrt(Delta_2)-pi)/5,

    T_D/D -> tau_TC=2 sqrt(Delta_2).
    (2.2)

Here is the equality audit for (2.2). Put

    u_D=(q-k)/D,
    x_D=f/D,
    r_D=R_D/D^2,
    p_D=P_F/D.

The loaded-chord identity gives mu_D >= u_D-o(1). The two canonical
endpoint inequalities are

    u_D >= p_D/2+x_D/2,

    u_D >= 2 sqrt(r_D)-2x_D.

Their convex combination with weights 4/5 and 1/5 is

    u_D >= (2p_D+2 sqrt(r_D))/5.

Since p_D -> pi, r_D -> Delta_2, and the assumed limit in (2.1)
equals the right-hand limit, u_D -> mu_TC. The two nonnegative gaps in
the two displayed inequalities therefore both tend to zero. Subtracting
the two asymptotic equalities gives

    x_D -> (4 sqrt(Delta_2)-pi)/5.

Finally, the train boundary lower bound and the canonical train-interface
upper bound squeeze T_D/D between 2 sqrt(r_D) and u_D+2x_D+o(1),
which proves (2.2).

The phase cut deletes O(D) crossing faces, so

    |E(G_D)|=R_D-O(D).

Consequently (2.2) gives

    |E(G_D)|/T_D^2 -> 1/4.
    (2.3)

The graph G_D is simple and triangle-free by the canonical train theorem:
two local trains cross at most once, and three pairwise crossing trains are
impossible.

## 3. A finite Mantel stability calculation

We use the following elementary form of stability, with its proof included
to avoid importing a graph theorem.

### Lemma MP.1

Let G be a triangle-free graph on t vertices with

    e(G)=t^2/4-o(t^2).

Then there is a partition V(G)=X union Y such that

    |X|=t/2-o(t),
    |Y|=t/2-o(t),

and the number M of missing cross edges satisfies

    M=|X||Y|-e_G(X,Y)=o(t^2).
    (3.1)

### Proof

For every edge xy, triangle-freeness gives

    d(x)+d(y) <= t.

Summing over edges,

    sum_z d(z)^2 <= t e(G).

If e(G)=t^2/4-epsilon_t t^2 with epsilon_t -> 0, then

    sum_z (d(z)-t/2)^2 <= epsilon_t t^3.

Choose a vertex x with

    |d(x)-t/2| <= sqrt(epsilon_t)t.

Set X=N(x) and Y=V(G)\X. The set X is independent. Hence

    e_G(X,Y)=sum_{z in X} d(z).

Cauchy--Schwarz and the preceding degree-variance estimate give

    e_G(X,Y)=t^2/4+O(sqrt(epsilon_t)t^2).

Since |X|=t/2+o(t), |Y|=t/2+o(t), subtracting e_G(X,Y)
from e(G) proves (3.1). \(\square\)

Apply Lemma MP.1 to (2.3). Let ell be the canonical phase label in
Z/3Z, and write

    x_i=|X cap ell^{-1}(i)|,
    y_i=|Y cap ell^{-1}(i)|.

Every crossing has distinct phase labels. In particular, all x_i y_i
same-label cross pairs are missing, so

    x_i y_i <= M
    for i=0,1,2.                    (3.2)

### Lemma MP.2 — a large near-complete two-label pair

Under (3.1)--(3.2), there are distinct labels i,j and subsets

    A subseteq X cap ell^{-1}(i),
    B subseteq Y cap ell^{-1}(j)

before phase cleaning such that

    |A|+|B| >= 3t/4-o(t),

    |A|,|B| >= t/4-o(t),

and the bipartite crossing graph between A and B has o(t^2)
missing pairs.

### Proof

Put h=sqrt(M+1). Let I be the labels with x_i>h and J the labels
with y_i>h. Equation (3.2) implies I and J are disjoint. Since
the two sides each have t/2-o(t) vertices and h=o(t), both I and J
are nonempty.

If I has one label, that label contains t/2-o(t) vertices of X,
while one of the at most two labels in J contains t/4-o(t) vertices
of Y. If I has two labels, one of them contains t/4-o(t) vertices
of X, while J has one label containing t/2-o(t) vertices of Y.
In either case choose distinct i in I and j in J with

    x_i+y_j >= 3t/4-o(t),

and with both terms at least t/4-o(t). The only missing pairs in the
selected X--Y cross product are counted by M, so the selected pair has
o(t^2) missing edges. \(\square\)

The labels i and j may be interchanged. In what follows choose lifts so that
the crossing phase law has the form

    beta_b-alpha_a=L+delta_ab,
    L=pi/3,
    delta_ab>0
    for every actual A--B crossing.
    (3.3)

The missing pair count remains o(D^2), because T_D=Theta(D).

### Lemma MP.2A — phase inversions cost only o(D) trains

Let A and B be the two-label pair supplied by Lemma MP.2, with reduced
phases x_a and x_b in one interval of length L. Suppose M of the p q
pairs are noncrossings. Then one can delete o(D) members of A union B
so that every remaining pair satisfies

    x_a < x_b.
    (3.4)

Here p,q=Theta(D) and M=o(D^2).

#### Proof

Make a bipartite inversion graph with the original A and B trains as its
shores, joining a and b when x_a>=x_b. Such a pair cannot be an actual
crossing, because every actual crossing has delta_ab=x_b-x_a>0.
Consequently the inversion graph has at most M edges.

Its neighborhoods are nested after the A and B trains are sorted by phase.
If it has a matching of size r, sort the matched A endpoints and,
using the nested-neighborhood property, sort their matched B endpoints
so that

    x_(a_1)<=...<=x_(a_r),
    x_(b_1)<=...<=x_(b_r),
    x_(a_k)>=x_(b_k).

Then every pair a_k b_l with l<=k is an inversion, so the inversion
graph has at least r(r+1)/2 edges. Thus r<=sqrt(2M).

The finite bipartite vertex-cover theorem gives a vertex cover of the
inversion graph of size at most r: one proof starts from a maximum
matching, follows alternating paths from unmatched A vertices, and
takes the reachable B vertices together with the nonreachable A vertices.
Deleting this cover removes every inversion. Since M=o(D^2), its size
is o(D), proving (3.4). \(\square\)

## 4. Near-complete two-label path lemma

The next theorem is stated with the exact geometric hypotheses used. It is
not a statement about an arbitrary abstract near-complete bipartite graph.

### Theorem MP.3

Let A and B be two families of actual local train segments in one harmonic
cell, with

    p=|A|=Theta(D),
    q=|B|=Theta(D).

Assume:

1. trains in each family are pairwise noncrossing;
2. every A--B crossing is simple and has one common crossing sign;
3. after phase cleaning, all train directions have lifts alpha_a and beta_b
   satisfying
   \[
   \beta_b-\alpha_a=L+\delta_{ab},\qquad 0<\delta_{ab}<L
   \]
   whenever a and b cross, and every pair obeys
   \[
   \alpha_a<\beta_b;
   \]
4. the number M of missing A--B pairs is o(D^2);
5. the total phase defect over the actual A--B crossings satisfies
   \[
   \sum_{ab\ {\rm crossing}}\delta_{ab}\le C D
   \]
   for one fixed C.

Then the convex hull of the source rhombus centers contains two points at
distance at least

    (sqrt(3)/2)(p+q)-o(D).
    (4.1)

In particular, if the centers lie in a source of diameter D, then

    D >= (sqrt(3)/2)(p+q)-o(D).

### Proof

The proof has four finite parts.

#### 4.1 Common orders on high-degree reference neighborhoods

Choose a reference a-star in A with at most M/p missing B-neighbors, and
put B_0=N(a-star). Then |B_0|=q-o(D). Choose b-star in B_0 with
at most M/|B_0| missing A-neighbors, and put A_0=N(b-star).
Then |A_0|=p-o(D).

All trains in A_0 union B_0 are strictly monotone in one common linear
coordinate. Indeed, put

    alpha_+=max_{a in A_0} alpha_a,
    beta_-=min_{b in B_0} beta_b,
    psi=(alpha_++beta_-)/2,

and take the projection direction with argument psi. The inequalities

    L < beta_b-alpha_a < 2L

follow from the phase bin and the strict all-pair order alpha_a<beta_b.
The standard train-cone calculation therefore gives positive projection for
every elementary displacement of every selected train, including steps
whose other side belongs to a third phase label.

Order B_0 by its crossing order along the forward-oriented reference train
a-star. Order A_0 by its crossing order along the forward-oriented reference
train b-star. The following elementary order fact will be used:

    if two A trains both cross two B trains, their relative B crossing
    order is the same on both A trains; and symmetrically.
    (4.2)

To prove (4.2), take the two B graphs as X-monotone disjoint graphs. If
their X-domains are disjoint, their left-right interval order fixes every
crossing order. If their domains overlap, their vertical order on the
overlap is fixed. A common-sign crossing changes an A graph from below the
first B graph to above it, so the opposite crossing order would force
the impossible chain

    A(X_0)>B_1(X_0)>B_2(X_0)>A(X_0)

at a point X_0 in the common domain. This proves the first assertion;
interchanging A and B proves the second.

Thus every A train sees its B_0 neighbors in the B_0 reference order,
and every B train sees its A_0 neighbors in the A_0 reference order.

#### 4.2 A low-defect edge near the two order corners

Let S be the sum of delta_ab over the A_0--B_0 crossings, so S<=CD.
Call an A_0 train bad if it has more than sqrt(M+1) missing B_0-neighbors
or if its incident phase-defect sum exceeds sqrt(D). The number of bad
A_0 trains is o(D). The same is true for B_0 trains.

Set

    eta_D=D^(-1/4)+(M/D^2)^(1/4),

which tends to zero and satisfies D/eta_D=o(D^2). Let r_D be the sum
of the two bad-vertex counts plus

    ceil(sqrt(M+CD/eta_D))+2.

Then r_D=o(D). Consider the first r_D A_0 trains in the A_0 order
and the last r_D B_0 trains in the B_0 order. After removing bad
trains, each prefix/suffix still has more than

    sqrt(M+CD/eta_D)

members. If every pair in the resulting rectangle were missing, there
would be more than M missing pairs. Therefore it contains actual
crossings. If every such crossing had delta_ab>eta_D, their total defect
would exceed CD, also impossible. Hence there is an actual crossing

    a_0 b_1

with a_0 among the first r_D A_0 trains, b_1 among the last r_D B_0
trains, both trains good, and

    delta_(a_0 b_1)<=eta_D=o(1).
    (4.3)

#### 4.3 The monotone two-arm path

Let alpha_+=max alpha_a and beta_-=min beta_b over A_0 and B_0, and
write

    g=beta_--alpha_+-L>0,
    r_a=alpha_+-alpha_a>=0,
    q_b=beta_b-beta_->=0.

For every crossing in A_0 x B_0,

    delta_ab=g+r_a+q_b.
    (4.4)

The common projection direction is still psi=(alpha_++beta_-)/2.
For a vector v_b in the forward displacement direction of an A train,

    e dot v_b
      = cos(L/2+g/2+q_b)
      >= sqrt(3)/2-g/2-q_b.
    (4.5)

For a vector u_a in the forward displacement direction of a B train,

    e dot u_a
      >= sqrt(3)/2-g/2-r_a.
    (4.6)

These use only the one-Lipschitz bound for cosine and the strict phase
interval; all relevant angular differences lie below 3L/2.

Because a_0 is in the first r_D A_0 positions and b_1 is in the last
r_D B_0 positions, and because both rows/columns are good, a_0 has

    q-o(D)

neighbors from B_0 before b_1 in the B_0 order, while b_1 has

    p-o(D)

neighbors from A_0 after a_0 in the A_0 order. The common-order fact
(4.2) makes these statements valid on the actual trains a_0 and b_1.
The sum of the q_b errors on the first set is at most sqrt(D), because

    sum delta_(a_0 b) <= sqrt(D).

The sum of the r_a errors on the second set is likewise at most sqrt(D).
Equation (4.4) also pays the g term within those same row and column
defect sums.

Start at the first B_0 crossing on a_0 before b_1, follow a_0 forward
to the crossing a_0 b_1, and then follow b_1 forward through its
A_0 crossings after a_0. The intermediate centerline steps not listed
above have nonnegative projection by the common train-cone calculation.
The standard endpoint half-step accounting for train centers loses at most
one unit on each arm. Therefore the two endpoint centers z_-,z_+ obey

    e dot(z_+-z_-)
      >= (sqrt(3)/2)(p+q-o(D))-2-o(D).

Both centers are averages of source points from their rhombi, hence lie in
the convex hull of the full source. Its diameter is D, so

    D >= |z_+-z_-|
      >= e dot(z_+-z_-)
      >= (sqrt(3)/2)(p+q)-o(D).

This proves (4.1). \(\square\)

The proof is finite at each D. The only asymptotic inputs are M=o(D^2),
p,q=Theta(D), and the stated O(D) phase-defect bound. No complete biclique
is asserted.

## 5. Exclusion of the exact full-core floor

Apply Lemma MP.2 to the Mantel partition of G_D. It gives a pair of labels
with

    p+q >= 3T_D/4-o(D),

and p,q>=T_D/4-o(D). Apply Lemma MP.2A and delete its o(D) phase-inversion
vertex cover. The pair still satisfies the hypotheses of Theorem MP.3:
the missing crossing count is o(D^2), and the phase-defect sum is at most
the canonical global O(D) defect budget.

Using T_D/D -> 2 sqrt(Delta_2), Theorem MP.3 yields

    D >= (sqrt(3)/2)(3T_D/4-o(D))-o(D)

and hence

    1 >= (3/4)sqrt(3 Delta_2)
    in the limit.
    (5.1)

But

    (3/4)sqrt(3 Delta_2)
      = (3/4)sqrt(pi sqrt(3)/2)
      = 1.2370906246...
      > 1.

The strict inequality is exact: it is equivalent to

    Delta_2>16/27,

which follows from

    Delta_2=pi/(2sqrt(3))>3/4>16/27.

This contradiction proves:

### Endpoint exclusion

There is no unbounded canonical full-core Type-II survivor sequence for
which

    mu_D -> mu_TC.
    (5.2)

Equivalently, the canonical train-coupled floor cannot be approached as an
equality endpoint by triangle-free global-minimizer representatives.

If the canonical full-core hypotheses are uniform over survivor sequences,
(5.2) also gives an existential positive separation from the floor: otherwise
a sequence with mu_D-mu_TC -> 0 would contradict (5.2). This separation is
not quantified here and does not eliminate the higher-surplus branch.

## 6. Exact remaining obstruction

The endpoint exclusion changes the full-core alternatives only as follows:

    mu_D >= mu_TC
        and mu_D cannot accumulate at mu_TC
        -> any surviving full-core sequence must remain in a higher-surplus
           branch.

The missing implication is still one of:

1. a higher-surplus upper bound on the aggregate outer-walk detour
   sum_r(L_r-2d_r);
2. a source-preserving finite deformation using the higher surplus;
3. an exact unit equilateral triangle forced by the loaded/train geometry; or
4. a theorem covering all higher-surplus full-core limits.

The macroscopic-container branch is untouched. In particular, the strict
fixed-container augmentations and the protected-capacity regression in the
companion chamber report do not provide a source-preserving exchange.

## 7. Scope and adversarial audit

The following conventions are load-bearing:

- G_D is the actual train-crossing graph after the canonical O(D) phase cut;
  no abstract crossing network is identified with the source without the
  center-of-rhombus endpoint argument.
- Same-label train pairs are noncrossing because every actual rhombus crossing
  has distinct labels; the train theorem supplies at-most-one crossing.
- The phase-inversion deletion removes only o(D) trains. It does not delete
  source points; it selects a train subfamily.
- Missing edges are counted in the selected two-label cross product, while
  the phase-defect sum is over actual selected crossings. They are not
  silently replaced by a complete graph.
- The common order is established only on high-degree reference
  neighborhoods, which is all the path requires. No global order for every
  train is asserted.
- Steps involving a third phase label are not discarded: the common projection
  cone gives them nonnegative projection.
- Every endpoint used in the diameter comparison is a rhombus center, hence
  a convex combination of actual source points. The source diameter, not a
  scaffold diameter, is used.
- Contact-isolated source points are retained in the source and are irrelevant
  only because this full-core train argument uses actual rhombus centers.

Binding regressions remain compatible:

- an abstract near-complete bipartite graph may have no linear complete
  biclique; Theorem MP.3 uses actual monotone train geometry instead;
- the five-sector C5 blow-up is triangle-free but has crossing density
  1/5 rather than the Mantel endpoint density 1/4, so it does not refute
  the endpoint calculation;
- vanishing-shear oblique lattices have no global-minimizer certificate and
  do not meet the near-Mantel endpoint conclusion for an actual full-core
  sequence;
- bridges, repeated train endpoints, and phase-cut boundary occurrences
  are handled by occurrence-counted train identities;
- no KKT coefficient lower bound, affine-kernel extension, or finite stress
  integration is used.

The main possible failure point is the geometric premise that a noncrossing
same-label pair of local trains cannot meet away from an actual rhombus.
That premise is part of the canonical train-crossing construction; if a
different train convention permits such meetings, MP.3 must be restricted
to the noncrossing subfamily supplied by that convention.

## 8. Literature and computation

No external mathematical theorem is imported. Lemma MP.1 and the label
extraction are proved here. The train cone, phase law, train boundary identity,
and source-center containment are canonical repository inputs with their
stated hypotheses.

No computation is logically required. The exact endpoint constants are:

    Delta_2 = 0.9068996821171089...
    T_D/D at the endpoint = 1.9046256137279147...
    (3/4)sqrt(3 Delta_2) = 1.2370906246401763...

The final sign has a margin of approximately 0.23709 in the normalized
diameter inequality. Floating-point values are orientation checks only; the
strict sign follows from Delta_2>16/27.

## 9. Claim ledger

| Claim | Classification | Exact status |
| --- | --- | --- |
| Mantel stability Lemma MP.1 | proved candidate | finite proof in §3 |
| Large two-label pair Lemma MP.2 | proved candidate | finite label counting |
| Near-complete two-arm Theorem MP.3 | proved candidate | finite geometric proof under stated train hypotheses |
| No sequence with mu_D -> mu_TC | proved candidate | follows from canonical endpoint inputs and MP.1--MP.3 |
| Uniform positive gap from mu_TC | conditional on uniform canonical family formulation | not quantified here |
| Exclusion of all higher-surplus full-core branches | unresolved | exact detour/deformation/triangle bridge missing |
| Exclusion of macroscopic containers | unresolved | collective protected exchange missing |
| Level I | open | original quantifiers not discharged |

## 10. Promotion and handoff

The artifact is unreviewed and noncanonical. It should not be used as a theorem
premise until an independent audit checks the local train order convention and
the phase-cleaning deletion in the actual canonical train complex.

If audited successfully, the endpoint exclusion advances the canonical
full-core floor by removing equality accumulation, but it does not change the
route's final obligation. The next serious target is a uniform higher-surplus
detour/deformation theorem or a source-level closure of the macroscopic
container branch.
