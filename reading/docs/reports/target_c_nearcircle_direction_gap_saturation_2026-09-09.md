> Generated reading edition · [exact source](../../../docs/reports/target_c_nearcircle_direction_gap_saturation_2026-09-09.md) · source SHA-256 `dee621bc46da8157176857e92e7088cd2558b80d064a305478e3cfa47fa4b960`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 1 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-6EE51866BCA9","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_nearcircle_direction_gap_saturation_2026-09-09.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=1e62375a3084784125c4877160746ba9a1a743f0; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — diameter-direction gap saturation in the near-circle endpoint

**Date:** 2026-09-09  
**Repository base:** PR #119 after DG/DC  
**Run type:** exact asymptotic stability extraction  
**Target:** post-ZF `x_B=o(D)` endpoint  
**Depends on:** DG.1-DG.6, DC.4  
**External web search:** not used  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

DG proves that consecutive actual diameter directions pay one angular quantum

```math
2a_D,
\qquad a_D=\arcsin\frac1{2D},
```

when their edges share an endpoint, and at least two quanta `4a_D` when they are vertex-disjoint. It also proves that at least

```math
d_H=q-h
```

cyclic consecutive pairs are disjoint.

DC then collapses `x_B=o(D)` to

```math
q/D\to\pi
```

and a near-circular force hull.

These facts force equality not only in the aggregate perimeter bound but in the complete cyclic gap budget. The number of disjoint neighbor pairs is asymptotically minimal, and almost every individual direction gap is asymptotically at its appropriate lower bound. Consequently almost every consecutive pair of diameter edges produces a source endpoint pair at distance `1+o(1)`.

This gives an explicit near-contact scaffold on the loaded boundary that any final stability theorem can exploit.

---

## 1. Exact gap-defect identity

Order the `h` actual diameter edges cyclically by projective direction. Let

```math
g_1,\ldots,g_h>0,
\qquad
\sum_i g_i=\pi.
\tag{1.1}
```

Let `I_dis` be the set of indices for which the two neighboring diameter edges are vertex-disjoint, and put

```math
m:=|I_{dis}|.
\tag{1.2}
```

DG proves

```math
m\ge d_H=q-h.
\tag{1.3}
```

Define the lower quantum for gap `i` by

```math
L_i:=
\begin{cases}
4a_D,& i\in I_{dis},\\
2a_D,& i\notin I_{dis}.
\end{cases}
\tag{1.4}
```

C67 and DG.1 give

```math
g_i\ge L_i.
\tag{1.5}
```

Therefore the total nonnegative angular excess is exactly

```math
\boxed{
E_{ang}
:=\sum_i(g_i-L_i)
=\pi-2a_D(h+m).
}
\tag{1.6}
```

Since `m>=q-h`,

```math
0\le E_{ang}
\le\pi-2a_Dq.
\tag{1.7}
```

At the same time the excess number of disjoint neighbor pairs satisfies

```math
2a_D[m-(q-h)]
\le\pi-2a_Dq.
\tag{1.8}
```

Both inequalities are finite.

---

## 2. The DG endpoint exhausts the full angular budget

Assume now

```math
x_B=o(D).
```

DG.6 gives

```math
q/D\to\pi.
\tag{2.1}
```

Also

```math
2Da_D\to1.
\tag{2.2}
```

Hence

```math
2a_Dq\to\pi.
\tag{2.3}
```

Equations (1.7)-(1.8) immediately give:

### Theorem DS.1 — global gap saturation

```math
\boxed{E_{ang}=o(1),}
\tag{DS.1}
```

and

```math
\boxed{m-(q-h)=o(D).}
\tag{DS.2}
```

Thus the cyclic direction order has only `o(D)` more disjoint adjacencies than the absolute graph-theoretic minimum supplied by the `d_H` tree-component deficit.

---

## 3. Almost every individual gap is minimally spaced

For fixed `epsilon>0`, let

```math
N_\epsilon(D)
:=\#\{i:g_i-L_i\ge\epsilon/D\}.
```

Then

```math
N_\epsilon(D)\frac\epsilon D
\le E_{ang}=o(1),
```

so

```math
\boxed{N_\epsilon(D)=o(D).}
\tag{3.1}
```

Equivalently, for every fixed `epsilon>0`, all but `o(D)` cyclic neighbor pairs obey

```math
g_i< L_i+\epsilon/D.
\tag{3.2}
```

In the usual diagonal-subsequence formulation:

### Theorem DS.2 — local gap saturation

All but `o(D)` consecutive diameter-direction pairs satisfy

```math
\boxed{
 g_i=2a_D+o(D^{-1})
}
```

when they share an endpoint, and

```math
\boxed{
 g_i=4a_D+o(D^{-1})
}
```

when they are vertex-disjoint.

