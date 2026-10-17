> Generated reading edition · [exact source](../../research/target_c_g0076_residual_stability_floor_1843555_hostile_audit_2026-09-15.md) · source SHA-256 `f1d9a03b7d678965e706f09f12e6d4b10a534624bf581d93d0683733c4c728b8`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 1 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "48008d1936ee5d813760fcbb7544dcf3d4db2688", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_g0076_residual_stability_floor_1843555_hostile_audit_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "ef279d6d9d5bbff92d0702ac44d4ca3106fbd229f0918df7af30471473c91c63"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — `g=0.0076` residual-coupled floor `1.843555`

**Date:** 2026-09-15  
**Reviewed:**
- `research/target_c_g0076_endpoint_residual_stability_2026-09-15.md`
- `research/target_c_g0076_residual_stability_floor_1843555_2026-09-15.md`
- `research/verify_target_c_g0076_residual_stability_floor_1843555.py`
- hostile-audited corrected `g=0.0076` physical one-orbit capacity theorem

**Disposition:** **PASS at stated proof-only full-core Type-II scope.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The candidate raises the current safe full-core low-`t` floor to

```math
\boxed{t=(q-k)/D\ge1.843555-o(1)}.
```

The gain comes from correlating three quantities that earlier proofs treated independently:

1. slack `h=U-C76` above the matched atomic endpoint;
2. exact atomic mass outside the dominant orbit; and
3. complement complete-train/rhombus incidence capacity.

The audit focuses on whether `U-M` legitimately controls both complement currencies, whether the physical pair theorem is used outside its family-size scope, and whether the feasible-triangle collapse combines incompatible extrema.

---

## 1. Endpoint residual theorem uses only scope-corrected capacity branches

The residual theorem imports the already-audited full physical one-orbit capacity `Psi` from the corrected `g=0.0076` proof.  That proof has three explicit center regimes:

- strong `1/10` physical pair branch while the center/leaf families are below `K=2/sqrt(3)`;
- universal `2/29` pair branch only up to `C=K`;
- generic triangle-free `C(W-C)` capacity for `C>K`.

The present residual theorem does not extend either pair bound beyond `K`.

On `U<=2.013`, the generic two-bin theorem gives dominant mass `M>1.9013`.  Over `1.9013<=W<=C76`, the three capacity branches each increase with derivative greater than `0.60`; the exact certificate gives lower bounds `0.6058`, `0.8461`, and `>1.15` respectively.  Therefore the maximum physical capacity also satisfies

```math
\Psi(C_{76})-\Psi(W)\ge0.60(C_{76}-W).
```

Together with the hostile-audited strict endpoint inequality `Psi(C76)<Delta2`, this yields the residual estimate without a hidden use of an invalid pair regime.

**Verdict:** PASS.

---

## 2. `U-M` safely dominates the actual residual exact-orbit mass

Let `A` be total exact atomic train mass and

```math
C=(T-q/2)/D.
```

The exposed-hull chain gives

```math
M\le A\le C\le U.
```

Thus actual exact atomic mass outside the dominant orbit obeys

```math
A-M\le U-M=:R.
```

The exact crossing decomposition consequently gives

```math
\Delta_2
\le\Psi(M)+{(A-M)^2\over4}
\le\Psi(M)+{R^2\over4}.
```

No equality between `A`, `C`, and `U` is assumed away from the endpoint.

**Verdict:** PASS.

---

## 3. The coefficient `1.05` is outward-safe on the complete target range

At `U=2.013`, the exact two-bin certificate gives

```math
R<0.11165<0.112.
```

If `M>=C76`, then `R<=h:=U-C76` immediately.  If `M<C76`, the capacity slope and crossing decomposition give

```math
0.60(R-h)<{R^2\over4},
```

hence

```math
R-h<{R^2\over2.4}
<{0.112\over2.4}R.
```

Therefore

```math
R<1.04896h<1.05h.
```

The proof intentionally rounds the factor upward.  There is no numerical root-finding in this step.

**Verdict:** PASS.

---

## 4. `R` controls both complement currencies

### Complete-train count

The total complete-train density is

```math
T/D=C+(t+\kappa)/2.
```

After removing the dominant orbit mass `M`, the complement density satisfies

```math
N_c
\le C+(t+\kappa)/2-M
\le(t+\kappa)/2+U-M.
```

Thus `R<=1.05h` gives exactly the claimed complement count ceiling.  This includes diffuse/non-atomic train mass because `C`, not merely `A`, appears before the `C<=U` relaxation.

### Rhombus incidence

