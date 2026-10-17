> Generated reading edition · [exact source](../../../docs/reports/target_c_post_zf_currency_coupling_2026-09-09.md) · source SHA-256 `3df3e493c9a4951904ebed008e510c0d87375d8418f58081aa79e9c2cfcf8a36`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-04573F491D2C","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — exact post-ZF currency coupling

**Date:** 2026-09-09  
**Repository base:** `e555cad22322c1e430a3aa1e25518742b35615c0`  
**Run type:** exact inequality coupling / closing-frontier refinement  
**Target:** Target C, C-II after ZF  
**Depends on:** ZT exact terminal partition, ZK component-slack cancellation, DB diameter lower bound; GU only for the final low-surplus corollary  
**External web search:** not used  
**Computation:** displayed decimals only; no computation is used in the proof

## LEVEL I STATUS

`STILL OPEN`

Current main describes two post-ZF currencies as largely independent:

- the loaded-contact / pinned-stress currency `e_BB+2s_C`; and
- the outer-walk / exceptional-face currency `x_B+Q`.

They are not independent. The exact ZK and ZT ledgers force a linear inequality coupling them.

Put

```math
A:=e_{BB}+2s_C,
\qquad
B:=x_B+Q,
\qquad
k:=d_H+s_Z.
```

Then every audited post-ZF survivor satisfies

```math
\boxed{2A+3B\ge 3q-12.}
\tag{KC.1}
```

Consequently

```math
\boxed{
\max\{A,B\}\ge \frac{3q-12}{5}.}
\tag{KC.2}
```

Since DB gives

```math
\liminf \frac hD\ge 2\rho,
\qquad \rho=\cos\rho=0.7390851332\ldots,
```

and `q>=h`, every unbounded post-ZF survivor sequence obeys

```math
\boxed{
\liminf\frac1D
\max\{e_{BB}+2s_C,\ x_B+Q\}
\ge \frac{6\rho}{5}
=0.8869021598\ldots .}
\tag{KC.3}
```

This is an exact coupling theorem followed by one asymptotic substitution. It does not close Level I, but it removes the possibility that both post-ZF currencies are merely small linear errors.

---

## 1. Exact derivation

The ZK component-slack identity is

```math
\sum_r\delta_r+R_I+s_B+3k
=6+e_{BB}+2s_C.
\tag{1.1}
```

All three terms preceding `3k` on the left are nonnegative. Therefore

```math
\boxed{A=e_{BB}+2s_C\ge 3k-6.}
\tag{1.2}
```

ZT gives the exact terminal partition

```math
q=x_B+Q+2d_H+2s_Z.
```

Hence

```math
\boxed{B=x_B+Q=q-2k.}
\tag{1.3}
```

Multiply (1.2) by two and (1.3) by three:

```math
2A\ge6k-12,
\qquad
3B=3q-6k.
```

Adding cancels `k` exactly and yields KC.1:

```math
2A+3B\ge3q-12.
```

No asymptotic estimate, planarity approximation, or discarded remainder occurs here. `square`

---

## 2. Minimax consequence

Let

```math
M:=\max\{A,B\}.
```

Since `A<=M` and `B<=M`,

```math
2A+3B\le5M.
```

KC.1 therefore gives

```math
5M\ge3q-12,
```

which is KC.2.

The constant is sharp for the **linear relaxation** consisting only of (1.2) and (1.3): equality occurs algebraically at

```math
k=\frac{q+6}{5},
\qquad
A=B=\frac{3q-12}{5}.
```

No claim is made that an actual geometric source attains this relaxation.

---

## 3. Diameter-scale consequence from DB

DB proves

```math
\liminf\frac hD\ge2\rho,
\qquad
\rho=\cos\rho.
```

The full diameter graph has no isolated terminal by definition, and the planar diameter-graph bound gives `h<=q`; thus

```math
\liminf\frac qD\ge2\rho.
```

Divide KC.2 by `D`. The additive `12/(5D)` vanishes, giving

```math
\liminf\frac MD
\ge\frac35\liminf\frac qD
\ge\frac{6\rho}{5},
```

which proves KC.3.

Numerically,

```math
\frac{6\rho}{5}=0.8869021598\ldots .
```

Thus every post-ZF survivor has either

```math
e_{BB}+2s_C\ge(0.886902-o(1))D
```

along the relevant lower-limit subsequence, or

```math
x_B+Q\ge(0.886902-o(1))D,
```

with the understood minimax meaning of KC.3.

---

## 4. Conditional tradeoff, not just a max bound

KC.1 is more useful than the symmetric minimax corollary. Rearranging gives the exact one-sided implications

```math
\boxed{
B\ge q-\frac23A-4,
}
\tag{KC.4}
```

and

```math
\boxed{
A\ge\frac32(q-B)-6.
}
\tag{KC.5}
```

Therefore any attempted upper bound on one currency automatically forces a quantitative lower bound on the other.

In particular, suppose along a sequence

```math
\limsup\frac AD\le\lambda.
```

Then DB and KC.4 give

```math
\boxed{
\liminf\frac BD
\ge2\rho-\frac{2\lambda}{3}.}
\tag{KC.6}
```

This remains useful even when `A` is linear rather than sublinear.

---

## 5. Interaction with the GU cavity threshold

GU defines

```math
\lambda_*:=\sqrt{\frac{\sqrt3}{\pi}}
=0.7425152492\ldots
```

and proves that if

```math
\limsup\frac{e_{BB}+2s_C}{D}<\lambda_*,
```

then the attachment-cell area gap is quadratic:

