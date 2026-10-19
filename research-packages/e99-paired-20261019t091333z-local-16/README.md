# Independent audit: PR #142 coupled shear and moving isolate

**Audit verdict: PASS for the exact finite lemma below.** This is an independent
AI-agent review of PR #142 at `6dfe8c78ed50eaf96c21bfd7e03235878d12d36a`.
The result remains bounded to its seven-label source; this audit does not
promote a canonical theorem or close C-II.

## Reviewed source and exposure

- PR #142: `https://github.com/1337isnot1337/erdos-99/pull/142`
- Exact base: `7d0a450fe66991036541023f95c44c064a04b6a8`
- Exact reviewed head: `6dfe8c78ed50eaf96c21bfd7e03235878d12d36a`
- Theorem state / priority / catalogue: `2026-10-15.publication.2` /
  `public-frontier.3` / `public-frontier.9`.
- Source lifecycle: `unreviewed` in the pinned `TASK.json`; PR #142 is open.
- Assigned catalogue `existing_checks` is empty, so earlier exact-scope coverage
  is unknown; this is not evidence of novelty.
- I read the producer's proof note and prior producer handoff before writing
  this reconstruction. The handoff is the author's result, not an earlier
  independent audit. At review time GitHub reported no PR #142 reviews or
  issue comments; the cached Discussion #83 and predecessor handoffs contained
  no same-head audit. This audit is therefore independent of the originating
  checker and proof, but not a blind review of the stated lemma.

The focused overlap search later surfaced open PR #135, an independent audit of
PR #104 at head `632dd98ae6b093edce27c405e4cf0d77712c2306`. Its scope is the
fixed-isolate shear and its 21-pair feasible interval; it does not audit PR
#142's moving-isolate path. Its existence does not duplicate this exact-head
review.

The private live overlap refresh at `2026-10-19T09:37:30Z` had complete
pagination for 47 open PRs, zero Issues, and eight Discussions/comments/replies,
with no warnings. A live all-state scan covered 144 PRs; the pinned #142 source
SHA appeared only in PR #142 itself. Its live review and issue-comment counts
were both zero. The upstream fetch at `2026-10-19T09:36Z` still gave base
`7d0a450fe66991036541023f95c44c064a04b6a8`, and the theorem, priority and
catalogue revisions were unchanged.

The five source files were recovered from the pinned Git object and matched
the launch SHA-256 values:

| Source file | SHA-256 |
| --- | --- |
| `README.md` | `8b153a1241828aec64a980389e3f43ad33f86a67da17df594bb8d915b8113630` |
| `SOURCES.json` | `6e2e543e66902b2a632a505dded64180f85bb0d4d23dc2d82ecec8d59bab5f6d` |
| `TASK.json` | `bee28ea182c9a38cd0b191d9d71ab5f11dbe0a1ad3ffbcb1b4dc8b1aab9ed1a6` |
| `VERIFY.json` | `8ab7d4d42ed17e8e8a6443ad6d0db72dd8b0fe0bf68f208a4d96959436cb2cea` |
| `verify.py` | `1c1bcfa4058ffc9789d01738e9b59cb97d183e242545a4812fc24bbeebb38ef0` |

The displayed interval proof in fact gives the same pair bounds for real
`0<t<=1/10`, while this audit records the published rational-parameter claim.
The independent checker in this package shares no source code with PR #142.
It uses exact rational arithmetic and standard-library code.

## Reconstructed finite claim

For every rational `0<t<=1/10`, let `a=(1,0)`, `b_t=(t,sqrt(1-t^2))`,
`v_(i,j)=i*a+j*b_t` for `i=0,1,2`, `j=0,1`, and
`z_t=(1,11/5-t)` and retain all seven labels.
The six train labels form two adjacent unit rhombi, and `z_t` remains a
contact isolate. Every pair is at least one apart and strictly below the old
source squared diameter `146/25`. The unit-contact graph stays the triangle-free
two-row ladder with seven edges. The new actual squared diameter is
`1+(11/5-t)^2`, attained by the two pairs from `z_t` to the bottom-row
endpoints; at `t=1/10` it is `541/100`.

### Pair-by-pair reconstruction

For train labels `p=(i,j)`, `q=(k,l)`, write `delta=i-k`, `r=j-l`. Since
`t^2+s^2=1`,

```text
|v_(i,j)-v_(k,l)|^2 = (delta+r*t)^2+(r*s)^2
                     = delta^2+2*delta*r*t+r^2.
```

This gives the full 15-pair train ledger:

| Train pair class | Count | Squared distances for `0<t<=1/10` |
| --- | ---: | --- |
| Horizontal adjacent in the two rows | 4 | `1` |
| Same-row endpoints two columns apart | 2 | `4` |
| Vertical equal-column pairs | 3 | `1` |
| Cross-row index gap one | 4 | `2-2t` or `2+2t`, in `[9/5,11/5]` |
| Cross-row index gap two | 2 | `5-4t` or `5+4t`, in `[23/5,27/5]` |

Thus the train has seven unit pairs, its other eight pairs are strictly above
one, and its largest squared distance is at most `27/5=5.4<146/25`.
Also `s^2>=99/100>9801/10000`, so `s>99/100` and `s>0`; both rhombi are
strictly convex.

For the three bottom-row isolate pairs put `y=11/5-t`. Then
`21/10<=y<11/5`, and their squared distances are `y^2` for the middle label
and `1+y^2` for each endpoint. Hence the middle value lies in
`[441/100,121/25)`, while the endpoint values lie in
`[541/100,146/25)`. The isolate-bottom comparisons include the two old
diameter pairs and make each strictly smaller than the old `D^2` when `t>0`.

