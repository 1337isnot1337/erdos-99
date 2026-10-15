<!-- theorem-state: {"artifact_id":"ART-8FA0E7BA966B","canonical":false,"claim_ids":["C-HEPTAGON-PSD-STRESS-FINITE-COMPETITOR-REGRESSION","C-TWO-POINT-HINGE-RANK-FINITE-FLEX-REGRESSION"],"claim_statuses":{"C-HEPTAGON-PSD-STRESS-FINITE-COMPETITOR-REGRESSION":"regression","C-TWO-POINT-HINGE-RANK-FINITE-FLEX-REGRESSION":"regression"},"index":"docs/state/artifact-index.jsonl","status":"regression","target":"target-c"} -->
# Independent audit: finite hinge and heptagon stress regressions

Date: 2026-10-08. Audit base: `origin/main=b7bab1e92efe8e8232635d814178cabccff8ef71`, state `2026-10-08.audit.121`; Target C C-II remains open.

Frozen source: `origin/swarm/sol/contact-convexity-exclusion-20261002` at `b79aa0cfd8ceb2d10685890fe06b12a71607745b`. Source report `docs/reports/target_c_finite_core_rigidity_and_cut_anchoring_2026-10-02.md`, SHA-256 `3e28bda1b7b64d86a220d77aae1ee036a4cd47770a1ef9ead556082669bbc99d`. Exact finite verifier `research/verify_target_c_finite_core_rigidity_2026_10_02.py`, SHA-256 `5005feac3244fe835262a9c5f1671631da7ca4403a288856f08267ea932f18b0`.

## Verdict

**PASS — register two scoped regressions.** The finite hinge shows that infinitesimal rigidity of an abstract bar framework alone does not prevent a two-vertex hinge. The regular-heptagon witness has a positive semidefinite equilibrium stress and an infinitesimally rigid mixed framework, yet an explicitly labeled same-cardinality unit-separated placement preserves all old contacts and has strictly smaller diameter. The heptagon is not globally optimal, and the replacement adds five contacts, including unit triangles. Neither example is a counterexample to a theorem whose hypotheses require a canonical global minimizer and the exact old contact graph.

## 1. Rank-five hinge regression

Take

```text
p0=(0,0), p1=(2,0), p2=(1,1), p3=(1,-2)
bars={(0,1),(0,2),(1,2),(0,3),(1,3)}.
```

The first three bars form a nondegenerate triangle. The last two constrain `p3` to its distances from `p0,p1`. The rigidity matrix has rank five, which is the planar infinitesimal-rigidity rank `2*4-3`. The graph has the two-vertex cut `{p0,p1}`. Reflecting `p3` across the line `x=1` to `(1,2)` preserves all five bar lengths, while changing the unbarred distance `|p2-p3|` from `3` to `1`. Since the five-row matrix has rank five, its self-stress space is zero-dimensional.

This is an exact counterexample to the inference “rank `2v-3` by itself implies no finite hinge across a two-vertex cut.” It is an abstract bar framework, not an actual Target C contact/diameter framework and not a global-minimizer claim.

## 2. Regular-heptagon positive-stress competitor regression

Let `p_0,...,p_6` be a regular unit heptagon in cyclic order. Its contact graph is the seven-cycle `C={i(i+1) mod 7}`. Its seven step-three chords `H={i(i+3) mod 7}` are the diameter pairs. Put `D=sin(3*pi/7)/sin(pi/7)=1/(2*sin(pi/14))`. The contact graph is triangle-free.

Assign contact stress `alpha=D^2/7` on each edge in `C` and diameter stress `beta=1/7` on each edge in `H`. Both are positive; their total masses are `D^2` and `1`. At each vertex the two contact-neighbor force vectors sum to `2(1-cos(2*pi/7))p_i`, and the two diameter-neighbor vectors sum to `2(1-cos(6*pi/7))p_i`. The identity `D^2(1-cos(2*pi/7))=1-cos(6*pi/7)` proves exact equilibrium.

