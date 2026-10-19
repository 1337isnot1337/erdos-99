<!-- theorem-state: {"artifact_id":"ART-7B6F9C6B4A70","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Destination exact-head review: positive-leaf anchor boundary distance


## Disposition

**CONDITIONAL.** At destination base `7d0a450fe66991036541023f95c44c064a04b6a8`, the implication from the two endpoint direction estimates in `TARGET-C-NEAR-DIAMETER-PAIR-MIDPOINT-BOUND-PR947` to

\[
\operatorname{dist}(a,\partial K_D)=O(D^{-2/3})
\]

is valid under the positive-leaf hypotheses below. The near-diameter premise is itself unreviewed and noncanonical in this destination. Therefore this audit does **not** strengthen the accepted `O(D^{-1/2})` statement `C-POSITIVE-LEAF-ANCHOR-INNER-BALL-BOUNDARY`. It establishes no vacancy, packet, movement, port-count improvement, C-II closure, or Level I result.

## Exact scope and inputs

- Destination head reviewed: `7d0a450fe66991036541023f95c44c064a04b6a8`.
- State: `2026-10-15.publication.2`; priority: `public-frontier.3`; catalogue: `public-frontier.9`.
- Candidate: `TARGET-C-POSITIVE-LEAF-ANCHOR-D23-PR947`, source PR [#947](https://github.com/1337isnot1337/e-99/pull/947), source head `1afb7e64d47c5619d872d32759b0e01f1526fd5a`, source base `d999528cfaafd811a4a19bcfacd00f217c2fc375`.
- The destination report bytes match the registry's SHA-256 `c46e90b1975345be2704b4df3085d63f5b84b15402ae6f9214a49faa3e3f32f7` and Git blob `906a2a49a5824fe6729f75980fe35a833a0936f3`. The corresponding source report bytes at the recorded source head match SHA-256 `f7df6238d32925d18a2a593f25ff631ef29d8fcd16e3767235f8e3c21dd51cf8` and blob `9668230200c9c2cac9a87d515bd31449bf487a35`.
- The second-referee report matches source and destination SHA-256 `08a363adb26216a9d5893891bae50d597b309341d7b146c97311a3b7b7102257` and blob `c3ea728a827f276474fb846823f2e8219d705487`. The referee ledger's source SHA/blob are `99a04e0c2505d7eb01d0a05388fd4fb92be78addfd4f8240a62ce78508c7768c` / `59224819f8e5df1ffba6f2d32194ddebc2fb31f4`; the destination SHA/blob are `a113dd7604cad043df72e0fe29cfc8487b808acc6ce0dd86ea1d9d09859f7e7e` / `c828d282def62a7913e3c89ff7d8f87337bf8a5b`. All six source/destination hash pairs were recomputed against the source PR head and this destination commit.

The precise question is: assuming the candidate near-diameter endpoint bounds at deficits `s=0` and `s=2`, do they force the stated boundary-distance rate for every qualifying positive leaf while retaining every source label? The hypotheses are a noncollinear global minimum-diameter source with `D` tending to infinity; an actual diameter endpoint `p` with exactly one actual unit neighbor `a`; a positive coefficient for contact `pa` in a normalized full-source KKT stress; the canonical full-source circumradius bound `R<=D/2+eta`, `eta=3^(1/4)sqrt(D)`; and the two stated near-diameter endpoint bounds for the same source. `K_D` and every intersection below use all points of `A`, including contact isolates.

At this destination head, `C-FS-GEOM` and `C-FS-DIAMETER-MIDPOINT-D2-3` are canonical. The required endpoint estimates come from the separate unreviewed near-diameter candidate, which in turn lists an unreviewed midpoint-tail candidate relation. This review takes only the endpoint estimates as an explicit conditional premise and does not audit those candidate proofs.

The exact canonical quantity affected is only `dist(a,partial K_D)` in `C-POSITIVE-LEAF-ANCHOR-INNER-BALL-BOUNDARY`; its accepted rate remains `O(D^(-1/2))` unless the near-diameter candidate is separately audited and adopted. A successful conditional implication may sharpen a local boundary input; it does not supply the source-realized move required by C-II. A failure would leave only the existing canonical rate and identify the failed inequality below.

## Reconstruction of the conditional implication

Let `c` be a full-source circumcenter and write `n=p-a`, so `|n|=1`. For a distinct source point `x`, put `d=|p-x|` and `nu=(p-x)/d`. The unreviewed near-diameter candidate gives, for `d>=D-2`,

\[
|(p-c)\cdot J\nu|\le 13D^{2/3}+4D^{1/3};
\]

for an actual diameter partner the same bound holds with `s=0`. Also `|x-c|<=R`, so

\[
(p-c)\cdot\nu=(x-c)\cdot\nu+d\ge d-R\ge D/2-\eta-2
\]

when `d>=D-2`; for `d=D` the lower bound is `D/2-eta`. These longitudinal components are positive for sufficiently large `D`. Dividing the transverse bounds by them shows that every direction `nu` for a pair with `d>=D-2`, and every actual diameter normal at `p`, lies within an angle `epsilon=O(D^(-1/3))` of `e=(p-c)/|p-c|`.

At `p`, the positive contact coefficient and full-source KKT balance give

\[
\alpha n=\sum_y\beta_y(p-y),\qquad \alpha>0,\quad\beta_y\ge0,
\]

where nonzero terms are actual diameter partners. Thus `n` is a positive combination of diameter normals in the same arc about `e`. For sufficiently large `D` that arc has width less than `pi`; its positive hull stays in the arc, so the angle between `n` and any `nu` above is at most `2epsilon`. Hence

\[
n\cdot\nu\ge\cos(2\epsilon)\ge1-2\epsilon^2=1-O(D^{-2/3}).
\]

Since `a=p-n`, for `d>=D-2`,

\[
|a-x|^2=|d\nu-n|^2=(d-1)^2+2d(1-n\cdot\nu)
\le(d-1)^2+O(dD^{-2/3}).
\]

Here `d<=D` and `d-1>=D-3`; rationalizing the square root gives `|a-x|<=d-1+O(D^(-2/3))<=D-1+O(D^(-2/3))`, uniformly over these `x`. For `d<D-2`, the triangle inequality gives `|a-x|<=d+1<D-1`. Thus for some `delta=O(D^(-2/3))`,

\[
|a-x|\le D-1+\delta\quad\text{for every }x\in A.
\tag{1}
\]

It remains to turn (1) into distance to the boundary, not merely an outer-radius estimate. Choose any actual diameter pair `u,v`, let `z=(u+v)/2`, and set `r=(1-\sqrt3/2)D-1`. For every source point `x`,

\[
|x-z|^2=\frac{|x-u|^2+|x-v|^2}{2}-\frac{D^2}{4}\le\frac{3D^2}{4}.
\]

Therefore the full ball `B(z,r)` lies in `K_D=\cap_{x\in A}\overline B(x,D-1)` for large `D`; in particular `K_D` is nonempty and has interior. Let `W_D=\cap_{x\in A}\overline B(x,D)`. Then `K_D+B(0,1)\subset W_D`. Each `p-y` in the KKT sum is an outward support normal to its active disk `B(y,D)` at `p`; since `W_D` is contained in that disk, it also supports `W_D` at `p`. Their nonnegative sum supports `W_D` there. Consequently

\[
h_{K_D}(n)+1\le h_{W_D}(n)=n\cdot p,
\]

so `h_{K_D}(n)<=n dot a`. Thus `a` is outside `K_D` or lies on its boundary.

Set `theta=r/(r+delta)` and `q=theta a+(1-theta)z`. For every `x in A`, using (1), `|z-x|<=sqrt(3)D/2=D-r-1`, and `theta delta=(1-theta)r`,

\[
|q-x|\le\theta(D-1+\delta)+(1-\theta)(D-r-1)=D-1.
\]

Hence `q in K_D`. Also `|a-z|<=D`, because `a,u,v` are source points of diameter `D`. If `a` is on the boundary the desired distance is zero; otherwise the segment from `a` to `q` reaches `partial K_D`, with

\[
\operatorname{dist}(a,\partial K_D)\le|a-q|
=\frac{\delta}{r+\delta}|a-z|=O(D^{-2/3}).
\]

Every disk inequality here is imposed for every `x in A`; no contact isolate is dropped. The centers also have separate roles: `c` gives the endpoint cone, while `z` supplies the inball and contraction.

## Adversarial checks and falsification attempts

- A positive combination could leave a narrow arc only if the arc were not a convex cone. Its aperture is `2epsilon<pi` for sufficiently large `D`, so the positive hull remains inside it. The angular loss in the dot product is quadratic, which is the source of the `D^(-2/3)` scale.
- The near-pair estimate is used only for `d>=D-2`; all shorter pairs are covered by the strict triangle-inequality bound. The error after square-root rationalization is uniform because `d-1` is order `D` on the near branch.
- The supporting-normal step needs the contact multiplier to be positive and diameter multipliers nonnegative. Dropping that sign condition would break the cone argument; it is explicitly among the hypotheses.
- The contraction checks the radius constraint against every retained source point. Replacing the full source by the nonisolated core would not justify either (1) or the inball membership.
- I found no counterexample to this conditional implication. I did not reproduce the proof of the near-diameter candidate itself and do not count the source PR's PASS language or second-referee note as authority for that premise.

## Existing review evidence and process limitation

Source PR #947 contains Audit.247 and a second-referee reconstruction of the same cone and contraction argument. The destination candidate registry at the reviewed head explicitly records “destination mathematical audit not performed”; its artifact index keeps both imported audit records unreviewed. The byte checks above confirm that the current destination proof report is the registered import from that source PR.

During my initial exact-string repository search, the text of Audit.247 and the second-referee proof was surfaced before I wrote this reconstruction. I therefore do not present this as a blind review. I re-derived the conditional geometry and inequalities from the source hypotheses, and treat the earlier PASS records only as predecessor and provenance evidence. This review is by a different AI agent from the source report, but the review-order limitation should remain visible to any later evaluator.

**Remaining named lemma:** independently establish `TARGET-C-NEAR-DIAMETER-PAIR-MIDPOINT-BOUND-PR947` at an exact destination head, including the uniform endpoint transverse bound for `s=0` and `s=2`, from canonical premises. Only then can this conditional review be used toward the stronger anchor claim. The separate source-realized C-II move remains open.

## Reproduction and attribution

The artifact/hash inspection used `gh pr view 947 --repo 1337isnot1337/e-99`, GitHub's contents API at source head `1afb7e64d47c5619d872d32759b0e01f1526fd5a`, local `sha256sum`, `git hash-object`, and the supplied offline overlap snapshot. Current destination `origin/main` matched the reviewed base SHA. The proof is analytic; no finite verifier claims to encode the cone or contraction argument.

OpenAI Codex (GPT-6 Luna xhigh) produced this destination review. It uses only project-authored research inputs and repository definitions; no external text or third-party material is included. The source report and prior referee records remain credited by their linked paths and source PR. This is an agent audit artifact, not human peer review or a theorem promotion transaction.
