> Generated reading edition · [exact source](../../research/target_c_two_leaf_strong_branch_scope_repair_2026-09-15.md) · source SHA-256 `ac33d794287234e760a47ec40fe22ba487bf1e6d3cd4ca74681d0188b89fcd04`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "bc52b6253aae8a6b2ca4a588c1bd9e0580603b8c", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_two_leaf_strong_branch_scope_repair_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "ec95ff3e3c536297e3b0bc02c1711847ab5b17e11e12000040e0761decd0bd71"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — scope repair for the two-leaf strong center/leaf branch

**Date:** 2026-09-15  
**Status:** hostile proof repair / dependency correction  
**Reviewed:** `t<=1.84364` and `t<=1.84365` two-leaf outer-energy exclusions and their hostile audits  
**Certificate:** `research/verify_target_c_two_leaf_strong_branch_scope_repair_184365.py`  
**Disposition:** **PASS AFTER REPAIR** at the stated proof-only full-core/no-macroscopic-container Type-II scope  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The hostile-audited two-leaf exclusions through `1.84364` and `1.84365` use the strong physical center/leaf pair estimate

```math
\rho\ge{(a+b-K)_+^2\over10},
\qquad
K={2\over\sqrt3},
```

which is valid when

```math
{(a+b-K)_+\over\min(a,b)}
\le r_{crit}:=\sqrt{20/29}.
\tag{SR.1}
```

Their written branch check replaces the larger leaf mass `U` by the contradiction threshold `U_0` and then checks

```math
{C_{max}+U_0-K\over U_0}<r_{crit}.
```

That is not a valid upper bound for the original configuration.  In the relevant interval `C<K`, the function

```math
L\longmapsto{(C+L-K)_+\over L}
=\left(1+{C-K\over L}\right)_+
```

is nondecreasing in `L`.  Thus an actual larger leaf `U>U_0` can have a larger ratio than the displayed substituted value.

This is a genuine proof-scope gap in the written argument and in the corresponding hostile-audit sentence.  It does **not** invalidate either theorem.  The same phasewise localization already proved earlier in each theorem supplies a stronger independent bound that closes the gap with substantial room.

---

## 1. Correct branch bound at `t<=1.84365`

The `1.84365` theorem proves before invoking the physical pair branch that

```math
z_C,z_U,z_V>0.702-o(1).
\tag{SR.2}
```

For one leaf phase, every complete stopped train has at most two selected outer terminal occurrences, each of weight at most one.  Therefore

```math
z_V\le2V+o(1),
```

so

```math
\boxed{V>0.351-o(1).}
\tag{SR.3}
```

The dominant orbit also satisfies

```math
W=C+U+V<1.912711+o(1).
\tag{SR.4}
```

Now assume the contradiction branch

```math
U\ge U_0:=0.5304.
\tag{SR.5}
```

For the larger center/leaf pair `(C,U)`, put

```math
e_U=(C+U-K)_+.
```

Equations (SR.3)--(SR.4) give

```math
C+U=W-V
<1.912711-0.351+o(1),
```

hence, using `K>=K_-` and `U>=U_0`,

```math
{e_U\over U}
\le
{1.912711-0.351-K_-\over0.5304}+o(1).
\tag{SR.6}
```

The exact companion verifier proves

```math
\boxed{
{1.912711-0.351-K_-\over0.5304}
<0.76737
<\sqrt{20/29}.
}
\tag{SR.7}
```

This is the required non-circular strong-branch certificate.

For the smaller leaf `V`, the same conclusion follows automatically on the main center interval.  There

```math
C<1.0443<K.
```

For fixed `C<K`, the ratio

```math
L\mapsto {(C+L-K)_+\over L}
```

is nondecreasing.  Since `V<=U`,

```math
{(C+V-K)_+\over V}
\le
{(C+U-K)_+\over U}
<r_{crit}.
\tag{SR.8}
```

Thus both physical center/leaf pairs are genuinely inside the `1/10` branch **before** the proof makes the adverse replacement `U -> U_0`.

Once branch validity is established for the original configuration, the already-audited capacity monotonicity applies:

- capacity increases with total orbit mass `W`;
- at fixed `C,W`, capacity decreases as the larger leaf `U` increases while `U>=V`.

Therefore replacing

```math
W\mapsto W_0,
\qquad
U\mapsto U_0
```

is adverse exactly as used in the one-variable capacity certificate.  There is no circular use of the desired conclusion `U<U_0`.

---

## 2. The same repair covers the `1.84364` parent

The hostile-audited `1.84364` theorem proves

```math
z_C,z_U,z_V>0.7045-o(1),
```

hence

```math
V>0.35225-o(1).
```

Its orbit and contradiction thresholds are

```math
W<1.912658+o(1),
\qquad
U\ge0.528.
```

Therefore

```math
{(C+U-K)_+\over U}
\le
{1.912658-0.35225-K_-\over0.528}+o(1).
```

The exact repair verifier proves

```math
\boxed{
{1.912658-0.35225-K_-\over0.528}
<0.7684
<\sqrt{20/29}.
}
\tag{SR.9}
```

Again the smaller leaf ratio is no larger because the main interval has `C<K` and `V<=U`.

Thus the `1.84364` theorem and its downstream uses remain valid after this substitution.

---

## 3. What is superseded

The following reasoning should no longer be used:

```text
U >= U0
and C <= Cmax
therefore
(C+U-K)/U <= (Cmax+U0-K)/U0.
```

The implication is false when `C<K`, because the ratio can increase with `U`.

The correct reusable pattern is

```text
phasewise retained outer mass z_V > A
    -> V > A/2
orbit mass W <= Wbar
    -> C+U = W-V <= Wbar-A/2
contradiction branch U >= U0
    -> (C+U-K)_+/U <= (Wbar-A/2-K)_+/U0.
```

This argument is stronger numerically and uses only quantities proved independently before the physical pair theorem is invoked.

---

## 4. Final disposition

The written strong-branch checks in the `1.84364` and `1.84365` proof notes and hostile audits are incomplete as stated.  Replacing them by (SR.6)--(SR.9) closes the gap.

All downstream capacity inequalities, retained-pair arguments, and final outer-energy contradictions are unchanged.  In particular the current proof-only full-core Type-II floor

```math
\boxed{\liminf (q-k)/D\ge1.84365}
```

remains valid at its stated scope.

C-II and Level I remain open.
