> Generated reading edition · [exact source](../../../docs/audits/target_c_section113_extended_stability_gap_hostile_audit_2026-09-12.md) · source SHA-256 `e8fc642123e5fb88598f3b0eaaac9112307d6a8cd2134ba62df4c35655b34e9a`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-916681E0B1F2","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — Section 113 full hostile audit

**Date:** 2026-09-12  
**Verdict:** **PASS as a proof-only theorem.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This audit reviews `research/target_c_section113_extended_stability_gap.md` at the
proof level. It does not promote Section 113 or mutate theorem authority. The canonical
Target-C state remains audit.44 / Section 104 until a separate theorem-state promotion
transaction is justified.

The audit checks the widened complement-gap window, exact carrier-area transfer,
outer-ledger train bound, corrected joint-shore extraction, reuse of the Section-104
leakage machinery, aggregate two-family projection accounting, and the final scalar
contradiction at `sigma=1.4e-3`.

The conclusion is that Section 113 survives those checks. Its proof-only endpoint is

$$
\theta_{17}=2.703205775845795918\ldots,
\qquad
\mu_{17}=\sin(\theta_{17}/2)
=0.976073147411914233\ldots .
$$

This is still only a quantitative carrier theorem. It does not force an exact unit
equilateral triangle and does not close C-II.

## 1. Largest-gap stability remains valid on the wider window

Section 113 assumes

$$
\theta_8\le\theta\le\theta_{17},
\qquad
0\le\sigma(\theta)\le1.4\times10^{-3},
$$

and uses the canonical scalar chain

$$
M\le C\le2\alpha\le|S|\le U,
\qquad U-M=\sigma.
$$

Therefore every individual slack in the chain is at most `sigma`, exactly as in
Sections 104 and 107.

Writing the largest complement gap as `g_1=theta-delta`, the proof first excludes
`delta>=0.1` by the same concavity/majorization transfer

$$
h_\theta(t)
=f(\theta-t)+f(\phi+t)-f(\theta)-f(\phi).
$$

On

$$
\theta_8\le\theta\le\theta_{17},
\qquad0\le t\le0.1,
$$

its derivative

$$
\partial_t h_\theta(t)
={1\over2}\cos{\phi+t\over2}
-{1\over2}\cos{\theta-t\over2}
$$

increases with `theta` and decreases with `t`. The lower corner used in Section 113
is therefore the correct worst case, and the displayed lower bound `>0.30` has ample
margin. Since `C-M<=0.0014`, the `delta>=0.1` branch is impossible.

For `delta<0.1`, integrating the same derivative gives

$$
C-M>0.30\delta,
$$

hence

$$
\boxed{\delta\le{10\over3}\sigma.}
$$

With

$$
g_2=\phi+x_2,
\quad g_3=\phi+x_3,
\quad \tau=\sum_{j\ge4}g_j,
$$

exact complement measure gives

$$
x_2+x_3+\tau=\delta+e,
\qquad0\le e\le\sigma,
$$

so

$$
\boxed{x_2,x_3,\tau\le{13\over3}\sigma.}
$$

At maximal slack this upper bound is only about `0.00607`, while `phi` remains above
`0.876`. The Section-104 fourth-gap argument therefore still proves that the two
support spans adjacent to the principal gap satisfy `s_+,s_-<=delta`.

The resulting principal-corridor mismatch bound

$$
\left|
\operatorname{dist}_{RP^1}(q_i,q_j)-{\pi\over3}
\right|
>
{\theta_8\over2}-{\pi\over3}-{73\over6}\sigma
$$

is consequently valid throughout the Section-113 window. At the upper endpoint its
right side is

$$
0.287223130294252762\ldots>0.
$$

## 2. Section 107's exact area identity can be reused beyond its original numerical window

The full Sections-107/108 hostile audit proved the identity

$$
\operatorname{area}(\operatorname{conv}S)
={\pi\over4}-{1\over8}\sum_j(g_j-\sin g_j)
$$

for arbitrary compact wrapping support with angular diameter below `pi`. The identity
itself has no `sigma<=10^-3` hypothesis.

Section 113 separately re-establishes the only numerical gap controls needed for the
area lower bound. With

$$
G(x)={x-\sin x\over8}
$$

and `q_*=(13/3)(1.4e-3)`, monotonicity and superadditivity give the conservative segment
loss

$$
G(\theta_{17})+2G(\phi_8+q_*)+G(q_*).
$$

Direct high-precision recomputation gives

$$
\operatorname{area}(\operatorname{conv}S)
\ge0.472929268\ldots>0.472.
$$

