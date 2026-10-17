> Generated reading edition · [exact source](../../../docs/reports/target_c_post_zf_difference_body_perimeter_2026-09-09.md) · source SHA-256 `2409c7d151654bf855edff2ee16dea7eb16bfac2723f5c0fe30e7e5fa89264af`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Presentation repairs: 1 exact-source-bound TeX/escape correction(s); [reviewed repair ledger](../../../docs/publication/reading-tex-repairs.json). Frozen source bytes are unchanged.

<!-- theorem-state: {"artifact_id":"ART-628A5B0F10DE","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — post-ZF difference-body perimeter theorem

**Date:** 2026-09-09  
**Repository base:** `58420d2f13ba3f75ea943d8b60e90b2984287081` plus the two preceding commits on this branch  
**Run type:** exact convex-geometric / post-ZF branch theorem  
**Target:** Target C C-II after ZF  
**Depends on:** C65 full diameter visibility, C67 diameter-direction separation, report-level ZE/ZT/ZS, planar convex perimeter identities  
**External web search:** not used in the proof  
**Computation:** arithmetic only for displayed decimals

## LEVEL I STATUS

`STILL OPEN`

The post-ZF stack gives at least `D` actual diameter edges, but that count does not use the fact that all their length-`D` vectors must fit simultaneously into one convex force hull. The difference body of the force hull supplies that missing global coupling.

Let

- `F=conv V(C)` be the C65 force hull;
- `D` be the source diameter;
- `H` be the full actual diameter graph on terminal set `B_+`;
- `h=|E(H)|`, `q=|B_+|`;
- `b` be the outer contact-face boundary-walk length;
- `Q=sum_F(deg F-4)` over bounded nonquadrilateral contact faces;
- `s_Z=e+h-(2v-2)>=0` be the ZF mixed-row surplus.

Put

```math
a_D:=\arcsin\frac1{2D}.
\tag{DB.0}
```

Then every audited post-ZF survivor obeys the exact finite inequality

```math
\boxed{
Q+2s_Z
\le
h+1-2D\cos\bigl((h-1)a_D\bigr).
}
\tag{DB.1}
```

In particular the nonnegative left side forces

```math
\boxed{
h+1\ge2D\cos\bigl((h-1)a_D\bigr).}
\tag{DB.2}
```

Consequently, if `rho` is the unique positive solution of

```math
\rho=\cos\rho,
\tag{DB.3}
```

then

```math
\boxed{
\liminf_{D\to\infty}\frac hD
\ge2\rho
=1.4781702664\ldots .
}
\tag{DB.4}
```

This improves the post-ZF count `h>=D` by about 47.8 percent without using any KKT weight floor.

The improvement feeds back into C67: the C67 projective spread now necessarily saturates its `pi/3` ceiling, so every post-ZF survivor satisfies

```math
\boxed{
\liminf_{D\to\infty}
\frac{area(F)}{D^2}
\ge\frac{\sqrt3}{4}
=0.4330127019\ldots .
}
\tag{DB.5}
```

Thus the previously committed ZA bound `0.5 sin(1)=0.420735...` is correct but no longer sharp downstream of DB.

For the perfect-matching diameter branch, `q=2h`, hence

```math
\boxed{
\liminf\frac qD
\ge4\rho
=2.9563405329\ldots,
}
\tag{DB.6}
```

which supersedes the preceding matching bound `2*3^(1/4)=2.632148...`.

---

## 1. All diameter vectors lie in the difference body

Choose one unit vector `u_e` along each projective direction of a diameter edge `e=bk`, so

```math
b-k=\pm D u_e.
```

Because `b,k in F`,

```math
\pm D u_e\in F-F.
\tag{1.1}
```

Define the centrally symmetric convex polygon

```math
P_H:=D\,conv\{\pm u_e:e\in E(H)\}.
\tag{1.2}
```

Then

```math
\boxed{P_H\subseteq F-F.}
\tag{1.3}
```

C67 proves that distinct actual diameter edges have distinct projective line directions and that their projective circular separation is at least

```math
\boxed{2a_D=2\arcsin\frac1{2D}.}
\tag{1.4}
```

Order the `h` projective directions cyclically on the projective circle of circumference `pi`, and write their gaps as

```math
g_1,\ldots,g_h.
```

Then

```math
\boxed{
g_i\ge2a_D,
\qquad
\sum_{i=1}^h g_i=\pi.}
\tag{1.5}
```

The `2h` points `+-D u_e` occur on the Euclidean circle of radius `D`; the projective gaps occur twice around that circle. Hence the exact perimeter of `P_H` is

```math
\boxed{
per(P_H)=4D\sum_{i=1}^h\sin\frac{g_i}{2}.}
\tag{1.6}
```

---

## 2. Difference-body perimeter converts directions into force-hull perimeter

For planar convex bodies, perimeter is monotone under inclusion. Also perimeter is Minkowski additive:

```math
per(K+L)=per(K)+per(L).
\tag{2.1}
```

For completeness, both statements follow directly from Cauchy's perimeter formula

```math
per(K)=\int_0^\pi w_K(\theta)\,d\theta,
```

because widths are monotone under inclusion and satisfy

```math
w_{K+L}=w_K+w_L.
```

Therefore

```math
per(F-F)=per(F)+per(-F)=2per(F).
\tag{2.2}
```

Using (1.3) and (1.6),

```math
2per(F)
=per(F-F)
\ge per(P_H)
=4D\sum_i\sin\frac{g_i}{2}.
```

Thus

```math
\boxed{
per(F)
\ge2D\sum_{i=1}^h\sin\frac{g_i}{2}.}
\tag{2.3}
```

This is the basic difference-body inequality. It uses the complete actual diameter graph but no diameter weights.

---

## 3. Exact minimization over the direction gaps

The function

```math
f(g)=\sin(g/2)
```

is concave on `[0,pi]`. Under the linear constraints

```math
g_i\ge2a_D,
\qquad
\sum g_i=\pi,
```

a concave function sum is minimized at an extreme point of the feasible simplex: all but at most one gap are at the lower bound.

Equivalently, repeated transfer of a small amount from the smaller of two nonminimal gaps to the larger cannot increase the sum, until one reaches the lower bound. Therefore

```math
\sum_{i=1}^h\sin\frac{g_i}{2}
\ge
(h-1)\sin a_D
+
\sin\left(
\frac{\pi-2(h-1)a_D}{2}
\right).
\tag{3.1}
```

Since

```math
\sin a_D=\frac1{2D},
```

and

```math
\sin\left(\frac\pi2-(h-1)a_D\right)
=\cos((h-1)a_D),
```

we obtain

```math
\boxed{
\sum_i\sin\frac{g_i}{2}
\ge
\frac{h-1}{2D}
+
\cos((h-1)a_D).}
\tag{3.2}
```

Insert this into (2.3):

```math
\boxed{
per(F)
\ge
h-1+2D\cos((h-1)a_D).}
\tag{3.3}
```

The feasibility of the gap constraints guarantees the remaining gap in (3.1) is at least `2a_D`; no extra assumption is hidden in the extremal form.

---

## 4. The post-ZF contact ledger gives the opposite perimeter bound

The outer contact-face boundary walk has geometric length exactly `b` and convex hull `F`, so the closed-walk perimeter lemma from OP gives

```math
\boxed{per(F)\le b.}
\tag{4.1}
```

ZE gives the exact Euler/ZF identity

```math
\frac{b+Q}{2}=h-s_Z.
\tag{4.2}
```

Thus

```math
\boxed{b=2h-Q-2s_Z.}
\tag{4.3}
```

Combine (3.3), (4.1), and (4.3):

```math
h-1+2D\cos((h-1)a_D)
\le2h-Q-2s_Z.
```

Rearranging proves DB.1:

```math
\boxed{
Q+2s_Z
\le
h+1-2D\cos((h-1)a_D).}
```

Since `Q,s_Z>=0`, DB.2 follows immediately.

This is an exact finite inequality. It is stronger than combining C67 with `h>=D`, because the diameter-direction system is now constrained by the actual contact-boundary budget.

---

## 5. Asymptotic diameter-edge constant

The diameter graph is a convex geometric thrackle, so

```math
h\le q.
```

Unit separation of consecutive force-hull vertices gives

```math
q\le per(F)\le\pi D.
```

Hence `h/D` is bounded. Take any subsequence on which

```math
\frac hD\to y.
```

Since

```math
a_D=\frac1{2D}+O(D^{-3}),
```

we have

```math
(h-1)a_D\to\frac y2.
```

Divide DB.2 by `D` and pass to the limit:

```math
\boxed{y\ge2\cos(y/2).}
\tag{5.1}
```

On `[0,pi]` the function

```math
\phi(y)=y-2\cos(y/2)
```

is strictly increasing because

```math
\phi'(y)=1+\sin(y/2)>0.
```

Its unique positive zero is `y=2rho`, where `rho` is the unique positive solution of

```math
\rho=\cos\rho.
```

Therefore every subsequential limit satisfies `y>=2rho`, proving DB.4.

Numerically,

```math
\rho=0.7390851332\ldots,
\qquad
2\rho=1.4781702664\ldots .
```

---

## 6. C67 now saturates at sixty degrees

C67 says among the `h` projective diameter directions there are two separated by at least

```math
\min\left\{\frac\pi3,(h-1)2a_D\right\}.
\tag{6.1}
```

DB.4 gives

```math
\liminf (h-1)2a_D
\ge2\rho
=1.47817\ldots
>\frac\pi3.
```

Thus for all sufficiently large post-ZF survivors the C67 ceiling is active. Two actual diameter chords then span a triangle or crossing quadrilateral of area at least

```math
\frac{D^2}{2}\sin\frac\pi3
=\frac{\sqrt3}{4}D^2
```

inside `F`. Therefore

```math
\boxed{
area(F)\ge\frac{\sqrt3}{4}D^2
}
\tag{6.2}
```

for all sufficiently large members of every unbounded post-ZF sequence, proving DB.5.

The full source hull `K=conv A` still satisfies

```math
area(K)\le\frac\pi4D^2,
```

so the external geometric shell has the universal post-ZF bound

```math
\boxed{
area(K\setminus F)
\le
\frac{\pi-\sqrt3}{4}D^2
=0.3523854604\ldots D^2.
}
\tag{6.3}
```

This remains quadratic, so it is not a force-bulk closure by itself.

---

## 7. Exact branching-defect ledger

ZT gives

```math
q=x_B+Q+2(q-h)+2s_Z,
```

because `f+g_F=Q` and `d_H=q-h`. Rearranging,

```math
\boxed{
2h-q=x_B+Q+2s_Z.}
\tag{7.1}
```

Every terminal is incident to at least one actual diameter edge, so

```math
\sum_{b\in B_+}(deg_H(b)-1)
=2h-q.
```

Hence

```math
\boxed{
\sum_{b\in B_+}(deg_H(b)-1)
=x_B+Q+2s_Z.}
\tag{7.2}
```

This is an exact finite interpretation of the post-ZF contact defect: outer-walk excess, bounded face defect, and extra mixed row dependencies pay exactly for total diameter branching above degree one.

Consequences:

1. if `x_B+Q+2s_Z=o(D)`, then all but `o(D)` terminals are diameter leaves;
2. if a linear fraction of terminals have diameter degree at least two, the contact/topology defect is automatically linear;
3. the perfect-matching case is exactly the zero-branching endpoint and therefore forces `x_B=Q=s_Z=0`, recovering MB.

---

## 8. Matching branch

If `H` is a perfect matching, then

```math
q=2h.
```

DB.4 immediately gives

```math
\boxed{
\liminf\frac qD
\ge4\rho
=2.9563405329\ldots .}
\tag{8.1}
```

This is stronger than the earlier ZA/MB bound

```math
2\,3^{1/4}=2.6321480259\ldots .
```

Since MB already proves

```math
per(F)=q,
```

the matching force hull has perimeter within at most

```math
(\pi-4\rho)D+o(D)
=0.1852521207\ldots D+o(D)
\tag{8.2}
```

of the maximum possible `pi D`.

The matching branch still requires a quadratic external rattler population by MB. DB does not itself exclude that shell, but it forces the pure rhombic core to have a much more nearly maximal perimeter than previously known.

---

## 9. Defect-dependent strengthening

DB.1 retains quantitative defect information rather than discarding it. Write along a subsequence

```math
\frac hD\to y,
\qquad
\frac{Q+2s_Z}{D}\to z
```

when the limits exist. Dividing DB.1 by `D` gives

```math
\boxed{
z\le y-2\cos(y/2).}
\tag{9.1}
```

The right side is strictly increasing in `y`. Therefore any positive linear contact/row defect forces the diameter-edge density strictly above the universal `2rho` endpoint.

This is potentially useful for a future high-defect / leaf-heavy split: the exact amount of topological defect becomes a lower bound on how far the diameter graph must move away from its minimum post-ZF edge density.

---

## 10. Regression audit

### Regular odd shell

The regular odd shell has `h=q`, one exceptional bounded `q`-gon, and positive `s_Z`. Its diameter directions are distributed around the full projective circle, so the difference-body lower bound is compatible with its near-maximal force-hull perimeter. DB does not falsely exclude it by local topology alone.

### Unit square

For the unit square, `D=sqrt(2)`, `h=2`, `Q=s_Z=0`. DB.1 reduces to a valid finite nonnegative inequality; the theorem is not claimed to be sharp at small `D`.

### Perfect matching

Allowed. DB strengthens its required perimeter but does not infer central symmetry or KKT weight uniformity. The exact noncentrally-symmetric hexagon regression in MB remains binding against such shortcuts.

### Near-star stress concentration

Allowed. DB counts actual diameter directions, not their `beta` weights. A low-weight diameter edge contributes its full length-`D` vector to `F-F` because C65 makes it an actual source diameter pair.

### External rattlers

Allowed. They do not enter `F-F`; DB constrains the positive core geometry and leaves external packing as the remaining force-bulk obligation.

---

## 11. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| `P_H subset F-F` | proved | every actual diameter vector is a difference of two force-hull points |
| `per(P_H)=4D sum sin(g_i/2)` | proved | exact chord lengths of the cyclic `2h`-gon |
| difference-body perimeter inequality (3.3) | proved | convex inclusion, Cauchy perimeter formula, exact concave gap minimization |
| DB.1 | proved and new | combine (3.3) with OP perimeter and ZE |
| `liminf h/D>=2rho` | proved | exact finite inequality plus compact subsequence limit |
| saturated C67 area floor `sqrt3/4` | proved post-ZF | DB edge density exceeds C67's `pi/3` threshold |
| branching ledger (7.2) | proved and new bookkeeping interpretation | direct ZT algebra plus degree sum |
| matching `q/D>=4rho` | proved | `q=2h` |
| Level I | still open | external source population / exact final contradiction remains |

---

## 12. Promotion recommendation

**Hold as report.**

DB depends on report-level ZF/ZE/ZT. If that stack is promoted, DB should replace the weaker downstream statements `h>=D` and the old post-ZF C67 area floor.

---

## 13. Next theorem

DB makes the external-shell problem substantially more rigid:

- at least `1.47817 D` actual diameter edges;
- force-hull area at least `sqrt3 D^2/4`;
- exact diameter branching equals `x_B+Q+2s_Z`;
- in the perfect-matching endpoint, force-hull perimeter at least `4rho D=2.95634D`.

The next high-value split is now exact:

1. **low branching defect** `x_B+Q+2s_Z=o(D)`: almost every terminal is a diameter leaf; attack the near-matching geometry plus the required external shell;
2. **linear branching defect**: DB.9 forces a larger diameter-edge density and the face/topology ledger already contains a linear defect currency that should be combined with DT/ZM.

Do not revert to a support-count-to-weight argument; DB is entirely weight-free.

---

## 14. Compact handoff

```text
LEVEL I STATUS: STILL OPEN

Difference-body theorem DB:
Let h be the number of actual diameter edges, let their projective gaps be g_i,
and put a_D=asin(1/(2D)). C67 gives g_i>=2a_D and sum g_i=pi.

Every +-D u_i lies in F-F. Hence
    per(F-F)=2 per(F)
      >= 4D sum_i sin(g_i/2).
Concavity gives
    sum_i sin(g_i/2)
      >= (h-1)/(2D) + cos((h-1)a_D),
so
    per(F)>=h-1+2D cos((h-1)a_D).

OP gives per(F)<=b, while ZE gives
    b=2h-Q-2s_Z.
Therefore
    Q+2s_Z
      <= h+1-2D cos((h-1)a_D).
In particular
    h+1>=2D cos((h-1)a_D).

If rho is the positive solution rho=cos rho,
    liminf h/D >= 2rho = 1.4781702664...

Thus C67 saturates its pi/3 spread ceiling and
    liminf area(F)/D^2 >= sqrt(3)/4 = 0.4330127019...

Exact branching ledger:
    sum_b(deg_H(b)-1)
      =2h-q
      =x_B+Q+2s_Z.

Perfect matching:
    q=2h,
so
    liminf q/D >=4rho=2.9563405329...
```
