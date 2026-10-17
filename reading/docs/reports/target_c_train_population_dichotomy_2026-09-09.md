> Generated reading edition · [exact source](../../../docs/reports/target_c_train_population_dichotomy_2026-09-09.md) · source SHA-256 `a0dac7c415690f3afb9069edc007c49457e1b74977ba19757be243f5191fa236`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Presentation repairs: 4 exact-source-bound TeX/escape correction(s); [reviewed repair ledger](../../../docs/publication/reading-tex-repairs.json). Frozen source bytes are unchanged.

<!-- theorem-state: {"artifact_id":"ART-D746BB355615","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — train/perimeter core-population dichotomy

**Date:** 2026-09-09  
**Repository state:** `be9cbfb78cbda059fb4c2581118b236729cfad84`, combined with the report-level clean-train/diameter-direction bounds on `research/zd-clean-train-shape-2026-09-09`  
**Run type:** exact consequence / source-population phase reduction  
**Target:** Target C Gate C-II / post-ZF Z route  
**External web search:** not used  
**Computation:** used only to quote numerical roots; proofs are analytic

## LEVEL I STATUS

`STILL OPEN`

This note derives a quantitative source-population consequence from the new diameter-direction perimeter theorem. It does not assume away contact-isolated source points. Instead, it proves that a post-ZF survivor with insufficiently many diameter edges must contain a positive **quadratic** density of such points.

The converse dense-core phase is also sharpened: if the nonisolated core contains all but `o(D^2)` source points, the existing DF theorem plus round-hull convergence forces a substantially larger diameter-edge density.

The resulting split is exact enough to remove a broad intermediate heuristic: the rattler population is now quantitatively coupled to `h/D`.

## 1. Setup

Use the post-ZF notation:

- `D=D(n)`;
- `v` = number of nonisolated contact-core vertices;
- `R` = number of bounded quadrilateral contact faces;
- `f` = number of bounded nonquadrilateral contact faces;
- `b` = outer contact-face walk length;
- `Q=sum_F(deg F-4)` over bounded nonquadrilateral faces;
- `T` = stopped-train count;
- `h` = number of actual diameter pairs;
- `F` = convex hull of the loaded/nonisolated diameter endpoints.

DT gives

```math
T=\frac{b+Q}{2}+2f,
\tag{1.1}
```

and Euler gives

```math
R=v+f-T-1.
\tag{1.2}
```

ZF gives

```math
b+Q\le2h.
\tag{1.3}
```

Every bounded nonquadrilateral face has degree at least five, so

```math
f\le Q.
\tag{1.4}
```

The distinguished outer-walk decomposition gives

```math
b\ge \operatorname{per}(F).
\tag{1.5}
```

Finally the diameter-direction perimeter theorem from the companion report gives, with

```math
a_D:=\arcsin\frac1{2D},
```

```math
\operatorname{per}(F)
\ge
(h-1)+2D\cos((h-1)a_D).
\tag{1.6}
```

## 2. Exact train-count upper bound from diameter support

### Theorem ZP.1

Every post-ZF survivor satisfies

```math
\boxed{
T\le5h-2\operatorname{per}(F).
}
\tag{ZP.1}
```

Consequently

```math
\boxed{
T\le
3h+2-4D\cos((h-1)a_D).
}
\tag{ZP.2}
```

### Proof

From (1.1), (1.3), and `f<=Q`,

```math
T
=\frac{b+Q}{2}+2f
\le h+2Q.
```

Equation (1.3) also gives

```math
Q\le2h-b.
```

Hence

```math
T\le h+2(2h-b)=5h-2b
\le5h-2\operatorname{per}(F),
```

proving ZP.1. Substitute (1.6):

```math
T
\le5h-2(h-1)-4D\cos((h-1)a_D),
```

which is ZP.2. QED.

The bound is finite and retains every exceptional-face and bridge term through the inequalities above. It does not use a dense-core assumption.

## 3. Exact core-population upper bound

DT proves that the train-crossing graph is simple and triangle-free, with `T` vertices and `R` edges. Mantel therefore gives

```math
R\le\frac{T^2}{4}.
\tag{3.1}
```

Euler (1.2) gives

```math
v=R-f+T+1\le R+T+1.
```

Thus:

### Theorem ZP.2

Every post-ZF survivor satisfies

```math
\boxed{
v\le\frac{T^2}{4}+T+1.}
\tag{ZP.3}
```

Combining with ZP.2 gives the explicit finite estimate

```math
\boxed{
 v\le
 \frac14 U_D(h)^2+U_D(h)+1,
}
\tag{ZP.4}
```

where

```math
\boxed{
U_D(h):=3h+2-4D\cos((h-1)\arcsin(1/(2D))).
}
\tag{ZP.5}
```

The estimate is useful precisely because `v`, not the full source cardinality `n`, appears on the left. Contact-isolated points are retained as the complementary population `n-v`.

## 4. Asymptotic rattler-density theorem

The standard global packing bounds give

```math
\frac{n}{D^2}\longrightarrow
\Delta:=\frac{\pi}{2\sqrt3}.
\tag{4.1}
```

Consider any subsequence for which

```math
\frac hD\longrightarrow x.
\tag{4.2}
```

The diameter-direction packing has `h=O(D)`, and the post-ZF theorem gives `x>=tau_*`, where

```math
\tau_*=1.4781702664\ldots
```

is the root of `tau=2cos(tau/2)`.

Since

```math
D\arcsin\frac1{2D}\longrightarrow\frac12,
```

ZP.2 yields

```math
\limsup\frac TD
\le
A(x):=3x-4\cos\frac x2.
\tag{4.3}
```

Therefore ZP.3 gives

```math
\boxed{
\limsup\frac v{D^2}
\le
\frac14\left(3x-4\cos\frac x2\right)^2.
}
\tag{ZP.6}
```

Subtract from (4.1):

### Corollary ZP.3 — quantitative inactive-population floor

Along every subsequence with `h/D->x`,

```math
\boxed{
\liminf\frac{n-v}{D^2}
\ge
\Delta-\frac14\left(3x-4\cos\frac x2\right)^2.
}
\tag{ZP.7}
```

whenever the displayed right side is positive.

Let `x_0` be the unique root above `tau_*` of

```math
3x-4\cos\frac x2=2\sqrt\Delta.
\tag{4.4}
```

Numerically,

```math
\boxed{x_0=1.5754757611\ldots .}
\tag{ZP.8}
```

Thus every hypothetical sequence with

```math
\limsup\frac hD<x_0
```

has a **positive quadratic density** of contact-isolated source points.

At the smallest diameter-edge density allowed by the new perimeter bootstrap, `x=tau_*`, the explicit lower coefficient is

```math
\boxed{
\Delta-\frac14A(\tau_*)^2
=0.3606528479\ldots .
}
\tag{ZP.9}
```

So a survivor near the new `h/D` endpoint would have at least about `0.36065 D^2` contact-isolated source points. This is not an `O(D)` bookkeeping effect.

## 5. The dense-core branch forces larger diameter-edge density

Now impose the existing DF hypothesis

```math
n-v=o(D^2).
\tag{5.1}
```

The reviewed proof of DF establishes two facts in this branch:

1. after scaling by `D`, the force/contact-core hull converges to the disk of diameter one, hence
   
   ```math
   \frac{\operatorname{per}(F)}D\longrightarrow\pi;
   \tag{5.2}
   ```

2. the exceptional-face count obeys
   
   ```math
   \liminf\frac fD
   \ge
   \kappa,
   \qquad
   \kappa:=
   \sqrt\Delta-\frac\pi4
   =0.166914643466509\ldots .
   \tag{5.3}
   ```


Since `Q>=f`, `b>=per(F)`, and a ZF survivor has `b+Q<=2h`,

```math
\frac{2h}{D}
\ge
\frac{b}{D}+\frac{Q}{D}
\ge
\frac{\operatorname{per}(F)}D+\frac fD.
```

Take lower limits.

### Theorem ZP.4 — dense-core diameter-edge floor

Every post-ZF sequence with `n-v=o(D^2)` satisfies

```math
\boxed{
\liminf\frac hD
\ge
\frac\pi2+\frac12
\left(\sqrt\Delta-\frac\pi4\right)
=1.6542536485\ldots .
}
\tag{ZP.10}
```

The same lower bound holds for `q/D`, because `q>=h`.

This is strictly stronger than both the general perimeter endpoint `tau_*=1.47817...` and the rattler-threshold root `x_0=1.57548...`.

## 6. Resulting phase split

The post-ZF source population is now constrained as follows.

- **Low diameter-edge phase:** if `h/D` stays below `x_0=1.5754757611...`, then `n-v` is necessarily `Theta(D^2)` from below, with the explicit coefficient in ZP.7.
- **Asymptotically full-core phase:** if `n-v=o(D^2)`, then `h/D` is at least `1.6542536485...`.
- **Intermediate/high phase:** the current theorems do not exclude quadratic rattlers when `h/D>=x_0`, nor do they prove a dense core. This remains a genuine branch rather than being silently discarded.

The gap between `x_0` and the dense-core floor is not a contradiction: the hypotheses of the two statements differ. It identifies the next useful interface theorem: any improvement that upper-bounds the inactive population from global capacity can be converted immediately into an improved lower bound on `h/D` through ZP.7.

## 7. Relation to the exact post-ZF ledgers

The exact ZE/ZT ledger on current main writes

```math
q=x_B+f+g_F+2d_H+2s_Z,
```

and

```math
T-q=2q-2x_B-2g_F-5(d_H+s_Z).
```

ZP does not replace these identities. It supplies an independent **metric upper bound** on `T` in terms of the actual diameter-direction support. Combining the exact ledger with ZP is therefore a plausible next route for controlling `s_Z`: equality or near equality in ZP forces simultaneous near equality in

```math
f\le Q,
\qquad
Q\le2h-b,
\qquad
b\ge\operatorname{per}(F),
\qquad
R\le T^2/4.
```

That is a much narrower equality regime than the raw exact ledger.

## 8. Regression audit

### Regular odd shell plus a large inactive filling

This is deliberately not excluded by ZP. A shell can have a linear contact core and a quadratic strict interior population. ZP classifies it in the quadratic-inactive branch. Exact global optimality is still missing for such constructions.

### Pure/dense rhombic core

The dense-core branch is retained and receives the stronger `h/D` floor ZP.10. ZP does not replace ZB or DF.

### Contact-isolated heptagon center

The `n=8` heptagon-center witness is consistent: ZP never declares isolated points to be diameter endpoints or members of `v`.

### Five-sector and DP regressions

No uniform local Oler charge is introduced. The argument uses only exact train counts, Mantel, the global diameter-direction perimeter bound, and the already-audited DF conclusion under its explicit population hypothesis.

## 9. Exact remaining theorem

The direct Level I endpoint remains

```math
\boxed{b+Q>2h.}
```

Equivalently, in the exact post-ZF ledger, one must rule out `s_Z>=0`.

ZP identifies a second, source-population-oriented route:

> prove a sufficiently strong upper bound on `n-v` for a global triangle-free minimizer as a function of the outer-face/force-hull geometry, then feed it through ZP.7 until the resulting mandatory `h/D` is incompatible with the diameter graph / face ledger.

The existing force-bulk localization does not supply such an upper bound; the old claim that every isolated point is diametral remains rejected.

## 10. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

ZP exact train bound:
    T <= 5h - 2 per(F)
      <= 3h+2 - 4D cos((h-1) asin(1/(2D))).

Mantel + Euler:
    v <= T^2/4 + T + 1.

If h/D -> x:
    limsup v/D^2 <= (3x-4cos(x/2))^2/4,
    liminf (n-v)/D^2 >= Delta-(3x-4cos(x/2))^2/4.

The inactive-population lower bound is positive for
    x < x_0 = 1.5754757611...
where
    3x_0-4cos(x_0/2)=2sqrt(Delta).
At the general post-ZF endpoint tau_*=1.4781702664..., it is at least
    0.3606528479... D^2.

If instead n-v=o(D^2), DF gives per(F)/D->pi and
    liminf f/D >= sqrt(Delta)-pi/4.
Therefore
    liminf h/D >= 1.6542536485...

Exact Level I endpoint remains:
    b+Q>2h
or equivalently exclude s_Z>=0.
```
