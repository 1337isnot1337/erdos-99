> Generated reading edition · [exact source](../../../docs/reports/target_c_extreme_circuit_train_branching_2026-09-10.md) · source SHA-256 `baa0ed0437158fe2a8fe897f6b23b442a0fa9ebee4df0860aa20310cafae7ec4`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-34E25A9AD7B9","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — train stability and DB feedback on extreme positive circuits

**Date:** 2026-09-10  
**Repository state:** PR #178 after EDB/LI  
**Run type:** exact selected-support train theorem / asymptotic branching transfer  
**Target:** Target C, C-II after ZF  
**Depends on:** DT finite train theorem, C77 train-intersection triangle-freeness, EC selected face identity, CT selected terminal ledger, EDB selected difference-body bound  
**External input:** none  
**Computation:** decimal value of the already-defined NB root only

## LEVEL I STATUS

`STILL OPEN`.

The full-support NM/NB train argument does not fundamentally require the full actual
contact graph. DT is explicitly stated for **any** finite connected straight-line
unit-contact graph of a unit-separated triangle-free planar point set. Therefore it
applies to the positive contact graph of an extreme normalized KKT circuit.

For such an extreme circuit write

```math
q_*=|B_*|,
\qquad
r_*:=2h_*-q_*,
\qquad
\sigma_*:=2v_*-2-(e_*+h_*).
```

Let `x_*=b_*-q_*`, and write the selected bounded nonquadrilateral face defect as

```math
Q_*=f_*+g_*.
```

Then the exact selected train-end inequality is

```math
\boxed{
h_*+\sigma_*-2
\le2x_*+3f_*+g_*.
}
\tag{ENM.1}
```

Using CT/EC,

```math
\boxed{
r_*=x_*+Q_*-2\sigma_*\ge0.}
\tag{ENM.2}
```

Consequently

```math
\boxed{
3r_*+5\sigma_*\ge h_*-2.
}
\tag{ENM.3}
```

The EDB defect-dependent perimeter inequality gives the stronger feedback estimate

```math
\boxed{
r_*
\ge
D\cos\bigl((h_*-1)a_D\bigr)
-\frac52\sigma_*-rac32,
\qquad
a_D=\arcsin\frac1{2D}.
}
\tag{ENB.1}
```

Hence if

```math
y:=\lim h_*/D,
\qquad
s:=\lim \sigma_*/D,
\qquad
r:=\lim r_*/D,
```

along a convergent subsequence, then

```math
\boxed{
r
\ge
\max\left\{
0,
\frac{y-5s}{3},
\cos(y/2)-\frac52s
\right\}.
}
\tag{ENB.2}
```

In particular, every low-degeneracy extreme circuit with

```math
\kappa_*=o(D)
```

has `sigma_*=o(D)` by CT, so EDB and ENB give simultaneously

```math
\boxed{
\frac{h_*}{D}\ge2\rho-o(1),
\qquad
\frac{2h_*-q_*}{D}\ge c_*-o(1),
}
\tag{ENB.3}
```

where

```math
\rho=\cos\rho,
\qquad
c_*=\cos(3c_*/2)=0.6099043189\ldots .
```

Thus a low-`kappa_*` extreme circuit inherits both principal full-support geometric
constants: DB-scale diameter-edge density and NB-scale diameter branching.

---

## 1. DT train count on the selected contact graph

DT applies to a finite connected triangle-free unit-contact graph, with no full-support
KKT hypothesis. The extreme selected positive contact graph satisfies exactly those
conditions.

Let `R_*` be its number of bounded quadrilateral faces and `T_*` its train count, with
edges incident to no quadrilateral counted as singleton trains as in DT. Then

```math
\boxed{
T_*=e_*-2R_*
=\frac{b_*+Q_*}{2}+2f_*.
}
\tag{1.1}
```

EC gives

```math
b_*+Q_*=2h_*+2\sigma_*.
```

Therefore

```math
\boxed{T_*=h_*+\sigma_*+2f_*.}
\tag{1.2}
```

