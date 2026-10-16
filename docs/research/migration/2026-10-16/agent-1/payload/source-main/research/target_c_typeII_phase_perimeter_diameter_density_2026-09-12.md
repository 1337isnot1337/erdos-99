# Target C — Type-II phase/perimeter coupling forces higher diameter-edge density

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Status:** proof-only research theorem; theorem authority unchanged.

The all-defect phase/train theorem combines with the canonical Type-II near-disk
perimeter limit more strongly than with the older difference-body inequality alone.
The result raises the asymptotic diameter-edge density from the canonical

\[
2\rho=1.4781702664\ldots
\]

to

\[
\boxed{
{4\over9}
\left(
\pi+\sqrt{\frac{\pi}{2\sqrt3}}
\right)
=1.8195135379794445\ldots .
}
\]

The proof retains the Woodall defect `d_H` and mixed-rigidity surplus `s_Z`; both make
the bound strictly stronger.

This still lies below the geometric maximum `pi`, so it is not by itself C-II
closure.  It substantially narrows the surviving Type-II diameter graph.

---

## 1. Inputs

Work along a Type-II full-core survivor sequence.  Put

\[
\Delta_2:={\pi\over2\sqrt3}.
\tag{1.1}
\]

Canonical Sections 79--80 give

\[
{R_4\over D^2}\to\Delta_2
\tag{1.2}
\]

and the scaled force hull converges in Hausdorff distance to the radius-`1/2` disk.
Perimeter continuity for convex bodies therefore gives

\[
\boxed{{\operatorname{per}(F)\over D}\to\pi.}
\tag{1.3}
\]

Use the exact core notation

- `h=|H|` for actual diameter edges;
- `q` for loaded force-hull vertices;
- `d_H=q-h>=0`;
- `s_Z=e+h-(2v-2)>=0`;
- `k=d_H+s_Z`;
- `f` for bounded nonquadrilateral contact faces;
- `Q=sum_F(deg F-4)>=f`.

The stopped-train identity proved in
`target_c_all_defect_phase_train_gap_2026-09-12.md` is

\[
\boxed{T=q+2f-k.}
\tag{1.4}
\]

The same theorem's phase-atomic/exposed-hull argument gives the sharper pre-elimination
form

\[
\boxed{
\liminf {T-q/2\over D}\ge2\sqrt{\Delta_2}.}
\tag{1.5}
\]

Finally the canonical Section-59 Euler coupling is the exact identity

\[
\boxed{b=2h-Q-2s_Z,}
\tag{1.6}
\]

where `b` is the occurrence-counted outer contact-walk length.  Since that walk has
convex hull `F`,

\[
\boxed{\operatorname{per}(F)\le b.}
\tag{1.7}
\]

---

## 2. Phase transport gives a face lower bound retaining `q` and `k`

Pass to an arbitrary subsequence on which the normalized variables converge:

\[
{h\over D}\to y,
\qquad
{d_H\over D}\to d,
\qquad
{s_Z\over D}\to s,
\tag{2.1}
\]

and, after a further subsequence if needed, `f/D` and `Q/D` converge.  Then

\[
{q\over D}\to y+d,
\qquad
{k\over D}\to d+s.
\tag{2.2}
\]

Substitute (1.4) into (1.5):

\[
{q/2+2f-k\over D}
\ge2\sqrt{\Delta_2}-o(1).
\]

Hence

\[
\boxed{
\liminf {f\over D}
\ge
\sqrt{\Delta_2}
-{y\over4}+{d\over4}+{s\over2}.
}
\tag{2.3}
\]

This is stronger than the universal `0.166914...D` face floor whenever `q/D` stays
away from `pi`.

---

## 3. The near-disk outer perimeter gives the opposing upper currency

From (1.3), (1.6), and (1.7),

\[
\pi
\le
2y-\liminf {Q\over D}-2s.
\]

Equivalently,

\[
\boxed{
\limsup {Q\over D}+2s\le2y-\pi.
}
\tag{3.1}
\]

Since every nonquadrilateral bounded face has degree at least five,

\[
Q\ge f.
\tag{3.2}
\]

