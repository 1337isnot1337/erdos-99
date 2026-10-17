> Generated reading edition · [exact source](../../../docs/reports/target_c_outer_train_rank_groemer_bank_synthesis_2026-10-05.md) · source SHA-256 `9fa8f6cf50dc90451b20464569632420f6cb116944f74af05582ce8b45d4cdbb`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-10D6BFB2C2DA","canonical":true,"claim_ids":["C-OUTER-TRAIN-DETERMINATION"],"claim_statuses":{"C-OUTER-TRAIN-DETERMINATION":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C — outer-train determination removes the nonunit-hull escape

**Date:** 2026-10-05
**Starting main:** f539af073a691c13327a0a7fef3c746fb7704e5f
**Preceding checkpoint:** 9d08f73f4e2374e286cb98b7f35e5d5587b9607c
**State:** 2026-09-14.audit.51
**Classification:** the finite outer-train determination theorem is canonical in `2026-10-05.audit.53` as `C-OUTER-TRAIN-DETERMINATION`; the report's later historical `R_F=o(D)` synthesis is not separately promoted. **LEVEL I STATUS: STILL OPEN. C-II REMAINS OPEN.**

## 1. The exact change in the frontier

Mixed rigidity makes contact flexes determined by outer-train angular rates.
There must be at least $`q-k+\sigma_C`$ outer-ended trains. The new Groemer
depletion therefore spends at least $`m_B-k+\sigma_C`$ extra trains, cancelling
$`5m_B`$ from the strongest physical inequality.

The cancellation applies to the conditional branch proved in
[the outer-pocket phase-depletion report](target_c_outer_pocket_groemer_phase_depletion_2026-10-05.md):

```math
R_F=o(D),\qquad
\lim_{L\to\infty}\limsup_{D\to\infty}
 D^{-1}\sum_{\ell_j>L}\ell_j=0.
\tag{H}
```

The finite rank theorem needs neither (H) nor Type-II asymptotics. The
synthesis also forces at least $`sD-o(D)`$ exceptional faces having **no
outer contact-edge occurrence**. Those faces are entirely unloaded. It
does not activate their near-contacts or construct a strict competitor.

## 2. Finite core and angular coordinates

Use the connected nonisolated positive-contact core of a canonical
triangle-free C-II source. Retain all isolates in the full source. Let
$`v,e,h,q,k=d_H+s_Z,f,T`$ have their canonical meanings and put

```math
\sigma_C=\dim\ker R_C^T=e-\operatorname{rank}R_C.
```

This is pure-contact row-nullity, distinct from rhombic train excess
$`\sigma_R`$. The canonical finite identities are

```math
e+h=2v-2+s_Z,\quad h=q-d_H,\quad T=q-k+2f.
\tag{2.1}
```

For a contact flex, the relative velocity on an oriented unit edge $`ij`$
has a unique form

```math
u_j-u_i=\omega_{ij}J(p_j-p_i).
\tag{2.2}
```

Differentiating closure on a strict unit rhombus forces opposite rates to
agree: its two side directions are independent. There is one rate per
stopped train, including singletons. No finite integration is asserted.

Angular coordinates and the exact face-closure corank identity were already
proved in the audited-working, noncanonical
[Sections 156--157 module](../targets/target-c/156-157-face-closure-and-outer-train-bracing-audited.md).
The finite determination argument below and its use with the new depletion
are additional steps, proved directly from canonical
[Section 57 mixed rigidity](../targets/target-c/57-zr-zf-rigidity-audit.md)
and actual occurrence-counted train geometry.

## 3. Outer-ended trains determine a contact flex

Let $`\mathcal O`$ be all trains having an old outer-contact-walk end.

**Theorem OR.1.** On the canonical core,

```math
\boxed{|\mathcal O|\ge q-k+\sigma_C.}
\tag{3.1}
```

### Proof

Restrict the angular-rate map to $`\mathcal O`$. Its kernel consists
exactly of translations. If these rates vanish, every outer contact-edge
occurrence has zero relative velocity. The entire occurrence-counted walk
therefore has one common velocity. Every loaded vertex has a distinguished
occurrence on this walk, so all loaded velocities agree.

Subtract that velocity. All loaded velocities are now zero, hence all
actual diameter first variations vanish. The original velocity preserves
all actual contacts to first order, so it is a mixed bar flex. Section 57
makes it Euclidean. It vanishes at two distinct loaded vertices, hence is
zero. This proves injection modulo translations, with bridges and repeated
outer occurrences included.

