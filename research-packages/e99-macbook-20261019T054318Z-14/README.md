# Independent audit of the finite phase-grid endpoint

**Classification:** independent agent audit of the finite result at pinned PR
#128 head. It is not a canonical Target B result or a proof about global
minimizers.

**Audit verdict: PASS, only for the complete finite-grid statement and exact
rational control in the stated domain.** The source PR's own package remains
marked `unreviewed`; this audit records evidence for its maintainers and makes
no lifecycle or theorem-state change.

Contributor and reviewer: OpenAI Codex (GPT-6 Luna xhigh), MacBook slot
`macbook-14`; this reviewer did not produce PR #128. Baseline:
`7d0a450fe66991036541023f95c44c064a04b6a8`; theorem state
`2026-10-15.publication.2`; priority `public-frontier.3`; catalogue
`public-frontier.9`. Investigation:
`audit-pr128-phase-grid-full-endpoint-macbook-20261019`. Prepared with AI
assistance. No human mathematical review is claimed. Apache-2.0-compatible new
work; the audited source keeps its original attribution.

## Exact lemma, hypotheses, and downstream quantity

Let `M,N >= 1`, let `u,v` be unit vectors with angle
`pi/3 < theta < pi/2`, and define the complete unit-rhombic grid

```text
P = { i u + j v : 0 <= i <= M, 0 <= j <= N, i,j integers }.
```

For `theta_s = theta + s(pi/2-theta)`, `0 <= s <= 1`, write
`c_s = cos(theta_s)`. The exact squared distance for a label difference
`(a,b)` is `q_s(a,b)=a^2+b^2+2ab*c_s`. Every pair remains at distance at least
one, and

```text
diam(P_s)^2 = M^2 + N^2 + 2 M N c_s.
```

Thus perpendicularization preserves all `((M+1)(N+1))` labels and strictly
lowers diameter. At every `s<1`, the unique diameter pair is the positive-sign
opposite-corner pair. At `s=1`, the other opposite-corner pair becomes co-active;
all other source pairs remain strictly below the current diameter. The canonical
defect contraction `theta_s = theta - s(theta-pi/3)` has the opposite diameter
sign: it increases the squared diameter by
`2MN(1/2-cos(theta)) > 0` at its endpoint. It may introduce new unit contacts
at `theta=pi/3`, but it never violates a lower pair bound.

This affects only the exact finite same-cardinality strict-diameter-competitor
claim for a complete rectangular unit-rhombic grid. It does not transfer to an
incomplete crossing graph, multiple grains, an arbitrary jammed source, or any
global-minimizer class. It changes no canonical theorem quantity or status.

## Independent reconstruction

Set `p=|a|`, `r=|b|`. On the perpendicularization path, `c` moves from
`c_0=cos(theta)` down to 0; on phase contraction it moves from `c_0` up to
`1/2`. Thus `0<=c<=1/2` on both paths.
If one label difference is zero, the squared distance is at least one. If
`ab>0`, it is at least `p^2+r^2 >= 2`. If `ab<0`, then

```text
p^2+r^2-2c_s p r >= p^2+r^2-pr = (p-r)^2+pr >= 1,
```

because `p,r` are positive integers. This proves the non-axis lower bound for
every pair, not only contacts or a sample of labels.

For `ab>=0`, termwise comparison with `p<=M`, `r<=N` bounds the squared
distance by `M^2+N^2+2MNc`. For `ab<0`, it is at most
`p^2+r^2 <= M^2+N^2`. Axial pairs are bounded by
`max(M^2,N^2) < M^2+N^2`. These bounds give the maximum-pair formula. When
`c>0`, only the same-sign full corner pair attains it. When `c=0`, both
full corner diagonals attain it. The second diagonal increases from below
`M^2+N^2` to that value; it never replaces the active pair before the endpoint.

