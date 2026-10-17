> Generated reading edition · [exact source](../../../docs/reports/target_c_discrete_pocket_hybrid_surplus_07739_2026-09-10.md) · source SHA-256 `1f2fce3a1bb1ea499930e4892a8e35da4cc48e421bf77214ad9aaede417f65fe`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-0308F4CA4967","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — discrete pocket capacity raises the post-ZF surplus floor to 0.773954

**Date:** 2026-09-10  
**Repository state:** `1ea7a3c5970d614c9f860841eea5ad3718ca171f` at start; branch `research/c99-c2-dpc-20260910-sol`  
**Run type:** closing proof / exact geometric sharpening / asymptotic branch exclusion  
**Target:** Target C, C-II after ZF/DB/FSDB  
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md`  
**External web search:** used only to locate possible diameter-graph equality literature; no external theorem is used below  
**Computation:** standard-library numerical evaluation of one explicitly defined scalar root only; no computation is a proof dependency

## LEVEL I STATUS

`STILL OPEN`

The strongest result of this run is a new exact finite outer-pocket inequality that uses the fact that the old pocket boundary is a chain of **unit edges**, not an arbitrary rectifiable curve. Combined with the September 9 PC/DB cavity ledgers and the September 10 FSDB whole-source force-hull area floor, it raises the report-level post-ZF lower bound

```math
\liminf_{D\to\infty}\frac{e_{BB}+2s_C}{D}
```

from `0.5882283437...` to

```math
\boxed{
\lambda_{DPH}=0.7739547058568927\ldots .
}
```

The constant is not obtained by a numerical optimizer. It is the unique root of an explicit one-variable monotone equation given in Section 5.

The result does not settle Level I. No proved universal upper bound on the same surplus currency below `lambda_DPH` is currently available.

## 1. Starting endpoint

Work with a sufficiently large triangle-free global minimizer in the C-II lexicographic normal form: contacts are minimized first and diameter pairs second, so `C=C_*`, `H=H_*`, all contact-isolated source points are retained, and the report-level ZF/DB/FSDB hypotheses are in force.

Use the post-ZF notation

- `F` = force hull;
- `P_F=per(F)`;
- `h` = number of actual diameter edges;
- `q=|B_+|` = number of actual diameter endpoints;
- `Q=sum_F(deg F-4)` over bounded nonquadrilateral contact faces;
- `s_Z=e+h-(2v-2)>=0`;
- `d_H=q-h>=0`;
- `e_BB` = number of loaded-loaded unit contacts;
- `s_C>=0` = extra pinned-contact left-nullity;
- `a` = number of missing force-hull side contacts, equivalently the number of OP outer pockets;
- `d_P=sum_P(k_P-3)` = total outer-pocket degree excess;
- `c_B` = number of loaded-loaded unit contacts that are not force-hull sides.

Put

```math
L:=e_{BB}+2s_C.
```

The September 10 FSJC report gave

```math
\liminf L/D\ge0.5882283437\ldots
```

by a continuous isoperimetric cavity bound. The closing implication attacked here is

```text
unit-edge discreteness of every OP pocket
    -> sharper exact outer-pocket area capacity
    -> combine with PC + DB + exceptional-face area
    -> sharpen the total cavity upper bound
    -> compare with the full-source FSDB/GU lower gap
    -> exclude a much larger interval of post-ZF surplus densities.
