> Generated reading edition · [exact source](../../../docs/reports/target_c_core_unilateral_local_rigidity_gap_slot07_2026-10-10.md) · source SHA-256 `807b5ca23e786a96c43ba5ae5a1fc643e05afc1af80f038b99a201924fb6d2ef`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-D96B18829DF6","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II: unilateral local-rigidity gap for stress transversals

**Worker slot:** 07
**Date:** 2026-10-10
**Starting main SHA:** `ab6dd3336f9f8d440f2bada76edb32153391cddc`
**Theorem state:** `2026-10-10.audit.234`
**Branch:** `research/sol61-slot07-20261010-stress-transversal`
**Classification:** proved candidate awaiting independent audit. This report does not promote a theorem or change C-II/Level I status.

## 1. Target and implication chain

The assigned gap is the cardinality-restoration step after a stress-transversal deletion. Under their recorded hypotheses, canonical Audits 87, 90, 170, and 171 give a strict first motion on the reduced source, with every retained source label—including contact isolates—still accounted for. Audit 90 separately proves that no assignment of velocities to the deleted unloaded core labels can make every deleted old contact open along that same reduced descent. This report strengthens that obstruction from first derivatives to a finite source-dependent distance barrier.

The proposed chain is

```text
full-support positive KKT stress + mixed-core infinitesimal rigidity
  -> explicit positive distance from the canonical core to every
     noncongruent placement satisfying all old contact lower bounds
     and old diameter upper bounds
  -> no continuous local restoration of any stress-transversal deletion
  -> any successful cardinality-restoring endpoint must use a nonlocal
     core relocation or discrete replacement.
```

The result narrows the motion route. It does not produce the required nonlocal replacement or close C-II.

## 2. Canonical inputs and notation

Let `A={p_i:i in X}` be the canonical contact-minimal, then actual-diameter-pair-minimal triangle-free global minimizer, with diameter `D>=9`. Let `V` be its nonisolated positive-contact core, `v=|V|`; let `C` be every actual unit-contact edge on `V`, and `H` the active actual diameter-edge set on `V`. Every endpoint of a row in `H` belongs to `V`. Contact-isolated labels remain in the full source, outside the core stress and rigidity matrices.

Use a relative-interior normalized KKT stress `(alpha,beta)` on these rows:

```text
R_C^T alpha - R_H^T beta = 0,
alpha_e > 0 (e in C),
beta_h > 0 (h in H),
sum_h beta_h = 1.
```

Here `R_{ij}u=(p_i-p_j) dot (u_i-u_j)`. The virial identity is `sum_C alpha_e=D^2`. Canonical `C-ZRF` gives

```text
rank R_{C union H}[V] = 2v-3,
ker R_{C union H}[V] = K,
```

where `K` is the three-dimensional space of planar infinitesimal Euclidean motions `u_i=a+omega J p_i`.

Set `m=|C|+|H|`, `alpha_min=min_e alpha_e`, and `beta_min=min_h beta_h`. Let

```text
sigma = min { ||R_{C union H} u||_2 : u in K^perp, ||u||_2=1 } > 0,
Lambda = max(1, D^2/alpha_min, D^2/beta_min),
epsilon_A = sigma/(sqrt(m) Lambda).
```

All constants are finite and source-dependent. No lower bound uniform in `n` is claimed.

## 3. Unilateral local-rigidity theorem

**Theorem (proved candidate).** For every planar placement `Q=(q_i)_{i in V}` satisfying

```text
|q_i-q_j| >= 1 for every {i,j} in C,
|q_i-q_j| <= D for every {i,j} in H,
```
either `Q` is congruent to `P=(p_i)_{i in V}`, or

```text
dist_2(Q, Iso(P)) >= epsilon_A.
```
`dist_2` is Euclidean distance in the `2v` coordinate space, minimized over all translations, rotations, and reflections of the core. Thus the theorem gives a concrete finite-source radius around the congruence orbit in which the unilateral active constraints admit only congruent core placements.

### Proof

Assume `Q` is not congruent to `P`, and let

```text
d = dist_2(Q, Iso(P)) > 0.
```
Choose an isometry `T` minimizing `||Q-TP||_2`. The residual `Q-TP` is orthogonal to the tangent space of the isometry orbit at `TP`; applying `T^{-1}` maps that tangent space to `K`. Thus, after replacing `Q` by `T^{-1}Q`, the residual `Delta=Q-P` has `||Delta||_2=d` and `Delta` is orthogonal to `K`. Put `u=Delta/d`; then `u in K^perp` and `||u||_2=1`.

For a contact row `e={i,j}`, write `r_e=p_i-p_j` and `Delta_e=Delta_i-Delta_j`. The lower-distance constraint gives

```text
|r_e+Delta_e|^2 >= |r_e|^2=1,
R_e u >= -|Delta_e|^2/(2d) >= -d,
```
since `|Delta_e|^2 <= 2||Delta||_2^2=2d^2`.

For a diameter row `h={i,j}`, `|r_h|=D` and the upper-distance constraint gives

```text
|r_h+Delta_h|^2 <= |r_h|^2,
R_h u <= -|Delta_h|^2/(2d) <= 0.
```

Stationarity yields the stress-work identity

