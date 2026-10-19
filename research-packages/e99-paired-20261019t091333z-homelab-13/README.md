# Independent destination audit: PR959 reflected-scale parity criterion

**Verdict: PASS for the exact supplied-parameter decision theorem and the
declared finite controls.** This is an independent AI-agent audit of the
destination bytes at base `7d0a450fe66991036541023f95c44c064a04b6a8`, tree
`db766e0e25b562054df26aeec7e627d5a579dd6d`. It does not promote the candidate
or change theorem state. The candidate remains noncanonical and unreviewed.

**Reviewer:** OpenAI Codex, GPT-6 Luna xhigh, homelab-13. **State:**
`2026-10-15.publication.2`; priority `public-frontier.3`; catalogue
`public-frontier.9`. **Scope key:** `51a30d04027d82be51360727`.

## Exact question and hypotheses

For a finite unit-separated planar source (p_1,ldots,p_n), let (D) be its
diameter. Fix a unit normal (u), perpendicular unit tangent (v), offset
(c), and positive squared scales (A,B). Put

\[
x_i=|u\cdot p_i-c|,\qquad y_i=v\cdot p_i,
\]

and choose one sign \(\sigma_i\in\{-1,1\}\) for every source label, giving
the actual planar endpoint position

\[
q_i=(\sqrt A\,\sigma_i x_i,\sqrt B\,y_i).
\]

For each unordered pair define

\[
s_{ij}=A(x_i-x_j)^2+B(y_i-y_j)^2,\qquad
o_{ij}=A(x_i+x_j)^2+B(y_i-y_j)^2.
\]

The audited statement is: a full-label endpoint with every squared distance
in \([1,D^2)\) exists if and only if (i) no pair has \(o_{ij}<1\) or
\(s_{ij}\ge D^2\), and (ii) the multigraph carrying an opposite-sign
constraint when \(s_{ij}<1\) and an equal-sign constraint when
\(o_{ij}\ge D^2\) is parity-consistent. When both inequalities hold for one
pair, both edges must remain. The proof and computations account for every
unordered pair and every label, including any contact isolates.

The only dependencies are the Euclidean coordinate identity and elementary
parity propagation over a signed graph. The result is an exact decision theorem
for supplied parameters; it neither finds parameters nor assumes canonical
global-minimizer structure. If an endpoint is found for a global minimizer with
\(n\ge2\), its same-cardinality unit-separated diameter is strictly below
\(D(n)\), a contradiction. That implication does not supply the parameters.

## Independent proof reconstruction

Because \(x_i,x_j\ge0\),
\[
o_{ij}-s_{ij}=4A x_i x_j\ge0.
\]
Same signs give squared distance \(s_{ij}\); opposite signs give
\(o_{ij}\). If \(o_{ij}<1\), even the larger option is too short. If
\(s_{ij}\ge D^2\), even the smaller option reaches the forbidden upper
endpoint. These are exactly the individual no-choice cases.

After excluding them, \(s_{ij}<1\) makes equal signs invalid and forces
opposite signs. Also, \(o_{ij}\ge D^2\) makes opposite signs invalid and
forces equal signs. All other sign choices for that pair lie in
\([1,D^2)\). Thus each remaining pair contributes zero, one, or two XOR
equations on its endpoint bits. Such equations have a solution exactly when
their parity sum is zero around every graph cycle. Rooting each component and
propagating the bits proves sufficiency; any endpoint supplies the same bits
and proves necessity. Two distinct constraints on the same pair form a
length-two contradictory cycle. Once every pair cost is computed, graph
construction and propagation take \(O(n^2)\) arithmetic/graph operations;
this is not a bit-complexity claim.

Every chosen endpoint bit maps to an actual point in \(\mathbb R^2\). The
pairwise lower bound \(1\) implies no two endpoint labels coincide, so the
endpoint has exactly \(n\) points. The proof does not assume contact-only
checks, a selected stress, an active-diameter subset, or source-point deletion.

## Adversarial checks and reproduced evidence

The new checker uses exact `Fraction` arithmetic. It compares a forced-XOR
system, solved by exhaustive sign-vector enumeration, with direct distances of
every reflected endpoint assignment. On the independent 400-case small-source
domain, the two agree in all cases: 97 feasible, 94 lower-pair obstructions,
119 upper-pair obstructions, and 90 parity inconsistencies. Its all-pairs
classification counts 91 pairwise double-forcing cases and 38 cycle-only
parity failures. The source verifier reports 89/124 lower/upper cases because
its solver exits at the first forbidden pair, while the independent checker
classifies all pairs and gives lower-pair obstructions precedence when a case
has both types. The five shifted labels therefore reflect category precedence;
both implementations agree on feasibility in all 400.

Exact boundary controls separately verify that `o=1` and `s=1` are permitted
at the lower endpoint, while `o=D^2` forces equal signs, `s=D^2` is fatal,
`o<1` is fatal, and `s<1` together with `o=D^2` yields a contradictory
parallel-edge pair.

