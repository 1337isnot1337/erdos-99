> Generated reading edition · [exact source](../../../docs/reports/target_c_two_phase_star_bracing_saturation_2026-10-01.md) · source SHA-256 `b0f298ef62173d5f3a2d853512292bf8b4faf7412bbaebe4d197ea1e4ee7f955`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-B1B47276233F","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II -- two-phase star-bracing saturation

Base main: c00bb08090cf3a7a89fc195cbe3ab450983a5de0. Proof-only; C-II remains open.

Let a_D=asin(1/(2D)). Current main proves that the diameter edges incident to every
loaded vertex v occupy one contiguous projective-direction interval I_v of span
Phi_v<=pi/3. In the rooted wrapping branch it also gives the exact angular excess

    E_D = pi - 2 a_D q,

with E_D<=Delta(lambda)+o(1), where

    Delta(lambda)=pi/2-[lambda+4 lambda sqrt(1-lambda^2)].

THEOREM 1 (exact star-span identity). If r_v=deg_H(v)>=2, then

    Phi_v = 2 a_D (r_v-1) + e_v,     0<=e_v<=E_D.

Proof. Write the incident diameter edges in their contiguous direction order. Each of
the r_v-1 internal gaps is a shared-endpoint gap, hence is at least 2a_D. Their sum is
Phi_v. The excesses above 2a_D are nonnegative summands of the global excess E_D.

Call a projective direction u straddled by v if two incident diameter rays at v have
opposite strict signs after dotting with Ju, using one common orientation of the rays.
Because I_v has aperture <pi, straddling forces u to lie in I_v. Hence if v straddles
two directions u,w,

    Phi_v >= d_P(u,w),

where d_P is shorter distance on the projective circle. Therefore

    deg_H(v) >= 1 + [d_P(u,w)-E_D]/(2a_D).              (1)

Now take the two fixed Section-90 inverse-phase train shores A_* and B_*. Their phase
labels are distinct and all reduced phases lie in one interval of width

    W_D = 4K/D.

Thus for any tau in A_* and sigma in B_*,

    d_P(dir tau, dir sigma) >= pi/3 - W_D.              (2)

Combining (1) and (2), any single diameter star that straddles one direction from each
Section-90 shore satisfies

    deg_H(v) >= 1 + [pi/3-W_D-E_D]/(2a_D).              (3)

In the rooted near-endpoint window this is

    deg_H(v) >= [pi/3-Delta(lambda)-o(1)] D.

At the exact rooted endpoint Delta(lambda_1)=0 and E_D=o(1), so

    deg_H(v) >= (pi/3-o(1)) D.                           (4)

THEOREM 2 (at most three two-phase stars at the endpoint). For all sufficiently large
members of an exact rooted-endpoint sequence, at most three diameter vertices can
straddle directions from both Section-90 phase shores.

Proof. The r_v-1 internal gaps of different stars are disjoint shared consecutive
diameter-direction pairs. Current main gives m_D=d_H and h=q-d_H, so the total number
of shared consecutive pairs is exactly q-2d_H. At the exact endpoint,

    q=pi D+o(D),   d_H=o(D).

Four vertices satisfying (4) would therefore require at least

    4(pi/3-o(1))D = 4pi D/3-o(D)

distinct shared gaps, exceeding pi D+o(D). Contradiction.

SECTION-157 COROLLARY. For an outer-to-outer train tau, suppose the two opposite-sign
diameter witnesses in audited-working Section 157 are both incident to one vertex v.
The common vertex lies on one fixed shore of the train cut, so all those crossing
edges receive the same orientation reversal when converted to rays from v. The two
Section-157 transverse signs therefore say exactly that v straddles the projective
train direction.

Thus, at the exact rooted endpoint, a vertex that single-star two-side braces one
outer-to-outer train from each Section-90 inverse-phase shore must be one of at most
three vertices and must have degree (pi/3-o(1))D.

This rules out diffuse two-phase bracing by many ordinary diameter stars. The remaining
escape is precise: either signed train bracing concentrates through at most three
asymptotically maximal stars, or the positive and negative diameter witnesses for many
trains are split across different stars. The next target is to bound the multiplicity
with which one star transition or one diameter edge can service nested train cuts.

No computation, verifier, numerical experiment, or CI result is used.
