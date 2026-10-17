> Generated reading edition · [exact source](../../../docs/reports/target_c_loaded_interface_two_unit_defect_2026-09-09.md) · source SHA-256 `7e1c0d0f0d7cd4ac2208f2469370b692cb2c8c97c7947a0940d44087dda1882f`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-F7AC32FC5C42","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_loaded_interface_two_unit_defect_2026-09-09.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=86d956469e0af0b1b0f8fde3fafc0da51329c91b; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — cap-minimal full core forces two diameter units of loaded-interface face defect

**Date:** 2026-09-09  
**Repository branch:** `research/post-uf-attachment-fill-2026-09-09`  
**Run type:** exact local-face/slack sharpening of TE  
**Target:** cap-minimal full-core near-circle endpoint  
**Depends on:** SI, TE, NBd, NC, ZU, ZT; local Euler face identity on every unloaded component  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

TE proves that at least `(2-o(1))D` total face defect lies outside the interiors of the two giant semicircle carriers, but leaves a possible escape through the internal faces of the remaining `o(D^2)`-population harmonic components.

That escape is impossible at leading linear order because internal face defect itself consumes the exact ZK Eppstein-slack currency.

Let

$$
Q_{all-int}:=\sum_rQ_r
$$

be the total bounded-face degree excess over **all** unloaded-component internal graphs `C[I_r]`, and let

$$
Q_B:=Q-Q_{all-int}
$$

be the defect on bounded faces incident to at least one loaded terminal.

Then the cap-minimal full-core branch satisfies

$$
\boxed{
Q_B\ge(2-o(1))D.
}
\tag{LI.1}

$$

Thus the remaining obstruction is now a genuinely loaded-boundary/interface phenomenon. Neither the two dense carrier interiors nor the graph-small harmonic components can absorb the mandatory two units of defect.

---

## 1. Exact local face identity for every unloaded component

For any unloaded component `I_r`, let

- `n_r=|I_r|`;
- `e_r` be its internal contact-edge count;
- `k_r` be the outer-face boundary-walk length of the connected plane graph `C[I_r]`;
- `Q_r=sum_F(deg F-4)` over its bounded faces;
- `delta_r` be its contact-graph diameter;
- `r_r=2n_r-delta_r-2-e_r>=0` be the ZK internal Eppstein slack.

Euler and face-edge incidence give exactly

$$
 e_r=2n_r-2-\frac{k_r+Q_r}{2}.
\tag{1.1}

$$

Therefore

$$
\boxed{
 r_r
=\frac{k_r+Q_r}{2}-\delta_r.
}
\tag{LI.2}

$$

Since `k_r>=0`,

$$
\boxed{
 r_r\ge\frac{Q_r}{2}-\delta_r.
}
\tag{1.2}

$$

This elementary inequality is enough to eliminate the small-component defect escape.

---

## 2. In cap-cost equality, all remaining component diameter is sublinear

TD/TS give two giant components `I_1,I_2` satisfying

$$
\delta_1/D\to1,
\qquad
\delta_2/D\to1,
$$

and the cap-minimal hypothesis is

$$
S:=\sum_r\delta_r=(2+o(1))D.
$$

Hence

$$
\boxed{
S_{small}:=\sum_{r\ge3}\delta_r=o(D).
}
\tag{2.1}

$$

Put

$$
Q_{small}:=\sum_{r\ge3}Q_r.
$$

Summing (1.2) over `r>=3` gives

$$
\boxed{
R_{small}:=\sum_{r\ge3}r_r
\ge\frac12Q_{small}-o(D).
}
\tag{2.2}

$$

No population estimate is needed for this step.

---

## 3. Combine with the semicircle carriers

SI gives for the two giant components

$$
 r_1+r_2
\ge
\left(\frac\pi2-1-o(1)\right)D
+\frac12(Q_1+Q_2).
\tag{3.1}
$$

Add (2.2). Since

$$
Q_{all-int}=Q_1+Q_2+Q_{small},
$$

we obtain the strengthened total slack bound

$$
\boxed{
R_I
\ge
\left(\frac\pi2-1-o(1)\right)D
+\frac12Q_{all-int}.
}
\tag{LI.3}

$$

This is the key improvement over TE.

---

## 4. The exact near-circle budget controls `k=d_H+s_Z`

NC gives

$$
E_{BB}=o(D).
$$

NBd gives

