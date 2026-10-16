# Hostile audit — coupled paired-remainder path and finite-defect strip through `t<=1.8687`

**Date:** 2026-09-15  
**Reviewed:** `target_c_coupled_paired_remainder_path_t18687_2026-09-15.md`, `verify_target_c_coupled_paired_remainder_path_t18687.py`, `target_c_finite_defect_kkt_strip_t18687_2026-09-15.md`, and `verify_target_c_finite_defect_kkt_strip_t18687.py`.

**Verdict:** **PASS at proof-only full-core Type-II scope.**  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The `1.8687` certificate re-evaluates the corrected retained-mass feasibility box and proves `delta_max<0.107`, `H(2.0477)<0`, and a uniform coupling slope `c=1.36`; it does not extrapolate the older `1.39` slope.

For retained terminal weights `a,b` and `w=min(a,b)`, pair weights `w,w` plus residual weights `a-w,b-w` partition the original occurrence measure exactly. The residual measure only decreases a perimeter-dominated measure, so it remains perimeter-dominated and the same bathtub applies. Hence `E_pair+F(z-2P)<=delta+o(1)` has no double counting.

The low-energy functional is increasing in `P` because `lambda>0.4787>2-sqrt(3)`, so substituting the endpoint-count lower bound for `P` is adverse. After the feasibility coupling is inserted, its detour derivative is
\[
L'=c+2-{1+(c+4)F'(r)\over\lambda}-{A\over\lambda^2}.
\]
The exact certificate uses `r<2.047`, `F'(r)<0.059`, `A<0.107`, and `lambda>0.4787` to obtain `L'>0.143`; no interior detour minimum is missed.

The adaptive threshold `lambda(delta)=0.5857-delta` remains positive and lies below the exact same-oriented root because `0.5857<2-sqrt(2)`. Thus selected trains genuinely use opposite physical terminal branches.

Outward endpoint arithmetic gives low-energy pair weight above `6.115e-4 D` and one-phase path weight above `2.038e-4 D`; the theorem rounds these to `0.0006D` and `0.0002D`.

For the finite-defect propagation, the parent proof only uses
\[
\sum N_i\le2\pi D,\qquad \sum D B_i\le2D,\qquad 2T_{tr}/D\le10T-4\pi+o(1).
\]
At `T=1.8687`, the new certificate independently checks
```text
Q/D upper                    0.5958073464
terminal occurrence upper    6.1206293856
combined complexity          14.4038146928
combined/path average        70954.7521814
```
with safe path floor `0.000203D`. Hence an eligible nonhub layer with `N_i+L_i+D B_i<70955` exists.

The crossing-neighborhood argument remains exact: a transverse train crossing one boundary but not the other must terminate in the intervening region, so the symmetric difference is at most `L_i`. Since every bounded exceptional face contributes at least five terminal occurrences, the selected strip contains at most `14190` such faces.

No finite-defect bound alone gives a strict diameter decrease; individual switching multipliers may still be arbitrarily small and no inverse-`D` adjacent phase gap is proved.

**Final verdict:** **PASS at proof-only scope. C-II and Level I remain open.**