```text
S := sum_C alpha_e R_e u = sum_H beta_h R_h u.
```
The contact bounds and `sum alpha=D^2` imply `S >= -D^2 d`; the diameter bounds imply `S <= 0`. Isolating one term in these sums gives, row by row,

```text
-d <= R_e u <= D^2 d/alpha_e       (e in C),
-D^2 d/beta_h <= R_h u <= 0       (h in H).
```
Therefore `||R_{C union H}u||_2 <= sqrt(m) Lambda d`. By the definition of `sigma`, the left side is at least `sigma`, so `d >= sigma/(sqrt(m)Lambda)=epsilon_A`. This proves the claim.

## 4. Consequences for full-source competitors and stress transversals

Every full-source placement with all pair distances at least one and diameter `D'<D` satisfies the theorem's old-contact and old-diameter inequalities on `V`. It cannot be congruent on `V`, because every old row in `H` has length `D` while the new full-source diameter is smaller. Hence every such placement must displace the core by at least `epsilon_A` modulo Euclidean motions. Contact-isolated labels are still present in this statement; moving them cannot evade the core lower bound.

In particular, take any canonical stress-transversal deletion supplied by Audits 87, 90, 170, or 171 and its strict reduced-source motion. If one tries to restore the deleted labels by a continuous assignment starting at their original coordinates while the core remains in a sufficiently small neighborhood of the source, the resulting full placement would violate the theorem as soon as it strictly lowered diameter. Thus the reduced strict motion cannot be integrated into a nearby same-cardinality strict-diameter endpoint, even by a non-differentiable restoration path. The restored labels must cross a source-dependent positive core-displacement barrier, or the proposed endpoint must arise from a different nonlocal rearrangement.

The proof checks every row in `C union H`; any additional lower constraints, newly active upper pairs, or retained-isolate pairs only restrict feasible full-source placements further. No contact isolate is deleted or treated as a core coordinate.

## 5. Adversarial checks and limitations

- **First-order restoration:** Audit 90 already proves the stress-weighted sum of deleted-contact derivatives is negative for every completion of the reduced velocity. The present theorem is stronger: it rules out every sufficiently small finite restoration, including assignments with no derivative at the source.
- **Square-root or other singular scaling:** the proof does not assume a power-series path. The global distance bound applies to every feasible placement and rules out all noncongruent placements inside the explicit radius.
- **Inactive pairs and isolates:** these are not used to obtain the bound. A full-source competitor must satisfy the old core rows, and the isolates remain part of that competitor.
- **Remote alternatives:** the theorem permits feasible placements at distance at least `epsilon_A`; it neither constructs nor rules out such placements.
- **Asymptotics:** `alpha_min`, `beta_min`, and `sigma` may degenerate with `D`. The bound gives no uniform radius along a sequence of minimizers and therefore no Level I contradiction.
- **Canonical scope:** the proof needs infinitesimal rigidity of the mixed core matrix and a stress strictly positive on every row in `C union H`. It gives no displacement control for contact-isolated labels themselves; those labels remain in the full source and may move within their inactive margins.

Three restoration mechanisms were separated. A velocity assignment is blocked by the existing Audit 90 regression. A continuous but nonsmooth local assignment is blocked by this theorem. A finite nonlocal discrete replacement remains the only unaddressed mechanism in this local route, and it must still pass every source-pair lower bound and every actual-diameter upper bound.

## 6. Exact remaining theorem

The next closure theorem is source-specific and global:

> For every sufficiently large canonical triangle-free minimizer in the relevant C-II branch, construct a same-cardinality full-source discrete replacement that moves the core beyond the source-dependent `epsilon_A` barrier, preserves all pair distances at least one, and either has diameter below `D` or has diameter `D` with fewer contacts. Include all contact-isolated labels and all old/new diameter pairs in the endpoint check.

The present result makes the local obstacle explicit but supplies no such endpoint. The global C-II and Level I quantifiers remain open.

## 7. Dependencies and validation boundary

Canonical dependencies used are `C-ZRF` (core mixed infinitesimal rigidity and row rank) and the relative-interior full-support KKT stress in the current Target C normalization. The stress-transversal application additionally uses the reduced-source outcomes of `C-UNLOADED-KKT-STRESS-TRANSVERSAL`, `C-PRESELECTED-LOADED-UNLOADED-TRANSVERSAL`, and `C-ALMOST-ACCESSIBLE-STRESS-TRANSVERSAL`; those claims remain exactly within their recorded scopes. No unmerged PR #947 claim is used as a theorem input.

This is an analytic proof; no finite verifier or numerical certificate is claimed. State/tool checks validate only repository metadata, not the independent mathematical audit of this candidate.

## 8. Reproducible repository validation

On this branch, the following commands passed:

```text
python3 tools/build_artifact_index.py --write --write-headers
python3 tools/check_theorem_state.py
theorem-state: OK
python3 tools/check_active_route_summaries.py
active-route-summary: OK
python3 tools/check_theorem_state_pr.py --base-ref origin/main
theorem-state: OK
git diff --cached --check
```

The hosted `state-consistency` job for PR #951 failed before executing a step: the Actions job record has an empty runner name and an empty step list, and GitHub exposes no job log. One rerun had the same startup failure. This does not replace the passing local checks and gives no mathematical evidence about the candidate.