```

The exact Level I target remains exclusion of every sufficiently large C-II source, or equivalently a theorem forcing the whole-source population inequality

```math
\delta_K+\mathscr O_A\ge(\sqrt3/4)\,per(K),
```

which is the same as `n-1 <= (pi/(2sqrt3))D^2` and contradicts the strict translated-lattice comparison for a global minimizer.

## 2. Strongest genuinely new finite theorem: discrete Dirichlet pocket capacity

### Theorem DPC.1 — one-pocket discrete Green-function bound

Let `P` be one OP outer pocket. Its boundary consists of

1. an old contact chain from `A` to `B` made of exactly `ell>=2` unit edges;
2. the missing force-hull side `BA`, of length `s=|A-B|`.

Then

```math
\boxed{
area(P)^2
\le
\frac{\ell^3-\ell}{6}\,(\ell-s).
}
\tag{DPC.1}
```

Equivalently,

```math
area(P)
\le
\frac1{\sqrt6}\sqrt{\ell^3-\ell}\,\sqrt{\ell-s}.
\tag{DPC.2}
```

This strictly improves the continuous DD bound

```math
area(P)\le\frac1{\sqrt6}\ell^{3/2}\sqrt{\ell-s}
```

for every finite `ell`.

#### Proof

Translate and rotate so

```math
A=(0,0),\qquad B=(s,0),
```

and `P` lies in the upper half-plane. Let the unit-contact chain vertices be

```math
p_j=(x_j,y_j),\qquad j=0,1,\ldots,\ell,
```

with `p_0=A`, `p_ell=B`. OP convexity gives `y_j>=0`, and `y_0=y_ell=0`.

Parameterize each unit edge linearly by arclength on `[j-1,j]`. Since every chain edge has length exactly one,

```math
(\Delta x_j)^2+(\Delta y_j)^2=1,
\qquad
\Delta x_j=x_j-x_{j-1},
\quad
\Delta y_j=y_j-y_{j-1}.
```

As in DD,

```math
(\Delta y_j)^2
=(1-\Delta x_j)(1+\Delta x_j)
\le2(1-\Delta x_j).
```

Summing and using `sum Delta x_j=s` gives

```math
\boxed{
\sum_{j=1}^{\ell}(\Delta y_j)^2
\le2(\ell-s).
}
\tag{DPC.3}
```

Because `y` is linear on every unit interval and the endpoint values vanish,

```math
\int_0^\ell y(t)\,dt
=\sum_{j=1}^{\ell-1}y_j.
\tag{DPC.4}
```

Now define the discrete Dirichlet Green function

```math
g_j=\frac12j(\ell-j),
\qquad 0\le j\le\ell.
```

It satisfies `g_0=g_ell=0` and

```math
2g_j-g_{j-1}-g_{j+1}=1
\qquad(1\le j\le\ell-1).
```

Discrete summation by parts therefore gives

```math
\sum_{j=1}^{\ell-1}y_j
=
\sum_{j=1}^{\ell}
(\Delta y_j)(\Delta g_j).
\tag{DPC.5}
```

Cauchy-Schwarz gives

```math
\left(\sum_{j=1}^{\ell-1}y_j\right)^2
\le
\left(\sum_{j=1}^{\ell}(\Delta y_j)^2\right)
\left(\sum_{j=1}^{\ell}(\Delta g_j)^2\right).
\tag{DPC.6}
```

The Green energy is exact:

```math
\sum_{j=1}^{\ell}(\Delta g_j)^2
=
\sum_{j=1}^{\ell-1}g_j
=
\frac{\ell(\ell^2-1)}{12}.
\tag{DPC.7}
```

Green's theorem in the same orientation as DD gives

```math
area(P)=\int_0^\ell y(t)x'(t)\,dt.
```

Since `y>=0` and `x'<=1`,

```math
area(P)\le\int_0^\ell y(t)\,dt.
\tag{DPC.8}
```

Insert DPC.3 and DPC.7 into DPC.6, then use DPC.4 and DPC.8:

```math
area(P)^2
\le
2(\ell-s)\frac{\ell(\ell^2-1)}{12}
=
\frac{\ell^3-\ell}{6}(\ell-s).
```

This proves DPC.1. `square`

### Theorem DPC.2 — exact global detour form

For each pocket put

```math
x_P:=\ell_P-2=k_P-3\in\mathbb Z_{\ge0}.
```

Then

```math
\sum_Px_P=d_P,
\qquad
\sum_P(\ell_P-s_P)=b-P_F.
```

Every post-ZF source satisfies

```math
\boxed{
H_{out}^2
\le
\frac{d_P^3+6d_P^2+11d_P+6a}{6}\,(b-P_F).
}
\tag{DPC.9}
```

#### Proof

DPC.2 and Cauchy-Schwarz give

```math
H_{out}^2
\le
\frac16
\left(\sum_P(\ell_P^3-\ell_P)\right)
\left(\sum_P(\ell_P-s_P)\right).
\tag{DPC.10}
```

For `x>=0`, let

```math
f(x)=(x+2)^3-(x+2)=x^3+6x^2+11x+6.
```

For `x,y>=0`,

```math
f(x+y)+f(0)-f(x)-f(y)
=3xy(x+y+4)\ge0.
\tag{DPC.11}
```

