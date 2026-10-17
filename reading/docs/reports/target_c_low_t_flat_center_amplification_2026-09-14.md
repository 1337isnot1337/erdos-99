> Generated reading edition · [exact source](../../../docs/reports/target_c_low_t_flat_center_amplification_2026-09-14.md) · source SHA-256 `3011d1939d6dcb7793504bd0d87e8c287095a0333bfc29a757082600a654c4a1`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-743EE1A4C170","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdos Problem #99 - low-t flat-center amplification

**Date:** 2026-09-14
**Target:** C-II, canonical contact-minimal full-core Type-II branch
**Dependencies:** low-t pentagon sea; empty-pentagon trapezoid stability; canonical contact-minimal local structure
**Claim class:** proof-only structural refinement awaiting independent audit
**External literature:** no new import

## LEVEL I STATUS

`STILL OPEN`

The low-t theorem forces far more pentagonal exceptional faces than the coarse AG42
face floor used in the first flat-chain extraction. There is also an avoidable
factor-five loss in the old count of distinct almost-flat middle vertices: one source
vertex cannot be the almost-flat middle of two different good pentagons once the
flatness threshold is chosen below `pi/12`.

Fix `epsilon_0=pi/12`. Empty-pentagon stability supplies `theta_0>0` such that every
pentagon with residual below `theta_0` is isolate-free and has a distinguished
boundary triple `l-m-r` satisfying

$$
|l-m|=|m-r|=1,\qquad \angle lmr>\pi-\epsilon_0.
\tag{LC.1}
$$

Call it good. Let `G_0` count good pentagons, `V_flat` count distinct distinguished
middle vertices, let `H_flat` be the maximum number of endpoint-disjoint hidden chords after choosing one center-to-shoulder diagonal from each good pentagon, and let `C_flat` be the maximum number of pairwise vertex-disjoint distinguished three-vertex chains. Then

$$
\boxed{V_{flat}=G_0.}
\tag{LC.2}
$$

On a convergent Type-II subsequence put

$$
t=(q-k)/D\to t,\quad \kappa=k/D\to\kappa,\quad
\delta=(b-P_F)/D\to\delta,
$$

and

$$
A(t,\delta,\kappa)=\pi+C_0-{5t\over2}+\delta+{\kappa\over2},
\qquad C_0=2\sqrt{\Delta_2}+0.00042.
$$

The low-t pentagon theorem and residual deletion give

$$
\boxed{{V_{flat}\over D}\ge
A(t,\delta,\kappa)-{R_F\over\theta_0D}-o(1),}
\tag{LC.3}
$$

and the flat center/shoulder angle pattern gives

$$
\boxed{{H_{flat}\over D}\ge {1\over4}
\left(A(t,\delta,\kappa)-{R_F\over\theta_0D}\right)-o(1).}
\tag{LC.4}
$$

The existing three-vertex conflict bound gives

$$
\boxed{{C_{flat}\over D}\ge {1\over13}
\left(A(t,\delta,\kappa)-{R_F\over\theta_0D}\right)-o(1).}
\tag{LC.5}
$$

On `R_F=o(D)`, at the current proof-only floor
`t_42=C_146+0.0013751=1.8208886379794447...`, and with the permissive
`delta=kappa=0`,

$$
\boxed{{V_{flat}\over D}\ge0.4944166723690961\ldots-o(1),}
\tag{LC.6}
$$
$$
\boxed{{H_{flat}\over D}\ge0.1236041680922740\ldots-o(1),}
\tag{LC.7}
$$
$$
\boxed{{C_{flat}\over D}\ge0.0380320517206997\ldots-o(1).}
\tag{LC.8}
$$

Throughout `t<=1.8585`, dropping nonnegative `delta,kappa`,

$$
\boxed{{V_{flat}\over D}\ge0.4003882673177079\ldots-o(1),}
\tag{LC.9}
$$
$$
\boxed{{H_{flat}\over D}\ge0.1000970668294269\ldots-o(1),}
\tag{LC.10}
$$
$$
\boxed{{C_{flat}\over D}\ge0.0307990974859775\ldots-o(1).}
\tag{LC.11}
$$

The center count (LC.6) is more than `14.7` times the old coarse
`f_*/5=0.0334249286...` bound; the disjoint-chain count (LC.8) is more than `2.95`
times the old `f_*/13=0.0128557418...` bound.

## 1. One near-flat middle per source vertex

Two distinct unit-contact rays at one source have angular separation at least `pi/3`;
equality would make their neighboring sources distance one and create a forbidden unit
equilateral triangle. Hence every sector between consecutive contact rays is strictly
larger than `pi/3`.

