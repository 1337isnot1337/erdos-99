> Generated reading edition · [exact source](../../../docs/reports/target_c_slope_one_detour_density_gap_2026-09-09.md) · source SHA-256 `b2149110ab37d20742b0802cbbf918cfdda03d9de21f8d6d50fc5ecf81ae7404`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Presentation repairs: 2 exact-source-bound TeX/escape correction(s); [reviewed repair ledger](../../../docs/publication/reading-tex-repairs.json). Frozen source bytes are unchanged.

<!-- theorem-state: {"artifact_id":"ART-F6E1FED24B16","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — SOD: outer-pocket detour raises the slope-one diameter-density floor to 1.5336

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-nearzero-physical-carrier`  
**Run type:** quantitative outer-pocket/exceptional-face capacity exclusion  
**Target:** Target C C-II, RCC slope-one endpoint  
**Depends on:** SAC, OD, PI, JC, ZT/PC  
**New external literature:** none  
**Computation:** displayed decimal checks only; a wide safety margin is retained

## LEVEL I STATUS

**STILL OPEN.**

SAC proves that at RCC slope one all harmonic attachment polygons have total area `o(D^2)`. It then obtains the preliminary diameter-density window

```math
1.5038163673\ldots\le h/D\le1.6349643789\ldots .
```

This note uses the exact outer-pocket detour theorem OD to eliminate a substantial interval above the lower endpoint.

### Theorem SOD

Assume

```math
D\varepsilon\to0,
\qquad
\frac{e_{BB}+2s_C}{D}\to1.
```

Then

```math
\boxed{
\liminf_{D\to\infty}\frac hD\ge1.5336.
}
\tag{SOD.1}
```

Since S1E gives `q-h=o(D)`, the same lower bound holds for `q/D`.

Combining with SAC's upper bound,

```math
\boxed{
1.5336
\le\liminf h/D
\le\limsup h/D
\le1+\pi-\sqrt{2\pi}
=1.6349643789\ldots .
}
\tag{SOD.2}
```

SOC's visible-skeleton bounds improve correspondingly to

```math
\boxed{x_B\ge0.5336D+2s_C-o(D),}
\tag{SOD.3}
```

and

```math
\boxed{N_1\ge0.5336D+s_C-o(D),}
\tag{SOD.4}
```

where `N_1` is the number of singleton harmonic components.

---

## 1. Variables and the SAC cell-area collapse

Pass to a subsequence with

```math
y:=\lim h/D,
\qquad
p:=\lim P_F/D,
\qquad
P_F:=\operatorname{per}(F).
```

S1E gives

```math
q/D\to y.
\tag{1.1}
```

SAC gives

```math
\sum_r area(P_r)=o(D^2),
```

hence, for the C49 attachment gap,

```math
G=area(F)-o(D^2).
\tag{1.2}
```

PI gives for `y<pi/2`

```math
\boxed{
\liminf area(F)/D^2\ge A(y):=\frac12\sin y.
}
\tag{1.3}
```

The interval eliminated below lies entirely below `pi/2`.

---

## 2. JC feasibility forces a perimeter lower bound

The actual-perimeter JC capacity and SAC give

```math
A(y)
\le
\frac{(t+\min\{y,p-y\})^2}{4\pi},
\qquad
0\le t:=\lim e_{BB}/D\le1.
\tag{2.1}
```

The outer walk satisfies

```math
P_F\le b=2h-Q-2s_Z\le2h,
```

so

```math
p\le2y.
\tag{2.2}
```

Therefore

```math
\min\{y,p-y\}=p-y.
```

Replacing `t` by its maximum value one only weakens the necessary condition, giving

```math
A(y)
\le
\frac{(1+p-y)^2}{4\pi}.
```

All terms are nonnegative, so

```math
\boxed{
p\ge p_{req}(y):=y-1+\sqrt{2\pi\sin y}.}
\tag{SOD.5}
```

This is the key link between the generic JC capacity and the geometric detour theorem.

---

## 3. The same perimeter requirement bounds both detour and face defect

ZT gives

```math
b=2h-Q-2s_Z.
\tag{3.1}
```

Hence

```math
\frac{b-P_F}{D}
=2y-p-\frac QD-\frac{2s_Z}{D}+o(1)
\le2y-p+o(1).
```

Insert SOD.5:

```math
\boxed{
\limsup\frac{b-P_F}{D}
\le d(y),
}
\tag{SOD.6}
```

where

```math
\boxed{
d(y):=y+1-\sqrt{2\pi\sin y}.}
\tag{SOD.7}
```

The same identity, using only `b>=P_F`, gives

```math
Q+2s_Z
\le2h-P_F.
```

Therefore

```math
\boxed{
\limsup Q/D\le d(y).
}
\tag{SOD.8}
```

Thus JC feasibility near its lower density endpoint simultaneously makes

1. the outer contact walk nearly geodesic relative to the force hull; and
2. the total exceptional-face degree currency small.

Those are exactly the two quantities controlling the two cavity types.

---

## 4. OD bounds the outer-pocket area

OD proves the exact finite inequality

```math
H_{out}
\le
\frac{\pi}{4\sqrt2}
(x_B+a)^{3/2}
\sqrt{b-P_F}.
\tag{4.1}
```

Here `a` is the number of missing force-hull side contacts / OP pockets.

Trivially

```math
x_B\le q,
\qquad
a\le q,
```

so by (1.1)

```math
x_B+a\le(2y+o(1))D.
\tag{4.2}
```

Using SOD.6 in OD gives

```math
\boxed{
\limsup\frac{H_{out}}{D^2}
\le
\frac{\pi}{4\sqrt2}
(2y)^{3/2}\sqrt{d(y)}.
}
\tag{SOD.9}
```

This bound remembers that every OP pocket lies between a unit-contact chain and its straight force-hull chord. A large isoperimetric square alone misses this detour penalty.

---

## 5. The exceptional faces have only quadratic-in-d(y) capacity

JC's exceptional-face estimate gives

```math
A_{exc}
\le
\frac{Q^2+O(D)}{4\pi}.
\tag{5.1}
```

Therefore SOD.8 yields

```math
\boxed{
\limsup\frac{A_{exc}}{D^2}
\le
\frac{d(y)^2}{4\pi}.
}
\tag{SOD.10}
```

The C49/ZG charging theorem says

```math
G\le H_{out}+A_{exc}+2q.
\tag{5.2}
```

Since `q=O(D)`, equations (1.2), (1.3), SOD.9, and SOD.10 imply the new necessary scalar inequality

```math
\boxed{
\frac12\sin y
\le
\frac{\pi}{4\sqrt2}(2y)^{3/2}\sqrt{d(y)}
+
\frac{d(y)^2}{4\pi}.
}
\tag{SOD.11}
```

This inequality is special to the SCC slope-one geometry because SAC.2 was needed to remove the attachment-cell area.

---

## 6. Exclude the interval through 1.5336

SAC already gives

```math
y\ge1.5038163673\ldots>1.5038.
\tag{6.1}
```

On the interval

```math
1.5038\le y\le1.5336,
```

`sin y` is increasing, so

```math
\frac12\sin y
\ge
\frac12\sin(1.5038)
>0.49887.
\tag{6.2}
```

Also `d(y)` is increasing there. Indeed

```math
d'(y)
=1-
\frac{\pi\cos y}{\sqrt{2\pi\sin y}}.
```

Throughout the interval `cos y<0.071`, `sin y>0.99`, and `pi<3.142`, so the fraction is less than `0.1`; hence `d'(y)>0.9`.

At the upper endpoint,

```math
d(1.5336)<0.02784.
\tag{6.3}
```

The right side of SOD.11 increases when either `y` or `d` is enlarged. Therefore throughout the entire interval it is at most

```math
\frac{\pi}{4\sqrt2}(2\cdot1.5336)^{3/2}\sqrt{0.02784}
+
\frac{0.02784^2}{4\pi}
<0.49782.
\tag{6.4}
```

Equations (6.2) and (6.4) contradict SOD.11 by more than `10^{-3}`. Thus no slope-one subsequence can have `y<=1.5336`, proving SOD.1.

The decimal checks above have a deliberately wide margin; no optimizer digits are being used as a proof dependency.

---

## 7. Stronger implicit endpoint

The conservative `1.5336` is not the natural root of SOD.11. Let `y_OD` be the first root above the SAC lower endpoint of

```math
\frac12\sin y
=
\frac{\pi}{4\sqrt2}(2y)^{3/2}
\sqrt{y+1-\sqrt{2\pi\sin y}}
+
\frac{(y+1-\sqrt{2\pi\sin y})^2}{4\pi}.
\tag{7.1}
```

Numerically,

```math
y_{OD}\approx1.53380484.
```

SOD.1 intentionally states the slightly weaker `1.5336` bound so the report does not depend on certifying the last digits of this scalar root. A future interval-arithmetic checker could safely promote a stronger terminating decimal.

---

## 8. Consequences for external population

The existing external-force-hull population theorem gives, when `h/D->y`,

```math
\liminf\frac{Z_{ext}}{D^2}
\ge
\frac\pi{2\sqrt3}
-
\frac{2y^2}{\pi\sqrt3}
```

whenever the right side is positive.

Thus the subphase

```math
1.5336\le y<\pi/2
```

still forces a quadratic population outside the force hull. At the new lower endpoint `y=1.5336`, the displayed coefficient is about `0.0424`.

The remaining upper subphase

```math
\pi/2\le y\le1.63496438\ldots
```

must instead be attacked through the near-maximal diameter support / singleton-cloud structure.

---

## 9. Regression audit

- OD is used only for the OP outer pockets; bounded exceptional faces are handled separately by the `Q^2/(4pi)` capacity.
- No assumption that one pocket dominates is used.
- The rough `x_B+a<=2q` bound is valid without any pocket-degree classification.
- The proof does not require `s_C=o(D)`; setting `t<=1` deliberately gives pinned surplus its most favorable possible cavity capacity.
- The proof does not require `Q=o(D)` a priori; SOD.8 derives the needed small `Q` from the perimeter requirement.
- The conservative endpoint `1.5336` has a numerical margin larger than `10^-3` in normalized area.
- Level I remains open because the interval above `1.5336` is not excluded.

---

## 10. Next target

The current slope-one density window is only about `0.1014` wide:

```math
1.5336\le y\le1.63496438\ldots .
```

The lower half still has a quadratic external force-hull population until `y=pi/2`; the upper half has increasingly dense actual diameter support.

Two high-value next moves are:

1. retain the exact PC variables `a,d_P,c_B,Q` in OD rather than use `x_B+a<=2q`; this should improve SOD.11 and may push the lower bound past `pi/2`;
2. combine `h=q-o(D)` with the diameter-graph caterpillar/odd-cycle classification and the C66 stress-star support to show that `y>=pi/2` forces a large topological off-star blocker family whose response cannot remain `o(1/D)`.

Crossing `pi/2` would be particularly valuable because it eliminates the entire subphase already known to contain a forced quadratic external population.

## 11. Compact handoff

```text
SOD at RCC slope one.
SAC gives attachment-cell area=o(D^2), so G=area(F)-o(D^2).
Let y=h/D<pi/2, p=per(F)/D. PI gives A=0.5 sin y.
Actual-perimeter JC with e_BB/D<=1 and p<=2y gives
    p >= p_req(y)=y-1+sqrt(2pi sin y).
Therefore with
    d(y)=2y-p_req(y)=y+1-sqrt(2pi sin y),
we have
    (b-P_F)/D <= d(y),
    Q/D <= d(y).
OD and x_B+a<=2q=(2y+o(1))D give
    H_out/D^2 <= [pi/(4sqrt2)](2y)^(3/2)sqrt(d(y)).
JC face isoperimetry gives
    A_exc/D^2 <= d(y)^2/(4pi).
Since G<=H_out+A_exc+O(D), every survivor must satisfy
    0.5 sin y
    <= [pi/(4sqrt2)](2y)^(3/2)sqrt(d(y))+d(y)^2/(4pi).
On 1.5038<=y<=1.5336, LHS>0.49887 while RHS<0.49782.
Contradiction. Hence
    liminf h/D >=1.5336.
Together with SAC:
    1.5336 <= h/D <=1.6349643789... at slope one.
```
