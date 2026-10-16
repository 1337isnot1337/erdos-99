<!-- theorem-state: {"artifact_id":"ART-CF6FD99D2EAE","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Hostile audit — Target C loaded-hull/train floor

**Date:** 2026-09-12  
**Reviewed:** `docs/reports/target_c_typeii_qk_train_hull_gap_2026-09-12.md`.  
**Disposition:** the advertised (1.9046256ldots) floor is **rejected**; a corrected
proof-only floor (1.6375621ldots) survives.

## 1. The exact algebraic failure

The report defines (t=(q-k)/D), (\Delta_2=\pi/(2\sqrt3)), and uses the valid
finite/asymptotic inequalities

\[
Q/D\le 2t-\pi+o(1),
\qquad
f/D\ge \sqrt{\Delta_2}-t/2+o(1)
\]

in the regime (t<2\sqrt{\Delta_2}), together with (f\le Q).  Therefore

\[
\sqrt{\Delta_2}-t/2\le 2t-\pi,
\]

which rearranges to

\[
\pi+\sqrt{\Delta_2}\le {5\over2}t,
\qquad
\boxed{t\ge {2\over5}(\pi+\sqrt{\Delta_2})}.
\]

The source report instead states

\[
t\ge {2\pi+2\sqrt{\Delta_2}\over3},
\]

which is not the solution of the displayed inequality.  Numerically,

\[
{2\over5}(\pi+\sqrt{\Delta_2})=1.6375621841815\ldots,
\qquad
2\sqrt{\Delta_2}=1.9046256137279\ldots.
\]

The claimed comparison that the former exceeds the latter is also false.

**Verdict:** the implication to (TQ.9) is invalid.

## 2. Corrected surviving floor

The same premises do yield the weaker floor.  Take any subsequential limit (t) of
((q-k)/D).  If (t\ge2\sqrt{\Delta_2}), then certainly

\[
t\ge {2\over5}(\pi+\sqrt{\Delta_2}).
\]

If (t<2\sqrt{\Delta_2}), the preceding valid inequalities and (f\le Q) give

\[
t\ge {2\over5}(\pi+\sqrt{\Delta_2}).
\]

Thus the corrected candidate conclusion is

\[
\boxed{
\liminf_{D\to\infty}{q-k\over D}
\ge {2\over5}\left(\pi+\sqrt{\frac\pi{2\sqrt3}}\right)
=1.6375621841815\ldots .
}
\]

This is stronger than the previously canonical direct floor (pi/2), provided the
source report’s two input inequalities are used in their stated Type-II scope.  It
does not imply the rejected (1.9046ldots) value.

## 3. What remains valid and what is not promoted

- The finite identities (Q=2(q-k)-b), (b\ge\operatorname{per}(F)), and (f\le Q)
  are not challenged here.
- The Type-II limits for (operatorname{per}(F)/D) and (R_4/D^2) are used only in
  the source report’s stated scope.
- No claim about (q/D\to\pi), separate (k/D), or aggregate detour is obtained.
- The corrected floor is proof-only and not a theorem-state promotion.
- The macroscopic inactive-container branch remains untouched.

## Final classification

**Regression plus corrected proved candidate.** The numerical (1.9046256ldots)
claim and its algebraic derivation are rejected. The exact same argument supports only
the (1.637562184ldots) floor, which is genuine but does not close C-II.
