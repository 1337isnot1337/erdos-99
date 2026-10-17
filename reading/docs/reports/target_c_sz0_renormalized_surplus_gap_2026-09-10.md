> Generated reading edition · [exact source](../../../docs/reports/target_c_sz0_renormalized_surplus_gap_2026-09-10.md) · source SHA-256 `4b6c7aed7dfe14af26206631165c09bc29d038bf38362707cc9114a3a998b170`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-8910EE3A79BE","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — the `s_Z=0` circuit phase pays three units per diameter-component defect

**Date:** 2026-09-10  
**Repository base:** `f0e565d92d331c74f672f32b2e2e6c81b587f61e`  
**Run type:** exact defect retention / circuit-phase branch reduction / endpoint exclusion  
**Target:** Target C, C-II after ZF, specialized to `s_Z=0`  
**Depends on:** PC, ZK, JC, GU/ZG, DD, FSDB, RSJ  
**External input:** none beyond the already imported RSJ theorem  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`.

The generic post-ZF lower currency is

```math
\lambda_D:=\frac{e_{BB}+2s_C}{D}.
```

In the exact mixed-circuit phase `s_Z=0`, the previously dropped `-3d_H` term can be
retained simultaneously in both places where the cavity argument spends boundary
currency.  Define

```math
\boxed{
\nu_D:=\frac{e_{BB}+2s_C-3d_H}{D}.
}
\tag{SZ.1}
```

Then the entire RSJ area/perimeter/cavity feasibility theorem remains valid with
`nu_D` in place of `lambda_D`.  Consequently, with `lambda_R` denoting the exact RSJ
constant,

```math
\boxed{
\liminf \nu_D\ge\lambda_R
=0.5921405436062881570\ldots .
}
\tag{SZ.2}
```

The endpoint is impossible.  In fact there are absolute constants
`epsilon_0>0` and `D_0<infinity` such that every sufficiently large post-ZF survivor
in the `s_Z=0` phase satisfies

```math
\boxed{
\frac{e_{BB}+2s_C-3d_H}{D}
\ge\lambda_R+\epsilon_0.
}
\tag{SZ.3}
```

Equivalently,

```math
\boxed{
\frac{e_{BB}+2s_C}{D}
\ge
\lambda_R+\epsilon_0+3\frac{d_H}{D}.
}
\tag{SZ.4}
```

This is a real structural strengthening of the generic RSJ floor: every linear amount
of diameter-component defect costs three additional units of pinned/contact surplus.
Thus any `s_Z=0` sequence whose ordinary surplus remains near the generic lower
frontier must satisfy

```math
\boxed{d_H=o(D).}
\tag{SZ.5}
```

Moreover, any hypothetical sequence approaching the un-gapped endpoint in SZ.2 would
force

```math
\boxed{
s_C=o(D),\qquad c_B=o(D),\qquad Q=o(D),
\qquad b-\operatorname{per}F=o(D),
}
\tag{SZ.6}
```

and is then contradicted directly by the DD outer-pocket detour theorem.  The endpoint
exclusion therefore has a C-II-native proof and does not need the RSJ equality-case
classification after the RSJ minimizer has been identified.

---

## 1. Exact `s_Z=0` identities

Assume the post-ZF source lies in the exact circuit phase

```math
\boxed{s_Z=0.}
\tag{1.1}
```

Then the mixed framework has exactly one row dependence, namely the normalized KKT
stress.  The exact ZF perimeter identity becomes

```math
\boxed{b+Q=2h.}
\tag{1.2}
```

Write

```math
d_H=q-h\ge0.
\tag{1.3}
```

Hence

```math
q=h+d_H.
\tag{1.4}
```

ZK gives

```math
\sum_r\delta_r+R_I+s_B+3d_H
=6+e_{BB}+2s_C.
\tag{1.5}
```

Set

```math
L_2:=6+e_{BB}+2s_C-3d_H.
\tag{1.6}
```

Every term on the left of (1.5) other than `3d_H` is nonnegative, so

```math
\boxed{L_2\ge0.}
\tag{1.7}
```

This is the first place where the `-3d_H` term must not be discarded.

---

## 2. The attachment-cell area uses `nu`, not `lambda`

The sharpened ZK/GU attachment estimate is

```math
\sum_r\operatorname{area}(P_r)
\le
\frac\pi4L_2^2+\pi L_2+\pi^2D.
\tag{2.1}
```

Pass to any unbounded convergent subsequence and write

```math
\lambda=\lim\frac{e_{BB}+2s_C}{D},
\qquad
d=\lim\frac{d_H}{D},
\qquad
\nu=\lambda-3d.
\tag{2.2}
```

By (1.7), `nu>=0`.  Dividing (2.1) by `D^2` gives

```math
\boxed{
\limsup\frac{\sum_r\operatorname{area}(P_r)}{D^2}
\le\frac\pi4\nu^2.
}
\tag{2.3}
```

The generic RSJ proof used `lambda` on the right after dropping the negative defect
term.  In the circuit phase the correct radius currency is `nu`.

---

## 3. Exact cavity perimeter also retains `-3d_H`

Use the PC notation

- `a`: number of missing force-hull side contacts / outer pockets;
- `d_P=sum_P(k_P-3)`;
- `c_B`: loaded-loaded unit contacts that are not force-hull sides;
- `P_F=per(F)`;
- `E_out=sum_P(L_P-3)`.

PC gives exactly

```math
x_B=a+d_P
\tag{3.1}
```

and

```math
e_{BB}=q-a+c_B.
\tag{3.2}
```

JC gives the exact pocket-perimeter identity

```math
E_{out}=x_B+P_F-q-a.
\tag{3.3}
```

Eliminate `a` with (3.2):

```math
\begin{aligned}
E_{out}
&=x_B+P_F-q-(q+c_B-e_{BB})\\
&=x_B+P_F-2q+e_{BB}-c_B.
\end{aligned}
\tag{3.4}
```

Since `s_Z=0`, (1.2) and `b=q+x_B` give

```math
x_B=2h-q-Q.
\tag{3.5}
```

Insert (3.5) and `q=h+d_H` into (3.4), then add `Q`:

```math
\boxed{
E_{out}+Q
=e_{BB}-c_B-3d_H+P_F-h.
}
\tag{3.6}
```

This is an equality, not an upper bound.

The force-hull perimeter also satisfies `P_F<=b=2h-Q`.  Therefore (3.6) gives the
second exact-side bound

```math
E_{out}+Q
\le e_{BB}-c_B-3d_H+h-Q.
\tag{3.7}
```

Combining (3.6) and (3.7),

```math
\boxed{
E_{out}+Q
\le
e_{BB}-c_B-3d_H
+
\min\{P_F-h,\ h-Q\}.
}
\tag{3.8}
```

All terms are finite and exact.

Now pass to a convergent subsequence and set

```math
t=\lim\frac{e_{BB}}D,
\quad
c=\lim\frac{c_B}D,
\quad
s=\lim\frac{s_C}D,
\quad
y=\lim\frac hD,
\quad
p=\lim\frac{P_F}D,
\quad
\xi=\lim\frac QD.
\tag{3.9}
```

Then

```math
\nu=t+2s-3d.
\tag{3.10}
```

Normalize (3.8):

```math
\limsup\frac{E_{out}+Q}{D}
\le
t-c-3d+\min\{p-y,y-\xi\}.
\tag{3.11}
```

Since `c,s,xi>=0`,

```math
\boxed{
\limsup\frac{E_{out}+Q}{D}
\le
\nu+\min\{p-y,y\}.
}
\tag{3.12}
```

The force hull has `q` unit-separated convex vertices, so

```math
q\le P_F.
```

Together with `q=h+d_H`, this records the stronger domain condition

```math
\boxed{y+d\le p.}
\tag{3.13}
```

Also (1.2) and `P_F<=b` give

```math
\boxed{p\le2y-\xi\le2y.}
\tag{3.14}
```

---

## 4. The RSJ feasibility theorem with `nu`

The same convex isoperimetric step used in JC gives

```math
H_{out}+A_{exc}
\le
\frac{(E_{out}+Q)^2}{4\pi}+o(D^2).
\tag{4.1}
```

ZG gives

```math
G
\le H_{out}+A_{exc}+O(D),
\tag{4.2}
```

where

```math
G=\operatorname{area}F-\sum_r\operatorname{area}(P_r).
```

Combining (2.3), (3.12), (4.1), and (4.2),

```math
\limsup\frac{\operatorname{area}F}{D^2}
\le
\frac\pi4\nu^2
+
\frac{(\nu+m(y,p))^2}{4\pi},
\tag{4.3}
```

with

```math
m(y,p):=\min\{y,p-y\}.
\tag{4.4}
```

But FSDB plus the merged RSJ central-symmetral theorem gives

```math
\liminf\frac{\operatorname{area}F}{D^2}
\ge
A_*(y,p):=
\max\left\{
\frac{y+\sin y}{4},
\frac\pi{(\pi-2)^2}\left(\frac p2-1\right)^2
\right\}.
\tag{4.5}
```

Therefore every `s_Z=0` survivor limit satisfies

```math
\boxed{
A_*(y,p)-\frac\pi4\nu^2
\le
\frac{(\nu+m(y,p))^2}{4\pi}.
}
\tag{4.6}
```

This is exactly the RSJ necessary inequality with `nu` substituted for `lambda`.
Its parameter domain is even smaller than the domain minimized in RSJ, because of
(3.13)–(3.14).  The RSJ minimization therefore applies immediately and gives

```math
\boxed{\nu\ge\lambda_R.}
\tag{4.7}
```

This proves SZ.2.

---

## 5. Equality-near structure in the circuit phase

Assume hypothetically that

```math
\nu_D\to\lambda_R.
\tag{5.1}
```

RSJ proves that its relaxed two-variable minimum is unique.  Hence

```math
\boxed{
\frac hD\to y_R,
\qquad
\frac{P_F}{D}\to p_R=2y_R.
}
\tag{5.2}
```

The exact cavity bound before relaxation is, from (3.11),

```math
\frac{E_{out}+Q}{D}
\le
\nu_D
-2\frac{s_C}{D}
-\frac{c_B}{D}
+
\min\left\{
\frac{P_F-h}{D},
\frac{h-Q}{D}
\right\}
+o(1).
\tag{5.3}
```

At the RSJ minimum, the relaxed last term tends to `y_R`.  The threshold root is
strictly decreasing in that cavity-perimeter argument.  Thus any fixed positive limit
of `s_C/D` or `c_B/D` would decrease the available cavity perimeter by a fixed amount
and force `nu` strictly above `lambda_R`.  Therefore

```math
\boxed{s_C=o(D),\qquad c_B=o(D).}
\tag{5.4}
```

Likewise, because `P_F/D->2y_R`, the first member of the minimum in (5.3) tends to
`y_R`.  If `Q/D` had a positive subsequential limit, the second member would be
strictly smaller than `y_R`; the same strict monotonicity would again force a positive
threshold gap.  Hence

```math
\boxed{Q=o(D).}
\tag{5.5}
```

Finally (1.2), (5.2), and (5.5) give

```math
\boxed{
\frac{b-P_F}{D}
=2\frac hD-\frac QD-\frac{P_F}{D}
\longrightarrow0.
}
\tag{5.6}
```

These are the circuit-phase equality currencies that were invisible after the generic
JC relaxations.

---

## 6. DD rules out the endpoint directly

DD proves the exact global outer-pocket estimate

```math
H_{out}
\le
\frac1{\sqrt6}(x_B+a)^{3/2}\sqrt{b-P_F}.
\tag{6.1}
```

PC gives `a<=x_B`, while `x_B<=b<=2h`.  Hence

```math
x_B+a=O(D).
\tag{6.2}
```

Together with (5.6), DD gives

```math
\boxed{H_{out}=o(D^2).}
\tag{6.3}
```

The exceptional-face isoperimetric estimate gives

```math
A_{exc}
\le\frac{Q^2+O(D)}{4\pi}.
\tag{6.4}
```

By (5.5),

```math
\boxed{A_{exc}=o(D^2).}
\tag{6.5}
```

ZG now yields

```math
\boxed{G=o(D^2).}
\tag{6.6}
```

But FSDB/RSJ and the attachment estimate give at the unique endpoint

```math
\liminf\frac G{D^2}
\ge
A_R-\frac\pi4\lambda_R^2.
\tag{6.7}
```

The right side is strictly positive: `A_R>0`, and the RSJ defining equation itself
writes

```math
A_R-\frac\pi4\lambda_R^2
=
\frac{(\lambda_R+y_R)^2}{4\pi}>0.
\tag{6.8}
```

Equations (6.6) and (6.7) contradict each other.  Therefore no sequence satisfying
(5.1) exists.

This proof uses the RSJ inequality and unique minimizer but does not use the equality
case of the Rogalski–Saint Raymond convex-body theorem.

---

## 7. Uniform circuit-phase gap

Suppose SZ.3 were false.  Then for every integer `j` there would be a post-ZF
`s_Z=0` survivor with `D_j>=j` and

```math
\nu_{D_j}<\lambda_R+\frac1j.
```

SZ.2 gives `liminf nu_{D_j}>=lambda_R`, so after passing to a subsequence

```math
\nu_{D_j}\to\lambda_R,
```

contradicting Section 6.  This proves SZ.3.

Since

```math
\lambda_D=\nu_D+3\frac{d_H}{D},
```

SZ.4 follows.

In particular, if a sequence has

```math
\lambda_D\le\lambda_R+\epsilon_0+o(1),
```

then SZ.4 forces

```math
d_H=o(D),
```

which proves SZ.5.

---

## 8. A local circuit sparsity inequality

The exact circuit assumption also gives a useful local fact independent of the area
argument.

Let `I_r` be one unloaded contact component, with `n_r=|I_r|`, attachment set
`A_r subset B`, and `a_r=|A_r|`.  Let `m_r` be the number of mixed edges of
`C union H` whose two endpoints both lie in `A_r`.

ZK gives

```math
e_r+t_r=2n_r+1+s_r.
\tag{8.1}
```

All these `e_r+t_r` contact edges lie in the mixed subgraph supported on
`I_r union A_r`, together with the `m_r` attachment-attachment mixed edges.

If this supported mixed edge set is a **proper** subset of the full circuit, circuit
minimality makes it independent, so

```math
2n_r+1+s_r+m_r
\le2(n_r+a_r)-3.
```

Therefore

```math
\boxed{s_r+m_r\le2a_r-4}
\tag{8.2}
```

for every proper component-plus-attachments subframework.

There is one exceptional possibility: a single unloaded component together with its
attachments may support the entire mixed circuit.  Then the full circuit has
`2(n_r+a_r)-2` edges, and the same count gives the exact identity

```math
\boxed{s_r+m_r=2a_r-3.}
\tag{8.3}
```

Thus the unconditional local statement is

```math
\boxed{s_r+m_r\le2a_r-3,}
\tag{8.4}
```

with the sharper `2a_r-4` bound whenever the local supported edge set is proper.

This confirms that pinned-contact surplus is not a free local stress currency in the
circuit phase.  It must be paid by attachment cardinality after every actual mixed
edge already present among the attachments is charged.  Summing (8.4) alone is not a
closure: the planar attachment-incidence bound still permits linear `s_C`.

---

## 9. Regression audit

- **Regular odd shell:** `d_H=0`, `s_C=0`, but its direct loaded-loaded contact count is
  large.  It lies far above the new lower endpoint and is not excluded falsely.
- **Perfect matching:** already excluded by NB.  SZ does not use that branch.
- **Contact-isolated source points:** retained.  FSDB/RSJ use the full-source
  circumcenter input from FS; no force-bulk assumption is introduced.
- **Large `d_H`:** not discarded.  SZ.4 charges it with coefficient three.
- **Large pinned surplus:** retained.  SZ.3 is a lower bound, not a claimed universal
  upper bound.
- **Outer-pocket detour:** used only after the equality-near chain proves
  `b-P_F=o(D)`; no uniform area-per-pocket assertion is made.
- **Local circuit inequality:** the whole-circuit exception is handled by (8.3); no
  proper-subset independence is applied to the full circuit itself.

---

## 10. Exact remaining obstruction

The circuit phase is now reduced to a stronger high-surplus state:

```math
\frac{e_{BB}+2s_C}{D}
\ge
\lambda_R+\epsilon_0+3\frac{d_H}{D}.
```

A useful closing theorem would give an upper tradeoff on the same three currencies.
The most direct possibilities are:

1. bound `s_C` using circuit sparsity plus the geometry of overlapping attachment
   sets, rather than planar incidence alone;
2. exploit `d_H=o(D)` in the near-frontier branch to classify the diameter thrackle as
   an `o(D)`-component perturbation of its unicyclic regime;
3. combine DD quantitatively with (3.8), retaining `Q,c_B,s_C,d_H` rather than only
   using the endpoint limit.  This should give an explicit improvement over
   `lambda_R` in the `s_Z=0` phase.

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Assume s_Z=0 and put
    nu_D=(e_BB+2s_C-3d_H)/D.
ZK gives attachment radius
    L2=6+e_BB+2s_C-3d_H,
so attachment-cell area / D^2 <= pi nu^2/4 + o(1).

Using PC exactly, not only JC.5:
    E_out+Q
      = e_BB-c_B-3d_H+P_F-h
      <= e_BB-c_B-3d_H+min(P_F-h,h-Q).
Thus the JC cavity upper bound is controlled by
    nu+min(p-y,y)
with y=h/D, p=P_F/D.
Therefore the merged RSJ feasibility theorem applies with nu in place of lambda:
    liminf nu_D >= lambda_R=0.592140543606288...

The endpoint cannot occur.  Approaching it forces
    y->y_R, p->2y_R,
    s_C=o(D), c_B=o(D), Q=o(D),
    b-P_F=o(D).
DD then gives H_out=o(D^2); Q=o(D) gives A_exc=o(D^2), while the
FSDB-minus-attachment gap stays positive. Contradiction.
Hence for some epsilon_0>0,
    (e_BB+2s_C-3d_H)/D >= lambda_R+epsilon_0
for all sufficiently large s_Z=0 survivors.
Equivalently
    (e_BB+2s_C)/D >= lambda_R+epsilon_0+3d_H/D.

For one unloaded component with a_r attachments and m_r mixed edges among them,
    s_r+m_r <= 2a_r-3
always, and <=2a_r-4 when its supported edge set is proper.

Next: make the DD exclusion quantitative in (y,p,Q,c_B,s_C,d_H), or exploit
near-frontier d_H=o(D) to classify the diameter thrackle.
```
