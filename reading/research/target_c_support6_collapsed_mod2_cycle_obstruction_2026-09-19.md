> Generated reading edition · [exact source](../../research/target_c_support6_collapsed_mod2_cycle_obstruction_2026-09-19.md) · source SHA-256 `4bf8eaa2bfe00063c85cf9b69cf27ba9a4a43a9d479c4da16659e9097ada84ac`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "61b7615a685faac466247a633b36a435645fefc6", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support6_collapsed_mod2_cycle_obstruction_2026-09-19.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "b40cc50b664e38cc5961f30fc1ab5e7aac533f908295b84d05922db27531b2e8"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — mod-2 cycle intersection excludes a second collapsed support-six cell

**Date:** 2026-09-19  
**Status:** proved global exclusion for a new certified collapsed parameter cell; theorem-state authority unchanged  
**Scope:** degree-pure collapsed support-six one-anchor blocks with relation graph `K_6\setminus M`, `M={03,14,25}`  
**Depends on:** canonical simple stopped-train centerlines; at-most-once train crossing; unit-rhombus crossing-angle criterion; strict convexity of exceptional faces; collapsed six-pentagon closure system  
**Certificate:** `research/verify_target_c_support6_collapsed_mod2_cycle_obstruction_2026_09_19.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The first global support-six obstruction used one Jordan train triangle in the only previously certified collapsed root box. That argument is local to one rotation/crossing cell. This note adds a more general plane-topology constraint: mod-2 intersection equations for pairs of relation cycles. The equations do not require either cycle to be simple after the train arcs are inserted, and they count train pairs which share an exceptional endpoint as well as independent train pairs.

A second regular local collapsed root box is certified. Its six pentagon closures and all strict local turn inequalities hold, but three cycle-intersection equations are inconsistent:

$$
x_{02,34}=0,
\qquad
x_{02,34}+x_{04,34}=0,
\qquad
x_{04,34}=1
\pmod 2.
$$

Their XOR is `0=1`. Hence no point of the new certified root box extends to a global stopped-train/rhombus source.

This still does not exclude every collapsed support-six solution. It supplies a reusable finite test on every proposed rotation/crossing cell.

---

## 1. A mod-2 relation-cycle equation

Contract each exceptional face only conceptually. For every residual relation train, keep its canonical train centerline from one terminal side midpoint to the other. If a relation cycle

$$
C=(v_0v_1\ldots v_{r-1}v_0)
$$

passes through an exceptional face `v_i`, join the two relevant train-end midpoints by a chord inside that strict convex face. The train arcs and these face chords form a closed immersed curve `gamma_C` in the plane. The curve may self-intersect; simplicity is not required.

Take two **edge-disjoint** relation cycles `C,D`. Their curves share no complete train. For distinct relation trains `e,f`, write

$$
x_{e,f}=1
$$

if their centerlines cross in a rhombus, and `0` otherwise. The canonical train theorem gives at most one such crossing for a fixed pair.

At a common exceptional face `v`, the two cycles use four distinct side midpoints. Put

$$
\eta_v(C,D)=1
$$

when those four endpoints alternate in the cyclic side order of the face, and `0` otherwise. Two interior chords of a convex polygon cross exactly in the alternating case.

After an arbitrarily small generic perturbation, two closed curves in the plane have zero mod-2 intersection number. Every intersection of `gamma_C` and `gamma_D` occurs either

1. in a rhombus, between one train of `C` and one train of `D`; or
2. inside a common exceptional face, where it contributes `eta_v(C,D)`.

Therefore every edge-disjoint cycle pair obeys

$$
\boxed{
\bigoplus_{e\in E(C),\ f\in E(D)}x_{e,f}
=
\bigoplus_{v\in V(C)\cap V(D)}\eta_v(C,D).
}
\tag{MI.1}
$$

This equation includes train pairs that share an exceptional endpoint. Such a pair can still meet later in a rhombus, and that crossing is correctly represented by `x_{e,f}`. No "good drawing" simplification is being assumed.

For projective train directions `u_e,u_f`, a strict unit-rhombus crossing requires

$$
|u_e\cdot u_f|<\frac12.
\tag{MI.2}
$$

Hence any pair with `|u_e.u_f|>1/2` has `x_{e,f}=0`. Once a rotation cell and the side of every `1/2` crossing threshold are fixed, (MI.1) becomes a finite linear system over `F_2`.

---

## 2. A second regular collapsed local cell

Use the same matching as the first certified collapsed example,

$$
M=\{03,14,25\},
$$

and the same anchor orientation split

$$
(s_0,s_1,s_2,s_3,s_4,s_5)=(+,+,+,-,-,-).
$$

The twelve internal relation trains are

$$
01,02,04,05,12,13,15,23,24,34,35,45.
$$

Fix

$$
\theta_{01}=-1.93018848,
\qquad
\theta_{02}=1.02838679.
$$

The exact certificate proves a unique root in the sup-norm `10^-10` box centered at

$$
\begin{array}{c|r}
04&-2.2622479662783364\\
05& 2.1256745629003877\\
12&-1.0409722289425172\\
13& 2.8026180119778759\\
15&-2.7238097420853755\\
23& 1.2700445670047056\\
24&-1.8490278001261384\\
34& 2.1429491086277803\\
35& 0.46329367519815784\\
45&-2.041770793051696
\end{array}
\tag{2.1}
$$

for the ten independent closure equations on faces `0,...,4`. The sixth closure follows from signed endpoint cancellation.

The interval Newton/Banach data certified by exact rational arithmetic are

$$
Y<3.146\times10^{-16},
\qquad
Z_0<1.713\times10^{-15},
$$

$$
\|C\|_\infty<11.914,
\qquad
Z<4.766\times10^{-9},
$$

and

$$
Y+Z\,10^{-10}<3.16\times10^{-16}<10^{-10}.
$$

Thus the box contains one exact closure root for the fixed two parameters, and the corresponding `10 x 10` Jacobian is invertible throughout the contraction argument. As in the first collapsed certificate, this is a regular point of the two-parameter local closure family.

The same certificate proves throughout the entire root box:

$$
0<\delta_i<\frac{2\pi}{3},
\qquad
\frac{2\pi}{3}<\delta_i+\delta_{i+1}<\pi
\tag{2.2}
$$

on every physical force pentagon. Numerically descriptive margins from the certified rational intervals are

$$
\min\delta_i>0.26417,
\qquad
\max\delta_i<2.06936,
$$

$$
\min(\delta_i+\delta_{i+1})>2.10062,
\qquad
\max(\delta_i+\delta_{i+1})<3.11908.
$$

So this cell is locally admissible under all of the current strict pentagon geometry.

---

## 3. The certified rotation system

The face-side cyclic orders, starting where displayed, are

$$
\begin{array}{c|ccccc}
0&a&02&05&04&01\\
1&a&01&13&15&12\\
2&a&23&12&02&24\\
3&35&34&a&23&13\\
4&04&24&a&45&34\\
5&15&45&a&35&05
\end{array}
\tag{3.1}
$$

where `a` is the unique outside anchor side. Deleting `a` gives the relation-edge rotations

$$
\begin{aligned}
0 &: (2,5,4,1),\\
1 &: (0,3,5,2),\\
2 &: (3,1,0,4),\\
3 &: (5,4,2,1),\\
4 &: (0,2,5,3),\\
5 &: (1,4,3,0).
\end{aligned}
\tag{3.2}
$$

All order separations are strict on the full certified box.

---

## 4. Three cycle equations

Consider the following edge-disjoint cycle pairs.

### 4.1 `012` against `234`

At the common face `2`, the four cycle halfedges appear in rotation order

$$
23(D),\ 21(C),\ 20(C),\ 24(D),
$$

so they do not alternate. Thus the right side of (MI.1) is `0`.

The exact angle intervals prove that among the nine train pairs in

$$
E(012)\times E(234),
$$

the only pair which can satisfy the strict rhombus crossing condition (MI.2) is `02,34`. Therefore

$$
\boxed{x_{02,34}=0.}
\tag{4.1}
$$

### 4.2 `024` against `345`

At the common face `4`, the cycle halfedges occur as

$$
40(C),\42(C),\45(D),\43(D),
$$

so the local alternation term is again zero. The only crossing-compatible train pairs across these cycles are `02,34` and `04,34`. Hence

$$
\boxed{x_{02,34}+x_{04,34}=0.}
\tag{4.2}
$$

### 4.3 `045` against `234`

Again the cycles meet only at face `4`, but now their halfedges occur as

$$
40(C),\42(D),\45(C),\43(D),
$$

which alternates. Thus the face contributes one. The only crossing-compatible train pair between the two cycles is `04,34`, so

$$
\boxed{x_{04,34}=1.}
\tag{4.3}
$$

The weakest certified margin from a crossing-forbidden pair to the threshold `1/2` is greater than `0.0035208`; the weakest margin from a crossing-compatible pair is greater than `0.0594295`. The `10^-10` root box is therefore far from every crossing-pattern wall used in (4.1)--(4.3).

XORing (4.1)--(4.3) gives

$$
0=1
\qquad\text{in }\mathbb F_2.
$$

Therefore

$$
\boxed{
\text{no point of the certified cell extends to a global stopped-train source.}
}
\tag{4.4}
$$

---

## 5. What changed and what remains

The earlier global obstruction used one explicit Jordan separator. Equation (MI.1) gives a systematic replacement: for any collapsed support-six rotation/crossing cell, enumerate edge-disjoint relation cycles and solve the resulting binary crossing system. An inconsistent system is a complete global obstruction at that cell. This remains finite once the face rotations and the sides of all `|u_e.u_f|=1/2` walls are known.

The present result removes a second open collapsed parameter cell and proves that local closure regularity does not imply global train integrability even away from the first certified witness. It does not prove that every collapsed support-six cell has an inconsistent mod-2 system. Numerical exploration found cells whose parity system is consistent, so claiming a complete support-six exclusion from (MI.1) alone would be false.

The next finite target is to enumerate closure-feasible collapsed rotation/crossing cells up to the octahedral symmetries and apply, in order:

1. the mod-2 cycle system (MI.1);
2. the triangle-free train-crossing theorem;
3. the Jordan separator test where parity is consistent; and
4. only then any remaining metric/diameter-locking constraints.

No theorem-state file is changed.

**Disposition:** proved the general mod-2 relation-cycle intersection equation and used it, with a new exact regular collapsed closure root box, to derive the incompatible system `x_02,34=0`, `x_02,34+x_04,34=0`, `x_04,34=1`. The entire new root box is globally nonintegrable. C-II remains open because collapsed cells with different rotations/crossing patterns remain unclassified.
