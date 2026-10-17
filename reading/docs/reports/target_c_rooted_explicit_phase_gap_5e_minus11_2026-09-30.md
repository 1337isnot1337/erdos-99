> Generated reading edition · [exact source](../../../docs/reports/target_c_rooted_explicit_phase_gap_5e_minus11_2026-09-30.md) · source SHA-256 `79a3d32aa54fe1a525891fe01059af147bc03bad890b1c75a4a0740f14f2e1f1`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-7DE13280BEDC","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II -- explicit rooted phase gap from the current defect ledger

Date: 2026-09-30
Base main: b12708a602af4b17bbb8ecf61e5ed461e4bb2e15
Status: proof-only; C-II remains open.

## Result

Let
```math
A(\lambda)=\lambda+4\lambda\sqrt{1-\lambda^2},
\qquad
A(\lambda_1)=\pi/2,
```
and put $`\sigma_0=5\cdot10^{-11}`$. Let $`\lambda_2>\lambda_1`$ be the
unique root
```math
\boxed{A(\lambda_2)=\pi/2-\sigma_0.}
\tag{1}
```
Then no positive-area locally rhombus-saturated center-wrapping harmonic-cell
sequence has normalized diameter in $`[\lambda_1,\lambda_2]`$.

Consequently the current Section-83/88 macroscopic-cell transfer improves the
rooted carrier conclusion to
```math
\boxed{\operatorname{diam}(P_*)\ge(\lambda_2-o(1))D}
\tag{2}
```
for an actual quadratic-area locally rhombus-saturated harmonic cell.

For orientation only,
```math
\lambda_1=0.9891345915624005433\ldots,\qquad
\lambda_2=0.9891345915643979535\ldots.
```
Thus the explicit increase is about $`1.9974\cdot10^{-12}`$. The proof uses
the exact equation (1), not these decimals.

## 1. Defect and gap slack

Assume a wrapping carrier has $`d_w/D\to\lambda\in[\lambda_1,\lambda_2]`$.
Write
```math
\theta=2\arcsin\lambda,\quad
\phi=2\pi-2\theta,\quad
\sigma=\pi/2-A(\lambda).
```
Current main proves $`A`$ strictly decreasing on the live interval, hence
```math
0\le\sigma\le\sigma_0.
\tag{3}
```

Let
```math
Z_D=\sum_r(L_r-\operatorname{per}P_r),\qquad Q_D=\sum_rQ_r.
```
The new rooted defect ledger on main gives
```math
\boxed{Z_D\le(2\sigma+o(1))D,\qquad Q_D\le(2\sigma+o(1))D.}
\tag{4}
```

Let $`g_j`$ be the complement gaps of the limiting circle support and
```math
C=\sum_j\sin(g_j/2).
```
The same main theorem defines
```math
M_D=\sum_rd_r-[\lambda+A(\lambda)]D
```
and gives $`M_D\le(\sigma+o(1))D`$. The complement-gap residual-cell moment
gives
```math
M_D\ge[C-A(\lambda)-o(1)]D.
```
Canonical Section 101 gives $`C\ge A(\lambda)`$. Therefore
```math
\boxed{0\le C-A(\lambda)\le\sigma.}
\tag{5}
```

Elementary Taylor bounds put the whole interval in
```math
2.8<\theta<2.85.
\tag{6}
```

## 2. Quantitative gap profile

Sort the gaps and write
```math
g_1=\theta-\delta,\qquad
g_2=\phi+x_2,\qquad
g_3=\phi+x_3,\qquad
\tau=\sum_{j\ge4}g_j.
```
If the total complement mass is $`\theta+2\phi+e`$, then
```math
x_2+x_3+\tau=\delta+e.
\tag{7}
```

Set $`f(t)=\sin(t/2)`$. On $`2.8\le\theta\le2.85`$, for $`0\le t\le0.1`$,
```math
\frac d{dt}\{f(\theta-t)+f(\phi+t)-f(\theta)-f(\phi)\}>0.30.
```
The Section-104 majorization argument and (5) therefore give
```math
\boxed{\delta\le(10/3)\sigma.}
\tag{8}
```

