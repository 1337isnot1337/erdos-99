# Coupled two-face shear and isolate descent

**Classification:** unreviewed exact finite result. No theorem is promoted.
**Investigation:** c-move-isolate-with-two-face-train-macbook-20261019.
**Refined scope key:** 817ef58a164be2a92b1037fb95fb2a1f3c131a3878a0d75f2cef283ad0f3f56a.
**Base:** 7d0a450fe66991036541023f95c44c064a04b6a8.
**State / priority / catalogue:** 2026-10-15.publication.2 /
public-frontier.3 / public-frontier.9.
**Theorem status:** Level I, A, B, and C-II remain open; C-I remains closed.

## Candidate statement and downstream quantity

Take the exact seven labels from PR #104: two unit rhombi in a three-column
train and its diameter-setting contact isolate. Permit a common face shear and
move the isolate along the same scalar parameter. The canonical quantity this
finite move can affect is (|C|,|H|), the number of unit pairs and actual
diameter pairs. A valid same-cardinality strict-sub-D result would contradict
global minimality if this exact source were a global minimizer. The construction
below proves that this particular seven-label source is nonglobal; it makes no
claim that canonical large sources contain the pattern.

**Candidate lemma.** For every rational t with 0 < t <= 1/10, set

~~~
a = (1,0),  b_t = (t,sqrt(1-t^2)),
v_(i,j) = i a + j b_t  (i=0,1,2; j=0,1),
z_t = (1,11/5-t).
~~~

Then the seven labels are pairwise at least one apart, all 21 squared
distances are strictly below the source value D^2=146/25, their contact
graph is the same triangle-free two-row ladder with seven edges, and their
actual diameter is

~~~
D_t^2 = 1 + (11/5-t)^2 < 146/25.
~~~

At t=1/10, this gives D_t^2=541/100. Both the two-face shear and isolate
displacement are nonzero. No labels are deleted or added.

## Full pair polynomials

Keep the isolate displacement (u,v) explicit first, writing
z=(1+u,11/5+v) and b=(c,s) with c^2+s^2=1. For grid labels
p=(i,j) and q=(k,l), put delta=i-k and r=j-l. The exact squared
distance is

~~~
|v_(i,j)-v_(k,l)|^2 = (delta+r*c)^2 + (r*s)^2
                      = delta^2 + 2*delta*r*c + r^2.
~~~

The second expression uses only c^2+s^2=1. The isolate-to-grid pair
polynomials are

~~~
|z-v_(i,0)|^2 = (1+u-i)^2 + (11/5+v)^2,
|z-v_(i,1)|^2 = (1+u-i-c)^2 + (11/5+v-s)^2.
~~~

The interval below specializes to u=0, v=-t, c=t, and
s=sqrt(1-t^2). Thus every old contact, noncontact lower bound, actual
diameter upper bound, and previously inactive upper pair is checked in the
full seven-label source.

## Exact interval proof

There are 21 pairs: 15 train pairs and six isolate pairs.

* In each row, the four adjacent pairs have squared distance 1; the two
  remaining pairs have squared distance 4.
* Across the rows, equal-column pairs have squared distance 1 (three pairs).
  For index difference of magnitude one, the four distances lie in
  [9/5,11/5]. For index difference of magnitude two, the two distances lie
  in [23/5,27/5]. The latter is at most 27/5=5.4 < 146/25=5.84.
  Both rhombi remain strictly convex since s>0. Their two diagonal values
  2-2t and 2+2t are in [9/5,11/5], so the face diagonals are included in this
  same complete lower/upper ledger.
* For the isolate and bottom row, let y=11/5-t, so
  21/10 <= y < 11/5. The middle pair has squared distance y^2, between
  441/100 and 121/25. Each endpoint pair has squared distance 1+y^2, at
  least 541/100 and strictly below 146/25 because t>0.
* For the isolate and top row, let q=11/5-t-s. Since t<=1/10,
  s^2>=99/100>(99/100)^2, while s<=1; hence
  11/10 <= q < 121/100. Also |1-i-t|<=11/10. Each of these three
  squared distances is therefore in
  [121/100,26741/10000), strictly between one and 146/25.

