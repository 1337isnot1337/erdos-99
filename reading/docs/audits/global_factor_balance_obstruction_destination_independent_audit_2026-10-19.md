> Generated reading edition · [exact source](../../../docs/audits/global_factor_balance_obstruction_destination_independent_audit_2026-10-19.md) · source SHA-256 `bdfdc5a9aea3a6440037e5859760f644e9aef5432e814d53de9c52b312225a72`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-4497C74058D9","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# Destination exact-head audit: GLOBAL-FACTOR-BALANCE-OBSTRUCTION

**Disposition: PASS for the exact conditional formal-array theorem and its convex-hull equivalence.**

This review covers only `GLOBAL-FACTOR-BALANCE-OBSTRUCTION`, investigation `audit-global-factor-balance-obstruction-paired-20261019` (scope key `cb843383ded632c11c182963`), at destination `main` commit `7d0a450fe66991036541023f95c44c064a04b6a8` (tree `db766e0e25b562054df26aeec7e627d5a579dd6d`). The recorded state is `2026-10-15.publication.2`, priority `public-frontier.3`, and catalogue `public-frontier.9`. It is not a review of the support-measure card's broader global-minimizer question. The candidate record marks the claim unreviewed; the destination artifact index marks all three source reports **unreviewed**. This audit does not promote a claim or change Level I, A, B, C-I, or C-II.

**Reviewer:** OpenAI Codex, GPT-6 Luna xhigh, assigned independent reviewer. I reconstructed the log argument before reading the earlier source-audit conclusions. No human mathematical review is claimed.

## Exact statement audited

Let `P=(p_i)_{i in V}` be a finite planar unit-separated source with `n>=2`, diameter `D>=1`, and `q_ij=|p_i-p_j|^2` for every unordered pair `i<j`. Define the actual contact family `C={ij:q_ij=1}` and actual diameter family `H={ij:q_ij=D^2}`. Suppose `a_e,b_f>=0`, with

```math
\sum_{e\in C}a_e=\sum_{f\in H}b_f=1,
\qquad
\sum_{e\in C:i\in e}a_e=\sum_{f\in H:i\in f}b_f\quad(i\in V).
```

For any positive factors `s_i>0`, set `q'_ij=q_ij s_i s_j` on the **complete** set of source pairs. Then

```math
\frac{\max_{i<j}q'_{ij}}{\min_{i<j}q'_{ij}}\ge D^2.
```

Moreover, for `D>1`, this bound holds for every positive factor vector exactly when the convex hulls of the incidence vectors `v_ij=e_i+e_j` in `R^V`, for `ij in C` and `ij in H`, intersect. Intersection is equivalent to the displayed normalized nonnegative weights. The `D=1` case is immediate: `C=H` is the full pair family and the ratio is at least one.

## Independent proof reconstruction

Write the common incidence at label `i` as `nu_i`. Since contacts have `q_e=1`, diameter pairs have `q_f=D^2`, and both weight families have total mass one,

```math
\begin{aligned}
\sum_{f\in H}b_f\log q'_f-\sum_{e\in C}a_e\log q'_e
&=\log D^2+\sum_{i\in V}\nu_i\log s_i-\sum_{i\in V}\nu_i\log s_i\\
&=\log D^2.
\end{aligned}
```

Let `M=max_{i<j}q'_ij` and `m=min_{i<j}q'_ij`. The diameter-weighted average is at most `log M`, while the contact-weighted average is at least `log m`. Subtracting gives `log(M/m)>=log D^2`. This proves the assertion for arbitrary positive factors, with no metric assumption on `q'`.

For the equivalence, a common point of the two finite convex hulls is exactly a pair of probability weight vectors with equal coordinates at every label. Conversely, if the compact convex hulls are disjoint, strict separation gives `x in R^V` with

```math
\min_{ij\in C}(x_i+x_j)>\max_{ij\in H}(x_i+x_j).
```

Set `s_i=exp(t x_i)`. At `t=0`, the complete array has minimum one exactly on `C`, maximum `D^2` exactly on `H`, and every other pair has a strict gap from both. Since there are finitely many pairs, for sufficiently small `t>0` the new minimum remains in `C`, the maximum remains in `H`, and

```math
\log(M(t)/m(t))=\log D^2+t\left(\max_H(x_i+x_j)-\min_C(x_i+x_j)\right)<\log D^2.
```

Thus disjoint hulls produce a formal improving factor array, proving the converse. This construction is not a Euclidean or planar realization theorem.

The realized-length statement in the factorized-distance report is a special case: if `|q_i-q_j|=r_i r_j |p_i-p_j|` for a placement `Q`, then its squared array uses positive factors `s_i=r_i^2`. The squared ratio is at least `D^2`, equivalently its length ratio is at least `D`. Normalizing the minimum length to one cannot make a strict-sub-`D` competitor.

## Adversarial scope checks

