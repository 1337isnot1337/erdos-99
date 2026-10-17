> Generated reading edition · [exact source](../../../docs/reports/target_c_all_surplus_explicit_0597_gap_2026-09-11.md) · source SHA-256 `f58f3abc983a838488aa9784d4abba1fd53cd7a4583288e47eb8d3cf28ea9c24`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-19825AFEDACB","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — explicit `0.597` ordinary-surplus floor for every post-ZF branch

**Date:** 2026-09-11  
**Repository base:** `053e1e1b85643b738b4cde306838d150ea325783`  
**Run type:** branch-unification / exact quantitative contradiction  
**Target:** Target C C-II after ZF, with arbitrary `s_Z>=0`  
**Depends on:** DB, FSDB, ZK, ZG/GU, JC/PC outer-pocket identities, DD, exceptional-face isoperimetry, and the scalar RSJ monotonicity argument used in E597  
**External input:** none  
**Computation:** none used in the proof

## LEVEL I STATUS

`STILL OPEN`.

The existing E597 report proves, only in the exact circuit phase `s_Z=0`, a uniform gap above `0.597` for the **renormalized** currency

```math
\frac{e_{BB}+2s_C-3d_H}{D}.
```

Its proof contains a stronger branch-uniform consequence that was not extracted. Put

```math
S:=e_{BB}+2s_C.
```

### Theorem AG.1 — all-surplus `0.597` gap

There are absolute constants

```math
\varepsilon_{AG}>0,
\qquad D_0<\infty
```

such that every sufficiently large post-ZF C-II survivor, with **arbitrary** `s_Z>=0`, satisfies

```math
\boxed{
\frac{e_{BB}+2s_C}{D}
\ge0.597+\varepsilon_{AG}.
}
\tag{AG.1}
```

Equivalently, no unbounded post-ZF survivor sequence can have

```math
\liminf\frac SD\le0.597.
```

The proof uses the same rational barriers `1.523`, `0.024`, and `0.597` as E597. The important point is monotonicity: positive `d_H` and positive `s_Z` only

1. decrease ZK's attachment-cell radius `6+S-3(d_H+s_Z)` relative to `6+S`; and
2. shorten the outer contact walk through `b+Q=2h-2s_Z`.

Thus they cannot rescue a state with ordinary surplus `S/D<=0.597`.

This does **not** eliminate the `s_Z>0` branch. It removes only its low-ordinary-surplus region. In particular regular odd shells have `s_Z=2` but `S/D` is large, so the required regression survives.

---

## 1. General normalized variables

Assume for contradiction that an unbounded sequence of post-ZF survivors has

```math
\lambda_D:=\frac{S}{D}
\to\lambda\le u_0,
\qquad
u_0:=u_0:=\frac{597}{1000}.
\tag{1.1}
```

Pass to a subsequence on which

```math
y:=\lim\frac hD,
\qquad
p:=\lim\frac{P_F}{D}
```

exist.

Write

```math
\delta:=2y-p\ge0.
\tag{1.2}
```

The post-ZF boundary geometry gives

```math
y\le p\le2y,
\qquad p\le\pi.
\tag{1.3}
```

Indeed `q=h+d_H>=h`, the `q` loaded boundary vertices are unit-separated around `partial F`, so `P_F>=q>=h`; while the outer contact walk satisfies

```math
b+Q=2h-2s_Z
```

and `P_F<=b`, hence `P_F<=2h`.

DB gives

```math
y\ge2\rho,
\qquad
\rho=\cos\rho,
\tag{1.4}
```

for every post-ZF survivor, independently of `s_Z`.

Define exactly as in E597

```math
\Phi(y)=\frac{y+\sin y}{4},
\qquad
\Psi(p)=\frac\pi{(\pi-2)^2}\left(\frac p2-1\right)^2,
\tag{1.5}
```

and

```math
J_u(m)=\frac\pi4u^2+\frac{(u+m)^2}{4\pi}.
\tag{1.6}
```

---

## 2. The RSJ necessary inequality is valid with ordinary surplus

FSDB gives the force-hull area lower bound

```math
\liminf\frac{\operatorname{area}F}{D^2}
\ge
\max\{\Phi(y),\Psi(p)\}.
\tag{2.1}
```

ZK gives the exact attachment-radius currency

```math
L_2=6+S-3(d_H+s_Z).
\tag{2.2}
```

Therefore

```math
L_2\le6+S
```

and the attachment-cell estimate gives

