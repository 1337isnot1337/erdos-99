> Generated reading edition · [exact source](../../../docs/reports/target_c_five_arc_pin_delay_09604_2026-09-10.md) · source SHA-256 `ee142b5f6f99d30a5151b491d13cb8d6b0959b22179a3c89b54651a9625ee119`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Presentation repairs: 3 exact-source-bound TeX/escape correction(s); [reviewed repair ledger](../../../docs/publication/reading-tex-repairs.json). Frozen source bytes are unchanged.

> Source formatting note: 22 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-D35CCB1790E4","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — attachment-pin density delays the five-arc phase past `0.9604`

**Date:** 2026-09-10  
**Repository branch:** `research/c2-renorm-paired-pocket-20260910` after TA  
**Run type:** projective-direction packing / attachment-incidence coupling  
**Target:** Target C, all post-ZF survivors  
**Computation:** exact rational sign certificate `research/target_c_five_arc_pin_threshold_check.py`

## LEVEL I STATUS

`STILL OPEN`.

TA gives a sharp three-component circular attachment envelope up to the first formal
five-component transition

```math
z_5=\sin\frac{2\pi}{5}=0.9510565\ldots .
```

A five-component maximal circle set exists immediately above `z_5`, but a Target C
unloaded component cannot use it immediately: C40 forces linearly many distinct loaded
attachment pins, and each pin carries a distinct actual diameter direction.  C67
separates those projective directions by `1/D+o(1/D)`.  The five arcs therefore need
positive angular measure before they can host enough pins.

Define `z_*` to be the unique root in `(z_5,1)` of

```math
\boxed{
10\arcsin z-4\pi=\frac z3.
}
\tag{FD.1}
```

Then every post-ZF survivor sequence satisfies

```math
\boxed{
\liminf\mu_D\ge z_*.
}
\tag{FD.2}
```

The exact certificate proves

```math
\boxed{0.9604<z_*<0.961.}
\tag{FD.3}
```

High-precision diagnostic evaluation gives

```math
z_*=0.9604607492747301\ldots .
```

Thus the explicit all-phase renormalized frontier jumps from `>0.8995` to
`>0.9604`.

---

## 1. Every attachment pin supplies a distinct projective diameter direction

Fix an unloaded component `I_r`.  Let

```math
\delta_r=\operatorname{diam}_{C[I_r]}I_r,
\qquad
A_r\subset B
```

be its loaded attachment set.  C40 gives

```math
\boxed{
\delta_r\le3|A_r|-3.
}
\tag{1.1}
```

Hence, if

```math
\delta_r/D\to z>0,
```

then

```math
\boxed{
\liminf\frac{|A_r|}{D}\ge\frac z3.
}
\tag{1.2}
```

Every `b in A_r` is a positively diameter-loaded force-hull vertex, so choose one
actual diameter edge `e_b` incident to `b`.

### Lemma FD.1 — injective pin-to-diameter-edge map below unit normalized diameter

If

```math
\delta_r/D\to z<1,
```

then the chosen edges `e_b` are distinct for all sufficiently large members of the
sequence.

#### Proof

For any two attachments `b,b' in A_r`, choose contact neighbors in `I_r` and a shortest
internal contact path.  As in RA,

```math
|b-b'|\le\delta_r+2.
\tag{1.3}
```

If `e_b=e_{b'}`, then `b,b'` are the two endpoints of one actual diameter edge, so

```math
|b-b'|=D.
```

Since `delta_r/D->z<1`, equation (1.3) is strictly below `D` for large `D`, a
contradiction. `square`

Thus `A_r` selects at least `|A_r|` distinct projective diameter directions.
Canonical C67 separates every two distinct actual diameter directions by

```math
\boxed{
\delta_D=2\arcsin\frac1{2D},
\qquad D\delta_D\to1.
}
\tag{1.4}
```

---

## 2. FS transfers attachment arcs to projective direction arcs

Let `o` be the full-source FS center.  For a selected incident diameter edge `e_b`,
orient its unit direction `u_b` toward endpoint `b`.  If `m_{e_b}` is its midpoint,
then exactly

```math
b-o=\frac D2u_b+(m_{e_b}-o).
\tag{2.1}
```