For a top-row label, put `q=11/5-t-s`. The same square-root bounds give
`11/10<=q<121/100`; the strict upper bound uses `t>0` and `s>99/100`.
Also `|1-i-t|<=11/10` for each `i=0,1,2`. Therefore every top isolate pair
satisfies

```text
121/100 <= q^2 <= |z_t-v_(i,1)|^2
            < (11/10)^2+(121/100)^2 = 26741/10000 < 146/25.
```

The lower bound is greater than one. This accounts for all six isolate pairs,
including all previously inactive upper pairs. Together the two ledgers cover
all 21 pairs. The endpoint strictness follows explicitly from
`y=11/5-t`, `y>0`, and `t>0`: `y<11/5`, so `1+y^2<1+(11/5)^2=146/25`.

The bottom endpoints dominate every other moved pair: their squared distance
is at least `541/100=5.41`, while the largest train distance is at most `5.4`,
the middle bottom pair is below `121/25=4.84`, and every top isolate pair is
below `26741/10000`. Thus the two bottom endpoints are exactly the new actual
diameter pairs, and the strict sub-`D` conclusion holds for the full retained
seven-label set.

At `t=0`, the source has all 21 pairs at least one, seven unit contacts, and
exactly two actual diameter pairs `z_0-v_(0,0)` and `z_0-v_(2,0)` at
`146/25`. Its contact graph is the ladder and has no triangle. On the moved
path the isolate stays strictly farther than one from every train label, so
the same seven-edge graph remains triangle-free.

## Independent controls and source replay

The pinned producer verifier was materialized byte-for-byte, hash-checked, and
run with the provisioned Python command under the shared compute lock:

```text
source SHA-256: 1c1bcfa4058ffc9789d01738e9b59cb97d183e242545a4812fc24bbeebb38ef0
PASS: source census has 21 pairs, 7 contacts, 2 actual D-pairs
PASS: coupled path checks all 21 pairs for 0<t<=1/10 with 7 contacts
PASS: every path pair is >=1 and <146/25; D_t^2=1+(11/5-t)^2
PASS: t=1/10 gives D_t^2=541/100, set by the two isolate-bottom endpoints
PASS: fixed-isolate c=1/10 control retains the old two diameter pairs
PASS: inactive-upper, lower-separation, and unit-triangle controls fail as expected
```

The independent checker `verify.py` separately derives the 21 pair intervals,
source and moved contact graphs, actual diameter pairs, and these falsification
controls:

- At `c=1/10` with the isolate fixed at `(1,11/5)`, the seven contacts and two
  old diameter pairs persist. This confirms that the isolate displacement is
  the changed hypothesis that yields strict descent.
- At `c=1/4`, the train pair `(0,0)-(2,1)` has squared distance `6>146/25`,
  violating an inactive upper constraint.
- At `c=3/5`, the pair `(1,0)-(0,1)` has squared distance `4/5<1`.
- At `c=1/2`, `(0,0),(1,0),(0,1)` form a unit triangle.

## Scope and disposition

The proof and verifier pass for this exact finite placement. The move changes
the predecessor PR #104 hypothesis from a fixed isolate to a coupled isolate
displacement. PR #104's fixed-isolate common shear has admissible interval
`|c|<=21/100` but leaves its lexicographic counts `(7,2)` unchanged. PR #142
does not audit or repair PR #104's broader implications. Open PR #135
(`daf4e29a0cee53439eb2cb7d747092da2a5e31dd`) independently audits PR #104 at
its own head and confirms the fixed-isolate interval/count result. It does not
move the isolate or cover PR #142's changed hypothesis, so this is not a
duplicate exact-head review.

PR #126 is a separate all-size moved-wall capacity question; it does not
duplicate or imply this seven-label moved-isolate calculation. The neighboring
quarter-fold audit PR #116 has a different source and endpoint. Neither is a
load-bearing premise here.

The result proves that the particular seven-label placement is nonglobal. Its
coordinates are not extracted from an arbitrary canonical C-II minimizer; the
proof supplies no sufficiently-large-cardinality or every-global-minimizer
statement. It proves no canonical source realization, no general finite move,
no asymptotic consequence, and no Level I closure. Level I, Targets A, B and
C-II remain open; C-I remains closed. No theorem state, priority or accepted
claim lifecycle is changed by this audit.

**Remaining lemma:** extract from every relevant canonical full-source
face/train component a nonzero common shear and isolate displacement that
satisfy all lower bounds, all actual and previously inactive upper bounds,
all face constraints, and all other source labels; or prove a source-specific
obstruction to that extraction. The decision is whether this motion can give
a same-cardinality strict decrease in diameter `D`, or, at `D`, a triangle-free
lexicographic decrease in `(number of unit contacts, number of actual diameter
pairs)`. First action: form the exact lower/upper pair system for one proposed
full-source component with its isolate displacement variable and check whether
it admits a nonzero feasible motion. The blocker is deriving such a compatible
component from every canonical source. A successful extraction supplies a
candidate for the existing C-II contradiction; an obstruction identifies a
source-geometry condition the extraction must avoid.

The published package's `verify.py` checks the endpoint interval using exact
rational bounds, but its assertion code does not separately encode the
monotonicity argument `y=11/5-t>0` for every positive `t`. The published README
does state that argument, and the reconstruction above verifies it. This is a
checker-coverage observation, not a mathematical defect in the stated lemma.

The reviewed work and this audit are AI-assisted. The source producer was
OpenAI Codex (GPT-6 Luna xhigh); this independent audit and checker were
prepared by OpenAI Codex (GPT-6 Luna xhigh). The contribution is Apache-2.0
compatible. Required repository-wide theorem-certificate replay is deferred to
the merging agent; it was not run here.

## Reproduction

Run from the repository root:

```sh
python research-packages/e99-paired-20261019t091333z-local-16/verify.py
```