The complement-rhombus incidence theorem charges the strict-rhombus crossing mass outside the dominant exact orbit.  That crossing mass is bounded by the square capacity of the actual residual exact atomic mass, hence by `R^2/4`; the audited incidence normalization produces the displayed allowance `R^2/2`.  Replacing `R` by `1.05h` is therefore safe.

At `h=0`, the chain

```math
M\le A\le C\le U=M
```

forces equality throughout.  There is no hidden non-atomic complement mass surviving at the collapsed corner.

**Verdict:** PASS.

---

## 5. Shared retention and energy do not double count

The shared-retention theorem gives

```math
z+p\ge\pi-t/2-x-1.05h-o(1),
\qquad x=\kappa/2.
```

The complement incidence theorem gives

```math
p(1-\delta)-e_c/2\le(1.05h)^2/2+o(1).
```

Dominant selected occurrences and complement selected terminal occurrences belong to disjoint train classes, so their physical outer-edge directional-energy sums are disjoint.  Therefore

```math
e_c\le\delta-F(z)+o(1)
```

is an allocation of the same total outer energy, not a second use of `delta`.

The resulting complement ceiling

```math
p\le{\delta-F(z)+(1.05h)^2\over2(1-\delta)}+o(1)
```

is therefore legitimate.

**Verdict:** PASS.

---

## 6. Maximizing over `z` is valid

Every survivor has `F(z)<=delta+o(1)`.  On the target range the exact certificate gives `delta<0.051`, while

```math
F(\pi)=\pi-3>0.14.
```

Thus the relevant inverse

```math
Z(\delta)=F^{-1}(\delta)
```

lies strictly in `(0,pi)` whenever `delta>0`.

For fixed `t,h,x`, define

```math
L(z)=z+{\delta-F(z)+c^2h^2\over2(1-\delta)}.
```

Since `F'(z)<0.134` and `delta<0.051`,

```math
L'(z)>0.
```

Hence the largest survivor capacity compatible with the energy constraint occurs at `z=Z(delta)`, where `F(z)=delta`.  No incompatible lower bound on `z` is inserted.

**Verdict:** PASS.

---

## 7. Feasible-triangle extrema are simultaneous

Write

```math
2\delta+x+h=R_t.
```

The necessary survivor capacity is

```math
Q(t,h,x)=Z(\delta)
+{c^2h^2\over2(1-\delta)}
-\left(\pi-t/2-x-ch\right).
```

The exact certificate covers the whole triangle for `t<=1.843555`:

```math
U<2.013,
\qquad
\delta<0.051,
\qquad
h<0.101.
```

At fixed `h,x`, `Q` increases with `t`.

At fixed `t,h`, the exact rational derivative bound is

```math
Q_x<-2.73<0.
```

At fixed `t,x`,

```math
Q_h<-2.56<0.
```

Thus the largest survivor capacity over the **same** feasible region occurs simultaneously at

```math
t=1.843555,
\qquad x=0,
\qquad h=0.
```

No independent extrema of `delta`, `U`, and `kappa` are combined.

**Verdict:** PASS.

---

## 8. Exact corner certificate

At `x=h=0`, complement residual allowance vanishes and feasibility reduces exactly to

```math
\delta_0(t)
\ge F(\pi-t/2),
```

where

```math
\delta_0(t)=\frac12\left(\frac92t-2\pi-C_{76}\right).
```

The committed exact verifier uses only `Fraction` arithmetic for asserted signs, Machin bounds for `pi`, integer-square-root enclosures, and alternating Taylor bounds for `sin`.  At `t=1.843555` it gives

```math
F(\pi-t/2)-\delta_0(t)
>1.5\times10^{-6}.
```

An independent Pyroam execution reproduced a lower margin of approximately

```math
1.61064636\times10^{-6}.
```

The non-load-bearing numerical crossing `1.8435557052...` is consistent with this safe rounded claim.

**Verdict:** PASS.

---

## Final disposition

The candidate validly proves, at proof-only full-core Type-II scope,

```math
\boxed{
\liminf(q-k)/D\ge1.843555.
}
```

The structural endpoint is the more important conclusion: at the weakest corner, all allowed exact atomic train mass lies in one exact three-phase orbit, topology slack vanishes, and there is no independent residual-rhombus budget.

This does not close C-II.  The next obstruction is internal to the dominant orbit: cyclic order of its outer-to-outer trains, near-saturated center/leaf crossing incidence, and Section-157 two-sided diameter bracing.

**Final verdict:** PASS. C-II and Level I remain open.
