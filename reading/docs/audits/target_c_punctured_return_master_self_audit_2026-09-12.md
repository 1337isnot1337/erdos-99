> Generated reading edition · [exact source](../../../docs/audits/target_c_punctured_return_master_self_audit_2026-09-12.md) · source SHA-256 `bd1987b27c1a528ca7633fd2fb25964dbc578f1ef002349ecd8a55c89dac7634`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-829C78895BA0","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — hostile self-audit of the global punctured-return master

**Date:** 2026-09-12  
**Artifact audited:** `research/target_c_punctured_return_master.md`  
**Disposition:** finite master inequality and equilateral averaging pass this same-run hostile audit; theorem remains proof-only.  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This audit targets the two places where the new argument could silently overreach: globalization of Section-116 signed return from one harmonic cell to the full positive-contact core, and realization of a rotating equilateral host triple by actual outer-walk vertices in the Type-II near-disk limit.

## 1. The punctured-packing algebra is exact

Canonical Section 67 gives

```math
b+Q=2(q-k),
\qquad
m=R_4+f+q-k+1,
```

and

```math
a_0N_F
\le
\operatorname{area}(F)+{a_0\over2}\operatorname{per}(F)+a_0-E_4.
```

Write

```math
N_F=m+Z_F,
\quad
\operatorname{area}(F)=A_4+G_F,
\quad
E_4=A_4-a_0R_4.
```

Cancellation gives

```math
f+(q-k)+Z_F
\le {G_F\over a_0}+{\operatorname{per}(F)\over2}.
```

With

```math
\Xi_F={G_F\over a_0}-Z_F
```

and

```math
\omega_F={G_F\over a_0}+{\operatorname{per}(F)\over2}-f-(q-k)-Z_F\ge0,
```

the identity

```math
b+P_{exc}
=\operatorname{per}(F)+2f+2\Xi_F-2\omega_F
```

is exact. No asymptotic step occurs here.

A useful hostile observation is that this identity does **not** by itself upper-bound the route length unless `Xi_F` or `omega_F` is controlled independently. Indeed

```math
f+\Xi_F-\omega_F
=2f+(q-k)-{\operatorname{per}(F)\over2}.
```

Thus the new theorem is a change of currency, not a hidden contradiction. The research note states this correctly in its boundary-order handoff.

## 2. Every strict-rhombus train terminates on the designated route system

Canonical Section 67 proves that every bounded four-face of the full connected positive-contact core is a convex strict unit rhombus and every other bounded face has degree at least five. Therefore a physical boundary side of the union of all strict-rhombus faces has on its opposite side either

1. the outer face of the positive-contact core, or
2. one bounded nonquadrilateral face.

A train cannot close cyclically inside a finite strict-rhombus complex. Along a train with fixed physical edge direction `u`, the transverse coordinate `det(u,x)` changes strictly in one sign through every crossed strict rhombus. A closed train would return to its initial value. Hence every train has two physical terminal side occurrences and both are represented in the outer-walk/nonquadrilateral-cycle route system.

## 3. Physical-occurrence injectivity survives bridges and articulations

The global outer face is used as its occurrence-counted boundary walk. A bridge can therefore occur twice with opposite face-side occurrences, and a repeated articulation vertex can occur many times. The train-end assignment is not by vertex or by underlying undirected edge; it is by the actual rhombus boundary edge-side occurrence.

Each such occurrence has exactly one opposite face. It is assigned either to its unique outer-walk occurrence or to the clockwise boundary occurrence of that bounded nonquadrilateral face. Thus no physical train end pays twice.

The three open outer arcs partition the outer-walk occurrences after the cut occurrences are chosen. Adding all bounded nonquadrilateral face cycles therefore gives total route length exactly

```math
b+P_{exc}
```

and total displacement norm exactly `Pi_3` on the three open arcs, zero on the closed cycles. Thus

```math
E_{route}=b+P_{exc}-\Pi_3.
```

## 4. Global train-area transport uses only the full-source diameter

For one complete train, the sum of its strict-rhombus areas is the transverse displacement between the two terminal boundary-edge midpoints. Those midpoints lie in `F`, since every terminal edge joins core vertices in `F`.

