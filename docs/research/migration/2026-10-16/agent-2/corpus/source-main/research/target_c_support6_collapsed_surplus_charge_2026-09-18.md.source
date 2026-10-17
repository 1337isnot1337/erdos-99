# Target C-II — support-six exclusion plus host-anchor charge improves corank

**Date:** 2026-09-18  
**Status:** proof-only propagation corollary; theorem-state authority unchanged
**Scope:** degree-pure collapsed support-six one-anchor components in the audited
one-anchor residual normal form  
**Certificate:** `research/verify_target_c_support6_collapsed_surplus_charge_2026_09_18.py`  
**Classification:** proved candidate awaiting promotion audit; C-II remains open

The collapsed support-six endpoint cannot be treated as a free replacement for the
noncollapsed support-six endpoint. The exact row-dependency input needed here is
already proved by the audited host-anchor theorem: a bounded-face component whose
outer train directions span one projective direction consumes one unit of the
pure-contact closure corank. The new step in this note is to combine that existing
charge with the completed noncollapsed support-six exclusions and solve the resulting
finite component-count inequality.

Let `c` be the number of pairwise disjoint degree-pure collapsed support-six blocks,
and retain the one-anchor notation `n_0,n_1,n_2` and

\[
\sigma_C=\dim\ker C_{\rm face}^{T}.
\]

Then

\[
\boxed{c\le \sigma_C\le s_Z.}
\tag{1}
\]

Combining this with the already audited exclusion of support five and of all
**noncollapsed** support-six blocks gives the finite implicit bound

\[
\boxed{
\sigma_C\le 2n_0+n_2+\frac{n_1-c}{7}+\frac c6
=2n_0+n_2+\frac{n_1}{7}+\frac c{42}.
}
\tag{2}
\]

Eliminating `c` with (1) yields the unconditional support-six-refined estimate

\[
\boxed{
\sigma_C\le \frac{42}{41}\left(2n_0+n_2+\frac{n_1}{7}\right).
}
\tag{3}
\]

This is weaker than the conditional `n_1/7` estimate when `c=0`, but improves the
old unrestricted `n_1/6` coefficient without assuming that the collapsed branch is
globally absent.

There is also an exact zero-surplus corollary:

\[
s_Z=0\quad\Longrightarrow\quad c=0,
\]

so the degree-pure support-six endpoint is excluded entirely in that branch.  More
generally, along any sequence with `s_Z=o(D)`, the collapsed support-six population is
`o(D)` and the `n_1/7` coefficient holds up to an `o(D)` error.

## 1. Specialization of the audited host-anchor theorem

The input is the audited theorem
`research/target_c_face_host_anchor_rank_2026-09-12.md`, specifically (HA.1).
In the degree-pure collapsed support-six reduction, the six pentagon faces form one
bounded-face train component and all six outside anchors are projectively parallel.
Thus its anchor span has dimension one, and (HA.1) supplies one independent
closure-row dependency. Pairwise disjoint degree-pure blocks supply independent
dependencies by disjoint row support. Hence

\[
c\le\sigma_C\le s_Z.
\tag{4}
\]

For completeness, the exact local row identity behind this specialization is recorded
below; it is not claimed as a new host-anchor theorem.

Use the degree-pure support-six notation.  The six residual faces are indexed by
`0,...,5`, their relation graph is `K_6` minus a perfect matching, and each has one
outside train.  Write the oriented outside side at face `i` as

\[
a_i=s_i e_1,
\qquad s_i\in\{+1,-1\},
\]

with the collapsed branch giving six projectively parallel anchors.  The twelve
internal relation trains occur once at each of their two endpoint faces, with
opposite oriented unit vectors.  The six outside trains occur once in the block.

For a train-angle rate `\omega`, an oriented unit side `u` has derivative `\omega Ju`.
Take the sum of the **first-coordinate** rows of the six linearized face-closure
equations.  Every internal relation train contributes

