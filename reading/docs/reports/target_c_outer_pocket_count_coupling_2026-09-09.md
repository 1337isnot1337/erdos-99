> Generated reading edition · [exact source](../../../docs/reports/target_c_outer_pocket_count_coupling_2026-09-09.md) · source SHA-256 `b9ffadc70d09b6de88e9aa9534e8d9dec7a339a9cadba28ae8c24b90e247f296`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-7A9C79D297BA","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — outer-pocket count and complexity coupling

**Date:** 2026-09-09  
**Run type:** exact OP/HB synthesis  
**Target:** Target C C-II after ZF  
**Depends on:** OP hull augmentation and convex-pocket theorem, HB loaded-contact coupling, DB, GU  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

HB proves `x_B+e_BB>=q`. The OP hull augmentation gives a stronger geometric localization. Let `a` be the number of force-hull sides that are absent from the positive contact graph and hence are added in OP. OP proves that exactly `a` new bounded convex outer pockets are created.

The same identities show that `x_B` has an exact decomposition into pocket count plus excess pocket degree.

---

## 1. Missing hull sides versus loaded-loaded contacts

There are `q` force-hull sides between consecutive loaded vertices. Exactly `a` are missing contact edges. Every one of the other `q-a` hull sides is a unit contact joining two loaded terminals. These edges are distinct and are counted by `e_BB`.

### Theorem PC.1

```math
\boxed{e_{BB}\ge q-a.}
\tag{PC.1}
```

Equivalently,

```math
\boxed{a+e_{BB}\ge q.}
\tag{PC.2}
```

Since every missing hull side forces the corresponding outer-walk interval to have length at least two, `a<=x_B`; thus PC.1 implies HB.2 but is geometrically sharper: the deficit is counted by actual missing hull sides, not arbitrary repeated outer-walk occurrences.

---

## 2. Exact pocket-complexity decomposition of `x_B`

OP proves:

- the number of new convex outer pockets is
  ```math
  p=a;
  
  ```
- if `k_P` is the number of graph-boundary edges of pocket `P`, then
  ```math
  \sum_P k_P=B+2a-q,
  
  ```
  where `B=b=q+x_B`.

Therefore

```math
\sum_P k_P=x_B+2a.
\tag{PC.3}
```

Subtract `3a`, using `p=a`:

### Theorem PC.2 — exact outer-excess decomposition

```math
\boxed{
x_B
=a+
\sum_{P}(k_P-3).
}
\tag{PC.4}
```

Every new pocket is a strict convex polygon, hence `k_P>=3` and every term is nonnegative.

Thus outer-walk excess has only two sources:

1. one mandatory unit for each missing hull side / convex outer pocket;
2. additional boundary complexity above triangular pockets.

There is no third bridge-excursion currency hidden in `x_B`. In particular, if every hull side is already a contact (`a=0`), then OP makes the original graph 2-connected and PC.4 forces `x_B=0`.

This corrects a tempting mental model in which arbitrarily many doubled bridge excursions could coexist with a complete contact hull cycle. C51+OP forbid that situation.

---

## 3. Exact relations with the HB theorem

From PC.4,

```math
a\le x_B.
\tag{PC.5}
```

Combining PC.1 and PC.5 recovers

```math
e_{BB}\ge q-a\ge q-x_B.
```

But PC.1 is often stronger because it says a small `e_BB` requires **many distinct convex pockets**:

```math
\boxed{a\ge q-e_{BB}.}
\tag{PC.6}
```

The HB/PC picture is therefore

```text
few loaded-loaded hull contacts
    -> many missing hull sides
    -> many distinct convex OP pockets;

few OP pockets
    -> almost every hull side is a unit loaded-loaded contact.
```

---

## 4. GU low-surplus branch has linearly many convex pockets

GU defines

```math
\lambda_2
=\limsup\frac{e_{BB}+2s_C}{D}
```

and its macroscopic-gap branch is active when

