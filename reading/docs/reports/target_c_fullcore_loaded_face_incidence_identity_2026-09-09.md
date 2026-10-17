> Generated reading edition · [exact source](../../../docs/reports/target_c_fullcore_loaded_face_incidence_identity_2026-09-09.md) · source SHA-256 `f306f3d7ed030c8baa08b9cdace4d8eb41a48c518ac5640b98682855e0665ced`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 10 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-111F878F8CFD","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_fullcore_loaded_face_incidence_identity_2026-09-09.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=ce5181b244456c070cadd9b653008f3c35175cb6; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — loaded contact-degree slack is exactly the asymptotic loaded-face aggregation defect

**Date:** 2026-09-09  
**Repository branch:** `research/fullcore-interface-perimeter-2026-09-09`  
**Run type:** exact face-incidence stability theorem  
**Target:** arbitrary full-core near-circle survivor  
**Depends on:** AS exact full-minus-component face identity, SL total component outer-walk identity, NC loaded shell completion, C35 loaded degree cap  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

Let `F_B` be the number of all bounded contact faces incident to at least one loaded terminal, including quadrilateral faces. Let

```math
I_B:=\sum_{F\in\mathcal F_B}|V(F)\cap B|
```

be the loaded vertex-face incidence count, and for a loaded-interface face let `m_F` be the number of direct loaded-loaded unit shell sides on its boundary.

In every full-core near-circle survivor,

```math
\boxed{F_B=q-s_B+o(D)=e_{BI}+o(D),}
\tag{FI.1}
```

```math
\boxed{I_B-2F_B=s_B+o(D),}
\tag{FI.2}
```

and

```math
\boxed{
\sum_{F\in\mathcal F_B}(m_F-1)_+
=s_B+o(D),
}
\tag{FI.3}
```

where faces meeting only the `o(D)` irregular loaded set are absorbed in the error.

Thus the loaded contact-degree slack `s_B` has three equivalent boundary interpretations at leading order:

1. missing loaded-to-interior spoke count: `s_B=q-e_BI+o(D)`;
2. excess loaded incidence above two loaded vertices per interface face;
3. excess direct shell-edge aggregation above one shell edge per interface face.

Combining with SL, if

```math
Q_B=(2+\xi+o(1))D,
```

then

```math
\boxed{
s_B\le\frac\xi2D+o(D),}
```

so each of the three defects above is at most `(xi/2+o(1))D`.

This supplies an explicit combinatorial stability theorem for quantitative HA: small interface surplus forces an almost one-spoke / two-loaded-vertices / one-shell-edge annulus even before the geometric fragmentation step is quantified.

---

## 1. Exact face count revisited

AS proved the finite identity

```math
4F_B
=2(e_{BB}+e_{BI})-b-Q_B+\sum_rk_r.
\tag{1.1}
```

SL proved throughout the full-core near-circle branch

```math
\sum_rk_r
=\pi D+Q_B-2s_B+o(D).
\tag{1.2}
```

The near-circle shell identities are

```math
q=(\pi+o(1))D,
\qquad
b=q+o(D),
\qquad
 e_{BB}=q+o(D),
\tag{1.3}
```

and by definition plus NC

```math
e_{BI}=q-s_B+o(D).
\tag{1.4}
```

Insert (1.2)--(1.4) into (1.1):

```math
\begin{aligned}
4F_B
&=2(2q-s_B)-q-Q_B+(q+Q_B-2s_B)+o(D)\\
&=4q-4s_B+o(D).
\end{aligned}
```

Hence

```math
F_B=q-s_B+o(D).
```

Together with (1.4),

```math
F_B=e_{BI}+o(D).
```

This proves FI.1.

The exact cancellation of `Q_B` is the point: the **number** of loaded-interface faces is controlled by loaded degree slack, while `Q_B` controls their total excess degree.

---

## 2. Loaded vertex-face incidence

All but `o(D)` loaded terminals have both adjacent direct unit shell contacts by NC. Call them regular shell terminals.

At a regular shell terminal `b`, C35 gives total contact degree at most three. Thus it has either zero or one interior contact.

- with zero interior contacts, the interior sector between the two shell edges belongs to one bounded face;
- with one interior contact, that spoke splits the interior sector into two bounded face incidences.

Therefore the number of bounded loaded-face incidences at `b` is exactly

```math
1+d_{BI}(b).
```

The `o(D)` irregular shell terminals have uniformly bounded contact degree and contribute only `o(D)` incidences. Summing,

```math
\boxed{I_B=q+e_{BI}+o(D).}
\tag{2.1}
```

Use FI.1 and `e_BI=q-s_B+o(D)`:

