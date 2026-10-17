# Hostile audit - adaptive strict-safe saturation after arbitrary deletion

**Date:** 2026-09-15  
**Reviewed:** `research/target_c_adaptive_safe_region_saturation_2026-09-15.md`  
**Disposition:** **PASS.**  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The candidate generalizes the older isolate-only safe-area barrier to an arbitrary
finite deletion set. The proof is short, but the quantifiers matter because the new
claim is used to rule out adaptive boundary-guard deletion.

---

## 1. Translation averaging is used in the correct direction

For the triangular lattice scaled by `lambda>1`, the expected number of translated
lattice points in a measurable bounded set `S` is

\[
\operatorname{area}(S)/(a_0\lambda^2).
\]

If this expectation is strictly above an integer `N-1`, some translate contains at
least `N` points. The proof never reverses an upper packing inequality and never claims
that an area upper bound determines non-strict capacity.

**Verdict:** PASS.

---

## 2. Case `E_C(R)=emptyset` really means every deleted point is contact-isolated

`E_C(R)` contains every old unit-contact edge incident to `R`. Hence if it is empty, no
vertex of `R` is incident to any unit contact, including an edge internal to `R`.
Every member of `R` is therefore contact-isolated.

The theorem separately assumes that the whole source has at least one unit contact, so
one may choose a contact-active vertex `v` outside `R`. If `v` had a contact neighbor in
`R`, that edge would belong to `E_C(R)`, impossible. Thus deleting `R union {v}` removes
at least one old contact and the points of `R` contribute none.

**Verdict:** PASS.

---

## 3. The replacement is genuinely a triangle-free global minimizer

The inserted lattice has spacing `lambda>1`, and strict safety gives distance greater
than one from every retained old source point. Therefore the inserted points create no
unit contact at all. Every retained old-old pair was already feasible and triangle-free.
So the comparison source is automatically triangle-free.

All inserted points lie in `int K`. For every `x in K` and `y in int K`,

\[
|x-y|<D,
\]

while retained old-old distances remain at most `D`. Hence the comparison source has
diameter at most `D(n)`. Global minimality upgrades this to equality, making the
contact-minimal lexicographic normalization applicable.

No assumption that the deleted vertices were diameter-inactive is needed.

**Verdict:** PASS.

---

## 4. The one-cell improvement when `R` already removes a contact is correct

If `R` touches an old unit contact, the proof replaces `|R|` deleted points by exactly
`|R|` strict lattice points. Therefore it only needs a lattice translate containing
`|R|` points, which follows from expectation greater than `|R|-1`.

This yields

\[
\operatorname{area}S\le a_0(|R|-1).
\]

The singleton case is especially sharp: if `R={v}` and `v` is contact-active, every
positive-area strict-safe region would contain at least one possible strict replacement
point and would contradict contact minimality.

**Verdict:** PASS.

---

## 5. The deleted-contact covering corollary is exact

For contact-active `v`, suppose one point `y in int K` were farther than one from every
other source point. The finitely many strict inequalities persist on a small open ball
around `y` contained in `int K`. That produces a positive-area strict-safe set relative
to `{v}`, contradicting the singleton case.

Hence

\[
int K\subseteq\bigcup_{a\ne v}\overline B(a,1).
\]

This is a pointwise covering statement, not an almost-everywhere consequence smuggled
out of an area estimate.

**Verdict:** PASS.

---

## 6. Boundary-guard application has the right scope

If `Z` is contact-isolated and `B` is a nonempty set of old contact-wall guard vertices,
then `Z cap B=emptyset` and `R=Z union B` certainly removes at least one old contact.
Any enlarged region that is strictly farther than one from every retained source point
therefore obeys

\[
\operatorname{area}S\le a_0(z+|B|-1).
\]

This does **not** say that a non-strict packing of `z+|B|` or more points is impossible.
Such a packing can sit exactly on unit constraints and is precisely the remaining
Type-I mechanism. The candidate states this limitation explicitly.

**Verdict:** PASS.

---

## 7. No conflict with the canonical multi-vertex exchange theorem

The canonical inactive-exchange theorem already says that protected finite exchanges
must repay lost contacts, and when a diameter pair is lost equality in contact count is
also forbidden by the second lexicographic normalization.

The present result is a different projection of that lexicographic obstruction: it
combines strict exchange with lattice translation averaging to bound the area of **any
strict-safe region after the deletion set has been chosen**. It does not duplicate or
weaken the exact non-strict contact-debt theorem.

**Final verdict:** **PASS.** Adaptive deletion of contact-wall guards cannot rescue a
strict-safe area-averaging proof of the Type-I diameter-cover capacity. Exact unit
contacts remain the only live packing mechanism in that route.
