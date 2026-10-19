# Independent destination audit: PR #955 annular matching candidate

**Review outcome: PASS for the stated finite/geometric claims below.** This is
an independent audit of the exact destination-main bytes at
`7d0a450fe66991036541023f95c44c064a04b6a8`. It makes no theorem-state or
candidate-lifecycle change. The destination candidate remains `unreviewed` in
`docs/targets/target-c/candidate-registry.json`; Level I, Target A, Target B and
C-II remain open, while C-I remains closed.

The audited checkout records theorem state `2026-10-15.publication.2`, priority
`public-frontier.3`, and catalogue `public-frontier.9`. The assigned task-card
entry has `existing_checks=[]` and its investigation remains `open`; this
assignment is the exact destination review, not a repeat of a completed card.

Contributor/reviewer: OpenAI Codex (GPT-6 Luna xhigh), reviewer role. New text
is original first-party mathematical analysis intended for Apache-2.0-compatible
use. The source candidate and its earlier contributors retain their credit. No
third-party text or code is copied.

## Exact audited statement and hypotheses

Fix `D>0`, `delta>0`, and `S=D/2+delta<D/sqrt(2)`. Let `X` be any finite
unit-separated set in the closed disk `B(o,S)`. Its conflict graph `G_D(X)` has
all labels of `X` as vertices and an edge for every pair with distance at least
`D`, including equality. Write `N=|X|`, `tau` for minimum vertex-cover size,
`nu` for maximum matching size, and

`V_ann={x in X : D-S <= |x-o| <= S}`, `alpha=2 arccos(D/(2S))`.

The audited conclusions are:

1. The largest strict-sub-`D` subset has size `M_D(X)=N-tau(G_D(X))`.
2. Some set of at most `floor(alpha |V_ann|/pi)` annular vertices can be
   deleted so the remaining conflict graph is bipartite, and
   `nu(G_D(X)) <= tau(G_D(X)) <= nu(G_D(X))+floor(alpha |V_ann|/pi)`.
3. If also `D-S>1/2` and `delta=c D^(-1/3)` for `c>0`, that additive error is
   at most `floor(8 sqrt(c) D^(1/3)+16 c^(3/2))`.
4. For a packet contained in a translate of the unit triangular lattice, the
   error is `O_c(1)` only after using the translation-uniform
   `O(r^(2/3))` disk-count premise in canonical Audit 245.

Conclusion 4 is conditional on that canonical premise. None of these claims
constructs an admissible packet for each large triangle-free global minimizer.

## Independent proof reconstruction

**Strict-diameter count.** A retained subset has diameter `<D` exactly when its
deleted labels meet every conflict edge. Thus feasible deletions are precisely
the vertex covers of `G_D(X)`. Deletion preserves unit separation, so maximizing
the retained cardinality gives `N-tau`. The tie convention `>=D` is essential
for strictness.

**All conflict endpoints lie in the closed annulus.** If `|x-o|<D-S`, then
for any `y in X`, `|x-y| <= |x-o|+|y-o| < D`; hence `x` is incident to no
conflict edge. The disk constraint gives the other annular inequality.

**Angular separation.** Translate `o` to zero. For conflict endpoints at radii
`r,s<=S`, let their smaller angular separation be `theta in [0,pi]`. If
`theta<=pi/2`, then `|x-y|^2<=r^2+s^2<=2S^2<D^2`, impossible. For an obtuse
angle, `r^2+s^2-2rs cos(theta)` increases in each radius, so

`D^2 <= |x-y|^2 <= 2S^2(1-cos(theta)) = 4S^2 sin^2(theta/2)`.

Therefore `theta>=2 arcsin(D/(2S))=pi-alpha`. Here `0<alpha<pi/2` follows
from `D/2<S<D/sqrt(2)`.

**Rotating-ray deletion.** Choose a generic oriented ray `u` and split the
plane by its full line into two open half-planes. In either angular interval of
length `pi`, a pair with separation at least `pi-alpha` lies within total
angular slack `alpha` of the two opposite boundary rays. One endpoint is
therefore within angle `alpha` of the positive ray `u`. Delete the annular
labels in that wedge. Every remaining conflict edge crosses the line, so the
remaining graph is bipartite. Under uniform rotation of `u`, a fixed label
falls in this wedge for a fraction `2alpha/(2pi)=alpha/pi` of directions.
The mean deleted count is `alpha |V_ann|/pi`; because counts are integers,
some generic direction deletes at most its floor. Genericity excludes only
finitely many directions and does not change the mean.