Hausdorff area continuity and local rhombic saturation then give, for sufficiently
large finite carriers,

$$
\boxed{R_D\ge0.472D^2.}
$$

No unsupported extension of the Section-107 `sigma<=10^-3` theorem is being used:
Section 113 uses the scale-independent area identity and reproves the wider-window
stability estimates itself.

## 3. The exact train-count improvement is valid

Canonical Sections 82 and 89 give

$$
L_D+Q_D=4a_D-6-2s_D-2c_D,
\qquad
P_{R,D}\le L_D+5Q_D,
\qquad
2T_D=P_{R,D}.
$$

Therefore

$$
T_D\le2a_D-3-s_D-c_D+2Q_D
\le2a_D+2Q_D.
$$

Retaining the favorable currency in the finite Section-101 route proof gives

$$
C\le2\alpha-\limsup_D{2s_D+c_D+Q_D\over D}.
$$

Together with `0<=2alpha-C<=sigma`, nonnegativity implies

$$
Q_D/D\le\sigma+o(1).
$$

Since `2alpha<=U`, this yields

$$
\boxed{T_D/D\le U(\theta)+2\sigma+o(1).}
$$

At the Section-113 endpoint the right side is

$$
1.829232020\ldots<1.83.
$$

Thus the finite ceiling `T_D<=1.83D` is justified after increasing the large-`D`
threshold. This is the same exact outer-ledger argument that appeared in the proof-only
local-train-count line; Section 113 rederives it and therefore does not logically depend
on the misnumbered intermediate source.

## 4. The corrected joint-shore capacity has no missing factor two

After the phase cut and defect deletion, Section 113 obtains for one fixed unordered
phase-label pair at least

$$
0.1566316422666667\ldots D^2
$$

crossings lying inside common reduced-phase bins.

For bin `j`, let `a_j,b_j` be the two label-shore populations. If every occupied bin
has one shore below `aD`, split bins into

$$
X=\{j:a_j<aD\},
\qquad
Y=\{j:a_j\ge aD,\ b_j<aD\}.
$$

Simplicity of the train-crossing graph gives

$$
e_j\le a_jb_j.
$$

Hence

$$
\sum_{j\in X}e_j\le aD\sum_{j\in X}b_j,
\qquad
\sum_{j\in Y}e_j\le aD\sum_{j\in Y}a_j.
$$

A local train segment has one reduced phase and one phase label, so it belongs to at
most one of these bin/label shore populations. The two selected labels are distinct.
Consequently

$$
\sum_{j\in X}b_j+\sum_{j\in Y}a_j\le T_D,
$$

not `2T_D`. Therefore the correct joint bad-bin capacity is

$$
\boxed{aDT_D.}
$$

With `a=0.085` and `T_D<=1.83D`, this is

$$
0.15555D^2,
$$

strictly below the retained crossing mass. Thus one common bin contains two
distinct-label train families `A_D,B_D` with

$$
|A_D|,|B_D|\ge0.085D.
$$

The common-bin width is `O(1/D)`, while the label offset is exactly `pi/3`, so their
limiting projective terminal directions are exactly `pi/3` apart.

Canonical train decomposition counts two distinct physical boundary-end occurrences
per full train. Thus each family supplies endpoint density

$$
E_0=0.17.
$$

## 5. The Section-104 leakage theorem still applies at `sigma=1.4e-3`

The technical leakage companion used by Section 104 is scale-free once four geometric
inputs hold:

1. `delta<=10sigma/3` and `x_2,x_3,tau<=13sigma/3`;
2. the two support spans adjacent to the largest gap are at most `delta`;
3. the main support region admits the same oriented tangent-direction lift with total
   variation strictly below `pi`;
4. the finite-cover limits are taken in the stated order before removing the auxiliary
   cutoff.

Items 1 and 2 were reproved in Section 113. At maximal slack the total tail and span
perturbations are below `0.0061` radians while the principal angular separations retain
fixed margins of order `10^-1`; the main oriented support interval therefore remains
strictly below the `pi` tangent-variation threshold. Nothing in the finite-cover limit
order depends on the numerical size `10^-7` used in Section 104.

Thus the inherited leakage estimate

$$
L(\sigma,h)
=w(h)+\left({1\over h}+{169\over6}\right)\sigma,
\qquad
w(h)={\pi\over3}-\arccos((1+h)/2)
$$

remains valid.

At `h=0.0488`, `sigma=0.0014`, independent high-precision recomputation gives

$$
L=0.096533380382893\ldots,
$$

so each selected family leaves at least

$$
\boxed{P=0.17-L=0.073466619617107\ldots}
$$

