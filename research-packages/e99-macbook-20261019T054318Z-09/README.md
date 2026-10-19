# Independent audit of PR #111 full-pair restoration

**Classification:** exact-head AI-agent audit with exact finite controls. The
conditional argument passes within its stated hypotheses. No canonical claim or
theorem state is promoted.

## Source and scope

- Audited PR: [#111](https://github.com/1337isnot1337/erdos-99/pull/111), exact
  head `4ae7399e2595074c0331398fbba9b58c5dea3e73`.
- Base: `7d0a450fe66991036541023f95c44c064a04b6a8`.
- Theorem state / priority / catalogue: `2026-10-15.publication.2` /
  `public-frontier.3` / `public-frontier.9`.
- Assignment: `audit-pr111-full-pair-restoration-macbook-20261019`, reviewer.
- The PR was open and draft with no GitHub reviews or comments when checked.

The audited package bytes are pinned by SHA-256: `README.md`
`2844e8e4efbd476ba9d88a32cf70c8e3ebfc39e989f520e0c60e4fd021ef5f23`,
`SOURCES.json`
`2bf7df124983722f07d3678a540d3f214739b01e1f1e07ad60b587261a57a137`,
`TASK.json`
`9896aba2849fe0070bf172ffd6e4cad434b82d6a3d7103896d0b77570561a474`,
`VERIFY.json`
`581081b4289ae787f7e5e32d4ff6f40736d1e69e049680edbd30019b6dacb9ee`, and
`verify.py`
`09f28f9e6cc50c9ffa9a584c7331aec2349213c82f489febb9afec4d1706fcf0`.

This audit checks the conditional cardinality rule, its lexicographic argument,
and the exact eleven-label fixture with all source labels retained in each pair
table. It does not prove the stress-deletion theorem again, supply a packet from
a canonical source, or establish global optimality of the finite fixture.

## Reconstructed conditional lemma

Let `A` be an `n`-label feasible source with diameter `D`, unit-contact graph
triangle-free, and selected among global diameter minimizers of size `n` first
by minimum contact count and then by minimum number of actual diameter pairs.
Every pair in `A` has squared distance in `[1,D^2]`. Let `R` be a deleted set of
size `k` supplied by the stress-deletion result.

There are two safe cardinality cases.

1. If `R` contains a vertex incident to a unit contact, delete `T=R` and insert
   exactly `k` labels in a packet `Z`.
2. If `R` contains no unit-contact vertex, choose a nonisolated contact vertex
   `v` outside `R`, delete `T=R union {v}`, and insert exactly `k+1` labels.

In either case, write `m=|T|=|Z|`. Require **every** pair within `Z` and every
pair from `Z` to every retained label in `A\T` to have squared distance
strictly in `(1,D^2)`. No pair from a packet label to a deleted label needs a
constraint because those old labels are absent.

The replacement `A*=(A\T) union Z` has exactly `n` labels. Old retained pairs
are unchanged and feasible; all new pairs satisfy both bounds strictly.
Therefore `A*` is unit-separated and has diameter at most `D`. It has no new
unit contacts, while deleting the nonisolated contact vertex in `T` removes at
least one old contact. Its contact graph is a subgraph of the old one, so it
remains triangle-free and has strictly fewer contacts.

If `diam(A*)<D`, it contradicts the global minimum diameter at cardinality `n`.
If `diam(A*)=D`, it is another global minimizer at cardinality `n` and the
strict contact decrease contradicts the first lexicographic tie-break. The
second tie-break on actual-diameter-pair count is not needed for this rule.

At the endpoint `D`, the actual-diameter graph is exactly the old actual-`D`
graph induced on retained labels: retained distances do not change, and every
new pair is strictly below `D^2`. Thus no old inactive upper pair can become a
new pair at the old diameter. When the endpoint diameter is `D'<D`, new actual
`D'` pairs can occur among retained old pairs or pairs involving `Z`; that is
harmless to the global-minimum contradiction and must still be included when
reporting the endpoint's diameter graph.

The counts `k` and `k+1` are exact for these two repairs. Replacing fewer than
the number of deleted labels changes cardinality and cannot be compared with
`D(n)`. If `R` consists only of contact isolates, a `k`-label packet restores
cardinality but need not remove any contact; deleting one additional contact
vertex requires `k+1` packet labels.

## Independent exact replay

The separate verifier `verify.py` uses `fractions.Fraction` and independently
reconstructs the coordinates and pair tables from scratch. It does not import
or execute PR #111's verifier. Results:

| Configuration | Labels | Unordered pairs | Contact pairs | Actual diameter pairs | Maximum squared distance |
|---|---:|---:|---:|---|---:|
| Source `p_i=(i,0), 0<=i<=9`, `q=(1/2,11/10)` | 11 | 55 | 9 | `p0-p9` | 81 |
| Delete `p0`, retain `q` | 10 | 45 | 8 | none at 81 | `3673/50` |
| Restore with `r=(8/5,11/10)` | 11 | 55 | 8 | `p9-q` at new `D'^2` | `3673/50` |

The replay also verifies the normalized source stress (`beta_09=1`, all nine
contact weights `alpha_i=9`), force balance, equilibrium rank 9 and normalized
rank 10. After deleting `p0`, the eight retained contact columns are independent
and there is no retained old-`D` row. The isolate `q` remains in all 45 and 55
pair tables. In the strict restoration, `p9-q` was an inactive source upper
pair at `3673/50<81`; it becomes the actual-diameter pair at the smaller
endpoint diameter. This is the right distinction between old `D` pairs and new
`D'` pairs.

## Falsification controls

- **Weak lower margin:** restore `p0` itself. The 11-label source, nine
  contacts and old `D` pair return unchanged. Equality at squared distance 1
  can restore a lost contact, so `>=1` alone does not prove a contact decrease.
- **Weak upper margin:** after deleting `p0`, insert
  `r_w=(32/5,36/5)`. Every new distance is strictly greater than 1 and at most
  81, but `|r_w-p1|^2=81`. This creates a new actual pair at the old `D` even
  though `p1-r_w` was not an old pair. The endpoint still has eight contacts,
  so contact minimality would remain a contradiction under the canonical
  hypotheses; strict upper margin is needed for the stronger no-new-old-`D`
  pair claim.
- **One-for-one replacement of an isolated deletion:** delete `q` and insert
  `q'=(1/2,6/5)`. All new distances are strictly in `(1,81)`, but the 11-label
  endpoint still has nine contacts and diameter squared 81. A `k`-packet alone
  need not improve the lexicographic objective when `R` deletes no contact.
- **Cardinality shortfall:** deleting `p0` without an inserted label leaves 10
  labels. Its smaller diameter is not a competitor for the 11-label value
  `D(11)`.
- **The `k+1` fallback:** delete `q` and the contact vertex `p0`; insert
  `q=(1/2,11/10)` and `r=(8/5,11/10)`. All pairs involving the packet are
  strictly in `(1,81)`, cardinality is 11, contacts fall from nine to eight,
  and the new maximum is `3673/50`.

These controls are finite logical checks, not counterexamples to a rule under
canonical-minimizer hypotheses. The source fixture is not proved globally
optimal, and its collinear core does not meet the full rigidity hypotheses of
the canonical stress-deletion theorem.

## Audit disposition and limits

The conditional replacement proof and the exact PR #111 pair ledger pass this
independent audit. The stated strict-margin conditions are sufficient, and the
`k` versus `k+1` count is correct. The argument does not rely on the secondary
actual-diameter-pair tie-break because it removes a unit contact in both cases.
When `D'<D`, a new actual-diameter pair such as `p9-q` is expected and does not
undermine the strict-diameter branch. At diameter `D`, strict upper margins
exclude any new pair at `D`.

No source-wide extraction of `W` or `Z` is given. The result cannot be applied
to every sufficiently large cardinality or every canonical C-II minimizer
without a theorem producing the required strict packet while checking every
label and every new pair. C-II, A, B, and Level I remain open; C-I remains
closed. The source package's lifecycle is unchanged; this audit is evidence,
not a promotion transaction.

## Reproduction

Run from the repository root with Python's standard library:

```sh
python research-packages/e99-macbook-20261019T054318Z-09/verify.py
python -O research-packages/e99-macbook-20261019T054318Z-09/verify.py
```

Both invocations perform the same exact rational checks. No external packages
are used.

## Open next question

- **Downstream decision:** can supplied-`W` stress deletion contradict C-II
  contact-minimality or minimum diameter for a canonical source?
- **Exact quantity:** the count of replacement labels admitting strict
  full-pair squared-distance margins against every retained source label.
- **Changed hypothesis:** derive the packet and its strict pair bounds from
  the geometry of an actual canonical source, including every contact isolate
  and old inactive upper pair.
- **What either outcome enables:** a uniform packet theorem supplies a
  same-cardinality contradiction; a counterexample identifies a missing
  capacity or guard condition.
- **First action and blocker:** test a source-extracted packet against the
  complete pair table. No current theorem supplies that packet from every
  canonical source.

## Attribution

This is original audit prose and an independent exact verifier offered under
Apache-2.0. OpenAI Codex GPT-6 Luna xhigh independently reconstructed the
conditional proof and wrote the checker; the exact PR #111 source was pinned
and read as the audited artifact. No source code was copied or imported.