Repeatedly merging two positive excesses therefore cannot decrease the sum of `f`. With `a` pockets and total excess `d_P`,

```math
\sum_P(\ell_P^3-\ell_P)
=\sum_Pf(x_P)
\le f(d_P)+(a-1)f(0)
=d_P^3+6d_P^2+11d_P+6a.
```

Use the exact OP identity for the total detour to obtain DPC.9. `square`

### Theorem DPC.3 — exact chord-floor form

Because each added force-hull side joins two distinct source points, unit separation gives `s_P>=1`. In fact `s_P>1`, because a force-hull side of length exactly one would already be a unit-contact edge and would not be counted among the missing sides.

Consequently

```math
\ell_P-s_P<\ell_P-1=x_P+1.
```

DPC.1 gives

```math
area(P)
<
\frac1{\sqrt6}(x_P+1)\sqrt{(x_P+2)(x_P+3)}.
\tag{DPC.12}
```

Using geometric mean <= arithmetic mean,

```math
\sqrt{(x+2)(x+3)}\le x+\frac52.
```

Hence

```math
area(P)
<
\frac1{\sqrt6}
\left(x_P^2+\frac72x_P+\frac52\right).
```

Summing and using `sum x_P^2 <= (sum x_P)^2=d_P^2` gives the exact finite estimate

```math
\boxed{
H_{out}
<
\frac1{\sqrt6}
\left(d_P^2+\frac72d_P+\frac52a\right).
}
\tag{DPC.13}
```

The leading quadratic cavity capacity is therefore controlled by `d_P^2`, not by the square of the total chain length `x_B+a`.

### Scope

DPC.1-DPC.3 are finite geometric statements for the OP outer pockets. They do not require global optimality or KKT beyond whatever is needed to produce the OP pocket decomposition. The global-minimizer hypothesis enters only in the FSDB/GU lower-gap comparison below.

### Why this is new

DD treats each pocket boundary as an arbitrary arclength-parametrized curve and uses the continuous `H_0^1` Green function, giving an `ell^3/12` dual energy. DPC uses the exact unit-edge mesh and its discrete Dirichlet Green function, replacing `ell^3` by `ell^3-ell`. More importantly, the unit separation of the missing hull-side endpoints supplies `s_P>1`, which yields DPC.13 and changes the leading global currency from total chain length to outer-pocket degree excess.

## 3. Hybrid asymptotic cavity capacity

Pass to a convergent post-ZF subsequence and write

```math
\lambda:=\lim\frac{L}{D},
\qquad
y:=\lim\frac hD,
\qquad
\nu:=\lim\frac QD.
```

Let

```math
\tau:=\lim\frac{d_P}{D}
```

along a further subsequence when needed. PC.2 gives

```math
e_{BB}=d_P+Q+2(d_H+s_Z)+c_B,
```

so

```math
\boxed{0\le\tau+\nu\le\lambda.}
\tag{3.1}
```

Define

```math
g(y):=y-2\cos(y/2).
\tag{3.2}
```

DB gives

```math
\frac{P_F}{D}
\ge y+2\cos(y/2)-o(1)
```

and the exact outer-walk formula gives

```math
\frac bD=2y-\nu-2\frac{s_Z}{D}+o(1).
```

Therefore the total detour satisfies

```math
\boxed{
\limsup\frac{b-P_F}{D}
\le g(y)-\nu.
}
\tag{3.3}
```

where dropping `2s_Z/D` only weakens the upper bound. DB also gives `y>=2rho`, where `rho=cos rho`.

DPC.9 and DPC.13 imply the two simultaneous leading bounds

```math
\limsup\frac{H_{out}}{D^2}
\le
\frac1{\sqrt6}\tau^{3/2}\sqrt{g(y)-\nu},
\tag{3.4}
```

and

```math
\limsup\frac{H_{out}}{D^2}
\le
\frac1{\sqrt6}\tau^2.
\tag{3.5}
```

The exceptional-face estimate used in JC/ED gives

```math
\limsup\frac{A_{exc}}{D^2}
\le\frac{\nu^2}{4\pi}.
\tag{3.6}
```

Set `C=1/sqrt(6)`. We now remove `nu` without numerical optimization.

For the chord-floor branch,

```math
C(\lambda-\nu)^2+\frac{\nu^2}{4\pi}
\le C\lambda^2
\tag{3.7}
```

