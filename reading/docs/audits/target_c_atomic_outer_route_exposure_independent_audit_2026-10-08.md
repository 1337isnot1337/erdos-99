> Generated reading edition · [exact source](../../../docs/audits/target_c_atomic_outer_route_exposure_independent_audit_2026-10-08.md) · source SHA-256 `f8a1ce7cced743f83c14c2ff88a3c22186a99f76e17581bed337320ea4a378ad`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-0746B4DCCF42","canonical":true,"claim_ids":["C-ATOMIC-OUTER-ROUTE-EXPOSURE"],"claim_statuses":{"C-ATOMIC-OUTER-ROUTE-EXPOSURE":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C Audit.130 — atomic outer-route exposure

Date: 2026-10-08  
Audit base: origin/main=462456b7b34140ea2c88aec71ffe3e1d5a0a6e6d, state 2026-10-08.audit.129  
Source snapshot: origin/research/target-c-atomic-boundary-audit-20261004 at 9d51e2120d36ba60161975d0de6e9c77786a1c53  
Classification: independently reconstructed theorem; **PASS — promote**.  
Scope audited: Theorem B, Section 7 only, of docs/reports/target_c_atomic_boundary_capacity_audit_2026-10-04.md. Theorem C, the collapsed-phase regression, and the companion sharp-orbit report were not audited.

Frozen source hashes: report e79dbcfcefcd7a65851e2f7e2307fede023f8860656f0b8979dec2d94b832b2f; finite verifier e4d1066e3cfd96e074a50f8780b3614ffb6da1bc3753401adb3f301251adee04.

## Exact claim

For every unbounded canonical contact-minimal, then diameter-pair-minimal, triangle-free global-source sequence in the Type-II branch, retain every source point including contact isolates. Use the notation from C-ATOMIC-TRACK-BOUNDARY-COST and put P_exc=Q+4f. The new claim is

```math
\liminf_{D\to\infty}\frac{P_{\rm exc}+x_B}{D}\ge4s_2,
\qquad s_2=\sqrt{\frac{\pi}{2\sqrt3}}. \tag{1}
```

Section 63 gives
```math
5Q+x_B=10(q-k)-5p+g-4z,
```
so (1), f<=Q, and p/D->pi imply
```math
\boxed{\liminf_{D\to\infty}
\frac{10(q-k)+g-4z}{D}\ge5\pi+4s_2.} \tag{2}
```
For t_D=(q-k)/D<=1.860+o(1), this yields
```math
g-4z\ge(c-o(1))D,\qquad
c=5\pi+4s_2-18.6\in(0.91721449540479,0.91721449540480).
```
In particular
```math
\frac qD\le\pi-c+o(1)
=18.6-4\pi-4s_2+o(1)
=2.2243781581850\ldots+o(1).
```
The source verifier's q_hi=PI_HI-demand_lo arithmetic is consistent with this Theorem B consequence. It is not a certificate for the analytic theorem.

## Dependencies

- C-ATOMIC-TRACK-BOUNDARY-COST, whose fixed-limit finite-window argument gives atomic track-direction mass a>=2s_2 for every joint weak limit.
- C-LOADED-HULL, including Section 63's occurrence-disjoint outer routes between consecutive loaded hull vertices and x_B=b-q>=0.
- C-FULLCORE-NEAR-DISK, giving D^-1 F -> B_(1/2), p/D -> pi, and convergence of perimeter-weighted tangent measures to uniform projective-direction measure of mass pi.
- C-RHOMBUS-POP and C-PUNCTURED-PHASE, giving actual strict unit rhombi and total angular area defect O(D), with the full source retained.
- C-TRAIN-INTERFACE-CURRENCY, with Theory 01, Theorem 10.6, for actual complete tracks and simple triangle-free finite crossing graphs.

All dependencies are canonical at the audit base. No unit-side assumption is made about the loaded hull boundary.

## Independent exposure reconstruction

Fix a subsequence along which (P_exc+x_B)/D approaches a finite liminf. The infinite case is immediate. On this subsequence P_exc/D and x_B/D are bounded; since q<=p and p/D->pi, also b/D=(q+x_B)/D=O(1). Pass jointly to limits of these scalar budgets and the normalized direction measures. Use the same fixed weak limit nu of actual track directions as in the preceding canonical theorem, so its atomic mass is a>=2s_2.

Let omega_D count every occurrence of a unit contact edge in the cyclic outer contact walk, with mass 1/D per occurrence. Let o_D be the outer terminal-occurrence measure of the actual tracks. Then o_D<=omega_D. Every track end has one terminal occurrence, so in the joint limit
```math
2\nu=o+j,
\qquad j\ge0,
\qquad \|j_D\|\le P_{\rm exc}/D. \tag{3}
```
In particular o<=2nu, so every atom of o lies at an atom of nu.

Fix a finite set A of atoms of nu, and let U be disjoint small direction neighborhoods of A, with boundary null for the limiting measures. Section 63 partitions the entire occurrence-counted outer walk into exactly q edge-disjoint routes W_i, one between each consecutive pair of distinguished loaded vertices; their edge counts ell_i sum to b=q+x_B. Route endpoints are distinct source points and therefore have separation at least one.

