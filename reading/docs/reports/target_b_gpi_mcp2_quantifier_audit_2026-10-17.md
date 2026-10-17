> Generated reading edition · [exact source](../../../docs/reports/target_b_gpi_mcp2_quantifier_audit_2026-10-17.md) · source SHA-256 `2e6b7243fcba18e9cdc7da055e5acc9216a9fdd64fbd113af83741f9ff37278f`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-CEFA4DB11E08","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-b"} -->
# Target B GPI/MCP2 scope and quantifier audit

**Status:** independent research note; unreviewed. No theorem-state promotion.  
**Source:** `e396ea07887dd0528b817ce4e656ff0e6b01f8fb`; state `2026-10-15.publication.2`; priority `public-frontier.3`; catalogue `public-frontier.7`.  
**Task:** `audit-target-b-gpi-scope`.  
**LEVEL I STATUS: STILL OPEN.**

## Result

This audit found no quantifier or summability defect in the canonical fixed-parameter claims. Reconstructing the Section-50 pruning and PC3 error gives the stated fixed-`lambda` summability in MCP2. The same explicit bounds also yield the diagonal schedule below. GPI remains a theorem for one fixed positive phase ratio under its dominant-component hypotheses; neither it nor MCP2 supplies the full multi-grain shell inequality.

The new diagonal estimate is a scoped, unreviewed consequence of the displayed Section-50 and PC3 bounds. It is not a promotion of `TB-DENSE-GRID` or a closure of Target B.

The inspected inputs are the [canonical dependency audit](target_b_dense_grid_penetration_interpolation_dependency_audit_2026-09-11.md), [Section 50](../targets/target-b/01-jammed-rhombic-branch.md), the [PC3 proof](target_b_penetration_charged_grid_cancellation_2026-09-05.md), the [GPI proof](target_b_explicit_general_phase_interpolation_2026-09-05.md), and the [current Target B route map](../targets/target-b/README.md). The canonical audit supplies the accepted scope of DT1–DT4, TG1–TG3, PDG, PC1/PC3, MCP1/MCP2 and GPI; this note independently reconstructs their parameter order and the use of those scopes.

## Fixed-parameter order

Take a sequence of pure rhombic disks with diameter `D` tending to infinity and train count `T<=C_T D`. Fix `eta,lambda` in `(0,1)` first, as in Theorem 50.1. After deleting edges with angular defect greater than `D^(-1+eta)` and pruning vertices of current degree below `lambda D`, every retained component has minimum degree at least `lambda D` and graph diameter

```text
L_0 <= ceil(3T/(lambda D)) <= ceil(3 C_T/lambda).
```

It follows that the number of retained components is at most `C_T/lambda+1`. The phase error from a root label to any vertex is at most `L_0 D^(-1+eta)`. For fixed `eta,lambda`, this is uniformly `O_lambda(D^(-1+eta))=o(1)` over all retained components.

In PC3, the angular error in one component contributes at most `O(alpha_D (M'_j+b'_j+s_in,j))`, where `alpha_D` is the maximum phase error and `s_in,j` counts in-component separators. Each term in parentheses is `O(D)`. Thus the `o(D)` inside the `j`th PC3 bracket can be taken uniformly over components. Since `d_j=O(D)` and there are `O_lambda(1)` components,

```text
sum_j d_j o(D) = o_lambda(D^2).
```

The deletion ledger is

```text
E_del <= C_delta D^(2-eta) + C_T lambda D^2,
E_del/D^2 <= C_delta D^(-eta) + C_T lambda.
```

