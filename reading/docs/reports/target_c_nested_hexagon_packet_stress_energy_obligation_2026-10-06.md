> Generated reading edition · [exact source](../../../docs/reports/target_c_nested_hexagon_packet_stress_energy_obligation_2026-10-06.md) · source SHA-256 `a918d2251b8ed9af98b8ff17c70b83e3c1c3e3675be067ccfac7d15054124e52`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-E352AC3C410D","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C: nested hexagon stresses in the nonaffine packet problem

Date: 2026-10-06. Authority: `a2811924d18778e8220c42904c9a5a92b58ffd78`,
state `2026-10-06.audit.66`. Classification: **proved candidate awaiting
independent audit** for the stress identities and necessary energy
inequalities; **exploratory** for the numerical discovery. No promotion,
capacity upper bound, canonical-source exclusion or Level I result.

The next implication under attack is

`actual three-direction wall + nonaffine strict packet -> every nested
ring energy at least the corner load -> first-order geometry forces one
energy below that load -> contradiction or a different finite packet`.

Only the necessary stress/energy step is proved here. The energy upper
bound and the resulting packet-existence/exclusion conclusion remain open.

## 1. Limiting packet and six physical corner guards

Use the six-sided curved unit wall of the preceding corner-barrier report,
with `M>=3`, and put `R=M-1`. The limiting candidate interior sites are
the complete triangular-lattice hexagon

$$
P_R=\{iu+jv:\ |i|,|j|,|i+j|\le R\},
\quad u=(1,0),\quad v=(1/2,\sqrt3/2).
$$

There are `3R^2+3R+1` sites. For each radius `r=1,...,R`, its six
radial corner sites are `r e_k`, with `e_k=Rot(k pi/3)u`. The outer
wall corners are `M e_k` at zero. The guard pair from `R e_k` to
`M e_k` has unit length. At positive curvature the wall corner is

$$
q_k(\theta)=L(\theta)e_k
=M e_k-C\theta^2e_k+O(\theta^4),
\quad C=M(M^2-1)/6.
\tag{1}
$$

No feasible old source containing this full limiting interior grid is
asserted. It is the target packet chart being tested. The wall itself is
an exact feasible triangle-free source; all extra packet constraints must
still be checked for any intended exchange.

## 2. A positive stress for each nested ring

Fix `r=1,...,R`. Select the `6r` unit edges of the radius-`r` hexagon ring and,
on each of the six radial rays, the unit chain from `r e_k` through
`(r+1)e_k,...,R e_k` to the fixed guard `M e_k`. Give each selected
edge weight one. All other interior contact pairs have weight zero.

At a noncorner ring vertex, its two selected ring vectors are opposite.
At a ring corner the two ring contact gradients sum to `e_k`, and the
first outward radial edge has gradient `-e_k`, so equilibrium holds.
At a subsequent radial vertex its two chain gradients are opposite.
There is no inner chain past the selected ring. Thus every moving
interior site has exact positive equilibrium on this selected support.
Only the six fixed guards bear a nonzero reaction.

Include also `r=0`: select all six full radial chains from the common
center to the six fixed guards, with no ring edges. At the center the
six gradients sum to zero; all other moving chain vertices again have
two opposite gradients. This supplies the six central spoke rows absent
from the positive-radius ring supports.

The selected contact count is

$$
6r+6(M-r)=6M.
\tag{2}
$$

For any first-order packet velocity `d` satisfying all unit lower
inequalities and the six stationary first-order corner guards, the
weighted sum of the selected first variations is zero by equilibrium.
Every summand is nonnegative. Hence every selected first variation
vanishes. Taking every `r=0,...,R` shows that all nested ring and radial-chain
rows are forced zero. Their distinct support, including the six guard
rows, has count

$$
\boxed{3R(R+1)+6R+6=3M(M+1).}\tag{3}
$$

The count is not a theorem that every other row is weak: completeness of
that classification would need a strictly positive certificate for all
other rows. The exact stress proves zero only on its stated support.
No affine restriction is placed on the velocity field.

## 3. Every smooth feasible packet must pay each ring's energy

Suppose a `C^2` nonaffine packet family has positions

$$
p_i(\theta)=p_i+\theta d_i+\theta^2b_i+o(\theta^2).
$$

For the six guards use (1), so their first velocities are zero and
second coefficients are `-C e_k`. Define

$$
E_r(d)=
\sum_{ij\in\mathrm{ring}_r}|d_i-d_j|^2
+\sum_{k=0}^5\sum_{s=r}^{R}|d_{s e_k}-d_{(s+1)e_k}|^2,
\quad d_{M e_k}=0.
\tag{4}
$$

All selected pairs had unit length and zero first variation by Section 2.
Summing their squared-distance changes to second order cancels every
moving `b_i` term by the same equilibrium. On the terminal guard edge,
the old difference from `R e_k` to `M e_k` is `-e_k`, giving the guard
contribution `-2C`. Therefore the summed theta-squared coefficient is
exactly

$$
\boxed{E_r(d)-12C.}\tag{5}
$$

All lower inequalities require

$$
\boxed{E_r(d)\ge12C=2M(M^2-1)
\qquad\text{for every }r=0,\ldots,R.}\tag{6}
$$

If every selected contact opens with strictly positive second-order
coefficient, its particular inequality is strict. A packet could open a
contact only at a later order, so strict finite feasibility alone does
not make (6) strict. Higher-order terms must not be discarded in the
equality case.

This is a necessary kinetic condition on a specified target packet, not
a count of available sites, route length or actual canonical stress.
The weights overlap between ring stresses: their inequalities may be
used separately, but their right sides cannot be added as independent
physical currencies.

## 4. Numerical discovery and exact limits

The exploratory script parameterizes all point velocities independently
in triangular axial coordinates. After division by `sqrt3`, the entire
first-order matrix is rational. It numerically identifies rows that
cannot have positive first variation, finds a point with positive slack
on the other rows, and then tests second-order coefficient feasibility.
It searches 63 velocity candidates per finite packet, with and without
the middle wall-root proposals.

For `M=3,4,5,6`, the numerical zero-row counts were 36,60,90,126,
matching (3). The sampled second-order programs supplied no positive
minimum coefficient. This does not exhaust the first-order polytope,
prove the zero-row classification, establish a quadratic maximum, or
rule out finite/higher-order packets. No floating result is load-bearing.

The source verifier runs `M=3,...,12`: it checks the selected stress supports
and moving-site equilibrium in those ten packets (16,365 checks), and checks
the first- and second-coefficient identities on 225 chosen polynomial-field
samples. Its JSON key `arbitrary_field_cancellation_checks` overstates those
samples; they are not an arbitrary-field test. The all-field cancellation and
every-`M` statement follow from the analytic ring/radial identities, not finite
enumeration. This scope clarification follows source PR #947; the canonical
analytic claim and the exact verifier bytes are unchanged.

## 5. Strengthened next obligation

The affine corner barrier leaves genuine independent point velocities.
The new missing statement is precise: under every first-order unit lower
and physical wall/root guard inequality, either construct a full finite
packet, or show that some `E_r(d)` is below `12C` and handle the equality
case through higher order. A theorem about one sampled velocity or one
ring does not suffice. A ring-energy upper bound must be proved from the
actual displacement inequalities; it cannot be inferred from graph
planarity or from the existence of a positive stress.

Even a complete local packet obstruction would leave remote finite
rearrangements and canonical chamber extraction open. The ultimate
required endpoint is still a same-cardinality source competitor or
canonical contact loss covering both exhaustive Target C branches.
