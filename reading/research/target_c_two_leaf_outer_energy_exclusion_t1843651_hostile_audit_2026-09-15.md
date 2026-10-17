> Generated reading edition · [exact source](../../research/target_c_two_leaf_outer_energy_exclusion_t1843651_hostile_audit_2026-09-15.md) · source SHA-256 `c8c3ff901f0db96beafb670696fa5c2c0dbd6d631820a136decdbef0c2075011`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "143e6f64f03060db1e5dc23d5343ad7f039340d4", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_two_leaf_outer_energy_exclusion_t1843651_hostile_audit_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "ec16e671a6ca76465a844425a8afd3ff394291353886e62f24f272a96a4177be"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — repaired two-leaf exclusion through `t=1.843651`

**Date:** 2026-09-15  
**Reviewed:**
- `research/target_c_two_leaf_outer_energy_exclusion_t1843651_2026-09-15.md`
- `research/verify_target_c_two_leaf_outer_energy_exclusion_t1843651.py`
- `research/target_c_two_leaf_strong_branch_scope_repair_2026-09-15.md`
- `research/verify_target_c_two_leaf_strong_branch_scope_repair_184365.py`
- hostile-audited two-leaf/common-center/cross-phase stack through `t=1.84365`

**Disposition:** **PASS at the stated proof-only full-core/no-macroscopic-container Type-II scope.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The candidate raises the rounded full-core Type-II exclusion endpoint from `1.84365` to

```math
\boxed{1.843651}.
```

This continuation is genuinely near the numerical ceiling of the present architecture. The exact certificate has load-bearing margins as small as `6.7e-8`, so the audit treats every scope gate and every adverse rounding as part of the proof rather than relying on floating-point agreement.

---

## 1. Residual stability is invoked only inside its proved range

The `g=.007707` residual theorem requires

```math
U_{net}\le2.013.
```

The candidate first uses the independent `t<=1.844` phase theorem

```math
z_C,z_U,z_V>.616-o(1),
```

so total retained dominant outer mass is above `1.848D`. The established three-well bathtub bound gives

```math
\delta\ge F(1.848)-o(1),
\qquad F(s)=s-6\sin(s/6),
```

and the exact certificate checks `F(1.848)>.029`. Hence at `t<=1.843651`,

```math
U_{net}<1.955085<1.956<2.013.
```

Only after this gate is the residual estimate

```math
R=U_{net}-W\le1.05h
```

used.

**Verdict:** PASS.

---

## 2. The residual cutoff is exact despite the small margin

At

```math
t=1.843651,
\qquad h=.0003828,
\qquad x=0,
```

the direct survivor condition fails by

```math
F(A_H)-\delta_H
=6.7371\ldots\times10^{-8}>0.
```

The certificate derives this sign from rational Machin bounds for `pi`, integer-square-root enclosures, and alternating Taylor bounds for `sin`. It is not a binary-float comparison.

The parent derivative bounds remain

```math
Q_x<-2.7,
\qquad Q_h<-2.5,
\qquad Q_t>0.
```

Therefore larger `h` or `x` cannot restore survival, and smaller `t` is easier. Thus

```math
h<.0003828-o(1)
```

is valid.

**Verdict:** PASS.

---

## 3. The dominant-orbit box rounds in the adverse direction

The cutoff is converted to

```math
W<1.9127155,
\qquad
E_{dom}>.90689964.
```

The verifier checks

```math
C_{707}+.0003828<1.9127155
```

with outward enclosures. For the crossing lower bound it subtracts the entire generic residual allowance

```math
{(1.05H)^2\over4}
```

from the lower enclosure for `Delta_2` before rounding down to `.90689964`.

**Verdict:** PASS.

---

## 4. The retained-mass boundary is feasible and correctly oriented

Assume `z<=Z=2.21936`. The capped retained quantity is increasing in `z`; the verifier proves its derivative exceeds `.96`.

On `delta>=F(Z)`, motion in `x` reaches the active boundary `delta=F(Z)`. At the largest allowed residual cutoff the corresponding boundary value remains positive:

```math
x>5.58\times10^{-7}.
```

Thus the proof is not evaluating an infeasible extrapolation. At the adverse endpoint `t=T,h=H`, the exact capped survivor excess is below

```math
-4.56\times10^{-6}.
```

The `delta<F(Z)` side is controlled by the already-audited negative `Q_x,Q_h` derivatives.

**Verdict:** PASS.

---

## 5. The phasewise promotion has a real exact margin

From `z>2.21936`, suppose one retained phase mass were at most

```math
A=.70202.
```

Strict convexity of

```math
f(s)=s-2\sin(s/2)
```

puts the cheapest other two phases at `(Z-A)/2`. The exact certificate gives

```math
f(A)+2f((Z-A)/2)-\delta_{max}
=1.1093\ldots\times10^{-7}>0.
```

Hence every retained phase mass is above `.70202D` asymptotically. The positive constant margin is sufficient to absorb the source/window `o(1)` terms in the prescribed limit order.

**Verdict:** PASS.

---

## 6. The strong physical-pair branch is non-circularly certified

This is the highest-risk logical point because the parent `1.84364/1.84365` proofs needed an explicit repair.

Before invoking the strong pair theorem, the candidate has already proved

```math
z_V>.70202-o(1).
```

