<!-- theorem-state: {"artifact_id":"ART-87D7450B695E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C: corner barrier for a three-direction wall packet

Date: 2026-10-06. Authority: `35f5843ab9f5d11327d0f4cc803ed00707806ae7`,
state `2026-10-06.audit.65`. Classification: **regression** for the
restricted packet family; **proved candidate awaiting independent audit**
for its analytic local exclusion. No capacity upper bound for arbitrary
packets, global optimizer, C-II closure or Level I result is claimed.

The failed implication is

`small convex bending of any near-triangular wall -> rotate and strictly
dilate its full triangular interior grid -> complete strict packet`.

The two-direction result needs a different argument for three-direction
walls. This report identifies exactly which corner constraints interfere.

## 1. Physical convex unit wall

Let `M>=3`. Take six side directions separated by `pi/3`, with `M`
unit edges on each side. On each side rotate edge `j` by
`(2j-M+1)theta`. All six side chords have length

\[
L(\theta)=\sum_{j=0}^{M-1}\cos((2j-M+1)\theta)
=M-C\theta^2+O(\theta^4),
\quad C=\frac{M(M^2-1)}6.
\tag{1}
\]

The chords close to a regular hexagon of circumradius `L`. Positive small
`theta` gives a strictly convex `6M`-vertex actual unit wall. All
nonconsecutive wall pairs are longer than one for sufficiently small
angle; this is a feasible triangle-free wall source. No canonical stress
or global optimality is attributed to this wall source.

At zero, its full triangular-lattice interior has
`3M^2-3M+1` sites. Consider only centered packets obtained by rotating
that whole interior grid by `phi` and dilating by `ell=1+epsilon`.
Strict mutual unit separation requires `epsilon>0` because the grid
contains unit pairs.

Fix the rightmost corner and its radial inner grid site. Their positions
are

\[
q_0=(L,0),\qquad p=(1+\epsilon)\operatorname{Rot}(\phi)(M-1,0).
\]

The old neighboring wall vertices at that corner are

\[
q_- =q_0-\operatorname{Rot}((M-1)\theta)(1/2,\sqrt3/2),
\]
\[
q_+ =q_0+\operatorname{Rot}(-(M-1)\theta)(-1/2,\sqrt3/2).
\tag{2}
\]

These three guards remain if wall deletions are restricted to the
middle banks of the two-direction construction.

## 2. Necessary small-motion bounds are incompatible

Work at fixed `M`, as `theta>0` tends to zero, with `phi->0` and
`epsilon>=0` tending to zero. For the two neighboring guards, Taylor
expansion of the exact squared norms gives

\[
|p-q_\pm|^2-1
=2a_*(M-1)(\theta\mp\phi)-(M-1)\epsilon
 +O(\theta^2+\phi^2+\epsilon^2),
\quad a_*=\sqrt3/2.
\tag{3}
\]

The constants in the remainders may depend on `M`. Cross terms are
absorbed by the displayed quadratic bound. If both distances are at
least one, the negative linear epsilon term permits its quadratic
remainder to be absorbed for small epsilon. Thus

\[
|\phi|\le\theta+O(\theta^2+\phi^2).
\]

For small `phi` this first gives `phi=O(theta)` and then

\[
\boxed{|\phi|\le\theta+O(\theta^2).}\tag{4}
\]

The corner guard itself gives the different exact expansion

\[
|p-q_0|^2-1
=M(M-1)\phi^2-2C\theta^2-2(M-1)\epsilon
 +O(\theta^4+\phi^4+\epsilon^2+\epsilon\theta^2
                                      +\epsilon\phi^2).
\tag{5}
\]

Again the epsilon terms can be absorbed into the strictly negative
linear term. With (4), the remaining upper bound is

\[
|p-q_0|^2-1
\le\left[M(M-1)-2C+o(1)\right]\theta^2
=\left[-\frac{M(M-1)(M-2)}3+o(1)\right]\theta^2<0.
\tag{6}
\]

For every fixed `M>=3`, there is therefore a neighborhood of
`(theta,phi,epsilon)=(0,0,0)` in which no positive-curvature rotated and
strictly dilated packet passes these three guards. The same conclusion
holds at every rotation by an integer multiple of `pi/3`, since those
rotations permute the interior triangular lattice.

Equivalently, if `phi=kappa theta+o(theta)` and
`epsilon=lambda theta^2+o(theta^2)`, `lambda>=0`, the neighboring guards
require `|kappa|<=1`, whereas the corner requires

\[
kappa^2\ge\frac{M+1}{3}+\frac{2\lambda}{M}>1.
\]

The contradiction is a lower-pair constraint, not an inactive upper
exception, weighted-energy inference or missing source point.

### 2.1 A general smooth affine packet cannot repair the corner barrier

More generally let a `C^2` packet family map every original interior
triangular site by `p -> T(theta)p+t(theta)`, with `T(0)=I`, `t(0)=0`.
The three unit lattice directions occur among interior pairs for `M>=3`.
Write `S_1=Sym T'(0)`. Unit separation makes `r^T S_1 r>=0` in those
three directions. The six corner guards give
`(M-1)r^T S_1r+r dot t'(0)<=0` for the six radial directions.
Their sum and
`sum_three r r^T=(3/2)I` force `tr S_1=0`. All three quadratic values
then vanish, hence `S_1=0`. Opposite corner guards force `t'(0)=0`.
Therefore `T'(0)=kappa J`, and the adjacent guards still require
`|kappa|<=1`.

Write

\[
T(\theta)=I+\kappa\theta J+\theta^2B+o(\theta^2),
\qquad t(\theta)=\theta^2w+o(\theta^2),
\qquad S_2=\operatorname{Sym}B+\tfrac12\kappa^2I.
\]

The second-order unit-pair inequalities give `r^T S_2r>=0` along all
three unit directions, hence `tr S_2>=0`. The sum of the six corner
squared-distance changes has theta-squared coefficient

\[
6\kappa^2M(M-1)-6(M-1)\operatorname{tr}S_2-12C
\le -2M(M-1)(M-2)<0.
\tag{7}
\]

The translation terms cancel between opposite corners. At least one
corner guard fails. Thus no such smooth affine family, including
translation and shear, can make this full interior grid into a feasible
packet for all sufficiently small positive curvatures. This does not
exclude a remote finite affine configuration or a nonaffine packet.

## 3. What the regression kills and how to strengthen the target

Small outward bow creates first-order side clearance, but the side
chords shorten by `C theta^2`. For this three-direction grid, a radial
inner corner site already has an old unit-distance guard at the corner.
Rotation sufficient to offset chord shortening violates a neighboring
guard at first order. The two-direction oblique packet had no such
third-family unit guard in its limiting interior cloud.

This kills direct use of a single rotation and dilation, and any smooth
affine repair starting at the complete three-direction interior lattice
with retained corner guards. It does
not show that another packet of that cardinality is impossible. It does
not supply a feasible canonical old cloud at that count or a globally
optimal wall source. It is not a Level I disproof.

The strengthened packet theorem must use at least one new premise or
construction: a nonaffine interior rearrangement, deletion and payment
of the corner guard labels, a different exact-contact packet with its
full contact budget, or a finite endpoint outside this small homothety
family. Any deleted point must be restored by an actual certified site.

Next attack the nonaffine packet with explicit corner displacements and
its contact budget. An abstract packing slack or leading Oler estimate
does not replace those coordinates. The macroscopic chamber and
full-core branches remain open.

## 4. Finite verifier

`research/verify_target_c_three_direction_corner_barrier_2026_10_06.py`
uses exact `Q(sqrt3)` arithmetic. It checks four feasible rational-angle
wall sources and 492 rational small homothety proposals against the
three guards. Every proposal fails at least one guard. It also checks
the exact negative coefficient in (6) for every integer `M=3,...,100`.
The universal local exclusion is the Taylor argument above, not these
samples. Remote rotations, translations, nonaffine packets, protected
capacity and global optimality are not enumerated.
