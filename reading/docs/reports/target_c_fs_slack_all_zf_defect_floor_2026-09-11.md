> Generated reading edition · [exact source](../../../docs/reports/target_c_fs_slack_all_zf_defect_floor_2026-09-11.md) · source SHA-256 `28ba8c124e6b140750846e4151faadfd3bf7d70638e78161a3a7e3792ae5ebf1`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-16019D53344E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_fs_slack_all_zf_defect_floor_2026-09-11.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=09fd2aff25e9fdd7a4845d0a36f48b55e04d2589; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — full-source slack raises the all-ZF defect floor

**Date:** 2026-09-11  
**Run type:** exact branch exclusion / Oler-slack and train-capacity synthesis  
**Target:** Target C C-II, including `s_Z>0` and contact isolates  
**Status:** report-level conditional theorem; no route-map promotion

## LEVEL I STATUS

`STILL OPEN`.

Combining the all-branch full-source cell-slack identity with the finite stopped-train
Mantel bound gives a stronger form of the preceding low-defect result. Conditional
on the audited FSDB area floor and the full-source slack theorem, every unbounded
post-ZF C-II sequence satisfies

```math
\boxed{\liminf_{D\to\infty}(x_B+Q)/D\ge\varepsilon_* > 0.0476.}
\tag{S.1}
```

Here `\varepsilon_*` is the positive root of

```math
\frac{\sqrt3}{8}\left(\frac\pi2+\frac52\varepsilon\right)^2
 +\frac{\varepsilon^2}{4\pi}=A_{FS},
\qquad A_{FS}=\frac{2\rho+\sin(2\rho)}4,\quad \rho=\cos\rho.
\tag{S.2}
```

Numerically, `\varepsilon_*=0.0476412815054\ldots`. The numerical value is not
needed: (S.2) defines a strictly positive constant because
`A_{FS}>\pi^2/16`.

The theorem excludes `x_B+Q=o(D)` in all three branches and also excludes the
entire interval below the displayed positive linear threshold. It still leaves the
linear-defect regime and does not settle Level I.

There is a useful population-spanning refinement. If the nonisolated core has
`v/D^2\to\Delta_2=\pi/(2\sqrt3)`, Eppstein's sharp triangle-free penny-graph
deficit and the exact definition of `s_Z` give `h/D\ge\pi/2-o(1)`. FSDB then
raises the area floor to

```math
A_{\rm span}=\frac{\pi/2+1}{4}.
\tag{S.3}
```

The same proof gives
`\liminf(x_B+Q)/D\ge\varepsilon_{\rm span}`, where
`U(\varepsilon_{\rm span})=A_{\rm span}` and
`\varepsilon_{\rm span}=0.0606976679\ldots`. Thus an isolate-subquadratic
sequence cannot approach even the lower defect endpoint (S.3 is a conditional
corollary of the unpromoted Eppstein/FSDB inputs).

For completeness, the endpoint optimization remains valid on this larger root
range: `U(1/10)>A_{\rm span}` by direct use of `a_0>0.866` and `\pi>3.14`, while
the difference (S.13) is positive for `r\le1/10` because its factored bracket is
greater than `1-3/10`.

## 1. Inputs and exact contradiction target

Let `F` be the actual force hull, `R` the number of bounded quadrilateral contact
faces, `f` the number of exceptional bounded faces, and `x=x_B`. Put

```math
Q=\sum_i(\deg F_i-4),\qquad a_0=\frac{\sqrt3}{2}.
```

The two report-level inputs are: FSDB, `\liminf area(F)/D^2\ge A_{FS}`; and FSCS,
the total quadrilateral area is `a_0R+O(D)` uniformly in C-II, including repeated
outer walks, both diameter topologies, arbitrary `s_Z`, and all contact-isolated
source points. The target contradiction is `\limsup area(F)/D^2<A_{FS}`.

## 2. Proof of the defect floor

Take any subsequence and, after a further extraction, suppose

```math
X:=\lim x/D,\qquad Y:=\lim Q/D,qquad r:=X+Y<\infty.
\tag{S.4}
```

The exact all-ZF identities are

```math
q=x+Q+2(d_H+s_Z),\qquad T=q-(d_H+s_Z)+2f.
\tag{S.5}
```

Since `f\le Q` and `q\le\operatorname{per}F\le\pi D`,

```math
\limsup T/D\le\frac\pi2+\frac X2+\frac52Y.
\tag{S.6}
```

The actual train-crossing graph is simple and triangle-free, so Mantel gives
`R\le T^2/4`. FSCS therefore gives

```math
\limsup\frac{a_0R+O(D)}{D^2}
\le\frac{a_0}{4}\left(\frac\pi2+\frac X2+\frac52Y\right)^2.
\tag{S.7}
```

The outer-pocket sum satisfies `\sum_P k_P=x+2a\le3x`, where `a\le x` is the
number of missing force-hull sides. Hence

```math
\limsup A_{out}/D^2\le9X^2/\pi.
\tag{S.8}
```

