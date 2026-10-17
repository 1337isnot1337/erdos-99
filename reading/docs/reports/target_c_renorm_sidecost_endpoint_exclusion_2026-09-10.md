> Generated reading edition · [exact source](../../../docs/reports/target_c_renorm_sidecost_endpoint_exclusion_2026-09-10.md) · source SHA-256 `ed65a4b58538894902e7ccc9a6c4ba99a116d05ec9afe52ec8395eb78fc87866`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-728E3401BA52","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — taut-side saturation excludes the `mu_SC` endpoint

**Date:** 2026-09-10  
**Repository branch:** `research/c2-renorm-paired-pocket-20260910` after SC  
**Target:** Target C, all post-ZF survivors  

## LEVEL I STATUS

`STILL OPEN`.

SC proves

$$
\liminf\mu_D\ge\mu_{SC}=0.836440399\ldots
$$

with `mu_SC` defined analytically by SC.5--SC.6.  This report proves that equality is
impossible.  Therefore there is a uniform nonexplicit positive gap above `mu_SC`.

The reason is exact: SC equality needs the projective side-cost budget to be saturated,
which spends all of `d_P` on macroscopic force-hull chords.  The corresponding outer
contact chains are then asymptotically taut and enclose only `o(D^2)` area, whereas the
same scalar equality demands a positive quadratic cavity.

---

## 1. Scalar endpoint data

Assume an unbounded post-ZF survivor sequence satisfies

$$
\mu_D\to\mu_{SC}.
\tag{1.1}
$$

SC gives

$$
\frac hD\to y_*,
\qquad
m_*:=\frac{\mu_{SC}+y_*}{2}=2\cos(y_*/2),
\tag{1.2}
$$

and

$$
\frac{d_P+Q}{D}\to m_*.
\tag{1.3}
$$

It also forces

$$
\frac{s_Z+a+c_B+2s_C}{D}\to0
\tag{1.4}
$$

through the exact RPE remainder.

The defining scalar equality is

$$
\boxed{
\Phi(y_*)
=
\frac\pi4\mu_{SC}^2+rac{m_*^2}{4\pi},
}
\tag{1.5}
$$

while the two force-area floors agree:

$$
\boxed{
\Phi(y_*)=A(m_*).
}
\tag{1.6}
$$

---

## 2. Force area, attachment area, and cavity area all saturate

GR/ZK gives

$$
\limsup\frac{C_{att}}{D^2}
\le\frac\pi4\mu_{SC}^2,
\tag{2.1}
$$

and the paired-pocket/exceptional-face estimate gives

$$
\limsup\frac G{D^2}
\le\frac{m_*^2}{4\pi}.
\tag{2.2}
$$

SC gives

$$
\liminf\frac{area(F)}{D^2}
\ge A(m_*)=\Phi(y_*).
\tag{2.3}
$$

Since

$$
area(F)=C_{att}+G
$$

and the sum of the right sides of (2.1)-(2.2) equals (2.3) by (1.5), all three
quantities have limits and all inequalities are sharp:

$$
\boxed{
\frac{area(F)}{D^2}\to A(m_*),
}
\tag{2.4}
$$

$$
\boxed{
\frac{C_{att}}{D^2}\to\frac\pi4\mu_{SC}^2,
\qquad
\frac G{D^2}\to\frac{m_*^2}{4\pi}>0.
}
\tag{2.5}
$$

The positive limit in (2.5) is the quantity contradicted below.

---

## 3. Equality in the side-cost area floor consumes the entire `d_P` budget

Use the notation of SC.  Let the positive limiting macroscopic projective gaps be
`r_j` and put

$$
c_j=2\sin(r_j/2).
$$

Let

$$
C:=\sum_jc_j.
$$

The force-side transfer and triangle inequality give

$$
C\le\liminf\frac{d_P}{D}.
\tag{3.1}
$$

Also

$$
\liminf\frac{area(F)}{D^2}
\ge
\frac14\left[\pi-\sum_j\varphi(c_j)\right]
\ge
\frac{\pi-\varphi(C)}4
\ge A(m_*),
\tag{3.2}
$$

where

$$
\varphi(c)=2\arcsin(c/2)-c\sqrt{1-c^2/4}
$$

is strictly increasing and superadditive, and the last inequality uses

$$
C\le d_P/D\le(d_P+Q)/D\to m_*.
$$

But (2.4) says the left side of (3.2) tends to `A(m_*)`.  Since `varphi` is strictly
increasing at the fixed positive point `m_*`, the last inequality can be sharp only if

$$
\boxed{C\to m_*.}
\tag{3.3}
$$

Then (3.1) and (1.3) squeeze

$$
\boxed{
\frac{d_P}{D}\to m_*,
\qquad
\frac QD\to0.
}
\tag{3.4}
$$

Thus all linear pocket/face currency is spent on the macroscopic opposite force-side
chords themselves.

---

## 4. The macroscopic pocket chains are asymptotically taut

