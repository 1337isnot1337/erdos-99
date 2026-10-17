> Generated reading edition · [exact source](../../../docs/reports/target_c_psd_response_cut_domination_2026-08-31.md) · source SHA-256 `9048a57637100198d56435907d35be755ff21ef12d8e477a3f5da354841f8bff`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-11871450C027","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C: PSD response cut domination and linear strict-terminal set

**Date:** 2026-08-31  
**Repository base:** `5c2e17f9` (main after Gate C-I closure / PR #65)  
**Run type:** exact Schur-PSD / response-support counting theorem  
**Target:** Target C Gate C-II  
**Depends on:** C26 full force visibility, C35-C36 terminal/component structure, C41 response decomposition, C43 anti-Reuleaux gap, C53 universal selected-stress PSD, C30 force-visible boundary count

## LEVEL I STATUS

**STILL OPEN.**

Gate C-I is closed. In Gate C-II choose a relative-interior normalized KKT stress, so every unit contact and every strong diameter edge has positive coefficient. Let `B=B_+` be the loaded force-hull boundary, `Lambda` the positive-contact Dirichlet response on `B`, and `L_H` the positive-diameter Laplacian.

The later universal PSD theorem C53 upgrades the older C41 response picture to

$$
\boxed{M:=\Lambda-L_H\succeq0.}
$$

This has two exact consequences.

First, the response conductance dominates the diameter stress across **every** boundary cut. In particular each loaded terminal has response degree at least its total positive diameter weight.

Second, equality at one terminal is rigid: a zero diagonal entry of a PSD matrix forces the entire row to vanish. Combining that row rigidity with C41's strict response cliques, C36's attachment size at least three, the absence of a diameter triangle, and the terminal contact-degree cap three gives a global count:

$$
\boxed{|T|\ge \frac{2}{5}|B|,}
$$

where `T` is the set of loaded terminals with **strict** local response-degree excess. Since C30 gives `2|B|>=ceil(D)+2`,

$$
\boxed{|T|\ge \frac{\lceil D\rceil+2}{5}.}
$$

Thus C41's strict defect cannot be confined to finitely many exceptional terminals. It occurs at linearly many force-hull vertices. No quantitative lower bound on the individual excesses is claimed.

## 1. Setup

Work with a sufficiently large contact-minimal triangle-free global minimizer after Gate C-I, so

$$
C=C_*.
$$

Choose a relative-interior normalized KKT stress. Then

- every contact conductance `alpha_e` is positive;
- every positive diameter weight `beta_h` is positive on the maximal strong diameter support;
- the positive contact graph is the entire nonisolated contact core and is connected;
- `B=B_+` is exactly the set of nonisolated diameter endpoints and the convex-hull vertex set of the contact core.

Write

$$
c_{bk}:=-\Lambda_{bk}\ge0\qquad(b\ne k),
$$

and extend the diameter weights by

$$
\beta_{bk}=0\qquad(bk\notin H_+).
$$

Define local response and diameter degrees

$$
d_b:=\sum_{k\ne b}c_{bk},
\qquad
s_b:=\sum_{k\ne b}\beta_{bk}>0.
$$

Since both `Lambda` and `L_H` are Laplacians,

$$
M_{bb}=d_b-s_b,
\qquad
M_{bk}=-(c_{bk}-\beta_{bk})\quad(b\ne k).
\tag{C64.1}
$$

## 2. C53 descends through the contact Schur complement

Order the full selected stress matrix by boundary `B` and contact-interior vertices `I`:

$$
\Omega
=L_C(\alpha)-L_H(\beta).
$$

C53-C54 give

$$
\Omega\succeq0.
\tag{C64.2}
$$

The positive contact Dirichlet block `L_{II}` is positive definite. The usual block Gaussian congruence for Kron reduction gives

$$
\Omega
\sim
\begin{pmatrix}
\Lambda-L_H&0\\
0&L_{II}
\end{pmatrix}.
\tag{C64.3}
$$

Therefore

$$
\boxed{M=\Lambda-L_H\succeq0.}
\tag{C64.4}
$$

The affine response identity still gives

$$
M\mathbf1=0,
\qquad
MP_B=0.
\tag{C64.5}
$$

C41 gives the independent strict trace statement

$$
\operatorname{tr}M>0.
\tag{C64.6}
$$

So `M` is a nonzero PSD equilibrium stress on the convex loaded boundary.

## 3. Every boundary cut is response-dominated

For `S subset B`, let `1_S` be its indicator. The Laplacian energy identity gives

$$
\mathbf1_S^{\mathsf T}M\mathbf1_S
=
\sum_{b\in S,\ k\notin S}
(c_{bk}-\beta_{bk}).
$$

Since `M>=0`,

### Theorem C64.1 (response cut domination)

For every boundary subset `S`,

$$
\boxed{
\sum_{b\in S,\ k\notin S}c_{bk}
\ge
\sum_{b\in S,\ k\notin S}\beta_{bk}.
}
\tag{C64.7}
$$

In particular, taking `S={b}`,

$$
\boxed{d_b\ge s_b\qquad(b\in B).}
\tag{C64.8}
$$

Moreover C41.6 implies

$$
\sum_{b\in B}(d_b-s_b)=\operatorname{tr}M>0,
\tag{C64.9}
$$

so at least one terminal has strict excess.

## 4. Zero local excess annihilates the whole defect row

Define

$$
Z:=\{b\in B:d_b=s_b\},
\qquad
T:=B\setminus Z.
\tag{C64.10}
$$

For a PSD matrix, every `2x2` principal minor is nonnegative:

$$
|M_{bk}|^2\le M_{bb}M_{kk}.
$$

Hence if `b in Z`, then `M_bb=0` and

$$
M_{bk}=0\qquad\text{for every }k.
$$

By C64.1,

### Lemma C64.2 (zero-excess row rigidity)

If `b in Z`, then

$$
\boxed{c_{bk}=\beta_{bk}\qquad\text{for every }k\ne b.}
\tag{C64.11}
$$

Consequently the response support seen from `b` is **exactly** its positive-diameter neighbor set.

Two immediate structural consequences follow.

1. `b` has no direct loaded-loaded unit contact. Such a contact would contribute `c_{bk}>=alpha_{bk}>0`, while `beta_{bk}=0` because `D>1`.
2. If an unpinned harmonic component `I_r` has `b` in its attachment set `A_r`, then every other `k in A_r` satisfies `bk in H_+`. Indeed C41.1 gives the strict component response `c^{(r)}_{bk}>0`, hence total `c_{bk}>0`, and C64.11 then forces `beta_{bk}>0`.

Thus every harmonic component touching a zero-excess terminal attaches all of its other boundary pins at diameter distance from that terminal.

## 5. One harmonic component contains at most one zero-excess terminal

C36 gives

$$
|A_r|\ge3
\tag{C64.12}
$$

for every unpinned component.

Suppose distinct `b,k in Z` both belonged to `A_r`. Choose

$$
l\in A_r\setminus\{b,k\}.
$$

By zero-row rigidity at `b`, strict clique response from `I_r` gives

$$
bk,bl\in H_+.
$$

By zero-row rigidity at `k`, it also gives

$$
kl\in H_+.
$$

Therefore `b,k,l` are three source points with all three pair distances equal to `D`. This is excluded for all sufficiently large global minimizers by C15, and a fortiori by the uniform C43 theorem.

### Lemma C64.3

Every unpinned harmonic component attachment set contains at most one zero-excess terminal:

$$
\boxed{|A_r\cap Z|\le1.}
\tag{C64.13}
$$

## 6. Double counting forces linearly many strict terminals

Fix `b in Z`. By Lemma C64.2 it has no direct loaded-loaded contact. The full positive contact graph is connected, so `b` is incident to at least one contact edge into some unpinned component `I_r`. Choose one such component and assign `b` to it.

By C64.13 different zero-excess terminals are assigned to different components.

For the component assigned to `b`, C36 gives at least three distinct attachments. One is `b`; every other attachment is in `T`, because `b` is the unique zero-excess attachment of that component. Hence each assigned zero terminal consumes at least **two distinct strict-terminal/component attachment incidences**.

On the other hand, a strict terminal `t in T` belongs to at most three distinct attachment sets. Each membership `t in A_r` requires at least one distinct contact edge from `t` into `I_r`, and C35 gives

$$
\deg_C(t)\le3.
\tag{C64.14}
$$

Therefore

$$
2|Z|\le3|T|.
\tag{C64.15}
$$

Since `|B|=|Z|+|T|`,

### Theorem C64.4 (linear strict-terminal set)

$$
\boxed{|T|\ge\frac25|B|.}
\tag{C64.16}
$$

C30 gives

$$
2|B|\ge\lceil D\rceil+2.
$$

Hence

$$
\boxed{
|T|
\ge
\frac{\lceil D\rceil+2}{5}.
}
\tag{C64.17}
$$

Thus every sufficiently large C-II survivor has `Omega(D)` loaded force-hull terminals with

$$
\boxed{d_b>s_b.}
\tag{C64.18}
$$

## 7. Stronger support interpretation

At every `b in T`, positive excess means the defect stress has

$$
M_{bb}>0.
$$

Equivalently, at least one of the following happens:

- response conductance from `b` reaches a non-diameter terminal;
- response conductance to diameter neighbors exceeds their total diameter weight after cancellations across several neighbors.

At every `b in Z`, neither is possible: the response row is exactly the diameter row.

This partitions the boundary into a linearly large set of terminals where the positive contact network performs genuinely more electrical coupling than the diameter stress, and a rigid equality set whose contact attachments are constrained to diameter stars.

## 8. Relation to the near-star regression

C64 does not yet give a numerical trace gap. A sequence can have

$$
d_b-s_b\downarrow0
$$

at every one of the `Omega(D)` strict terminals. Thus the theorem does not contradict the near-star response regression by itself.

It does, however, eliminate the weakest version of that regression in which all non-additivity is localized at `O(1)` exceptional terminals. Any mechanical near-star approximation compatible with a C-II KKT framework must distribute positive local response excess over a linear set of boundary vertices.

This is the correct next quantitative target:

> convert the `Omega(D)` strict excess locations into a lower bound on the aggregate excess using unit-contact mechanics, C43's uniform short-pair geometry, or C40's attachment-diameter budget.

## 9. Regression audit

- **Unit square:** all four terminals have positive defect diagonal, so C64.16 holds.
- **No interior vertices:** every loaded-loaded unit contact creates positive non-diameter response and hence its endpoints lie in `T`; zero terminals cannot occur.
- **Many tiny effective conductances:** allowed; only strict positivity is counted.
- **Positive diameter star:** allowed. A zero-excess center can have many diameter neighbors, but each harmonic component touching it has all other attachments among those neighbors and contains no second zero terminal.
- **Contact-isolated source points:** outside the positive contact core and irrelevant to the theorem.

## 10. Compact handoff

**LEVEL I STATUS:** still open.

**C64.1:** C53 plus Schur reduction gives `Lambda-L_H>=0`, hence response conductance dominates positive diameter weight across every boundary cut.

**C64.2:** if a terminal has zero local degree excess, its entire PSD defect row vanishes, so its response row equals its diameter row exactly.

**C64.3:** every harmonic component contains at most one such zero terminal; otherwise its strict response clique creates a diameter triangle.

**C64.4:** each zero terminal must attach to a component with at least two strict terminals, while a strict terminal belongs to at most three components. Therefore `2|Z|<=3|T|`, so `|T|>=2|B|/5 >= (ceil D+2)/5`.

**Next:** obtain aggregate quantitative mass from these linearly many strict response terminals.