for `0<=nu<=lambda`, because `C>1/(4pi)` and direct expansion gives a nonnegative difference.

For the detour branch, put

```math
P(\nu)=C(\lambda-\nu)^{3/2}(g-\nu)^{1/2}
```

on `0<=nu<=min(lambda,g)`, where `g=g(y)`. Since

```math
(1-\nu/\lambda)^{3/2}(1-\nu/g)^{1/2}
\le1-\nu/\lambda,
```

we have

```math
P(0)-P(\nu)
\ge C\lambda^{1/2}\sqrt g\,\nu.
```

Also `nu<=min(lambda,g)<=sqrt(lambda g)`, so

```math
\frac{\nu^2}{4\pi}
\le
\frac1{4\pi}\lambda^{1/2}\sqrt g\,\nu
< C\lambda^{1/2}\sqrt g\,\nu.
```

Thus

```math
\boxed{
P(\nu)+\frac{\nu^2}{4\pi}
\le P(0)
=C\lambda^{3/2}\sqrt{g(y)}.
}
\tag{3.8}
```

Combining both branches, ZG/GU therefore gives the clean hybrid cavity ceiling

```math
\boxed{
\limsup\frac G{D^2}
\le
C\lambda^{3/2}\sqrt{\min\{\lambda,g(y)\}}.
}
\tag{3.9}
```

The maximizing relaxation has `Q/D=0`; positive exceptional-face density cannot rescue the low-surplus branch.

## 4. Full-source lower gap and the one-variable necessary condition

FSDB gives, for

```math
\Phi(y):=\frac{y+\sin y}{4},
```

```math
\liminf\frac{area(F)}{D^2}\ge\Phi(y).
```

GU bounds the attachment-cell area by `(pi/4)L^2+o(D^2)`, hence

```math
\boxed{
\liminf\frac G{D^2}
\ge
\Phi(y)-\frac\pi4\lambda^2.
}
\tag{4.1}
```

This is where the **whole global source**, including contact-isolated points, enters the proof through FSDB's full-source circumradius transport and the global-minimum comparison behind it.

Equations 3.9 and 4.1 force every survivor limit to satisfy

```math
\boxed{
\Phi(y)-\frac\pi4\lambda^2
\le
\frac1{\sqrt6}
\lambda^{3/2}\sqrt{\min\{\lambda,g(y)\}},
\qquad
2\rho\le y\le\pi.
}
\tag{4.2}
```

This is the new post-ZF feasible-region inequality.

## 5. Exact optimization and the new surplus floor

FSJC already proves

```math
\lambda\ge\lambda_{FSJC}=0.5882283437\ldots>0.58.
\tag{5.1}
```

For completeness, the strict `>0.58` follows directly from the exact FSJC quadratic. At `lambda=29/50`, its left side is

```math
\frac{54}{625}\pi^2-rac{21}{50}\pi+rac{841}{2500}<0
```

using `pi<22/7` and `pi>3.14`; the resulting upper estimate is `-158/1225`.

Fix `lambda>=0.58`. Since `g'(y)=1+sin(y/2)>0`, there is a unique `y_lambda` with

```math
g(y_\lambda)=\lambda
```

for every `lambda<pi`.

### Lemma 5.1 — the detour branch decreases up to the crossover

On `g(y)<=lambda`, define

```math
J(y)=\Phi(y)-C\lambda^{3/2}\sqrt{g(y)}.
```

A derivative calculation gives

```math
J'(y)\le0
\iff
\sqrt{g(y)}\bigl(1-\sin(y/2)\bigr)
\le C\lambda^{3/2}.
\tag{5.2}
```

The left side has a uniform elementary bound below `0.171`. To prove it, put `t=y/2` and

```math
R(t)=\sqrt{2(t-\cos t)}(1-\sin t),
\qquad \rho\le t\le\pi/2.
```

At the endpoints `R=0`. On the interior the sign of `R'` is the sign of

```math
3\cos t-2t,
```

which is strictly decreasing. Hence there is a unique maximizer `t_0`, satisfying

```math
3\cos t_0=2t_0.
```

Using the alternating Taylor upper bound

```math
\cos(0.93)\le1-0.93^2/2+0.93^4/24<0.62
```

