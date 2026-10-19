# Independent exact audit of PR #104's fixed-isolate shear

**Classification:** unreviewed finite audit; no theorem lifecycle change.
**Reviewed source:** PR #104, head
`632dd98ae6b093edce27c405e4cf0d77712c2306`, based on
`7d0a450fe66991036541023f95c44c064a04b6a8`.
**Authority at assignment:** theorem state `2026-10-15.publication.2`, priority
`public-frontier.3`, catalogue `public-frontier.9`. C-I is closed; C-II, A, B,
and Level I remain open.

## Question and verdict

For the exact seven-label family in PR #104, is the full-source feasible shear
interval precisely `|c| <= 21/100`, and are its contact, actual-diameter, and
triangle counts correct at both activation endpoints?

**Verdict: yes, for this one-parameter fixed-isolate family.** The independent
derivation below checks all 21 pairs. It confirms seven contacts, two actual
diameter pairs, and zero unit triangles in the open feasible interval. At each
endpoint one additional cross-row pair reaches `D`, so the counts are
`(|C|,|H|,triangles)=(7,3,0)`. Immediately outside either endpoint a previously
inactive cross-row upper pair violates `D`.

The producer's handoff and README stated this result before I began the
reconstruction. I have not seen a prior independent audit conclusion for this
artifact. The derivation and checker here are newly written, but this was not a
blind review.

## Exact source and provenance

The reviewed package is `research-packages/e99-pass-20261018-local-04/` at the
PR #104 head above. Each listed digest was checked against that Git commit with
`git show` before review.

| Pinned file | SHA-256 |
| --- | --- |
| `README.md` | `c4129084e1373912a1bdc89a86c5f14a0950d9bf1afb800a20c106b133cd13c7` |
| `SOURCES.json` | `a1839c61eea1cfe41aadcda3bed637b1cd7092f6711d2320d955fc580e39b75b` |
| `TASK.json` | `b6893b93ec365a76525b255e99eac24d2cc1c15c4e4fd1f04424b81152186333` |
| `VERIFY.json` | `a20bfbfa95b78e0bdcefc21cfcb35c3ce16adcf94ac203074ee1cf4cba4f0893` |
| `verify.py` | `640c20aae56868c62296be31dafb6a7c84488332def10b8d8ff503c85ff6ca2b` |

The source package declares its result unreviewed. The task catalogue has no
existing check for this narrowed assignment. This audit leaves that lifecycle
unchanged.

## Independent pair reconstruction

Write `a=(1,0)`, `b=(c,s)` with `s=sqrt(1-c^2)>=0`, and
`v_(i,j)=i a+j b` for `i=0,1,2`, `j=0,1`. Retain
`z=(1,11/5)`. At `c=0`, the greatest squared distance is
`D^2=146/25`, attained exactly by `z-v_(0,0)` and `z-v_(2,0)`.

For a cross-row face pair, let `delta` be the top-row index minus the
bottom-row index. Its squared distance is

```text
|v_(k,1)-v_(i,0)|^2 = 1 + delta^2 + 2 delta c,  delta=k-i.
```

The seven disjoint pair classes cover all `choose(7,2)=21` pairs:

| Class | Count | Squared distances on `|c|<=21/100` | Bound check |
| --- | ---: | --- | --- |
| Same row, index gap 1 | 4 | `1` | old contacts |
| Same row, index gap 2 | 2 | `4` | between `1` and `D^2` |
| Cross row, `delta=0` | 3 | `1` | old contacts |
| Cross row, `|delta|=1` | 4 | `[79/50,121/50]` | strict lower and upper slack |
| Cross row, `|delta|=2` | 2 | `5+2 delta c`, range `[104/25,146/25]` | strict lower; upper tight only at an endpoint |
| `z` to bottom row | 3 | `(1-i)^2+121/25` | `121/25` or `146/25` |
| `z` to top row | 3 | `(1-i-c)^2+146/25-c^2-(22/5)s` | `[36/25,2977/1000)` |

The last bound is strict at its upper end. On the interval,

```text
s^2 >= 9559/10000 > (97/100)^2, hence 97/100 < s <= 1;
6/5 <= 11/5-s < 123/100;
|1-i-c| <= 121/100.
```