Combining (2.3), (3.1), and (3.2) gives

\[
2y-\pi
\ge
\sqrt{\Delta_2}
-{y\over4}+{d\over4}+{5s\over2}.
\tag{3.3}
\]

Therefore

\[
\boxed{
{9y\over4}
\ge
\pi+\sqrt{\Delta_2}+{d\over4}+{5s\over2}.
}
\tag{3.4}
\]

or

\[
\boxed{
y
\ge
{4\over9}\left(\pi+\sqrt{\Delta_2}\right)
+{d\over9}+{10s\over9}.
}
\tag{3.5}
\]

Because the original subsequence was arbitrary, this proves the sequence-level
inequality

\[
\boxed{
\liminf {1\over D}
\left(
 h-{d_H\over9}-{10s_Z\over9}
\right)
\ge
{4\over9}
\left(
\pi+\sqrt{\frac{\pi}{2\sqrt3}}
\right).
}
\tag{3.6}
\]

In particular,

\[
\boxed{
\liminf {h\over D}
\ge
h_*:={4\over9}
\left(
\pi+\sqrt{\frac{\pi}{2\sqrt3}}
\right)
=1.8195135379794445\ldots .
}
\tag{3.7}
\]

---

## 4. Secondary consequences

### 4.1 Strong penalty on non-Woodall-connected or mixed-surplus regimes

Equation (3.5) keeps the defects instead of discarding them.  A linear Woodall defect
costs `d_H/9` directly in the required diameter-edge density, while a linear mixed
surplus costs `10s_Z/9`.

Since `h<=q<=per(F)=pi D+o(D)`, (3.5) also yields the explicit coarse defect cap

\[
\boxed{
{d_H+10s_Z\over D}
\le
9\pi-4\pi-4\sqrt{\Delta_2}+o(1)
=5\pi-4\sqrt{\Delta_2}+o(1).
}
\tag{4.1}
\]

This numerical cap is not itself sharp; the retained form (3.5) is the useful theorem.

### 4.2 Improved difference-body perimeter and area floors

Canonical Section 59 gives, along any subsequence with `h/D->y`,

\[
\liminf {\operatorname{per}(F)\over D}
\ge y+2\cos(y/2)
\tag{4.2}
\]

and

\[
\liminf {\operatorname{area}(F)\over D^2}
\ge {y+\sin y\over4}.
\tag{4.3}
\]

Both right-hand sides are increasing on `[0,pi]`.  Inserting `h_*` gives the stronger
post-phase working floors

\[
\operatorname{per}(F)
\ge
(3.0478\ldots-o(1))D,
\tag{4.4}
\]

and

\[
\operatorname{area}(F)
\ge
(0.6971\ldots-o(1))D^2.
\tag{4.5}
\]

These decimals are descriptive consequences; the exact theorem is (3.6)--(3.7).
In the Type-II branch the already-known near-disk limit is stronger than (4.4)--(4.5),
but these formulas can be useful when transporting the new density theorem back into
pre-Type-II scalar currencies.

---

## 5. Hostile checks

1. **No full-source ZR/ZF extension.** All `v,e,h,s_Z` quantities belong to the
   nonisolated positive-contact core.  Contact-isolated source points remain present.
2. **Outer walk versus convex perimeter.** The proof uses only the safe inequality
   `per(F)<=b`, with bridge occurrences retained.  It does not identify the outer walk
   with the convex hull boundary.
3. **Near-disk input.** The limit `per(F)/D->pi` is used only in the Type-II full-core
   branch, where canonical Sections 79--80 supply Hausdorff convergence of the scaled
   force hull to the disk.  It is not asserted in the macroscopic-container branch.
4. **Exceptional faces.** No local area or phase charge per face is assumed.  Only the
   exact combinatorial inequality `Q>=f` is used, so the even-hole zero-phase
   regression is fully compatible with the proof.
5. **Diameter topology.** Both Woodall branches and arbitrary `s_Z>=0` are retained;
   their contributions appear with positive coefficients in (3.5).
6. **No carrier decimal.** No `mu` estimate enters the proof.

**Disposition:** proved proof-only theorem.  C-II remains open.