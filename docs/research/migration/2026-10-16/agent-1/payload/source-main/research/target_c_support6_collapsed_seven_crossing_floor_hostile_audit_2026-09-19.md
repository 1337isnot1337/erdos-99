# Hostile audit — collapsed support-six seven-crossing floor

**Date:** 2026-09-19  
**Audited note:** `research/target_c_support6_collapsed_seven_crossing_floor_2026-09-19.md`  
**Certificate:** `research/verify_target_c_support6_collapsed_seven_crossing_floor_2026_09_19.cpp`  
**Disposition:** PASS at exact finite/global train-topology scope; theorem-state authority unchanged; C-II remains open.

## 1. Main claim under audit

The note claims that every globally realizable degree-pure collapsed support-six block has at least seven strict-rhombus crossings between its twelve internal relation trains:

\[
X_K\ge7.
\]

This is stronger than the preceding positive-genus statement `X_K>=g_K>=1`. The new proof needs three ingredients simultaneously:

1. MI.1 parity;
2. joint metric feasibility of every asserted crossing; and
3. the **correct**, not freely chosen, local rotation at each crossing.

The third item is the main point requiring hostile checking.

---

## 2. The crossing rotation sign is correct

Fix an internal relation train `e` with upper-half-plane representative `u_e`. By definition of the coherent relation orientation, its terminal occurrence is `+u_e` at the tail exceptional face and `-u_e` at the head.

Orient the complete train midpoint path from tail to head.

At the tail, the exceptional-face boundary traverses the terminal contact edge as `+u_e`, so the adjacent rhombus traverses the same shared edge as `-u_e`. In that rhombus the opposite side is `+u_e`. When the train crosses that opposite side into the next rhombus, boundary orientation reverses again, so the next rhombus is entered through `-u_e`. Induction gives:

> every rhombus on the oriented train is entered through its `-u_e` side and exited through its `+u_e` side.

Now take a crossing rhombus for trains `e,f` and write

\[
D=\det(u_e,u_f).
\]

If `D>0`, a counterclockwise side order is

\[
-u_e,-u_f,+u_e,+u_f.
\]

Direct midpoint subtraction gives

\[
t_e=-u_f,
\qquad
t_f=+u_e.
\]

Hence

\[
\det(t_e,t_f)=D>0.
\]

If `D<0`, a counterclockwise side order is

\[
-u_e,+u_f,+u_e,-u_f,
\]

and midpoint subtraction gives

\[
t_e=+u_f,
\qquad t_f=-u_e,
\]

again with

\[
\det(t_e,t_f)=D<0.
\]

Thus the note's equation

\[
\operatorname{sign}\det(t_e,t_f)
=
\operatorname{sign}\det(u_e,u_f)
\]

is correct.

The conversion from train tangent to the dart toward the lower-numbered relation endpoint is also correct. In the base cell encoding,

```text
orientation_bits[e]=0  => tail = E[e].a,
orientation_bits[e]=1  => tail = E[e].b.
```

Therefore the dart `eA` toward `E[e].a` is `-t_e` in the first case and `+t_e` in the second. The same holds for `f`, proving the code's sign formula

\[
\operatorname{sign}\det(eA,fA)
=c_ec_f\operatorname{sign}D.
\]

Finally, for two transverse lines, positive `det(eA,fA)` gives cyclic order

\[
eA,fA,eB,fB,
\]

while negative determinant gives

\[
eA,fB,eB,fA.
\]

So the verifier is right to use exactly one of the two alternating crossing rotations once the oriented crossing window is fixed. Allowing the crossing rotation to be chosen freely would be an invalid relaxation in the opposite direction and, in fact, admits abstract two-crossing planarizations in some cells. The geometric sign is load-bearing.

---

## 3. The selected crossing windows are exact and simultaneous

For projective representatives `0<alpha_e,alpha_f<pi`, a strict unit-rhombus crossing requires acute projective angle strictly larger than `pi/3`. This is equivalent to

\[
{\pi\over3}<|\alpha_e-\alpha_f|<{2\pi\over3}.
\]

After scaling `x=3 alpha/pi`, the two oriented possibilities are exactly

\[
1<x_e-x_f<2,
\qquad
1<x_f-x_e<2.
\]

The certificate appends every selected crossing window to one common copy of the rotation-cell difference system. It does **not** test the selected pairs independently. This fixes the weakness documented by the preceding coarse parity regression.

All resulting inequalities remain strict integer differences. The inherited `14c-1` Bellman--Ford transformation is therefore still an exact feasibility test. No floating-point comparison enters.

Unselected pairs are deliberately unconstrained. This cannot create a false exclusion. An actual drawing with crossing set `S` must satisfy all windows for pairs in `S`; it need not make every angle-compatible pair cross. The verifier gives noncrossing pairs more freedom than geometry does.

---

## 4. The MI.1 filter is complete at the stated scope

The certificate re-enumerates every simple cycle of `K_6\setminus M` and every unordered edge-disjoint cycle pair. For each pair it forms the audited equation

\[
\bigoplus_{e\in E(C),f\in E(D)}z_{e,f}
=
\bigoplus_{v\in V(C)\cap V(D)}\eta_v(C,D).
\]

