<!-- migration-source: path=docs/reports/target_c_interface_budget_collective_chamber_2026-09-14.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=3066c4af3bdd31321f6bd68568ddb8eff3f5aa8c; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Target C-II interface budget and collective-chamber regressions

Date: 2026-09-14

Status: unreviewed candidate report. This report does not change theorem-state
authority and does not close Target C-II or Level I.

## Scope and canonical hypotheses

This note records three exact results obtained while testing the remaining
Target C-II branches.

The first result applies in the canonical full-core, no-macroscopic-container,
near-disk Type-II regime. The source is the full source configuration, while
the attachment cells below are the actual convex hulls of the source subsets
assigned to the loaded carrier cells. The canonical facts used are:

* the normalized loaded carrier has diameter scale D, with P_F/D -> pi;
* the actual attachment cells P_r have pairwise disjoint interiors;
* sum_r area(P_r) = pi D^2/4 - o(D^2);
* sum_r sqrt(area(P_r)) = O(D);
* in this branch every loaded-loaded unit chord is a hull side, so c_B=0;
* contact-isolated source points are retained in the source, and the canonical
  de-atomization bound gives c_I=o(D);
* the canonical Section-62 attachment-perimeter inequality is
  sum_r per(P_r) <= pi(2+2q-e_BB-k).

Here q is the number of loaded carrier vertices, e_BB is the number of
loaded-loaded carrier edges, k=d_H+s_Z, and c_I is the canonical
interior-contact count. The full-core scalar is

    mu_D = (e_BB + 2 s_C - 3 k)/D.

The second result is a finite fixed-container regression. It constructs a
unit-separated, triangle-free set with one more point than the usual strict
triangular-lattice filling of an axial hexagon. It is deliberately not a
global-minimizer statement.

## 1. The signed attachment-interface budget

Define

    I_D = (1/2)(sum_r per(P_r) - P_F).

This is a signed quantity: it measures the total attachment perimeter in excess
of the loaded carrier perimeter, with the factor one half matching the
two-sided interface convention. No assertion that it is nonnegative for every
finite representative is made.

### Proposition IB.1

Under the full-core hypotheses above,

    liminf_{D -> infinity} I_D/D >= 0.

Moreover, if along a sequence mu_D -> mu, then

    limsup_{D -> infinity} I_D/D <= (pi/2)(mu - 1).

Consequently, along any sequence attaining the canonical train/loaded-chord
floor, meaning mu_D -> mu_TC,

    mu_TC = (2 pi + 2 sqrt(pi/(2 sqrt(3))))/5

one has the explicit upper budget

    limsup I_D/D <= iota_TC,

where

    iota_TC = (pi/2)(mu_TC - 1)
             = 1.001480337015631909...

#### Proof

For every planar convex body of area a, the isoperimetric inequality gives

    per(P_r) >= 2 sqrt(pi a).

Therefore Cauchy--Schwarz and the cell-area saturation imply

    sum_r per(P_r)
      >= 2 sqrt(pi) sum_r sqrt(area(P_r))
      >= 2 sqrt(pi) sqrt(sum_r area(P_r))
      = pi D - o(D).

Since P_F/D -> pi, this gives I_D/D >= -o(1), and hence the liminf statement
claimed.

In the near-disk full-core branch, the exact scalar identity and c_B=0 give

    2 + 2q - e_BB - k = mu_D D + 2 c_I + 6.

The Section-62 inequality hence becomes

    sum_r per(P_r) <= pi(mu_D D + 2 c_I + 6).

Because c_I=o(D) and P_F/D -> pi, division by 2D gives

    limsup I_D/D <= (pi/2)(mu - 1).

Substitution of the displayed value of mu_TC gives the stated decimal. All
limits are along the specified full-core sequence; this proposition does not
make a uniform finite assertion for arbitrary representatives.

### Why this does not close the detour obstruction

The lower bound is only the ordinary isoperimetric lower bound. It does not
control the aggregate outer-walk detour

    sum_r (L_r - 2 d_r),

which is the residual source-level quantity in the canonical Sections 122--123
frontier. In particular, even a sharp bound on I_D would need an additional
theorem converting interface excess, detour, or non-rhombic area into either an
exact unit equilateral triangle or a finite source-preserving strict decrease
of the global diameter.