Fix an integer M>=1. At most b/(M+1) routes have more than M unit-edge occurrences. For a route of length at most M whose every edge direction lies in U, choose fixed unit-vector lifts u_1,...,u_r of the finitely many directions in A. Its chord vector differs by at most M delta from one of the finitely many signed sums
```math
\sum_{j=1}^{\ell}\varepsilon_j u_{i_j},
\qquad 1\le\ell\le M,
\quad \varepsilon_j\in\{-1,1\},
```
where delta is the maximum neighborhood width. If the limiting signed sum is zero, then for M delta<1 the route chord would have length less than one, contradicting separation of its endpoints. Every nonzero signed sum belongs to a finite set and has a fixed direction; as delta->0, all such route chords lie in neighborhoods shrinking to a finite set of loaded hull-side directions.

For fixed M and neighborhood width δ, let S_{M,δ} be a union of closed direction arcs around the finitely many nonzero signed-sum directions above, chosen so its width tends to zero as δ tends to zero. The short routes whose every edge lies in U have distinct loaded-hull sides directed into S_{M,δ}. Each such side has length at least one, so their number R_D divided by D is at most the normalized loaded-hull tangent measure of S_{M,δ}. Its weak limit is the uniform measure μ; choosing arc boundaries μ-null gives
```math
\limsup_{D\to\infty}R_D/D\le\mu(S_{M,\delta}),
\qquad \mu(S_{M,\delta})\to0\quad(\delta\downarrow0,\ M\text{ fixed}).
```
This uses the actual loaded hull and does not assume its sides are unit. At most b/(M+1) routes are longer than M. Every other route contains at least one outer-walk occurrence outside U. These routes are edge-occurrence disjoint, and the full walk has b occurrences, so
```math
\omega_D(U)\le\frac{x_B}{D}+\frac{R_D}{D}+\frac{b/D}{M+1}. \tag{4}
```
Choose a joint subsequence on which b/D and x_B/D converge, and choose shrinking neighborhoods U of A whose boundaries are null for the weak limit omega. For fixed M and U, the route count and the tangent-measure bound give
```math
\omega(U)\le X+\mu(S_{M,\delta})+\frac{B}{M+1},
```
where X=lim x_B/D, B=lim b/D, and δ is the width of U. Here weak convergence applies because the boundary of U is omega-null. First let δ tend to zero at fixed M, so μ(S_{M,δ}) tends to zero; then let M tend to infinity. Continuity from above gives omega(A)<=X. Since o<=omega and o<=2nu, every atom of o lies in the countable atom set of nu. Exhausting that set by finite A shows that the outer terminal measure's total atomic mass is at most X.

Taking atomic masses in (3), the exceptional terminal measure has total mass at most lim P_exc/D, while the outer terminal atoms cost at most lim x_B/D. Hence
```math
2a\le\lim\frac{x_B+P_{\rm exc}}D.
```
Together with a>=2s_2, this proves (1) on the finite-liminf subsequence, and therefore on the full sequence.

## Adversarial checks

- The route partition is the canonical Section 63 partition of the full outer walk. It keeps bridge excursions and repeated vertices in their distinct occurrences; routes are not identified by endpoints or labels.
- A route's endpoints are consecutive, distinct loaded hull vertices, so unit separation supplies the lower bound one needed to rule out a zero limiting signed sum.
- The finite direction set depends on the fixed finite atom set and fixed length cutoff M. The order of limits avoids an unsupported uniform bound as M->infinity.
- Long routes are charged directly by their M+1 distinct edge occurrences. The tangent-measure estimate only handles short routes whose every edge direction lies in U.
- Mantel is applied only to finite crossing graphs of actual tracks, not a phase-collapsed graph. The finite collapsed-phase triangle regression therefore does not refute the argument.
- No condition q/D->pi or m=o(D) is assumed. The proof only uses p/D->pi, q<=p, and full source separation.
- The source verifier passes its 12 rational budget checks, 1,677 exact full-source pair checks, and 462 exact convex-support checks. Its q_hi assertion checks the constant in the Theorem B endpoint; those finite arithmetic/geometric checks do not verify route exposure, weak limits, or the asymptotic theorem.

## Verdict and frontier effect

**PASS — promote C-ATOMIC-OUTER-ROUTE-EXPOSURE.** Removing m is justified by an outer-route exposure count; it is not an algebraic consequence of Theorem A alone. The theorem strengthens the low-t_D metric restriction to g-4z >= (c-o(1))D, and the source verifier's q/D constant check is correct for this stronger result.

This still supplies no upper bound for g-4z, no finite competitor, and no contradiction with the canonical lower bounds on q. It does not close C-II or Level I. Theorem C and the companion sharp-orbit report remain unreviewed.

Promotion transaction: PR #812 merged as `2cfa44ede117adac592fbe26351fd3e546969879`, advancing state to `2026-10-08.audit.130`. Protected `state-consistency` check `37730857919` and post-main workflow `37731378719` both passed.
