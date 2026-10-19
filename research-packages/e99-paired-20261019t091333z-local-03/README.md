# Single exterior attachments permit a coupled-shear descent

**Classification:** unreviewed exact finite evidence; no theorem is promoted.
**Investigation:** `c-shear-exterior-attachment-paired-20261019`.
**Base:** `7d0a450fe66991036541023f95c44c064a04b6a8`.
**State / priority / catalogue:** `2026-10-15.publication.2` /
`public-frontier.3` / `public-frontier.9`.
**Theorem status:** Level I, A, B, and C-II remain open; C-I remains closed.

## Result and downstream quantity

The exact PR #142 two-face train/moved-isolate path remains feasible after adding
one exterior label in either of two attachment modes. For each `h` in
`{1, 11/10}` and every rational `0 < t <= 1/10`, the eight labels below remain
unit-separated and every pair is strictly shorter than the source diameter.
The unique source and path diameter pair is `W-A_0`; its squared length strictly
decreases. All 28 unordered pairs are included.

At `h=1`, `W=(3,1)` is outside the six-point train hull and has exactly one new
unit contact, with `B_2=(2,1)`. The source diameter is newly set by
`W-A_0`, with `D^2=10`. At `h=11/10`, `W=(3,11/10)` is also exterior, has no
new unit contact (`|W-B_2|^2=101/100`), and has unique actual diameter pair
`W-A_0`, with `D^2=1021/100`. Thus the explicit single-contact and
diameter-only attachment variants both permit a strict sub-D endpoint.

The affected canonical quantity is the actual diameter, hence the same-cardinality
strict-sub-D test in the C-II endpoint route. These finite sources are not claimed
to be global minimizers. The result does not say arbitrary exterior attachments
permit a descent and does not extract either attachment or its motion from a
canonical source.

## Coordinates and all pair polynomials

For `i=0,1,2`, put

```text
A_i = (i, 0)
B_i = (i+t, s),       s = sqrt(1-t^2)
Z   = (1, 11/5-t)
W_h = (3+6t/5, h-5t),  h in {1, 11/10}.
```

The interval gives `s^2 >= 99/100 > (99/100)^2`, so
`99/100 < s <= 1`. The 28 pairs partition as follows; the displayed formulas
are the actual squared-distance polynomials, with `s^2=1-t^2` reduced where
useful.

| Pair class | Count | Squared distance |
|---|---:|---|
| `A_i,A_k` or `B_i,B_k` | 6 | `(i-k)^2` |
| `A_i,B_k` | 9 | `1+(i-k)^2-2(i-k)t` |
| `Z,A_i` | 3 | `(1-i)^2+(11/5-t)^2` |
| `Z,B_i` | 3 | `(1-i-t)^2+(11/5-t-s)^2` |
| `W_h,A_i` | 3 | `(3-i+6t/5)^2+(h-5t)^2` |
| `W_h,B_i` | 3 | `(3-i+t/5)^2+(h-5t-s)^2` |
| `W_h,Z` | 1 | `(2+6t/5)^2+(h-11/5-4t)^2` |
| **Total** | **28** | |

For the six train same-row pairs, four adjacent pairs have squared distance 1
and two have squared distance 4. Among the nine cross-row train pairs, three
with `i-k=0` have squared distance 1; four with `|i-k|=1` lie in
`[9/5,11/5]`; and two with `|i-k|=2` lie in `[23/5,27/5]`. Thus all train
lower bounds and inactive uppers hold.

For `Z-A_i`, `21/10 <= 11/5-t <= 11/5`, so the three distances lie between
`541/100` and `146/25` (for `i=0,2`) or between `441/100` and `121/25`
(for `i=1`). For `Z-B_i`, set `q=11/5-t-s`. Then
`11/10 < q < 121/100` and `|1-i-t| <= 11/10`; hence every such distance is
strictly between 1 and `26741/10000`.

For the new label, the three `W_h-A_i` polynomials are

```text
(3-i)^2 + h^2 + (12(3-i)/5 - 10h)t + (661/25)t^2.
```

In particular the new actual diameter pair is

```text
h=1:     |W_1-A_0|^2       = 10 - (14/5)t + (661/25)t^2
h=11/10: |W_11/10-A_0|^2  = 1021/100 - (19/5)t + (661/25)t^2.
```

For both choices, the difference from the source value is
`t(L+(661/25)t)` with `L=-14/5` or `L=-19/5`. At `t=1/10`, these bracket
values are `-39/250` and `-289/250`, respectively, so they remain negative
throughout the interval. At `t=1/10`, the actual squared diameters are
`24961/2500` and `6309/625`.

To verify that `W-A_0` remains the actual diameter, its minimum on the interval
is `6561/661 > 9.9` for `h=1`, and `166464/16525 > 10` for `h=11/10`. For
every other `W-A_i` pair, the upper bound `(3-i+3/25)^2+h^2` is below `5.71`.
For `W_h-B_i`, put `r=h-5t-s`. The exact ranges are
`-1/2 < r <= 0` when `h=1`, and `-2/5 < r <= 1/10` when `h=11/10`.
Therefore the largest `W_h-B_i` upper bounds are below `9.3704` and `9.2804`,
respectively. Finally, `W_h-Z` is

```text
h=1:     136/25 + (72/5)t + (436/25)t^2 <= 7.0544
h=11/10: 521/100 + (68/5)t + (436/25)t^2 <= 6.7444.
```

