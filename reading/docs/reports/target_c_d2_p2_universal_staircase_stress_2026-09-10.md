> Generated reading edition · [exact source](../../../docs/reports/target_c_d2_p2_universal_staircase_stress_2026-09-10.md) · source SHA-256 `b680719f151ef630de5f1acea8347aecf3f6cb1eae6e760184bbd8abe3fe9c90`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 1 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-CBDE7F9F9BEA","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdos Problem #99 — D2/P2 has a universal word-independent positive KKT stress

**Date:** 2026-09-10  
**Repository branch:** `research/target-c-d2-transversality-2026-09-10`  
**Run type:** exact statics solution / route elimination  
**Target:** cyclic primitive `d_H=2`, P2 endpoint  
**Depends on:** D2S/D2R/SW staircase geometry from PR #118; P2E on this branch  
**Computation:** numerical staircase solves suggested the formula; computation is not used in the proof

## LEVEL I STATUS

`STILL OPEN`

P2E proves that the four A/B transition contacts have equal positive KKT coefficient. Scale the unique stress so that all four transition coefficients equal one.

The remaining stress can then be solved **exactly**, for every staircase word at once.

Put

```math
\tau_D:=\sqrt{1-\frac1{4D^2}},
\qquad
\sigma_D:=\sqrt{1-\frac1{D^2}},
\qquad
\boxed{c_D:=\frac{\sigma_D}{\tau_D}}.
\tag{US.1}
```

Then `0<c_D<1`.

### Theorem US — universal P2 staircase stress

For every P2 survivor with both staircase bodies nontrivial, the unique positive KKT stress, under the normalization `alpha=1` on the four transition contacts, is:

1. every shell contact internal to one of the four blocks has
   
   ```math
   \boxed{\alpha=c_D;}
   \tag{US.2}
   ```

2. in either diameter-direction block, every interior diameter state has
   
   ```math
   \boxed{\beta_{\rm int}=\frac{c_D}{D^2};}
   \tag{US.3}
   ```

3. each extreme diameter state adjacent to a cross-tree switch has
   
   ```math
   \boxed{\beta_{\rm end}=\frac{1+c_D/2}{D^2}.}
   \tag{US.4}
   ```


If one tree is the one-edge `K_2` component, its single diameter state is both extremes and has

```math
\boxed{\beta_{K_2}=\frac2{D^2}.}
\tag{US.5}
```

All coefficients are strictly positive.

The formulas depend only on `D`, not on either staircase word, its star runs, or its center-switch pattern.

Consequently, in every P2 survivor the weighted contact cycle has the universal resistance pattern

```math
\boxed{
r_e=1\quad\text{on the four transition sides},
\qquad
r_e=r_D:=\frac1{c_D}=\frac{\tau_D}{\sigma_D}
\quad\text{on every other shell side}.}
\tag{US.6}
```

Thus WT transfer in P2 depends only on the four block lengths and the endpoints of the selected diameter chords. A statics/sign argument internal to the two `D,D,1` staircase bodies cannot distinguish the words.

---

## 1. Arithmetic direction progression inside one staircase

Take one SW staircase body. Orient all of its diameter edges from its first color class `U` to its second `V` and write

```math
z_t=D e^{i(\theta+t\delta)},
\qquad
0\le t\le L,
```

where

```math
\delta=2\arcsin\frac1{2D}.
```

Put

```math
d_t:=z_{t+1}-z_t.
```

D2S gives

```math
|d_t|=1,
```

and SW says a `U` step creates the contact vector `-d_t`, while a `V` step creates `+d_t`.

The diameter progression satisfies

```math
z_{t+1}+z_{t-1}=2\cos\delta\,z_t.
```

Since

```math
2\cos\delta=2-\frac1{D^2},
```

we obtain the exact second-difference identity

```math
\boxed{
d_t-d_{t-1}=-\frac1{D^2}z_t.}
\tag{1.1}
```

Summing from `a` to `b` gives

```math
\boxed{
d_b-d_{a-1}
=-\frac1{D^2}\sum_{t=a}^bz_t.}
\tag{1.2}
```

This telescoping identity is the reason the stress is independent of the staircase word.

---

## 2. One P2 switch gives the endpoint reaction vector

Rotate so the first diameter state is

```math
z_0=(D,0).
```

At a P2 switch, the neighboring diameter direction from the other tree is at angle

