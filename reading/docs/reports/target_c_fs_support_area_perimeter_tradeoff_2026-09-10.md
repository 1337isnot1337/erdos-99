> Generated reading edition · [exact source](../../../docs/reports/target_c_fs_support_area_perimeter_tradeoff_2026-09-10.md) · source SHA-256 `5c7e29a634bec6030dff62251414fbe0e532ab4416b2b72fa7cd71ab2b31efd0`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-CB2830F96972","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_fs_support_area_perimeter_tradeoff_2026-09-10.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=858e6489b3ca9de69abab8e69fbb041bcebbee14; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — support triangulation strengthens the FS perimeter/area tradeoff

**Date:** 2026-09-10  
**Branch base:** `f977f2d0d25f5022c2a587e59cab38375d85caee`  
**Depends on:** FD and QPA on this branch  
**Run type:** exact convex-geometric strengthening  
**Target:** Target C, C-II after ZF  
**External input:** none

## LEVEL I STATUS

`STILL OPEN`.

QPA converts the actual normalized force-hull perimeter into a lower bound for the
centered inradius of the central symmetral.  The strongest simple use of that inradius
is not the inball area and not the QPD inball-plus-diameter hull.  Because the
symmetral is a polygon, triangulation from its center gives

```math
\operatorname{area}S\ge\frac12r\operatorname{per}S.
```

This yields a strictly stronger perimeter-dependent area function throughout the
interior `2<p<pi`.

Retain

```math
f(a)=2\left(\arcsin a+\sqrt{1-a^2}\right),
\qquad
\alpha=f^{-1}:[2,\pi]\to[0,1]
\tag{SA.1}
```

from QPA.  Define

```math
\boxed{
\Xi(p):=\frac{p\,\alpha(p)}4,
\qquad 2\le p\le\pi.
}
\tag{SA.2}
```

Then for the actual force hull `F`, with `P=per(F)`, FD's error term gives

```math
\boxed{
\operatorname{area}F
\ge
D^2\Xi(P/D)-L_DP-\pi L_D^2.
}
\tag{SA.3}
```

Consequently, if `P/D->p`,

```math
\boxed{
\liminf\frac{\operatorname{area}F}{D^2}\ge\Xi(p).
}
\tag{SA.4}
```

Moreover

```math
\boxed{
\Xi(p)>\Omega(p)>\Psi(p)
\qquad(2<p<\pi),
}
\tag{SA.5}
```

where `Omega` is QPD and `Psi` is QPA.

---

## 1. Support triangulation

Let `K` be a centrally symmetric convex polygon centered at the origin.  Let

```math
r:=\min_{|u|=1}h_K(u).
\tag{1.1}
```

Thus every supporting line of `K` is at distance at least `r` from the origin.
Write the side lengths of `K` as `ell_1,...,ell_N`, and let `d_i` be the distance from
the origin to the supporting line containing side `i`.  Convexity and centrality place
the origin in `K`, so triangulation from the origin gives the exact identity

```math
\operatorname{area}K
=\frac12\sum_{i=1}^N d_i\ell_i.
\tag{1.2}
```

Since every `d_i>=r`,

```math
\boxed{
\operatorname{area}K
\ge
\frac r2\sum_i\ell_i
=\frac r2\operatorname{per}K.
}
\tag{1.3}
```

No smooth support formula is needed; this is finite polygon geometry.

---

## 2. Insert QPA's inradius bound

Now let `K` be centrally symmetric with diameter `D` and perimeter `P`.  QPA proves
that its centered inradius satisfies

```math
\boxed{
\frac{2r}{D}\ge\alpha(P/D).
}
\tag{2.1}
```

Put

```math
p=P/D.
```

Then (1.3) and (2.1) give

```math
\begin{aligned}
\operatorname{area}K
&\ge\frac12\left(\frac D2\alpha(p)\right)(pD)\\
&=D^2\frac{p\alpha(p)}4.
\end{aligned}
```

Hence

```math
\boxed{
\frac{\operatorname{area}K}{D^2}\ge\Xi(p).
}
\tag{2.2}
```

Apply this to FD's central symmetral

```math
S=\frac12((F-o)-(F-o)).
```

FD gives

```math
\operatorname{diam}S=D,
\qquad
\operatorname{per}S=P,
\tag{2.3}
```

and

```math
0\le\operatorname{area}S-\operatorname{area}F
\le L_DP+\pi L_D^2.
\tag{2.4}
```

