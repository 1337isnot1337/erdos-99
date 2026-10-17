> Generated reading edition · [exact source](../../../docs/reports/target_c_clean_endpoint_face_defect_separation_2026-09-09.md) · source SHA-256 `95762194548daab03d0fc4ab4c132ca0d0e520dc1820479bae29da5214aeba63`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-360261EF9719","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — clean-endpoint face-defect separation

**Date:** 2026-09-09  
**Repository base:** PR #119 after CE  
**Run type:** exact consequence / currency separation  
**Target:** post-ZF `x_B=o(D)`, `n-v=o(D^2)` branch  
**Depends on:** CE one-ended train theorem, ZE/ZT exact ledgers  
**External web search:** not used

## LEVEL I STATUS

`STILL OPEN`

CE proved in the near-circle full-core branch

$$
\liminf\frac{T-q}{D}\ge2\sqrt\Delta,
\qquad
\Delta=\frac\pi{2\sqrt3}.
$$

Its first stated consequence lower-bounded the combined branching currency `Q+2s_Z`. The exact terminal ledger actually separates the currencies more strongly: the bounded-face defect `Q` itself must already carry the full `1.390168...D` lower bound.

### Theorem CF — linear face defect independent of mixed surplus

Every post-ZF sequence satisfying

$$
x_B=o(D),
\qquad
n-v=o(D^2)
$$

obeys

$$
\boxed{
\liminf\frac QD
\ge
\frac\pi5+\frac45\sqrt\Delta
=1.3901687762\ldots .
}
\tag{CF.1}
$$

and

$$
\boxed{
\limsup\frac{d_H+s_Z}{D}
\le
\frac25(\pi-\sqrt\Delta)
=0.8757119387\ldots .
}
\tag{CF.2}
$$

Thus the CE endpoint cannot hide its boundary-scale defect in extra mixed-framework stress dependencies. A genuinely linear amount of bounded nonquadrilateral face degree is mandatory.

### Proof

ZE gives

$$
2f=(T-q)+d_H+s_Z.
$$

CE gives `T-q >= (2sqrt(Delta)-o(1))D`, hence

$$
\frac fD
\ge
\sqrt\Delta
+\frac12\frac{d_H+s_Z}{D}
-o(1).
\tag{1.1}
$$

Every bounded exceptional face has degree at least five, so `Q>=f`.

On the other hand the exact terminal ledger is

$$
q=x_B+Q+2d_H+2s_Z.
$$

DG/DC gives `q/D->pi` and the present hypothesis gives `x_B/D->0`. Put

$$
k_D:=\frac{d_H+s_Z}{D}.
$$

Then

$$
\frac QD
=\pi-2k_D+o(1).
\tag{1.2}
$$

Combine `Q>=f`, (1.1), and (1.2):

$$
\pi-2k_D
\ge
\sqrt\Delta+\frac{k_D}{2}-o(1).
$$

Therefore

$$
\frac52k_D
\le
\pi-\sqrt\Delta+o(1),
$$

which proves CF.2.

Substitute the resulting upper bound into (1.2):

$$
\begin{aligned}
\liminf\frac QD
&\ge
\pi-\frac45(\pi-\sqrt\Delta)\\
&=
\frac\pi5+\frac45\sqrt\Delta.
\end{aligned}
$$

This proves CF.1. `square`

### Consequences

Because `Q=sum_F(deg F-4)` and CE also gives `f/D>=sqrt(Delta)`, the average defect degree satisfies only the weak lower ratio

$$
\frac Qf\ge1
$$

in general; CF does not force high-degree faces. The binding near-triangular pentagon regression remains possible.

However, CF materially changes the remaining theorem target. The full-core branch now has simultaneous mandatory bounds

$$
T-q\ge(1.9046256-o(1))D,
$$

$$
f\ge(0.9523128-o(1))D,
$$

$$
Q\ge(1.3901688-o(1))D,
$$

$$
K_{exc}=Q+4f\ge(6.9508439-o(1))D.
$$

The `Q` lower bound is geometric/topological and survives even if `s_Z` is large.

```text
LEVEL I STATUS: STILL OPEN

Near-circle full core:
    2f >= 2sqrt(Delta)D + d_H+s_Z-o(D),
    Q >= f,
    pi D = Q+2(d_H+s_Z)+o(D).
Therefore
    (d_H+s_Z)/D <= 2(pi-sqrt(Delta))/5 + o(1),
    Q/D >= pi/5+4sqrt(Delta)/5-o(1)
        = 1.3901687762...-o(1).
```
