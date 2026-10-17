> Generated reading edition · [exact source](../../../docs/reports/target_c_weak_packet_correction_mass_2026-10-02.md) · source SHA-256 `df4003dd1111efa3cf5c215d9932698b52146483820e6a2db02818743b8f5965`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-CFEE5349DA89","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C: weak packets require macroscopic correction mass

```text
subunit balanced internal packets -> normalized diameter mass at most 2/3+o(1)
 -> contradiction in the weak-dominated threshold subbranch;
outside that subbranch, directional contact stress is charged explicitly.
Neither statement eliminates all threshold sources or supplies Level I closure.
```

**Date:** 2026-10-02
**Starting checkout:** `539f5187b3cac9287f6b30cdf6b36aafb1763c5a`
**Research base:** `fbeae9b3fa18a63e07573676b4e2e512a91ca4d5`
**Theorem state:** `2026-09-14.audit.51`
**Owned branch:** `swarm/sol/threshold-global-moment-20261002`
**Mission:** weight-free cross-shore correction and global second-moment coupling.
**Classification:** proved candidates awaiting independent audit/promotion;
conditional threshold application; exact regressions. Artifact lifecycle: unreviewed.
**Level I / C-II:** STILL OPEN / OPEN.
**Literature imports:** none.

No assignment issue was open. Current open packets #613, #618--620 were inspected,
along with the October main chain. This mission addresses normalized *aggregate*
correction mass rather than a lower bound on individual multipliers.

## 1. Authority and dependencies

The state lock and current Target C ledger govern lifecycle. The canonical source is
contact-minimal, then diameter-pair-minimal, and retains contact-isolated points.
Neither the following finite geometry nor the exact regression deletes source points.

Canonical input: [Theory 01, Theorem 4.1](../theory/01-local-structure.md) gives
normalized diameter weights, vertex equilibrium, the contact stress trace `D^2`,
and the contact/diameter second-moment identity. The cut equation below is obtained
by summing vertex equilibrium; it does not need a response inequality.

Conditional threshold inputs, all **unpromoted**:

- [paired staircase](target_c_exact_phase_threshold_paired_staircase_2026-10-01.md);
- [transverse rail saturation](target_c_exact_phase_threshold_transverse_rail_saturation_2026-10-01.md);
- [joint switch/four-host theorem](target_c_complete_grid_joint_switch_budget_2026-10-01_r2.md).

The cross-shore packet report at remote `898e282c` and the packet mass report at
PR #619 head `d73f06e0` were inspected. Their exported-load identities and balanced
pair decomposition are acknowledged; the needed identities are rederived below.
PR #618's unique weak-pivot localization is not a premise. This report neither
audits the whole extraction stack nor promotes another PR.

## 2. Finite weak-pair geometry

Let a unit-separated finite source have diameter `D>=2`. Fix a unit vector `u`.
Two actual diameter bars have four distinct source endpoints, oriented vectors

$$
r_p=d_pu+q_pJu,\qquad r_n=d_nu-q_nJu,\qquad q_p,q_n>0,
$$

and `d_p+d_n>=0`. Give them coefficients `w_p,w_n>0` with
`w_p q_p=w_n q_n`. Write

$$
B=w_p+w_n,\quad \rho={w_pd_p+w_nd_n\over B}<1,\quad
P=w_pr_p-w_nr_n.
$$

Then

$$
|d_p|,|d_n|<3/2,\qquad
{P\cdot Ju\over B}\ge Q_D:=\sqrt{D^2-9/4},\qquad
{|P\cdot u|\over B}<X_D:={1\over2\sqrt{1-D^{-2}}}.
\tag{WG}
$$

### Proof, including the finite angle bound

Put `r_p=D(cos(theta),sin(theta))` and
`r_n=D(cos(psi),-sin(psi))`, with `theta,psi in (0,pi)`.
The axial-sum hypothesis gives `theta+psi<=pi`. Equality would make the two
diameters parallel. Two distinct parallel length-`D` segments in a diameter-`D`
source cannot occur: the two cross-endpoint upper bounds force their longitudinal
midpoint displacement to vanish, then their transverse displacement to vanish.
Thus `delta=pi-theta-psi>0`.

