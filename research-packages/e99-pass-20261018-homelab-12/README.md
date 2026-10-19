# Independent exact-head audit: supplied slow-chart contact-port exclusion

**Classification:** unreviewed reviewer evidence; no theorem promotion.  
**Reviewing agent:** OpenAI Codex, GPT-6 Luna xhigh.  
**Originating agent:** not identified in the pinned artifact.  
**Repository/base:** `1337isnot1337/erdos-99` at `7d0a450fe66991036541023f95c44c064a04b6a8`.  
**State / priority / catalogue:** `2026-10-15.publication.2` / `public-frontier.3` / `public-frontier.9`.

This is an independent reconstruction of only
`TARGET-C-SLOW-CHART-CONTACT-PORT-COVER-EXCLUSION-PR947`,
[the published Audit.254 artifact](../../docs/audits/target_c_slow_chart_contact_port_cover_independent_audit_2026-10-10.md).
At the pinned destination base, that artifact is indexed `unreviewed`; its
candidate-registry record says the destination mathematical audit was not
performed. The source PR's PASS/promote wording is historical and is not used as
authority. Source PR [#947](https://github.com/1337isnot1337/e-99/pull/947) was
open at head `1afb7e64d47c5619d872d32759b0e01f1526fd5a`. The only open PR in the
destination repository at review time was unrelated Target A PR #102.

## Frozen artifact bytes

The supplied `candidate.json` destination SHA-256 values were checked against the
files at the launch commit; all three matched. The source GitHub content endpoint
at the pinned PR head also matched each recorded source blob and source SHA-256.

| Artifact | Source blob | Source SHA-256 | Destination SHA-256 |
| --- | --- | --- | --- |
| `docs/audits/target_c_slow_chart_contact_port_cover_independent_audit_2026-10-10.md` | `246844015df1544acc8732ff8f6c47005583f935` | `8a63e14ea5787f2a120c46d0a48c2f6f42064372baf23d37fb62f0e86b675f73` | `4f40354d0af913209245992c18e88680ccf65973d68265ef085c32d4329a9391` |
| `docs/audits/target_c_positive_leaf_anchor_sharpening_independent_audit_2026-10-10.md` | `9668230200c9c2cac9a87d515bd31449bf487a35` | `f7df6238d32925d18a2a593f25ff631ef29d8fcd16e3767235f8e3c21dd51cf8` | `c46e90b1975345be2704b4df3085d63f5b84b15402ae6f9214a49faa3e3f32f7` |
| `docs/audits/target_c_referee_run_ledger_2026-10-10.md` | `59224819f8e5df1ffba6f2d32194ddebc2fb31f4` | `99a04e0c2505d7eb01d0a05388fd4fb92be78addfd4f8240a62ce78508c7768c` | `a113dd7604cad043df72e0fe29cfc8487b808acc6ce0dd86ea1d9d09859f7e7e` |

The candidate's current destination status remains `unreviewed`. The canonical
dependencies below retain the scopes recorded at this exact base.

## Exact question and hypotheses

Let `A_D` be a sequence of canonical post-ZF, contact-minimal then actual-diameter-
pair-minimal, triangle-free C-II global minimizers, with `D -> infinity`,
`C=C_*`, and `H=H_*`. Retain the entire source, including all contact isolates.
Let `B_D` be the loaded endpoint set used by the canonical diameter graph, `q=|B_D|`,
and `h` its positive active diameter-edge count. Supply at most a fixed `J` charts

```text
phi_s(lambda) = lambda + g_s(lambda), lambda in X_s subset Lambda_s,
```

on arbitrary subsets of unit rhombic lattices with basis angle in `[pi/3,2pi/3]`,
and with `|g_s(lambda)-g_s(mu)| <= (K/D)|lambda-mu|` for fixed `K`.

An endpoint is counted as covered when either (L) it is an actual diameter endpoint
with exactly one actual unit neighbor, that contact has positive coefficient in
some normalized full-source KKT stress, and the neighbor is an exact image in one
supplied chart; or (P) it is an actual diameter endpoint with two distinct actual
unit neighbors that are images of the same supplied chart. The question is whether
the combined covered set is `O_{J,K}(D^(4/5))`, hence leaves at least
`D-O_{J,K}(D^(4/5))` loaded endpoints uncovered from `q>=h>=ceil(D)`.

## Independent reconstruction

### Positive-stress leaves

For a leaf `(p,a)`, the canonical full-source anchor theorem
`C-POSITIVE-LEAF-ANCHOR-INNER-BALL-BOUNDARY` gives

```text
dist(a, partial K_D) <= C D^(-1/2),
K_D = intersection over every x in A_D of closed_ball(x,D-1).
```

This is the already canonical rate, and it is sufficient. For any actual diameter
pair `u,v` at distance `D`, let `m=(u+v)/2` and
`c_*=1-sqrt(3)/2`. Every source point `x` is within both radius-`D` disks around
`u,v`, so

```text
|x-m|^2 = (|x-u|^2+|x-v|^2)/2 - D^2/4 <= 3D^2/4.
```

Therefore `closed_ball(m,c_*D-1)` is contained in `K_D`. Also `K_D` is contained
in a radius-`D-1` disk centered at any selected source point. Thus, after recentering
to the inball center, `K_D` has inradius `cD` and outer radius `C'D`, and is an
intersection of disks of radii at most `D`. Isolates remain among the disk centers.

The distinct anchors are unit-separated source points. Assign each anchor to one
chart in which it is an exact chart image, partitioning the anchor set if charts
overlap. Apply canonical `C-SLOW-CHART-NEAR-BOUNDARY-COUNT` with
`rho_D=C D^(-1/2)` and chart-image tolerance `tau_D=0`:

```text
number of distinct anchors
  <= O_{J,K}(D^(4/5) + D*rho_D)
   = O_{J,K}(D^(4/5) + D^(1/2))
   = O_{J,K}(D^(4/5)).
```

An anchor can support more than one leaf endpoint, so count multiplicity. The
endpoints lie on the unit circle centered at the anchor and are pairwise unit
separated. Seven such points force at least one angular gap to be at most
`2*pi/7 < pi/3`, yielding chord distance below one. Thus at most six leaf
endpoints share an anchor. Multiplying by six preserves the `O(D^(4/5))` leaf bound.

The source artifact invokes the proposed `O(D^(-2/3))` Audit.247 anchor candidate,
and the destination candidate registry records that candidate relation without
listing the weaker `C-POSITIVE-LEAF-ANCHOR-INNER-BALL-BOUNDARY` theorem among this
entry's canonical dependencies. At the pinned theorem state, that weaker
`O(D^(-1/2))` anchor theorem is already canonical. Substituting it still gives the
same combined exponent, so the stronger candidate is unnecessary here. This audit
does not review or promote Audit.247's stronger claim, and it does not edit the
candidate registry or theorem manifest.

### Double ports

For two same-chart neighbors `a=phi(lambda_a)` and `b=phi(lambda_b)` of one
diameter endpoint `p`, unit separation gives `1<=|b-a|<=2`. The displacement
Lipschitz bound makes `phi` lower-Lipschitz by `1-K/D`, so for large `D` the
integer label difference is bounded. The rhombic Gram lower bound
`|iu+jv|^2 >= (i^2+j^2)/2` leaves a fixed finite set of label differences.

For each difference, `p` is one of the two intersections of the unit circles
through `a,b`:

```text
p-a = w/2 +/- (Jw/|w|) sqrt(1-|w|^2/4),  w=b-a.
```

The actual `w` differs from its lattice vector by `O_K(D^(-1))`; the square-root
term is one-half-Hölder, including near tangency at `|w|=2`. Hence each offset
places `p` within `O_K(D^(-1/2))` of a translate of the chart lattice. Patch the
convex hull of actual diameter endpoints at scale `r=D^(4/5)`. It has perimeter
`O(D)` and lies on the boundary of the full-source ball intersection
`W_D=intersection_x closed_ball(x,D)`, which has an inball of radius
`(1-sqrt(3)/2)D` and outer radius `O(D)`. On each patch, chart drift contributes
`O_K(r/D)` additional lattice error. The canonical local curved-boundary capacity
estimate, summed over `O(D/r)` patches, the finite offsets, and `J` charts, gives

```text
O_{J,K}( r + D^(1/2) + D^(4/3) r^(-2/3) + D/r )
  = O_{J,K}(D^(4/5)).
```

This is the canonical `C-SLOW-CHART-DOUBLE-PORT-COUNT` scope: arbitrary chart
domains, same chart for both neighbors, all other source points retained, and no
full occupancy, globality, or stress condition needed for this count.

### Union and loaded-endpoint remainder

The two classes need not be disjoint; their union has size at most the sum of their
separate `O_{J,K}(D^(4/5))` bounds. In the post-ZF convention, `q` counts vertices
of the loaded diameter graph and `h` its active diameter edges. Canonical `C-ZRF`
gives `h>=ceil(D)`, while `C-WOODALL` gives `q>=h` for this graph (caterpillar
forest in the forest case, or the single odd-unicyclic case). If the endpoint set
is enlarged to include additional geometric diameter endpoints, its cardinality
can only increase. Therefore

```text
q - number_covered >= D - C_(J,K) D^(4/5),
```

which is at least a positive fixed multiple of `D` for all sufficiently large `D`
at fixed `J,K`.

## Adversarial scope and falsification checks

- The leaf count fails to establish this exponent if the anchor error does not
  decay: the near-boundary term is `D*rho_D`; fixed `rho_D>0` costs order `D`.
  The actual canonical `D^(-1/2)` rate costs only `D^(1/2)`.
- The factor six is necessary because a chart anchor need not identify a unique
  leaf endpoint.
- Zero-stress leaves are excluded; so are double ports whose two neighbors are
  split across different charts. The number of charts must remain fixed.
- Every source point, including contact isolates, remains in the full-source
  separation and disk-intersection hypotheses. No point is moved or deleted.
- The conclusion bounds only these two covered classes. It does not bound the
  uncovered endpoints' contact structure or stress weights.
- No supplied chart atlas is extracted from all canonical sources. No
  same-cardinality source motion or strict-diameter competitor is constructed;
  no C-II or Level I closure follows. The full lower-pair and actual/inactive
  upper-pair ledger becomes relevant only for a proposed competitor, which is
  absent here.

## Exact arithmetic verifier

`verify.py` checks only the exponent arithmetic in the near-boundary and patch
summations. It does not encode the geometric theorems or prove their premises.
The check includes the failure control that a nondecaying boundary error cannot
be silently absorbed into `O(D^(4/5))`.

Commands run at review time:

```text
python research-packages/e99-pass-20261018-homelab-12/verify.py
python -O research-packages/e99-pass-20261018-homelab-12/verify.py
python scripts/research_package.py --package research-packages/e99-pass-20261018-homelab-12 --check-only
```

Repository checks, their actual outcomes, and the PR head are recorded in the
external controller handoff. Required repository-wide theorem-certificate replay
is deferred to the merging agent; no full replay is claimed.

## Downstream use and remaining lemma

This conditional bound controls the exact quantity `q_covered`, the number of
loaded endpoints covered by fixed supplied slow charts as positive-stress leaves
or same-chart double ports. Its result does not change the canonical C-II endpoint
or priority allocation. A useful changed hypothesis would be a source-derived
fixed `J,K` atlas; even then the bound leaves linearly many endpoints outside these
two classes.

**Remaining lemma:** from the `Omega(D)` uncovered loaded endpoints, construct a
same-cardinality full-source placement that preserves every old unit lower bound,
checks every old diameter and inactive upper pair, and either has strict diameter
below `D` or stays at `D` triangle-free while strictly improving the lexicographic
pair (unit contacts, actual diameter pairs). Keep all isolates. This is the next
source-level decision; the present result supplies only a population, not that
placement.

## Provenance and attribution

The reviewed candidate and canonical dependency files are SHA-pinned in
`SOURCES.json`. Their source proof/artifacts remain attributed to source PR #947;
this package does not copy their proof text wholesale. New text and the exact
arithmetic verifier are original Apache-2.0-compatible work. No third-party paper
text or private repository material is copied. This independent review was
prepared by OpenAI Codex, GPT-6 Luna xhigh; no human mathematical review is
claimed. The result remains unreviewed as an artifact and does not alter the
canonical manifest, theorem state, route, priority, release state, or generated
views.
