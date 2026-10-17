> Generated reading edition · [exact source](../../../docs/audits/target_c_angular_surplus_bounded_variation_chart_independent_audit_2026-10-09.md) · source SHA-256 `be577aa3325026703aa20904d5ad3a7f954ac75768d34ddeedf6951c5e25367f`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-77784B652D48","canonical":true,"claim_ids":["C-ANGULAR-SURPLUS-BOUNDED-SHORE-VARIATION","C-TYPEII-ACTUAL-RHOMBUS-CHART-EXCLUSION"],"claim_statuses":{"C-ANGULAR-SURPLUS-BOUNDED-SHORE-VARIATION":"canonical","C-TYPEII-ACTUAL-RHOMBUS-CHART-EXCLUSION":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C Audit.215 — angular surplus forces bounded chart variation

Date: 2026-10-09. Audit base: `origin/main=bb6e6309e5c2a639c965b97ab446cb11e1e1d528`, state `2026-10-09.audit.209`.

## Frozen candidate and verdict

- Source branch: `origin/research/level-i-fused-review-20261009`.
- Frozen source commit: `6132201c1d3056ca68a222217094acb819f5b4d7`.
- Candidate: Section 13 of `docs/reports/target_c_localized_curved_boundary_slow_lattice_deformation_2026-10-09.md`, SHA-256 `2bc5da1876e0b2cd079fe2c533b62c8d884a61d845a90cb652dcfbcf28cf5a48`.
- Verdict: **PASS — promote** `C-ANGULAR-SURPLUS-BOUNDED-SHORE-VARIATION` and the conditional canonical exclusion `C-TYPEII-ACTUAL-RHOMBUS-CHART-EXCLUSION`.
- The result audits only the explicit actual-chart hypotheses in Section 13.1. It does not extract such a chart from a train grid or harmonic cell.

## Exact claims

### Finite angular-surplus lemma

Let

```math
p_{ij}=p_{00}+\sum_{s=1}^{i}u_s+\sum_{t=1}^{j}v_t,
\qquad u_s=(\cos\alpha_s,\sin\alpha_s),\quad
v_t=(\cos\beta_t,\sin\beta_t),
```

on a finite rectangular index domain, with real phase lifts satisfying

```math
\pi/3<\beta_t-\alpha_s\le\pi/2
\quad\hbox{for every }s,t.
```

Let `R` be a set of index pairs. Suppose every shore increment participates in at least `cD` cells of `R`, for a fixed `c>0`, and

```math
E_R:=\sum_{(s,t)\in R}\left(\sin(\beta_t-\alpha_s)-\sqrt3/2\right)\le C_0D
```

for a fixed `C_0`. Put `c_ang=3(2-sqrt(3))/pi`, let `alpha_* = max_s alpha_s`, and choose the unit reference directions `u_0` and `v_0` of angles `alpha_*` and `alpha_*+pi/3`. Then, with

```math
a_i=\sum_{s=1}^i(u_s-u_0),\qquad
b_j=\sum_{t=1}^j(v_t-v_0),
```

the actual chart has total shore variation

```math
\sum_i|a_i-a_{i-1}|+\sum_j|b_j-b_{j-1}|
\le {C_0\over c\,c_{\rm ang}}.
```

The bound is independent of the rectangle dimensions and `D`.

### Conditional Type-II exclusion

There is no unbounded sequence of canonical post-ZF Type-II sources with a nonempty unloaded harmonic cell whose distinct actual loaded attachments all occupy one such actual additive chart, if (i) the phase window above holds, and (ii) every shore increment participates in at least `cD` distinct bounded quadrilateral faces of the canonical positive-contact core for one fixed `c>0`, with each such face represented by its corresponding chart cell. The actual full source, including contact-isolated points, is retained.

## Independent reconstruction

Set

```math
x_s=\alpha_*-\alpha_s\ge0,\qquad
y_t=\beta_t-\alpha_*-\pi/3>0.
```

The phase-window hypothesis implies `x_s+y_t=beta_t-alpha_s-pi/3` lies in `[0,pi/6]`. On this interval, concavity of sine places `sin(pi/3+z)-sqrt(3)/2` above its endpoint chord, whose slope is exactly

```math
c_{\rm ang}={1-\sqrt3/2\over\pi/6}
={3(2-\sqrt3)\over\pi}.
```

Hence each selected face contributes at least `c_ang*(x_s+y_t)`. Summing by increment and using the minimum incidence gives

```math
E_R\ge c_{\rm ang}\left(\sum_s\deg_R(s)x_s+\sum_t\deg_R(t)y_t\right)
\ge c_{\rm ang}cD\left(\sum_sx_s+\sum_ty_t\right).
```

For unit vectors, chord length is at most angular difference. Therefore

```math
\sum_s|u_s-u_0|+\sum_t|v_t-v_0|
\le\sum_sx_s+\sum_ty_t
\le {C_0\over c\,c_{\rm ang}}.
```

This is precisely the bounded total variation required by `C-BOUNDED-VARIATION-LATTICE-ENDPOINT-COUNT`; it is not a Lipschitz bound on individual increments.


## Hostile checks and scope

- The incidence condition counts distinct actual face cells and is imposed on every increment on both shores. Incidence only in an auxiliary selected train grid does not satisfy it.
- The chart positions used for the counted attachments are actual source points; the proof does not identify an abstract scaffold with the source.
- The selected faces are included in the canonical `E_4` ledger only because they are distinct bounded quadrilateral faces of the positive-contact core and each has nonnegative area surplus. No cancellation from unselected or negative-defect cells is assumed.
- All contact-isolated points remain in the full-source packing and stress constraints. The argument deletes no source labels.
- No verifier certifies the angular inequality; it is an exact concavity and incidence calculation. The consequence uses only the canonical `E_4` bound, the canonical linear attachment lower bound, and the independently audited Audit.214 endpoint-count theorem.
- No full-cell chart extraction, finite source move, strict-diameter competitor, C-II closure, or Level-I conclusion follows.

## Canonical disposition

Promote the finite conditional variation lemma and the exact Type-II no-go consequence. This rules out a bounded-variation actual chart only when the stated all-pairs phase window and linear actual-face incidence hold. Those premises are not supplied for the canonical cells by current train-grid or contact-return results; the C-II frontier is unchanged.
