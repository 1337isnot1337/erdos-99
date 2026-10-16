# Reflected-scale endpoints and capacity regressions (source PR #959)

**Scope:** whole-source Level I comparison; cross-route evidence for Target C.
**Lifecycle:** imported, noncanonical, unreviewed. The theorem-state manifest
remains authoritative; no theorem status changed in this migration.
**Frozen source:** `e-99` main `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`;
open draft PR #959 head `e25041f236d268a7e815dacd346180989690ed71`, tree
`a0b268d8b050e0350c8ae2ffb38c139fc6570dab`; merge base
`a43c69dac7e7b0627dec2900e12c60fd4608d519`.

## What the package establishes

### Exact endpoint decision for supplied parameters

For a finite source, fixed line, offset, and positive squared normal/tangent
scales, each label has two reflected positions. Every pair therefore has a
same-sign squared cost `s_ij` and an opposite-sign squared cost `o_ij`, with
`s_ij <= o_ij`. A full-label endpoint with every squared distance in
`[1,D^2)` exists exactly when no pair has `o_ij < 1` or `s_ij >= D^2`, and the
signed graph of forced opposite/equal signs is parity-consistent. Both
constraints must be retained when one pair forces both parities. This is a
necessary-and-sufficient decision theorem for the supplied parameters and
takes `O(n^2)` arithmetic operations; it does not extract parameters for a
global minimizer.

The paired exact verifier includes a 157-label source with two contact
isolates. It checks all 12,246 pairs and certifies squared diameter `916` to
`865065744/1008005`, while retaining all labels. This source is nonglobal.
An infinite rectangle family also gives strict full-source competitors and
escapes an exact affine/stress obstruction. Its PSD stress is supported on the
boundary; it is not a full-source rigidity or global-optimality result.

### A leading-density obstruction to macroscopic one-step scales

For any sequence of finite unit-separated sources with
`n/D^2 -> pi/(2 sqrt(3))`, if a one-step reflected-scale endpoint retains every
label, remains unit-separated, and has diameter at most `(1+o(1))D`, then both
squared scales tend to one. The proof uses canonical Oler, a full-source
empirical disk limit, and second and fourth moments. It allows arbitrary
offsets and sign assignments, but proves no convergence rate, sign structure,
strict lower-order improvement, or nonattainment. The exact finite moment
identity identifies odd-moment terms that can still affect finite sources.

This result narrows the one-step route: any successful large-source endpoint
must use near-identity scales. It does not rule out such endpoints.

### Steiner symmetrization does not preserve exact capacity in general

Two regressions disprove the proposed implication `N(SK) >= N(K)`:

- A four-label rotated square is a triangle-free global diameter minimizer
  with `N(K)=4` and `N(SK)=3`.
- An unbounded triangle-free rhombus family has exact fixed-container
  capacity `(m+1)^2`, while Oler bounds the symmetrized capacity below it by
  at least `ceil(m/10 - 2/3)`. These large sources are nonglobal for diameter,
  despite optimal fixed-container capacity and asymptotically optimal area
  density.

The first example is finite and does not address eventual minimizers. The
second rules out capacity preservation from triangle-freeness, container
optimality, or leading area density alone; it does not refute a theorem using
the additional geometry of large global diameter minimizers.

## Verification

From the repository root, run:

```sh
python3 research/verify_global_reflected_scale_2026_10_12.py
python3 research/verify_global_steiner_capacity_loss_2026_10_12.py
```

The reports contain the analytical proofs; the scripts check exact finite
fixtures. In particular, the reflection checker does not prove parameter
extraction, and the capacity checker does not prove global optimality of the
large rhombi. The moment report relies on canonical Oler Lemma 21.1 and cites
the isodiametric equality input; no third-party paper or extracted text is
bundled.

## Current frontier and next obligations

Canonical theorem-state is unchanged. The C-II question and Level I remain
open. These whole-source arguments are cross-route tools and do not derive a
C-II hypothesis or conclusion.

The missing Level I implication remains: for every sufficiently large
triangle-free global diameter minimizer, produce a same-cardinality planar
unit-separated endpoint of strictly smaller diameter, or independently prove
an unbounded globally optimal triangle-free family. On the reflected-scale
route, this requires source-derived near-identity parameters and signs that
satisfy every lower and upper pair bound, including isolates. A finite
certificate, an affine obstruction, a boundary stress, or a moment limit is
not that extraction. The Steiner route needs a full-label repacking argument
using source information that survives the capacity counterexamples.

Before duplicating work, compare the separate planar endpoint and palette
route in [PR #958](global-planar-endpoint-palette-pr958.md) and the queued
rank/radius arguments in source PR #960. The packages have different proof
content; shared endpoint goals do not make their claims redundant. Candidate
claims, provenance, dependencies, and obstructions are indexed in the
[machine-readable registry](../../targets/target-c/candidate-registry.json).
Every source path and transformation is recorded in the
[migration ledger](../migration/2026-10-16/ledger/source-pr-files.jsonl), with
the independent scope analysis in the
[scientific reconciliation](../migration/2026-10-16/scientific-reconciliation.md).