Fix `epsilon>0` and retain the finitely many projective gaps whose limiting side-pair
cost is at least `epsilon`; let `S_D` be the corresponding finite family of actual OP
pockets.  Their force-hull chord lengths have total

$$
\sum_{P\in S_D}s_P=(C+o(1))D.
\tag{4.1}
$$

Their old contact-chain lengths satisfy `ell_P>=s_P`, while

$$
\sum_P(\ell_P-2)=d_P.
\tag{4.2}
$$

Because `|S_D|=O_epsilon(1)`, equations (3.3)-(3.4) imply

$$
\sum_{P\in S_D}(\ell_P-s_P)=o(D)
\tag{4.3}
$$

as first `D->infinity` and then `epsilon->0`.  They also imply that the total degree
excess of all pockets not in `S_D` is `o(D)`.

Moreover (1.4) gives `a=o(D)`.  Hence the total old-chain length of the remaining
pockets is

$$
\sum_{P\notin S_D}\ell_P
=
\sum_{P\notin S_D}(\ell_P-2)+2|\{P\notin S_D\}|
=o(D).
\tag{4.4}
$$

after the same two-step limit.

---

## 5. Taut chains have only subquadratic pocket area

For one convex pocket with chain length `ell` and chord `s`, the canonical DD/Dido
bound gives

$$
area(P)
\le
\frac1{\sqrt6}\ell^{3/2}\sqrt{\ell-s}.
\tag{5.1}
$$

For the finitely many pockets in `S_D`, their total chain length is `O(D)` while the
total detour in (4.3) is `o(D)`.  Cauchy/Hölder applied to (5.1) gives

$$
\boxed{
\sum_{P\in S_D}area(P)=o(D^2).
}
\tag{5.2}
$$

For the remaining pockets use the reflection bound

$$
area(P)\le\frac{\ell_P^2}{2\pi}.
$$

Equation (4.4) gives

$$
\sum_{P\notin S_D}area(P)
\le
\frac1{2\pi}
\left(\sum_{P\notin S_D}\ell_P\right)^2
=o(D^2).
\tag{5.3}
$$

Letting `epsilon->0`,

$$
\boxed{H_{out}=o(D^2).}
\tag{5.4}
$$

By (3.4), the exceptional-face isoperimetric estimate also gives

$$
\boxed{A_{exc}=o(D^2).}
\tag{5.5}
$$

ZG therefore implies

$$
\boxed{G=o(D^2).}
\tag{5.6}
$$

This contradicts the positive endpoint limit in (2.5):

$$
G/D^2\to m_*^2/(4\pi)>0.
$$

Hence no SC endpoint sequence exists.

### Theorem SCE.1 — endpoint exclusion

There is no unbounded post-ZF survivor sequence satisfying

$$
\mu_D\to\mu_{SC}.
\tag{SCE.1}
$$

### Corollary SCE.2 — uniform gap

There exist absolute constants `epsilon_SC>0` and `D_0<infinity` such that every
post-ZF survivor with `D>=D_0` satisfies

$$
\boxed{
\mu_D\ge\mu_{SC}+\epsilon_{SC}.
}
\tag{SCE.2}
$$

The usual sequential compactness argument applies.

---

## 6. What remains

The explicit all-phase lower endpoint has now moved from `0.5947` to

$$
\mu_{SC}>0.834
$$

and the endpoint is excluded.  The remaining high-`mu` phase can no longer imitate
any scalar equality state used by GR, RP, RL, or SC.

The next useful step is quantitative stability of (3.2)-(5.1): a positive quadratic
cavity requires a definite amount of chain detour beyond the projective side cost.
That detour raises `d_P` above the amount allowed by the exact RPE/RL pocket ledger.
A direct side-plus-detour inequality should therefore raise the **explicit** constant
again, potentially toward the unrenormalized paired-lens threshold.

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

SC endpoint:
  mu_D->mu_SC,
  h/D->y_*,
  m_*=(mu_SC+y_*)/2=2cos(y_*/2),
  (d_P+Q)/D->m_*,
  area(F)/D^2->A(m_*)=Phi(y_*),
  G/D^2->m_*^2/(4pi)>0.

Side-cost equality gives total macroscopic opposite-side chord cost C->m_*.
Since C<=d_P/D<=(d_P+Q)/D->m_*,
  d_P/D->m_*, Q/D->0.
Thus the macroscopic pocket chains have total chain-minus-chord detour o(D), and all
remaining pocket chain mass is o(D).  DD/Dido then gives H_out=o(D^2); Q=o(D) gives
A_exc=o(D^2); ZG gives G=o(D^2), contradicting the positive endpoint cavity.

Therefore some epsilon_SC>0 exists with
  mu_D>=mu_SC+epsilon_SC,
  mu_SC=0.836440399... (>0.834 rigorously),
for all sufficiently large post-ZF survivors.

Next: quantify the side-cost/detour tradeoff instead of using endpoint compactness.
```
