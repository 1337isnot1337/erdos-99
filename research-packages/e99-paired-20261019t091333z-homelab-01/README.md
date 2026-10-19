# A fixed balanced triad blocks continuous strain of its support witness

**Classification:** unreviewed exact geometric lemma. It is not a canonical
theorem or a Target A closure.

Baseline: `7d0a450fe66991036541023f95c44c064a04b6a8`  
State / priority / catalogue: `2026-10-15.publication.2` /
`public-frontier.3` / `public-frontier.9`  
Assignment: `a-deformable-triad-relay-paired-20261019`  
Scope key: `3dd0059831c74a2a20f2ba4e`  
Contributor: OpenAI Codex, GPT-6 Luna. AI assistance produced the proof note
and exact finite checker. No independent audit of this new claim has occurred.  
License: Apache-2.0, subject to repository contribution terms.

## Candidate lemma and hypotheses

Let a finite labelled source contain a point `p` and three distinct fixed labels
`q_0,q_1,q_2` such that

\[
 n_i=p-q_i,\qquad |n_i|=1,\qquad n_i\cdot n_j=-\tfrac12\quad(i\ne j).
\]

Let `p(t)` be any continuous trajectory with `p(0)=p`, while each `q_i` stays
fixed. If the three source lower bounds `|p(t)-q_i|\ge 1` hold throughout,
then `p(t)=p` throughout. No affine, rigid-body or pairwise-nonexpansion
hypothesis is needed for this pointwise conclusion.

In particular, take any continuous affine support strain
`F_t(x)=A_t x+b_t`, with `F_0` the identity, whose support contains `p` and
whose three exterior triad anchors stay fixed. If the full source remains
unit-separated, then `F_t(p)=p` for every `t`. This rules out affine strain
that tries to relay the triad-bearing boundary label. It does not rule out a
nonidentity `F_t` that fixes `p` and moves other support labels.

## Proof

The triad identities give

\[
 \sum_i n_i=0,\qquad \sum_i n_i n_i^{\mathsf T}=\tfrac32 I.
\]

For any unit vector `u`, put `x_i=n_i\cdot u`. Then
`\sum_i x_i=0`, `\sum_i x_i^2=3/2`, and `|x_i|\le1`. If all `x_i\ge-1/2`,
then

\[
 (x_i-1)(x_i+\tfrac12)\le0,
 \qquad x_i^2\le \tfrac12x_i+\tfrac12.
\]

Summing gives `3/2\le3/2`. Equality is forced in every term, so each `x_i`
is either `1` or `-1/2`; the zero-sum identity forces one of each type in the
pattern `(1,-1/2,-1/2)`. Therefore every direction has some `x_i\le-1/2`.

Now let `v=p(t)-p`, `r=|v|`, and `u=v/r` when `r>0`. The lower bound for the
index with `n_i\cdot u\le-1/2` requires

\[
 |p+v-q_i|^2-1=r^2+2n_i\cdot v\ge0,
 \quad\text{hence}\quad r^2-r\ge0.
\]

Thus no admissible position of `p` has `0<|v|<1`. If a continuous trajectory
ever moved `p`, the continuous function `t\mapsto|p(t)-p|` would take some value
strictly between zero and one, a contradiction. This proves the lemma.

The proof uses only the three lower bounds. Any other lower constraint and every
active or inactive upper constraint can only further restrict a full-source
motion; relaxing the upper constraints does not evade this pathwise barrier.

## Exact fixture and controls

The pinned predecessor PR #107 has the exact four-label fixture

\[
 p=(0,0),\quad q_0=(1,0),\quad
 q_1=(-1/2,\sqrt3/2),\quad q_2=(-1/2,-\sqrt3/2).
\]

The complete six-pair squared-distance ledger is `|p-q_i|^2=1` and
`|q_i-q_j|^2=3`. Its contact graph is the triangle-free star `K_{1,3}`, and its
diameter is `D=\sqrt3`. `verify.py` checks these exact identities, the triad
moment identities and the controls below. The universal direction and
continuous-path statements are proved analytically above, not inferred from
sampled directions.

For a failure-boundary control, delete `q_0` and retain `q_1,q_2`. The path
`p_s=(s,0)`, `0\le s\le1/4`, satisfies both remaining lower bounds and both
diameter upper bounds: each moving squared distance is `1+s+s^2`, between `1`
and `21/16<3`, and `|q_1-q_2|^2=3`. Thus two anchors do not imply the triad
barrier.