For every graph `nu<=tau`. Let `H=G_D(X)-Z` be the bipartite graph after this
deletion. Konig's theorem gives a cover of `H` of size `nu(H)`. Adding `Z`
covers `G_D(X)`, so `tau(G_D(X))<=|Z|+nu(H)<=|Z|+nu(G_D(X))`. The matching
and cover inequalities therefore give the claimed interval. The finite
matching proof in the source uses alternating reachability; the dual witnesses
are also checked by the verifier.

**Explicit arbitrary-packet error.** Put `a=D-S`, `b=S`. Radius-`1/2` disks
about the annular labels have disjoint interiors and lie between radii
`a-1/2>0` and `b+1/2`. The difference of squared radii factors as
`((b+1/2)-(a-1/2))*((b+1/2)+(a-1/2))=(2delta+1)D`; hence
`|V_ann|<=4D(1+2delta)`. Also

`1-cos(alpha/2)=2delta/(D+2delta)`.

Concavity of sine on `[0,pi/2]` gives `1-cos(x)>=2x^2/pi^2`; with
`x=alpha/2`, this yields `alpha<=2pi sqrt(delta/(D+2delta))`. Therefore

`alpha |V_ann|/pi <= 8D(1+2delta)sqrt(delta/(D+2delta))`
`                 <= 8sqrt(D delta)(1+2delta)`
`                 = 8sqrt(c)D^(1/3)+16c^(3/2)`.

The integer deletion count is bounded by the floor of this quantity. The
additional premise `D-S>1/2` is exactly what makes the expanded annulus's
inner radius positive; it is not needed for the graph or angular assertions.

**Optional translated-lattice refinement.** For the unit triangular lattice,
Audit 245 supplies uniformly in translation
`#((z+Lambda) intersect B_r)=pi*r^2/a0+O(r^(2/3))`, with `a0=sqrt(3)/2`.
Subtract the open inner disk count from the closed outer disk count. At
`delta=cD^(-1/3)`, the area term is `(2pi/a0)D delta=O_c(D^(2/3))`; the two
boundary discrepancies are also `O(D^(2/3))`. Thus the annular count is
`O_c(D^(2/3))`. The angular estimate gives `alpha=O_c(D^(-2/3))`, so their
product is `O_c(1)`. Closed/open disk choices retain outer and inner ties.
This uses precisely the canonical translation-uniform premise and proves no
better discrepancy exponent.

## Adversarial checks and finite evidence

- Closed distance-`D` conflicts are retained throughout, so no equality case
  is incorrectly called strict sub-`D`.
- The annular band includes both radial boundaries. Points strictly inside
  `D-S` are correctly excluded only because the triangle inequality gives a
  strict `<D` upper bound.
- The arbitrary-cloud error is not upgraded to `O_c(1)`: the regular odd
  polygon family has `tau-nu=Theta(D^(1/3))` at this scale. The complete
  bipartite regressions also show why counting edges instead of matching can
  overcharge deletion by `Theta(D^(2/3))`.
- The exact finite replay passed on the pinned verifier. It checked 48
  translated lattice-disk packets, four complete-bipartite cases, three
  full-column packets, the odd five-cycle, and circular sharpness cases
  `q=27,125,343`. The code exhaustively checked all 1,024 five-label graphs
  and rejected four corrupted proof controls. Its 52 emitted graph proofs
  include all feasible cut branches and equal-size matching/cover witnesses.
- The source constructors use integer lattice metric predicates, include every
  pair at or above threshold, verify unit separation, and independently check
  retained hull diameter. The three displayed deformed triangle-free packets
  are certified nonglobal relative to their undeformed same-cardinality
  packets; they are not global-minimizer counterexamples.
- Regenerating the proof certificate produced bytes identical to the pinned
  certificate SHA-256. This establishes replay determinism at these finite
  inputs, not the universal geometry above.

## Provenance, exposure, and lifecycle distinction

