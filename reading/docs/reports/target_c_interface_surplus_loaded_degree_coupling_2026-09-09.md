> Generated reading edition · [exact source](../../../docs/reports/target_c_interface_surplus_loaded_degree_coupling_2026-09-09.md) · source SHA-256 `e566e50485db81272e70b697db37f0c08e562209e3e3a8ff846e35379d03a71a`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 13 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-0F3CF230E39E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_interface_surplus_loaded_degree_coupling_2026-09-09.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=655781f352d292ce7461568161e40bd5ff331031; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — loaded-interface surplus pays twice the loaded contact-degree slack

**Date:** 2026-09-09  
**Repository branch:** `research/fullcore-interface-perimeter-2026-09-09`  
**Run type:** exact-ledger quantitative stability corollary  
**Target:** arbitrary full-core near-circle survivor, not only the sharp equality branch  
**Depends on:** GP group-perimeter theorem, NBd exact loaded-boundary ledger, HBd near-circle identities, NC loaded-loaded contact completion  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

Put

```math
Q_B:=Q-Q_{\rm int}
```

for the bounded-face degree excess carried by faces incident to loaded terminals, and let

```math
s_B:=3q-e_{BI}-2e_{BB}\ge0
```

be the loaded contact-degree slack.

GP proves `Q_B>=2D-o(D)` in every full-core near-circle survivor. Retaining the previously discarded `s_B` term strengthens this to

```math
\boxed{
Q_B\ge2D+2s_B-o(D).
}
\tag{SL.1}
```

Since NC gives

```math
e_{BB}=q-o(D)
```

in the near-circle branch,

```math
s_B=q-e_{BI}+o(D).
```

Therefore SL.1 is equivalently

```math
\boxed{
e_{BI}
\ge
q-\frac{Q_B-2D}{2}-o(D).
}
\tag{SL.2}
```

Thus if

```math
Q_B=(2+\xi+o(1))D,
\qquad \xi\ge0,
```

then

```math
\boxed{
s_B\le\frac\xi2D+o(D),}
\tag{SL.3}
```

and

```math
\boxed{
e_{BI}\ge q-\frac\xi2D-o(D).}
\tag{SL.4}
```

Because all but `o(D)` loaded terminals already have their two direct unit shell contacts and C35 caps their total contact degree at three, SL.4 says that all but at most

```math
\left(\frac\xi2+o(1)\right)D
```

loaded terminals use the one remaining contact slot on an unloaded interior neighbor.

This gives an explicit stability modulus for the **spoke-count** part of the HA equality classification. The remaining nonquantitative step in HA is geometric fragmentation of the two half-disk attachment-cell groups.

---

## 1. Start from the group-perimeter lower bound

GP gives

```math
\sum_r k_r\ge(\pi+2-o(1))D.
\tag{1.1}
```

For each unloaded component the exact local face identity is

```math
r_r=\frac{k_r+Q_r}{2}-\delta_r.
```

Summing,

```math
R_I
=\frac12\sum_rk_r+\frac12Q_{\rm int}-S.
```

Therefore (1.1) gives

```math
\boxed{
R_I
\ge
\left(\frac{\pi+2}{2}-o(1)\right)D
+\frac12Q_{\rm int}-S.
}
\tag{1.2}
```

No equality or cap-minimality hypothesis is used.

---

## 2. Insert the exact loaded-boundary ledger

NBd is the finite identity

```math
S+R_I+s_B+2E_{BB}+3c_I+s_C=q+2x_B.
\tag{2.1}
```

In the near-circle branch,

```math
q=(\pi+o(1))D,
\qquad
x_B=o(D),
\qquad
E_{BB}=o(D),
\qquad
c_I=o(D).
\tag{2.2}
```

Insert (1.2) into (2.1); `S` cancels:

```math
\left(\frac{\pi+2}{2}-o(1)\right)D
+\frac12Q_{\rm int}
+s_B+s_C
\le
(\pi+o(1))D.
\tag{2.3}
```

HBd gives

```math
Q+2s_C=(\pi+o(1))D.
\tag{2.4}
```

Since

```math
Q_{\rm int}=Q-Q_B,
```

(2.4) gives

```math
Q_{\rm int}
=(\pi+o(1))D-2s_C-Q_B.
\tag{2.5}
```

Insert (2.5) into (2.3):