The stress matrix is the circulant weighted Laplacian

```text
Omega = (D^2/7) L_1 - (1/7) L_3,
lambda_k = (4/7) [D^2 sin^2(k*pi/7) - sin^2(3*k*pi/7)], k=0,...,6.
```

Modes `k=0,1,6` have eigenvalue zero; these are exactly the constant and two coordinate modes. For `k=2,5`, the positive term compares `sin(3*pi/7)sin(2*pi/7)` with `sin^2(pi/7)`, so it is strictly larger. For `k=3,4`, it compares `sin^2(3*pi/7)` with `sin(2*pi/7)sin(pi/7)`, again strictly larger. Thus `Omega` is positive semidefinite with rank four and precisely the affine kernel.

The mixed framework consisting of `C union H` is infinitesimally rigid. The nondegenerate bar triangles `(0,1,4)`, `(1,4,5)`, `(1,2,5)`, `(2,5,6)`, `(2,3,6)` start with one rigid triangle and add each remaining vertex along a shared edge. The two bars to the shared edge endpoints determine the new vertex's velocity, giving rank `2*7-3=11`.

Now use the labeled placement

```text
q0=(0,0), q1=(1,0), q2=(1/2,sqrt(3)/2), q3=(-1/2,sqrt(3)/2),
q4=(-1,0), q5=(-1/2,-sqrt(3)/2), q6=(1/2,-sqrt(3)/2).
```

The exact squared distances of its 21 pairs are all at least `1`, its diameter is `2`, and all seven old cycle contacts remain unit. The old step-three squared lengths become `(1,4,4,4,1,3,3)`, with sum `20`; five additional unit contacts appear. Since `pi/14 < 11/49 < 1/4` and `sin(x)<x`, the old diameter `D=1/(2 sin(pi/14))` is strictly greater than `2`. Hence the new placement is a same-cardinality strict sub-`D` competitor to this heptagon. The stress-weighted old-diameter gain is `D^2-20/7>8/7`; the contact contribution is unchanged.

The heptagon is not a global minimum-diameter seven-point set: the displayed placement already has smaller diameter. The replacement itself has triangles and a different contact graph. It therefore does **not** contradict the canonical finite contact-isometry theorem, which assumes a global minimizer and forbids new contacts, and it says nothing about Level I. It refutes only the overstrong claim that positive semidefinite equilibrium stress plus mixed infinitesimal rigidity alone blocks a finite contact-preserving strict-diameter competitor when extra contacts are allowed.

## 3. Certificate audit and scope

The frozen verifier was inspected and rerun. It uses exact `Fraction`/SymPy arithmetic; its hinge check verifies rank, bar-length preservation, the changed nonedge, and zero self-stress dimension. Its heptagon check stores the seven-point placement in rational coordinates scaled by `sqrt(3)` and checks all 21 pair distances, the seven old contacts, the seven old diameter lengths, the five new contacts, and the exact gain lower bound. The script does not certify the universal Fourier-spectrum argument or infer global optimality; those points are proved analytically above, with global nonoptimality demonstrated by the explicit competitor.

Counter-scope checks: the hinge is not a source framework; the heptagon is not a global minimizer; the finite replacement introduces unit contacts and equilateral triangles; the diameter decrease is finite and does not supply a feasible path. These exclusions are part of each regression's scope.

| Claim | Verdict | Canonical disposition |
| --- | --- | --- |
| Rank-five two-vertex hinge | REGRESSION VALID | `C-TWO-POINT-HINGE-RANK-FINITE-FLEX-REGRESSION` |
| Positive-stress regular heptagon with a strict contact-preserving competitor | REGRESSION VALID | `C-HEPTAGON-PSD-STRESS-FINITE-COMPETITOR-REGRESSION` |
| Either finite example refutes C-II or Level I | REJECTED SCOPE | Neither is a canonical global-minimizer counterexample |

The audit adds no dependency theorem and changes no C-II or Level I obligation. The exact source verifier is registered as a finite regression certificate; its analytic claims remain those in this audit.
