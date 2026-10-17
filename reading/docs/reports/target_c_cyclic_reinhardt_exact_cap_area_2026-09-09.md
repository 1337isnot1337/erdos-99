> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_reinhardt_exact_cap_area_2026-09-09.md) · source SHA-256 `d054964d71ca796d93e5e1f322a83f140acd47f08b00613e3806d225a97e65d9`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-AD41F741E102","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — exact area gap between the Reinhardt completion and force hull

**Date:** 2026-09-09  
**Repository branch:** PR #118 after RE/RC/RD/FB/WG  
**Run type:** exact convex-geometry bookkeeping  
**Target:** cyclic primitive endpoint, `d_H=0`  
**Depends on:** RE exact Reinhardt relation and FB cap decomposition  
**External literature:** none  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

FB identifies `R\setminus F` as the union of the circular caps cut off by the `q` unit sides of the exact Reinhardt force hull. Because RE fixes both the common radius and the common central angle, the total cap area is explicit.

### Theorem CA — exact completion-minus-hull area

Let `R` be the width-`D` Reuleaux completion of the exact cyclic `d_H=0` force hull `F`. Then

```math
\boxed{
\operatorname{area}(R)-\operatorname{area}(F)
=
\frac{qD^2}{2}
\left(
\frac\pi q-\sin\frac\pi q
\right).}
\tag{CA.1}
```

Using

```math
D=\frac1{2\sin(\pi/(2q))},
```

this can also be written

```math
\boxed{
\operatorname{area}(R)-\operatorname{area}(F)
=
\frac{\pi}{8\sin^2 x}
\left(1-\frac{\sin x\cos x}{x}\right),
\qquad x:=\frac\pi{2q}.}
\tag{CA.2}
```

In particular,

```math
\boxed{
\operatorname{area}(R)-\operatorname{area}(F)
=
\frac\pi{12}
+
\frac{\pi^3}{360q^2}
+
\frac{\pi^5}{10080q^4}
+O(q^{-6}).}
\tag{CA.3}
```

Thus the entire curved completion outside the polygonal force hull has only constant area:

```math
\boxed{
\operatorname{area}(R)-\operatorname{area}(F)
\to\frac\pi{12}.}
\tag{CA.4}
```

This is much sharper than the earlier `O(D)` force-area comparisons.

---

## 1. One side gives one circular segment

Take consecutive force-hull vertices `p_i,p_{i+1}`. RE gives

```math
|p_i-p_{i+1}|=1,
```

and the corresponding boundary portion of `R` is a radius-`D` minor circular arc with central angle

```math
\delta=2\arcsin\frac1{2D}=\frac\pi q.
```

The area between a radius-`D` minor arc of angle `delta` and its chord is the circular-segment area

```math
A_{cap}
=\frac{D^2}{2}(\delta-\sin\delta).
\tag{1.1}
```

FB shows that the `q` such cap interiors are disjoint and their union is exactly `R\setminus F`. Hence

```math
\operatorname{area}(R)-\operatorname{area}(F)
=qA_{cap},
```

which proves CA.1. `square`

---

## 2. Exact simplification in the Reinhardt parameter

Put

```math
x=\frac\pi{2q},
\qquad
\delta=2x.
```

RE gives

```math
D=\frac1{2\sin x}.
```

Substitute into CA.1:

```math
\begin{aligned}
q\frac{D^2}{2}(2x-\sin2x)
&=
\frac{q}{8\sin^2x}
(2x-2\sin x\cos x)\\
&=
\frac{qx}{4\sin^2x}
\left(1-\frac{\sin x\cos x}{x}\right).
\end{aligned}
```

Since `qx=pi/2`, this is CA.2.

---

## 3. Expansion

The elementary Taylor expansions give

```math
\frac{1}{\sin^2x}
=\frac1{x^2}+\frac13+\frac{x^2}{15}+O(x^4),
```

and

```math
1-\frac{\sin x\cos x}{x}
=\frac{2}{3}x^2-\frac{2}{15}x^4+\frac{4}{315}x^6+O(x^8).
```

Multiplying in CA.2 yields

```math
\operatorname{area}(R)-\operatorname{area}(F)
=
\frac\pi{12}
+
\frac{\pi}{90}x^2
+
\frac\pi{630}x^4
+O(x^6).
```