```math
\limsup
\frac{\sum_r\operatorname{area}(P_r)}{D^2}
\le\frac\pi4\lambda^2.
\tag{2.3}
```

Let `G` be the uncovered force-hull gap. Hence

```math
\liminf\frac G{D^2}
\ge
\max\{\Phi(y),\Psi(p)\}-\frac\pi4\lambda^2.
\tag{2.4}
```

On the cavity side, the exact post-ZF identity is

```math
E_{out}+Q
=e_{BB}-c_B-3d_H-2s_Z+P_F-h.
\tag{2.5}
```

Every omitted term is nonnegative, and `e_BB<=S`, so

```math
E_{out}+Q
\le S+P_F-h.
\tag{2.6}
```

The joint pocket/exceptional-face isoperimetric estimate gives

```math
H_{out}+A_{exc}
\le\frac{(E_{out}+Q)^2}{4\pi}+o(D^2),
\tag{2.7}
```

and ZG gives

```math
G\le H_{out}+A_{exc}+O(D).
\tag{2.8}
```

Combining (2.4), (2.6)--(2.8) gives the necessary condition

```math
\boxed{
\max\{\Phi(y),\Psi(p)\}
\le
J_\lambda(p-y).
}
\tag{2.9}
```

Since `lambda<=u_0` and `J_u(m)` is increasing in `u,m>=0`, every proposed survivor in (1.1) satisfies

```math
\boxed{
\max\{\Phi(y),\Psi(2y-\delta)\}
\le
J_{u_0}(y-\delta).
}
\tag{2.10}
```

This is exactly the scalar inequality used by E597. No `s_Z=0` identity has been used.

---

## 3. The same rational barriers force `y<1.523`

For auditability, repeat the numerical-free certificate rather than importing its conclusion by prose.

Use

```math
\frac{6283}{2000}<\pi<\frac{3927}{1250}<\frac{22}{7},
\tag{3.1}
```

so

```math
\frac\pi4<\frac{3927}{5000},
\qquad
\frac1{4\pi}<\frac{500}{6283}.
\tag{3.2}
```

The audited FSDB constants give

```math
\frac{739}{1000}<\rho<\frac{37}{50},
\qquad
\sin\rho>\frac{84}{125},
\tag{3.3}
```

and therefore

```math
A_{FS}:=\Phi(2\rho)
=\frac{\rho(1+\sin\rho)}2
>
\boxed{\frac{154451}{250000}}
=0.617804.
\tag{3.4}
```

Let

```math
y_0:=\frac{1523}{1000}.
```

Writing `y_0=pi/2-z`, the bound `pi<22/7` gives `0<z<339/7000`; hence

```math
\sin y_0>\frac{4993}{5000}
```

and

```math
\boxed{\Phi(y_0)>0.6304.}
\tag{3.5}
```

RSJ's crossover analysis for the scalar inequality (2.10) gives, for `y>=y_R`, the optimizing perimeter

```math
p_e(y)=2+2\sqrt{\frac{\Phi(y)}{c_R}},
\qquad
c_R=\frac\pi{(\pi-2)^2},
\tag{3.6}
```

with a strictly increasing threshold `r_+(y)`.

As in E597, `c_R>77/32` and `Phi(y_0)<2523/4000` imply

```math
p_e(y_0)<3.024<3.046=2y_0,
\tag{3.7}
```

so `y_0>y_R`. Also

```math
m_e(y_0):=p_e(y_0)-y_0<1.501.
```

Then

```math
\begin{aligned}
J_{u_0}(m_e(y_0))
&<J_{u_0}(1.501)\\
&<
\frac{3927}{5000}\left(\frac{597}{1000}\right)^2
+
\frac{500}{6283}\left(\frac{2098}{1000}\right)^2\\
&<0.630203
<\Phi(y_0).
\end{aligned}
\tag{3.8}
```

Thus `lambda<=u_0` is impossible at `y_0`, and strict monotonicity of the RSJ threshold for `y>=y_R` excludes every larger `y`. Therefore

```math
\boxed{y<1.523.}
\tag{3.9}
```

---

## 4. The same scalar inequality forces `delta<0.024`

A lower bound on the crossover perimeter is also unchanged. From `pi>6283/2000` one obtains

```math
c_R<2.411.
\tag{4.1}
```

Together with (3.5),

```math
\frac{\Phi(y_0)}{c_R}
>\frac{0.6304}{2.411}>(0.511)^2,
```

so

```math
p_e(y_0)>3.022.
```

