<!-- theorem-state: {"artifact_id":"ART-0E9ABD5CB6AB","canonical":true,"claim_ids":["C-COMMON-ANGLE-ALGEBRAIC-FULL-SOURCE-PAIR-TEST"],"claim_statuses":{"C-COMMON-ANGLE-ALGEBRAIC-FULL-SOURCE-PAIR-TEST":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit: common-angle full-source pair test

Date: 2026-10-07. Audit base: `origin/main=f45467a9c814d08f130fe3f5e211bcbebf97c0a7`, state `2026-10-07.audit.115`; Target C C-II remains open.

Frozen source: Worker 1 branch `research/sol/target-c-owner-order-closure-20261006` at `bf288c82e8a62466d5580025c94e750a177e63e2`. Source report `docs/reports/target_c_common_angle_train_closure_and_full_endpoint_2026-10-06.md`, SHA-256 `176b0eae82355d398d6674ce0e047446e443feb6ea11d31e4f1e9f9d45df9233`. Exact finite verifier `research/verify_target_c_common_angle_train_endpoint_2026_10_06.py`, SHA-256 `a5feeb67ff9b97123c016f5cccf9d839928c8cfb41f0ac55951de42a4efab14b`.

## Verdict

**PASS — promote the exact full-source pair test and algebraic one-parameter decision criterion.** The train closure/integration is already covered by `C-FACE-COUPLED-QUARTER-FOLD-INTEGRATION` (Audit.83), and the active-diameter amplitude obstruction is already covered by `C-COMMON-ANGLE-ACTIVE-DIAMETER-AMPLITUDE-GAP` (Audit.97). The new theorem is only the explicit pairwise quadratic test, including contact isolates, and the exact decision procedure for algebraic input. It asserts no favorable parameter or nonconstant pattern.

The endpoint chain is:

```text
closed complete-train bit pattern -> exact full-source pair quadratics
                                  -> feasible parameter plus one strict old-D row
                                  -> smaller diameter or fewer actual diameter pairs
                                  -> contradiction to canonical lexicographic minimality
```

## 1. Exact statement

Let a finite source have diameter `D>1`. Let `V` be a connected component of its unit-contact graph, with a plane embedding and contacts partitioned into complete stopped trains. Fix one bit `x_tau` for each train, and suppose the selected-edge field is closed on every bounded face, so a potential `y` exists with

```text
y_j-y_i = x_tau (p_j-p_i)
```

on every oriented core contact `ij`. Fix one additive normalization of `y`; the test below is for that specified choice. Hold every source label outside `V` fixed by setting its displacement potential to zero; this includes contact isolates and may include other contact components. Since `V` is a contact component, no unit contact crosses between `V` and its complement. For angle `theta`, define `p'_i=p_i+(Rot(theta)-I)y_i` on all labels. This preserves every old contact exactly.

For any labelled source pair, including pairs involving isolates, put

```text
r = p_i-p_j,  s = y_i-y_j,
A = (r-s) dot s,  B = r dot J(s),  t = tan(theta/2).
```
For finite real `t`, its exact squared-distance change is

```text
|p'_i-p'_j|^2 - |p_i-p_j|^2 = 4t(B-tA)/(1+t^2).
```

Writing `ell=|r|^2-1>0` for an old noncontact's lower slack and `u=D^2-|r|^2>0` for an old nondiameter's upper slack, the full-source endpoint checks are exactly:

```text
old noncontact:       ell(1+t^2)+4tB-4t^2A > 0
old nondiameter:      u(1+t^2)-4tB+4t^2A > 0
old actual diameter:  t(B-tA) <= 0.
```

The diameter inequality must be strict for at least one old actual diameter pair. Every old contact is preserved exactly and needs no additional inequality. These checks range over all original pairs, not only pairs in `V`.

For the omitted angle `theta=pi` (equivalently, `Rot(theta)=-I`), the squared-distance change is `-4A`. The checks become `ell-4A>0` for old noncontacts, `u+4A>0` for old nondiameters, and `A>=0` for old actual diameters, with `A>0` for at least one old actual diameter.

For algebraic source coordinates, the finite-`t` conditions form a finite system of strict and weak univariate polynomial sign constraints with algebraic coefficients. Isolating all real roots partitions the line into finitely many intervals on which every sign is constant; testing each interval and each root decides whether a permitted finite `t` exists. The `theta=pi` endpoint is checked separately. This is a decision procedure for the specified move and source, not a uniform bound over sources.

If the source is the canonical contact-minimal, then actual-diameter-pair-minimal triangle-free global-minimizer representative and these complete checks pass, then the contact graph remains unchanged, every old diameter remains at most `D`, every old nondiameter remains strictly below `D`, and one old diameter shortens. If the new maximum is below `D`, this contradicts global minimality. If it remains `D`, no new diameter pair has appeared and an old one has disappeared, contradicting the secondary minimum.

## 2. Independent derivation

Since `Rot(theta)-I = 2(tJ-t^2I)/(1+t^2)`,

```text
p'_i-p'_j = (r-s)+Rot(theta)s.
```

Expanding the squared norm and subtracting `|r|^2` gives

```text
2(r-s) dot (Rot(theta)-I)s
  = 4t(r dot J(s))/(1+t^2) - 4t^2((r-s) dot s)/(1+t^2),
```

which is the claimed identity. Multiplying each strict lower or upper condition by the positive factor `1+t^2` gives the displayed quadratics. For an old diameter, requiring the change to be nonpositive gives `t(B-tA)<=0`; one strict row is necessary for either a strict decrease of the maximum or a reduction in its attaining pair set.

On a core contact, `s` is either `r` or zero, so `A=B=0`; the contact length is unchanged. Every other pair, including each isolate-to-core pair and isolate-to-isolate pair, is explicitly included in the same formula. Thus no core-only upper or lower conclusion is used.

The common-angle contact motion itself is a reparameterized quarter-fold: set `s_tau=2x_tau-1` and `phi=theta/2`. A global rotation by `-phi` sends each selected contact vector to `Rot(phi)q` and each unselected contact vector to `Rot(-phi)q`, which is `cos(phi)q+sin(phi)s_tau J(q)`. This confirms that the closure and contact integration are subsumed by Audit.83. The isolate labels can be carried through this rigid rotation when comparing pair distances; the source endpoint test still checks every isolate pair. The stress-derived amplitude threshold is Audit.97 and is not reproved here.

## 3. Hostile scope checks

- Equality in a noncontact lower check would create a new contact and is not accepted by the contact-minimal endpoint test.
- Equality for an old nondiameter upper check could create a new diameter without decreasing the diameter-pair count; strict inequality is required.
- Equality is allowed on old diameter rows, but at least one must be strict. If all are strict, the new maximum is strictly below `D`; otherwise the retained old diameter rows ensure the new diameter is `D` and the attaining set is a proper subset.
- Contact isolates are fixed in the common-angle coordinates and remain included in all pair checks. Audit.95's retained-isolate example demonstrates why a core-only upper check is insufficient.
- `t` ranges over all finite real values and covers every angle modulo `2pi` except `pi`; `pi` is handled by its separate exact test.
- The interval decision is asserted only for algebraic coordinates. The geometric identity and inequalities hold for arbitrary real coordinates, but no exact algorithm for arbitrary real input is claimed.
- This is one fixed train-bit path. It proves neither that a nonconstant face-closed pattern exists nor that any pattern admits a permitted parameter.

The exact finite verifier was rerun from the frozen source snapshot. It checked 64 hexagon bit patterns, 10 closed patterns, 420 exact pair-change identities including a retained isolate, and the listed finite regression checks. Output SHA-256 `fb1bc03761f7dadab87e5b5672c21d12c2e9dc2291f341552996edb33a21593f` matches the previously audited Audit.95 run. The verifier supports only those finite examples; the general identity and decision criterion are established by the derivation above.

## 4. Canonical disposition

| Claim | Verdict | Disposition |
| --- | --- | --- |
| Common-angle closure/integration | PASS — already subsumed | `C-FACE-COUPLED-QUARTER-FOLD-INTEGRATION` |
| Active-diameter amplitude gap | PASS — already subsumed | `C-COMMON-ANGLE-ACTIVE-DIAMETER-AMPLITUDE-GAP` |
| Exact full-source pair quadratics, including isolates | PASS — promote | `C-COMMON-ANGLE-ALGEBRAIC-FULL-SOURCE-PAIR-TEST` |
| Exact algebraic one-parameter sign decision | PASS — promote | Included in `C-COMMON-ANGLE-ALGEBRAIC-FULL-SOURCE-PAIR-TEST` |
| Existence of a beneficial bit pattern or endpoint in a canonical source | NOT PROVED | Remains open |
| C-II or Level I closure | NOT PROVED | Both remain open |

This promotion adds a check for candidate finite motions. It does not change the exact active full-core obligation, the macroscopic-container branch, C-II status, or Level I status.