This accounts for every pair. The only unit pairs are the four horizontal
adjacencies and three vertical equal-column pairs. They form the two-row
ladder, which has no triangle. The two isolate-to-bottom endpoint pairs have
squared distance at least 541/100; every train pair is at most 540/100,
the middle bottom pair is below 121/25, and every top isolate pair is below
26741/10000. Thus the actual diameter is exactly 1+y^2, attained by the
two endpoint pairs. For every t>0, it is strictly below the old D^2.

The verifier enumerates all 21 pairs using these rational interval bounds.
It also checks the source at t=0, the predecessor's fixed-isolate shear at
c=1/10, a shear that violates an inactive upper bound, a displacement that
violates a lower bound, and a unit-triangle control.

## Comparison with the predecessor and live neighbors

PR #104 (632dd98ae6b093edce27c405e4cf0d77712c2306) pins z=(1,11/5) and
shows that fixed-isolate common shear preserves (|C|,|H|)=(7,2) throughout
its admissible interval. Its exact files were retrieved from that immutable
commit from package research-packages/e99-pass-20261018-local-04/. The source
PR remains open/draft and its result remains unreviewed. All five SHA-256
values matched the launch pins:

| Pinned source file | SHA-256 |
| --- | --- |
| README.md | c4129084e1373912a1bdc89a86c5f14a0950d9bf1afb800a20c106b133cd13c7 |
| SOURCES.json | a1839c61eea1cfe41aadcda3bed637b1cd7092f6711d2320d955fc580e39b75b |
| TASK.json | b6893b93ec365a76525b255e99eac24d2cc1c15c4e4fd1f04424b81152186333 |
| VERIFY.json | a20bfbfa95b78e0bdcefc21cfcb35c3ce16adcf94ac203074ee1cf4cba4f0893 |
| verify.py | 640c20aae56868c62296be31dafb6a7c84488332def10b8d8ff503c85ff6ca2b |

This package changes the hypothesis by moving z by (0,-t) together with the
shear. The derivation and verifier here were written independently; no source
code or report text was copied.

Open PR #126 concerns a separate all-size rhombic grid and proves zero safe
insertion capacity along its specified moved-wall rotation. It neither tests
nor contradicts this seven-label moved-isolate path. The cached Discussion #83
handoffs concern Target A and Target B. The live #83 thread and the inspected
quarter-fold audit PR #116 contain no matching moved-isolate result.

## Falsification and stopping rule

**Falsification controls:** at t=1/4, a two-column cross-row pair has
squared distance 6>D^2; at t=3/5, a one-column cross-row pair has squared
distance 4/5<1; at c=1/2, three train labels form a unit triangle. The
fixed-isolate control at c=1/10 keeps the old two diameter pairs, confirming
that isolate movement is the changed hypothesis responsible for the descent.

**Stop condition:** stop after the exact interval, all 21 lower/upper pair
bounds, diameter formula, contact graph, and independent controls pass. Do not
search larger patterns or infer source extraction from this fixture.

## Limits and next lemma

This is a finite exact regression on the seven-label source of PR #104. That
source is nonglobal by the strict competitor proved here and is not a canonical
large-source model. The strict competitor does not prove that any canonical
C-II minimizer contains this configuration or admits this displacement. There
is no asymptotic or Level I claim, and theorem state and priority are unchanged.
The full-core and macroscopic-container obligations remain open.

The next lemma is to derive, for a canonical full-source face/train component,
a nonzero isolate displacement and common train shear satisfying every source
pair lower and upper bound. The affected decision remains the C-II endpoint
quantity (|C|,|H|) at D. A source-realized member of this motion class would
give a finite strict-sub-D contradiction; a proof that its isolate inequalities
force the displacement to zero would identify a precise obstruction. The
remaining blocker is extracting a compatible component and displacement from
every canonical source while keeping all other labels and pairs in the ledger.

## Reproduction and provenance

Run the declared verifier with Python 3.14:

~~~
python research-packages/e99-macbook-20261019T054318Z-03/verify.py
~~~

This proof and independent verifier were produced by OpenAI Codex
(GPT-6 Luna xhigh), producer macbook-03, in the owner's one-time coordinated
cohort. The contribution is offered under Apache-2.0. No external literature,
private source, or unstated dependency is used. The new result remains
unreviewed; required repository-wide theorem-certificate replay is deferred to
the merging agent if the final impact plan requires it.