This is the selected-circuit replacement for the full NM identity
`T=h-s_Z+2f`.

---

## 2. Bad outer intervals and exceptional train ends

Order the selected positive diameter endpoints `B_*` cyclically on the selected force
hull `F_*`. Split a distinguished pass of the selected outer contact-face walk into
subwalks between consecutive vertices of `B_*`.

Exactly as in NM, if an interval has length one, its unique contact edge is the convex
hull side. If an interval has length at least two, call it bad. Since

```math
b_*=q_*+x_*,
```

the number of outer-walk edge occurrences in bad intervals is at most

```math
\boxed{2x_*.}
\tag{2.1}
```

For bounded exceptional faces the exact total boundary incidence is

```math
5f_*+g_*.
\tag{2.2}
```

A train with both ends on good unit hull sides is a good train. Its two terminal hull
sides are parallel. Two distinct good trains have alternating boundary endpoint pairs,
so their embedded train tracks cross. C77/DT says the train-intersection graph is
triangle-free. Therefore at most two trains are good.

Every other train consumes at least one bad outer or exceptional-face end. Hence

```math
T_*-2\le2x_*+5f_*+g_*.
\tag{2.3}
```

Insert (1.2):

```math
h_*+\sigma_*+2f_*-2
\le2x_*+5f_*+g_*,
```

which rearranges to ENM.1.

No full actual row, loaded degree cap, or full `s_Z` identity is used.

---

## 3. Selected branching identity

Woodall gives

```math
d_*:=q_*-h_*\ge0.
```

CT gives

```math
q_*+2\sigma_*=x_*+Q_*+2d_*.
```

Since

```math
r_*=2h_*-q_*=q_*-2d_*,
```

we obtain

```math
\boxed{r_*=x_*+Q_*-2\sigma_*.}
\tag{3.1}
```

The left side is nonnegative because every selected diameter endpoint has positive
diameter degree, so `q_*<=2h_*`.

---

## 4. Selected NM inequality

From ENM.1,

```math
h_*+\sigma_*-2
\le2x_*+3f_*+g_*.
\tag{4.1}
```

Using `Q_*=f_*+g_*` and (3.1),

```math
3r_*+6\sigma_*
=3x_*+3f_*+3g_*.
```

The right side dominates the right side of (4.1), because

```math
(3x_*+3f_*+3g_*)-(2x_*+3f_*+g_*)
=x_*+2g_*\ge0.
```

Thus

```math
h_*+\sigma_*-2
\le3r_*+6\sigma_*.
```

Rearranging proves ENM.3:

```math
3r_*+5\sigma_*\ge h_*-2.
```

Equivalently,

```math
\boxed{
r_*\ge\frac{h_*-2-5\sigma_*}{3}.}
\tag{4.2}
```

---

## 5. Feed EDB's face defect back into train stability

A sharper selected analogue of NB follows by retaining `Q_*` rather than replacing
all defect currencies at once.

From (3.1),

```math
x_*=r_*-Q_*+2\sigma_*.
```

Therefore

```math
2x_*+3f_*+g_*
\le2x_*+3Q_*
=2r_*+Q_*+4\sigma_*.
\tag{5.1}
```

ENM.1 yields

```math
h_*+\sigma_*-2
\le2r_*+Q_*+4\sigma_*.
```

Hence

```math
h_*-2
\le2r_*+Q_*+3\sigma_*.
\tag{5.2}
```

EDB gives

```math
Q_*
\le
h_*+2\sigma_*+1
-2D\cos((h_*-1)a_D).
\tag{5.3}
```

Insert (5.3) into (5.2) and cancel `h_*`:

```math
-2
\le2r_*+5\sigma_*+1
-2D\cos((h_*-1)a_D).
```

Therefore

```math
2r_*
\ge
2D\cos((h_*-1)a_D)-5\sigma_*-3,
```

which proves ENB.1.

---

## 6. Asymptotic optimization

Let

```math
h_*/D\to y,
\qquad
\sigma_*/D\to s,
\qquad
r_*/D\to r.
```