normalized physical terminal-edge occurrences on the union of the three principal
corridors.

## 6. There is one global route-excess budget, not one budget per corridor

This point was checked explicitly because an incorrect factor two here would destroy
Section 113's endpoint.

For every fixed finite family of positive complement gaps, the exact Section-82 outer
ledger gives

$$
\sum_j\ell_j\le2\alpha.
$$

After the scale limit and exhaustion of the positive complement components,
nonnegativity gives the same inequality for the complete route family. Canonical
Section 101 gives

$$
C=\sum_j\sin(g_j/2),
\qquad
0\le2\alpha-C\le\sigma.
$$

Every route dominates its endpoint chord, so

$$
\boxed{
\sum_j\bigl(\ell_j-\sin(g_j/2)\bigr)\le\sigma.
}
$$

This is a single global normalized excess budget over all principal routes together.
There is no additional factor two. This is also the budget independently checked in
the Sections-107/108 hostile audit and used by the aggregate Section-112 proof-only
argument.

The terminal-edge occurrences selected from `A_D` and `B_D` are disjoint physical edge
occurrences. A selected unit edge on principal corridor `i`, with projective angle `d`
from that corridor chord, contributes at least

$$
1-\cos d
$$

to route length minus oriented chord projection. If its directed projection is
negative, the actual loss is larger, so using projective distance is conservative.
Therefore all selected A/B losses may be summed inside the one global budget:

$$
\sigma\ge
\sum_{F\in\{A,B\}}\sum_{i=1}^3
p_{F,i}
\left(1-\cos\operatorname{dist}_{RP^1}(u_F,q_i)\right).
$$

## 7. The two-family projective metric step is correct

For each family choose a nearest principal corridor and call the two nearest distances
`x,y`. Since each family has total principal endpoint density at least `P`, monotonicity
of `1-cos t` gives

$$
\sigma\ge P[(1-\cos x)+(1-\cos y)].
$$

If the two families choose the same principal corridor, the triangle inequality in
`RP^1` and `dist(u_A,u_B)=pi/3` give

$$
x+y\ge\pi/3.
$$

If they choose distinct principal corridors, the metric 1-Lipschitz inequality gives

$$
\left|
\operatorname{dist}_{RP^1}(q_i,q_j)-\pi/3
\right|
\le x+y,
$$

so the corridor mismatch bound yields

$$
x+y>m(\sigma).
$$

Because `1-cos t` is increasing and convex on `[0,pi/2]`, and because
`m(sigma)<pi/3` on this window, both cases imply

$$
\boxed{
\sigma\ge
2P\left(1-\cos{m(\sigma)\over2}\right).
}
$$

No Euclidean/projective-angle convention is mixed in this step: every distance is the
standard `RP^1` distance in `[0,pi/2]`.

## 8. Endpoint arithmetic and monotonicity close the stated window

At `sigma=0.0014`, direct high-precision recomputation gives

$$
\begin{aligned}
U(\theta_{17})+2\sigma&=1.829232020\ldots,\\
\operatorname{area}(\operatorname{conv}S)&\ge0.472929268\ldots,\\
P&=0.073466619617107\ldots,\\
m&=0.287223130294253\ldots,\\
2P(1-\cos(m/2))&=0.001512593891192\ldots .
\end{aligned}
$$

The final margin is therefore

$$
0.001512593891192\ldots-0.0014
=1.12593891192\times10^{-4}>0.
$$

For fixed `h=0.0488`, decreasing `sigma` decreases leakage, increases `P`, and increases
`m`, while the available route budget `sigma` decreases. Thus the contradiction is
monotone and holds on the entire interval

$$
0\le\sigma\le0.0014.
$$

## 9. Disposition

Section 113 survives this hostile review as a proof-only quantitative theorem. Under
the stated full-core Type-II hypotheses it excludes the entire carrier-angle window
through `theta_17` and supports the finite carrier conclusion

$$
\boxed{
\operatorname{diam}(P_*)
\ge(0.976073147411914233\ldots-o(1))D.
}
$$

The result does **not** settle C-II. It neither forces an exact unit equilateral
triangle nor supplies a source-preserving same-cardinality deformation of diameter
strictly below `D`.

The repository also contains duplicate/misaligned Section-109--112 numbering. Section
113 avoids making that a logical defect by rederiving the train count, joint-shore
bound, and aggregate projection argument. The numbering should still be normalized
before any audit.45 theorem-state promotion so authority points to an unambiguous
proof chain.

**Audit verdict:** PASS as proof-only. Theorem state unchanged.
