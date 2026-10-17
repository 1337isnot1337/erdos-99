> Generated reading edition · [exact source](../../../docs/reports/target_c_fs_matching_gap_exact_audit_2026-09-10.md) · source SHA-256 `8a53d0b7876b355373d7142503e978ff445f1d61c2087a42f81a9b7c8977d00e`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-5054E84B66A7","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_fs_matching_gap_exact_audit_2026-09-10.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=ba30aed0eb6e3431e934e4084782791bd496c053; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — exact rational audit of the FSDB matching-area gap

**Date:** 2026-09-10  
**Repository state:** PR #159 head `dd39eae04fe235fa9256f936787456181518de1c`  
**Run type:** exact constant audit  
**Target:** Target C post-ZF perfect-matching branch  
**Computation:** none used in the proof

## LEVEL I STATUS

`STILL OPEN`

The companion matching-branch report uses the strict constant comparison

```math
A_{FS}:=\frac{2\rho+\sin(2\rho)}4
>\frac{\pi^2}{16},
\qquad \rho=\cos\rho,
\tag{1}
```

where `rho` is the unique root of `cos x=x` in `(0,pi/2)`.
This note gives a completely rational certificate for (1), so the branch closure does
not depend on printed decimal approximations.

## 1. Rational enclosure for the Dottie root

Put

```math
a=\frac{739}{1000},\qquad b=\frac{37}{50}.
```

On `(0,pi/2)`, the function

```math
f(x)=\cos x-x
```

is strictly decreasing because

```math
f'(x)=-\sin x-1<0.
```

For `0<x<1`, the alternating Taylor series gives

```math
\cos x>
1-\frac{x^2}{2}+\frac{x^4}{24}-\frac{x^6}{720}
\tag{2}
```

and

```math
\cos x<
1-\frac{x^2}{2}+\frac{x^4}{24}.
\tag{3}
```

At `a=739/1000`, direct rational arithmetic gives

```math
1-\frac{a^2}{2}+\frac{a^4}{24}-\frac{a^6}{720}-a
=
\frac{101004823138270439}{720000000000000000000}>0.
\tag{4}
```

Hence `f(a)>0`.

At `b=37/50`, direct rational arithmetic gives

```math
1-\frac{b^2}{2}+\frac{b^4}{24}-b
=-\frac{195839}{150000000}<0.
\tag{5}
```

Hence `f(b)<0`.

Since `f` is strictly decreasing and `f(rho)=0`, (4)--(5) prove

```math
\boxed{\frac{739}{1000}<\rho<\frac{37}{50}.}
\tag{6}
```

## 2. Rational lower bound for `A_FS`

Because `rho in (0,pi/2)` and `rho=cos rho`,

```math
\sin\rho=\sqrt{1-\rho^2}
```

and therefore

```math
A_{FS}
=\frac{\rho}{2}\left(1+\sqrt{1-\rho^2}\right).
\tag{7}
```

The upper bound in (6) gives

```math
1-\rho^2>1-\left(\frac{37}{50}\right)^2
=\frac{1131}{2500}.
```

Also

```math
\frac{1131}{2500}>\left(\frac{84}{125}\right)^2,
```

because

```math
1131\cdot15625=17671875
>
17640000=7056\cdot2500.
```

Thus

```math
\sqrt{1-\rho^2}>\frac{84}{125}.
\tag{8}
```

Using the lower bound on `rho` from (6) and (8) in (7),

```math
A_{FS}
>
\frac{739}{2000}\left(1+\frac{84}{125}\right)
=
\boxed{\frac{154451}{250000}}.
\tag{9}
```

## 3. Rational upper bound for `pi^2/16`

The classical Archimedean bound `pi<22/7` can be certified by the exact identity

```math
\frac{22}{7}-\pi
=
\int_0^1
\frac{x^4(1-x)^4}{1+x^2}\,dx>0.
\tag{10}
```

(The equality follows by polynomial division and
`integral_0^1 dx/(1+x^2)=pi/4`; positivity is immediate.)
Therefore

```math
\frac{\pi^2}{16}
<
\frac1{16}\left(\frac{22}{7}\right)^2
=
\boxed{\frac{121}{196}}.
\tag{11}
```

Finally,

```math
\frac{154451}{250000}>\frac{121}{196},
```

because

```math
154451\cdot196
=30272396
>
30250000
=121\cdot250000.
\tag{12}
```

Combining (9), (11), and (12) proves the desired exact inequality

```math
\boxed{
A_{FS}>\frac{\pi^2}{16}.
}
\tag{13}
```

No transcendental decimal evaluation is used.

## 4. Effect on the matching proof

The companion report proves in the perfect-matching branch

```math
\operatorname{area}F\le\frac{\pi^2}{16}D^2,
```

while FSDB gives along every unbounded post-ZF sequence

```math
\liminf\frac{\operatorname{area}F}{D^2}\ge A_{FS}.
```

Equation (13) supplies the exact strict margin needed to make those inequalities
incompatible.  Thus the matching-branch exclusion is a genuine proof, not a
floating-point comparison.

## Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| `739/1000<rho<37/50` | proved exactly | alternating cosine bounds and rational arithmetic |
| `sin rho>84/125` | proved exactly | upper bound on `rho` and integer square comparison |
| `A_FS>154451/250000` | proved exactly | preceding two bounds |
| `pi^2/16<121/196` | proved exactly | positive integral proof of `pi<22/7` |
| `154451/250000>121/196` | proved exactly | integer cross multiplication |
| `A_FS>pi^2/16` | proved exactly | transitivity |

## Compact handoff

```text
Exact MFS constant certificate:
  739/1000 < rho < 37/50, rho=cos rho.
The lower inequality follows from
  1-a^2/2+a^4/24-a^6/720-a
  =101004823138270439/720000000000000000000 >0,
and the upper from
  1-b^2/2+b^4/24-b=-195839/150000000<0.
Thus sin rho=sqrt(1-rho^2)>84/125 and
  A_FS=rho(1+sin rho)/2 >154451/250000.
Also pi<22/7 via
  22/7-pi=int_0^1 x^4(1-x)^4/(1+x^2) dx>0,
so pi^2/16<121/196.
Finally 154451*196=30272396>30250000=121*250000.
Hence A_FS>pi^2/16 exactly.
```