shows `3cos(0.93)<2(0.93)`, so `t_0<0.93`. At the critical point set `c=cos t_0=2t_0/3<0.62`. Then `g(2t_0)=c`, so

```math
R(t_0)=\sqrt c\left(1-\sqrt{1-c^2}\right).
```

This expression increases with `c in (0,1)`. Since

```math
\sqrt{0.62}<0.788,
\qquad
\sqrt{1-0.62^2}=\sqrt{0.6156}>0.784,
```

we obtain

```math
R(t_0)<0.788(1-0.784)=0.170208<0.171.
\tag{5.3}
```

On the other hand, for `lambda>=0.58`,

```math
C\lambda^{3/2}
\ge C(0.58)^{3/2}>0.171,
```

because after squaring the last inequality reduces exactly to

```math
\frac{(29/50)^3}{6}-\left(\frac{171}{1000}\right)^2
=rac{9833}{3000000}>0.
```

Thus `J'(y)<0` throughout the detour branch.

### Lemma 5.2 — the chord-floor branch increases after the crossover

On `g(y)>=lambda`, the right side of 4.2 is simply `C lambda^2`, independent of `y`, while

```math
\Phi'(y)=\frac{1+\cos y}{4}\ge0.
```

Thus the gap between the two sides of 4.2 increases after `y_lambda`.

Lemmas 5.1-5.2 prove that for every fixed `lambda>=0.58`, the easiest point at which 4.2 can hold is exactly

```math
\boxed{g(y_\lambda)=\lambda.}
\tag{5.4}
```

At that crossover, 4.2 becomes

```math
\boxed{
\Phi(y_\lambda)
\le
\left(\frac\pi4+\frac1{\sqrt6}\right)\lambda^2.
}
\tag{5.5}
```

Define

```math
A:=\frac\pi4+\frac1{\sqrt6}
```

and

```math
K(\lambda):=\Phi(g^{-1}(\lambda))-A\lambda^2.
```

Differentiating through `g(y_lambda)=lambda` gives the exact simplification

```math
\frac{d}{d\lambda}\Phi(y_\lambda)
=
\frac{\Phi'(y_\lambda)}{g'(y_\lambda)}
=
\frac{1-\sin(y_\lambda/2)}2.
```

Hence

```math
K'(\lambda)
=
\frac{1-\sin(y_\lambda/2)}2-2A\lambda
<\frac12-2\frac34(0.58)<0
\tag{5.6}
```

for `lambda>=0.58`. Thus `K` is strictly decreasing in the entire relevant range.

Moreover `K(0.58)>0`: `Phi(y)>=Phi(2rho)>0.575`, while `A<101/84` and `(0.58)^2<0.337`, so `A(0.58)^2<0.406`. Also `K(1)<0` because `Phi<=pi/4<A`. Therefore there is a unique

```math
\boxed{\lambda_{DPH}\in(0.58,1)}
```

with `K(lambda_DPH)=0`.

Equivalently, if `y_*` is the unique solution in `(2rho,pi)` of

```math
\boxed{
\frac{y_*+\sin y_*}{4}
=
\left(\frac\pi4+\frac1{\sqrt6}\right)
\left(y_*-2\cos(y_*/2)\right)^2,
}
\tag{5.7}
```

then

```math
\boxed{
\lambda_{DPH}=y_*-2\cos(y_*/2).
}
\tag{5.8}
```

Numerically,

```math
y_*=1.9205467456885863\ldots,
```

```math
\boxed{
\lambda_{DPH}=0.7739547058568927\ldots .
}
\tag{5.9}
```

Since 4.2 is impossible for every `lambda<lambda_DPH`, every post-ZF survivor sequence obeys

```math
\boxed{
\liminf_{D\to\infty}
\frac{e_{BB}+2s_C}{D}
\ge
0.7739547058568927\ldots .
}
\tag{DPH.1}
```

This proves the claimed new floor.

## 6. Endpoint stability

The proof gives more than the scalar constant. If a survivor sequence approaches the new endpoint,

```math
\frac{e_{BB}+2s_C}{D}\to\lambda_{DPH},
```

then every relaxed inequality above must be asymptotically sharp. In particular:

1. `h/D -> y_*`;
2. `Q/D -> 0`, because the exceptional-face relaxation is strict for positive normalized `Q`;
3. `d_P/D -> lambda_DPH` and `e_BB/D -> lambda_DPH`;
4. `s_C/D ->0`;
5. from PC.2,
   ```math
   d_H/D\to0,\qquad s_Z/D\to0,\qquad c_B/D\to0;
   
   ```