The elementary two-half-disk partition shows why convex-cell perimeter alone
cannot supply that bridge. Partition a disk of diameter D by a diameter into
two half-disks. Their total perimeter is pi D + 2D, while the carrier perimeter
is pi D; thus I_D=D. This has the same linear scale as the iota_TC D budget and
contains no contact-graph or global-minimality information. The example is a
geometric calibration, not a unit-separated source configuration.

## 2. A collective fixed-container chamber regression

Let

    u_0 = (1,0),  v_0 = (1/2, sqrt(3)/2),

and let

    C_R = {x u_0 + y v_0 : |x| <= R, |y| <= R,
           |x+y| <= R}.

Write

    H_(R-1) = {(i,j) in Z^2 : |i| <= R-1, |j| <= R-1,
               |i+j| <= R-1}.

The strict triangular-lattice filling used in the existing chamber regression
is

    Z_R = (1+R^(-2)) {i u_0 + j v_0 : (i,j) in H_(R-1)}.

It has 3R^2 - 3R + 1 points. The following construction adds one point while
preserving unit separation and triangle-freeness.

### Proposition CR.1

For every integer R >= 8, set

    delta_R = 1/(100 R^2),

    u_R = u_0,

    v_R = (cos(pi/3 + delta_R), sin(pi/3 + delta_R)),

and define

    Y_R = {i u_R + j v_R : (i,j) in H_(R-1) union {(R,0)}}.

Then:

1. Y_R is contained in C_R;
2. |Y_R| = 3R^2 - 3R + 2;
3. all distinct points of Y_R are at distance at least one;
4. the unit-distance graph of Y_R consists only of the two basis directions
   u_R and v_R, and is bipartite; in particular Y_R contains no unit
   equilateral triangle.

#### Proof

Put theta=pi/3+delta_R. Relative to the original axial basis,

    v_R = alpha_R u_0 + beta_R v_0,

where

    alpha_R = cos(theta) - sin(theta)/sqrt(3),
    beta_R  = 2 sin(theta)/sqrt(3).

For 0 < delta_R <= 1/6400, elementary trigonometric estimates give

    |alpha_R| <= 2 delta_R,
    0 < beta_R - 1 <= delta_R,
    |alpha_R + beta_R - 1| <= delta_R.

For (i,j) in H_(R-1), the three axial coordinates of i u_R + j v_R are

    i + alpha_R j,  beta_R j,  i + (alpha_R+beta_R)j.

The defining inequalities for H_(R-1), together with the three coefficient
bounds, show that these coordinates have absolute value at most
R-1+2 delta_R (R-1) < R for R >= 8. The added point is R u_0, which lies on
the boundary of C_R. Thus Y_R is contained in C_R. The cardinality is
immediate because (R,0) is not in H_(R-1).

For a difference of two points, write the difference in the oblique basis as
a u_R + b v_R with integers a,b, not both zero. Its squared length is

    Q(a,b) = a^2 + b^2 + 2 cos(theta) a b.

Since 0 < cos(theta) < 1/2, if ab >= 0 and both coordinates are nonzero, then
Q(a,b)>1; equality occurs only for a coordinate-axis difference of absolute
value one. If ab<0, put A=|a| and B=|b|. Then

    Q(a,b) = (A-B)^2 + 2 A B (1-cos(theta)).

If A != B, the first term is at least one and the second is positive. If
A=B, then A=B=1 gives Q=2(1-cos(theta))>1 because cos(theta)<1/2, and
larger A only increases the value. Hence every distinct pair is separated by
more than one except for differences +u_R, -u_R, +v_R, and -v_R, which have
length exactly one.

The unit graph therefore consists of edges joining lattice indices differing
by (1,0) or (0,1). The parity of i+j changes on every such edge, so the graph
is bipartite and has no odd cycle. A unit equilateral triangle would be an odd
3-cycle, so none exists.

## 2A. A strict contact-free one-point chamber augmentation

The fixed-container regression can be strengthened. The previous Proposition
CR.1 used basis vectors of length one and therefore had basis-direction unit
contacts. A simultaneous scale and angle perturbation removes those contacts
while still allowing one extra point.

### Proposition CR.2

For every even integer R >= 8, put

    delta_R = 1/R^2,
    s_R = 1 + delta_R/10,
    theta_R = pi/3 + delta_R,

and define

    u_R = s_R(1,0),
    v_R = s_R(cos(theta_R), sin(theta_R)).

With C_R and H_(R-1) as above, set

    Y_R^strict
      = {i u_R + j v_R : (i,j) in H_(R-1)
          union {(R/2,R/2)}}.

