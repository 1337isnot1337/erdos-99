> Generated reading edition · [exact source](../../../docs/reports/target_c_section146_face_rank_endpoint_stability_2026-09-12.md) · source SHA-256 `0e3e383107f7b4547cacd5a100a485a84624831d332647ca050f744e412579d5`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-638F5DF039AF","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — Section-146 face-rank endpoint stability

**Date:** 2026-09-12
**Classification:** proof-only audited-working composition; noncanonical
**LEVEL I STATUS:** STILL OPEN. C-II REMAINS OPEN.

Let

$$
C_{146}={4\over9}\left(\pi+\sqrt{\Delta_2}\right)
=1.8195135379794445\ldots,\qquad
\Delta_2={\pi\over2\sqrt3},
$$

and $t_D=(q-k)/D$, $k=d_H+s_Z$. Along a Type-II subsequence assume

$$
t_D\le C_{146}+\eta+o(1)
$$

for fixed $\eta\ge0$.

## 1. Scalar stability

Audited-working §146 gives

$$
t-\frac{d_H+s_Z}{9D}\ge C_{146},
$$

so

$$
\boxed{\frac{d_H+s_Z}{D}\le9\eta+o(1).}
\tag{146S.1}
$$

The same face inequalities give

$$
\frac fD\ge\sqrt{\Delta_2}-{t\over4}
 +{d_H+s_Z\over4D},
\qquad
\frac QD\le2t-\pi+o(1).
$$

Therefore

$$
\boxed{\frac{Q-f}{D}\le{9\over4}\eta+o(1).}
\tag{146S.2}
$$

Since $Q-f$ counts degree excess beyond pentagons, all but

$$
\boxed{\left({8\sqrt{\Delta_2}-\pi\over9}-{5\over2}\eta-o(1)\right)D}
\tag{146S.3}
$$
of the bounded nonquadrilateral faces are pentagons. At $\eta=0$, the coefficient
is $0.4974344224\ldots$.

## 2. Outer detour collapses at the endpoint

The exact ledger is $b=2h-Q-2s_Z$. Since $h/D=t+s_Z/D$,

$$
\frac{b-\operatorname{per}(F)}D
\le2t-\frac fD-\pi+o(1)
\le\boxed{{9\over4}\eta+o(1)}.
\tag{146S.4}
$$

Thus a sequence approaching $C_{146}$ cannot hide its pentagon population in a
linear outer-walk detour.

## 3. Face-closure rank

The audited proof-only face-closure identity gives

$$
2f-\operatorname{rank}C_{\rm face}=\sigma_C,\qquad
0\le\sigma_C\le s_Z.
$$

Combining this with the lower face bound yields

$$
\boxed{
\frac{\operatorname{rank}C_{\rm face}}D
\ge
0.9948688448\ldots-5\eta-o(1).
}
\tag{146S.5}
$$

At the scalar endpoint, the pentagon closure matrix has asymptotically full row
rank: its row corank is $o(D)$. The associated stopping-face Hall theorem also
gives $|N(S)|\ge2|S|-9\eta D-o(D)$ for every defect-face subset $S$.

## 4. Exact remaining obstruction

The audited composition reduces the formal §146 endpoint to a linear network of
unit pentagons with vanishing degree excess, vanishing mixed surplus, vanishing
outer detour, and nearly full closure rank. This is a structural narrowing, not a
contradiction. A closing theorem must use the pentagon edge directions and train
phases to show that this network cannot satisfy both the §142 quadratic crossing
measure and the full-rank closure equations, or must produce a finite
source-preserving diameter descent.

The linear-detour branch and the macroscopic inactive-container branch remain open.