- **Normalization and signs:** both weight sums equal one, and all weights are nonnegative, so each displayed sum is a probability average. Positivity of `s_i` and `q_ij>=1` makes every logarithm finite. Zero-weight edges contribute nothing; the proof needs no strict positivity of edge weights.
- **Contact-isolated labels:** every label has its own balance equation. If an isolate has zero incidence in both supported families, its factor cancels as `0 log(s_i)-0 log(s_i)`. If it is a positive-weight diameter endpoint but has no contact incidence, the balance hypothesis fails and the theorem makes no assertion. Every isolate still participates in the complete-array extrema `M,m`.
- **Inactive pairs:** the forward bound takes extrema over every unordered pair, so an inactive pair becoming a new extremum cannot evade it. In the converse, strict inactive gaps and finiteness justify one common sufficiently small `t`; this is not an assumption that an inactive upper constraint stays inactive for arbitrary `t`.
- **Necessity of balance:** the pinned separable-distortion checker includes a four-label collinear formal array with source ratio `9`, positive factors giving formal ratio `6`, and Cayley–Menger determinant `-72`. This is a valid regression to the universal-factor claim when the incidence hulls are disjoint, and the nonzero determinant rules out treating that improved array as a planar four-point placement.
- **Isolate-inclusive exact control:** I separately checked the exact nine-label source consisting of a unit-edge regular octagon and its center. In `Q(sqrt(2))`, the rim squared chord values for cyclic gaps `1,2,3,4` are `1, 2+sqrt(2), 3+2sqrt(2), 4+2sqrt(2)`, and each center-to-rim squared distance is `1+sqrt(2)/2`. The center is a contact isolate and is not a diameter endpoint. Weights `1/8` on the eight rim contacts and `1/4` on the four antipodal diameter pairs give incidence `1/4` at every rim label and zero at the center. In vertex order `0,...,7,center`, the four exact rational factor vectors were `[1,2,3,4,5,1/2,2/3,3/5,1]`, `[1/10,10,1/3,5,7/2,2,1/7,9,100]`, `[3,1/5,9,1/10,2,5/3,4,1/8,1/100]`, and `[1/100,20,1/50,8,1/3,7,1/9,11,1000]`. Exact comparisons over all 36 pairs give full-array ratio at least `D^2=4+2sqrt(2)` in each case. This finite fixture checks isolate and full-pair bookkeeping; it is not a proof of the universal statement.
- **Geometric bridge:** the disjoint-hull separator only supplies formal factors. The nonplanarity regression and the report's own scope statement correctly prevent an inference from formal array improvement to a planar configuration. No global-minimizer property, triangle-freeness, large-`n` quantifier, or balanced certificate for every minimizer is proved here.

## Inputs, lifecycle, and predecessor comparison

The three assignment-pinned reports were read at the exact destination bytes. Each destination SHA-256 matches its assignment pin:

| Destination artifact | Git blob at reviewed head | SHA-256 |
| --- | --- | --- |
| `docs/reports/global_separable_distortion_obstruction_2026-10-12.md` | `0010924a77aa84485e16cd49109a27cea33e41f2` | `de71af209c8ea4753862de88d0a9029ab4d209dc4ce439096547ad8aad56a439` |
| `docs/reports/global_factorized_distance_barrier_2026-10-12.md` | `eab3d98818f1a77ea084e9fc823de1b7525c821d` | `bd5e04fc103c1d172af746c44595c7c9efeec68918ba30d7f71f4d00339e54e2` |
| `docs/reports/global_vertex_factor_relocation_2026-10-12.md` | `843d297b766866b4fce3f36c9009e0cefb919181` | `a6d34bcadceef3087ebd91529fc987e8b7053ad295d4f7a1f68ad3393cddae57` |

The first report gives the stronger formal-array equivalence; the second gives its realized-length corollary, regular-rim family, and explicit scope boundary. The third is listed as the planar-realization/factor-obstruction predecessor; its separate classification is not a load-bearing dependency of the audited formal theorem. That predecessor cites conformal-map literature as background, but neither it nor any other external theorem is used in this log/convexity proof. Candidate metadata lists no canonical theorem dependencies. The broad support-measure card's Oler and lattice-reserve prerequisites are not imported into this exact audit.

I read `docs/audits/pr960_autonomous_proof_audit_2026-10-15.md` only after reconstructing the proof above. It audits the originating source PR and explicitly identifies itself as provenance rather than the destination exact-head audit. The destination artifact index at the reviewed head marks the three candidate reports **unreviewed**; the source report's historical audit therefore does not discharge this destination review. No other exact destination audit was present in the local audit registry, prior local/homelab/MacBook handoffs, Discussion #83, or the live open-PR bodies and changed-file lists examined for this assignment.

No canonical claim is advanced. The concrete remaining bridge is a source-globality argument that produces an actual planar, same-cardinality competitor with all lower and upper pair constraints checked. Excluding balanced incidence alone only gives a formal improving array; it does not realize that array in the plane. A direct nonfactorized planar replacement would also discharge the route obligation.

## Reproduction and limits

At the reviewed commit, these unchanged source verifiers were run serially under the shared host compute lock:

```text
flock -x /home/cinna/.local/state/erdos99-host-compute.lock python research/verify_global_separable_distortion_obstruction.py
PASS: 499 odd-rim incidence certificates (m=5,...,1001)
PASS: 122 exact cyclotomic all-pair Mobius identities
PASS: formal improved squared ratio 6 < 9; Cayley–Menger determinant -72

flock -x /home/cinna/.local/state/erdos99-host-compute.lock python research/verify_global_factorized_distance_barrier.py
PASS: 98 regular-rim incidence/product checks; 5 rational square inversions with all 6 pairs checked each
```

The repository catalogue has no registered checks for the broad alternative-support card; the candidate metadata names these two scripts. Their finite outputs corroborate only the listed exact families and identities. The handwritten octagon-plus-center control is a bounded audit calculation, not a registered verifier. No repository-wide theorem-certificate replay was run; **required full replay deferred to the merging agent**. No external theorem or third-party data was imported. The source PR #960 audit credits the originating proof/checker work to OpenAI Codex (GPT-6); the separate PR #995 planar-classification material is identified as a predecessor, not a dependency. This review was produced with OpenAI Codex (GPT-6 Luna xhigh).