Also $`f'(t)=(1/2)\cos(t/2)>1/20`$ for $`0\le t\le2.85`$. Delete the excess
gap mass $`e`$, preserving three gaps of length at least $`\phi`$, until the
total is $`\theta+2\phi`$. The resulting vector still has chord sum at least
$`A(\lambda)`$, while deleting mass $`e`$ lowers the chord sum by at least
$`e/20`$. Hence
```math
\boxed{e\le20\sigma.}
\tag{9}
```
Thus
```math
x_2+x_3+\tau\le(70/3)\sigma,
\qquad
C_{\rm tail}:=\sum_{j\ge4}\sin(g_j/2)\le(35/3)\sigma.
\tag{10}
```

Since $`\tau<\phi`$, the Section-104 fourth-gap argument gives that the two
support spans $`a,b`$ adjacent to the largest gap obey
```math
a,b\le\delta.
\tag{11}
```

Normalize $`g_1`$ from angle $`0`$ to $`g_1`$, with $`g_2`$ after span $`a`$
and $`g_3`$ before span $`b`$. Direct midpoint calculation gives, for the two
pairs involving $`g_1`$, error from the endpoint separation $`\theta/2`$ at
most
```math
(3/2)\delta+(1/2)(\delta+e)\le(50/3)\sigma,
```
and for the $`g_2,g_3`$ pair, error from $`\pi-\theta`$ at most
```math
(7/2)\delta+e/2\le(65/3)\sigma.
```
Therefore every distinct pair of principal corridor directions $`q_i,q_j`$
satisfies
```math
\boxed{
\left|\operatorname{dist}_{\mathbb{RP}^1}(q_i,q_j)-\pi/3\right|>0.35.
}
\tag{12}
```
Indeed $`\theta>2.8`$ and $`\pi<22/7`$ give
```math
\theta/2-\pi/3>0.352,\qquad
\pi/3-(\pi-\theta)>0.704,
```
while $`(65/3)\sigma_0<1.1\cdot10^{-9}`$.

## 3. Two uniform inverse-phase families

For $`G(t)=(t-\sin t)/8`$,
```math
\operatorname{area}(\operatorname{conv}S)=\pi/4-\sum_jG(g_j).
```
Using $`g_1<2.85`$, $`\sin(2.85)>0.285`$, $`g_2,g_3<0.687`$,
$`G(t)<t^3/48`$, and (10), one gets
```math
\operatorname{area}(\operatorname{conv}S)>0.44.
\tag{13}
```
Local rhombus saturation therefore gives more than $`0.40D^2`$ strict rhombi
for large $`D`$. Take $`r=0.40`$ in canonical Section 90.

Section 100 gives
```math
2\alpha\le3\theta-2\pi<2.27,
```
so $`a_D<1.14D`$ eventually. Section 89 gives $`T_D<7D`$. Thus Section 90.3
with $`C_T=7`$ supplies two fixed distinct phase-label train families
$`\mathcal A_D,\mathcal B_D`$, each with at least
```math
\frac{r}{32C_T}D=\frac1{560}D
```
train segments. Their limiting projective directions $`u_A,u_B`$ satisfy
```math
\boxed{\operatorname{dist}_{\mathbb{RP}^1}(u_A,u_B)=\pi/3.}
\tag{14}
```
Each family has at least
```math
E_0D,\qquad E_0=1/280,
\tag{15}
```
physical boundary-end occurrences.

## 4. Off-principal leakage

For the wrapping cell,
```math
Z_w=L_w-\operatorname{per}(P_w)\le(2\sigma+o(1))D.
\tag{16}
```
At most $`5Q_w\le(10\sigma+o(1))D`$ train ends face bounded
nonquadrilateral faces. All other ends occur on consecutive-attachment outer
routes.

For one route with base length $`b_i`$, base direction $`q_i`$, unit route
vectors $`z`$, and length $`\ell_i`$, projection gives exactly
```math
\ell_i-b_i=\sum_z(1-q_i\cdot z).
\tag{17}
```