The projective angle `delta` of the vectors `r_p,-r_n` obeys

$$
\delta\ge4\arcsin(1/(2D)). \tag{AG}
$$

For completeness, put `C=D cos(delta/2)`, `S=D sin(delta/2)` and let `(a,b)`
be the difference of their midpoints in vector-bisector coordinates. The two
opposite-endpoint distance bounds imply
`a^2+b^2+2C|a|<=S^2`. The smaller corresponding-endpoint distance squared is
`a^2+(S-|b|)^2`. With `t=|b|<=S`, it is at most

$$
2D^2-2C\sqrt{D^2-t^2}-2St\le2D(D-C).
$$

The last inequality follows on setting `t=D sin(phi)`,
`0<=phi<=delta/2`. Unit separation gives
`1<=2D(D-C)=4D^2 sin^2(delta/4)`, proving (AG).
This is the previously known disjoint-diameter angle bound, not a novelty claim.

Set `A=(theta+psi)/2`, `T=(theta-psi)/2`. Equal transverse flow gives exactly

$$
\rho={D\cos A\over\cos T},\qquad
{P\cdot u\over B}=-{D\sin T\over\sin A}.
$$

By (AG), `D cos A>=sqrt(1-1/(4D^2))`. Since `rho<1`,
`cos T>sqrt(1-1/(4D^2))`, hence `D|sin T|<1/2`. Also
`D cos A=rho cos T<1`, so `sin A>sqrt(1-D^-2)`.
This proves the bound on `P.u`. Moreover

$$
d_p=\rho\cos^2T-D\sin A\sin T,\qquad
d_n=\rho\cos^2T+D\sin A\sin T,
$$

so both longitudinal components have absolute value below `3/2`.
Each transverse component is at least `sqrt(D^2-9/4)`, and
`P.Ju=w_p q_p+w_n q_n`. This proves (WG).

## 3. Aggregate correction mass: a normalized floor

Let actual diameter multipliers satisfy `sum_h beta_h=1`. Suppose one actual
contact cut has every crossed unit-contact vector oriented as

$$
v=\cos\vartheta\,u+\sin\vartheta\,Ju,\qquad
0<\vartheta<\pi,\quad\cos\vartheta\ne0.
$$

Summing full vertex equilibrium on one side of the cut gives

$$
C v=\sum_{h\text{ crossing cut}}\beta_h\widehat r_h,\quad C>0.
\tag{CUT}
$$

Choose any collection of pairs satisfying Section 2. The pair coefficients may
split original diameter coefficients, but their total coefficient on each bar
must not exceed `beta_h`. Both bars in every pair cross this cut, and their
cut orientations are `r_p` and `-r_n`. Let `M` be their aggregate coefficient
mass. Define

$$
\gamma_D(\vartheta)=|\cos\vartheta|Q_D-\sin\vartheta\,X_D.
$$

When `gamma_D>0`,

$$
\boxed{M\le {D\over D+\gamma_D(\vartheta)},\qquad
1-M\ge {\gamma_D(\vartheta)\over D+\gamma_D(\vartheta)}.}
\tag{CM}
$$

Indeed (WG) shows that the chosen exported vector has `sigma Jv` projection at least
`gamma_D M`. All remaining diameter coefficients have aggregate mass at most
`1-M`, including pairs not crossing the cut. Their oriented vector sum has norm
at most `D(1-M)`. The `Jv` projection of (CUT) is zero, so
`gamma_D M<=D(1-M)`, where `sigma=sign(cos(vartheta))`.

If the projective angle is `pi/3+O(D^-1)`, this is

$$
\boxed{M\le2/3+O(D^{-1}),\qquad 1-M\ge1/3-O(D^{-1}).}
\tag{CM60}
$$

This floor is on aggregate **outside** mass. It needs no individual multiplier
floor and is uniform over all normalized stresses satisfying the actual cut law.
It does not say that the outside mass lies in long internal packets.

### Conditional threshold application

For an internal staircase packet, orient all rows from lower to higher A-layer.
Tree-cut balance gives `sum beta_h c_h=0`. Put `f_h=beta_h|c_h|` and
`W=sum_positive f_h=sum_negative f_h`. Pair a positive and a negative row with
equal-flow coefficient `tau_pn=f_p f_n/W`; give the pair bar coefficients
`tau_pn/|c_p|`, `tau_pn/|c_n|`. Summing these pair coefficients recovers every
original bar coefficient exactly.