Consequently, for each fixed `eta,lambda`, the high-defect and coherence errors vanish after `D -> infinity`, while the normalized deleted-edge allowance is at most `C_T lambda` (times MCP2's explicit factor `2(2/sqrt(3)-1)`). One may then take the outer limit `lambda -> 0` in this scalar bound. This is an iterated limit; the fixed-parameter statement alone does not authorize substituting a `D`-dependent `lambda` into an unnamed `o(D^2)` term.

## A quantitative diagonal schedule for MCP2

The proof of Theorem 50.1 gives more than a pointwise little-oh. If `lambda_D=D^(-kappa)`, then

```text
L_0 = O(D^kappa),
alpha_D = O(D^(kappa-1+eta)),
number of retained components = O(D^kappa).
```

The zero-gain-cycle step still holds when `kappa<1-eta`, since `(2L_0+1)D^(-1+eta)=o(1)`. In PC3 the uniform angular contribution per component is then `O(D^(kappa+eta))`; multiplying by `d_j=O(D)` and summing over `O(D^kappa)` components gives

```text
total coherence error = O(D^(1+2 kappa+eta)).
```

Therefore, for fixed `eta` and

```text
0 < kappa < (1-eta)/2,
```

the sum of PC3 coherence errors is `o(D^2)`. Along the same schedule,

```text
E_del/D^2 = O(D^(-eta)) + C_T D^(-kappa) -> 0.
```

For example, `eta=1/3`, `kappa=1/4` gives a normalized coherence error `O(D^(-1/6))` and a normalized deletion bound `O(D^(-1/4))+O(D^(-1/3))`. This diagonal conclusion is derived from the explicit graph-diameter and phase-defect bounds in Theorem 50.1 and the explicit `O(alpha_D D)` angular term in PC3; it is not obtained by exchanging two bare little-oh limits. The accompanying verifier checks the exponent conditions and the GPI decimal margins, not the geometric lemmas.

## Exact GPI scope

GPI is stated for a fixed `tau>0` and a sequence of one coherent component with

```text
M >= b >= a,   b/M >= tau,
Delta = [M(a+b)-E]/M^2,
```

plus triangle-freeness, `o(1)` phase coherence, `o(M^2)` crossings involving outside trains, and the core-carrying hypotheses `R=E+o(M^2)` and `T=O(M)`. Its conclusion is

```text
liminf Delta >= 4e-17 tau^2.
```

The ratio is fixed before the asymptotic limit. From the Section-50 degree floor, a vertex in the largest phase class has at most `a+b<=2b` retained neighbors, so `lambda D<=2b`. Since `M<=T<=C_T D`, any selected retained component has `b/M>=lambda/(2 C_T)`. A safe fixed GPI parameter is `tau_lambda=min(1,lambda/(2C_T))`. If such a component exists and `lambda/(2C_T)<=1`, the resulting coefficient is `1e-17 lambda^2/C_T^2`; if the ratio bound exceeds one, no such component can exist. This application is valid only **if that component also satisfies GPI's core-carrying and outside-crossing hypotheses**.

Two restrictions follow. First, an arbitrary retained component need not carry the global quadratic rhombus core: several grains may share it, so GPI cannot be applied to every component and summed. Second, along the diagonal schedule `lambda_D=D^(-kappa)`, the degree argument only gives `tau_D=D^(-kappa)/(2C_T) -> 0`. The fixed-`tau` GPI theorem does not by itself give a uniform result for this varying parameter. The diagonal MCP2 estimate above therefore supplies no local GPI deficit and no multi-grain closure.

## Remaining global gap

Target B still requires a source-valid inequality coupling retained physical crossings, deleted/interface crossings, and virtual noncrossing determinant mass, or a full source-preserving strict sub-`D` competitor. The diagonal schedule makes the displayed MCP2 pruning and coherence losses negligible, but does not force a large enough complete grid, give a source-wide deficit payment, or connect local deficits to the global diameter. The canonical state still reads **Target B OPEN; Level I OPEN**.

## Reproduction and scope

From the repository root, run:

```sh
python research/verify_target_b_gpi_mcp2_quantifier_audit_2026_10_17.py
python tools/check_public.py
git diff --check
```

The verifier uses only the Python standard library and checks rounded GPI arithmetic and the stated rational exponent example. It does not verify Theorem 50.1, PC3, the GPI geometric argument, source extraction, global minimizer hypotheses, or the conjecture.

The refreshed overlap scan found the adjacent two-grain interface handoff and [open PR #86](https://github.com/1337isnot1337/erdos-99/pull/86) (`compute-b-two-grain-interface-regressions`); those finite inventory calculations are not repeated here. This note audits the fixed-parameter scope and the phase-error summation. Originating AI agent: OpenAI Codex GPT-6, for proof reconstruction and the arithmetic verifier. No independent review of this new diagonal consequence has been performed; it remains unreviewed under the repository policy. This contribution changes no canonical state, priority, or task card; the PR requests review without canonical promotion.