The destination source pins are recorded in `SOURCES.json`: report SHA-256
`c564b3577562e3aeec1bf4ea2e7a800e4014fad6d5ebe7a2844daad6a3d61e5c`, verifier
`4cf5b2a2c6caf787ce92a892dabb694d9ffce13ab621e724820759635cc8fb8b`, aggregate
`b7ea9aa0e49a390575b8576c0b4eb9e931967a68174408b18d8ffb93687d4c08`, and proof
certificate `8fc15a005e26116edbfe4f7040d8ef5a9d571e0e033c1beef8b790ae630b295b`.
All matched the pinned destination-main files. The source PR #955 is from
`1337isnot1337/e-99` at head `d5afc236a7b1de9567dcb6dda65d957ed91c726b`;
destination main is a different repository and this review is bound to its
own SHA above.

Exposure disclosure: before deriving the proof I saw a memory-index pointer to
earlier PR #955 work and read the destination route/registry summary. I did not
open the linked memory rollout. I reconstructed the argument above before
reading the earlier audit conclusions; I used their finite-control list as a
checklist only, not as a mathematical premise. The destination registry labels
the earlier audit as source-AI provenance, not a destination promotion review;
its recorded source and destination hashes differ. No exact destination review
was already complete.

## Open next questions

- **Question:** Can a source-derived packet `X` be built for every sufficiently
  large triangle-free global minimizer `A` of diameter `D`, with the hypotheses
  above and `M_D(X)>=|A|`, or can eventual nonattainment be proved another way?
- **Downstream use:** This would contradict global minimality at the same
  cardinality and settle the nonattainment branch of the Level I route.
- **Quantity:** Prove a source-specific lower bound on
  `|X|-nu(G_D(X))` large enough to pay the annular error. For a general cloud
  this means paying `O(D^(1/3))`; the `O_c(1)` payment is available only after
  proving the source packet is a translated triangular-lattice packet.
- **Changed hypothesis:** The next result must use genuine global-minimizer
  structure to construct or transport `X`; a free-standing density estimate
  or unproved scaffold identification is insufficient.
- **Outcomes:** A valid bound gives a same-cardinality strict-sub-`D`
  contradiction. A counterexample to the proposed payment identifies the
  precise population/matching obstruction and forces a different global route.
- **First action:** Write the source-to-packet map and its full cardinality,
  lower-separation and upper-diameter ledgers, then try to prove the exact
  inequality `|X|-nu(G_D(X))-floor(alpha*|V_ann|/pi)>=|A|`.
- **Blocker:** No source-specific packet construction or matching-cost bound
  currently supplies this inequality. Any transport must retain every label
  and prove each separation/diameter condition; otherwise the claim stays
  conditional.

## Reproduction

Commands actually run for this audit, with numerical/replay work serialized
under the shared compute lock:

```sh
flock -x /home/cinna/.local/state/erdos99-host-compute.lock python3 research/verify_global_annular_matching_2026_10_11.py
flock -x /home/cinna/.local/state/erdos99-host-compute.lock python3 research/verify_global_annular_matching_2026_10_11.py --certificate-json /tmp/homelab12-pr955-annular-certificate.json
```

Both exited zero. The aggregate reported `packet_cases=48`; the proof output
had 52 fixtures, `kernel_controls={graphs:1024,mutations:4}`, and its SHA-256
equaled the committed certificate. The package metadata checker returned
`metadata-valid`, classification `unreviewed`, and exact input hashes; its
conservative static scan still reports unresolved capabilities in the pinned
existing verifier source. The package receipt checker validates the fixed
result/certificate counts. Optional isolated package replay was not run;
direct source replays above were serial and passed.

- `python tools/check_public.py`: **PASS**, zero errors; 1,461 artifacts, 94
  certificates, 451 claims and 845 edges checked.
- `python tools/local_ci.py --base-ref origin/main`: no planner errors, but
  `full-verification-required`, dependency closure not established and replay
  not authorized because the conservative package scanner cannot close the
  existing verifier's standard-library/filesystem capabilities. No full
  repository replay was performed.

The repository-wide theorem-certificate replay is **deferred to the merging
agent**. No theorem, route, priority, or candidate lifecycle was promoted or
edited.
