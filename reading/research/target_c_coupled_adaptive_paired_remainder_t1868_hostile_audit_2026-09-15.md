> Generated reading edition · [exact source](../../research/target_c_coupled_adaptive_paired_remainder_t1868_hostile_audit_2026-09-15.md) · source SHA-256 `22cd958515aa93c68e94e3aa121583c23a62b7ac2321cedfcdd7546569f218cc`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "1688779a8d8d372d6ed6209ff1e8577d50c46e73", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_coupled_adaptive_paired_remainder_t1868_hostile_audit_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "df4cffeddda0edc14a4674f0e95ff8f45a84698744b27f92decd8fba1158fc56"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — coupled adaptive paired-remainder O–O path through `t<=1.868`

**Date:** 2026-09-15  
**Audited source:** `research/target_c_coupled_adaptive_paired_remainder_t1868_2026-09-15.md`  
**Certificates:** `research/verify_target_c_coupled_adaptive_paired_remainder_t1868.py`, `research/verify_target_c_coupled_adaptive_paired_remainder_t1868_threshold.py`  
**Verdict:** **PASS at proof-only scope.**  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

## 1. No scope enlargement is hidden in the new coupling

The proof uses only ingredients already valid on the canonical full-core/no-macroscopic-container Type-II branch:

1. the hostile-audited scope-safe matched all-train floor `C707`;
2. the corrected joint-retention/complement-incidence feasibility inequalities;
3. the hostile-audited paired-remainder energy inequality;
4. the physical opposite-terminal-branch theorem;
5. phase-free path-region saturation and diameter-interval Helly routing.

The theorem changes only how the already-valid scalar inequalities are combined.  It does not extend any dependency to a new branch.

**Disposition:** PASS.

## 2. Endpoint relaxation has the correct direction

For an actual source write

```math
U={9t\over2}-2\pi-2\delta-\kappa/2,
\qquad \kappa\ge0.
```

The corrected parent theorem already proves that, for fixed retained mass and detour, the weakest shared-retention/complement feasibility inequality over `t<=T` is obtained at `t=T` and `kappa=0`.  The present `G(delta,z)` is exactly that endpoint relaxation.

For the paired-remainder lower bound, after replacing pair weight by its endpoint-count floor,

```math
P_0=z-U_0(t)+2\delta+\kappa/2,
\qquad
s_0=2U_0(t)-z-4\delta-\kappa.
```

On the certified box, `F'(s_0)<0.058` and the strict adaptive threshold exceeds `0.4836`.  Therefore

```math
{\partial L\over\partial U_0}
=-1+{2F'(s_0)\over\lambda}<0,
```

while

```math
{\partial L\over\partial\kappa}
={1\over2}-{F'(s_0)\over\lambda}>0.
```

Thus the adverse choices are again `t=T` and `kappa=0`.  No favorable endpoint has been substituted.

**Disposition:** PASS.

## 3. The affine retained-mass floor is a direct differential barrier

The certificate proves on five rational detour intervals covering

```math
0.0398\le\delta<0.106
```

that

```math
G_\delta<-1.3.
```

It also gives `0<G_z<1`.  Hence along

```math
z_{line}(\delta)=2.0527+1.3(\delta-0.0398)
```

we have

```math
{d\over d\delta}G(\delta,z_{line}(\delta))
=G_\delta+1.3G_z<0.
```

The separately certified anchor is

```math
G(0.0398,2.0527)<-4.9\times10^{-5}.
```

Therefore `G` is strictly negative on the whole affine line.  Since feasibility requires `G>=-o(1)` and `G` is increasing in `z`, every survivor lies above that line up to `o(1)`.

This argument does not assume differentiability of an implicitly selected numerical root.  The five-bin derivative certificate is enough.

The interval bounds used for `r(U)` and `r'(U)` have the correct orientation: `r` and `r'` increase with `U` on the present branch, while `U=U_0-2delta` decreases with detour.  The verifier uses the left endpoint for the required upper `r` bound and the right endpoint for lower `r,r'` bounds, with outward square-root enclosures.

**Disposition:** PASS.

## 4. Pair/remainder energy is not double counted

The new theorem inherits the exact paired-remainder decomposition.  For each retained train, subtract the pair weight `w=min(a,b)` from both terminal occurrence weights.  The pair and remainder occurrence weights partition the original retained measure pointwise.  Therefore