6. the DPC concentration step forces one outer pocket to carry asymptotically all `d_P`: if `M=max_P x_P`, then
   ```math
   M/D\to\lambda_{DPH},
   
   ```
   because `sum x_P^2<=M d_P` and equality in the quadratic leading term forces `M/d_P->1`.

The last point gives a macroscopic outer-pocket contact chain. It is a useful structural target for the next run, but no contradiction from it is claimed here.

## 7. Exact target implication

Before this run, the strongest full-source C-II cavity theorem gave

```math
\liminf (e_{BB}+2s_C)/D\ge0.5882283437\ldots .
```

DPC/DPH replaces that report-level endpoint by

```math
\boxed{
\liminf (e_{BB}+2s_C)/D\ge0.7739547058\ldots .
}
```

The improvement is not a scalar iteration of JC. It comes from a new finite geometric theorem, DPC.1-DPC.3, that uses the integer unit-edge structure and the unit lower bound on every missing force-hull side.

The shortest remaining implication is now:

```math
\boxed{
\text{derive a universal C-II upper bound on }(e_{BB}+2s_C)/D
\text{ below }\lambda_{DPH},
}
```

or exclude the DPH endpoint/high-surplus geometry directly by FS.4 common-center symmetry, diameter-thrackle structure, or an exact smaller-diameter rearrangement.

## 8. Audit classification of other claims

| Claim | Classification | Reason |
| --- | --- | --- |
| DPC.1 discrete one-pocket bound | proved | exact discrete Green function + unit-edge transverse energy |
| DPC.9 global detour form | proved | Cauchy + exact convex concentration polynomial |
| DPC.13 chord-floor form | proved | every missing hull side has length `>1` |
| hybrid cavity ceiling 3.9 | proved asymptotically | DPC + PC + DB + exceptional-face bound, with `Q` optimized analytically |
| crossover optimization | proved | monotonicity on both sides of `g(y)=lambda` |
| `lambda_DPH=0.773954...` floor | proved asymptotically | unique root of the explicit monotone scalar equation |
| DPH endpoint has one macroscopic excess pocket | proved as an endpoint-stability consequence | equality in `sum x_P^2<=d_P^2` |
| FS.4 forces a second macroscopic pocket | not proved | approximate central symmetry need not preserve finite edge subdivision |
| universal upper bound below `lambda_DPH` | not proved | remains the main closure gap |
| Level I | still open | high-surplus C-II sources are not yet excluded |

## 9. Regression tests

| Regression | Passed? | Exact reason |
| --- | --- | --- |
| regular odd shell | yes | DPC upper geometry is compatible; the decisive FSDB/GU lower gap uses global minimum-diameter source information that a large odd shell lacks |
| dense isolated fillings | yes | isolates never enter DPC, but are retained in the FSDB full-source lower bound; artificial fillings still lack a global-optimality certificate |
| many thin triangular pockets | yes | `x_P=0`; each contributes only the explicit `O(1)` term in DPC.13, hence `O(D)` total |
| one giant outer pocket | yes | DPC.9/DPC.13 deliberately allow concentration into one macroscopic pocket; endpoint stability identifies this as the extremal pattern rather than assuming it away |
| positive exceptional-face density | yes | its `Q^2/(4pi)` capacity is included and is proved unable to beat the `Q=0` relaxation |
| odd-shell response trace defect | yes | no operator-norm or small-trace inference is used |

The decisive use of information absent from the shell regressions is the FSDB/GU lower gap: it is derived from the **entire globally minimizing source**, including isolates, via the full-source circumradius/global comparison. DPC itself is only the geometric upper half of the argument.

## 10. Failed routes and no-go results

1. **Near-central-symmetry immediately duplicates the giant pocket.** FS.4 gives Hausdorff central symmetry of the normalized force hull, but a macroscopic side on one side may converge to an opposite flat segment subdivided into many finite hull sides. No theorem currently turns that opposite segment into a second macroscopic OP pocket. This implication is therefore not used.
2. **Force-hull near-perimeter equality alone closes C-II.** False as a principle; constant-width and shell-type regressions survive. DPH uses the full DB detour and pocket ledgers instead.
3. **Linear strict response-minor count supplies a numerical trace gap.** Still unavailable; positivity without magnitude remains insufficient.