```math
\liminf\frac G{D^2}>0.
```

KC strengthens that low-surplus branch simultaneously on the boundary/face side. Substituting `lambda=lambda_*` into KC.6 gives

```math
\boxed{
\liminf\frac{x_B+Q}{D}
\ge
2\rho-\frac{2\lambda_*}{3}
=0.9831601003\ldots
}
\tag{KC.7}
```

whenever the GU low-surplus hypothesis holds with a strict asymptotic margin; more precisely, if `limsup A/D<=lambda<lambda_*`, then the lower bound is `2rho-2lambda/3`, and one may let `lambda` approach `lambda_*`.

So the GU branch now has two simultaneous mandatory features:

1. a quadratic attachment-cell gap `G=Omega(D^2)`; and
2. an almost unit-per-diameter linear outer/face defect `x_B+Q >= (0.98316-o(1))D`.

GU already localizes the quadratic gap to a macroscopic outer pocket or a giant exceptional face. KC shows that this geometry cannot occur while the discrete outer/face currency is small.

---

## 6. Relation to NB

NB proves

```math
r_H:=2h-q=x_B+Q+2s_Z
\ge(0.6099043189-o(1))D.
```

KC is genuinely different:

- NB controls the **diameter degree excess** `x_B+Q+2s_Z`;
- KC couples `x_B+Q` to the **pinned/contact** currency `e_BB+2s_C` and contains no `s_Z` on its boundary side.

Thus a survivor cannot hide all of NB's branching defect in `s_Z` while simultaneously keeping both `e_BB+2s_C` and `x_B+Q` small.

The strongest current scalar picture is therefore

```math
\begin{aligned}
x_B+Q+2s_Z &\ge (0.609904-o(1))D,\\
\max\{e_{BB}+2s_C,\ x_B+Q\}
&\ge(0.886902-o(1))D.
\end{aligned}
```

These inequalities constrain different projections of the exact post-ZF ledger.

---

## 7. Why this still does not close Level I

The desired contradiction remains

```math
b+Q>2h,
```

or equivalently `s_Z<0`, whereas ZF gives `s_Z>=0`.

KC does not give a sign contradiction. Large `A` can be realized algebraically by many direct loaded-loaded contacts and/or pinned-contact stress dependencies. Large `B` can be realized algebraically by outer-walk excess and exceptional-face degree. The theorem proves these two resources cannot both be cheap, but a source-specific geometric cost for the expensive branch is still required.

No individual KKT coefficient or response conductance is lower-bounded here. Tiny-weight regressions remain binding.

---

## 8. Regression audit

### Regular odd shell

For a regular unit odd `q`-gon with contact graph equal to the boundary cycle,

```math
e_{BB}=q,\quad s_C=0,\quad x_B=0,\quad Q=q-4.
```

Thus

```math
A=q,\qquad B=q-4,
```

and KC.1 reads

```math
2q+3(q-4)=5q-12\ge3q-12.
```

The shell is retained; KC does not falsely exclude it.

### Unit square

Here

```math
A=4,\qquad B=0,\qquad q=4.
```

KC.1 gives `8>=0`. The bound is deliberately a large-source structural coupling, not a sharp small-`q` classification.

### Perfect matching endpoint

The now-excluded perfect-matching branch had `x_B=Q=s_Z=0`, hence `B=0`. KC.5 would force

```math
A\ge\frac32q-6.
```

The stronger matching theorem excludes the branch geometrically; KC is consistent with that result and does not replace it.

---

## 9. Next theorem

KC suggests a sharper two-branch closing program than the previous independent-axis split.

### Branch A: large pinned/contact currency

If

```math
e_{BB}+2s_C\ge cD,
```

use the loaded degree-three boundary budget, the ZK incidence identity, and response/rigidity structure to convert that linear count into either response mass or a packing-area loss.

### Branch B: large outer/face currency

If

```math
x_B+Q\ge cD,
```

separate outer-walk repetition from exceptional-face degree and charge either quantity to force-hull perimeter/area. The GU low-`A` branch already strengthens this to `x_B+Q >= (0.98316-o(1))D` plus a quadratic attachment gap.

The next useful theorem should therefore bound one of

```math
x_B,\quad Q,\quad e_{BB},\quad s_C
```

by a source-specific area or response quantity rather than introduce another independent ledger variable.

---

## 10. Promotion recommendation

**Hold as report pending independent audit.**

The proof is an exact algebraic consequence of report-level ZK/ZT and the asymptotic constant uses report-level DB. It should not be promoted independently of those dependencies.

---

## 11. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Let
  A=e_BB+2s_C,
  B=x_B+Q,
  k=d_H+s_Z.

ZK:
  A >= 3k-6.
ZT:
  B = q-2k.
Therefore exactly
  2A+3B >= 3q-12,
and hence
  max(A,B) >= (3q-12)/5.

DB gives liminf q/D >= liminf h/D >= 2rho,
rho=cos rho=0.7390851332... . Thus
  liminf max(A,B)/D >= 6rho/5
                       =0.8869021598... .

Tradeoff form:
  B >= q-(2/3)A-4.
So if limsup A/D<=lambda,
  liminf B/D >= 2rho-2lambda/3.
At GU's lambda_*=sqrt(sqrt(3)/pi)=0.7425152492...,
  B/D >= 0.9831601003... .
Hence the GU low-surplus branch simultaneously has
  G=Omega(D^2)
and
  x_B+Q >= (0.98316-o(1))D.

Next: convert the expensive branch (A or B) into response mass, area loss,
or a finite strict sub-D motion.
```