```math
E_{pair}+E_{res}=E_{dom},
```

and the residual measure remains dominated by the hull-perimeter measure.  Applying the three-well bathtub theorem only to that residual gives

```math
E_{pair}+F(z-2P)\le\delta+o(1).
```

No outer-energy unit is charged to both terms.

**Disposition:** PASS.

## 5. Substituting the pair-weight floor is monotone

For fixed `z,delta`, define

```math
\Phi(P)=P-{\delta-F(z-2P)\over\lambda}.
```

Then

```math
\Phi'(P)=1-{2F'(z-2P)\over\lambda}.
```

The certified bounds `F'<0.058` and `lambda>0.4836` make this strictly positive.  Therefore replacing `P` by its lower bound

```math
P\ge z-U
```

weakens the conclusion and is safe.

After that substitution, the functional is also increasing in `z` because

```math
1-{F'(s_0)\over\lambda}>0.
```

Thus replacing `z` by the affine lower barrier is again adverse, not favorable.

**Disposition:** PASS.

## 6. The adaptive threshold is strict and uniform

The equality threshold

```math
\lambda_*(\delta)
=2-\delta-\sqrt{2-\delta^2}
```

is the lower root of the exact same-oriented branch equality.  The theorem does **not** select at equality.  It uses

```math
\lambda(\delta)=\lambda_*(\delta)-10^{-4}.
```

The side certificate proves

```math
0.4836<\lambda(\delta)<0.547
```

throughout the detour interval and `lambda(0.0398)>0.5464`.  Hence every train selected by terminal energy `<lambda(delta)` has a strict physical contradiction in the same-oriented branch.

The uniform upper bound `0.547` is also below the adaptive-path parent's certified separation range, so the two opposite physical terminal arcs retain a fixed positive gap.  No limiting equality case is used to build the path.

**Disposition:** PASS.

## 7. The low-energy functional really increases with detour after coupling

Along the affine feasibility barrier the theorem has

```math
P'=3.3,
\qquad
s_0'=-5.3.
```

Writing

```math
A=\delta-F(s_0),
```

we have `A<=delta`, and the adaptive threshold satisfies

```math
-1<\lambda'(\delta)<0.
```

Therefore

```math
L'
=3.3-{1+5.3F'(s_0)\over\lambda}
+{A\lambda'\over\lambda^2}
```

has the rigorous lower bound

```math
L'
\ge3.3-{1+5.3(0.058)\over0.483}
-{0.106\over0.483^2}
>0.138.
```

If `A<0`, the last term is positive and the displayed lower bound only becomes safer.  Thus the minimum is indeed the lower-detour boundary, not an interior numerical minimizer.

**Disposition:** PASS.

## 8. Boundary arithmetic and topology

At `delta=0.0398,z=2.0527` the exact certificate gives

```math
P_0>0.0094853,
\quad
s_0>2.033729,
\quad
F(s_0)>0.0387195,
```

and finally

```math
P_{low}>0.0075065D-o(D)>0.007D-o(D).
```

Pigeonholing among the at most three dominant phase windows gives more than `0.0023D-o(D)` actual selected O–O trains in one window.  Pair weight per train is at most one, so this conversion does not inflate the train count.

The inherited pseudosegment/path theorems then apply: same-window selected trains are noncrossing, their opposite physical terminal arcs are separated, every dual-path region is diameter-loaded, all diameter intervals share one hub, and nonhub switching is one-sided.  Averaging

```math
\sum_iN_i\le2\pi D+o(D)
```

over more than `0.0023D-o(D)` internal boundaries gives an average below `2732`, hence some integer switching count satisfies

```math
N_i\le2731.
```

The exact local KKT reduction to one or two switching bars is an inherited theorem and does not depend on the older `1.8623` density.

**Disposition:** PASS.

## 9. Scope of the gain

A floating solve of the same coupled system gives a zero-low-energy endpoint near `1.868775`.  That number is diagnostic only.  The theorem claims the exact certified round endpoint `1.868` and no more.

This still does not close C-II: it supplies a denser finite-strip obstruction over a wider high-`t` interval.  A closing theorem must now exploit the finite one/two-bar reaction, the finite-defect strip structure, or another global incompatibility.

**Final verdict:** PASS at proof-only scope.  The coupled adaptive paired-remainder normal form is valid through `t<=1.868`.