A bounded contact face occupies one such sector at each boundary occurrence. A good
pentagon uses a distinguished sector at `m` larger than `11pi/12`. Suppose two good
pentagons shared the same distinguished middle `m`.

If `d(m)>=3`, the two good face sectors are disjoint and every remaining sector is
strictly larger than `pi/3`. Their total angle would therefore exceed

$$
2(\pi-\pi/12)+(d(m)-2){\pi\over3}
\ge {13\pi\over6}>2\pi,
$$

impossible.

If `d(m)=2`, the two face sectors sum to `2pi`. Two distinct convex pentagons cannot
both use angles below `pi`. The only limiting loophole is two straight `pi` sectors.
Then the two unit neighbors are exactly opposite and `m` is their midpoint, so `m` is
not extreme. Canonical contact-minimality says every nonisolated degree-at-most-two
contact vertex is a diameter endpoint, while every diameter endpoint is extreme. This
is again impossible. Thus (LC.2) holds.

## 2. Low-t supply and residual deletion

The low-t pentagon-sea theorem gives

$$
{p_5\over D}\ge A(t,\delta,\kappa)-o(1).
\tag{LC.12}
$$

Exceptional-face residuals are nonnegative and sum to at most `R_F`, so at most
`R_F/theta_0` pentagons fail the good-face threshold. Hence

$$
G_0\ge p_5-R_F/\theta_0.
\tag{LC.13}
$$

Together with (LC.2), this proves (LC.3).

## 3. Endpoint-disjoint hidden chords: factor four, not factor nine

In the flat trapezoid, the two hidden chords from `m` end at the two shoulder vertices
`a,b`, whose face angles are `2pi/3`. Tighten `theta_0` once more so every good
pentagon has shoulder angles larger than `7pi/12`.

Choose either hidden chord from each good pentagon; this may in particular be the
shorter hidden chord. Chosen hidden chords from distinct pentagonal faces are distinct: each lies in the interior of its convex face except at its endpoints, while distinct planar face interiors are disjoint. A source vertex can be a flat center for at most one good
pentagon by Section 1. It can be a shoulder of at most three good pentagons, because
four disjoint shoulder sectors larger than `7pi/12` exceed `2pi`. If it is itself a
flat center, it can be a shoulder of at most one other good pentagon, because

$$
{11\pi\over12}+2{7\pi\over12}>2\pi.
\tag{LC.14}
$$

Therefore, in the graph containing one chosen hidden chord per good pentagon, a center
endpoint has total chord incidence at most two and the other endpoint has incidence at
most three. Each chosen chord conflicts with at most

$$
(2-1)+(3-1)=3
$$

other chosen chords. Greedy matching retains at least `G_0/4` endpoint-disjoint
hidden chords, proving (LC.4). This improves the generic factor `1/9` from the
contact-degree-five bound.

## 4. Vertex-disjoint chain extraction

Keep `l-m-r` from every good pentagon. A source belongs to at most five bounded
exceptional faces because triangle-freeness bounds contact degree by five. Thus one
selected path conflicts with at most `3(5-1)=12` others. Greedy extraction keeps at
least `G_0/13`, proving (LC.5). Multiplicity one for middle vertices does not by itself
improve this denominator because a path endpoint can still belong to several other
exceptional faces.

## 5. Frontier effect

On `R_F=o(D)` and `t<=1.8585`, the source contains at least
`0.400388D-o(D)` distinct actual vertices with two unit contacts whose angle can be
diagonalized to `pi-o(1)`, and at least `0.100097D-o(D)` endpoint-disjoint hidden near-contacts, and at least `0.030799D-o(D)` pairwise vertex-disjoint such chains. Near `t_42` these strengthen to `0.494416...`, `0.123604...`, and `0.038032...`.

This does not close C-II. Existing near-chain regressions show that a short
almost-straight contact path is not automatically a legal source-preserving flex and
need not be unloaded from the diameter graph. The next bridge must be global: charge
this linear flat-center population to the near-extremal Woodall diameter network and
outer-train bracing system, or construct a simultaneous feasible motion.

## 6. Scope audit

- The numerical coefficients inherit proof-only AG42 `0.00042`.
- Multiplicity one uses contact-minimality only for the exact degree-two straight
  loophole.
- (LC.3)-(LC.5) keep the explicit `R_F/theta_0` loss.
- No KKT weight floor, exact hidden contact, local flex, or strict sub-`D` competitor
  is asserted.

C-II and Level I remain open.

---


**Recovery provenance:** copied from `research/c2-closure-sol-20260914-r7` at exact
tip `1541dac85e9ddf6450bb3cd7b14f5ce76e119420` during the 2026-10-04 Slot 2
branch audit. This recovered claim remains unreviewed and noncanonical.
