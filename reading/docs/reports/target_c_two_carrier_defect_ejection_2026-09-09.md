> Generated reading edition · [exact source](../../../docs/reports/target_c_two_carrier_defect_ejection_2026-09-09.md) · source SHA-256 `6a4d563930e793339bdbb58065592096f78ae91adca46d5869da4cfb5a7cbeb5`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-D97D635B7BA9","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cap-minimal full-core ledger ejects two diameter units of face defect from the giant carriers

**Date:** 2026-09-09  
**Repository branch:** `research/post-uf-attachment-fill-2026-09-09`  
**Run type:** exact asymptotic ledger sharpening  
**Target:** SI/TS full-core cap-minimal near-circle endpoint  
**Depends on:** NC, NBd, SI, ZU, ZT  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

SI first combined the semicircle internal-perimeter cost with UF and obtained a positive lower bound on face defect outside the two giant carrier interiors. The exact post-ZF terminal ledger gives a much stronger result; UF is not needed.

Let `Q_int=Q_1+Q_2` be the bounded-face degree excess internal to the two TS semicircle-scale harmonic components. In the full-core cap-minimal regime

```math
S/D\to2,
\qquad
x_B=o(D),
\qquad
q/D\to\pi,
```

one has

```math
\boxed{
Q\ge Q_{int}+(2-o(1))D.
}
\tag{TE.1}
```

Equivalently,

```math
\boxed{
Q-Q_{int}\ge(2-o(1))D.
}
\tag{TE.2}
```

Thus at least two full source-diameter units of exceptional-face defect are forced **outside** the interiors of the two positive-density semicircle carriers.

This strictly supersedes SI's earlier numerical consequence `Q_B>=0.248576D`, although TE.2 does not by itself say all two units are incident to the loaded boundary: some may lie in the internal faces of the remaining `o(D^2)`-population harmonic components.

---

## 1. Semicircle perimeter cost inside NBd

SI proves

```math
\boxed{
R_I
\ge
\left(\frac\pi2-1-o(1)\right)D
+\frac12Q_{int}.
}
\tag{1.1}
```

NC proves

```math
E_{BB}=o(D).
\tag{1.2}
```

NBd gives the exact boundary budget

```math
S+R_I+s_B+2E_{BB}+3c_I+s_C=q+2x_B.
\tag{1.3}
```

In the cap-minimal near-circle endpoint,

```math
S=(2+o(1))D,
\qquad
q=(\pi+o(1))D,
\qquad
x_B=o(D).
```

Insert (1.1)--(1.2) into (1.3), discard `s_B>=0`, and rearrange:

```math
\boxed{
3c_I+s_C+\frac12Q_{int}
\le
\left(\frac\pi2-1+o(1)\right)D.
}
\tag{1.4}
```

This is already stronger than the SI bound `Q_int<=(pi-2+o(1))D` because it keeps the component-count and pinned-stress currencies instead of discarding them.

---

## 2. Convert to the mixed/diameter defect `k=d_H+s_Z`

ZU gives exactly

```math
c_I+e_{BB}+s_C=q-2+k,
\qquad
k:=d_H+s_Z.
\tag{2.1}
```

NC gives

```math
e_{BB}=q+o(D)
```

in the near-circle branch. Hence

```math
\boxed{
 k=c_I+s_C+o(D).
}
\tag{2.2}
```

Since `c_I>=0`,

```math
c_I+s_C\le3c_I+s_C.
```

Equation (1.4) therefore yields

```math
\boxed{
 k
\le
\left(\frac\pi2-1+o(1)\right)D
-\frac12Q_{int}.
}
\tag{2.3}
```

No stress coefficient lower bound enters this estimate.

---

## 3. ZT forces the complementary face defect

ZT gives the exact terminal partition

```math
q=x_B+Q+2k.
\tag{3.1}
```

Thus

```math
Q=q-x_B-2k.
\tag{3.2}
```

Use

```math
q=(\pi+o(1))D,
\qquad
x_B=o(D),
```

and insert (2.3):

