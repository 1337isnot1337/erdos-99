> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_extreme_boundary_slack_transfer_2026-09-10.md) · source SHA-256 `d869a2a335fad9043f535639b351bbe61f2d16dca187f93c2b8804b1616d0e92`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-90F72FD23C23","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic extreme boundary-slack transfer removes the `kappa` loss

**Date:** 2026-09-10  
**Repository state:** PR #178 after MX  
**Run type:** retained-defect cyclic optimization / exact selected-to-full boundary comparison  
**Target:** Target C, maximal cyclic extreme branch  
**Depends on:** MX selected `s_Z=0` infrastructure and cyclic transplant; AE/AX atomic cyclic theorem; full C36 loaded-attachment lower bound; full and selected ZU ledgers  
**External input:** none  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`.

MX proves that a maximal extreme positive circuit (`sigma_*=0`) in Woodall's cyclic
selected branch (`d_*=0`) inherits the full cyclic `0.995540...` theorem. Its first
full-currency comparison lost `2kappa_*`, because it bounded all omitted contact rows
at once.

That loss is unnecessary. The only omitted structure that can reduce the full
pinned/contact currency relative to the selected one lives at the **loaded boundary**.
Retaining the selected loaded contact-degree slack removes all dependence on omitted
interior vertex count.

Let

$$
L_*:=e_{BB,*}+2s_{C,*},
\qquad
s_{B,*}:=3q_*-e_{BI,*}-2e_{BB,*}\ge0,
\tag{BS.1}
$$

and let

$$
L:=e_{BB}+2s_C
$$

be the full C65 currency.

### Theorem BS.1 — retained selected cyclic floor

There exists an absolute constant `epsilon_B>0` such that every sufficiently large
maximal cyclic extreme circuit satisfies

$$
\boxed{
{L_*-(2/3)s_{B,*}\over D}
\ge
\lambda_A+\epsilon_B,
}
\tag{BS.2}
$$

where

$$
\lambda_A
={\pi\over
\sqrt{\pi^2+\left(\frac54-
\sqrt{\frac{\pi}{2\sqrt3}}\right)^2}}
=0.9955405845835427\ldots .
\tag{BS.3}
$$

### Theorem BS.2 — exact full/selected boundary transfer

For every maximal cyclic extreme circuit in a full post-ZF C65 source,

$$
\boxed{
L
\ge
L_*-\frac23s_{B,*}+2d_H+2s_Z.
}
\tag{BS.4}
$$

Consequently **no low-degeneracy hypothesis is needed**:

$$
\boxed{
\liminf {e_{BB}+2s_C\over D}
\ge
\lambda_A+\epsilon_B
>0.9955405845\ldots
}
\tag{BS.5}
$$

along every unbounded post-ZF sequence whose normalized KKT polytope contains a
maximal cyclic extreme circuit.

Even more sharply,

$$
\boxed{
{e_{BB}+2s_C\over D}
\ge
\lambda_A+\epsilon_B
+2{d_H+s_Z\over D}-o(1).
}
\tag{BS.6}
$$

Thus any full diameter-component or mixed-stress defect only raises the full surplus
above the selected cyclic threshold.

---

## 1. Keep `s_{B,*}` in the selected attachment radius

MX proves the selected ZK identity

$$
\sum_r\delta_r+R_{I,*}+s_{B,*}
=6+L_*
\tag{1.1}
$$

because `d_*=0`. Therefore

$$
\sum_r\delta_r
\le6+L_*-s_{B,*}.
\tag{1.2}
$$

The selected attachment-hull area estimate consequently has the sharper asymptotic
form

$$
\limsup {1\over D^2}
\sum_r\operatorname{area}(P_{r,*})
\le
{\pi\over4}\eta^2,
\tag{1.3}
$$

where along a convergent subsequence

$$
\lambda:=\lim {L_*\over D},
\qquad
u:=\lim {s_{B,*}\over D},
\qquad
\boxed{\eta:=\lambda-\nu\ge0.}
\tag{1.4}
$$

Nonnegativity of `eta` follows from (1.1).

The selected cyclic force hull still satisfies

$$
{\operatorname{area}F_*\over D^2}\to{\pi\over4},
\qquad
H_{out,*}=o(D^2).
\tag{1.5}
$$

Hence the refined exceptional-face argument in CRC now gives

$$
\boxed{
w\ge\pi\sqrt{1-\eta^2}}
\tag{1.6}
$$

whenever `eta<1`, where

$$
w:=\lim(Q_*-f_*)/D.
$$

If `eta>=1`, the target BS.2 is already immediate because

$$
\lambda-\frac23\nu
=\eta+\frac13\nu
\ge1>\lambda_A.
\tag{1.7}
$$

Thus only `eta<1` needs further analysis.

---

## 2. The atomic train bound still controls `lambda`

The CRE/DE/AE part of the cyclic proof is unchanged. It depends on the selected
rhombus density and exceptional-face endpoint capacity, not on `s_{B,*}`.

As in AE, if

$$
r:=\lim R_{4,*}/D^2,
$$

then

$$
r\ge {\pi^2-w^2\over2\pi\sqrt3}.
\tag{2.1}
$$

Atomic train incidence gives

$$
4\sqrt r\le\xi+4\varphi,
\qquad
\xi:=\lim Q_*/D,
\qquad
\varphi:=\lim f_*/D,
\qquad
w=\xi-\varphi.
\tag{2.2}
$$

Since selected PC gives

$$
Q_*\le e_{BB,*}\le L_*,
$$

we have `xi<=lambda`. Eliminating `xi,phi,r` exactly as in AE yields

$$
\boxed{
\lambda
\ge
F(w):=rac45
\left(
 w+\sqrt{\frac{\pi^2-w^2}{2\pi\sqrt3}}
\right).
}
\tag{2.3}
$$

Also simply

$$
\boxed{\lambda\ge w}
\tag{2.4}
$$

because `w<=xi<=lambda`.

The function `F(w)` is strictly increasing on the relevant interval `0<=w<=1` used
at the low endpoint. Combining (1.6) and (2.3),

$$
\lambda
\ge
F\bigl(\pi\sqrt{1-\eta^2}\bigr)
\tag{2.5}
$$

whenever the right-hand `w` lies at most one. If it exceeds one, (2.4) is already the
stronger branch for the optimization below.

Substitute

$$
\Delta:=\frac\pi{2\sqrt3}.
$$

At the lower value

$$
w_0(\eta):=\pi\sqrt{1-\eta^2},
$$

the square-root term in (2.3) simplifies exactly:

$$
\sqrt{\frac{\pi^2-w_0(\eta)^2}{2\pi\sqrt3}}
=\sqrt\Delta\,\eta.
\tag{2.6}
$$

Hence define

$$
\boxed{
F_0(\eta)
:=\frac45
\left(
\pi\sqrt{1-\eta^2}+\sqrt\Delta\,\eta
\right).
}
\tag{2.7}
$$

The original atomic threshold `lambda_A` is exactly the unique solution in `(0,1)` of

$$
\boxed{\lambda_A=F_0(\lambda_A).}
\tag{2.8}
$$

---

## 3. Optimize the retained boundary slack

The quantity relevant for transfer to the full graph is

$$
J:=\lambda-\frac23\nu.
$$

Since `nu=lambda-eta`,

$$
\boxed{J={\lambda+2\eta\over3}.}
\tag{3.1}
$$

We prove

$$
\boxed{J\ge\lambda_A.}
\tag{3.2}
$$

If `eta>=lambda_A`, then `lambda>=eta` because `nu>=0`, so

$$
J\ge eta\ge\lambda_A.
\tag{3.3}
$$

Assume now `0<=eta<=lambda_A` and put

$$
w_0=\pi\sqrt{1-\eta^2}.
$$

There are two subranges.

### Range I: `w_0>=F_0(eta)`

Then (2.4) gives `lambda>=w_0`, hence

$$
3J\ge w_0+2\eta.
\tag{3.4}
$$

The function

$$
K(\eta):=\pi\sqrt{1-\eta^2}+2\eta
$$

is concave on `[0,1]`. Therefore its minimum on the closed Range-I interval occurs at
an endpoint. At `eta=0`,

$$
K(0)=\pi>3\lambda_A.
$$

At the other endpoint, where `w_0=F_0(eta)`, the value agrees with the Range-II lower
bound below and is strictly larger than `3lambda_A` because that crossing occurs
strictly below `lambda_A`.

Thus `J>lambda_A` throughout Range I.

### Range II: `F_0(eta)>=w_0`

Now (2.5) gives `lambda>=F_0(eta)`, so

$$
3J\ge F_0(\eta)+2\eta.
\tag{3.5}
$$

The function

$$
H(\eta):=F_0(\eta)+2\eta
$$

is also concave on `[0,1]`, being a positive multiple of
`sqrt(1-eta^2)` plus a linear term. Hence its minimum on the Range-II interval
intersected with `[0,lambda_A]` occurs at an endpoint.

At the lower endpoint it equals the Range-I value and is strictly larger than
`3lambda_A`. At the upper endpoint `eta=lambda_A`, equation (2.8) gives

$$
H(\lambda_A)
=F_0(\lambda_A)+2\lambda_A
=3\lambda_A.
\tag{3.6}
$$

Therefore

$$
J\ge\lambda_A,
$$
with equality possible only when

$$
\boxed{
\eta=\lambda=\lambda_A,
\qquad
\nu=0.
}
\tag{3.7}
$$

Thus the formal minimum of the retained quantity occurs at **zero selected loaded
contact-degree slack** and exactly at the old AX endpoint.

---

## 4. Endpoint exclusion gives a uniform retained gap

Suppose there were an unbounded sequence with

$$
{L_*-(2/3)s_{B,*}\over D}	o\lambda_A.
\tag{4.1}
$$

The equality analysis in Section 3 forces

$$
{s_{B,*}\over D}\to0,
\qquad
{L_*\over D}\to\lambda_A.
\tag{4.2}
$$

But MX transplants AX's endpoint exclusion to the selected graph: no selected maximal
cyclic circuit sequence can satisfy `L_*/D->lambda_A`.

Therefore (4.1) is impossible. The standard compactness contradiction now gives an
absolute `epsilon_B>0` and large-`D` threshold such that BS.2 holds.

This proof does not need a numerical value of `epsilon_B`.

---

## 5. Exact full/selected comparison without `kappa`

Let

$$
g:=q-q_*\ge0,
\qquad
B_0:=e_{BB}-e_{BB,*}\ge0,
\qquad
M_0:=e_{BI}-e_{BI,*}\ge0.
\tag{5.1}
$$

LI gives

$$
I_*=V_*\cap I,
\qquad I:=V\setminus B.
\tag{5.2}
$$

Let `c_I,c_{I,*}` be the full and selected interior-component counts.

A full interior component that meets `I_*` contains at least one selected interior
component. Hence the only way `c_I` can exceed `c_{I,*}` is through full interior
components disjoint from `I_*`.

Let `r_0` be the number of such omitted-only full components. Each one has at least
three full contact edges to the loaded set `B` by the canonical C36/C40 attachment
theorem. Every one of those attachment edges is absent from the selected contact
support, because its interior endpoint is not in `V_*`. Therefore

$$
3r_0\le M_0.
\tag{5.3}
$$

Since

$$
c_I-c_{I,*}\le r_0,
$$

we obtain

$$
\boxed{2(c_I-c_{I,*})\le\frac23M_0.}
\tag{5.4}
$$

Now subtract the full and selected ZU ledgers. Full ZU is

$$
c_I+e_{BB}+s_C=q-2+d_H+s_Z,
\tag{5.5}
$$

while selected cyclic ZU is

$$
c_{I,*}+e_{BB,*}+s_{C,*}=q_*-2.
\tag{5.6}
$$

A direct rearrangement gives

$$
\boxed{
L_*-L
=B_0-2g+2(c_I-c_{I,*})-2d_H-2s_Z.
}
\tag{5.7}
$$

Use (5.4):

$$
L_*-L
\le
B_0+\frac23M_0-2g-2d_H-2s_Z.
\tag{5.8}
$$

The full and selected loaded contact-degree slacks are

$$
s_B=3q-e_{BI}-2e_{BB}\ge0,
\tag{5.9}
$$

$$
s_{B,*}=3q_*-e_{BI,*}-2e_{BB,*}\ge0.
\tag{5.10}
$$

Subtracting gives

$$
\boxed{M_0+2B_0=3g+s_{B,*}-s_B.}
\tag{5.11}
$$

Since

$$
B_0+\frac23M_0
\le\frac23(M_0+2B_0),
$$

and `s_B>=0`,

$$
B_0+\frac23M_0
\le2g+\frac23s_{B,*}.
\tag{5.12}
$$

Insert into (5.8). The `2g` cancels exactly:

$$
L_*-L
\le
\frac23s_{B,*}-2d_H-2s_Z.
$$

Therefore

$$
\boxed{
L
\ge
L_*-\frac23s_{B,*}+2d_H+2s_Z,
}
$$

which is BS.4.

This is strictly stronger than MX.8. It is independent of the number of omitted
interior vertices and of the circuit rank gap `kappa_*`.

---

## 6. Full-source consequence

Combine BS.2 and BS.4:

$$
{L\over D}
\ge
\lambda_A+\epsilon_B
+2{d_H+s_Z\over D}-o(1).
$$

This proves BS.5--BS.6.

Thus a maximal cyclic extreme circuit cannot be hidden inside a much larger full C65
support to evade the cyclic surplus theorem. Any omitted full interior complexity is
paid through three-edge loaded attachments; exact boundary-degree accounting cancels
that cost.

The only unresolved issue in this branch is what to do with the resulting very high
full pinned/contact surplus. There is no proved universal upper bound below one.

---

## 7. Regressions and scope

- The proof does **not** assume `kappa_*=o(D)` or `v-v_*=o(D)`.
- Omitted-only full interior components may be arbitrarily large; only their three
  mandatory loaded attachments are used.
- Selected contact-degree slack may be linear. Section 3 retains it and proves that
  exactly the combination `L_*-(2/3)s_{B,*}` still has the `lambda_A` floor.
- ESR even shells are not in the hypothesis because their extreme circuits have
  `sigma_*>0`.
- A selected maximal **forest** circuit (`d_*>0`) is not covered; this is now the
  highest-value maximal-circuit branch left after QP/GS.

---

## 8. Exact next target

There are now only two ways a maximal (`sigma=0`) extreme can avoid the cyclic
high-surplus conclusion:

1. its selected diameter thrackle is a caterpillar forest (`d_*>0`);
2. no maximal extreme exists, so every KKT-polytope vertex is an underbraced singular
   circuit (`sigma_*>0`), the QP/GS branch.

The next theorem should attack the selected maximal forest case. A direct selected SZ
identity already gives

$$
{e_{BB,*}+2s_{C,*}\over D}
\ge
\lambda_R+\epsilon_0+3{d_*\over D}
$$

once the selected support-local version is rebuilt; ENB/EDB additionally force
`h_*` and branching unless `d_*` itself is large. Combining the `3d_*` penalty with
Woodall's caterpillar geometry may produce a stronger forest-specific threshold or a
finite exclusion.

---

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

For a maximal cyclic extreme, retain selected loaded contact slack
    s_B*=3q_*-e_BI,* -2e_BB,*.
Selected ZK gives attachment radius
    sum delta_r <=6+L_*-s_B*,
    L_*=e_BB,*+2s_C,*.
Put lambda=L_*/D, nu=s_B*/D, eta=lambda-nu.
Disk force-hull area and exceptional-face squaring give
    w >= pi sqrt(1-eta^2).
Atomic train incidence gives
    lambda >= F(w)
and lambda>=w. At w0=pi sqrt(1-eta^2),
    F(w0)=(4/5)[pi sqrt(1-eta^2)+sqrt(Delta) eta].
The retained transfer quantity is
    J=lambda-(2/3)nu=(lambda+2eta)/3.
Piecewise concavity plus the defining equation for lambda_A proves
    J>=lambda_A,
with equality only at eta=lambda=lambda_A, nu=0. AX excludes that endpoint, so
    (L_*-(2/3)s_B*)/D >=lambda_A+epsilon_B.

For the full graph, let B0=e_BB-e_BB,* and M0=e_BI-e_BI,*.
Every full interior component absent from selected I_* uses >=3 omitted B-I contacts,
so
    2(c_I-c_I*) <= (2/3)M0.
Loaded degree slacks give
    M0+2B0=3(q-q*)+s_B*-s_B.
Subtract full/selected ZU:
    L_*-L=B0-2(q-q*)+2(c_I-c_I*)-2d_H-2s_Z.
Therefore exactly
    L >= L_*-(2/3)s_B*+2d_H+2s_Z.
Hence ANY maximal cyclic extreme, regardless kappa, forces
    liminf L/D >=lambda_A+epsilon_B>0.9955405845...
plus the positive 2(d_H+s_Z)/D correction.

Next: selected maximal forest circuits, or the all-underbraced QP/GS singular branch.
```