```math
\left(\frac{\pi+2}{2}-o(1)\right)D
+\frac12\left((\pi+o(1))D-2s_C-Q_B\right)
+s_B+s_C
\le(\pi+o(1))D.
```

The `s_C` terms cancel exactly. Simplifying,

```math
D+s_B-\frac12Q_B\le o(D),
```

or

```math
Q_B\ge2D+2s_B-o(D).
```

This proves SL.1.

The cancellation is important: SL.1 is independent of the pinned-stress surplus and of all component graph diameters.

---

## 3. Convert to interior-spoke count

By definition

```math
s_B=3q-e_{BI}-2e_{BB}.
```

NC gives

```math
e_{BB}=q-o(D),
```

hence

```math
\boxed{s_B=q-e_{BI}+o(D).}
\tag{3.1}
```

Combine with SL.1:

```math
q-e_{BI}
\le\frac{Q_B-2D}{2}+o(D),
```

which is SL.2.

All but `o(D)` loaded terminals have both neighboring shell contacts. At such a terminal C35 gives degree at most three, so it has at most one loaded-to-unloaded contact. Thus `q-e_BI+o(D)` is exactly the number of missing interior-spoke slots up to sublinear error, proving the interpretation of SL.3-SL.4.

---

## 4. Companion outer-walk identity

The same ledgers give a useful exact asymptotic expression for the total unloaded-component outer-walk length.

From

```math
R_I=\frac12\sum_rk_r+\frac12Q_{\rm int}-S
```

and NBd,

```math
\frac12\sum_rk_r
+\frac12Q_{\rm int}
+s_B+2E_{BB}+3c_I+s_C
=q+2x_B.
```

Use the near-circle reductions and (2.5):

```math
\boxed{
\sum_rk_r
=\pi D+Q_B-2s_B+o(D).
}
\tag{SL.5}
```

Thus for `Q_B=(2+xi+o(1))D`,

```math
\boxed{
\frac1D\sum_rk_r
=\pi+2+\xi-2\frac{s_B}{D}+o(1).
}
\tag{SL.6}
```

Together with SL.3,

```math
\pi+2-o(1)
\le
\frac1D\sum_rk_r
\le
\pi+2+\xi+o(1).
\tag{SL.7}
```

Hence `xi` controls the total excess unloaded-component boundary length above the two-half-disk minimum as well as the number of missing spokes.

This is exactly the two-parameter stability package needed for a quantitative version of HA.

---

## 5. Interaction with HA

HA excludes `xi->0` qualitatively. SL identifies the two geometric quantities that must remain close to equality whenever `xi` is small:

```text
interface excess xi D
    -> missing interior spokes <= (xi/2)D
    -> total component outer-walk excess <= xi D.
```

A quantitative fragmentation theorem for the two HG half-disk groups can now use the **same** `xi D` budget. Once it yields explicit lower bounds on

1. the population of one dominant component in each half-disk;
2. the length of its curved shell-facing translated boundary;

HA's atomic/non-atomic train estimate becomes an explicit inequality in `xi`.

No additional KKT weight lower bound is needed.

---

## 6. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| `Q_B>=2D+2s_B-o(D)` | proved | GP + NBd + HBd exact cancellations |
| `s_B=q-e_BI+o(D)` | proved | NC `e_BB=q-o(D)` |
| missing spoke count `<=xi D/2+o(D)` | proved | C35 degree cap + previous identities |
| total outer-walk identity SL.5 | proved | local Euler + NBd/HBd |
| explicit numerical lower bound on `xi` | not yet proved | needs quantitative half-disk fragmentation/exposure |
| Level I | still open | HA gap remains nonquantified |

---

## 7. Next target

Prove an explicit half-disk partition stability lemma of the following form.

Let convex attachment cells with disjoint interiors fill a diameter-one semicircle in measure and suppose their total perimeter is at most

```math
1+\frac\pi2+\varepsilon.
```

Then one cell has area at least

```math
\frac\pi8-C_1\varepsilon^\alpha
```

and covers all but at most

```math
C_2\varepsilon^\beta
```

of the outer semicircular boundary measure.

Even coarse explicit constants/exponents should suffice because HA has a contradiction margin `0.820724D`. Combine that lemma with SL.3's independent `xi/2` spoke-loss bound and rerun HA to obtain an explicit positive root for `xi`.