```math
\begin{aligned}
Q
&\ge
(\pi-o(1))D
-2\left[
\left(\frac\pi2-1+o(1)\right)D
-\frac12Q_{int}
\right]\\
&=
Q_{int}+(2-o(1))D.
\end{aligned}
```

This proves TE.1--TE.2.

The exact constant two comes from a clean cancellation:

```math
\pi-2\left(\frac\pi2-1\right)=2.
```

---

## 4. Interpretation of the expelled defect

Every bounded face of the full contact graph falls into one of two classes:

1. all boundary vertices lie in one unloaded component `I_r`, in which case it is an internal face of `C[I_r]`;
2. the face boundary contains at least one loaded terminal.

Let

```math
Q_{small}
:=
\sum_{r\ge3}Q_r
```

be the internal face defect of all harmonic components other than the two TS carriers, and let `Q_B` be the defect on bounded faces incident to `B_+`. Then

```math
Q=Q_{int}+Q_{small}+Q_B.
\tag{4.1}
```

TE.2 is therefore the exact asymptotic alternative

```math
\boxed{
Q_{small}+Q_B\ge(2-o(1))D.
}
\tag{4.2}
```

TS proves the small components carry only `o(D^2)` vertices, but this does **not** yet imply `Q_small=o(D)`: a linear collection of bounded-size exceptional components can carry linear face defect while having subquadratic population.

Thus the next target is sharply separated:

- either the small-component family itself carries `Omega(D)` exceptional-face defect;
- or the loaded boundary/interface carries `Omega(D)` exceptional-face defect.

Both are source-boundary-order phenomena.

---

## 5. Component-count interaction

Equation (1.4) also constrains the first alternative. Since every additional nonempty unloaded component contributes one unit to `c_I`, a linear number of small components consumes three units of the same boundary budget per component.

For example, if

```math
Q_{int}=o(D),
```

then

```math
\limsup\frac{c_I}{D}
\le
\frac13\left(\frac\pi2-1\right)
=0.1902654423\ldots .
```

A future theorem of the form

```math
Q_r\le C+o(1)
```

for graph-small harmonic components would immediately turn (4.2) into a quantitative loaded-interface lower bound. No such universal bound is asserted here; a component of sublinear diameter may still contain many exceptional faces.

---

## 6. Stronger full-core face-defect floor

Discarding `Q_int>=0` from TE.1 gives the simple global consequence

```math
\boxed{
Q\ge(2-o(1))D
}
\tag{6.1}
```

throughout the cap-minimal full-core branch.

This improves the UF full-core lower bound

```math
Q\ge
\left(
\frac\pi5+\frac45\sqrt\Delta-o(1)
\right)D
= (1.3901687762\ldots-o(1))D
```

without using UF's exposed-train estimate beyond the near-circle/full-core/cap-minimal setup that produced TS.

The improved value is still compatible with ZT because `q/D->pi`; it forces

```math
\limsup\frac{k}{D}
\le\frac{\pi-2}{2}
=0.5707963268\ldots .
```

---

## 7. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| budget inequality (1.4) | proved | SI + NBd + NC + `S/D->2` |
| `k=c_I+s_C+o(D)` | proved | ZU + NC |
| `Q>=Q_int+2D-o(D)` | proved | ZT substitution |
| global cap-minimal `Q>=2D-o(D)` | proved | discard `Q_int` |
| all expelled defect touches `B_+` | not proved | small components may carry linear internal defect |
| Level I | still open | defect ejection is not yet a contradiction |

---

## 8. Next target

TE reduces the cap-minimal full-core branch to a **defect-location dichotomy**:

```math
Q_{small}+Q_B\ge(2-o(1))D.
```

The two most direct continuations are:

1. **small-component efficiency:** bound internal face defect per unit of `3c_I+R_I` for components whose total graph diameter is `o(D)`;
2. **loaded-interface efficiency:** bound face defect incident to an almost-complete convex unit hull cycle using the one remaining contact slot at each loaded terminal.

Either theorem can feed into the same exact budget (1.4). A coefficient strong enough to show that two units of expelled face defect cost more than `(pi/2-1)D` would close the cap-minimal full-core branch.