$$
S+R_I+s_B+2E_{BB}+3c_I+s_C=q+2x_B.
$$

Use

$$
S=(2+o(1))D,
\quad
q=(\pi+o(1))D,
\quad
x_B=o(D),
$$

and insert LI.3. Discard `s_B>=0`:

$$
\boxed{
3c_I+s_C+\frac12Q_{all-int}
\le
\left(\frac\pi2-1+o(1)\right)D.
}
\tag{4.1}

$$

ZU plus NC gives

$$
 k:=d_H+s_Z=c_I+s_C+o(D).
\tag{4.2}

$$

Because `c_I>=0`,

$$
k\le3c_I+s_C+o(D).
$$

Thus

$$
\boxed{
 k
\le
\left(\frac\pi2-1+o(1)\right)D
-\frac12Q_{all-int}.
}
\tag{4.3}

$$

---

## 5. ZT pushes two units onto loaded-interface faces

ZT gives

$$
q=x_B+Q+2k.
$$

Hence

$$
Q=q-x_B-2k.
$$

Insert `q=(pi+o(1))D`, `x_B=o(D)`, and (4.3):

$$
\begin{aligned}
Q
&\ge
(\pi-o(1))D
-2\left[
\left(\frac\pi2-1+o(1)\right)D
-\frac12Q_{all-int}
\right]\\
&=
Q_{all-int}+(2-o(1))D.
\end{aligned}
$$

Therefore

$$
\boxed{
Q_B:=Q-Q_{all-int}
\ge(2-o(1))D.
}
$$

This proves LI.1.

---

## 6. Why `Q_B` is exactly a loaded-interface currency

A bounded face of the full contact graph with no loaded boundary vertex has all consecutive face-boundary vertices in the same connected component after deleting `B_+`; therefore it is a bounded face of one internal graph `C[I_r]`.

Conversely, the planarity argument in SI shows every bounded internal face of `C[I_r]` persists as a bounded face of the full contact graph.

Hence the partition is exact:

$$
\boxed{
Q=Q_{all-int}+Q_B,
}
$$

where every face counted by `Q_B` contains at least one loaded terminal.

Thus LI does not merely relocate defect outside the two giant components. It forces the full two-unit linear defect onto faces that touch the nearly saturated loaded hull cycle.

---

## 7. Consequences for the one-slot boundary picture

NC proves that all but `o(D)` loaded terminals have exactly the two unit hull-side contacts available as mandatory `B-B` contacts, and no nonconsecutive loaded-loaded unit chord exists. C35 gives loaded contact degree at most three.

Therefore at all but `o(D)` terminals there is at most **one** contact edge available to the unloaded harmonic interior.

LI now says that bounded faces incident to this one-slot boundary family carry total excess

$$
Q_B\ge(2-o(1))D.
$$

This is the sharp active target. A proof that such interface defect requires more than one interior contact slot per `O(1)` units of defect can close the cap-minimal branch.

A giant interface face remains the main regression: a face of degree `Theta(D)` can carry linear `Q_B` while touching only a few loaded terminals. Any successful interface theorem must therefore use convexity/semicircle geometry, not just face incidence counts.

---

## 8. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| local slack identity `r_r=(k_r+Q_r)/2-delta_r` | proved | Euler + face incidence |
| small-component `R_small>=Q_small/2-o(D)` | proved | total small diameter `o(D)` |
| total `R_I` bound LI.3 | proved | add SI giant-carrier bound |
| `Q_B>=2D-o(D)` | proved | NBd/NC/ZU/ZT exact algebra |
| giant interface face impossible | not proved | remains a binding regression |
| Level I | still open | loaded-interface geometry remains |

---

## 9. Next target

LI leaves one sharply defined boundary-order problem:

> In a near-circular force hull with an almost complete unit loaded hull cycle and two positive-density complementary semicircular harmonic carriers, can bounded convex contact faces touching the loaded hull carry `2D-o(D)` total degree excess while each loaded terminal has at most one interior contact slot?

The two plausible closing mechanisms are:

1. a long interface face has large convex perimeter and cuts too much area from one of the Oler-saturated semicircle carriers;
2. many shorter interface faces require too many distinct loaded interior-contact slots.

This suggests a length-threshold split on the `Q_B` faces: isolate faces of perimeter `>=epsilon D` and use cap-area loss; charge the remaining defect combinatorially to one-slot loaded terminals. That split is the next concrete proof target.
