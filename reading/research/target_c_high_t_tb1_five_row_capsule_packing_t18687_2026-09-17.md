> Generated reading edition · [exact source](../../research/target_c_high_t_tb1_five_row_capsule_packing_t18687_2026-09-17.md) · source SHA-256 `f7f6b6d6db9838b88fbc46bb9b3e79f767fa7708dc8f2eddc015f4ab1e24395a`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target C-II — exact capsule packing sharpens inverse-`D` near-unit bandwidth to five rows

**Date:** 2026-09-17  
**Status:** proof-only strengthening of the high-`t` exact-swap branch; no canonical promotion claimed  
**Scope:** selected O--O path coordinates in the one-sign strong-TB1 branch through `t=(q-k)/D<=1.8687`  
**Dependencies:** crossed-row rhombus-center capsule lemma; strict unit-rhombus inradius separation; six-row Oler blocker theorem; simultaneous exact-swap active-constraint decoupling; Horn poison-forest reduction; Oler O--O path-capacity theorem  
**Certificate:** `research/verify_target_c_high_t_tb1_five_row_capsule_packing_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The previous Oler argument proves that the centers of the rhombi crossed by an inverse-`D` near-unit source segment form a `sqrt(3)/2`-separated set in the radius-`1/2` capsule around that segment. Applying Oler directly gave path bandwidth at most six.

That bound is not sharp for this capsule. A finite exact packing certificate proves the stronger statement below.

> **Five-row capsule theorem.** Let
> 

$$

> S_L:=([0,L]\times\{0\})+B(0,1/2).
> 
$$


> If
> 

$$

> L\le {21\over20},
> 
$$


> and `X subset S_L` satisfies
> 

$$

> |x-x'|\ge {\sqrt3\over2}
> \qquad(x\ne x'),
> 
$$


> then
> 

$$

> \boxed{|X|\le5.}
> \tag{FP.1}
> 
$$


>
> The number five is sharp already for `L=1`.

Consequently every source pair with

$$
1<|x-y|\le1+{K\over D}
$$

crosses at most five selected O--O rows once `D>=20K`. In particular every inverse-`D` near-unit LOWER exact-swap blocker has

$$
\boxed{
|\operatorname{reg}(x)-\operatorname{reg}(y)|\le5
}
\tag{FP.2}
$$

for all sufficiently large sources.

This changes the Horn thinning scale again. One residue class modulo six is enough. The retained one-sign exact-swap system can therefore be taken with density

$$
\boxed{
\gamma_6={791\over3{,}840{,}000{,}000}
=2.05989583333\ldots\times10^{-7},
}
\tag{FP.3}
$$

which is exactly `7/6` times the seven-spaced density. The poison-forest and local-ladder conclusions propagate with the same factor.

---

## 1. The geometric input from the crossed-row center argument

Use the ordered selected O--O crosscuts

$$
R_0\xleftrightarrow{\tau_1}R_1
\xleftrightarrow{\tau_2}\cdots
\xleftrightarrow{\tau_m}R_m.
\tag{FP.4}
$$

Let source vertices `x,y` lie in regions `R_p,R_q`, `p<q`, and put

$$
L=|x-y|,
\qquad
N=q-p.
$$

The segment `xy` meets every separating selected row. For every crossed row choose one strict unit rhombus whose midpoint centerline meets `xy`, and let `c_j` be its rhombus center.

The previous center-capsule proof gives two facts that do not use TB1 or KKT stress:

1. the midpoint centerline has length one and its midpoint is `c_j`, so
   $$
   \operatorname{dist}(c_j,xy)\le {1\over2};
   $$
2. every strict unit rhombus has inradius greater than `sqrt(3)/4`, and distinct selected rows use distinct contact faces with disjoint interiors, so
   $$
   |c_i-c_j|\ge {\sqrt3\over2}
   \qquad(i\ne j).
   $$

After a rigid motion taking `xy` to `[0,L] x {0}`, the `N` centers form a `sqrt(3)/2`-separated subset of `S_L`. Thus (FP.1) immediately implies `N<=5` whenever `L<=21/20`.

For a near-unit blocker with

$$
L\le1+{K\over D},
$$

we have `L<=21/20` as soon as `D>=20K`. This proves (FP.2).

---

## 2. Exact finite proof of the capsule packing theorem

The certificate uses a rational square cover; no floating-point decision enters the upper bound.

Take the grid of closed squares

$$
Q_{ij}
=
\left[{i\over24},{i+1\over24}\right]
\times
\left[{j\over24},{j+1\over24}\right].
\tag{FP.5}
$$

Retain every square whose closure intersects `S_{21/20}`. The exact segment-distance test leaves

$$
\boxed{1096}
\tag{FP.6}
$$

squares. The test is performed after scaling all coordinates by `24*20=480`, so it is an integer comparison against the squared radius.

Every grid square has squared diameter

$$
{2\over24^2}={1\over288}<{3\over4}.
\tag{FP.7}
$$

Therefore a `sqrt(3)/2`-separated set contains at most one point in each retained square.

Build a graph `G` on the 1096 retained squares. Two squares are adjacent only when their containing rectangles could possibly hold two points at distance at least `sqrt(3)/2`. Explicitly, for rectangles

$$
Q=[x_0,x_1]\times[y_0,y_1],
\qquad
Q'=[X_0,X_1]\times[Y_0,Y_1],
$$

set

$$
\Delta_x=
\max\{|x_0-X_1|,|x_1-X_0|\},
\qquad
\Delta_y=
\max\{|y_0-Y_1|,|y_1-Y_0|\}.
$$

The edge is retained exactly when

$$
\Delta_x^2+\Delta_y^2\ge {3\over4}.
\tag{FP.8}
$$

Because the grid coordinates have denominator 24, (FP.8) is the integer test

$$
4(a^2+b^2)\ge3\cdot24^2.
\tag{FP.9}
$$

Any six admissible points would occupy six distinct retained squares, and every pair of those squares would satisfy (FP.8). Hence six admissible points would create a `K_6` in `G`.

The certificate performs an exhaustive branch-and-bound clique decision using Python integer bitsets. A greedy coloring is used only as a rigorous upper bound for pruning; absence of `K_6` is not inferred from a heuristic coloring. The search visits 320050 recursive nodes and returns

$$
\boxed{G\text{ contains no }K_6.}
\tag{FP.10}
$$

The clique routine is also checked against brute-force enumeration on deterministic small random graphs before it is used on `G`.

Equations (FP.5)--(FP.10) prove the upper bound `|X|<=5`.

### Sharpness at `L=1`

The following five rational points all lie in `S_1`:

$$
\left(-{1\over2},0\right),
\quad
\left({1\over4},{1\over2}\right),
\quad
\left({1\over4},-{1\over2}\right),
\quad
\left({6\over5},{9\over20}\right),
\quad
\left({6\over5},-{9\over20}\right).
\tag{FP.11}
$$

A direct rational check gives squared pairwise distances at least `3/4`. Thus the packing number is exactly five at `L=1`; the certificate is proving a genuine packing threshold, not merely improving the previous Oler arithmetic.

---

## 3. Six-spacing removes all LOWER multi-coordinate coupling

Let

$$
s_0={791\over320{,}000{,}000}.
$$

The one-sign strong-TB1 population satisfies

$$
|M_D|>{s_0\over2}D-o(D).
\tag{FP.12}
$$

Partition its layer indices into the six residue classes modulo six and retain a largest class `P_D^0`. Then

$$
|P_D^0|
>{s_0\over12}D-o(D)
=(\gamma_6-o(1))D,
\tag{FP.13}
$$

and distinct retained indices differ by at least six.

The retained layers are therefore nonadjacent, so the simultaneous exact-swap active-contact/old-diameter decoupling theorem still applies. By (FP.2), a LOWER singleton blocker owned by one retained layer cannot have its other endpoint in another retained layer. It is a permanent one-coordinate constraint.

Delete the `O(1)` retained coordinates incident to the source-wide genuine-upper binary exceptions exactly as in the seven-spaced reduction. This changes (FP.13) only by `O(1)`. No genuinely new two-coordinate obstruction remains, and the Horn implication reduction applies verbatim.

The previous seven-spacing proof used no additional numerical property of seven. Its requirements were:

- retained coordinates are nonadjacent;
- a LOWER blocker cannot contain two retained endpoint layers;
- the bounded genuine-upper binary exception is removed.

Spacing six plus (FP.2) satisfies all three.

---

## 4. Horn and LOWER-ladder constants

Substituting `gamma_6` for `gamma_7`, the poison-forest theorem forces one of

$$
\boxed{
N_{\rm permanent\ lower}
>
\left({\gamma_6\over4}-o(1)\right)D
=
(5.14973958333\ldots\times10^{-8}-o(1))D,
}
\tag{FP.14}
$$

$$
\boxed{
N_{\rm permanent\ upper}
>
\left({\gamma_6\over8}-o(1)\right)D
=
(2.57486979167\ldots\times10^{-8}-o(1))D,
}
\tag{FP.15}
$$

or

$$
\boxed{
N_{\rm implication\ forest}
>
\left({\gamma_6\over2}-o(1)\right)D
=
(1.02994791667\ldots\times10^{-7}-o(1))D.
}
\tag{FP.16}
$$

In the permanent LOWER branch, orient blockers by which side contains the nonowner endpoint. The owners are six-spaced and every support interval has depth at most five. Hence the oriented support intervals are pairwise disjoint. The same global train-defect/terminal-variation extraction gives more than

$$
\boxed{
\left({\gamma_6\over16}-o(1)\right)D
=
(1.28743489583\ldots\times10^{-8}-o(1))D
}
\tag{FP.17}
$$

good five-deep windows, each with a pure common column family of size

$$
(0.6436-o(1))D.
$$

Using the complete-train bound

$$
T_D<(T_*+o(1))D,
\qquad
T_*={6121\over2000},
$$

one fixed train threads more than

$$
\boxed{
\left(
{\gamma_6\over16}{0.6436\over T_*}-o(1)
\right)D
=\left(
{1{,}272{,}719\over470{,}092{,}800{,}000{,}000}-o(1)
\right)D
}
\tag{FP.18}
$$

such pairwise-disjoint local ladders. Numerically the coefficient is

$$
2.70737820277\ldots\times10^{-9}.
$$

The local geometric seam is correspondingly smaller: every permanent LOWER blocker now crosses at most five inverse-`D` near-equilateral selected rows.

---

## 5. UPPER localization inherits the same `7/6` gain

Every upper Horn extraction whose input coefficient is linear in the retained density improves by the exact factor

$$
{\gamma_6\over\gamma_7}={7\over6}.
\tag{FP.19}
$$

In particular, combine six-spacing with the current Oler O--O path-capacity coefficient

$$
A_*={14\over3\sqrt3}.
\tag{FP.20}
$$

The same-type localized upper family obtained by the path-incidence argument can use coefficient

$$
\widehat c_{*,6}
={\gamma_6\over48A_*}
=
\boxed{
{113\sqrt3\over122{,}880{,}000{,}000}
}
=1.59278760787\ldots\times10^{-9}.
\tag{FP.21}
$$

This is exactly `7/6` times the current seven-spaced Oler-path coefficient. The flexible-scale COMMON-CUT/LOCAL-WINDOW alternatives are unchanged structurally; only their input-density constants improve.

---

## 6. Frontier effect

The improvement is finite and structural rather than a new decimal optimization:

```text
near-unit center packing:
    old Oler theorem:      bandwidth <= 6
    exact capsule theorem: bandwidth <= 5

exact-swap thinning:
    old retained spacing:  7
    new retained spacing:  6

retained Horn density:
    old gamma_7 = 1.765625e-7
    new gamma_6 = 2.05989583333e-7
    gain = 7/6

permanent LOWER geometry:
    pairwise-disjoint support windows now have depth <= 5;
    one fixed transverse train still threads linearly many of them.
```

This does **not** close C-II. The exact remaining obstruction is still metric:

- LOWER: classify or rule out a strict near-unit source chord crossing at most five co-phased rows in the repeated local ladder;
- UPPER SIGNED/THIN: convert the localized train-fence order into a strict metric contradiction or a diameter-reducing move.

The five-row theorem removes one more layer of combinatorial slack from the LOWER branch and increases every Horn-derived upper population by a fixed factor, but it does not by itself produce the required source-preserving strict diameter decrease.

**Disposition:** proved by exact finite certificate that the near-unit rhombus-center capsule has packing number five throughout `L<=21/20`; sharpened inverse-`D` LOWER path bandwidth from six to five; upgraded the retained Horn subsystem from seven-spacing to six-spacing; propagated the improved density through the LOWER ladder and current Oler-path UPPER localization. C-II and Level I remain open.