Divide (4.2) and ENB.1 by `D`. Since

```math
(h_*-1)a_D\to y/2,
```

we get

```math
r\ge\frac{y-5s}{3},
\qquad
r\ge\cos(y/2)-\frac52s,
\qquad
r\ge0.
```

This is ENB.2.

If `kappa_*=o(D)`, CT gives `sigma_*=o(D)`, so `s=0`. EDB already gives

```math
y\ge2\rho.
```

Then

```math
r\ge\max\{y/3,\cos(y/2)\}.
```

The full NB report solved this one-variable minimization exactly: the minimum over
`y>=0` occurs at the unique crossover

```math
y/3=\cos(y/2),
```

or `y=3c_*`, and equals

```math
c_*=0.6099043189\ldots .
```

Since `3c_*=1.8297...>2rho`, the EDB lower restriction `y>=2rho` does not change the
minimum. This proves ENB.3.

---

## 7. Low-degeneracy selected normal form

Combine ENB.3 with LI. If

```math
\kappa_*=o(D),
```

then simultaneously

```math
\boxed{
q_*=q-o(D),
\qquad
h_*\ge(2\rho-o(1))D,
\qquad
2h_*-q_*\ge(c_*-o(1))D,
\qquad
\sigma_*=o(D).
}
\tag{7.1}
```

Thus the selected positive diameter graph is not near a matching: it has a fixed
linear amount of degree excess even after passing to one extreme circuit.

At the full DB endpoint `h/D->2rho`, LI further gives `h-h_*=o(D)`, so the selected
circuit captures almost every full actual diameter edge while retaining ENB branching.

---

## 8. Regressions and scope

- ESR regular even shells have `sigma/D->pi/2`; the `-5sigma` terms make ENM/ENB
  deliberately weak there. They are not falsely excluded.
- A straight-chain extreme has `sigma=Theta(D)` and lies in the same allowed
  high-degeneracy regime.
- DT explicitly includes bridges, disconnected rhombic-face regions, and edges between
  exceptional faces. No pure-disk assumption is imported.
- The selected contact graph can omit full actual contacts. The proof uses only its own
  unit edges, faces, outer walk, and selected convex force hull.
- No individual stress-weight lower bound is used.

---

## 9. Exact next target

The low-`kappa_*` branch now has almost the full loaded boundary, DB-scale diameter
support, and NB-scale branching on **one rigidity circuit**. Further scalar
`h_*`,`q_*` optimization is unlikely to close it by itself.

The next useful theorem is a selected/full defect comparison: show that a circuit with
(7.1) and `kappa_*=o(D)` inherits enough of the full contact-face or full-source area
structure to contradict the existing `s_Z=0` endpoint inequalities, or else forces
`kappa_*=Omega(D)`.

The complementary high-`kappa_*` branch remains an ensemble problem; ESR shows it
cannot be eliminated from one selected circuit in isolation.

---

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

DT applies to every extreme selected positive contact graph. Its train count is
    T_*=(b_*+Q_*)/2+2f_*=h_*+sigma_*+2f_*
by EC. Repeating NM's bad-end argument gives
    h_*+sigma_*-2 <=2x_*+3f_*+g_*.
CT gives selected branching
    r_*=2h_*-q_*=x_*+Q_*-2sigma_* >=0.
Therefore
    3r_*+5sigma_* >= h_*-2.

Using EDB's
    Q_* <= h_*+2sigma_*+1
           -2D cos((h_*-1)asin(1/(2D)))
inside the train inequality gives
    r_* >= D cos((h_*-1)asin(1/(2D)))
           -(5/2)sigma_*-3/2.
Hence for limits y=h_*/D, s=sigma_*/D, r=r_*/D,
    r >= max{0,(y-5s)/3,cos(y/2)-(5/2)s}.

If kappa_*=o(D), then s=0; EDB gives y>=2rho and the NB optimization gives
    r >= c_*=0.6099043189... .
Together with LI, one low-degeneracy extreme already contains almost every loaded
terminal, DB-scale diameter density, and NB-scale branching.
```
