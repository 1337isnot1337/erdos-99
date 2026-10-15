<!-- theorem-state: {"artifact_id":"ART-92297DF7A3DF","canonical":false,"claim_ids":["C-SORTED-RATE-NESTED-ENERGY-EQUALITY-REGRESSION"],"claim_statuses":{"C-SORTED-RATE-NESTED-ENERGY-EQUALITY-REGRESSION":"regression"},"index":"docs/state/artifact-index.jsonl","status":"regression","target":"target-c"} -->
# Independent audit: sorted-rate packet energy equality

Date: 2026-10-07. Source branch: `research/sol/target-c-owner-order-closure-20261006`, immutable snapshot `0d3b0182c064f73d2a6a64452ee01d140f1b1475`. Source report: `docs/reports/target_c_sorted_rate_packet_classification_2026-10-06.md`.

**Verdict: REGRESSION VALID — promote only the explicit finite packet and ring-energy equality.** The report's projected-permutahedron proof, local uniqueness theorem, and highest-population exclusion are not included in this audit and remain unreviewed.

## Exact claim

Fix an integer (M\ge3), let
[
\Lambda_M=\{M-1,M-3,\ldots,-M+1\},\qquad
C=\frac{M(M^2-1)}6,
]
and choose any ordering (\tau_0,\ldots,\tau_{M-1}) of (\Lambda_M). For the six-sided curved unit wall whose side-edge angle rates are the increasing ordering of (\Lambda_M), the source's sorting construction gives, for every fixed ordering (\tau) and all sufficiently small positive (\theta), an exactly unit-separated finite packet with:

- (N=3M^2-3M+1) interior sites, or (N-1) sites after deleting the center;
- an exact unit equilateral triangle remaining after center deletion when (M\ge3);
- the same nested-ring energies (E_s=12C=2M(M^2-1)) for every (s=0,\ldots,M-1).

Here (E_s) is exactly the ring-plus-radial-chain quantity in canonical claim `C-NESTED-HEXAGON-STRESS-ENERGY-DEMAND`. Thus no strict bound (E_s<12C) follows from its full unit-separation and six-guard hypotheses alone. This is not a triangle-free packet or a global-minimizer regression.

## Independent reconstruction

Identify the plane with \(\mathbb C\), set (u=1), (v=e^{i\pi/3}), and (w=v-u). Put
[
z_h=e^{i\tau_h\theta},\quad
S_r=\sum_{h<r}z_h,
]
and let (U_{r,j}) be the sum of the (j) vectors (z_h), (h<r), with the (j) smallest rates. In one triangular sector set
[
p_{r,j}=S_r u+U_{r,j}w\quad(0\le j\le r\le M);
]
rotate this sector six times and identify shared radial-edge points. Since the rates are permuted, (S_M) is the prescribed wall-side vector. The layer (r=M) is exactly the wall boundary; at (	heta=0), the interior layers are the radius-((M-1)) triangular grid.

For fixed (M), every pair whose limiting distance exceeds one keeps strict upper slack for sufficiently small (	heta). Every limiting unit pair is in one of three local classes: a same-layer edge has difference (z_hw); one of the two parent edges to the preceding layer has difference (z_hu) or (z_hv); the other parent edge has squared length
[
2-2\cos\!\left(\frac\pi3+|\tau_h-\tau_{h'}|\theta\right)>1
]
for sufficiently small positive (	heta). The wall edges are the same unit (z_hw) edges. The rate differences are nonzero, and there are finitely many pairs for fixed (M), so one positive onset works for the whole packet. Strict containment of the (r<M) sites follows by continuity from their strict containment in the limiting regular hexagon.

For each insertion (h=r-1), let (k) be the number of earlier rates below (	au_h). The three sites (p_{r,k},p_{r,k+1},p_{r-1,k}) have pair differences (z_hw,z_hu,z_hv), all of length one. This is one exact equilateral triangle per sector at layer (r). Layers (r=2,ldots,M-1) give (6(M-2)) triangles wholly inside the wall that do not use the center. Since (M\ge3), center deletion leaves at least one such triangle.

Differentiating the explicit packet gives the nested energy directly. On ring (s), each rate (	au_h) with (h<s) occurs once per sector as an edge whose velocity difference has squared norm (	au_h^2); on the six radial chains, each (h\ge s) occurs once per sector with the same squared norm. Therefore
[
E_s=6\sum_{h<s}\tau_h^2+6\sum_{h\ge s}\tau_h^2
=6\sum_{h=0}^{M-1}\tau_h^2
=6\cdot\frac{M(M^2-1)}3
=12C.
]
This holds for every ordering, every ring, and every fixed (M\ge3).

## Adversarial scope and computational evidence

The packet has actual unit triangles. It refutes a strict ring-energy gap derived solely from the physical unit lower constraints and the six guard expansion. It does not refute a stronger statement whose hypotheses already require a triangle-free packet, and it supplies no triangle-free competitor or canonical-source extraction.

The exact source verifier was rerun at the immutable snapshot. It checks 14 cases for (M=3,4,5,6): 37,773 full-pair distances, 2,412 unit-row first variations, 1,016 subset sums, all reported ring energies, and full pinned ranks modulo (10^9+7) for those sampled matrices. Exact arithmetic is in \(\mathbb Q(\sqrt3)\) and rationals. The finite rank checks do not prove the all-(M) theorem; the explicit construction and counting argument above do. The certificate does not verify arbitrary-cloud compactness, local pinned equilibrium continuation, highest-population exclusion, global optimality, or Level I.

After the audited snapshot, the branch advanced to `bf288c82e8a62466d5580025c94e750a177e63e2`. The sorted-rate report and saved certificate are unchanged. The verifier diff only adds an optional tangent override to its geometry helper; its default sampled run and the claim audited here are unchanged. The separate one-deficit root-release lead on that newer tip is outside this audit.

## Canonical disposition

Promote only `C-SORTED-RATE-NESTED-ENERGY-EQUALITY-REGRESSION). Keep the source report's finite local classification and arbitrary (z=N) highest-population result unreviewed. The equality branch of audit.71's local energy demand has explicit feasible realizations, so subsequent work must use a triangle-free condition or another hypothesis that excludes these packets; no strict shortfall can be obtained from the audited energy constraints alone. Target C-II remains open.