The force hull has diameter exactly `D`: normalization gives at least one positive actual diameter row, and the endpoints of every positive diameter row are loaded vertices in `B subset F`. Hence

```math
\sum_{R\in\tau}\operatorname{area}(R)\le D.
```

This step uses the full-source diameter only as an upper bound. It does not identify the core vertex count with the full source cardinality and does not discard contact-isolated points.

## 5. The equilateral width integral is exact

For three unit hosts at arguments `0,2pi/3,4pi/3`, adding `0` changes no support value because zero lies in their convex hull. On `0<=t<=pi/3`, direct comparison of the three scalar products gives

```math
w(t)=\sqrt3\cos(t-\pi/6).
```

Therefore

```math
\int_0^{\pi/3}w(t)\,dt=\sqrt3,
```

so the mean one-direction return is

```math
2-{3\sqrt3\over\pi}.
```

Translation in the rotation parameter shows that each train direction has this same mean independently of its phase. Hence every rhombus, regardless of the angle between its two train directions, has mean pair return

```math
c_{eq}=4-{6\sqrt3\over\pi}.
```

Fubini over the finite rhombus set is immediate. No phase purity, no coherent-grain decomposition, and no `O(1/D)` phase collapse are used.

The exact constant check is

```math
{\pi\over4}c_{eq}
=\pi-{3\sqrt3\over2}.
```

## 6. Type-II support vertices approximate every prescribed disk point uniformly

Canonical Section 80 gives translated Hausdorff convergence

```math
D^{-1}F\to B(0,1/2).
```

Let the Hausdorff error be `epsilon_D->0`. For any unit vector `u`, choose a vertex `x_D(u)` of `D^{-1}F` maximizing `u dot x`. Since support functions converge uniformly,

```math
u\cdot x_D(u)\ge {1\over2}-\epsilon_D.
```

Also

```math
|x_D(u)|\le {1\over2}+\epsilon_D.
```

Writing `x_D(u)=(u dot x_D)u+x_D^perp` gives

```math
|x_D^perp|^2
\le({1\over2}+\epsilon_D)^2-({1\over2}-\epsilon_D)^2
=2\epsilon_D.
```

Thus

```math
\sup_{u\in S^1}|x_D(u)-u/2|\to0.
```

Every vertex of `F` is loaded and occurs on the outer walk. Applying this to three directions separated by `2pi/3` gives three distinct cyclic outer-walk cuts for all sufficiently large `D`. Their triangle perimeter is

```math
(3\sqrt3/2+o(1))D
```

uniformly in the common rotation, and their chord-host triple is uniformly `o(1)` from a rotated equilateral host triple.

Because support width changes by at most twice the maximum host displacement, the induced return error is `o(1)` per unit area. Since `A_4=O(D^2)`, the total return error is `o(D^2)`.

The finite-net phrase in the research note is therefore conservative: uniform support convergence allows one simply to choose an ideal maximizing rotation for each finite `D` and then realize its three support directions by actual vertices.

## 7. The disk equality is real, not a numerical coincidence

Canonical Type-II gives

```math
A_4/D^2\to\pi/4,
\qquad
\operatorname{per}(F)/D\to\pi.
```

The actual equilateral-support cuts give

```math
\Pi_3/D\to3\sqrt3/2.
```

Thus the leading lower demand is

```math
{\pi\over4}\left(4-{6\sqrt3\over\pi}\right)
=\pi-{3\sqrt3\over2},
```

while the leading convex-perimeter route budget is the same

```math
\pi-{3\sqrt3\over2}.
```

There is no positive constant gap to exploit. Any claimed immediate C-II contradiction from this averaging would be false.

## 8. Surviving obligation after this audit

The theorem is useful because it removes harmonic-cell multiplicity and phase orientation simultaneously. It does **not** close the full-core branch. The remaining full-core task is now genuinely first-order/boundary-order:

```math
2D(f+\Xi_F-\omega_F)
\ge
(c_{eq}-o(1))A_4
-D(\operatorname{per}(F)-\Pi_3).
```

One must prove that the left-side defect currency is too small, or that a positive amount of it enables a strict source-preserving diameter decrease. A valid proof must retain the separate macroscopic inactive-container branch.

**Audit verdict:** PASS at proof-only scope. The authoritative state remains audit.44; C-II remains open.