Then Y_R^strict is contained in C_R, has

    |Y_R^strict| = 3R^2 - 3R + 2,

and every two distinct points have distance strictly greater than one.
Consequently its unit-distance graph is empty and it contains no unit
equilateral triangle.

#### Proof

Write theta=theta_R and delta=delta_R. Relative to the original axial basis,

    v_R = s_R(alpha u_0 + beta v_0),

where

    alpha = cos(theta) - sin(theta)/sqrt(3),
    beta  = 2 sin(theta)/sqrt(3),
    gamma = alpha + beta - 1.

For 0 < delta <= 1/64, elementary trigonometric estimates give

    |alpha| <= 2 delta,
    1 < beta <= 1 + delta,
    -delta <= gamma <= -delta/2.

For an index (i,j) in H_(R-1), the three axial coordinates of
iu_R+jv_R are

    s_R(i+alpha j),  s_R beta j,  s_R(i+(alpha+beta)j).

Their absolute values are at most

    s_R(R-1)(1+2 delta) < R

for R >= 8. For the added index (R/2,R/2), the first two coordinates have
absolute value less than R because

    s_R(1+2 delta)/2 < 1

and the third coordinate is

    s_R R(1+gamma/2)
    <= s_R R(1-delta/4)
    < R.

Thus every point lies in C_R. The added index has axial norm R and is not in
H_(R-1), so the cardinality is 3R^2-3R+2.

For a nonzero integer difference (a,b), the squared distance divided by
s_R^2 is

    a^2+b^2+2 cos(theta)ab.

Here 0<cos(theta)<1/2. If ab>=0, this expression is at least one, with
equality only for a coordinate-axis difference of absolute value one. If
ab<0, writing A=|a| and B=|b| gives

    (A-B)^2+2AB(1-cos(theta)) > 1.

Therefore the unscaled oblique lattice has squared minimum distance one,
and multiplication by s_R>1 makes every nonzero lattice difference strictly
longer than one. This proves strict separation and the empty unit graph.

## 2B. The protected chamber pays a linear capacity loss

The preceding construction gains one point only by using the boundary room of
the full chamber. The next proposition quantifies the cost of the one-unit
protection required by a source-preserving internal-chamber exchange.

### Proposition CR.3

Let

    C_R = {x u_0 + y v_0 : |x| <= R, |y| <= R, |x+y| <= R}

with \(u_0=(1,0)\), \(v_0=(1/2,\sqrt3/2)\), and let

    C_R^(-1) = {x in C_R : dist(x,partial C_R) >= 1}.

For \(R>2/\sqrt3\),

    C_R^(-1)=C_(R-2/sqrt(3)).

Every unit-separated set \(W\subseteq C_R^{(-1)}\) satisfies

    |W| <= 3R^2 + (3-4sqrt(3))R + 5 - 2sqrt(3).

In particular, for the even integers \(R\ge8\), the strict contact-free
augmentation \(Y_R^strict\) of Proposition CR.2 obeys

    |Y_R^strict| - |W|
      >= (4sqrt(3)-6)R + 2sqrt(3)-3

for every unit-separated \(W\subseteq C_R^{(-1)}\). The right-hand side is
positive and linear in \(R\).

#### Proof

The six sides of \(C_R\) have inward normal distance \(a_0R\) from the
center, where \(a_0=\sqrt3/2\). Moving every supporting line inward by one
therefore changes the axial radius from \(R\) to

    R - 1/a_0 = R - 2/sqrt(3).

Their intersection is exactly the inner parallel body \(C_R^{(-1)}\).

The area and perimeter of the regular axial hexagon \(C_t\) are

    area(C_t)=3a_0 t^2,
    per(C_t)=6t.

Applying the planar Oler inequality to a unit-separated set \(W\) in
\(C_t\) gives

    a_0|W| <= area(C_t) + (sqrt(3)/4) per(C_t) + a_0
           = a_0(3t^2+3t+1).

Thus \(|W|\le3t^2+3t+1\). Substituting
\(t=R-2/\sqrt3\) gives

    |W| <= 3R^2 + (3-4sqrt(3))R + 5 - 2sqrt(3).

Proposition CR.2 gives
\(|Y_R^strict|=3R^2-3R+2\). Subtracting the preceding upper bound yields
the displayed difference. \(\square\)

## 3. A linear-perimeter, quadratic-area empty-face regression

