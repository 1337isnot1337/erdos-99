> Generated reading edition · [exact source](../../../docs/reports/target_c_sz0_explicit_05981_detour_gap_2026-09-10.md) · source SHA-256 `87490799051257775bf4a9d58f0ca2995b8adf16ec0f8f856fbb9240ac04cc77`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Presentation repairs: 2 exact-source-bound TeX/escape correction(s); [reviewed repair ledger](../../../docs/publication/reading-tex-repairs.json). Frozen source bytes are unchanged.

<!-- theorem-state: {"artifact_id":"ART-599BDCFC19DB","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — exact `0.5981` circuit-phase surplus floor

**Date:** 2026-09-10  
**Repository base:** `7e1bafe15ba51b4ec7441bf158d7c18e53759485`  
**Run type:** quantitative C-II branch exclusion / exact rational certificate  
**Target:** Target C, post-ZF `s_Z=0` mixed-circuit phase  
**Depends on:** SZ, E597, RSJ, FSDB, ZK, DD, exceptional-face isoperimetry, ZG  
**External input:** none beyond already imported dependencies  
**Computation:** exact rational certificate only; no floating-point assertion is used

## LEVEL I STATUS

`STILL OPEN`.

The current main report E597 proves an explicit lower floor `0.597` for

```math
\nu_D:=\frac{e_{BB}+2s_C-3d_H}{D}
```

in the post-ZF `s_Z=0` circuit phase.  Retaining the same RSJ and DD inequalities but
certifying the feasible `(y,delta)` region at finer scale improves this to

```math
\boxed{
\liminf_{D\to\infty}\nu_D>\frac{5981}{10000}=0.5981.
}
\tag{E5981.1}
```

Equivalently, there are absolute constants `epsilon_5981>0` and `D_0<infinity` such
that every sufficiently large post-ZF survivor in the `s_Z=0` phase satisfies

```math
\boxed{
\frac{e_{BB}+2s_C-3d_H}{D}
\ge0.5981+\epsilon_{5981}.
}
\tag{E5981.2}
```

Thus

```math
\boxed{
\frac{e_{BB}+2s_C}{D}
\ge0.5981+\epsilon_{5981}+3\frac{d_H}{D}.
}
\tag{E5981.3}
```

The proof is not a floating-point optimization.  The accompanying script
`research/target_c_e5981_certificate.py` checks 470 exact rational interval cells.
Its weakest localization margin is

```math
\frac{133924761}{9620843750000000}>0,
```

and its weakest force-gap/cavity-capacity margin is

```math
\frac{55831047300377}{307867000000000000}>0.
```

The improvement is small numerically but has a precise structural meaning: after the
SZ renormalization, every exact mixed-circuit survivor must spend more than `0.5981D`
of the combined component-diameter, Eppstein-defect, and loaded-degree-slack budget,
because ZK gives

```math
\nu_DD
=
\sum_r\delta_r+R_I+s_B-6.
```

Level I remains open because no universal upper bound below this floor is known, and
the `s_Z>0` phase remains outside the present theorem.

---

## 1. Endpoint and exact implication

Assume throughout the post-ZF `s_Z=0` phase.  Set

```math
y_D:=\frac hD,
\qquad
p_D:=\frac{P_F}{D},
\qquad
\delta_D:=2y_D-p_D.
\tag{1.1}
```

SZ gives

```math
2\rho\le y_D+o(1),
\qquad
y_D\le p_D\le2y_D,
\tag{1.2}
```

and the RSJ necessary inequality with `nu` in place of the generic pinned/contact
currency.  On a convergent subsequence write

```math
y=\lim y_D,
\qquad
p=\lim p_D,
\qquad
\delta=2y-p.
```

Put

```math
\Phi(y):=\frac{y+\sin y}{4},
\qquad
\Psi(p):=\frac\pi{(\pi-2)^2}\left(\frac p2-1\right)^2,
\tag{1.3}
```

and

```math
J_u(m):=\frac\pi4u^2+\frac{(u+m)^2}{4\pi}.
\tag{1.4}
```

Since `p<=2y`, the RSJ cavity-perimeter variable is `m=p-y=y-delta`.  Hence every
limit with `nu<=u` satisfies

```math
\boxed{
\Phi(y)
\le
\max\{\Phi(y),\Psi(p)\}
\le
J_u(y-\delta).
}
\tag{1.5}
```

The proof below combines (1.5) with the sharper DD geometry rather than replacing DD
by the isoperimetric cavity bound already built into RSJ.

The exact closing implication is

```text
nu <= 0.5981
  + RSJ -> y<1.525 and a cellwise upper bound on delta=2y-p
  + DD  -> cellwise upper bound on H_out+A_exc
  + FSDB/ZK -> strictly larger cellwise lower bound on G
  + ZG: G<=H_out+A_exc+o(D^2)
  -> contradiction.
```

Every comparison in the final cellwise step is rational.

---

## 2. Rational barriers

Use the already audited E597 bounds

```math
\boxed{
\frac{6283}{2000}<\pi<\frac{3927}{1250}<\frac{22}{7},
\qquad
\rho>\frac{739}{1000}.
}
\tag{2.1}
```

Consequently

```math
\frac1{4\pi}<\frac{500}{6283}.
\tag{2.2}
```

For DD use

```math
\boxed{
\frac1{\sqrt6}<\frac{1633}{4000},
}
\tag{2.3}
```

which is exact because

```math
6\left(\frac{1633}{4000}\right)^2-1
=\frac{67}{8000000}>0.
```

Throughout the proof put

```math
u_0:=\frac{5981}{10000}.
\tag{2.4}
```

For any rational `x` in the range used below, define the rational lower bound

```math
\underline\Phi(x)
:=
\frac14\left[
 x+1-\frac12\left(\frac{11}{7}-x\right)^2
\right].
\tag{2.5}
```

All relevant `x` are below `pi/2`.  Writing `z=pi/2-x`, we have

```math
0<z<\frac{11}{7}-x,
```

and

```math
\sin x=\cos z\ge1-\frac{z^2}{2}
>1-\frac12\left(\frac{11}{7}-x\right)^2.
```

Therefore

```math
\boxed{\Phi(x)>\underline\Phi(x).}
\tag{2.6}
```

Also define the rational upper bound

```math
\overline J_u(m)
:=
\frac{3927}{5000}u^2
+
\frac{500}{6283}(u+m)^2.
\tag{2.7}
```

By (2.1)–(2.2),

```math
\boxed{J_u(m)<\overline J_u(m).}
\tag{2.8}
```

---

## 3. RSJ localizes the diameter density below `1.525`

### Lemma E5981.1

Every subsequential limit satisfying `nu<=u_0` obeys

```math
\boxed{y<\frac{61}{40}=1.525.}
\tag{3.1}
```

### Proof

E597 already proves `y_R<1.523`, where `y_R` is the RSJ crossover, and RSJ proves
that for `y>=y_R` the best allowed perimeter is

```math
p_e(y)=2+2\sqrt{\frac{\Phi(y)}{c_R}},
\qquad
c_R:=\frac\pi{(\pi-2)^2},
\tag{3.2}
```

with the corresponding threshold `r_+(y)` strictly increasing.

Set

```math
y_0:=\frac{61}{40}.
```

The function `x/(x-2)^2` is decreasing for `x>2`.  Using
`pi<3927/1250`,

```math
c_R
>
\frac{3927/1250}{(3927/1250-2)^2}
=
\frac{4908750}{2036329}
>
\frac{241}{100}.
\tag{3.3}
```

Trivially

```math
\Phi(y_0)<\frac{y_0+1}{4}=\frac{101}{160}.
```

The exact rational comparison

```math
\frac{101/160}{241/100}
<\left(\frac{64}{125}\right)^2
\tag{3.4}
```

therefore gives

```math
p_e(y_0)<2+2\frac{64}{125}=3.024.
```

Thus

```math
m_e(y_0):=p_e(y_0)-y_0<1.499.
\tag{3.5}
```

On the other hand, (2.5) gives

```math
\underline\Phi(y_0)=\frac{395751}{627200},
```

while exact rational arithmetic gives

```math
\overline J_{u_0}(1.499)
=
\frac{1982080763828101}{3141500000000000}.
```

Their difference is

```math
\boxed{
\underline\Phi(y_0)
-
\overline J_{u_0}(1.499)
=
\frac{7086830235551}{153933500000000000}>0.
}
\tag{3.6}
```

Since `J_u` is increasing in `m`, (3.5)–(3.6) show that even the optimal RSJ
perimeter at `y_0` requires `nu>u_0`.  Because `r_+` is strictly increasing for
`y>=y_R`, no state with `nu<=u_0` can have `y>=y_0`. `square`

---

## 4. A monotone rational detour localizer

For a rational candidate detour `d`, put

```math
F_d(y):=J_{u_0}(y-d)-\Phi(y).
\tag{4.1}
```

Then

```math
F_d'(y)
=
\frac{u_0+y-d}{2\pi}
-
\frac{1+\cos y}{4}.
\tag{4.2}
```

On

```math
\frac{739}{500}\le y\le\frac{61}{40},
\qquad
0\le d\le\frac{13}{500},
\tag{4.3}
```

we have

```math
0<\frac\pi2-y
<\frac{11}{7}-\frac{739}{500}
=\frac{327}{3500}<\frac1{10}.
```

Hence

```math
\cos y
=\sin(\pi/2-y)<\frac1{10}.
```

Using `pi<22/7`, (4.2) therefore gives the exact lower bound

```math
\begin{aligned}
F_d'(y)
&>
\left(
\frac{5981}{10000}
+
\frac{739}{500}
-
\frac{13}{500}
\right)\frac7{44}
-
\frac{11}{40}\\
&=
\boxed{\frac{22507}{440000}>0.}
\end{aligned}
\tag{4.4}
```

Thus every `F_d` used below is strictly increasing on the entire possible range.

Now partition

```math
\left[\frac{739}{500},\frac{61}{40}\right]
```

into the 470 rational cells

```math
I_k=[L_k,U_k],
\qquad
L_k=\frac{739}{500}+\frac{k}{10000},
\qquad
U_k=L_k+\frac1{10000},
\tag{4.5}
```

for `k=0,...,469`.

For each cell choose `d_k` to be the first multiple of `10^{-5}` for which

```math
\boxed{
\overline J_{u_0}(U_k-d_k)
<
\underline\Phi(U_k).
}
\tag{4.6}
```

The exact certificate verifies `d_k<=0.026` for every cell.  By (2.6), (2.8), and
(4.4),

```math
F_{d_k}(y)<F_{d_k}(U_k)<0
\qquad(y\in I_k).
\tag{4.7}
```

If a feasible state in `I_k` had `delta>=d_k`, then monotonicity of `J` in its second
argument and (1.5) would give

```math
\Phi(y)
\le J_{u_0}(y-\delta)
\le J_{u_0}(y-d_k),
```

contradicting (4.7).  Therefore

```math
\boxed{
y\in I_k\Longrightarrow\delta<d_k.}
\tag{4.8}
```

The weakest exact margin in (4.6) occurs on the cell

```math
[1.4872,1.4873]
```

with `d_k=0.01846`; it is

```math
\boxed{
\frac{133924761}{9620843750000000}>0.
}
\tag{4.9}
```

So the localization has a certified strict sign on every cell.

---

## 5. DD versus the force-gap lower bound

We now derive the second exact inequality certified cellwise.

In the `s_Z=0` phase, DD.15 and the PC identities give

```math
x_B+a
=2h-Q-e_{BB}+c_B.
\tag{5.1}
```

Since `c_B` counts a subset of the `e_{BB}` loaded-loaded contacts,

```math
\boxed{x_B+a\le2h.}
\tag{5.2}
```

Also

```math
b-P_F=2h-Q-P_F\ge0.
```

Therefore

```math
\boxed{
Q\le2h-P_F=\delta_DD,
\qquad
b-P_F\le\delta_DD.
}
\tag{5.3}
```

DD and the exceptional-face isoperimetric estimate now imply, on a subsequence with
`y_D->y` and `delta_D->delta`,

```math
\boxed{
\limsup\frac{H_{out}+A_{exc}}{D^2}
\le
\frac1{\sqrt6}(2y)^{3/2}\sqrt\delta
+
\frac{\delta^2}{4\pi}.
}
\tag{5.4}
```

On the lower side, FSDB gives

```math
\liminf\frac{\operatorname{area}F}{D^2}\ge\Phi(y),
\tag{5.5}
```

while SZ/ZK gives

```math
\limsup\frac{\sum_r\operatorname{area}(P_r)}{D^2}
\le\frac\pi4\nu^2.
\tag{5.6}
```

Thus, for the attachment-cell gap

```math
G=\operatorname{area}F-\sum_r\operatorname{area}(P_r),
```

any state with `nu<=u_0` satisfies

```math
\boxed{
\liminf\frac GD^2
\ge
\Phi(y)-\frac\pi4u_0^2.
}
\tag{5.7}
```

Fix a cell `I_k`.  By (4.8), `y<=U_k` and `delta<d_k`.  Choose the least rational
`s_k` with denominator `10^6` satisfying

```math
s_k^2\ge2U_kd_k.
\tag{5.8}
```

Then

```math
(2y)^{3/2}\sqrt\delta
<
(2U_k)\sqrt{2U_kd_k}
\le2U_ks_k.
\tag{5.9}
```

Using (2.2)–(2.3), (5.4) is therefore bounded above by the rational number

```math
\boxed{
C_k
:=
\frac{1633}{4000}(2U_k)s_k
+
\frac{500}{6283}d_k^2.
}
\tag{5.10}
```

Since `Phi` is increasing on this interval, (2.1), (2.6), and (5.7) bound the force
gap below by

```math
\boxed{
B_k
:=
\underline\Phi(L_k)
-
\frac{3927}{5000}u_0^2.
}
\tag{5.11}
```

The exact certificate checks

```math
\boxed{B_k>C_k}
\tag{5.12}
```

for every one of the 470 cells.

The smallest difference occurs on the final cell

```math
[1.5249,1.525],
```

where

```math
d_k=0.02587,
\qquad
s_k=0.280898,
```

and

```math
\boxed{
B_k-C_k
=
\frac{55831047300377}{307867000000000000}
>0.
}
\tag{5.13}
```

Hence every cell satisfies a fixed strict asymptotic separation

```math
\liminf\frac GD^2
>
\limsup\frac{H_{out}+A_{exc}}{D^2}.
\tag{5.14}
```

But ZG gives

```math
G\le H_{out}+A_{exc}+O(D),
\tag{5.15}
```

which contradicts (5.14).  Therefore no unbounded survivor subsequence can have
`nu<=u_0`.

This proves E5981.1. `square`

---

## 6. Uniform finite threshold

Suppose E5981.2 were false.  Then for every integer `j` there would be an `s_Z=0`
post-ZF survivor with

```math
D_j\ge j,
\qquad
\nu_{D_j}<u_0+\frac1j.
```

Pass to a subsequence on which `y_D` and `p_D` converge; their normalized domains are
compact.  Then `nu_D->u_0` or to a smaller value after a further subsequence, which is
excluded by Sections 3–5.  Hence a uniform `epsilon_5981>0` and `D_0` exist, proving
E5981.2. `square`

---

## 7. Reproducible exact certificate

Run

```bash
python research/target_c_e5981_certificate.py
```

The script uses `fractions.Fraction` and integer square roots only.  The assertions do
not depend on binary floating point.  On the repository state used for this report it
prints

```text
PASS: exact rational E5981 certificate
cells = 470
ymax RSJ margin decimal = 4.6038258309926036e-05
derivative lower bound decimal = 0.05115227272727273
worst localization cell = 1.4872 1.4873
  dbar = 0.01846
  decimal localization margin = 1.392027190962331e-08
worst capacity cell = 1.5249 1.525
  dbar = 0.02587
  sqrt upper = 0.280898
  decimal capacity margin = 0.0001813479434313421
```

The decimal lines are display only; the script also prints the exact rational margins
and asserts their positivity before any output.

### Encoded assumptions

The script encodes only the scalar consequences used above: the E597 rational
constant barriers, the RSJ localization formulas, FSDB/ZK's gap lower bound, DD's
pocket upper bound, the exceptional-face estimate, and the exact `s_Z=0` perimeter
identities.

### Omitted assumptions

It does not prove those geometric inputs, does not encode the full packing, and does
not test global optimality directly.  A PASS is a certificate for the algebraic
combination in Sections 3–5, not a Level I solution.

---

## 8. Adversarial audit

### 8.1 Does the proof accidentally use the disputed RSR equality classification?

No.  RSJ is used only for its inequality and its analytically proved minimizer/
monotonicity.  The endpoint equality classification from Rogalski–Saint Raymond is not
used.

### 8.2 Is `delta=2y-p` really nonnegative?

Yes.  In `s_Z=0`, `b+Q=2h`, and `P_F<=b`, hence `p<=2y-Q/D<=2y`.

### 8.3 Is `Q/D<=delta` valid?

Yes, exactly from

```math
b-P_F=2h-Q-P_F\ge0.
```

Thus `Q<=2h-P_F` before taking limits.

### 8.4 Is `x_B+a<=2h` valid after retaining all PC variables?

Yes.  DD.15 has

```math
x_B+a=2h-Q-e_{BB}+c_B,
```

and `0<=c_B<=e_{BB}`, so the discarded terms only decrease the DD right side.

### 8.5 Does the cellwise `delta` argument reverse a monotonicity?

No.  Feasibility gives `Phi(y)<=J_nu(y-delta)`.  Replacing `nu` by the larger `u_0`
raises `J`.  If `delta>=d_k`, replacing `delta` by the smaller `d_k` also raises `J`.
Thus a necessary condition is `Phi(y)<=J_u0(y-d_k)`.  Section 4 proves the opposite
strictly on each cell.

### 8.6 Do interval endpoints leave gaps?

No.  The 470 cells are adjacent and cover `[1.478,1.525]` exactly.  DB/E597 gives
`y>=2rho>1.478`, while Lemma E5981.1 gives `y<1.525`.

### 8.7 Is the square-root bound numerical rather than certified?

No.  For each cell the script chooses integer `k` and denominator `10^6`, then checks
with integer arithmetic that `(k/10^6)^2>=2U_kd_k`.

### 8.8 Could contact-isolated source points violate the argument?

No.  The force-hull/circumradius transport entering FSDB comes from the full-source FS
statement and therefore retains isolates.  The post-ZF graph variables concern the
nonisolated positive contact network exactly as in SZ/E597.

### 8.9 Odd-shell regression

The odd-shell regression is not excluded by a generic near-radiality statement here.
The proof requires the full post-ZF RSJ/ZK/DD global-source chain and the `s_Z=0`
renormalized defect identity.  The shell's response trace/matching pathology is not
used or contradicted.

### 8.10 Quantifier scope

E5981 excludes every unbounded sequence of lexicographically normalized post-ZF
triangle-free global sources in the `s_Z=0` phase with `nu<=0.5981+o(1)`.  It does not
exclude `s_Z>0` survivors and therefore does not settle C-II.

---

## 9. Claim classification

| Claim | Classification | Reason |
| --- | --- | --- |
| `y<1.525` for `nu<=0.5981` | proved | RSJ monotonicity + exact rational endpoint barrier |
| cellwise `delta` bounds | proved | monotonic `F_d` + 470 exact rational checks |
| DD cavity ceiling on each cell | proved | DD + exact PC/ZF inequalities + rational square-root upper bounds |
| force-gap lower bound on each cell | proved | FSDB + ZK + rational `Phi`/`pi` barriers |
| no `nu<=0.5981` survivor sequence | proved | strict cellwise gap contradicts ZG |
| uniform positive gap above `0.5981` | proved | diagonal subsequence argument |
| analogous result for `s_Z>0` | not proved | SZ renormalization is circuit-phase specific |
| Level I | still open | no full C-II exclusion / upper bound on the surviving currency |

---

## 10. Exact effect on the frontier

The current explicit circuit-phase statement on `main` is E597:

```math
\nu_D>0.597+o(1).
```

E5981 replaces the explicit constant by

```math
\boxed{\nu_D>0.5981+o(1)}
```

and gives a finite rational certificate.  In terms of the original pinned/contact
currency,

```math
\boxed{
\frac{e_{BB}+2s_C}{D}
>
0.5981+3\frac{d_H}{D}+o(1).
}
\tag{10.1}
```

ZK also rewrites the renormalized numerator exactly as

```math
\boxed{
e_{BB}+2s_C-3d_H
=
\sum_r\delta_r+R_I+s_B-6.
}
\tag{10.2}
```

So every surviving circuit-phase source has

```math
\sum_r\delta_r+R_I+s_B
>(0.5981+o(1))D.
\tag{10.3}
```

This is the cleanest structural form of the new obstruction.

---

## 11. Precise remaining implication

The present mechanism is close to its own numerical limit: optimizing the relaxed
RSJ+DD inequalities numerically places the first feasible point only slightly above
`0.5981`.  Iterating the same scalar partition indefinitely is therefore not a
credible Level I route.

A genuinely closing next theorem should use information not spent in E5981.  In the
`s_Z=0` phase, a sufficient result is

```math
\boxed{
\sum_r\delta_r+R_I+s_B
\le(0.5981+o(1))D,
}
\tag{11.1}
```

which would contradict (10.3), or an equivalent upper tradeoff retaining the
individual terms.  The strongest candidate source of such an upper bound is the
Laman-circuit sparsity of component-plus-attachment subframeworks combined with the
noncrossing attachment incidence geometry and the convex-thrackle diameter graph.

For the full C-II problem one must additionally eliminate or reduce the `s_Z>0`
phase.  Merely improving the constant in E5981 does not address that branch.

---

## 12. Promotion recommendation

**Promote after independent audit as a report-level quantitative strengthening of
E597.**

The theorem uses no new external literature and changes no canonical definition.  If
promoted, retain E597 for its coarser hand-checkable rational proof and index E5981 as
the stronger exact finite certificate.  Do not present E5981 as a Level I closure.

---

## 13. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

In post-ZF s_Z=0 define
    nu=(e_BB+2s_C-3d_H)/D.
Current main E597 gives nu>0.597+o(1).

New E5981:
    liminf nu > 0.5981,
and uniformly
    nu >= 0.5981+epsilon_5981
for all sufficiently large circuit-phase survivors.

Proof:
RSJ localizes every nu<=0.5981 state to y=h/D<1.525.
Partition [1.478,1.525] into 470 width-1e-4 cells.  In each cell exact
rational evaluation of Phi(y)<=J_nu(y-delta) gives a rational d_k with
    delta=2y-p<d_k.
DD plus Q/D<=delta and x_B+a<=2h then gives an exact rational upper bound
on (H_out+A_exc)/D^2.  FSDB+ZK gives the strictly larger lower bound
    G/D^2 >= Phi(y)-pi*nu^2/4.
All 470 margins are positive; the smallest is
    55831047300377/307867000000000000 > 0.
ZG contradicts this.

Exact certificate:
    research/target_c_e5981_certificate.py

Structural form via ZK:
    sum_r delta_r + R_I + s_B > (0.5981+o(1))D.

Remaining:
prove an upper tradeoff on those three exact slacks, preferably from Laman-circuit
component sparsity + noncrossing attachment incidence + convex-thrackle diameter
geometry; also cover s_Z>0.
```