FS gives, uniformly over all actual diameter edges,

```math
|m_e-o|=o(D).
\tag{2.2}
```

Therefore the oriented angular direction of `u_b` differs from the polar direction of
`b-o` by `o(1)`, uniformly in `b`.  Passing to the projective circle only identifies
opposite directions.

Now suppose the scaled attachment directions converge into a maximal feasible closed
ordinary-circle set `M`.  Because its diameter is `<1`, `M` contains no antipodal pair,
so projection modulo `pi` is injective on `M` and preserves its total angular measure.
If `M` has `m=O(1)` components and total angular measure `L`, the selected projective
directions all lie in an `o(1)` neighborhood of the projected union of those `m`
arcs.

A `delta_D`-separated set of `N` points contained in a union of `m` projective arcs of
total length `L+o(1)` satisfies

```math
N\delta_D\le L+o(1)+m\delta_D.
\tag{2.3}
```

Indeed, put disjoint radius-`delta_D/2` arcs around the selected directions; their
union lies in the corresponding thickening of the `m` host arcs.

Using `N>=|A_r|`, (1.2), and `Ddelta_D->1` gives:

### Theorem FD.2 — attachment-pin angular measure

For a macroscopic unloaded component with

```math
\delta_r/D\to z<1,
```

every maximal feasible circle set `M` containing its limiting attachment directions
has angular measure

```math
\boxed{|M|\ge z/3.}
\tag{FD.4}
```

---

## 3. The five-component phase is delayed

Use TA notation

```math
\theta=2\arcsin z,
\qquad
\varphi=\pi-\theta.
```

TA proves that an inclusion-maximal feasible wrapping circle set with `m` connected
components has

```math
\boxed{|M|=\pi-m\varphi,}
\tag{3.1}
```

and `m` must be odd.

In the first five-component range

```math
z_5<z<z_7:=\sin\frac{3\pi}{7},
```

one has

```math
\frac\pi7<\varphi<\frac\pi5,
```

so a wrapping maximal set has `m=3` or `m=5`.

For `m=5`, (3.1) is

```math
|M|
=
\pi-5(\pi-2\arcsin z)
=
10\arcsin z-4\pi.
\tag{3.2}
```

FD.4 therefore gives the necessary condition

```math
\boxed{
10\arcsin z-4\pi\ge z/3.
}
\tag{3.3}
```

The left-minus-right function has derivative

```math
\frac{10}{\sqrt{1-z^2}}-\frac13>0,
```

so it has at most one root.  At `z=z_5` the first two terms in (3.3) cancel to zero,
while `z/3>0`; hence the inequality fails.  It is positive before `z=1`, so there is a
unique root `z_*` satisfying FD.1.

Consequently:

### Corollary FD.3

For every

```math
z_5<z<z_*,
```

a Target C macroscopic unloaded attachment set cannot belong to a five-component
maximal feasible circle set.  Any wrapping maximal extension must still have exactly
three components.

---

## 4. The three-arc envelope therefore persists to `z_*`

TA's three-component proof does not use `z<z_5` except to exclude `m=5`.  Once FD.3
supplies that exclusion, the same Jensen calculation gives

```math
\boxed{
area(conv A_r)/D^2
\le W_3(z)+o(1),
}
\tag{4.1}
```

for every macroscopic component with normalized graph diameter

```math
\sqrt3/2\le z<z_*.
```

Here

```math
W_3(z)
=
\frac\pi4-
\frac38\left(g(z)-\sin g(z)\right),
\qquad
g(z)=\frac{4\pi}{3}-2\arcsin z.
\tag{4.2}
```

The concentration argument from TA also extends.  At most one attachment component can
wrap the center because two such components would consume at least `sqrt(3)>mu` of
the graph-diameter budget.  The remaining cap components have total normalized mass
below `0.1`.  Throughout `z<=z_*<0.961`, one has

```math
g(z)>\pi/2,
```

and hence

```math
W_3'(z)
=
\frac34\frac{1-\cos g(z)}{\sqrt{1-z^2}}
>\frac32,
```

