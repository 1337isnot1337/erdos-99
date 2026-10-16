# Target C: double touch-three rank-loss cancellation

Date: 2026-09-23

Status: rigorous strengthening of the remaining eight-no-root `k=6,D=-1,p=9` Profile B. The preceding double-witness theorem bounded the deficiency of the union puncture only when deleting the two touch-three witness triples preserved coefficient rank two. This note removes that hypothesis. The same deficiency bound survives coefficient-rank loss exactly because the loss of external puncture rank and the growth of the descendant functional quotient cancel.

Profile B and Target C-II are not yet closed.

Companion exact filter:

`research/verify_target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_profile_b_double_touch3_rankloss_cancellation_2026_09_23.py`

## 1. Setup

Use the fixed source-basis model already established for Profile B:

```text
V = Q^9,
q_1,...,q_9 is the chosen source singleton basis,
L = W^perp <= V,
dim L = 6.
```

Let `b=q_i` and `c=q_j` be two distinct dependency-active aligned touch-three witnesses, with touch triples `T,U`. The previous forcing theorem gives

```text
|T intersect U| <= 1,
K_T = E_T direct-sum <q_i>,
K_U = E_U direct-sum <q_j>.
```

Put

```text
R = T union U,
r = |R| in {5,6},
t = 8-r in {3,2}.
```

Let `P<=Q^8` be the source coefficient plane, `dim P=2`, and let `P_R` denote its projection to the `t` surviving coordinates. Write

```text
k_R = 2-rank(P_R).
```

Thus `k_R` is the coefficient-rank loss under deletion of `R`. Equivalently,

```text
k_R = dim(P intersect Q^R),
```

where `Q^R` is the coordinate subspace supported on `R`.

The preceding note treated only `k_R=0`. Here `k_R` may be `0,1,2`.

## 2. External puncture span loses exactly k_R dimensions

Let `ell_s<=L` be the one-coordinate puncture-kernel line attached to source coordinate `s`. The exact external-kernel theorem proves that the labeled relation plane among

```text
ell_1,...,ell_8
```

is diagonally projectively equivalent to the source coefficient plane `P`. Independent nonzero coordinate rescalings do not change which subsets of the labeled lines are linearly dependent.

Therefore the linear relations among `{ell_s:s in R}` are exactly the coefficient-codeword relations supported in `R`. Their relation-space dimension is

```text
dim(P intersect Q^R)=k_R.
```

Hence, for

```text
E_R = span{ell_s : s in R},
```

we have the exact identity

```text
dim E_R = r-k_R.                                  (2.1)
```

This is the point missed by the rank-preserving-only argument: a one-dimensional coefficient-rank drop removes exactly one dimension from the external puncture span, and a two-dimensional drop removes exactly two.

Because `T,U subset R`,

```text
E_T+E_U = E_R.                                    (2.2)
```

Indeed both sides are the span of the same labeled one-puncture lines indexed by `R=T union U`.

## 3. Descendant quotient dimension gains exactly k_R dimensions

The rank-uniform replacement-functional accounting already proved in the `k=6` reduction says that a `t`-row virtual-canonical state with coefficient rank `a` and deficiency `d` has replacement-functional quotient dimension

```text
s = t-a+d.
```

For the union descendant,

```text
a = 2-k_R,
```

so if its virtual-canonical deficiency is `d_R`, then

```text
s_R
 = t-(2-k_R)+d_R
 = 6-r+k_R+d_R.                                   (3.1)
```

The nine source basis classes map surjectively to this descendant quotient by puncture functoriality. Let

```text
K_R = ker(V -> V_R).
```

Then

```text
dim K_R
 = 9-s_R
 = 3+r-k_R-d_R.                                   (3.2)
```

## 4. The rank-loss terms cancel

Puncture functoriality gives

```text
K_T <= K_R,
K_U <= K_R.
```

Using the two witness splittings and (2.2),

```text
span(E_R,q_i,q_j) <= K_R.                          (4.1)
```

Define

```text
sigma_R = dim span(E_R,q_i,q_j)-dim E_R.
```

Both witness classes are dependency-active, so neither lies in `L`, while `E_R<=L`. Therefore

```text
sigma_R in {1,2}.                                  (4.2)
```

By (2.1), the forced subspace in (4.1) has dimension

```text
(r-k_R)+sigma_R.
```

Combining with (3.2),

```text
3+r-k_R-d_R >= r-k_R+sigma_R.
```

The `r-k_R` terms cancel, leaving

```text
d_R <= 3-sigma_R.                                 (4.3)
```

This is exactly the same bound as in the rank-preserving case, with no hypothesis on `rank(P_R)`.

Consequently every pair of forced touch-three witnesses, including every coefficient-rank-drop pair, satisfies

```text
d_R <= 2.                                          (4.4)
```

If `sigma_R=2`, then

```text
d_R <= 1.                                          (4.5)
```

Thus coefficient-rank loss is not a separate escape branch. It cannot weaken the union-kernel deficiency drop.

## 5. Borderline d_R=2 remains rigid under rank loss

Suppose the union descendant has `d_R=2`, regardless of its coefficient rank. Then (4.3) forces

```text
sigma_R=1.
```

Equivalently the two witness source classes become projectively dependent modulo `E_R`:

```text
q_i-lambda q_j in E_R
```

for some nonzero rational `lambda` after rescaling one witness coordinate.

Since `E_R<=L`, the two classes are also projectively equal in `V/L`. Hence the previous rigidity statement for the `d_R=2` branch survives coefficient-rank loss unchanged.

## 6. Exact source-level filter

The companion verifier layers on the previous double-touch-three filter but no longer skips rank-drop union punctures. For every witness pair it:

1. constructs `R=T union U`;
2. computes the exact projected coefficient rank `rank(P_R)` and `k_R=2-rank(P_R)`;
3. reconstructs the virtual-canonical union descendant at that actual coefficient rank;
4. maps the nine fixed source singleton states into the descendant quotient, allowing a source state to remain valid even if the lower-rank descendant admits additional compatible singleton states;
5. computes the exact descendant kernel `K_R`;
6. checks the rank-uniform quotient target `t-rank(P_R)+d_R`;
7. computes `E_R` from the one-puncture lines and checks `dim E_R=r-k_R`;
8. checks `K_T,K_U<=K_R` and `span(E_R,q_i,q_j)<=K_R`;
9. computes `sigma_R` and rejects any state with `d_R>3-sigma_R`.

This is a necessary filter. It does not depend on GitHub Actions or any external numerical rank test.

## 7. Remaining bottleneck

The previous bottleneck split into

- rank-drop union punctures; and
- rank-preserving punctures with `d_R<=2`, with `d_R=2` only when `sigma_R=1`.

The first branch is now absorbed into the second. Every witness-pair union, at every possible projected coefficient rank, has

```text
d_R<=2,
```

and every `d_R=2` union has the exact collapse `sigma_R=1`.

The next target is therefore singular: analyze or exhaust the `sigma_R=1,d_R=2` union-kernel collapse. Any pair with `sigma_R=2` already has `d_R<=1` regardless of coefficient-rank loss.