Fix one phase family, with limiting direction $`u`$, and set
$`\eta=10^{-3}`$.

If a nonprincipal route base is projectively at least $`\eta`$ from $`u`$,
then for large $`D`$ each selected terminal edge pays at least
$`1-\cos(\eta/2)\ge\eta^2/12`$ in (17). By (16), such ends have density at
most
```math
24\sigma/\eta^2+o(1).
\tag{18}
```

For nonprincipal route bases within $`\eta`$ of $`u`$, convex boundary-direction
monotonicity gives the same directional-length bound used in Section 104.
A projective radius-$`\eta`$ window has two oriented lifts, whose circular
pieces have total normalized length at most $`2\eta`$; the nonprincipal
straight pieces are tail-gap chords of total length at most $`C_{\rm tail}`$.
Hence their base lengths total at most
```math
(2\eta+C_{\rm tail}+o(1))D.
```
Adding their route excess from (16), their selected endpoint density is at most
```math
2\eta+C_{\rm tail}+2\sigma+o(1).
\tag{19}
```

Combining (10), (18), (19), and the bounded-face term,
```math
\frac{N_{\rm off}}D
\le
2\eta+\frac{24\sigma}{\eta^2}+\frac{71}{3}\sigma+o(1).
\tag{20}
```
At $`\eta=10^{-3}`$, $`\sigma\le5\cdot10^{-11}`$, the explicit part of the
right side is below $`0.003201`$. Since $`E_0=1/280>0.003571`$, each phase
family leaves more than $`0.00036D`$ ends on the three principal corridors.
Thus one principal corridor carries at least
```math
\boxed{\rho D,\qquad \rho=10^{-4}}
\tag{21}
```
ends of each selected family.

## 5. Contradiction

Suppose a principal corridor of limiting direction $`q`$ carries the
$`\rho D`$ ends from a phase family of limiting direction $`u`$. Its route
excess is at most (16), so (17) gives
```math
\rho(1-\cos x)\le2\sigma,
\qquad
x=\operatorname{dist}_{\mathbb{RP}^1}(u,q).
```
Using $`1-\cos x\ge2x^2/\pi^2`$ on $`[0,\pi/2]`$,
```math
x^2\le\pi^2\sigma/\rho<5\cdot10^{-6},
```
hence
```math
x<0.0023.
\tag{22}
```

Apply this to both phase families. They cannot use the same principal corridor,
or (22) would contradict their exact $`\pi/3`$ separation. If they use distinct
corridors $`q_i,q_j`$, then (14) and (22) give
```math
\left|\operatorname{dist}_{\mathbb{RP}^1}(q_i,q_j)-\pi/3\right|<0.0046,
```
contradicting (12). This proves (1)-(2).

The standard current-main macroscopic transfer finishes (2): the two-half-disk
alternative already has diameter $`1-o(1)`$, while in the wrapping alternative
all macroscopic limits below $`\lambda_2`$ would now have to be cap type.
Section 88 cap-family capacity at the fixed $`\lambda_2<1`$, plus Section 83
small-cell control, is strictly below the Type-II area $`\pi D^2/4-o(D^2)`$.

## Scope

This is theorem/proof work. No numerical verifier or CI result is load-bearing.
The decimal roots above only evaluate exact equations. Repeated outer-walk
occurrences, bridges, and contact-isolated source points are handled in the
canonical conventions. The macroscopic inactive-container branch is unchanged,
and C-II remains open.

## Salvage provenance and lifecycle

Salvaged on 2026-10-04 from
`proof/rooted-explicit-phase-gap-1e12-20260930-run13` at tip
`841831b6a9345eab0320dbf522d0d280b4008d80`. This is an explicit quantitative
exclusion for the single near-endpoint window defined above; the decimal values are
orientation only and the proof uses the exact root equations. It remains an unreviewed,
proof-only candidate depending on the stated current-main C-II dependencies. The
macroscopic inactive-container branch, full C-II, and Level I remain open; theorem state
is unchanged.