whereas the cap envelope satisfies `B'(r)<1/100` for `r<0.1`.  Thus shifting the
remaining graph-diameter mass into the three-component wrapping cell only increases
the area upper bound.

Therefore for every convergent survivor subsequence with

```math
\sqrt3/2\le\mu<z_*,
```

```math
\boxed{
\limsup\frac{C_{att}}{D^2}\le W_3(\mu).
}
\tag{FD.5}
```

---

## 5. Joint force-side feedback excludes the entire interval below `z_*`

TA used only FSDB's fixed area lower bound.  Here keep the stronger side-area feedback
from JS/SC.

Let `C` be the total normalized chord cost from positive macroscopic projective gaps.
SC gives

```math
\boxed{
\liminf\frac{area(F)}{D^2}
\ge
A(C):=\frac{\pi-\phi(C)}4,
}
\tag{5.1}
```

where

```math
\phi(C)=2\arcsin(C/2)-C\sqrt{1-C^2/4}.
```

JS gives the joint budget

```math
3x+C\le2\mu+\pi,
\qquad
C\le x,
\tag{5.2}
```

for

```math
x=(d_P+Q)/D.
```

RP paired-pocket capacity gives

```math
G/D^2\le x^2/(4\pi)+o(1).
\tag{5.3}
```

Together with FD.5 and `area(F)=C_att+G`, every survivor with `mu<z_*` would need some
`C` satisfying

```math
\boxed{
A(C)
\le
W_3(\mu)+
\frac{(2\mu+\pi-C)^2}{36\pi}.
}
\tag{5.4}
```

We show that the easiest value is `C=0` throughout this interval.

Put `B_0=2mu+pi`.  From `C<=x` and (5.2),

```math
C\le B_0/4.
```

The exact certificate proves `z_*<0.961`; with `pi<22/7`,

```math
C<\frac{2(0.961)+22/7}{4}
=
\frac{17727}{14000}
<\frac{51}{40}.
\tag{5.5}
```

Subtract the left-minus-right gap at `C=0`.  The difference is

```math
D(C)
=-\frac{\phi(C)}4
+
\frac{C(2B_0-C)}{36\pi}.
\tag{5.6}
```

It is concave because `phi` is convex.  Also `D(0)=0`.  At the other allowed endpoint
`C=B_0/4`,

```math
D(C)
=-\frac{\phi(C)}4+\frac{7C^2}{36\pi}.
```

For `C<=51/40`, elementary integration of

```math
\phi'(u)=\frac{u^2}{2\sqrt{1-u^2/4}}
```

gives

```math
\frac{\phi(C)}{C^2}
\le
\frac C6+\frac{C^3}{80}+\frac{3C^5}{1120}
\le
\frac{28377658153}{114688000000}
<
\frac{49}{198}
<
\frac7{9\pi}.
\tag{5.7}
```

For completeness, the reciprocal estimate used in the integration is

```math
(1-t)^{-1/2}\le1+t/2+3t^2/5,
\qquad
0\le t\le41/100;
```

after squaring, the required sign reduces to the increasing cubic
`36t^3+24t^2+85t-45`, which is still negative at `t=41/100`.

Thus `D(B_0/4)>0`; concavity gives

```math
D(C)\ge0
```
throughout the full allowed interval.  Hence `C=0` minimizes the obstruction in
(5.4).

At `C=0`, condition (5.4) becomes

```math
\boxed{
\frac\pi4
\le
W_3(\mu)+
\frac{(2\mu+\pi)^2}{36\pi}.
}
\tag{5.8}
```

The right side is strictly increasing in `mu`.  The exact certificate proves that even
at

```math
\mu=0.961
```

the reverse strict inequality holds, with positive rigorous margin.  Since
`z_*<0.961`, equation (5.8) is impossible for every `mu<z_*`.

Combining with RA for the lower interval proves FD.2.

---

## 6. Exact certificate and numerical value

Run

```sh
python3 research/target_c_five_arc_pin_threshold_check.py
```

The script uses `fractions.Fraction`, integer square-root enclosures, and alternating
arctangent bounds.  It proves:

```math
F_5(0.9604)<0,
\qquad
F_5(0.961)>0,
```

where

```math
F_5(z)=10\arcsin z-4\pi-z/3.
```