Select only pairs with `rho<1`. The hull-arc axial ordering supplies
`d_p+d_n>=0`. A shared-endpoint pair in the same layer role has angle at most
`pi/3` and reaction at least `sqrt(3)D/2`, so it cannot be selected. All selected
pairs have four distinct endpoints. Four-host internality gives full B support
with the orientations of Section 3. Therefore (CM) applies simultaneously to
all selected pairs over all internal A packets and to **every** retained B cut.

The conclusion excludes domination by subunit balanced internal pairs beyond
`2/3+o(1)`. Boundary-touching weak packets are not covered by this argument:
their full opposite-shore support has not been established.

## 4. Global contact-direction stress charge

There is a second, independent obstruction to treating correction mass as free.
Let

$$
F_\vartheta(w)=\sigma(w\cdot Ju)(w\cdot Jv),\quad
\lambda_+=(1+|\cos\vartheta|)/2,\quad
\lambda_-=(|\cos\vartheta|-1)/2.
$$

These are the eigenvalue bounds for `F` on unit vectors. Every weak-pair bar
from Section 2 satisfies

$$
F_\vartheta(r_h)/D^2\ge
a_D:=|\cos\vartheta|(1-9/(4D^2))-3\sin\vartheta/(2D).
$$

For any normalized KKT stress, call a contact good when its projective direction
is within `epsilon` of `u` or `v`, and let `S_bad` be the total multiplier mass
of all other actual unit contacts. If `0<=epsilon<lambda_+`, then

$$
\boxed{
{S_{\rm bad}\over D^2}\ge
\left[{a_DM+\lambda_-(1-M)-\epsilon\over\lambda_+-\epsilon}\right]_+ .}
\tag{DC}
$$

Proof: `F` vanishes at `u,v` and its angular derivative has absolute value at
most one. Good unit contacts contribute at most `epsilon` times their stress.
Bad contacts contribute at most `lambda_+` times their stress. The total contact
stress is `D^2`. The exact KKT second-moment identity equates this contact sum
of `F` to the diameter sum, whose weak part is at least `a_D M D^2` and whose
remaining part is at least `lambda_-(1-M)D^2`. Rearranging gives (DC).

In the inverse-diameter triangular-angle regime with `epsilon=O(D^-1)`,

$$
S_{\rm bad}/D^2\ge[M-1/3-O(D^{-1})]_+.
\tag{DC60}
$$

This is a stress charge, not a population/area charge. For completeness each
actual unit-contact coefficient is at most `D`: sum vertex equilibrium on one
side of the perpendicular bisector of that contact and project onto its unit
direction. Every crossing contact contributes nonnegatively and that contact
contributes its entire coefficient. The diameter side is at most `D sum beta=D`.
Thus (DC60) also forces at least `(M-1/3-o(1))D` bad contact edges when positive.
It gives no quadratic count; an `O(D)` exceptional network can still absorb it.

## 5. Closing attempts and exact regression

The first attempted closure multiplies the required correction by the number of
B cuts. It is false: a single full-support correction family contributes to every
cut. The following rational sources and formal systems make that failure exact.

Put `t=1/k`, `s0=2t/(1+t^2)`, `d=(1-t^2)/(1+t^2)`,
`D=1/(2s0)`, `q=D(1-2s0^2)`, `a=D-q`. The original four source points are

$$
(-d/2,-q/2),\ (d/2,q/2),\ (-d/2,q/2+a),\ (d/2,-q/2+a).
$$

The two selected diagonals have vectors `(d,q),(d,-q)`, diameter `D`, and
reaction `d<1`. The two short sides are unit contacts and an additional vertical
side is an actual diameter. These are the old sharp disjoint-pair sources in
rotated coordinates, not a new sharpness claim. Add the reference endpoints
`(+/-D/2,a/2)` and, for rational unit `v=(c,s)`, the two endpoints
`(0,a/2)+/-sigma(Ds,-Dc)/2`, where `sigma=sign(c)`. The latter are a further actual diameter.