For exceptional faces, the exact degree-defect estimate gives

```math
\limsup A_{exc}/D^2\le Y^2/(4\pi).
\tag{S.9}
```

The augmented contact subdivision partitions `F` into these three classes. Thus

```math
\limsup area(F)/D^2\le V(X,Y),
\quad V(X,Y)=\frac{a_0}{4}\left(\frac\pi2+\frac X2+\frac52Y\right)^2
 +\frac{9X^2}{\pi}+\frac{Y^2}{4\pi}.
\tag{S.10}
```

At fixed `r=X+Y`, the function `X\mapsto V(X,r-X)` is convex, so its maximum is
at an endpoint. The endpoint values are

```math
V(r,0)=\frac{a_0}{4}\left(\frac\pi2+\frac r2\right)^2+\frac{9r^2}{\pi},
\tag{S.11}
```

and

```math
V(0,r)=\frac{a_0}{4}\left(\frac\pi2+\frac{5r}{2}\right)^2+\frac{r^2}{4\pi}=:U(r).
\tag{S.12}
```

The root of `U(r)=A_{FS}` is less than `1/20`. Indeed `\rho<37/50` and
`\sin(2\rho)<1` give `A_{FS}<0.62`, while `a_0>0.866`, `\pi>3.14` give
`U(1/20)>0.622`. For `0\le r\le1/20`, `V(0,r)\ge V(r,0)`: their difference is

```math
\frac{a_0\pi}{2}r+\left(\frac{3a_0}{2}-\frac{35}{4\pi}\right)r^2>0.
\tag{S.13}
```

The difference is positive on this interval: `a_0\pi/2>1` and its quadratic
coefficient is greater than `-3`, so after factoring out `r` the bracket is
greater than `1-3/20>0`. Also `U` is strictly increasing and
`U(0)=a_0\pi^2/16<A_{FS}`. Let `\varepsilon_*` be the unique positive root of
`U(\varepsilon_*)=A_{FS}`. If `r<\varepsilon_*`, (S.10)--(S.13) contradict
FSDB. Consequently every finite subsequential limit of `(x+Q)/D` is at least
`\varepsilon_*`; an unbounded ratio causes no issue. This proves (S.1). `\square`

## 3. Why the result covers `s_Z>0`

No circuit identity with `s_Z=0` is used. From (S.5), increasing `s_Z` increases
`q` and decreases the train count in precisely the combination giving (S.6). The
cyclic/forest diameter-topology dichotomy is therefore irrelevant here. This is an
all-branch statement, not a cyclic reduction.

Contact-isolated source points are retained through FSDB and FSCS; no isolate is
assumed to lie in the force hull.

The same calculation gives a useful three-parameter necessary inequality. If along
a subsequence

```math
v/D^2\to\nu,\qquad s_Z/D\to\sigma,
```

then Eppstein's edge deficit and `s_Z=e+h-(2v-2)` imply

```math
\liminf h/D\ge\sigma+c_E\sqrt\nu,
\qquad c_E=\frac12\sqrt{2\pi\sqrt3}.
\tag{S.14}
```

Since `y\mapsto(y+\sin y)/4` is increasing on `[0,\pi]`, FSDB and (S.10) give

```math
\boxed{
\frac{\sigma+c_E\sqrt\nu+\sin(\sigma+c_E\sqrt\nu)}4
\le V(X,Y),
}
\tag{S.15}
```

whenever the left argument is at most `\pi`; if it exceeds `\pi`, the branch is
already impossible because `h\le q\le\pi D`. In particular, for a
population-spanning core `\nu=\Delta_2`, one has `c_E\sqrt{\Delta_2}=\pi/2`,
which yields the refinement (S.3) and forces
`(x_B+Q)/D\ge0.0606976\ldots`. Thus the remaining low-defect escape in (S.1) is
necessarily isolate-heavy or carries a larger face/outer defect.

## 4. Regression audit and exact scope

| Regression | Treatment |
|---|---|
| odd shell with `s_Z=2` | retained; it has linear `x+Q` and is not claimed excluded |
| `s_Z>0` | retained in (S.5) |
| contact isolates | retained by FSDB/FSCS full-source bookkeeping |
| repeated outer edges | counted by `x` and `\sum k_P=x+2a` |
| one giant exceptional face | charged by `Y^2/(4\pi)` |
| near-equilateral rhombi | FSCS retains their possible vanishing slack |
| forest component count | no sublinear-component assumption |

FSDB and FSCS are unpromoted reports. This report is consequently conditional and
must not be promoted automatically.

## 5. Exact surviving obstruction

The survivors obey at least

```math
x_B+Q\ge(0.0476412\ldots-o(1))D,
```

as well as the independent linear ledgers involving `e_{BB}`, `s_C`, `d_H`, and
`s_Z`. Current theory has no opposing upper bound on the linear area capacity
supplied by this defect and no globally admissible deletion/shear removing it while
preserving all diameter inequalities. Thus this theorem narrows C-II but does not
settle Erdős #99.