The pinned candidate verifier also passed. It independently exhausts 400
small rational instances against all sign vectors; retains both contact
isolates in the 157-label fixture; checks all 12,246 endpoint pairs and the
exact interval
\[
\left[\frac{405441}{403202},\frac{865065744}{1008005}\right];
\]
and verifies the two explicit lattice-family controls at \((M,K)=(40,1)\)
and \((60,2)\), with 29,403 and 182,710 pairs respectively. These are exact
finite controls, not evidence of global optimality.

I also checked the linked infinite rectangle proof's decision-relevant bounds.
For \(u=(351,280)/449\), \(v=(-280,351)/449\), \(A=1/2\), \(B=9/5\),
and \(L=4K+2\), a lower-forcing pair must have opposite original normal
signs. Its \(s_{ij}<1\) bound gives \(|\Delta y|<1\); combining
\(|\Delta j|\le2K\) with opposite signs yields both horizontal indices in
\(|i|< (s/c+2c/s)K+1/s < L\). Conversely every same cost is bounded by
\(37M^2/10<4M^2\), while an opposite cost touching that central strip is
bounded by \(3887M^2/1000<4M^2\le D^2\). Hence the stated sign assignment
satisfies all lower and upper pair constraints. The integer quadratic form
forbids equality at one by reduction modulo 5 and then modulo 25. This
supports the report's explicit nonglobal family only; it gives no global
source extraction. The affine-stress and separate moment/Steiner claims are
outside this audit's exact scope.

## Source pins, prior work, and lifecycle

At destination main `7d0a450fe66991036541023f95c44c064a04b6a8`, the exact
candidate artifacts have these SHA-256 values:

| Destination artifact | SHA-256 |
| --- | --- |
| `docs/reports/global_reflected_scale_competitors_2026-10-12.md` | `63f9abd9de3a50d6d52a5ca37354ef6e461425250fea379bd928fe6a6e7dff35` |
| `research/verify_global_reflected_scale_2026_10_12.py` | `caef9c87b7773aa1089ec845d30b35fb09bd70bde5f0264a128b51fc7f531403` |
| `docs/audits/pr959_autonomous_proof_audit_2026-10-15.md` | `30ce4ddc5721a402f0b98080c48d7c0ae5cecbf4b0e27393300983ec60ad34f1` |

The destination report and artifact index classify the source candidate as
unreviewed, with no canonical claim IDs. The 2026-10-15 PR959 audit is an
earlier source-side proof-audit record; it explicitly says it is provenance,
not the destination exact-head audit. I read that record after reconstructing
the proof above. It covers overlapping mathematical and finite scope, and the
new review preserves that credit while independently rebuilding the criterion
against these destination bytes. Live Discussion #83 had no PR959/reflected
parity handoff. Open destination PRs #130, #115, and #118 audit distinct PR958
flattening, palette, and interpolation claims; none audits this PR959 theorem.

No theorem-state, canonical manifest, route, priority, or certificate
registration is changed. The candidate stays unreviewed until an authorized
maintainer makes any separate lifecycle decision.

## Exact commands and limits

- With the shared host compute lock held, provisioned Python 3.14.6 ran `python research/verify_global_reflected_scale_2026_10_12.py` — passed; exact source verifier reported 400/400 parity-oracle cases, the 157-label fixture, both family controls, and its stated no-globality limit.
- With the shared host compute lock held, provisioned Python 3.14.6 ran `python research-packages/e99-paired-20261019t091333z-homelab-13/verify.py` — passed: 400/400 exact small-source cases (97 feasible, 94 lower-forbidden, 119 upper-forbidden, 90 parity-inconsistent), 91 double-forcing pairs, 38 cycle-only parity failures, and all five strict-boundary controls.
- `python scripts/research_package.py --package research-packages/e99-paired-20261019t091333z-homelab-13 --check-only` — `metadata-valid`, classification `unreviewed`, `full_verified=false`, and no command execution. Optional isolated replay remains unauthorized by static dependency analysis (`__debug__`, `__name__`, and the pinned source checker's `dataclasses` import); this does not undo the direct focused run.
- `flock -x <shared host compute lock> python tools/build_artifact_index.py --write` — wrote 1,461 records and updated zero headers.
- `flock -x <shared host compute lock> python tools/build_reading_edition.py` — passed with 2,180 source documents, 72,073 normalized math pairs, and 59 current links; `python tools/build_reading_edition.py --check` passed with zero errors.
- `flock -x <shared host compute lock> python tools/check_public.py` — passed; 1,461 artifacts, 94 certificates, 451 claims, 845 edges, 7 nonredistributed reference links, 25 tasks, zero errors; `mathematical_proof=false`.
- Repository integrity, local CI planning, diff, and live-overlap outcomes are recorded in the PR body and controller `RESULT.md` after running them.

The missing theorem-level step is still: for every sufficiently large
triangle-free global minimizer, derive supplied \((u,c,A,B)\) and a
parity-consistent assignment meeting every lower and strict upper pair bound,
including all labels and inactive pairs. This is the exact parameter-extraction
bridge needed before the finite decision result can affect Level I. The audit
does not prove it, nor prove a uniform onset or a C-II endpoint.

The included checker and proof note are first-party contributions offered
under Apache-2.0. OpenAI Codex (GPT-6 Luna xhigh) produced this independent
proof reconstruction, checker, and audit record; the earlier source audit is
credited as predecessor provenance. No human mathematical review is claimed.
