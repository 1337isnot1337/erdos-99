# Target C — all-regime fan/train scalar floor (retracted)

**Date:** 2026-09-12  
**Status:** rejected density-floor derivation; finite pair lemma retained.
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The bounded-face fan pair budget was claimed to combine with the audited all-Type-II
stopped-train floor, not only the stronger two-half-disk floor. The resulting bound
is withdrawn below; the center-wrapping branch remains open.

**Retraction.** The displayed floor and the convex elimination are invalid because
the finite fan term `20f` is only `O(D)`, while `T(T-1)-2R` is `O(D^2)`. Dividing by
`D^2` yields no `20(f/D)` term. See the normalization correction report.

\[
\boxed{
\liminf_{D\to\infty}{q-k\over D}
\ge t_{\rm ar}=2.3036394677\ldots .
}
\]

Here

\[
\Delta_2={\pi\over2\sqrt3},\qquad s=\sqrt{\Delta_2},
\]

and

\[
t_{\rm ar}=\sqrt{8s^2+160s+100}-4s-10.
\]

The two-half-disk branch does not acquire the displayed improvement from this report,
and no lower-density gap is filled for center-wrapping configurations. The high-
density Type-II region and Type-I inactive-container branch remain open.

## 1. Implication chain

```text
bounded-face fan pair budget
  + all-Type-II stopped-train floor
  + Type-II loaded-hull perimeter upper bound
  -> attempted convex endpoint obstruction (invalid after normalization correction).
```

The proof does not assume `b/D=pi` or use the two-half-disk decomposition.

## 2. Normalized inputs

Along a Type-II survivor subsequence write

\[
t={q-k\over D},\qquad \kappa={k\over D},\qquad
\phi={f\over D},\qquad {T\over D}=t+2\phi.
\]

The audited all-Type-II stopped-train floor gives

\[
{T-q/2\over D}\ge2s-o(1).
\tag{2.1}
\]

Since `q/D=t+\kappa`, this implies

\[
\phi\ge s-{t\over4}+{\kappa\over4}-o(1).
\tag{2.2}
\]

The canonical Type-II outer ledger and `f<=Q` give

\[
\phi\le2t-\pi+o(1).
\tag{2.3}
\]

Finally, the audited bounded-face fan pair budget gives

\[
20\phi\le(t+2\phi)^2-2\Delta_2+o(1).
\tag{2.4}
\]

## 3. Convex elimination

Set

\[
a_\kappa(t)=s-{t\over4}+{\kappa\over4},
\qquad b(t)=2t-\pi,
\]

and

\[
H_t(\phi)=(t+2\phi)^2-20\phi-2\Delta_2.
\]

If the interval `[a_\kappa(t),b(t)]` is empty, the train and outer ledgers already
contradict. Otherwise `0<=\kappa<=\pi-t+o(1)` gives the limiting admissibility bound

\[
t\ge t_0:={4(s+\pi)\over9}=1.8195135379\ldots.
\tag{3.1}
\]

At the lower endpoint,

\[
t+2a_\kappa(t)={t\over2}+2s+{\kappa\over2}
\le {\pi\over2}+2s+o(1)<5.
\]

Thus `H_t(a_\kappa(t))` decreases as `\kappa` increases, and

\[
H_t(a_\kappa(t))
\le H_t(a_0(t)),
\qquad a_0(t)=s-{t\over4}.
\tag{3.2}
\]

The right-hand side is strictly increasing in `t` and vanishes at

\[
t=t_{\rm ar}=\sqrt{8s^2+160s+100}-4s-10.
\tag{3.3}
\]

It is therefore negative for `t<t_ar`.

At the upper endpoint,

\[
H_t(b(t))=(5t-2\pi)^2-40t+20\pi-2\Delta_2=:J(t).
\tag{3.4}
\]

`J` is convex. Certified evaluation gives `J(t_0)<-3.84` and
`J(t_ar)<-3.72`, so `J(t)<0` on `[t_0,t_ar]`.

For any limiting `t<t_ar`, both endpoint values of the convex function `H_t` are
strictly negative. Hence `H_t(\phi)<0` throughout the admissible interval, contrary
to (2.4). The `o(1)` terms are harmless after fixing a strict limiting gap.

Consequently `liminf(q-k)/D>=t_ar`.

## 4. Scope

This retracted candidate used the audited strict stopped-train phase gap's weaker base
inequality, the bounded-face fan pair theorem, and the canonical Type-II outer
estimate. It supplies no all-Type-II density floor or source-level descent.

Contact-isolated source points remain retained and are absent only from the train
graph, as in the imported fan theorem.

**Classification:** rejected density-floor derivation; finite fan pair lemma retained.
