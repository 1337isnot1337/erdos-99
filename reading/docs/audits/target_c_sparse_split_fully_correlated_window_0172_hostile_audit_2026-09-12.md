> Generated reading edition · [exact source](../../../docs/audits/target_c_sparse_split_fully_correlated_window_0172_hostile_audit_2026-09-12.md) · source SHA-256 `1de352ad4ac7b8594cb6b701da410c4285cac8c09c58f09bb34984e8b26d74fa`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-DEB6B1499C76","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Hostile audit — fully correlated sparse-return window through `sigma=0.0172`

**Date:** 2026-09-12  
**Reviewed:** `docs/reports/target_c_sparse_split_fully_correlated_window_0172_2026-09-12.md`  
**Verdict:** **PASS at inherited proof-only scope.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The reviewed theorem correctly strengthens the sparse/directional full-core exclusion to

```math
\boxed{0\le\sigma\le0.0172.}
```

The gain is structural, not a finer decimal evaluation of the old bound. The previous
proof separately maximized two terms that require incompatible slack allocations. The
new proof keeps the shared simplex correlated until it reduces analytically to one
variable.

---

## 1. Uniform endpoint relaxation has the correct inequality directions

For every physical `sigma<=s_0=0.0172`, the Section-101 angular parameter satisfies

```math
\theta\le\theta_0,
\qquad
U\le U_0,
\qquad
\lambda\le\lambda_0.
```

The circular-segment function `G` is increasing. Therefore replacing `theta` by
`theta_0` decreases the area lower bound, replacing `U` by `U_0` increases the
negative directional product, and replacing `lambda` by `lambda_0` increases the
negative sparse penalty. All three replacements lower `widetilde J` and are therefore
conservative.

The relaxed domain is enlarged from the physical equality simplex to

```math
x+y+z+w\le s_0.
```

For fixed `x,y,z`, the relaxed lower bound is strictly decreasing in `w` because

```math
\partial_w A
={10\over3}A_r<0,
```

```math
\partial_w(-\lambda_0P)
=-{25\over3}\lambda_0<0,
```

and

```math
\partial_w(-2CB)
=-{20\over3}C<0.
```

Here `C>0`. Hence the relaxed global minimum lies on `x+y+z+w=s_0`. Filling unused
slack with `w` is an optimization device only; it is not asserted to describe a new
physical source.

---

## 2. The inherited geometry remains valid at `0.0172`

The hostile-audited largest-gap transfer has derivative above `0.30` on
`theta>=theta_8`, `0<=delta<=0.1`, and the coarse `delta>=0.1` branch costs above
`0.0326`. Since `w<=0.0172`, the coarse branch remains impossible and

```math
\delta\le10w/3.
```

Using the exact correlated identity rather than independent slack bounds,

```math
x_2+x_3+\tau=\delta+x
\le x+{10\over3}w
\le{10\over3}s_0
=0.0573333\ldots .
```

The residual principal gap is still

```math
\phi_0=0.8700560\ldots,
```

so the fourth-gap/adjacent-span argument stays in the same strict branch.

The tangent-lift extent is

```math
U_0+10s_0/3
=1.8938419\ldots<\pi,
```

and the coarser corridor-mismatch lower bound is still `0.0949897...>0`. Thus no
projective-lift or principal-corridor collision is introduced by the extension.

The tooth inverse reaches only

```math
Q(s_0)=0.1006739\ldots<0.101<\pi/3.
```

All Section-118 geometric prerequisites used by the sparse split therefore survive.

---

## 3. The `x` derivative is strictly positive without numerics

After setting `w=s_0-x-y-z`, let

```math
r={10s_0\over3}-{7x\over3}-{10y\over3}-{10z\over3},
```

```math
C=U_0-x-y+2z,
```

```math
B=Q(y)+{10s_0\over3}-{7x\over3}-{7y\over3}-{10z\over3}.
```

The area derivative

```math
A_r=-2G'(\phi_8+r)-G'(r)
```

is negative. Direct differentiation gives