Hence

```math
\boxed{0<2y_0-p_e(y_0)<0.024.}
\tag{4.2}
```

Suppose `delta>=0.024`. If `y<=y_R`, then `p_e(y)>=2y`, so `p=2y-delta<p_e(y)`. If `y_R<=y<y_0`, RSJ gives `p_e'(y)<1`, hence

```math
\delta_e(y):=2y-p_e(y)
```

is increasing and, by (4.2), `delta_e(y)<0.024<=delta`; again `p<p_e(y)`.

Thus throughout the allowed range, `Psi(p)<Phi(y)` and (2.10) reduces to

```math
\Phi(y)
\le J_{u_0}(y-\delta)
\le J_{u_0}(y-0.024).
\tag{4.3}
```

Define

```math
F(y):=J_{u_0}(y-0.024)-\Phi(y).
```

On `[2rho,y_0]`,

```math
F'(y)
=\frac{u_0+y-0.024}{2\pi}-\frac{1+\cos y}{4}
>0.326-0.275
>0.
\tag{4.4}
```

At `y_0`,

```math
J_{u_0}(1.499)<0.629535<0.6304<\Phi(y_0),
```

so `F(y_0)<0`. Since `F` is increasing, `F(y)<0` on the entire interval, contradicting (4.3). Therefore

```math
\boxed{\delta<0.024.}
\tag{4.5}
```

Again this used only the general scalar necessary inequality (2.10).

---

## 5. Positive `s_Z` makes the DD detour bound stronger

Return to the finite sequence and put

```math
\delta_D:=\frac{2h-P_F}{D},
\qquad
\xi_D:=\frac QD,
\qquad
\sigma_D:=\frac{s_Z}{D}.
\tag{5.1}
```

Then `delta_D->delta<0.024`.

The exact post-ZF closing identity is

```math
b+Q=2h-2s_Z.
\tag{5.2}
```

Therefore

```math
\boxed{
\frac{b-P_F}{D}
=\delta_D-\xi_D-2\sigma_D\ge0.
}
\tag{5.3}
```

Consequently

```math
0\le\xi_D+2\sigma_D
\le\delta_D
<0.024+o(1),
\tag{5.4}
```

and, separately,

```math
\frac{b-P_F}{D}<0.024+o(1),
\qquad
\frac QD<0.024+o(1).
\tag{5.5}
```

Also

```math
x_B=b-q=h-d_H-2s_Z-Q\le h,
\tag{5.6}
```

and PC gives `a<=x_B`. Hence, using `h/D<1.523+o(1)`,

```math
\boxed{
\frac{x_B+a}{D}<3.046+o(1).
}
\tag{5.7}
```

DD.2 is valid with arbitrary `s_Z` and gives

```math
H_{out}
\le
\frac1{\sqrt6}(x_B+a)^{3/2}\sqrt{b-P_F}.
\tag{5.8}
```

Use the same rational square-root barriers as E597:

```math
\frac1{\sqrt6}<0.409,
\qquad
\sqrt{3.046}<1.746,
\qquad
\sqrt{0.024}<0.155.
```

Thus

```math
\boxed{
\limsup\frac{H_{out}}{D^2}
<0.33715464282.
}
\tag{5.9}
```

Exceptional-face isoperimetry and (5.5) give

```math
\boxed{
\limsup\frac{A_{exc}}{D^2}
<0.00004608.
}
\tag{5.10}
```

Therefore

```math
\boxed{
\limsup\frac{H_{out}+A_{exc}}{D^2}
<0.33720072282.
}
\tag{5.11}
```

Since ZG gives `G<=H_out+A_exc+O(D)`,

```math
\boxed{
\limsup\frac G{D^2}<0.33720072282.
}
\tag{5.12}
```

Notice that `s_Z>0` only subtracts `2s_Z` from the available detour in (5.3). It cannot enlarge this upper capacity.

---

## 6. FSDB and general ZK force a larger gap

By DB, `y>=2rho`, and FSDB therefore gives

```math
\liminf\frac{\operatorname{area}F}{D^2}
\ge A_{FS}
>0.617804.
\tag{6.1}
```

General ZK gives

```math
L_2=6+S-3(d_H+s_Z)\le6+S.
```

The attachment-cell estimate therefore yields

```math
\limsup\frac{\sum_r\operatorname{area}(P_r)}{D^2}
\le\frac\pi4\lambda^2.
```

Under `lambda<=0.597`,