Here the `o(D^{-1})` statement means that for every fixed `epsilon>0`, the number of violations of the corresponding `epsilon/D` bound is `o(D)`.

---

## 4. Shared consecutive pairs create near-unit partner distances

Suppose two consecutive diameter edges share a terminal `z`:

```math
za,
\qquad
zb,
\qquad
|z-a|=|z-b|=D.
```

If their projective direction gap is `g`, then

```math
|a-b|=2D\sin\frac g2.
\tag{4.1}
```

The lower bound `g>=2a_D` is exactly the statement `|a-b|>=1`, because

```math
2D\sin a_D=1.
```

For a saturated shared gap

```math
g=2a_D+o(D^{-1}),
```

we have

```math
|a-b|
=2D\sin(a_D+o(D^{-1}))
=1+o(1).
```

Thus:

### Corollary DS.3

For all but `o(D)` saturated shared cyclic neighbor pairs, the two nonshared diameter endpoints satisfy

```math
\boxed{|a-b|=1+o(1).}
\tag{4.2}
```

---

## 5. Disjoint consecutive pairs create a near-unit cross pair

DG.1 proved more than the angular lower bound. For vertex-disjoint diameter edges at projective angle `g`, its midpoint calculation gives

```math
\boxed{
\min\{|A-B|,|C-D|\}
\le2D\sin\frac g4
}
\tag{5.1}
```

after the endpoint orientation used in DG.1.

Unit separation gives the reverse lower bound `>=1` for every distinct endpoint pair.

For a saturated disjoint gap

```math
g=4a_D+o(D^{-1}),
```

we obtain

```math
2D\sin\frac g4
=2D\sin(a_D+o(D^{-1}))
=1+o(1).
```

Hence:

### Corollary DS.4

For all but `o(D)` saturated disjoint cyclic neighbor pairs, at least one cross-endpoint pair satisfies

```math
\boxed{|p-r|=1+o(1).}
\tag{5.2}
```

The pair need not be an actual unit contact. This report does not make the invalid inference `1+o(1) -> 1`.

---

## 6. Simultaneous loaded-boundary saturation

DC.5 independently proves in the same endpoint

```math
e_{BB}\ge q-x_B
=\pi D-o(D).
```

Thus all but `o(D)` loaded hull intervals are exact unit contact sides, while DS.2-DS.4 show all but `o(D)` consecutive diameter-direction pairs produce an endpoint pair at distance `1+o(1)`.

The source therefore has two simultaneous boundary-scale structures:

1. an almost complete exact unit-contact cycle around a near-circular force hull;
2. an almost minimally spaced diameter-direction scaffold whose neighboring chords nearly create additional unit contacts.

This is substantially more rigid than the aggregate statements `per(F)~pi D` and `Q+2s_Z=Omega(D)`.

---

## 7. Regression and limitation

A large regular odd unit polygon exhibits the same qualitative limiting geometry: near-circular hull, unit boundary cycle, and cyclic diameter chords whose local gaps nearly saturate the unit-separation threshold. It remains a valid local regression family.

Therefore DS is not itself a Level I contradiction. The missing ingredient is still global packing optimality / interior capacity. A final theorem must show that an asymptotically Oler-saturated global packing cannot support this near-equality boundary scaffold while remaining triangle-free.

---

## 8. Next target

The most concrete next stability statement is now:

> **near-contact promotion or penalty theorem.** In the DC near-circle/Oler-saturated endpoint, the `Theta(D)` near-unit endpoint pairs supplied by DS must either create an actual unit triangle/contact pattern forbidden by triangle-freeness, or force a positive boundary-order loss in packing capacity.

Any proof must remain exact; mere convergence of distances to one is insufficient.

---

## 9. Compact handoff

```text
LEVEL I STATUS: STILL OPEN

Let m be the number of vertex-disjoint cyclic neighbor pairs among the h diameter
directions. DG gives m>=d_H=q-h. With lower gaps
    L_i=2a_D (shared), 4a_D (disjoint),
we have exactly
    E_ang=sum(g_i-L_i)=pi-2a_D(h+m)>=0.
Hence
    E_ang<=pi-2a_D q,
    2a_D[m-(q-h)]<=pi-2a_D q.

In the x_B=o(D) endpoint, q/D->pi and 2Da_D->1, so
    E_ang=o(1),
    m-(q-h)=o(D).
For every fixed epsilon>0, only o(D) gaps exceed their lower bound by epsilon/D.

Thus all but o(D) consecutive diameter pairs are asymptotically minimally spaced.
Shared pairs have opposite endpoints at distance 1+o(1); disjoint pairs have at least
one cross-endpoint pair at distance 1+o(1).

Together with DC:
    e_BB=pi D-o(D) or larger,
so the near-circle endpoint has both an almost complete exact unit-contact hull cycle
and an almost-minimal diameter near-contact scaffold.
```
