# Target C-II — optimize the high-t singleton/full-flower split at the train-network level

**Date:** 2026-09-15
**Status:** proof-only high-t structural strengthening
**Scope:** canonical full-core/no-macroscopic-container Type-II train-measure branch, throughout the positive uniform pentagon-sea range
**Dependencies:** uniform pentagon sea; exact inequality `P_5-F_5^{full}<=2S`; exact terminal bound `N_full>=5F_5^{full}/2`; modern train-slack identity
**Certificate:** `research/verify_target_c_singleton_or_flower_train_network.py`
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The existing singleton/full-flower theorem balances the number `S` of singleton stopped trains against the number `F_5^{full}` of fully rhombic pentagons. For network arguments that is not the natural balance. A fully rhombic pentagon has five non-singleton train-terminal occurrences, and one complete stopped train has at most two terminal occurrences. Hence

\[
N_{full}\ge {5\over2}F_5^{full}.
\]

Combining this with

\[
P_5-F_5^{full}\le2S
\]

gives a sharper train-level dichotomy.

Let

\[
p_5(T)=C_{707}+\pi-{5T\over2},
\qquad
C_{707}=2\sqrt{\Delta_2}+0.007707,
\qquad
\Delta_2={\pi\over2\sqrt3}.
\]

For every fixed endpoint `t<=T` in the positive pentagon-sea range,

\[
P_5\ge(p_5(T)-o(1))D.
\]

Choose

\[
a(T):={5\over12}p_5(T).
\]

If `S>=a(T)D-o(D)`, the singleton-network branch holds. Otherwise

\[
F_5^{full}
\ge P_5-2S
>\left(p_5(T)-2a(T)-o(1)\right)D
=\left({p_5(T)\over6}-o(1)\right)D,
\]

and therefore

\[
N_{full}
\ge {5\over2}F_5^{full}
>\left({5p_5(T)\over12}-o(1)\right)D
=\left(a(T)-o(1)\right)D.
\]

Thus

\[
\boxed{
\max\{S,N_{full}\}
\ge\left({5\over12}p_5(T)-o(1)\right)D.
}
\]

This is a strict improvement over balancing `S` directly against `F_5^{full}`, which gives only `p_5(T)/3` at the level of the two branch populations. The gain factor is

\[
{5/12\over1/3}={5\over4}.
\]

Representative certified rows are:

| endpoint `T` | `P_5/D` lower | `max(S,N_full)/D` lower |
|---:|---:|---:|
| 1.88 | 0.3539 | 0.147 |
| 1.90 | 0.3039 | 0.126 |
| 1.92 | 0.2539 | 0.105 |
| 1.96 | 0.1539 | 0.064 |
| 2.00 | 0.0539 | 0.022 |
| 2.01 | 0.0289 | 0.012 |
| 2.02 | 0.0039 | 0.0016 |

The conditional full-flower branch also has a stronger rhombic-train slack than under the old balanced cutoff. Since `S<a(T)D+o(D)` and `sigma_R=2tau_D-2S` with `tau_D>=(tau_0-o(1))D`, `tau_0=0.7467921`,

\[
\boxed{
\sigma_R>2\left(\tau_0-{5p_5(T)\over12}\right)D-o(D).
}
\]

The exact Mantel identity then gives the corresponding quadratic crossing deficit.

This theorem does not close either branch. Its use is to put the high-t alternative in the correct network currency: either linearly many one-edge stopped trains, or equally many distinct non-singleton trains ending on fully rhombic empty pentagons. Any subsequent bracing, closure-rank, endpoint-order, or train-capacity theorem can now be applied to populations of the same object type.

**Disposition:** proved proof-only 5/4 strengthening of the singleton/full-flower high-t network dichotomy. C-II and Level I remain open.