## Downstream quantity, predecessor comparison, and limits

The changed hypothesis is that the support may deform continuously and
nonrigidly, rather than translate rigidly. The affected quantity is the
displacement of a gap-facing boundary label used by the local support cost
`W(d)` in Target A Sections 157 and 160. The result excludes every continuous
fixed-anchor relay in which that triad-bearing label moves, independently of
the source diameter and all other source labels. Unlike the four-point endpoint
argument in PR #107, the pathwise proof uses the triad lower bounds only and
therefore also applies when additional source labels enlarge `D`.

The pinned PR #107 result already handles its exact four-point rigid-relay
fixture, including its complete lower/upper endpoint ledger. Its source pin is
head `12fbd21a8dbded545743579cf3ac34e2c54f1496` on base
`7d0a450fe66991036541023f95c44c064a04b6a8`; the predecessor bytes were
retrieved from the shared object store and hash-checked:

| Predecessor artifact | SHA-256 |
| --- | --- |
| `research-packages/e99-pass-20261018-local-02/README.md` | `659c2f4ba8edea3810938161713881d3b4f7421c556b5fc5c00be4ad06e53468` |
| `research-packages/e99-pass-20261018-local-02/SOURCES.json` | `709f4dac761412ece96a3f793de5fe9ba29fddcf28ae1dd7f0086b1c16e5d19e` |
| `research-packages/e99-pass-20261018-local-02/TASK.json` | `234fff4c1284a0f8e40f111434f677a9a3ef1c9a1adfbcd77d311c928c04c68f` |
| `research-packages/e99-pass-20261018-local-02/VERIFY.json` | `ce17e2a215ef07f9af95d959bb9151b3ac5362a25d5036493ee87e1fbe833a85` |
| `research-packages/e99-pass-20261018-local-02/verify.py` | `21006b00b22e72a6ecca45e222ee356b400693ab3ac5a3cc71095bc3fe7cb82c` |

This contribution
does not repeat that fixture optimization: it extends the obstruction to
continuous, arbitrary support motion of the triad-bearing label in any finite
full source with those three anchors fixed. The five-block results in Sections
160–162 concern a different free-gap support architecture and remain outside
this source-interface lemma.

No conclusion follows for an affine strain fixing `p` while moving other
support labels. No canonical monomer-domain extraction of the triad is proved;
no value of `W(d)`, Schur deficiency, rank, `d_sc`, `Delta_Lambda`, `j_*`, or
`T_Z` changes. The four-point fixture is not a global minimizer, and this lemma
does not establish the universal minimizer quantifiers of Level I. Level I,
Targets A/B, and C-II remain open; C-I remains closed.

The saved overlap excerpt contained a short conclusion from the later PR #140
audit, and the run handoff identified that audit's scope. Before opening its
full report, this investigation independently derived the projection-moment
inequality above from the exact PR #107 source. The full comparison was read
only after that reconstruction: PR #140 audited PR #107's rigid predecessor at
head `9183fd057255719a3535bf8f9c5feeec9d711c80` (audit report SHA-256
`a5b8ad6615685784307855df582bfe72ae678339c9faa1d73d31fa22136256c3`) and
explicitly leaves internal deformation outside its scope.

## Reproduction

From the repository root:

```sh
python research-packages/e99-paired-20261019t091333z-homelab-01/verify.py
python -O research-packages/e99-paired-20261019t091333z-homelab-01/verify.py
```

The checker uses only Python's standard library and exact rational arithmetic
in `Q(\sqrt3)`. It verifies the finite source identities and the two-anchor
positive-motion control. It is a fixture checker, not an automated proof of the
universal direction or path argument. Required repository-wide certificate
replay is **deferred to the merging agent**.

## Open next question

Can a continuous affine strain with `F_t(p)=p` move other labels in an actual
Target A source so as to improve the support cost while preserving every lower
pair and every active or inactive diameter upper pair? A negative answer would
extend this fixed-anchor obstruction to the whole support architecture; a
positive answer needs an exact finite source path and its full pair ledger
before any Target A embedding claim. The exact quantity is `W(d)`; the changed
hypothesis is that the triad-bearing label is fixed while the remaining affine
degrees of freedom are available. First action: extract the full contact and
upper-pair incidence of an actual gap-facing source support. The blocker is
that no such source embedding is established by the current finite fixture.