Subtracting (2.4) from (2.2) proves SA.3.  Since `P<=pi D` and
`L_D=O(D^{3/4})`, the error is `o(D^2)`, proving SA.4.

---

## 3. SA strictly dominates QPD

Parameterize by

```math
a=\alpha(p),
\qquad
p=f(a)=2\left(\arcsin a+\sqrt{1-a^2}\right).
\tag{3.1}
```

Then

```math
\Xi(p)
=\frac a2\left(\arcsin a+\sqrt{1-a^2}\right).
\tag{3.2}
```

QPD gives

```math
\Omega(p)
=\frac14\left[
\pi a^2+2a\sqrt{1-a^2}-2a^2\arccos a
\right].
\tag{3.3}
```

Using `arccos a=pi/2-arcsin a`, direct subtraction yields

```math
\boxed{
\Xi(p)-\Omega(p)
=\frac12a(1-a)\arcsin a.
}
\tag{3.4}
```

This is strictly positive for `0<a<1`, proving the first inequality in SA.5.  QPD
already proves `Omega>Psi` in the same interior range.

At the disk endpoint,

```math
\Xi(\pi)=\frac\pi4,
\tag{3.5}
```

so SA still agrees with FD exactly at maximal perimeter.

---

## 4. Exact interaction with DB

DB gives

```math
p\ge g(y):=y+2\cos(y/2),
\qquad
2\rho\le y\le\pi.
\tag{4.1}
```

As in QPD,

```math
\alpha(g(y))=\sin(y/2).
\tag{4.2}
```

Therefore SA simplifies on the DB lower-perimeter curve to

```math
\boxed{
\Xi(g(y))
=\frac14\left[y\sin(y/2)+\sin y\right].
}
\tag{4.3}
```

FSDB is

```math
\Phi(y)=\frac{y+\sin y}{4}.
```

Hence

```math
\boxed{
\Phi(y)-\Xi(g(y))
=\frac y4\left(1-\sin(y/2)\right)>0
\qquad(0<y<\pi).
}
\tag{4.4}
```

Thus, exactly as required for a clean compact optimization, FSDB controls the minimum
DB perimeter while SA controls sufficiently large actual perimeter.

---

## 5. Derivative gap

Differentiate `Xi(p)=p alpha(p)/4`.  With `a=alpha(p)` and

```math
f'(a)=2\frac{1-a}{\sqrt{1-a^2}},
```

one obtains

```math
\boxed{
\Xi'(p)
=\frac a4
+\frac p8\sqrt{\frac{1+a}{1-a}}.
}
\tag{5.1}
```

QPD already proves every feasible post-ZF perimeter satisfies

```math
p>\frac{14}{5},
\qquad
a>\frac12.
\tag{5.2}
```

Therefore, using `sqrt(3)>5/3`,

```math
\begin{aligned}
\Xi'(p)
&>
\frac18
+\frac{14/5}{8}\sqrt3\\
&>
\frac18+\frac{7}{12}
=\boxed{\frac{17}{24}}
>\frac12.
\end{aligned}
\tag{5.3}
```

This is stronger than the derivative gap used in QJ.  In particular, for the unique
FSDB/SA crossover perimeter `c(y)` defined by

```math
\Xi(c(y))=\Phi(y),
```

one has

```math
0\le c'(y)=\frac{\Phi'(y)}{\Xi'(c(y))}<1.
\tag{5.4}
```

---

## 6. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| polygon support triangulation `area>=rP/2` | proved | exact sum of side triangles |
| QPA centered-inradius lower bound | already proved on branch | disk/strip perimeter envelope |
| SA finite force-hull bound | proved | support triangulation + QPA + FD area transfer |
| `Xi>Omega>Psi` on `2<p<pi` | proved | exact positive difference + QPD |
| DB-boundary identity SA.4.3 | proved | `alpha(g(y))=sin(y/2)` |
| derivative gap `Xi'>17/24` on post-ZF range | proved | explicit derivative and QPD's `p>14/5,a>1/2` |
| Level I | still open | SA is a stronger area currency, not yet a closing contradiction |

---

## 7. Next run

Repeat the QJ compact optimization with `Xi` in place of `Omega`.  The same monotonic
proof applies with stronger derivative margin.  The exact transition is the unique
`y_* in (2rho,pi/2)` satisfying

```math
\Xi(2y_*)=\Phi(y_*).
```

This should replace the QPD-based `0.589461...` report-level floor by a stronger
explicit constant.