The domain dimension is

```math
\dim(\ker R_C/\mathrm{Trans})
=2v-e+\sigma_C-2
=h-s_Z+\sigma_C=q-k+\sigma_C.
```

Injection into $`\mathbb R^{|\mathcal O|}`$ proves (3.1). Rotation has not
been removed: it has a nonzero constant train-rate vector. Subtracting
three Euclidean dimensions would lose one without justification. □

Isolates are absent from the matrix argument and remain in the source.
There is no affine-kernel or rigidity statement on them.

## 4. Deplete every bounded-degree exceptional face touching the outer walk

Fix $`K\ge5`$. Let $`\mathcal B_K`$ contain all physical exceptional faces
of degree at most $`K`$ having **any** outer-contact-edge occurrence.
They need not touch a unit loaded-hull side. Put $`N_K=|\mathcal B_K|`$.
Let $`\mathcal D_K`$ be every train with an outer end or an end on
$`\mathcal B_K`$.

**Theorem OR.2.** Under (H), $`\mathcal D_K`$ has $`o(D^2)`$ aggregate
rhombus incidence, for every fixed $`K`$.

### Proof: phase propagation through two chambers

Choose one outer contact occurrence per selected face. Distinct faces
choose distinct occurrences. Apply OP.1 from the preceding report to the
face with this unit edge as distinguished chord. Its other boundary edges
are a unit path. Selected-face residuals sum to at most $`R_F`$; all but
$`o(D)`$ selected faces have every boundary phase within any fixed
$`\eta>0`$ of their chosen edge phase.

That edge either is an actual unit hull side or belongs on its outer side
to one hull-augmented pocket. For pockets of length at most a fixed $`L`$,
OP.1 puts its phase within $`\eta`$ of the added hull-side phase, apart
from $`o(D)`$ bad pocket occurrences. One pocket anchors at most $`L`$
chosen faces; each contributes at most $`K`$ terminal occurrences. Thus a
fixed reduced phase bin has at most $`O(KL\eta D)+o_{K,L,\eta}(D)`$
selected members from these pockets and direct hull anchors. Long pockets
contribute at most

```math
K\sum_{\ell_j>L}\ell_j
```

additional possible terminal occurrences. The uniform hull-side normal
estimate, the simple crossing graph, and Section-69 phase-bin deletion now
give the same incidence estimate as OP.2.

Take limits in order: $`D\to\infty`$; $`\eta\downarrow0`$ with $`K,L`$
fixed; then $`L\to\infty`$. The face cutoff $`K`$ stays fixed. Pocket reuse
is charged to actual contact occurrences; distinct physical faces are
not assumed to have distinct pocket anchors. □

## 5. Exact face rank adds charge

Let $`C_B`$ be the two-coordinate vector-closure rows of the selected
faces on actual train columns, and set $`r_B=\operatorname{rank}C_B`$.
Every used column lies in $`\mathcal D_K`$.

The full closure matrix has rank $`2f-\sigma_C`$. Indeed bounded face
boundaries span the real cycle space, and rhombus closures already hold
by (2.2). Assigning train rates and imposing exceptional-face closures
gives exactly $`\ker R_C/\mathrm{Trans}`$. Its dimension above and
$`T=q-k+2f`$ prove this rank identity. A row dependence on $`C_B`$ extends
by zero to the full matrix, hence

```math
r_B\ge2N_K-\sigma_C.
\tag{5.1}
```

Also define the finite geometric weight

```math
w_B=\sum_{F\in\mathcal B_K}
\dim\operatorname{span}\{Jr_e:
 e\text{ is an outer contact occurrence of }F\}.
\tag{5.2}
```

Each such edge is a singleton train, with an outer face and an exceptional
face on its two sides. Its column occurs in only that bounded face's rows.
The submatrix on these columns is block diagonal, so $`r_B\ge w_B`$.
Collinear boundary edges are allowed: a local rank is one or two, not
the number of its outer edges.

The contact-flex map into $`\mathcal D_K`$ is injective modulo
translations, since the family contains $`\mathcal O`$. Its image satisfies
all $`r_B`$ independent selected-face equations. Therefore

```math
\boxed{|\mathcal D_K|\ge q-k+\sigma_C+r_B
\ge q-k+\max\{2N_K,\sigma_C+w_B\}.}
\tag{5.3}
```

