> Generated reading edition · [exact source](../../research/target_c_high_t_tb1_thin_growing_braid_fixed_bracket_t18687_2026-09-17.md) · source SHA-256 `c2b25eccdec29cfaadb2de3da3ef8af585f281d1e7dea63be5a495cc404d40b3`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "2a17dd77c260378be04717216c4b551b60f76e44", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_high_t_tb1_thin_growing_braid_fixed_bracket_t18687_2026-09-17.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "95c9d12c2e8a9659a055e533c424722851620acf441c847c87278fa9e03711ec"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — the growing THIN braid can be trapped between one fixed circumcenter-bracketing train pair

**Date:** 2026-09-17  
**Status:** proof-only continuation of the THIN growing-braid common-spine theorem; no canonical promotion claimed  
**Scope:** THIN side of the 15-spaced one-sign strong-TB1 Horn upper family through `t=(q-k)/D<=1.8687`  
**Dependencies:** THIN growing-braid common spine; low-defect rich-row purification; exact train-step metric bound; full-source circumdisk bound; triangle-free complete-train crossing graph; THIN near-diameter midpoint localization  
**Certificate:** `research/verify_target_c_high_t_tb1_thin_growing_braid_fixed_bracket_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The current THIN frontier contains a slowly growing pairwise-crossing matching of inactive almost-diameters and one fixed complete train through `D^(1-o(1))` common inverse-`D` phase rows. The rowwise circumcenter flanks can be synchronized too.

The key point is that every low-defect rich row has not merely one large purified train family. Its purified crossing centers contain **linear left and right flank sets** below `-0.01D` and above `+0.01D`. Counting

```math
(\text{row},\ \text{THIN braid},\ \text{left flank train},\ \text{right flank train})
```

instead of the previous `(row, braid, train)` tuples forces one fixed ordered pair of complete trains through the same growing braid ladder.

Let

```math
\gamma={791\over9{,}600{,}000{,}000},
\qquad
N:=|T_D|>\left({\gamma\over16}-o(1)\right)D,
\tag{FB.1}
```

and retain the audited constants

```math
p_0={1609\over2500}=0.6436,
\qquad
T_*={6121\over2000}=3.0605.
\tag{FB.2}
```

At flank level

```math
\mu=0.01,
```

put

```math
\boxed{
q_0:=p_0-{1.02\over\sqrt3}
=0.05470272542658\ldots .
}
\tag{FB.3}
```

Then for every fixed positive integer `r`, there exist

- an `r`-edge vertex-disjoint THIN matching `F_*`;
- two fixed complete trains `b_-`, `b_+`;
- a common row family `A_D^{br}(r)`;

such that every two edges of `F_*` cross properly, every edge of `F_*` crosses every row in `A_D^{br}(r)`, both fixed trains cross every such row, and

```math
\boxed{
|A_D^{br}(r)|>
\left(
{3q_0^2\over4T_*^2 5^r}-o(1)
\right)N.
}
\tag{FB.4}
```

All rows in `A_D^{br}(r)` have one common projective phase to `O(D^-1)`. On every one of them, after orienting by that phase,

```math
\boxed{
h_a(z_{a,b_-})<-0.01D,}
\tag{FB.5}
```

```math
\boxed{
h_a(z_{a,b_+})>+0.01D.}
\tag{FB.6}
```

Thus the same two actual complete trains bracket the circumcenter corridor on every retained row.

For `r=2`, the coefficient in (FB.4) is

```math
9.58416796134773\ldots\times10^{-6}
```

relative to `N`, hence

```math
\boxed{
|A_D^{br}(2)|>
(4.93559691238675\times10^{-14}-o(1))D.
}
\tag{FB.7}
```

The important statement is asymptotic rather than the small explicit coefficient. As in the preceding braid theorem, choose `r=r_D->infinity` sufficiently slowly. The same count gives

```math
\boxed{|F_D|=r_D\to\infty}
\tag{FB.8}
```

and

```math
\boxed{|A_D^{br}|=D^{1-o(1)}.}
\tag{FB.9}
```

Every pair of chords in `F_D` crosses properly, and all chords share one consecutive exact selected-cut support block of length at least `D^(1-o(1))`. The two fixed bracket trains need only be asserted on the retained `D^(1-o(1))` phase rows, not on every row of that consecutive support block.

This replaces the THIN frontier

```text
growing crossing braid
+ one train spine
+ near-linear common row family
```

by

```text
growing crossing braid
+ one fixed noncrossing train pair b_-, b_+
+ the same train pair bracketing -0.01D and +0.01D on every retained row
+ D^(1-o(1)) common inverse-D phase rows
+ one common consecutive braid-support block of D^(1-o(1)) rows.
```

No inactive THIN chord is promoted to an actual diameter or a KKT-loaded edge.

---

## 1. Inputs from the growing-braid theorem

Use the low-defect rich-row family `R_D` from the current THIN growing-braid state. Uniformly over `a in R_D`, let

- `B_a subset T_D` be the THIN blockers whose exact selected-cut support contains `a`;
- `P_a` be the purified complete-train family on `a`.

The audited estimates are

```math
\boxed{|R_D|>\left({3\over2}-o(1)\right)N,}
\tag{FB.10}
```

```math
\boxed{|B_a|>\left({1\over5}-o(1)\right)N,}
\tag{FB.11}
```

```math
\boxed{|P_a|>(p_0-o(1))D,}
\tag{FB.12}
```

and for every `b in P_a`,

```math
0<\theta(a,b)-{\pi\over3}\le {C_0\over D}
\tag{FB.13}
```

for one source-independent constant `C_0`.

The blocker graph on each rich row has

```math
\Delta(B_a)=O(D^{3/4})=o(N).
\tag{FB.14}
```

Therefore, for fixed `r`, the number `M_r(a)` of unordered `r`-edge matchings in `B_a` satisfies

```math
\boxed{
M_r(a)>
\left({1\over r!5^r}-o(1)\right)N^r.
}
\tag{FB.15}
```

Every edge in every such matching is THIN:

```math
D-{1\over4D}<|e|<D,
\qquad
|e|>\sqrt{D^2-1}.
\tag{FB.16}
```

Hence every matching is a pairwise-properly-crossing straight-line braid by the superdiameter-thrackle theorem.

The global complete-train count is

```math
\boxed{
T_{\rm all}\le(T_*+o(1))D.
}
\tag{FB.17}
```

---

## 2. Every rich low-defect row has purified `+-0.01D` flanks

Fix `a in R_D`. Orient the row track-edge unit vector `u_a` so that

```math
h_a(x):=\det(u_a,x-o)
\tag{FB.18}
```

strictly increases along the crossing-center order of `P_a`.

The exact train-step inequality gives an increment greater than

```math
{\sqrt3\over2}
```

between consecutive selected crossing centers. The full source lies in a circumdisk of radius

```math
R_D={D\over2}+o(D).
```

The number of crossing centers in `P_a` with

```math
h_a(z)\ge-0.01D
```

is therefore at most

```math
\left({1.02\over\sqrt3}+o(1)\right)D.
\tag{FB.19}
```

Since `|P_a|>(p_0-o(1))D`, the initial flank

```math
P_a^-:=\{b\in P_a:h_a(z_{a,b})<-0.01D\}
```

has

```math
\boxed{|P_a^-|>(q_0-o(1))D.}
\tag{FB.20}
```

The symmetric terminal count gives

```math
P_a^+:=\{b\in P_a:h_a(z_{a,b})>+0.01D\},
```

```math
\boxed{|P_a^+|>(q_0-o(1))D.}
\tag{FB.21}
```

The same `q_0` is the rowwise flank constant already implicit in the common-spine theorem. Here it will be double-counted across the braid.

---

## 3. Fixed-`r` braid plus fixed bracket pair

Fix `r>=1`. Count quadruples

```math
(a,F,b_-,b_+)
\tag{FB.22}
```

with

```math
a\in R_D,
\qquad
F\text{ an }r\text{-edge matching in }B_a,
\qquad
b_-\in P_a^-,
\qquad
b_+\in P_a^+.
```

By (FB.10), (FB.15), (FB.20), and (FB.21),

```math
\#\{(a,F,b_-,b_+)\}
>
\left(
{3q_0^2\over2r!5^r}-o(1)
\right)N^{r+1}D^2.
\tag{FB.23}
```

There are at most

```math
{N\choose r}\le {N^r\over r!}
\tag{FB.24}
```

possible blocker `r`-sets and, by (FB.17), at most

```math
(T_*^2+o(1))D^2
\tag{FB.25}
```

ordered complete-train pairs.

Pigeonhole therefore gives one fixed braid `F_*` and one fixed ordered train pair `(b_-,b_+)` occurring on more than

```math
\boxed{
\left(
{3q_0^2\over2T_*^2 5^r}-o(1)
\right)N
}
\tag{FB.26}
```

rows.

For every such row:

- every chord `e in F_*` crosses the row by exact selected-cut support;
- `b_-` crosses below `-0.01D`;
- `b_+` crosses above `+0.01D`;
- both train crossings are purified `pi/3+O(D^-1)` rhombi;
- the full row still has the original THIN richness and purified train density.

The two fixed trains cannot cross each other. If they did, together with any retained row they would form a triangle in the complete-train crossing graph, contradicting triangle-freeness.

Relative to the fixed track direction of `b_-`, every retained row has one of two projective phase signs. Retain the larger sign class. This gives `A_D^{br}(r)` with

```math
\boxed{
|A_D^{br}(r)|>
\left(
{3q_0^2\over4T_*^2 5^r}-o(1)
\right)N,
}
\tag{FB.27}
```

which is (FB.4).

All rows in `A_D^{br}(r)` now share one projective phase to `O(D^-1)` while the **same** two fixed trains occupy opposite circumcenter flanks.

---

## 4. Concrete `r=2` crossed-pair bracket

At `r=2`, `F_*={e_1,e_2}` consists of two vertex-disjoint THIN blockers. Hence

```math
\boxed{e_1\text{ and }e_2\text{ cross properly}.}
\tag{FB.28}
```

The coefficient in (FB.27) is

```math
{3q_0^2\over100T_*^2}
=9.58416796134773\ldots\times10^{-6}.
\tag{FB.29}
```

Using

```math
N>\left({\gamma\over16}-o(1)\right)D,
```

we obtain

```math
\boxed{
|A_D^{br}(2)|>
(4.93559691238675\times10^{-14}-o(1))D.
}
\tag{FB.30}
```

The coefficient is small because this extraction simultaneously fixes two inactive blockers, two complete trains, a left/right circumcenter orientation, and one row phase. It is nevertheless a genuine positive constant independent of the source.

Every row in this fixed-pair family is crossed by

```text
e_1, e_2, b_-, b_+,
```

with `e_1,e_2` properly crossing each other and `b_-,b_+` noncrossing each other.

---

## 5. Slow diagonal: a growing braid inside one fixed bracket

The growing-braid theorem chooses integers `r_D->infinity` sufficiently slowly that, with

```math
\Delta_D:=\max_{a\in R_D}\Delta(B_a)=O(D^{3/4}),
```

one has

```math
r_D\epsilon_D\to0,
\qquad
{r_D^2\Delta_D\over N}\to0,
\qquad
{r_D\over\log D}\to0,
\tag{FB.31}
```

where `epsilon_D->0` dominates the uniform asymptotic errors in the input estimates.

Then uniformly in `a in R_D`,

```math
M_{r_D}(a)
\ge
{1-o(1)\over r_D!}
\left({N\over5}\right)^{r_D}.
\tag{FB.32}
```

Repeat the count of Section 3 with `r=r_D`. There are one matching `F_D`, one ordered complete-train pair `(b_D^-,b_D^+)`, and after the phase split one row family `A_D^{br}` satisfying

```math
\boxed{|F_D|=r_D\to\infty}
\tag{FB.33}
```

and

```math
|A_D^{br}|>
\left({3q_0^2\over4T_*^2}-o(1)\right)
{N\over5^{r_D}}.
\tag{FB.34}
```

Since `N=Theta(D)` and `r_D=o(log D)`,

```math
5^{r_D}=D^{o(1)},
```

so

```math
\boxed{|A_D^{br}|=D^{1-o(1)}.}
\tag{FB.35}
```

Every pair of chords in `F_D` crosses properly. Both fixed trains cross every row in `A_D^{br}` and satisfy the same flank inequalities

```math
h_a(z_{a,b_D^-})<-0.01D,
\qquad
h_a(z_{a,b_D^+})>+0.01D.
\tag{FB.36}
```

The bracket trains are noncrossing.

---

## 6. The growing braid still has one common consecutive support block

Every row in `A_D^{br}` belongs to the exact selected-cut support interval of every chord in `F_D`. Let

```math
a_-:=\min A_D^{br},
\qquad
a_+:=\max A_D^{br}.
```

An interval containing both endpoints contains the whole block between them. Hence every chord in `F_D` supports

```math
\boxed{
\{a_-,a_-+1,\ldots,a_+\}.
}
\tag{FB.37}
```

Its length is at least `|A_D^{br}|`, so

```math
\boxed{
\text{all braid chords share a consecutive support block of length }D^{1-o(1)}.
}
\tag{FB.38}
```

No analogous interval claim is made for `b_D^-` or `b_D^+`: they are only asserted to cross the selected `D^(1-o(1))` rows of `A_D^{br}`.

---

## 7. Uniform central-threading versus angle separation for every braid chord

Fix `a in A_D^{br}`. Along the oriented row centerline, `b_D^-` and `b_D^+` bracket all points with

```math
|h_a(x)|\le0.01D.
\tag{FB.39}
```

Take any braid chord `e in F_D` and any intersection `x in e cap a`. The THIN midpoint localization gives

```math
|m(e)-o|=O(D^{3/4})=o(D).
\tag{FB.40}
```

Since `|e|<D`, writing `d_e` for its unit direction gives

```math
|h_a(x)|
\le |m(e)-o|+{D\over2}|\det(u_a,d_e)|.
\tag{FB.41}
```

If `x` lies outside the row subarc between the fixed bracket crossings, then

```math
|h_a(x)|>0.01D
```

and therefore

```math
\boxed{
|\det(u_a,d_e)|>0.02-o(1).
}
\tag{FB.42}
```

All retained rows have one common projective phase to `O(D^-1)`. Consequently each fixed braid chord falls into one of two classes:

1. **central-threading:** every intersection with every retained row lies between the same fixed trains `b_D^-`, `b_D^+`;
2. **angle-separated:** its projective direction has
   ```math
   \sin\theta(e,u_*)\ge0.02-o(1)
   
   ```
   from the common row phase.

Because `|F_D|=r_D->infinity`, one of these classes contains an unbounded sub-braid. In the angle-separated case, a further two-way projective-side split leaves an unbounded sub-braid on one common side of the row phase.

Thus the fixed bracket converts the former collective relative-position seam into the sharper fork

```text
unbounded pairwise-crossing braid centrally threads the same two trains
on D^(1-o(1)) rows,

