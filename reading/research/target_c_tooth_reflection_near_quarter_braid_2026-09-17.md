> Generated reading edition · [exact source](../../research/target_c_tooth_reflection_near_quarter_braid_2026-09-17.md) · source SHA-256 `b2fa3983a7623ad638695aa5c5485dfbc5fd7c64d7552f928c390b7b680568a4`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 2 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "2916b51a2d8f5288a856490a015142c1231c1447", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_tooth_reflection_near_quarter_braid_2026-09-17.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "d43ae3df4e2e6d31b2a3b8379659eaadba03e0e30e5e94c5c5a749872e44d114"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — the reflection branch contains a near-quarter-power pairwise-crossing braid

**Date:** 2026-09-17  
**Status:** proof-only strengthening of the flat-cap reflection crossing braid; no canonical promotion claimed  
**Scope:** Type-II full-core shallow-tooth reflection branch  
**Dependencies:** shallow-tooth count/detour ledger; reflection/perimeter collapse; flat-cap crossing-braid theorem; same-center full-source disk sandwich; fixed-slack midpoint/star localization  
**Certificate:** `research/verify_target_c_tooth_reflection_near_quarter_braid_2026_09_17.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The first flat-cap crossing-braid theorem used the deliberately conservative normal-bin width

```math
w_D=D^{-1/8}
```

and obtained an explicit `Omega(D^(1/8))` family of pairwise vertex-disjoint, pairwise properly crossing reflection blockers.

The exponent loss is unnecessary. The geometric errors in that proof are only

```math
O(D^{-1/4}),
```

and the blocker midpoints lie in an `O(D^(3/4))` common central ball. Therefore one may take

```math
\boxed{
w_D=D^{-1/4}\log D.}
\tag{NQ.1}
```

Then

```math
O(D^{-1/4})=o(w_D)
```

while

```math
{D^{3/4}\over w_D}
=O\left({D\over\log D}\right)
=o(D).
```

Thus both the direction-separation and segment-crossing steps still work, but a normal bin now has capacity only `O(D^(3/4) log D)`. The linear blocked-tooth population therefore forces a near-quarter-power braid.

A fixed parameter can also be optimized for this objective. Use

```math
\boxed{\eta={3\over26}.}
\tag{NQ.2}
```

The current tooth ledger gives

```math
\boxed{
U_D>
(0.411394921870116\ldots-o(1))D
}
\tag{NQ.3}
```

upper-blocked `eta`-shallow teeth. Their bases have length at least

```math
\boxed{s_{min}=2-\eta={49\over26},}
\tag{NQ.4}
```

and their reflection blockers have fixed slack

```math
C_\eta^2=4\eta-\eta^2={303\over676}<1.
\tag{NQ.5}
```

After flat-cap purification, one normal bin of width (NQ.1) contains at most

```math
\boxed{
\left({13\over49}+o(1)\right)D^{3/4}\log D
}
\tag{NQ.6}
```

blocked bases. A winning normal quadrant, followed by one residue class modulo three, therefore gives a blocker family `B_D` with

```math
\boxed{
|B_D|>
(0.129220199818177\ldots-o(1))
{D^{1/4}\over\log D}.
}
\tag{NQ.7}
```

Every pair of edges in `B_D` is vertex-disjoint and crosses properly.

Thus the reflection branch has a geometric normal form at essentially the same exponent as the arbitrary fixed-slack matching theorem, losing only one logarithm in exchange for complete pairwise crossing.

---

## 1. Parameter-dependent blocked-tooth floor

Let

```math
N_2/D
\ge
0.4363893718701161781\ldots-o(1)
\tag{NQ.8}
```

be the current two-edge tooth floor and let

```math
{d_{out}\over D}
\le0.002883975+o(1).
\tag{NQ.9}
```

Every two-edge tooth base `s_i` contributes exactly

```math
2-s_i
```

to `d_out`. Hence for every fixed `eta>0`, the number of teeth with

```math
s_i<2-\eta
```

is at most

```math
{d_{out}\over\eta}.
```

Therefore

```math
{N_{sh}(\eta)\over D}
\ge
0.4363893718701161781\ldots
-{0.002883975\over\eta}
-o(1).
\tag{NQ.10}
```

For

```math
\eta={3\over26},
```

this is

```math
0.411394921870116\ldots-o(1).
\tag{NQ.11}
```

The global-turn theorem applies because the corresponding tooth half-angle is below `pi/6`. All but two shallow tooth occurrences have distinct apices.

The reflection/perimeter argument removes only `o(D)` exterior-witness teeth for every fixed admissible `eta`, so (NQ.3) follows.

---

## 2. Reflection slack at `eta=3/26`

For an `eta`-shallow tooth, write its height above the loaded base as

```math
h\le h_\eta
=\sqrt{\eta-\eta^2/4}.
```

Reflection moves the apex by at most

```math
C_\eta:=2h_\eta.
```

At (NQ.2),

```math
C_\eta^2
=4\eta-\eta^2
={303\over676},
```

so

```math
1-C_\eta^2={373\over676}>0.
\tag{NQ.12}
```

Every retained upper reflection blocker therefore has original length

```math
|xy|>D-C_\eta.
\tag{NQ.13}
```

The fixed-slack midpoint and star estimates remain uniform because `C_eta<1` is fixed.

---

## 3. Flat-cap purification is unchanged

Let

```math
E_D=\operatorname{per}(K)-\operatorname{per}(F)=o(D).
```

Set

```math
\tau_D=\sqrt{E_D/D}+D^{-1/4}.
```

As in the flat-cap crossing theorem, all but `o(D)` blocked bases have source-hull cap excess at most `tau_D`, and every such cap has depth

```math
H_D=o(1).
```

For a flat blocked base with inward normal `n`, tooth apex `x`, and upper blocker direction `d`, the same-center annulus gives

```math
\boxed{
\angle(d,n)=O(D^{-1/4})
}
\tag{NQ.14}
```

uniformly over the purified family.

The blocker midpoint also satisfies

```math
\boxed{|m-o|=O(D^{3/4}).}
\tag{NQ.15}
```

No parameter-dependent loss enters these exponents.

---

## 4. Near-quarter normal bins

Set

```math
w_D=D^{-1/4}\log D.
```

For large `D`, `w_D<pi/2`. Fix one angular bin of inward normals of width `w_D`.

The flat-cap boundary-projection theorem gives, for any fixed shallow threshold,

```math
\sum_{ab\text{ in bin}}|a-b|\cos(w_D/2)
\le
2S_D+2R_+\sin(w_D/2),
\tag{NQ.16}
```

where

```math
S_D=O(D^{3/4}),
\qquad
R_+={D\over2}+O(\sqrt D).
```

Now

```math
2S_D=o(D^{3/4}\log D)
```

and

```math
2R_+\sin(w_D/2)
=\left({1\over2}+o(1)\right)D^{3/4}\log D.
\tag{NQ.17}
```

At `eta=3/26`, every selected base has length at least `49/26`. Hence the number of flat blocked bases in one bin is at most

```math
\begin{aligned}
N_{bin}
&\le
{26\over49}
\left({1\over2}+o(1)\right)
D^{3/4}\log D\\
&=
\boxed{
\left({13\over49}+o(1)\right)D^{3/4}\log D.
}
\end{aligned}
\tag{NQ.18}
```

This proves (NQ.6).

---

## 5. Occupied-bin count

Partition the oriented normal circle into four fixed quadrants. One quadrant contains at least

```math
\left({U_D\over4}-o(D)\right)
```

flat blocked bases.

Using (NQ.3) and (NQ.18), the number of occupied `w_D` bins in that quadrant is at least

```math
\left(
{0.411394921870116\ldots/4\over13/49}
-o(1)
\right)
{D^{1/4}\over\log D}.
\tag{NQ.19}
```

Color the bins by their index modulo three and retain the largest color class. Two retained bins are separated by at least one full unused bin, so their inward normals differ by at least `2w_D`.

Choose one flat blocked tooth from every retained occupied bin. The selected count is

```math
\left(
0.411394921870116\ldots
{49\over156}
-o(1)
\right)
{D^{1/4}\over\log D}.
```

The coefficient is

```math
\boxed{0.129220199818177\ldots,}
```

proving (NQ.7).

---

## 6. Direction errors are negligible at the new scale

By (NQ.14), the blocker direction differs from its inward base normal by

```math
O(D^{-1/4}).
```

But

```math
{D^{-1/4}\over w_D}
={1\over\log D}
\to0.
\tag{NQ.20}
```

Therefore two blockers selected from the retained normal bins have projective line angle

```math
\theta\ge(2-o(1))w_D>w_D
\tag{NQ.21}
```

for sufficiently large `D`.

The same fixed-slack star argument as in the first crossing-braid theorem then shows that no two selected blocker edges share a source endpoint: any shared endpoint would have two fixed-slack near-diameter neighbors whose ray separation is at least `w_D`, while the star width is only `O(D^-1/4)=o(w_D)`.

Thus the selected blocker edges are pairwise vertex-disjoint.

---

## 7. Pairwise crossings remain inside the finite segments

Take two selected blocker edges with midpoints `m_1,m_2`, line angle `theta`, and lengths `ell_i>D-C_eta`.

By (NQ.15),

```math
|m_1-m_2|=O(D^{3/4}).
```

The intersection `z` of their supporting lines satisfies

```math
|z-m_i|
\le
{O(D^{3/4})\over\sin\theta}
\le
{O(D^{3/4})\over\sin w_D}.
```

Since `w_D->0`,

```math
\sin w_D\sim w_D=D^{-1/4}\log D,
```

so

```math
\boxed{
|z-m_i|=O\left({D\over\log D}\right)=o(D).
}
\tag{NQ.22}
```

But

```math
{\ell_i\over2}>{D-C_\eta\over2}.
```

Hence `z` lies in the relative interior of both blocker segments for all sufficiently large `D`. Every pair crosses properly.

---

## 8. Frontier effect

The reflection branch now has two complementary blocker normal forms:

```text
arbitrary disjoint matching:
    Omega(D^(1/4)) fixed-slack blockers;

ordered crossing braid:
    Omega(D^(1/4)/log D) fixed-slack blockers;
    pairwise vertex-disjoint;
    pairwise properly crossing;
    base normals cyclically separated;
    all crossings lie in an o(D) central region.
```

The second form is only a logarithm below the natural quarter-power ceiling set by the `O(D^(3/4))` midpoint uncertainty.

This still does not contradict a near-circular source: many inactive almost-diameters can cross pairwise. The exact next bridge is promotion or motion, not more combinatorial extraction. One must use the tooth/reflection tag to show that this near-quarter-power approximate thrackle either contains `D-o(1)`/actual diameter edges or supports a finite multi-tooth exchange that reduces the actual diameter graph while preserving unit separation.

**Disposition:** pushed the pairwise-crossing reflection family from `Omega(D^(1/8))` to `Omega(D^(1/4)/log D)` and simultaneously improved its explicit coefficient using the rational threshold `eta=3/26`. C-II and Level I remain open.