```math
\boxed{
\limsup\frac{\sum_r\operatorname{area}(P_r)}{D^2}
<0.2799236286.
}
\tag{6.2}
```

Hence

```math
\boxed{
\liminf\frac G{D^2}
>
0.617804-0.2799236286
=0.3378803714.
}
\tag{6.3}
```

This contradicts (5.12), with the same fixed separation as E597:

```math
\boxed{
0.3378803714-0.33720072282
=0.00067964858>0.
}
\tag{6.4}
```

Therefore no unbounded post-ZF survivor subsequence can satisfy `lambda<=0.597`.

---

## 7. Uniform positive gap

If AG.1 failed for every positive `epsilon`, choose post-ZF survivors with

```math
D_j\ge j,
\qquad
\frac{S_j}{D_j}<0.597+\frac1j.
```

Pass to a convergent subsequence of `S_j/D_j`. Its limit is at most `0.597`, contradicting Section 6. Therefore some absolute `epsilon_AG>0` and `D_0` exist, proving AG.1.

No numerical value of `epsilon_AG` is claimed.

---

## 8. What this changes and what it does not

E597 remains strictly stronger inside `s_Z=0`, because there it controls

```math
\frac{S-3d_H}{D},
```
not merely `S/D`.

AG.1 instead has broader scope:

```math
\boxed{
\text{all post-ZF branches, including }s_Z>0:
\quad S/D>0.597+\varepsilon_{AG}.
}
```

The theorem removes the entire low-ordinary-surplus positive-`s_Z` region from the C-II ledger. It does **not** prove `s_Z=0`, does not bound `s_Z` by `o(D)`, and does not settle the high-surplus region.

In particular:

- regular odd shells have `s_Z=2` and are not excluded by AG.1;
- contact-isolated source points remain fully allowed;
- no `s_Z=0` circuit sparsity, exact `b+Q=2h`, or Woodall forest/cyclic branch classification was used;
- the proof is compatible with arbitrary `d_H>=0` because positive `d_H` only decreases `L_2` and the exact cavity currency.

---

## 9. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| general RSJ inequality (2.9) with `S` | proved | FSDB + ZK + exact cavity + joint isoperimetry |
| `y<1.523`, `delta<0.024` | proved | same rational scalar argument as E597 |
| DD capacity with arbitrary `s_Z` | proved | exact `b+Q=2h-2s_Z` and general DD.2 |
| general attachment lower gap | proved | `L_2<=6+S` |
| all-branch `S/D>0.597+epsilon_AG` | proved | fixed-margin contradiction + compactness |
| renormalized bound for `s_Z>0` | not proved | positive surplus is not canceled from the cavity identity |
| elimination of `s_Z>0` | not proved | high ordinary surplus remains feasible |
| Level I | still open | high-surplus and exact-source obstructions remain |

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Let S=e_BB+2s_C and suppose S/D->lambda<=0.597 along arbitrary post-ZF survivors,
with no assumption s_Z=0. FSDB and general ZK give
    area(F)/D^2 >= max(Phi(y),Psi(p)),
    attachment area/D^2 <= (pi/4)lambda^2.
The exact cavity identity gives
    E_out+Q=e_BB-c_B-3d_H-2s_Z+P_F-h
           <= S+P_F-h.
Hence exactly the same scalar RSJ necessary inequality holds:
    max(Phi(y),Psi(p)) <= J_lambda(p-y).
The E597 rational barriers therefore still force
    y=h/D<1.523,
    delta=(2h-P_F)/D<0.024.

General post-ZF closing gives
    b+Q=2h-2s_Z,
so
    (b-P_F)/D=delta-Q/D-2s_Z/D,
and therefore both Q/D and (b-P_F)/D are <0.024+o(1).
Also x_B+a<=2h<3.046D+o(D).
General DD then gives
    H_out/D^2<0.33715464282,
and exceptional-face area adds <0.00004608.
Thus
    G/D^2<0.33720072282.

But DB+FSDB give area(F)/D^2>0.617804, while
    L_2=6+S-3(d_H+s_Z)<=6+S
makes attachment area/D^2<0.2799236286. Hence
    G/D^2>0.3378803714,
a contradiction with fixed margin 0.00067964858.

Therefore some epsilon_AG>0 exists such that every sufficiently large post-ZF
survivor, including s_Z>0, satisfies
    (e_BB+2s_C)/D >=0.597+epsilon_AG.
This does not eliminate s_Z>0; it eliminates only its low ordinary-surplus region.
```
