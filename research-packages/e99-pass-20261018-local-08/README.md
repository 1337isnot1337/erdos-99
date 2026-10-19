# Strict packet restoration after supplied-W stress deletion

**Classification: unreviewed conditional rule with an exact finite fixture.**
The fixture is not a global minimizer and does not change Level I or C-II.

Contributor: OpenAI Codex, GPT-6 Luna xhigh (local-08). Task:
`compute-c-stress-deletion-restoration-regression`. Baseline:
`7d0a450fe66991036541023f95c44c064a04b6a8`; state
`2026-10-15.publication.2`; priority `public-frontier.3`; catalogue
`public-frontier.9`. AI assistance produced the proof note and exact checker.
The work is offered under Apache-2.0 and reuses the cited project sources without
copying third-party material.

## Conditional restoration rule

Let `A` be a triangle-free canonical C-II source with `D=diam(A)>=9`, chosen
first with minimum unit-contact count and then minimum actual-diameter-pair
count among global minimum-diameter sources of its cardinality. Let `B` be the
full actual-diameter endpoint set, `V` the nonisolated contact core, and
`I=V\B`. For a supplied nonempty `W subset B`, take the deletion
`R=U union Y` from the canonical almost-accessible stress-transversal theorem,
where `U subset W`, `Y subset I`, and `|R|<=s_Z+1`; it kills every normalized
retained-source stress. It loses `k=|R|` labels. All source labels, including
contact isolates, are part of the pair ledger.

Suppose there is a packet `Z` of exactly `k` new labels when `R` contains at
least one nonisolated unit-contact vertex. Otherwise suppose `A\R` contains a
nonisolated unit-contact vertex `v` and `|Z|=k+1`. Require every pair in `Z`,
and every pair from `Z` to `A\(R union {v})` (omit `v` from this deletion term
when it is not used), to satisfy the **strict** squared-distance bounds

```text
1 < |z-z'|^2 < D^2.
```

Then replacing `R` (and `v` in the second case) by `Z` preserves cardinality,
unit separation and diameter at most `D`. No packet edge is a unit contact or a
pair at the old diameter `D`; every old pair among retained labels is unchanged.
If the new diameter is still `D`, its actual-diameter graph is a subgraph of the
old graph induced on retained labels, so deleted old diameter pairs may
disappear and **no replacement pair at `D` can appear**. If the new diameter is
`D'<D`, pairs involving `Z` can become new actual-diameter pairs at `D'`; the
strict diameter decrease itself contradicts global minimality, regardless of
that replacement graph. In the first case at least one old contact disappears
and none is added. In the second case the same holds because `v` is
nonisolated. Thus the endpoint either has diameter below `D`, or has diameter
`D` and fewer contacts, contrary to the source normalization.

This is a sufficient packet rule, not a packet-existence theorem. Its exact
packet count for this repair is `k` or `k+1` labels respectively. If `R` consists
only of contact isolates, the extra label must remove a contact vertex outside
`R`; isolates retained outside the deletion remain labels and every one of their
new pair distances must be checked.

## Exact rational fixture

The verifier uses eleven source labels:

```text
p_i=(i,0), 0<=i<=9;    q=(1/2,11/10).
```

The source has `D^2=81`, contact path `p0-p1-...-p9`, and sole actual diameter
pair `p0-p9`. `q` is a contact isolate; its squared distance to `p_i` is
`(i-1/2)^2+121/100`, which is strictly between `1` and `81` for every `i`.
The normalized row-system stress has upper weight `beta(p0p9)=1` and lower
weight `alpha(p_i p_(i+1))=9` on all nine contacts. Exact force balance and the
normalized linear system give affine stress dimension zero. For `W={p0}`,
`R={p0}` has size `s_Z+1`; deleting it removes the only old-`D` row, so the
retained row system has no normalized stress. The retained isolate `q` remains
in every pair check.

The strict replacement `r=(8/5,11/10)` has squared distances strictly between
`1` and `81` to each of `p1,...,p9,q`. Replacing deleted `p0` by `r` preserves
the eleven-label cardinality, leaves eight unit contacts, and gives maximum
squared distance `3673/50<81`. The old pair `p0-p9` disappears; `p9-q` is the
replacement actual-diameter pair at the smaller endpoint diameter. `q` and
inserted `r` are contact isolates. The verifier reports the old-`D` and new-`D'`
graphs separately.

This is an exact rational stress-row fixture, not a canonical source: it is not
proved globally optimal, and its collinear contact core does not satisfy the
full rigidity hypotheses used in Audit.171. It checks the supplied-`W` deletion
bookkeeping and the full-pair restoration distinction only. The general rule
above is conditional on an actual canonical source and the Audit.171 deletion.

The failure control restores the deleted point at `p0` itself. This weak packet
has unit pairs along the full path and the old diameter pair `p0-p9`, so it
restores the old contact and actual-diameter constraints and yields no
improvement. This explains why `>=1` and `<=D` margins do not support the rule.

The verifier independently enumerates every pair in all three configurations,
checks the isolate and triangle statuses, and verifies the stress balance using
exact `Fraction` arithmetic. Run from the repository root:

```sh
python research-packages/e99-pass-20261018-local-08/verify.py
```

## Scope and predecessors

Audit.171 proves the supplied-`W` deletion but explicitly leaves restoration
open. The October 5 one-spare-site report proves the strict-packet
contact-minimality argument in a source-independent form. This package states
the deletion-aware `k` versus `k+1` threshold and gives an exact rational
stress-deletion fixture with a retained isolate and complete pair ledger. It
does not duplicate PR #102, whose source-image Hall overlap result concerns
Target A.

No source-extraction theorem supplies such a strict packet for every canonical
C-II minimizer. No global-minimizer quantifier, eventual statement, C-II closure,
or Level I conclusion follows. Required repository-wide certificate replay is
deferred to the merging agent. The exact fixture is independently reproducible;
no independent mathematical audit has been performed on this package.

## Open next question

- **Downstream decision:** whether a canonical supplied-`W` deletion can be
  restored to contradict C-II contact-minimality or diameter minimality.
- **Exact quantity:** strict full-pair packet capacity relative to the
  deletion size `k`, with threshold `k` when a contact is deleted and `k+1`
  when an additional contact vertex must be removed.
- **Changed hypothesis:** extract the strict packet from the actual canonical
  source, including every contact isolate and every old diameter pair.
- **What either outcome enables:** a uniform packet theorem gives the desired
  same-cardinality contradiction; a counterexample identifies a missing
  capacity or guard-motion condition.
- **First step:** apply the exact packet-distance check to a source-extracted
  candidate region and its complete pair table.
- **Blocker:** no current theorem produces this packet for every canonical
  source, and fixed-wall capacity is known to fail in specified models.
