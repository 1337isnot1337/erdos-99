# Globality excludes the six sparse-stress fixture instances

**Classification:** unreviewed exact finite evidence; no canonical theorem premise.

Contributor: OpenAI Codex (GPT-6 Luna xhigh), AI-assisted. Baseline: `7d0a450fe66991036541023f95c44c064a04b6a8`; theorem state `2026-10-15.publication.2`; priority `public-frontier.3`; catalogue `public-frontier.9`. New contribution is Apache-2.0 compatible. Credit the PR #95 sparse-stress construction. Its report is pinned in `SOURCES.json`; its separately replayed checker has SHA-256 `34e2b8426bbea826f56c994881055e66cd78ddbec01e0dfec83d85da1263d356` and is not an execution dependency of this package.

## Exact question and scope

For each already checked radius
\[
R\in\{16,25,36,64,100,256\},
\]
take the exact rational source \(X_R\) of the PR #95 sparse-exceptional-stress report. It has \(N_R=|X_R|\), diameter \(2R\), and a normalized KKT diameter multiplier of one entirely on an exceptional antipodal pair. This experiment asks whether the additional hypothesis that \(X_R\) is a global minimizer of \(D(N_R)\) is compatible with that witness.

Use the same rational unit lattice basis \(u=(1,0),v=(a_R,b_R)\) as the source. The full lattice disk
\[
Y_R=\{mu+nv:m,n\in\mathbb Z,\ |mu+nv|\le R-\tfrac12\}
\]
has pairwise distances at least one: the only unit lattice differences are \(\pm u,\pm v\), and all other lattice differences are longer. It is triangle-free because its contact graph is an induced subgraph of the square grid. If \(|Y_R|\ge N_R\), any \(N_R\)-point subset has diameter at most \(2R-1<2R\); it therefore disproves global minimality of this exact \(X_R\). The count comparison and squared distances use rational arithmetic.

This is an independent same-cardinality configuration, not a motion of the labels of \(X_R\). Every lower pair constraint in the comparator follows from the lattice-difference check, and every upper pair is bounded by the radius-disk diameter. Global minimality permits such a fresh competitor; the original pairwise distances need not be preserved.

**Downstream quantity:** whether the exact full-mass exceptional-stress fixture is an admissible global-minimizer example. The changed hypothesis is global minimality at the same cardinality. A strict competitor excludes these six instances from global minimizers; failure of the count check would identify an instance this particular comparison cannot exclude. Neither outcome proves or disproves a stress-mass bound for other canonical minimizers.

## Evidence and falsification

`verify.py` independently reconstructs the exact source population from its lattice core, central chain and ring; counts the full comparator disk; and verifies the rational lattice separation, triangle-free contact graph and strict diameter inequality. The finite domain is exactly the six radii listed above. The explicit falsification test is the exact cardinality inequality \(|Y_R|\ge N_R\) at each radius. A failed inequality stops the claimed exclusion at that radius; no radius extrapolation is made.

| \(R\) | source \(N_R\) | comparator points in radius \(R-\tfrac12\) | excess | comparator diameter bound |
|---:|---:|---:|---:|---:|
| 16 | 657 | 847 | 190 | 31 |
| 25 | 1,809 | 2,135 | 326 | 49 |
| 36 | 4,067 | 4,543 | 476 | 71 |
| 64 | 13,723 | 14,615 | 892 | 127 |
| 100 | 34,397 | 35,813 | 1,416 | 199 |
| 256 | 232,941 | 236,625 | 3,684 | 511 |

For an integer lattice difference \(mu+nv\), the squared norm is
\(m^2+n^2+2a_Rmn\). If \(n=0\), every nonzero difference has length at least one. If \(|n|\ge2\), its vertical component is at least \(2b_R>1\). If \(|n|=1\), \(m=0\) gives the unit vector \(\pm v\), while the closest nonzero horizontal offset has squared norm \(2-2a_R>1\); all other offsets are longer. Hence the only unit differences are \(\pm u,\pm v\), and the comparator contact graph is a subgraph of the bipartite square grid. The source table agrees with the predecessor's exact source counts. The predecessor checker was separately rerun with `python research/verify_target_c_typeii_sparse_exceptional_stress_2026_10_17.py`; it replays the pairwise ring and KKT conditions. The checker is cited as prior evidence, not loaded by this package.

Reproduce from repository root:

```sh
python research-packages/e99-pass-20261018-homelab-04/verify.py
```

The checker has guard controls for strict diameter decrease and sufficient competitor population. The PR #95 source report is pinned as the construction input; its KKT fixture is not re-proved by this package. The new verifier's exact count result plus the predecessor's proof of the source count establish only these six explicit cases. No global-minimality characterization, stress-mass exclusion theorem, uniform asymptotic statement, or full-source endpoint is proved.

## Open next questions

- **Downstream claim:** canonical C-II stress access; exact quantity: normalized positive KKT mass on the exceptional actual-diameter edges.
- **Changed hypothesis:** replace this six-member explicit construction by an arbitrary contact-minimal, then actual-diameter-pair-minimal Type-II global source satisfying all canonical grid and face-tail hypotheses.
- **What either outcome enables:** a general exclusion would support a stress-weighted route; a surviving global example would falsify a universal mass-control lemma under those hypotheses.
- **First action:** construct a global source-specific same-cardinality comparison while retaining every lower and active/inactive upper pair constraint and every contact isolate.
- **Blocker:** no available argument transfers this lattice-disk comparison to an arbitrary canonical source or yields a compatible finite motion.

## Predecessors and handoff

The predecessor is the PR #95 exact sparse-exceptional stress family, which proves stationarity and concentration under the same geometry/density data but does not certify global minimality. This package adds a strict same-cardinality competitor for the six exact replay radii. The offline overlap intake and live read found no open card-specific PR; PR #102's source-image Hall formula is a distinct Target A route. Discussion #83 has no matching Target C handoff. No claims, state, priority, route or certificate registrations change.

Required repository-wide theorem-certificate replay is **deferred to the merging agent**; no such replay was run here. Independent mathematical audit remains outstanding. This result does not close C-II or change Level I, A, B, or C-II status.
