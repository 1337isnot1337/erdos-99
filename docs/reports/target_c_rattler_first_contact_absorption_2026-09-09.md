<!-- theorem-state: {"artifact_id":"ART-BA8767277F89","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — finite first-contact absorption of C65 rattlers

**Date:** 2026-09-09  
**Repository base:** `be9cbfb78cbda059fb4c2581118b236729cfad84`  
**Run type:** exact finite reconfiguration theorem  
**Target:** Target C C-II / residual rattler population  
**Depends on:** C65 full diameter visibility and the existence of a fixed core diameter pair  
**External web search:** not used  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

C65 proves that in the lexicographically normalized C-II source every point outside the positive contact core is a fully inactive contact-isolated rattler. This report proves a finite global statement that is stronger than the local product germ but deliberately weaker than force visibility:

> every hypothetical triangle-free C-II counterexample has another triangle-free global minimizer of the same cardinality and same diameter in which **every source point has at least one unit contact**, while the original positive core is held fixed pointwise.

The newly created contacts need not be KKT-positive. Thus this theorem does not identify the full source with the positive force core and does not by itself close the force-bulk problem.

---

## 1. Setup

Let

\[
A=C\sqcup R
\]

be the C65 lexicographically normalized triangle-free global minimizer of cardinality `n` and diameter `D`.

C65 gives:

1. `C` is the unique nontrivial positive contact core;
2. the full actual diameter graph is KKT-visible;
3. every `r in R` is contact-isolated;
4. no `r in R` is an actual diameter endpoint.

The earlier Target C force-hull theorem also gives a fixed pair

\[
u,v\in C,
\qquad |u-v|=D.
\tag{1.1}
\]

Only (3) and the fixed core pair (1.1) are needed in the finite construction below. In fact the argument tolerates a rattler becoming diametral during the reconfiguration because the core pair keeps the global diameter equal to `D`.

---

## 2. Convex-hull diameter safety

### Lemma RA.1

If a finite set `A` has diameter `D`, then every point

\[
x\in\operatorname{conv}A
\]

satisfies

\[
|x-a|\le D
\qquad(a\in A).
\tag{RA.1}
\]

#### Proof

Write

\[
x=\sum_i\lambda_i a_i,
\qquad \lambda_i\ge0,
\qquad \sum_i\lambda_i=1.
\]

For fixed `a in A`, convexity of the norm gives

\[
|x-a|
\le
\sum_i\lambda_i|a_i-a|
\le
D.
\]

`square`

Consequently one source point may be moved along any segment lying in the current source convex hull without ever increasing its distance from a fixed source point above `D`.

---

## 3. One isolated point can be given exactly one first contact

### Lemma RA.2 — generic first-contact motion

Let `A` be a two-dimensional unit-separated finite set of diameter `D`, let `r in A` be contact-isolated, and assume some pair in `A\setminus{r}` already has distance `D`.

Then there is a replacement point `r'` such that

1. `(A\setminus{r}) union {r'}` is unit-separated;
2. its diameter is exactly `D`;
3. `r'` has exactly one unit contact with `A\setminus{r}`;
4. every relation among the fixed points is unchanged.

If `A` was triangle-free, the new configuration is also triangle-free.

#### Proof

Choose any fixed source point `p in A\setminus{r}`. Because `conv A` is two-dimensional, the set

\[
U=\operatorname{int}(\operatorname{conv}A)\cap B^\circ(p,1)
\]

is nonempty after choosing a point sufficiently close to `p` on an inward segment.

For `y in U`, consider the segment

\[
\gamma_y(t)=(1-t)r+ty,
\qquad 0\le t\le1.
\]

It lies in `conv A`. By Lemma RA.1,

\[
|\gamma_y(t)-a|\le D
\qquad(a\in A\setminus\{r\})
\tag{RA.2}
\]

throughout the motion.

Initially `r` is outside every closed unit disk centered at a fixed source point, while the endpoint `y` lies inside the open unit disk centered at `p`. Therefore the segment has a first intersection with

\[
\bigcup_{a\ne r}\overline B(a,1).
\]

There are only finitely many pairwise intersections of the unit-circle boundaries. If the first intersection of the segment lies on two or more unit circles, the target `y` lies on one of finitely many rays beginning at `r` and passing through such a circle-intersection point. Choose `y in U` outside this finite union of rays.

For that generic choice, the first intersection point `r'` lies on exactly one unit circle. Hence

\[
|r'-p_*|=1
\]

for one fixed source point `p_*`, while

\[
|r'-a|>1
\qquad(a\ne r,p_*).
\]

Thus the new set is unit-separated and `r'` has exactly one contact.

Equation RA.2 gives diameter at most `D`, while the fixed diameter pair in `A\setminus{r}` remains at distance exactly `D`. Therefore the new diameter is exactly `D`.

If the old configuration was triangle-free, any new unit triangle would have to contain `r'`. But `r'` has unit-contact degree exactly one, so this is impossible. `square`

---

## 4. Theorem RA — absorb every isolated rattler into the contact graph

### Theorem RA.3

Assume a C65 triangle-free C-II global minimizer exists. Then there is another triangle-free global minimizer `A^+` with

\[
|A^+|=|A|=n,
\qquad
\operatorname{diam}(A^+)=D(n),
\]

such that

1. every original positive-core vertex remains fixed;
2. every original positive-core contact remains unchanged;
3. every point of `A^+` is incident to at least one unit contact.

Equivalently, the full unit-contact graph of `A^+` has no isolated vertices.

#### Proof

Begin with the C65 source. Its positive core `C` contains the fixed diameter pair (1.1), and every point of `R` is isolated.

If there is an isolated point `r`, apply Lemma RA.2 to the current configuration while fixing every other point. The core pair remains fixed, the configuration stays a triangle-free global minimizer of diameter `D`, and `r` acquires exactly one contact.

No previously nonisolated point can become isolated because no fixed point moves and the moved point had no contact to lose. If the unique new contact joins `r` to another currently isolated point, both isolated vertices disappear from the isolated set. Otherwise at least `r` disappears from it.

Thus each step strictly decreases the number of isolated source points by at least one. The process terminates after finitely many steps. At termination every source point has positive full-contact degree, while the original core has never moved. `square`

---

## 5. Equivalent extremal formulation

A direct corollary avoids any reference to the C65 construction.

### Corollary RA.4

Among triangle-free global `n`-point minimizers that contain a fixed diameter pair not involving a chosen isolated vertex, any representative maximizing the number of unit contacts has no contact-isolated vertices.

Indeed Lemma RA.2 strictly increases the contact count without changing `n`, `D`, or triangle-freeness.

For the actual Target C campaign, Theorem RA.3 is stronger because C65 supplies one core diameter pair that remains fixed throughout the complete finite sequence.

---

## 6. What RA does and does not buy

### What it proves

A macroscopic population of fully inactive rattlers is **not unavoidable across all triangle-free global representatives**. If one C65 counterexample exists, there is a same-cardinality triangle-free global optimum with no contact-isolated points at all.

This is a finite source-wide statement. It goes beyond the local product-germ observation that rattlers have free coordinates near one representative.

### What it does not prove

The new contacts created at first events may have zero multiplier in every KKT stress. Therefore

\[
V(C_+)\ne A^+
\]

may still occur. RA does **not** prove:

- full KKT force visibility;
- `n=m` for the C65 positive core;
- a quantitative stress floor;
- pinned rigidity of the new contacts;
- connectedness of the full contact graph;
- Level I.

In particular, replacing the C65 source by `A^+` and silently reusing `C=C_*`, `H=H_*`, ZR, or ZF would be invalid. Those statements belong to the lexicographically normalized representative, not automatically to RA's contact-richer representative.

---

## 7. Why the first-contact construction is safe

### Diameter events are harmless

A moved point may become diametral to a fixed point before its first unit contact. This does not obstruct the path: Lemma RA.1 gives `<=D` at every point of the segment. Even if equality occurs at an intermediate time, the segment never violates the diameter constraint.

The fixed core pair keeps the final diameter exactly `D`.

### Existing contacts are preserved

Only a currently isolated point moves. Hence it has no incident unit edge to lose. All fixed-fixed contact edges are unchanged.

### Triangle-freeness is preserved

The generic first event gives exactly one new contact at the moved point. Therefore that point cannot complete a unit triangle at the event.

### The construction remains available after earlier steps

At every stage the current configuration has diameter `D` and contains the unchanged core pair. Any remaining isolated point can therefore be treated by the same argument using the **current** source convex hull. Previous new contacts are between fixed points during the next step and are preserved.

---

## 8. Regression audit

- **Heptagon plus isolated center:** the center may be moved toward a hull vertex until its first unit contact. The resulting eight-point set still has the fixed heptagon diameter and is a global minimizer, but is no longer the contact-minimal representative. This is exactly allowed.
- **External rattler:** the segment may be chosen toward the interior of the source hull. Convex-hull diameter safety is independent of whether the starting point lies outside the force hull.
- **Several nearby rattlers:** a generic first event can hit another rattler. Then both become nonisolated; no triangle appears because the moved point has only that one contact.
- **Diameter equality during motion:** allowed, as above.
- **One-dimensional source:** outside the sufficiently-large Target C regime; C19 already excludes the one-dimensional force-hull phase. RA is stated in the two-dimensional setting used by C-II.

---

## 9. Relation to the OP outer-pocket theorem

OP proves that internal outer-face rattlers are quantitatively absorbed by the force-hull area gap, leaving only source points outside the force hull as the C52 population obligation.

RA gives a different kind of reduction: those external rattlers can be converted, in another same-diameter triangle-free global representative, into ordinary contact vertices by finite first-contact motions.

The two results do not combine automatically because OP is tied to the C65 positive core while RA's new contacts need not be force-visible. A useful next theorem would transport a **global packing or contact-topology invariant** from the rattler-free representative back to the fixed C65 core without claiming positivity of the added contacts.

---

## 10. Promotion recommendation

**Hold as report.**

RA is exact but changes representatives. It should not be promoted into the active C-II theorem stack until there is a proved invariant transported through this representative change.

Its main immediate value is as a no-go/corrective fact: future force-bulk arguments must distinguish

- a rattler population forced in the particular C65 lexicographic representative, from
- a rattler population unavoidable among all triangle-free global minimizers.

Only the first can occur.

---

## 11. Next target

Two routes are now concrete:

1. **external completion-shell route:** bound `Z_ext` directly in the C65 source using the diameter-completion geometry outside the force hull;
2. **representative-transfer route:** prove a source-wide invariant on RA's rattler-free representative that depends only on the fixed original core / cardinality / diameter and therefore transfers back to C65.

Do not treat new RA contacts as positive KKT contacts without a separate theorem.

---

## 12. Compact handoff

```text
LEVEL I STATUS: STILL OPEN

RA theorem:
Start from the C65 lexicographic counterexample A=C disjoint-union R.
The core C is fixed and contains a diameter-D pair; every r in R is isolated.

For an isolated r, choose a generic segment from r to a point inside the
unit disk of some source point, with the segment inside conv(A).
Every point x on the segment satisfies |x-a|<=D for every fixed a in A.
Stop at the first unit-circle event. Generically exactly one new contact
appears, so triangle-freeness is preserved and the fixed core pair keeps
diameter exactly D.

Repeat. Each step strictly lowers the isolated-vertex count, so finitely many
steps produce a same-n, same-D triangle-free global minimizer A+ with no
contact-isolated vertices and with the original C65 core fixed pointwise.

Caution:
The newly created contacts need not be KKT-positive. RA does not imply n=m
for the positive force core and does not permit reusing ZR/ZF on A+.
```