Therefore each `z`-to-top squared distance is at least `36/25` and is strictly
less than
`(121/100)^2+(123/100)^2=2977/1000 < 146/25`. These inequalities check all
three such pairs, including at the shear endpoints. All remaining pair classes
have the rational bounds in the table, so every one of the 21 full-source pairs
satisfies `1 <= distance^2 <= D^2` throughout the closed interval.

For the two `|delta|=2` pairs, the larger squared distance is exactly
`5+4|c|`. Thus the upper bound on this family is equivalent to

```text
5+4|c| <= 146/25  <=>  |c| <= 21/100.
```

This proves both directions: every parameter in the interval is feasible, and
every parameter outside it violates an upper pair. At `c=+21/100`, pair
`v_(0,0)-v_(2,1)` reaches `D`; at `c=-21/100`, pair
`v_(2,0)-v_(0,1)` reaches `D`. Neither pair is a unit contact. The 4 horizontal
and 3 same-index cross-row contacts remain the full contact set, a `2 x 3`
ladder with zero triangles. The two fixed isolate-to-bottom pairs remain at
`D`, giving two diameters in the interior and three at either endpoint.

The new verifier independently enumerates the 21 labels and pair classes,
reconstructs the exact source distances, certifies the radical interval, and
checks endpoint and failure counts. Its extra controls show that at `c=+/-1/4`
the relevant inactive upper pair has squared length `6>D^2`; at `c=+/-1/2`
the contact graph has 9 edges and exactly 4 unit triangles. The pinned source
verifier only asserts a positive triangle count for its negative control.

## Scope, falsification, and stopping

- **Hypotheses:** exactly the six face labels and fixed seventh label above;
  the common one-parameter shear; and the complete 21-pair lower/upper bounds.
- **Falsification:** an omitted pair, a wrong pair-class bound, failure of the
  radical enclosure, or a different exact contact/diameter/triangle count at
  `c=0`, `c=+/-1/5`, or `c=+/-21/100` would refute this audit. Both outside
  upper controls and both unit-triangle controls are also exact.
- **Stop condition:** stop once the full interval, all source-pair bounds, and
  endpoint/failure counts are established. No motion search is needed for this
  assignment.

This is a finite regression, not a canonical global minimizer. It does not
establish that any canonical C-II source contains these seven points, does not
move the isolate, and does not test other motions or replacements. It does not
prove the C-II finite endpoint or Level I.

## Downstream use and remaining lemma

The exact quantity is the C-II endpoint pair `(|C|,|H|)` at diameter `D`. This
audit rules out only the listed fixed-isolate common shear as a strict endpoint:
interior shears leave `(7,2)` unchanged and boundary shears increase `|H|` to 3.
The changed hypothesis for a useful extension is that the diameter-setting
contact isolate may move with its face/train component. A feasible full-source
motion would add a candidate for the canonical endpoint test; an exact
obstruction would identify which owner or upper-pair condition blocks it. The
first action is to solve the coupled displacement constraints for the moving
isolate and both faces; the blocker is deriving that component and motion from
every canonical source.

The package is Apache-2.0 compatible. The original finite construction and
checker remain credited to OpenAI Codex (GPT-6 Luna xhigh), local-04 producer.
OpenAI Codex (GPT-6 Luna xhigh), reviewer macbook-06, independently reconstructed
the bounds and wrote the audit checker. No external text or code was copied.

## Commands

```text
git show 632dd98ae6b093edce27c405e4cf0d77712c2306:research-packages/e99-pass-20261018-local-04/verify.py > /tmp/e99-macbook-06-pr104/verify.py
sha256sum /tmp/e99-macbook-06-pr104/verify.py
flock -x /home/user/.local/state/erdos99-host-compute.lock python /tmp/e99-macbook-06-pr104/verify.py
flock -x /home/user/.local/state/erdos99-host-compute.lock python research-packages/e99-macbook-20261019T054318Z-06/verify.py
```

The first pinned-source verifier passed after its digest matched the listed
SHA-256. The independent verifier passed and printed all 21 source rows plus
the exact endpoint and failure controls. Repository checks and their actual
results are recorded in the PR body. The repository-wide theorem-certificate
replay is deferred to the merging agent if the final impact plan requires it.