```math
\lambda_2<\lambda_*
:=\sqrt{\frac{\sqrt3}{\pi}}
=0.7425152492\ldots .
```

Since `e_BB<=e_BB+2s_C`, PC.6 gives

```math
\frac aD
\ge
\frac qD-\frac{e_{BB}}D.
```

DB gives `liminf q/D>=2rho`, where

```math
\rho=0.7390851332\ldots .
```

Hence along every GU low-surplus subsequence,

```math
\boxed{
\liminf\frac aD
\ge
2\rho-\lambda_*
=0.7356550172\ldots .
}
\tag{PC.7}
```

So the GU branch can now be stated geometrically as follows:

> A low `e_BB+2s_C` survivor has a quadratic attachment-cell gap and at least `0.735655 D-o(D)` distinct strict convex outer pockets cut off by missing force-hull sides, unless GU localizes the gap instead to a giant bounded exceptional face.

This is stronger than the previous statement `x_B>=0.735655D-o(D)`: PC.7 counts distinct pockets rather than repeated edge occurrences.

---

## 5. Pocket perimeter and area identities retained from OP

Let `L_add` be the total length of the `a` missing hull sides and `P_F=per(F)`. OP gives

```math
P_F=(q-a)+L_{add},
\tag{PC.8}
```

and

```math
\sum_P L_P
=B+2L_{add}-P_F.
\tag{PC.9}
```

Using `B=q+x_B` and PC.8,

```math
\boxed{
\sum_P L_P
=x_B+2a+P_F-q.
}
\tag{PC.10}
```

Together with PC.4 this is an exact finite description of the number, combinatorial degree, and total perimeter of the convex outer pockets.

OP also gives

```math
\sum_P area(P)=H_{out},
\tag{PC.11}
```

where `H_out` is the outer contact-face area inside the force hull.

If GU's localization lands in the outer-pocket alternative

```math
H_{out}\ge gD^2
```

for some fixed `g>0`, then `a<=q<=pi D` implies at least one individual OP pocket has

```math
\boxed{
area(P)\ge\frac g\pi D.
}
\tag{PC.12}
```

Thus the diffuse GU outer region can always be localized to a single strict convex outer pocket of at least linear area. This is still far below the `D^2` scale and is not itself contradictory.

---

## 6. Regression audit

- A triangular pocket has `k_P=3` and contributes exactly one unit to `x_B`, through its missing hull side.
- A long thin convex pocket can have arbitrarily small area relative to the square of its contact-chain length; PC does not assert a uniform area per pocket.
- Regular shell: `a=x_B=0`, `e_BB=q`; equality in PC.2 and PC.1.
- Pure matching/rhombic hull cycle: again `a=x_B=0`, outside the low-contact pocket branch.
- Bridge excursions with a complete hull contact cycle are not a valid regression: OP's 2-connectivity theorem makes `a=0` imply `x_B=0`.

---

## 7. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| `a+e_BB>=q` | proved | nonmissing hull sides are distinct loaded-loaded unit contacts |
| `x_B=a+sum(k_P-3)` | proved | OP exact edge-incidence identity |
| `a<=x_B` | proved | PC.4 |
| GU low-surplus gives `a>=0.735655D-o(D)` | proved | PC.6 + DB + GU threshold |
| outer GU area gives one pocket of area `Omega(D)` | proved | `a<=q<=pi D` |
| linear pocket count forces quadratic pocket area | false/not claimed | pockets may be thin |
| Level I | open | need a stability/capacity theorem for the linear family of convex pockets or the giant-face alternative |

---

## 8. Next target

The low-surplus branch is now sharply localized:

1. `Omega(D)` distinct convex OP pockets, with exact total degree/perimeter identities PC.4 and PC.10; and
2. an independent quadratic attachment-cell gap from GU.

The next useful theorem should couple these rather than charging pockets one by one. A scalar lower area per pocket is impossible in general; the proof must use the shared loaded hull, contact equilibrium along the pocket chains, or global source capacity.