For the certified parameter ranges all 28 pair distances lie in `[1,D]`. There
are exactly five actual diameter edges; the script retains all five. Put
`eta=1/(100D^2)`, assign weight `eta` to the vertical diameter and to the
reference, weight `M/2` to each weak diagonal, and weight `b` to the correction,
where

$$
M={1-\eta(2+|c|)\over1+|c|q/D},\qquad b=|c|(Mq/D+\eta).
$$

Every actual diameter has positive weight and the weights sum to one. The weak
export plus vertical diameter and correction equals `C_B v`, with
`C_B=(Mq+eta D)s>0`. Use this identical vector on
`n=floor(D/100)` formal B cuts. It requires the **same** coefficient `b` on all
of them, not `nb`; as `D` grows, `M` approaches `1/(1+|c|)` while `n` grows linearly.

The strengthened attempt adds the contact stress trace, the global second-moment
identity and `alpha_e<=D` to those repeated cut equations. It also survives.
One formal A cut uses stress `C_A=Md+eta D`, and the B cuts use `C_B` each.
Subtract their tensor contributions from the actual weighted diameter tensor.
For every certified case the remaining rational `2x2` tensor is positive definite.
Its explicit LDL decomposition yields two more formal unit-contact directions;
split their coefficients into copies of size at most `D`. This gives exact tensor
and trace identities and only `O(D)` formal contacts, including the linear B shore.

**Omitted hypotheses:** these formal contacts are not the original source's two
unit contacts. No vertex equilibrium, actual train cut realization, PSD stress
with the canonical kernel, full mixed rigidity, quadratic population or global
optimality is claimed. The regression rejects closure from these scalar/vector
and tensor conditions alone; it is not a counterexample to an actual source theorem.

### Repaired attack: add an actual dense complete grid

The omitted quadratic population is not, by itself, the cure. For an unbounded
sequence of integers `k`, put `b0=k^2`, `a0=floor(sqrt(3)b0)` and choose

$$
c_k={a_0^2-b_0^2\over a_0^2+b_0^2},\qquad
s_k={2a_0b_0\over a_0^2+b_0^2}.
$$

Then `0<c_k<1/2`, `c_k^2+s_k^2=1` and
`c_k=1/2-O(k^-2)`. Use this direction for the boundary correction construction.
At its common center `o=(0,a/2)`, add all points of
`o+Z u+Z v_k` in the disk of radius `R=D/2-3`.

This is an actual triangle-free unit-separated source, including the eight
boundary points, and still has diameter **exactly** `D`. For the lattice,
`|iu+jv|^2=i^2+j^2+2cij`. Same-sign indices give at least one; opposite-sign
indices of absolute values `a,b>=1` give at least `a^2+b^2-ab>=1`, with strict
inequality at `a=b=1` because `c<1/2`. The only unit vectors are `+/-u,+/-v`.
Its contact graph is a square grid and has no triangle. The original boundary
contacts are only the two disjoint short sides. Every added point is at least
distance two from every boundary point: the boundary radii lie between
`D/2-1` and `D/2+1`. The same bounds give strict upper cross distances below
`R+D/2+1=D-2`. Interior pair distances are at most `2R<D`.

The actual central rhombus complex contains a complete rectangle with both shores
linear in `D`: indices `|i|,|j|<=floor(R/4)` give such a rectangle. This is a
**local** complete grid; no global O--O extension is asserted.

The population even has the optimal leading density. A centered fundamental
parallelogram has radius at most one and area `s_k`. Every point of the radius
`R-1` disk belongs to a translate whose lattice center is in the radius `R` disk.
Thus, with `N_k` interior points,

$$
N_ks_k\ge\pi(R-1)^2,\qquad
N_k\ge{\pi\over2\sqrt3}D^2-O(D).
$$

This preserves finite near-disk geometry, inverse-square angle excess, actual weak
diameters and quadratic source population simultaneously. It does **not** preserve
vertex KKT: the diameter endpoints have no unit contacts to the grid, and the
reference/correction endpoints have no unit contacts at all. Positive diameter load cannot equilibrate
there. The two formal tensor-completion directions remain uncoembedded. The
example therefore sharpens the omitted hypothesis to actual load transmission,
rather than refuting any global-minimizer theorem.