Thus

```math
0.9604<z_*<0.961.
```

It also certifies the side-cost inequality (5.7) and a strict positive version of
(5.8)'s contradiction at `mu=0.961`.

Floating-point diagnostics give

```math
z_*=0.9604607492747301\ldots .
```

No floating-point value participates in an assertion.

---

## 7. Endpoint structure

A sequence with

```math
\mu_D\to z_*
```

cannot remain in the three-component attachment phase, because (5.8) has a fixed
positive gap at `z_*`.  It must therefore contain one macroscopic unloaded component
with normalized graph diameter tending to `z_*` whose maximal attachment set has five
components.

The pin-density inequalities then all become sharp:

```math
\boxed{
\frac{|A_r|}{D}\to\frac{z_*}{3},
\qquad
|M|\to\frac{z_*}{3}.
}
\tag{7.1}
```

Since this one component already consumes all available graph-diameter mass,

```math
\boxed{
\frac1D\sum_{s\ne r}\delta_s\to0,
\qquad
R_I/D\to0,
\qquad
s_B/D\to0.
}
\tag{7.2}
```

C40's chain

```math
\delta_r+3\le t_r\le3|A_r|
```

is also asymptotically sharp, so

```math
\boxed{
t_r/D\to z_*,}
\tag{7.3}
```

and all but `o(D)` of the giant component's attachment pins use all three available
loaded contact incidences into that same component.

The selected incident projective diameter directions asymptotically saturate the five
host arcs at spacing `delta_D`.  This is the new exact endpoint normal form.

No contradiction to this five-arc/pinned-circuit geometry is proved here.

---

## 8. Next target

The endpoint has one giant unloaded component satisfying simultaneously:

- `delta_r/D -> z_*`;
- `|A_r|/D -> z_*/3`;
- `t_r/D -> z_*`;
- almost every giant-component attachment pin has contact degree three entirely into
  that component;
- the component's Eppstein slack `r_r=o(D)`;
- the global loaded contact-degree slack `s_B=o(D)`;
- its five attachment arcs are projectively saturated by actual diameter directions.

The next theorem should exploit this combined **Eppstein-equality + five-arc +
three-contact pin** structure.  A promising route is to use the equality proof of
Eppstein's `e<=2n-delta-2` theorem: `r_r=o(D)` means the component is asymptotically
quadrangulated with nearly minimum outer boundary for its graph diameter.  Its outer
boundary must then accommodate `z_*D` pin incidences concentrated into five short
loaded arcs.  A quantitative boundary-turning or rhombic-train argument may make those
requirements incompatible.

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

C40: delta_r<=3|A_r|-3.  For delta_r/D->z<1, choose one actual diameter edge at each
attachment pin.  Two pins cannot choose the same edge because that would make them a
diameter pair, while diam(A_r)<=delta_r+2<D.  Thus there are |A_r| distinct chosen
projective diameter directions.  FS makes each chosen direction o(1)-close to the
pin's polar direction; C67 separates them by delta_D~1/D.

If a maximal wrapping attachment set M has five components, TA gives
  |M|=10 asin z-4pi.
Projective packing and |A_r|/D>=z/3 force
  |M|>=z/3.
Hence five components are impossible before the unique root
  z_*: 10 asin z_*-4pi=z_*/3,
  z_*=0.96046074927...,
with exact 0.9604<z_*<0.961.

Below z_* every wrapping attachment cell is still three-component, so
  C_att/D^2<=W3(mu).
Keeping JS's joint side/pocket budget and SC's force-side area floor yields
  A(C)<=W3(mu)+(2mu+pi-C)^2/(36pi).
For mu<z_* the C-dependent obstruction is minimized at C=0.  An exact certificate
shows even mu=.961 violates
  pi/4<=W3(mu)+(2mu+pi)^2/(36pi).
Therefore
  liminf mu_D>=z_*>0.9604.

Endpoint: one giant component has five attachment arcs, |A_r|/D->z_*/3,
t_r/D->z_*, R_I,s_B=o(D), and almost every giant pin uses all three contact slots into
that component.  Next: combine this with Eppstein near-equality / quadrangulation.
```