This is a simultaneous rank estimate. It does not count separate feasible
swaps or assume their shores are compatible.

## 6. Substitute immediately: the $`m_B`$ term cancels

The #699 good-hull family $`G_D`$ lies in $`\mathcal D_K`$ and has
$`|G_D|=q-m_B-d_D`$, where $`0\le d_D\le2`$. The additional depleted
bank $`z_K=|\mathcal D_K|-|G_D|`$ obeys

```math
z_K\ge m_B-k+d_D+\sigma_C+r_B.
\tag{6.1}
```

It is nonnegative whether or not this lower bound is positive. Let $`S_U`$
count singleton trains outside $`\mathcal D_K`$; they can also be deleted
at zero rhombus cost, once each.

Use the finite #699 synthesis, including $`5d_D`$, and Mantel after
deleting $`\mathcal D_K`$ and those singletons. Substituting (6.1)
cancels both $`5m_B`$ and $`5d_D`$:

```math
\boxed{
4S+2\sigma_R\ge2(\pi+s)D
 +5(\sigma_C+r_B+S_U)
 +2(Q-f)+2(b-P_F)-o(D).
}
\tag{6.2}
```

Thus $`5\max\{2N_K,\sigma_C+w_B\}`$ is a valid additional payment.
No small-$`m_B`$, terminality $`q/D\to\pi`$, or positive individual
KKT coefficient floor is assumed. This closes the **nonunit-hull escape
mechanism** in branch (H); it does not close that branch itself. Large
singleton or rhombic train excess remains possible.

## 7. At least $`sD`$ entirely unloaded interior exceptional faces

The weighted inequality in Section 6 and the face-bank count are algebraic
forms of the same exact identity, since `4S+2sigma_R=4T-8sqrt(R_4)`.
After substituting the face and outer-walk ledgers, Section 6 is equivalent
to `2f>=2sD+sigma_C+r_B+S_U-o(D)`. They cannot be counted as independent
payments. A further structural or phase argument is needed for closure.

The retained train bank has size at most

```math
T-|\mathcal D_K|
\le2f-\sigma_C-r_B\le2(f-N_K).
\tag{7.1}
```

OR.2 and Mantel therefore imply

```math
\boxed{f-N_K\ge(s-o(1))D.}
\tag{7.2}
```

Let $`f_{\rm in}`$ count exceptional faces with no outer contact-edge
occurrence. Every other unselected face has degree greater than $`K`$.
Since $`Q\le P_F=(\pi+o(1))D`$, the number of such faces is at most
$`Q/(K-3)`$. For each fixed $`K`$,

```math
\liminf f_{\rm in}/D\ge s-\pi/(K-3).
```

Taking the supremum over fixed $`K`$ gives

```math
\boxed{\liminf f_{\rm in}/D\ge s.}
\tag{7.3}
```

These faces have no loaded vertices. At a loaded extreme vertex, all
contact directions lie in its tangent cone of width less than $`\pi`$.
Triangle-freeness makes consecutive directions differ by more than
$`\pi/3`$, so contact degree is at most three. The two extreme contact
rays are outer-face incidences. Each bounded-face sector among at most
three rays uses at least one such ray, hence an outer contact edge.
Every bounded face incident to a loaded vertex is therefore outer-edge
incident. This proves the entirely unloaded scope in (7.3).

This enlarges the face bank available to Groemer/activation arguments.
It does not itself activate a hidden pair or supply another independent
train charge.

## 8. Hostile checks and exact surviving obligation

The [exact verifier](../../../research/verify_target_c_outer_train_rank_groemer_bank_2026_10_05.py)
uses rational unit-separated sources with a genuine missing contact and
a convex exceptional hexagon. It checks every actual pair, positive pinned
equilibrium, contact rank, train decomposition, outer-rate determination,
and the sharp marked-face rank payment. The assigned pins include collinear
boundary vertices and are not all actual diameter endpoints. They certify neither canonical-source
existence nor global optimality.

The proofs retain bridge occurrences, distinguish translation from
rotation, allow dependent contact rows, use actual singleton columns for
unique-anchor rank, and charge pocket reuse by occurrences. They make no
local descent or full-source ZR claim.

The surviving branches are positive $`R_F/D`$, persistent outer-pocket
occurrence tails, and the singleton/rhombic-excess burden in (6.2), with
the forced unloaded interior face bank. The macroscopic inactive-container
branch remains separate and open. The original sufficiently-large,
every-global-minimizer quantifier remains unsettled.