```math
-\Delta_2,
\qquad
\Delta_2=2\arcsin(1/D).
```

The common-midpoint P-cell transition vector acting from the other body toward the `U` endpoint is, up to the cut orientation,

```math
p_-:=\frac{z_0-D(\cos\Delta_2,-\sin\Delta_2)}2.
```

Using

```math
\cos\Delta_2=1-\frac2{D^2},
\qquad
\sin\Delta_2=\frac2D\sigma_D,
```

we get

```math
\boxed{p_-=(1/D,\sigma_D).}
\tag{2.1}
```

The first internal unit side vector is

```math
d_0=z_1-z_0
=\left(-\frac1{2D},\tau_D\right).
\tag{2.2}
```

With

```math
c_D=\frac{\sigma_D}{\tau_D},
\qquad
b_E:=\frac{1+c_D/2}{D^2},
```

(2.1)-(2.2) give the exact endpoint identity

```math
\boxed{p_-=b_Ez_0+c_Dd_0.}
\tag{2.3}
```

At the right end of the staircase, after rotating by the final direction, the neighboring other-tree diameter lies `+Delta_2` away. The symmetric identity is

```math
\boxed{p_+=b_Ez_L-c_Dd_{L-1}.}
\tag{2.4}
```

These are exactly the two P2 boundary reaction pairs when the transition contact coefficient is one.

---

## 3. Internal run equilibrium

A vertex of one staircase color persists through a contiguous interval of diameter states

```math
[a,b].
```

This is immediate from the monotone SW word: the relevant color coordinate stays fixed until the next step of that color.

First assume

```math
0<a\le b<L.
```

The vertex has two same-color contact neighbors, corresponding to `d_(a-1)` and `d_b`. Give both contacts coefficient `c_D`. Give every incident diameter state coefficient

```math
b_I:=\frac{c_D}{D^2}.
```

For a `U` vertex, the signed equilibrium sum is

```math
b_I\sum_{t=a}^bz_t
+c_D(d_b-d_{a-1}).
```

By (1.2) this is exactly zero.

For a `V` vertex every vector sign reverses, so the same scalar identity proves equilibrium.

Thus every fully internal staircase run balances with the universal coefficients US.2-US.3, regardless of run length.

---

## 4. Runs touching one or both staircase ends

At the left endpoint, the run receives the P2 transition force `-p_-` on the `U` side and `+p_-` on the `V` side.

For the one-state left run, (2.3) is exactly

```math
b_Ez_0+c_Dd_0-p_-=0.
\tag{4.1}
```

Extending the run by one additional internal state changes the left side by

```math
b_Iz_t+c_D(d_t-d_{t-1})=0
```

from (1.1). Therefore (4.1) remains true for a left run of arbitrary length, until the final state is reached.

The right endpoint is identical using (2.4).

If one color coordinate never changes at all, its single vertex spans the entire interval `[0,L]`. The two endpoint identities plus the telescoping internal identities give

```math
b_E(z_0+z_L)
+b_I\sum_{t=1}^{L-1}z_t
-p_--p_+=0,
```

again with the opposite signed equation on the other color.

Hence every vertex of the staircase body is in exact force equilibrium.

---

## 5. Assemble the two bodies

P2E gives one common coefficient on all four transition contacts. Scale it to one.

Apply Sections 1-4 independently to the two SW bodies. Each body equilibrates exactly under the forces exerted by those four transitions, with internal contact coefficient `c_D`, interior diameter coefficient `b_I`, and extreme diameter coefficient `b_E`.

Across each transition contact the two bodies receive equal and opposite forces, so their separate equilibria assemble into one global central-force KKT equilibrium.

All coefficients are positive because `D>1` gives

```math
0<\sigma_D<\tau_D,
\qquad
0<c_D<1.
```

The cyclic `d_H=2` phase has `s_Z=0`, so the normalized KKT stress is unique. Therefore the explicit positive stress just constructed is **the** P2 stress, up to common scale.

This proves US.2-US.4.

---

## 6. Singleton-tree case

If one diameter tree is a single edge, then `L=0`: the same two endpoints receive both P2 switch reaction pairs and there are no internal contact edges in that body.

In coordinates with the diameter vector `(D,0)`, the two switch vectors are

```math
p_-=(1/D,\sigma_D),
\qquad
p_+=(1/D,-\sigma_D).
```

Their sum is

