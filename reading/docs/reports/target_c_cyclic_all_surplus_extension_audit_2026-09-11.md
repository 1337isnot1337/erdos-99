> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_all_surplus_extension_audit_2026-09-11.md) · source SHA-256 `2759cfd0e5beb709e07702685100c139d3230f85fc62d4ecf633495538baa890`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-8D3C3AFB8C21","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Audit correction for the cyclic all-surplus extension

**Date:** 2026-09-11

**Audited report:** `target_c_cyclic_all_surplus_extension_2026-09-11.md`

**LEVEL I STATUS:** `STILL OPEN`.

## Superseding independent audit

The original version of this file stated that the main PR #191 theorem survived review and repaired only one scalar implication in Section 6. That conclusion is withdrawn.

The independent dependency audit

`target_c_pr191_dependency_audit_2026-09-11.md`

found an earlier load-bearing geometric failure which the scalar audit did not inspect. The September 10 cyclic Reuleaux-cap detour report places an OP outer pocket on the wrong side of its force-hull chord. An OP pocket is an inward bounded face inside `F`; the minor Reuleaux circular cap is outside the inscribed force hull. Therefore the claimed containment and the derived local inequality

```math
\ell\le D\phi
```

are false. The six-point regular pentagon plus center gives an exact finite force-visible regression with `ell=2>D*pi/5`.

Consequently the general cyclic claims

```math
b-P_F=O(\sqrt D),
\qquad
H_{out}=o(D^2)
```

are not proved by the cited argument. PR #191 then loses the exceptional-face-only cavity inequality, the normalized train/outer-walk chain built on that detour, and therefore the reported ordinary-surplus floor

```math
0.99554058458\ldots
```

and its qualitative endpoint gap.

The scalar correction below remains algebraically valid **conditional on the earlier cyclic cavity/train premises**, but those premises are not currently established. It must not be read as an audit of the full theorem.

## Surviving PR #191 subclaims

The independent audit separately certifies the following pieces:

1. the odd diameter-cycle skeleton gives
   ```math
   P_F=\pi D-O(\sqrt D)
   
   ```
   without using outer pockets;
2. FS.4 plus maximal-perimeter central-symmetral rigidity gives
   ```math
   area(F)/D^2\to\pi/4;
   
   ```
3. the exact `s_Z` terms cancel in the full-source Oler bookkeeping;
4. the independent full-source cell-slack theorem proves
   ```math
   E=O(D)
   
   ```
   in every C-II branch, without the cyclic detour.

What does not survive is the assertion that the inward outer-contact region is negligible.

---

## Conditional scalar correction retained for provenance

Assume, contrary to the current theorem state, that one has independently proved the cyclic premises

```math
w\ge w_0(\nu):=\pi\sqrt{1-\nu^2}\quad(0\le\nu<1),
```

```math
\xi\ge {4\over5}H(w),\qquad
H(w):=w+\sqrt{{\pi^2-w^2\over2\pi\sqrt3}},
```

and

```math
\xi\le\nu+\kappa,
\qquad
\lambda=\nu+3\kappa.
```

The old Section 6 used the unjustified implication `w>=1 => nu<=sqrt(1-1/pi^2)`. The correct scalar separation is as follows.

If `w>=pi`, then `xi>=w>=pi>nu`, so

```math
\lambda\ge\nu+3(\xi-\nu)=3\xi-2\nu>3\pi-2>1.
```

Now suppose `1<=w<=pi`. The function

```math
w\mapsto \sqrt{\pi^2-w^2}
```

is concave on `[1,pi]`; hence `H` is concave there and its minimum is attained at an endpoint. Both endpoint values exceed one:

```math
H(\pi)=\pi,
```

and

```math
H(1)=1+\sqrt{{\pi^2-1\over2\pi\sqrt3}}>1+{1\over\sqrt2},
```

because `pi^2-1>pi sqrt(3)`. Therefore

```math
\xi\ge {4\over5}\min\{H(1),H(\pi)\}
>{4\over5}\left(1+{1\over\sqrt2}\right)>1.
```

Since `nu<1`, again `xi>nu`, so

```math
\lambda\ge3\xi-2\nu
>{12\over5}\left(1+{1\over\sqrt2}\right)-2>1.
```

Thus no minimizer of the limiting ordinary surplus below one lies in `w>=1`.

It remains to consider `0<=w<1`. Then the assumed cavity inequality forces `w_0(nu)<1`, so

```math
\nu>\nu_0:=\sqrt{1-1/\pi^2}.
```

On `[0,1]`,

```math
H'(w)=1-{w\over2\pi\sqrt3\sqrt{r_{min}(w)}}>0,
```

using `r_min(w)>1/2`. Hence

```math
\nu+\kappa\ge\xi\ge F(\nu):={4\over5}
\left(\pi\sqrt{1-\nu^2}+\nu\sqrt\Delta\right),
\qquad \Delta={\pi\over2\sqrt3}.
```

Let `lambda_A` be the unique root of `F(nu)=nu` in `(0,1)`. If `nu>=lambda_A`, then `lambda>=nu>=lambda_A`. If `nu_0<nu<lambda_A`, then `kappa>=F(nu)-nu` and therefore

```math
\lambda\ge G(\nu):=3F(\nu)-2\nu.
```

The derivative is

```math
G'(\nu)= {12\over5}
\left(\sqrt\Delta-{\pi\nu\over\sqrt{1-\nu^2}}\right)-2.
```

For `nu>=nu_0`, the ratio `nu/sqrt(1-nu^2)` is increasing and

```math
{\pi\nu_0\over\sqrt{1-\nu_0^2}}=\pi^2\nu_0>\sqrt\Delta.
```

Thus `G'(nu)<-2<0` on this interval. Consequently

```math
G(\nu)>G(\lambda_A)=\lambda_A
\qquad(\nu<\lambda_A).
```

So the scalar optimization itself was repairable. It simply has no current theorem to optimize because the necessary cyclic cavity/train premise is missing.

## Final audit conclusion

| Item | Status after independent dependency audit |
| --- | --- |
| scalar `w>=1` correction in this file | valid conditional algebra |
| `P_F=pi D-O(sqrt D)` | valid |
| `area(F)/D^2->pi/4` | valid |
| arbitrary-`s_Z` Oler cancellation | valid |
| `E=O(D)` | valid independently |
| Reuleaux minor cap contains inward OP pocket | false |
| general `b-P_F=O(sqrt D)` | unproved |
| general `H_out=o(D^2)` | unproved |
| PR #191 `0.99554058458...` theorem | rejected as a proved theorem |
| endpoint gap above that number | rejected as a proved theorem |

A replacement proof must control the inward contact chain itself. Exterior Reuleaux-cap geometry is insufficient.
