> Generated reading edition · [exact source](../../../docs/reports/target_c_full_source_annular_capacity_gap_2026-09-11.md) · source SHA-256 `0b9766b06e868cc1a25f677710654986b1be4424e4f301c490caf29370e31158`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-F9FA14B1BD2C","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_full_source_annular_capacity_gap_2026-09-11.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=a79890c407eb1e62022787151434e6f7bfda8e80; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — full-source annular capacity gap after the post-ZF area floor

**Date:** 2026-09-11  
**Repository state:** `053e1e1b85643b738b4cde306838d150ea325783`  
**Run type:** exact full-source capacity synthesis  
**Target:** Target C C-II, force-bulk obstruction  
**LEVEL I STATUS:** STILL OPEN

This report combines the external-annulus estimate with Oler on the points inside
the force hull. It applies to the general C-II source, including contact-isolated
points in the force hull. The result is a whole-source upper bound, but its
constants leave a positive gap above the triangular packing density. That gap is
the exact failed implication; it is not treated as a contradiction.

## 1. Setup

Let `A` be the C65 lexicographically normalized source, `D` its diameter, `K=conv A`
the full source hull, and `F` the force hull of the positive contact core. Write

```math
 A_F=\operatorname{area}F,
 \qquad A_K=\operatorname{area}K.
```

Every non-core source point is contact-isolated and every positive contact-core
vertex lies in `F`. Split the source as

```math
 A=(A\cap F)\sqcup(A\setminus F).
```

The split is geometric; no claim is made that the points in `A\cap F` are in the
positive core.

## 2. Two finite capacity inequalities

Oler applied to all source points in the convex container `F` gives

```math
 |A\cap F|\frac{\pi}{4}
 \le A_F+\frac12\operatorname{per}F+\frac\pi4.
```

Equivalently,

```math
 |A\cap F|
 \le \frac4\pi A_F+2\operatorname{per}F+1.
 \tag{2.1}
```

For the external part, Theorem EA (the external-annulus capacity theorem) applied
to `F subset K` and `X=A\setminus F` gives

```math
 |A\setminus F|\frac{\pi}{4}
 \le A_K-A_F+\frac12(\operatorname{per}K+\operatorname{per}F)+\frac\pi4,
```

so

```math
 |A\setminus F|
 \le \frac4\pi(A_K-A_F)
 +\frac2\pi(\operatorname{per}K+\operatorname{per}F)+1.
 \tag{2.2}
```

Adding (2.1) and (2.2), the `A_F` coefficient is the important term:

```math
 n
 \le \frac4\pi A_K
 -\left(\frac4\pi-\frac4\pi\right)A_F
 +O(D).
```

This direct sum does not improve ordinary Oler: the force-hull area cancels. To
retain a force-hull penalty, use the sharper Oler coefficient for the inside points
coming from the triangular cell form of the same inequality:

```math
 |A\cap F|\le \frac2{\sqrt3}A_F+\frac12\operatorname{per}F+1.
 \tag{2.3}
```

This is valid for the full set `A\cap F`, not only for the contact core. Adding
(2.2) to (2.3) gives

```math
 n\le \frac4\pi A_K
 -\left(\frac4\pi-\frac2{\sqrt3}\right)A_F
 +\frac12\operatorname{per}F
 +\frac2\pi(\operatorname{per}K+\operatorname{per}F)+2.
 \tag{2.4}
```

All boundary terms are `O(D)` because both `K` and `F` have diameter at most `D`.

## 3. Asymptotic consequence

Use the isodiametric and perimeter bounds

```math
 A_K\le\frac\pi4D^2,
 \qquad \operatorname{per}K,\operatorname{per}F\le\pi D.
```

Then (2.4) gives

```math
 \frac n{D^2}
 \le
 1-\kappa\frac{A_F}{D^2}+o(1),
 \qquad
 \kappa:=\frac4\pi-\frac2{\sqrt3}>0.
 \tag{3.1}
```

The post-ZF FSDB theorem gives

```math
 \liminf\frac{A_F}{D^2}
 \ge A_{FS}:=
 \frac{2\rho+\sin(2\rho)}4,
 \qquad \rho=\cos\rho.
 \tag{3.2}
```

Therefore every post-ZF source obeys

```math
 \limsup\frac n{D^2}
 \le 1-\kappa A_{FS}
 =0.9266870758\ldots .
 \tag{3.3}
```

The global minimum-diameter asymptotic is

```math
 \frac n{D^2}\longrightarrow
 \Delta:=\frac\pi{2\sqrt3}=0.9068996821\ldots .
 \tag{3.4}
```

The remaining numerical margin is

```math
 (1-\kappa A_{FS})-\Delta
 =0.0197873937\ldots>0.
 \tag{3.5}
```

Thus this whole-source capacity theorem does not close C-II.

## 4. Equivalent population formulation

The same calculation separates the two capacities. At the FSDB floor,

```math
 \frac2{\sqrt3}A_{FS}=0.7141486636\ldots,
 \qquad
 1-\frac4\pi A_{FS}=0.2125384122\ldots .
```

Hence the total source density can still fit within the formal capacities

```math
 0.7141486636+0.2125384122=0.9266870758,
```

while the required density is only `0.9068996821`. The annular theorem leaves a
formal `0.0197873937 D^2` capacity margin. This is why applying the annular bound
to all general C-II isolates does not produce the missing contradiction.

## 5. What would close the gap

Any one of the following would make (3.1) decisive:

1. a force-hull area floor
   
   ```math
   \frac{A_F}{D^2}>\frac{1-\Delta}{\kappa}=0.7853981633\ldots,
   ```

   which is the disk value and is unavailable in the forest branch;
2. a strict triangular-density loss for the contact-isolated points in either
   `F` or `K\\F` of at least `0.0197873937 D^2`;
3. a source-preserving transfer theorem that charges the interface between `F` and
   `K\\F` by a quadratic amount rather than the `O(D)` annular boundary term;
4. a global competitor reducing the diameter while retaining all source points.

The exact obstruction is therefore a second-order full-source packing inequality,
not a missing first-order area estimate.

## 6. Regression audit

- Contact-isolated points inside `F` are included in (2.3); they are not silently
  discarded.
- Points outside `F` are handled by the annular theorem, including points with no
  unit contacts.
- No hull saturation or secondary representative is added.
- The regular odd-shell filling remains a valid local regression because (3.1) is
  not strict enough to exclude it.
- The matching branch has a stronger pure-core estimate and is already excluded
  independently; this report concerns the unrestricted source split.

## 7. Classification

| Claim | Status | Reason |
|---|---|---|
| full-source split (2.4) | proved | Oler inside `F` plus EA outside `F` |
| post-ZF bound (3.3) | proved | FSDB and isodiametric/perimeter bounds |
| contradiction with `n/D^2 -> Delta` | false | margin (3.5) is positive |
| Level I settlement | not proved | second-order capacity gap remains |

**Promotion recommendation:** hold as report. It is a synthesis of established
capacity inputs and does not alter authoritative theorem status.

## 8. Compact handoff

```text
For every C65 post-ZF source, split A into points in F and outside F.
Oler in F plus external-annulus capacity outside F gives

    n <= (4/pi) area(K)
         - (4/pi - 2/sqrt(3)) area(F) + O(D).

FSDB gives area(F)/D^2 >= 0.6184708847..., hence

    limsup n/D^2 <= 0.9266870758...

but the required density is

    Delta=0.9068996821...

The exact failed implication leaves a gap 0.0197873937 D^2. Closing it
requires a second-order triangle-free/source-capacity theorem or a global
competitor. Contact-isolated points have been retained throughout.
```