The `M x N` rhombi give one crossing for each pair of the two train classes,
so the train-crossing graph is `K_{M,N}`. Orient all edges from the `u`-train
class to the `v`-train class. The signed projective step is `+theta` on every
edge; setting the two class labels to 0 and 1 gives one consistent phase
orientation and defect `delta=theta-pi/3` throughout the grid. In Sections
49–50, defect relaxation means `dot(delta)<0`. For this two-class orientation
that decreases `theta` and increases `cos(theta)`, so the grid diameter
increases. Section 50.3's topological-rank velocity has exactly this sign.

On perpendicularization, `d(theta_s)/ds>0`. The active same-sign corner pair
has derivative `-2MN sin(theta_s) d(theta_s)/ds < 0`. Any other same-sign pair
also decreases or stays fixed. Opposite-sign pairs increase, but their squares
are bounded by `M^2+N^2`, strictly below the moving diameter until `s=1`; only
the full opposite corner pair reaches that bound and becomes co-active at the
endpoint. Axial pairs are constant and strictly below the diameter. Under
phase contraction, `theta` decreases and `cos(theta)` increases, so the
same-sign active diameter increases and remains the unique active pair because
`cos(theta)>0` throughout. Opposite-sign pairs fall; every nonactive same-sign
pair remains below the full-corner maximum by the same termwise bound. This
agrees with Section 50.3's explicit warning that defect relaxation alone is not
claimed to be diameter-nonincreasing.

## Exact six-label replay and wrong-sign control

The rational fixture has `(M,N)=(2,1)` and `cos(theta)=7/25`, with
`0 < 7/25 < 1/2`, so `pi/3 < theta < pi/2`. Its basis vectors are
`u=(1,0)` and `v=(7/25,24/25)`, both exactly unit. It has six labels and
fifteen unordered pairs. Its exact values are:

| Configuration | cosine | minimum squared pair distance | squared diameter | active corner pairs |
| --- | ---: | ---: | ---: | ---: |
| initial | `7/25` | `1` | `153/25` | 1 |
| perpendicular endpoint | `0` | `1` | `5` | 2 |
| phase contraction to `pi/3` | `1/2` | `1` | `7` | 1 |

The old inactive opposite-corner pair has squared distance `97/25` initially,
then reaches `5` at perpendicularization and becomes co-active. The squared
diameter improvement is `28/25`. At the wrong-sign contraction endpoint the
two opposite-sign unit-difference pairs become new unit contacts; separation is
still respected, while squared diameter worsens by `22/25` from its initial
value. The contraction endpoint adds diagonal contacts and unit triangles; it
is only the wrong-sign control, not a triangle-free source claim. The
independent verifier enumerates all fifteen pairs at the initial, perpendicular,
and contraction configurations and tests general
label-difference bounds for all `M,N` in a bounded parameter grid. For each
path it checks both endpoints; since each pair square and the proposed diameter
square are affine in `cos(theta)`, those endpoint checks cover every
intermediate path value.

## Falsification checks and replay

The proof would fail if a non-axis integer pair had squared length below one,
if an inactive upper pair exceeded the proposed moving diameter, if the active
pair formula missed an extremal label difference, or if the phase sign were
reversed. `verify.py` checks exact integer/Fraction arithmetic on the rational
source, the perpendicular endpoint, the phase-contraction control, every pair,
all contact counts, and a deterministic grid of label-difference cases. The
general proof above covers all integer `M,N>=1`; the bounded replay is a check,
not a substitute for that proof.

**Stopping condition:** this finite audit ends once the all-`M,N` inequalities
and the exact six-label control are checked. Any lower-pair violation, an
inactive upper pair exceeding the moving diameter, or a different active-pair
transition within the stated domain would falsify the claim. Do not extend the
argument to incomplete or multi-grain sources within this investigation.

Exact source bytes were read from PR #128 head
`e80e7e35b1130d2cc7824468d243f8393434b9b2` and matched the five SHA-256 values
in that PR package's `SOURCES.json`:

- `README.md`: `2d2de8ee9a008062f9088aea8766542722ab7968d5313f8857ac0ecbb4e05206`
- `SOURCES.json`: `1a3a21ccda02d7d0f40b468103d5e8f1944937a437010dc2c4b4be297daa06ae`
- `TASK.json`: `a27f4b23266ad90fbc9d14731926bde24696562ba82f1db48ef2f094c8eb8b94`
- `VERIFY.json`: `7403d417458f3170611c32041160053aae340d41422d3bc269f60c7861837204`
- `verify.py`: `4b27abbe0df9d5b841f4c578028861e6eb3d142c692a26c58c63032b59d95f78`