It is tempting to combine the global boundary-scale area deficit with the
Section-62 estimate that total attachment perimeter is O(D), and infer that
every local non-rhombic or empty region has only O(D) area. That inference is
false.

### Proposition EF.1

For every even integer m >= 8, let E_m be the regular m-gon with side length
one, and let X_m be its vertex set. Then X_m is unit-separated, its
unit-distance graph is exactly the cycle C_m, and

    per(E_m) = m,
    diam(E_m) = d_m = csc(pi/m),
    area(E_m) = m/(4 tan(pi/m)).

Moreover,

    per(E_m)/d_m -> pi,
    area(E_m)/d_m^2 -> pi/4.

Thus a triangle-free unit-edge face can have linear perimeter and quadratic
area, with the same leading area-to-diameter ratio as a disk.

#### Proof

The distance between vertices separated by k cyclic steps is

    sin(k pi/m)/sin(pi/m),    1 <= k <= m/2.

It equals one for k=1 and is strictly greater than one for
2 <= k <= m/2. Hence the only unit contacts are consecutive sides, and the
unit graph is C_m, which is triangle-free. For even m, opposite vertices
realize the diameter, so d_m=1/sin(pi/m). The regular-polygon area formula is
area(E_m)=m/(4 tan(pi/m)). Therefore

    m/d_m = m sin(pi/m) -> pi

and

    area(E_m)/d_m^2 = (m/8) sin(2 pi/m) -> pi/4.

This proves the proposition.

Viewed as a contact complex, E_m has one bounded nonquadrilateral face with
degree excess Q=m-4 and exceptional perimeter currency
P_exc=4+(m-4)=m. Its empty interior has area asymptotic to pi d_m^2/4.
Consequently P_exc=O(D), or a global O(D) convex-hull area deficit, does not
imply an O(D) bound on area(P_r)-A_(4,r). The canonical Type-II hypothesis
A_4=area(F)-o(D^2) excludes an Omega(D^2) empty face in that branch, but
does not upgrade the error to O(D). Such an upgrade requires an additional
source-level theorem controlling macroscopic empty faces or converting their
area into strict global descent. This is a contact-complex regression, not a
claimed global minimizer.

## 4. Exact status of these results

Proposition IB.1 is a proved candidate awaiting promotion only if repository
maintainers accept its dependence on the already canonical full-core cell and
perimeter statements. It is an interface-budget bound, not a closure.

Proposition CR.1 is an exact fixed-container regression. Together with the
strict contact-free filling Z_R, it shows that quadratic chamber populations
and one-point larger feasible fillings can both occur without a unit
equilateral triangle. The new filling has basis-direction unit contacts, but
its contact graph is bipartite. It does not compare the chamber construction
with D(n), does not place it as a source inside a global minimizer, and does not
provide a source-preserving diameter-reducing deformation.

Proposition CR.2 is stronger: it is a strict contact-free filling with one
more point than Z_R in the same fixed container. It still does not assert any
compatibility with retained source points outside the chamber or any global
optimality property.

Proposition EF.1 is an exact finite empty-face regression. It is not a
full-core Type-II survivor because its quadratic interior is empty, but that is
precisely the missing hypothesis in an attempted O(D) local-defect upgrade.

Thus the live exact implications remain:

    aggregate detour / interface data
        -> ? source-preserving global descent or exact unit triangle,

and

    macroscopic inactive chamber or exterior cap
        -> ? contact/core-coupled global descent or exact unit triangle.

Neither arrow has been proved here.

## 5. Regressions checked against these claims

The following existing exact regressions remain compatible and were not used as
premises: the scalar full-core witness; the strict saturated triangular chamber;
the two-geodesic central-face corridor; the sheared triangular lattice with
linear outer detour; the square-grid harmonic attachment complex; and the
one-sided exterior-cap exchange theorem with its unresolved low-slack case.
They respectively block scalar-only closure, local near-geodesic closure, local
detour upper bounds, and unqualified contact-creation arguments.

The contact-isolated-point correction is respected throughout: Proposition
IB.1 uses the canonical c_I=o(D) estimate but never deletes isolated source
coordinates from the source. Proposition CR.1 is a standalone fixed-container
set and is not silently promoted to a source/scaffold co-embedding.

No imported mathematical theorem is needed beyond the elementary planar
isoperimetric inequality and Cauchy--Schwarz. The official Erdős Problems entry
remains the external status reference for Problem 99; it is not used as evidence
for any geometric step.