Using `x=pi/(2q)` gives CA.3.

---

## 4. Consequence for Reuleaux-core area bounds

Let `nu` be the odd Reuleaux/diameter-cycle core size from RC. Firey--Sallee gives

```math
\operatorname{area}(R)
\le
A_\nu^{reg}(D)
:=
\frac{D^2}{2}
\left(
\pi-\nu\tan\frac\pi{2\nu}
\right).
\tag{4.1}
```

CA therefore gives the direct force-hull upper bound

```math
\boxed{
\operatorname{area}(F)
\le
A_\nu^{reg}(D)-C_q,}
\tag{CA.5}
```

where

```math
C_q
:=
\frac{qD^2}{2}
\left(
\frac\pi q-\sin\frac\pi q
\right)
=\frac\pi{12}+O(q^{-2}).
```

Combining with the exact Wegner lower bound WG.1 gives the finite necessary inequality

```math
\boxed{
A_\nu^{reg}(D)-C_q
\ge
\frac{\sqrt3}{2}(n-1)
-\frac q2
+\frac{2-\sqrt3}{4}
\left\lceil\sqrt{12n-3}-3\right\rceil.}
\tag{CA.6}
```

This is a sharper finite version of the asymptotic core-growth bound: the completion-to-hull conversion loses only the explicit constant `C_q`, rather than a perimeter-scale error.

---

## 5. Why CA matters

The remaining exact cyclic branch has two natural geometric objects:

1. the polygonal source/force hull `F`, on which finite packing theorems such as Wegner act directly;
2. the constant-width Reuleaux completion `R`, on which Firey--Sallee and Reuleaux-variation theorems act naturally.

CA shows that these two area currencies differ by only

```math
\frac\pi{12}+o(1).
```

Therefore any future improvement of order `D`, `sqrt(D)`, or even a fixed constant in a Reuleaux-area estimate transfers essentially unchanged to the actual source hull.

The completion is not hiding an `O(D)` area reservoir.

---

## 6. Regression audit

### Regular odd shell

For the regular odd shell, `R` is the regular Reuleaux `q`-gon and the formula reduces to the obvious sum of `q` congruent circular segments.

### Nonregular Reinhardt polygon

No regularity is used. Every force-hull side is still a unit chord on one radius-`D` completion arc, so every cap has the same segment area even though several consecutive caps may lie on the same defining Reuleaux circle.

### Overlap

Cap interiors cannot overlap because `F` is convex, each cap lies beyond one distinct side of `F`, and FB already identifies their union with `R\setminus F`.

---

## 7. Next theorem

CA reduces the remaining population problem to comparing two sharp finite inequalities without a large translation error:

```math
\text{Wegner lower bound on }\operatorname{area}(F)
```

versus

```math
\text{Reuleaux-composition upper bound on }\operatorname{area}(R)
-C_q.
```

The next useful step is therefore a composition-sensitive upper bound for a Reinhardt Reuleaux polygon, stronger than the regular-`nu` envelope whenever its dihedral composition is uneven. Because the loss `C_q` is constant-order, even a sublinear composition penalty can now survive the transfer back to `F`.

---

## 8. Promotion recommendation

**Hold as report pending independent audit.**

The proof is elementary downstream of RE/FB. No new external dependency is introduced.

---

## 9. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

In exact cyclic d_H=0, each of the q force-hull unit sides is a chord of a radius-D
Reuleaux-completion arc with central angle delta=pi/q. The q circular caps are
disjoint and exactly fill R\F. Hence
  area(R)-area(F)
    = q D^2/2 (pi/q - sin(pi/q)).
With x=pi/(2q), D=1/(2sin x):
  = pi/[8 sin^2 x] * [1-sin x cos x/x]
  = pi/12 + pi^3/(360q^2)+pi^5/(10080q^4)+O(q^-6).

Thus completion-to-force-hull area loss is only constant, tending pi/12.
If nu is the Reuleaux core size, Firey-Sallee plus Wegner gives the finite inequality
  A_reg_nu(D)-C_q
    >= sqrt3/2(n-1)-q/2
       +(2-sqrt3)/4 ceil(sqrt(12n-3)-3).

Next: composition-sensitive Reuleaux area penalty. Any o(D) improvement now transfers
to F without being swallowed by an O(D) completion error.
```
