> Generated reading edition · [exact source](../../research/target_c_high_t_tb1_thin_partner_star_bandwidth_t18687_2026-09-17.md) · source SHA-256 `1dd1c7b597a4b465825dc2a3f2dbf7a2dbb127a6742ab070a4c3bcdd00a71dc2`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 25 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

# Target C-II — fifteen-spaced THIN partner stars have a sharpened `D^(3/4)` cap

**Date:** 2026-09-17  
**Status:** proof-only continuation of the THIN rich-cut / linear weak-rail branch; no canonical promotion claimed  
**Scope:** THIN blockers on the phase-pure blocker-rich row in the 15-spaced one-sign strong-TB1 Horn subsystem through `t=(q-k)/D<=1.8687`  
**Dependencies:** THIN rich-cut phase synchronization; linear THIN weak rail; short-pair path-bandwidth lemma; full-source circumradius estimate; superdiameter geometric-thrackle theorem  
**Certificate:** `research/verify_target_c_high_t_tb1_thin_partner_star_bandwidth_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The latest THIN weak-rail theorem leaves one explicit defect relative to the active-diameter rail: many distinct fifteen-spaced owners may share one opposite-shore partner vertex. The generic inactive near-diameter degree theorem bounds such a star by

```math
(8\,3^{1/8}+o(1))D^{3/4},
```

but it ignores the path spacing of the owners.

The path spacing is useful. If one partner `q` is joined to `d` THIN owners in retained layers whose indices are pairwise at least fifteen apart, then the two extreme owners are separated by at least `15(d-1)` selected O--O rows. The short-pair path-bandwidth theorem turns that index separation into a Euclidean lower bound on the extreme-owner chord. The fact that both extreme owners are almost diametrically far from the same `q`, together with the full-source circumradius estimate, gives a competing `O(D^(3/4))` upper bound on that same chord.

The resulting star bound is

```math
\boxed{
 d<1+{8\Xi_D+2\pi\sqrt3\over15},
}
\tag{PS.1}
```

where

```math
\eta_D=3^{1/4}\sqrt D,
\qquad
\ell_D=D-{1\over4D},
\qquad
\Xi_D=\sqrt{(D+2\eta_D)^2-\ell_D^2}.
\tag{PS.2}
```

Since

```math
\Xi_D=(2\,3^{1/8}+o(1))D^{3/4},
```

this is

```math
\boxed{
 d<\left({16\,3^{1/8}\over15}+o(1)\right)D^{3/4}.
}
\tag{PS.3}
```

The leading coefficient is

```math
{16\,3^{1/8}\over15}=1.22368286980\ldots,
```

a factor `7.5` smaller than the generic inactive near-diameter coefficient `8*3^(1/8)`.

This does not make partner multiplicity bounded. It does remove the generic degree estimate from the synchronized THIN row and gives a source-specific spread law for every repeated-partner plateau.

As a consequence, the phase-pure blocker-rich row itself contains a vertex-disjoint pairwise-crossing THIN matching of size

```math
\boxed{
\left(
 {15\gamma\over2560\,3^{1/8}}-o(1)
\right)D^{1/4}
}
\tag{PS.4}
```

with

```math
\gamma={791\over9{,}600{,}000{,}000},
```

so the coefficient is

```math
\boxed{
4.20839394782\ldots\times10^{-10}.
}
\tag{PS.5}
```

Every edge in this matching still crosses the same inverse-`D` phase-pure row `tau_*`, whose retained common transverse family has size `(0.6436-o(1))D` and whose two circumcenter flank families each have density `0.0547027254...-o(1)`.

After fixing one physical owner host and one monotone partner-region run, one obtains a synchronized endpoint-disjoint staircase/nested rail of size

```math
\boxed{
\left(
 {15\gamma\over10240\,3^{1/8}}-o(1)
\right)D^{1/4}
=
(1.05209848696\ldots\times10^{-10}-o(1))D^{1/4}.
}
\tag{PS.6}
```

Thus partner repetition remains a linear-scale issue, but it can no longer erase an unbounded genuine crossing rail inside the same phase-pure train scaffold.

---

## 1. A common-partner THIN triangle is acute

Let

```math
qp,
\qquad
qp'
```

be two distinct THIN blockers sharing the partner endpoint `q`. The THIN condition gives

```math
\ell_D<|q-p|,|q-p'|<D,
\qquad
\ell_D=D-{1\over4D}.
\tag{PS.7}
```

Unit separation and the source diameter bound give

```math
1\le |p-p'|\le D.
\tag{PS.8}
```

Write

```math
a=|q-p|,
\qquad
b=|q-p'|,
\qquad
c=|p-p'|.
```

For `D>1`,

```math
2\ell_D^2-D^2
=D^2-1+{1\over8D^2}>0.
\tag{PS.9}
```

Hence

```math
a^2+b^2>D^2\ge c^2,
```

so the angle at `q` is acute.

At either leaf,

```math
\ell_D^2+1-D^2
={1\over2}+{1\over16D^2}>0.
\tag{PS.10}
```

Thus

```math
a^2+c^2>D^2>b^2,
\qquad
b^2+c^2>D^2>a^2,
```

and the two leaf angles are acute as well.

Therefore the triangle `qpp'` is acute. Its minimum enclosing circle is its circumcircle.