```math
p_-+p_+=(2/D,0)=\frac2{D^2}z_0.
```

Therefore the single diameter coefficient is

```math
\beta=2/D^2,
```

which proves US.5.

It is also the value obtained by treating the state as both endpoint states in the telescoping formula:

```math
2b_E-b_I
=\frac2{D^2}.
```

---

## 7. Exact contact resistance pattern

Under the chosen transition normalization,

```math
\alpha_{trans}=1,
\qquad
\alpha_{internal}=c_D.
```

Therefore the cycle resistances `r=1/alpha` are

```math
r_{trans}=1,
\qquad
r_{internal}=\frac1{c_D}
=\frac{\tau_D}{\sigma_D}.
```

This proves US.6.

The deviation from uniformity is only second order:

```math
\frac1{c_D}
=1+\frac{3}{8D^2}+O(D^{-4}).
\tag{7.1}
```

But unlike an asymptotic statement, US.6 is exact for every finite P2 source.

---

## 8. Diameter coefficient pattern

For a tree with `L>=1`, its total unnormalized diameter weight is

```math
2b_E+(L-1)b_I
=\frac{2+Lc_D}{D^2}.
```

Since the two staircase lengths satisfy

```math
L_A+L_B=m=q-4,
```

the total unnormalized diameter weight is

```math
\boxed{
\sum_{h\in H}\beta_h
=\frac{4+mc_D}{D^2}.}
\tag{8.1}
```

The same formula holds when one tree is a singleton, by US.5.

Normalizing the KKT stress by `sum beta=1` therefore multiplies every displayed coefficient by

```math
\frac{D^2}{4+mc_D}.
```

No additional geometric condition is hidden in this normalization.

---

## 9. Route elimination and new WT target

The proposed next step after P2E was to use equal transition reactions to force one special staircase word or a contact/diameter sign failure.

US disproves that route completely.

Every admissible SW staircase word supports the same positive local coefficient pattern. Center switches and star runs do not alter any coefficient. Thus **internal body statics cannot distinguish the words**.

This is a binding regression theorem, not merely a numerical counterexample.

At the same time it creates a sharper route. WT transfer on the contact cycle now uses only two edge-resistance values:

```math
1,
\qquad
r_D=\tau_D/\sigma_D,
```

with the four unit resistances at the block transitions. Therefore every WT arc sum is an explicit affine function of the number of internal shell edges in that arc.

The remaining C56-G condition can be attacked combinatorially from the four block sizes and the staircase diameter endpoint incidences, with no unknown contact weights.

---

## Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| second-difference identity | proved | arithmetic direction progression |
| common internal contact coefficient `c_D` | proved | endpoint reaction plus telescoping |
| common interior diameter coefficient `c_D/D^2` | proved | internal run equilibrium |
| extreme coefficient `(1+c_D/2)/D^2` | proved | exact P2 switch vector |
| singleton-tree coefficient `2/D^2` | proved | sum of two switch reactions |
| word independence | proved | each vertex is only a contiguous state interval |
| all KKT signs positive | proved | explicit formulas |
| equal reactions force special staircase word | refuted | universal formula works for every word |
| Level I | still open | shell closure / WT-C56 compatibility remains |

---

## Compact handoff

```text
P2E lets us scale all four transition contact coefficients to 1.
Set
    tau=sqrt(1-1/(4D^2)), sigma=sqrt(1-1/D^2), c=sigma/tau.
For one staircase diameter progression z_t=D exp(i(theta+t delta)), d_t=z_(t+1)-z_t,
    d_t-d_(t-1)=-(1/D^2) z_t.
A monotone staircase vertex occupies a contiguous state interval [a,b].
Hence internal equilibrium telescopes if
    alpha_internal=c,
    beta_internal=c/D^2.
At a P2 switch the unit boundary reaction is p_-=(1/D,sigma), while
    d_0=(-1/(2D),tau),
so exactly
    p_-=((1+c/2)/D^2) z_0 + c d_0.
The right endpoint is symmetric. Therefore every extreme diameter state has
    beta_end=(1+c/2)/D^2.
If a tree is K2, its one diameter edge has beta=2/D^2.
These formulas balance every staircase word exactly.

Thus P2 contact resistances are universal:
    r_transition=1,
    r_internal=tau/sigma.
Internal statics cannot close P2. Next use WT/C56-G with these explicit arc sums.
```