\[
e_1\cdot(\omega Ju)+e_1\cdot(-\omega Ju)=0,
\]

because its two endpoint occurrences have opposite vectors.  An outside train
contributes

\[
e_1\cdot(\omega J(s_i e_1))=0,
\]

because the common anchor direction is `e_1`.  Therefore the row vector which is `1`
on the first-coordinate row of each of these six faces and `0` elsewhere satisfies

\[
\lambda^T C_{\rm face}=0.
\tag{5}
\]

This identity is exact.  It uses neither the certified local numerical root nor the
local turn inequalities.  It is a dependency in the global matrix because a
degree-pure block has no residual train column leaving these six faces.

For pairwise disjoint degree-pure collapsed blocks, the corresponding `\lambda`
vectors have disjoint row supports and are linearly independent. This is the direct
support-six realization of (HA.1); the audited mixed-rigidity closure theorem gives
`\sigma_C\le s_Z`, proving (1).

The dependency is only one-dimensional without an additional constraint on the six
outside angular rates.  In particular, the argument does not claim that the collapsed
local family is globally impossible, nor does it silently impose a common outer
rotation on the six distinct outside trains.

Combining (4) with `\sigma_C\le s_Z` also proves the zero-surplus corollary directly:
one collapsed block would give `1\le\sigma_C\le0`, an impossibility.  This is a
genuine exclusion of collapsed support six in the exact `s_Z=0` branch, not a
regularity or asymptotic argument.

## 2. New support-six corank bookkeeping

The audited one-anchor transpose-kernel argument gives at most one scalar mode per
nonzero relation component.  Support five is excluded.  A noncollapsed support-six
component is excluded by the current exact H7/H6/H5 chain, while a collapsed
support-six component has size six.  Thus the one-anchor fiber contribution is at most

\[
\frac{n_1-c}{7}+\frac c6.
\]

The `n_0` and `n_2` face blocks retain their prior dimension bounds `2n_0+n_2`.
This proves (2).  Since `c\le\sigma_C`,

\[
\sigma_C\le 2n_0+n_2+\frac{n_1}{7}+\frac{\sigma_C}{42},
\]

which is exactly (3).

## 3. Terminal propagation

Put

\[
E_U=a_F+\frac{x_A}{2}+\frac{n_0+n_2}{2},
\qquad f=a_F+n_0+n_1+n_2.
\]

The same elementary comparison used in the existing conditional support-six note gives

\[
2n_0+n_2+\frac{n_1}{7}
\le \frac f7+\frac{26}{7}E_U.
\]

Therefore (3) implies the explicit form

\[
\boxed{
\sigma_C\le \frac6{41}f+\frac{156}{41}E_U.
}
\tag{5}
\]

At the current terminal pair-shield floor `E_U=o(D)`, the audited bound
`limsup f/D\le0.7791330454911659` gives

\[
\boxed{
\limsup\frac{\sigma_C}{D}
\le \frac6{41}(0.7791330454911659)
<0.114019471.
}
\tag{6}
\]

The old unrestricted support-six estimate gives `f/6`, approximately `0.129855508`
at the same floor.  The conditional full exclusion gives the sharper `f/7`, but (6)
is unconditional with respect to the collapsed branch.

## 4. Dependency chain and limits

\[
\text{collapsed support-six block}
\to \text{exact closure-row dependency}
\to c\le\sigma_C\le s_Z
\to \text{support-six-refined corank bound (3)}.
\]

This does not close C-II.  It supplies a new charge on the only remaining local
support-six mechanism and reduces the live terminal corank budget.  A closure of the
collapsed branch still requires a global train-corridor, source-embedding, or actual
diameter/KKT incompatibility theorem.  The certified local realization remains a
binding regression against purely local exclusion.

**Disposition:** exact collapsed-block surplus charge and unconditional corank
improvement; no theorem-state change.