These bounds, together with the first seven pair classes, show that every pair
other than `W-A_0` is below the minimum value of `|W-A_0|^2` on this interval.
For lower bounds, `Z-A_i` is at least `441/100` and `Z-B_i` is greater than
`121/100`; `W_h-A_2` is at least `5/4` or `34/25`; `W_h-B_2` has horizontal
separation `1+t/5`; all other `W_h` pairs have larger horizontal separation.
Every source and path pair is therefore in `[1,D^2]`, and every path pair is
strictly below the source `D^2` for `t>0`.

## Contacts, diameter pairs, and controls

At `t=0` the six train labels have the seven-edge two-row ladder. The `h=1`
point adds only the pendant contact `W-B_2`; the `h=11/10` point adds no unit
contact. Both contact graphs are triangle-free, and `W-A_0` is the unique
actual diameter pair. At every positive path parameter, `W-B_2` has horizontal
separation `1+t/5>1`; all other new-involving pairs have strict lower slack.
The path contact graph is again the triangle-free seven-edge ladder.

Falsification controls in the verifier check that `t=0` retains the source
diameter, while at `t=1/5` the proposed `W-A_0` upper pair exceeds its source
bound for both `h` values. The end of the claimed interval is also checked
exactly at `t=1/10`.

## Predecessors, overlap, and source pins

- PR #104 (`632dd98ae6b093edce27c405e4cf0d77712c2306`) pins the isolate and
  studies the two-face shear; its feasible shears keep the old lexicographic
  counts. PR #135 (`daf4e29a0cee53439eb2cb7d747092da2a5e31dd`) audits that
  fixed-isolate interval. Neither includes this moving exterior eighth label.
- PR #142 (`6dfe8c78ed50eaf96c21bfd7e03235878d12d36a`) moves the seventh
  contact-isolated label and proves the seven-label path. This package adds the
  eighth exterior label and gives it a new explicit velocity. All five pinned
  PR #142 package-file hashes matched the launch pin file:

  | File | SHA-256 |
  |---|---|
  | `README.md` | `8b153a1241828aec64a980389e3f43ad33f86a67da17df594bb8d915b8113630` |
  | `SOURCES.json` | `6e2e543e66902b2a632a505dded64180f85bb0d4d23dc2d82ecec8d59bab5f6d` |
  | `TASK.json` | `bee28ea182c9a38cd0b191d9d71ab5f11dbe0a1ad3ffbcb1b4dc8b1aab9ed1a6` |
  | `VERIFY.json` | `8ab7d4d42ed17e8e8a6443ad6d0db72dd8b0fe0bf68f208a4d96959436cb2cea` |
  | `verify.py` | `1c1bcfa4058ffc9789d01738e9b59cb97d183e242545a4812fc24bbeebb38ef0` |

  All PR #104 and PR #135 package hashes also matched the launch pins; their
  exact heads are above and their bytes are unchanged.
- PR #108 and #112 concern conditional train-return linkage and separator
  results; PR #139's near-diameter estimate assumes `D>=216`. Their scopes do
  not cover this finite eight-label path. PR #126 studies a different moved-wall
  capacity family. Discussion #83 had no handoff on this attachment question;
  the predecessor local-04, macbook-03, and macbook-06 handoffs were read.
- The offline overlap snapshot had complete pagination for 47 open PRs, 97
  closed PRs, zero Issues, and eight Discussions. Live `gh` checks confirmed
  PRs #104, #135, and #142 still point to the pinned heads on the same base;
  PR #142 has no review or issue comments. The private submission overlap
  refresh completed at `2026-10-19T09:44:55Z`: 49 PRs, zero Issues, and
  eight Discussions, all with complete pagination and no warnings. The exact
  task search found no new investigation match; newly opened PRs #149 and #150
  audit separate PR #948 array claims. `origin/main` and all three state
  revisions remained unchanged.

This package was independently derived from the coordinates and pair inequalities;
it does not copy predecessor proof text or checker code. Exact source coordinates
are from PR #142's immutable head above. The canonical problem and route inputs
are SHA-pinned in `SOURCES.json`.

## Limits and next lemma

This is an exact finite witness for two eight-label attachments. It does not show
that the original or enlarged source is globally minimizing, that such an
attachment occurs in any canonical C-II source, or that a compatible velocity
can be extracted while retaining an arbitrary full source. It does not change
the theorem manifest, priority, or catalogue. Level I, A, B, and C-II remain
open; C-I remains closed.

The next lemma is to extract, from every canonical full-source face/train
component, an exterior unit or actual-diameter attachment with a velocity whose
28 local inequalities and all inequalities to the remaining source are
compatible. A proof would make this finite move available to the C-II endpoint
route; a contrary full-source pair would identify an attachment obstruction.
The missing bridge is source extraction and compatibility with every retained
label, including contact isolates and inactive diameter uppers.

The theorem-state manifest remains authoritative. The result remains
**unreviewed** until an independent AI-agent audit on the exact submitted head.
Required repository-wide theorem-certificate replay is **deferred to the
merging agent**. This contribution is offered under Apache-2.0. The exact proof
module and verifier were produced by OpenAI Codex (GPT-6 Luna xhigh), producer
local-03, with AI assistance disclosed. No external literature is used.

## Reproduction

```text
python research-packages/e99-paired-20261019t091333z-local-03/verify.py
python scripts/research_package.py --package research-packages/e99-paired-20261019t091333z-local-03 --check-only
```
