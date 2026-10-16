# Target C-II — a Jordan train-cycle excludes the certified collapsed support-six cell globally

**Date:** 2026-09-19  
**Status:** proof-only global train-integrability obstruction; theorem-state authority unchanged  
**Scope:** the exact `10^-10` collapsed support-six root box certified in `target_c_support6_collapsed_local_realization_2026-09-18.md`  
**Depends on:** audited stopped-train path/crossing theorem; strict convexity of exceptional faces; exact collapsed local root/order certificate  
**Certificate:** `research/verify_target_c_support6_collapsed_global_train_obstruction_2026_09_19.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The previously certified collapsed support-six realization is genuinely local: it solves the six pentagon closure equations and all local separation/turn inequalities. This note proves that the entire certified root box cannot occur inside any global stopped-train/rhombus system.

The obstruction is topological. In the certified box, the three relation trains `01,12,02` are pairwise too close in projective direction to cross in a strict rhombus. Joining their midpoint paths through straight chords inside the three convex pentagons `F_0,F_1,F_2` therefore gives a Jordan curve `J`.

The certified cyclic orders place train `04` on one side of `J` at `F_0` and train `23` on the other side at `F_2`. Both train directions are too close to all three cycle directions to cross `J`. Hence `F_4` and `F_3` must lie on opposite sides of `J`.

But train `34` is also too close to all three cycle directions to cross any of them. A complete train joining `F_3` to `F_4` would therefore have to connect opposite sides of a Jordan curve without meeting it. Contradiction.

Thus

\[
\boxed{
\text{no point of the certified collapsed support-six root box extends to a global stopped-train source.}
}
\tag{GJ.1}
\]

This does **not** exclude every collapsed support-six solution. It removes the only currently certified local realization and supplies a new global necessary condition: a collapsed block must avoid this Jordan-cycle order/angle cell. Future searches for collapsed blocks must satisfy train-crossing compatibility, not merely the six pentagon closure equations.

---

## 1. Train arcs and the strict crossing-angle test

For a complete train, use its audited midpoint path through the chain of strict rhombi, together with the obvious infinitesimal transverse connector in the singleton case. This gives a simple arc between its two terminal exceptional/outer incidences. Distinct complete trains can meet only by crossing in a common strict rhombus, and two trains meet in at most one such rhombus.

If two trains with projective contact directions `u,v` cross in a strict unit rhombus, their acute projective angle satisfies

\[
{\pi\over3}<\angle_{\rm proj}(u,v)\le{\pi\over2}.
\]

For unit representatives this is equivalent to

\[
\boxed{|u\cdot v|<{1\over2}.}
\tag{1.1}
\]

Therefore a certified inequality

\[
|u\cdot v|>{1\over2}
\tag{1.2}
\]

is an exact no-crossing certificate for the two complete train arcs.

The new verifier uses rational Taylor/Lagrange enclosures for sine and cosine over the existing root box. For every pair used below it proves the stronger margin

\[
\boxed{|u\cdot v|>{11\over20}.}
\tag{1.3}
\]

No floating-point angle comparison enters the proof.

---

## 2. The certified rotation data

Use the same labels and matching as the local realization:

\[
M=\{03,14,25\}.
\]

The existing exact root certificate fixes `theta_01` and `theta_02` and puts every other solved internal train angle in a radius-`10^-10` interval around its recorded rational center. The new verifier independently rechecks the relevant cyclic side orders throughout that full box:

\[
\begin{array}{c|l}
F_0 & a,02,04,05,01,\\
F_1 & a,15,01,13,12,\\
F_2 & a,23,12,24,02.
\end{array}
\tag{2.1}
\]

Here `a` denotes the unique outside anchor side. The orders are counterclockwise orders of oriented sides of the strict convex pentagons.

The verifier also certifies (1.3) for all of the following fifteen train pairs:

1. the three pairs among `01,12,02`;
2. every pair of one of `04,15,23` with one of `01,12,02`;
3. every pair of `34` with one of `01,12,02`.

Hence none of those fifteen train pairs can share a rhombus.

---

## 3. The relation triangle is a Jordan curve

Consider the relation triangle

\[
F_0\xleftrightarrow{01}F_1
\xleftrightarrow{12}F_2
\xleftrightarrow{02}F_0.
\]

The three complete train arcs `01,12,02` are individually simple. By Section 2 they are pairwise disjoint away from their terminal face incidences.

Inside each of the strict convex faces `F_0,F_1,F_2`, join the two relevant side midpoints by the straight chord lying in the face interior. Specifically use

- the chord from midpoint `02` to midpoint `01` in `F_0`;
- the chord from midpoint `01` to midpoint `12` in `F_1`;
- the chord from midpoint `12` to midpoint `02` in `F_2`.

A complete train not terminating at one of these faces does not enter its interior. The three face interiors are disjoint. Therefore the three train arcs and three internal chords form a simple closed curve

\[
\boxed{J.}
\tag{3.1}
\]

Singleton relation trains cause no problem: the common terminal edge midpoint is simply the zero-length train segment between the two adjacent face incidences, and the same local Jordan construction is obtained after an arbitrarily small transverse thickening.

---

## 4. The rotation system puts `04` and `23` on opposite sides

Orient `J` in the order

\[
F_0\to F_1\to F_2\to F_0.
\]

At each face disk, one component of the complement of `J` corresponds to the counterclockwise boundary sector from the incoming cycle side to the outgoing cycle side; the other component corresponds to the complementary sector. Which one is geometrically the bounded component is irrelevant. The same choice gives the same side of the oriented Jordan curve at all three faces.

At `F_0`, the incoming cycle side is `02` and the outgoing side is `01`. From (2.1), the counterclockwise sector

\[
02\rightsquigarrow01
\]

contains `04` and `05`. Call this side `A`.

At `F_2`, the incoming side is `12` and the outgoing side is `02`. The corresponding counterclockwise sector

\[
12\rightsquigarrow02
\]

contains `24`; its complementary sector contains `23`. Thus the `23` half-train leaves `F_2` into the opposite side, call it `B`.

By Section 2, train `04` cannot cross any of the three train arcs making `J`. It also cannot meet one of the internal face chords, because a complete train does not enter an exceptional face at which it does not terminate. Starting on side `A` at `F_0`, it therefore remains in side `A` all the way to its other terminal face. Consequently

\[
\boxed{F_4\subset A.}
\tag{4.1}
\]

Likewise train `23` cannot cross `J`; starting on side `B` at `F_2`, it forces

\[
\boxed{F_3\subset B.}
\tag{4.2}
\]

The statements mean that the interiors of the corresponding exceptional-face disks lie in those components of `R^2\setminus J`. Since `J` does not meet `F_3` or `F_4`, all their side attachments lie in the same respective components.

---

## 5. Train `34` gives the contradiction

The relation graph is `K_6\setminus\{03,14,25\}`, so train `34` is one of the twelve internal relation trains. It connects a side of `F_3` to a side of `F_4`.

Equations (4.1)--(4.2) put its two endpoints in opposite components of the complement of the Jordan curve `J`. Any continuous arc joining those endpoints must meet `J`.

The `34` midpoint path cannot meet the three internal face chords of `J`: it does not terminate at `F_0,F_1,F_2`, and train paths stay in the rhombic region until their terminal exceptional face. Hence any intersection with `J` would have to be a rhombus crossing with one of the cycle trains `01,12,02`.

But Section 2 certifies

\[
|u_{34}\cdot u_{01}|>{11\over20},
\qquad
|u_{34}\cdot u_{12}|>{11\over20},
\qquad
|u_{34}\cdot u_{02}|>{11\over20}.
\]

By the strict rhombus crossing test (1.1), none of those crossings can occur. This is impossible. The contradiction proves (GJ.1).

---

## 6. What this changes and what it does not

The earlier local realization remains a valid certificate for a solution of the isolated six-face closure equations. What is now ruled out is its interpretation as a piece of an actual global canonical stopped-train source. The missing condition was exactly global train-track integrability.

This is stronger than observing that the auxiliary side-pairing surface had genus two. The genus computation alone did not prove nonrealizability because additional rhombi/train crossings could in principle resolve the abstract gluing. The Jordan argument uses the actual train-crossing theorem and the certified direction inequalities to show that the crossings required by the rotation system are forbidden.

The proof is still local in **parameter space**: it covers the full certified `10^-10` root box, not every solution of the collapsed six-face closure equations. A different collapsed solution could have a different cyclic order or could move one of the required train-direction pairs past the `pi/3` crossing threshold. Such a solution is not excluded here.

The next finite target is therefore clear. Classify collapsed support-six solutions by a relation-triangle rotation cell and the `pi/3` crossing-compatibility pattern. Any cell containing a triangle for which two noncrossing spokes force an opposite-side relation edge that is itself noncrossing is globally impossible by the same Jordan lemma. A complete finite/analytic classification of those cells would exclude the collapsed branch without needing a new local pentagon inequality.

No theorem-state file is changed.

**Disposition:** the only currently certified collapsed support-six local realization, including its entire rigorous root box, is globally nonintegrable as a stopped-train/rhombus source. The obstruction is an exact Jordan separation forced by the certified rotation system and fifteen strict no-crossing inequalities. C-II remains open because other collapsed parameter/order cells have not yet been excluded.
