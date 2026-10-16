<!-- theorem-state: {"artifact_id":"ART-B545E1640A60","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Hostile audit — Section-120 companions and two-half-disk scalar regressions

**Date:** 2026-09-13  
**Base state:** 2026-09-12.audit.46  
**Reviewed:**

- research/target_c_section120_interface_ceiling.md;
- research/target_c_section120_neardisk_sampling_regression.md;
- research/target_c_two_halfdisk_scalar_regression_2026-09-12.md;
- research/target_c_two_halfdisk_post173_scalar_regression_2026-09-12.md.

**Disposition:** all four findings pass at their stated proof-only/regression scopes.
They do not weaken a canonical theorem, construct a source, or close C-II.

## 1. Two-half-disk scalar witnesses

Both scalar reports use the same exact rational point

    t=21/10, kappa=0, S=14/5, G=3/10, mu=31/10,
    m=1, e=11/10, u=1/10, Q=1, f=9/10, T=39/10.

The exact identities are

    mu=S+G, m=mu-t, e=2*t+kappa-mu, Q+u=e-2*kappa,
    T=t+2*f, q/D=t+kappa=m+e.

The two verifier scripts were rerun and passed:

    python3 research/verify_target_c_two_halfdisk_scalar_regression.py
    python3 research/verify_target_c_two_halfdisk_post173_scalar_regression.py

The common witness has these exact margins before irrational floors:

    T-q/(2D)=57/20=2.85,
    T=39/10=3.9,
    S+G=31/10=3.1,
    5*t=21/2=10.5,
    5*t-2*mu=43/10=4.3,
    4*f+Q=23/5=4.6 < 10*(e-kappa)=11,
    u+mu+kappa=16/5=3.2,
    10*(e-kappa)+2*(2-S)=47/5=9.4.

Using 3.14159 < pi < 3.14160, 1.73205 < sqrt(3) < 1.73206,
and 1.41421 < sqrt(2), the required irrational right sides are bounded by

    2*sqrt(pi/sqrt(3)) < 2.70,
    2+pi*(4-2*sqrt(3))/8 < 2.22,
    pi*(2-sqrt(3))/4 < 0.22,
    2*sqrt(pi/(2*sqrt(3))) < 1.91,
    2*sqrt(pi/(2*sqrt(3)))-pi/2 < 0.34,
    pi < 3.15,
    pi*(2-sqrt(3))/2 < 0.43.

Thus the witness passes every displayed scalar test with a strict margin. The second
script uses ordinary floating-point evaluation for some diagnostic constants, but all
comparisons above have margins much larger than floating-point roundoff; the first
script independently checks the same point with rational bounds. This certifies the
claimed arithmetic regression, not geometric realization.

**Verdict:** both reports are audited arithmetic regressions. They show only that the
listed scalar currencies do not contradict one another. The witnesses are not sources,
do not satisfy the geometric hypotheses merely by satisfying normalized inequalities,
and do not disprove any perimeter or train theorem.

## 2. Section-120 local interface ceiling

For unit train directions at acute projective angle phi in (pi/3, pi/2], the local
return is C(q;u,v)=4-2*(|q.u|+|q.v|). The exact planar minimization is

    min_|q|=1 (|q.u|+|q.v|) = sin(phi),

attained by a direction perpendicular to one train direction. Therefore

    C(q;u,v) <= 4-2*sin(phi) < 4-sqrt(3).

The strict inequality is the strict-rhombus angle hypothesis; equality is only a
limit as phi decreases to pi/3. If the full-core Type-II inputs r=D,
A_4/D^2 -> pi/4, and per(F)/D -> pi are granted, Section 120 can force at most

    kappa_120 <= 2-pi+(4-sqrt(3))*pi/4
               = 0.6396504768243367...

Canonical Section 85 already gives

    kappa_85 = 4*sqrt(pi/(2*sqrt(3)))-pi
              = 0.6676585738660363...

and the exact difference is 0.0280080970416996... > 0. The calculation is correct.
It is a ceiling on one proposed use of Section 120, not a new lower bound and not a
refutation of Section 120.

The inherited near-disk equalities are an explicit scope condition. Without them the
coefficient comparison is not an all-regime statement.

**Verdict:** PASS as a method-ceiling regression. Uniform first-order Section-120 use
cannot replace the stronger canonical Section-85 train-interface bound.

## 3. Uniform near-disk chord sampling

For the projective grid xi_j=j*pi/m, the uniform Riemann-sum estimate for the
Lipschitz periodic function |cos| gives

    sup_u | m^(-1) sum_j |xi_j.u| - 2/pi | -> 0.

Applying the finite Section-120 inequality to the finitely many extreme-vertex chord
pairs, then taking D -> infinity at fixed m, is legitimate under canonical near-disk
convergence: each chord has r/D -> 1, while A_4/D^2 -> pi/4. The averaged inequality
becomes

    liminf (L+P_exc)/D >= 2 + (pi/4)*(4-8/pi-4*eta_m)
                              = pi-pi*eta_m.

Letting m -> infinity gives exactly liminf (L+P_exc)/D >= pi. The cancellation check
is exact: 2 + (pi/4)*(4-8/pi) = pi.

Canonical Section 85 instead gives
liminf (L+P_exc)/D >= 4*sqrt(pi/(2*sqrt(3))) = pi+0.6676585....
Hence the uniform chord average is first-order weaker, as claimed.

The order of limits matters: the argument is fixed-grid first, then D, then grid
size. It does not claim a uniform finite-grid chord selection over a changing source,
and it does not use a second-order correlation that the note explicitly leaves open.

**Verdict:** PASS as a route-selection barrier. Isotropic chord sampling alone cannot
close the full-core branch.

## 4. Frontier and claim classification

The scalar witnesses are regressions, audited arithmetic only. The two Section-120
companions are audited-working proof-only method ceilings. None is a promoted closure
theorem. The macroscopic-container branch, the aggregate detour upper bound, and the
source-preserving descent/unit-triangle alternatives remain open. C-II and Level I
remain open.
