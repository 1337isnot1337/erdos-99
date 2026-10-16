# Target C-II — combined generic H7b endpoint: 22 C7 cells

**Date:** 2026-09-19  
**Scope:** generic interior-ground `H7b` only  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

Two independent nonlinear layers now sharpen the repaired full-angle endpoint.

The exact full-angle affine system leaves 27 generic `C7` cells. The audited law-of-sines reduction excludes

\[
\{115,118,145,146\}.
\]

The independent force-closure argument excludes

\[
\{176\}.
\]

These sets are disjoint. Therefore the current generic interior-ground endpoint is

\[
\boxed{27\longrightarrow22}.
\]

The surviving one-based canonical orbit indices are

```text
129, 130,
134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144,
147, 148,
169, 170, 171, 172, 173, 174, 175
```

All remain of missing-graph type `C7`.

## Validation correction

The historical full-angle verifier had a one-site dispatch defect and was repaired by

`verify_target_c_support7_h7b_full_angle_reduction_repaired_2026_09_19.py`.

The later law-of-sines verifier invoked the broken historical file directly through `runpy`, so it inherited the same executable failure before reaching its own certificate payload. The repair shim

`verify_target_c_support7_h7b_law_of_sines_repaired_2026_09_19.py`

redirects that dependency to the repaired full-angle namespace and otherwise executes the law-of-sines verifier unchanged. This is an implementation correction, not a change to the four law-of-sines exclusions themselves.

## Metric formulation after the reduction

For every remaining cell, radial metric compatibility is a complete-graph condition. If

\[
g_{ij}=\log\sin A_{ij}-\log\sin A_{ji},
\]

then `g` must be exact on all 21 edges of `K7`. The complete cycle rank is 15. The 14-edge present relation graph has cycle rank only 8, so relation-only law-of-sines checks omit seven independent metric cycles carried by missing relation edges.

A root-fan basis gives the fifteen equations

\[
\sin A_{1i}\sin A_{ij}\sin A_{j1}
=
\sin A_{i1}\sin A_{ji}\sin A_{1j},
\qquad 2\le i<j\le7.
\]

Under the strict full-angle hypotheses these fifteen equations reconstruct a common reciprocal radial metric up to similarity. After that reconstruction, force closure at the seven non-ground vertices automatically implies force closure at the ground by pairwise cancellation of edge forces.

Equivalently, each remaining cell can be tested by the nonnegative analytic defect

\[
\Phi
=
\sum_{i=1}^7 C_i
+
\sum_{2\le i<j\le7}M_{ij}^2,
\]

where `C_i` is the squared five-unit-vector closure residual of force pentagon `i` and `M_ij` is the complete sine-cycle residual. Within a surviving strict generic cell, feasibility is equivalent to existence of a zero of `Phi`.

## Remaining bottleneck

The 22 cells above have not been proved realizable or impossible. A numerical force-only probe identified orbit 129 as another likely nonclosing cell, but no rigorous certificate is currently committed for it; numerical residuals are not evidence of exclusion.

The next useful finite target is therefore either:

1. derive an orbit-129 analogue of the exact cross-face gap identities used for orbit 176 and turn it into an analytic force-closure contradiction; or
2. certify `Phi>0` on each remaining strict affine cell using validated interval subdivision, with boundary boxes handed to the already separate reciprocal-collinearity/order-wall analysis.

The generic `H7b` branch is only one support-seven branch. Reciprocal-collinearity walls, `H7a`, `H6`, and surviving `H8` cases remain separate.

No theorem-state file is changed. C-II remains open.