The full source lies in the canonical circumdisk

```math
K\subset B(o,R_D),
\qquad
R_D<{D\over2}+\eta_D,
\qquad
\eta_D=3^{1/4}\sqrt D.
\tag{PS.11}
```

Since the three triangle vertices lie in `K`, their minimum enclosing radius is at most `R_D`. Hence their circumradius `R_\triangle` satisfies

```math
\boxed{R_\triangle\le R_D.}
\tag{PS.12}
```

---

## 2. Two leaves of one THIN star are only `O(D^(3/4))` apart

Let

```math
\theta=\angle pqp'.
```

The law of cosines in half-angle form gives

```math
c^2=(a-b)^2+4ab\sin^2{\theta\over2}
\ge4\ell_D^2\sin^2{\theta\over2}.
\tag{PS.13}
```

Since

```math
R_\triangle={c\over2\sin\theta},
```

(PS.13) implies

```math
R_\triangle
\ge {\ell_D\over2\cos(\theta/2)}.
\tag{PS.14}
```

Combine this with (PS.11)--(PS.12):

```math
\boxed{
\cos{\theta\over2}
>{\ell_D\over D+2\eta_D}.
}
\tag{PS.15}
```

Now

```math
c
=2R_\triangle\sin\theta
\le2R_D\sin\theta
<(D+2\eta_D)\sin\theta.
\tag{PS.16}
```

Using

```math
\sin\theta
=2\sin{\theta\over2}\cos{\theta\over2}
\le2\sin{\theta\over2}
```

and (PS.15),

```math
\sin{\theta\over2}
<
\sqrt{1-{\ell_D^2\over(D+2\eta_D)^2}}.
```

Therefore

```math
\boxed{
|p-p'|=c
<2\sqrt{(D+2\eta_D)^2-\ell_D^2}
=2\Xi_D.
}
\tag{PS.17}
```

The quantity under the square root has the exact expansion

```math
\begin{aligned}
\Xi_D^2
&=(D+2\eta_D)^2-\left(D-{1\over4D}\right)^2\\
&=4D\eta_D+4\eta_D^2+{1\over2}-{1\over16D^2}.
\end{aligned}
\tag{PS.18}
```

Since `eta_D=3^(1/4)D^(1/2)`, this gives

```math
\boxed{
\Xi_D=(2\,3^{1/8}+o(1))D^{3/4}.
}
\tag{PS.19}
```

No diameter activity of the THIN chords is used.

---

## 3. Fifteen-spaced owner tags force leaf spread

Now let one partner vertex `q` be shared by `d` THIN blockers in the owned Horn family. Write their distinct owner region indices in increasing order:

```math
i_1<i_2<\cdots<i_d.
\tag{PS.20}
```

The retained Horn coordinates are fifteen-spaced, so

```math
\boxed{i_d-i_1\ge15(d-1).}
\tag{PS.21}
```

Let `p_1,p_d` be the corresponding owner endpoints. They lie in path regions `R_{i_1},R_{i_d}`. The phase-free exact path support theorem says that the segment `p_1p_d` is separated by exactly

```math
N=i_d-i_1
```

selected O--O rows.

The short-pair path-bandwidth lemma is valid for an arbitrary source segment of length `L`, not only a near-unit blocker:

```math
N<4L+2\pi\sqrt3.
\tag{PS.22}
```

Hence

```math
15(d-1)
<4|p_1-p_d|+2\pi\sqrt3.
\tag{PS.23}
```

Equivalently every repeated-partner star obeys the **leaf-spread lower bound**

```math
\boxed{
|p_1-p_d|
>{15(d-1)-2\pi\sqrt3\over4}.
}
\tag{PS.24}
```

This statement is useful independently of the circumradius estimate: a long repeated-partner plateau must occupy a proportionally long Euclidean chord on its owner shore.

---

## 4. Combine the two bounds: sharpened partner-star capacity

Apply (PS.17) to the same extreme leaves in (PS.23):

```math
15(d-1)
<8\Xi_D+2\pi\sqrt3.
```

Thus

```math
\boxed{
 d<1+{8\Xi_D+2\pi\sqrt3\over15}.
}
\tag{PS.25}
```

By (PS.19),

```math
\boxed{
 d<
\left({16\,3^{1/8}\over15}+o(1)\right)D^{3/4}.
}
\tag{PS.26}
```

The generic inactive near-diameter theorem has coefficient `8*3^(1/8)`. Their ratio is exactly

```math
{8\,3^{1/8}\over(16/15)3^{1/8}}
={15\over2}=7.5.
\tag{PS.27}
```

The gain comes entirely from the fifteen-spaced physical owner tags. It is not a stronger source-wide degree theorem.