```math
\mathcal F_x
=-{7\over3}A_r
+{47\over6}\lambda_0
+2B+{14\over3}C.
```

Every term is positive. Thus the minimizer must have

```math
\boxed{x=0.}
```

No sampled optimizer is involved.

---

## 4. The `z` derivative has margin above six

The corresponding derivative is

```math
\mathcal F_z
=-{10\over3}A_r
-\lambda_0\left(10+{1\over\kappa}-{25\over3}\right)
-4B+{20\over3}C.
```

The first term is positive. Throughout the simplex,

```math
C\ge U_0-s_0=1.81930858\ldots,
```

and

```math
B\le Q(s_0)+10s_0/3<0.158008.
```

Dropping the favorable area derivative still gives

```math
\mathcal F_z>6.225.
```

Hence every minimizer has

```math
\boxed{z=0.}
```

This is the decisive correction to the earlier independent-max argument: the worst
`z` penalty is not simultaneously available at the directional product extremum.

---

## 5. The one-dimensional function is globally strictly convex

After `x=z=0`, the report's `H(y)` is exact on `0<=y<=s_0`.

For the tooth inverse,

```math
Q'={1\over2F'(Q)},
\qquad
Q''=-{F''(Q)\over4F'(Q)^3}<0.
```

Since `Q<0.101`,

```math
F'(Q)\le\sqrt3Q<0.175,
```

and

```math
F''(Q)>1.62.
```

Thus

```math
-Q''>75.7.
```

The second derivative of the area term is bounded below by `-25/6`. Also

```math
Q'>1/(2(0.175))>2.857,
```

and `U_0-y>1.8193`. Therefore direct differentiation gives the uniform lower bound

```math
H''
>-{25\over6}
+4\left({1\over0.35}-{7\over3}\right)
+2(1.8193)(75.7)
>273.
```

So `H` is strictly convex on the full interval. As `y downarrow0`, `Q'` diverges and
`H'` tends to `-infinity`, consistent with one interior minimum.

---

## 6. The minimum bracket has fixed positive margin

Direct recomputation gives

```math
H'(0.00669)=-0.0068266\ldots< -0.0068,
```

```math
H'(0.00670)=0.0059257\ldots>0.0059.
```

Strict convexity places the unique minimizer inside that interval.

At its midpoint,

```math
H(0.006695)=0.0023269894\ldots .
```

Within the bracket, `H'` lies between the two endpoint derivatives. Moving at most
`5e-6` from the midpoint can therefore lower `H` by less than

```math
0.0069(5\times10^{-6})<3.5\times10^{-8}.
```

Hence

```math
\boxed{\min H>0.0023269>0.00232.}
```

The contradiction is not a floating-point sign at zero.

---

## 7. Scalar envelope check

Solving the same reduced one-dimensional problem as a function of the endpoint slack
gives first numerical zero

```math
0.0173116294\ldots .
```

This is not promoted as a theorem endpoint. The safe `0.0172` value lies more than
`1.1e-4` below it and has the fixed `>0.00232` return-bracket margin above.

---

## 8. Regression table

| Failure mode | Audit result |
| --- | --- |
| Same slack spent in both product and sparse penalty | Repaired: exact shared simplex retained |
| Endpoint relaxation changes sign | Checked: all replacements lower `widetilde J` |
| Fictitious slack interpreted physically | No: only used to minimize enlarged relaxed domain |
| `delta>=0.1` branch reappears | No: cost `>0.0326>0.0172` |
| Fourth-gap/tangent lift leaves its branch | No: `0.0574` perturbation versus `0.8700` gap; extent `<1.894<pi` |
| Interior `x` or `z` minimizer | Excluded analytically |
| Multiple `y` minima | Excluded by `H''>273` |
| Numerical minimum too close to zero | No: margin `>0.00232` |
| Contact-isolated affine-kernel extension | Not used |
| Type-I closure | Not claimed |

**Verdict:** PASS as an audited-working proof-only extension. The full-core surviving
window is reduced to `sigma>0.0172`; C-II and Level I remain open.