```math
\begin{aligned}
I_B-2F_B
&=q+(q-s_B)-2(q-s_B)+o(D)\\
&=s_B+o(D).
\end{aligned}
```

This proves FI.2.

A bounded face meeting a regular loaded terminal contains at least one of the two incident shell sides, hence at least two loaded vertices. Faces whose loaded incidences are supported entirely on the irregular `o(D)` terminals contribute only `o(D)` total incidence. Therefore the negative part of `|V(F) cap B|-2` is sublinear, and FI.2 may equivalently be read as

```math
\sum_F(|V(F)\cap B|-2)_+=s_B+o(D).
\tag{2.2}
```

---

## 3. Shell-edge aggregation

There are

```math
q-o(D)
```

direct loaded-loaded unit shell sides. Only `o(D)` of them are contact bridges or are adjacent to the outer face on both sides; all remaining direct shell sides are incident on their interior side to one bounded face in `F_B`.

Hence

```math
\boxed{
\sum_{F\in\mathcal F_B}m_F=q+o(D).
}
\tag{3.1}
```

All but `o(D)` interface faces contain at least one regular shell side: otherwise every loaded incidence on that face would have to lie in the irregular shell set, whose total incidence is `o(D)`.

Thus the number of faces with `m_F=0` is `o(D)`, and

```math
\sum_F(m_F-1)_+
=\sum_Fm_F-F_B+o(D).
```

Using (3.1) and FI.1,

```math
\sum_F(m_F-1)_+
=q-(q-s_B)+o(D)
=s_B+o(D).
```

This proves FI.3.

---

## 4. Small-interface-surplus stability

SL gives

```math
Q_B\ge2D+2s_B-o(D).
```

If

```math
Q_B=(2+\xi+o(1))D,
```

then

```math
s_B\le\frac\xi2D+o(D).
```

Insert this into FI.1--FI.3:

```math
F_B\ge q-\frac\xi2D-o(D),
```

```math
I_B-2F_B\le\frac\xi2D+o(D),
```

```math
\sum_F(m_F-1)_+\le\frac\xi2D+o(D).
```

Also

```math
e_{BI}\ge q-\frac\xi2D-o(D).
```

Therefore a small `xi` simultaneously implies:

- at most `xi D/2` missing interior spoke slots;
- at most `xi D/2` excess loaded incidences beyond two per interface face;
- at most `xi D/2` excess shell sides aggregated into multi-shell-edge interface faces.

This is stronger than the sharp-branch AS theorem in one respect: it gives an explicit linear modulus away from equality.

---

## 5. What remains unquantified

FI does **not** control the internal contact-path length of a face with exactly one shell edge and exactly two loaded endpoints. Such a face may have degree

```math
k_F=L_F+3
```

with `L_F` arbitrarily large, and its defect

```math
Q_F=L_F-1
```

may absorb a large part of `Q_B` without changing `I_B` or `m_F`.

At the exact `xi=0` endpoint, CF used the separate half-disk perimeter equality to show that these annular path defects are only `o(D)` and the baseline `2D` defect concentrates in the central face. Quantitatively, the missing theorem is therefore:

> bound the total annular internal-path excess in terms of the half-disk cell-perimeter excess, which SL already bounds by `xi D`.

This is a geometric length-allocation problem, not another incidence count.

---

## 6. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| `F_B=q-s_B+o(D)` | proved | AS exact face count + SL outer-walk identity |
| `F_B=e_BI+o(D)` | proved | NC definition of `s_B` |
| loaded incidence excess `=s_B+o(D)` | proved | regular terminal sector count |
| shell-edge aggregation excess `=s_B+o(D)` | proved | shell-side incidence count |
| all three defects `<=xi D/2+o(D)` | proved | SL |
| annular path-degree excess `O(xi D)` | not yet proved | requires quantitative half-disk perimeter allocation |
| Level I | still open | long one-shell-edge annular faces remain the stability escape |

---

## 7. Next target

Quantify the annular path excess. For each one-shell-edge/two-loaded-endpoint face, its interior boundary path lies on one harmonic component outer walk and has length `1+Q_F`. The sum of all component outer walks is known exactly from SL.5, while the two HG half-disk groups require baseline perimeter `pi+2`.

A successful decomposition should show that after charging the unavoidable two diameter-side group separators, every additional annular path edge contributes to

```math
\sum_rk_r-(\pi+2)D
\le\xi D+o(D).
```

If so, all but `O(xi D)` shell edges would become exact quadrilateral translated faces. HA's curved-good-end count would then degrade only linearly in `xi`, leaving ample room to extract an explicit positive lower bound on `xi`.