Since one train supplies at most two selected terminal occurrences,

```math
V>.35101-o(1).
```

On the contradiction branch

```math
U\ge U_0=.53052,
```

and with `W<1.9127155`,

```math
C+U=W-V<1.9127155-.35101+o(1).
```

Therefore the actual larger-leaf ratio, before any adverse replacement, satisfies

```math
{(C+U-K)_+\over U}
\le
{1.9127155-.35101-K_-\over.53052}+o(1).
```

The exact certificate gives

```math
0.76718118\ldots
<0.83045479\ldots
=\sqrt{20/29}.
```

The main center interval also has `C<1.0443<K`. For fixed `C<K`, the ratio

```math
L\mapsto{(C+L-K)_+\over L}
```

is nondecreasing, so the smaller leaf `V<=U` is automatically no worse.

Only after these facts establish the strong branch for the original configuration does the proof use the already-audited monotonic adverse replacements

```math
W\mapsto W_0,
\qquad
U\mapsto U_0.
```

There is no reuse of the desired conclusion `U<U_0` to justify its own proof.

**Verdict:** PASS AFTER APPLYING THE EXISTING SCOPE REPAIR.

---

## 7. Positive-part handling and the one-variable capacity are valid

At the reduced point the verifier explicitly checks

```math
C_{low}+U_0-K_+>0,
\qquad
W_0-U_0-K_+>0.
```

Thus both physical pair deficits in the reduced one-variable capacity are genuinely on their positive branches; squaring them does not replace a vanishing positive part by an artificial positive penalty.

Generic center capacity excludes both center tails. On the remaining compact interval the symbolic curvature bound gives

```math
G''<-2.
```

At `c_0=.9314032`, the tangent estimate yields

```math
E_{dom}-\max G
=1.2908\ldots\times10^{-7}>0.
```

Again this is exact outward arithmetic.

**Verdict:** PASS.

---

## 8. The bad-center pair budget is global, not duplicated

The leaf mass and retained-occurrence bounds give

```math
P_U,P_V>.1715-o(1).
```

The missing center/leaf correlation bounds the total bad retained pair weight across both leaves. With the candidate constants, the quadratic certificate for

```math
B_{bad}<.03666
```

has discriminant

```math
-1.7643959\times10^{-5}<0.
```

Therefore each individual bad weight is at most the same total `.03666` budget, and each leaf retains

```math
G_U,G_V>.13484-o(1).
```

The proof deliberately subtracts the whole total bad allowance from each leaf; it does not invent two separate bad budgets.

**Verdict:** PASS.

---

## 9. The endpoint-energy constant is enclosed in the correct direction

Every good cross-leaf pair shares a center neighbor and is noncrossing by triangle-freeness. The hostile-audited endpoint theorem therefore supplies

```math
e_\tau+e_\sigma\ge2-\sqrt3-o(1).
```

At this endpoint the older convenient estimate `sqrt(3)<1.7321` loses more than the remaining proof margin. The candidate instead reuses the verifier's existing 100-digit integer-square-root enclosure

```math
\sqrt3< (\sqrt3)_+.
```

Hence

```math
2-(\sqrt3)_+
<2-\sqrt3
```

is a valid lower bound on the endpoint-energy constant. This is a precision improvement only; no mathematical inequality is strengthened beyond the exact constant already proved.

**Verdict:** PASS.

---

## 10. The final energy ledger has no double counting

The two-leaf weighted product gives

```math
E_U+E_V
>(2-\sqrt3)(.13484)-o(1).
```

The center one-well energy is carried by selected outer occurrences in the disjoint center phase window. The leaf payment uses selected terminal occurrences in the two disjoint leaf phase windows. These supports were already checked as physically disjoint in the parent hostile audit, so the payments add.

The exact verifier obtains

```text
leaf energy lower          0.0361302691074...
center energy lower        0.0143272023217...
total required             0.0504574714291...
detour budget upper        0.0504557895462...
final contradiction        1.6818829e-6
```

**Verdict:** PASS.

---

## 11. Independent live recheck

Running the committed verifier from the live Pyroam clone gives

```text
PASS: no full-core Type-II survivor with t<=1.843651
residual-scope U upper          1.9550845182969783
h localization margin          6.73718718085424e-08
z cap excess upper            -4.56955114863074e-06
phase imbalance margin         1.1093276438073699e-07
non-circular strong ratio      0.7671811837833606
strong threshold lower         0.8304547985373997
leaf capacity margin           1.290864355121894e-07
bad quadratic discriminant    -1.7643959e-05
final contradiction margin     1.6818829446151618e-06
```

The separate scope-repair verifier also passes independently.

**Verdict:** PASS.

---

## 12. Frontier

This certificate is essentially a terminal decimal refinement of the present two-leaf scalar architecture. A corrected continuous solve puts the relaxed zero near `1.84365114`; this number is exploratory and not used in the proof. The same architecture should not be advertised at `1.843652`.

Further C-II progress should come from a stronger structural inequality, not another unchecked decimal continuation. The live repository already contains adjacent-cut finite-cusp/triple-small reductions and multishear work that are better candidates for the next closing step.

**Final verdict:** **PASS** for the proof-only full-core Type-II statement

```math
\boxed{\liminf (q-k)/D\ge1.843651}
```

at the stated scope. C-II and Level I remain open.
