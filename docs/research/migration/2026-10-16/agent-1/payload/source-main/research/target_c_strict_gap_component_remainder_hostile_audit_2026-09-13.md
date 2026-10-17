# Hostile audit — strict aggregate gap component remainder

**Date:** 2026-09-13  
**Reviewed artifact:** `target_c_strict_gap_component_remainder_2026-09-13.md`  
**Disposition:** PASS at proof-only scope; theorem-state authority unchanged.  
**LEVEL I STATUS:** STILL OPEN. C-II REMAINS OPEN.

## 1. Finite algebra

The artifact defines

`X_D=q-k-S_D` and `G_D=2+q+m-k-S_D`.

Direct subtraction gives

`G_D=m+2+X_D`.

No asymptotic estimate or face-occurrence identification is used in this step. The
strict-gap input is exactly the previously audited proof-only bound
`liminf X_D/D >= pi(2-sqrt(3))/20`, so the conclusion
`liminf (G_D-m)/D >= alpha` follows.

The identification with the §160 remainder is valid in its audited Type-II scope:
`G_D=R_I+s_B+sum_r eta_r`, with every summand nonnegative. The artifact does not
mistake this for a global KKT stress or a local face count.

## 2. Long-side correction

The audited §172 identity is

`chi_D=S_D+G_D+k-per(F)-2`, and the exact outer-walk split is
`b-per(F)=u_B+chi_D` with `u_B>=0`.

Along a subsequence with `S_D/D -> S`, `m/D -> mu`, and `k/D -> kappa`, inserting
the remainder lower bound and `per(F)/D -> pi` gives

`liminf chi_D/D >= S+mu+kappa+alpha-pi`.

Since the actual outer detour is nonnegative, taking the positive part is safe. The
endpoint constant is

`S118 + alpha - pi = -0.3009069810...`;

the displayed threshold is rounded only in the explanatory decimal, not used as a
proof premise.

## 3. Ledger compatibility and scope

In Type II, `e_BB=q-m`; combining `e_BB=Q+2k+u_B` with the exact outer ledger gives
the stated inequality (SGR.11). This is a compatibility condition, not a claimed
contradiction.

All source points remain in the source. Contact-isolated points are not inserted into
the core rigidity matrices. No strict sub-diameter source, unit triangle, or Level-I
claim follows.

**Final verdict:** the composition is arithmetically and logically sound at the
stated proof-only scope. C-II remains open.