## 11. Literature imported

No external theorem is imported into the proof. A web search located secondary summaries of the classical characterization of planar diameter graphs/straight convex thrackles as caterpillars or an odd cycle with pendant edges. That lead was not used because this report did not verify a primary-source theorem statement with the exact hypotheses needed for the DPH proof.

## 12. Computation and reproducibility

Only the decimal evaluation of the uniquely defined root in 5.7-5.8 uses computation. The proof of existence, uniqueness, and the lower bound is analytic.

A standard-library bisection check can evaluate the displayed decimal by solving 5.7 on `[2rho,pi]` after solving `rho=cos rho`. No floating-point value is used to establish a sign needed by the proof; all proof-critical sign estimates in Lemma 5.1 are given by explicit rational inequalities.

## 13. Canonical promotion recommendation

**Hold as report pending independent audit.** DPC.1-DPC.3 are finite exact results and are candidates for promotion. DPH.1 also appears promotable if the report-level PC/DB/FSDB/GU/ZG dependencies survive independent review.

If promoted, update:

- the Target C route map with DPC/DPH;
- the active Target C continuation prompt, replacing `0.588228...` as the best report-level full-source surplus floor;
- `research/README.md` only if a durable root-check script is added.

## 14. Next run

The highest-value next theorem is a structural exclusion of the DPH endpoint/high-surplus regime.

The endpoint already forces one macroscopic outer pocket together with `Q,s_Z,d_H,c_B,s_C=o(D)`. Two concrete routes remain live:

1. combine the macroscopic pocket with FS.4 common-center Hausdorff symmetry and prove that the opposite support segment must carry enough independent pocket-degree mass to violate the one-pocket concentration required by DPH equality;
2. use the near-equality diameter graph (`q-h=o(D)` at any endpoint where `d_H=o(D)`) together with the classical diameter-thrackle caterpillar/odd-cycle structure, but only after checking a primary source and deriving a quantitative stability statement rather than a qualitative equality classification.

## 15. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Strongest new theorem:
For one OP pocket with ell unit contact edges and missing force-hull chord length s,
    area(P)^2 <= ((ell^3-ell)/6)(ell-s).
Writing x_P=ell_P-2 and d_P=sum x_P gives
    H_out^2 <= [(d_P^3+6d_P^2+11d_P+6a)/6](b-P_F),
and since every missing hull side has s_P>1,
    H_out < (1/sqrt6)(d_P^2+(7/2)d_P+(5/2)a).

With PC + DB + FSDB/GU/ZG, every survivor limit (lambda,y) satisfies
    Phi(y)-pi lambda^2/4
      <= (1/sqrt6) lambda^(3/2) sqrt(min(lambda,g(y))),
    Phi(y)=(y+sin y)/4,
    g(y)=y-2cos(y/2),
    y>=2rho, rho=cos rho.
For lambda>0.58 the weakest y is exactly g(y)=lambda.
The unique root is
    lambda_DPH=0.7739547058568927...,
so
    liminf (e_BB+2s_C)/D >= lambda_DPH.

Endpoint stability:
    h/D -> y_*=1.9205467456885863...,
    Q,s_Z,d_H,c_B,s_C=o(D),
    d_P/D,e_BB/D -> lambda_DPH,
and one OP pocket carries x_P=lambda_DPH D+o(D).

Exact endpoint now:
Exclude the high-surplus DPH geometry, or prove a universal upper bound
    limsup (e_BB+2s_C)/D < lambda_DPH.

Binding regressions:
odd shells, dense isolated fillings, near-chain local stars, and response-minor
positivity without magnitude. Global optimality enters only through FSDB/GU.

Authoritative starting files:
docs/targets/target-c/56-ci-restored-frontier.md
docs/targets/target-c/01-force-hull-and-shear.md
docs/reports/target_c_full_source_circumradius_response_2026-09-10.md
docs/reports/target_c_fs_symmetric_difference_body_area_2026-09-10.md
docs/reports/target_c_post_zf_difference_body_perimeter_2026-09-09.md
docs/reports/target_c_outer_pocket_internal_chord_ledger_2026-09-09.md
docs/reports/target_c_outer_pocket_dirichlet_dual_detour_2026-09-09.md
```