The local alternation bit is read from the exact four-edge cyclic relation order stored in the rotation cell. Train pairs sharing an exceptional endpoint are retained on the left. That matches the earlier MI.1 hostile audit.

Gaussian elimination and syndrome evaluation use only bit operations over `F_2`.

MI.1 is used only as a necessary filter. Even if it were incomplete as a characterization of planar train drawings, that would not hurt the proof: every actual drawing must satisfy the equations that are used.

---

## 5. The planarization test is necessary and exhaustive

For a selected crossing set, each crossing is replaced by a degree-four vertex. Each original relation train becomes a chain through its selected crossing vertices.

At the six exceptional-face vertices, the verifier retains the exact cyclic order of the four internal relation incidences. Deleting the unique anchor incidence does not alter the cyclic order among those four endpoints.

At a crossing vertex, the forced rotation from Section 2 is used.

If one train participates in several selected crossings, the coarse angle cell does not determine their order along that train. The verifier enumerates every permutation of its selected crossing vertices. These permutations are independent across the twelve trains. Therefore the actual crossing order of any putative global drawing is included.

For each resulting orientable rotation system the face permutation is computed exactly and Euler characteristic gives the genus. A planar stopped-train drawing would necessarily produce genus zero after planarization. Consequently positive genus for every permutation is a valid obstruction.

The converse is not used. Genus zero would not prove a metric rhombic realization.

External trains and external-train crossings do not create a loophole. Delete every train not internal to the block from a hypothetical global drawing. The twelve internal paths, their mutual crossing vertices, and the six exceptional terminal disks remain a planar drawing with exactly the rotation data tested by the certificate. External crossings can occur between two retained internal crossings along a train, but deleting them does not change the relative order of the retained crossings; that relative order is among the permutations enumerated.

Singleton internal relation trains also cause no problem. A singleton cannot participate in a strict-rhombus crossing. The verifier nevertheless allows every internal relation train to be selected in a crossing set. This is again an over-relaxation, so it cannot falsely exclude an actual source.

---

## 6. The finite search through weight six is complete

For weights `0,1,2,3,4`, the certificate enumerates every subset directly.

For weight five it uses a `2+3` meet-in-the-middle split. Requiring the two selected variable indices to precede the three selected indices makes every sorted five-set appear exactly once.

For weight six it uses the analogous `3+3` split, again with a strict index separator so every sorted six-set appears exactly once.

The reproduced exact census is

```text
all-cross matching
  k=0 parity=0 metric=0 planar=0
  k=1 parity=0 metric=0 planar=0
  k=2 parity=156 metric=132 planar=0
  k=3 parity=1176 metric=96 planar=0
  k=4 parity=10788 metric=756 planar=0
  k=5 parity=87648 metric=1416 planar=0
  k=6 parity=583296 metric=5160 planar=0
mixed matching
  k=0 parity=0 metric=0 planar=0
  k=1 parity=0 metric=0 planar=0
  k=2 parity=40 metric=32 planar=0
  k=3 parity=696 metric=192 planar=0
  k=4 parity=10024 metric=528 planar=0
  k=5 parity=82264 metric=1288 planar=0
  k=6 parity=617952 metric=5480 planar=0
PASS: no collapsed support-six rotation cell admits a planar, angle-compatible MI.1 crossing pattern with at most six internal crossings.
CONCLUSION: every global collapsed support-six block has X_K >= 7 internal strict-rhombus crossings.
```

The implementation was independently reproduced locally against the exact rotation-cell enumeration logic with `g++ -O3 -std=c++17 -Wall -Wextra -pedantic`; the full enumeration completed with the counts above and all assertions passing.

---

## 7. The global `R_4>=7c_6` payment does not double-count

Distinct one-anchor relation components have disjoint internal relation-train sets. A strict rhombus contains exactly two complete train tracks. If both tracks are internal to component `K`, the same rhombus cannot also have both tracks internal to a different component `K'`.

Therefore the internal crossing rhombi counted by the different `X_K` are disjoint. Summing `X_K>=7` gives

\[
R_4\ge7c_6.
\]

Combining with the earlier tangent payment is legitimate because these are independent upper bounds on the same count `c_6`:

\[
c_6\le {d_C-M_0\over2},
\qquad
c_6\le {R_4\over7}.
\]

Multiplying their minimum by the existing coefficient `1/7` yields exactly the correction term in (SC.4).

---

## 8. Scope guard

The theorem does **not** say that seven crossings suffice. No seven-crossing realization has been proved, and the nonlinear six-face closure equations were not imposed in this certificate.

It also does not exclude the collapsed support-six branch outright. It proves only the rigorous lower bound

\[
X_K\ge7.
\]

The correct next question is whether the forced-crossing rotation argument has a structural extension that forbids every possible crossing set, or whether seven-or-more-crossing cells survive and can then be attacked by nonlinear closure or by the global terminal rhombus budget.

**Audit disposition:** PASS. The seven-crossing floor follows from necessary conditions only, all finite decisions are exact, the geometric crossing rotation has the correct sign, crossing-order freedom is exhausted rather than guessed, and the global rhombus payment does not double-count. C-II remains open.