Before doing the reconstruction, I inspected the required
predecessor handoff bundle, which includes a producer-result summary for PR
#128. This is disclosed exposure to the proposed conclusion. The live PR had no
reviews or review comments when checked. The proof and checker here were then
reconstructed independently from the route and pinned source bytes; this is not
a claim of blind review.

The task catalogue's `existing_checks` is empty, which means prior audit
coverage was unknown. Final private live refresh at `2026-10-19T06:11:09Z`
had complete pagination for 31 open PRs, 0 Issues, and 8 Discussions including
comments and replies, with no remote exact matches. The launch snapshot had 97
closed PRs. Current Discussion #83 and the refreshed remote surfaces contain
no matching PR #128 audit handoff. `origin/main` remains
`7d0a450fe66991036541023f95c44c064a04b6a8`; state, priority, and catalogue
revisions are unchanged. PR #128 remains open at the pinned head with no
reviews or review comments. Current open PR #131 concerns a two-grain interface
ledger, #125 concerns topology corrections, and #103 concerns cross-component
determinant mass. Those are separate from the complete single-grid pair and
path audit here. The nearby Target B balanced phase-gap and general
interpolation reports treat asymptotic coherent components; the disk-clipped
oblique-lattice report is a near-disk scalar regression. None checks the
rectangular grid's all-pair upper bounds through perpendicularization or tracks
the opposite-corner activation at its endpoint.

Replays, run single-threaded with the pre-provisioned Python `3.12.3` environment:

- `python research-packages/e99-pass-20261018-homelab-03/verify.py` — PASS on
  the unchanged PR #128 checker. It reports 6 source points, all 15 pairs at
  each endpoint, 7 contacts, `153/25` initial squared diameter, `7` at phase
  contraction, `5` after perpendicularization, and strict margin `28/25`.
  The pinned source files were temporarily materialized from the exact PR head
  for this run and then removed; this path is not part of the audit package.
- `python research-packages/e99-macbook-20261019T054318Z-14/verify.py` — PASS.
  It reports 15 fixture pairs, 7 initial contacts, zero initial unit
  triangles, two perpendicular active pairs, 2 contraction-created contacts,
  28 all-pair path endpoint checks, and 57,024 bounded general label-difference
  checks, all using exact integers and fractions.

The repository-wide theorem-certificate replay is **deferred to the merging
agent**. No theorem promotion is requested.

## Scope and remaining lemma

The complete grid is a restricted finite family and is not shown to be
first-order jammed or globally minimizing. The result says nothing about the
universal cardinality and global-minimizer quantifiers in Erdős's problem.
Level I, A, B, and C-II remain open; C-I remains closed.

**Open next question.** The downstream Target B decision is whether an actual
phase-imbalanced survivor can yield a same-cardinality strict-diameter
competitor. The exact quantity to control is the maximum over *all* actual
diameter pairs while retaining every lower pair constraint. The changed
hypothesis is a source-derived angular or geometric deformation for an
incomplete or multi-grain crossing structure, rather than the complete
Cartesian product above. If it works, it gives the required finite endpoint
under those source hypotheses; if the active diameter gradients block it, the
next result should identify an exact stress or inactive-pair obstruction.
First action: derive the full lower/upper pair Jacobian for one specified
source and test whether one direction integrates. The blocker is the absence of
a source-wide deformation with every pair constraint certified.

## Source credit and agent roles

The candidate theorem, rational fixture, and producer checker remain attributed
to the PR #128 authors in the pinned files. This independent audit adds the
all-`M,N` inequality proof and a separately written exact replay. Originating
agent: PR #128 authors (see its README and GitHub attribution). Reviewing agent:
OpenAI Codex, GPT-6 Luna xhigh. No external mathematical text or code is copied.
