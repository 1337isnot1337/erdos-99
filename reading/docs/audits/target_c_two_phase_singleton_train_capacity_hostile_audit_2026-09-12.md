> Generated reading edition · [exact source](../../../docs/audits/target_c_two_phase_singleton_train_capacity_hostile_audit_2026-09-12.md) · source SHA-256 `d1447a71efd9e97445faa1586fbb7394743e050b722e5643885a5df75a99bea9`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-BEDCF932EE1F","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Hostile audit — Target C two-phase singleton-train capacity

**Date:** 2026-09-12  
**Reviewed:** `research/target_c_two_phase_singleton_train_capacity_2026-09-12.md`  
**Base state:** `2026-09-12.audit.46`  
**Disposition:** **PASS at the stated conditional scope.**  
**LEVEL I STATUS:** STILL OPEN. C-II REMAINS OPEN.

## 1. Train-occurrence capacity

The report counts physical outer-face edge occurrences, not boundary vertices. Under
the canonical stopped-train convention, every non-singleton train has at most two
terminal outer occurrences, and a singleton bridge contributes its two face-side
occurrences to the same train. An outer occurrence whose projective direction is
outside the selected pair therefore belongs to an off-phase train. This proves

```math
N_o\le2T_o.
```

No injectivity between different outer occurrences is assumed; the inequality is
deliberately a multiplicity bound. The audit retains bridges and articulation
repetitions.

**Verdict:** valid.

## 2. Two-phase crossing capacity

Under the explicit hypothesis that all but `o(D^2)` strict-rhombus faces use the two
selected projective directions, each selected rhombus is a crossing of one `u` train
and one `v` train. The stopped-train crossing graph is simple, so there is at most one
rhombus per ordered train pair. Thus

```math
R_{uv}\le T_uT_v
\le \frac{(T-T_o)^2}{4}.
```

Combining `T_o\ge N_o/2` gives

```math
T\ge2\sqrt{R_{uv}}+\frac{N_o}{2}.
```

The inequality is safe if some phase-aligned singleton trains do not participate in a
quadrilateral: retaining them in `T_u+T_v` only weakens the upper bound. The argument
does not infer phase concentration from train-direction measures; it states that
concentration as a hypothesis on the rhombus faces.

**Verdict:** valid at the stated finite scope.

## 3. Projection variation and slack algebra

The two determinant-variation inequalities are the audited finite walk statement:

```math
sN_u+N_o\ge2\operatorname{width}_{Jv}(P),\qquad
sN_v+N_o\ge2\operatorname{width}_{Ju}(P).
```

With both widths `D-o(D)` and `b=N_u+N_v+N_o\le xD+o(D)`, adding gives

```math
\frac{N_o}{D}\ge\frac{4-sx}{2-s}-o(1).
```

The train ledger `2T=b+Q+4f` then yields

```math
\frac{Q+4f}{D}
\ge4\sqrt{\Delta_2}+\frac{4-2x}{2-s}-o(1).
```

For `x\ge\pi` the numerator `4-2x` is negative, so the lower bound is minimized at
`s=1`, giving `4\sqrt{\Delta_2}+4-2x-o(1)`. At `x=\pi` this is
`1.5260659202...`; the loss under `x=\pi+\delta` is exactly `2\delta`.

The monotonicity and the displayed constants are correct. The certificate checks the
rational enclosures and a surviving scalar witness.

**Verdict:** valid.

## 4. Exact scope and remaining gap

The result is conditional on all of the following being supplied by the same source
sequence:

1. two selected train directions whose rhombus population satisfies
   `R_uv/D^2 -> pi/(2sqrt(3))`;
2. the two near-disk width estimates;
3. the near-geodesic bound on the actual occurrence-counted outer walk; and
4. the canonical stopped-train ledger.

The proof does not identify `N_o` with exceptional-face perimeter, does not bound
`e_BB-k` from above, and does not construct a source-preserving diameter decrease.
The scalar witness in the source confirms that the linear payment is compatible with
the current normalized region. The Type-I branch is untouched.

Contact-isolated source points remain outside the core train ledger and are not
deleted. No full-source affine-kernel claim is used.

**Final verdict:** the slack-aware two-phase singleton-train capacity inequality is
an audited-working proof-only conditional theorem. It is a useful coupling to the
live aggregate detour currency, but it does not close C-II or change canonical state.