---

## 5. The blocker-rich row contains a synchronized crossing matching

The THIN rich-cut theorem gives one row `tau_*` and a blocker family `T_*` with

```math
|T_*|>
\left({\gamma\over80}-o(1)\right)D,
\qquad
\gamma={791\over9{,}600{,}000{,}000},
\tag{PS.28}
```

such that:

- every blocker crosses `tau_*`;
- every blocker is THIN and therefore superdiameter;
- all owner coordinates are distinct and fifteen-spaced;
- `tau_*` carries the common phase-pure train family and circumcenter flanks.

Each blocker owner lies on one of the two complementary shores of `tau_*`. Keep the larger owner-shore class `T_1`:

```math
\boxed{|T_1|\ge {|T_*|\over2}.}
\tag{PS.29}
```

All owner vertices in `T_1` are distinct and lie on one shore; every partner vertex lies on the opposite shore. Therefore an owner vertex cannot equal any partner vertex within `T_1`.

For a fixed partner vertex, its incident edges in `T_1` have fifteen-spaced owner tags, so (PS.25)--(PS.26) bound its multiplicity by

```math
\Delta_*<
\left({16\,3^{1/8}\over15}+o(1)\right)D^{3/4}.
\tag{PS.30}
```

Choose one blocker for every distinct partner vertex occurring in `T_1`. The chosen blockers have distinct owners and distinct partners, hence are vertex-disjoint. Their number is at least

```math
{|T_1|\over\Delta_*}.
```

Using (PS.28)--(PS.30),

```math
\boxed{
M_D^{sync}
>
\left(
{15\gamma\over2560\,3^{1/8}}-o(1)
\right)D^{1/4}.
}
\tag{PS.31}
```

Numerically,

```math
{15\gamma\over2560\,3^{1/8}}
=4.20839394782\ldots\times10^{-10}.
\tag{PS.32}
```

Every two chosen blockers are vertex-disjoint superdiameter chords, so the superdiameter-thrackle theorem makes them cross properly.

Unlike the older unsynchronized inactive matching, this matching is already supported on the same row `tau_*` with bounded total angular defect and the same `(0.6436-o(1))D` inverse-`D` common train family.

---

## 6. Recover an endpoint-disjoint ordered rail inside the same scaffold

Starting from the matching in Section 5, fix one physical owner host, losing at most a factor `2`. The owner tags then occur in strict path order along the host. Pairwise crossing orders the distinct partners on the opposite shore.

The opposite-shore region word has one turn. Keep one monotone run, losing at most one more factor `2`. The exact selected-cut supports are then either a staircase or a strictly nested family exactly as in the inactive common-cut rail theorem.

Therefore the same phase-pure row contains an endpoint-disjoint ordered rail of size

```math
\boxed{
M_D^{rail}
>
\left(
{15\gamma\over10240\,3^{1/8}}-o(1)
\right)D^{1/4}.
}
\tag{PS.33}
```

The coefficient is

```math
\boxed{
{15\gamma\over10240\,3^{1/8}}
=1.05209848696\ldots\times10^{-10}.
}
\tag{PS.34}
```

Every retained rail chord simultaneously has:

```text
D - 1/(4D) < |e| < D;
vertex-disjoint endpoints across the retained rail;
pairwise proper crossing;
one common blocker-rich selected row tau_*;
distinct fifteen-spaced owner tags;
one fixed physical owner host;
staircase or strictly nested exact path supports;
> (0.6436-o(1))D inverse-D near-60 columns on tau_*;
and both common 0.01D circumcenter flanks.
```

---

## 7. What this does and does not remove

The latest THIN audit identified partner repetition as the only reason the new linear weak rail was not already a genuine endpoint-disjoint rail. The present theorem quantifies that repetition using information specific to the Horn branch:

```text
repeated partner of multiplicity d
=> owner-index span at least 15(d-1)
=> extreme owners are Euclidean distance Omega(d)
=> common near-diameter partner + near-circular source gives distance O(D^(3/4))
=> d <= (16*3^(1/8)/15+o(1))D^(3/4).
```

So partner repetition cannot erase an unbounded endpoint-disjoint ordered rail from the **same phase-pure blocker-rich row**. It only costs the unavoidable `D^(3/4)` star scale supplied by the present circumradius error.

This is not a C-II closure. The linear weak rail can still consist of `Theta(D^(1/4))` or more sublinear stars, and the extracted synchronized crossing rail is only `Omega(D^(1/4))`. To improve the exponent one needs a sharper metric restriction on a common superdiameter star than the source-wide `R_D-D/2=O(sqrt D)` circumradius error, or a direct contradiction between one repeated star and the local train scaffold.

**Disposition:** sharpened THIN partner multiplicity by combining fifteen-spaced path bandwidth with the near-circular source bound, and recovered an endpoint-disjoint pairwise-crossing staircase/nested rail inside the same phase-pure dense-grid row. C-II and Level I remain open.