The next local repair tries to attach a prescribed `v_k` contact at the lower
left weak endpoint. It fails exactly: its separation from the adjacent lower
right endpoint is `|v_k-(d,a)|<1`, certified in the script. The corresponding
reflected upper port fails as well. This is not a universal port exclusion: an
angle excess of order `1/D` can remove the obstruction, and the current extraction
only bounds excess by `O(1/D)`, with no coefficient small enough to forbid it.
Thus neither population nor a naive port continuation closes the actual branch.

### Finite strict competitor for the repaired source family

In fact the entire dense family has a contact-preserving finite release. Translate
the two lower short-side endpoints upward by `lambda Ju`, and the two upper
short-side endpoints downward by the same amount. Translate the two reference
endpoints toward each other by `lambda u` each, and translate the two correction
endpoints toward each other by `lambda sigma(su-cJu)` each. Fix every lattice point.

The two old unit contacts are translated rigidly; all lattice contacts are fixed.
The two weak diagonals change from `(d,+/-q)` to `(d,+/-(q-2lambda))`, so both
strictly shorten. The additional vertical diameter, reference and correction each
change in length from `D` to `D-2lambda`. These are **all** actual diameter pairs.
Every other pair has strict upper and lower slack initially. Finiteness gives a
positive interval of `lambda` preserving that slack. Thus for each family member
there is a same-cardinality, unit-separated source of diameter strictly below `D`,
with its full original contact graph preserved.

For the three dense certified instances, the explicit choice `lambda=1/(100D)`
passes every boundary pair constraint, preserving precisely the two short contacts.
All moved boundary radii remain between `D/2-1-lambda` and `D/2+1`; this keeps
every interior-boundary pair strictly between one and `D`. Interior pairs are fixed
and bounded by `D-6`. These radius bounds certify the whole large source, not only
the eight-point shell. No inference from an infinitesimal derivative is used.

This is a strict-competitor theorem for the constructed family, and therefore a
complete rejection of that proposed near-optimal family as global minimizers. It
does not prove that arbitrary canonical sources admit the same motion: such sources
have actual load-transmitting contacts and additional inactive pairs absent here.

## 6. Certificate and hostile audit

Run [the exact certificate](../../../research/verify_weak_packet_correction_mass_2026_10_02.py):

```sh
python3 research/verify_weak_packet_correction_mass_2026_10_02.py
```

It certifies 36 rational eight-point sources / 1,008 source distances, positive
normalized weights on every actual diameter, 120 repeated B cut balances,
13,032 bounded formal contact coefficients, and exact tensor/trace identities.
It also certifies dense sources with 8,061 / 13,011 / 25,989 actual points and
local complete grids of sizes 22x22 / 28x28 / 42x42. Radius inequalities certify
all interior-boundary distances simultaneously; the lattice distance proof above
certifies interior separation without a quadratic pair scan.
Three explicit finite strict competitors preserve every actual unit contact.
All arithmetic is rational. The geometric general statements have the proofs above;
finite success is not a global-optimality argument.

Hostile checks: individual weights need not have a floor; source points and formal
contacts are distinct; inactive pairs are not promoted to contacts; no motions are
integrated; no Euler-path inference or boundary occurrence identification is used;
contact isolates remain retained. Boundary weak packets, open-cell exact phase,
nonconstant phase, split-star, inactive interfaces, higher-surplus full core and the
macroscopic inactive-container/exterior-cap branch remain open.

## 7. Exact frontier and next obligation

There is no canonical frontier change. The new finite result gives a uniform
aggregate correction floor and an actual contact-direction stress charge; it does
not deliver a strict same-cardinality competitor or an exact triangle.

The next actual-source obligation is to exclude or finitely release a correction
family with total mass at least `1/3-o(1)` that is reused over all B cuts, while its
outside contact network pays (DC). The regression shows that normalized cut forces,
the tensor identity and individual contact upper bounds cannot supply that exclusion
without vertex/face co-embedding. An independent audit should first check the pair
coefficient splitting, cut orientation at internal host endpoints, and (DC).

**Promotion recommendation:** preserve as unreviewed; no state-version or active
prompt change. Level I remains open.
