<!-- theorem-state: {"artifact_id":"ART-B5EB3C97391E","canonical":true,"claim_ids":["C-MU-09604"],"claim_statuses":{"C-MU-09604":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Erdős Problem #99 — three-gap attachment-perimeter repair of the five-component endpoint

**Date:** 2026-09-11  
**Target:** Target C, post-ZF C-II  
**Depends on:** certified FD lower bound and endpoint mass localization, C36/C40, FS.4, elementary planar Euler counting  
**Supersedes:** the unproved five-populated-arc step in `target_c_attachment_perimeter_capacity_five_arc_endpoint_2026-09-11.md`  

## LEVEL I STATUS

`STILL OPEN`.

The FD theorem gives

\[
\liminf\mu_D\ge z_*>0.9604,
\qquad
10\arcsin z_*-4\pi=z_*/3,
\qquad
z_*<0.961.
\]

At a hypothetical endpoint sequence `mu_D->z_*`, FD localizes all macroscopic component-diameter mass into one unloaded component `I` with

\[
\frac{\delta_I}{D}\to z_*,
\qquad
\frac{|A|}{D}\to z_*/3,
\]

where `A` is its distinct loaded attachment set. The limiting attachment directions are contained in an inclusion-maximal feasible circle set `M` with five connected components.

A previous September 11 report tried to exclude this endpoint by asserting that all five host components contain actual attachment pins. That assertion is stronger than the FD packing equality proves. It is unnecessary.

This report proves that the actual limiting attachment set must meet at least **three** host components, and three inter-component gaps already violate a direct attachment-perimeter upper bound.

Consequently the endpoint `mu_D->z_*` is impossible and there is a nonexplicit uniform gap above `z_*`.

## 1. Attachment-perimeter capacity

Let `I` be one unloaded component. Put

- `n=|I|`;
- `A` for its distinct loaded attachment set, `a=|A|`;
- `e` for internal contact edges of `I`;
- `t` for contact edges from `I` to `A`;
- `P_A=per(conv A)`.

### Lemma APC3.1

For every such component in the fully force-visible C-II class,

\[
\boxed{P_A\le4a-6.}
\]

More precisely, if

\[
s_I=e+t-2n-1\ge0,
\]

then

\[
\boxed{P_A\le4a-6-2s_I.}
\]

### Proof

Pin the loaded vertices. The C33/C40 pinned-rank argument gives full column rank `2n`, while the positive contact stress gives a nonzero left-kernel relation. Thus

\[
e+t=2n+1+s_I.
\tag{1.1}
\]

Consider the straight-line graph consisting of the vertices `I union A` and only the `e+t` internal/attachment contact edges. It is connected, simple, planar, and triangle-free. C36 gives `I subset conv A`, and every member of `A` is an extreme force-hull vertex, hence a vertex of `conv A`.

Let `b` be the outer-face boundary-walk length, with bridges counted twice. The outer walk contains every extreme vertex in `A`; its convex hull is therefore `conv A`. The closed-walk perimeter inequality gives

\[
b\ge P_A.
\tag{1.2}
\]

If `f` is the number of bounded faces, Euler gives

\[
f=e+t-(n+a)+1.
\]

Every bounded face walk has length at least four. Hence

\[
2(e+t)\ge b+4f
=b+4(e+t-n-a+1),
\]

so

\[
e+t\le2(n+a)-2-b/2.
\tag{1.3}
\]

Insert (1.1):

\[
2n+1+s_I\le2n+2a-2-b/2,
\]

which gives

\[
b\le4a-6-2s_I.
\]

Together with (1.2), this proves the lemma. `square`

The proof uses no equality classification of Eppstein's theorem.

## 2. Endpoint notation on the circle

Assume for contradiction that

\[
\mu_D\to z_*.
\]

Pass to the giant component supplied by FD. Scale by `D` and translate by the FS center. After taking a subsequence, its finite attachment sets converge to a closed set

\[
S\subset\{x:|x|=1/2\}
\]

with Euclidean diameter at most `z_*`.

Put

\[
\theta_*=2\arcsin z_*,
\qquad
\varphi_*=\pi-\theta_*.
\]

FD puts `S` inside an inclusion-maximal feasible set `M` with five connected components. TA's maximal-set identity gives

\[
|M|=\pi-5\varphi_*=z_*/3.
\tag{2.1}
\]

The five complementary gaps of `M` each have angular length at least

\[
2\varphi_*.
\tag{2.2}
\]

Indeed `T\setminus M=N_{\varphi_*}(M+\pi)` and, at maximality, the five component neighborhoods do not merge. Each complementary component is one component of `M+pi` expanded by `varphi_*` at both ends.

Because

\[
z_*<0.961<\sin(5\pi/12),
\]

we have

\[
\arcsin z_*<5\pi/12,
\qquad
\boxed{\varphi_*>\pi/6.}
\tag{2.3}
\]

The elementary radical inequality in (2.3) is rigorous: `sin^2(5pi/12)=(2+sqrt3)/4>37/40>(961/1000)^2`, using `sqrt3>17/10`.

Thus every host gap has length strictly greater than `pi/3`.

## 3. The actual attachment limit must wrap the center

Suppose first that

\[
0\notin conv S.
\]

Then the RA cap theorem gives

\[
\limsup\frac{area(conv A)}{D^2}
\le
B(z_*),
\qquad
B(z)=\frac{\arcsin z-z\sqrt{1-z^2}}4.
\tag{3.1}
\]

At the FD endpoint all other component-diameter mass is `o(D)`. The ordinary attachment diameter bound makes their total attachment-cell area `o(D^2)`. Hence

\[
\limsup C_{att}/D^2\le B(z_*).
\tag{3.2}
\]

JS with the nonnegative side cost discarded gives

\[
x:=\limsup\frac{d_P+Q}{D}\le\frac{2z_*+\pi}{3}.
\]

RP then gives

\[
\limsup G/D^2\le\frac{(2z_*+\pi)^2}{36\pi}.
\tag{3.3}
\]

The two right sides are far below the FSDB force-hull floor. A coarse exact estimate is enough.

From `z_*>0.9604`, `z_*<0.961`, and

\[
\sqrt{1-(0.961)^2}>0.276,
\]

we have

\[
z_*\sqrt{1-z_*^2}>0.265.
\]

Together with `arcsin z_*<5pi/12` and `pi<22/7`,

\[
B(z_*)
<\frac{5(22/7)/12-265/1000}{4}
=\frac{13708451}{52500000}.
\tag{3.4}
\]

Using `pi>3` in the denominator and `pi<22/7` in the numerator,

\[
\frac{(2z_*+\pi)^2}{36\pi}
<
\frac{(2(0.961)+22/7)^2}{108}
=\frac{34916281}{147000000}.
\tag{3.5}
\]

The sum of (3.4) and (3.5) is

\[
\frac{122166573}{245000000}<\frac12.
\]

But FSDB gives the stronger universal bound

\[
\liminf\frac{area(F)}{D^2}
>\frac{154451}{250000}>\frac12.
\]

Since `area(F)=C_att+G`, this is a contradiction. Therefore

\[
\boxed{0\in conv S.}
\tag{3.6}
\]

So the actual limiting attachment set is wrapping. This conclusion does not assume that every host component of `M` is populated.

## 4. Wrapping forces at least three occupied host components

### Lemma APC3.2

The set `S` meets at least three of the five connected components of `M`.

### Proof

Assume `S` meets at most two host components. On a cyclic list of five host components there is then a run of at least two consecutive unoccupied components.

Take the open circle arc beginning after the nearest occupied component before that run and ending before the nearest occupied component after it. This arc contains at least three complementary gaps of `M`, plus the intervening unoccupied host components. By (2.2)-(2.3), its angular length is greater than

\[
3(2\varphi_*)>\pi.
\]

The arc contains no point of `S`, because `S subset M` and all host components inside it are unoccupied. Hence all of `S` lies in the complementary arc of length `<pi`. A subset of the radius-`1/2` circle contained in an open semicircle cannot contain the origin in its convex hull. This contradicts (3.6). `square`

Thus three occupied components are forced purely by wrapping and the size of the five host gaps.

## 5. Three actual gaps already violate APC3.1

Because `S` meets at least three host components, the finite attachment sets have, for sufficiently large `D`, at least three cyclic transitions between occupied host-component neighborhoods. Each transition crosses at least one complementary gap of `M`. Therefore the corresponding angular gaps between consecutive actual attachment points satisfy

\[
\gamma_j\ge2\varphi_*-o(1),
\qquad j=1,2,3.
\tag{5.1}
\]

The wrapping limit and `diam S<=z_*<1` keep these consecutive minor gaps strictly below `pi`. FS.4 places all attachment points at radius `D/2+o(D)`. Hence each of the three corresponding edges of `conv A` has length at least

\[
D\sin\varphi_*-o(D).
\]

Consequently

\[
\boxed{
\liminf\frac{P_A}{D}
\ge3\sin\varphi_*.
}
\tag{5.2}
\]

On the other hand, APC3.1 and the FD endpoint pin count give

\[
\boxed{
\limsup\frac{P_A}{D}
\le4\frac{z_*}{3}.
}
\tag{5.3}
\]

But

\[
\sin\varphi_*
=\sin(2\arcsin z_*)
=2z_*\sqrt{1-z_*^2}.
\]

Thus (5.2) is strictly larger than (5.3) whenever

\[
6z_*\sqrt{1-z_*^2}>\frac{4z_*}{3},
\]

i.e. whenever

\[
\sqrt{1-z_*^2}>\frac29.
\tag{5.4}
\]

Equation (5.4) follows immediately from `z_*<0.961`, since

\[
(0.961)^2=\frac{923521}{10^6}<\frac{77}{81}
=1-\frac4{81}.
\]

Therefore (5.2) and (5.3) are incompatible.

### Theorem APE3 — five-component endpoint exclusion

There is no unbounded post-ZF C-II survivor sequence with

\[
\boxed{\mu_D\to z_*.}
\]

The proof requires only three populated host components, not five.

## 6. Uniform consequence

FD already proves

\[
\liminf\mu_D\ge z_*.
\]

If there were no uniform positive gap above `z_*`, choose survivors with `D_j->infinity` and

\[
\mu_{D_j}<z_*+1/j.
\]

FD forces `mu_{D_j}->z_*`, contradicting APE3. Hence:

### Corollary APG3

There exist absolute constants `epsilon_AP>0` and `D_0<infinity` such that every sufficiently large post-ZF C-II survivor satisfies

\[
\boxed{\mu_D\ge z_*+\epsilon_{AP}.}
\]

The present argument does not give a useful explicit value of `epsilon_AP` because FD's endpoint localization is qualitative.

## 7. Audit disposition

| Claim | Status |
| --- | --- |
| `P_A<=4|A|-6` | proved directly |
| FD `liminf mu_D>=z_*>0.9604` | certified by the PR #188 dependency audit |
| endpoint attachment set wraps | proved here by cap-area contradiction |
| endpoint meets at least three host components | proved here |
| five host components all contain actual pins | not proved and not needed |
| endpoint `mu_D->z_*` | excluded |
| uniform nonexplicit gap above `z_*` | proved |
| Level I | still open |

The previous five-gap endpoint report remains useful for its APC derivation, but its five-populated-arc passage should not be used. APE3 is the repaired endpoint theorem.
