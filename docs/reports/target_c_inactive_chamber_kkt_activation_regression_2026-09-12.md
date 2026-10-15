<!-- theorem-state: {"artifact_id":"ART-F06D29047A37","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — KKT-realizable inactive-chamber activation regression

**Date:** 2026-09-12  
**Repository branch:** research/c2-closure-sol-20260912-r1  
**State version:** 2026-09-12.audit.44  
**Run type:** hostile regression / macroscopic inactive-container branch  
**Target:** C-II  
**Computation:** research/verify_target_c_inactive_chamber_kkt_activation_regression.py

## STATUS

REGRESSION — PROVED FINITE FAMILY, NONCANONICAL

This note gives a stronger inactive-chamber regression. A macroscopic chamber is
co-embedded with a square unit-contact frame whose two diagonal diameter pairs
support an explicit positive KKT multiplier system. The chamber population is a
near-capacity rhombic lattice with angle pi/3+O(1/M), hence only O(M) isolate-only
Oler slack.

The chamber points can be collapsed continuously from a strict scaled lattice to
an exact-contact rhombic grid. The homotopy remains unit-separated, the frame
diameter remains fixed, and the terminal contact graph remains bipartite. Thus
first-order KKT stationarity, collective exact-contact activation, and the current
chamber capacity/matching statistics still do not force a unit equilateral triangle.

The family is not a global minimum-diameter source. It does not disprove Erdős
Problem #99 and does not close C-II. It eliminates a local closure route and
isolates the missing use of global optimality.

## 1. Rational near-triangular lattice

For an integer M>=8 define

    a_M=floor(M/sqrt(3))+1,  t_M=a_M/M,
    c_M=(1-t_M^2)/(1+t_M^2),
    r_M=2t_M/(1+t_M^2).

The vectors u=(1,0) and v=(c_M,r_M) are unit vectors with rational coordinates.
Since t_M>1/sqrt(3),

    0<c_M<1/2,
    pi/3<angle(u,v)<pi/2,
    angle(u,v)-pi/3=O(1/M).

For an integer lattice difference (p,q), the squared length is

    Q_M(p,q)=p^2+2c_M p q+q^2.

Because c_M<1/2, the only nonzero integer differences with Q_M(p,q)=1 are
the four generator differences (plus or minus one,0) and (0,plus or minus one).
For opposite signs the shortest mixed difference has squared length
2-2c_M>1; all other mixed differences are longer. Every finite patch therefore
has a bipartite unit-contact graph and contains no unit equilateral triangle.

## 2. Square frame and near-capacity inactive chamber

Use ordinary Cartesian coordinates for

    B_M={(i,j) in Z^2: 0<=i,j<=M and
         (i=0 or i=M or j=0 or j=M)}.

This is the boundary cycle of the square [0,M]^2. It has 4M vertices and 4M
unit edges. Its two diagonal pairs are the only diameter pairs, and

    D_M=M sqrt(2).

Let I_M^0 be all points iu+jv whose Cartesian coordinates lie in
the square [3,M-3]^2. A fundamental-parallelogram boundary-strip count gives

    |I_M^0|=M^2/sin(angle(u,v))+O(M).

Since sin(angle(u,v))=sqrt(3)/2+O(1/M), this is a quadratic population at
asymptotically maximal planar packing density.

Let o_M=(M/2,M/2), q_M=1+1/M, and define

    I_M^+={o_M+q_M(p-o_M): p in I_M^0}.

Every point of I_M^+ lies strictly more than 5/2 from each supporting line of
the square, and therefore more than one unit from every frame point. Every
initial inner-inner distance is q_M times a nonzero lattice distance. Hence

    A_M^+=B_M union I_M^+

is unit-separated and the points of I_M^+ are genuinely contact-isolated.
The bounded face inside the frame contains Omega(M^2) such points.

The isolate-only Oler slack of the square chamber is

    M^2/(sqrt(3)/2)+2M+1-|I_M^+|=O(M).

For completeness, the estimate follows from the lattice count above and
sin(angle(u,v))=sqrt(3)/2+O(1/M). The ratio of the lattice cell area to
sqrt(3)/2 differs from one by O(1/M), and the square boundary contributes O(M).
The lower bound is finite Oler; the verifier checks the conservative upper bound
80M at the tested scales.

## 3. Deep near-unit matching

For every horizontal lattice neighbor p,p+u in I_M^0, the corresponding initial
points have distance exactly q_M=1+1/M. Alternating these neighbors row by row
gives Omega(M^2) vertex-disjoint pairs. Their points stay in a fixed-width
interior square, uniformly separated from the frame. This realizes the same
quadratic deep near-unit matching used by the canonical Type-I branch.

## 4. Positive KKT certificate

Use the Lagrangian with unit-separation constraints 1-|x_i-x_j| and diameter
constraints |x_i-x_j|-D. Give every frame unit edge multiplier

    gamma=1/(2 sqrt(2)),

and give each of the two diagonal diameter pairs multiplier h=1/2. Give all
chamber constraints multiplier zero, including the exact inner contacts at the
terminal time.

At a non-corner frame vertex the two unit-edge derivatives cancel. At a corner,
the two unit contacts contribute an outward diagonal vector with coefficient
gamma. The opposite diameter pair contributes the inward diagonal vector with
coefficient h/sqrt(2)=gamma. Position stationarity therefore holds at every
frame vertex. Diameter stationarity is

    1-2h=0.

The inner points have zero multiplier balance because they form an interior
component separated from the frame. The same certificate applies before and
after the homotopy, with the terminal contacts entering the active set at zero
weight. This is a first-order stationary feasible family, not a local or global
minimum claim.

## 5. Collective collapse to exact contacts

For 0<=t<=1 move all chamber points by

    I_M(t)={o_M+q_t(p-o_M): p in I_M^0},
    q_t=1+(1-t)/M.

The initial source is A_M^+ and the terminal source is A_M^0=B_M union I_M^0.
Inner-inner distances are at least one throughout because q_t>=1 and the
unscaled lattice has minimum distance one. The inner points remain in
[5/2,M-5/2]^2, so their distance to the frame is greater than one.

At t=1 the inner population has the exact-contact rhombic-grid graph generated
by u and v. This graph is bipartite under the parity of lattice indices. The
frame is a cycle and there are no frame-to-grid contacts. Consequently the
terminal contact graph is triangle-free.

The frame is fixed. Its diagonal diameter pairs remain present, and all inner
points remain inside the square, so

    diam(A_M(t))=D_M

for every t. The homotopy creates a quadratic number of exact contacts but
neither changes the diameter nor creates positive KKT support.

## 6. Scope and surviving obstruction

The construction rules out the local implication

    near-capacity inactive chamber
    + quadratic deep near-unit matching
    + positive KKT equilibrium on a triangle-free diameter frame
    + collective pair activation
      -> exact unit equilateral triangle or strict diameter decrease.

All distance and contact classifications are exact rational calculations. The
only irrational normalization in the Oler discussion is sqrt(3)/2. No source
point is deleted, the initial and terminal sources have the same cardinality,
and no full-source ZR/ZF statement is used.

The exact surviving C-II obstruction is global:

    prove that a true global diameter minimizer cannot realize this
    frame-plus-rhombic-chamber geometry, or construct a strict same-cardinality
    sub-D competitor that moves the diameter-carrying core.

The chamber statistics and first-order KKT equations are insufficient. This
regression is noncanonical and leaves theorem state unchanged.

## 7. Verification

Run:

    python3 research/verify_target_c_inactive_chamber_kkt_activation_regression.py

The script checks the rational basis, exact initial and terminal contact graphs,
triangle-freeness, cross-separation, fixed diameter, near-capacity slack bound,
deep matching, and the KKT scalar balance. It does not establish global
optimality or C-II closure.
