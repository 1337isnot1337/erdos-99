> Generated reading edition · [exact source](../../../docs/reports/target_c_zero_transfer_additive_promotion_2026-09-11.md) · source SHA-256 `0c6fca62ad2a0a0448fdeafc138d23940d18606beccac794bae5bb7c7e84547c`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-3F124163F5D2","canonical":true,"claim_ids":["C-ZTA"],"claim_statuses":{"C-ZTA":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C — audit and promotion of the zero-transfer equality exclusion

**Date:** 2026-09-11  
**Target:** C-II  
**Status:** promoted audited addendum  
**Dependencies:** promoted C53/C63 normalization, C26/C34/C35, the circular-planar
split representation and interval-sign lemma, and SEPq.

## Theorem

Let (A) be the contact-minimal, then diameter-pair-minimal C-II representative,
with all source points retained. Let (B) be the loaded endpoints of a
relative-interior normalized stress and

$$
K=Q^{\mathsf T}\Lambda^+Q,
$$

where the diameter edges have one legal C53 projective orientation. If (D\ge9),
then

$$
\boxed{\min_{e\ne f}K_{ef}=0\text{ is impossible}.}
$$

Thus every surviving two-dimensional C-II stress is in the strict-negative phase

$$
\boxed{\min_{e\ne f}K_{ef}<0.}
$$

This conclusion is independent of (s_Z), the cyclic/forest topology of the actual
diameter graph, and the number or location of contact-isolated source points.

## Audit proof

Write the consistently oriented diameter vectors as

$$
u_i=a_i(1,t_i),\qquad a_i>0,qquad t_1<\cdots<t_m,
$$

and put (Γ=\operatorname{diag}(a_i\beta_i)). The promoted C53 identities are

$$
M=\Gamma(\Beta^{-1}-K)\Gamma\succeq0,
\qquad M\mathbf1=Mt=0,
$$

with (M_{ij}=-\gamma_i\gamma_jK_{ij}) for (i\ne j).

Assume (min_{i\ne j}K_{ij}=0). Then all off-diagonal entries of (K) are
nonnegative, so (M) is a weighted Laplacian. Since the slopes (t_i) are distinct,

$$
0=t^{\mathsf T}Mt
 =\sum_{i<j}\gamma_i\gamma_jK_{ij}(t_i-t_j)^2
$$

forces every off-diagonal (K_{ij}) to vanish. Hence (K=\Beta^{-1}).

Let (W) be the actual circular-planar effective-resistance metric. Its interval
split representation gives, after centering,

$$
K=\sum_A\lambda_Az_Az_A^{\mathsf T},
\qquad \lambda_A\ge0,
\qquad z_A=Q^{\mathsf T}\mathbf1_A.
$$

For three ordered diameter edges (i<j<k), the audited C53 interval-sign lemma is

$$
z_k(z_i-z_j)\le0,
\qquad z_i(z_k-z_j)\le0.
$$

Comparing the zero entries (K_{ri}=K_{r,i+1}) term by term shows that every
positive split with (z_i\ne z_{i+1}) has support contained in
({i,i+1}). Applying this at adjacent gaps rules out every positive split vector
with two-coordinate support when (m\ge3). A nonzero constant split vector is also
impossible because it would contribute positively to every off-diagonal entry of
(K). Splits with (z_A=0) contribute nothing and are discarded.

It follows that every positive split is singleton-supported. A singleton split gives
an additive resistance metric, so

$$
W_{ij}=r_i+r_j\qquad(i\ne j).
$$

For completeness, no non-singleton zero-crossing split has been silently excluded:
if a proper interval split crosses no diameter edge, each nonempty shore contains a
whole diameter edge because every loaded terminal is incident to an actual diameter
edge. Two such edges lie in disjoint cyclic intervals and do not cross, contradicting
the diameter-thrackle property. Only (z_A=0) splits remain, and they have no
effect on (K).

SEPq now applies to the actual positive contact network. It supplies a contact
vertex (z) such that every component of (C-z) contains at most one loaded
terminal. Therefore

$$
\deg_C(z)\ge |B|\quad(z\notin B),
\qquad
\deg_C(z)\ge |B|-1\quad(z\in B).
$$

C34 gives (2|B|\ge\lceil D\rceil+2), so (D\ge9) implies (|B|\ge6). The
C26/C35 degree caps are (5) for an unloaded vertex and (3) for a loaded one,
contradicting both alternatives. This proves the theorem.

## Exact effect on the frontier

The theorem removes the equality branch from all three required ledgers:

1. cyclic (s_Z=0);
2. forest (s_Z=0); and
3. (s_Z>0).

The remaining C53 phase is strict-negative. It is not enough to close C-II: the
weighted four-cycle common-block regression permits negative, zero, or positive
cross-transfer, and the actual C-II source may still have a non-additive response
with arbitrarily small strict minors. Contact-isolated points remain part of the
source population throughout.

This addendum promotes only the displayed equality exclusion. It does not promote
any claim that strict-negative transfer has a uniform magnitude or that it yields a
finite release or a strict smaller-diameter competitor.