or

unbounded pairwise-crossing braid stays a fixed angular distance from the
common row phase, with one common projective side after thinning.
```

No contradiction between these two normal forms is claimed here.

---

## 8. Frontier effect

The growing-braid theorem already removed the possibility that the common-spine phenomenon came from one exceptional THIN chord. The present result removes another freedom: the dense rowwise circumcenter flanks can no longer vary independently from row to row.

The surviving THIN object is now

```text
r_D -> infinity vertex-disjoint THIN hull chords;
every two braid chords cross properly;
one common consecutive braid-support block of D^(1-o(1)) selected rows;

one fixed complete train b_D^-;
one fixed complete train b_D^+;
b_D^- and b_D^+ do not cross;

D^(1-o(1)) retained common rows;
one inverse-D row phase;
b_D^- crossing below -0.01D on every retained row;
b_D^+ crossing above +0.01D on every retained row;
>0.6436D purified near-60 trains still available rowwise.
```

The next THIN target is therefore no longer to locate a train flank. It is to rule out one of two explicit geometries inside a **fixed macroscopic train bracket**: an unbounded centrally-threading crossing braid, or an unbounded fixed-angle crossing braid. Either contradiction would eliminate the THIN Horn upper branch.

**Disposition:** synchronized the growing pairwise-crossing THIN braid with one fixed noncrossing pair of complete trains that bracket `+-0.01D` on `D^(1-o(1))` common phase-pure rows; derived the resulting central-threading versus fixed-angle sub-braid fork. C-II and Level I remain open.
